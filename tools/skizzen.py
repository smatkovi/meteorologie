#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Zeichnet die Skizzen zu den Lektionen und Herleitungen.

Eine Herleitung ist eine Kette von Sätzen, und an genau einer Stelle hängt
sie an einem Bild: der Luftsäule, dem Kräftegleichgewicht, dem Strahlengang
im Tropfen. Wer das Bild vor sich hat, liest die Rechnung als Beschreibung
dessen, was er sieht.

Gezeichnet wird schematisch, nicht abbildend. Alles bei 3x und am Ende
verkleinert, sonst treppen die Schrägen. Die Beschriftung steckt im Bild,
also gibt es jede Skizze zweimal: <name>.png und <name>.en.png.

    tools/skizzen.py            # -> bilder/skizze-*.png
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "bilder")

W, H = 440, 300
S = 3

GRUND = (14, 14, 18)
LINIE = (120, 130, 150)
DUENN = (70, 78, 94)
TEXT = (226, 230, 240)
BETONT = (90, 169, 255)
WARN = (255, 177, 78)
GUT = (126, 231, 135)
ROT = (226, 74, 74)
KOERPER = (232, 236, 244)
WOLKE = (200, 206, 218)
GELB = (255, 214, 92)

SPRACHE = "de"
GESEHEN = set()

EN = {
    "Höhe": "height", "Temperatur": "temperature", "Boden": "ground",
    "Troposphäre": "troposphere", "Tropopause": "tropopause",
    "Stratosphäre": "stratosphere", "Stratopause": "stratopause",
    "Mesosphäre": "mesosphere", "Mesopause": "mesopause",
    "Thermosphäre": "thermosphere", "Ozon heizt": "ozone heats",
    "Wetter": "weather", "von unten geheizt": "heated from below",
    "Druck": "pressure", "Luftsäule": "column of air",
    "Gewicht der Scheibe": "weight of the slab",
    "Druck von unten": "pressure from below", "Druck von oben": "pressure from above",
    "je Skalenhöhe auf 1/e": "to 1/e per scale height",
    "Standardatmosphäre": "standard atmosphere",
    "Luftpaket": "air parcel", "dehnt sich aus": "expands", "kühlt ab": "cools",
    "steigt": "rises", "Umgebung": "environment", "Adiabate": "adiabat",
    "stabil": "stable", "neutral": "neutral", "labil": "unstable",
    "Inversion": "inversion", "gehoben": "lifted", "sinkt zurück": "sinks back",
    "steigt weiter": "keeps rising", "Paket": "parcel",
    "Sättigungsdampfdruck": "saturation vapour pressure",
    "Verdopplung je 10 K": "doubling every 10 K", "Taupunkt": "dew point",
    "Spreizung": "spread", "Wolkenbasis": "cloud base", "feucht": "moist",
    "trocken": "dry", "Wolke": "cloud", "Aufstieg": "sounding",
    "Sonne": "sun", "reflektiert": "reflected", "absorbiert": "absorbed",
    "Infrarot ins All": "infrared to space", "Erde": "Earth",
    "Schicht": "layer", "Gegenstrahlung": "back radiation", "All": "space",
    "Nacht": "night", "Tag": "day", "Minimum vor Sonnenaufgang": "minimum before sunrise",
    "Maximum 15 Uhr": "maximum 15:00", "Tau, Nebel": "dew, fog",
    "Nettostrahlung": "net radiation", "Uhr": "h",
    "Kelvin (reines Wasser)": "Kelvin (pure water)", "Köhler (Salzkern)": "Köhler (salt nucleus)",
    "kritisch": "critical", "Dunst": "haze", "aktiviert": "activated",
    "Radius": "radius", "Übersättigung": "supersaturation",
    "Diffusion": "diffusion", "Koaleszenz": "coalescence", "Zeit": "time",
    "Regen": "rain", "Wolkentropfen": "cloud drop",
    "ruht im rotierenden System": "at rest in the rotating frame",
    "von außen gesehen": "seen from outside", "Kreisbahn der Spitze": "circle of the tip",
    "Erdachse": "Earth's axis", "Äquator": "equator", "Pol": "pole",
    "Nord": "north", "oben": "up", "Breite": "latitude",
    "Tief": "low", "Hoch": "high", "Druckgradientkraft": "pressure gradient force",
    "Coriolis": "Coriolis", "Wind": "wind", "Isobaren": "isobars",
    "warm": "warm", "kalt": "cold", "Druckflächen": "pressure surfaces",
    "Wind in die Bildebene": "wind into the page", "Jet": "jet",
    "geostrophischer Wind": "geostrophic wind", "am Boden": "at the ground",
    "Ekman-Spirale": "Ekman spiral", "zum Tief": "toward the low",
    "Hadley": "Hadley", "Ferrel": "Ferrel", "Polar": "polar",
    "ITCZ": "ITCZ", "Passat": "trade wind", "Westwind": "westerlies",
    "Subtropenhoch": "subtropical high", "Polarfront": "polar front",
    "Wüste": "desert", "Breitengrad": "latitude",
    "Rossby-Welle": "Rossby wave", "Phase nach Westen": "phase westward",
    "antizyklonal": "anticyclonic", "zyklonal": "cyclonic", "Grundstrom": "mean flow",
    "Warmfront": "warm front", "Kaltfront": "cold front", "Warmsektor": "warm sector",
    "Cirrus": "cirrus", "Altostratus": "altostratus", "Nimbostratus": "nimbostratus",
    "Cumulonimbus": "cumulonimbus", "Okklusion": "occlusion",
    "Luv": "windward", "Lee": "lee", "Kamm": "crest", "Stau": "orographic rain",
    "Föhn": "foehn", "See": "sea", "Land": "land", "Seewind": "sea breeze",
    "Rückstrom oben": "return flow aloft", "Molekül": "molecule",
    "blau stark": "blue strong", "rot schwach": "red weak", "Tröpfchen": "droplet",
    "alle Farben gleich": "all colours alike", "weiß": "white",
    "Sonnenlicht": "sunlight", "Tropfen": "drop", "Beobachter": "observer",
    "Eisprisma": "ice prism", "Gitterzelle": "grid cell", "Cumulus": "cumulus",
    "parametrisiert": "parametrised", "Tage": "days", "Mitglieder": "members",
    "Streuung": "spread", "Vorhersage": "forecast", "Mittel": "mean",
    "Höhenmesser": "altimeter", "Rayleigh": "Rayleigh", "Mie": "Mie",
    "Sättigung": "saturation", "Niveau freier Konvektion": "level of free convection",
    "Gleichgewichtsniveau": "equilibrium level",
    "Trockenadiabate": "dry adiabat", "Feuchtadiabate": "moist adiabat",
    "Hebung": "lifting", "Luft": "air", "Kaltluft": "cold air", "Warmluft": "warm air",
    "Kondensation": "condensation", "Absinken": "subsidence",
}


def schrift(groesse):
    for pfad in ("/usr/share/fonts/dejavu/DejaVuSans.ttf",
                 "/usr/share/fonts/TTF/DejaVuSans.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if os.path.exists(pfad):
            return ImageFont.truetype(pfad, groesse)
    return ImageFont.load_default()


def leinwand():
    bild = Image.new("RGB", (W * S, H * S), GRUND)
    return bild, ImageDraw.Draw(bild)


def sichern(bild, name):
    os.makedirs(OUT, exist_ok=True)
    if SPRACHE != "de":
        name = name + "." + SPRACHE
    bild.resize((W, H), Image.LANCZOS).save(os.path.join(OUT, name + ".png"))
    print("  %s" % name)


def uebersetzen(inhalt):
    """Ein Beschriftungstext, Wort fuer Wort durch die Tafel.

    Zusammengesetzte Beschriftungen ("Höhe (km)") werden an Klammern,
    Kommas und Zahlen vorbei uebersetzt, damit die Tafel nur Woerter kennt.
    """
    if SPRACHE == "de":
        GESEHEN.add(inhalt)
        return inhalt
    if inhalt in EN:
        return EN[inhalt]
    if inhalt.strip() in EN:
        return inhalt.replace(inhalt.strip(), EN[inhalt.strip()])
    import re
    teile = re.split(r"(\(|\)|,|:|\d[\d.,]*\s*[a-zA-Z°%/²³]*|\s[-–]\s)", inhalt)
    raus = []
    for t in teile:
        k = t.strip()
        if k in EN:
            raus.append(t.replace(k, EN[k]))
        else:
            raus.append(t)
    return "".join(raus)


def pruefen():
    """Jede deutsche Beschriftung braucht ihren englischen Eintrag."""
    import re
    fehlt = []
    for s in sorted(GESEHEN):
        if s in EN:
            continue
        teile = re.split(r"(\(|\)|,|:|\d[\d.,]*\s*[a-zA-Z°%/²³]*|\s[-–]\s)", s)
        for t in teile:
            k = t.strip()
            if k and not re.match(r"^[\d\s.,°%/²³a-zA-Z_+=×·−-]*$", k) and k not in EN:
                fehlt.append(s)
                break
    return fehlt


def text(draw, x, y, inhalt, groesse=13, farbe=TEXT, mitte=False, rechts=False):
    inhalt = uebersetzen(inhalt)
    f = schrift(groesse * S)
    kasten = draw.textbbox((0, 0), inhalt, font=f)
    breite = (kasten[2] - kasten[0]) / float(S)
    if mitte:
        x -= breite / 2.0
    elif rechts:
        x -= breite
    draw.text((x * S, y * S), inhalt, font=f, fill=farbe)


def strich(draw, x1, y1, x2, y2, farbe=LINIE, dicke=2):
    draw.line([(x1 * S, y1 * S), (x2 * S, y2 * S)], fill=farbe, width=dicke * S)


def linie(draw, punkte, farbe=LINIE, dicke=2):
    draw.line([(x * S, y * S) for x, y in punkte], fill=farbe, width=dicke * S,
              joint="curve")


def gestrichelt(draw, x1, y1, x2, y2, farbe=DUENN, dicke=1, laenge=6):
    weite = math.hypot(x2 - x1, y2 - y1)
    if weite <= 0:
        return
    schritte = max(1, int(weite / laenge))
    for i in range(schritte):
        if i % 2:
            continue
        a, b = i / float(schritte), min(1.0, (i + 1) / float(schritte))
        strich(draw, x1 + (x2 - x1) * a, y1 + (y2 - y1) * a,
               x1 + (x2 - x1) * b, y1 + (y2 - y1) * b, farbe, dicke)


def pfeil(draw, x1, y1, x2, y2, farbe=BETONT, dicke=2, spitze=7):
    strich(draw, x1, y1, x2, y2, farbe, dicke)
    winkel = math.atan2(y2 - y1, x2 - x1)
    for seite in (+1, -1):
        a = winkel + seite * 2.6
        strich(draw, x2, y2, x2 + spitze * math.cos(a), y2 + spitze * math.sin(a),
               farbe, dicke)


def bogen(draw, cx, cy, r, von, bis, farbe=DUENN, dicke=1):
    draw.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
             von, bis, fill=farbe, width=dicke * S)


def kreis(draw, cx, cy, r, farbe=KOERPER, rand=None, dicke=1):
    draw.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S],
                 fill=farbe, outline=rand, width=dicke * S if rand else 0)


def flaeche(draw, punkte, farbe):
    draw.polygon([(x * S, y * S) for x, y in punkte], fill=farbe)


def wolke(draw, cx, cy, breite, hoehe, farbe=WOLKE):
    """Ein paar Ballen auf einer flachen Basis."""
    n = max(3, int(breite / 14))
    for i in range(n):
        x = cx - breite / 2 + breite * (i + 0.5) / n
        r = hoehe * (0.55 + 0.35 * math.sin(i * 2.1 + 0.4))
        kreis(draw, x, cy - r * 0.6, r, farbe)
    draw.rectangle([(cx - breite / 2) * S, (cy - hoehe * 0.3) * S,
                    (cx + breite / 2) * S, cy * S], fill=farbe)


def achsen(draw, x0, y0, x1, y1, xname, yname):
    """Ein Koordinatenkreuz mit Pfeilen: Ecke (x0, y0), x nach rechts bis x1,
    y nach oben bis y1."""
    pfeil(draw, x0, y0, x1, y0, DUENN, 1, 5)
    pfeil(draw, x0, y0, x0, y1, DUENN, 1, 5)
    text(draw, x1, y0 + 6, xname, 10, DUENN, rechts=True)
    text(draw, x0 + 6, y1 - 2, yname, 10, DUENN)


# ===========================================================================
# 1  Atmosphäre
# ===========================================================================

def schichtung():
    bild, draw = leinwand()
    x0, y0 = 70, 262
    achsen(draw, x0, y0, 400, 30, "Temperatur", "Höhe")
    # Hoehe nichtlinear: 0-12 km auf 90 px, 12-50 auf 70, 50-85 auf 50, 85-100 auf 30
    def hy(z):
        if z <= 12: return y0 - z / 12.0 * 90
        if z <= 50: return y0 - 90 - (z - 12) / 38.0 * 70
        if z <= 85: return y0 - 160 - (z - 50) / 35.0 * 50
        return y0 - 210 - (z - 85) / 15.0 * 30
    def tx(T):
        return x0 + 30 + (T + 100) / 130.0 * 300
    profil = [(15, 0), (-56, 12), (-56, 20), (-2, 50), (-90, 85), (-90, 90), (20, 100)]
    linie(draw, [(tx(T), hy(z)) for T, z in profil], WARN, 2)
    for z, name in ((12, "Tropopause"), (50, "Stratopause"), (85, "Mesopause")):
        gestrichelt(draw, x0, hy(z), 400, hy(z), DUENN)
        text(draw, 398, hy(z) - 12, name, 9, DUENN, rechts=True)
        text(draw, x0 - 6, hy(z) - 6, "%d km" % z, 9, DUENN, rechts=True)
    text(draw, x0 - 6, y0 - 6, "0 km", 9, DUENN, rechts=True)
    text(draw, 84, hy(6) - 6, "Troposphäre", 11, TEXT)
    text(draw, 84, hy(6) + 8, "von unten geheizt", 9, DUENN)
    text(draw, 84, hy(30) - 6, "Stratosphäre", 11, TEXT)
    text(draw, 84, hy(30) + 8, "Ozon heizt", 9, DUENN)
    text(draw, 84, hy(66) - 6, "Mesosphäre", 11, TEXT)
    text(draw, 84, hy(94) - 4, "Thermosphäre", 11, TEXT)
    for T in (-80, -40, 0):
        text(draw, tx(T), y0 + 8, "%d °C" % T, 9, DUENN, mitte=True)
    sichern(bild, "skizze-schichtung")


def luftsaeule():
    bild, draw = leinwand()
    # Links: die Saeule mit einer Scheibe
    x, b = 60, 90
    draw.rectangle([x * S, 40 * S, (x + b) * S, 262 * S], outline=DUENN, width=S)
    y1, y2 = 140, 170
    draw.rectangle([(x + 1) * S, y1 * S, (x + b - 1) * S, y2 * S], fill=(40, 48, 70))
    pfeil(draw, x + b / 2, y2 + 40, x + b / 2, y2 + 4, GUT, 2)
    text(draw, x + b / 2 + 8, y2 + 12, "p(z)·A", 11, GUT)
    pfeil(draw, x + b / 2, y1 - 40, x + b / 2, y1 - 4, BETONT, 2)
    text(draw, x + b / 2 + 8, y1 - 36, "p(z+dz)·A", 11, BETONT)
    pfeil(draw, x + b / 2 - 28, y1 + 4, x + b / 2 - 28, y2 + 30, ROT, 2)
    text(draw, x + b / 2 - 34, y2 + 30, "ρ·g·A·dz", 11, ROT, rechts=True)
    text(draw, x + b + 6, (y1 + y2) / 2 - 7, "dz", 11, TEXT)
    text(draw, x + b / 2, 24, "Luftsäule", 11, TEXT, mitte=True)
    text(draw, x + b / 2, 268, "Boden", 10, DUENN, mitte=True)
    # Rechts: p(z) exponentiell
    ax, ay = 230, 262
    achsen(draw, ax, ay, 420, 40, "Druck", "Höhe")
    pts = [(ax + 170 * math.exp(-z / 7.3), ay - z / 25.0 * 200) for z in range(0, 26)]
    linie(draw, pts, WARN, 2)
    gestrichelt(draw, ax, ay - 7.3 / 25.0 * 200, ax + 170 / math.e, ay - 7.3 / 25.0 * 200, DUENN)
    text(draw, ax + 4, ay - 7.3 / 25.0 * 200 - 12, "H = R·T/g ≈ 7,5 km", 10, GUT)
    text(draw, ax + 90, ay - 7.3 / 25.0 * 200 + 4, "je Skalenhöhe auf 1/e", 9, DUENN)
    text(draw, ax + 170, ay + 8, "p₀", 10, DUENN, mitte=True)
    sichern(bild, "skizze-luftsaeule")


def standard():
    bild, draw = leinwand()
    ax, ay = 80, 262
    achsen(draw, ax, ay, 420, 30, "Druck (hPa)", "Höhe (km)")
    g, R, G, T0 = 9.81, 287.05, 0.0065, 288.15
    def p(z):
        if z <= 11000: return 1013.25 * (1 - G * z / T0) ** (g / (R * G))
        return 226.32 * math.exp(-g * (z - 11000) / (R * 216.65))
    def px(pp): return ax + pp / 1013.25 * 320
    def zy(z): return ay - z / 20000.0 * 215
    linie(draw, [(px(p(z)), zy(z)) for z in range(0, 20001, 500)], WARN, 2)
    for pp, z in ((850, 1457), (700, 3012), (500, 5574), (300, 9164), (200, 11784)):
        gestrichelt(draw, ax, zy(z), px(pp), zy(z), DUENN)
        gestrichelt(draw, px(pp), zy(z), px(pp), ay, DUENN)
        text(draw, px(pp), ay + 6, "%d" % pp, 9, DUENN, mitte=True)
        text(draw, ax - 4, zy(z) - 6, "%d m" % z, 9, DUENN, rechts=True)
    text(draw, px(1013.25), ay + 6, "1013", 9, DUENN, mitte=True)
    gestrichelt(draw, ax, zy(11000), 420, zy(11000), BETONT)
    text(draw, 418, zy(11000) - 12, "Tropopause −56,5 °C", 9, BETONT, rechts=True)
    text(draw, 250, 60, "T = 15 °C − 6,5 K/km · z", 11, TEXT)
    text(draw, 250, 76, "Standardatmosphäre", 10, DUENN)
    sichern(bild, "skizze-standard")


# ===========================================================================
# 2  Thermodynamik
# ===========================================================================

