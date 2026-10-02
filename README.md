# Meteorologie

Meteorologie für Physiker, deutsch oder englisch, auf dem Nokia N9 und N950
(MeeGo 1.2 Harmattan) und auf Sailfish OS.

Der Leser kann Thermodynamik, Mechanik und Elektrodynamik und braucht sie
**angewandt**: auf eine Luftsäule von zehn Kilometern auf einer rotierenden
Kugel mit Wasser darin. Elf Kapitel, 30 Lektionen, 71 Aufgaben:

1. Die Atmosphäre als Gas — Zusammensetzung, Hydrostatik, Skalenhöhe,
   Standardatmosphäre und Höhenmesser
2. Thermodynamik trockener Luft — Trockenadiabate, potentielle Temperatur,
   Brunt-Väisälä-Frequenz
3. Feuchte Luft — Clausius-Clapeyron, Kondensationsniveau, Feuchtadiabate,
   Emagramm und CAPE
4. Strahlung — Strahlungsgleichgewicht, Einschichtmodell des Treibhauses,
   Tagesgang am Boden
5. Wolken und Niederschlag — Kelvin, Köhler, Diffusionswachstum,
   Bergeron-Findeisen, Koaleszenz, die zehn Gattungen
6. Dynamik — die Coriolis-Kraft hergeleitet (samt der Ableitung der
   Einheitsvektoren), geostrophischer Wind, Gradientwind, thermischer Wind,
   Ekman-Spirale
7. Zirkulation — Hadley-Zelle und Drehimpuls, Rossby-Wellen
8. Synoptik — Margules, Zyklogenese und barokline Instabilität
9. Mesoskala — Föhn (durchgerechnet), Seewind und Zirkulationssatz, Gewitter
10. Optik — Rayleigh und Koschmieder, Regenbogen (Descartes) und Halo
11. Vorhersage — CFL-Bedingung, Lorenz und Ensembles

**Jede Formel wird hergeleitet**, mit Formelzeichen, Gültigkeitsgrenze und
Zahlenbeispiel; jede Zahlenaufgabe rechnet ihren Wert aus denselben
Konstanten, die die Lektion lehrt. Die Herleitungen hängen am Lektionstext,
die Formeln sind gesetzt (LaTeX über matplotlib.mathtext), auch im
Fließtext.

## Bilder

Alle 30 Skizzen sind gezeichnet (`tools/skizzen.py`, Pillow): Luftsäule,
Emagramm, Köhler-Kurve, rotierendes Bezugssystem, Kräftegleichgewicht,
Hadley-Zellen, Frontquerschnitt, Zyklone, Föhn, Strahlengang im Tropfen und
im Eisprisma. Die Beschriftung steckt im Bild, deshalb gibt es jede zweimal
(`<name>.png`, `<name>.en.png`). Die Wolkenbilder stammen aus
[segelflug](https://github.com/smatkovi/segelflug) (`tools/clouds.py`).

## Wie das gebaut ist

Das Programm ist [C-Lehrer](https://github.com/smatkovi/c-lehrer)
beziehungsweise dessen Sailfish-Fassung
[harbour-lehrer](https://github.com/smatkovi/harbour-lehrer): Die App liest
ihren ganzen Kurs aus `data/kurs.json` und weiß nichts vom Fach.

```
kurs.py               Kapitel, Lektionen, Aufgaben, zweisprachig
herleitungen.py       die Herleitung jeder Formel, je Lektion
kursformeln.py        Formelkästen: Textzeile, TeX, Zeichen, Erklärung
tools/make-kurs.py    schreibt data/kurs.json, mischt die Antworten
tools/formeln.py      setzt alle $...$-Formeln als PNG (matplotlib, Baurechner)
tools/skizzen.py      zeichnet bilder/skizze-*.png
tools/icon.py         das Squircle-Icon
tools/build-deb.sh    packt das Harmattan-.deb
```

Formeln im Text stehen als `$...$` (in der Zeile) oder `$$...$$` (als
Absatz); `make-kurs.py` ersetzt sie durch Marker auf die gesetzten Bilder,
die die Oberfläche als `<img>` in den Rich Text setzt. Je Formel liegen eine
helle und eine dunkle Fassung bei; Harmattan braucht nur die helle.

## Bauen

```sh
python3 tools/skizzen.py         # Skizzen zeichnen
python3 tools/formeln.py         # Formeln setzen (braucht matplotlib)
python3 tools/make-kurs.py       # data/kurs.json erzeugen
tools/build-deb.sh 1.0           # braucht ~/ps/c-lehrer/build/c-lehrer
```

Die Sailfish-RPMs entstehen im Baum von `harbour-lehrer`
(`cmake -DKURS=meteorologie`), wo `kurs.json` und die Bilder als
`kurse/meteorologie/` liegen.

## Installieren

* **N9 / N950:** `aegis-dpkg -i meteorologie_1.0_armel.deb`
* **Sailfish OS:** `pkcon install-local harbour-meteorologie-1.0.0-1.<arch>.rpm`
