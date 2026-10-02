#!/usr/bin/env python3
"""Turns the authored meteorology course into the data file the app reads.

Same engine as C-Lehrer: it reads <app>/data/kurs.json and knows nothing
about the subject. What differs here is that every readable string is a
{"de": ..., "en": ...} pair and that lessons carry pictures instead of code.

    tools/make-kurs.py        # -> data/kurs.json
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import formeln as formelsatz
import kartenherleitungen
import kurs


def mischen(optionen, antwort, saat):
    """Die Antwortmöglichkeiten durchmischen und den Index nachführen.

    Beim Schreiben steht die richtige Antwort bequem an erster Stelle. Bliebe
    sie dort, wäre der ganze Kurs mit einem Fingertipp lösbar, ohne eine
    einzige Frage gelesen zu haben -- und genau so ist es aufgefallen: "es
    wird immer die erste Antwort ausgewählt".

    Gemischt wird deterministisch aus der Fragenkennung, nicht zufällig: Die
    Reihenfolge muss über Neubauten hinweg gleich bleiben, sonst sitzt eine
    gemerkte Position beim nächsten Update woanders.

    Die Streuung ist FNV-1a mit Nachmischung. Ein einfaches "mal 131 plus
    Zeichen" genügt hier nicht: Die Saatwerte unterscheiden sich oft nur in
    der letzten Ziffer, und dann liefern aufeinanderfolgende Fragen
    systematisch verwandte Reihenfolgen -- im ersten Versuch landete die
    richtige Antwort dadurch in der Hälfte aller Fälle wieder vorne.
    """
    zustand = 2166136261
    for zeichen in saat:
        zustand = ((zustand ^ ord(zeichen)) * 16777619) & 0xffffffff
    zustand ^= zustand >> 15
    zustand = (zustand * 2246822519) & 0xffffffff
    zustand ^= zustand >> 13
    zustand = (zustand * 3266489917) & 0xffffffff
    zustand ^= zustand >> 16

    def naechste():
        nonlocal zustand
        zustand ^= (zustand << 13) & 0xffffffff
        zustand ^= zustand >> 17
        zustand ^= (zustand << 5) & 0xffffffff
        return zustand

    reihen = list(range(len(optionen)))
    for i in range(len(reihen) - 1, 0, -1):
        j = naechste() % (i + 1)
        reihen[i], reihen[j] = reihen[j], reihen[i]
    return [optionen[k] for k in reihen], reihen.index(antwort)



def aufgabe(task, saat):
    """Rename the authoring keys to the ones the engine reads."""
    out = {"kind": task["kind"], "q": task["q"], "warum": task["warum"],
           "bild": task.get("bild", "")}
    # Die Herleitung liegt daneben (kartenherleitungen.py) und wird ueber
    # den deutschen Fragetext zugeordnet, damit die Aufgaben selbst
    # unberuehrt bleiben. Sie steht in der Loesung; die Skizze dazu auch,
    # und ausdruecklich nicht in "bild" -- das steht ueber der Frage und
    # wuerde die Antwort verraten.
    frage = task["q"]
    schluessel = frage["de"] if isinstance(frage, dict) else frage
    herleitung = kartenherleitungen.HERLEITUNGEN.get(schluessel)
    if herleitung:
        out["herleitung"] = herleitung
        out["skizze"] = kartenherleitungen.SKIZZEN.get(schluessel, "")
    if task["kind"] == "mc":
        optionen, antwort = mischen(task["optionen"], task["antwort"], saat)
        out["options"] = optionen
        out["answer"] = antwort
        out["code"] = task.get("code", "")
    elif task["kind"] == "zahl":
        out["antwort"] = task["antwort"]
        out["einheit"] = task["einheit"]
        out["toleranz"] = task.get("toleranz", 0.1)
    return out


def pruefen(chapters, sprachen):
    """Faellt, bevor ein halbfertiger Kurs ausgeliefert wird.

    Zwei Dinge sind im Feld schon schiefgegangen und beide fallen im
    Alltag nicht auf: eine Lektion, die nur auf Deutsch uebersetzt ist
    (die App zeigt dann stillschweigend die andere Sprache), und eine
    Formel ohne Herleitung. Also hier, beim Erzeugen, und nicht spaeter.
    """
    fehler = []

    def zwei(wert, wo):
        if isinstance(wert, dict):
            for code in sprachen:
                if not wert.get(code, "").strip():
                    fehler.append("%s: %s fehlt" % (wo, code))
        elif isinstance(wert, str) and wert.strip():
            fehler.append("%s: nur einsprachig" % wo)

    for c in chapters:
        zwei(c.get("titel"), "Kapitel %s Titel" % c["id"])
        zwei(c.get("text"), "Kapitel %s Text" % c["id"])
        for l in c["lektionen"]:
            zwei(l.get("titel"), "%s Titel" % l["id"])
            zwei(l.get("text"), "%s Text" % l["id"])
            for i, a in enumerate(l.get("aufgaben", [])):
                zwei(a.get("q"), "%s Aufgabe %d Frage" % (l["id"], i))
                zwei(a.get("warum"), "%s Aufgabe %d Begruendung" % (l["id"], i))
                for j, o in enumerate(a.get("optionen", []) or []):
                    zwei(o, "%s Aufgabe %d Antwort %d" % (l["id"], i, j))
    return fehler


def herleitungen_pruefen():
    """Jeder Schluessel muss auf eine wirkliche Frage zeigen.

    Ein Tippfehler waere sonst unsichtbar: die Herleitung faende ihre Karte
    nicht, und die Karte bliebe ohne Herleitung -- genau der Zustand, den
    es hier abzustellen gilt.
    """
    alle = set()
    for kapitel in kurs.KAPITEL:
        for lektion in kapitel["lektionen"]:
            for t in lektion["aufgaben"]:
                frage = t["q"]
                alle.add(frage["de"] if isinstance(frage, dict) else frage)
    verwaist = sorted(set(kartenherleitungen.HERLEITUNGEN) - alle) \
             + sorted(set(kartenherleitungen.SKIZZEN) - alle)
    for q in verwaist:
        print("Herleitung zeigt ins Leere: " + q, file=sys.stderr)
    return not verwaist


def formeln_pruefen():
    """Keine Formel ohne Herleitung.

    Die Regel des Kurses ist, dass jede Formel hergeleitet wird. Der
    Erzeuger haengt die Herleitung nach Lektionskennung an; eine Lektion mit
    Formelkasten, aber ohne Eintrag in HERLEITUNGEN, waere genau die
    Luecke, die niemandem auffaellt, bis ein Physiker danach fragt.
    """
    import herleitungen
    offen = []
    for kapitel in kurs.KAPITEL:
        for lektion in kapitel["lektionen"]:
            if lektion.get("formeln") and lektion["id"] not in herleitungen.HERLEITUNGEN:
                offen.append(lektion["id"])
            for eintrag in lektion.get("formeln", []):
                if not eintrag.get("zeichen"):
                    offen.append("%s: Formel ohne Zeichenerklaerung (%s)"
                                 % (lektion["id"], eintrag["code"]))
    for o in offen:
        print("Formel ohne Herleitung: " + o, file=sys.stderr)
    return not offen


def rohes_tex(knoten, schluessel=None):
    """Alle Textstellen, in denen nach dem Ersetzen noch ein $ steht."""
    if isinstance(knoten, dict):
        return [r for k, v in knoten.items()
                if k not in ("tex", "code") for r in rohes_tex(v, k)]
    if isinstance(knoten, list):
        return [r for v in knoten for r in rohes_tex(v, schluessel)]
    if isinstance(knoten, str) and "$" in knoten:
        i = knoten.index("$")
        return [knoten[max(0, i - 30):i + 30].replace("\n", " ")]
    return []


def main():
    if not herleitungen_pruefen() or not formeln_pruefen():
        return 1
    chapters = []
    for chapter in kurs.KAPITEL:
        lessons = []
        for lesson in chapter["lektionen"]:
            lessons.append({
                "id": lesson["id"],
                "titel": lesson["titel"],
                "begriffe": lesson["begriffe"],
                "text": lesson["text"],
                "bild": lesson.get("bild", ""),
                "formeln": [dict(f) for f in lesson.get("formeln", [])],
                # No runnable example here -- the app hides the whole block
                # when it is empty, which is what a theory course wants.
                "beispiel": "",
                "ausgabe": "",
                "aufgaben": [aufgabe(t, lesson["id"] + "#" + str(i))
                             for i, t in enumerate(lesson["aufgaben"])],
            })
        chapters.append({
            "id": chapter["id"], "titel": chapter["titel"],
            "stufe": chapter["stufe"], "sprache": "-",
            "text": chapter["text"], "lektionen": lessons,
        })

    # Zu jeder Formel das Bild dazulegen, das tools/formeln.py gesetzt hat.
    # Fehlt eines, bleibt die Textzeile stehen und nur das Gesetzte fehlt --
    # matplotlib gibt es nur auf dem Baurechner, der Kurs soll sich ueberall
    # bauen lassen.
    bilder = formelsatz.gesetzte()
    ohne_bild = []
    for kap in chapters:
        for lek in kap["lektionen"]:
            for eintrag in lek.get("formeln", []):
                name = formelsatz.kennung(eintrag["tex"])
                daten = bilder.get(name)
                if not daten:
                    ohne_bild.append(eintrag["tex"])
                    continue
                eintrag["bild"] = name
                eintrag["breite"] = daten["breite"]
                eintrag["hoehe"] = daten["hoehe"]
    if ohne_bild:
        print("%d Formeln ohne Bild -- tools/formeln.py auf dem Baurechner "
              "laufen lassen:" % len(ohne_bild), file=sys.stderr)
        for tex in ohne_bild:
            print("   " + tex, file=sys.stderr)

    # Die Formeln im Fliesstext: $...$ wird zum Marker auf das gesetzte
    # Bild. Ist keines da (nicht auf dem Baurechner gesetzt), bleibt die
    # TeX-Zeile als Programmtext stehen -- lesbar, nur nicht schoen.
    ungesetzt = []

    def ersetzen(text):
        def absatz(m):
            return "\n\n" + marker("$" + m.group(1).strip() + "$",
                                   formelsatz.GROESSE_ABSATZ) + "\n\n"

        def zeile(m):
            return marker("$" + m.group(1).strip() + "$",
                          formelsatz.GROESSE_ZEILE)

        def marker(tex, groesse):
            name = formelsatz.kennung(tex, groesse)
            daten = bilder.get(name)
            if not daten:
                ungesetzt.append(tex)
                return "`" + tex.strip("$") + "`"
            return "[[formel:%s:%d:%d]]" % (name, daten["breite"], daten["hoehe"])

        text = formelsatz.MUSTER_ABSATZ.sub(absatz, text)
        text = formelsatz.MUSTER_ZEILE.sub(zeile, text)
        # Ein Absatzmarker steht allein in seiner Zeile; drei Umbrueche
        # hintereinander waeren ein leerer Absatz zu viel.
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")
        return text.strip("\n") if text.startswith("\n") else text

    def durchgehen(knoten):
        if isinstance(knoten, dict):
            return {k: (v if k in ("tex", "code", "bild", "skizze", "id")
                        else durchgehen(v)) for k, v in knoten.items()}
        if isinstance(knoten, list):
            return [durchgehen(v) for v in knoten]
        if isinstance(knoten, str) and "$" in knoten:
            return ersetzen(knoten)
        return knoten

    chapters = durchgehen(chapters)

    plan = [{"id": c["id"], "titel": c["titel"], "stufe": c["stufe"],
             "sprache": "-", "fertig": True} for c in chapters]
    for ident, titel, stufe in kurs.PLAN:
        plan.append({"id": ident, "titel": titel, "stufe": stufe,
                     "sprache": "-", "fertig": False})

    items = []
    for entry in kurs.EINSTUFUNG:
        e_optionen, e_antwort = mischen(entry["optionen"], entry["antwort"],
                                        entry["id"])
        items.append({
            "id": entry["id"], "stufe": entry["stufe"],
            "thema": entry["thema"], "frage": entry["q"],
            "code": "", "bild": entry.get("bild", ""),
            "optionen": e_optionen, "antwort": e_antwort,
            "warum": entry["warum"],
        })

    items = durchgehen(items)
    # Was jetzt noch ein Dollarzeichen traegt, hat kein Muster getroffen --
    # meist eine Formel mit Leerzeichen am Rand ($T = $). In der App waere
    # das ein Loch im Text, also ein Fehler und kein Hinweis.
    roh = rohes_tex(chapters) + rohes_tex(items)
    if roh:
        for r in roh[:10]:
            print("  rohes TeX: " + r, file=sys.stderr)
        print("%d Textstellen mit ungesetztem $ -- kein kurs.json geschrieben"
              % len(roh), file=sys.stderr)
        return 1
    if ungesetzt:
        print("%d Textformeln ohne Bild -- tools/formeln.py auf dem Baurechner "
              "laufen lassen:" % len(set(ungesetzt)), file=sys.stderr)
        for tex in sorted(set(ungesetzt))[:20]:
            print("   " + tex, file=sys.stderr)

    fehler = pruefen(chapters, ["de", "en"])
    if fehler:
        for f in fehler[:25]:
            print("  FEHLER " + f, file=sys.stderr)
        print("%d Maengel -- kein kurs.json geschrieben" % len(fehler),
              file=sys.stderr)
        return 1
    print("Zweisprachigkeit: vollstaendig")

    out = {
        "titel": {"de": "Meteorologie", "en": "Meteorology"},
        "untertitel": {
            "de": ("Meteorologie für Physiker: die Atmosphäre aus "
                   "Thermodynamik, Strahlung und Mechanik hergeleitet."),
            "en": ("Meteorology for physicists: the atmosphere derived from "
                   "thermodynamics, radiation and mechanics."),
        },
        "ausfuehrbar": False,
        "sprachen": ["de", "en"],
        "kapitel": chapters,
        "plan": plan,
        "einstufung": {"themen": kurs.THEMEN, "fragen": items},
    }
    path = os.path.join(ROOT, "data", "kurs.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print("data/kurs.json: %d Kapitel, %d Lektionen, %d Aufgaben, "
          "%d Einstufungsfragen, %d B"
          % (len(chapters), sum(len(c["lektionen"]) for c in chapters),
             sum(len(l["aufgaben"]) for c in chapters for l in c["lektionen"]),
             len(items), os.path.getsize(path)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