def paket():
    bild, draw = leinwand()
    gestrichelt(draw, 40, 262, 400, 262, DUENN)
    text(draw, 400, 266, "Boden", 10, DUENN, rechts=True)
    for i, (z, T, r) in enumerate(((0, 20, 16), (1000, 10, 21), (2000, 0, 27))):
        y = 240 - i * 90
        kreis(draw, 160, y, r, (40, 60, 100), BETONT, 1)
        text(draw, 160 + r + 10, y - 16, "%d m" % z, 10, DUENN)
        text(draw, 160 + r + 10, y - 2, "%d °C" % T, 12, WARN)
        text(draw, 160 + r + 10, y + 12, "p = %d hPa" % (1013, 899, 795)[i], 9, DUENN)
        if i < 2:
            pfeil(draw, 160, y - r - 6, 160, y - 90 + 27 + 6, GUT, 2)
    text(draw, 100, 40, "Luftpaket", 12, TEXT)
    text(draw, 100, 56, "steigt, dehnt sich aus, kühlt ab", 10, DUENN)
    text(draw, 300, 150, "−9,8 K je km", 13, GUT)
    text(draw, 300, 168, "Γ = g / c_p", 12, TEXT)
    text(draw, 300, 190, "keine Wärme tauscht,", 9, DUENN)
    text(draw, 300, 202, "Arbeit gegen den Außendruck", 9, DUENN)
    sichern(bild, "skizze-paket")


def theta():
    bild, draw = leinwand()
    ax, ay = 80, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 60) / 100.0 * 320
    def zy(z): return ay - z / 10.0 * 215
    linie(draw, [(tx(15 - 6.5 * z), zy(z)) for z in (0, 10)], WARN, 2)
    linie(draw, [(tx(15 - 9.8 * z), zy(z)) for z in (0, 7.5)], BETONT, 2)
    linie(draw, [(tx(15 + 3.3 * z), zy(z)) for z in (0, 10)], GUT, 2)
    text(draw, tx(15 - 6.5 * 9) - 4, zy(9) - 4, "Umgebung 6,5 K/km", 10, WARN, rechts=True)
    text(draw, tx(15 - 9.8 * 5) - 4, zy(5) + 4, "Adiabate 9,8 K/km", 10, BETONT, rechts=True)
    text(draw, tx(15 + 3.3 * 7) + 6, zy(7), "θ: + 3,3 K/km", 10, GUT)
    kreis(draw, tx(15), zy(0), 4, KOERPER)
    text(draw, tx(15) + 6, zy(0) - 16, "15 °C, 1000 hPa", 9, DUENN)
    gestrichelt(draw, ax, zy(5), tx(15 + 3.3 * 5), zy(5), DUENN)
    text(draw, ax - 4, zy(5) - 6, "500 hPa", 9, DUENN, rechts=True)
    text(draw, tx(15 - 6.5 * 5) - 2, zy(5) + 6, "−18 °C", 9, WARN, rechts=True)
    text(draw, tx(15 + 3.3 * 5) + 4, zy(5) + 6, "θ = 309 K", 9, GUT)
    sichern(bild, "skizze-theta")


def stabilitaet():
    bild, draw = leinwand()
    ax, ay = 60, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 30) / 60.0 * 330
    def zy(z): return ay - z / 3.0 * 215
    z0, T0 = 1.0, 10.0
    kreis(draw, tx(T0), zy(z0), 4, KOERPER)
    # Adiabate durch den Punkt
    linie(draw, [(tx(T0 + 9.8 * (z0 - z)), zy(z)) for z in (0, 3)], BETONT, 2)
    text(draw, tx(T0 - 9.8 * 1.9) - 4, zy(2.9), "Adiabate", 10, BETONT, rechts=True)
    for G, name, farbe in ((6.5, "stabil", GUT), (9.8, "neutral", DUENN), (13, "labil", ROT), (-5, "Inversion", WARN)):
        pts = [(tx(T0 + G * (z0 - z)), zy(z)) for z in (0.4, 2.6)]
        if G == 9.8:
            gestrichelt(draw, pts[0][0], pts[0][1], pts[1][0], pts[1][1], DUENN, 1)
        else:
            linie(draw, pts, farbe, 1)
        ex, ey = pts[1]
        text(draw, ex + (4 if G < 9.8 else -4), ey - 4, name, 10, farbe, rechts=G >= 9.8)
    # gehobenes Paket auf der Adiabate
    zh = 2.2
    kreis(draw, tx(T0 - 9.8 * (zh - z0)), zy(zh), 4, BETONT)
    text(draw, tx(T0 - 9.8 * (zh - z0)) - 8, zy(zh) - 16, "Paket, gehoben", 9, BETONT, rechts=True)
    text(draw, 240, 240, "kälter als die Umgebung: sinkt zurück", 9, GUT)
    text(draw, 240, 254, "wärmer als die Umgebung: steigt weiter", 9, ROT)
    sichern(bild, "skizze-stabilitaet")


# ===========================================================================
# 3  Feuchte
# ===========================================================================

def e_s(T):
    return 6.112 * math.exp(17.62 * T / (243.12 + T))


def dampfdruck():
    bild, draw = leinwand()
    ax, ay = 70, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur (°C)", "e_s (hPa)")
    def tx(T): return ax + (T + 20) / 60.0 * 330
    def ey(e): return ay - e / 80.0 * 215
    linie(draw, [(tx(T), ey(e_s(T))) for T in range(-20, 41)], WARN, 2)
    for T in (0, 10, 20, 30):
        gestrichelt(draw, tx(T), ay, tx(T), ey(e_s(T)), DUENN)
        gestrichelt(draw, ax, ey(e_s(T)), tx(T), ey(e_s(T)), DUENN)
        text(draw, tx(T), ay + 6, "%d" % T, 9, DUENN, mitte=True)
        text(draw, ax - 4, ey(e_s(T)) - 6, "%.1f" % e_s(T), 9, DUENN, rechts=True)
    text(draw, tx(-20), ay + 6, "−20", 9, DUENN, mitte=True)
    text(draw, 110, 50, "Sättigungsdampfdruck", 11, TEXT)
    text(draw, 110, 66, "Verdopplung je 10 K", 10, GUT)
    # Taupunkt-Beispiel: T = 25, Td = 15
    kreis(draw, tx(25), ey(e_s(25)), 4, WARN)
    kreis(draw, tx(15), ey(e_s(15)), 4, BETONT)
    gestrichelt(draw, tx(25), ey(e_s(15)), tx(25), ey(e_s(25)), BETONT)
    kreis(draw, tx(25), ey(e_s(15)), 4, BETONT, rand=None)
    text(draw, tx(25) + 8, ey(e_s(25)) - 6, "T = 25 °C", 9, WARN)
    text(draw, tx(25) + 8, ey(e_s(15)) - 6, "e = e_s(T_d), 54 %", 9, BETONT)
    text(draw, tx(15) - 6, ey(e_s(15)) - 14, "Taupunkt 15 °C", 9, BETONT, rechts=True)
    sichern(bild, "skizze-dampfdruck")


def hebung():
    bild, draw = leinwand()
    ax, ay = 90, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 30) / 60.0 * 310
    def zy(z): return ay - z / 4.0 * 215
    T0, Td0 = 24.0, 12.0
    zl = (T0 - Td0) / 8.0
    Tl = T0 - 9.8 * zl
    linie(draw, [(tx(T0), zy(0)), (tx(Tl), zy(zl))], WARN, 2)
    linie(draw, [(tx(Td0), zy(0)), (tx(Tl), zy(zl))], BETONT, 2)
    linie(draw, [(tx(Tl), zy(zl)), (tx(Tl - 6 * (4 - zl)), zy(4))], GUT, 2)
    gestrichelt(draw, ax, zy(zl), 420, zy(zl), DUENN)
    for i in range(4):
        wolke(draw, tx(Tl) + 40 + i * 44, zy(zl) - 2, 36, 18)
    text(draw, tx(T0) + 4, zy(0) - 16, "T = 24 °C", 10, WARN)
    text(draw, tx(Td0) - 4, zy(0) - 16, "T_d = 12 °C", 10, BETONT, rechts=True)
    text(draw, (tx(T0) + tx(Tl)) / 2 + 8, (zy(0) + zy(zl)) / 2, "−9,8 K/km", 9, WARN)
    text(draw, (tx(Td0) + tx(Tl)) / 2 - 8, (zy(0) + zy(zl)) / 2, "−1,8 K/km", 9, BETONT, rechts=True)
    text(draw, ax - 4, zy(zl) - 6, "LCL %d m" % int(zl * 1000), 9, GUT, rechts=True)
    text(draw, ax - 4, zy(zl) + 6, "Wolkenbasis", 9, DUENN, rechts=True)
    text(draw, tx(Tl - 6 * 2) - 6, zy(3), "Feuchtadiabate −6 K/km", 9, GUT, rechts=True)
    text(draw, 250, 230, "Spreizung schließt sich mit 8 K/km", 9, TEXT)
    text(draw, 250, 244, "z = 125 m/K × (T − T_d)", 11, GUT)
    sichern(bild, "skizze-hebung")


def emagramm():
    bild, draw = leinwand()
    ax, ay = 70, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "ln p  (Höhe)")
    def tx(T): return ax + (T + 60) / 100.0 * 330
    def zy(z): return ay - z / 12.0 * 215
    # Umgebung: 25 °C am Boden, Inversion in 1-1,5 km, dann 7 K/km, Tropopause 11 km
    def Tu(z):
        if z < 1.0: return 25 - 9.0 * z
        if z < 1.6: return 16 + 2.0 * (z - 1.0)
        if z < 11: return 17.2 - 7.0 * (z - 1.6)
        return 17.2 - 7.0 * 9.4
    umg = [(tx(Tu(z / 10.0)), zy(z / 10.0)) for z in range(0, 121)]
    linie(draw, umg, WARN, 2)
    # Taupunkt: 18 am Boden, fallend
    linie(draw, [(tx(18 - 2.5 * z), zy(z)) for z in (0, 12)], BETONT, 1)
    # Paket: trocken bis LCL (7 K Spreizung -> 0,88 km), dann feucht 5 K/km
    zl = 7 / 8.0
    Tl = 25 - 9.8 * zl
    def Tp(z):
        if z < zl: return 25 - 9.8 * z
        return Tl - 5.0 * (z - zl)
    pak = [(tx(Tp(z / 10.0)), zy(z / 10.0)) for z in range(0, 121)]
    # CIN (rot) und CAPE (gruen) als Flaechen zwischen Paket und Umgebung
    def band(z_von, z_bis, farbe):
        pts = [(tx(Tp(z / 10.0)), zy(z / 10.0)) for z in range(int(z_von * 10), int(z_bis * 10) + 1)]
        pts += [(tx(Tu(z / 10.0)), zy(z / 10.0)) for z in range(int(z_bis * 10), int(z_von * 10) - 1, -1)]
        flaeche(draw, pts, farbe)
    # Schnittpunkte grob: Paket kaelter 0,9-2,2 km (CIN), waermer 2,2-11 km (CAPE)
    lfc = 2.25
    band(zl, lfc, (90, 30, 30))
    band(lfc, 11.0, (30, 70, 40))
    linie(draw, pak, GUT, 2)
    linie(draw, umg, WARN, 2)
    gestrichelt(draw, ax, zy(zl), 420, zy(zl), DUENN)
    gestrichelt(draw, ax, zy(lfc), 420, zy(lfc), DUENN)
    gestrichelt(draw, ax, zy(11), 420, zy(11), DUENN)
    text(draw, ax - 4, zy(zl) - 6, "LCL", 9, DUENN, rechts=True)
    text(draw, ax - 4, zy(lfc) - 6, "LFC", 9, DUENN, rechts=True)
    text(draw, ax - 4, zy(11) - 6, "EL", 9, DUENN, rechts=True)
    text(draw, tx(Tu(6)) + 8, zy(6), "Aufstieg", 10, WARN)
    text(draw, tx(Tp(7)) - 8, zy(7) - 10, "Paket", 10, GUT, rechts=True)
    text(draw, tx(18 - 2.5 * 4) - 6, zy(4) + 2, "Taupunkt", 9, BETONT, rechts=True)
    text(draw, tx(Tp(1.6)) - 30, zy(1.5) + 4, "CIN", 10, ROT, rechts=True)
    text(draw, tx(Tp(6)) - 30, zy(5), "CAPE", 12, GUT, rechts=True)
    sichern(bild, "skizze-emagramm")


# ===========================================================================
# 4  Strahlung
# ===========================================================================

def bilanz():
    bild, draw = leinwand()
    cx, cy, r = 300, 165, 70
    kreis(draw, cx, cy, r, (40, 70, 110), BETONT, 1)
    text(draw, cx, cy - 6, "Erde", 12, TEXT, mitte=True)
    # Sonnenstrahlen von links
    for i, dy in enumerate((-50, -25, 0, 25, 50)):
        pfeil(draw, 40, cy + dy, cx - r - 6, cy + dy, GELB, 2)
    text(draw, 40, cy - 80, "Sonne: S₀ = 1361 W/m²", 11, GELB)
    text(draw, 40, cy - 66, "auf die Scheibe π·R²", 9, DUENN)
    # reflektiert
    pfeil(draw, cx - r + 10, cy - 30, 120, 60, GELB, 1)
    text(draw, 118, 44, "reflektiert: A = 0,3", 9, GELB)
    # Infrarot in alle Richtungen
    for a in range(0, 360, 45):
        rad = math.radians(a)
        pfeil(draw, cx + (r + 4) * math.cos(rad), cy + (r + 4) * math.sin(rad),
              cx + (r + 34) * math.cos(rad), cy + (r + 34) * math.sin(rad), ROT, 1, 5)
    text(draw, cx + r + 40, cy + 52, "Infrarot ins All", 10, ROT)
    text(draw, cx + r + 40, cy + 66, "über 4π·R²", 9, DUENN)
    text(draw, 40, 250, "absorbiert: S₀(1−A)/4 = 238 W/m²  =  σ·T⁴  →  T = 255 K", 11, GUT)
    text(draw, 40, 270, "Erde: 255 K von außen, 288 K am Boden", 10, TEXT)
    sichern(bild, "skizze-bilanz")


def einschicht():
    bild, draw = leinwand()
    yb, ys = 240, 120
    draw.rectangle([40 * S, yb * S, 400 * S, (yb + 14) * S], fill=(70, 60, 50))
    text(draw, 42, yb + 16, "Boden  T_s", 10, TEXT)
    draw.rectangle([40 * S, ys * S, 400 * S, (ys + 6) * S], fill=(50, 70, 110))
    text(draw, 42, ys - 14, "Schicht  T_a  (schwarz im Infrarot, durchsichtig für Licht)", 9, BETONT)
    text(draw, 42, 30, "All", 10, DUENN)
    # Sonne durch die Schicht zum Boden
    pfeil(draw, 90, 40, 90, yb - 4, GELB, 2)
    text(draw, 96, 70, "Sonne F", 10, GELB)
    # Boden strahlt nach oben, von der Schicht geschluckt
    pfeil(draw, 180, yb - 2, 180, ys + 10, ROT, 2)
    text(draw, 186, (yb + ys) / 2 - 6, "σT_s⁴", 10, ROT)
    # Schicht strahlt nach oben und nach unten
    pfeil(draw, 270, ys - 2, 270, 44, WARN, 2)
    text(draw, 276, 70, "σT_a⁴", 10, WARN)
    pfeil(draw, 340, ys + 8, 340, yb - 4, WARN, 2)
    text(draw, 346, (yb + ys) / 2 - 6, "σT_a⁴", 10, WARN)
    text(draw, 346, (yb + ys) / 2 + 8, "Gegenstrahlung", 9, DUENN)
    text(draw, 42, 270, "oben: σT_a⁴ = F     Boden: σT_s⁴ = F + σT_a⁴ = 2σT_a⁴", 10, GUT)
    text(draw, 42, 284, "T_s = 2^(1/4)·T_a = 303 K", 11, GUT)
    sichern(bild, "skizze-einschicht")


def tagesgang():
    bild, draw = leinwand()
    ax, ay = 60, 240
    achsen(draw, ax, ay, 420, 40, "Uhr", "Temperatur")
    def hx(h): return ax + h / 24.0 * 340
    for h in (0, 6, 12, 18, 24):
        text(draw, hx(h), ay + 6, "%d" % h, 9, DUENN, mitte=True)
        gestrichelt(draw, hx(h), ay, hx(h), 50, DUENN)
    # Temperaturkurve: Minimum um 6, Maximum um 15
    def T(h):
        return 14 - 6 * math.cos(2 * math.pi * (h - 15) / 24.0)
    def ty(t): return ay - (t - 6) / 16.0 * 150
    linie(draw, [(hx(h / 2.0), ty(T(h / 2.0))) for h in range(0, 49)], WARN, 2)
    # Nettostrahlung: positiv 7-17, negativ sonst
    def Q(h):
        return max(-0.25, math.cos(2 * math.pi * (h - 12) / 24.0) * 1.1 - 0.25)
    def qy(q): return ay - 40 - q * 60
    linie(draw, [(hx(h / 2.0), qy(Q(h / 2.0))) for h in range(0, 49)], GUT, 1)
    gestrichelt(draw, ax, qy(0), hx(24), qy(0), DUENN)
    text(draw, hx(12) + 4, qy(0.85) - 12, "Nettostrahlung", 9, GUT)
    text(draw, hx(2), qy(-0.25) + 4, "−60 W/m²", 8, GUT)
    kreis(draw, hx(6), ty(T(6)), 3, BETONT)
    text(draw, hx(6) + 6, ty(T(6)) + 4, "Minimum vor Sonnenaufgang", 9, BETONT)
    text(draw, hx(6) + 6, ty(T(6)) + 16, "Tau, Nebel", 9, DUENN)
    kreis(draw, hx(15), ty(T(15)), 3, ROT)
    text(draw, hx(15) - 6, ty(T(15)) - 16, "Maximum 15 Uhr", 9, ROT, rechts=True)
    text(draw, hx(1), 60, "Nacht", 9, DUENN)
    text(draw, hx(11), 60, "Tag", 9, DUENN)
    text(draw, 60, 270, "Die Bilanz, nicht die Einstrahlung, bestimmt die Temperatur", 10, TEXT)
    sichern(bild, "skizze-tagesgang")


# ===========================================================================
# 5  Wolken
# ===========================================================================

def koehler():
    bild, draw = leinwand()
    ax, ay = 70, 230
    achsen(draw, ax, ay, 420, 40, "Radius (log)", "Übersättigung (%)")
    a = 1.2e-9       # m
    b = 1.7e-22      # m³  (NaCl-Kern 0,1 μm, 1,2·10⁷ Moleküle, i = 2)
    def rx(r): return ax + (math.log10(r) + 8) / 3.0 * 330     # 10 nm .. 10 μm
    def sy(s): return ay - s / 1.0 * 180                         # -? .. 1 %
    gestrichelt(draw, ax, sy(0), 420, sy(0), DUENN)
    text(draw, ax + 6, sy(0) + 4, "Sättigung 100 %", 9, DUENN)
    kel = [(rx(r), sy(min(1.0, (a / r) * 100))) for r in [10 ** (-8 + i / 40.0) for i in range(0, 121)]]
    kel = [p for p in kel if p[1] >= 42]
    linie(draw, kel, DUENN, 1)
    text(draw, rx(2e-8), sy(0.9) - 2, "Kelvin (reines Wasser)", 9, DUENN)
    koe = []
    for i in range(0, 121):
        r = 10 ** (-8 + i / 40.0)
        s = (a / r - b / r ** 3) * 100
        if s < -1.1:
            continue
        koe.append((rx(r), min(ay + 60, sy(s))))
    koe = [p for p in koe if p[1] <= ay + 50]
    linie(draw, koe, GUT, 2)
    rk = math.sqrt(3 * b / a)
    sk = math.sqrt(4 * a ** 3 / (27 * b)) * 100
    kreis(draw, rx(rk), sy(sk), 4, WARN)
    text(draw, rx(rk) - 8, sy(sk) - 22, "kritisch: %.2f %% bei %.2f μm" % (sk, rk * 1e6), 9, WARN, rechts=True)
    text(draw, rx(3e-8), sy(-0.6), "Köhler (Salzkern)", 10, GUT)
    text(draw, rx(3e-8), sy(-0.8), "Dunst: stabil", 9, DUENN)
    text(draw, rx(1.5e-6), sy(0.2), "aktiviert: wächst", 9, GUT)
    for r, name in ((1e-8, "10 nm"), (1e-7, "0,1 μm"), (1e-6, "1 μm"), (1e-5, "10 μm")):
        text(draw, rx(r), ay + 6, name, 9, DUENN, mitte=True)
    sichern(bild, "skizze-koehler")


def wachstum():
    bild, draw = leinwand()
    ax, ay = 70, 262
    achsen(draw, ax, ay, 420, 30, "Zeit (min)", "Radius (log)")
    def ty(r): return ay - (math.log10(r) + 6) / 3.0 * 215      # 1 μm .. 1 mm
    def tx(t): return ax + t / 40.0 * 330
    for r, name in ((1e-6, "1 μm"), (1e-5, "10 μm"), (1e-4, "0,1 mm"), (1e-3, "1 mm")):
        gestrichelt(draw, ax, ty(r), 420, ty(r), DUENN)
        text(draw, ax - 4, ty(r) - 6, name, 9, DUENN, rechts=True)
    for t in (0, 10, 20, 30, 40):
        text(draw, tx(t), ay + 6, "%d" % t, 9, DUENN, mitte=True)
    # Diffusion: r² = r0² + 2ξSt, ξS = 0,5e-10
    dif = [(tx(t), ty(math.sqrt(1e-12 + 2 * 0.5e-10 * t * 60))) for t in range(0, 41)]
    linie(draw, dif, BETONT, 2)
    text(draw, tx(28), ty(1.5e-5) - 14, "Diffusion ~ √t", 10, BETONT)
    # Koaleszenz ab 20 μm: dr/dt ∝ r² -> r = 1/(1/r0 - k t)
    r0, k = 2e-5, 1.0 / (2e-5 * 20 * 60) * 0.98
    koa = []
    for t in range(0, 41):
        tt = max(0, t - 12) * 60
        r = 1.0 / (1.0 / r0 - k * tt) if (1.0 / r0 - k * tt) > 1e3 else 1e-3
        koa.append((tx(t), ty(min(1e-3, max(r0, r)))))
    linie(draw, koa, GUT, 2)
    text(draw, tx(27), ty(3e-4) + 2, "Koaleszenz ~ r⁴", 10, GUT)
    text(draw, tx(2), ty(5e-4) - 6, "Regen", 9, DUENN)
    text(draw, tx(2), ty(1.5e-5) + 6, "Wolkentropfen", 9, DUENN)
    sichern(bild, "skizze-wachstum")


# ===========================================================================
# 6  Dynamik
# ===========================================================================

def coriolis():
    bild, draw = leinwand()
    # Links: ein Einheitsvektor, der im rotierenden System ruht, von aussen
    cx, cy = 120, 150
    pfeil(draw, cx, cy + 90, cx, cy - 110, DUENN, 1)
    text(draw, cx + 6, cy - 118, "Ω", 13, TEXT)
    # Ellipse als perspektivischer Kreis um die Achse
    a, b = 70, 24
    draw.ellipse([(cx - a) * S, (cy - 40 - b) * S, (cx + a) * S, (cy - 40 + b) * S],
                 outline=DUENN, width=S)
    # Vektor e von der Achse zur Kreisbahn
    ex, ey = cx + a * math.cos(0.6), cy - 40 + b * math.sin(0.6)
    pfeil(draw, cx, cy + 40, ex, ey, BETONT, 2)
    text(draw, ex + 6, ey - 4, "e", 13, BETONT)
    # de = Omega x e dt, tangential
    tx_, ty_ = -a * math.sin(0.6), b * math.cos(0.6)
    n = math.hypot(tx_, ty_)
    pfeil(draw, ex, ey, ex - tx_ / n * 36, ey - ty_ / n * 36, GUT, 2)
    text(draw, ex - tx_ / n * 36 - 6, ey - ty_ / n * 36 - 18, "de = Ω×e dt", 10, GUT, rechts=True)
    bogen(draw, cx, cy + 40, 30, 270, 270 + 40, WARN, 1)
    text(draw, cx + 6, cy + 2, "α", 11, WARN)
    text(draw, cx - 14, cy + 50, "sin α", 9, DUENN)
    text(draw, 30, 262, "ruht im rotierenden System", 9, DUENN)
    text(draw, 30, 276, "von außen gesehen: Kreisbahn der Spitze", 9, DUENN)
    # Rechts: der Weg eines Pakets, gerade von aussen, gekruemmt auf der Scheibe
    sx, sy = 330, 150
    kreis(draw, sx, sy, 80, (24, 26, 34), DUENN, 1)
    gestrichelt(draw, sx, sy + 76, sx, sy - 76, DUENN)
    text(draw, sx + 4, sy - 90, "gerade (von außen)", 9, DUENN)
    pts = []
    for i in range(0, 41):
        t = i / 40.0
        r = 76 * (1 - 2 * t)      # von unten nach oben durch die Mitte
        ang = -math.pi / 2 + 0.9 * t
        pts.append((sx + (-r) * math.sin(ang - math.pi / 2 + math.pi / 2) * 0 + r * math.cos(ang + math.pi / 2),
                    sy + r * math.sin(ang + math.pi / 2)))
    linie(draw, pts, ROT, 2)
    pfeil(draw, pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], ROT, 2)
    text(draw, sx - 84, sy + 86, "auf der Scheibe: nach rechts abgelenkt", 9, ROT)
    bogen(draw, sx, sy, 92, 200, 250, WARN, 1)
    pfeil(draw, sx + 92 * math.cos(math.radians(250)), sy + 92 * math.sin(math.radians(250)),
          sx + 92 * math.cos(math.radians(256)), sy + 92 * math.sin(math.radians(256)), WARN, 1, 5)
    text(draw, sx - 100, sy - 60, "Ω", 11, WARN)
    sichern(bild, "skizze-coriolis")


def breite():
    bild, draw = leinwand()
    cx, cy, r = 170, 160, 110
    kreis(draw, cx, cy, r, (24, 30, 44), DUENN, 1)
    gestrichelt(draw, cx - r, cy, cx + r, cy, DUENN)
    text(draw, cx + r + 4, cy - 6, "Äquator", 9, DUENN)
    pfeil(draw, cx, cy + r + 10, cx, cy - r - 24, WARN, 2)
    text(draw, cx + 6, cy - r - 30, "Ω", 13, WARN)
    text(draw, cx + 6, cy - r - 4, "Pol", 9, DUENN)
    text(draw, cx - 4, cy - r - 44, "Erdachse", 9, DUENN, rechts=True)
    phi = math.radians(45)
    px, py = cx + r * math.cos(phi), cy - r * math.sin(phi)
    kreis(draw, px, py, 4, KOERPER)
    strich(draw, cx, cy, px, py, DUENN, 1)
    bogen(draw, cx, cy, 40, -45, 0, GUT, 1)
    text(draw, cx + 44, cy - 20, "φ", 12, GUT)
    # lokale Achsen k (oben) und j (Nord)
    kx, ky = math.cos(phi), -math.sin(phi)
    jx, jy = -math.sin(phi), -math.cos(phi)
    pfeil(draw, px, py, px + 60 * kx, py + 60 * ky, BETONT, 2)
    text(draw, px + 60 * kx + 4, py + 60 * ky - 6, "k (oben)", 10, BETONT)
    pfeil(draw, px, py, px + 60 * jx, py + 60 * jy, BETONT, 2)
    text(draw, px + 60 * jx - 4, py + 60 * jy - 14, "j (Nord)", 10, BETONT, rechts=True)
    # Omega am Ort, zerlegt
    pfeil(draw, px, py, px, py - 70, WARN, 1)
    text(draw, px + 4, py - 80, "Ω", 10, WARN)
    gestrichelt(draw, px, py - 70, px + 70 * math.sin(phi) * kx, py - 70 + 70 * math.sin(phi) * ky * 0, WARN)
    pfeil(draw, px, py, px + 70 * math.sin(phi) * kx, py + 70 * math.sin(phi) * ky, ROT, 2)
    pfeil(draw, px, py, px + 70 * math.cos(phi) * jx, py + 70 * math.cos(phi) * jy, GUT, 2)
    text(draw, 300, 60, "Ω = Ω (0, cos φ, sin φ)", 12, TEXT)
    text(draw, 300, 84, "Ω sin φ  entlang k", 11, ROT)
    text(draw, 300, 100, "Ω cos φ  entlang j", 11, GUT)
    text(draw, 300, 130, "f = 2 Ω sin φ", 14, ROT)
    text(draw, 300, 152, "45°: 1,03·10⁻⁴ /s", 10, DUENN)
    text(draw, 300, 166, "Pol: 1,46·10⁻⁴ /s", 10, DUENN)
    text(draw, 300, 180, "Äquator: 0", 10, DUENN)
    text(draw, 300, 210, "Winkel zwischen Achse", 9, DUENN)
    text(draw, 300, 222, "und Senkrechter: 90° − φ", 9, DUENN)
    sichern(bild, "skizze-breite")


def geostrophisch():
    bild, draw = leinwand()
    for i, p in enumerate((996, 1000, 1004, 1008)):
        y = 60 + i * 55
        strich(draw, 40, y, 400, y, DUENN, 1)
        text(draw, 404, y - 6, "%d hPa" % p, 9, DUENN)
    text(draw, 40, 30, "Tief", 12, BETONT)
    text(draw, 40, 266, "Hoch", 12, WARN)
    text(draw, 300, 30, "Isobaren", 9, DUENN)
    x, y = 200, 142
    kreis(draw, x, y, 5, KOERPER)
    pfeil(draw, x, y, x + 110, y, GUT, 3)
    text(draw, x + 60, y - 20, "Wind  v_g", 12, GUT)
    pfeil(draw, x, y, x, y - 60, BETONT, 2)
    text(draw, x + 6, y - 58, "Druckgradientkraft", 10, BETONT)
    pfeil(draw, x, y, x, y + 60, ROT, 2)
    text(draw, x + 6, y + 46, "Coriolis  −f k×v", 10, ROT)
    text(draw, 44, 170, "Gleichgewicht:", 9, DUENN)
    text(draw, 44, 182, "Wind parallel zu den Isobaren,", 9, DUENN)
    text(draw, 44, 194, "Tief links (Nordhalbkugel)", 9, DUENN)
    text(draw, 44, 220, "v_g = (1/ρf) · ∂p/∂n", 11, TEXT)
    sichern(bild, "skizze-geostrophisch")


def thermisch():
    bild, draw = leinwand()
    ax, ay = 60, 240
    strich(draw, ax, ay, 420, ay, LINIE, 2)
    text(draw, ax, ay + 6, "kalt", 11, BETONT)
    text(draw, 400, ay + 6, "warm", 11, ROT, rechts=True)
    text(draw, 230, ay + 6, "1000 hPa", 9, DUENN, mitte=True)
    # Druckflaechen, nach rechts (warm) ansteigend
    for i, p in enumerate((850, 700, 500, 300)):
        yl = ay - 40 * (i + 1)
        yr = yl - 12 * (i + 1)
        strich(draw, ax, yl, 420, yr, LINIE, 1)
        text(draw, ax - 4, yl - 6, "%d" % p, 9, DUENN, rechts=True)
        # Wind in die Bildebene: Kreis mit Kreuz, Groesse nach Hoehe
        rr = 3 + 3 * i
        xm = 240
        ym = (yl + yr) / 2 - 2
        kreis(draw, xm, ym, rr, None, GUT, 1)
        strich(draw, xm - rr * 0.7, ym - rr * 0.7, xm + rr * 0.7, ym + rr * 0.7, GUT, 1)
        strich(draw, xm - rr * 0.7, ym + rr * 0.7, xm + rr * 0.7, ym - rr * 0.7, GUT, 1)
    text(draw, 270, 60, "Wind in die Bildebene", 9, GUT)
    text(draw, 270, 72, "wächst mit der Höhe", 9, GUT)
    text(draw, 270, 90, "Jet", 12, GUT)
    text(draw, ax, 30, "Druckflächen neigen sich zur kalten Seite", 10, TEXT)
    text(draw, ax, 46, "immer stärker mit der Höhe", 10, TEXT)
    text(draw, ax, 262, "∂v_g/∂ln p = −(R/f) k×∇T   —   kalt zur Linken", 10, TEXT)
    sichern(bild, "skizze-thermisch")


def ekman():
    bild, draw = leinwand()
    # Hodograph: Spitzen der Windvektoren, vom Boden bis geostrophisch
    ox, oy = 90, 220
    pfeil(draw, ox - 30, oy, 400, oy, DUENN, 1, 5)
    pfeil(draw, ox, oy + 30, ox, 60, DUENN, 1, 5)
    ug = 250.0
    pts = []
    for i in range(0, 61):
        zz = i / 60.0 * math.pi
        u = ug * (1 - math.exp(-zz) * math.cos(zz))
        v = ug * math.exp(-zz) * math.sin(zz)
        pts.append((ox + u, oy - v))
    linie(draw, pts, GUT, 2)
    for i in (6, 15, 30):
        px, py = pts[i]
        pfeil(draw, ox, oy, px, py, BETONT, 1)
        kreis(draw, px, py, 3, BETONT)
    pfeil(draw, ox, oy, ox + ug, oy, WARN, 2)
    text(draw, ox + ug - 4, oy + 8, "geostrophischer Wind", 10, WARN, rechts=True)
    text(draw, pts[6][0] + 6, pts[6][1] - 14, "am Boden: 45° zum Tief", 9, BETONT)
    text(draw, pts[30][0] + 6, pts[30][1] - 12, "Ekman-Spirale", 10, GUT)
    bogen(draw, ox, oy, 40, -45, 0, ROT, 1)
    text(draw, ox + 44, oy - 24, "45°", 9, ROT)
    text(draw, ox, 40, "Tief", 11, DUENN)
    pfeil(draw, ox - 10, 70, ox - 10, 50, DUENN, 1, 5)
    text(draw, ox - 4, 56, "zum Tief", 9, DUENN)
    text(draw, 60, 262, "D = π·√(2K/f) ≈ 1400 m     Bodenwind konvergiert ins Tief", 10, TEXT)
    sichern(bild, "skizze-ekman")


# ===========================================================================
# 7  Zirkulation
# ===========================================================================

def zellen():
    bild, draw = leinwand()
    ax, ay = 40, 220
    strich(draw, ax, ay, 420, ay, LINIE, 2)
    # Tropopause: hoch am Aequator, tief am Pol
    tp = [(ax + (90 - b) / 90.0 * 380, ay - (8 + 9 * math.cos(math.radians(b))) * 10) for b in range(0, 91, 5)]
    gestrichelt(draw, tp[0][0], tp[0][1], tp[-1][0], tp[-1][1], DUENN)
    linie(draw, tp, DUENN, 1)
    text(draw, 418, 38, "Tropopause", 9, DUENN, rechts=True)
    def bx(b): return ax + (90 - b) / 90.0 * 380
    for b in (0, 30, 60, 90):
        text(draw, bx(b), ay + 6, "%d°" % b, 9, DUENN, mitte=True)
    text(draw, bx(0), ay + 20, "Äquator", 9, DUENN, mitte=True)
    text(draw, bx(90), ay + 20, "Pol", 9, DUENN, mitte=True)
    # Zellen als Rechteckschleifen mit Pfeilen
    def zelle(b1, b2, h, farbe, name, direkt=True):
        x1, x2 = bx(b1), bx(b2)
        yt = ay - h
        if direkt:   # steigt bei b1 (aequatorwaerts), sinkt bei b2
            pfeil(draw, x1 - 8, ay - 8, x1 - 8, yt + 8, farbe, 2)
            pfeil(draw, x1 - 8, yt + 2, x2 + 8, yt + 2, farbe, 2)
            pfeil(draw, x2 + 8, yt + 8, x2 + 8, ay - 8, farbe, 2)
            pfeil(draw, x2 + 8, ay - 2, x1 - 8, ay - 2, farbe, 2)
        else:
            pfeil(draw, x2 + 8, ay - 8, x2 + 8, yt + 8, farbe, 2)
            pfeil(draw, x2 + 8, yt + 2, x1 - 8, yt + 2, farbe, 2)
            pfeil(draw, x1 - 8, yt + 8, x1 - 8, ay - 8, farbe, 2)
            pfeil(draw, x1 - 8, ay - 2, x2 + 8, ay - 2, farbe, 2)
        text(draw, (x1 + x2) / 2, yt + (ay - yt) / 2 - 7, name, 11, farbe, mitte=True)
    zelle(2, 30, 150, WARN, "Hadley")
    zelle(32, 60, 90, BETONT, "Ferrel", direkt=False)
    zelle(62, 88, 60, GUT, "Polar")
    text(draw, bx(0) + 4, ay - 170, "ITCZ", 9, WARN)
    text(draw, bx(16), ay - 20, "Passat", 9, WARN, mitte=True)
    text(draw, bx(30), ay - 36, "Subtropenhoch", 8, DUENN, mitte=True)
    text(draw, bx(30), ay - 48, "Wüste", 8, DUENN, mitte=True)
    text(draw, bx(46), ay - 20, "Westwind", 9, BETONT, mitte=True)
    text(draw, bx(60), ay - 110, "Polarfront, Jet", 8, DUENN, mitte=True)
    text(draw, 40, 262, "Breitengrad →  Hadley endet bei 30°: Drehimpuls", 10, TEXT)
    sichern(bild, "skizze-zellen")


def rossby():
    bild, draw = leinwand()
    ax, ay = 40, 150
    gestrichelt(draw, ax, ay, 420, ay, DUENN)
    text(draw, 420, ay - 12, "Grundstrom U →", 9, DUENN, rechts=True)
    pfeil(draw, 60, 40, 140, 40, WARN, 2)
    text(draw, 146, 34, "U nach Osten", 10, WARN)
    pts = [(ax + i, ay - 55 * math.sin(2 * math.pi * i / 190.0)) for i in range(0, 381)]
    linie(draw, pts, GUT, 2)
    text(draw, 300, 40, "Nord ↑", 9, DUENN)
    # Nordausschlag: antizyklonal, Suedausschlag: zyklonal
    for i, (x, dy, name, farbe, drehsinn) in enumerate(((ax + 47, -55, "antizyklonal", ROT, 1),
                                                      (ax + 142, 55, "zyklonal", BETONT, -1))):
        cx_, cy_ = x, ay + dy
        bogen(draw, cx_, cy_, 22, 20, 320, farbe, 1)
        ea = math.radians(320 if drehsinn > 0 else 20)
        pfeil(draw, cx_ + 22 * math.cos(ea), cy_ + 22 * math.sin(ea),
              cx_ + 22 * math.cos(ea) + (3 if drehsinn > 0 else -3), cy_ + 22 * math.sin(ea) - (4 if drehsinn > 0 else -4) * drehsinn, farbe, 1, 5)
        text(draw, cx_, cy_ + (-44 if dy < 0 else 30), name, 9, farbe, mitte=True)
        text(draw, cx_, cy_ + (-32 if dy < 0 else 42), "f größer, ζ kleiner" if dy < 0 else "f kleiner, ζ größer", 8, DUENN, mitte=True)
    pfeil(draw, ax + 240, ay - 85, ax + 180, ay - 85, GUT, 2)
    text(draw, ax + 244, ay - 92, "Phase nach Westen", 9, GUT)
    text(draw, 40, 240, "ζ + f erhalten:  c = U − β/k²", 12, TEXT)
    text(draw, 40, 260, "lang: steht oder läuft rückwärts  —  kurz: zieht nach Osten", 9, DUENN)
    sichern(bild, "skizze-rossby")


# ===========================================================================
# 8  Synoptik
# ===========================================================================

def fronten():
    bild, draw = leinwand()
    ay = 230
    strich(draw, 20, ay, 420, ay, LINIE, 2)
    # Warmfront links: flache Rampe von (200, ay) nach links oben
    flaeche(draw, [(20, ay), (200, ay), (20, ay - 70)], (36, 50, 80))
    linie(draw, [(200, ay), (20, ay - 70)], ROT, 2)
    # Kaltfront rechts: steiler Keil
    flaeche(draw, [(330, ay), (420, ay), (420, ay - 120), (360, ay - 60)], (36, 50, 80))
    linie(draw, [(330, ay), (360, ay - 60), (420, ay - 120)], BETONT, 2)
    text(draw, 30, ay + 6, "kalt", 10, BETONT)
    text(draw, 265, ay + 6, "Warmsektor", 10, ROT, mitte=True)
    text(draw, 410, ay + 6, "kalt", 10, BETONT, rechts=True)
    text(draw, 200, ay + 6, "Warmfront", 9, ROT, mitte=True)
    text(draw, 330, ay + 6, "Kaltfront", 9, BETONT, mitte=True)
    # Wolken entlang der Warmfront
    for x, w, h, name in ((40, 50, 8, "Cirrus"), (100, 60, 14, "Altostratus"), (165, 70, 24, "Nimbostratus")):
        yk = ay - 70 * (200 - x) / 180.0 - 10 - h
        wolke(draw, x + w / 2, yk, w, h)
        text(draw, x + w / 2, yk - h - 14, name, 8, DUENN, mitte=True)
    # Regen aus dem Nimbostratus
    for i in range(5):
        gestrichelt(draw, 150 + i * 10, ay - 40, 146 + i * 10, ay - 4, BETONT, 1, 4)
    # Cumulonimbus an der Kaltfront
    wolke(draw, 318, ay - 70, 30, 40)
    kreis(draw, 318, ay - 120, 20, WOLKE)
    flaeche(draw, [(300, ay - 130), (360, ay - 130), (355, ay - 122), (305, ay - 122)], WOLKE)
    text(draw, 300, ay - 150, "Cumulonimbus", 8, DUENN)
    text(draw, 20, 30, "Warmfront: Rampe 1:100-1:300, Dauerregen", 10, TEXT)
    text(draw, 20, 46, "Kaltfront: Keil 1:50-1:100, Schauer", 10, TEXT)
    pfeil(draw, 250, 80, 320, 80, DUENN, 1)
    text(draw, 326, 74, "Zugrichtung", 9, DUENN)
    text(draw, 20, 262, "tan α = (f·T/g) · Δu/ΔT   (Margules)", 10, TEXT)
    sichern(bild, "skizze-fronten")


def zyklone():
    bild, draw = leinwand()
    cx, cy = 200, 140
    for r in (40, 70, 100):
        bogen(draw, cx, cy, r, 0, 360, DUENN, 1)
    text(draw, cx, cy - 8, "T", 16, BETONT, mitte=True)
    # Warmfront: nach Osten (rechts), rote Linie mit Halbkreisen
    wf = [(cx + 20, cy + 30), (cx + 90, cy + 60), (cx + 170, cy + 70)]
    linie(draw, wf, ROT, 2)
    for i in range(1, 6):
        t = i / 6.0
        px = wf[0][0] + (wf[2][0] - wf[0][0]) * t
        py = wf[0][1] + (wf[2][1] - wf[0][1]) * t
        bogen(draw, px, py - 1, 5, 180, 360, ROT, 2)
    # Kaltfront: nach Suedwesten, blaue Linie mit Dreiecken
    kf = [(cx + 20, cy + 30), (cx - 20, cy + 90), (cx - 80, cy + 130)]
    linie(draw, kf, BETONT, 2)
    for i in range(1, 6):
        t = i / 6.0
        if t < 0.5:
            px = kf[0][0] + (kf[1][0] - kf[0][0]) * t * 2
            py = kf[0][1] + (kf[1][1] - kf[0][1]) * t * 2
        else:
            px = kf[1][0] + (kf[2][0] - kf[1][0]) * (t - 0.5) * 2
            py = kf[1][1] + (kf[2][1] - kf[1][1]) * (t - 0.5) * 2
        flaeche(draw, [(px, py), (px + 6, py - 4), (px + 4, py + 6)], BETONT)
    # Okklusion: vom Zentrum zum Treffpunkt
    linie(draw, [(cx, cy + 10), (cx + 20, cy + 30)], (180, 110, 220), 2)
    text(draw, cx + 110, cy + 90, "Warmfront", 9, ROT)
    text(draw, cx - 110, cy + 120, "Kaltfront", 9, BETONT)
    text(draw, cx + 60, cy + 20, "Warmsektor", 9, DUENN)
    text(draw, cx + 24, cy + 2, "Okklusion", 8, (180, 110, 220))
    # Wind gegen den Uhrzeigersinn
    for a in (30, 120, 210, 300):
        a1, a2 = math.radians(a), math.radians(a - 25)
        strich(draw, cx + 100 * math.cos(a1), cy + 100 * math.sin(a1),
               cx + 100 * math.cos(a2), cy + 100 * math.sin(a2), GUT, 2)
        pfeil(draw, cx + 100 * math.cos(a2 + 0.05), cy + 100 * math.sin(a2 + 0.05),
              cx + 100 * math.cos(a2), cy + 100 * math.sin(a2), GUT, 2, 6)
    text(draw, 20, 20, "Nord ↑", 9, DUENN)
    text(draw, 320, 30, "Wind gegen den", 9, GUT)
    text(draw, 320, 42, "Uhrzeigersinn", 9, GUT)
    text(draw, 320, 66, "Höhentrog westlich", 9, DUENN)
    text(draw, 320, 78, "des Bodentiefs", 9, DUENN)
    gestrichelt(draw, cx - 130, cy - 110, cx - 60, cy + 80, WARN, 1)
    text(draw, cx - 134, cy - 122, "Trogachse 500 hPa", 8, WARN)
    text(draw, 20, 272, "Norwegisches Modell: Welle auf der Polarfront", 10, TEXT)
    sichern(bild, "skizze-zyklone")


# ===========================================================================
# 9  Mesoskala
# ===========================================================================

def foehn():
    bild, draw = leinwand()
    ay = 250
    def zy(z): return ay - z / 3500.0 * 190
    berg = [(20, zy(500)), (120, zy(1200)), (200, zy(3000)), (260, zy(2600)), (330, zy(1500)), (420, zy(500))]
    flaeche(draw, [(20, ay)] + berg + [(420, ay)], (40, 44, 52))
    linie(draw, berg, LINIE, 2)
    # Luvseite: Weg mit Temperaturen
    pfad = [(30, zy(500)), (110, zy(1500)), (195, zy(3100)), (260, zy(2700)), (335, zy(1600)), (410, zy(500))]
    linie(draw, pfad[:3], GUT, 2)
    linie(draw, pfad[2:], ROT, 2)
    pfeil(draw, pfad[4][0], pfad[4][1], pfad[5][0], pfad[5][1], ROT, 2)
    for (x, y), name in zip(pfad[:3], ("20 °C, 500 m", "10 °C, LCL 1500 m", "1 °C, Kamm 3000 m")):
        kreis(draw, x, y, 3, KOERPER)
    text(draw, 34, zy(500) - 14, "20 °C", 10, GUT)
    text(draw, 34, zy(500) - 2, "T_d 12 °C", 8, DUENN)
    text(draw, 60, zy(1500) - 14, "LCL 1500 m, 10 °C", 9, GUT)
    text(draw, 195, zy(3000) - 24, "Kamm 3000 m, 1 °C", 9, TEXT, mitte=True)
    text(draw, 300, zy(500) - 26, "25,7 °C", 11, ROT)
    text(draw, 300, zy(500) - 12, "500 m, 27 %", 8, DUENN)
    # Wolke am Luv und Regen
    wolke(draw, 150, zy(2300), 90, 26)
    for i in range(6):
        gestrichelt(draw, 118 + i * 12, zy(2100), 114 + i * 12, zy(1500) + 10, BETONT, 1, 4)
    text(draw, 118, zy(2100) + 24, "Stau", 8, BETONT)
    text(draw, 60, 30, "Luv", 11, DUENN)
    text(draw, 380, 30, "Lee", 11, DUENN)
    text(draw, 60, 46, "feucht hinauf: 6 K/km", 9, GUT)
    text(draw, 380, 46, "trocken hinunter: 9,8 K/km", 9, ROT, rechts=True)
    text(draw, 20, 268, "Föhn: 5,7 K wärmer auf gleicher Höhe — die Kondensationswärme des Regens im Luv", 9, TEXT)
    sichern(bild, "skizze-foehn")


def seewind():
    bild, draw = leinwand()
    ay = 220
    draw.rectangle([20 * S, ay * S, 200 * S, (ay + 30) * S], fill=(30, 60, 110))
    draw.rectangle([200 * S, ay * S, 420 * S, (ay + 30) * S], fill=(70, 60, 44))
    text(draw, 110, ay + 8, "See (kühl)", 10, TEXT, mitte=True)
    text(draw, 310, ay + 8, "Land (warm)", 10, TEXT, mitte=True)
    # Zirkulation: unten See->Land, über Land auf, oben Land->See, über See ab
    pfeil(draw, 60, ay - 14, 330, ay - 14, GUT, 3)
    text(draw, 195, ay - 34, "Seewind", 11, GUT, mitte=True)
    pfeil(draw, 340, ay - 20, 340, 80, WARN, 2)
    text(draw, 348, 130, "warm, steigt", 9, WARN)
    pfeil(draw, 330, 70, 70, 70, BETONT, 2)
    text(draw, 200, 52, "Rückstrom oben", 9, BETONT, mitte=True)
    pfeil(draw, 60, 80, 60, ay - 24, DUENN, 2)
    text(draw, 66, 130, "sinkt", 9, DUENN)
    for i in range(3):
        wolke(draw, 260 + i * 55, 110, 40, 16)
    text(draw, 260, 84, "Cumulus an der Seewindfront", 8, DUENN)
    text(draw, 20, 262, "Druck oben über Land höher (warme Säule dicker) → Zirkulation", 9, TEXT)
    text(draw, 20, 276, "dC/dt = −∮dp/ρ: Solenoide aus Isobaren und Isosteren", 9, TEXT)
    sichern(bild, "skizze-seewind")


# ===========================================================================
# 10  Optik
# ===========================================================================

def streuung():
    bild, draw = leinwand()
    # links: Molekuel
    mx, my = 120, 150
    for y in (my - 30, my, my + 30):
        pfeil(draw, 20, y, mx - 10, y, KOERPER, 2)
    text(draw, 20, my - 60, "Sonnenlicht", 10, KOERPER)
    kreis(draw, mx, my, 4, TEXT)
    text(draw, mx, my + 12, "Molekül", 9, DUENN, mitte=True)
    for a, farbe, l in ((60, (90, 140, 255), 70), (120, (90, 140, 255), 70), (240, (90, 140, 255), 70), (300, (90, 140, 255), 70),
                        (80, ROT, 22), (280, ROT, 22), (100, ROT, 22), (260, ROT, 22)):
        rad = math.radians(a)
        pfeil(draw, mx, my, mx + l * math.cos(rad), my - l * math.sin(rad), farbe, 2, 5)
    text(draw, 40, 220, "Rayleigh: ~ 1/λ⁴", 11, TEXT)
    text(draw, 40, 236, "blau stark, rot schwach", 9, DUENN)
    text(draw, 40, 250, "Teilchen < λ/10", 9, DUENN)
    # rechts: Troepfchen
    tx_, ty_ = 320, 150
    for y in (ty_ - 30, ty_, ty_ + 30):
        pfeil(draw, 230, y, tx_ - 24, y, KOERPER, 2)
    kreis(draw, tx_, ty_, 20, (60, 80, 120), BETONT, 1)
    text(draw, tx_, ty_ + 26, "Tröpfchen 10 μm", 9, DUENN, mitte=True)
    for a in (20, 50, 330, 310, 160, 200, 90, 270):
        rad = math.radians(a)
        l = 60 if a < 60 or a > 300 else 30
        pfeil(draw, tx_ + 20 * math.cos(rad), ty_ - 20 * math.sin(rad), tx_ + (20 + l) * math.cos(rad), ty_ - (20 + l) * math.sin(rad), KOERPER, 2, 5)
    text(draw, 240, 220, "Mie: alle Farben gleich", 11, TEXT)
    text(draw, 240, 236, "weiß, vorwärts gestreut", 9, DUENN)
    text(draw, 240, 250, "Teilchen > λ", 9, DUENN)
    sichern(bild, "skizze-streuung")


def regenbogen():
    bild, draw = leinwand()
    cx, cy, r = 250, 140, 80
    kreis(draw, cx, cy, r, (30, 50, 90), BETONT, 1)
    text(draw, cx, cy + r + 8, "Tropfen", 9, DUENN, mitte=True)
    n = 1.333
    i = math.acos(math.sqrt((n * n - 1) / 3))
    rr = math.asin(math.sin(i) / n)
    # Einfall von links, parallel zur x-Achse, Hoehe r*sin(i)
    ye = cy - r * math.sin(i)
    xe = cx - r * math.cos(i)
    pfeil(draw, 40, ye, xe, ye, GELB, 2)
    text(draw, 40, ye - 14, "Sonnenlicht", 9, GELB)
    # Innen: Winkel am Mittelpunkt. Einfallspunkt bei Winkel (pi - i) relativ zur Achse
    a1 = math.pi - i                      # Position des Einfallspunkts (Winkel von +x, gegen Uhrzeiger, y nach oben)
    a2 = a1 - (math.pi - 2 * rr)          # Reflexionspunkt
    a3 = a2 - (math.pi - 2 * rr)          # Austrittspunkt
    def P(a): return (cx + r * math.cos(a), cy - r * math.sin(a))
    p1, p2, p3 = P(a1), P(a2), P(a3)
    linie(draw, [p1, p2], GELB, 2)
    linie(draw, [p2, p3], GELB, 2)
    # Austritt: Richtung gegenueber der Normalen um i
    norm3 = a3
    aus = norm3 - i if True else norm3 + i
    # Austrittsstrahl laeuft nach links unten zurueck zum Beobachter
    ex, ey = p3[0] + 150 * math.cos(math.pi + aus), p3[1] - 150 * math.sin(math.pi + aus)
    pfeil(draw, p3[0], p3[1], ex, ey, ROT, 2)
    kreis(draw, ex, ey + 4, 5, KOERPER)
    text(draw, ex - 10, ey + 12, "Beobachter", 9, DUENN, rechts=True)
    gestrichelt(draw, ex, ey, ex + 160, ey, DUENN)
    text(draw, ex + 100, ey + 4, "zum Sonnengegenpunkt", 8, DUENN)
    bogen(draw, ex, ey, 40, -42, 0, GUT, 1)
    text(draw, ex + 44, ey - 26, "42°", 11, GUT)
    text(draw, 20, 230, "δ = 180° + 2i − 4r,  Minimum bei cos i = √((n²−1)/3)", 10, TEXT)
    text(draw, 20, 248, "i = 59,5°, r = 40,3°, δ = 138°  →  Bogen bei 42°", 10, GUT)
    text(draw, 20, 266, "rot außen (n = 1,331: 42,4°), blau innen (1,343: 40,6°)", 9, DUENN)
    sichern(bild, "skizze-regenbogen")


def halo():
    bild, draw = leinwand()
    cx, cy, r = 200, 150, 70
    pts = [(cx + r * math.cos(math.radians(60 * k + 30)), cy + r * math.sin(math.radians(60 * k + 30))) for k in range(6)]
    flaeche(draw, pts, (40, 60, 100))
    linie(draw, pts + [pts[0]], BETONT, 1)
    text(draw, cx, cy + r + 10, "Eisprisma, Sechseck", 9, DUENN, mitte=True)
    # Strahl durch zwei Flaechen im 60°-Winkel (Flaechen 0 und 2), symmetrischer Gang
    n = 1.31
    A = math.radians(60)
    i1 = math.asin(n * math.sin(A / 2))
    # Eintrittspunkt auf Flaeche zwischen pts[4] und pts[5] (links), Austritt zwischen pts[0] und pts[1]... vereinfachend:
    ein = ((pts[4][0] + pts[5][0]) / 2, (pts[4][1] + pts[5][1]) / 2)
    aus = ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2)
    # Innenstrahl parallel zur Basis der beiden Flaechen
    linie(draw, [ein, aus], GELB, 2)
    # Aussen: Einfallsrichtung um i1 gegen die Normale der Eintrittsflaeche
    delta = math.degrees(2 * i1 - A)
    richt_in = math.radians(180 + 0)      # Strahl von links, abgelenkt um delta/2 je Flaeche
    x0, y0 = ein[0] - 120 * math.cos(math.radians(delta / 2)), ein[1] + 120 * math.sin(math.radians(delta / 2))
    pfeil(draw, x0, y0, ein[0], ein[1], GELB, 2)
    x1, y1 = aus[0] + 120 * math.cos(math.radians(delta / 2)), aus[1] + 120 * math.sin(math.radians(delta / 2))
    pfeil(draw, aus[0], aus[1], x1, y1, ROT, 2)
    gestrichelt(draw, aus[0], aus[1], aus[0] + 120, aus[1], DUENN)
    bogen(draw, aus[0], aus[1], 50, 0, delta, GUT, 1)
    text(draw, aus[0] + 54, aus[1] + 4, "δ = 21,8°", 11, GUT)
    text(draw, 20, 40, "Sonnenlicht", 9, GELB)
    text(draw, 20, 240, "δ_min = 2·arcsin(n·sin 30°) − 60°,  n = 1,31", 10, TEXT)
    text(draw, 20, 258, "Ring 22° um die Sonne, innen rot", 10, GUT)
    text(draw, 20, 274, "Cirrostratus: Warmfront in 12-24 h", 9, DUENN)
    sichern(bild, "skizze-halo")


# ===========================================================================
# 11  Vorhersage
# ===========================================================================

def gitter():
    bild, draw = leinwand()
    x0, y0, d = 60, 40, 60
    for i in range(6):
        strich(draw, x0 + i * d, y0, x0 + i * d, y0 + 3 * d, DUENN, 1)
    for j in range(4):
        strich(draw, x0, y0 + j * d, x0 + 5 * d, y0 + j * d, DUENN, 1)
    for i in range(5):
        for j in range(3):
            kreis(draw, x0 + i * d + d / 2, y0 + j * d + d / 2, 2, LINIE)
    text(draw, x0 + 2.5 * d, y0 + 3 * d + 8, "Gitterzelle Δx = 10 km, Werte nur im Punkt", 9, DUENN, mitte=True)
    # ein Cumulus, kleiner als die Zelle
    wolke(draw, x0 + 3.5 * d, y0 + 1.5 * d + 8, 22, 12, WOLKE)
    text(draw, x0 + 3.5 * d, y0 + 1.5 * d + 14, "Cumulus 1 km", 8, WARN, mitte=True)
    text(draw, x0 + 3.5 * d, y0 + 1.5 * d + 26, "parametrisiert", 8, WARN, mitte=True)
    pfeil(draw, x0 + 0.5 * d, y0 + 0.5 * d, x0 + 1.5 * d - 6, y0 + 0.5 * d, GUT, 2)
    text(draw, x0 + 1.0 * d, y0 + 0.5 * d - 16, "c·Δt < Δx", 10, GUT, mitte=True)
    text(draw, 60, 250, "7 Gleichungen, 7 Unbekannte (u, v, w, p, ρ, T, q)", 10, TEXT)
    text(draw, 60, 266, "10⁹ Punkte × 2000 Schritte für zehn Tage", 9, DUENN)
    sichern(bild, "skizze-gitter")


def ensemble():
    bild, draw = leinwand()
    ax, ay = 60, 250
    achsen(draw, ax, ay, 420, 40, "Tage", "Vorhersage")
    for d in range(0, 11, 2):
        text(draw, ax + d / 10.0 * 340, ay + 6, "%d" % d, 9, DUENN, mitte=True)
    import random
    rnd = random.Random(7)
    for k in range(16):
        pts = [(ax, ay - 100)]
        y = ay - 100
        drift = rnd.uniform(-1, 1)
        for i in range(1, 41):
            t = i / 4.0
            y += drift * 1.2 * math.exp(t / 5.0) * 0.4 + rnd.uniform(-2, 2) * math.sqrt(t) * 0.4
            pts.append((ax + t / 10.0 * 340, max(50, min(ay - 4, y))))
        linie(draw, pts, (80, 150, 100) if k else GUT, 1)
    strich(draw, ax, ay - 100, ax + 340, ay - 100, WARN, 2)
    text(draw, ax + 344, ay - 106, "Mittel", 9, WARN)
    text(draw, ax + 250, 60, "Streuung wächst", 9, DUENN)
    text(draw, ax + 250, 72, "exponentiell", 9, DUENN)
    text(draw, ax + 20, ay - 125, "50 Mitglieder, gestörter Start", 9, GUT)
    text(draw, 60, 270, "Fehlerverdopplung alle 2 Tage → Grenze bei zwei Wochen", 10, TEXT)
    sichern(bild, "skizze-ensemble")



# ===========================================================================
# Nachgebesserte Fassungen (ersetzen die gleichnamigen oben)
# ===========================================================================

def bilanz():
    bild, draw = leinwand()
    cx, cy, r = 260, 160, 66
    kreis(draw, cx, cy, r, (40, 70, 110), BETONT, 1)
    text(draw, cx, cy - 6, "Erde", 12, TEXT, mitte=True)
    for dy in (-45, -22, 0, 22, 45):
        pfeil(draw, 30, cy + dy, cx - r - 6, cy + dy, GELB, 2)
    text(draw, 30, cy - 86, "Sonne: S₀ = 1361 W/m²", 11, GELB)
    text(draw, 30, cy - 72, "auf die Scheibe π·R²", 9, DUENN)
    pfeil(draw, cx - r + 10, cy - 30, 110, 50, GELB, 1)
    text(draw, 112, 36, "reflektiert: A = 0,3", 9, GELB)
    for a in range(0, 360, 45):
        rad = math.radians(a)
        pfeil(draw, cx + (r + 4) * math.cos(rad), cy + (r + 4) * math.sin(rad),
              cx + (r + 30) * math.cos(rad), cy + (r + 30) * math.sin(rad), ROT, 1, 5)
    text(draw, cx + r + 36, cy - 30, "Infrarot ins All", 10, ROT)
    text(draw, cx + r + 36, cy - 16, "über 4π·R²", 9, DUENN)
    text(draw, 30, 248, "absorbiert: S₀(1−A)/4 = 238 W/m² = σ·T⁴  →  T = 255 K", 11, GUT)
    text(draw, 30, 268, "Erde: 255 K von außen, 288 K am Boden", 10, TEXT)
    sichern(bild, "skizze-bilanz")


def breite():
    bild, draw = leinwand()
    cx, cy, r = 140, 165, 105
    kreis(draw, cx, cy, r, (24, 30, 44), DUENN, 1)
    gestrichelt(draw, cx - r, cy, cx + r, cy, DUENN)
    text(draw, cx - r + 4, cy + 4, "Äquator", 9, DUENN)
    pfeil(draw, cx, cy + r + 10, cx, cy - r - 22, WARN, 2)
    text(draw, cx - 8, cy - r - 36, "Ω  Erdachse", 11, WARN, rechts=True)
    text(draw, cx - 8, cy - r - 4, "Pol", 9, DUENN, rechts=True)
    phi = math.radians(45)
    px, py = cx + r * math.cos(phi), cy - r * math.sin(phi)
    strich(draw, cx, cy, px, py, DUENN, 1)
    bogen(draw, cx, cy, 36, -45, 0, GUT, 1)
    text(draw, cx + 40, cy - 22, "φ", 12, GUT)
    kx, ky = math.cos(phi), -math.sin(phi)
    jx, jy = -math.sin(phi), -math.cos(phi)
    pfeil(draw, px, py, px + 56 * kx, py + 56 * ky, BETONT, 2)
    text(draw, px + 56 * kx + 4, py + 56 * ky - 4, "k (oben)", 10, BETONT)
    pfeil(draw, px, py, px + 56 * jx, py + 56 * jy, BETONT, 2)
    text(draw, px + 56 * jx - 4, py + 56 * jy - 6, "j (Nord)", 10, BETONT, rechts=True)
    kreis(draw, px, py, 4, KOERPER)
    # Omega am Ort (parallel zur Achse) und seine beiden Komponenten
    pfeil(draw, px, py, px, py - 64, WARN, 1)
    text(draw, px + 5, py - 72, "Ω", 10, WARN)
    pfeil(draw, px, py, px + 64 * math.sin(phi) * kx, py + 64 * math.sin(phi) * ky, ROT, 2)
    pfeil(draw, px, py, px + 64 * math.cos(phi) * jx, py + 64 * math.cos(phi) * jy, GUT, 2)
    gestrichelt(draw, px + 64 * math.sin(phi) * kx, py + 64 * math.sin(phi) * ky, px, py - 64, DUENN)
    gestrichelt(draw, px + 64 * math.cos(phi) * jx, py + 64 * math.cos(phi) * jy, px, py - 64, DUENN)
    x = 290
    text(draw, x, 50, "Ω = Ω (0, cos φ, sin φ)", 12, TEXT)
    text(draw, x, 76, "Ω sin φ  entlang k", 11, ROT)
    text(draw, x, 92, "Ω cos φ  entlang j", 11, GUT)
    text(draw, x, 124, "f = 2 Ω sin φ", 14, ROT)
    text(draw, x, 150, "45°: 1,03·10⁻⁴ /s", 10, DUENN)
    text(draw, x, 164, "Pol: 1,46·10⁻⁴ /s", 10, DUENN)
    text(draw, x, 178, "Äquator: 0", 10, DUENN)
    text(draw, x, 206, "Winkel zwischen Achse", 9, DUENN)
    text(draw, x, 218, "und Senkrechter: 90° − φ", 9, DUENN)
    sichern(bild, "skizze-breite")


def coriolis():
    bild, draw = leinwand()
    cx, cy = 115, 150
    pfeil(draw, cx, cy + 90, cx, cy - 110, DUENN, 1)
    text(draw, cx + 6, cy - 118, "Ω", 13, TEXT)
    a, b = 70, 24
    draw.ellipse([(cx - a) * S, (cy - 40 - b) * S, (cx + a) * S, (cy - 40 + b) * S],
                 outline=DUENN, width=S)
    ex, ey = cx + a * math.cos(0.6), cy - 40 + b * math.sin(0.6)
    pfeil(draw, cx, cy + 40, ex, ey, BETONT, 2)
    text(draw, ex + 6, ey - 4, "e", 13, BETONT)
    tx_, ty_ = -a * math.sin(0.6), b * math.cos(0.6)
    n = math.hypot(tx_, ty_)
    pfeil(draw, ex, ey, ex - tx_ / n * 36, ey - ty_ / n * 36, GUT, 2)
    text(draw, ex - tx_ / n * 36 - 6, ey - ty_ / n * 36 - 18, "de = Ω×e dt", 10, GUT, rechts=True)
    bogen(draw, cx, cy + 40, 30, 270, 270 + 40, WARN, 1)
    text(draw, cx + 6, cy + 2, "α", 11, WARN)
    text(draw, cx + 30, cy - 70, "sin α", 9, DUENN)
    text(draw, 20, 252, "e ruht im rotierenden System;", 9, DUENN)
    text(draw, 20, 266, "von außen gesehen: Kreisbahn der Spitze", 9, DUENN)
    # Rechts: Scheibe von oben, Bahn eines Pakets
    sx, sy = 330, 150
    kreis(draw, sx, sy, 80, (24, 26, 34), DUENN, 1)
    gestrichelt(draw, sx, sy + 76, sx, sy - 76, DUENN)
    text(draw, sx + 6, sy - 92, "gerade (von außen)", 9, DUENN)
    pts = [(sx + 70 * t * t, sy + 76 - 152 * t) for t in [i / 30.0 for i in range(31)]]
    linie(draw, pts, ROT, 2)
    pfeil(draw, pts[-2][0], pts[-2][1], pts[-1][0], pts[-1][1], ROT, 2)
    text(draw, sx - 90, sy + 90, "auf der Scheibe: nach rechts abgelenkt", 9, ROT)
    bogen(draw, sx, sy, 92, 200, 250, WARN, 1)
    pfeil(draw, sx + 92 * math.cos(math.radians(204)), sy + 92 * math.sin(math.radians(204)),
          sx + 92 * math.cos(math.radians(200)), sy + 92 * math.sin(math.radians(200)), WARN, 1, 5)
    text(draw, sx - 104, sy - 54, "Ω", 11, WARN)
    sichern(bild, "skizze-coriolis")


def geostrophisch():
    bild, draw = leinwand()
    for i, p in enumerate((996, 1000, 1004, 1008)):
        y = 60 + i * 55
        strich(draw, 40, y, 360, y, DUENN, 1)
        text(draw, 364, y - 6, "%d hPa" % p, 9, DUENN)
    text(draw, 40, 30, "Tief", 12, BETONT)
    text(draw, 40, 266, "Hoch", 12, WARN)
    text(draw, 280, 30, "Isobaren", 9, DUENN)
    x, y = 200, 142
    kreis(draw, x, y, 5, KOERPER)
    pfeil(draw, x, y, x + 110, y, GUT, 3)
    text(draw, x + 60, y - 20, "Wind  v_g", 12, GUT)
    pfeil(draw, x, y, x, y - 60, BETONT, 2)
    text(draw, x + 6, y - 58, "Druckgradientkraft", 10, BETONT)
    pfeil(draw, x, y, x, y + 60, ROT, 2)
    text(draw, x + 6, y + 46, "Coriolis  −f k×v", 10, ROT)
    text(draw, 44, 170, "Gleichgewicht:", 9, DUENN)
    text(draw, 44, 182, "Wind parallel zu den Isobaren,", 9, DUENN)
    text(draw, 44, 194, "Tief links (Nordhalbkugel)", 9, DUENN)
    text(draw, 44, 220, "v_g = (1/ρf) · ∂p/∂n", 11, TEXT)
    sichern(bild, "skizze-geostrophisch")


def hebung():
    bild, draw = leinwand()
    ax, ay = 90, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 30) / 60.0 * 310
    def zy(z): return ay - z / 4.0 * 215
    T0, Td0 = 24.0, 12.0
    zl = (T0 - Td0) / 8.0
    Tl = T0 - 9.8 * zl
    linie(draw, [(tx(T0), zy(0)), (tx(Tl), zy(zl))], WARN, 2)
    linie(draw, [(tx(Td0), zy(0)), (tx(Tl), zy(zl))], BETONT, 2)
    linie(draw, [(tx(Tl), zy(zl)), (tx(Tl - 6 * (4 - zl)), zy(4))], GUT, 2)
    gestrichelt(draw, ax, zy(zl), 420, zy(zl), DUENN)
    for i in range(4):
        wolke(draw, tx(Tl) + 40 + i * 44, zy(zl) - 2, 36, 18)
    text(draw, tx(T0) + 6, zy(0) - 10, "T = 24 °C", 10, WARN)
    text(draw, tx(Td0) - 6, zy(0) - 10, "T_d = 12 °C", 10, BETONT, rechts=True)
    text(draw, (tx(T0) + tx(Tl)) / 2 + 10, (zy(0) + zy(zl)) / 2, "−9,8 K/km", 9, WARN)
    text(draw, (tx(Td0) + tx(Tl)) / 2 - 10, (zy(0) + zy(zl)) / 2, "−1,8 K/km", 9, BETONT, rechts=True)
    text(draw, ax - 4, zy(zl) - 6, "LCL %d m" % int(zl * 1000), 9, GUT, rechts=True)
    text(draw, ax - 4, zy(zl) + 6, "Wolkenbasis", 9, DUENN, rechts=True)
    text(draw, tx(Tl - 6 * 2) - 6, zy(3), "Feuchtadiabate −6 K/km", 9, GUT, rechts=True)
    text(draw, 100, 36, "Spreizung schließt sich mit 8 K/km", 9, TEXT)
    text(draw, 100, 50, "z = 125 m/K × (T − T_d)", 11, GUT)
    sichern(bild, "skizze-hebung")


def emagramm():
    bild, draw = leinwand()
    ax, ay = 70, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "ln p  (Höhe)")
    ZMAX = 14.0
    def tx(T): return ax + (T + 70) / 110.0 * 330
    def zy(z): return ay - z / ZMAX * 215
    def Tu(z):
        if z < 1.0: return 25 - 9.0 * z
        if z < 1.6: return 16 + 2.0 * (z - 1.0)
        if z < 11: return 17.2 - 7.2 * (z - 1.6)
        return 17.2 - 7.2 * 9.4
    zl = 7 / 8.0
    Tl = 25 - 9.8 * zl
    def Tp(z):
        if z < zl: return 25 - 9.8 * z
        return Tl - 5.5 * (z - zl)
    zs = [i / 20.0 for i in range(0, int(ZMAX * 20) + 1)]
    # Schnittpunkte von Paket und Umgebung oberhalb des LCL
    kreuz = []
    for z1, z2 in zip(zs, zs[1:]):
        if z1 < zl: continue
        if (Tp(z1) - Tu(z1)) * (Tp(z2) - Tu(z2)) < 0:
            kreuz.append(z1)
    lfc, el = kreuz[0], kreuz[1]
    def band(z_von, z_bis, farbe):
        pts = [(tx(Tp(z)), zy(z)) for z in zs if z_von <= z <= z_bis]
        pts += [(tx(Tu(z)), zy(z)) for z in reversed(zs) if z_von <= z <= z_bis]
        flaeche(draw, pts, farbe)
    band(zl, lfc, (90, 30, 30))
    band(lfc, el, (30, 70, 40))
    linie(draw, [(tx(Tp(z)), zy(z)) for z in zs], GUT, 2)
    linie(draw, [(tx(Tu(z)), zy(z)) for z in zs], WARN, 2)
    linie(draw, [(tx(18 - 2.5 * z), zy(z)) for z in (0, 7)], BETONT, 1)
    for z, name in ((zl, "LCL"), (lfc, "LFC"), (el, "EL")):
        gestrichelt(draw, ax, zy(z), 420, zy(z), DUENN)
        text(draw, ax - 4, zy(z) - 6, name, 9, DUENN, rechts=True)
    text(draw, tx(Tu(7)) + 8, zy(7), "Aufstieg", 10, WARN)
    text(draw, tx(Tp(9)) - 8, zy(9) - 10, "Paket", 10, GUT, rechts=True)
    text(draw, tx(18 - 2.5 * 5) - 6, zy(5) + 2, "Taupunkt", 9, BETONT, rechts=True)
    text(draw, tx(Tp(2)) - 10, zy(2.3), "CIN", 10, ROT, rechts=True)
    text(draw, tx(Tp(7)) - 30, zy(6.5), "CAPE", 12, GUT, rechts=True)
    text(draw, 240, 250, "Trockenadiabate bis LCL, dann Feuchtadiabate", 8, DUENN)
    sichern(bild, "skizze-emagramm")


def paket():
    bild, draw = leinwand()
    gestrichelt(draw, 40, 262, 400, 262, DUENN)
    text(draw, 400, 266, "Boden", 10, DUENN, rechts=True)
    for i, (z, T, r) in enumerate(((0, 20, 16), (1000, 10, 21), (2000, 0, 27))):
        y = 240 - i * 90
        kreis(draw, 130, y, r, (40, 60, 100), BETONT, 1)
        text(draw, 130 + r + 10, y - 16, "%d m" % z, 10, DUENN)
        text(draw, 130 + r + 10, y - 2, "%d °C" % T, 12, WARN)
        text(draw, 130 + r + 10, y + 12, "p = %d hPa" % (1013, 899, 795)[i], 9, DUENN)
        if i < 2:
            pfeil(draw, 130, y - r - 6, 130, y - 90 + 27 + 6, GUT, 2)
    text(draw, 270, 50, "Luftpaket", 12, TEXT)
    text(draw, 270, 66, "steigt, dehnt sich aus, kühlt ab", 9, DUENN)
    text(draw, 270, 150, "−9,8 K je km", 13, GUT)
    text(draw, 270, 168, "Γ = g / c_p", 12, TEXT)
    text(draw, 270, 190, "keine Wärme tauscht,", 9, DUENN)
    text(draw, 270, 202, "Arbeit gegen den Außendruck", 9, DUENN)
    sichern(bild, "skizze-paket")


def theta():
    bild, draw = leinwand()
    ax, ay = 80, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 60) / 100.0 * 320
    def zy(z): return ay - z / 10.0 * 215
    linie(draw, [(tx(15 - 6.5 * z), zy(z)) for z in (0, 10)], WARN, 2)
    linie(draw, [(tx(15 - 9.8 * z), zy(z)) for z in (0, 7.5)], BETONT, 2)
    linie(draw, [(tx(15 + 3.3 * z), zy(z)) for z in (0, 8)], GUT, 2)
    text(draw, tx(15 - 6.5 * 9) - 4, zy(9) - 4, "Umgebung 6,5 K/km", 10, WARN, rechts=True)
    text(draw, tx(15 - 9.8 * 5) - 4, zy(5) + 4, "Adiabate 9,8 K/km", 10, BETONT, rechts=True)
    text(draw, tx(15 + 3.3 * 8) - 4, zy(8) - 14, "θ: + 3,3 K/km", 10, GUT, rechts=True)
    kreis(draw, tx(15), zy(0), 4, KOERPER)
    text(draw, tx(15) + 6, zy(0) - 16, "15 °C, 1000 hPa", 9, DUENN)
    gestrichelt(draw, ax, zy(5), tx(15 + 3.3 * 5), zy(5), DUENN)
    text(draw, ax - 4, zy(5) - 6, "500 hPa", 9, DUENN, rechts=True)
    text(draw, tx(15 - 6.5 * 5) - 2, zy(5) + 6, "−18 °C", 9, WARN, rechts=True)
    text(draw, tx(15 + 3.3 * 5) + 4, zy(5) + 6, "θ = 309 K", 9, GUT)
    sichern(bild, "skizze-theta")


def stabilitaet():
    bild, draw = leinwand()
    ax, ay = 60, 262
    achsen(draw, ax, ay, 420, 30, "Temperatur", "Höhe")
    def tx(T): return ax + (T + 30) / 60.0 * 330
    def zy(z): return ay - z / 3.0 * 215
    z0, T0 = 1.0, 10.0
    linie(draw, [(tx(T0 + 9.8 * (z0 - z)), zy(z)) for z in (0, 3)], BETONT, 2)
    text(draw, tx(T0 - 9.8 * 1.95) - 4, zy(2.95) + 2, "Adiabate", 10, BETONT, rechts=True)
    for G, name, farbe, zz in ((6.5, "stabil", GUT, 2.6), (13, "labil", ROT, 0.45), (-5, "Inversion", WARN, 0.45)):
        pts = [(tx(T0 + G * (z0 - z)), zy(z)) for z in (0.4, 2.6)]
        linie(draw, pts, farbe, 1)
        text(draw, tx(T0 + G * (z0 - zz)) + 5, zy(zz) - 6, name, 10, farbe)
    text(draw, tx(T0 - 9.8 * 1.0) + 5, zy(2.0) - 6, "neutral = Adiabate", 9, DUENN)
    kreis(draw, tx(T0), zy(z0), 4, KOERPER)
    text(draw, tx(T0) + 8, zy(z0) + 2, "Paket in Ruhe", 9, DUENN)
    zh = 2.2
    kreis(draw, tx(T0 - 9.8 * (zh - z0)), zy(zh), 4, BETONT)
    text(draw, tx(T0 - 9.8 * (zh - z0)) - 8, zy(zh) + 2, "Paket, gehoben", 9, BETONT, rechts=True)
    text(draw, 200, 236, "kälter als die Umgebung: sinkt zurück", 9, GUT)
    text(draw, 200, 250, "wärmer als die Umgebung: steigt weiter", 9, ROT)
    sichern(bild, "skizze-stabilitaet")


def standard():
    bild, draw = leinwand()
    ax, ay = 80, 262
    achsen(draw, ax, ay, 420, 30, "hPa", "Höhe (km)")
    g, R, G, T0 = 9.81, 287.05, 0.0065, 288.15
    def p(z):
        if z <= 11000: return 1013.25 * (1 - G * z / T0) ** (g / (R * G))
        return 226.32 * math.exp(-g * (z - 11000) / (R * 216.65))
    def px(pp): return ax + pp / 1013.25 * 300
    def zy(z): return ay - z / 20000.0 * 215
    linie(draw, [(px(p(z)), zy(z)) for z in range(0, 20001, 500)], WARN, 2)
    for pp, z in ((850, 1457), (700, 3012), (500, 5574), (300, 9164), (200, 11784)):
        gestrichelt(draw, ax, zy(z), px(pp), zy(z), DUENN)
        gestrichelt(draw, px(pp), zy(z), px(pp), ay, DUENN)
        text(draw, px(pp), ay + 6, "%d" % pp, 9, DUENN, mitte=True)
        text(draw, ax - 4, zy(z) - 6, "%d m" % z, 9, DUENN, rechts=True)
    text(draw, px(1013.25), ay + 6, "1013", 9, DUENN, mitte=True)
    gestrichelt(draw, ax, zy(11000), 420, zy(11000), BETONT)
    text(draw, 418, zy(11000) - 12, "Tropopause −56,5 °C", 9, BETONT, rechts=True)
    text(draw, 250, 60, "T = 15 °C − 6,5 K/km · z", 11, TEXT)
    text(draw, 250, 76, "Standardatmosphäre", 10, DUENN)
    sichern(bild, "skizze-standard")


def rossby():
    bild, draw = leinwand()
    ax, ay = 40, 140
    gestrichelt(draw, ax, ay, 420, ay, DUENN)
    text(draw, 420, ay - 12, "Grundstrom U →", 9, DUENN, rechts=True)
    pfeil(draw, 60, 36, 140, 36, WARN, 2)
    text(draw, 146, 30, "U nach Osten", 10, WARN)
    pts = [(ax + i, ay - 50 * math.sin(2 * math.pi * i / 190.0)) for i in range(0, 381)]
    linie(draw, pts, GUT, 2)
    text(draw, 300, 36, "Nord ↑", 9, DUENN)
    for x, dy, name, farbe, hinweis in ((ax + 47, -50, "antizyklonal", ROT, "f größer, ζ kleiner"),
                                        (ax + 142, 50, "zyklonal", BETONT, "f kleiner, ζ größer")):
        cx_, cy_ = x, ay + dy
        bogen(draw, cx_, cy_, 20, 20, 320, farbe, 1)
        text(draw, cx_, cy_ + (-44 if dy < 0 else 26), name, 9, farbe, mitte=True)
        text(draw, cx_, cy_ + (-32 if dy < 0 else 38), hinweis, 8, DUENN, mitte=True)
    pfeil(draw, ax + 250, ay - 78, ax + 190, ay - 78, GUT, 2)
    text(draw, ax + 254, ay - 85, "Phase nach Westen", 9, GUT)
    text(draw, 40, 246, "ζ + f erhalten:  c = U − β/k²", 12, TEXT)
    text(draw, 40, 266, "lang: steht oder läuft rückwärts  —  kurz: zieht nach Osten", 9, DUENN)
    sichern(bild, "skizze-rossby")


def regenbogen():
    bild, draw = leinwand()
    cx, cy, r = 300, 92, 60
    kreis(draw, cx, cy, r, (30, 50, 90), BETONT, 1)
    text(draw, cx + r + 6, cy - 6, "Tropfen", 9, DUENN)
    n = 1.333
    i = math.acos(math.sqrt((n * n - 1) / 3))
    rr = math.asin(math.sin(i) / n)
    def P(a_deg):
        a = math.radians(a_deg)
        return (cx + r * math.cos(a), cy - r * math.sin(a))
    a1 = 180 - math.degrees(i)
    a2 = a1 - (180 - 2 * math.degrees(rr))
    a3 = a2 - (180 - 2 * math.degrees(rr))
    p1, p2, p3 = P(a1), P(a2), P(a3)
    pfeil(draw, 30, p1[1], p1[0], p1[1], GELB, 2)
    text(draw, 30, p1[1] - 14, "Sonnenlicht", 9, GELB)
    linie(draw, [p1, p2], GELB, 2)
    linie(draw, [p2, p3], GELB, 2)
    delta = 180 + 2 * math.degrees(i) - 4 * math.degrees(rr)
    d = math.radians(-delta)
    L = 105
    ex, ey = p3[0] + L * math.cos(d), p3[1] - L * math.sin(d)
    pfeil(draw, p3[0], p3[1], ex, ey, ROT, 2)
    kreis(draw, ex, ey, 5, KOERPER)
    text(draw, ex - 8, ey + 8, "Beobachter", 9, DUENN, rechts=True)
    gestrichelt(draw, ex, ey, ex + 150, ey, DUENN)
    text(draw, ex + 40, ey + 4, "zum Sonnengegenpunkt", 8, DUENN)
    bogen(draw, ex, ey, 40, -42, 0, GUT, 1)
    text(draw, ex + 44, ey - 26, "42°", 11, GUT)
    bogen(draw, p1[0], p1[1], 22, 0, math.degrees(i), DUENN, 1)
    text(draw, p1[0] + 24, p1[1] + 4, "i", 10, DUENN)
    text(draw, 20, 244, "δ = 180° + 2i − 4r,  Minimum bei cos i = √((n²−1)/3)", 10, TEXT)
    text(draw, 20, 262, "i = 59,5°, r = 40,3°, δ = 138°  →  Bogen bei 42°", 10, GUT)
    text(draw, 20, 280, "rot außen (n = 1,331: 42,4°), blau innen (1,343: 40,6°)", 9, DUENN)
    sichern(bild, "skizze-regenbogen")


def halo():
    bild, draw = leinwand()
    cx, cy, r = 220, 150, 62
    def V(a_deg):
        a = math.radians(a_deg)
        return (cx + r * math.cos(a), cy - r * math.sin(a))
    pts = [V(60 * k) for k in range(6)]
    flaeche(draw, pts, (40, 60, 100))
    linie(draw, pts + [pts[0]], BETONT, 1)
    text(draw, cx, cy + r + 8, "Eisprisma, Sechseck", 9, DUENN, mitte=True)
    n = 1.31
    A = 60.0
    i1 = math.degrees(math.asin(n * math.sin(math.radians(A / 2))))
    delta = 2 * i1 - A
    ein = ((V(120)[0] + V(180)[0]) / 2, (V(120)[1] + V(180)[1]) / 2)
    aus = ((V(0)[0] + V(60)[0]) / 2, (V(0)[1] + V(60)[1]) / 2)
    linie(draw, [ein, aus], GELB, 2)
    h = delta / 2
    x0, y0 = ein[0] - 130 * math.cos(math.radians(h)), ein[1] + 130 * math.sin(math.radians(h))
    pfeil(draw, x0, y0, ein[0], ein[1], GELB, 2)
    x1, y1 = aus[0] + 130 * math.cos(math.radians(h)), aus[1] + 130 * math.sin(math.radians(h))
    pfeil(draw, aus[0], aus[1], x1, y1, ROT, 2)
    gestrichelt(draw, aus[0], aus[1], aus[0] + 130 * math.cos(math.radians(h)), aus[1] - 130 * math.sin(math.radians(h)), DUENN)
    bogen(draw, aus[0], aus[1], 60, -h, h, GUT, 1)
    text(draw, aus[0] + 64, aus[1] - 6, "δ = 21,8°", 11, GUT)
    text(draw, x0 - 4, y0 - 14, "Sonnenlicht", 9, GELB)
    text(draw, 20, 238, "δ_min = 2·arcsin(n·sin 30°) − 60°,  n = 1,31", 10, TEXT)
    text(draw, 20, 256, "Ring 22° um die Sonne, innen rot", 10, GUT)
    text(draw, 20, 272, "Cirrostratus: Warmfront in 12-24 h", 9, DUENN)
    sichern(bild, "skizze-halo")


def wachstum():
    bild, draw = leinwand()
    ax, ay = 70, 262
    achsen(draw, ax, ay, 420, 30, "Zeit (min)", "Radius (log)")
    def ty(r): return ay - (math.log10(r) + 6) / 3.0 * 215
    def tx(t): return ax + t / 40.0 * 330
    for r, name in ((1e-6, "1 μm"), (1e-5, "10 μm"), (1e-4, "0,1 mm"), (1e-3, "1 mm")):
        gestrichelt(draw, ax, ty(r), 420, ty(r), DUENN)
        text(draw, ax - 4, ty(r) - 6, name, 9, DUENN, rechts=True)
    for t in (0, 10, 20, 30, 40):
        text(draw, tx(t), ay + 6, "%d" % t, 9, DUENN, mitte=True)
    xiS = 6e-13 * 0.5
    dif = [(tx(t), ty(math.sqrt(1e-12 + 2 * xiS * t * 60))) for t in range(0, 41)]
    linie(draw, dif, BETONT, 2)
    text(draw, tx(22), ty(2.2e-5) - 2, "Diffusion ~ √t", 10, BETONT)
    r0 = 2.5e-5
    k = 1.0 / (r0 * 18 * 60)
    koa = []
    for t in range(0, 41):
        tt = max(0, t - 14) * 60
        nen = 1.0 / r0 - k * tt
        r = 1.0 / nen if nen > 1e3 else 1e-3
        koa.append((tx(t), ty(min(1e-3, max(r0, r)))))
    linie(draw, koa, GUT, 2)
    text(draw, tx(26), ty(2.5e-4), "Koaleszenz ~ r⁴", 10, GUT)
    text(draw, tx(2), ty(5e-4) - 6, "Regen", 9, DUENN)
    text(draw, tx(2), ty(1.5e-5) + 6, "Wolkentropfen", 9, DUENN)
    sichern(bild, "skizze-wachstum")


def fronten():
    bild, draw = leinwand()
    ay = 230
    strich(draw, 20, ay, 420, ay, LINIE, 2)
    flaeche(draw, [(20, ay), (200, ay), (20, ay - 70)], (36, 50, 80))
    linie(draw, [(200, ay), (20, ay - 70)], ROT, 2)
    flaeche(draw, [(330, ay), (420, ay), (420, ay - 120), (360, ay - 60)], (36, 50, 80))
    linie(draw, [(330, ay), (360, ay - 60), (420, ay - 120)], BETONT, 2)
    text(draw, 30, ay + 6, "kalt", 10, BETONT)
    text(draw, 265, ay + 6, "Warmsektor", 10, ROT, mitte=True)
    text(draw, 410, ay + 6, "kalt", 10, BETONT, rechts=True)
    text(draw, 200, ay + 6, "Warmfront", 9, ROT, mitte=True)
    text(draw, 330, ay + 6, "Kaltfront", 9, BETONT, mitte=True)
    for x, w, h, name in ((40, 50, 8, "Cirrus"), (100, 60, 14, "Altostratus"), (165, 70, 24, "Nimbostratus")):
        yk = ay - 70 * (200 - x) / 180.0 - 10 - h
        wolke(draw, x + w / 2, yk, w, h)
        text(draw, x + w / 2, yk - h - 14, name, 8, DUENN, mitte=True)
    for i in range(5):
        gestrichelt(draw, 150 + i * 10, ay - 40, 146 + i * 10, ay - 4, BETONT, 1, 4)
    wolke(draw, 318, ay - 70, 30, 40)
    kreis(draw, 318, ay - 120, 20, WOLKE)
    flaeche(draw, [(300, ay - 130), (360, ay - 130), (355, ay - 122), (305, ay - 122)], WOLKE)
    text(draw, 360, ay - 150, "Cumulonimbus", 8, DUENN)
    text(draw, 20, 30, "Warmfront: Rampe 1:100-1:300, Dauerregen", 10, TEXT)
    text(draw, 20, 46, "Kaltfront: Keil 1:50-1:100, Schauer", 10, TEXT)
    pfeil(draw, 230, 70, 300, 70, DUENN, 1)
    text(draw, 306, 64, "Zugrichtung", 9, DUENN)
    text(draw, 20, 262, "tan α = (f·T/g) · Δu/ΔT   (Margules)", 10, TEXT)
    sichern(bild, "skizze-fronten")


def seewind():
    bild, draw = leinwand()
    ay = 220
    draw.rectangle([20 * S, ay * S, 200 * S, (ay + 30) * S], fill=(30, 60, 110))
    draw.rectangle([200 * S, ay * S, 420 * S, (ay + 30) * S], fill=(70, 60, 44))
    text(draw, 110, ay + 8, "See (kühl)", 10, TEXT, mitte=True)
    text(draw, 310, ay + 8, "Land (warm)", 10, TEXT, mitte=True)
    pfeil(draw, 60, ay - 14, 330, ay - 14, GUT, 3)
    text(draw, 195, ay - 34, "Seewind", 11, GUT, mitte=True)
    pfeil(draw, 340, ay - 20, 340, 80, WARN, 2)
    text(draw, 348, 140, "warm, steigt", 9, WARN)
    pfeil(draw, 330, 70, 70, 70, BETONT, 2)
    text(draw, 200, 52, "Rückstrom oben", 9, BETONT, mitte=True)
    pfeil(draw, 60, 80, 60, ay - 24, DUENN, 2)
    text(draw, 66, 140, "sinkt", 9, DUENN)
    for i in range(3):
        wolke(draw, 250 + i * 50, 126, 40, 16)
    text(draw, 250, 90, "Cumulus an der Seewindfront", 8, DUENN)
    text(draw, 20, 262, "Druck oben über Land höher (warme Säule dicker) → Zirkulation", 9, TEXT)
    text(draw, 20, 276, "dC/dt = −∮dp/ρ: Solenoide aus Isobaren und Isosteren", 9, TEXT)
    sichern(bild, "skizze-seewind")


def foehn():
    bild, draw = leinwand()
    ay = 250
    def zy(z): return ay - z / 3500.0 * 190
    berg = [(20, zy(500)), (120, zy(1200)), (200, zy(3000)), (260, zy(2600)), (330, zy(1500)), (420, zy(500))]
    flaeche(draw, [(20, ay)] + berg + [(420, ay)], (40, 44, 52))
    linie(draw, berg, LINIE, 2)
    pfad = [(30, zy(500)), (110, zy(1500)), (195, zy(3100)), (260, zy(2700)), (335, zy(1600)), (410, zy(500))]
    linie(draw, pfad[:3], GUT, 2)
    linie(draw, pfad[2:], ROT, 2)
    pfeil(draw, pfad[4][0], pfad[4][1], pfad[5][0], pfad[5][1], ROT, 2)
    for (x, y) in pfad[:3]:
        kreis(draw, x, y, 3, KOERPER)
    text(draw, 34, zy(500) - 26, "20 °C, 500 m", 10, GUT)
    text(draw, 34, zy(500) - 14, "T_d 12 °C", 8, DUENN)
    text(draw, 24, zy(1500) - 24, "LCL 1500 m", 9, GUT)
    text(draw, 24, zy(1500) - 12, "10 °C", 9, GUT)
    text(draw, 195, zy(3000) - 24, "Kamm 3000 m, 1 °C", 9, TEXT, mitte=True)
    text(draw, 300, zy(500) - 26, "25,7 °C", 11, ROT)
    text(draw, 300, zy(500) - 12, "500 m, 27 %", 8, DUENN)
    wolke(draw, 150, zy(2300), 90, 26)
    for i in range(6):
        gestrichelt(draw, 118 + i * 12, zy(2100), 114 + i * 12, zy(1500) + 10, BETONT, 1, 4)
    text(draw, 196, zy(1900), "Stau", 8, BETONT)
    text(draw, 60, 30, "Luv", 11, DUENN)
    text(draw, 380, 30, "Lee", 11, DUENN)
    text(draw, 60, 46, "feucht hinauf: 6 K/km", 9, GUT)
    text(draw, 380, 46, "trocken hinunter: 9,8 K/km", 9, ROT, rechts=True)
    text(draw, 20, 268, "Föhn: 5,7 K wärmer auf gleicher Höhe — die Kondensationswärme des Regens im Luv", 9, TEXT)
    sichern(bild, "skizze-foehn")


# Englische Fassungen ganzer Beschriftungen (die Worttafel oben reicht fuer
# zusammengesetzte Saetze nicht).
EN.update({
    "0,1 μm": "0.1 μm", "1 μm": "1 μm", "10 μm": "10 μm", "10 nm": "10 nm",
    "0,1 mm": "0.1 mm", "1 mm": "1 mm",
    "10⁹ Punkte × 2000 Schritte für zehn Tage": "10⁹ points × 2000 steps for ten days",
    "45°: 1,03·10⁻⁴ /s": "45°: 1.03·10⁻⁴ /s",
    "50 Mitglieder, gestörter Start": "50 members, perturbed start",
    "7 Gleichungen, 7 Unbekannte (u, v, w, p, ρ, T, q)": "7 equations, 7 unknowns (u, v, w, p, ρ, T, q)",
    "Arbeit gegen den Außendruck": "work against the outside pressure",
    "Breitengrad →  Hadley endet bei 30°: Drehimpuls": "latitude →  Hadley ends at 30°: angular momentum",
    "Cirrostratus: Warmfront in 12-24 h": "cirrostratus: warm front in 12-24 h",
    "D = π·√(2K/f) ≈ 1400 m     Bodenwind konvergiert ins Tief": "D = π·√(2K/f) ≈ 1400 m     surface wind converges into the low",
    "Diffusion ~ √t": "diffusion ~ √t", "Druck (hPa)": "pressure (hPa)", "hPa": "hPa",
    "Druck oben über Land höher (warme Säule dicker) → Zirkulation": "pressure aloft higher over land (warm column thicker) → circulation",
    "Druckflächen neigen sich zur kalten Seite": "pressure surfaces tilt toward the cold side",
    "Dunst: stabil": "haze: stable",
    "Erde: 255 K von außen, 288 K am Boden": "Earth: 255 K from outside, 288 K at the ground",
    "Fehlerverdopplung alle 2 Tage → Grenze bei zwei Wochen": "error doubling every 2 days → limit at two weeks",
    "Föhn: 5,7 K wärmer auf gleicher Höhe — die Kondensationswärme des Regens im Luv": "foehn: 5.7 K warmer at the same height — the condensation heat of the windward rain",
    "Gitterzelle Δx = 10 km, Werte nur im Punkt": "grid cell Δx = 10 km, values only at the point",
    "Gleichgewicht:": "balance:", "Grundstrom U →": "mean flow U →",
    "H = R·T/g ≈ 7,5 km": "H = R·T/g ≈ 7.5 km", "Höhe (km)": "height (km)",
    "Höhentrog westlich": "upper trough west", "des Bodentiefs": "of the surface low",
    "Kaltfront: Keil 1:50-1:100, Schauer": "cold front: wedge 1:50-1:100, showers",
    "Koaleszenz ~ r⁴": "coalescence ~ r⁴", "Land (warm)": "land (warm)",
    "Mie: alle Farben gleich": "Mie: all colours alike", "Nord ↑": "north ↑",
    "Norwegisches Modell: Welle auf der Polarfront": "Norwegian model: wave on the polar front",
    "Pol: 1,46·10⁻⁴ /s": "pole: 1.46·10⁻⁴ /s", "Radius (log)": "radius (log)",
    "Rayleigh: ~ 1/λ⁴": "Rayleigh: ~ 1/λ⁴",
    "Schicht  T_a  (schwarz im Infrarot, durchsichtig für Licht)": "layer  T_a  (black in the infrared, transparent to light)",
    "See (kühl)": "sea (cool)", "Sonne: S₀ = 1361 W/m²": "sun: S₀ = 1361 W/m²",
    "Spreizung schließt sich mit 8 K/km": "spread closes at 8 K/km",
    "Streuung wächst": "spread grows", "exponentiell": "exponentially",
    "T_s = 2^(1/4)·T_a = 303 K": "T_s = 2^(1/4)·T_a = 303 K",
    "Teilchen < λ/10": "particles < λ/10", "Teilchen > λ": "particles > λ",
    "Temperatur (°C)": "temperature (°C)", "Tief links (Nordhalbkugel)": "low on the left (northern hemisphere)",
    "Tröpfchen 10 μm": "droplet 10 μm",
    "Warmfront: Rampe 1:100-1:300, Dauerregen": "warm front: ramp 1:100-1:300, steady rain",
    "Zeit (min)": "time (min)",
    "absorbiert: S₀(1−A)/4 = 238 W/m² = σ·T⁴  →  T = 255 K": "absorbed: S₀(1−A)/4 = 238 W/m² = σ·T⁴  →  T = 255 K",
    "aktiviert: wächst": "activated: grows", "am Boden: 45° zum Tief": "at the ground: 45° toward the low",
    "auf der Scheibe: nach rechts abgelenkt": "on the disc: deflected to the right",
    "auf die Scheibe π·R²": "onto the disc π·R²", "c·Δt < Δx": "c·Δt < Δx",
    "dC/dt = −∮dp/ρ: Solenoide aus Isobaren und Isosteren": "dC/dt = −∮dp/ρ: solenoids of isobars and isosteres",
    "de = Ω×e dt": "de = Ω×e dt", "e = e_s(T_d), 54 %": "e = e_s(T_d), 54 %", "e_s (hPa)": "e_s (hPa)",
    "f = 2 Ω sin φ": "f = 2 Ω sin φ", "f größer, ζ kleiner": "f larger, ζ smaller", "f kleiner, ζ größer": "f smaller, ζ larger",
    "feucht hinauf: 6 K/km": "moist up: 6 K/km", "gerade (von außen)": "straight (from outside)",
    "i = 59,5°, r = 40,3°, δ = 138°  →  Bogen bei 42°": "i = 59.5°, r = 40.3°, δ = 138°  →  bow at 42°",
    "immer stärker mit der Höhe": "ever more steeply with height", "j (Nord)": "j (north)", "k (oben)": "k (up)",
    "keine Wärme tauscht,": "exchanges no heat,",
    "kälter als die Umgebung: sinkt zurück": "colder than the surroundings: sinks back",
    "lang: steht oder läuft rückwärts  —  kurz: zieht nach Osten": "long: stands or runs backward  —  short: moves east",
    "ln p  (Höhe)": "ln p  (height)",
    "oben: σT_a⁴ = F     Boden: σT_s⁴ = F + σT_a⁴ = 2σT_a⁴": "top: σT_a⁴ = F     ground: σT_s⁴ = F + σT_a⁴ = 2σT_a⁴",
    "p(z)·A": "p(z)·A", "p(z+dz)·A": "p(z+dz)·A", "p₀": "p₀", "reflektiert: A = 0,3": "reflected: A = 0.3",
    "rot außen (n = 1,331: 42,4°), blau innen (1,343: 40,6°)": "red outside (n = 1.331: 42.4°), blue inside (1.343: 40.6°)",
    "sin α": "sin α", "tan α = (f·T/g) · Δu/ΔT   (Margules)": "tan α = (f·T/g) · Δu/ΔT   (Margules)",
    "trocken hinunter: 9,8 K/km": "dry down: 9.8 K/km", "und Senkrechter: 90° − φ": "and vertical: 90° − φ",
    "v_g = (1/ρf) · ∂p/∂n": "v_g = (1/ρf) · ∂p/∂n",
    "von außen gesehen: Kreisbahn der Spitze": "seen from outside: the tip moves on a circle",
    "e ruht im rotierenden System;": "e is at rest in the rotating frame;",
    "weiß, vorwärts gestreut": "white, scattered forward", "wächst mit der Höhe": "grows with height",
    "wärmer als die Umgebung: steigt weiter": "warmer than the surroundings: keeps rising",
    "z = 125 m/K × (T − T_d)": "z = 125 m/K × (T − T_d)", "Äquator: 0": "equator: 0",
    "Übersättigung (%)": "supersaturation (%)", "über 4π·R²": "over 4π·R²", "Γ = g / c_p": "Γ = g / c_p",
    "Ω": "Ω", "Ω = Ω (0, cos φ, sin φ)": "Ω = Ω (0, cos φ, sin φ)", "Ω cos φ  entlang j": "Ω cos φ  along j",
    "Ω sin φ  entlang k": "Ω sin φ  along k", "Ω  Erdachse": "Ω  Earth's axis", "α": "α",
    "δ = 180° + 2i − 4r,  Minimum bei cos i = √((n²−1)/3)": "δ = 180° + 2i − 4r,  minimum at cos i = √((n²−1)/3)",
    "δ = 21,8°": "δ = 21.8°", "δ_min = 2·arcsin(n·sin 30°) − 60°,  n = 1,31": "δ_min = 2·arcsin(n·sin 30°) − 60°,  n = 1.31",
    "ζ + f erhalten:  c = U − β/k²": "ζ + f conserved:  c = U − β/k²", "θ = 309 K": "θ = 309 K", "θ: + 3,3 K/km": "θ: + 3.3 K/km",
    "ρ·g·A·dz": "ρ·g·A·dz", "σT_a⁴": "σT_a⁴", "σT_s⁴": "σT_s⁴", "φ": "φ", "e": "e", "i": "i",
    "∂v_g/∂ln p = −(R/f) k×∇T   —   kalt zur Linken": "∂v_g/∂ln p = −(R/f) k×∇T   —   cold on the left",
    "kritisch: 0.12 % bei 0.65 μm": "critical: 0.12 % at 0.65 μm",
    "Umgebung 6,5 K/km": "environment 6.5 K/km", "Adiabate 9,8 K/km": "adiabat 9.8 K/km",
    "15 °C, 1000 hPa": "15 °C, 1000 hPa", "500 hPa": "500 hPa", "−18 °C": "−18 °C",
    "Paket in Ruhe": "parcel at rest", "Paket, gehoben": "parcel, lifted", "neutral = Adiabate": "neutral = adiabat",
    "Luftpaket": "air parcel", "steigt, dehnt sich aus, kühlt ab": "rises, expands, cools",
    "−9,8 K je km": "−9.8 K per km", "Tropopause −56,5 °C": "tropopause −56.5 °C",
    "T = 15 °C − 6,5 K/km · z": "T = 15 °C − 6.5 K/km · z", "Standardatmosphäre": "standard atmosphere",
    "LCL 1500 m": "LCL 1500 m", "Wolkenbasis": "cloud base", "Feuchtadiabate −6 K/km": "moist adiabat −6 K/km",
    "T = 24 °C": "T = 24 °C", "T_d = 12 °C": "T_d = 12 °C", "−9,8 K/km": "−9.8 K/km", "−1,8 K/km": "−1.8 K/km",
    "Trockenadiabate bis LCL, dann Feuchtadiabate": "dry adiabat to the LCL, then moist adiabat",
    "Sättigungsdampfdruck": "saturation vapour pressure", "Verdopplung je 10 K": "doubling every 10 K",
    "T = 25 °C": "T = 25 °C", "Taupunkt 15 °C": "dew point 15 °C",
    "Sonne F": "sun F", "Gegenstrahlung": "back radiation", "Boden  T_s": "ground  T_s",
    "Minimum vor Sonnenaufgang": "minimum before sunrise", "Tau, Nebel": "dew, fog", "Maximum 15 Uhr": "maximum at 15:00",
    "−60 W/m²": "−60 W/m²", "Nettostrahlung": "net radiation",
    "Die Bilanz, nicht die Einstrahlung, bestimmt die Temperatur": "the budget, not the insolation, sets the temperature",
    "Kelvin (reines Wasser)": "Kelvin (pure water)", "Köhler (Salzkern)": "Köhler (salt nucleus)",
    "Sättigung 100 %": "saturation 100 %", "Regen": "rain", "Wolkentropfen": "cloud drops",
    "Wind  v_g": "wind  v_g", "Druckgradientkraft": "pressure gradient force", "Coriolis  −f k×v": "Coriolis  −f k×v",
    "Wind parallel zu den Isobaren,": "wind parallel to the isobars,", "Isobaren": "isobars",
    "Wind in die Bildebene": "wind into the page", "1000 hPa": "1000 hPa",
    "geostrophischer Wind": "geostrophic wind", "Ekman-Spirale": "Ekman spiral", "45°": "45°", "zum Tief": "toward the low",
    "Polarfront, Jet": "polar front, jet", "Subtropenhoch": "subtropical high",
    "U nach Osten": "U eastward", "Phase nach Westen": "phase westward",
    "Zugrichtung": "direction of travel", "Warmsektor": "warm sector",
    "Trogachse 500 hPa": "trough axis 500 hPa", "Wind gegen den": "wind anti-", "Uhrzeigersinn": "clockwise",
    "20 °C, 500 m": "20 °C, 500 m", "T_d 12 °C": "T_d 12 °C", "10 °C": "10 °C", "Kamm 3000 m, 1 °C": "crest 3000 m, 1 °C",
    "25,7 °C": "25.7 °C", "500 m, 27 %": "500 m, 27 %", "Stau": "orographic rain",
    "warm, steigt": "warm, rises", "sinkt": "sinks", "Rückstrom oben": "return flow aloft",
    "Cumulus an der Seewindfront": "cumulus along the sea-breeze front",
    "blau stark, rot schwach": "blue strong, red weak", "Molekül": "molecule",
    "Tropfen": "drop", "Beobachter": "observer", "zum Sonnengegenpunkt": "toward the antisolar point", "42°": "42°",
    "Eisprisma, Sechseck": "ice prism, hexagon", "Ring 22° um die Sonne, innen rot": "ring 22° around the sun, red inside",
    "Cumulus 1 km": "cumulus 1 km", "parametrisiert": "parametrised",
    "Mittel": "mean", "Vorhersage": "forecast", "Tage": "days",
    "je Skalenhöhe auf 1/e": "to 1/e per scale height", "Luftsäule": "column of air", "dz": "dz",
    "Infrarot ins All": "infrared to space", "Erde": "Earth", "All": "space", "Nacht": "night", "Tag": "day",
    "Thermosphäre": "thermosphere", "Mesosphäre": "mesosphere", "Stratosphäre": "stratosphere", "Troposphäre": "troposphere",
    "Ozon heizt": "ozone heats", "von unten geheizt": "heated from below",
    "Tropopause": "tropopause", "Stratopause": "stratopause", "Mesopause": "mesopause",
    "Höhe": "height", "Temperatur": "temperature", "Boden": "ground", "Druck": "pressure",
})

# ===========================================================================

# ===========================================================================
#  Wolken lesen: die Wolke als Messgerät
# ===========================================================================

EN.update({
    "Drei Messungen am Himmel": "Three measurements in the sky",
    "Kippen": "tilt", "Scherung": "shear", "Wellen": "waves",
    "Schichtung": "stratification", "Billows": "billows",
    "Turbulenz": "turbulence", "Gebirgskamm": "mountain ridge",
    "oben schnell": "fast above", "unten langsam": "slow below",
    "ΔU": "ΔU", "λ": "λ",
    "tan α = ΔU/w": "tan α = ΔU/w",
    "λ = 2π·U/N": "λ = 2π·U/N",
    "Ri = N²/(du/dz)² < 1/4": "Ri = N²/(du/dz)² < 1/4",
})


def wolkenlesen_sonde():
    """Drei Ablesungen: Kippen (Scherung), Wellenabstand (Schichtung),
    Billows (Turbulenzschwelle). Je Feld eine Zahl."""
    bild, draw = leinwand()
    text(draw, 220, 10, "Drei Messungen am Himmel", 12, TEXT, mitte=True)
    for x in (148, 292):
        gestrichelt(draw, x, 30, x, 262, DUENN, 1, 8)

    # --- 1  Kippen misst die Scherung ---------------------------------------
    text(draw, 79, 34, "Kippen", 11, BETONT, mitte=True)
    text(draw, 79, 48, "Scherung", 9, DUENN, mitte=True)
    bx, by = 40, 216
    gestrichelt(draw, bx, by, bx, 84, DUENN)
    strich(draw, bx - 18, by, bx + 18, by, DUENN, 1)
    text(draw, bx, by + 6, "Wolkenbasis", 9, DUENN, mitte=True)
    for i in range(8):
        a = i / 7.0
        kreis(draw, bx + 56 * a * a, by - 126 * a, 8 + 4 * a, WOLKE)
    linie(draw, [(bx + 56 * (i / 12.0) ** 2, by - 126 * i / 12.0)
                 for i in range(13)], BETONT, 1)
    bogen(draw, bx, by, 46, -90, -40, DUENN, 1)
    text(draw, bx + 22, by - 44, "α", 11, DUENN)
    pfeil(draw, bx - 22, by - 24, bx - 22, by - 86, GUT, 2, 5)
    text(draw, bx - 26, by - 62, "w", 10, GUT, rechts=True)
    pfeil(draw, bx + 66, 92, bx + 104, 92, WARN, 2, 5)
    text(draw, bx + 85, 74, "ΔU", 10, WARN, mitte=True)
    text(draw, 79, 250, "tan α = ΔU/w", 10, TEXT, mitte=True)

    # --- 2  Der Wellenabstand misst die Schichtung --------------------------
    text(draw, 220, 34, "Wellen", 11, BETONT, mitte=True)
    text(draw, 220, 48, "Schichtung", 9, DUENN, mitte=True)
    flaeche(draw, [(156, 216), (176, 176), (196, 216)], (62, 70, 84))
    strich(draw, 152, 216, 288, 216, DUENN, 1)
    text(draw, 176, 224, "Gebirgskamm", 9, DUENN, mitte=True)
    pfeil(draw, 152, 158, 174, 158, WARN, 2, 5)
    text(draw, 178, 150, "U", 10, WARN)
    lam = 36.0
    linie(draw, [(176 + i, 132 - 14 * math.cos(2 * math.pi * i / lam))
                 for i in range(0, 95)], DUENN, 1)
    for k in (1, 2):
        cx = 176 + lam * k
        for j in range(5):
            kreis(draw, cx - 14 + j * 7, 118 + abs(j - 2) * 1.6,
                  6.5 - abs(j - 2) * 1.3, WOLKE)
    pfeil(draw, 176 + lam, 96, 176 + 2 * lam, 96, BETONT, 1, 5)
    pfeil(draw, 176 + 2 * lam, 96, 176 + lam, 96, BETONT, 1, 5)
    text(draw, 176 + 1.5 * lam, 80, "λ", 10, BETONT, mitte=True)
    text(draw, 220, 250, "λ = 2π·U/N", 10, TEXT, mitte=True)

    # --- 3  Billows messen die Turbulenzschwelle ----------------------------
    text(draw, 361, 34, "Billows", 11, BETONT, mitte=True)
    text(draw, 361, 48, "Turbulenz", 9, DUENN, mitte=True)
    gestrichelt(draw, 298, 172, 424, 172, DUENN)
    pfeil(draw, 304, 122, 416, 122, WARN, 2, 5)
    text(draw, 300, 102, "oben schnell", 9, WARN)
    pfeil(draw, 304, 206, 344, 206, WARN, 2, 5)
    text(draw, 300, 212, "unten langsam", 9, WARN)
    for k in range(5):
        cx = 310 + k * 26
        for j in range(7):
            a = -1.1 + j * 0.62
            kreis(draw, cx + 11 * math.sin(a) + j * 1.1,
                  172 - 11 * math.cos(a) - j * 0.9, 5.0, WOLKE)
    text(draw, 361, 250, "Ri = N²/(du/dz)² < 1/4", 9, TEXT, mitte=True)

    sichern(bild, "wolkenlesen-sonde")


ALLE = [schichtung, luftsaeule, standard, paket, theta, stabilitaet,
        dampfdruck, hebung, emagramm, bilanz, einschicht, tagesgang,
        koehler, wachstum, coriolis, breite, geostrophisch, thermisch, ekman,
        zellen, rossby, fronten, zyklone, foehn, seewind, streuung,
        regenbogen, halo, gitter, ensemble,
        wolkenlesen_sonde]


# ===========================================================================
# 5b  Das Wolkenbuch
# ===========================================================================

def wb_stockwerke():
    """Die drei Stockwerke, nach Breite gestaffelt -- weil die Tropopause
    nach Breite gestaffelt ist. Dazu, woran man das Stockwerk erkennt."""
    bild, draw = leinwand()
    ax, ay = 62, 252
    achsen(draw, ax, ay, 424, 30, "", "Höhe (km)")

    def zy(z):
        return ay - z / 18.0 * 212

    for z in (0, 5, 10, 15):
        gestrichelt(draw, ax, zy(z), 418, zy(z), DUENN, 1, 8)
        text(draw, ax - 5, zy(z) - 6, "%d" % z, 9, DUENN, rechts=True)

    # je Breite: tief, mittel, hoch als eigene Saeule, damit die amtliche
    # Ueberlappung von mittel und hoch nichts verdeckt
    FARBEN = ((76, 84, 100), (58, 96, 140), (120, 132, 158))
    gruppen = (("polar", 96, ((0, 2), (2, 4), (3, 8)), 8.0),
               ("gemäßigt", 206, ((0, 2), (2, 7), (5, 13)), 11.0),
               ("tropisch", 316, ((0, 2), (2, 8), (6, 18)), 17.0))
    tropo = []
    for name, x0, baender, zt in gruppen:
        for i, (unten, oben) in enumerate(baender):
            x = x0 + i * 26
            draw.rectangle([x * S, zy(oben) * S, (x + 20) * S, zy(unten) * S],
                           fill=FARBEN[i])
            text(draw, x + 10, zy(oben) - 12, "%d" % oben, 8, DUENN, mitte=True)
        text(draw, x0 + 36, ay + 6, name, 10, TEXT, mitte=True)
        tropo.append((x0 - 6, zy(zt)))
        tropo.append((x0 + 78, zy(zt)))
    linie(draw, tropo, WARN, 1)
    text(draw, 68, zy(8.0) - 19, "Tropopause", 9, WARN)

    # Legende, damit die drei Baender nicht im Balken beschriftet werden
    for i, name in enumerate(("tief", "mittel", "hoch")):
        x = 92 + i * 78
        draw.rectangle([x * S, 42 * S, (x + 14) * S, 52 * S], fill=FARBEN[i])
        text(draw, x + 19, 41, name, 9, TEXT)

    gestrichelt(draw, ax, zy(8.5), 418, zy(8.5), GUT, 1, 6)
    text(draw, 416, zy(8.5) - 15, "−40 °C: nur noch Eis", 9, GUT, rechts=True)
    text(draw, 240, 278, "scharfer Rand und Korona heißt Wasser, "
         "faserig und Halo heißt Eis", 9, TEXT, mitte=True)
    sichern(bild, "wolkenbuch-stockwerke")


def wb_sonderformen():
    """Drei Sonderformen als Schnitt: Amboss mit mammatus, pileus ueber
    dem steigenden Turm, virga unter der Basis."""
    bild, draw = leinwand()
    strich(draw, 14, 258, 426, 258, DUENN, 1)
    text(draw, 426, 262, "Boden", 9, DUENN, rechts=True)
    gestrichelt(draw, 14, 58, 426, 58, WARN, 1, 7)
    text(draw, 14, 42, "Tropopause", 9, WARN)

    # 1  Cumulonimbus: Amboss, ueberschiessende Kuppel, mammatus
    flaeche(draw, [(18, 88), (142, 88), (128, 60), (34, 60)], WOLKE)
    kreis(draw, 80, 54, 11, WOLKE)
    flaeche(draw, [(56, 258), (64, 90), (96, 90), (104, 258)], WOLKE)
    for x in (26, 40, 112, 126, 138):
        kreis(draw, x, 92, 5, (168, 174, 190))
    for i in range(4):
        gestrichelt(draw, 70 + i * 7, 180, 64 + i * 7, 256, DUENN, 1, 5)
    text(draw, 80, 68, "incus", 10, GRUND, mitte=True)
    text(draw, 80, 32, "Kuppel", 9, GUT, mitte=True)
    text(draw, 18, 104, "mammatus", 9, BETONT)
    text(draw, 80, 268, "Cumulonimbus", 9, TEXT, mitte=True)

    # 2  pileus ueber dem schnell steigenden Turm
    flaeche(draw, [(186, 258), (198, 152), (240, 152), (254, 258)], WOLKE)
    for x, y, r in ((202, 150, 10), (220, 144, 12), (236, 150, 9)):
        kreis(draw, x, y, r, WOLKE)
    draw.ellipse([178 * S, 124 * S, 262 * S, 136 * S], fill=(224, 230, 242))
    pfeil(draw, 220, 160, 220, 142, GUT, 2, 6)
    text(draw, 220, 94, "pileus", 10, GUT, mitte=True)
    text(draw, 220, 110, "am LCL der gehobenen Schicht", 8, DUENN,
         mitte=True)
    text(draw, 220, 268, "Cumulus congestus", 9, TEXT, mitte=True)

    # 3  virga: Fallstreifen, die in der Luft aufhoeren
    wolke(draw, 360, 150, 104, 26)
    for i in range(6):
        x = 318 + i * 17
        gestrichelt(draw, x, 152, x + 14, 196, BETONT, 1, 5)
    text(draw, 360, 206, "virga", 10, BETONT, mitte=True)
    text(draw, 360, 220, "rund 120 m, dann verdunstet", 8, DUENN, mitte=True)
    text(draw, 360, 268, "Altocumulus", 9, TEXT, mitte=True)
    text(draw, 220, 282, "Jede Sonderform ist ein Mechanismus", 9, TEXT,
         mitte=True)
    sichern(bild, "wolkenbuch-sonderformen")


def wb_kondensstreifen():
    """Die Mischungsgerade des Abgases an der Saettigungskurve: Beruehrung
    heisst Schwellentemperatur."""
    bild, draw = leinwand()
    ax, ay = 70, 250
    achsen(draw, ax, ay, 420, 34, "Temperatur (°C)", "e (Pa)")

    def tx(T):
        return ax + (T + 62) / 32.0 * 330

    def ey(e):
        return ay - e / 60.0 * 206

    def ew(T):
        return 611.2 * math.exp(17.62 * T / (243.12 + T))

    def ei(T):
        return 611.2 * math.exp(22.46 * T / (272.62 + T))

    for T in (-60, -50, -40, -30):
        gestrichelt(draw, tx(T), ay, tx(T), 36, DUENN, 1, 9)
        text(draw, tx(T), ay + 6, "%d" % T, 9, DUENN, mitte=True)
    linie(draw, [(tx(T / 2.0), ey(ew(T / 2.0))) for T in range(-124, -59)],
          WARN, 2)
    linie(draw, [(tx(T / 2.0), ey(ei(T / 2.0))) for T in range(-124, -59)],
          BETONT, 2)

    # Die Gerade, die die Kurve beruehrt: Steigung G, Fusspunkt trocken
    Gsa = 1.25 * 1004.0 * 25000.0 / (0.622 * 43.0e6 * 0.70)
    Tc = -41.73
    eC = ew(Tc)
    T0 = Tc - eC / Gsa
    linie(draw, [(tx(T0), ey(0)), (tx(-31.5), ey(eC + Gsa * (-31.5 - Tc)))],
          GUT, 2)
    kreis(draw, tx(Tc), ey(eC), 4, GUT)
    kreis(draw, tx(T0), ey(0), 3, GUT)
    # und eine, die sie nicht erreicht: zu warme Umgebung
    linie(draw, [(tx(-36.0), ey(0)), (tx(-31.0), ey(Gsa * 5.0))], ROT, 2)

    text(draw, 398, 60, "über Wasser", 9, WARN, rechts=True)
    text(draw, 398, 104, "über Eis", 9, BETONT, rechts=True)
    text(draw, tx(Tc) + 8, ey(eC) - 8, "Berührung: de_s/dT = G", 9, GUT)
    text(draw, tx(T0), 270, "trockene Umgebung", 8, DUENN, mitte=True)
    text(draw, 356, 226, "zu warm: kein Streifen", 8, ROT, rechts=True)
    text(draw, 100, 62, "Mischungsgerade, Steigung G = 1,68 Pa/K", 10, GUT)
    text(draw, 100, 78, "T_c = −41,7 °C, also 8,7 km", 10, TEXT)
    sichern(bild, "wolkenbuch-kondensstreifen")


EN.update({
    "Höhe (km)": "height (km)", "polar": "polar", "gemäßigt": "temperate",
    "tropisch": "tropical", "tief": "low", "mittel": "middle",
    "hoch": "high", "−40 °C: nur noch Eis": "−40 °C: ice only",
    "incus": "incus", "Kuppel": "overshooting top", "mammatus": "mammatus",
    "Cumulonimbus": "cumulonimbus", "pileus": "pileus",
    "am LCL der gehobenen Schicht": "at the LCL of the lifted layer",
    "Cumulus congestus": "cumulus congestus", "virga": "virga",
    "rund 120 m, dann verdunstet": "about 120 m, then evaporated",
    "Altocumulus": "altocumulus",
    "Jede Sonderform ist ein Mechanismus":
        "every supplementary feature is a mechanism",
    "über Wasser": "over water", "über Eis": "over ice",
    "Berührung: de_s/dT = G": "tangency: de_s/dT = G",
    "trockene Umgebung": "dry environment",
    "zu warm: kein Streifen": "too warm: no trail",
    "Mischungsgerade, Steigung G = 1,68 Pa/K":
        "mixing line, slope G = 1.68 Pa/K",
    "T_c = −41,7 °C, also 8,7 km": "T_c = −41.7 °C, hence 8.7 km",
    "e (Pa)": "e (Pa)",
    "scharfer Rand und Korona heißt Wasser, faserig und Halo heißt Eis":
        "a sharp edge and a corona mean water, fibres and a halo mean ice",
})

ALLE = ALLE + [wb_stockwerke, wb_sonderformen, wb_kondensstreifen]

# ===========================================================================
# Spuren am Boden, Den Himmel lesen, Selbst messen
# ===========================================================================

def bo_mischungsnebel():
    """Die Sehne zwischen zwei gesaettigten Paketen liegt ueber der Kurve."""
    bild, draw = leinwand()
    ax, ay = 76, 258
    achsen(draw, ax, ay, 420, 30, "Temperatur (°C)", "e (hPa)")
    def tx(T): return ax + (T + 5) / 32.0 * 330
    def ey(e): return ay - e / 27.0 * 215
    linie(draw, [(tx(T / 2.0), ey(e_s(T / 2.0))) for T in range(-10, 53)], WARN, 2)
    p0 = (tx(0), ey(e_s(0)))
    p2 = (tx(20), ey(e_s(20)))
    strich(draw, p0[0], p0[1], p2[0], p2[1], BETONT, 2)
    pm = (tx(10), ey((e_s(0) + e_s(20)) / 2.0))
    ps = (tx(10), ey(e_s(10)))
    kreis(draw, p0[0], p0[1], 4, GELB)
    kreis(draw, p2[0], p2[1], 4, GELB)
    kreis(draw, pm[0], pm[1], 4, BETONT)
    kreis(draw, ps[0], ps[1], 3, DUENN)
    pfeil(draw, pm[0], ps[1], pm[0], pm[1], ROT, 2, 6)
    gestrichelt(draw, ax, pm[1], pm[0], pm[1], DUENN)
    gestrichelt(draw, ax, ps[1], pm[0], ps[1], DUENN)
    for T in (0, 10, 20):
        text(draw, tx(T), ay + 6, "%d" % T, 9, DUENN, mitte=True)
    text(draw, p0[0] + 8, p0[1] - 2, "gesättigt, 0 °C", 9, GELB)
    text(draw, p2[0] - 10, p2[1] + 10, "gesättigt, 20 °C", 9, GELB, rechts=True)
    text(draw, pm[0] + 8, pm[1] - 14, "Mischung: 10 °C, 14,7 hPa", 9, BETONT)
    text(draw, ps[0] + 8, ps[1] + 4, "e_s (10 °C) = 12,3 hPa", 9, DUENN)
    text(draw, pm[0] + 10, (pm[1] + ps[1]) / 2 - 4, "Δe = 2,5 hPa", 9, ROT)
    text(draw, 150, 48, "Mischungsgerade über der Kurve", 11, BETONT)
    text(draw, 150, 64, "e_s ist konvex, die Sehne liegt darüber", 9, DUENN)
    text(draw, 150, 230, "120 % Feuchte, 1,5 g/kg Nebel", 11, GUT)
    sichern(bild, "boden-mischungsnebel")


def hi_luftmasse():
    """Weg des Sehstrahls durch die Luftsaeule: 1/sin h."""
    bild, draw = leinwand()
    bodeny, obenx = 258, 430
    deckel = 118
    x0 = 92
    flaeche(draw, [(60, deckel), (obenx, deckel), (obenx, bodeny), (60, bodeny)],
            (22, 30, 46))
    strich(draw, 54, bodeny, obenx, bodeny, LINIE, 2)
    gestrichelt(draw, 54, deckel, obenx, deckel, DUENN)
    text(draw, 58, bodeny + 6, "Boden", 9, DUENN)
    text(draw, 58, deckel - 14, "Luftsäule, 10 330 kg/m²", 9, DUENN)
    kreis(draw, x0, bodeny - 3, 4, KOERPER)
    text(draw, x0 - 6, bodeny - 20, "Auge", 9, TEXT, rechts=True)
    d = bodeny - deckel
    pfeil(draw, x0, bodeny, x0, deckel, GUT, 2, 6)
    text(draw, x0 + 6, deckel + 10, "Luftmasse 1", 10, GUT)
    for h, farbe in ((30.0, BETONT), (10.0, WARN)):
        dx = d / math.tan(math.radians(h))
        xe = min(obenx - 6, x0 + dx)
        ye = bodeny - (xe - x0) * math.tan(math.radians(h))
        pfeil(draw, x0, bodeny, xe, ye, farbe, 2, 6)
        text(draw, xe - 6, ye - 14, "1/sin h = %.0f" % (1.0 / math.sin(math.radians(h))),
             9, farbe, rechts=True)
    bogen(draw, x0, bodeny, 40, -32, 0, DUENN, 1)
    text(draw, x0 + 46, bodeny - 14, "h", 10, DUENN)
    text(draw, 150, 44, "Am Horizont: 38 Luftmassen", 11, ROT)
    text(draw, 150, 60, "die Krümmung begrenzt den Weg", 9, DUENN)
    text(draw, 120, 268, "Transmission: grün 2,5 %, rot 16 %", 10, TEXT)
    text(draw, 120, 283, "Verhältnis 6,4 — deshalb rot", 11, GELB)
    sichern(bild, "himmel-luftmasse")


def sb_stock():
    """Sonnenhoehe aus Stock und Schatten."""
    bild, draw = leinwand()
    bodeny = 250
    fuss = 150
    hoehe = 120
    h = 50.0
    laenge = hoehe / math.tan(math.radians(h))
    strich(draw, 40, bodeny, 420, bodeny, LINIE, 2)
    strich(draw, fuss, bodeny, fuss, bodeny - hoehe, KOERPER, 2)
    strich(draw, fuss, bodeny, fuss + laenge, bodeny, ROT, 2)
    for i in range(4):
        y = bodeny - hoehe + i * 26
        pfeil(draw, fuss - 86 + i * 6, y - 78, fuss - 6 + i * 6, y, GELB, 1, 5)
    strich(draw, fuss, bodeny - hoehe, fuss + laenge, bodeny, GELB, 1)
    bogen(draw, fuss + laenge, bodeny, 44, 180, 180 + h, DUENN, 1)
    text(draw, fuss + laenge - 50, bodeny - 26, "h = 50°", 10, DUENN)
    text(draw, fuss - 8, bodeny - hoehe / 2, "Stock L", 10, KOERPER, rechts=True)
    text(draw, fuss + laenge / 2, bodeny + 6, "Schatten S", 10, ROT, mitte=True)
    text(draw, fuss - 108, bodeny - hoehe - 84, "Sonne", 10, GELB)
    text(draw, 240, 60, "tan h = L / S", 13, GUT)
    text(draw, 240, 84, "1,20 m / 1,00 m → h = 50°", 9, DUENN)
    text(draw, 240, 112, "S = S₀ · sin h · τ", 12, TEXT)
    text(draw, 240, 134, "60°, τ = 0,75: 884 W/m²", 9, GELB)
    text(draw, 240, 148, "19°, τ = 0,6: 263 W/m²", 9, BETONT)
    text(draw, 40, 284, "Mittagshöhe und Datum geben die Breite", 9, DUENN)
    sichern(bild, "selbstmessen-stock")


EN.update({
    "e (hPa)": "e (hPa)",
    "gesättigt, 0 °C": "saturated, 0 °C",
    "gesättigt, 20 °C": "saturated, 20 °C",
    "Mischung: 10 °C, 14,7 hPa": "mixture: 10 °C, 14.7 hPa",
    "e_s (10 °C) = 12,3 hPa": "e_s (10 °C) = 12.3 hPa",
    "Δe = 2,5 hPa": "Δe = 2.5 hPa",
    "Mischungsgerade über der Kurve": "the mixing line lies above the curve",
    "e_s ist konvex, die Sehne liegt darüber":
        "e_s is convex, so the chord lies above it",
    "120 % Feuchte, 1,5 g/kg Nebel": "120 % humidity, 1.5 g/kg of fog",
    "Luftsäule, 10 330 kg/m²": "column of air, 10 330 kg/m²",
    "Auge": "eye",
    "Luftmasse 1": "air mass 1",
    "1/sin h = 2": "1/sin h = 2",
    "1/sin h = 6": "1/sin h = 6",
    "h": "h",
    "Am Horizont: 38 Luftmassen": "at the horizon: 38 air masses",
    "die Krümmung begrenzt den Weg": "curvature limits the path",
    "Transmission: grün 2,5 %, rot 16 %": "transmission: green 2.5 %, red 16 %",
    "Verhältnis 6,4 — deshalb rot": "ratio 6.4 — hence red",
    "Stock L": "stick L",
    "Schatten S": "shadow S",
    "Sonne": "sun",
    "h = 50°": "h = 50°",
    "tan h = L / S": "tan h = L / S",
    "1,20 m / 1,00 m → h = 50°": "1.20 m / 1.00 m → h = 50°",
    "S = S₀ · sin h · τ": "S = S₀ · sin h · τ",
    "60°, τ = 0,75: 884 W/m²": "60°, τ = 0.75: 884 W/m²",
    "19°, τ = 0,6: 263 W/m²": "19°, τ = 0.6: 263 W/m²",
    "Mittagshöhe und Datum geben die Breite":
        "noon elevation and date give the latitude",
})

ALLE = ALLE + [bo_mischungsnebel, hi_luftmasse, sb_stock]


def main():
    global SPRACHE
    for SPRACHE in ("de", "en"):
        print("Skizzen (%s):" % SPRACHE)
        for f in ALLE:
            f()
        if SPRACHE == "de":
            fehlt = pruefen()
            if fehlt:
                print("Ohne englische Beschriftung:", file=sys.stderr)
                for s in fehlt:
                    print("   " + s, file=sys.stderr)
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
