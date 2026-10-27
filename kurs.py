# -*- coding: utf-8 -*-
"""Meteorologie für Physiker, deutsch und englisch.

Der Leser kann Thermodynamik, Mechanik und Elektrodynamik und braucht
weder den ersten Hauptsatz noch die Coriolis-Kraft erklärt, sondern
**angewandt**: Was folgt aus ihnen für eine Luftsäule von 10 km Höhe auf
einer rotierenden Kugel mit Wasser darin? Deshalb beginnt jedes Kapitel
bei einer Gleichung, die der Leser schon kennt, und endet bei einer
Beobachtung, die er vom Fenster aus prüfen kann.

Jede Zeichenkette, die ein Mensch liest, ist ein Sprachpaar t(de, en).
Die Herleitungen stehen in herleitungen.py, die Formeln (Textzeile, TeX,
Zeichen, Skizze) in kursformeln.py; lektion() hängt beides selbst an,
damit keine Formel ohne Begründung durchrutscht.

Zahlenantworten werden hier **gerechnet, nicht abgetippt**: jede
zahl()-Aufgabe nimmt ihren Wert aus den Konstanten unten und derselben
Formel, die die Lektion lehrt. Ein Physiker rechnet nach.
"""
from __future__ import unicode_literals

import math

from herleitungen import HERLEITUNGEN
from kursformeln import KURSFORMELN

# --- Konstanten, aus denen alle Zahlenantworten folgen ----------------------
G = 9.81            # m/s²
R_L = 287.05        # J/(kg K), trockene Luft
R_V = 461.5         # J/(kg K), Wasserdampf
C_P = 1004.0        # J/(kg K)
L_V = 2.5e6         # J/kg, Verdampfungswärme bei 0 °C
SIGMA = 5.67e-8     # W/(m² K⁴)
OMEGA = 7.292e-5    # 1/s
S_0 = 1361.0        # W/m², Solarkonstante
ERDRADIUS = 6.371e6 # m
P_0 = 101325.0      # Pa
T_0 = 288.15        # K


def t(de, en):
    return {"de": de, "en": en}


def mc(q, options, answer, why, bild="", code=""):
    return {"kind": "mc", "q": q, "optionen": options, "antwort": answer,
            "warum": why, "bild": bild, "code": code}


def zahl(q, answer, einheit, why, toleranz=0.05, bild=""):
    """Eine Zahl zum Ausrechnen. Verglichen mit Toleranz, weil im Kopf
    niemand auf vier Stellen rechnet -- aber enger als im Flugkurs, hier
    rechnet ein Physiker mit Taschenrechner."""
    return {"kind": "zahl", "q": q, "antwort": answer, "einheit": einheit,
            "warum": why, "toleranz": toleranz, "bild": bild}


def lektion(ident, titel, begriffe, text, bild, aufgaben, formeln=None):
    # Die Herleitung hängt hinten an, in beiden Sprachen. Sie steht nicht
    # im Lektionstext selbst, damit sie an einer Stelle zu überblicken ist
    # und keine Formel ohne Begründung durchrutscht.
    h = HERLEITUNGEN.get(ident)
    if h:
        text = {"de": text["de"] + "\n\n" + h["de"],
                "en": text["en"] + "\n\n" + h["en"]}
    return {"id": ident, "titel": titel, "begriffe": begriffe, "text": text,
            "bild": bild, "aufgaben": aufgaben,
            "formeln": formeln or KURSFORMELN.get(ident, [])}


def kapitel(ident, titel, stufe, blurb, lektionen):
    return {"id": ident, "titel": titel, "stufe": stufe, "text": blurb,
            "lektionen": lektionen}


def rund(x, stellen=0):
    return round(x, stellen) if stellen else float(round(x))


# ===========================================================================
# 1  Die Atmosphäre als Gas
# ===========================================================================

SKALENHOEHE_250 = R_L * 250.0 / G                     # m
DICHTE_NORMAL = P_0 / (R_L * T_0)                     # kg/m³
MASSE_JE_M2 = P_0 / G                                 # kg/m²
DRUCK_5500 = P_0 * math.exp(-5500.0 / (R_L * 255.0 / G))   # Pa, isotherm 255 K

K_ATMOSPHAERE = kapitel(
    "atmosphaere", t("Die Atmosphäre als Gas", "The atmosphere as a gas"), 1,
    t("Zehn Tonnen Luft über jedem Quadratmeter, und fast alles davon in "
      "den untersten zehn Kilometern. Das ideale Gas und die Hydrostatik "
      "reichen, um zu sagen, wie dick die Lufthülle ist und warum sie nach "
      "oben so schnell dünn wird.",
      "Ten tonnes of air above every square metre, and nearly all of it in "
      "the lowest ten kilometres. The ideal gas and hydrostatics are enough "
      "to say how thick the envelope is and why it thins so fast with "
      "height."), [

    lektion("at-aufbau",
        t("Zusammensetzung und Schichtung", "Composition and layering"),
        ["gaskonstante", "stockwerke"],
        t("Trockene Luft ist zu 78 % Stickstoff, 21 % Sauerstoff, 0,9 % "
          "Argon; der Rest sind Spurengase, darunter 0,04 % CO₂. Weil das "
          "Mischungsverhältnis bis in 100 km Höhe konstant bleibt "
          "(Turbulenz mischt schneller, als die Schwerkraft entmischt), "
          "lässt sich die Mischung als **ein** Gas mit mittlerer Molmasse "
          "`M = 28,96 g/mol` behandeln. Die spezifische Gaskonstante ist "
          "dann $R_L = R^*/M = 8{,}314/0{,}02896 = 287$ J/(kg·K), und die "
          "Zustandsgleichung lautet $p = \\rho\\,R_L\\,T$.\n\n"
          "Der Wasserdampf ist der eine Bestandteil, der **nicht** konstant "
          "ist: zwischen fast null und 4 %. Er macht die ganze Meteorologie "
          "aus und bekommt ein eigenes Kapitel.\n\n"
          "**Die Stockwerke** sind durch den Temperaturverlauf definiert, "
          "nicht durch die Höhe. In der **Troposphäre** (bis 8 km an den "
          "Polen, 17 km am Äquator) sinkt die Temperatur mit im Mittel "
          "6,5 K/km, weil sie von unten geheizt wird: der Boden nimmt die "
          "Sonne auf, die Luft ist für sichtbares Licht durchsichtig. Alles "
          "Wetter spielt sich hier ab. An der **Tropopause** hört das "
          "Sinken auf. In der **Stratosphäre** steigt die Temperatur wieder "
          "bis auf etwa 0 °C in 50 km, weil Ozon dort UV-Strahlung "
          "absorbiert -- ein Gas, das von oben geheizt wird, schichtet sich "
          "stabil und verdient den Namen *stratus*, Schicht. Darüber die "
          "**Mesosphäre** (wieder kälter, bis −90 °C in 85 km, kältester "
          "Ort der Atmosphäre) und die **Thermosphäre**, in der die wenigen "
          "verbliebenen Moleküle durch Absorption harter UV-Strahlung über "
          "1000 K heiß werden, ohne dass man es fühlen würde.\n\n"
          "Die Tropopause ist nicht nur eine Linie im Temperaturprofil: "
          "Sie ist ein Deckel. Konvektion stößt an sie an, weil darüber "
          "jedes Luftpaket kälter und dichter als seine Umgebung wäre. "
          "Deshalb breiten sich Gewitteramboss und Vulkanasche an ihr "
          "aus.",
          "Dry air is 78 % nitrogen, 21 % oxygen, 0.9 % argon; the rest is "
          "trace gases, among them 0.04 % CO₂. Because the mixing ratio "
          "stays constant up to 100 km (turbulence mixes faster than gravity "
          "separates), the mixture can be treated as **one** gas with mean "
          "molar mass `M = 28.96 g/mol`. The specific gas constant is then "
          "$R_L = R^*/M = 8.314/0.02896 = 287$ J/(kg·K), and the equation "
          "of state reads $p = \\rho\\,R_L\\,T$.\n\n"
          "Water vapour is the one constituent that is **not** constant: "
          "between almost nothing and 4 %. It makes up the whole of "
          "meteorology and gets a chapter of its own.\n\n"
          "**The layers** are defined by the temperature profile, not by "
          "height. In the **troposphere** (up to 8 km at the poles, 17 km "
          "at the equator) temperature falls at 6.5 K/km on average, "
          "because it is heated from below: the ground absorbs the sun, the "
          "air is transparent to visible light. All weather happens here. "
          "At the **tropopause** the fall stops. In the **stratosphere** "
          "the temperature rises again to about 0 °C at 50 km, because "
          "ozone absorbs UV there -- a gas heated from above stratifies "
          "stably and earns the name *stratus*, layer. Above it the "
          "**mesosphere** (colder again, down to −90 °C at 85 km, the "
          "coldest place in the atmosphere) and the **thermosphere**, where "
          "the few remaining molecules are heated above 1000 K by hard UV "
          "without anyone being able to feel it.\n\n"
          "The tropopause is not just a line on a profile: it is a lid. "
          "Convection bumps against it, because above it any parcel would "
          "be colder and denser than its surroundings. That is why "
          "thunderstorm anvils and volcanic ash spread out along it."),
        "skizze-schichtung", [
        mc(t("Warum nimmt die Temperatur in der Stratosphäre mit der Höhe "
             "zu?",
             "Why does temperature increase with height in the "
             "stratosphere?"),
           [t("Ozon absorbiert dort UV-Strahlung; die Schicht wird von "
              "oben geheizt.",
              "Ozone absorbs UV there; the layer is heated from above."),
            t("Die Luft ist dünner und speichert deshalb mehr Wärme.",
              "The air is thinner and therefore stores more heat."),
            t("Die Sonne ist näher.", "The sun is closer."),
            t("Reibung mit der Troposphäre erwärmt sie.",
              "Friction with the troposphere warms it.")], 0,
           t("Die Troposphäre wird vom Boden geheizt und ist deshalb unten "
             "warm; die Stratosphäre wird vom Ozon geheizt und ist deshalb "
             "oben warm. Wer von oben heizt, bekommt stabile Schichtung.",
             "The troposphere is heated by the ground and so is warm at the "
             "bottom; the stratosphere is heated by ozone and so is warm at "
             "the top. Heating from above gives stable stratification.")),
        zahl(t("Luftdichte bei 1013,25 hPa und 15 °C, mit "
               "R_L = 287 J/(kg·K)? (in kg/m³, zwei Nachkommastellen)",
               "Air density at 1013.25 hPa and 15 °C, with "
               "R_L = 287 J/(kg·K)? (in kg/m³, two decimals)"),
             rund(DICHTE_NORMAL, 2), t("kg/m³", "kg/m³"),
             t("`ρ = p / (R_L·T) = 101325 / (287 × 288,15) = 1,225 kg/m³`. "
               "Das ist die Normdichte der Standardatmosphäre -- jede "
               "Faustformel der Luftfahrt steckt sie irgendwo drin.",
               "`ρ = p / (R_L·T) = 101325 / (287 × 288.15) = 1.225 kg/m³`. "
               "That is the standard-atmosphere density -- every rule of "
               "thumb in aviation has it tucked away somewhere."),
             toleranz=0.02),
        ]),

    lektion("at-hydrostatik",
        t("Hydrostatik und barometrische Höhenformel",
          "Hydrostatics and the barometric formula"),
        ["hydrostatik", "skalenhoehe"],
        t("Luft bewegt sich, und doch gilt in der Senkrechten fast immer "
          "**Gleichgewicht**: der Druckgradient nach oben trägt genau das "
          "Gewicht der Luft darüber. $dp/dz = -\\rho g$. Das ist keine Näherung "
          "für ruhende Luft, sondern eine Skalenaussage -- die vertikalen "
          "Beschleunigungen sind selbst im Gewitter klein gegen `g`, und "
          "außerhalb von Gewittern um Größenordnungen kleiner.\n\n"
          "Setzt man die Zustandsgleichung ein, wird daraus "
          "$dp/p = -g\\,dz/(R_L T)$. Für konstante Temperatur folgt die "
          "**barometrische Höhenformel** $p = p_0\\,e^{-z/H}$ mit der "
          "**Skalenhöhe** $H = R_L T/g$. Bei 250 K, einer vernünftigen "
          "Mitteltemperatur der Troposphäre, sind das 7,3 km; bei 288 K "
          "8,4 km. In jeder Skalenhöhe fällt der Druck auf `1/e`, also "
          "etwa 37 %; alle 5,5 km halbiert er sich. Auf dem Everest "
          "(8848 m) bleiben rund 31 % übrig -- deshalb reicht die Luft dort "
          "gerade noch zum Überleben, aber nicht zum Denken.\n\n"
          "Zwei Zahlen, die daraus folgen und die man behalten sollte: Die "
          "**Masse der Luftsäule** ist $p_0/g = 10\\,330$ kg/m², etwa zehn "
          "Tonnen -- die ganze Atmosphäre entspricht einer 10 m hohen "
          "Wasserschicht. Und in Bodennähe ist **ein Hektopascal etwa "
          "acht Meter**: $\\Delta z = \\Delta p/(\\rho g) = 100/(1{,}225\\cdot 9{,}81) = 8{,}3$ m. "
          "Das ist die Zahl, mit der jeder Höhenmesser arbeitet, und sie "
          "wächst mit der Höhe, weil `ρ` fällt: in 5,5 km sind es schon "
          "16 m je Hektopascal.\n\n"
          "Weil `H` von `T` abhängt, ist eine warme Luftsäule **dicker** "
          "als eine kalte: Bei gleichem Bodendruck liegt die 500-hPa-Fläche "
          "über warmer Luft höher. Daraus wird später der thermische Wind "
          "und die ganze Höhenwetterkarte.",
          "Air moves, and yet in the vertical it is almost always in "
          "**balance**: the upward pressure gradient carries exactly the "
          "weight of the air above. $dp/dz = -\\rho g$. This is not an "
          "approximation for air at rest but a statement about scales -- "
          "vertical accelerations are small against `g` even in a "
          "thunderstorm, and outside thunderstorms smaller by orders of "
          "magnitude.\n\n"
          "Inserting the equation of state gives $dp/p = -g\\,dz/(R_L T)$. "
          "For constant temperature this yields the **barometric formula** "
          "$p = p_0\\,e^{-z/H}$ with the **scale height** $H = R_L T/g$. At "
          "250 K, a sensible mean temperature for the troposphere, that is "
          "7.3 km; at 288 K, 8.4 km. Over each scale height the pressure "
          "falls to `1/e`, about 37 %; every 5.5 km it halves. On Everest "
          "(8848 m) about 31 % remains -- which is why the air there is "
          "just enough to survive on but not to think with.\n\n"
          "Two numbers that follow and are worth keeping: the **mass of "
          "the air column** is $p_0/g = 10\\,330$ kg/m², about ten tonnes -- "
          "the whole atmosphere equals a 10 m layer of water. And near the "
          "ground **one hectopascal is about eight metres**: "
          "$\\Delta z = \\Delta p/(\\rho g) = 100/(1.225\\cdot 9.81) = 8.3$ m. That is the "
          "number every altimeter works with, and it grows with height "
          "because `ρ` falls: at 5.5 km it is already 16 m per "
          "hectopascal.\n\n"
          "Because `H` depends on `T`, a warm column is **thicker** than a "
          "cold one: for the same surface pressure the 500 hPa surface "
          "lies higher over warm air. Later this becomes the thermal wind "
          "and the whole upper-air chart."),
        "skizze-luftsaeule", [
        zahl(t("Skalenhöhe H = R_L·T/g für T = 250 K? (in km, eine "
               "Nachkommastelle)",
               "Scale height H = R_L·T/g for T = 250 K? (in km, one "
               "decimal)"),
             rund(SKALENHOEHE_250 / 1000.0, 1), t("km", "km"),
             t("`H = 287 × 250 / 9,81 = 7315 m ≈ 7,3 km`. In dieser Höhe "
               "ist der Druck auf 37 % gefallen.",
               "`H = 287 × 250 / 9.81 = 7315 m ≈ 7.3 km`. At that height "
               "the pressure has fallen to 37 %."),
             toleranz=0.03),
        zahl(t("Isotherme Atmosphäre mit 255 K: Welcher Druck herrscht in "
               "5500 m, wenn unten 1013 hPa sind? (in hPa)",
               "Isothermal atmosphere at 255 K: what is the pressure at "
               "5500 m if it is 1013 hPa at the bottom? (in hPa)"),
             rund(DRUCK_5500 / 100.0), t("hPa", "hPa"),
             t("`H = 287 × 255 / 9,81 = 7460 m`, also "
               "`p = 1013 × exp(−5500/7460) = 1013 × 0,478 ≈ 485 hPa`. "
               "Die 500-hPa-Fläche, die Hauptkarte der Synoptik, liegt "
               "tatsächlich bei rund 5,5 km.",
               "`H = 287 × 255 / 9.81 = 7460 m`, so "
               "`p = 1013 × exp(−5500/7460) = 1013 × 0.478 ≈ 485 hPa`. The "
               "500 hPa surface, the main chart of synoptic meteorology, "
               "does lie at about 5.5 km."),
             toleranz=0.03),
        mc(t("Zwei Luftsäulen, gleicher Bodendruck, die eine 20 K wärmer. "
             "Wo liegt die 500-hPa-Fläche höher?",
             "Two columns, same surface pressure, one 20 K warmer. Where "
             "does the 500 hPa surface lie higher?"),
           [t("Über der warmen Säule -- ihre Skalenhöhe ist größer.",
              "Over the warm column -- its scale height is larger."),
            t("Über der kalten Säule -- kalte Luft ist dichter.",
              "Over the cold column -- cold air is denser."),
            t("Gleich hoch, der Bodendruck ist ja derselbe.",
              "Same height, the surface pressure is the same after all."),
            t("Das hängt von der Feuchte ab.",
              "That depends on humidity.")], 0,
           t("Warme Luft braucht mehr Höhe, um denselben Druckabfall zu "
             "erreichen. Die Druckfläche wölbt sich über warmer Luft auf; "
             "die Höhenkarte zeigt deshalb über den Tropen hohe und über "
             "den Polen tiefe 500-hPa-Höhen.",
             "Warm air needs more height to achieve the same pressure "
             "drop. Pressure surfaces bulge up over warm air; the upper "
             "chart therefore shows high 500 hPa heights over the tropics "
             "and low ones over the poles.")),
        ]),

    lektion("at-standard",
        t("Die Standardatmosphäre und der Höhenmesser",
          "The standard atmosphere and the altimeter"),
        ["standardatmosphaere", "druckhoehe"],
        t("Die Temperatur ist nicht konstant, und für die Luftfahrt braucht "
          "man ein verbindliches Profil: die **ICAO-Standardatmosphäre**. "
          "Am Boden 15 °C und 1013,25 hPa, in der Troposphäre ein linearer "
          "Gradient $\\Gamma = 6{,}5$ K/km bis 11 km, dann isotherm −56,5 °C bis "
          "20 km. Mit linearem Gradienten $T = T_0 - \\Gamma z$ ist die "
          "Hydrostatik immer noch geschlossen lösbar:\n\n"
          r"$$p = p_0\left(1 - \frac{\Gamma z}{T_0}\right)^{g/(R_L\Gamma)}$$" "\n\n"
          "Der Exponent ist $9{,}81/(287\\cdot 0{,}0065) = 5{,}26$. Daraus: 850 hPa "
          "in 1457 m, 700 hPa in 3012 m, 500 hPa in 5574 m, 300 hPa in "
          "9164 m, 200 hPa an der Tropopause. Diese **Standardhöhen** sind "
          "die Hauptdruckflächen der Wetterkarten.\n\n"
          "Ein **Höhenmesser** ist ein Barometer mit dieser Formel auf der "
          "Skala. Er zeigt die Höhe, in der in der Standardatmosphäre "
          "der gemessene Druck herrschen würde -- die **Druckhöhe**. Zwei "
          "Fehler bleiben: der Bodendruck ist nicht 1013 hPa (dafür stellt "
          "man das QNH ein), und die Luft ist nicht standardwarm. In kalter "
          "Luft sind die Hektopascal enger gestapelt, der Höhenmesser zeigt "
          "**zu viel** -- etwa 4 % je 10 K Abweichung. *Vom Hoch ins Tief, "
          "von warm nach kalt: geht's schief.*\n\n"
          "Für den Physiker ist die Standardatmosphäre vor allem eine "
          "**Vereinbarung**, keine Physik. Der reale Gradient schwankt "
          "zwischen Inversion (Temperatur steigt mit der Höhe) und "
          "trockenadiabatisch (9,8 K/km); 6,5 K/km ist der Mittelwert, "
          "den eine feuchtkonvektive Atmosphäre einstellt -- das nächste "
          "Kapitel sagt, warum.",
          "Temperature is not constant, and aviation needs an agreed "
          "profile: the **ICAO standard atmosphere**. At the surface 15 °C "
          "and 1013.25 hPa, in the troposphere a linear lapse rate "
          "$\\Gamma = 6.5$ K/km up to 11 km, then isothermal −56.5 °C to 20 km. "
          "With a linear lapse rate $T = T_0 - \\Gamma z$ hydrostatics still has "
          "a closed solution:\n\n"
          r"$$p = p_0\left(1 - \frac{\Gamma z}{T_0}\right)^{g/(R_L\Gamma)}$$" "\n\n"
          "The exponent is $9.81/(287\\cdot 0.0065) = 5.26$. From it: 850 hPa "
          "at 1457 m, 700 hPa at 3012 m, 500 hPa at 5574 m, 300 hPa at "
          "9164 m, 200 hPa at the tropopause. These **standard heights** "
          "are the main pressure levels of weather charts.\n\n"
          "An **altimeter** is a barometer with this formula on its scale. "
          "It shows the height at which the measured pressure would occur "
          "in the standard atmosphere -- the **pressure altitude**. Two "
          "errors remain: the surface pressure is not 1013 hPa (the QNH "
          "setting corrects that), and the air is not standard-warm. In "
          "cold air the hectopascals are stacked more tightly and the "
          "altimeter reads **too high** -- about 4 % per 10 K deviation. "
          "*From high to low, from warm to cold: look out below.*\n\n"
          "For the physicist the standard atmosphere is above all a "
          "**convention**, not physics. The real lapse rate varies between "
          "inversion (temperature rising with height) and dry adiabatic "
          "(9.8 K/km); 6.5 K/km is the mean that a moist-convective "
          "atmosphere settles on -- the next chapter says why."),
        "skizze-standard", [
        zahl(t("Standardatmosphäre: In welcher Höhe liegt 700 hPa? "
               "Exponent g/(R_L·Γ) = 5,26. (in m)",
               "Standard atmosphere: at what height is 700 hPa? Exponent "
               "g/(R_L·Γ) = 5.26. (in m)"),
             rund(T_0 / 0.0065 * (1.0 - (700.0 / 1013.25) ** (1.0 / (G / (R_L * 0.0065))))),
             t("m", "m"),
             t("Umgestellt: `z = T₀/Γ · [1 − (p/p₀)^(1/5,26)]` = "
               "`44 331 × [1 − 0,6908^0,190] = 44 331 × 0,0679 ≈ 3010 m`.",
               "Rearranged: `z = T₀/Γ · [1 − (p/p₀)^(1/5.26)]` = "
               "`44 331 × [1 − 0.6908^0.190] = 44 331 × 0.0679 ≈ 3010 m`."),
             toleranz=0.03),
        mc(t("Der Höhenmesser ist auf das richtige QNH gestellt, die Luft "
             "ist aber 20 K kälter als Standard. Was zeigt er in 3000 m "
             "wahrer Höhe?",
             "The altimeter is set to the correct QNH, but the air is 20 K "
             "colder than standard. What does it read at 3000 m true "
             "altitude?"),
           [t("Zu viel, etwa 3200 m -- kalte Luft stapelt die Druckflächen "
              "enger.",
              "Too much, about 3200 m -- cold air stacks the pressure "
              "surfaces more tightly."),
            t("Zu wenig, etwa 2750 m.", "Too little, about 2750 m."),
            t("Genau 3000 m, das QNH gleicht alles aus.",
              "Exactly 3000 m, the QNH corrects for everything."),
            t("Das hängt vom Luftdruck am Boden ab.",
              "That depends on the surface pressure.")], 0,
           t("Die Skalenhöhe ist proportional zu `T`. 20 K unter 288 K "
             "sind 7 % weniger Skalenhöhe: Der Druck, der in Standardluft "
             "in 3000 m herrscht, wird hier schon in 2790 m erreicht -- "
             "umgekehrt zeigt der Höhenmesser in wahren 3000 m rund "
             "3200 m an.",
             "The scale height is proportional to `T`. 20 K below 288 K is "
             "7 % less scale height: the pressure found at 3000 m in "
             "standard air is reached here already at 2790 m -- conversely "
             "the altimeter reads about 3200 m at a true 3000 m.")),
        ]),
    ])


# ===========================================================================
# 2  Thermodynamik trockener Luft
# ===========================================================================

GAMMA_D = G / C_P * 1000.0                    # K/km
KAPPA = R_L / C_P
THETA_500 = 253.15 * (1000.0 / 500.0) ** KAPPA  # K, −20 °C in 500 hPa
N_BV = math.sqrt(G / 290.0 * (6.0 / 1000.0))    # 1/s bei dθ/dz = 6 K/km... s.u.
# Brunt-Väisälä für Standardgradient: dθ/dz = (Γ_d − Γ)·θ/T ≈ 3,3 K/km bei
# θ ≈ T. Mit θ ≈ 290 K: N² = 9,81/290 × 0,0033
N_STANDARD = math.sqrt(G / 290.0 * ((GAMMA_D - 6.5) / 1000.0))
PERIODE_STANDARD = 2 * math.pi / N_STANDARD    # s

K_THERMO = kapitel(
    "thermo", t("Thermodynamik trockener Luft", "Thermodynamics of dry air"), 2,
    t("Ein Luftpaket, das steigt, dehnt sich aus und kühlt ab -- ohne "
      "Wärmeaustausch, weil Luft ein schlechter Leiter ist und die "
      "Bewegung schneller geht als die Strahlung. Aus dem ersten Hauptsatz "
      "folgen der adiabatische Gradient, die potentielle Temperatur und "
      "die Frage, ob die Atmosphäre stabil ist.",
      "A rising parcel expands and cools -- with no heat exchange, because "
      "air conducts badly and the motion is faster than radiation. From "
      "the first law follow the adiabatic lapse rate, potential "
      "temperature and the question of whether the atmosphere is "
      "stable."), [

    lektion("th-adiabate",
        t("Der trockenadiabatische Gradient", "The dry adiabatic lapse rate"),
        ["adiabate", "paketmethode"],
        t("Die **Paketmethode** ist das Gedankenexperiment der ganzen "
          "Meteorologie: Man denkt sich ein Volumen Luft, das sich beim "
          "Aufsteigen dem Umgebungsdruck sofort anpasst (Schallgeschwindigkeit), "
          "aber keine Wärme austauscht (Zeit zu kurz, Leitung zu schlecht, "
          "Strahlung zu schwach). Der erste Hauptsatz je Kilogramm lautet "
          "$\\delta q = c_p\\,dT - \\alpha\\,dp$ mit $\\alpha = 1/\\rho$. Adiabatisch ist $\\delta q = 0$, "
          "und hydrostatisch ist $dp = -\\rho g\\,dz$. Einsetzen:\n\n"
          r"$$c_p\,dT = -g\,dz \quad\Rightarrow\quad \frac{dT}{dz} = -\frac{g}{c_p} = -9{,}8\ \frac{\mathrm{K}}{\mathrm{km}}$$" "\n\n"
          "Das ist der **trockenadiabatische Gradient** `Γ_d`, rund "
          "**1 K je 100 m**. Bemerkenswert daran: Er hängt weder vom "
          "Druck noch von der Temperatur ab, nur von `g` und `c_p`, und "
          "gilt deshalb vom Boden bis zur Tropopause gleich. Auf dem Mars "
          "(g = 3,7, CO₂ mit c_p = 850) sind es 4,4 K/km.\n\n"
          "Was dabei physikalisch passiert: Das Paket leistet beim "
          "Ausdehnen Arbeit gegen den Außendruck, und diese Arbeit kommt "
          "aus der inneren Energie. Mit `c_v` statt `c_p` wäre die Rechnung "
          "falsch -- das `c_p` enthält bereits die Ausdehnungsarbeit bei "
          "konstantem Druck, und genau die wird hier geleistet.\n\n"
          "Umgekehrt beim Absinken: Luft, die in einem Hoch aus 3 km "
          "herabsinkt, kommt 30 K wärmer unten an. Deshalb sind Hochs "
          "wolkenfrei (Absinken verdunstet alles) und deshalb ist der Föhn "
          "warm. Und deshalb ist im Sommer die Luft auf dem Berg kälter, "
          "obwohl sie der Sonne näher ist: nicht die Entfernung zur Sonne "
          "zählt, sondern der Druck, bei dem die Luft angekommen ist.",
          "The **parcel method** is the thought experiment of all "
          "meteorology: imagine a volume of air that adjusts to the "
          "ambient pressure instantly as it rises (speed of sound) but "
          "exchanges no heat (too little time, poor conduction, weak "
          "radiation). The first law per kilogram reads "
          "$\\delta q = c_p\\,dT - \\alpha\\,dp$ with $\\alpha = 1/\\rho$. Adiabatic means $\\delta q = 0$, "
          "and hydrostatic means $dp = -\\rho g\\,dz$. Substituting:\n\n"
          r"$$c_p\,dT = -g\,dz \quad\Rightarrow\quad \frac{dT}{dz} = -\frac{g}{c_p} = -9.8\ \frac{\mathrm{K}}{\mathrm{km}}$$" "\n\n"
          "That is the **dry adiabatic lapse rate** `Γ_d`, about **1 K "
          "per 100 m**. What is remarkable: it depends neither on pressure "
          "nor on temperature, only on `g` and `c_p`, and so holds the "
          "same from the ground to the tropopause. On Mars (g = 3.7, CO₂ "
          "with c_p = 850) it is 4.4 K/km.\n\n"
          "What happens physically: the parcel does work against the "
          "outside pressure as it expands, and that work comes out of its "
          "internal energy. With `c_v` instead of `c_p` the calculation "
          "would be wrong -- `c_p` already contains the expansion work at "
          "constant pressure, and that is exactly the work being done "
          "here.\n\n"
          "The reverse on descent: air sinking from 3 km in an "
          "anticyclone arrives 30 K warmer at the bottom. That is why "
          "highs are cloud-free (subsidence evaporates everything) and "
          "why the foehn is warm. And it is why mountain air is colder in "
          "summer although it is nearer the sun: what counts is not the "
          "distance to the sun but the pressure the air has arrived at."),
        "skizze-paket", [
        zahl(t("Ein Luftpaket sinkt trockenadiabatisch von 3000 m auf "
               "500 m. Um wie viel Kelvin erwärmt es sich? (g = 9,81, "
               "c_p = 1004)",
               "A parcel sinks dry-adiabatically from 3000 m to 500 m. By "
               "how many kelvin does it warm? (g = 9.81, c_p = 1004)"),
             rund(G / C_P * 2500.0, 1), t("K", "K"),
             t("`ΔT = g/c_p · Δz = 0,00977 × 2500 = 24,4 K`.",
               "`ΔT = g/c_p · Δz = 0.00977 × 2500 = 24.4 K`."),
             toleranz=0.02),
        mc(t("Warum steht in der Herleitung des adiabatischen Gradienten "
             "c_p und nicht c_v?",
             "Why does the derivation of the adiabatic lapse rate contain "
             "c_p and not c_v?"),
           [t("Weil das Paket beim Steigen gegen den Außendruck Arbeit "
              "leistet; c_p enthält diese Ausdehnungsarbeit.",
              "Because the parcel does work against the outside pressure "
              "as it rises; c_p includes that expansion work."),
            t("Weil der Druck konstant bleibt.",
              "Because the pressure stays constant."),
            t("Weil c_v nur für Festkörper gilt.",
              "Because c_v applies only to solids."),
            t("Reine Konvention, beide Werte liefern dasselbe Ergebnis.",
              "Pure convention, both values give the same result.")], 0,
           t("`δq = c_p dT − α dp`: Der Term `α dp` ist die Arbeit, und "
             "hydrostatisch ist er genau `−g dz`. Mit `c_v` käme 14 K/km "
             "heraus, und keine Messung bestätigt das.",
             "`δq = c_p dT − α dp`: the `α dp` term is the work, and "
             "hydrostatically it is exactly `−g dz`. With `c_v` one would "
             "get 14 K/km, and no measurement confirms that.")),
        ]),

    lektion("th-theta",
        t("Die potentielle Temperatur", "Potential temperature"),
        ["potentielle-temperatur", "poisson"],
        t("Die Temperatur eines Pakets ändert sich beim Steigen auch ohne "
          "Wärmezufuhr -- sie ist als Etikett unbrauchbar. Brauchbar ist "
          "die Temperatur, die das Paket **hätte, wenn man es adiabatisch "
          "auf 1000 hPa brächte**: die **potentielle Temperatur** θ. Aus "
          "der Poisson-Gleichung $T\\,p^{-\\kappa} = \\mathrm{const}$ mit `κ = R_L/c_p = "
          "0,286` folgt\n\n"
          r"$$\theta = T\left(\frac{1000\ \mathrm{hPa}}{p}\right)^{0{,}286}$$" "\n\n"
          "θ ist bei adiabatischen Vorgängen **erhalten**. Das macht sie "
          "zum Tracer: Ein Paket mit θ = 300 K bleibt auf der 300-K-Fläche, "
          "wohin es auch strömt, solange es nicht gestrahlt oder "
          "kondensiert wird. Die Entropie je Kilogramm ist `s = c_p·ln θ + "
          "const`; θ ist also nichts anderes als die Entropie in "
          "Temperatur-Einheiten, und Isentropen und Flächen gleicher θ "
          "sind dasselbe.\n\n"
          "In der realen Atmosphäre **nimmt θ mit der Höhe zu**: Bei "
          "6,5 K/km Umgebungsgradient fällt T langsamer als die Adiabate, "
          "also steigt θ um rund 3,3 K/km. In der Stratosphäre steigt sie "
          "steil (θ = 400 K in 100 hPa, über 1000 K in 10 hPa). Deshalb "
          "sind θ-Flächen in der Troposphäre flach und in der "
          "Stratosphäre dicht gestapelt -- und deshalb muss ein Paket, "
          "das die Tropopause durchstoßen will, Entropie gewinnen, was "
          "nur Strahlung oder Kondensation liefern.\n\n"
          "Wo θ mit der Höhe **abnimmt**, ist die Luft überadiabatisch "
          "geschichtet: schwere Luft über leichter. Das gibt es nur in "
          "den untersten Metern über sonnenbeschienenem Boden und hält "
          "nur Minuten -- Konvektion räumt es sofort auf. Ein gut "
          "durchmischter Nachmittag hat deshalb eine Grenzschicht mit "
          "**konstanter θ**: Das ist das Kennzeichen von Durchmischung "
          "im Profil einer Radiosonde.",
          "A parcel's temperature changes as it rises even without heat "
          "input -- it is useless as a label. What is useful is the "
          "temperature the parcel **would have if brought adiabatically "
          "to 1000 hPa**: the **potential temperature** θ. From Poisson's "
          "relation $T\\,p^{-\\kappa} = \\mathrm{const}$ with $\\kappa = R_L/c_p = 0.286$ "
          "follows\n\n"
          r"$$\theta = T\left(\frac{1000\ \mathrm{hPa}}{p}\right)^{0.286}$$" "\n\n"
          "θ is **conserved** in adiabatic processes. That makes it a "
          "tracer: a parcel with θ = 300 K stays on the 300 K surface "
          "wherever it flows, as long as it neither radiates nor "
          "condenses. The entropy per kilogram is $s = c_p\\ln\\theta + \\mathrm{const}$; "
          "θ is nothing but entropy in temperature units, and isentropes "
          "and surfaces of equal θ are the same thing.\n\n"
          "In the real atmosphere **θ increases with height**: with a "
          "6.5 K/km environmental lapse rate T falls more slowly than the "
          "adiabat, so θ rises by about 3.3 K/km. In the stratosphere it "
          "rises steeply (θ = 400 K at 100 hPa, over 1000 K at 10 hPa). "
          "That is why θ surfaces are flat in the troposphere and tightly "
          "stacked in the stratosphere -- and why a parcel that wants to "
          "punch through the tropopause has to gain entropy, which only "
          "radiation or condensation can supply.\n\n"
          "Where θ **decreases** with height the air is superadiabatic: "
          "heavy air over light. That exists only in the lowest metres "
          "over sunlit ground and lasts only minutes -- convection clears "
          "it immediately. A well-mixed afternoon therefore has a "
          "boundary layer with **constant θ**: that is the signature of "
          "mixing in a radiosonde profile."),
        "skizze-theta", [
        zahl(t("In 500 hPa werden −20 °C gemessen. Potentielle "
               "Temperatur? (κ = 0,286; in K)",
               "−20 °C is measured at 500 hPa. Potential temperature? "
               "(κ = 0.286; in K)"),
             rund(THETA_500), t("K", "K"),
             t("`θ = 253,15 × 2^0,286 = 253,15 × 1,219 = 308,6 K`. "
               "Zum Vergleich: Am Boden sind bei 1000 hPa und 15 °C "
               "θ = 288 K. Die Luft in 500 hPa ist potentiell 20 K wärmer "
               "-- stabil geschichtet.",
               "`θ = 253.15 × 2^0.286 = 253.15 × 1.219 = 308.6 K`. For "
               "comparison: at the surface, 1000 hPa and 15 °C give "
               "θ = 288 K. The air at 500 hPa is potentially 20 K warmer "
               "-- stably stratified."),
             toleranz=0.01),
        mc(t("Eine Radiosonde zeigt in den untersten 1500 m konstante "
             "potentielle Temperatur. Was heißt das?",
             "A radiosonde shows constant potential temperature in the "
             "lowest 1500 m. What does that mean?"),
           [t("Die Grenzschicht ist durch Konvektion gut durchmischt; "
              "die Temperatur fällt dort trockenadiabatisch.",
              "The boundary layer is well mixed by convection; the "
              "temperature falls dry-adiabatically there."),
            t("Es herrscht eine Inversion.", "There is an inversion."),
            t("Die Temperatur ist konstant, also isotherm.",
              "The temperature is constant, so isothermal."),
            t("Die Sonde ist defekt.", "The sonde is faulty.")], 0,
           t("Konstante θ heißt: jedes Paket könnte adiabatisch an jede "
             "Höhe gebracht werden und wäre dort genauso warm wie die "
             "Umgebung. Genau das stellt Konvektion ein. Die wirkliche "
             "Temperatur fällt dabei mit 9,8 K/km.",
             "Constant θ means: any parcel could be brought adiabatically "
             "to any height and would be exactly as warm as its "
             "surroundings. That is what convection establishes. The "
             "actual temperature falls at 9.8 K/km.")),
        ]),

    lektion("th-stabilitaet",
        t("Statische Stabilität und die Brunt-Väisälä-Frequenz",
          "Static stability and the Brunt–Väisälä frequency"),
        ["stabilitaet", "brunt-vaisala", "inversion"],
        t("Hebt man ein Paket um `δz`, kühlt es mit `Γ_d` ab, während die "
          "Umgebung den Gradienten `Γ` hat. Nach dem Heben ist das Paket "
          "um $(\\Gamma - \\Gamma_d)\\,\\delta z$ kälter als die Umgebung -- oder wärmer, wenn "
          "$\\Gamma > \\Gamma_d$. Der Auftrieb je Masse ist $g\\,(T' - T)/T$ mit `T'` "
          "der Pakettemperatur. Das ergibt die Bewegungsgleichung eines "
          "harmonischen Oszillators:\n\n"
          r"$$\frac{d^2\,\delta z}{dt^2} = -N^2\,\delta z, \qquad N^2 = \frac{g}{\theta}\,\frac{d\theta}{dz}$$" "\n\n"
          "`N` ist die **Brunt-Väisälä-Frequenz**. Bei $d\\theta/dz = 3{,}3$ K/km "
          "(Standardatmosphäre) ist $N = 0{,}011$ /s, die Periode "
          "$2\\pi/N \\approx 9{,}5$ min. Das ist die Zeitskala, mit der die "
          "Atmosphäre auf jede Störung antwortet: Wellen hinter Bergen, "
          "Schwingungen hinter Gewittern, die Abstände zwischen "
          "Wolkenstreifen in Lee-Wellen. Bei $N^2 < 0$ wird aus der "
          "Schwingung exponentielles Wachstum -- **Instabilität**.\n\n"
          "Daraus die drei Fälle, immer mit $\\Gamma_d = 9{,}8$ K/km als "
          "Maßstab:\n\n"
          "**Stabil**, $\\Gamma < \\Gamma_d$: gehobene Luft ist kälter als die "
          "Umgebung und sinkt zurück. Die Standardatmosphäre mit 6,5 K/km "
          "ist für trockene Luft stabil.\n\n"
          "**Neutral**, $\\Gamma = \\Gamma_d$: die Grenzschicht am Nachmittag.\n\n"
          "**Labil**, $\\Gamma > \\Gamma_d$: nur bodennah, nur kurz.\n\n"
          "Der Grenzfall mit umgekehrtem Vorzeichen ist die **Inversion**, "
          "$\\Gamma < 0$: Temperatur steigt mit der Höhe. Sie entsteht nachts "
          "durch Ausstrahlung am Boden, in Hochs durch Absinken "
          "(Absinkinversion, oft in 1-2 km, Deckel über dem Dunst) und an "
          "Fronten. Eine Inversion ist für vertikale Bewegung eine Wand: "
          "Rauch breitet sich unter ihr flach aus, Schadstoffe sammeln "
          "sich, der Smog im Winterbecken ist eine Inversion mit "
          "Industrie darunter.\n\n"
          "Für feuchte Luft kommt ein zweiter Maßstab hinzu, der "
          "**feuchtadiabatische** Gradient von rund 6 K/km -- und zwischen "
          "beiden liegt der interessanteste Fall: bedingt labil. Das ist "
          "das nächste Kapitel.",
          "Lift a parcel by `δz`: it cools at `Γ_d` while the environment "
          "has lapse rate `Γ`. After lifting, the parcel is "
          "$(\\Gamma - \\Gamma_d)\\,\\delta z$ colder than its surroundings -- or warmer if "
          "$\\Gamma > \\Gamma_d$. Buoyancy per mass is $g\\,(T' - T)/T$ with `T'` the "
          "parcel temperature. That gives the equation of motion of a "
          "harmonic oscillator:\n\n"
          r"$$\frac{d^2\,\delta z}{dt^2} = -N^2\,\delta z, \qquad N^2 = \frac{g}{\theta}\,\frac{d\theta}{dz}$$" "\n\n"
          "`N` is the **Brunt–Väisälä frequency**. With "
          "$d\\theta/dz = 3.3$ K/km (standard atmosphere) $N = 0.011$ /s, the "
          "period $2\\pi/N \\approx 9.5$ min. That is the time scale on which the "
          "atmosphere answers any disturbance: waves behind mountains, "
          "oscillations behind thunderstorms, the spacing of cloud bands "
          "in lee waves. For $N^2 < 0$ the oscillation becomes exponential "
          "growth -- **instability**.\n\n"
          "Hence the three cases, always with $\\Gamma_d = 9.8$ K/km as the "
          "yardstick:\n\n"
          "**Stable**, $\\Gamma < \\Gamma_d$: lifted air is colder than its "
          "surroundings and sinks back. The standard atmosphere at "
          "6.5 K/km is stable for dry air.\n\n"
          "**Neutral**, $\\Gamma = \\Gamma_d$: the afternoon boundary layer.\n\n"
          "**Unstable**, $\\Gamma > \\Gamma_d$: only near the ground, only briefly.\n\n"
          "The limiting case with reversed sign is the **inversion**, "
          "$\\Gamma < 0$: temperature rising with height. It forms at night by "
          "radiation from the ground, in anticyclones by subsidence "
          "(subsidence inversion, often at 1-2 km, the lid over the haze) "
          "and at fronts. An inversion is a wall to vertical motion: "
          "smoke spreads flat beneath it, pollutants accumulate, the "
          "winter smog of a basin is an inversion with industry "
          "underneath.\n\n"
          "For moist air a second yardstick appears, the **moist "
          "adiabatic** lapse rate of about 6 K/km -- and between the two "
          "lies the most interesting case: conditionally unstable. That "
          "is the next chapter."),
        "skizze-stabilitaet", [
        zahl(t("dθ/dz = 3,3 K/km, θ = 290 K. Periode der "
               "Brunt-Väisälä-Schwingung? (in Minuten, eine "
               "Nachkommastelle)",
               "dθ/dz = 3.3 K/km, θ = 290 K. Period of the Brunt–Väisälä "
               "oscillation? (in minutes, one decimal)"),
             rund(2 * math.pi / math.sqrt(G / 290.0 * 0.0033) / 60.0, 1),
             t("min", "min"),
             t("`N² = 9,81/290 × 0,0033 = 1,116·10⁻⁴ /s²`, "
               "`N = 0,01057 /s`, `T = 2π/N = 595 s ≈ 9,9 min`.",
               "`N² = 9.81/290 × 0.0033 = 1.116·10⁻⁴ /s²`, "
               "`N = 0.01057 /s`, `T = 2π/N = 595 s ≈ 9.9 min`."),
             toleranz=0.03),
        mc(t("Ein Radiosondenaufstieg zeigt zwischen 800 und 2000 m einen "
             "Gradienten von 8 K/km. Wie ist diese Schicht für trockene "
             "Luft geschichtet?",
             "A sounding shows a lapse rate of 8 K/km between 800 and "
             "2000 m. How is that layer stratified for dry air?"),
           [t("Stabil -- 8 K/km liegt unter dem trockenadiabatischen "
              "Wert von 9,8 K/km.",
              "Stable -- 8 K/km is below the dry adiabatic 9.8 K/km."),
            t("Labil -- 8 K/km ist steiler als der Standardgradient.",
              "Unstable -- 8 K/km is steeper than the standard lapse "
              "rate."),
            t("Neutral.", "Neutral."),
            t("Eine Inversion.", "An inversion.")], 0,
           t("Maßstab ist die Adiabate, nicht die Standardatmosphäre. "
             "Gehobene trockene Luft wäre nach 1 km um 1,8 K kälter als "
             "die Umgebung und sänke zurück. Für gesättigte Luft sähe es "
             "anders aus -- bedingt labil.",
             "The yardstick is the adiabat, not the standard atmosphere. "
             "Lifted dry air would be 1.8 K colder than its surroundings "
             "after 1 km and would sink back. For saturated air it would "
             "look different -- conditionally unstable.")),
        ]),
    ])


# ===========================================================================
# 3  Feuchte Luft
# ===========================================================================

def e_s(T_celsius):
    """Magnus-Formel, hPa. Gut auf 0,1 % zwischen −45 und +60 °C."""
    return 6.112 * math.exp(17.62 * T_celsius / (243.12 + T_celsius))


E_S_20 = e_s(20.0)                                   # hPa
TAUPUNKT_SPREIZUNG = 1.0 / (GAMMA_D / 1000.0 - 0.0017) # m je K ≈ 123
# Feuchtadiabate bei 0 °C und 1000 hPa (Herleitung in herleitungen.py)
def gamma_s(T_K, p_hPa):
    es = e_s(T_K - 273.15)
    r = 0.622 * es / (p_hPa - es)
    zaehler = 1.0 + L_V * r / (R_L * T_K)
    nenner = 1.0 + L_V ** 2 * r * 0.622 / (C_P * R_L * T_K ** 2)
    return G / C_P * zaehler / nenner * 1000.0          # K/km
GAMMA_S_0 = gamma_s(273.15, 1000.0)
GAMMA_S_20 = gamma_s(293.15, 1000.0)
W_MAX_1000 = math.sqrt(2 * 1000.0)                   # m/s bei CAPE 1000 J/kg
LCL_FAUST = 125.0 * 12.0                             # m bei 12 K Spreizung

K_FEUCHTE = kapitel(
    "feuchte", t("Feuchte Luft", "Moist air"), 3,
    t("Ein Prozent der Masse, aber der Stoff, der Wärme transportiert, "
      "Wolken macht und die Stabilität umkehrt. Alles hängt an einer "
      "Gleichung: Clausius-Clapeyron, und daran, dass sie exponentiell "
      "ist.",
      "One per cent of the mass, but the substance that carries heat, "
      "makes clouds and reverses stability. Everything hangs on one "
      "equation: Clausius–Clapeyron, and on the fact that it is "
      "exponential."), [

    lektion("fe-dampf",
        t("Dampfdruck und Clausius-Clapeyron",
          "Vapour pressure and Clausius–Clapeyron"),
        ["clausius-clapeyron", "taupunkt", "feuchtemasse"],
        t("Über einer Wasserfläche stellt sich ein Gleichgewicht ein, bei "
          "dem so viele Moleküle verdampfen wie kondensieren. Der "
          "Partialdruck des Dampfes in diesem Zustand ist der "
          "**Sättigungsdampfdruck** `e_s(T)`, und er hängt **nur von der "
          "Temperatur** ab -- nicht vom Luftdruck, nicht davon, ob "
          "überhaupt Luft da ist. Die Gleichung dafür ist Clausius-"
          "Clapeyron:\n\n"
          r"$$\frac{de_s}{dT} = \frac{L_v\,e_s}{R_v\,T^2}$$" "\n\n"
          "Integriert mit konstantem `L_v` ergibt das eine Exponentialfunktion, "
          "praktisch die **Magnus-Formel** "
          "$e_s = 6{,}112\\ \\mathrm{hPa}\\cdot\\exp\\!\\left(\\frac{17{,}62\\,t}{243{,}12 + t}\\right)$ mit `t` in °C. "
          "Die Zahlen, die man kennen sollte: 6,1 hPa bei 0 °C, 12,3 bei "
          "10 °C, 23,3 bei 20 °C, 42,3 bei 30 °C -- **je 10 K etwa das "
          "Doppelte**, oder 7 % je Kelvin. Dieses Verdoppeln ist der "
          "wichtigste Zahlenwert der Meteorologie: Warme Luft kann "
          "nicht ein bisschen, sondern exponentiell mehr Wasser "
          "tragen.\n\n"
          "Daraus die Feuchtemaße: Die **relative Feuchte** $RH = e/e_s$. "
          "Der **Taupunkt** `T_d` ist die Temperatur, bei der `e` gleich "
          "`e_s` würde -- er misst den Dampfgehalt und nicht die "
          "Temperatur, und ist deshalb das bessere Maß. Das "
          "**Mischungsverhältnis** $r = 0{,}622\\,e/(p - e)$ in kg Dampf je kg "
          "trockener Luft; die 0,622 sind $M_{Wasser}/M_{Luft} = 18/28{,}96$. "
          "Bei 20 °C und 1000 hPa gesättigt: 14,8 g/kg.\n\n"
          "Weil Wasserdampf **leichter** ist als Luft (18 gegen 29), ist "
          "feuchte Luft bei gleichem Druck und gleicher Temperatur weniger "
          "dicht -- entgegen dem Alltagsgefühl. Man rechnet mit der "
          "**virtuellen Temperatur** $T_v = T\\,(1 + 0{,}61\\,r)$, der "
          "Temperatur, bei der trockene Luft dieselbe Dichte hätte. Bei "
          "14,8 g/kg sind das 2,6 K mehr -- ein Auftrieb, der in den "
          "Tropen zählt.",
          "Over a water surface an equilibrium sets in at which as many "
          "molecules evaporate as condense. The partial pressure of the "
          "vapour in that state is the **saturation vapour pressure** "
          "`e_s(T)`, and it depends **only on temperature** -- not on the "
          "air pressure, not on whether there is any air at all. The "
          "equation for it is Clausius–Clapeyron:\n\n"
          r"$$\frac{de_s}{dT} = \frac{L_v\,e_s}{R_v\,T^2}$$" "\n\n"
          "Integrated with constant `L_v` this gives an exponential, in "
          "practice the **Magnus formula** "
          "$e_s = 6.112\\ \\mathrm{hPa}\\cdot\\exp\\!\\left(\\frac{17.62\\,t}{243.12 + t}\\right)$ with `t` in °C. "
          "Numbers worth knowing: 6.1 hPa at 0 °C, 12.3 at 10 °C, 23.3 at "
          "20 °C, 42.3 at 30 °C -- **roughly doubling every 10 K**, or "
          "7 % per kelvin. That doubling is the most important number in "
          "meteorology: warm air can carry not a little but exponentially "
          "more water.\n\n"
          "Hence the humidity measures: **relative humidity** "
          "$RH = e/e_s$. The **dew point** `T_d` is the temperature at "
          "which `e` would equal `e_s` -- it measures vapour content, not "
          "temperature, and is therefore the better measure. The **mixing "
          "ratio** $r = 0.622\\,e/(p - e)$ in kg of vapour per kg of dry "
          "air; the 0.622 is $M_{water}/M_{air} = 18/28.96$. Saturated at "
          "20 °C and 1000 hPa: 14.8 g/kg.\n\n"
          "Because water vapour is **lighter** than air (18 against 29), "
          "moist air at the same pressure and temperature is less dense "
          "-- contrary to everyday feeling. One works with the **virtual "
          "temperature** $T_v = T\\,(1 + 0.61\\,r)$, the temperature at which "
          "dry air would have the same density. At 14.8 g/kg that is "
          "2.6 K more -- a buoyancy that matters in the tropics."),
        "skizze-dampfdruck", [
        zahl(t("Sättigungsdampfdruck bei 20 °C nach Magnus? (in hPa, "
               "eine Nachkommastelle)",
               "Saturation vapour pressure at 20 °C by Magnus? (in hPa, "
               "one decimal)"),
             rund(E_S_20, 1), t("hPa", "hPa"),
             t("`6,112 × exp(17,62 × 20 / 263,12) = 6,112 × 3,82 = "
               "23,3 hPa`. Das sind 2,3 % des Luftdrucks: selbst "
               "gesättigt ist Dampf ein Spurengas.",
               "`6.112 × exp(17.62 × 20 / 263.12) = 6.112 × 3.82 = "
               "23.3 hPa`. That is 2.3 % of the air pressure: even "
               "saturated, vapour is a trace gas."),
             toleranz=0.02),
        mc(t("Die Luft hat 25 °C und Taupunkt 15 °C. Relative Feuchte "
             "ungefähr?",
             "The air is at 25 °C with dew point 15 °C. Relative humidity, "
             "roughly?"),
           [t("Etwa 54 % -- e_s(15)/e_s(25) = 17,0/31,6.",
              "About 54 % -- e_s(15)/e_s(25) = 17.0/31.6."),
            t("Etwa 90 %.", "About 90 %."),
            t("Etwa 25 %.", "About 25 %."),
            t("Genau 60 %, zehn Grad Spreizung sind 40 %.",
              "Exactly 60 %, ten degrees of spread is 40 %.")], 0,
           t("Der Dampfdruck ist der Sättigungsdampfdruck beim Taupunkt. "
             "Zehn Kelvin Spreizung sind grob eine Halbierung, weil "
             "e_s sich je 10 K verdoppelt -- die Faustregel ist 5 % je "
             "Kelvin Spreizung nahe der Sättigung.",
             "The vapour pressure is the saturation value at the dew "
             "point. Ten kelvin of spread is roughly a halving, because "
             "e_s doubles every 10 K -- the rule of thumb is 5 % per "
             "kelvin of spread near saturation.")),
        ]),

    lektion("fe-hebung",
        t("Hebung, Kondensationsniveau und die Feuchtadiabate",
          "Lifting, condensation level and the moist adiabat"),
        ["kondensationsniveau", "feuchtadiabate", "theta-e"],
        t("Ein Paket steigt vom Boden auf. Seine Temperatur fällt mit "
          "9,8 K/km. Sein Taupunkt fällt auch, aber langsamer: Das "
          "Mischungsverhältnis bleibt konstant, der Dampfdruck `e` sinkt "
          "proportional zum Druck, und über Clausius-Clapeyron folgt daraus "
          "$dT_d/dz \\approx -1{,}7$ K/km. Die Spreizung `T − T_d` schließt sich "
          "also mit 8,1 K/km, und das **Hebungskondensationsniveau** "
          "liegt bei\n\n"
          r"$$z_{LCL} \approx 125\ \frac{\mathrm{m}}{\mathrm{K}}\cdot(T - T_d)$$" "\n\n"
          "Das ist die Wolkenbasis jeder Cumulus-Wolke, und man kann sie "
          "vom Boden aus mit Thermometer und Taupunkt vorhersagen -- "
          "Segelflieger tun das jeden Morgen.\n\n"
          "Oberhalb kondensiert Dampf, und die freiwerdende Verdampfungs"
          "wärme $L_v = 2{,}5$ MJ/kg bremst die Abkühlung. Der "
          "**feuchtadiabatische Gradient** ist deshalb kleiner als der "
          "trockene:\n\n"
          r"$$\Gamma_s = \Gamma_d\;\frac{1 + \dfrac{L_v\,r_s}{R_L\,T}}{1 + \dfrac{0{,}622\,L_v^2\,r_s}{c_p\,R_L\,T^2}}$$" "\n\n"
          "Bei 0 °C und 1000 hPa sind das 6,5 K/km, bei 20 °C nur noch "
          "4,2 K/km, bei −40 °C fast wieder 9,8 K/km, weil kaum noch "
          "Dampf da ist. Das Mittel über die Troposphäre ist eben jener "
          "Standardgradient von 6,5 K/km: Die Atmosphäre liegt dort, wo "
          "die feuchte Konvektion sie hinstellt.\n\n"
          "Was ist beim Kondensieren erhalten? Nicht θ -- das Paket "
          "gewinnt Entropie aus der latenten Wärme. Die Erhaltungsgröße "
          "ist die **äquivalentpotentielle Temperatur** "
          "$\\theta_e \\approx \\theta\\,\\exp(L_v r/(c_p T))$: die potentielle Temperatur, die "
          "das Paket hätte, wenn man allen Dampf auskondensieren ließe. "
          "Bei 14,8 g/kg und 293 K ist der Exponent 0,126, θ_e also 13 % "
          "über θ -- rund 38 K. So viel Wärme steckt in der Feuchte eines "
          "Sommertages, und ein Gewitter holt sie heraus.",
          "A parcel rises from the ground. Its temperature falls at "
          "9.8 K/km. Its dew point falls too, but more slowly: the mixing "
          "ratio stays constant, the vapour pressure `e` falls in "
          "proportion to the pressure, and through Clausius–Clapeyron "
          "that gives $dT_d/dz \\approx -1.7$ K/km. The spread `T − T_d` thus "
          "closes at 8.1 K/km, and the **lifting condensation level** "
          "lies at\n\n"
          r"$$z_{LCL} \approx 125\ \frac{\mathrm{m}}{\mathrm{K}}\cdot(T - T_d)$$" "\n\n"
          "That is the base of every cumulus cloud, and it can be "
          "predicted from the ground with a thermometer and the dew point "
          "-- glider pilots do it every morning.\n\n"
          "Above it vapour condenses, and the released latent heat "
          "$L_v = 2.5$ MJ/kg slows the cooling. The **moist adiabatic "
          "lapse rate** is therefore smaller than the dry one:\n\n"
          r"$$\Gamma_s = \Gamma_d\;\frac{1 + \dfrac{L_v\,r_s}{R_L\,T}}{1 + \dfrac{0.622\,L_v^2\,r_s}{c_p\,R_L\,T^2}}$$" "\n\n"
          "At 0 °C and 1000 hPa that is 6.5 K/km, at 20 °C only 4.2 K/km, "
          "at −40 °C almost 9.8 K/km again because hardly any vapour is "
          "left. The mean over the troposphere is precisely that standard "
          "lapse rate of 6.5 K/km: the atmosphere sits where moist "
          "convection puts it.\n\n"
          "What is conserved during condensation? Not θ -- the parcel "
          "gains entropy from the latent heat. The conserved quantity is "
          "the **equivalent potential temperature** "
          "$\\theta_e \\approx \\theta\\,\\exp(L_v r/(c_p T))$: the potential temperature the "
          "parcel would have if all its vapour were condensed out. At "
          "14.8 g/kg and 293 K the exponent is 0.126, so θ_e is 13 % "
          "above θ -- about 38 K. That much heat sits in the humidity of "
          "a summer day, and a thunderstorm takes it out."),
        "skizze-hebung", [
        zahl(t("Am Boden 24 °C, Taupunkt 12 °C. Höhe der Wolkenbasis "
               "nach der 125-m-Regel? (in m)",
               "At the ground 24 °C, dew point 12 °C. Cloud base height "
               "by the 125 m rule? (in m)"),
             rund(LCL_FAUST), t("m", "m"),
             t("`12 K × 125 m/K = 1500 m` über Grund.",
               "`12 K × 125 m/K = 1500 m` above ground."),
             toleranz=0.02),
        zahl(t("Feuchtadiabatischer Gradient bei 0 °C und 1000 hPa "
               "(r_s = 3,8 g/kg)? (in K/km, eine Nachkommastelle)",
               "Moist adiabatic lapse rate at 0 °C and 1000 hPa "
               "(r_s = 3.8 g/kg)? (in K/km, one decimal)"),
             rund(GAMMA_S_0, 1), t("K/km", "K/km"),
             t("Zähler `1 + 2,5·10⁶ × 0,0038 / (287 × 273) = 1,121`; "
               "Nenner `1 + 6,25·10¹² × 0,0038 × 0,622 / (1004 × 287 × "
               "273²) = 1,688`; `Γ_s = 9,77 × 1,121 / 1,688 = 6,5 K/km`.",
               "Numerator `1 + 2.5·10⁶ × 0.0038 / (287 × 273) = 1.121`; "
               "denominator `1 + 6.25·10¹² × 0.0038 × 0.622 / (1004 × 287 "
               "× 273²) = 1.688`; `Γ_s = 9.77 × 1.121 / 1.688 = 6.5 K/km`."),
             toleranz=0.05),
        mc(t("Warum ist der feuchtadiabatische Gradient in den Tropen "
             "kleiner als in der Arktis?",
             "Why is the moist adiabatic lapse rate smaller in the "
             "tropics than in the Arctic?"),
           [t("Warme gesättigte Luft enthält exponentiell mehr Dampf, "
              "also wird je Meter Hebung mehr latente Wärme frei.",
              "Warm saturated air holds exponentially more vapour, so "
              "more latent heat is released per metre of lift."),
            t("Weil g am Äquator kleiner ist.",
              "Because g is smaller at the equator."),
            t("Weil die Tropopause höher liegt.",
              "Because the tropopause is higher."),
            t("Er ist überall gleich, 6,5 K/km.",
              "It is the same everywhere, 6.5 K/km.")], 0,
           t("Bei 25 °C trägt gesättigte Luft 20 g/kg, bei −20 °C nur "
             "0,8 g/kg. Entsprechend 4 K/km gegen 9 K/km. Deshalb ist die "
             "tropische Troposphäre fast feuchtadiabatisch und sehr hoch.",
             "At 25 °C saturated air carries 20 g/kg, at −20 °C only "
             "0.8 g/kg. Correspondingly 4 K/km against 9 K/km. That is "
             "why the tropical troposphere is nearly moist adiabatic and "
             "very deep.")),
        ]),

    lektion("fe-emagram",
        t("Das Emagramm, CAPE und bedingte Labilität",
          "The emagram, CAPE and conditional instability"),
        ["emagramm", "cape", "bedingt-labil"],
        t("Das Werkzeug, das alles Bisherige auf ein Blatt bringt, ist "
          "das thermodynamische Diagramm -- **Emagramm**, Skew-T oder "
          "Stüve, je nach Achsenwahl. Waagrecht die Temperatur, senkrecht "
          "`ln p` (so dass die Höhe ungefähr linear ist). Eingezeichnet "
          "sind Trockenadiabaten (θ = const), Feuchtadiabaten (θ_e = "
          "const) und Linien gleichen Sättigungsmischungsverhältnisses. "
          "Darauf trägt man den gemessenen Aufstieg ein: Temperatur und "
          "Taupunkt der Radiosonde.\n\n"
          "Nun die Paketmethode grafisch: Vom Bodenwert aus folgt das "
          "Paket der Trockenadiabate, bis es die Mischungsverhältnislinie "
          "seines Taupunkts trifft -- das ist das **LCL**. Ab dort folgt "
          "es der Feuchtadiabate. Solange die Paketkurve **links** der "
          "Umgebungskurve liegt, ist das Paket kälter: Es muss gehoben "
          "werden, die Fläche zwischen den Kurven ist die **CIN** "
          "(convective inhibition, Energie, die der Deckel kostet). Wo "
          "die Paketkurve die Umgebung kreuzt, ist das **Niveau freier "
          "Konvektion**; ab da ist das Paket wärmer, steigt von selbst, "
          "und die Fläche bis zum erneuten Kreuzen (Gleichgewichtsniveau, "
          "meist nahe der Tropopause) ist die **CAPE**:\n\n"
          r"$$\mathrm{CAPE} = \int g\,\frac{T_v' - T_v}{T_v}\,dz$$" "\n\n"
          "in J/kg. Energetisch ist das die maximale Aufwindenergie, "
          "$w_{max} = \\sqrt{2\\,\\mathrm{CAPE}}$: bei 1000 J/kg sind das 45 m/s; "
          "tatsächlich erreicht ein Aufwind etwa die Hälfte, weil "
          "Einmischung und Wasserlast bremsen. 500 J/kg: Schauer. 1500: "
          "kräftige Gewitter. Über 3000: Hagel und Superzellen.\n\n"
          "Damit ist der dritte Stabilitätsfall benannt: **bedingt "
          "labil**, $\\Gamma_s < \\Gamma < \\Gamma_d$. Trocken stabil, gesättigt labil. "
          "Die Standardatmosphäre mit 6,5 K/km ist genau das -- und das "
          "ist der Normalzustand der Erde. Die Atmosphäre ist ein "
          "geladener Zustand, der auf einen Auslöser wartet: Hebung über "
          "Berge, Fronten, Konvergenz oder einfach die Mittagssonne, die "
          "die CIN wegheizt.",
          "The tool that brings everything so far onto one sheet is the "
          "thermodynamic diagram -- **emagram**, skew-T or Stüve, "
          "depending on the choice of axes. Horizontal the temperature, "
          "vertical `ln p` (so that height is roughly linear). Drawn in "
          "are dry adiabats (θ = const), moist adiabats (θ_e = const) and "
          "lines of equal saturation mixing ratio. Onto it one plots the "
          "measured ascent: temperature and dew point from the "
          "radiosonde.\n\n"
          "Now the parcel method graphically: from the surface value the "
          "parcel follows the dry adiabat until it meets the mixing-ratio "
          "line of its dew point -- that is the **LCL**. From there it "
          "follows the moist adiabat. As long as the parcel curve lies "
          "to the **left** of the environment curve the parcel is "
          "colder: it has to be lifted, and the area between the curves "
          "is the **CIN** (convective inhibition, the energy the lid "
          "costs). Where the parcel curve crosses the environment is the "
          "**level of free convection**; from there the parcel is "
          "warmer, rises by itself, and the area up to the next crossing "
          "(equilibrium level, usually near the tropopause) is the "
          "**CAPE**:\n\n"
          r"$$\mathrm{CAPE} = \int g\,\frac{T_v' - T_v}{T_v}\,dz$$" "\n\n"
          "in J/kg. Energetically this is the maximum updraught energy, "
          "$w_{max} = \\sqrt{2\\,\\mathrm{CAPE}}$: at 1000 J/kg that is 45 m/s; in reality "
          "an updraught reaches about half, because entrainment and "
          "water loading slow it. 500 J/kg: showers. 1500: strong "
          "thunderstorms. Over 3000: hail and supercells.\n\n"
          "That names the third stability case: **conditionally "
          "unstable**, $\\Gamma_s < \\Gamma < \\Gamma_d$. Stable dry, unstable saturated. "
          "The standard atmosphere at 6.5 K/km is exactly that -- and it "
          "is the Earth's normal state. The atmosphere is a loaded state "
          "waiting for a trigger: lifting over mountains, fronts, "
          "convergence, or simply the midday sun burning away the CIN."),
        "skizze-emagramm", [
        zahl(t("CAPE = 1000 J/kg. Theoretische maximale "
               "Aufwindgeschwindigkeit? (in m/s)",
               "CAPE = 1000 J/kg. Theoretical maximum updraught speed? "
               "(in m/s)"),
             rund(W_MAX_1000), t("m/s", "m/s"),
             t("`w = √(2 × 1000) = 44,7 m/s`. Real etwa die Hälfte -- "
               "immer noch genug, um Hagel von 2 cm in der Schwebe zu "
               "halten.",
               "`w = √(2 × 1000) = 44.7 m/s`. In reality about half -- "
               "still enough to hold 2 cm hail aloft."),
             toleranz=0.03),
        mc(t("Ein Aufstieg zeigt 7 K/km vom Boden bis zur Tropopause, "
             "die Luft ist feucht. Was gilt?",
             "A sounding shows 7 K/km from the ground to the tropopause "
             "and the air is moist. What holds?"),
           [t("Bedingt labil: Trocken stabil, aber ein gesättigtes Paket "
              "wird wärmer als die Umgebung -- Gewitter sind möglich, "
              "wenn etwas die Hebung auslöst.",
              "Conditionally unstable: stable dry, but a saturated parcel "
              "becomes warmer than its surroundings -- thunderstorms are "
              "possible if something triggers the lift."),
            t("Absolut stabil, 7 ist kleiner als 9,8.",
              "Absolutely stable, 7 is less than 9.8."),
            t("Absolut labil, 7 ist größer als 6,5.",
              "Absolutely unstable, 7 is more than 6.5."),
            t("Neutral.", "Neutral.")], 0,
           t("Zwischen Γ_s (etwa 5-6 K/km in warmer Luft) und Γ_d "
             "(9,8 K/km) liegt die bedingte Labilität. Entscheidend ist "
             "dann die CIN: Wie viel Hebung nötig ist, bis das Paket das "
             "Niveau freier Konvektion erreicht.",
             "Between Γ_s (about 5-6 K/km in warm air) and Γ_d "
             "(9.8 K/km) lies conditional instability. What decides is "
             "then the CIN: how much lifting it takes until the parcel "
             "reaches the level of free convection.")),
        ]),
    ])


# ===========================================================================
# 4  Strahlung
# ===========================================================================

T_EFFEKTIV = (S_0 * (1 - 0.30) / (4 * SIGMA)) ** 0.25      # K
T_EINSCHICHT = T_EFFEKTIV * 2 ** 0.25                       # K
WIEN_SONNE_NM = 2.898e-3 / 5772.0 * 1e9
WIEN_ERDE_UM = 2.898e-3 / 288.0 * 1e6
ANTRIEB_2XCO2 = 5.35 * math.log(2.0)                        # W/m²
DT_OHNE_RUECKKOPPLUNG = ANTRIEB_2XCO2 / (4 * SIGMA * T_EFFEKTIV ** 3)
AUSSTRAHLUNG_BODEN_288 = SIGMA * 288.0 ** 4                 # W/m²
NACHTKUEHLUNG = 60.0 * 3600.0 * 8 / (1.2 * C_P * 200.0)     # K bei 60 W/m² netto, 8 h, 200 m Schicht

K_STRAHLUNG = kapitel(
    "strahlung", t("Strahlung", "Radiation"), 4,
    t("Die einzige Energiequelle ist die Sonne, der einzige Ausgang ist "
      "Infrarot ins All. Dazwischen liegt eine Atmosphäre, die für das "
      "eine durchsichtig ist und für das andere nicht. Aus Planck und "
      "Stefan-Boltzmann folgen die 255 K, die 288 K und der Tagesgang.",
      "The only energy source is the sun, the only exit is infrared to "
      "space. In between lies an atmosphere transparent to one and not to "
      "the other. From Planck and Stefan–Boltzmann follow the 255 K, the "
      "288 K and the diurnal cycle."), [

    lektion("st-bilanz",
        t("Sonne, Albedo und die Strahlungstemperatur",
          "Sun, albedo and the radiative temperature"),
        ["solarkonstante", "strahlungsgleichgewicht", "albedo"],
        t("Die Sonne strahlt als schwarzer Körper mit 5772 K; nach Wien "
          "liegt ihr Maximum bei $\\lambda = 2898\\ \\mathrm{\\mu m\\,K}/5772\\ \\mathrm{K} = 0{,}50\\ \\mathrm{\\mu m}$, "
          "mitten im Sichtbaren -- unsere Augen sind an die Sonne "
          "angepasst, nicht umgekehrt. Nach Stefan-Boltzmann strahlt sie "
          "$\\sigma T^4 = 6{,}3\\cdot 10^7$ W/m² ab; auf die Erdbahn verdünnt mit "
          "$(R_{Sonne}/1\\ \\mathrm{AE})^2$ bleiben davon $S_0 = 1361$ W/m², die "
          "**Solarkonstante**.\n\n"
          "Die Erde fängt davon ihre Querschnittsfläche `π·R²` auf, "
          "strahlt aber über die Kugelfläche `4π·R²` ab: Im Mittel kommen "
          "also $S_0/4 = 340$ W/m² an. Davon wird die **Albedo** $A = 0{,}30$ "
          "reflektiert (Wolken, Schnee, Wüsten), 238 W/m² werden "
          "absorbiert. Im Gleichgewicht muss dieselbe Leistung als "
          "Infrarot abgestrahlt werden:\n\n"
          r"$$\sigma\,T_e^4 = \frac{S_0\,(1 - A)}{4} \quad\Rightarrow\quad T_e = 255\ \mathrm{K}$$" "\n\n"
          "Das ist die **effektive Strahlungstemperatur** der Erde, "
          "−18 °C. Von außen, aus dem Infrarot gesehen, *ist* die Erde "
          "so kalt -- die 255 K sind die Temperatur in etwa 5 km Höhe, "
          "von wo im Mittel die Strahlung ins All entkommt. Dass es am "
          "Boden 288 K sind, 33 K mehr, ist der Treibhauseffekt, und der "
          "kommt gleich.\n\n"
          "Das Erdspektrum liegt nach Wien bei $2898/288 = 10\\ \\mathrm{\\mu m}$, im "
          "thermischen Infrarot. Sonnen- und Erdstrahlung überlappen "
          "praktisch nicht (die Sonne unter 4 μm, die Erde darüber); "
          "deshalb spricht man von **kurz-** und **langwelliger** "
          "Strahlung, und deshalb kann ein Gas für die eine durchsichtig "
          "sein und die andere schlucken.\n\n"
          "Die Albedo ist der größte Hebel und der unsicherste Wert: "
          "Meer 0,06, Wald 0,15, Wüste 0,3, Wolken 0,5, Neuschnee 0,85. "
          "Ein Prozent Albedo sind 3,4 W/m² -- so viel wie eine "
          "Verdopplung des CO₂.",
          "The sun radiates as a black body at 5772 K; by Wien its "
          "maximum lies at $\\lambda = 2898\\ \\mathrm{\\mu m\\,K}/5772\\ \\mathrm{K} = 0.50\\ \\mathrm{\\mu m}$, in the "
          "middle of the visible -- our eyes are adapted to the sun, not "
          "the other way round. By Stefan–Boltzmann it emits "
          "$\\sigma T^4 = 6.3\\cdot 10^7$ W/m²; diluted to Earth's orbit by "
          "$(R_{sun}/1\\ \\mathrm{AU})^2$ that leaves $S_0 = 1361$ W/m², the **solar "
          "constant**.\n\n"
          "The Earth intercepts that over its cross-section `π·R²` but "
          "radiates over its surface `4π·R²`: on average $S_0/4 = 340$ W/m² "
          "arrive. Of this the **albedo** $A = 0.30$ is reflected (clouds, "
          "snow, deserts), 238 W/m² are absorbed. In equilibrium the same "
          "power must be emitted as infrared:\n\n"
          r"$$\sigma\,T_e^4 = \frac{S_0\,(1 - A)}{4} \quad\Rightarrow\quad T_e = 255\ \mathrm{K}$$" "\n\n"
          "That is the **effective radiative temperature** of the Earth, "
          "−18 °C. Seen from outside, in the infrared, the Earth *is* "
          "that cold -- the 255 K is the temperature at about 5 km, from "
          "where on average the radiation escapes to space. That the "
          "surface is at 288 K, 33 K more, is the greenhouse effect, and "
          "that comes next.\n\n"
          "The Earth's spectrum peaks by Wien at $2898/288 = 10\\ \\mathrm{\\mu m}$, in "
          "the thermal infrared. Solar and terrestrial radiation hardly "
          "overlap (the sun below 4 μm, the Earth above); hence one speaks "
          "of **shortwave** and **longwave** radiation, and hence a gas "
          "can be transparent to one and absorb the other.\n\n"
          "The albedo is the biggest lever and the least certain value: "
          "sea 0.06, forest 0.15, desert 0.3, clouds 0.5, fresh snow 0.85. "
          "One per cent of albedo is 3.4 W/m² -- as much as a doubling of "
          "CO₂."),
        "skizze-bilanz", [
        zahl(t("Effektive Strahlungstemperatur der Erde für S₀ = 1361 W/m² "
               "und Albedo 0,30? (in K)",
               "Effective radiative temperature of the Earth for "
               "S₀ = 1361 W/m² and albedo 0.30? (in K)"),
             rund(T_EFFEKTIV), t("K", "K"),
             t("`T_e = [1361 × 0,7 / (4 × 5,67·10⁻⁸)]^(1/4) = "
               "(4,20·10⁹)^(1/4) = 254,6 K`.",
               "`T_e = [1361 × 0.7 / (4 × 5.67·10⁻⁸)]^(1/4) = "
               "(4.20·10⁹)^(1/4) = 254.6 K`."),
             toleranz=0.01),
        mc(t("Die Albedo stiege von 0,30 auf 0,31. Was passiert mit der "
             "effektiven Temperatur?",
             "The albedo rises from 0.30 to 0.31. What happens to the "
             "effective temperature?"),
           [t("Sie sinkt um rund 0,9 K -- ein Prozent Albedo sind "
              "3,4 W/m² weniger Absorption.",
              "It drops by about 0.9 K -- one per cent of albedo is "
              "3.4 W/m² less absorption."),
            t("Sie steigt, weil mehr reflektiert wird.",
              "It rises, because more is reflected."),
            t("Sie bleibt gleich, die Albedo wirkt nur auf das Licht.",
              "It stays the same, albedo acts only on light."),
            t("Sie sinkt um 10 K.", "It drops by 10 K.")], 0,
           t("`dT/T = dF/(4F)`: 1,4 % weniger absorbierte Leistung geben "
             "0,36 % weniger Temperatur, also 0,9 K von 255 K. Die "
             "Eis-Albedo-Rückkopplung macht aus dieser Zahl eine "
             "Verstärkung: kälter heißt mehr Schnee heißt mehr Albedo.",
             "`dT/T = dF/(4F)`: 1.4 % less absorbed power gives 0.36 % "
             "less temperature, that is 0.9 K out of 255 K. The ice–albedo "
             "feedback turns this number into an amplifier: colder means "
             "more snow means more albedo.")),
        ]),

    lektion("st-treibhaus",
        t("Der Treibhauseffekt im Einschichtmodell",
          "The greenhouse effect in the one-layer model"),
        ["treibhaus", "einschichtmodell", "strahlungsantrieb"],
        t("Das einfachste Modell, das die 33 K erklärt: eine Atmosphäre "
          "als **eine Schicht**, durchsichtig für Sonnenlicht, schwarz "
          "für Infrarot. Sie absorbiert alles, was der Boden abstrahlt, "
          "und strahlt selbst mit ihrer Temperatur `T_a` nach oben und "
          "nach unten. Die Bilanz oben: Was ins All geht, ist nur die "
          "Schichtstrahlung, $\\sigma T_a^4 = S_0(1-A)/4$, also `T_a = T_e = "
          "255 K`. Die Bilanz am Boden: Er bekommt Sonne plus die "
          "Gegenstrahlung der Schicht, `σT_s⁴ = S₀(1−A)/4 + σT_a⁴ = "
          "2σT_a⁴`. Daraus\n\n"
          r"$$T_s = 2^{1/4}\,T_e = 303\ \mathrm{K}$$" "\n\n"
          "Das ist zu warm -- 30 °C statt 15 °C. Der Fehler ist "
          "lehrreich: Die reale Atmosphäre ist im Infrarot nicht völlig "
          "schwarz (das atmosphärische Fenster bei 8-12 μm lässt rund "
          "40 W/m² direkt vom Boden ins All), und vor allem transportiert "
          "**Konvektion** Wärme vom Boden nach oben, 100 W/m² als "
          "latente und fühlbare Wärme. Ohne Konvektion hätte die Erde "
          "ein Strahlungsgleichgewicht mit viel steilerem Gradienten; "
          "die Konvektion stellt den feuchtadiabatischen ein und kühlt "
          "den Boden auf 288 K.\n\n"
          "Das Modell liefert trotzdem die richtige Mechanik: Treibhaus"
          "gase heben die **Abstrahlungshöhe**. Mehr absorbierendes Gas "
          "heißt, dass die Strahlung ins All im Mittel aus größerer Höhe "
          "kommt; dort ist es kälter, die Erde strahlt weniger ab, und "
          "die ganze Säule muss sich erwärmen, bis die Abstrahlungshöhe "
          "wieder 255 K hat. Bei 6,5 K/km Gradient heißt jede 100 m "
          "höhere Abstrahlungshöhe 0,65 K am Boden.\n\n"
          "Quantitativ: Der **Strahlungsantrieb** einer CO₂-Verdopplung "
          "ist $\\Delta F = 5{,}35\\ \\mathrm{W/m^2}\\cdot\\ln(C/C_0) = 3{,}7$ W/m². Logarithmisch, "
          "weil die Bandzentren längst gesättigt sind und nur die "
          "Bandflügel noch mehr absorbieren. Ohne Rückkopplungen folgt "
          "aus $\\Delta T = \\Delta F/(4\\sigma T_e^3) = 1{,}0$ K; mit Wasserdampf (der "
          "wichtigsten Rückkopplung: wärmer heißt nach Clausius-Clapeyron "
          "7 % mehr Dampf je Kelvin, und Dampf ist das stärkste "
          "Treibhausgas), Wolken und Eis kommen 2,5 bis 4 K heraus.",
          "The simplest model that explains the 33 K: an atmosphere as "
          "**one layer**, transparent to sunlight, black to infrared. It "
          "absorbs everything the ground emits and itself radiates at "
          "its temperature `T_a` upward and downward. The balance at the "
          "top: what goes to space is only the layer's radiation, "
          "$\\sigma T_a^4 = S_0(1-A)/4$, so $T_a = T_e = 255$ K. The balance at "
          "the ground: it receives sun plus the layer's back radiation, "
          "$\\sigma T_s^4 = S_0(1-A)/4 + \\sigma T_a^4 = 2\\sigma T_a^4$. Hence\n\n"
          r"$$T_s = 2^{1/4}\,T_e = 303\ \mathrm{K}$$" "\n\n"
          "That is too warm -- 30 °C instead of 15 °C. The error is "
          "instructive: the real atmosphere is not fully black in the "
          "infrared (the atmospheric window at 8-12 μm lets about 40 W/m² "
          "go straight from the ground to space), and above all "
          "**convection** carries heat upward from the ground, 100 W/m² "
          "as latent and sensible heat. Without convection the Earth "
          "would have a radiative equilibrium with a much steeper lapse "
          "rate; convection establishes the moist adiabatic one and "
          "cools the ground to 288 K.\n\n"
          "The model still gives the right mechanism: greenhouse gases "
          "raise the **emission height**. More absorbing gas means that "
          "the radiation to space comes on average from a greater "
          "height; it is colder there, the Earth emits less, and the "
          "whole column has to warm until the emission height is back at "
          "255 K. At a 6.5 K/km lapse rate every 100 m of higher emission "
          "height means 0.65 K at the ground.\n\n"
          "Quantitatively: the **radiative forcing** of a CO₂ doubling is "
          "$\\Delta F = 5.35\\ \\mathrm{W/m^2}\\cdot\\ln(C/C_0) = 3.7$ W/m². Logarithmic, because "
          "the band centres are long saturated and only the band wings "
          "absorb more. Without feedbacks $\\Delta T = \\Delta F/(4\\sigma T_e^3) = 1.0$ K "
          "follows; with water vapour (the most important feedback: "
          "warmer means 7 % more vapour per kelvin by Clausius–Clapeyron, "
          "and vapour is the strongest greenhouse gas), clouds and ice "
          "the result is 2.5 to 4 K."),
        "skizze-einschicht", [
        zahl(t("Einschichtmodell: Bodentemperatur bei T_e = 255 K? (in K)",
               "One-layer model: surface temperature for T_e = 255 K? "
               "(in K)"),
             rund(255.0 * 2 ** 0.25), t("K", "K"),
             t("`T_s = 2^(1/4) × 255 = 1,189 × 255 = 303 K`. Zu warm, "
               "weil das Modell weder das Fenster noch die Konvektion "
               "kennt.",
               "`T_s = 2^(1/4) × 255 = 1.189 × 255 = 303 K`. Too warm, "
               "because the model knows neither the window nor "
               "convection."),
             toleranz=0.01),
        zahl(t("Strahlungsantrieb von 3,7 W/m², keine Rückkopplungen: "
               "Erwärmung ΔT = ΔF/(4σT_e³) mit T_e = 255 K? (in K, eine "
               "Nachkommastelle)",
               "Radiative forcing of 3.7 W/m², no feedbacks: warming "
               "ΔT = ΔF/(4σT_e³) with T_e = 255 K? (in K, one decimal)"),
             rund(3.7 / (4 * SIGMA * 255.0 ** 3), 1), t("K", "K"),
             t("`4σT³ = 4 × 5,67·10⁻⁸ × 1,66·10⁷ = 3,76 W/(m²·K)`, also "
               "`ΔT = 3,7 / 3,76 = 1,0 K`. Das ist die Planck-Antwort; "
               "alles darüber sind Rückkopplungen.",
               "`4σT³ = 4 × 5.67·10⁻⁸ × 1.66·10⁷ = 3.76 W/(m²·K)`, so "
               "`ΔT = 3.7 / 3.76 = 1.0 K`. That is the Planck response; "
               "everything beyond it is feedback."),
             toleranz=0.05),
        mc(t("Warum erwärmt mehr CO₂ den Boden, obwohl die Erde nach "
             "außen weiter mit 255 K strahlen muss?",
             "Why does more CO₂ warm the ground even though the Earth "
             "must still radiate at 255 K to space?"),
           [t("Die Abstrahlungshöhe steigt; bei festem Gradienten liegt "
              "der Boden dann weiter unter dem 255-K-Niveau.",
              "The emission height rises; at a fixed lapse rate the "
              "ground then lies further below the 255 K level."),
            t("CO₂ absorbiert Sonnenlicht.",
              "CO₂ absorbs sunlight."),
            t("CO₂ erhöht die Wärmekapazität der Luft.",
              "CO₂ raises the heat capacity of the air."),
            t("Es erwärmt den Boden nicht, nur die Stratosphäre.",
              "It does not warm the ground, only the stratosphere.")], 0,
           t("Die 255 K bleiben, sie wandern nur nach oben. Der Gradient "
             "darunter ist durch Konvektion festgelegt, also muss der "
             "Boden wärmer werden. Die Stratosphäre darüber wird dabei "
             "übrigens kälter -- gemessen, und ein Fingerabdruck des "
             "Mechanismus.",
             "The 255 K stays, it just moves upward. The lapse rate "
             "below it is fixed by convection, so the ground must warm. "
             "The stratosphere above cools in the process -- measured, "
             "and a fingerprint of the mechanism.")),
        ]),

    lektion("st-tagesgang",
        t("Der Tagesgang: Strahlungsbilanz am Boden",
          "The diurnal cycle: the surface radiation budget"),
        ["tagesgang", "strahlungsnebel", "bodeninversion"],
        t("Am Boden lautet die Bilanz $Q = (1-A)\\,S + L_\\downarrow - L_\\uparrow$, mit `S` "
          "der Sonnenstrahlung, `L↓` der Gegenstrahlung der Atmosphäre "
          "und $L_\\uparrow = \\sigma T_s^4$ der Ausstrahlung des Bodens (390 W/m² bei "
          "288 K). Nachts ist `S = 0`, und übrig bleibt $L_\\downarrow - L_\\uparrow$: Bei "
          "klarem Himmel strahlt die Atmosphäre mit rund 300 W/m² "
          "zurück, der Boden verliert netto 60 bis 100 W/m². Unter einer "
          "Wolkendecke dagegen kommt `L↓` von der Wolkenbasis, fast so "
          "warm wie der Boden, und der Verlust schrumpft auf 10 W/m². "
          "**Deshalb sind klare Nächte kalt und bewölkte mild** -- die "
          "Wolke ist eine Decke, im Wortsinn.\n\n"
          "Was der Boden verliert, holt er aus der Luft darüber. Weil "
          "Luft schlecht leitet, kühlt zuerst nur die unterste Schicht: "
          "Nach einer klaren Nacht ist es in 2 m Höhe 5 bis 10 K kälter "
          "als in 200 m -- die **Bodeninversion**. Mit 60 W/m² über acht "
          "Stunden und einer 200 m dicken Schicht: `ΔT = 60 × 28 800 / "
          "(1,2 × 1004 × 200) = 7 K`. Sinkt dabei die Temperatur unter "
          "den Taupunkt, kondensiert der Dampf: erst als **Tau** auf "
          "dem Gras (das Gras strahlt am besten aus und ist am "
          "kältesten), dann in der Luft als **Strahlungsnebel**, der sich "
          "in Senken sammelt, weil kalte Luft abfließt. Unter 0 °C: Reif "
          "statt Tau, und bei vorher gefallenem Taupunkt überspringt der "
          "Dampf die Flüssigphase -- Reif ohne Tau, das ist Resublimation.\n\n"
          "Morgens kehrt sich alles um. Die Sonne heizt den Boden, "
          "der die Luft, die Inversion wird von unten aufgefressen, "
          "der Nebel hebt sich zu Stratus und löst sich auf. Ab Mittag "
          "ist die Grenzschicht durchmischt, 1 bis 2 km dick, mit "
          "konstanter θ, und oben drauf wachsen die ersten Cumuli am "
          "Kondensationsniveau. Das Temperaturmaximum kommt erst gegen "
          "15 Uhr, weil der Boden so lange noch mehr bekommt, als er "
          "verliert -- die Bilanz, nicht die Einstrahlung, bestimmt die "
          "Temperatur.\n\n"
          "Über dem Meer gibt es das alles kaum: Wasser mischt die Wärme "
          "in 50 m Tiefe, der Tagesgang der Temperatur ist ein halbes "
          "Kelvin. Deshalb ist Seeklima ausgeglichen und Wüste extrem.",
          "At the ground the budget reads $Q = (1-A)\\,S + L_\\downarrow - L_\\uparrow$, with "
          "`S` the solar radiation, `L↓` the atmosphere's back radiation "
          "and $L_\\uparrow = \\sigma T_s^4$ the ground's emission (390 W/m² at 288 K). "
          "At night `S = 0`, leaving $L_\\downarrow - L_\\uparrow$: under a clear sky the "
          "atmosphere radiates back about 300 W/m², the ground loses "
          "60 to 100 W/m² net. Under a cloud deck, by contrast, `L↓` "
          "comes from the cloud base, almost as warm as the ground, and "
          "the loss shrinks to 10 W/m². **That is why clear nights are "
          "cold and cloudy ones mild** -- the cloud is a blanket, "
          "literally.\n\n"
          "What the ground loses it takes from the air above. Because "
          "air conducts badly, only the lowest layer cools at first: "
          "after a clear night it is 5 to 10 K colder at 2 m than at "
          "200 m -- the **surface inversion**. With 60 W/m² over eight "
          "hours and a 200 m layer: `ΔT = 60 × 28 800 / (1.2 × 1004 × "
          "200) = 7 K`. If the temperature falls below the dew point, "
          "vapour condenses: first as **dew** on the grass (grass "
          "radiates best and is coldest), then in the air as **radiation "
          "fog**, which collects in hollows because cold air drains. "
          "Below 0 °C: frost instead of dew, and if the dew point was "
          "already below zero the vapour skips the liquid phase -- hoar "
          "frost without dew, that is deposition.\n\n"
          "In the morning everything reverses. The sun heats the ground, "
          "the ground the air, the inversion is eaten from below, the "
          "fog lifts into stratus and dissolves. By noon the boundary "
          "layer is mixed, 1 to 2 km deep, with constant θ, and on top "
          "of it the first cumuli grow at the condensation level. The "
          "temperature maximum comes only around 15:00, because until "
          "then the ground still gains more than it loses -- the budget, "
          "not the insolation, sets the temperature.\n\n"
          "Over the sea hardly any of this happens: water mixes the heat "
          "down to 50 m, the diurnal temperature range is half a kelvin. "
          "That is why maritime climate is even and desert climate "
          "extreme."),
        "skizze-tagesgang", [
        zahl(t("Netto-Ausstrahlung 60 W/m² über 8 Stunden kühlt eine "
               "200 m dicke Schicht (ρ = 1,2 kg/m³, c_p = 1004). Um wie "
               "viel Kelvin? (eine Nachkommastelle)",
               "A net loss of 60 W/m² over 8 hours cools a 200 m layer "
               "(ρ = 1.2 kg/m³, c_p = 1004). By how many kelvin? (one "
               "decimal)"),
             rund(NACHTKUEHLUNG, 1), t("K", "K"),
             t("`ΔT = Q·t / (ρ·c_p·h) = 60 × 28 800 / (1,2 × 1004 × 200) "
               "= 7,2 K`. In Wirklichkeit konzentriert sich die Kühlung "
               "auf die untersten Dekameter, dort sind es mehr.",
               "`ΔT = Q·t / (ρ·c_p·h) = 60 × 28 800 / (1.2 × 1004 × 200) "
               "= 7.2 K`. In reality the cooling concentrates in the "
               "lowest tens of metres, where it is more."),
             toleranz=0.03),
        mc(t("Zwei Nächte, gleiche Luftmasse: eine klar, eine mit "
             "tiefer Stratus-Decke. Welche wird kälter, und warum?",
             "Two nights, same air mass: one clear, one with a low "
             "stratus deck. Which gets colder, and why?"),
           [t("Die klare -- der Boden strahlt 390 W/m² ins All und "
              "bekommt nur etwa 300 zurück; die Wolke strahlt fast so "
              "viel zurück, wie der Boden abgibt.",
              "The clear one -- the ground radiates 390 W/m² to space "
              "and gets only about 300 back; the cloud returns almost "
              "as much as the ground emits."),
            t("Die bewölkte -- Wolken schirmen die Wärme ab.",
              "The cloudy one -- clouds shield the heat."),
            t("Beide gleich, nachts gibt es keine Strahlung.",
              "Both the same, there is no radiation at night."),
            t("Das hängt nur vom Wind ab.",
              "That depends only on the wind.")], 0,
           t("Die Bilanz $L_\\downarrow - L_\\uparrow$ entscheidet. Eine Wolkenbasis bei "
             "10 °C strahlt mit 364 W/m² zurück, der klare Himmel "
             "effektiv mit 300. Der Unterschied von 60 W/m² ist genau "
             "die Nachtkühlung der klaren Nacht.",
             "The budget $L_\\downarrow - L_\\uparrow$ decides. A cloud base at 10 °C "
             "radiates 364 W/m² back, the clear sky effectively 300. The "
             "60 W/m² difference is exactly the night cooling of the "
             "clear night.")),
        ]),
    ])


# ===========================================================================
# 5  Wolken und Niederschlag
# ===========================================================================

OBERFLAECHENSPANNUNG = 0.0756   # N/m bei 0 °C
def kelvin_faktor(r_m, T=273.15):
    return math.exp(2 * OBERFLAECHENSPANNUNG / (R_V * 1000.0 * T * r_m))
KELVIN_01 = kelvin_faktor(0.1e-6)
KELVIN_001 = kelvin_faktor(0.01e-6)
STOKES_10UM = 2.0 / 9.0 * 1000.0 * G * (10e-6) ** 2 / 1.8e-5   # m/s
# Diffusionswachstum: r² = r₀² + 2·ξ·S·t; ξ ≈ 6·10⁻¹³ m²/s je Prozent
# Übersättigung bei 0 °C (Herleitung in herleitungen.py)
XI_PROZENT = 6.0e-13
ZEIT_1_10 = ((10e-6) ** 2 - (1e-6) ** 2) / (2 * XI_PROZENT * 0.5)   # s

K_WOLKEN = kapitel(
    "wolken", t("Wolken und Niederschlag", "Clouds and precipitation"), 5,
    t("Warum Wasserdampf überhaupt kondensiert, obwohl die Thermodynamik "
      "reiner Tröpfchen es verbietet; warum ein Tropfen eine Million Mal "
      "wachsen muss, um zu fallen; und welche der zehn Wolkengattungen "
      "einem was über die Luft darüber sagt.",
      "Why water vapour condenses at all although the thermodynamics of "
      "pure droplets forbids it; why a drop must grow a million-fold to "
      "fall; and which of the ten cloud genera tells you what about the "
      "air above."), [

    lektion("wo-tropfen",
        t("Kelvin, Köhler und die Kondensationskerne",
          "Kelvin, Köhler and condensation nuclei"),
        ["kelvin-gleichung", "koehler", "kondensationskerne"],
        t("Über einem gekrümmten Tröpfchen ist der Sättigungsdampfdruck "
          "höher als über der ebenen Fläche: Die Oberflächenspannung "
          "presst, und ein Molekül am Rand hat weniger Nachbarn, die es "
          "halten. Die **Kelvin-Gleichung** sagt, um wie viel:\n\n"
          r"$$\frac{e_s(r)}{e_s(\infty)} = \exp\!\left(\frac{2\sigma}{\rho_w\,R_v\,T\,r}\right)$$" "\n\n"
          "Bei 0,1 μm ist das 1,1 % Übersättigung, bei 0,01 μm schon "
          "12 %. Ein Tropfen aus reinem Wasser, der durch Zufall aus ein "
          "paar hundert Molekülen entsteht, hat also einen Dampfdruck weit "
          "über dem der Umgebung und verdampft sofort. Homogene "
          "Nukleation bräuchte 300 bis 400 % relative Feuchte. In der "
          "Atmosphäre werden aber selten mehr als 101 % gemessen. Also "
          "kondensiert Wasser **nie** aus sich selbst.\n\n"
          "Es braucht **Kondensationskerne**: Aerosole, auf denen die "
          "Krümmung von Anfang an klein ist, und besser noch solche, die "
          "sich lösen. Ein gelöstes Salz **senkt** den Dampfdruck "
          "(Raoult: proportional zum Molenbruch des Wassers), und zwar "
          "um so mehr, je kleiner der Tropfen, weil die Lösung dann "
          "konzentrierter ist. Beide Effekte zusammen sind die "
          "**Köhler-Kurve**: Bei kleinen Radien gewinnt der Lösungseffekt "
          "(Dampfdruck unter 100 %, der Tropfen ist stabil, auch in "
          "ungesättigter Luft -- Dunst), bei großen Radien gewinnt die "
          "Krümmung, und dazwischen liegt ein Maximum, die **kritische "
          "Übersättigung**: Für einen Salzkern von 0,1 μm etwa 0,1 %, "
          "für 0,01 μm etwa 1 %. Darüber hinaus wächst der Tropfen von "
          "selbst, er ist **aktiviert**.\n\n"
          "Die Folge: Die Übersättigung in einer Wolke pendelt sich bei "
          "0,1 bis 1 % ein, denn sobald sie höher wird, aktivieren mehr "
          "Kerne und fressen den Dampf weg. Über dem Meer gibt es 100 "
          "Kerne je cm³ (Seesalz, Sulfat aus Plankton), über Land 1000, "
          "über Städten 10 000. Mehr Kerne heißt mehr und kleinere "
          "Tropfen bei gleichem Wasser -- hellere Wolken, die schlechter "
          "regnen. Das ist der Grund, warum Schiffsspuren auf "
          "Satellitenbildern zu sehen sind.",
          "Over a curved droplet the saturation vapour pressure is "
          "higher than over a flat surface: surface tension squeezes, "
          "and a molecule at the edge has fewer neighbours to hold it. "
          "The **Kelvin equation** says by how much:\n\n"
          r"$$\frac{e_s(r)}{e_s(\infty)} = \exp\!\left(\frac{2\sigma}{\rho_w\,R_v\,T\,r}\right)$$" "\n\n"
          "At 0.1 μm that is 1.1 % supersaturation, at 0.01 μm already "
          "12 %. A pure-water drop that forms by chance from a few "
          "hundred molecules therefore has a vapour pressure far above "
          "that of its surroundings and evaporates at once. Homogeneous "
          "nucleation would need 300 to 400 % relative humidity. In the "
          "atmosphere more than 101 % is rarely measured. So water "
          "**never** condenses by itself.\n\n"
          "It needs **condensation nuclei**: aerosols on which the "
          "curvature is small from the start, and better still ones that "
          "dissolve. A dissolved salt **lowers** the vapour pressure "
          "(Raoult: proportional to the mole fraction of water), and the "
          "more so the smaller the drop, because the solution is then "
          "more concentrated. Both effects together are the **Köhler "
          "curve**: at small radii the solution effect wins (vapour "
          "pressure below 100 %, the drop is stable even in unsaturated "
          "air -- haze), at large radii the curvature wins, and in "
          "between lies a maximum, the **critical supersaturation**: for "
          "a 0.1 μm salt nucleus about 0.1 %, for 0.01 μm about 1 %. "
          "Beyond it the drop grows by itself; it is **activated**.\n\n"
          "The consequence: the supersaturation in a cloud settles at "
          "0.1 to 1 %, because as soon as it rises more nuclei activate "
          "and eat the vapour away. Over the sea there are 100 nuclei "
          "per cm³ (sea salt, sulphate from plankton), over land 1000, "
          "over cities 10 000. More nuclei mean more and smaller drops "
          "for the same water -- brighter clouds that rain less well. "
          "That is why ship tracks are visible on satellite images."),
        "skizze-koehler", [
        zahl(t("Kelvin-Effekt: Übersättigung über einem reinen "
               "Wassertröpfchen von r = 0,1 μm bei 0 °C "
               "(σ = 0,0756 N/m, R_v = 461,5)? (in %, eine "
               "Nachkommastelle)",
               "Kelvin effect: supersaturation over a pure water droplet "
               "of r = 0.1 μm at 0 °C (σ = 0.0756 N/m, R_v = 461.5)? "
               "(in %, one decimal)"),
             rund((KELVIN_01 - 1) * 100, 1), t("%", "%"),
             t("Exponent `2 × 0,0756 / (1000 × 461,5 × 273 × 10⁻⁷) = "
               "0,0120`, also `exp(0,012) − 1 = 1,2 %`. Bei 1 μm ist es "
               "nur noch 0,12 %: Ab dort spielt die Krümmung keine Rolle "
               "mehr.",
               "Exponent `2 × 0.0756 / (1000 × 461.5 × 273 × 10⁻⁷) = "
               "0.0120`, so `exp(0.012) − 1 = 1.2 %`. At 1 μm it is only "
               "0.12 %: from there on curvature no longer matters."),
             toleranz=0.1),
        mc(t("Warum regnet eine Wolke über dem Meer leichter als "
             "dieselbe Wassermenge über einer Stadt?",
             "Why does a cloud over the sea rain more readily than the "
             "same amount of water over a city?"),
           [t("Weniger Kondensationskerne, also weniger und größere "
              "Tropfen -- und große Tropfen fallen und sammeln.",
              "Fewer condensation nuclei, so fewer and larger drops -- "
              "and large drops fall and collect."),
            t("Über dem Meer ist die Luft feuchter.",
              "The air over the sea is moister."),
            t("Über der Stadt ist es zu warm zum Regnen.",
              "It is too warm to rain over the city."),
            t("Das stimmt nicht, Städte regnen mehr.",
              "That is not true, cities rain more.")], 0,
           t("Gleiches Wasser auf zehnmal mehr Kerne verteilt heißt "
             "Tropfen mit halbem Radius. Die Fallgeschwindigkeit geht "
             "mit r², das Einsammeln mit r⁴ -- die Stadtwolke bleibt "
             "länger in der Schwebe.",
             "The same water spread over ten times as many nuclei means "
             "drops of half the radius. Fall speed goes as r², "
             "collection as r⁴ -- the city cloud stays suspended "
             "longer.")),
        ]),

    lektion("wo-wachstum",
        t("Vom Tröpfchen zum Regentropfen",
          "From droplet to raindrop"),
        ["diffusionswachstum", "bergeron", "koaleszenz"],
        t("Ein Wolkentröpfchen hat 10 μm Radius, ein Regentropfen 1 mm: "
          "hundertmal größer, eine **Million** mal mehr Masse. Wie "
          "schafft das die Wolke in einer halben Stunde?\n\n"
          "Zuerst durch **Diffusion**: Dampf diffundiert zum Tropfen, die "
          "Kondensationswärme muss weg. Die Lösung der Diffusionsgleichung "
          "um eine Kugel gibt $r\\,dr/dt = \\xi S$, mit `S` der Übersättigung "
          "und $\\xi \\approx 6\\cdot 10^{-13}$ m²/s je Prozent. Also $r^2 = r_0^2 + 2\\xi S t$: Der "
          "Radius wächst mit $\\sqrt{t}$, und zwar **immer langsamer**. Von 1 "
          "auf 10 μm bei 0,5 % dauert es knapp drei Minuten -- gut. Von 10 "
          "auf 100 μm aber 100-mal länger, fast fünf Stunden, und auf 1 mm "
          "bräuchte es drei Wochen. "
          "Diffusion macht Wolken, keinen Regen.\n\n"
          "Der zweite Weg ist der **Bergeron-Findeisen-Prozess**, und er "
          "braucht Eis. Über Eis ist der Sättigungsdampfdruck niedriger "
          "als über unterkühltem Wasser (bei −12 °C um 12 %, das Maximum "
          "des Unterschieds). In einer Mischwolke, in der neben Millionen "
          "unterkühlter Tröpfchen ein paar Eiskristalle schweben, ist "
          "die Luft für Wasser gesättigt, für Eis aber um 12 % "
          "**übersättigt**: Die Kristalle wachsen auf Kosten der Tropfen, "
          "die verdampfen und den Dampf nachliefern. Ein Kristall ist in "
          "Minuten so groß, dass er fällt, sammelt unterwegs Tröpfchen "
          "auf (Bereifung, bis zum Graupel) und schmilzt unter der "
          "Nullgradgrenze zum Regen. **Der meiste Regen der mittleren "
          "Breiten war einmal Schnee.** Eiskeime sind noch seltener als "
          "Kondensationskerne -- Mineralstaub, bestimmte Bakterien -- und "
          "erst unter −10 °C aktiv; unter −38 °C gefriert alles von "
          "selbst. Deshalb bleiben viele Wolken bis −20 °C flüssig, und "
          "deshalb vereist ein Flugzeug darin.\n\n"
          "Der dritte Weg braucht kein Eis: **Koaleszenz**. Ein Tropfen, "
          "der größer ist als die anderen, fällt schneller (Stokes: "
          "$v = 2\\rho_w g r^2/(9\\eta)$, bei 10 μm 1 cm/s, bei 50 μm 25 cm/s) und "
          "sammelt die kleinen ein. Die Masse wächst mit dem Querschnitt "
          "mal der Relativgeschwindigkeit, also etwa mit $r^4$ -- das "
          "läuft, einmal gestartet, davon. In warmen tropischen Wolken "
          "ist das der einzige Weg, und er reicht: aus einem 1 km dicken "
          "Cumulus über dem Meer regnet es nach 20 Minuten.",
          "A cloud droplet has a radius of 10 μm, a raindrop 1 mm: a "
          "hundred times larger, a **million** times more mass. How does "
          "a cloud manage that in half an hour?\n\n"
          "First by **diffusion**: vapour diffuses to the drop and the "
          "condensation heat has to be carried away. The solution of the "
          "diffusion equation around a sphere gives $r\\,dr/dt = \\xi S$, "
          "with `S` the supersaturation and $\\xi \\approx 6\\cdot 10^{-13}$ m²/s per per "
          "cent. So $r^2 = r_0^2 + 2\\xi S t$: the radius grows with $\\sqrt{t}$, and "
          "**ever more slowly**. From 1 to 10 μm at 0.5 % takes under three "
          "minutes -- fine. From 10 to 100 μm, however, 100 times longer, "
          "nearly five hours, and to 1 mm three weeks. Diffusion makes clouds, not "
          "rain.\n\n"
          "The second route is the **Bergeron–Findeisen process**, and it "
          "needs ice. Over ice the saturation vapour pressure is lower "
          "than over supercooled water (at −12 °C by 12 %, the maximum "
          "of the difference). In a mixed cloud where a few ice crystals "
          "float among millions of supercooled droplets, the air is "
          "saturated with respect to water but **supersaturated** by "
          "12 % with respect to ice: the crystals grow at the expense of "
          "the drops, which evaporate and resupply the vapour. Within "
          "minutes a crystal is large enough to fall, collects droplets "
          "on the way (riming, up to graupel) and melts to rain below "
          "the freezing level. **Most mid-latitude rain was once snow.** "
          "Ice nuclei are even rarer than condensation nuclei -- mineral "
          "dust, certain bacteria -- and only active below −10 °C; below "
          "−38 °C everything freezes by itself. That is why many clouds "
          "stay liquid down to −20 °C, and why an aircraft ices up in "
          "them.\n\n"
          "The third route needs no ice: **coalescence**. A drop larger "
          "than the others falls faster (Stokes: $v = 2\\rho_w g r^2/(9\\eta)$, "
          "1 cm/s at 10 μm, 25 cm/s at 50 μm) and sweeps up the small "
          "ones. Its mass grows with its cross-section times the "
          "relative speed, roughly as $r^4$ -- once started, it runs "
          "away. In warm tropical clouds this is the only route, and it "
          "suffices: a 1 km deep cumulus over the sea rains after 20 "
          "minutes."),
        "skizze-wachstum", [
        zahl(t("Diffusionswachstum r² = r₀² + 2ξSt mit ξ = 6·10⁻¹³ m²/s je "
               "Prozent, S = 0,5 %. Zeit von 1 μm auf 10 μm? (in s)",
               "Diffusion growth r² = r₀² + 2ξSt with ξ = 6·10⁻¹³ m²/s per "
               "per cent, S = 0.5 %. Time from 1 μm to 10 μm? (in s)"),
             rund(ZEIT_1_10), t("s", "s"),
             t("`t = (r² − r₀²)/(2ξS) = (10⁻¹⁰ − 10⁻¹²)/(2 × 6·10⁻¹³ × 0,5) "
               "= 165 s ≈ 2,8 min`. Von 10 auf 100 μm wären es 4,6 "
               "Stunden, auf 1 mm 19 Tage -- Diffusion allein regnet nie.",
               "`t = (r² − r₀²)/(2ξS) = (10⁻¹⁰ − 10⁻¹²)/(2 × 6·10⁻¹³ × 0.5) "
               "= 165 s ≈ 2.8 min`. From 10 to 100 μm it would be 4.6 "
               "hours, to 1 mm 19 days -- diffusion alone never rains."),
             toleranz=0.05),
        zahl(t("Stokes-Fallgeschwindigkeit eines Tröpfchens mit "
               "r = 10 μm (η = 1,8·10⁻⁵ Pa·s, ρ_w = 1000)? (in cm/s, eine "
               "Nachkommastelle)",
               "Stokes fall speed of a droplet with r = 10 μm "
               "(η = 1.8·10⁻⁵ Pa·s, ρ_w = 1000)? (in cm/s, one decimal)"),
             rund(STOKES_10UM * 100, 1), t("cm/s", "cm/s"),
             t("`v = 2 × 1000 × 9,81 × 10⁻¹⁰ / (9 × 1,8·10⁻⁵) = "
               "0,0121 m/s = 1,2 cm/s`. Ein Aufwind von 1 m/s trägt das "
               "mühelos; die Wolke schwebt.",
               "`v = 2 × 1000 × 9.81 × 10⁻¹⁰ / (9 × 1.8·10⁻⁵) = "
               "0.0121 m/s = 1.2 cm/s`. An updraught of 1 m/s carries "
               "that effortlessly; the cloud floats."),
             toleranz=0.05),
        mc(t("Warum wachsen in einer Mischwolke bei −12 °C die "
             "Eiskristalle auf Kosten der Tröpfchen?",
             "Why do ice crystals grow at the expense of droplets in a "
             "mixed cloud at −12 °C?"),
           [t("Der Sättigungsdampfdruck über Eis ist niedriger als über "
              "Wasser; für die Kristalle ist dieselbe Luft übersättigt.",
              "The saturation vapour pressure over ice is lower than "
              "over water; for the crystals the same air is "
              "supersaturated."),
            t("Eis ist schwerer und fällt schneller.",
              "Ice is heavier and falls faster."),
            t("Die Tröpfchen gefrieren beim Berühren.",
              "The droplets freeze on contact."),
            t("Eis hat eine größere Oberfläche.",
              "Ice has a larger surface.")], 0,
           t("Das ist Bergeron-Findeisen: 12 % Unterschied bei −12 °C, "
             "genug, dass ein Kristall in Minuten fallbereit ist. Ohne "
             "Eiskeime bleibt die Wolke dagegen bis −38 °C flüssig und "
             "regnet nicht.",
             "That is Bergeron–Findeisen: 12 % difference at −12 °C, "
             "enough for a crystal to be ready to fall within minutes. "
             "Without ice nuclei the cloud instead stays liquid down to "
             "−38 °C and does not rain.")),
        ]),

    lektion("wo-gattungen",
        t("Die zehn Gattungen, und was sie verraten",
          "The ten genera, and what they give away"),
        ["wolkengattungen", "stockwerke-wolken"],
        t("Luke Howard hat 1802 die Wolken nach ihrer **Form** benannt, "
          "und die Form ist Physik: Haufen (*cumulus*) heißt Konvektion, "
          "Schicht (*stratus*) heißt stabile Hebung oder Abkühlung, "
          "Faser (*cirrus*) heißt Eis, Regen (*nimbus*) heißt "
          "Niederschlag. Die Vorsilben geben das Stockwerk: ohne = tief "
          "(unter 2 km), *alto-* = mittel (2-7 km), *cirro-* = hoch "
          "(über 7 km, immer Eis).\n\n"
          "**Cumulus humilis**: flache Haufen mit scharfer Basis am "
          "Kondensationsniveau. Konvektion, die an einer Inversion "
          "endet. Schönwetter. **Cumulus congestus**: dieselbe Konvektion "
          "ohne Deckel, blumenkohlartig, Schauer möglich. "
          "**Cumulonimbus**: der Turm hat die Tropopause erreicht und "
          "breitet sich als Amboss aus; die faserige Spitze ist "
          "vereist, und ab da gilt Bergeron-Findeisen: Platzregen, "
          "Hagel, Blitz.\n\n"
          "**Stratus**: eine gleichförmige tiefe Schicht, oft gehobener "
          "Nebel. **Stratocumulus**: eine Schicht, die in Ballen "
          "zerfallen ist -- unter einer Absinkinversion, die die "
          "Konvektion flachdrückt. Die häufigste Wolke der Welt, über "
          "den kalten Ozeanen. **Nimbostratus**: dicke graue Schicht "
          "mit Dauerregen, die Warmfront.\n\n"
          "**Altostratus**: die Sonne scheint durch wie durch Milchglas. "
          "Warmfront in 6 Stunden. **Altocumulus**: mittelhohe Ballen; "
          "als *castellanus* mit Türmchen das Zeichen für Labilität in "
          "der Höhe und Gewitter am Nachmittag; als *lenticularis* die "
          "stehende Linse im Lee eines Berges, die Welle sichtbar "
          "gemacht.\n\n"
          "**Cirrus**: Eisfasern, ausgekämmt vom Höhenwind, der "
          "Vorbote einer Warmfront, 12 bis 24 Stunden voraus. "
          "**Cirrostratus**: Eisschleier mit Halo -- ein 22°-Ring um die "
          "Sonne, den die Optik später erklärt. **Cirrocumulus**: feine "
          "Schäfchen, selten, Instabilität in 8 km.\n\n"
          "Aus der Reihenfolge am Himmel liest man die Front: Cirrus, "
          "Cirrostratus, Altostratus, Nimbostratus -- die klassische "
          "Warmfront, 1000 km lang, tiefer werdend. Umgekehrt der "
          "plötzliche Cumulonimbus mit Böenfront: die Kaltfront. Und "
          "der Cumulus humilis, der am Nachmittag nicht größer wird: "
          "ein Hoch mit Absinken darüber, das Wetter hält.",
          "Luke Howard named the clouds in 1802 by their **form**, and "
          "the form is physics: heap (*cumulus*) means convection, layer "
          "(*stratus*) means stable lifting or cooling, fibre (*cirrus*) "
          "means ice, rain (*nimbus*) means precipitation. The prefixes "
          "give the level: none = low (below 2 km), *alto-* = middle "
          "(2-7 km), *cirro-* = high (above 7 km, always ice).\n\n"
          "**Cumulus humilis**: flat heaps with a sharp base at the "
          "condensation level. Convection ending at an inversion. Fair "
          "weather. **Cumulus congestus**: the same convection without a "
          "lid, cauliflower-like, showers possible. **Cumulonimbus**: the "
          "tower has reached the tropopause and spreads out as an anvil; "
          "the fibrous top is glaciated, and from then on Bergeron–"
          "Findeisen applies: downpour, hail, lightning.\n\n"
          "**Stratus**: a uniform low layer, often lifted fog. "
          "**Stratocumulus**: a layer broken into rolls -- under a "
          "subsidence inversion that flattens the convection. The most "
          "common cloud in the world, over the cold oceans. "
          "**Nimbostratus**: thick grey layer with steady rain, the warm "
          "front.\n\n"
          "**Altostratus**: the sun shines through as through frosted "
          "glass. Warm front in 6 hours. **Altocumulus**: mid-level "
          "rolls; as *castellanus* with turrets the sign of instability "
          "aloft and thunderstorms in the afternoon; as *lenticularis* "
          "the standing lens in the lee of a mountain, the wave made "
          "visible.\n\n"
          "**Cirrus**: ice fibres combed out by the upper wind, the "
          "herald of a warm front 12 to 24 hours ahead. **Cirrostratus**: "
          "an ice veil with a halo -- a 22° ring around the sun that "
          "optics explains later. **Cirrocumulus**: fine ripples, rare, "
          "instability at 8 km.\n\n"
          "From the sequence in the sky one reads the front: cirrus, "
          "cirrostratus, altostratus, nimbostratus -- the classic warm "
          "front, 1000 km long and thickening. Conversely the sudden "
          "cumulonimbus with gust front: the cold front. And the cumulus "
          "humilis that does not grow during the afternoon: a high with "
          "subsidence above, the weather holds."),
        "cu-zyklus", [
        mc(t("Cirrus, dann Cirrostratus mit Halo, dann Altostratus: "
             "Welche Entwicklung kündigt sich an?",
             "Cirrus, then cirrostratus with a halo, then altostratus: "
             "what is coming?"),
           [t("Eine Warmfront -- warme Luft gleitet auf, die Wolken "
              "werden tiefer und dichter, Dauerregen folgt.",
              "A warm front -- warm air is sliding up, the clouds get "
              "lower and denser, steady rain follows."),
            t("Eine Kaltfront mit Gewittern.",
              "A cold front with thunderstorms."),
            t("Ein stabiles Hoch.", "A stable high."),
            t("Föhn.", "Foehn.")], 0,
           t("Die Warmfront ist eine flache Rampe (1:100 bis 1:300): Die "
             "Hebung beginnt 1000 km voraus in der Höhe und arbeitet "
             "sich nach unten.",
             "The warm front is a shallow ramp (1:100 to 1:300): the "
             "lifting starts 1000 km ahead at height and works its way "
             "down."),
           bild="cirrus"),
        mc(t("Die Spitze eines Cumulus congestus wird faserig. Was ist "
             "physikalisch passiert?",
             "The top of a cumulus congestus turns fibrous. What has "
             "happened physically?"),
           [t("Die Wolke ist dort vereist; Bergeron-Findeisen setzt ein, "
              "aus der Wolke wird ein Cumulonimbus.",
              "The cloud has glaciated there; Bergeron–Findeisen sets in "
              "and the cloud becomes a cumulonimbus."),
            t("Die Wolke löst sich auf.", "The cloud is dissolving."),
            t("Der Wind zerreißt sie.", "The wind is tearing it apart."),
            t("Sie hat das Kondensationsniveau erreicht.",
              "It has reached the condensation level.")], 0,
           t("Flüssige Tropfen bleiben klein und machen scharfe Ränder; "
             "Eiskristalle wachsen und fallen und machen Fasern. Die "
             "faserige Spitze ist der Moment, in dem die Wolke zu regnen "
             "beginnt.",
             "Liquid drops stay small and make sharp edges; ice crystals "
             "grow and fall and make fibres. The fibrous top is the "
             "moment the cloud starts to rain."),
           bild="cumulonimbus"),
        ]),
    ])


# ===========================================================================
# 6  Dynamik
# ===========================================================================

F_45 = 2 * OMEGA * math.sin(math.radians(45.0))              # 1/s
F_60 = 2 * OMEGA * math.sin(math.radians(60.0))
V_GEO = 1.0 / (1.2 * F_45) * (400.0 / 400000.0)              # m/s: 4 hPa je 400 km
ROSSBY = 10.0 / (F_45 * 1.0e6)                               # U=10 m/s, L=1000 km
TRAEGHEITSPERIODE_45 = 2 * math.pi / F_45 / 3600.0           # h
# Thermischer Wind: Δu über 500-1000 hPa bei 1 K je 100 km Temperaturgefälle
DU_THERMISCH = R_L / F_45 * (1.0 / 100000.0) * math.log(1000.0 / 500.0)
EKMAN_TIEFE = math.pi * math.sqrt(2 * 10.0 / F_45)           # m, K = 10 m²/s
GRADIENTWIND_ZYKLONAL = None  # (Rechnung in der Aufgabe selbst)

K_DYNAMIK = kapitel(
    "dynamik", t("Dynamik auf der rotierenden Erde",
                 "Dynamics on the rotating Earth"), 6,
    t("Warum der Wind nicht vom Hoch zum Tief weht, sondern um sie herum. "
      "Die Coriolis-Kraft wird hergeleitet, nicht behauptet; danach "
      "folgen geostrophischer Wind, Gradientwind, thermischer Wind und "
      "die Reibung, die das Tief am Ende doch auffüllt.",
      "Why the wind does not blow from high to low but around them. The "
      "Coriolis force is derived, not asserted; after it follow the "
      "geostrophic wind, gradient wind, thermal wind and the friction "
      "that fills the low in the end."), [

    lektion("dy-coriolis",
        t("Die Coriolis-Kraft, hergeleitet",
          "The Coriolis force, derived"),
        ["coriolis", "rotierendes-system", "rossby-zahl"],
        t("Die Erde dreht sich einmal am Tag, und wir beschreiben den Wind "
          "in einem Koordinatensystem, das sich mitdreht. Newtons "
          "Gleichung gilt aber nur im Inertialsystem. Also muss man die "
          "Zeitableitung umrechnen -- und dabei entstehen zwei "
          "Scheinkräfte, die kein Beobachter von außen sieht, die aber "
          "jeder Wind spürt.\n\n"
          "Der ganze Weg steht in der Herleitung unten. Das Ergebnis ist "
          "die Bewegungsgleichung im rotierenden System:\n\n"
          r"$$\frac{d\vec v}{dt} = -\frac{1}{\rho}\nabla p "
          r"- 2\vec\Omega\times\vec v - \vec\Omega\times(\vec\Omega\times\vec r) + \vec g^* + \vec F$$"
          "\n\n"
          "Der Term " r"$-2\vec\Omega\times\vec v$" " ist die **Coriolis-Beschleunigung**. "
          "Sie steht senkrecht auf der Geschwindigkeit, leistet also "
          "keine Arbeit und ändert nur die Richtung: auf der Nordhalbkugel "
          "nach **rechts**, auf der Südhalbkugel nach links. Der "
          "Zentrifugalterm " r"$-\vec\Omega\times(\vec\Omega\times\vec r)$" " hängt "
          "nicht von der Bewegung ab; er wird in die Schwerkraft "
          "eingerechnet (" r"$\vec g^*$" ", deshalb ist die Erde abgeplattet und "
          r"$g$" " am Äquator um 0,5 % kleiner).\n\n"
          "Für die Meteorologie zählt nur die Horizontalkomponente. "
          "Zerlegt man " r"$\vec\Omega$" " in die lokalen Richtungen (Herleitung "
          "unten), bleibt vom Kreuzprodukt für die waagrechte Bewegung "
          "der **Coriolis-Parameter**\n\n"
          r"$$f = 2\,\Omega\,\sin\varphi$$"
          "\n\n"
          "mit " r"$\Omega = 7{,}29\cdot 10^{-5}\,\mathrm{s^{-1}}$" " und der "
          "geographischen Breite " r"$\varphi$" ". In 45° ist "
          r"$f = 1{,}03\cdot 10^{-4}\,\mathrm{s^{-1}}$" "; am Äquator null -- dort gibt "
          "es keine Ablenkung und deshalb keine Hurrikane; sie entstehen "
          "erst ab 5° Breite. Die Beschleunigung ist " r"$f\cdot v$" ": bei "
          "10 m/s nur " r"$10^{-3}\,\mathrm{m/s^2}$" ", ein Zehntausendstel von "
          r"$g$" ". Winzig -- aber sie wirkt stundenlang, immer quer, und "
          "nichts hält dagegen. Nach einer **Trägheitsperiode** "
          r"$2\pi/f$" ", in 45° sind das 17 Stunden, hat sie ein Luftpaket "
          "einmal im Kreis geführt.\n\n"
          "Ob die Rotation zählt, sagt die **Rossby-Zahl** "
          r"$Ro = U/(fL)$" ", das Verhältnis von Trägheits- zu "
          "Coriolis-Beschleunigung. Für ein Tief mit " r"$U = 10$" " m/s und "
          r"$L = 1000$" " km ist " r"$Ro = 0{,}1$" ": Rotation dominiert. Für eine "
          "Gewitterzelle (10 km) ist " r"$Ro = 10$" ", für das Wasser im "
          "Waschbecken " r"$10^{5}$" " -- das Abfluss-Märchen ist eines.",
          "The Earth turns once a day, and we describe the wind in a "
          "coordinate system that turns with it. Newton's equation, "
          "however, holds only in an inertial frame. So the time "
          "derivative has to be converted -- and in doing so two "
          "fictitious forces appear that no outside observer sees but "
          "every wind feels.\n\n"
          "The whole route is in the derivation below. The result is the "
          "equation of motion in the rotating frame:\n\n"
          r"$$\frac{d\vec v}{dt} = -\frac{1}{\rho}\nabla p "
          r"- 2\vec\Omega\times\vec v - \vec\Omega\times(\vec\Omega\times\vec r) + \vec g^* + \vec F$$"
          "\n\n"
          "The term " r"$-2\vec\Omega\times\vec v$" " is the **Coriolis "
          "acceleration**. It is perpendicular to the velocity, so it does "
          "no work and only changes direction: to the **right** in the "
          "northern hemisphere, to the left in the southern. The "
          "centrifugal term " r"$-\vec\Omega\times(\vec\Omega\times\vec r)$"
          " does not depend on the motion; it is folded into gravity "
          "(" r"$\vec g^*$" ", which is why the Earth is flattened and "
          r"$g$" " is 0.5 % smaller at the equator).\n\n"
          "For meteorology only the horizontal component counts. "
          "Decomposing " r"$\vec\Omega$" " into the local directions "
          "(derivation below), what remains of the cross product for "
          "horizontal motion is the **Coriolis parameter**\n\n"
          r"$$f = 2\,\Omega\,\sin\varphi$$"
          "\n\n"
          "with " r"$\Omega = 7.29\cdot 10^{-5}\,\mathrm{s^{-1}}$" " and the "
          "latitude " r"$\varphi$" ". At 45° "
          r"$f = 1.03\cdot 10^{-4}\,\mathrm{s^{-1}}$" "; at the equator zero "
          "-- there is no deflection there and hence no hurricanes; they "
          "form only from 5° latitude. The acceleration is " r"$f\cdot v$"
          ": at 10 m/s only " r"$10^{-3}\,\mathrm{m/s^2}$" ", a ten-thousandth "
          "of " r"$g$" ". Tiny -- but it acts for hours, always sideways, and "
          "nothing resists it. After one **inertial period** "
          r"$2\pi/f$" ", 17 hours at 45°, it has led a parcel once around a "
          "circle.\n\n"
          "Whether rotation matters is told by the **Rossby number** "
          r"$Ro = U/(fL)$" ", the ratio of inertial to Coriolis "
          "acceleration. For a low with " r"$U = 10$" " m/s and "
          r"$L = 1000$" " km, " r"$Ro = 0.1$" ": rotation dominates. For a "
          "thunderstorm cell (10 km) " r"$Ro = 10$" ", for the water in a "
          "basin " r"$10^{5}$" " -- the drain myth is one."),
        "skizze-coriolis", [
        zahl(t("Coriolis-Parameter in 60° Nord? (Ω = 7,292·10⁻⁵ /s; in "
               "10⁻⁴ /s, zwei Nachkommastellen)",
               "Coriolis parameter at 60° north? (Ω = 7.292·10⁻⁵ /s; in "
               "10⁻⁴ /s, two decimals)"),
             rund(F_60 * 1e4, 2), t("10⁻⁴/s", "10⁻⁴/s"),
             t("`f = 2 × 7,292·10⁻⁵ × sin 60° = 1,458·10⁻⁴ × 0,866 = "
               "1,26·10⁻⁴ /s`.",
               "`f = 2 × 7.292·10⁻⁵ × sin 60° = 1.458·10⁻⁴ × 0.866 = "
               "1.26·10⁻⁴ /s`."),
             toleranz=0.02),
        zahl(t("Trägheitsperiode 2π/f in 45° Breite? (in Stunden, eine "
               "Nachkommastelle)",
               "Inertial period 2π/f at 45° latitude? (in hours, one "
               "decimal)"),
             rund(TRAEGHEITSPERIODE_45, 1), t("h", "h"),
             t("`f = 1,031·10⁻⁴ /s`, `2π/f = 60 900 s = 16,9 h`. Am Pol "
               "wären es 12 h -- der halbe Tag, nicht der ganze, weil die "
               "2 in 2Ω steckt.",
               "`f = 1.031·10⁻⁴ /s`, `2π/f = 60 900 s = 16.9 h`. At the "
               "pole it would be 12 h -- half a day, not a whole one, "
               "because of the 2 in 2Ω."),
             toleranz=0.02),
        mc(t("Warum leistet die Coriolis-Kraft keine Arbeit?",
             "Why does the Coriolis force do no work?"),
           [t("Sie steht immer senkrecht auf der Geschwindigkeit: "
              "−2Ω×v · v = 0.",
              "It is always perpendicular to the velocity: "
              "−2Ω×v · v = 0."),
            t("Weil sie eine Scheinkraft ist.",
              "Because it is a fictitious force."),
            t("Weil sie zu klein ist.", "Because it is too small."),
            t("Sie leistet Arbeit, nur sehr wenig.",
              "It does do work, just very little.")], 0,
           t("Das Spatprodukt eines Vektors mit sich selbst ist null. "
             "Die Coriolis-Kraft kann einen Wind beliebig weit umlenken, "
             "aber weder beschleunigen noch bremsen -- deshalb kreist "
             "ein Paket im Trägheitskreis mit konstantem Betrag.",
             "The triple product of a vector with itself is zero. The "
             "Coriolis force can turn a wind as far as it likes but "
             "neither speed it up nor slow it down -- which is why a "
             "parcel circles the inertial circle at constant speed.")),
        ]),

    lektion("dy-geostrophisch",
        t("Geostrophischer Wind und Gradientwind",
          "Geostrophic and gradient wind"),
        ["geostrophisch", "gradientwind", "buys-ballot"],
        t("Großräumig (" r"$Ro \ll 1$" ") und ohne Reibung bleiben in der "
          "Horizontalen zwei Terme übrig: Druckgradient und Coriolis. "
          "Sind sie im Gleichgewicht, gibt es keine Beschleunigung, und "
          "der Wind weht **parallel zu den Isobaren**:\n\n"
          r"$$v_g = \frac{1}{\rho f}\,\frac{\partial p}{\partial n}$$"
          "\n\n"
          "mit " r"$n$" " der Richtung quer zu den Isobaren. Das ist der "
          "**geostrophische Wind**. Vier Hektopascal auf 400 km (ein "
          "typischer Isobarenabstand auf der Bodenkarte) geben in 45° "
          "Breite " r"$v_g = 400/(1{,}2\cdot 1{,}03\cdot 10^{-4}\cdot 4\cdot 10^{5}) = 8$"
          " m/s. Die Richtung folgt dem Vorzeichen des Kreuzprodukts: "
          "Auf der Nordhalbkugel liegt das Tief **links** vom Wind. Das "
          "ist die **Regel von Buys-Ballot**: Mit dem Rücken zum Wind ist "
          "das Tief links vorn. Umgekehrt: Wind um ein Tief gegen den "
          "Uhrzeigersinn, um ein Hoch im Uhrzeigersinn -- und auf der "
          "Südhalbkugel genau andersherum.\n\n"
          "Das Gleichgewicht ist eine Konsequenz, keine Ursache: Luft, "
          "die vom Hoch zum Tief startet, wird nach rechts gelenkt, bis "
          "Coriolis und Druckgradient sich gegenüberstehen. Nach etwa "
          "einer Trägheitsperiode ist sie dort. Deshalb ist der reale "
          "Wind in der freien Atmosphäre auf 10-20 % geostrophisch, und "
          "deshalb kann man aus einer Höhenkarte den Wind ablesen.\n\n"
          "Auf gekrümmten Bahnen kommt die Zentripetalbeschleunigung "
          r"$v^2/R$" " hinzu: der **Gradientwind**. Um ein Tief hilft die "
          "Coriolis-Kraft, die Kurve zu halten; der Druckgradient muss "
          "beides liefern, und der Wind ist **sub**geostrophisch. Um ein "
          "Hoch zeigt die Coriolis-Kraft nach außen, muss also "
          "Zentripetalkraft *und* Druckgradient übertreffen: der Wind "
          "ist **super**geostrophisch -- aber nur bis zu einer Grenze. "
          "Die quadratische Gleichung hat für das Hoch nur eine Lösung, "
          "wenn " r"$|\partial p/\partial n| < \rho f^2 R/4$" " ist: Ein Hoch "
          "kann keinen starken Druckgradienten tragen. **Deshalb sind "
          "Hochs groß, flach und windschwach, Tiefs klein, tief und "
          "stürmisch.** Ein Hurrikan ist ein Tief mit 50 hPa auf 50 km; "
          "ein Hoch dieser Stärke ist physikalisch unmöglich.",
          "On the large scale (" r"$Ro \ll 1$" ") and without friction two "
          "terms remain in the horizontal: pressure gradient and "
          "Coriolis. If they balance, there is no acceleration and the "
          "wind blows **parallel to the isobars**:\n\n"
          r"$$v_g = \frac{1}{\rho f}\,\frac{\partial p}{\partial n}$$"
          "\n\n"
          "with " r"$n$" " the direction across the isobars. That is the "
          "**geostrophic wind**. Four hectopascals over 400 km (a "
          "typical isobar spacing on a surface chart) give at 45° "
          r"$v_g = 400/(1.2\cdot 1.03\cdot 10^{-4}\cdot 4\cdot 10^{5}) = 8$"
          " m/s. The direction follows the sign of the cross product: "
          "in the northern hemisphere the low lies to the **left** of "
          "the wind. That is **Buys-Ballot's law**: with your back to "
          "the wind, the low is on your left. Equivalently: wind around "
          "a low anticlockwise, around a high clockwise -- and in the "
          "southern hemisphere the other way round.\n\n"
          "The balance is a consequence, not a cause: air that sets "
          "off from high to low is turned to the right until Coriolis "
          "and pressure gradient face each other. After about one "
          "inertial period it is there. That is why the real wind in "
          "the free atmosphere is geostrophic to within 10-20 %, and why "
          "the wind can be read off an upper-air chart.\n\n"
          "On curved paths the centripetal acceleration " r"$v^2/R$"
          " is added: the **gradient wind**. Around a low the Coriolis "
          "force helps hold the curve; the pressure gradient has to "
          "supply both, and the wind is **sub**geostrophic. Around a "
          "high the Coriolis force points outward, so it must exceed "
          "centripetal force *and* pressure gradient: the wind is "
          "**super**geostrophic -- but only up to a limit. The "
          "quadratic has a solution for the high only if "
          r"$|\partial p/\partial n| < \rho f^2 R/4$" ": a high cannot "
          "carry a strong pressure gradient. **That is why highs are "
          "large, flat and calm, lows small, deep and stormy.** A "
          "hurricane is a low with 50 hPa over 50 km; a high of that "
          "strength is physically impossible."),
        "skizze-geostrophisch", [
        zahl(t("Geostrophischer Wind bei 4 hPa je 400 km, ρ = 1,2 kg/m³, "
               "f = 1,03·10⁻⁴ /s? (in m/s, eine Nachkommastelle)",
               "Geostrophic wind for 4 hPa per 400 km, ρ = 1.2 kg/m³, "
               "f = 1.03·10⁻⁴ /s? (in m/s, one decimal)"),
             rund(400.0 / (1.2 * 1.03e-4 * 4.0e5), 1), t("m/s", "m/s"),
             t("`v_g = 400 Pa / (1,2 × 1,03·10⁻⁴ × 4·10⁵ m) = 8,1 m/s`. "
               "Halber Isobarenabstand, doppelter Wind: Deshalb liest man "
               "den Sturm an den engen Isobaren.",
               "`v_g = 400 Pa / (1.2 × 1.03·10⁻⁴ × 4·10⁵ m) = 8.1 m/s`. "
               "Half the isobar spacing, twice the wind: that is why the "
               "storm is read from the tight isobars."),
             toleranz=0.03),
        mc(t("Du stehst mit dem Rücken zum Wind, Nordhalbkugel. Wo ist "
             "das Tief?",
             "You stand with your back to the wind, northern hemisphere. "
             "Where is the low?"),
           [t("Links vorn.", "Ahead to the left."),
            t("Rechts vorn.", "Ahead to the right."),
            t("Direkt voraus.", "Straight ahead."),
            t("Hinter dir.", "Behind you.")], 0,
           t("Buys-Ballot. Der geostrophische Wind weht mit dem tiefen "
             "Druck zur Linken; die leichte Reibungskomponente zum Tief "
             "hin macht aus 'links' ein 'links vorn'.",
             "Buys-Ballot. The geostrophic wind blows with low pressure "
             "on its left; the slight frictional component toward the "
             "low turns 'left' into 'ahead to the left'.")),
        mc(t("Warum gibt es keine Hochs mit Hurrikan-Druckgradienten?",
             "Why are there no highs with hurricane pressure gradients?"),
           [t("Im Hoch zeigt die Coriolis-Kraft nach außen und muss "
              "Druckgradient und Zentripetalkraft zusammen übertreffen; "
              "das geht nur bis ρf²R/4.",
              "In a high the Coriolis force points outward and must "
              "exceed pressure gradient and centripetal force together; "
              "that works only up to ρf²R/4."),
            t("Weil Hochs immer kalt sind.",
              "Because highs are always cold."),
            t("Weil absinkende Luft keine Energie hat.",
              "Because subsiding air has no energy."),
            t("Es gibt sie, sie heißen nur anders.",
              "There are, they are just called differently.")], 0,
           t("Die Gradientwindgleichung ist für das Hoch eine "
             "quadratische Gleichung, deren Diskriminante bei starkem "
             "Gradienten negativ wird: kein stationärer Wind möglich, "
             "das Hoch läuft auseinander.",
             "For the high the gradient-wind equation is a quadratic "
             "whose discriminant turns negative for a strong gradient: "
             "no steady wind is possible, the high spreads out.")),
        ]),

    lektion("dy-thermisch",
        t("Thermischer Wind und Jetstream",
          "Thermal wind and the jet stream"),
        ["thermischer-wind", "hypsometrie", "jetstream"],
        t("Die Hydrostatik hat gezeigt, dass warme Luftsäulen dicker "
          "sind. In Druckkoordinaten lautet das: die **Schichtdicke** "
          "zwischen zwei Druckflächen ist proportional zur mittleren "
          "Temperatur,\n\n"
          r"$$z_2 - z_1 = \frac{R_L\,\overline{T}}{g}\,\ln\frac{p_1}{p_2}$$"
          "\n\n"
          "(hypsometrische Gleichung). Zwischen 1000 und 500 hPa sind "
          "das bei 250 K Mittel 5071 m, bei 270 K 5476 m: 20 K machen "
          "400 m aus. Gibt es also einen waagrechten Temperaturgradienten "
          "-- und den gibt es immer, vom Äquator zum Pol --, dann neigen "
          "sich die Druckflächen mit der Höhe immer stärker zur kalten "
          "Seite. Ein stärkerer Gefällewinkel heißt stärkerer "
          "geostrophischer Wind. Der Wind **ändert sich also mit der "
          "Höhe**, und zwar proportional zum Temperaturgradienten:\n\n"
          r"$$\frac{\partial \vec v_g}{\partial \ln p} = -\frac{R_L}{f}\,\hat k\times\nabla T$$"
          "\n\n"
          "Das ist der **thermische Wind** -- kein Wind, sondern eine "
          "Windscherung, und sie weht mit der kalten Luft zur Linken "
          "(Nordhalbkugel). Mit 1 K je 100 km, wie in der mittleren "
          "Breite im Winter, nimmt der Westwind zwischen 1000 und 500 hPa "
          "um " r"$R_L/f\cdot 10^{-5}\cdot\ln 2 = 19$" " m/s zu. Bis zur "
          "Tropopause summiert sich das auf 40 bis 60 m/s: der "
          "**Jetstream**. Er liegt genau dort, wo der Temperaturgradient "
          "am größten ist -- an der Polarfront -- und genau an der "
          "Tropopause, weil darüber der Gradient umkehrt (die polare "
          "Stratosphäre ist wärmer als die tropische) und der Wind "
          "wieder abnimmt.\n\n"
          "Der thermische Wind erklärt auch, warum **Höhentiefs kalt und "
          "Höhenhochs warm** sind: Ein Bodentief mit kalter Luft darüber "
          "vertieft sich nach oben, ein warmes Bodentief (Hitzetief, "
          "Hurrikan) ist in der Höhe ein Hoch. Und er sagt, wie man aus "
          "der Winddrehung mit der Höhe die Advektion liest: Dreht der "
          "Wind mit der Höhe nach rechts (Süd unten, West oben), wird "
          "warme Luft herangeführt -- Warmluftadvektion, meist vor einer "
          "Warmfront.",
          "Hydrostatics showed that warm columns are thicker. In "
          "pressure coordinates that reads: the **thickness** between "
          "two pressure surfaces is proportional to the mean "
          "temperature,\n\n"
          r"$$z_2 - z_1 = \frac{R_L\,\overline{T}}{g}\,\ln\frac{p_1}{p_2}$$"
          "\n\n"
          "(hypsometric equation). Between 1000 and 500 hPa that is "
          "5071 m at a mean of 250 K, 5476 m at 270 K: 20 K make 400 m. "
          "So if there is a horizontal temperature gradient -- and there "
          "always is, from equator to pole -- the pressure surfaces tilt "
          "ever more steeply toward the cold side with height. A steeper "
          "slope means a stronger geostrophic wind. So the wind "
          "**changes with height**, in proportion to the temperature "
          "gradient:\n\n"
          r"$$\frac{\partial \vec v_g}{\partial \ln p} = -\frac{R_L}{f}\,\hat k\times\nabla T$$"
          "\n\n"
          "That is the **thermal wind** -- not a wind but a wind shear, "
          "and it blows with the cold air on its left (northern "
          "hemisphere). With 1 K per 100 km, as in mid-latitudes in "
          "winter, the westerly wind increases between 1000 and 500 hPa "
          "by " r"$R_L/f\cdot 10^{-5}\cdot\ln 2 = 19$" " m/s. Up to the "
          "tropopause that adds up to 40 to 60 m/s: the **jet stream**. "
          "It lies exactly where the temperature gradient is largest -- "
          "at the polar front -- and exactly at the tropopause, because "
          "above it the gradient reverses (the polar stratosphere is "
          "warmer than the tropical) and the wind decreases again.\n\n"
          "The thermal wind also explains why **upper lows are cold and "
          "upper highs warm**: a surface low with cold air above deepens "
          "upward, a warm surface low (heat low, hurricane) is a high "
          "aloft. And it says how to read advection from the turning of "
          "the wind with height: if the wind veers with height (south "
          "below, west above), warm air is being brought in -- warm "
          "advection, usually ahead of a warm front."),
        "skizze-thermisch", [
        zahl(t("Schichtdicke 1000-500 hPa bei einer Mitteltemperatur von "
               "250 K? (R_L = 287, g = 9,81; in m)",
               "Thickness 1000-500 hPa at a mean temperature of 250 K? "
               "(R_L = 287, g = 9.81; in m)"),
             rund(R_L * 250.0 / G * math.log(2.0)), t("m", "m"),
             t("`Δz = 287 × 250 / 9,81 × ln 2 = 7315 × 0,693 = 5070 m`. "
               "Die 5400 m-Linie der relativen Topographie ist die "
               "Faustgrenze für Schnee bis in die Niederungen -- sie "
               "entspricht etwa 266 K Mittel.",
               "`Δz = 287 × 250 / 9.81 × ln 2 = 7315 × 0.693 = 5070 m`. "
               "The 5400 m line of the thickness chart is the rule of "
               "thumb for snow down to the lowlands -- it corresponds to "
               "about 266 K mean."),
             toleranz=0.02),
        zahl(t("Thermischer Wind: Temperaturgradient 1 K je 100 km, "
               "f = 1,03·10⁻⁴. Zunahme des geostrophischen Windes zwischen "
               "1000 und 500 hPa? (in m/s)",
               "Thermal wind: temperature gradient 1 K per 100 km, "
               "f = 1.03·10⁻⁴. Increase of the geostrophic wind between "
               "1000 and 500 hPa? (in m/s)"),
             rund(DU_THERMISCH), t("m/s", "m/s"),
             t("`Δv = R_L/f × |∇T| × ln(p₁/p₂) = 287/1,03·10⁻⁴ × 10⁻⁵ × "
               "0,693 = 19 m/s`.",
               "`Δv = R_L/f × |∇T| × ln(p₁/p₂) = 287/1.03·10⁻⁴ × 10⁻⁵ × "
               "0.693 = 19 m/s`."),
             toleranz=0.05),
        mc(t("Der Wind dreht mit der Höhe von Südost auf Südwest. Was "
             "wird advehiert?",
             "The wind veers with height from south-east to south-west. "
             "What is being advected?"),
           [t("Warmluft -- Rechtsdrehung mit der Höhe heißt, die kalte "
              "Luft liegt links der Scherung, also wird warme "
              "herangeführt.",
              "Warm air -- veering with height means the cold air lies "
              "to the left of the shear, so warm air is being brought "
              "in."),
            t("Kaltluft.", "Cold air."),
            t("Nichts, der Wind dreht immer mit der Höhe.",
              "Nothing, the wind always turns with height."),
            t("Feuchte.", "Moisture.")], 0,
           t("Der thermische Windvektor (oben minus unten) zeigt von "
             "Südost-Wind nach Südwest-Wind, also nach Westen. Er weht mit "
             "der kalten Luft zur Linken: kalt ist Norden, warm ist Süden "
             "-- und der Bodenwind aus Südost bringt genau diese warme "
             "Luft heran. Merkregel: rechtsdrehend = warm, linksdrehend = "
             "kalt.",
             "The thermal wind vector (upper minus lower) points from a "
             "south-easterly to a south-westerly, i.e. west. It blows with "
             "the cold air on its left: cold is north, warm is south -- "
             "and the surface wind from the south-east brings exactly that "
             "warm air in. Rule: veering = warm advection, backing = cold "
             "advection.")),
        ]),

    lektion("dy-reibung",
        t("Reibung, Ekman-Spirale und warum das Tief Wolken hat",
          "Friction, the Ekman spiral and why the low has clouds"),
        ["ekman", "grenzschicht", "konvergenz"],
        t("In den untersten 1000 m bremst der Boden. Die Reibung ist "
          "turbulent, nicht molekular: Wirbel tauschen Impuls aus, und "
          "man beschreibt sie als Diffusion mit einem Austauschkoeffizienten "
          r"$K \approx 1\ldots 10\,\mathrm{m^2/s}$" " -- milliardenfach größer als "
          "die molekulare Viskosität. Mit einem konstanten " r"$K$" " lässt "
          "sich die Grenzschicht lösen (Ekman 1905, ursprünglich für den "
          "Ozean): Der Wind dreht sich mit der Höhe spiralförmig in den "
          "geostrophischen hinein, die **Ekman-Spirale**. Am Boden weht "
          "er theoretisch 45° nach links vom geostrophischen (zum tiefen "
          "Druck hin), real sind es 10° bis 30°, weil " r"$K$" " nicht "
          "konstant ist. Die Dicke der Schicht ist "
          r"$D = \pi\sqrt{2K/f}$" ", bei " r"$K = 10$" " etwa 1400 m.\n\n"
          "Die Folge ist die wichtigste **Sekundärzirkulation** der "
          "Meteorologie. Weil der Bodenwind eine Komponente zum Tief hin "
          "hat, **konvergiert** Luft in der Grenzschicht im Tief und muss "
          "aufsteigen; im Hoch **divergiert** sie und wird durch "
          "Absinken ersetzt. Die Vertikalgeschwindigkeit an der "
          "Oberkante ist " r"$w \approx \zeta_g \sqrt{K/(2f)}$" " mit "
          r"$\zeta_g$" " der geostrophischen Wirbelstärke: für ein "
          "Tief mit " r"$\zeta_g = 10^{-5}$" " /s zwei Millimeter je "
          "Sekunde, knapp 200 Meter am Tag -- genug für eine "
          "Wolkendecke. **Deshalb hat das Tief Wolken und das Hoch "
          "blauen Himmel**, nicht weil der Druck selbst etwas mit "
          "Wolken zu tun hätte.\n\n"
          "Dieselbe Konvergenz füllt das Tief auch auf: Sie führt Masse "
          "hinein, die Wirbelstärke nimmt ab (Ekman-Pumpen), mit einer "
          "Zeitkonstante von einigen Tagen. Ein Tief, das nicht aus der "
          "Höhe nachgefüttert wird, ist nach einer Woche verschwunden. "
          "Dasselbe gilt für die Teetasse: Die Teeblätter sammeln sich "
          "in der Mitte, weil die Bodenreibung die Rotation bremst und "
          "die Bodenströmung nach innen läuft -- Einstein hat das 1926 "
          "für die Mäander von Flüssen aufgeschrieben.",
          "In the lowest 1000 m the ground brakes. The friction is "
          "turbulent, not molecular: eddies exchange momentum, and it "
          "is described as diffusion with an eddy coefficient "
          r"$K \approx 1\ldots 10\,\mathrm{m^2/s}$" " -- a billion times "
          "larger than the molecular viscosity. With constant " r"$K$"
          " the boundary layer can be solved (Ekman 1905, originally for "
          "the ocean): the wind turns with height in a spiral into the "
          "geostrophic wind, the **Ekman spiral**. At the ground it "
          "blows theoretically 45° to the left of geostrophic (toward "
          "low pressure), in reality 10° to 30°, because " r"$K$" " is not "
          "constant. The depth of the layer is " r"$D = \pi\sqrt{2K/f}$"
          ", about 1400 m for " r"$K = 10$" ".\n\n"
          "The consequence is the most important **secondary "
          "circulation** in meteorology. Because the surface wind has a "
          "component toward the low, air **converges** in the boundary "
          "layer of a low and must rise; in a high it **diverges** and "
          "is replaced by subsidence. The vertical velocity at the top "
          "is " r"$w \approx \zeta_g \sqrt{K/(2f)}$" " with " r"$\zeta_g$"
          " the geostrophic vorticity: for a low with "
          r"$\zeta_g = 10^{-5}$" " /s two millimetres per second, nearly "
          "200 metres a day -- enough for a cloud deck. **That is "
          "why the low has clouds and the high blue sky**, not because "
          "pressure itself had anything to do with clouds.\n\n"
          "The same convergence also fills the low: it carries mass in, "
          "the vorticity decays (Ekman pumping), with a time constant of "
          "several days. A low that is not fed from aloft is gone after "
          "a week. The same holds for the teacup: the tea leaves gather "
          "in the middle because bottom friction slows the rotation and "
          "the bottom flow runs inward -- Einstein wrote that up in 1926 "
          "for the meanders of rivers."),
        "skizze-ekman", [
        zahl(t("Ekman-Schichtdicke D = π·√(2K/f) für K = 10 m²/s und "
               "f = 1,03·10⁻⁴ /s? (in m)",
               "Ekman layer depth D = π·√(2K/f) for K = 10 m²/s and "
               "f = 1.03·10⁻⁴ /s? (in m)"),
             rund(EKMAN_TIEFE), t("m", "m"),
             t("`√(2 × 10 / 1,03·10⁻⁴) = √194 000 = 441 m`, mal π: "
               "**1385 m**. Ungefähr die Höhe, in der der Wind "
               "geostrophisch wird.",
               "`√(2 × 10 / 1.03·10⁻⁴) = √194 000 = 441 m`, times π: "
               "**1385 m**. About the height at which the wind becomes "
               "geostrophic."),
             toleranz=0.03),
        mc(t("Warum ist der Himmel im Hoch meist wolkenlos?",
             "Why is the sky in a high usually cloudless?"),
           [t("Der Bodenwind weht aus dem Hoch heraus; die Divergenz wird "
              "durch Absinken ersetzt, und absinkende Luft erwärmt sich "
              "und trocknet.",
              "The surface wind blows out of the high; the divergence is "
              "replaced by subsidence, and subsiding air warms and "
              "dries."),
            t("Weil hoher Druck Wasserdampf komprimiert.",
              "Because high pressure compresses water vapour."),
            t("Weil es im Hoch keine Feuchte gibt.",
              "Because there is no moisture in a high."),
            t("Weil der Wind fehlt.", "Because there is no wind.")], 0,
           t("Ekman-Divergenz am Boden, Absinken darüber, Erwärmung mit "
             "1 K je 100 m: Die relative Feuchte fällt, Wolken lösen sich "
             "auf, und unter der Absinkinversion sammelt sich der Dunst.",
             "Ekman divergence at the surface, subsidence above, warming "
             "by 1 K per 100 m: relative humidity falls, clouds dissolve, "
             "and the haze collects beneath the subsidence inversion.")),
        ]),
    ])


# ===========================================================================
# 7  Die allgemeine Zirkulation
# ===========================================================================

def u_drehimpuls(phi_grad):
    """Zonalwind aus Drehimpulserhaltung: ruhend am Äquator gestartet."""
    phi = math.radians(phi_grad)
    return OMEGA * ERDRADIUS * math.sin(phi) ** 2 / math.cos(phi)
U_30 = u_drehimpuls(30.0)
U_60 = u_drehimpuls(60.0)
BETA_45 = 2 * OMEGA * math.cos(math.radians(45.0)) / ERDRADIUS   # 1/(m s)
# Stationäre Rossby-Welle bei U = 15 m/s: L = 2π·√(U/β)
L_STATIONAER = 2 * math.pi * math.sqrt(15.0 / BETA_45) / 1000.0  # km

K_ZIRKULATION = kapitel(
    "zirkulation", t("Die allgemeine Zirkulation", "The general circulation"), 7,
    t("Die Tropen bekommen mehr Sonne, als sie abstrahlen, die Pole "
      "weniger. Irgendetwas muss Wärme polwärts tragen -- und auf einer "
      "rotierenden Kugel kann das keine einfache Umwälzung sein. Hadley "
      "schafft es bis 30°, dann übernehmen die Wellen.",
      "The tropics receive more sun than they emit, the poles less. "
      "Something has to carry heat poleward -- and on a rotating sphere "
      "that cannot be a simple overturning. Hadley manages it to 30°, "
      "then the waves take over."), [

    lektion("zi-hadley",
        t("Hadley-Zelle, Passat und die Grenze bei 30°",
          "Hadley cell, trade winds and the limit at 30°"),
        ["hadley", "passat", "drehimpuls"],
        t("Am Äquator steigt die Luft auf (die **innertropische "
          "Konvergenzzone**, ein Gürtel aus Cumulonimben), strömt in der "
          "Höhe polwärts, sinkt bei 30° ab und kehrt am Boden zurück. Das "
          "ist die **Hadley-Zelle**, und sie erklärt auf einen Schlag: "
          "den Regenwald am Äquator, die Wüsten bei 25-30° (Absinken, "
          "Erwärmung, Austrocknung -- Sahara, Kalahari, Australien) und "
          "den **Passat**, den Rückstrom am Boden, der auf der "
          "Nordhalbkugel durch Coriolis nach rechts gelenkt wird und aus "
          "Nordost weht.\n\n"
          "Warum endet sie bei 30° und nicht am Pol? **Drehimpuls.** Ein "
          "Luftpaket, das am Äquator relativ zur Erde ruht, hat den "
          "Drehimpuls " r"$\Omega a^2$" " je Masse. Bewegt es sich ohne "
          "Drehmoment polwärts, schrumpft sein Abstand zur Achse auf "
          r"$a\cos\varphi$" ", und es muss schneller werden:\n\n"
          r"$$u = \Omega a\,\frac{\sin^2\varphi}{\cos\varphi}$$"
          "\n\n"
          "Bei 30° sind das 134 m/s, bei 60° wären es 700 m/s. So "
          "schnell kann kein Wind sein -- die Strömung wird bei etwa 30° "
          "**baroklin instabil** und zerfällt in Wirbel. Der reale "
          "Subtropenjet hat 40 m/s, weil die Wirbel Drehimpuls "
          "abführen.\n\n"
          "Was die Zelle transportiert: Wärme als " r"$c_p T + g z + L_v r$"
          " (**feuchtstatische Energie**). Oben strömt trockene, "
          "potentiell warme Luft polwärts, unten feuchte, kühlere "
          "äquatorwärts; die Differenz ist der Wärmetransport, rund "
          r"$3\cdot 10^{15}$" " W je Hemisphäre -- wie 3000 Kernkraftwerke "
          "je Breitengrad.\n\n"
          "Die ITCZ wandert mit der Sonne, im Juli nach 10° Nord, im "
          "Januar nach 5° Süd. Das macht den **Monsun**: Im Sommer "
          "greift der Südostpassat über den Äquator, wird dort zum "
          "Südwestwind und bringt dem indischen Subkontinent die "
          "Feuchte des Ozeans -- verstärkt durch das Hitzetief über "
          "dem Land und den Hochpass des Himalaya, der die Luft zum "
          "Aufsteigen zwingt.\n\n"
          "Zwischen 30° und 60° liegt die **Ferrel-Zelle**, "
          "thermodynamisch indirekt (kalt steigt, warm sinkt), eine "
          "statistische Restspur der Wirbel, keine echte Zirkulation. "
          "Am Pol eine schwache Polarzelle. Die Westwinde der mittleren "
          "Breiten sind der thermische Wind zum Temperaturgefälle -- und "
          "ihre Wellen das nächste Thema.",
          "At the equator the air rises (the **intertropical convergence "
          "zone**, a belt of cumulonimbus), flows poleward aloft, sinks "
          "at 30° and returns at the surface. That is the **Hadley "
          "cell**, and it explains in one go: the rainforest at the "
          "equator, the deserts at 25-30° (subsidence, warming, drying "
          "-- Sahara, Kalahari, Australia) and the **trade wind**, the "
          "return flow at the surface, deflected to the right by "
          "Coriolis in the northern hemisphere and blowing from the "
          "north-east.\n\n"
          "Why does it end at 30° and not at the pole? **Angular "
          "momentum.** A parcel at rest relative to the Earth at the "
          "equator has angular momentum " r"$\Omega a^2$" " per mass. "
          "Moving poleward without torque, its distance from the axis "
          "shrinks to " r"$a\cos\varphi$" " and it must speed up:\n\n"
          r"$$u = \Omega a\,\frac{\sin^2\varphi}{\cos\varphi}$$"
          "\n\n"
          "At 30° that is 134 m/s, at 60° it would be 700 m/s. No wind "
          "can be that fast -- the flow becomes **baroclinically "
          "unstable** at about 30° and breaks into eddies. The real "
          "subtropical jet has 40 m/s, because the eddies carry angular "
          "momentum away.\n\n"
          "What the cell transports: heat as " r"$c_p T + g z + L_v r$"
          " (**moist static energy**). Aloft dry, potentially warm air "
          "flows poleward, below moist, cooler air equatorward; the "
          "difference is the heat transport, about " r"$3\cdot 10^{15}$"
          " W per hemisphere -- like 3000 nuclear plants per degree of "
          "latitude.\n\n"
          "The ITCZ migrates with the sun, to 10° N in July, to 5° S in "
          "January. That makes the **monsoon**: in summer the south-east "
          "trade crosses the equator, becomes a south-westerly there and "
          "brings the Indian subcontinent the moisture of the ocean -- "
          "reinforced by the heat low over the land and the Himalayan "
          "barrier that forces the air to rise.\n\n"
          "Between 30° and 60° lies the **Ferrel cell**, "
          "thermodynamically indirect (cold rises, warm sinks), a "
          "statistical residue of the eddies, not a real circulation. "
          "At the pole a weak polar cell. The westerlies of the "
          "mid-latitudes are the thermal wind to the temperature "
          "gradient -- and their waves are the next topic."),
        "skizze-zellen", [
        zahl(t("Ein Paket startet am Äquator ohne Relativgeschwindigkeit "
               "und bewegt sich drehimpulserhaltend nach 30°. Zonalwind "
               "dort? (Ω = 7,292·10⁻⁵, a = 6371 km; in m/s)",
               "A parcel starts at the equator with no relative velocity "
               "and moves to 30° conserving angular momentum. Zonal wind "
               "there? (Ω = 7.292·10⁻⁵, a = 6371 km; in m/s)"),
             rund(U_30), t("m/s", "m/s"),
             t("`u = Ω·a·sin²φ/cos φ = 7,292·10⁻⁵ × 6,371·10⁶ × 0,25 / "
               "0,866 = 134 m/s`. Bei 60° wären es 700 m/s: Spätestens "
               "dort muss die Zelle enden.",
               "`u = Ω·a·sin²φ/cos φ = 7.292·10⁻⁵ × 6.371·10⁶ × 0.25 / "
               "0.866 = 134 m/s`. At 60° it would be 700 m/s: the cell "
               "must end well before that."),
             toleranz=0.03),
        mc(t("Warum liegen die großen Wüsten bei 25-30° Breite?",
             "Why do the great deserts lie at 25-30° latitude?"),
           [t("Dort sinkt der absteigende Ast der Hadley-Zelle: "
              "Erwärmung, relative Feuchte fällt, keine Wolken.",
              "The descending branch of the Hadley cell sinks there: "
              "warming, relative humidity falls, no clouds."),
            t("Weil die Sonne dort am höchsten steht.",
              "Because the sun is highest there."),
            t("Weil es dort keine Ozeane gibt.",
              "Because there are no oceans there."),
            t("Zufall der Kontinentverteilung.",
              "Chance of the continental layout.")], 0,
           t("Die Sonne steht am Äquator am höchsten, und dort regnet es "
             "am meisten. Die Wüste ist das Gegenstück dazu: wo die "
             "aufgestiegene Luft wieder herunterkommt, getrocknet und "
             "adiabatisch erwärmt.",
             "The sun is highest at the equator, and that is where it "
             "rains most. The desert is the counterpart: where the risen "
             "air comes back down, dried and adiabatically warmed.")),
        ]),

    lektion("zi-rossby",
        t("Rossby-Wellen und der Beta-Effekt",
          "Rossby waves and the beta effect"),
        ["rossby-wellen", "beta-effekt", "vorticity"],
        t("Die Westwinde mäandrieren: Auf jeder Höhenkarte zieht sich "
          "der Jetstream in vier bis sechs Wellen um den Pol. Das sind "
          "**Rossby-Wellen**, und ihre Rückstellkraft ist weder Druck "
          "noch Auftrieb, sondern die **Breitenabhängigkeit der "
          "Coriolis-Kraft**.\n\n"
          "Die Erhaltungsgröße ist die **absolute Wirbelstärke** "
          r"$\zeta + f$" ": die Rotation des Windes relativ zur Erde plus "
          "die Rotation der Erde selbst. Verschiebt man eine Luftsäule "
          "nach Norden, wächst " r"$f$" ", also muss " r"$\zeta$" " abnehmen -- "
          "sie dreht antizyklonal und kehrt nach Süden zurück; dort "
          "überschießt sie, " r"$\zeta$" " wird zyklonal, zurück nach Norden. "
          "Das ist eine Welle. Mit " r"$\beta = df/dy = 2\Omega\cos\varphi/a$"
          " (in 45° " r"$1{,}6\cdot 10^{-11}$" " /(m·s)) lautet die "
          "Dispersionsrelation für eine Welle der Wellenzahl " r"$k$"
          " im Grundstrom " r"$U$" ":\n\n"
          r"$$c = U - \frac{\beta}{k^2}$$"
          "\n\n"
          "Rossby-Wellen laufen **relativ zur Strömung nach Westen**, "
          "und zwar um so schneller, je länger sie sind. Kurze Wellen "
          "werden vom Westwind nach Osten getragen (das sind die "
          "Tröge und Rücken, die mit den Tiefs über uns hinwegziehen, "
          "Wellenlänge 3000-5000 km, 10 m/s nach Osten). Lange Wellen "
          "bleiben **stehen**: bei " r"$U = 15$" " m/s ist "
          r"$L = 2\pi\sqrt{U/\beta} = 6000$" " km, Wellenzahl 4 bis 5 um "
          "den Pol. Noch längere laufen rückwärts. Die stehenden "
          "Wellen werden von den Gebirgen (Rocky Mountains, Himalaya) "
          "und den Land-Meer-Kontrasten angeregt; deshalb liegt der "
          "Trog über dem Ostatlantik so oft an derselben Stelle, und "
          "deshalb ist Westeuropa ein Wetterbrennpunkt.\n\n"
          "Wo eine lange Welle stehen bleibt und sich verstärkt, "
          "entsteht ein **Blocking**: ein Hoch, das wochenlang die "
          "Tiefs umlenkt -- Dürre und Hitze im Sommer, Dauerfrost im "
          "Winter. Die Vorhersage, wann ein Block zerfällt, ist eine "
          "der schwersten Aufgaben der Numerik.\n\n"
          "Was die Wellen leisten: Sie transportieren Wärme polwärts, "
          "effektiver als jede Zelle, als **Wirbelflüsse** "
          r"$\overline{v'T'}$" " -- warm nach Norden auf der Vorderseite "
          "des Troges, kalt nach Süden auf der Rückseite. Die ganze "
          "Ferrel-Zelle ist nur der Mittelwert davon.",
          "The westerlies meander: on every upper-air chart the jet "
          "stream winds around the pole in four to six waves. These are "
          "**Rossby waves**, and their restoring force is neither "
          "pressure nor buoyancy but the **latitude dependence of the "
          "Coriolis force**.\n\n"
          "The conserved quantity is the **absolute vorticity** "
          r"$\zeta + f$" ": the rotation of the wind relative to the "
          "Earth plus the rotation of the Earth itself. Displace a "
          "column northward and " r"$f$" " grows, so " r"$\zeta$" " must "
          "decrease -- it turns anticyclonically and returns south; "
          "there it overshoots, " r"$\zeta$" " becomes cyclonic, back "
          "north. That is a wave. With "
          r"$\beta = df/dy = 2\Omega\cos\varphi/a$" " (at 45° "
          r"$1.6\cdot 10^{-11}$" " /(m·s)) the dispersion relation for a "
          "wave of wavenumber " r"$k$" " in a mean flow " r"$U$" " reads:\n\n"
          r"$$c = U - \frac{\beta}{k^2}$$"
          "\n\n"
          "Rossby waves propagate **westward relative to the flow**, "
          "and the faster the longer they are. Short waves are carried "
          "east by the westerlies (these are the troughs and ridges "
          "that pass over us with the lows, wavelength 3000-5000 km, "
          "10 m/s eastward). Long waves **stand still**: at "
          r"$U = 15$" " m/s " r"$L = 2\pi\sqrt{U/\beta} = 6000$" " km, "
          "wavenumber 4 to 5 around the pole. Even longer ones run "
          "backwards. The standing waves are excited by mountain ranges "
          "(Rockies, Himalaya) and by land-sea contrasts; that is why "
          "the trough over the eastern Atlantic so often sits in the "
          "same place, and why western Europe is a weather hotspot.\n\n"
          "Where a long wave stalls and amplifies, a **block** forms: a "
          "high that diverts the lows for weeks -- drought and heat in "
          "summer, persistent frost in winter. Forecasting when a block "
          "decays is one of the hardest tasks in numerical "
          "prediction.\n\n"
          "What the waves accomplish: they transport heat poleward, "
          "more effectively than any cell, as **eddy fluxes** "
          r"$\overline{v'T'}$" " -- warm northward ahead of the trough, "
          "cold southward behind it. The whole Ferrel cell is just the "
          "average of that."),
        "skizze-rossby", [
        zahl(t("Stationäre Rossby-Welle: L = 2π·√(U/β) für U = 15 m/s "
               "und β = 1,62·10⁻¹¹ /(m·s)? (in km)",
               "Stationary Rossby wave: L = 2π·√(U/β) for U = 15 m/s "
               "and β = 1.62·10⁻¹¹ /(m·s)? (in km)"),
             rund(2 * math.pi * math.sqrt(15.0 / 1.62e-11) / 1000.0),
             t("km", "km"),
             t("`√(15 / 1,62·10⁻¹¹) = √(9,26·10¹¹) = 9,62·10⁵ m`, mal 2π: "
               "**6050 km**. Der 45. Breitenkreis ist 28 300 km lang: "
               "Wellenzahl 4,7.",
               "`√(15 / 1.62·10⁻¹¹) = √(9.26·10¹¹) = 9.62·10⁵ m`, times "
               "2π: **6050 km**. The 45th parallel is 28 300 km long: "
               "wavenumber 4.7."),
             toleranz=0.03),
        mc(t("Warum laufen Rossby-Wellen relativ zur Strömung nach "
             "Westen?",
             "Why do Rossby waves propagate westward relative to the "
             "flow?"),
           [t("Nordwärts verschobene Luft gewinnt planetare und verliert "
              "relative Wirbelstärke; die so entstehende antizyklonale "
              "Drehung verlagert die Auslenkung nach Westen.",
              "Air displaced northward gains planetary and loses relative "
              "vorticity; the resulting anticyclonic turning shifts the "
              "displacement westward."),
            t("Weil die Erde sich nach Osten dreht.",
              "Because the Earth turns eastward."),
            t("Weil der Jetstream sie zurückdrückt.",
              "Because the jet stream pushes them back."),
            t("Sie laufen nach Osten.", "They propagate eastward.")], 0,
           t("Erhaltung von ζ + f mit wachsendem f nach Norden. Westlich "
             "eines Nordausschlags induziert die antizyklonale Drehung "
             "Nordwind, östlich Südwind: Der Wellenberg wandert nach "
             "Westen.",
             "Conservation of ζ + f with f growing northward. West of a "
             "northward bulge the anticyclonic turning induces northward "
             "flow, east of it southward: the crest moves west.")),
        ]),
    ])


# ===========================================================================
# 8  Synoptik: Luftmassen, Fronten, Zyklonen
# ===========================================================================

# Margules: tan α = f·(ρ₁u₁ − ρ₂u₂)/(g·(ρ₂ − ρ₁)) ≈ f·T·Δu/(g·ΔT)
MARGULES = F_45 * 280.0 * 10.0 / (G * 10.0)          # Neigung bei Δu=10, ΔT=10
ROSSBY_RADIUS = N_STANDARD * 10000.0 / F_45 / 1000.0  # km, H = 10 km
EADY_WELLE = 3.9 * ROSSBY_RADIUS                      # km
# Druckfall 20 hPa in 24 h, Windsprung 10 m/s...

K_SYNOPTIK = kapitel(
    "synoptik", t("Synoptik: Fronten und Zyklonen",
                  "Synoptic meteorology: fronts and cyclones"), 8,
    t("Das Wetter der mittleren Breiten ist das Ergebnis einer "
      "Instabilität: Die Atmosphäre baut mit dem Temperaturgefälle "
      "verfügbare potentielle Energie auf und entlädt sie in Zyklonen. "
      "Fronten sind die Nahtstellen, an denen das passiert.",
      "Mid-latitude weather is the product of an instability: the "
      "atmosphere builds available potential energy with the "
      "temperature gradient and discharges it in cyclones. Fronts are "
      "the seams where that happens."), [

    lektion("sy-fronten",
        t("Luftmassen und Fronten", "Air masses and fronts"),
        ["luftmassen", "fronten", "margules"],
        t("Luft, die Tage über einer Fläche liegt, nimmt deren "
          "Eigenschaften an: **Luftmassen** -- maritim oder kontinental, "
          "polar, tropisch, arktisch. Kontinentale Arktikluft im Winter: "
          "−30 °C, trocken, bodennah inversiv. Maritime Tropikluft: "
          "20 °C, 15 g/kg, labil. Wo zwei aufeinandertreffen, mischen "
          "sie sich nicht einfach, sondern bilden eine schmale "
          "Übergangszone: eine **Front**, 50-100 km breit, mit einem "
          "Temperatursprung von 5 bis 15 K.\n\n"
          "Die Front ist keine senkrechte Wand, sondern eine schräge "
          "Fläche, und ihre Neigung folgt aus dem Gleichgewicht "
          "(**Margules**): Die kalte Luft liegt als Keil unter der "
          "warmen, und damit der Keil nicht einfach auseinanderläuft, "
          "braucht es einen Windsprung quer zur Front -- Coriolis hält "
          "ihn. Die Neigung ist\n\n"
          r"$$\tan\alpha = \frac{f\,T}{g}\,\frac{\Delta u}{\Delta T}$$"
          "\n\n"
          "Mit 10 m/s Windsprung und 10 K Temperatursprung in 45° "
          "Breite: 1:340. Reale Fronten liegen zwischen 1:50 und 1:300 "
          "-- über 1000 km Horizontaldistanz steigt die Frontfläche nur "
          "3 bis 10 km. **Deshalb kündigt sich die Warmfront einen Tag "
          "vorher mit Cirrus an**: Die warme Luft gleitet auf dem "
          "flachen Keil auf, und ihre Kondensation beginnt 1000 km vor "
          "der Bodenfront in 8 km Höhe.\n\n"
          "**Warmfront**: Warme Luft verdrängt kalte, gleitet auf "
          "(1:100 bis 1:300). Ablauf: Cirrus, Cirrostratus (Halo), "
          "Altostratus, Nimbostratus mit Dauerregen 6-12 Stunden, "
          "Druckfall, Wind dreht von Südost auf Süd; nach dem Durchgang "
          "Temperaturanstieg, Wind auf Südwest, Druck konstant. Im "
          "Winter ist der Regen in die Kaltluft unten oft gefrierender "
          "Regen.\n\n"
          "**Kaltfront**: Kalte Luft schiebt sich unter die warme, "
          "steiler (1:50 bis 1:100), weil die Reibung den Keil am "
          "Boden bremst und oben vorlaufen lässt. Die warme Luft wird "
          "gehoben wie von einem Pflug: Cumulonimbus, Böenlinie, "
          "Schauer, Gewitter, dann rasche Aufheiterung, Wind springt "
          "von Südwest auf Nordwest, Druck steigt steil, Temperatur "
          "fällt um 5-10 K in einer Stunde.\n\n"
          "**Okklusion**: Die schnellere Kaltfront holt die Warmfront "
          "ein und hebt die Warmluft ganz vom Boden ab. Das ist das "
          "Ende der Zyklone, und ein Tag mit grauem, nassem, lauem "
          "Wetter ohne klare Entwicklung.",
          "Air that sits over a surface for days takes on its "
          "properties: **air masses** -- maritime or continental, polar, "
          "tropical, arctic. Continental arctic air in winter: −30 °C, "
          "dry, inverted near the ground. Maritime tropical air: 20 °C, "
          "15 g/kg, unstable. Where two meet they do not simply mix but "
          "form a narrow transition zone: a **front**, 50-100 km wide, "
          "with a temperature jump of 5 to 15 K.\n\n"
          "The front is not a vertical wall but a sloping surface, and "
          "its slope follows from balance (**Margules**): the cold air "
          "lies as a wedge under the warm, and for the wedge not to "
          "simply spread out it needs a wind jump across the front -- "
          "Coriolis holds it. The slope is\n\n"
          r"$$\tan\alpha = \frac{f\,T}{g}\,\frac{\Delta u}{\Delta T}$$"
          "\n\n"
          "With a 10 m/s wind jump and a 10 K temperature jump at 45°: "
          "1:340. Real fronts lie between 1:50 and 1:300 -- over 1000 km "
          "of horizontal distance the frontal surface rises only 3 to "
          "10 km. **That is why the warm front announces itself a day "
          "ahead with cirrus**: the warm air slides up the shallow wedge "
          "and its condensation begins 1000 km ahead of the surface "
          "front at 8 km height.\n\n"
          "**Warm front**: warm air displaces cold, overrunning it "
          "(1:100 to 1:300). Sequence: cirrus, cirrostratus (halo), "
          "altostratus, nimbostratus with 6-12 hours of steady rain, "
          "falling pressure, wind backing from south-east to south; "
          "after passage temperature rise, wind south-west, pressure "
          "steady. In winter the rain falling into the cold air below "
          "is often freezing rain.\n\n"
          "**Cold front**: cold air pushes under the warm, steeper "
          "(1:50 to 1:100), because friction slows the wedge at the "
          "ground and lets it run ahead aloft. The warm air is lifted "
          "as by a plough: cumulonimbus, squall line, showers, "
          "thunderstorms, then rapid clearing, wind veering from "
          "south-west to north-west, pressure rising sharply, "
          "temperature falling 5-10 K in an hour.\n\n"
          "**Occlusion**: the faster cold front catches the warm front "
          "and lifts the warm air off the ground entirely. That is the "
          "end of the cyclone, and a day of grey, wet, mild weather "
          "with no clear development."),
        "skizze-fronten", [
        zahl(t("Margules-Neigung: f = 1,03·10⁻⁴, T = 280 K, Δu = 10 m/s, "
               "ΔT = 10 K. Wie weit (km) muss man waagrecht gehen, bis "
               "die Frontfläche 1 km höher liegt?",
               "Margules slope: f = 1.03·10⁻⁴, T = 280 K, Δu = 10 m/s, "
               "ΔT = 10 K. How far (km) horizontally until the frontal "
               "surface is 1 km higher?"),
             rund(1.0 / (1.03e-4 * 280.0 * 10.0 / (G * 10.0))),
             t("km", "km"),
             t("`tan α = 1,03·10⁻⁴ × 280 × 10 / (9,81 × 10) = 2,94·10⁻³`, "
               "also 1:340. Für 1 km Höhe 340 km Strecke.",
               "`tan α = 1.03·10⁻⁴ × 280 × 10 / (9.81 × 10) = 2.94·10⁻³`, "
               "i.e. 1:340. For 1 km of height, 340 km of distance."),
             toleranz=0.03),
        mc(t("Der Wind springt in einer Stunde von Südwest auf "
             "Nordwest, der Druck steigt steil, es schauert. Was war das?",
             "Within an hour the wind jumps from south-west to "
             "north-west, the pressure rises sharply, there are showers. "
             "What was that?"),
           [t("Eine Kaltfront.", "A cold front."),
            t("Eine Warmfront.", "A warm front."),
            t("Eine Okklusion.", "An occlusion."),
            t("Ein Föhndurchbruch.", "A foehn breakthrough.")], 0,
           t("Der steile Keil hebt die Warmluft schnell: Schauer statt "
             "Dauerregen, Windsprung statt Drehung, und der Druck steigt, "
             "weil die kalte Luftsäule schwerer ist.",
             "The steep wedge lifts the warm air quickly: showers "
             "instead of steady rain, a wind jump instead of a slow "
             "turn, and pressure rises because the cold column is "
             "heavier.")),
        ]),

    lektion("sy-zyklone",
        t("Zyklogenese und barokline Instabilität",
          "Cyclogenesis and baroclinic instability"),
        ["zyklone", "baroklin", "norwegisches-modell"],
        t("Das **norwegische Zyklonenmodell** (Bjerknes 1919) beschreibt "
          "den Lebenslauf: Auf der Polarfront bildet sich eine kleine "
          "Welle, die warme Luft stößt nach Norden vor (Warmsektor), die "
          "kalte folgt von hinten; der Druck im Wellenscheitel fällt, "
          "die Zirkulation um ihn wächst, die Kaltfront holt die "
          "Warmfront ein, die Zyklone okkludiert und stirbt nach 3 bis "
          "6 Tagen -- 2000 km weiter östlich. Ein Tief, das in 24 h um "
          "mehr als 24 hPa fällt, heißt **Bombe**.\n\n"
          "Woher die Energie kommt, sagt die **barokline Instabilität** "
          "(Charney 1947, Eady 1949). Ein Temperaturgefälle von "
          "Süd nach Nord bedeutet geneigte Flächen gleicher Dichte; "
          "darin steckt **verfügbare potentielle Energie**: Könnte man "
          "die warme Luft über die kalte legen, sänke der Schwerpunkt. "
          "Eine Welle, die warme Luft polwärts *und aufwärts*, kalte "
          "äquatorwärts *und abwärts* bewegt -- schräg, flacher als die "
          "Isentropen --, zapft diese Energie an und wächst exponentiell. "
          "Eadys Modell gibt die am schnellsten wachsende Wellenlänge:\n\n"
          r"$$L \approx 3{,}9\,\frac{N\,H}{f}$$"
          "\n\n"
          "mit " r"$N$" " der Brunt-Väisälä-Frequenz und " r"$H$" " der "
          "Troposphärenhöhe; " r"$NH/f$" " ist der **Rossby-Deformations"
          "radius**, rund 1000 km. Also " r"$L \approx 4000$" " km und "
          "eine Verdopplungszeit von etwa einem Tag. Genau das ist die "
          "Größe der Tiefs und ihr Tempo. Die Instabilität braucht ein "
          "Temperaturgefälle und eine mit der Höhe zunehmende "
          "Strömung (thermischer Wind!) -- beides liefert der Winter "
          "reichlicher als der Sommer, deshalb sind Winterstürme "
          "stärker.\n\n"
          "In der Höhe sieht man die Zyklone als **Trog**, der dem "
          "Bodentief nach Westen vorausgeht -- die Achse ist nach "
          "Westen geneigt, und das ist die Signatur des Wachstums: "
          "Vor dem Höhentrog divergiert die Strömung (die Luft "
          "beschleunigt in den Jet hinein), saugt von unten Masse ab, "
          "und der Bodendruck fällt. Hinter dem Trog Konvergenz, "
          "Absinken, das Hoch. Eine Zyklone ist also immer ein Paar: "
          "Trog oben, Tief unten, versetzt. Liegt der Trog genau über "
          "dem Tief, ist das Wachstum vorbei.\n\n"
          "Das Vorhersagen einer Zyklogenese war hundert Jahre lang "
          "die Kunst des Synoptikers; heute rechnet es ein Modell. Die "
          "Physik dahinter ist dieselbe, und sie bleibt chaotisch -- "
          "Kapitel 11.",
          "The **Norwegian cyclone model** (Bjerknes 1919) describes "
          "the life cycle: a small wave forms on the polar front, the "
          "warm air pushes north (warm sector), the cold follows from "
          "behind; pressure at the crest falls, the circulation around "
          "it grows, the cold front catches the warm front, the cyclone "
          "occludes and dies after 3 to 6 days -- 2000 km further east. "
          "A low that deepens by more than 24 hPa in 24 h is called a "
          "**bomb**.\n\n"
          "Where the energy comes from is told by **baroclinic "
          "instability** (Charney 1947, Eady 1949). A temperature "
          "gradient from south to north means tilted surfaces of equal "
          "density; in them lies **available potential energy**: if the "
          "warm air could be laid over the cold, the centre of mass "
          "would drop. A wave that moves warm air poleward *and "
          "upward*, cold air equatorward *and downward* -- obliquely, "
          "shallower than the isentropes -- taps this energy and grows "
          "exponentially. Eady's model gives the fastest-growing "
          "wavelength:\n\n"
          r"$$L \approx 3.9\,\frac{N\,H}{f}$$"
          "\n\n"
          "with " r"$N$" " the Brunt–Väisälä frequency and " r"$H$" " the "
          "depth of the troposphere; " r"$NH/f$" " is the **Rossby radius "
          "of deformation**, about 1000 km. So " r"$L \approx 4000$" " km "
          "and a doubling time of about a day. That is exactly the size "
          "of lows and their pace. The instability needs a temperature "
          "gradient and a flow that increases with height (thermal "
          "wind!) -- winter supplies both more generously than summer, "
          "which is why winter storms are stronger.\n\n"
          "Aloft the cyclone shows as a **trough** that precedes the "
          "surface low to the west -- the axis tilts westward, and that "
          "is the signature of growth: ahead of the upper trough the "
          "flow diverges (air accelerates into the jet), draws mass up "
          "from below, and surface pressure falls. Behind the trough "
          "convergence, subsidence, the high. A cyclone is therefore "
          "always a pair: trough above, low below, offset. Once the "
          "trough lies right over the low, growth is over.\n\n"
          "Forecasting cyclogenesis was the art of the synoptician for "
          "a hundred years; today a model computes it. The physics "
          "behind it is the same, and it remains chaotic -- chapter "
          "11."),
        "skizze-zyklone", [
        zahl(t("Rossby-Deformationsradius N·H/f für N = 0,0105 /s, "
               "H = 10 km, f = 1,03·10⁻⁴ /s? (in km)",
               "Rossby radius of deformation N·H/f for N = 0.0105 /s, "
               "H = 10 km, f = 1.03·10⁻⁴ /s? (in km)"),
             rund(0.0105 * 10000.0 / 1.03e-4 / 1000.0), t("km", "km"),
             t("`0,0105 × 10⁴ / 1,03·10⁻⁴ = 1,02·10⁶ m ≈ 1020 km`. "
               "Mal 3,9: die Eady-Wellenlänge von 4000 km.",
               "`0.0105 × 10⁴ / 1.03·10⁻⁴ = 1.02·10⁶ m ≈ 1020 km`. "
               "Times 3.9: the Eady wavelength of 4000 km."),
             toleranz=0.03),
        mc(t("Die Trogachse in 500 hPa liegt genau über dem Bodentief. "
             "Was heißt das für die Entwicklung?",
             "The 500 hPa trough axis lies directly over the surface low. "
             "What does that mean for its development?"),
           [t("Das Tief vertieft sich nicht mehr; die Divergenz vor dem "
              "Trog liegt nicht mehr über ihm.",
              "The low no longer deepens; the divergence ahead of the "
              "trough is no longer above it."),
            t("Jetzt beginnt die stärkste Vertiefung.",
              "Now the strongest deepening begins."),
            t("Das Tief wird zum Hoch.", "The low becomes a high."),
            t("Keine Aussage möglich.", "No conclusion possible.")], 0,
           t("Wachstum braucht die Westneigung der Achse: Höhendivergenz "
             "über dem Bodentief. Senkrechte Achse heißt ausgereift oder "
             "okkludiert -- ein 'kaltes Tief', das nur noch langsam "
             "zerfällt.",
             "Growth needs the westward tilt of the axis: upper "
             "divergence above the surface low. A vertical axis means "
             "mature or occluded -- a 'cold low' that now only slowly "
             "decays.")),
        mc(t("Warum sind Winterstürme im Atlantik stärker als "
             "Sommerstürme?",
             "Why are Atlantic winter storms stronger than summer "
             "storms?"),
           [t("Der Temperaturgegensatz Pol-Äquator ist im Winter größer, "
              "also mehr verfügbare potentielle Energie und ein "
              "stärkerer Jet.",
              "The pole-equator temperature contrast is larger in "
              "winter, so more available potential energy and a stronger "
              "jet."),
            t("Weil das Meer im Winter kälter ist.",
              "Because the sea is colder in winter."),
            t("Weil die Luft im Winter dichter ist.",
              "Because the air is denser in winter."),
            t("Sie sind nicht stärker, nur häufiger.",
              "They are not stronger, only more frequent.")], 0,
           t("Barokline Instabilität wächst mit dem meridionalen "
             "Temperaturgradienten. Im Winter ist der Pol 60 K kälter als "
             "der Äquator, im Sommer 30 K.",
             "Baroclinic instability grows with the meridional "
             "temperature gradient. In winter the pole is 60 K colder "
             "than the equator, in summer 30 K.")),
        ]),
    ])


# ===========================================================================
# 9  Mesoskala: Föhn, Land-See-Wind, Gewitter
# ===========================================================================

# Föhn-Rechnung: Luv 20 °C in 500 m, Taupunkt 12 °C → LCL 1500 m (T = 10 °C),
# feucht bis Kamm 3000 m mit 6 K/km → 1 °C; Lee trocken 2500 m → 25,5 °C
FOEHN_LCL = 500.0 + 125.0 * 8.0
FOEHN_KAMM = 20.0 - 9.8 * (FOEHN_LCL - 500.0) / 1000.0 - 6.0 * (3000.0 - FOEHN_LCL) / 1000.0
FOEHN_LEE = FOEHN_KAMM + 9.8 * 2.5
# Seewind: Druckgradient aus 5 K Unterschied über 1 km dicker Schicht,
# Bjerknes-Zirkulation... Zahl: Hydrostatischer Druckunterschied
SEEWIND_DP = 1.2 * G * 1000.0 * 5.0 / 290.0        # Pa
HAGEL_V = math.sqrt(4 * 900.0 * G * 0.02 / (3 * 0.6 * 0.9))   # m/s für 2 cm Durchm... s.u.

K_MESOSKALA = kapitel(
    "mesoskala", t("Mesoskala: Föhn, Seewind, Gewitter",
                   "Mesoscale: foehn, sea breeze, thunderstorms"), 8,
    t("Zwischen Zyklone und Turbulenz liegen die Phänomene, die man "
      "an einem Nachmittag erlebt: der warme Fallwind, die Brise vom "
      "Meer, das Gewitter. Hier ist die Rossby-Zahl nahe eins, die "
      "Thermodynamik regiert, und alles ist nachrechenbar.",
      "Between the cyclone and turbulence lie the phenomena one "
      "experiences in an afternoon: the warm downslope wind, the breeze "
      "from the sea, the thunderstorm. Here the Rossby number is near "
      "one, thermodynamics rules, and everything can be checked by "
      "hand."), [

    lektion("me-foehn",
        t("Föhn: eine Rechnung über den Alpenkamm",
          "Foehn: a calculation across the Alpine crest"),
        ["foehn", "feuchtlabil"],
        t("Südwind gegen die Alpen. Im Luv liegt Luft mit 20 °C und "
          "Taupunkt 12 °C in 500 m Höhe. Sie wird zum Aufsteigen "
          "gezwungen. Trockenadiabatisch bis zum Kondensationsniveau: "
          "8 K Spreizung, also " r"$8 \cdot 125 = 1000$" " m höher, in "
          "**1500 m** bei **10 °C**. Von dort bis zum Kamm in 3000 m "
          "feuchtadiabatisch mit rund 6 K/km: am Kamm **1 °C**, und "
          "unterwegs sind 9 g/kg Wasser ausgeregnet -- der Stau, der "
          "Dauerregen im Tessin.\n\n"
          "Jetzt sinkt die Luft im Lee bis auf 500 m, trocken, weil der "
          "Dampf fehlt: " r"$2{,}5 \cdot 9{,}8 = 24{,}5$" " K wärmer, also "
          "**25,5 °C**. Dieselbe Luft, dieselbe Höhe, 5,5 K wärmer als "
          "vorher und mit 2 g/kg statt 9: relative Feuchte 10 %. Das ist "
          "der **Föhn**, und seine Wärme ist nicht aus dem Süden "
          "importiert, sondern die Kondensationswärme des Regens auf "
          "der anderen Seite. Die Buchhaltung mit " r"$\theta_e$"
          ": erhalten über den Kamm hinweg; " r"$\theta$" " dagegen "
          "nimmt um genau " r"$L_v \Delta r / c_p = 2{,}5\cdot 10^{6}\cdot 0{,}007/1004 \approx 17$"
          " K zu, abzüglich dessen, was in der Rechnung über die "
          "Feuchtadiabate schon drinsteckt.\n\n"
          "Zwei Einwände, beide berechtigt: Erstens muss die Luft, die "
          "im Lee ankommt, nicht die vom Talboden sein -- oft stammt sie "
          "aus Kammhöhe und war schon vorher trocken (\"trockener "
          "Föhn\"), und der Lee-Absturz allein reicht für die Wärme. "
          "Zweitens: Warum sinkt die Luft im Lee überhaupt, statt in "
          "ihrer Gleichgewichtshöhe weiterzuströmen? Weil die Strömung "
          "über ein Hindernis bei geeigneter Schichtung wie ein "
          "**Wasserfall** bricht -- der hydraulische Sprung, "
          "wiederzuerkennen an den Föhnfenstern und den stationären "
          "Lenticularis-Wolken, die die Welle markieren. Die "
          "**Froude-Zahl** " r"$Fr = U/(N\,h)$" " entscheidet: nahe 1 "
          "stürzt die Luft ins Tal.\n\n"
          "Föhn gibt es überall, wo Gebirge quer zur Strömung stehen: "
          "Chinook an den Rockies (Temperatursprung von −20 auf +10 °C "
          "in Stunden), Zonda in Argentinien, Santa Ana in Kalifornien "
          "mit den Waldbränden, und der Nordföhn im Tessin, wenn der "
          "Wind von der anderen Seite kommt.",
          "A southerly against the Alps. On the windward side lies air "
          "at 20 °C with dew point 12 °C at 500 m. It is forced to rise. "
          "Dry-adiabatically to the condensation level: 8 K spread, so "
          r"$8 \cdot 125 = 1000$" " m higher, at **1500 m** and **10 °C**. "
          "From there to the crest at 3000 m moist-adiabatically at "
          "about 6 K/km: at the crest **1 °C**, and on the way 9 g/kg of "
          "water has rained out -- the orographic rain, the steady "
          "downpour of Ticino.\n\n"
          "Now the air sinks on the lee side to 500 m, dry, because the "
          "vapour is gone: " r"$2.5 \cdot 9.8 = 24.5$" " K warmer, so "
          "**25.5 °C**. The same air, the same height, 5.5 K warmer than "
          "before and with 2 g/kg instead of 9: relative humidity 10 %. "
          "That is the **foehn**, and its warmth is not imported from "
          "the south but is the condensation heat of the rain on the "
          "other side. The bookkeeping with " r"$\theta_e$" ": conserved "
          "across the crest; " r"$\theta$" " on the other hand increases "
          "by " r"$L_v \Delta r / c_p = 2.5\cdot 10^{6}\cdot 0.007/1004 \approx 17$"
          " K, minus what the moist adiabat already accounted for.\n\n"
          "Two objections, both valid: first, the air that arrives in "
          "the lee need not be the valley-floor air -- often it comes "
          "from crest level and was dry to begin with (\"dry foehn\"), "
          "and the lee descent alone accounts for the warmth. Second: "
          "why does the air descend in the lee at all, rather than flow "
          "on at its equilibrium height? Because flow over an obstacle "
          "with suitable stratification breaks like a **waterfall** -- "
          "the hydraulic jump, recognisable in the foehn gap and the "
          "stationary lenticular clouds that mark the wave. The "
          "**Froude number** " r"$Fr = U/(N\,h)$" " decides: near 1 the "
          "air plunges into the valley.\n\n"
          "Foehn exists wherever mountains stand across the flow: the "
          "Chinook of the Rockies (a jump from −20 to +10 °C in hours), "
          "the Zonda in Argentina, the Santa Ana in California with its "
          "wildfires, and the north foehn in Ticino when the wind comes "
          "from the other side."),
        "skizze-foehn", [
        zahl(t("Luv: 20 °C, Taupunkt 12 °C in 500 m. Kamm 3000 m. "
               "Trockenadiabate 9,8 K/km bis zum Kondensationsniveau "
               "(125 m/K), Feuchtadiabate 6 K/km, Lee-Abstieg trocken "
               "auf 500 m. Temperatur im Lee? (in °C, eine "
               "Nachkommastelle)",
               "Windward: 20 °C, dew point 12 °C at 500 m. Crest 3000 m. "
               "Dry adiabat 9.8 K/km to the condensation level "
               "(125 m/K), moist adiabat 6 K/km, dry descent in the lee "
               "to 500 m. Temperature in the lee? (in °C, one decimal)"),
             rund(FOEHN_LEE, 1), t("°C", "°C"),
             t("LCL in 1500 m: 20 − 9,8 = 10,2 °C. Kamm: 10,2 − 1,5 × 6 = "
               "1,2 °C. Lee: 1,2 + 2,5 × 9,8 = **25,7 °C**. Gewinn: "
               "5,7 K, und davon stammt jedes Zehntel aus dem Regen im "
               "Luv.",
               "LCL at 1500 m: 20 − 9.8 = 10.2 °C. Crest: 10.2 − 1.5 × 6 "
               "= 1.2 °C. Lee: 1.2 + 2.5 × 9.8 = **25.7 °C**. Gain: 5.7 K, "
               "every tenth of it from the rain on the windward side."),
             toleranz=0.02),
        mc(t("Warum ist Föhnluft so trocken?",
             "Why is foehn air so dry?"),
           [t("Der Dampf ist im Luv ausgeregnet, und im Lee erwärmt sich "
              "die Luft trockenadiabatisch -- e bleibt klein, e_s wächst "
              "exponentiell.",
              "The vapour rained out on the windward side, and in the "
              "lee the air warms dry-adiabatically -- e stays small, e_s "
              "grows exponentially."),
            t("Weil sie aus der Wüste kommt.",
              "Because it comes from the desert."),
            t("Weil Berge Feuchte aufsaugen.",
              "Because mountains soak up moisture."),
            t("Föhnluft ist nicht trocken, nur warm.",
              "Foehn air is not dry, only warm.")], 0,
           t("2 g/kg bei 25 °C sind 10 % relative Feuchte. Deshalb die "
             "Föhnsicht von 200 km, deshalb die Waldbrandgefahr, deshalb "
             "der Kopfschmerz, über den noch gestritten wird.",
             "2 g/kg at 25 °C is 10 % relative humidity. Hence the foehn "
             "visibility of 200 km, the wildfire danger, and the "
             "headache that is still argued about.")),
        ]),

    lektion("me-seewind",
        t("Land-See-Wind und Berg-Tal-Wind",
          "Sea breeze and valley wind"),
        ["seewind", "zirkulationssatz", "talwind"],
        t("Am Vormittag heizt sich das Land schneller auf als das Meer "
          "(Wasser mischt die Wärme nach unten und hat die dreifache "
          "Wärmekapazität). Über dem Land dehnt sich die Luftsäule aus; "
          "in 1 km Höhe ist der Druck über dem Land dann höher als "
          "über dem Meer -- hydrostatisch: 5 K auf 1 km Dicke geben "
          r"$\Delta p = \rho g h\,\Delta T/T = 1{,}2\cdot 9{,}81\cdot 1000\cdot 5/290 \approx 2$"
          " hPa. Oben strömt Luft seewärts ab, dadurch fällt der "
          "Bodendruck über Land, und unten setzt der **Seewind** ein: "
          "10 bis 20 km/h, 20 bis 50 km landeinwärts, mit einer "
          "**Seewindfront**, an der sich die Cumuli aufreihen -- auf dem "
          "Satellitenbild der Küste als wolkenfreier Streifen über dem "
          "Meer und Wolkenlinie landeinwärts zu sehen. Nachts kehrt sich "
          "alles um, schwächer: Landwind.\n\n"
          "Das Prinzip ist der **Zirkulationssatz von Bjerknes**: Die "
          "Zirkulation " r"$C = \oint \vec v\cdot d\vec l$" " um eine "
          "geschlossene Kurve ändert sich mit\n\n"
          r"$$\frac{dC}{dt} = -\oint \frac{dp}{\rho}$$"
          "\n\n"
          "Das Integral verschwindet, wenn Druck- und Dichteflächen "
          "zusammenfallen (barotrop). Fallen sie nicht zusammen -- "
          "warm über Land, kalt über See bei gleichem Druck --, dann "
          "treibt jeder **Solenoid** (jede Masche aus Isobaren und "
          "Isosteren) die Zirkulation an, immer so, dass die warme Luft "
          "aufsteigt. Dasselbe Prinzip treibt die Hadley-Zelle, den "
          "Monsun und die Thermik.\n\n"
          "Im Gebirge dasselbe mit anderen Namen. Tagsüber heizen die "
          "Hänge: **Hangaufwind** (Segelflieger: Hangflug), die Luft "
          "steigt an den Flanken auf, das Tal saugt vom Vorland nach: "
          "**Talwind**, der nachmittags in den Alpentälern mit 20-30 "
          "km/h taleinwärts weht. Nachts kühlt der Hang, die Luft "
          "fließt als **Hangabwind** zu Tal, sammelt sich und läuft als "
          "**Bergwind** talauswärts -- und in Becken ohne Abfluss "
          "entstehen Kaltluftseen mit Frost im Juni, während es 100 m "
          "höher 10 K wärmer ist. Jeder Winzer kennt die Hangzone, in "
          "der weder Frost noch Nebel hinkommt: den **thermischen "
          "Hangbereich**, dort, wo der nächtliche Abfluss gerade "
          "beginnt.\n\n"
          "Die Coriolis-Kraft dreht den Seewind im Lauf des Tages nach "
          "rechts: Morgens senkrecht zur Küste, abends küstenparallel. "
          "Das Zeitmaß dafür ist wieder " r"$1/f$" " -- bei einer "
          "Rossby-Zahl von 1 ist das genau der Unterschied zwischen "
          "Mittag und Abend.",
          "In the morning the land heats faster than the sea (water "
          "mixes the heat downward and has three times the heat "
          "capacity). Over the land the column expands; at 1 km the "
          "pressure over the land is then higher than over the sea -- "
          "hydrostatically: 5 K over a 1 km layer give "
          r"$\Delta p = \rho g h\,\Delta T/T = 1.2\cdot 9.81\cdot 1000\cdot 5/290 \approx 2$"
          " hPa. Aloft air flows seaward, so surface pressure over land "
          "falls and the **sea breeze** sets in below: 10 to 20 km/h, "
          "20 to 50 km inland, with a **sea-breeze front** along which "
          "the cumuli line up -- visible on satellite images of coasts "
          "as a cloud-free strip over the sea and a cloud line inland. "
          "At night everything reverses, weaker: land breeze.\n\n"
          "The principle is **Bjerknes' circulation theorem**: the "
          "circulation " r"$C = \oint \vec v\cdot d\vec l$" " around a "
          "closed curve changes at\n\n"
          r"$$\frac{dC}{dt} = -\oint \frac{dp}{\rho}$$"
          "\n\n"
          "The integral vanishes if surfaces of pressure and density "
          "coincide (barotropic). If they do not -- warm over land, "
          "cold over sea at the same pressure -- then every "
          "**solenoid** (every mesh of isobars and isosteres) drives "
          "the circulation, always so that the warm air rises. The same "
          "principle drives the Hadley cell, the monsoon and "
          "thermals.\n\n"
          "In the mountains the same under other names. By day the "
          "slopes heat: **upslope wind** (glider pilots: ridge soaring), "
          "the air rises along the flanks, the valley draws from the "
          "foreland: **valley wind**, blowing up-valley in Alpine "
          "valleys at 20-30 km/h in the afternoon. At night the slope "
          "cools, the air drains as **downslope wind** to the valley "
          "floor, collects and runs down-valley as **mountain wind** -- "
          "and in basins without outflow cold-air pools form with frost "
          "in June while it is 10 K warmer 100 m up. Every winegrower "
          "knows the slope zone that neither frost nor fog reaches: the "
          "**thermal belt**, where the nocturnal drainage just "
          "begins.\n\n"
          "The Coriolis force turns the sea breeze to the right over "
          "the day: perpendicular to the coast in the morning, "
          "coast-parallel in the evening. The time scale is again "
          r"$1/f$" " -- at a Rossby number of 1 that is exactly the "
          "difference between noon and evening."),
        "skizze-seewind", [
        zahl(t("Luftsäule 1 km dick, über Land 5 K wärmer als über See "
               "(T = 290 K, ρ = 1,2). Druckunterschied an der Oberkante "
               "Δp = ρ·g·h·ΔT/T? (in hPa, eine Nachkommastelle)",
               "Column 1 km deep, 5 K warmer over land than over sea "
               "(T = 290 K, ρ = 1.2). Pressure difference at the top "
               "Δp = ρ·g·h·ΔT/T? (in hPa, one decimal)"),
             rund(SEEWIND_DP / 100.0, 1), t("hPa", "hPa"),
             t("`1,2 × 9,81 × 1000 × 5 / 290 = 203 Pa = 2,0 hPa`. Auf "
               "20 km sind das 10 Pa/km -- genug für 5 m/s in einer "
               "Stunde Beschleunigung.",
               "`1.2 × 9.81 × 1000 × 5 / 290 = 203 Pa = 2.0 hPa`. Over "
               "20 km that is 10 Pa/km -- enough for 5 m/s after an hour "
               "of acceleration."),
             toleranz=0.05),
        mc(t("Wann ist der Zirkulationssatz dC/dt = −∮dp/ρ ungleich null?",
             "When is the circulation theorem dC/dt = −∮dp/ρ non-zero?"),
           [t("Wenn Druck- und Dichteflächen sich schneiden -- "
              "barokline Schichtung, etwa warm über Land neben kalt "
              "über See.",
              "When pressure and density surfaces intersect -- "
              "baroclinic stratification, e.g. warm over land next to "
              "cold over sea."),
            t("Immer, sobald Wind weht.", "Always, as soon as wind blows."),
            t("Nur in rotierenden Systemen.", "Only in rotating systems."),
            t("Nie, Zirkulation ist erhalten.",
              "Never, circulation is conserved.")], 0,
           t("Für ρ = ρ(p) ist dp/ρ ein totales Differential und das "
             "Ringintegral null (Kelvin). Erst die Solenoide der "
             "baroklinen Atmosphäre erzeugen Zirkulation -- jede "
             "thermische Zirkulation, vom Seewind bis zur Hadley-Zelle.",
             "For ρ = ρ(p), dp/ρ is an exact differential and the loop "
             "integral is zero (Kelvin). Only the solenoids of a "
             "baroclinic atmosphere generate circulation -- every "
             "thermal circulation, from the sea breeze to the Hadley "
             "cell.")),
        ]),

    lektion("me-gewitter",
        t("Gewitter: Zelle, Scherung, Hagel, Blitz",
          "Thunderstorms: cell, shear, hail, lightning"),
        ["gewitterzelle", "windscherung", "hagel", "blitz"],
        t("Ein Gewitter ist CAPE, die freigesetzt wird. Die **Einzelzelle** "
          "lebt 30 bis 60 Minuten: Aufwind, Kondensation, Tropfen "
          "wachsen (Bergeron oben, Koaleszenz unten), der Niederschlag "
          "fällt **durch den eigenen Aufwind** und erstickt ihn -- der "
          "fallende Regen zieht Luft mit nach unten, verdunstet "
          "unterwegs und kühlt sie, und dieser **Abwind** breitet sich "
          "am Boden als **Böenfront** aus, 10 bis 20 km voraus, mit "
          "Windsprung und Temperatursturz. Die Zelle hat sich selbst "
          "den Nachschub abgeschnitten.\n\n"
          "Was sie am Leben hält, ist **Windscherung**: Nimmt der Wind "
          "mit der Höhe zu, kippt der Aufwind, der Niederschlag fällt "
          "neben den Aufwind statt hinein, und die Böenfront hebt an "
          "ihrer Vorderkante neue Warmluft -- die **Multizelle**, die "
          "sich stundenlang erneuert. Bei starker Scherung mit "
          "Richtungsdrehung (Süd unten, West oben) beginnt der ganze "
          "Aufwind zu rotieren: die **Superzelle**, 2 bis 6 Stunden, mit "
          "Mesozyklone, Großhagel und, wenn die Rotation bis zum Boden "
          "reicht, dem Tornado. Die Rotation kommt aus der Scherung: "
          "Horizontale Wirbelstärke " r"$\partial u/\partial z$" " wird vom "
          "Aufwind in die Senkrechte gekippt.\n\n"
          "**Hagel** braucht einen Aufwind, der ein Korn in der Schwebe "
          "hält, während es durch Anfrieren unterkühlter Tropfen "
          "wächst. Die Fallgeschwindigkeit eines Hagelkorns mit "
          "Durchmesser " r"$D$" " ist "
          r"$v = \sqrt{4\,\rho_{Eis}\,g\,D\,/\,(3\,c_w\,\rho_{Luft})}$" ": "
          "für 2 cm rund 20 m/s, für 5 cm 30 m/s. Ein Golfball braucht "
          "also einen 30-m/s-Aufwind, das heißt CAPE über 2000 J/kg -- "
          "und Scherung, damit das Korn mehrmals durch die "
          "Wachstumszone kreist. Die Schichten im aufgeschnittenen "
          "Korn zählen die Runden.\n\n"
          "**Blitz**: Die Ladungstrennung passiert, wo Graupel und "
          "Eiskristalle bei −10 bis −20 °C zusammenstoßen; der Graupel "
          "wird negativ und fällt, die Kristalle positiv und steigen. "
          "Die Wolke wird zum Kondensator mit 100 MV und einem Feld, "
          "das in Wolkenhöhe die Durchschlagsfestigkeit der dünnen Luft "
          "erreicht. Ein Blitz transportiert 20 C bei 30 kA, der Kanal "
          "wird 30 000 K heiß -- fünfmal die Sonnenoberfläche --, und "
          "die Stoßwelle ist der Donner. Entfernung: Sekunden durch "
          "drei gibt Kilometer. Faustregel für den Beobachter: Kein "
          "Gewitter ohne Eis -- deshalb braucht es die Vereisung der "
          "Spitze, und deshalb gibt es in warmen tropischen "
          "Regenwolken ohne Eisphase Platzregen, aber keinen Blitz.",
          "A thunderstorm is CAPE being released. The **single cell** "
          "lives 30 to 60 minutes: updraught, condensation, drops grow "
          "(Bergeron above, coalescence below), the precipitation falls "
          "**through its own updraught** and chokes it -- the falling "
          "rain drags air down, evaporates on the way and cools it, "
          "and this **downdraught** spreads at the ground as a **gust "
          "front**, 10 to 20 km ahead, with a wind jump and a "
          "temperature drop. The cell has cut off its own supply.\n\n"
          "What keeps it alive is **wind shear**: if the wind increases "
          "with height, the updraught tilts, the precipitation falls "
          "beside the updraught instead of into it, and the gust front "
          "lifts new warm air at its leading edge -- the **multicell**, "
          "renewing itself for hours. With strong shear and directional "
          "turning (south below, west above) the whole updraught begins "
          "to rotate: the **supercell**, 2 to 6 hours, with a "
          "mesocyclone, giant hail and, if the rotation reaches the "
          "ground, the tornado. The rotation comes from the shear: "
          "horizontal vorticity " r"$\partial u/\partial z$" " is tilted "
          "into the vertical by the updraught.\n\n"
          "**Hail** needs an updraught that holds a stone aloft while it "
          "grows by freezing supercooled drops. The fall speed of a "
          "hailstone of diameter " r"$D$" " is "
          r"$v = \sqrt{4\,\rho_{ice}\,g\,D\,/\,(3\,c_d\,\rho_{air})}$" ": "
          "about 20 m/s for 2 cm, 30 m/s for 5 cm. A golf ball thus "
          "needs a 30 m/s updraught, that is CAPE above 2000 J/kg -- and "
          "shear, so that the stone circles through the growth zone "
          "several times. The layers in a cut stone count the laps.\n\n"
          "**Lightning**: charge separation happens where graupel and "
          "ice crystals collide at −10 to −20 °C; the graupel becomes "
          "negative and falls, the crystals positive and rise. The "
          "cloud becomes a capacitor at 100 MV with a field that "
          "reaches the breakdown strength of the thin air at cloud "
          "height. A flash carries 20 C at 30 kA, the channel heats to "
          "30 000 K -- five times the solar surface -- and the shock "
          "wave is the thunder. Distance: seconds divided by three "
          "gives kilometres. Rule for the observer: no thunderstorm "
          "without ice -- which is why the top has to glaciate, and why "
          "warm tropical rain clouds without an ice phase give "
          "downpours but no lightning."),
        "cumulonimbus", [
        zahl(t("Fallgeschwindigkeit eines Hagelkorns mit D = 2 cm: "
               "v = √(4·ρ_Eis·g·D / (3·c_w·ρ_Luft)) mit ρ_Eis = 900, "
               "c_w = 0,6, ρ_Luft = 0,9 kg/m³? (in m/s)",
               "Fall speed of a hailstone with D = 2 cm: "
               "v = √(4·ρ_ice·g·D / (3·c_d·ρ_air)) with ρ_ice = 900, "
               "c_d = 0.6, ρ_air = 0.9 kg/m³? (in m/s)"),
             rund(HAGEL_V), t("m/s", "m/s"),
             t("`√(4 × 900 × 9,81 × 0,02 / (3 × 0,6 × 0,9)) = √436 = "
               "21 m/s`. Das ist das Mindest-CAPE-Äquivalent von "
               "`½v² = 220 J/kg` -- real braucht es das Vierfache.",
               "`√(4 × 900 × 9.81 × 0.02 / (3 × 0.6 × 0.9)) = √436 = "
               "21 m/s`. That is a minimum CAPE equivalent of "
               "`½v² = 220 J/kg` -- in reality four times that is "
               "needed."),
             toleranz=0.03),
        mc(t("Warum lebt eine Gewitterzelle ohne Windscherung nur eine "
             "Stunde?",
             "Why does a thunderstorm cell without wind shear live only "
             "an hour?"),
           [t("Der Niederschlag fällt in den eigenen Aufwind und "
              "erstickt ihn; der kalte Abwind schneidet die Warmluft "
              "ab.",
              "The precipitation falls into its own updraught and "
              "chokes it; the cold downdraught cuts off the warm "
              "inflow."),
            t("Weil die CAPE nach einer Stunde verbraucht ist.",
              "Because the CAPE is used up after an hour."),
            t("Weil die Tropopause sie stoppt.",
              "Because the tropopause stops it."),
            t("Weil sie wegdriftet.", "Because it drifts away.")], 0,
           t("Mit Scherung kippt der Aufwind, Regen und Aufwind trennen "
             "sich, und die Böenfront hebt neue Luft: Dann wird aus der "
             "Stunde eine Nacht.",
             "With shear the updraught tilts, rain and updraught "
             "separate, and the gust front lifts fresh air: then the hour "
             "becomes a night.")),
        mc(t("Zwischen Blitz und Donner vergehen 9 Sekunden. "
             "Entfernung?",
             "Nine seconds pass between flash and thunder. Distance?"),
           [t("Etwa 3 km -- Schall 340 m/s, also 3 s je km.",
              "About 3 km -- sound at 340 m/s, i.e. 3 s per km."),
            t("Etwa 9 km.", "About 9 km."),
            t("Etwa 1 km.", "About 1 km."),
            t("Etwa 27 km.", "About 27 km.")], 0,
           t("Das Licht ist sofort da, der Schall braucht 2,9 s je "
             "Kilometer. Unter 10 s heißt: im Freien in Deckung.",
             "The light arrives instantly, the sound needs 2.9 s per "
             "kilometre. Under 10 s means: take cover if outdoors.")),
        ]),
    ])


# ===========================================================================
# 10  Optik
# ===========================================================================

N_WASSER_ROT, N_WASSER_BLAU = 1.331, 1.343
def regenbogen(n):
    """Minimum der Ablenkung des Hauptregenbogens: Einfallswinkel und
    Bogenwinkel (Descartes)."""
    cos_i = math.sqrt((n * n - 1.0) / 3.0)
    i = math.acos(cos_i)
    r = math.asin(math.sin(i) / n)
    ablenkung = math.pi + 2 * i - 4 * r
    return math.degrees(i), math.degrees(2 * math.pi - ablenkung - math.pi)  # Winkel zur Antisonne
BOGEN_ROT = 180.0 - math.degrees(math.pi + 2 * math.radians(regenbogen(N_WASSER_ROT)[0]) - 4 * math.asin(math.sin(math.radians(regenbogen(N_WASSER_ROT)[0])) / N_WASSER_ROT))
BOGEN_BLAU = 180.0 - math.degrees(math.pi + 2 * math.radians(regenbogen(N_WASSER_BLAU)[0]) - 4 * math.asin(math.sin(math.radians(regenbogen(N_WASSER_BLAU)[0])) / N_WASSER_BLAU))
HALO_22 = math.degrees(2 * math.asin(1.31 * math.sin(math.radians(30.0))) - math.radians(60.0))
RAYLEIGH_VERHAELTNIS = (650.0 / 450.0) ** 4
SICHTWEITE = 3.912 / 0.0001 / 1000.0     # km bei β = 10⁻⁴ /m

K_OPTIK = kapitel(
    "optik", t("Optik des Himmels", "Optics of the sky"), 9,
    t("Warum der Himmel blau ist, die Wolke weiß, der Regenbogen bei "
      "42° steht und der Halo bei 22°: Streuung und Brechung, und jede "
      "Zahl ausgerechnet.",
      "Why the sky is blue, the cloud white, the rainbow at 42° and the "
      "halo at 22°: scattering and refraction, every number worked "
      "out."), [

    lektion("op-streuung",
        t("Rayleigh, Mie und die Sichtweite",
          "Rayleigh, Mie and visibility"),
        ["rayleigh", "mie", "sichtweite"],
        t("Ein Molekül ist viel kleiner als die Wellenlänge des Lichts. "
          "Das elektrische Feld der Welle induziert einen Dipol, der "
          "mit derselben Frequenz schwingt und abstrahlt -- und die "
          "Abstrahlung eines Dipols geht mit " r"$\omega^4$" ". Deshalb ist "
          "der **Rayleigh-Streuquerschnitt** proportional zu "
          r"$1/\lambda^4$" ": Blau (450 nm) wird "
          r"$(650/450)^4 = 4{,}4$" "-mal stärker gestreut als Rot "
          "(650 nm). Der Himmel ist blau, weil wir gestreutes Licht "
          "sehen, und nicht violett, weil die Sonne weniger Violett "
          "enthält und das Auge dort unempfindlich ist. Die Sonne "
          "selbst wird um das Gestreute ärmer: gelblich am Tag, "
          "**rot am Abend**, wenn der Weg durch die Atmosphäre "
          "zehnmal länger ist und auch das Grün herausgestreut wurde. "
          "Nach Vulkanausbrüchen, mit mehr feinem Aerosol in der "
          "Stratosphäre, werden die Abendröten für Jahre spektakulär.\n\n"
          "Wolkentröpfchen sind 10 μm, viel größer als die Wellenlänge: "
          "**Mie-Streuung**, die kaum von " r"$\lambda$" " abhängt. "
          "Deshalb sind Wolken weiß, Nebel weiß, Milch weiß. Eine dicke "
          "Wolke ist von unten grau, weil das Licht nach hundert "
          "Streuungen nach oben zurückgeworfen ist: Die Albedo einer "
          "dicken Wolke liegt bei 0,7 bis 0,9. Die Vorwärtsstreuung "
          "der Mie-Theorie macht auch den **Glanz** um die Sonne im "
          "Dunst und die **Korona** (farbige Ringe um den Mond hinter "
          "dünnen Wolken, Beugung an gleichgroßen Tröpfchen, Ring"
          "radius umgekehrt proportional zur Tropfengröße).\n\n"
          "**Sichtweite**: Ein Objekt verschwindet, wenn sein Kontrast "
          "zum Horizont unter 2 % fällt. Mit dem Extinktionskoeffizienten "
          r"$\beta$" " nimmt der Kontrast wie " r"$e^{-\beta x}$" " ab, "
          "also (**Koschmieder**)\n\n"
          r"$$V = \frac{-\ln 0{,}02}{\beta} = \frac{3{,}9}{\beta}$$"
          "\n\n"
          "Reine Luft: " r"$\beta = 10^{-5}$" " /m, 390 km -- die Sicht "
          "bei Föhn. Dunst: " r"$10^{-4}$" ", 39 km. Nebel: "
          r"$10^{-2}$" ", 390 m; dichter Nebel unter 50 m hat "
          r"$\beta \approx 0{,}1$" " /m. Die Flugwetterwarte misst "
          r"$\beta$" " mit einem Transmissometer und rechnet genau so.",
          "A molecule is much smaller than the wavelength of light. The "
          "wave's electric field induces a dipole that oscillates at "
          "the same frequency and radiates -- and dipole radiation goes "
          "as " r"$\omega^4$" ". Hence the **Rayleigh cross-section** is "
          "proportional to " r"$1/\lambda^4$" ": blue (450 nm) is "
          "scattered " r"$(650/450)^4 = 4.4$" " times more strongly than "
          "red (650 nm). The sky is blue because we see scattered "
          "light, and not violet because the sun contains less violet "
          "and the eye is insensitive there. The sun itself is "
          "depleted of what is scattered: yellowish by day, **red in "
          "the evening**, when the path through the atmosphere is ten "
          "times longer and the green has been scattered out too. After "
          "volcanic eruptions, with more fine aerosol in the "
          "stratosphere, the sunsets are spectacular for years.\n\n"
          "Cloud droplets are 10 μm, much larger than the wavelength: "
          "**Mie scattering**, which hardly depends on " r"$\lambda$" ". "
          "That is why clouds are white, fog white, milk white. A thick "
          "cloud is grey from below because after a hundred scatterings "
          "the light has been thrown back upward: the albedo of a thick "
          "cloud is 0.7 to 0.9. Mie's forward scattering also makes the "
          "**glare** around the sun in haze and the **corona** (coloured "
          "rings around the moon behind thin cloud, diffraction by "
          "equal-sized droplets, ring radius inversely proportional to "
          "droplet size).\n\n"
          "**Visibility**: an object disappears when its contrast "
          "against the horizon falls below 2 %. With the extinction "
          "coefficient " r"$\beta$" " the contrast decays as "
          r"$e^{-\beta x}$" ", hence (**Koschmieder**)\n\n"
          r"$$V = \frac{-\ln 0.02}{\beta} = \frac{3.9}{\beta}$$"
          "\n\n"
          "Clean air: " r"$\beta = 10^{-5}$" " /m, 390 km -- the view in "
          "foehn. Haze: " r"$10^{-4}$" ", 39 km. Fog: " r"$10^{-2}$" ", "
          "390 m; dense fog below 50 m has " r"$\beta \approx 0.1$" " /m. "
          "The aviation weather office measures " r"$\beta$" " with a "
          "transmissometer and calculates exactly so."),
        "skizze-streuung", [
        zahl(t("Rayleigh: Um welchen Faktor wird 450 nm stärker gestreut "
               "als 650 nm? (eine Nachkommastelle)",
               "Rayleigh: by what factor is 450 nm scattered more "
               "strongly than 650 nm? (one decimal)"),
             rund(RAYLEIGH_VERHAELTNIS, 1), t("", ""),
             t("`(650/450)⁴ = 1,444⁴ = 4,4`.",
               "`(650/450)⁴ = 1.444⁴ = 4.4`."),
             toleranz=0.03),
        zahl(t("Koschmieder: Sichtweite bei β = 10⁻⁴ /m? (in km)",
               "Koschmieder: visibility for β = 10⁻⁴ /m? (in km)"),
             rund(SICHTWEITE), t("km", "km"),
             t("`V = 3,9 / 10⁻⁴ = 39 000 m = 39 km`. Leichter Dunst.",
               "`V = 3.9 / 10⁻⁴ = 39 000 m = 39 km`. Light haze."),
             toleranz=0.03),
        mc(t("Warum ist eine Wolke weiß, der Himmel aber blau?",
             "Why is a cloud white but the sky blue?"),
           [t("Tröpfchen sind größer als die Wellenlänge und streuen "
              "alle Farben gleich (Mie); Moleküle sind kleiner und "
              "streuen mit 1/λ⁴ (Rayleigh).",
              "Droplets are larger than the wavelength and scatter all "
              "colours equally (Mie); molecules are smaller and scatter "
              "as 1/λ⁴ (Rayleigh)."),
            t("Wasser ist weiß.", "Water is white."),
            t("Die Wolke reflektiert, der Himmel absorbiert.",
              "The cloud reflects, the sky absorbs."),
            t("Die Wolke ist näher.", "The cloud is closer.")], 0,
           t("Dieselbe Physik, anderer Größenbereich: Der Übergang von "
             "Rayleigh zu Mie liegt bei Teilchen von etwa λ/10.",
             "Same physics, different size range: the transition from "
             "Rayleigh to Mie lies at particles of about λ/10.")),
        ]),

    lektion("op-regenbogen",
        t("Regenbogen bei 42°, Halo bei 22°",
          "Rainbow at 42°, halo at 22°"),
        ["regenbogen", "halo", "descartes"],
        t("Ein Sonnenstrahl trifft einen Regentropfen, wird gebrochen, "
          "an der Rückseite reflektiert und beim Austritt wieder "
          "gebrochen. Die Gesamtablenkung hängt vom Einfallswinkel "
          r"$i$" " ab:\n\n"
          r"$$\delta(i) = \pi + 2i - 4r, \qquad \sin i = n\,\sin r$$"
          "\n\n"
          "Die Strahlen, die den Tropfen in verschiedenen Abständen von "
          "der Achse treffen, werden verschieden abgelenkt -- aber die "
          "Ablenkung hat ein **Minimum** (Descartes 1637), und dort "
          "häufen sich die Strahlen: Alle Strahlen in der Nähe des "
          "Minimums kommen unter fast demselben Winkel heraus, dort ist "
          "es hell. Die Herleitung unten gibt "
          r"$\cos i = \sqrt{(n^2-1)/3}$" ", für " r"$n = 1{,}333$" " also "
          r"$i = 59{,}4^\circ$" " und ein Minimum der Ablenkung von "
          "138°. Vom Beobachter aus liegt der Bogen also "
          r"$180^\circ - 138^\circ = 42^\circ$" " vom Gegenpunkt der Sonne "
          "entfernt: der **Hauptregenbogen**, ein Kreis um den eigenen "
          "Schatten. Deshalb steht er morgens und abends hoch und "
          "mittags gar nicht (Sonne über 42°: der Bogen liegt unter dem "
          "Horizont).\n\n"
          "Die Farben kommen von der Dispersion: Rot hat "
          r"$n = 1{,}331$" " und 42,4°, Blau " r"$n = 1{,}343$" " und "
          "40,6°. **Rot außen**. Innerhalb des Bogens ist es heller als "
          "außerhalb, weil alle Strahlen mit Ablenkung über dem Minimum "
          "dorthin fallen; außerhalb ist das Alexanders dunkle Band. "
          "Zwei Reflexionen im Tropfen geben den **Nebenbogen** bei "
          "51°, mit umgekehrter Farbfolge und ein Zehntel so hell.\n\n"
          "Der **22°-Halo** ist dasselbe Prinzip mit Eis statt Wasser "
          "und Prisma statt Kugel: Sechseckige Eisplättchen und -säulen "
          "in Cirrostratus brechen das Licht durch zwei Flächen im "
          "Winkel von 60°. Die minimale Ablenkung eines Prismas ist "
          r"$\delta = 2\arcsin(n\sin 30^\circ) - 60^\circ$" ", mit "
          r"$n_{Eis} = 1{,}31$" " also **21,8°**. Der Halo ist ein Ring "
          "**um die Sonne** (nicht um den Gegenpunkt), innen rot, "
          "außen bläulich-weiß, und sein Erscheinen heißt: "
          "Cirrostratus, eine Warmfront ist 12 bis 24 Stunden entfernt. "
          "Die 90°-Prismen der Säulenenden geben den 46°-Halo, waagrecht "
          "schwebende Plättchen die **Nebensonnen** bei 22° neben der "
          "tiefstehenden Sonne.\n\n"
          "Was keine Brechung ist: die **Glorie**, farbige Ringe um den "
          "Schatten des eigenen Kopfes auf einer Nebelwand oder um den "
          "Flugzeugschatten auf der Wolke -- Beugung und "
          "Oberflächenwellen an Tröpfchen, bis heute nicht ganz "
          "verstanden.",
          "A ray of sunlight meets a raindrop, is refracted, reflected "
          "at the back and refracted again on leaving. The total "
          "deviation depends on the angle of incidence " r"$i$" ":\n\n"
          r"$$\delta(i) = \pi + 2i - 4r, \qquad \sin i = n\,\sin r$$"
          "\n\n"
          "Rays hitting the drop at different distances from the axis "
          "are deviated by different amounts -- but the deviation has a "
          "**minimum** (Descartes 1637), and there the rays pile up: all "
          "rays near the minimum emerge at nearly the same angle, so it "
          "is bright there. The derivation below gives "
          r"$\cos i = \sqrt{(n^2-1)/3}$" ", for " r"$n = 1.333$" " hence "
          r"$i = 59.4^\circ$" " and a minimum deviation of 138°. Seen "
          "from the observer the bow therefore lies "
          r"$180^\circ - 138^\circ = 42^\circ$" " from the antisolar "
          "point: the **primary rainbow**, a circle around your own "
          "shadow. That is why it stands high in the morning and "
          "evening and not at all at noon (sun above 42°: the bow is "
          "below the horizon).\n\n"
          "The colours come from dispersion: red has " r"$n = 1.331$"
          " and 42.4°, blue " r"$n = 1.343$" " and 40.6°. **Red "
          "outside**. Inside the bow it is brighter than outside, "
          "because all rays with deviation above the minimum fall "
          "there; outside is Alexander's dark band. Two reflections in "
          "the drop give the **secondary bow** at 51°, with reversed "
          "colour order and a tenth as bright.\n\n"
          "The **22° halo** is the same principle with ice instead of "
          "water and a prism instead of a sphere: hexagonal ice plates "
          "and columns in cirrostratus refract the light through two "
          "faces at 60°. The minimum deviation of a prism is "
          r"$\delta = 2\arcsin(n\sin 30^\circ) - 60^\circ$" ", with "
          r"$n_{ice} = 1.31$" " hence **21.8°**. The halo is a ring "
          "**around the sun** (not the antisolar point), red inside, "
          "bluish-white outside, and its appearance means: "
          "cirrostratus, a warm front is 12 to 24 hours away. The 90° "
          "prisms of the column ends give the 46° halo, horizontally "
          "floating plates the **sun dogs** 22° beside the low sun.\n\n"
          "What is not refraction: the **glory**, coloured rings around "
          "the shadow of your own head on a fog bank or around the "
          "aircraft's shadow on the cloud -- diffraction and surface "
          "waves on droplets, not fully understood to this day."),
        "skizze-regenbogen", [
        zahl(t("Minimale Ablenkung im Prisma: δ = 2·arcsin(n·sin 30°) − "
               "60° für Eis, n = 1,31? (in Grad, eine Nachkommastelle)",
               "Minimum deviation in a prism: δ = 2·arcsin(n·sin 30°) − "
               "60° for ice, n = 1.31? (in degrees, one decimal)"),
             rund(HALO_22, 1), t("°", "°"),
             t("`arcsin(1,31 × 0,5) = arcsin 0,655 = 40,9°`, mal 2 minus "
               "60: **21,8°**. Der 22°-Halo.",
               "`arcsin(1.31 × 0.5) = arcsin 0.655 = 40.9°`, times 2 "
               "minus 60: **21.8°**. The 22° halo."),
             toleranz=0.02),
        zahl(t("Regenbogen für Rot, n = 1,331: cos i = √((n²−1)/3), "
               "δ = 180° + 2i − 4r. Winkel des Bogens vom Gegenpunkt der "
               "Sonne, 180° − δ? (in Grad, eine Nachkommastelle)",
               "Rainbow for red, n = 1.331: cos i = √((n²−1)/3), "
               "δ = 180° + 2i − 4r. Angle of the bow from the antisolar "
               "point, 180° − δ? (in degrees, one decimal)"),
             rund(BOGEN_ROT, 1), t("°", "°"),
             t("`cos i = √(0,7716/3) = 0,5072`, `i = 59,5°`; "
               "`sin r = sin i / n = 0,6474`, `r = 40,4°`; "
               "`δ = 180 + 119,1 − 161,4 = 137,6°`; Bogen bei **42,4°**. "
               "Für Blau (1,343) 40,6°: Rot außen.",
               "`cos i = √(0.7716/3) = 0.5072`, `i = 59.5°`; "
               "`sin r = sin i / n = 0.6474`, `r = 40.4°`; "
               "`δ = 180 + 119.1 − 161.4 = 137.6°`; bow at **42.4°**. "
               "For blue (1.343) 40.6°: red outside."),
             toleranz=0.02),
        mc(t("Warum ist der Regenbogen bei 42° hell und nicht "
             "gleichmäßig über alle Winkel verschmiert?",
             "Why is the rainbow bright at 42° and not smeared evenly "
             "over all angles?"),
           [t("Die Ablenkung hat dort ein Minimum; dδ/di = 0, also "
              "kommen viele Strahlen unter fast demselben Winkel "
              "heraus.",
              "The deviation has a minimum there; dδ/di = 0, so many "
              "rays emerge at nearly the same angle."),
            t("Weil Tropfen genau diese Form haben.",
              "Because drops have exactly this shape."),
            t("Weil die Sonne 42° über dem Horizont steht.",
              "Because the sun is 42° above the horizon."),
            t("Zufall der Brechzahl.",
              "Coincidence of the refractive index.")], 0,
           t("Eine Kaustik: Wo die Ablenkung stationär ist, häuft sich "
             "die Intensität. Dieselbe Mathematik macht die hellen Linien "
             "am Boden eines Schwimmbeckens.",
             "A caustic: where the deviation is stationary, intensity "
             "piles up. The same mathematics makes the bright lines on "
             "the floor of a swimming pool.")),
        ]),
    ])


# ===========================================================================
# 11  Vorhersage
# ===========================================================================

CFL_DT = 10000.0 / 340.0             # s, Schall auf 10-km-Gitter
VERDOPPLUNGEN_14_TAGE = 14.0 / 2.0   # bei 2 Tagen Verdopplungszeit
FEHLERWACHSTUM = 2 ** VERDOPPLUNGEN_14_TAGE

K_VORHERSAGE = kapitel(
    "vorhersage", t("Vorhersage und ihre Grenzen", "Forecasting and its limits"), 10,
    t("Die Gleichungen sind bekannt, die Rechner sind groß, und doch "
      "endet jede Wettervorhersage nach zwei Wochen. Wie ein Modell "
      "rechnet, warum es trotzdem nicht alles weiß, und was ein "
      "Ensemble dagegen tut.",
      "The equations are known, the computers are large, and yet every "
      "weather forecast ends after two weeks. How a model computes, why "
      "it still does not know everything, and what an ensemble does "
      "about it."), [

    lektion("vo-numerik",
        t("Das numerische Modell", "The numerical model"),
        ["primitive-gleichungen", "cfl", "parametrisierung"],
        t("Richardson hat 1922 das erste numerische Wetter von Hand "
          "gerechnet: sechs Wochen für sechs Stunden Vorhersage, und das "
          "Ergebnis war falsch (ein Druckanstieg von 145 hPa), weil die "
          "Anfangsdaten unausgeglichene Schwerewellen enthielten. Seit "
          "1950 (ENIAC, Charney) läuft es auf Maschinen, und das "
          "Prinzip ist dasselbe geblieben: die **primitiven "
          "Gleichungen** -- Bewegungsgleichung in beiden "
          "Horizontalrichtungen, Hydrostatik (oder neuerdings die volle "
          "Vertikalgleichung), Kontinuität, erster Hauptsatz, "
          "Wasserbilanz, Zustandsgleichung: sieben Gleichungen für "
          "sieben Unbekannte " r"$u, v, w, p, \rho, T, q$" " -- werden auf "
          "einem Gitter diskretisiert und in Zeitschritten "
          "vorwärtsgerechnet.\n\n"
          "Das Gitter: global heute 9 km (ECMWF), regional 1 bis 2 km, "
          "mit 100 bis 140 Schichten. Der Zeitschritt ist durch die "
          "**CFL-Bedingung** begrenzt: Information darf je Schritt "
          "nicht weiter als eine Gitterzelle laufen, "
          r"$\Delta t < \Delta x / c$" ". Mit Schallwellen ("
          r"$c = 340$" " m/s) wären das bei 10 km nur 30 s; deshalb "
          "behandelt man Schall und Schwerewellen implizit oder "
          "filtert sie durch die Hydrostatik heraus und kommt auf "
          "Zeitschritte von Minuten. Ein globaler Lauf über zehn Tage "
          "macht dann 2000 Schritte auf 10⁹ Gitterpunkten.\n\n"
          "Was kleiner ist als eine Gitterzelle, kann das Modell nicht "
          "auflösen: einzelne Cumuli, Turbulenz, Strahlung auf "
          "Molekülebene, die Tropfenphysik. Das wird "
          "**parametrisiert** -- aus den aufgelösten Größen wird die "
          "mittlere Wirkung des Unaufgelösten geschätzt. Die "
          "Konvektionsparametrisierung ist die größte Fehlerquelle "
          "jedes Modells und der Grund, warum das Gewitter um 15 Uhr "
          "nicht vorhergesagt wird, sondern nur, dass es Gewitter geben "
          "wird.\n\n"
          "Der Anfangszustand kommt aus der **Datenassimilation**: "
          "Beobachtungen (Satelliten über 90 %, dazu Radiosonden, "
          "Flugzeuge, Schiffe, Bojen, Bodenstationen -- 10⁸ Werte am "
          "Tag) werden mit dem vorherigen Modelllauf zu einem "
          "physikalisch konsistenten Zustand verrechnet (4D-Var: "
          "Minimierung des gewichteten Abstands zu allen Beobachtungen "
          "innerhalb eines Zeitfensters, unter der Nebenbedingung, dass "
          "die Lösung dem Modell gehorcht). Das ist die Hälfte der "
          "Rechenzeit und mehr als die Hälfte der Vorhersagequalität. "
          "Richardsons Fehler war ein Assimilationsfehler.",
          "Richardson computed the first numerical weather by hand in "
          "1922: six weeks for a six-hour forecast, and the result was "
          "wrong (a pressure rise of 145 hPa), because the initial data "
          "contained unbalanced gravity waves. Since 1950 (ENIAC, "
          "Charney) it runs on machines, and the principle has stayed "
          "the same: the **primitive equations** -- momentum equations "
          "in both horizontal directions, hydrostatics (or lately the "
          "full vertical equation), continuity, first law, water "
          "budget, equation of state: seven equations for seven "
          "unknowns " r"$u, v, w, p, \rho, T, q$" " -- are discretised "
          "on a grid and stepped forward in time.\n\n"
          "The grid: global today 9 km (ECMWF), regional 1 to 2 km, "
          "with 100 to 140 levels. The time step is limited by the "
          "**CFL condition**: information may not travel further than "
          "one grid cell per step, " r"$\Delta t < \Delta x / c$" ". With "
          "sound waves (" r"$c = 340$" " m/s) that would be only 30 s at "
          "10 km; hence sound and gravity waves are treated implicitly "
          "or filtered out by hydrostatics, and time steps of minutes "
          "become possible. A global ten-day run then takes 2000 steps "
          "on 10⁹ grid points.\n\n"
          "What is smaller than a grid cell the model cannot resolve: "
          "individual cumuli, turbulence, radiation at the molecular "
          "level, droplet physics. That is **parametrised** -- the mean "
          "effect of the unresolved is estimated from the resolved "
          "quantities. Convection parametrisation is the largest error "
          "source of every model and the reason why the thunderstorm at "
          "15:00 is not forecast, only that there will be "
          "thunderstorms.\n\n"
          "The initial state comes from **data assimilation**: "
          "observations (satellites over 90 %, plus radiosondes, "
          "aircraft, ships, buoys, surface stations -- 10⁸ values a day) "
          "are combined with the previous model run into a physically "
          "consistent state (4D-Var: minimising the weighted distance "
          "to all observations within a time window, subject to the "
          "solution obeying the model). That is half the computing "
          "time and more than half the forecast quality. Richardson's "
          "error was an assimilation error."),
        "skizze-gitter", [
        zahl(t("CFL: Gitterweite 10 km, Schallgeschwindigkeit 340 m/s. "
               "Maximaler Zeitschritt? (in s)",
               "CFL: grid spacing 10 km, speed of sound 340 m/s. Maximum "
               "time step? (in s)"),
             rund(CFL_DT), t("s", "s"),
             t("`Δt < 10 000 / 340 = 29 s`. Mit implizitem Schall oder "
               "hydrostatischer Filterung zählt stattdessen der Wind "
               "(100 m/s): 100 s, und mit semi-Lagrangescher Advektion "
               "auch das nicht mehr.",
               "`Δt < 10 000 / 340 = 29 s`. With implicit sound or "
               "hydrostatic filtering the wind (100 m/s) counts instead: "
               "100 s, and with semi-Lagrangian advection not even "
               "that."),
             toleranz=0.03),
        mc(t("Warum kann ein globales Modell mit 9 km Gitter kein "
             "Gewitter rechnen?",
             "Why can a global model with a 9 km grid not compute a "
             "thunderstorm?"),
           [t("Ein Aufwind ist 1 km breit -- kleiner als die Zelle; er "
              "wird parametrisiert, als mittlere Wirkung auf die Zelle.",
              "An updraught is 1 km wide -- smaller than the cell; it is "
              "parametrised as a mean effect on the cell."),
            t("Weil Gewitter zu kurz leben.",
              "Because thunderstorms live too briefly."),
            t("Weil die Gleichungen keine Feuchte enthalten.",
              "Because the equations contain no moisture."),
            t("Weil das Modell hydrostatisch ist.",
              "Because the model is hydrostatic.")], 0,
           t("Die Konvektionsparametrisierung sagt der Zelle, wie viel "
             "Regen und Wärme sie im Mittel von ihren Gewittern bekäme. "
             "Ob eines davon über deinem Haus steht, weiß sie nicht.",
             "The convection parametrisation tells the cell how much "
             "rain and heat it would on average get from its "
             "thunderstorms. Whether one of them is over your house it "
             "does not know.")),
        ]),

    lektion("vo-chaos",
        t("Chaos, Ensembles und zwei Wochen",
          "Chaos, ensembles and two weeks"),
        ["lorenz", "ensemble", "vorhersagbarkeit"],
        t("1961 ließ Edward Lorenz ein einfaches Konvektionsmodell "
          "ein zweites Mal laufen, mit Anfangswerten, die er vom "
          "Ausdruck abgetippt hatte: drei statt sechs Stellen. Nach "
          "kurzer Zeit hatte die zweite Rechnung mit der ersten nichts "
          "mehr gemein. Das System -- drei gekoppelte Gleichungen, der "
          "**Lorenz-Attraktor** -- ist deterministisch und trotzdem "
          "unvorhersagbar: Benachbarte Zustände entfernen sich "
          "**exponentiell**, " r"$\delta(t) = \delta_0\,e^{\lambda t}$" ", "
          "mit dem Lyapunov-Exponenten " r"$\lambda$" ".\n\n"
          "Die Atmosphäre ist so ein System. Fehler in der Skala eines "
          "Gewitters verdoppeln sich in Stunden, synoptische Fehler in "
          "etwa **zwei Tagen**, und die Fehlerkaskade läuft von klein "
          "nach groß: Ein unbeobachteter Cumulus beeinflusst nach "
          "einer Woche die Lage eines Tiefs. Mit einer Verdopplungszeit "
          "von 2 Tagen ist ein Anfangsfehler nach 14 Tagen auf das "
          r"$2^7 = 128$" "-fache gewachsen -- auch bei zehnmal besseren "
          "Beobachtungen gewinnt man so nur drei Tage. **Die Grenze der "
          "deterministischen Wettervorhersage liegt bei etwa zwei "
          "Wochen**, nicht wegen der Rechner, sondern wegen der "
          "Physik.\n\n"
          "Was man dagegen tun kann: nicht einen Lauf, sondern "
          "**fünfzig**, jeder mit einer leicht gestörten Anfangslage "
          "(in Richtung der am schnellsten wachsenden Fehler, berechnet "
          "mit singulären Vektoren) und gestörter Physik. Das "
          "**Ensemble** liefert eine Verteilung statt einer Zahl: Liegen "
          "die 50 Mitglieder nach fünf Tagen beieinander, ist die Lage "
          "vorhersagbar; streuen sie, ist das die ehrliche Antwort. "
          "\"70 % Regenwahrscheinlichkeit\" heißt: 35 von 50 Läufen "
          "regnen. Das Ensemble sagt auch, welche Beobachtung die "
          "Vorhersage am meisten verbessern würde -- und steuert "
          "Flugzeuge dorthin.\n\n"
          "Was trotz Chaos vorhersagbar bleibt: der **Mittelwert**. Das "
          "Klima -- die Statistik des Wetters über 30 Jahre -- hängt "
          "nicht von Anfangsbedingungen ab, sondern von Randbedingungen "
          "(Sonne, Zusammensetzung, Ozean). Dass es im Juli wärmer ist "
          "als im Januar, ist eine sichere Vorhersage, obwohl kein Tag "
          "im Juli vorhersagbar ist. Lorenz selbst hat beides "
          "formuliert: die Unvorhersagbarkeit des Wetters und die "
          "Vorhersagbarkeit des Klimas als Attraktor.\n\n"
          "Die Verbesserung seit 1980: Die 5-Tage-Vorhersage ist heute "
          "so gut wie damals die 2-Tage-Vorhersage -- ein Tag je "
          "Jahrzehnt. Gewonnen wurde das durch Satelliten, Assimilation "
          "und Auflösung; die Physik ist dieselbe geblieben.",
          "In 1961 Edward Lorenz ran a simple convection model a second "
          "time, with initial values he had typed in from the printout: "
          "three digits instead of six. After a short while the second "
          "run had nothing in common with the first. The system -- "
          "three coupled equations, the **Lorenz attractor** -- is "
          "deterministic and yet unpredictable: neighbouring states "
          "separate **exponentially**, "
          r"$\delta(t) = \delta_0\,e^{\lambda t}$" ", with the Lyapunov "
          "exponent " r"$\lambda$" ".\n\n"
          "The atmosphere is such a system. Errors on the scale of a "
          "thunderstorm double in hours, synoptic errors in about "
          "**two days**, and the error cascade runs from small to "
          "large: an unobserved cumulus affects the position of a low "
          "after a week. With a doubling time of 2 days an initial "
          "error has grown " r"$2^7 = 128$" "-fold after 14 days -- even "
          "with ten times better observations one gains only three "
          "days. **The limit of deterministic weather forecasting lies "
          "at about two weeks**, not because of the computers but "
          "because of the physics.\n\n"
          "What can be done about it: not one run but **fifty**, each "
          "with a slightly perturbed initial state (in the direction of "
          "the fastest-growing errors, computed with singular vectors) "
          "and perturbed physics. The **ensemble** delivers a "
          "distribution instead of a number: if the 50 members stay "
          "together after five days, the situation is predictable; if "
          "they spread, that is the honest answer. \"70 % chance of "
          "rain\" means: 35 of 50 runs rain. The ensemble also says "
          "which observation would improve the forecast most -- and "
          "steers aircraft there.\n\n"
          "What stays predictable despite chaos: the **mean**. Climate "
          "-- the statistics of weather over 30 years -- does not depend "
          "on initial conditions but on boundary conditions (sun, "
          "composition, ocean). That July is warmer than January is a "
          "safe forecast although no day in July is predictable. Lorenz "
          "himself formulated both: the unpredictability of weather and "
          "the predictability of climate as an attractor.\n\n"
          "The improvement since 1980: today's 5-day forecast is as "
          "good as the 2-day forecast was then -- a day per decade. "
          "That was won by satellites, assimilation and resolution; the "
          "physics has stayed the same."),
        "skizze-ensemble", [
        zahl(t("Fehlerverdopplung alle 2 Tage. Um welchen Faktor ist ein "
               "Anfangsfehler nach 14 Tagen gewachsen?",
               "Error doubling every 2 days. By what factor has an "
               "initial error grown after 14 days?"),
             rund(FEHLERWACHSTUM), t("", ""),
             t("`2^(14/2) = 2⁷ = 128`. Zehnmal bessere Anfangsdaten "
               "schieben die Grenze um `log₂ 10 × 2 = 6,6` Tage hinaus -- "
               "theoretisch; praktisch wächst der Fehler am Anfang "
               "schneller.",
               "`2^(14/2) = 2⁷ = 128`. Ten times better initial data "
               "push the limit by `log₂ 10 × 2 = 6.6` days -- in theory; "
               "in practice the error grows faster at the start."),
             toleranz=0.02),
        mc(t("Das Ensemble streut nach fünf Tagen weit auseinander. Was "
             "ist die richtige Vorhersage?",
             "The ensemble spreads widely after five days. What is the "
             "right forecast?"),
           [t("Die Verteilung selbst: Die Lage ist unsicher, und die "
              "Streuung sagt, wie sehr.",
              "The distribution itself: the situation is uncertain, and "
              "the spread says how much."),
            t("Der Mittelwert der Mitglieder.",
              "The mean of the members."),
            t("Das Mitglied mit der höchsten Auflösung.",
              "The member with the highest resolution."),
            t("Der ungestörte Kontrolllauf.",
              "The unperturbed control run.")], 0,
           t("Ein Mittelwert über zwei Wetterlagen ist keine von "
             "beiden. Die Information liegt in der Breite -- und ein "
             "ehrliches '50 %' ist eine bessere Vorhersage als ein "
             "zufälliges 'ja'.",
             "A mean over two weather regimes is neither of them. The "
             "information lies in the width -- and an honest '50 %' is a "
             "better forecast than a random 'yes'.")),
        ]),
    ])


# ===========================================================================
# 12  Den Himmel lesen
# ===========================================================================

LUFTMASSE_HORIZONT = 38.0        # Rayleigh-Luftmasse bei h = 0 (gekrümmte Schicht)
TAU_GRUEN = 0.097                # optische Dicke der reinen Luft, 550 nm
TAU_ROT = 0.048                  # 650 nm
TRANS_GRUEN = math.exp(-LUFTMASSE_HORIZONT * TAU_GRUEN)
TRANS_ROT = math.exp(-LUFTMASSE_HORIZONT * TAU_ROT)
ROTVERHAELTNIS = TRANS_ROT / TRANS_GRUEN                  # 6,4
KORONA_20UM = math.degrees(1.22 * 550e-9 / 20e-6)         # Grad
BETA_40KM = 3.9 / 40000.0                                 # 1/m
BETA_10KM = 3.9 / 10000.0
Z0_GRAS = 0.03                                            # m
PROFIL_GRAS = math.log(10.0 / Z0_GRAS) / math.log(2.0 / Z0_GRAS)
PROFIL_VORSTADT = math.log(10.0 / 0.5) / math.log(2.0 / 0.5)
BEAUFORT_A = 0.836

def beaufort_v(b):
    """Windgeschwindigkeit zur Beaufort-Stufe, m/s."""
    return BEAUFORT_A * b ** 1.5

V_B6 = beaufort_v(6.0)
STAUDRUCK_B6 = 0.5 * 1.225 * V_B6 ** 2                    # Pa
V_B12 = beaufort_v(12.0)
STAUDRUCK_B12 = 0.5 * 1.225 * V_B12 ** 2
ETA_LUFT = 1.8e-5                                         # Pa s

def v_stokes(r_m):
    return 2.0 / 9.0 * 1000.0 * G * r_m ** 2 / ETA_LUFT   # m/s

RE_40UM = v_stokes(40e-6) * 80e-6 / 1.5e-5                # ≈ 1
V_REGEN_1MM = 6.5                                         # m/s, gemessen
FALLZEIT_1MM = 2000.0 / V_REGEN_1MM / 60.0                # min aus 2 km
FALLZEIT_NIESEL = 2000.0 / 0.72 / 60.0                    # min, 0,2-mm-Tropfen

K_HIMMEL = kapitel(
    "himmel", t("Den Himmel lesen", "Reading the sky"), 9,
    t("Streuung, Brechung, Ekman-Spirale und Tropfenwachstum sind "
      "hergeleitet. Hier werden sie eingelöst: vier Lektionen, die beim "
      "Hinsehen anfangen, beim Mechanismus weitergehen und bei einer "
      "Zahl aufhören, die man draußen abschätzen kann.",
      "Scattering, refraction, the Ekman spiral and drop growth have "
      "been derived. Here they are cashed in: four lessons that start "
      "from what is visible, go on to the mechanism and end at a number "
      "one can estimate outdoors."), [

    lektion("hi-farben",
        t("Himmelsfarben und Lichterscheinungen, Stunde für Stunde",
          "Colours and lights of the sky, hour by hour"),
        ["luftmasse", "daemmerung", "halo-korona"],
        t("**Was zu sehen ist.** Mittags ist der Himmel im Zenit tief "
          "blau und am Horizont milchig weiß; die Grenze ist nicht "
          "scharf, aber jeder sieht sie. Am Nachmittag stehen bei "
          "Wolkenlücken **Dämmerungsstrahlen** -- Schattenbahnen in "
          "staubiger Luft, perspektivisch gefächert, in Wirklichkeit "
          "parallel. Nach Sonnenuntergang steigt im Osten ein dunkles, "
          "nach oben scharf begrenztes Band: der **Erdschatten**, und "
          "darüber der rosa **Venusgürtel**, in dem Luft beleuchtet "
          "wird, die der Schatten noch nicht erreicht hat. Dann die "
          "blaue Stunde, in der kein direktes Sonnenlicht mehr da ist "
          "und nur noch die zweifach gestreute, kurzwellige Strahlung "
          "übrig bleibt. Und mit Glück, über einer scharfen "
          "Horizontlinie, eine halbe Sekunde **grüner Blitz**: der "
          "Rand der Sonne, von der Refraktion farbig zerlegt.\n\n"
          "**Was das ist.** Alles folgt aus der einen Zahl, die "
          "op-streuung geliefert hat: Rayleigh streut mit $1/\\lambda^4$. Blau "
          "wird herausgestreut, deshalb ist der Himmel blau und die "
          "Sonne gelb. Der Zenit ist dunkelblau, weil der Sehstrahl nur "
          "durch eine Luftmasse geht; zum Horizont hin wächst der Weg "
          "wie $1/\\sin h$, und bei vielen Streuungen hintereinander "
          "verliert das Licht seine Farbe: Vielfachstreuung macht weiß. "
          "Der milchige Horizont **ist** die Sättigung der Streuung. "
          "Die Säulenmasse über uns steht in at-hydrostatik: $p_0/g = 10\\,330$ "
          "kg/m² ist die Luftmasse 1, senkrecht nach oben.\n\n"
          "**Die Zahl.** Am Horizont trägt die Krümmung der Schicht die "
          "Luftmasse nicht ins Unendliche, sondern auf etwa **38**. Mit "
          "der optischen Dicke der reinen Luft (0,097 bei 550 nm, 0,048 "
          "bei 650 nm) bleibt an Transmission $e^{-38\\cdot 0{,}097} = 2{,}5$ % "
          "im Grün gegen $e^{-38\\cdot 0{,}048} = 16$ % im Rot: ein "
          "Verhältnis von **6,4**. Deshalb ist die untergehende Sonne "
          "nicht einfach blasser, sondern rot -- und deshalb kann man "
          "ihr ins Gesicht sehen.\n\n"
          "**Und die Erscheinungen?** Welche Farbfigur am Himmel steht, "
          "verrät, aus was die Wolke besteht, und das verrät das "
          "Wetter. Ein Ring von 22° Radius um Sonne oder Mond, innen "
          "rot, kommt vom 60°-Prisma des Eiskristalls (op-regenbogen): "
          "Cirrostratus, also Warmfront in 12 bis 24 Stunden. Eng um "
          "die Sonne, innen weiß, in bunten Ringen: **Korona**, und das "
          "ist Beugung an Wassertröpfchen, keine Brechung. Der erste "
          "Ring steht bei $\\theta \\approx 1{,}22\\,\\lambda/d$, für $d = 20$ μm "
          "also bei 1,9° -- ein Viertel der Faustbreite am "
          "ausgestreckten Arm (gut 8°). Je größer die Tröpfchen, desto "
          "enger der Ring: Die Korona ist ein Messgerät für die "
          "Tropfengröße. **Irisieren** am Rand einer dünnen Wolke ist "
          "dasselbe in Unordnung, die **Glorie** um den eigenen "
          "Flugzeugschatten dasselbe in Rückwärtsrichtung.\n\n"
          "**Was man daraus schließt.** Ring weit und innen rot heißt "
          "Eis und heißt Vorwarnung; Ring eng und innen weiß heißt "
          "Wasser und heißt nichts über morgen, aber alles über die "
          "Wolke, in der er steht.",
          "**What is visible.** At noon the sky is deep blue at the "
          "zenith and milky white at the horizon; the boundary is not "
          "sharp, but everyone sees it. In the afternoon, where the "
          "cloud deck breaks, **crepuscular rays** stand out -- lanes "
          "of shadow in dusty air, splayed by perspective, in fact "
          "parallel. After sunset a dark band with a sharp upper edge "
          "rises in the east: the **shadow of the Earth**, and above it "
          "the pink **belt of Venus**, where air is still lit that the "
          "shadow has not yet reached. Then the blue hour, when no "
          "direct sunlight is left and only the twice-scattered, "
          "short-wave light remains. And with luck, over a crisp "
          "horizon, half a second of **green flash**: the limb of the "
          "sun, dispersed by refraction.\n\n"
          "**What it is.** All of it follows from the one number "
          "op-streuung supplied: Rayleigh scattering goes as $1/\\lambda^4$. Blue "
          "is scattered out, so the sky is blue and the sun yellow. The "
          "zenith is dark blue because the line of sight crosses only "
          "one air mass; towards the horizon the path grows as $1/\\sin h$, "
          "and after many successive scatterings the light loses its "
          "colour: multiple scattering makes white. The milky horizon "
          "**is** scattering gone saturated. The column mass above us "
          "stands in at-hydrostatik: $p_0/g = 10\\,330$ kg/m² is air mass 1, "
          "straight up.\n\n"
          "**The number.** At the horizon the curvature of the layer "
          "keeps the air mass finite -- about **38**. With the optical "
          "depth of clean air (0.097 at 550 nm, 0.048 at 650 nm) the "
          "transmission left is $e^{-38\\cdot 0.097} = 2.5$ % in the green "
          "against $e^{-38\\cdot 0.048} = 16$ % in the red: a ratio of "
          "**6.4**. That is why the setting sun is not merely paler but "
          "red -- and why one can look straight at it.\n\n"
          "**And the optical figures?** Which coloured figure stands in "
          "the sky tells what the cloud is made of, and that tells the "
          "weather. A ring of 22° radius around sun or moon, red on the "
          "inside, comes from the 60° prism of an ice crystal "
          "(op-regenbogen): cirrostratus, hence a warm front 12 to 24 "
          "hours out. Tight around the sun, white on the inside, in "
          "coloured rings: a **corona**, and that is diffraction by "
          "water droplets, not refraction. The first ring sits at "
          "$\\theta \\approx 1{.}22\\,\\lambda/d$, so for $d = 20$ μm at 1.9° -- a "
          "quarter of a fist at arm's length (a good 8°). The larger "
          "the droplets, the tighter the ring: a corona is an "
          "instrument for droplet size. **Iridescence** at the edge of "
          "a thin cloud is the same thing in disorder, the **glory** "
          "around one's own aircraft shadow the same thing "
          "backwards.\n\n"
          "**What follows.** A wide ring with red inside means ice and "
          "means advance warning; a tight ring with white inside means "
          "water and says nothing about tomorrow, but everything about "
          "the cloud it stands in."),
        "himmel-luftmasse", [
        zahl(t("Luftmasse 38 am Horizont: Um welchen Faktor kommt mehr "
               "Rot (τ = 0,048) durch als Grün (τ = 0,097)? (eine "
               "Nachkommastelle)",
               "Air mass 38 at the horizon: by what factor does more "
               "red (τ = 0.048) get through than green (τ = 0.097)? "
               "(one decimal)"),
             rund(ROTVERHAELTNIS, 1), t("", ""),
             t("`exp(−38 × 0,048) / exp(−38 × 0,097) = exp(38 × 0,049) "
               "= 6,4`. Das ist die Rotverschiebung des Sonnenlichts am "
               "Horizont, und sie steckt allein im Weg.",
               "`exp(−38 × 0.048) / exp(−38 × 0.097) = exp(38 × 0.049) "
               "= 6.4`. That is the reddening of sunlight at the "
               "horizon, and it lies entirely in the path length."),
             toleranz=0.05),
        zahl(t("Korona: Radius des ersten Rings bei Tröpfchen von 20 μm "
               "Durchmesser, λ = 550 nm? (in Grad, eine "
               "Nachkommastelle)",
               "Corona: radius of the first ring for droplets of 20 μm "
               "diameter, λ = 550 nm? (in degrees, one decimal)"),
             rund(KORONA_20UM, 1), t("°", "°"),
             t("`θ = 1,22 λ/d = 1,22 × 550·10⁻⁹ / 20·10⁻⁶ = 0,0336 rad "
               "= 1,9°`. Beugung an der Kreisscheibe, dieselbe Formel "
               "wie beim Teleskop -- nur umgekehrt benutzt: Hier ist "
               "der Winkel bekannt und die Tropfengröße gesucht.",
               "`θ = 1.22 λ/d = 1.22 × 550·10⁻⁹ / 20·10⁻⁶ = 0.0336 rad "
               "= 1.9°`. Diffraction at a circular disc, the same "
               "formula as for a telescope -- used backwards: here the "
               "angle is known and the droplet size wanted."),
             toleranz=0.05),
        mc(t("Um den Mond steht ein enger, bunter Ring von etwa 2° "
             "Radius, innen weiß. Was folgt daraus?",
             "A tight, coloured ring of about 2° radius stands around "
             "the moon, white on the inside. What follows?"),
           [t("Eiskristalle in 8 km Höhe, eine Warmfront ist im "
              "Anmarsch.",
              "Ice crystals at 8 km, a warm front is approaching."),
            t("Eine Korona: Beugung an Wassertröpfchen von etwa 20 μm, "
              "also eine dünne Wasserwolke dicht über uns -- über das "
              "Wetter von morgen sagt sie nichts.",
              "A corona: diffraction by water droplets of about 20 μm, "
              "so a thin water cloud close above -- it says nothing "
              "about tomorrow's weather."),
            t("Dunst am Boden.", "Haze at the ground."),
            t("Der Mond selbst steht im Nebel des Erdschattens.",
              "The moon itself stands in the shadow of the Earth.")], 1,
           t("Der 22°-Halo ist Brechung an Eis und innen rot, die "
             "Korona ist Beugung an Wasser und innen weiß. Zwei "
             "Erscheinungen, zwei Phasen, zwei Vorhersagen: Der Halo "
             "ist eine Warnung, die Korona eine Messung.",
             "The 22° halo is refraction in ice and red inside, the "
             "corona is diffraction by water and white inside. Two "
             "phenomena, two phases, two forecasts: the halo is a "
             "warning, the corona a measurement."),
           bild="skizze-halo"),
        ]),

    lektion("hi-dunst",
        t("Dunst, Sichtweite und die blauen Berge",
          "Haze, visibility and the blue mountains"),
        ["dunstschicht", "luftlicht", "mischungshoehe"],
        t("**Was zu sehen ist.** Von einem Berg aus liegt der Dunst als "
          "Schicht im Tal, und sie hat eine **Oberkante** -- oft so "
          "scharf, dass man sie mit der Hand abdecken könnte. Von unten "
          "sieht man dieselbe Grenze als die Höhe, in der der Himmel "
          "aufhört, trüb zu sein. Ferne Berge werden mit der Entfernung "
          "nicht dunkler, sondern blasser und blauer, bis der letzte "
          "Kamm nur noch eine Tönung des Himmels ist. Nach einer "
          "Kaltfront reißt die Fernsicht auf; nach drei Hochdrucktagen "
          "ist derselbe Kamm verschwunden.\n\n"
          "**Was das ist.** Die Oberkante der Dunstschicht ist die "
          "**Mischungshöhe**: Darunter verteilt die Turbulenz das "
          "Aerosol, darüber liegt eine stabile Schicht, und die mischt "
          "nicht (th-stabilitaet). Die Grenze ist deshalb keine Grenze "
          "des Staubs, sondern eine Grenze des Austauschs -- sie macht "
          "die Inversion sichtbar, in genau der Höhe, in der sie liegt. "
          "Dass die Berge blau werden und nicht schwarz, ist das "
          "**Luftlicht**: Zwischen Auge und Berg wird Sonnenlicht in "
          "den Sehstrahl hineingestreut, und was hineingestreut wird, "
          "ist blau (op-streuung). Der dunkle Wald liefert über die "
          "Entfernung $x$ nur noch $e^{-\\beta x}$ seiner eigenen Helligkeit, "
          "das Luftlicht aber den Rest: Der Kontrast geht gegen null, "
          "die Farbe gegen Himmelsblau.\n\n"
          "**Die Zahl.** Koschmieder umgekehrt gelesen: Wer weiß, wie "
          "weit der entfernteste noch erkennbare Gipfel steht, hat den "
          "Extinktionskoeffizienten gemessen, $\\beta = 3{,}9/V$. Ein "
          "Gipfel in 40 km heißt $\\beta = 9{,}75\\cdot 10^{-5}$ /m; wenn "
          "dieselbe Landmarke am nächsten Tag verschwunden ist und nur "
          "noch die 10-km-Kirche steht, ist $\\beta = 3{,}9\\cdot 10^{-4}$ /m -- "
          "**viermal mehr Aerosol in derselben Luftsäule, binnen eines "
          "Tages**. Deshalb lohnt es sich, drei Landmarken in "
          "bekannter Entfernung auszusuchen und die Sichtweite nicht "
          "zu schätzen, sondern abzulesen.\n\n"
          "**Was man daraus schließt.** Dunst ist kein Wetter, sondern "
          "ein Anzeiger: Er steht im Hoch, weil Absinken die "
          "Mischungshöhe drückt und das Aerosol in eine dünnere Schicht "
          "presst, und er verschwindet mit der Kaltfront, weil "
          "Hebung und Durchmischung die Säule auf 3 km aufziehen. Wer "
          "morgens die Oberkante tief sieht, weiß, dass die Thermik "
          "flach bleibt -- und dass am Abend der Horizont wieder "
          "orange wird.",
          "**What is visible.** From a mountain the haze lies as a "
          "layer in the valley, and it has an **upper edge** -- often "
          "so sharp one could cover it with a hand. From below the same "
          "boundary appears as the height at which the sky stops being "
          "turbid. Distant mountains do not get darker with distance "
          "but paler and bluer, until the last ridge is no more than a "
          "shade of the sky. After a cold front the long view opens up; "
          "after three days of high pressure the same ridge has "
          "vanished.\n\n"
          "**What it is.** The top of the haze layer is the **mixing "
          "height**: below it turbulence spreads the aerosol, above it "
          "lies a stable layer, and that does not mix "
          "(th-stabilitaet). The boundary is therefore not a boundary "
          "of dust but a boundary of exchange -- it makes the inversion "
          "visible, at exactly the height where it sits. That the "
          "mountains turn blue and not black is **airlight**: between "
          "eye and mountain sunlight is scattered into the line of "
          "sight, and what is scattered in is blue (op-streuung). Over "
          "the distance $x$ the dark forest delivers only $e^{-\\beta x}$ of its "
          "own brightness, while airlight supplies the remainder: the "
          "contrast tends to zero, the colour to sky blue.\n\n"
          "**The number.** Koschmieder read backwards: anyone who "
          "knows how far away the most distant recognisable summit "
          "stands has measured the extinction coefficient, "
          "$\\beta = 3{.}9/V$. A summit at 40 km means "
          "$\\beta = 9{.}75\\cdot 10^{-5}$ /m; if the same landmark has gone the "
          "next day and only the church at 10 km is left, "
          "$\\beta = 3{.}9\\cdot 10^{-4}$ /m -- **four times as much aerosol in "
          "the same column of air, within one day**. Hence it pays to "
          "pick three landmarks at known distances and to read the "
          "visibility off rather than guess it.\n\n"
          "**What follows.** Haze is not weather but an indicator: it "
          "builds under a high, because subsidence presses the mixing "
          "height down and squeezes the aerosol into a thinner layer, "
          "and it clears with the cold front, because lifting and "
          "mixing stretch the column to 3 km. Whoever sees a low upper "
          "edge in the morning knows the thermals will stay shallow -- "
          "and that the horizon will be orange again in the evening."),
        "skizze-streuung", [
        zahl(t("Der entfernteste erkennbare Gipfel steht 40 km weit. "
               "Wie groß ist β? (in 10⁻⁵ /m, zwei Nachkommastellen)",
               "The most distant recognisable summit stands 40 km "
               "away. How large is β? (in 10⁻⁵ /m, two decimals)"),
             rund(BETA_40KM / 1e-5, 2), t("10⁻⁵ /m", "10⁻⁵ /m"),
             t("`β = 3,9/V = 3,9 / 40 000 m = 9,75·10⁻⁵ /m`. Knapp "
               "zehnmal der Wert reiner Luft -- 40 km Sicht sind schon "
               "ein guter Tag, keine saubere Atmosphäre.",
               "`β = 3.9/V = 3.9 / 40 000 m = 9.75·10⁻⁵ /m`. Nearly ten "
               "times the value for clean air -- 40 km of visibility "
               "is already a good day, not a clean atmosphere."),
             toleranz=0.05),
        zahl(t("Am nächsten Tag reicht die Sicht nur noch 10 km. Um "
               "welchen Faktor hat β zugenommen?",
               "The next day the view reaches only 10 km. By what "
               "factor has β risen?"),
             rund(BETA_10KM / BETA_40KM, 1), t("", ""),
             t("β geht wie `1/V`, also genau Faktor 4. Die Luftsäule "
               "ist dieselbe; was sich geändert hat, ist die "
               "Aerosolbeladung und meist auch die Feuchte, die das "
               "Aerosol anschwellen lässt.",
               "β goes as `1/V`, hence exactly a factor of 4. The "
               "column of air is the same; what changed is the aerosol "
               "load and usually the humidity, which makes the aerosol "
               "swell."),
             toleranz=0.03),
        mc(t("Warum wird ein dunkler Bergrücken mit der Entfernung "
             "heller und blauer statt dunkler?",
             "Why does a dark ridge become brighter and bluer with "
             "distance instead of darker?"),
           [t("Weil die Luft dazwischen Blau absorbiert.",
              "Because the air in between absorbs blue."),
            t("Weil die Erdkrümmung den Fuß des Bergs verdeckt.",
              "Because the Earth's curvature hides the foot of the "
              "mountain."),
            t("Sein eigenes Licht wird mit e^(−βx) geschwächt, "
              "gleichzeitig wird blaues Luftlicht in den Sehstrahl "
              "gestreut -- der Kontrast geht gegen null, die Farbe "
              "gegen Himmelsblau.",
              "Its own light is attenuated as e^(−βx) while blue "
              "airlight is scattered into the line of sight -- the "
              "contrast tends to zero, the colour to sky blue."),
            t("Weil ferne Berge höher liegen und mehr Sonne bekommen.",
              "Because distant mountains are higher and get more "
              "sun.")], 2,
           t("Kontrast ist eine Differenz, und das Luftlicht addiert "
             "sich zu beiden Seiten der Differenz. Deshalb ist die "
             "Sichtweite eine Kontrastschwelle (2 %) und keine "
             "Helligkeitsschwelle.",
             "Contrast is a difference, and airlight adds to both sides "
             "of that difference. That is why visibility is a contrast "
             "threshold (2 %) and not a brightness threshold.")),
        ]),

    lektion("hi-windzeichen",
        t("Windzeichen: Rauch, Bäume, Wellen, Böen",
          "Signs of wind: smoke, trees, waves, gusts"),
        ["beaufort", "logarithmisches-profil", "boeigkeit"],
        t("**Was zu sehen ist.** Eine Rauchfahne, die als dünnes Band "
          "kilometerweit waagrecht liegt und sich kaum verdünnt. Eine "
          "zweite, die in Schlaufen auf und ab schlägt und manchmal den "
          "Boden berührt. Blattunterseiten, die umklappen; Gras, das in "
          "Wellen läuft; auf dem Wasser erst Kräuselung, dann "
          "Schaumkämme, dann Schaumstreifen **in** der Windrichtung. "
          "Und oben: tiefe Wolken, die sichtbar anders ziehen als der "
          "Wind am Boden weht.\n\n"
          "**Was das ist.** Die beiden Rauchfahnen sind die beiden "
          "Vorzeichen von $d\\theta/dz$. In einer Inversion steigt der Rauch "
          "bis zu seinem Auftriebsniveau und breitet sich dort flach "
          "aus: stabil, keine Vermischung, schlechte Luft. In labiler "
          "Schichtung reißen die Thermikblasen die Fahne auf und holen "
          "sie bis zum Boden: labil und böig. **Böigkeit ist "
          "heruntergemischter Impuls** -- dieselbe Turbulenz, die "
          "Wärme nach oben trägt, trägt schnellen Wind nach unten. "
          "Dass der Bodenwind schräg zum Wolkenzug steht, ist die "
          "Ekman-Spirale aus dy-reibung: In der Reibungsschicht ist die "
          "Druckgradientkraft nicht mehr durch Coriolis allein "
          "ausgeglichen, der Wind dreht zum tiefen Druck hin, über Land "
          "um 20 bis 30°, über See um 10 bis 15°, und die Schicht ist "
          "$D = \\pi\\sqrt{2K/f} \\approx 1400$ m dick. Mit Buys-Ballot "
          "(dy-geostrophisch) wird daraus eine Richtungsangabe: Rücken "
          "zum Wind, dann liegt das Tief links -- und ein Tief links "
          "vorne heißt, die Front kommt noch.\n\n"
          "**Die Zahlen.** Zwei, und beide braucht man draußen. Erstens "
          "das logarithmische Profil: Über Gras ($z_0 = 3$ cm) ist der "
          "Wind in 10 m um den Faktor $\\ln(10/z_0)/\\ln(2/z_0) = 1{,}38$ "
          "stärker als der, den man im Gesicht hat; über einem Vorort "
          "($z_0 = 0{,}5$ m) sind es 2,2. Die Wettermeldung gilt für 10 m "
          "über freiem Gras -- gefühlter Wind ist nicht derselbe Wind. "
          "Zweitens Beaufort als Widerstandsleiter: $v = 0{,}836\\,B^{1{,}5}$ "
          "m/s. B 6 sind 12,3 m/s, Staudruck $\\rho v^2/2 = 92$ Pa, auf "
          "einen Quadratmeter 92 N -- 9,4 kg Zug. Weil $q \\propto v^2$ und "
          "$v \\propto B^{1{,}5}$, geht der Druck wie $B^3$: B 12 ist nicht "
          "doppelt so stark wie B 6, sondern **achtmal** (740 Pa).\n\n"
          "**Was man daraus schließt.** Rauch, Bäume und Wellen geben "
          "nicht nur die Stärke, sondern die Schichtung; die Differenz "
          "zwischen Bodenwind und Wolkenzug gibt die Lage des Tiefs; "
          "und die dritte Potenz erklärt, warum zwischen \"frisch\" und "
          "\"Sturm\" nicht ein Unterschied im Gefühl liegt, sondern "
          "einer im Schaden.",
          "**What is visible.** A smoke plume that lies flat as a thin "
          "ribbon for kilometres and hardly spreads. A second one that "
          "loops up and down and now and then touches the ground. "
          "Undersides of leaves turning over; grass running in waves; "
          "on water first ripples, then whitecaps, then streaks of foam "
          "**along** the wind. And above: low clouds visibly moving "
          "differently from the wind at the ground.\n\n"
          "**What it is.** The two plumes are the two signs of $d\\theta/dz$. "
          "In an inversion the smoke rises to its level of buoyancy and "
          "spreads out flat there: stable, no mixing, bad air. In "
          "unstable stratification thermals tear the plume apart and "
          "bring it down to the ground: unstable and gusty. "
          "**Gustiness is momentum mixed down** -- the same turbulence "
          "that carries heat up carries fast wind down. That the "
          "surface wind stands at an angle to the cloud motion is the "
          "Ekman spiral from dy-reibung: in the friction layer the "
          "pressure gradient force is no longer balanced by Coriolis "
          "alone, the wind turns towards low pressure, by 20 to 30° "
          "over land, 10 to 15° over sea, and the layer is "
          "$D = \\pi\\sqrt{2K/f} \\approx 1400$ m deep. With Buys-Ballot "
          "(dy-geostrophisch) that becomes a bearing: back to the wind, "
          "and the low lies to your left -- and a low to the left and "
          "ahead means the front is still to come.\n\n"
          "**The numbers.** Two, and both are needed outdoors. First "
          "the logarithmic profile: over grass ($z_0 = 3$ cm) the wind at "
          "10 m is stronger than the one in your face by the factor "
          "$\\ln(10/z_0)/\\ln(2/z_0) = 1{.}38$; over a suburb ($z_0 = 0{.}5$ m) it is "
          "2.2. The weather report applies to 10 m over open grass -- "
          "felt wind is not the same wind. Second, Beaufort as a drag "
          "ladder: $v = 0{.}836\\,B^{1{.}5}$ m/s. B 6 is 12.3 m/s, dynamic "
          "pressure $\\rho v^2/2 = 92$ Pa, on one square metre 92 N -- a pull "
          "of 9.4 kg. Because $q \\propto v^2$ and $v \\propto B^{1{.}5}$, the "
          "pressure goes as $B^3$: B 12 is not twice as strong as B 6 but "
          "**eight times** (740 Pa).\n\n"
          "**What follows.** Smoke, trees and waves give not only the "
          "strength but the stratification; the difference between "
          "surface wind and cloud motion gives the position of the low; "
          "and the third power explains why the step from \"fresh\" to "
          "\"gale\" is not a difference in feel but a difference in "
          "damage."),
        "skizze-ekman", [
        zahl(t("Windgeschwindigkeit bei Beaufort 6? (in m/s, eine "
               "Nachkommastelle)",
               "Wind speed at Beaufort 6? (in m/s, one decimal)"),
             rund(V_B6, 1), t("m/s", "m/s"),
             t("`v = 0,836 × 6^1,5 = 0,836 × 14,70 = 12,3 m/s` -- "
               "44 km/h, 'starker Wind', große Zweige in Bewegung.",
               "`v = 0.836 × 6^1.5 = 0.836 × 14.70 = 12.3 m/s` -- "
               "44 km/h, 'strong breeze', large branches in motion."),
             toleranz=0.03),
        zahl(t("Staudruck dieses Winds auf eine Fläche quer dazu "
               "(ρ = 1,225 kg/m³)? (in Pa)",
               "Dynamic pressure of that wind on a surface across it "
               "(ρ = 1.225 kg/m³)? (in Pa)"),
             rund(STAUDRUCK_B6), t("Pa", "Pa"),
             t("`q = ρv²/2 = 1,225 × 12,3² / 2 = 92 Pa`, auf 1 m² also "
               "92 N. Bei B 12 sind es 740 Pa: achtmal, weil `q ∝ B³`.",
               "`q = ρv²/2 = 1.225 × 12.3² / 2 = 92 Pa`, hence 92 N on "
               "1 m². At B 12 it is 740 Pa: eight times, because "
               "`q ∝ B³`."),
             toleranz=0.05),
        mc(t("Zwei Schornsteine, gleicher Wind: Der eine Rauch liegt "
             "als dünnes Band kilometerweit flach, der andere schlägt "
             "in Schlaufen und erreicht den Boden. Was unterscheidet "
             "die beiden Luftmassen?",
             "Two chimneys, the same wind: one plume lies flat as a "
             "thin ribbon for kilometres, the other loops and reaches "
             "the ground. What distinguishes the two air masses?"),
           [t("Der erste Rauch ist wärmer.",
              "The first plume is warmer."),
            t("Der zweite Schornstein ist höher.",
              "The second chimney is taller."),
            t("Das flache Band steht in stabiler Schichtung (dθ/dz > 0, "
              "keine vertikale Vermischung), die Schlaufen in labiler "
              "-- Thermikblasen reißen die Fahne auf und mischen sie "
              "bis zum Boden.",
              "The flat ribbon sits in stable stratification "
              "(dθ/dz > 0, no vertical mixing), the loops in unstable "
              "-- thermals tear the plume apart and mix it down to the "
              "ground."),
            t("Beim zweiten weht es in der Höhe aus einer anderen "
              "Richtung.",
              "Above the second one the wind comes from a different "
              "direction.")], 2,
           t("Dieselbe Diagnose wie am Emagramm, nur mit Rauch statt "
             "Radiosonde: Das flache Band ist eine Inversion, die "
             "Schlaufen sind eine durchmischte Grenzschicht -- und "
             "deshalb ist die zweite Luft böig und die erste schlecht.",
             "The same diagnosis as on the emagram, with smoke instead "
             "of a radiosonde: the flat ribbon is an inversion, the "
             "loops are a mixed boundary layer -- which is why the "
             "second air is gusty and the first is foul.")),
        ]),

    lektion("hi-niederschlag",
        t("Niederschlag am Aussehen erkennen",
          "Telling precipitation by its look"),
        ["niederschlagsarten", "fallgeschwindigkeit", "virga"],
        t("**Was zu sehen ist.** Nieseln: Tropfen, die man einzeln "
          "nicht sieht, ein Vorhang ohne Struktur, aus einer tiefen "
          "grauen Schicht, die Sicht unter 2 km. Landregen: "
          "gleichmäßig, stundenlang, kein Rand. Schauer: ein Vorhang "
          "mit **scharfem Rand**, der über die Landschaft wandert, "
          "dahinter wieder Sonne. Graupel: weiße, weiche Körner, die "
          "hüpfen. Hagel: harte Körner mit Schalen. Und **Fallstreifen** "
          "(Virga), die unter der Wolkenbasis anfangen und in der Luft "
          "aufhören.\n\n"
          "**Was das ist.** Die Form folgt dem Wachstumsweg aus "
          "wo-wachstum: Diffusion bringt einen Tropfen in zwanzig "
          "Minuten auf 10 μm und dann nicht weiter, weil $r^2$ linear mit "
          "der Zeit geht; auf 1 mm kommt nur die **Koaleszenz**, und "
          "die braucht eine dicke Wolke und Zeit. Deshalb heißt feiner "
          "Niesel: flache Wolke, lange Verweilzeit, keine Eisphase. "
          "Deshalb heißt Schauer mit scharfem Rand: eine einzelne Zelle "
          "mit kräftigem Aufwind, in der große Tropfen in Minuten "
          "entstehen. Graupel ist bereifter Schnee (Eis sammelt "
          "unterkühlte Tröpfchen ein), Hagel ist derselbe Vorgang "
          "mehrfach in einem Aufwind, der die Körner trägt, bis sie zu "
          "schwer sind. Und die Flockengröße ist ein Thermometer: Große "
          "nasse Flocken gibt es nur knapp unter 0 °C, weil ein "
          "Wasserfilm die Kristalle verklebt; bei −15 °C sind sie "
          "trocken und fallen als Griesel.\n\n"
          "**Die Zahl, und ihre Grenze.** Die Stokes-Geschwindigkeit "
          "$v = 2\\rho_w g r^2/(9\\eta)$ gibt für 10 μm Radius 1,2 cm/s -- "
          "deshalb schwebt eine Wolke. Sie gilt aber nur, solange "
          "$Re = 2rv/\\nu < 1$, und das ist bei etwa **40 μm** vorbei "
          "(v = 0,19 m/s, Re = 1). Für einen Regentropfen von 1 mm "
          "Durchmesser liefert Stokes 30 m/s, gemessen sind 6,5 m/s: "
          "Faktor 4,7 daneben, weil die Nachlaufströmung längst "
          "turbulent ist. Das ist die Fußnote, die wo-wachstum fehlt. "
          "Mit den gemessenen Werten gerechnet: aus 2 km Basishöhe "
          "braucht der 1-mm-Tropfen 5,1 Minuten, ein 0,2-mm-Nieseltropfen "
          "bei 0,72 m/s aber 46 Minuten -- und in 46 Minuten verdunstet "
          "er in trockener Luft. **Deshalb erreicht Niesel nur aus "
          "tiefen Wolken den Boden, und deshalb ist jede Virga ein "
          "Hinweis auf trockene Luft unter der Wolke.**\n\n"
          "**Was man daraus schließt.** Tropfengröße, Randschärfe und "
          "Fallstreifenlänge sagen zusammen, was für eine Wolke oben "
          "steht und wie trocken die Luft darunter ist -- ohne Radar, "
          "aus dem Fenster.",
          "**What is visible.** Drizzle: drops one cannot see "
          "individually, a curtain without structure, out of a low grey "
          "layer, visibility below 2 km. Steady rain: even, for hours, "
          "no edge. A shower: a curtain with a **sharp edge** that "
          "travels across the landscape, sunshine behind it. Soft hail: "
          "white, soft grains that bounce. Hail: hard stones with "
          "shells. And **fall streaks** (virga) that begin below the "
          "cloud base and end in mid-air.\n\n"
          "**What it is.** The form follows the growth path from "
          "wo-wachstum: diffusion takes a drop to 10 μm in twenty "
          "minutes and no further, because $r^2$ grows linearly with time; "
          "to 1 mm only **coalescence** gets there, and that needs a "
          "deep cloud and time. Hence fine drizzle means: shallow "
          "cloud, long residence time, no ice phase. Hence a shower "
          "with a sharp edge means a single cell with a strong updraught "
          "in which large drops form within minutes. Soft hail is rimed "
          "snow (ice collecting supercooled droplets), hail is the same "
          "process repeated in an updraught that carries the stones "
          "until they are too heavy. And flake size is a thermometer: "
          "large wet flakes occur only just below 0 °C, because a film "
          "of water glues the crystals together; at −15 °C they are dry "
          "and fall as grains.\n\n"
          "**The number, and where it stops.** The Stokes velocity "
          "$v = 2\\rho_w g r^2/(9\\eta)$ gives 1.2 cm/s for a 10 μm radius -- "
          "which is why a cloud floats. But it holds only while "
          "$Re = 2rv/\\nu < 1$, and that is over at about **40 μm** "
          "(v = 0.19 m/s, Re = 1). For a raindrop of 1 mm diameter "
          "Stokes gives 30 m/s where 6.5 m/s is measured: a factor of "
          "4.7 out, because the wake has long gone turbulent. That is "
          "the footnote wo-wachstum lacks. Computed with the measured "
          "values: from a 2 km cloud base the 1 mm drop takes 5.1 "
          "minutes, a 0.2 mm drizzle drop at 0.72 m/s takes 46 minutes "
          "-- and in 46 minutes it evaporates in dry air. **That is why "
          "drizzle reaches the ground only from low clouds, and why "
          "every virga points to dry air below the cloud.**\n\n"
          "**What follows.** Drop size, edge sharpness and the length "
          "of the fall streaks together say what kind of cloud stands "
          "above and how dry the air beneath it is -- without radar, "
          "from the window."),
        "skizze-wachstum", [
        zahl(t("Stokes: Fallgeschwindigkeit eines Wolkentropfens von "
               "10 μm Radius? (in cm/s, eine Nachkommastelle)",
               "Stokes: terminal velocity of a cloud drop of 10 μm "
               "radius? (in cm/s, one decimal)"),
             rund(STOKES_10UM * 100.0, 1), t("cm/s", "cm/s"),
             t("`v = 2 × 1000 × 9,81 × (10⁻⁵)² / (9 × 1,8·10⁻⁵) = "
               "0,012 m/s = 1,2 cm/s`. Ein Aufwind von 2 cm/s hält ihn "
               "oben -- das kann jede Wolke.",
               "`v = 2 × 1000 × 9.81 × (10⁻⁵)² / (9 × 1.8·10⁻⁵) = "
               "0.012 m/s = 1.2 cm/s`. An updraught of 2 cm/s holds it "
               "up -- any cloud can manage that."),
             toleranz=0.05),
        zahl(t("Wie lange fällt ein 1-mm-Regentropfen (6,5 m/s) aus "
               "einer Basis in 2 km Höhe? (in min, eine "
               "Nachkommastelle)",
               "How long does a 1 mm raindrop (6.5 m/s) fall from a "
               "base at 2 km? (in min, one decimal)"),
             rund(FALLZEIT_1MM, 1), t("min", "min"),
             t("`2000 / 6,5 = 308 s = 5,1 min`. Der Nieseltropfen mit "
               "0,72 m/s braucht 46 Minuten und kommt in trockener Luft "
               "nicht an: Das ist die Virga.",
               "`2000 / 6.5 = 308 s = 5.1 min`. The drizzle drop at "
               "0.72 m/s needs 46 minutes and does not arrive in dry "
               "air: that is virga."),
             toleranz=0.05),
        mc(t("Warum fallen große nasse Flocken nur knapp unter 0 °C "
             "und bei −15 °C feiner Griesel?",
             "Why do large wet flakes fall only just below 0 °C and "
             "fine grains at −15 °C?"),
           [t("Knapp unter 0 °C trägt jeder Kristall einen Wasserfilm "
              "und verklebt beim Zusammenstoß mit anderen; bei −15 °C "
              "sind die Kristalle trocken und prallen ab.",
              "Just below 0 °C every crystal carries a film of water "
              "and sticks on collision; at −15 °C the crystals are dry "
              "and bounce off."),
            t("Bei −15 °C ist weniger Dampf da, deshalb bleiben die "
              "Kristalle klein.",
              "At −15 °C there is less vapour, so the crystals stay "
              "small."),
            t("Kalte Luft ist dichter und bremst das Wachstum.",
              "Cold air is denser and slows the growth."),
            t("Bei −15 °C fällt der Schnee schneller und hat weniger "
              "Zeit.",
              "At −15 °C the snow falls faster and has less time.")], 0,
           t("Aggregation ist Klebstoff, nicht Wachstum: Die einzelnen "
             "Kristalle sind bei −15 °C sogar größer (dort ist die "
             "Differenz der Dampfdrücke über Eis und Wasser maximal, "
             "wo-wachstum), aber sie haften nicht. Deshalb ist "
             "Flockengröße ein Thermometer für die Schicht knapp über "
             "dem Boden.",
             "Aggregation is glue, not growth: at −15 °C the individual "
             "crystals are in fact larger (that is where the difference "
             "in vapour pressure over ice and water is greatest, "
             "wo-wachstum), but they do not stick. Flake size is "
             "therefore a thermometer for the layer just above the "
             "ground.")),
        ]),
    ])


# ===========================================================================
# 13  Spuren am Boden
# ===========================================================================

SIGMA_283 = SIGMA * 283.15 ** 4                 # W/m², Boden bei 10 °C
L_AB_KLAR = 294.0                               # W/m², Gegenstrahlung klar
NETTO_FREI = SIGMA_283 - L_AB_KLAR              # W/m², freies Feld, ψ = 1
HIMMELSFAKTOR_KRONE = 0.3                       # ψ unter einer Baumkrone
NETTO_KRONE = HIMMELSFAKTOR_KRONE * NETTO_FREI  # W/m²
TAU_GRENZE_MM = 60.0 * 8 * 3600.0 / L_V         # mm: alle Energie in Tau
MULDE_OHNE_AUSTAUSCH = 60.0 * 6 * 3600.0 / (1.2 * C_P * 10.0)   # K
MULDE_MISCHHOEHE = 60.0 * 6 * 3600.0 / (1.2 * C_P * 8.0)        # m bei 8 K
E_MISCH = (e_s(0.0) + e_s(20.0)) / 2.0          # hPa, halb und halb
RH_MISCH = 100.0 * E_MISCH / e_s(10.0)          # %
FLUESSIG_MISCH = 0.622 * (E_MISCH - e_s(10.0)) / 1000.0 * 1000.0  # g/kg
AUTOKONVEKTIV = G / R_L * 1000.0                # K/km
ASPHALT_FAKTOR = 10000.0 / AUTOKONVEKTIV        # 10 K/m, in Vielfachen

K_BODEN = kapitel(
    "boden", t("Spuren am Boden: Tau, Reif, Nebel, Flimmern",
               "Traces at the ground: dew, frost, fog, shimmer"), 4,
    t("Die Strahlungsbilanz des Bodens steht in st-tagesgang. Hier wird "
      "sie besichtigt: Jedes nasse Grasblatt, jede Reifnadel, jeder "
      "Nebelfetzen und jedes Flimmern über dem Asphalt ist ein Glied "
      "dieser Bilanz -- und jedes lässt sich nachrechnen.",
      "The surface radiation budget stands in st-tagesgang. Here it is "
      "inspected: every wet blade of grass, every needle of frost, "
      "every patch of fog and every shimmer over the asphalt is a term "
      "of that budget -- and each one can be checked by "
      "calculation."), [

    lektion("bo-tau",
        t("Tau, Reif und der Kaltluftsee in der Senke",
          "Dew, frost and the cold pool in the hollow"),
        ["tau", "reif", "himmelsblickfaktor"],
        t("**Was zu sehen ist.** Am Morgen ist das Gras nass und der "
          "Gehsteig daneben trocken. Das Autodach ist beschlagen, die "
          "Motorhaube weniger, der große Stein im Garten gar nicht. "
          "Unter dem Apfelbaum steht eine trockene Insel im nassen "
          "Rasen, und unter einer Wolkendecke gibt es überhaupt keinen "
          "Tau. Im Winter ist die Brücke weiß, während die Straße davor "
          "und dahinter schwarz bleibt. Reif liegt als **Nadeln** auf "
          "dem Blatt, gefrorener Tau als **Perlen**; nach einer "
          "Nebelnacht sitzt Rauhreif in Fahnen an den Zweigen, immer "
          "gegen den Wind. Und im Frühjahr ist der Frost in der Senke, "
          "während es fünfzig Meter höher am Hang frostfrei bleibt.\n\n"
          "**Was das ist.** Alles sind Glieder der Bilanz aus "
          "st-tagesgang, aber mit einem Faktor, der dort fehlt: Der "
          "Boden verliert nicht gegen den ganzen Himmel, sondern gegen "
          "den Teil, den er **sieht**. Mit dem Himmelsblickfaktor $\\psi$ "
          "(1 im freien Feld, 0,3 unter einer Krone, 0 in der Garage) "
          "ist der Verlust $L_{netto} = \\psi\\,(\\sigma T_s^4 - L_\\downarrow)$. Bei 10 °C "
          "strahlt der Boden 364 W/m², die klare Atmosphäre 294 W/m² "
          "zurück: im Freien **70 W/m²**, unter dem Baum **21 W/m²**. "
          "Deshalb die trockene Insel. Der zweite Faktor ist die "
          "Ankopplung nach unten: Ein Grasblatt hat fast keine "
          "Wärmekapazität und steckt in stehender Luft, es folgt der "
          "Strahlung sofort; Asphalt und Stein ziehen Wärme aus dem "
          "Erdboden nach (der Bodenwärmestrom `G`) und bleiben wärmer. "
          "Die Brücke hat gar kein Erdreich unter sich: $G = 0$, und "
          "deshalb friert sie zuerst. Ob **Reif** oder gefrorener Tau "
          "entsteht, entscheidet die Reihenfolge: Fällt die Temperatur "
          "erst unter 0 °C und dann unter den Taupunkt, geht der Dampf "
          "direkt in Eis über (Resublimation, Nadeln), weil $e_s$ über Eis "
          "kleiner ist als über Wasser (wo-wachstum); umgekehrt "
          "gefriert ein schon gebildeter Tautropfen (Perlen). Rauhreif "
          "ist etwas Drittes: unterkühlte **Nebeltröpfchen**, die beim "
          "Anprall festfrieren -- deshalb wächst er dem Wind "
          "entgegen.\n\n"
          "**Die Zahlen.** Erstens eine Obergrenze: Wenn die ganze "
          "Ausstrahlung einer Nacht in Kondensation ginge, gäbe "
          "60 W/m² über 8 Stunden gerade $1{,}73$ MJ/m², geteilt durch "
          "$L_v = 2{,}5$ MJ/kg sind das 0,69 kg/m², also **0,69 mm Tau**. "
          "Gemessen werden 0,1 bis 0,3 mm -- der Rest des Verlusts geht "
          "in den Boden und in die Luft. Die Abschätzung nagelt die "
          "Größenordnung fest und sagt gleich, wo sie zu hoch liegt. "
          "Zweitens die Senke: eine Mulde von 100 m Breite und 10 m "
          "Tiefe, 60 W/m² über 6 Stunden. Ohne jeden Austausch gäbe das "
          "$\\Delta T = Q t/(\\rho c_p h) = 108$ K -- absurd, also **muss** "
          "ausgetauscht werden. Umgekehrt gerechnet: Die gemessenen 8 K "
          "brauchen eine Schicht von $Q t/(\\rho c_p \\Delta T) = 134$ m. So dick "
          "ist der Kaltluftsee, und so weit reicht die Bodeninversion.\n\n"
          "**Was man daraus schließt.** Kalte Luft hat ein kleineres θ "
          "(th-theta) und fließt wie Wasser hangabwärts; deshalb liegt "
          "der Frost unten, deshalb legt man Obstgärten an den Hang und "
          "nicht in die Mulde. Und wer in der Meldung \"Bodenfrost\" "
          "liest, soll wissen, dass die in 5 cm Höhe gemeint ist: In "
          "klarer Nacht sind es dort 3 bis 5 K weniger als in der "
          "Hütte in 2 m.",
          "**What is visible.** In the morning the grass is wet and the "
          "pavement beside it dry. The car roof is fogged, the bonnet "
          "less so, the large stone in the garden not at all. Under the "
          "apple tree a dry island stands in the wet lawn, and under a "
          "cloud deck there is no dew at all. In winter the bridge is "
          "white while the road before and after it stays black. Frost "
          "sits as **needles** on the leaf, frozen dew as **beads**; "
          "after a foggy night hoar frost sits in vanes on the twigs, "
          "always into the wind. And in spring the frost is in the "
          "hollow while fifty metres higher up the slope it stays "
          "frost-free.\n\n"
          "**What it is.** All of it belongs to the budget of "
          "st-tagesgang, but with a factor that is missing there: the "
          "ground does not lose against the whole sky, only against "
          "the part it **sees**. With the sky view factor $\\psi$ (1 in the "
          "open field, 0.3 under a canopy, 0 in a garage) the loss is "
          "$L_{net} = \\psi\\,(\\sigma T_s^4 - L_\\downarrow)$. At 10 °C the ground emits "
          "364 W/m² and the clear atmosphere returns 294 W/m²: in the "
          "open **70 W/m²**, under the tree **21 W/m²**. Hence the dry "
          "island. The second factor is the coupling downward: a blade "
          "of grass has almost no heat capacity and sits in still air, "
          "so it follows the radiation at once; asphalt and stone draw "
          "heat up from the soil (the ground heat flux `G`) and stay "
          "warmer. A bridge has no soil beneath it at all: $G = 0$, and "
          "that is why it freezes first. Whether **frost** or frozen "
          "dew forms is decided by the order of events: if the "
          "temperature drops below 0 °C before it drops below the dew "
          "point, the vapour goes straight to ice (deposition, "
          "needles), because $e_s$ over ice is lower than over water "
          "(wo-wachstum); the other way round, an existing dew drop "
          "freezes (beads). Hoar frost is a third thing: supercooled "
          "**fog droplets** that freeze on impact -- which is why it "
          "grows into the wind.\n\n"
          "**The numbers.** First an upper bound: if a whole night's "
          "radiative loss went into condensation, 60 W/m² over 8 hours "
          "would give $1{.}73$ MJ/m², divided by $L_v = 2{.}5$ MJ/kg that is "
          "0.69 kg/m², hence **0.69 mm of dew**. Measured values are "
          "0.1 to 0.3 mm -- the rest of the loss goes into the soil and "
          "into the air. The estimate pins the order of magnitude and "
          "says at once where it is too high. Second the hollow: a "
          "depression 100 m across and 10 m deep, 60 W/m² over 6 hours. "
          "Without any exchange that would give "
          "$\\Delta T = Q t/(\\rho c_p h) = 108$ K -- absurd, so exchange "
          "**must** happen. Read backwards: the measured 8 K require a "
          "layer of $Q t/(\\rho c_p \\Delta T) = 134$ m. That is how deep the cold "
          "pool is, and how far the surface inversion reaches.\n\n"
          "**What follows.** Cold air has a smaller θ (th-theta) and "
          "drains downhill like water; that is why the frost lies at "
          "the bottom, and why orchards are planted on the slope and "
          "not in the hollow. And whoever reads \"ground frost\" in a "
          "forecast should know it means 5 cm above the soil: on a "
          "clear night it is 3 to 5 K colder there than in the screen "
          "at 2 m."),
        "skizze-tagesgang", [
        zahl(t("Obergrenze der Taumenge: 60 W/m² über 8 Stunden, alles "
               "in Kondensation (L_v = 2,5 MJ/kg). Wie viel mm? (zwei "
               "Nachkommastellen)",
               "Upper bound for the amount of dew: 60 W/m² over 8 "
               "hours, all of it into condensation (L_v = 2.5 MJ/kg). "
               "How many mm? (two decimals)"),
             rund(TAU_GRENZE_MM, 2), t("mm", "mm"),
             t("`60 × 28 800 = 1,73 MJ/m²`, geteilt durch 2,5 MJ/kg "
               "gibt 0,69 kg/m² -- und 1 kg/m² ist 1 mm. Gemessen sind "
               "0,1 bis 0,3 mm: Der Boden gibt nur einen Teil seines "
               "Verlusts an den Dampf ab.",
               "`60 × 28 800 = 1.73 MJ/m²`, divided by 2.5 MJ/kg gives "
               "0.69 kg/m² -- and 1 kg/m² is 1 mm. Measured: 0.1 to "
               "0.3 mm, so the ground passes only part of its loss on "
               "to the vapour."),
             toleranz=0.05),
        zahl(t("In der Mulde kühlt es über 6 Stunden bei 60 W/m² um "
               "8 K ab. Wie dick ist die Luftschicht, die diese "
               "Kühlung trägt? (in m)",
               "In the hollow it cools by 8 K over 6 hours at 60 W/m². "
               "How deep is the layer of air that carries this "
               "cooling? (in m)"),
             rund(MULDE_MISCHHOEHE), t("m", "m"),
             t("`h = Q·t/(ρ·c_p·ΔT) = 60 × 21 600 / (1,2 × 1004 × 8) = "
               "134 m`. Zehn Meter Mulde würden 108 K ergeben -- die "
               "Luft wird also über die Mulde hinaus gemischt, und "
               "genau diese 134 m sind die Dicke der Bodeninversion.",
               "`h = Q·t/(ρ·c_p·ΔT) = 60 × 21 600 / (1.2 × 1004 × 8) = "
               "134 m`. Ten metres of hollow would give 108 K -- so the "
               "air is mixed well beyond the hollow, and those 134 m "
               "are the depth of the surface inversion."),
             toleranz=0.05),
        mc(t("Warum ist die Brücke weiß, während die Straße davor und "
             "dahinter schwarz bleibt?",
             "Why is the bridge white while the road before and after "
             "it stays black?"),
           [t("Beton strahlt stärker ab als Asphalt.",
              "Concrete radiates more strongly than asphalt."),
            t("Unter der Brücke ist es windiger.",
              "It is windier under the bridge."),
            t("Die Brücke liegt höher und damit in kälterer Luft.",
              "The bridge is higher up and therefore in colder air."),
            t("Unter der Fahrbahn ist kein Erdreich: Der "
              "Bodenwärmestrom G fehlt, der Verlust muss allein aus der "
              "dünnen Platte kommen, und die kühlt viel schneller unter "
              "den Gefrierpunkt.",
              "There is no soil under the deck: the ground heat flux G "
              "is missing, the loss has to come out of the thin slab "
              "alone, and that cools below freezing far faster.")], 3,
           t("Dieselbe Bilanz, nur ohne den Nachschub von unten. "
             "Deshalb warnen Schilder vor Brücken und nicht vor "
             "Straßen -- und deshalb gefriert eine Pfütze auf einer "
             "Holzterrasse vor der auf dem Erdweg.",
             "The same budget, only without the supply from below. "
             "That is why warning signs stand on bridges and not on "
             "roads -- and why a puddle on a wooden deck freezes "
             "before one on bare earth.")),
        ]),

    lektion("bo-nebel",
        t("Vier Nebel und wie jeder vergeht",
          "Four kinds of fog, and how each one goes"),
        ["strahlungsnebel", "advektionsnebel", "mischungsnebel"],
        t("**Was zu sehen ist.** Vier Nebel, und man unterscheidet sie "
          "nicht am Aussehen, sondern am **Verhalten**.\n\n"
          "**Strahlungsnebel** entsteht in der zweiten Nachthälfte, "
          "liegt in Senken und Flusstälern, ist oft nur 20 bis 100 m "
          "dick, und er löst sich vormittags **von den Rändern her** "
          "auf, sobald die Sonne den Boden erreicht. Von einer Brücke "
          "sieht man dann die Dächer herausschauen. "
          "**Advektionsnebel** zieht mit dem Wind heran, wenn warme "
          "feuchte Luft über kalten Grund läuft -- über schmelzendem "
          "Schnee, über kaltem Meerwasser; er hält sich bei 5 m/s Wind "
          "und mittags genauso, und er ist der Nebel, der Tage dauert. "
          "**Mischungsnebel** steht dort, wo zwei gesättigte Luftmassen "
          "zusammenkommen: Seerauch über offenem Wasser bei "
          "Frost, der eigene Atem, die Fahne über dem Kühlturm. "
          "**Hochnebel** schließlich ist gehobener Nebel: eine "
          "Stratusdecke mit scharfer Oberkante, von oben strahlend "
          "weiß, von unten grau, und sie hält sich den ganzen Winter"
          "tag, weil die Sonne nicht an den Boden kommt.\n\n"
          "**Was das ist.** Strahlungsnebel ist die Bilanz von "
          "st-tagesgang, nur bis unter den Taupunkt weitergeführt; er "
          "verschwindet von den Rändern, weil dort zuerst Boden "
          "freiliegt, der Wärme liefert. Advektionsnebel lebt vom "
          "**Kontakt**, nicht von der Strahlung: Die Luft kühlt an der "
          "Unterlage, und solange die Unterlage kalt bleibt, hilft die "
          "Sonne nichts -- sie heizt ja nicht die Luft, sondern den "
          "Boden, und der ist hier die Senke. Hochnebels Oberkante "
          "**ist** die Inversion (fe-hebung): Darüber sinkt die Luft ab "
          "und ist trocken, darunter ist alles gesättigt.\n\n"
          "**Die Zahl -- und die neue Physik.** Warum macht Mischen "
          "Nebel? Weil $e_s(T)$ **konvex** ist. Mischt man zwei gesättigte "
          "Pakete, so mischen sich Temperatur und Dampfdruck linear, "
          "also liegt der Mischpunkt auf der **Sehne** zwischen den "
          "beiden Punkten der Sättigungskurve -- und die Sehne einer "
          "konvexen Kurve liegt **über** ihr. Konkret: 0 °C mit "
          "6,11 hPa und 20 °C mit 23,33 hPa, halb und halb gemischt, "
          "gibt 10 °C und $e = 14{,}72$ hPa, während $e_s(10) = 12{,}26$ hPa "
          "ist: **120 % relative Feuchte**. Die überschüssigen 2,46 hPa "
          "müssen kondensieren, das sind $0{,}622\\,\\Delta e/p = 1{,}5$ g/kg "
          "flüssiges Wasser -- dichter Nebel. Genau das ist der "
          "Atem im Winter, und genau das ist der Grund, warum "
          "Kondensstreifen entstehen.\n\n"
          "**Was man daraus schließt.** Wer wissen will, wann der "
          "Nebel weggeht, muss wissen, welcher es ist: Der "
          "Strahlungsnebel geht mit der Sonne, der Advektionsnebel mit "
          "dem Wind, der Mischungsnebel mit der Trennung der beiden "
          "Luftmassen, und der Hochnebel erst mit der nächsten Front.",
          "**What is visible.** Four kinds of fog, and they are told "
          "apart not by their looks but by their **behaviour**.\n\n"
          "**Radiation fog** forms in the second half of the night, "
          "lies in hollows and river valleys, is often only 20 to 100 m "
          "deep, and in the morning it dissolves **from its edges "
          "inward** as soon as the sun reaches the ground. From a "
          "bridge one then sees the roofs sticking out. **Advection "
          "fog** arrives with the wind, when warm moist air runs over "
          "cold ground -- over melting snow, over cold sea water; it "
          "survives a 5 m/s wind and noon alike, and it is the fog that "
          "lasts for days. **Mixing fog** stands where two saturated "
          "air masses meet: sea smoke over open water in frost, one's "
          "own breath, the plume over a cooling tower. **High fog**, "
          "finally, is lifted fog: a stratus deck with a sharp top, "
          "brilliant white from above, grey from below, and it holds "
          "all winter's day because the sun never reaches the "
          "ground.\n\n"
          "**What it is.** Radiation fog is the budget of st-tagesgang "
          "carried on below the dew point; it disappears from the edges "
          "because that is where bare ground is exposed first and "
          "delivers heat. Advection fog lives on **contact**, not on "
          "radiation: the air cools at the surface, and as long as the "
          "surface stays cold the sun is no help -- it heats the "
          "ground, not the air, and here the ground is the sink. The "
          "top of high fog **is** the inversion (fe-hebung): above it "
          "the air subsides and is dry, below it everything is "
          "saturated.\n\n"
          "**The number -- and the new physics.** Why does mixing make "
          "fog? Because $e_s(T)$ is **convex**. Mix two saturated parcels "
          "and temperature and vapour pressure mix linearly, so the "
          "mixture lies on the **chord** between the two points of the "
          "saturation curve -- and the chord of a convex curve lies "
          "**above** it. Concretely: 0 °C with 6.11 hPa and 20 °C with "
          "23.33 hPa, mixed half and half, give 10 °C and $e = 14{.}72$ hPa, "
          "while $e_s(10) = 12{.}26$ hPa: **120 % relative humidity**. The "
          "excess 2.46 hPa must condense, which is "
          "$0{.}622\\,\\Delta e/p = 1{.}5$ g/kg of liquid water -- dense fog. That "
          "is exactly one's breath in winter, and exactly the reason "
          "contrails exist.\n\n"
          "**What follows.** Whoever wants to know when the fog will "
          "go must know which fog it is: radiation fog goes with the "
          "sun, advection fog with the wind, mixing fog when the two "
          "air masses part, and high fog not before the next front."),
        "boden-mischungsnebel", [
        zahl(t("Zwei gesättigte Pakete, 0 °C und 20 °C, halb und halb "
               "gemischt. Relative Feuchte der Mischung? (in %)",
               "Two saturated parcels, 0 °C and 20 °C, mixed half and "
               "half. Relative humidity of the mixture? (in %)"),
             rund(RH_MISCH), t("%", "%"),
             t("`e = (6,11 + 23,33)/2 = 14,72 hPa` bei `T = 10 °C`, und "
               "`e_s(10) = 12,26 hPa`: `120 %`. Die Sehne liegt über der "
               "Kurve, weil e_s(T) exponentiell ist.",
               "`e = (6.11 + 23.33)/2 = 14.72 hPa` at `T = 10 °C`, and "
               "`e_s(10) = 12.26 hPa`: `120 %`. The chord lies above "
               "the curve because e_s(T) is exponential."),
             toleranz=0.03),
        zahl(t("Wie viel Wasser kondensiert dabei je Kilogramm Luft? "
               "(in g/kg, eine Nachkommastelle, p = 1000 hPa)",
               "How much water condenses per kilogram of air? (in "
               "g/kg, one decimal, p = 1000 hPa)"),
             rund(FLUESSIG_MISCH, 1), t("g/kg", "g/kg"),
             t("`Δr = 0,622 · Δe/p = 0,622 × 2,46/1000 = 1,5·10⁻³` "
               "oder 1,5 g/kg. Zum Vergleich: Eine gewöhnliche Wolke "
               "trägt 0,5 bis 1 g/kg -- Mischungsnebel ist dicht.",
               "`Δr = 0.622 · Δe/p = 0.622 × 2.46/1000 = 1.5·10⁻³` or "
               "1.5 g/kg. For comparison: an ordinary cloud carries 0.5 "
               "to 1 g/kg -- mixing fog is dense."),
             toleranz=0.05),
        mc(t("Ein Nebel steht um 13 Uhr noch genauso dicht wie um "
             "7 Uhr, bei schwachem Wind vom Meer. Welcher ist es, und "
             "warum hilft die Sonne nicht?",
             "At 13:00 a fog is still as dense as at 07:00, with a "
             "light wind off the sea. Which fog is it, and why does the "
             "sun not help?"),
           [t("Advektionsnebel: Die Luft kühlt am kalten Untergrund, "
              "und der bleibt kalt -- die Sonne heizt den Boden, aber "
              "hier ist der Boden die Senke, nicht die Quelle.",
              "Advection fog: the air cools at the cold surface, and "
              "that stays cold -- the sun heats the ground, but here "
              "the ground is the sink, not the source."),
            t("Strahlungsnebel: Er ist zu dick geworden.",
              "Radiation fog: it has simply grown too thick."),
            t("Mischungsnebel: Zwei Luftmassen mischen sich dauernd.",
              "Mixing fog: two air masses keep mixing."),
            t("Hochnebel: Die Inversion liegt zu hoch.",
              "High fog: the inversion lies too high.")], 0,
           t("Strahlungsnebel verschwindet, weil der Boden zur Quelle "
             "wird; über kaltem Wasser oder Schnee wird er das nie. "
             "Deshalb liegt Seenebel auch im Juli und löst sich erst "
             "auf, wenn der Wind dreht.",
             "Radiation fog goes because the ground turns into a "
             "source; over cold water or snow it never does. That is "
             "why sea fog lies there in July as well and clears only "
             "when the wind shifts.")),
        ]),

    lektion("bo-flimmern",
        t("Hitzeflimmern, Luftspiegelung und die ersten Thermiken",
          "Shimmer, mirage and the first thermals"),
        ["autokonvektiv", "luftspiegelung", "thermikbeginn"],
        t("**Was zu sehen ist.** Über dem heißen Asphalt zittert der "
          "Hintergrund, Kanten verlaufen, und am Ende der Straße "
          "spiegelt sich der Himmel als silberne Pfütze. Über dem "
          "Stoppelfeld steht eine Staubfahne und dreht sich. Gras "
          "bewegt sich für einen Augenblick, obwohl es windstill ist. "
          "Vögel kreisen, ohne zu schlagen, und steigen dabei.\n\n"
          "**Was das ist.** Alles dasselbe: Die unterste Luftschicht "
          "ist nicht nur labil, sie ist **weit jenseits** jedes "
          "adiabatischen Maßes labil. In den ersten Millimetern über "
          "dem Boden gibt es keine Turbulenz mehr, dort trägt nur noch "
          "Wärmeleitung, und Luft leitet miserabel -- also baut sich "
          "ein gewaltiger Gradient auf. Jede Dichteschwankung ist "
          "damit auch eine Schwankung der Brechzahl ($n - 1 \\approx 2{,}9\\cdot 10^{-4}$ "
          "bei Normaldruck, proportional zur Dichte): Deshalb flimmert "
          "es. Weil die Brechzahl **nach oben zunimmt**, werden flach "
          "einfallende Strahlen nach oben weggekrümmt; ein Strahl vom "
          "Himmel erreicht das Auge, nachdem er über dem Asphalt "
          "umgelenkt wurde -- die Pfütze ist der Himmel, nicht Wasser. "
          "Und die Schicht ist nicht stabil zu halten: Sie bricht in "
          "Blasen auf, und das sind die ersten Thermiken des Tages "
          "(th-stabilitaet). Der Staubteufel ist eine solche Blase mit "
          "Drehimpuls.\n\n"
          "**Die Zahl.** Es gibt eine harte Grenze, und sie folgt aus "
          "zwei Konstanten, die der Kurs schon hat. Aus der Hydrostatik "
          "(at-hydrostatik) und dem Gasgesetz folgt: Die Dichte nimmt "
          "mit der Höhe genau dann **zu**, wenn die Temperatur "
          "schneller fällt als\n\n"
          "$$\\left|\\frac{dT}{dz}\\right|_{autokonv} = \\frac{g}{R_L} = \\frac{9{,}81}{287} = 34{,}2\\ \\frac{\\mathrm{K}}{\\mathrm{km}}$$"
          "\n\n"
          "Das ist der **autokonvektive Gradient**: dreieinhalbmal der "
          "Trockenadiabate (th-adiabate), und oberhalb davon steht "
          "schwere Luft über leichter -- unhaltbar. Über heißem Asphalt "
          "misst man in den ersten Zentimetern 10 K je Meter, also "
          "10 000 K/km: **293-mal** der autokonvektive Wert. Eine "
          "Schicht in diesem Zustand hält keine Sekunde; sie flimmert, "
          "weil sie dauernd zusammenbricht.\n\n"
          "**Was man daraus schließt.** Flimmern und Spiegelung sind "
          "keine Kuriosität, sondern die Anzeige, dass die Konvektion "
          "läuft: Wer um 10 Uhr die Straße zittern sieht, weiß, dass "
          "die Thermik eingesetzt hat, bevor die erste Wolke am "
          "Kondensationsniveau steht (fe-hebung).",
          "**What is visible.** Over hot asphalt the background "
          "trembles, edges blur, and at the end of the road the sky is "
          "mirrored as a silver puddle. Over the stubble field a plume "
          "of dust stands and turns. Grass moves for a moment although "
          "the air is calm. Birds circle without a wingbeat and gain "
          "height doing it.\n\n"
          "**What it is.** All of it the same thing: the lowest layer "
          "of air is not merely unstable, it is unstable **far beyond** "
          "any adiabatic measure. In the first few millimetres above "
          "the ground there is no turbulence left, only conduction "
          "carries heat there, and air conducts miserably -- so an "
          "enormous gradient builds up. Every fluctuation of density is "
          "thereby a fluctuation of refractive index "
          "($n - 1 \\approx 2{.}9\\cdot 10^{-4}$ at standard pressure, proportional to "
          "density): hence the shimmer. Because the refractive index "
          "**increases upward**, grazing rays are bent away upward; a "
          "ray from the sky reaches the eye after being turned over the "
          "asphalt -- the puddle is the sky, not water. And the layer "
          "cannot be held: it breaks up into bubbles, and those are the "
          "first thermals of the day (th-stabilitaet). A dust devil is "
          "such a bubble with angular momentum.\n\n"
          "**The number.** There is a hard limit, and it follows from "
          "two constants the course already has. From hydrostatics "
          "(at-hydrostatik) and the gas law: density increases with "
          "height exactly when temperature falls faster than\n\n"
          "$$\\left|\\frac{dT}{dz}\\right|_{autoconv} = \\frac{g}{R_L} = \\frac{9{.}81}{287} = 34{.}2\\ \\frac{\\mathrm{K}}{\\mathrm{km}}$$"
          "\n\n"
          "That is the **autoconvective lapse rate**: three and a half "
          "times the dry adiabat (th-adiabate), and above it heavy air "
          "stands on light -- untenable. Over hot asphalt one measures "
          "10 K per metre in the first centimetres, i.e. 10 000 K/km: "
          "**293 times** the autoconvective value. A layer in that "
          "state does not last a second; it shimmers because it keeps "
          "collapsing.\n\n"
          "**What follows.** Shimmer and mirage are not a curiosity "
          "but an indicator that convection is running: whoever sees "
          "the road tremble at 10:00 knows the thermals have started, "
          "before the first cloud stands at the condensation level "
          "(fe-hebung)."),
        "skizze-stabilitaet", [
        zahl(t("Autokonvektiver Gradient g/R_L? (in K/km, eine "
               "Nachkommastelle)",
               "Autoconvective lapse rate g/R_L? (in K/km, one "
               "decimal)"),
             rund(AUTOKONVEKTIV, 1), t("K/km", "K/km"),
             t("`9,81 / 287,05 = 0,0342 K/m = 34,2 K/km`. Oberhalb "
               "dieses Gradienten nimmt die Dichte mit der Höhe zu -- "
               "ein Zustand, der sich nur in den untersten Zentimetern "
               "über heißem Boden halten lässt, und dort auch nur "
               "zitternd.",
               "`9.81 / 287.05 = 0.0342 K/m = 34.2 K/km`. Above this "
               "lapse rate density increases with height -- a state "
               "that can only exist in the lowest centimetres over hot "
               "ground, and even there only in a shimmer."),
             toleranz=0.03),
        zahl(t("Über heißem Asphalt werden 10 K je Meter gemessen. Wie "
               "viele autokonvektive Gradienten sind das?",
               "Over hot asphalt 10 K per metre is measured. How many "
               "autoconvective lapse rates is that?"),
             rund(ASPHALT_FAKTOR), t("", ""),
             t("`10 K/m = 10 000 K/km`, geteilt durch 34,2 K/km gibt "
               "293. Deshalb ist die Luft über dem Asphalt kein "
               "Gleichgewicht, sondern eine Kette platzender Blasen.",
               "`10 K/m = 10 000 K/km`, divided by 34.2 K/km gives "
               "293. That is why the air over asphalt is not an "
               "equilibrium but a chain of bursting bubbles."),
             toleranz=0.05),
        mc(t("Warum spiegelt sich der Himmel am Ende einer heißen "
             "Straße?",
             "Why is the sky mirrored at the end of a hot road?"),
           [t("Der Asphalt wird glänzend, wenn der Bitumen weich "
              "wird.", "The asphalt turns glossy when the bitumen "
              "softens."),
            t("In der heißen Schicht ist die Luft dünner, die Brechzahl "
              "also kleiner als oben; flach einfallende Strahlen werden "
              "nach oben weggekrümmt und erreichen das Auge aus der "
              "Richtung der Straße.",
              "In the hot layer the air is thinner, so the refractive "
              "index is smaller than above; grazing rays are bent away "
              "upward and reach the eye from the direction of the "
              "road."),
            t("Wasserdampf über dem Asphalt bildet eine spiegelnde "
              "Schicht.",
              "Water vapour above the asphalt forms a reflecting "
              "layer."),
            t("Der Horizont ist durch die Erdkrümmung gehoben.",
              "The horizon is lifted by the curvature of the "
              "Earth.")], 1,
           t("Es ist derselbe Mechanismus wie bei der Refraktion am "
             "Horizont, nur mit umgekehrtem Vorzeichen des Gradienten: "
             "Normalerweise nimmt die Dichte nach oben ab und krümmt "
             "Strahlen nach unten; im heißen Bodenfilm ist es "
             "umgekehrt.",
             "It is the same mechanism as refraction at the horizon, "
             "with the sign of the gradient reversed: normally density "
             "decreases upward and bends rays downward; in the hot "
             "surface film it is the other way round.")),
        ]),
    ])


# ===========================================================================
# 14  Selbst beobachten und messen
# ===========================================================================

E_GLAS = e_s(11.0)                              # hPa, Beschlag bei 11 °C
RH_GLAS = 100.0 * E_GLAS / e_s(22.0)            # %
R_GLAS = 0.622 * E_GLAS / (1000.0 - E_GLAS) * 1000.0   # g/kg
LCL_26_11 = 125.0 * (26.0 - 11.0)               # m
SCHATTEN_H40 = 1.8 * math.tan(math.radians(40.0))      # km bei 1,8 km Abstand
GAMMA_LUFT = 1.4                                # c_p/c_v der Luft
C_SCHALL = math.sqrt(GAMMA_LUFT * R_L * T_0)    # m/s bei 15 °C
SEK_JE_KM = 1000.0 / C_SCHALL                   # s
S_H60 = S_0 * math.sin(math.radians(60.0)) * 0.75      # W/m²
S_H19 = S_0 * math.sin(math.radians(18.8)) * 0.6       # W/m², Wien im Dezember
# Schallkrümmung: dc/dz = (c/2T)·dT/dz, Standardgradient 6,5 K/km
DC_DZ = C_SCHALL / (2 * T_0) * (-6.5e-3)        # 1/s
SCHALL_RADIUS = C_SCHALL / abs(DC_DZ)           # m
HOERWEITE_1KM = math.sqrt(2 * SCHALL_RADIUS * 1000.0)  # m
DRUCKFALL = 20.0 / 500000.0 * 12.0 * 3600.0     # hPa/h
METER_JE_HPA = 100.0 / (1.2 * G)                # m
TAU_ZELLE = 20000.0 / 12.0 / 60.0               # min

K_SELBSTMESSEN = kapitel(
    "selbstmessen", t("Selbst beobachten und messen",
                      "Observing and measuring for yourself"), 10,
    t("Der Kurs beginnt jedes Kapitel bei einer bekannten Gleichung und "
      "endet bei einer Beobachtung am Fenster. Dieses Kapitel ist "
      "dieser Satz: vier Messungen mit Glas, Stock, Stoppuhr und "
      "Barometer -- und am Schluss die Frage, warum das eigene Auge "
      "unter einer Stunde besser ist als jedes Modell.",
      "Every chapter of this course starts from an equation the reader "
      "knows and ends at an observation he can check from the window. "
      "This chapter is that sentence: four measurements with a glass, a "
      "stick, a stopwatch and a barometer -- and at the end the "
      "question why one's own eye beats any model below one hour."), [

    lektion("sb-taupunkt",
        t("Taupunkt mit einem Glas Wasser",
          "Dew point with a glass of water"),
        ["taupunktmessung", "feuchtemass"],
        t("**Der Versuch.** Ein dünnwandiges Glas, Wasser, ein paar "
          "Eiswürfel, ein Thermometer im Wasser, und rühren. Die "
          "Temperatur, bei der die Außenwand gerade **anläuft**, ist "
          "der Taupunkt der Luft im Zimmer. Sie ist überraschend scharf "
          "zu treffen: ein halbes Kelvin, wenn man langsam kühlt und in "
          "schrägem Licht gegen eine dunkle Fläche schaut.\n\n"
          "**Warum das der Taupunkt ist.** Die Wand nimmt die "
          "Temperatur des gerührten Wassers an; die Luft unmittelbar an "
          "der Wand wird auf diese Temperatur abgekühlt, bei "
          "unverändertem Dampfdruck. Sie kondensiert in dem Moment, in "
          "dem $e$ den Sättigungsdampfdruck dieser Temperatur erreicht -- "
          "und das ist die Definition des Taupunkts (fe-dampf). Drei "
          "Fehlerquellen muss man mitdenken: **ohne Rühren** ist die "
          "Wand unten kälter als das Thermometer oben anzeigt, und man "
          "misst zu warm; **dickwandiges Glas oder Keramik** hinkt der "
          "Wassertemperatur nach; und der **eigene Atem** hebt den "
          "Dampfdruck lokal um Millibar, also nicht über das Glas "
          "beugen.\n\n"
          "**Die Rechnung.** Aus $T$ und $T_d$ folgt alles. Beispiel: "
          "Zimmer 22 °C, erster Beschlag bei 11 °C. Magnus gibt "
          "$e = e_s(11\\,^\\circ\\mathrm{C}) = 13{,}1$ hPa und $e_s(22\\,^\\circ\\mathrm{C}) = 26{,}4$ hPa, also\n\n"
          "$$\\mathrm{RH} = \\frac{e}{e_s(T)} = \\frac{13{,}1}{26{,}4} = 50\\ \\%, \\qquad r = 0{,}622\\,\\frac{e}{p-e} = 8{,}3\\ \\frac{\\mathrm{g}}{\\mathrm{kg}}$$"
          "\n\n"
          "Acht Gramm Wasser in jedem Kilogramm Zimmerluft, bei einem "
          "Zimmer von 40 m³ also ein halbes Kilo. Und die Spreizung "
          "$T - T_d = 11$ K heißt nach fe-hebung: Stünde diese Luft "
          "draußen und würde gehoben, läge ihre Wolkenbasis bei "
          "1375 m.\n\n"
          "**Die Gegenprobe.** Dieselbe Messung an der Fensterscheibe "
          "sagt etwas anderes: Beschlägt sie innen, ist ihre Oberfläche "
          "kälter als 11 °C, und die Wand in der kalten Ecke daneben "
          "liegt kaum darüber. Schimmel wächst ab 80 % relativer Feuchte "
          "an der Wandoberfläche, und das ist bei $e = 13{,}1$ hPa schon bei "
          "einer Wandtemperatur von 14 °C erreicht -- nicht erst am "
          "Taupunkt. Lüften hilft im Winter immer, weil kalte Außenluft "
          "selbst bei 100 % Feuchte wenig Dampf mitbringt: bei −5 °C sind "
          "es 4,2 hPa gegen die 13,1 hPa im Zimmer.\n\n"
          "**Was man daraus schließt.** Der Taupunkt ist die eine "
          "Zahl, die man draußen nicht sieht und ohne die nichts geht: "
          "Er gibt die Wolkenbasis, die Frostgefahr der Nacht, die "
          "Nebelwahrscheinlichkeit und über $\\theta_e$ die Energie, die in "
          "einem Gewitter steckt. Ein Glas Wasser ersetzt das "
          "Psychrometer.",
          "**The experiment.** A thin-walled glass, water, a few ice "
          "cubes, a thermometer in the water, and stir. The temperature "
          "at which the outer wall just **mists over** is the dew point "
          "of the air in the room. It can be caught surprisingly "
          "sharply: half a kelvin, if one cools slowly and looks at a "
          "grazing angle against a dark background.\n\n"
          "**Why that is the dew point.** The wall takes on the "
          "temperature of the stirred water; the air right at the wall "
          "is cooled to that temperature at unchanged vapour pressure. "
          "It condenses the moment $e$ reaches the saturation vapour "
          "pressure of that temperature -- and that is the definition "
          "of the dew point (fe-dampf). Three sources of error have to "
          "be kept in mind: **without stirring** the wall is colder at "
          "the bottom than the thermometer reads at the top, and the "
          "measurement comes out too warm; **thick glass or ceramic** "
          "lags behind the water temperature; and **one's own breath** "
          "raises the local vapour pressure by millibars, so do not "
          "lean over the glass.\n\n"
          "**The calculation.** From $T$ and $T_d$ everything follows. "
          "Example: room at 22 °C, first misting at 11 °C. Magnus gives "
          "$e = e_s(11\\,^\\circ\\mathrm{C}) = 13{.}1$ hPa and $e_s(22\\,^\\circ\\mathrm{C}) = 26{.}4$ hPa, hence\n\n"
          "$$\\mathrm{RH} = \\frac{e}{e_s(T)} = \\frac{13{.}1}{26{.}4} = 50\\ \\%, \\qquad r = 0{.}622\\,\\frac{e}{p-e} = 8{.}3\\ \\frac{\\mathrm{g}}{\\mathrm{kg}}$$"
          "\n\n"
          "Eight grams of water in every kilogram of room air, so half "
          "a kilogram in a 40 m³ room. And the spread $T - T_d = 11$ K means, "
          "by fe-hebung: were this air outside and lifted, its cloud "
          "base would lie at 1375 m.\n\n"
          "**The counter-check.** The same measurement on a window "
          "pane says something else: if it mists over on the inside, its "
          "surface is colder than 11 °C, and the wall in the cold corner "
          "beside it is barely warmer. Mould grows from 80 % relative "
          "humidity at the wall surface upward, and at $e = 13{.}1$ hPa that "
          "is reached at a wall temperature of 14 °C already -- not only "
          "at the dew point. Airing always helps in winter, because cold "
          "outside air brings little vapour even at 100 % humidity: at "
          "−5 °C it is 4.2 hPa against the 13.1 hPa indoors.\n\n"
          "**What follows.** The dew point is the one number one "
          "cannot see outdoors and without which nothing works: it "
          "gives the cloud base, the night's frost risk, the "
          "likelihood of fog, and through $\\theta_e$ the energy stored in a "
          "thunderstorm. A glass of water replaces the "
          "psychrometer."),
        "skizze-dampfdruck", [
        zahl(t("Zimmer 22 °C, erster Beschlag bei 11 °C. Relative "
               "Feuchte? (in %)",
               "Room at 22 °C, first misting at 11 °C. Relative "
               "humidity? (in %)"),
             rund(RH_GLAS), t("%", "%"),
             t("`e = e_s(11) = 13,1 hPa`, `e_s(22) = 26,4 hPa`, "
               "`RH = 13,1/26,4 = 50 %`. Die Faustregel '7 % je "
               "Kelvin' gibt bei 11 K Spreizung ebenfalls etwa die "
               "Hälfte.",
               "`e = e_s(11) = 13.1 hPa`, `e_s(22) = 26.4 hPa`, "
               "`RH = 13.1/26.4 = 50 %`. The rule of thumb '7 % per "
               "kelvin' also gives about one half for an 11 K "
               "spread."),
             toleranz=0.03),
        zahl(t("Und das Mischungsverhältnis bei p = 1000 hPa? (in "
               "g/kg, eine Nachkommastelle)",
               "And the mixing ratio at p = 1000 hPa? (in g/kg, one "
               "decimal)"),
             rund(R_GLAS, 1), t("g/kg", "g/kg"),
             t("`r = 0,622 × 13,1 / (1000 − 13,1) = 8,26·10⁻³` oder "
               "8,3 g/kg. Diese Zahl bleibt beim Heben und Senken "
               "erhalten, die relative Feuchte nicht -- deshalb "
               "rechnet der Meteorologe mit r.",
               "`r = 0.622 × 13.1 / (1000 − 13.1) = 8.26·10⁻³` or "
               "8.3 g/kg. This number is conserved on lifting and "
               "sinking, relative humidity is not -- which is why the "
               "meteorologist works with r."),
             toleranz=0.03),
        mc(t("Warum muss man das Eiswasser rühren?",
             "Why must the iced water be stirred?"),
           [t("Damit das Eis schneller schmilzt.",
              "So that the ice melts faster."),
            t("Damit die Luft am Glas nicht gesättigt bleibt.",
              "So that the air at the glass does not stay saturated."),
            t("Ungerührt schichtet sich das Wasser: unten kalt, oben "
              "wärmer. Die Wand läuft dann unten an, während das "
              "Thermometer oben eine zu hohe Temperatur zeigt -- der "
              "gemessene Taupunkt wäre zu hoch.",
              "Unstirred, the water stratifies: cold at the bottom, "
              "warmer at the top. The wall then mists over at the "
              "bottom while the thermometer at the top reads too high "
              "-- the measured dew point would come out too high."),
            t("Damit sich die Eiswürfel nicht an die Wand legen.",
              "So that the ice cubes do not rest against the "
              "wall.")], 2,
           t("Der Versuch misst eine **Wandtemperatur** und nennt sie "
             "Wassertemperatur. Jede Abweichung zwischen beiden geht "
             "voll in den Fehler, und 1 K Fehler im Taupunkt sind "
             "nach fe-hebung schon 125 m Wolkenbasis.",
             "The experiment measures a **wall temperature** and calls "
             "it the water temperature. Any difference between the two "
             "goes straight into the error, and 1 K of error in the dew "
             "point is already 125 m of cloud base by fe-hebung.")),
        ]),

    lektion("sb-wolkenbasis",
        t("Die Wolkenbasis vom Boden aus",
          "Cloud base from the ground"),
        ["wolkenbasis", "fehlerrechnung"],
        t("**Drei Wege.** Erstens die **125-m-Regel**: Thermometer und "
          "Taupunkt, Differenz mal 125 m je Kelvin (fe-hebung). Bei "
          "26 °C und einem Taupunkt von 11 °C sind das "
          "$15 \\times 125 = 1875$ m über Grund. Zweitens der **Vergleich**: "
          "Ein Berg, ein Sendeturm, ein Hochhaus bekannter Höhe, in das "
          "die Wolke hineinreicht oder das sie freilässt, gibt eine "
          "Schranke, die nicht zu schlagen ist. Drittens der "
          "**Schattenwurf**: Sieht man eine Wolke und ihren Schatten "
          "auf dem Boden, ist bei der Sonnenhöhe $h$ und dem waagrechten "
          "Abstand $s$ zwischen Wolke und Schatten\n\n"
          "$$z = s\\,\\tan h$$"
          "\n\n"
          "Bei $s = 1{,}8$ km und $h = 40^\\circ$ also 1,51 km -- in "
          "hügeligem Gelände von einem Aussichtspunkt gut zu "
          "schätzen.\n\n"
          "**Was die Regel wirklich kann.** Die 125 m je Kelvin sind "
          "kein Messwert, sondern das Ergebnis einer Division: Die "
          "Trockenadiabate fällt mit 9,8 K/km, der Taupunkt mit "
          "1,7 K/km, die Spreizung schließt sich also mit 8,1 K/km, und "
          "$1/8{,}1$ K/km sind 123 m/K. Daraus folgt gleich die "
          "Fehlerrechnung: **1 K Unsicherheit im Taupunkt sind 125 m "
          "Unsicherheit in der Basis.** Ein Taupunkt auf 0,5 K ist "
          "schon gut gemessen, also taugt die Regel für \"1900 m\" und "
          "nicht für \"1875 m\". Und sie gilt nur für Cumulus aus der "
          "durchmischten Schicht: Deren Basis **ist** das "
          "Kondensationsniveau der Bodenluft. Für Stratus, Hochnebel "
          "oder eine aufgeglittene Warmfrontwolke gilt sie nicht, denn "
          "deren Basis liegt dort, wo eine Inversion oder die "
          "Gleitfläche sitzt, und nicht dort, wo die Bodenluft "
          "gesättigt wäre.\n\n"
          "**Der Tagesgang.** Die Basis steigt im Laufe des "
          "Nachmittags, und zwar nicht, weil es wärmer wird, sondern "
          "weil die wachsende Grenzschicht trockene Luft von oben "
          "einmischt: Der Taupunkt am Boden **fällt** um 2 bis 4 K "
          "zwischen 10 und 16 Uhr, und die Spreizung öffnet sich von "
          "beiden Seiten. Wer morgens 1200 m rechnet, hat am Abend "
          "1800 m.\n\n"
          "**Was man daraus schließt.** Drei Wege, drei "
          "Fehlerquellen, eine Kontrolle: Stimmen Regel und "
          "Schattenwurf auf 20 % überein, ist die Luft durchmischt und "
          "die Wolke eine Cumulus-Wolke. Weichen sie stark ab, ist es "
          "keine, und das ist die interessantere Auskunft.",
          "**Three ways.** First the **125 m rule**: thermometer and "
          "dew point, difference times 125 m per kelvin (fe-hebung). At "
          "26 °C with a dew point of 11 °C that is "
          "$15 \\times 125 = 1875$ m above ground. Second, **comparison**: a "
          "mountain, a mast, a tower of known height that the cloud "
          "reaches into or leaves clear gives a bound that cannot be "
          "beaten. Third, the **shadow**: if one can see a cloud and "
          "its shadow on the ground, then with the solar elevation $h$ and "
          "the horizontal distance $s$ between cloud and shadow\n\n"
          "$$z = s\\,\\tan h$$"
          "\n\n"
          "So for $s = 1{.}8$ km and $h = 40^\\circ$, 1.51 km -- in hilly "
          "country this is easy to estimate from a viewpoint.\n\n"
          "**What the rule can really do.** The 125 m per kelvin are "
          "not a measurement but the result of a division: the dry "
          "adiabat falls at 9.8 K/km, the dew point at 1.7 K/km, so the "
          "spread closes at 8.1 K/km, and $1/8{.}1$ K/km is 123 m/K. The "
          "error budget follows at once: **1 K of uncertainty in the "
          "dew point is 125 m of uncertainty in the base.** A dew point "
          "measured to 0.5 K is already good, so the rule is good for "
          "\"1900 m\" and not for \"1875 m\". And it holds only for "
          "cumulus out of the mixed layer: their base **is** the "
          "condensation level of the surface air. For stratus, high fog "
          "or a warm-front cloud that has glided up it does not hold, "
          "because their base sits where an inversion or the gliding "
          "surface sits, and not where the surface air would be "
          "saturated.\n\n"
          "**The daily course.** The base rises through the afternoon, "
          "and not because it gets warmer but because the growing "
          "boundary layer mixes dry air down from above: the surface "
          "dew point **falls** by 2 to 4 K between 10:00 and 16:00, and "
          "the spread opens from both sides. Whoever computes 1200 m in "
          "the morning has 1800 m by evening.\n\n"
          "**What follows.** Three ways, three sources of error, one "
          "check: if the rule and the shadow agree to within 20 %, the "
          "air is mixed and the cloud is a cumulus. If they differ "
          "strongly, it is not -- and that is the more interesting "
          "piece of information."),
        "skizze-hebung", [
        zahl(t("26 °C, Taupunkt 11 °C. Wolkenbasis nach der "
               "125-m-Regel? (in m)",
               "26 °C, dew point 11 °C. Cloud base by the 125 m rule? "
               "(in m)"),
             rund(LCL_26_11), t("m", "m"),
             t("`(26 − 11) × 125 = 1875 m` über Grund. Bei 1 K "
               "Unsicherheit im Taupunkt ist das 1875 ± 125 m, also "
               "sinnvoll gerundet 1900 m.",
               "`(26 − 11) × 125 = 1875 m` above ground. With 1 K of "
               "uncertainty in the dew point that is 1875 ± 125 m, so "
               "sensibly rounded 1900 m."),
             toleranz=0.03),
        zahl(t("Eine Wolke und ihr Schatten liegen 1,8 km auseinander, "
               "die Sonne steht 40° hoch. Basishöhe? (in km, zwei "
               "Nachkommastellen)",
               "A cloud and its shadow lie 1.8 km apart, the sun "
               "stands 40° high. Base height? (in km, two decimals)"),
             rund(SCHATTEN_H40, 2), t("km", "km"),
             t("`z = s·tan h = 1,8 km × tan 40° = 1,8 × 0,839 = "
               "1,51 km`. Der Fehler steckt im Abstand, nicht im "
               "Winkel: 20 % Fehler in s sind 20 % in z.",
               "`z = s·tan h = 1.8 km × tan 40° = 1.8 × 0.839 = "
               "1.51 km`. The error is in the distance, not in the "
               "angle: 20 % error in s is 20 % in z."),
             toleranz=0.03),
        mc(t("Warum gibt die 125-m-Regel bei einer Stratusdecke den "
             "falschen Wert?",
             "Why does the 125 m rule give the wrong answer for a "
             "stratus deck?"),
           [t("Weil Stratus aus Eis besteht.",
              "Because stratus consists of ice."),
            t("Weil die Regel nur im Sommer gilt.",
              "Because the rule holds only in summer."),
            t("Weil Stratus zu tief liegt für eine Rechnung.",
              "Because stratus is too low to calculate."),
            t("Weil ihre Basis nicht das Kondensationsniveau der "
              "Bodenluft ist: Stratus entsteht durch Hebung oder "
              "Abkühlung einer ganzen Schicht und hängt an einer "
              "Inversion, nicht an der Luft unten am Thermometer.",
              "Because its base is not the condensation level of the "
              "surface air: stratus forms by lifting or cooling of a "
              "whole layer and hangs on an inversion, not on the air "
              "down at the thermometer.")], 3,
           t("Die Regel setzt voraus, dass das Paket an der "
             "Wolkenbasis vom Boden gekommen ist und seinen "
             "Dampfgehalt mitgebracht hat. Das gilt für Cumulus in "
             "einer durchmischten Schicht, sonst nicht -- deshalb "
             "rechnen Segelflieger damit und Flugwetterwarten nicht.",
             "The rule assumes that the parcel at cloud base came from "
             "the ground and brought its vapour with it. That holds for "
             "cumulus in a mixed layer and otherwise not -- which is "
             "why glider pilots use it and aviation forecasters do "
             "not.")),
        ]),

    lektion("sb-stock",
        t("Stock und Stoppuhr: Sonnenhöhe und Gewitterentfernung",
          "Stick and stopwatch: solar elevation and storm distance"),
        ["sonnenhoehe", "schallgeschwindigkeit", "donner"],
        t("**Der Stock.** Ein Stock senkrecht in den Boden, die Länge "
          "$L$, der Schatten $S$, und $\\tan h = L/S$. Ein Stock von 1,20 m "
          "mit 1,00 m Schatten gibt $h = 50^\\circ$. Damit drei Dinge: die "
          "Sonnenhöhe, aus dem kürzesten Schatten des Tages die "
          "Mittagshöhe und daraus mit der Deklination die eigene Breite "
          "($\\varphi = 90^\\circ - h_{mittag} + \\delta$), und aus der Höhe die "
          "Einstrahlung (st-bilanz):\n\n"
          "$$S = S_0\\,\\sin h\\cdot \\tau$$"
          "\n\n"
          "Bei $h = 60^\\circ$ und einer Transmission von 0,75 sind das "
          "884 W/m². Am 21. Dezember steht die Sonne in Wien nur 18,8° "
          "hoch, und der längere Weg durch die Atmosphäre drückt die "
          "Transmission auf 0,6: 263 W/m². **Faktor 3,4** -- und das "
          "ist der Winter, nicht die Entfernung zur Sonne. Dass das "
          "Temperaturmaximum nicht zur Mittagsstunde kommt, sondern "
          "gegen 15 Uhr, steht in st-tagesgang: Es entscheidet die "
          "Bilanz, nicht die Einstrahlung.\n\n"
          "**Die Stoppuhr.** Blitz sehen, zählen, Donner hören, durch "
          "drei teilen -- die Entfernung in Kilometern. Genauer: Die "
          "Schallgeschwindigkeit in einem Gas ist "
          "$c = \\sqrt{\\gamma R_L T}$ (adiabatische Kompression, "
          "$\\gamma = c_p/c_v = 1{,}4$), bei 15 °C also 340 m/s und damit **2,94 "
          "Sekunden je Kilometer**. Die drei Sekunden sind genau genug, "
          "und zwei Messungen im Abstand von zehn Minuten geben die "
          "Verlagerungsgeschwindigkeit der Zelle.\n\n"
          "**Zwei Beobachtungen, die mehr sagen als die Faustregel.** "
          "Erstens **rollt** der Donner, weil der Blitzkanal Kilometer "
          "lang ist: Der Schall vom nächsten Punkt kommt zuerst, der "
          "vom fernsten Ende Sekunden später, und dazwischen liegt das "
          "Grollen. Ein kurzer, harter Knall heißt: der Kanal steht "
          "quer und nah. Zweitens hört man über etwa 25 km hinaus "
          "**nichts mehr**, und das ist keine Dämpfung, sondern "
          "Geometrie: Weil $c \\propto \\sqrt{T}$ und die Temperatur nach oben "
          "abnimmt, ist $dc/dz = (c/2T)\\,dT/dz = -3{,}8\\cdot 10^{-3}$ /s, und ein "
          "Schallstrahl krümmt sich mit dem Radius $R = c/|dc/dz| = 89$ km "
          "**nach oben**. Von einer Quelle in der Höhe $H$ erreicht der "
          "Strahl den Boden nur innerhalb von $\\sqrt{2RH}$: 13 km für den "
          "untersten Kilometer des Kanals, 30 km für sein oberes Ende "
          "in 5 km. Dahinter liegt eine **Schattenzone**. Deshalb sieht "
          "man ferne Gewitter wetterleuchten, ohne etwas zu hören.\n\n"
          "**Was man daraus schließt.** Stock und Stoppuhr geben zwei "
          "Zahlen, die in keiner Meldung stehen: wie viel Energie "
          "gerade auf den Quadratmeter fällt, und wie weit die Zelle "
          "weg ist, die man am Horizont sieht.",
          "**The stick.** A stick upright in the ground, its length $L$, "
          "its shadow $S$, and $\\tan h = L/S$. A stick of 1.20 m with a "
          "1.00 m shadow gives $h = 50^\\circ$. That yields three things: the "
          "solar elevation; from the shortest shadow of the day the "
          "noon elevation and from it, with the declination, one's own "
          "latitude ($\\varphi = 90^\\circ - h_{noon} + \\delta$); and from the "
          "elevation the insolation (st-bilanz):\n\n"
          "$$S = S_0\\,\\sin h\\cdot \\tau$$"
          "\n\n"
          "At $h = 60^\\circ$ and a transmission of 0.75 that is 884 W/m². On "
          "21 December the sun in Vienna stands only 18.8° high, and the "
          "longer path through the atmosphere pushes the transmission "
          "down to 0.6: 263 W/m². **A factor of 3.4** -- and that is "
          "winter, not the distance to the sun. Why the temperature "
          "maximum comes not at noon but around 15:00 stands in "
          "st-tagesgang: the budget decides, not the insolation.\n\n"
          "**The stopwatch.** See the flash, count, hear the thunder, "
          "divide by three -- the distance in kilometres. More "
          "precisely: the speed of sound in a gas is "
          "$c = \\sqrt{\\gamma R_L T}$ (adiabatic compression, "
          "$\\gamma = c_p/c_v = 1{.}4$), hence 340 m/s at 15 °C and therefore "
          "**2.94 seconds per kilometre**. Three seconds is accurate "
          "enough, and two measurements ten minutes apart give the "
          "speed at which the cell is travelling.\n\n"
          "**Two observations that say more than the rule of thumb.** "
          "First, thunder **rolls** because the lightning channel is "
          "kilometres long: sound from the nearest point arrives first, "
          "from the far end seconds later, and the rumble lies in "
          "between. A short hard crack means the channel stands across "
          "and close. Second, beyond about 25 km **nothing is heard at "
          "all**, and that is not absorption but geometry: because "
          "$c \\propto \\sqrt{T}$ and temperature decreases upward, "
          "$dc/dz = (c/2T)\\,dT/dz = -3{.}8\\cdot 10^{-3}$ /s, and a sound ray curves "
          "**upward** with radius $R = c/|dc/dz| = 89$ km. From a source at "
          "height $H$ the ray reaches the ground only within $\\sqrt{2RH}$: "
          "13 km for the lowest kilometre of the channel, 30 km for its "
          "upper end at 5 km. Beyond that lies a **shadow zone**. That "
          "is why distant storms can be seen flashing without a "
          "sound.\n\n"
          "**What follows.** Stick and stopwatch give two numbers that "
          "appear in no forecast: how much energy is falling on the "
          "square metre right now, and how far away the cell is that "
          "one can see on the horizon."),
        "selbstmessen-stock", [
        zahl(t("Schallgeschwindigkeit bei 15 °C aus c = √(γ·R_L·T), "
               "γ = 1,4? (in m/s)",
               "Speed of sound at 15 °C from c = √(γ·R_L·T), γ = 1.4? "
               "(in m/s)"),
             rund(C_SCHALL), t("m/s", "m/s"),
             t("`√(1,4 × 287 × 288) = √115 800 = 340 m/s`, also 2,94 s "
               "je Kilometer. In kalter Luft (−15 °C) sind es 325 m/s "
               "-- die Faustregel irrt um 5 %.",
               "`√(1.4 × 287 × 288) = √115 800 = 340 m/s`, hence 2.94 s "
               "per kilometre. In cold air (−15 °C) it is 325 m/s -- "
               "the rule of thumb is 5 % off."),
             toleranz=0.03),
        zahl(t("Sonne 60° hoch, Transmission 0,75. Einstrahlung auf "
               "eine waagrechte Fläche? (in W/m²)",
               "Sun 60° high, transmission 0.75. Irradiance on a "
               "horizontal surface? (in W/m²)"),
             rund(S_H60), t("W/m²", "W/m²"),
             t("`1361 × sin 60° × 0,75 = 1361 × 0,866 × 0,75 = "
               "884 W/m²`. Im Dezember in Wien (18,8°, τ = 0,6) sind es "
               "263 W/m², ein Drittel.",
               "`1361 × sin 60° × 0.75 = 1361 × 0.866 × 0.75 = "
               "884 W/m²`. In Vienna in December (18.8°, τ = 0.6) it is "
               "263 W/m², one third."),
             toleranz=0.03),
        mc(t("Man sieht ein Gewitter am Horizont blitzen, hört aber "
             "nichts. Was ist der Grund?",
             "A storm can be seen flashing on the horizon but nothing "
             "is heard. Why?"),
           [t("Weil die Temperatur nach oben abnimmt, krümmen sich die "
              "Schallstrahlen nach oben (R ≈ 89 km); über etwa 25 km "
              "hinaus liegt der Boden in der Schattenzone.",
              "Because temperature decreases upward the sound rays "
              "curve upward (R ≈ 89 km); beyond about 25 km the ground "
              "lies in the shadow zone."),
            t("Der Schall wird in der Luft vollständig absorbiert.",
              "The sound is completely absorbed in the air."),
            t("Ferne Blitze sind zu schwach für Donner.",
              "Distant flashes are too weak to produce thunder."),
            t("Der Wind weht aus der falschen Richtung.",
              "The wind is blowing from the wrong direction.")], 0,
           t("Dieselbe Strahlenkrümmung wie bei der Luftspiegelung "
             "(bo-flimmern), nur für Schall und mit umgekehrtem "
             "Vorzeichen: Nach unten nimmt c zu, also werden die "
             "Strahlen nach oben weggebogen. Bei einer Bodeninversion "
             "ist es umgekehrt, und dann hört man den Donner "
             "ungewöhnlich weit.",
             "The same ray bending as in a mirage (bo-flimmern), for "
             "sound and with the opposite sign: c increases downward, "
             "so the rays are bent away upward. In a surface inversion "
             "it is the other way round, and then thunder carries "
             "unusually far.")),
        ]),

    lektion("sb-druck",
        t("Das Barometer als Messgerät für die Verlagerung",
          "The barometer as a gauge of movement"),
        ["drucktendenz", "vorhersagbarkeit"],
        t("**Was man messen kann.** Jedes Telefon hat ein Barometer mit "
          "0,1 hPa Auflösung. Es zeigt nicht das Wetter an, sondern "
          "**die Änderung**: Fällt der Druck in einer Stunde um mehr "
          "als 1 hPa, zieht ein Tief oder eine Front heran; steigt er "
          "nach dem Durchgang ebenso schnell, folgt Kaltluft mit "
          "Schauern. Eine Bedingung muss man ernst nehmen: Ein Stock"
          "werk höher sind es 0,35 hPa weniger -- mehr als das Signal. "
          "Wer die Tendenz messen will, muss das Gerät liegen lassen, "
          "wo es liegt.\n\n"
          "**Was dahintersteckt.** Ein Druckfeld, das sich mit der "
          "Geschwindigkeit $c$ verlagert, ohne sich zu ändern, gibt am "
          "festen Ort\n\n"
          "$$\\frac{\\partial p}{\\partial t} = -c\\,\\frac{\\partial p}{\\partial x}$$"
          "\n\n"
          "Die Drucktendenz ist also kein eigenes Phänomen, sondern das "
          "Verlagern eines Musters, und sie misst ein Produkt aus "
          "Gradient und Zuggeschwindigkeit. Mit einem Wert von der "
          "Karte: 20 hPa über 500 km, Verlagerung 12 m/s, gibt "
          "$4\\cdot 10^{-5}\\,\\mathrm{hPa/m} \\cdot 12\\,\\mathrm{m/s} = 1{,}7$ hPa/h. Genau das "
          "zeigt das Barometer vor einer Kaltfront. Umgekehrt: Wer den "
          "Gradienten aus der Karte kennt und die Tendenz selbst misst, "
          "hat die Zuggeschwindigkeit -- und damit die Ankunftszeit.\n\n"
          "**Die Höhenfalle, gerechnet.** Hydrostatik "
          "(at-hydrostatik): $dp/dz = -\\rho g$, mit $\\rho = 1{,}2$ kg/m³ sind "
          "das 11,8 Pa je Meter, also **1 hPa je 8,5 m**. Drei Stufen "
          "einer Treppe sind eine Zehntel-Hektopascal, die ganze "
          "Tendenz einer Stunde sind 14 m Höhenunterschied. Deshalb "
          "melden Stationen ihren Druck immer auf Meereshöhe "
          "zurückgerechnet, und deshalb ist die Tendenz eines "
          "wandernden Telefons wertlos.\n\n"
          "**Und zuletzt: wie weit trägt das eigene Auge?** Ein "
          "Wettersystem bleibt ungefähr so lange erkennbar, wie es "
          "braucht, um sich selbst zu durchqueren, $\\tau \\approx L/U$. Eine "
          "Schauerzelle von 20 km bei 12 m/s: 28 Minuten. Ein Tief von "
          "2000 km bei 15 m/s: 37 Stunden. Darum gewinnt der Beobachter "
          "unter einer Stunde -- er kennt den Anfangszustand seines "
          "20-km-Systems genauer als jedes Modell, das es nicht einmal "
          "auflöst -- und verliert über sechs Stunden, wo nur noch die "
          "große Skala zählt, die er nicht sehen kann. Die kleinen "
          "Skalen verlieren ihre Vorhersagbarkeit zuerst (vo-chaos): "
          "**Das Auge und das Modell scheitern aus entgegengesetzten "
          "Gründen**, und deshalb braucht man beide.",
          "**What one can measure.** Every phone has a barometer with "
          "0.1 hPa resolution. It does not show the weather but **the "
          "change**: if the pressure falls by more than 1 hPa in an "
          "hour, a low or a front is approaching; if it rises just as "
          "fast after the passage, cold air with showers follows. One "
          "condition has to be taken seriously: one floor higher up the "
          "reading is 0.35 hPa lower -- more than the signal. Whoever "
          "wants to measure the tendency must leave the instrument "
          "where it lies.\n\n"
          "**What lies behind it.** A pressure field that travels at "
          "speed $c$ without changing gives, at a fixed place,\n\n"
          "$$\\frac{\\partial p}{\\partial t} = -c\\,\\frac{\\partial p}{\\partial x}$$"
          "\n\n"
          "The pressure tendency is thus not a phenomenon of its own "
          "but the translation of a pattern, and it measures a product "
          "of gradient and travel speed. With a value off the chart: "
          "20 hPa over 500 km, travelling at 12 m/s, gives "
          "$4\\cdot 10^{-5}\\,\\mathrm{hPa/m} \\cdot 12\\,\\mathrm{m/s} = 1{.}7$ hPa/h. That is "
          "exactly what the barometer shows ahead of a cold front. "
          "Conversely: whoever knows the gradient from the chart and "
          "measures the tendency himself has the travel speed -- and "
          "with it the time of arrival.\n\n"
          "**The height trap, worked out.** Hydrostatics "
          "(at-hydrostatik): $dp/dz = -\\rho g$, with $\\rho = 1{.}2$ kg/m³ that is "
          "11.8 Pa per metre, hence **1 hPa per 8.5 m**. Three steps of "
          "a staircase are a tenth of a hectopascal, a whole hour's "
          "tendency is 14 m of height. That is why stations always "
          "report their pressure reduced to sea level, and why the "
          "tendency measured by a travelling phone is worthless.\n\n"
          "**And finally: how far does one's own eye carry?** A weather "
          "system stays recognisable roughly as long as it takes to "
          "cross itself, $\\tau \\approx L/U$. A shower cell of 20 km at 12 m/s: "
          "28 minutes. A depression of 2000 km at 15 m/s: 37 hours. "
          "That is why the observer wins below one hour -- he knows the "
          "initial state of his 20 km system better than any model that "
          "does not even resolve it -- and loses beyond six hours, "
          "where only the large scale counts, which he cannot see. "
          "Small scales lose their predictability first (vo-chaos): "
          "**the eye and the model fail for opposite reasons**, and "
          "that is why one needs both."),
        "skizze-zyklone", [
        zahl(t("20 hPa über 500 km, das Muster zieht mit 12 m/s. "
               "Drucktendenz am festen Ort? (in hPa/h, zwei "
               "Nachkommastellen)",
               "20 hPa over 500 km, the pattern travelling at 12 m/s. "
               "Pressure tendency at a fixed place? (in hPa/h, two "
               "decimals)"),
             rund(DRUCKFALL, 2), t("hPa/h", "hPa/h"),
             t("`∂p/∂t = −c·∂p/∂x = 12 m/s × 20 hPa / 500 000 m = "
               "4,8·10⁻⁴ hPa/s = 1,73 hPa/h`. Ein typischer Wert vor "
               "einer Kaltfront; 3 hPa/h heißt Sturm.",
               "`∂p/∂t = −c·∂p/∂x = 12 m/s × 20 hPa / 500 000 m = "
               "4.8·10⁻⁴ hPa/s = 1.73 hPa/h`. A typical value ahead of "
               "a cold front; 3 hPa/h means a gale."),
             toleranz=0.03),
        zahl(t("Wie viel Höhenunterschied entspricht 1 hPa in "
               "Bodennähe (ρ = 1,2 kg/m³)? (in m, eine "
               "Nachkommastelle)",
               "How much height difference corresponds to 1 hPa near "
               "the ground (ρ = 1.2 kg/m³)? (in m, one decimal)"),
             rund(METER_JE_HPA, 1), t("m", "m"),
             t("`dz = dp/(ρg) = 100 Pa / (1,2 × 9,81) = 8,5 m`. "
               "Deshalb ist ein Stockwerk 0,35 hPa und eine Messreihe "
               "aus der Hand unbrauchbar.",
               "`dz = dp/(ρg) = 100 Pa / (1.2 × 9.81) = 8.5 m`. That "
               "is why one storey is 0.35 hPa and a hand-held series of "
               "readings is useless."),
             toleranz=0.03),
        mc(t("Das Barometer zu Hause fällt zwei Stunden lang um "
             "2 hPa/h. Was ist die beste Deutung?",
             "The barometer at home falls by 2 hPa/h for two hours. "
             "What is the best interpretation?"),
           [t("Es wird wärmer, warme Luft ist leichter.",
              "It is getting warmer, and warm air is lighter."),
            t("Ein kräftiger Druckgradient zieht über den Ort: Aus "
              "∂p/∂t = −c·∂p/∂x folgt bei 4 hPa je 100 km eine "
              "Verlagerung um 14 m/s -- Front und starker Wind binnen "
              "Stunden.",
              "A strong pressure gradient is passing over the place: "
              "from ∂p/∂t = −c·∂p/∂x, a gradient of 4 hPa per 100 km "
              "implies a travel speed of 14 m/s -- a front and strong "
              "wind within hours."),
            t("Das Gerät ist defekt, 2 hPa/h gibt es nicht.",
              "The instrument is broken, 2 hPa/h does not occur."),
            t("Es wird regnen, aber windstill bleiben.",
              "It will rain but stay calm.")], 1,
           t("Die Tendenz ist ein Produkt: Gradient mal "
             "Zuggeschwindigkeit. Beides zusammen heißt Wind, denn der "
             "Gradient **ist** der Wind (dy-geostrophisch). Deshalb ist "
             "ein schnell fallendes Barometer eine Windwarnung und "
             "nicht nur eine Regenwarnung.",
             "The tendency is a product: gradient times travel speed. "
             "Both together mean wind, because the gradient **is** the "
             "wind (dy-geostrophisch). That is why a rapidly falling "
             "barometer is a wind warning and not merely a rain "
             "warning.")),
        ]),
    ])


# ===========================================================================
# Zusammenstellung
# ===========================================================================

# ===========================================================================
# Wolken lesen (phänomenologisch, hinter der Dynamik)
# ===========================================================================

# Oberkanten in 1800 m, Basis (LCL) in 1200 m, Boden 26 °C: trocken bis zur
# Basis, feucht darüber. Die Pakettemperatur an der Oberkante ist die
# Umgebungstemperatur der Inversionsunterkante.
WL_T_OBERKANTE = 26.0 - GAMMA_D * 1.2 - 6.0 * 0.6             # °C
# Auslösetemperatur: Deckel in 1500 m mit 14 °C, trockenadiabatisch herunter.
WL_T_DECKEL = 14.0
WL_Z_DECKEL = 1.5                                              # km
WL_T_TRIGGER = WL_T_DECKEL + GAMMA_D * WL_Z_DECKEL             # °C
# Zelle 25 km entfernt, Verlagerung mit dem 700-hPa-Wind.
WL_ZUG = 15.0                                                  # m/s
WL_ANKUNFT = 25000.0 / WL_ZUG / 60.0                           # min
# Lebensdauer: Wolkendicke durch Aufwind.
WL_ZEITSKALA = 3000.0 / 3.0 / 60.0                             # min
# Kippen eines Turms: tan α = ΔU/w, Versatz der Spitze = ΔU·z/(2w).
WL_W_TURM = 8.0                                                # m/s
WL_DU_TURM = 16.0                                              # m/s über 4 km
WL_KIPPWINKEL = math.degrees(math.atan(WL_DU_TURM / WL_W_TURM))  # Grad
WL_VERSATZ = WL_DU_TURM * 4000.0 / (2 * WL_W_TURM)             # m
# Wellenwolken: λ = 2πU/N (th-stabilitaet) zurückgerechnet auf dθ/dz.
WL_LAMBDA = 8600.0                                             # m
WL_U_WELLE = 15.0                                              # m/s
WL_N_WELLE = 2 * math.pi * WL_U_WELLE / WL_LAMBDA              # 1/s
WL_DTHETA_DZ = WL_N_WELLE ** 2 * 290.0 / G * 1000.0            # K/km
# Kelvin-Helmholtz: Ri < 1/4 verlangt du/dz > 2N.
WL_SCHERUNG_MIN = 2 * 0.011 * 1000.0                           # m/s je km

K_WOLKENLESEN = kapitel(
    "wolkenlesen", t("Wolken lesen: Form, Uhr und Sonde",
                     "Reading clouds: form, clock and probe"), 6,
    t("Eine Wolke ist ein Messgerät, das die Atmosphäre selbst aufgestellt "
      "hat. Ihre Form verrät das Vorzeichen von dθ/dz, ihr Kippen die "
      "Scherung, der Abstand ihrer Ballen die Brunt-Väisälä-Frequenz, und "
      "die Uhrzeit, zu der sie entsteht, die Höhe des Deckels. Dieses "
      "Kapitel liest zurück: vom Hinsehen zu den Gleichungen der Kapitel "
      "2 bis 6.",
      "A cloud is an instrument the atmosphere has put up by itself. Its "
      "shape gives away the sign of dθ/dz, its tilt the shear, the "
      "spacing of its rolls the Brunt–Väisälä frequency, and the hour at "
      "which it appears the height of the lid. This chapter reads "
      "backwards: from looking at the sky to the equations of chapters 2 "
      "to 6."), [

    lektion("wb-schichtung",
        t("Wolken als Zeugen der Schichtung",
          "Clouds as witnesses to the stratification"),
        ["wolkenform", "schichtung-lesen", "absinkinversion"],
        t("Ein Blick nach oben ist eine Messung. Nicht von Temperatur oder "
          "Druck -- die bleiben verborgen --, sondern von genau dem "
          "Vorzeichen, auf das Kapitel 2 hinauslief: dem von "
          "$d\\theta/dz$. Die Wolke zeigt es, weil sie aus Luft besteht, die "
          "gerade gehoben wurde, und weil die Art, wie sie dabei "
          "stehengeblieben ist, von der Schichtung bestimmt wird. Man "
          "lernt also keine Namen, sondern ein Vorzeichen abzulesen.\n\n"
          "**Blumenkohl mit harten Rändern.** Ein Rand ist scharf, wenn er "
          "aus Tröpfchen besteht, und ein Tröpfchen lebt nur Minuten, "
          "bevor es verdunstet oder vereist. Ein scharfer, nach außen "
          "drängender Rand ist deshalb **jung**: Hier steigt es schneller, "
          "als die Einmischung trockener Umgebungsluft die Wolke abbauen "
          "kann. Nach th-stabilitaet heißt das $N^2 < 0$ -- aber für das "
          "*gesättigte* Paket, also bedingte Labilität zwischen $\\Gamma_s$ und "
          "$\\Gamma_d$ (fe-emagram). Trockenlabil ist die freie Atmosphäre fast "
          "nie.\n\n"
          "**Oberkanten in einer Linie.** Das ist der schärfste Messwert "
          "am ganzen Himmel: Wenn ein Feld von Cumuli oben wie mit dem "
          "Lineal abgeschnitten ist, liegt dort die Unterkante einer "
          "**Inversion** -- der Deckel, an dem $d\\theta/dz$ das Vorzeichen "
          "wechselt. Nicht die Wolke endet, sondern der Auftrieb. In einem "
          "Hoch ist es die Absinkinversion in 1 bis 2 km, über dem Meer "
          "die Passatinversion. Die Höhe schätzt man aus dem Verhältnis "
          "von Wolkendicke zu Wolkenbreite: Ballen, die breiter als hoch "
          "sind, haben den Deckel schon erreicht.\n\n"
          "**Glatte, strukturlose Schichten.** Stratus, Altostratus, "
          "Cirrostratus: gehobene *Schichten*, nicht gehobene *Pakete*. "
          "$N^2 > 0$, die Hebung kommt nicht von innen, sondern von außen -- "
          "Aufgleiten an einer Front, großflächiges Steigen, nächtliche "
          "Abkühlung einer ganzen Lage. Ein stabil geschichteter Himmel "
          "hat keine Textur, weil keine Zelle den Nachbarn überholen "
          "kann.\n\n"
          "**Türmchen im Mittelstockwerk.** Altocumulus *castellanus*: "
          "kleine Zinnen auf einer mittelhohen Schicht. Dieselbe Aussage "
          "wie beim Blumenkohl, nur 4 km höher -- und daher wichtiger, "
          "denn Labilität im Mittelstockwerk am Morgen ist die "
          "Voraussetzung dafür, dass die Nachmittagskonvektion nicht in "
          "2 km aufhört.\n\n"
          "**Zerfaserte Basen, fractus, schiefe Ballen.** Wo die Basis "
          "ausfranst und einzelne Fetzen darunter treiben, ist die "
          "Grenzschicht turbulent und geschert (dy-reibung): Der Wind "
          "nimmt mit der Höhe zu, und die Wolke wird auseinandergezogen, "
          "bevor sie fertig ist. Dasselbe Bild heißt bei Stratocumulus "
          "*undulatus* -- Wellen auf einer Sprungschicht.\n\n"
          "**Die Linse im Lee.** Lenticularis ist die stabilste Form, die "
          "es gibt: Sie steht still, während die Luft durch sie "
          "hindurchströmt, und sie wäre ohne $N^2 > 0$ unmöglich. Wer eine "
          "Linse sieht, weiß, dass es in dieser Höhe keine Konvektion "
          "geben wird, egal wie warm der Boden wird.\n\n"
          "**Die Zahl.** Ein Feld Cumulus humilis, Basis in 1200 m, alle "
          "Oberkanten in 1800 m, Bodentemperatur am Nachmittag 26 °C. Das "
          "Paket steigt trockenadiabatisch bis zur Basis "
          "($\\Gamma_d = 9{,}8$ K/km, th-adiabate) und feuchtadiabatisch mit "
          "6 K/km darüber (fe-hebung):\n\n"
          r"$$T_{Spitze} = 26 - 9{,}8\cdot 1{,}2 - 6{,}0\cdot 0{,}6 = 10{,}7$$" "\n\n"
          "-- alles in Grad Celsius; an der Basis in 1200 m sind es "
          "14,3 °C. Die beiden Zahlen zusammen sind ein halber "
          "Radiosondenaufstieg. Zwischen 1200 und 1800 m **muss** die "
          "Umgebung kälter sein als die Feuchtadiabate, sonst wären die "
          "Türme nie bis 1800 m gekommen -- diese Schicht ist bedingt "
          "labil. Und in 1800 m **muss** sie wärmer sein als 10,7 °C, "
          "sonst wären sie weitergewachsen. Genau dort kippt das "
          "Vorzeichen von $d\\theta/dz$: **die Unterkante der "
          "Absinkinversion, abgelesen am Lineal der Wolkenoberkanten und "
          "an einem Thermometer am Boden.** Ein Radiosondenaufstieg würde "
          "dasselbe liefern und 300 km entfernt starten.",
          "Looking up is a measurement. Not of temperature or pressure -- "
          "those stay hidden -- but of exactly the sign chapter 2 was "
          "driving at: that of $d\\theta/dz$. The cloud shows it because it is "
          "made of air that has just been lifted, and because the way it "
          "came to rest is set by the stratification. So what is learnt "
          "here is not a set of names but how to read off a sign.\n\n"
          "**Cauliflower with hard edges.** An edge is sharp when it is "
          "made of droplets, and a droplet lives only minutes before it "
          "evaporates or freezes. A sharp, outward-bulging edge is "
          "therefore **young**: here the air is rising faster than the "
          "entrainment of dry ambient air can eat the cloud away. In the "
          "language of th-stabilitaet that is $N^2 < 0$ -- but for the "
          "*saturated* parcel, i.e. conditional instability between $\\Gamma_s$ "
          "and $\\Gamma_d$ (fe-emagram). The free atmosphere is almost never "
          "unstable for dry air.\n\n"
          "**Tops in a straight line.** This is the sharpest reading the "
          "sky offers: when a field of cumuli is cut off above as if with "
          "a ruler, that is the base of an **inversion** -- the lid where "
          "$d\\theta/dz$ changes sign. It is not the cloud that ends but the "
          "buoyancy. In an anticyclone it is the subsidence inversion at "
          "1 to 2 km, over the ocean the trade-wind inversion. Its height "
          "can be judged from the ratio of cloud depth to cloud width: "
          "rolls that are wider than they are tall have already reached "
          "the lid.\n\n"
          "**Smooth, featureless layers.** Stratus, altostratus, "
          "cirrostratus: lifted *layers*, not lifted *parcels*. $N^2 > 0$, "
          "and the lifting comes from outside rather than from within -- "
          "upglide at a front, large-scale ascent, the nocturnal cooling "
          "of a whole slab. A stably stratified sky has no texture, "
          "because no cell can overtake its neighbour.\n\n"
          "**Turrets at mid level.** Altocumulus *castellanus*: little "
          "battlements on a mid-level sheet. The same statement as the "
          "cauliflower, only 4 km higher up -- and therefore more "
          "important, because instability at mid level in the morning is "
          "what decides whether the afternoon convection stops at 2 km or "
          "does not.\n\n"
          "**Frayed bases, fractus, leaning rolls.** Where the base "
          "unravels and single shreds drift below it, the boundary layer "
          "is turbulent and sheared (dy-reibung): the wind increases with "
          "height and the cloud is pulled apart before it is finished. "
          "The same picture in a stratocumulus sheet is called "
          "*undulatus* -- waves on a discontinuity.\n\n"
          "**The lens in the lee.** Lenticularis is the most stable form "
          "there is: it stands still while the air streams through it, "
          "and without $N^2 > 0$ it could not exist at all. Anyone who sees "
          "a lens knows there will be no convection at that height, "
          "however warm the ground gets.\n\n"
          "**The number.** A field of cumulus humilis, base at 1200 m, "
          "every top at 1800 m, surface temperature in the afternoon "
          "26 °C. The parcel rises dry adiabatically to the base "
          "($\\Gamma_d = 9.8$ K/km, th-adiabate) and moist adiabatically at "
          "6 K/km above it (fe-hebung):\n\n"
          r"$$T_{top} = 26 - 9.8\cdot 1.2 - 6.0\cdot 0.6 = 10.7$$" "\n\n"
          "-- all of it in degrees Celsius; at the base, 1200 m up, it is "
          "14.3 °C. The two numbers together are half a radiosonde "
          "ascent. Between 1200 and 1800 m the environment **must** be "
          "colder than the moist adiabat, otherwise the towers would "
          "never have reached 1800 m -- that layer is conditionally "
          "unstable. And at 1800 m it **must** be warmer than 10.7 °C, "
          "otherwise they would have kept going. That is where the sign "
          "of $d\\theta/dz$ flips: **the base of the subsidence "
          "inversion, read off the ruler of the cloud tops and a "
          "thermometer at the ground.** A radiosonde would give the same "
          "answer and be launched 300 km away."),
        "skizze-stabilitaet", [
        zahl(t("Cumulus-Basis 1200 m, alle Oberkanten 1800 m, Boden "
               "26 °C. Trockenadiabatisch bis zur Basis, dann 6 K/km: "
               "Welche Temperatur hat das Paket an der Oberkante? (in °C, "
               "eine Nachkommastelle)",
               "Cumulus base 1200 m, every top at 1800 m, ground 26 °C. "
               "Dry adiabatic to the base, then 6 K/km: what is the "
               "parcel temperature at the top? (in °C, one decimal)"),
             rund(WL_T_OBERKANTE, 1), t("°C", "°C"),
             t("`26 − 9,8·1,2 − 6,0·0,6 = 26 − 11,7 − 3,6 = 10,7 °C`. Weil "
               "das Steigen genau dort aufhört, ist das die Temperatur der "
               "Umgebung in 1800 m -- die Unterkante der Inversion.",
               "`26 − 9.8·1.2 − 6.0·0.6 = 26 − 11.7 − 3.6 = 10.7 °C`. "
               "Because the ascent stops exactly there, that is the "
               "environmental temperature at 1800 m -- the base of the "
               "inversion."),
             toleranz=0.04),
        mc(t("Ein ganzes Feld Cumulus ist oben in derselben Höhe wie mit "
             "dem Lineal abgeschnitten. Was ist damit gemessen?",
             "A whole field of cumulus is cut off above at one and the "
             "same height, as if with a ruler. What has been measured?"),
           [t("Die Wolken haben dort ihren Dampf aufgebraucht.",
              "The clouds have used up their vapour at that height."),
            t("Der Höhenwind schneidet sie ab.",
              "The upper wind is shearing them off."),
            t("Die Höhe, in der $d\\theta/dz$ das Vorzeichen wechselt: die "
              "Unterkante einer Inversion.",
              "The height at which $d\\theta/dz$ changes sign: the base of "
              "an inversion."),
            t("Das Kondensationsniveau.", "The condensation level.")], 2,
           t("Die Basis ist das LCL, die Oberkante ist der Deckel. Beides "
             "zusammen gibt die Dicke der Mischungsschicht, und mit der "
             "Bodentemperatur den ganzen Aufstieg bis dorthin.",
             "The base is the LCL, the top is the lid. Together they give "
             "the depth of the mixed layer, and with the surface "
             "temperature the entire sounding up to it."),
           bild="cu-humilis"),
        mc(t("Welche der vier Wolken beweist die **stabilste** Schichtung "
             "in ihrer Höhe?",
             "Which of the four clouds proves the **most stable** "
             "stratification at its own height?"),
           [t("Cumulus congestus mit harten Rändern.",
              "Cumulus congestus with hard edges."),
            t("Altocumulus lenticularis, die stehende Linse.",
              "Altocumulus lenticularis, the standing lens."),
            t("Altocumulus castellanus mit Türmchen.",
              "Altocumulus castellanus with turrets."),
            t("Cumulus fractus mit zerfaserter Basis.",
              "Cumulus fractus with a frayed base.")], 1,
           t("Eine stehende Welle braucht $N^2 > 0$; je stärker die "
             "Stabilität, desto kürzer und schärfer die Linse. "
             "Castellanus und congestus beweisen das Gegenteil, fractus "
             "beweist Turbulenz.",
             "A standing wave needs $N^2 > 0$; the stronger the stability, "
             "the shorter and sharper the lens. Castellanus and congestus "
             "prove the opposite, fractus proves turbulence."),
           bild="lenticularis"),
        ]),

    lektion("wb-tageslauf",
        t("Der Tag einer Konvektionszelle, mit der Uhr",
          "The day of a convective cell, by the clock"),
        ["tageslauf-konvektion", "ausloesetemperatur", "gewitteranzeichen"],
        t("Konvektion hat einen Fahrplan, und er ist nachrechenbar. Was "
          "folgt, ist ein Beobachtungsprotokoll eines Sommertages im "
          "Flachland -- mit der Uhrzeit, denn die Uhrzeit ist das "
          "Messgerät.\n\n"
          "**8 Uhr.** Kein Wölkchen, aber der Himmel ist nicht blau, "
          "sondern milchig, und die Dunstschicht hat eine erstaunlich "
          "scharfe Oberkante. Das ist die nächtliche Bodeninversion "
          "(st-tagesgang): Unter ihr sammelt sich alles, über ihr ist es "
          "klar. Steht man auf einem Hügel, sieht man sie von oben.\n\n"
          "**9 bis 10 Uhr.** Die Sonne heizt den Boden, der Boden heizt "
          "die unterste Luft, und die Inversion wird **von unten "
          "weggefressen**: Eine durchmischte Schicht wächst nach oben. Sie "
          "ist trockenadiabatisch geschichtet, also wird ihre potentielle "
          "Temperatur einheitlich -- genau die Figur aus th-theta.\n\n"
          "**Die erste Wolke, und ihre Uhrzeit.** Sie erscheint, sobald "
          "die Mischungsschicht ihr Kondensationsniveau erreicht. Liegt "
          "über der Inversion ein Deckel -- eine Schicht mit 14 °C in "
          "1500 m --, dann muss die Bodentemperatur so weit steigen, dass "
          "ein trockenadiabatisch aufsteigendes Paket dort noch wärmer "
          "ist. Die **Auslösetemperatur** ist\n\n"
          r"$$T_{Trigger} = T_{Deckel} + \Gamma_d\,z_{Deckel} = 14 + 9{,}8\cdot 1{,}5 = 28{,}7$$" "\n\n"
          "-- in Grad Celsius gerechnet. "
          "Das ist die nützlichste Zahl des ganzen Kapitels. Erreicht der "
          "Tag nur 26 °C, bleiben die Haufen flach unter dem Deckel, so "
          "warm es sich auch anfühlt. "
          "Erreicht er 30 °C, geht es in dem Moment los, in dem das "
          "Thermometer durch 28,7 °C läuft -- in der Praxis zwischen 11 "
          "und 13 Uhr. Dieselbe Zahl erklärt, warum ein Tag im Juni mit "
          "28 °C nichts bringt und einer im August mit 31 °C ein Gewitter "
          "pro Tal.\n\n"
          "**11 bis 12 Uhr.** Erste Fetzen am LCL, Cumulus fractus, dann "
          "humilis mit flacher Basis. Und etwas Merkwürdiges: Die Basis "
          "**steigt** im Tagesverlauf, von 900 m am Morgen auf 1600 m am "
          "Nachmittag. Nach fe-hebung ist $z_{LCL} = 125$ m/K $\\cdot(T - T_d)$, "
          "und die Spreizung wächst von beiden Seiten -- `T` steigt, weil "
          "die Sonne heizt, und $T_d$ **sinkt**, weil die wachsende "
          "Mischungsschicht trockene Luft von oben einmischt. Die Wolke "
          "fährt mit ihrem eigenen Kondensationsniveau nach oben.\n\n"
          "**13 bis 15 Uhr.** Mediocris, dann congestus: Türme, die höher "
          "als breit sind, mit harten Rändern. Dann wird die Spitze "
          "faserig -- sie ist vereist, Bergeron-Findeisen setzt ein "
          "(wo-wachstum), und der Schauer beginnt. Die **Zeitskala** einer "
          "Zelle ist Dicke durch Aufwind: 3 km / 3 m/s = 17 min, bis das "
          "Wasser oben ist und als Regen zurückkommt. Beobachtet werden 30 "
          "bis 60 Minuten Lebensdauer (me-gewitter) -- das Doppelte, weil "
          "die Zelle nachliefert, solange der Aufwind steht.\n\n"
          "**Die Anzeichenkette, mit Zeiten.** Am Morgen Altocumulus "
          "castellanus oder floccus und ein Taupunkt über 16 °C: "
          "Labilität bis ins Mittelstockwerk, Gewitter wahrscheinlich. "
          "Mittags harte Cu-Ränder und Türme, die über ihre Nachbarn "
          "hinausschießen. Dann der Amboss, dessen Faserung **gegen den "
          "Bodenwind** zeigt -- Scherung, also eine Zelle, die sich "
          "erneuert. Eine dunkle, regenfreie Basis und ein Arcus davor: "
          "die Böenfront, 10 bis 20 km vor dem Regen (me-gewitter). Wind, "
          "der plötzlich aus der falschen Richtung einfällt, und 15 "
          "Minuten später der Temperatursturz. Mammatus auf der Rückseite "
          "heißt: vorbei.\n\n"
          "**Die Gegenprobe.** Cumulus humilis, der um 15 Uhr nicht "
          "größer wird, ist die zuverlässigste Schönwettervorhersage, die "
          "es ohne Modell gibt: Der Deckel sitzt fest, das Tagesmaximum "
          "ist durch, es bleibt, wie es ist.\n\n"
          "**Die Zahl zum Mitnehmen.** Eine Zelle zieht etwa mit dem "
          "700-hPa-Wind. Bei 15 m/s sind das 54 km/h; eine Zelle, die am "
          "Horizont in 25 km steht, ist in 28 Minuten da, die Böenfront in "
          "10 bis 15. So lange hat man, um die Wäsche zu holen.",
          "Convection runs to a timetable, and the timetable can be "
          "calculated. What follows is an observing log of a summer day "
          "in the lowlands -- with the clock times, because the clock is "
          "the instrument.\n\n"
          "**08:00.** Not a cloud, but the sky is not blue either: it is "
          "milky, and the haze layer has a surprisingly sharp top. That "
          "is the nocturnal surface inversion (st-tagesgang): everything "
          "collects below it and above it the air is clean. From a hill "
          "one looks down on it.\n\n"
          "**09:00 to 10:00.** The sun heats the ground, the ground heats "
          "the lowest air, and the inversion is **eaten away from "
          "below**: a mixed layer grows upward. It is stratified dry "
          "adiabatically, so its potential temperature becomes uniform -- "
          "exactly the picture from th-theta.\n\n"
          "**The first cloud, and its hour.** It appears as soon as the "
          "mixed layer reaches its condensation level. If a lid sits "
          "above the inversion -- a layer at 14 °C at 1500 m -- then the "
          "surface temperature has to rise far enough that a parcel "
          "ascending dry adiabatically is still warmer up there. The "
          "**trigger temperature** is\n\n"
          r"$$T_{trigger} = T_{lid} + \Gamma_d\,z_{lid} = 14 + 9.8\cdot 1.5 = 28.7$$" "\n\n"
          "-- in degrees Celsius. "
          "That is the most useful number in the whole chapter. If the day "
          "reaches only 26 °C the heaps stay flat under the lid, however "
          "warm it feels. If it "
          "reaches 30 °C, things start the moment the thermometer passes "
          "28.7 °C -- in practice between 11:00 and 13:00. The same "
          "number explains why a June day at 28 °C gives nothing and an "
          "August day at 31 °C gives one thunderstorm per valley.\n\n"
          "**11:00 to 12:00.** First shreds at the LCL, cumulus fractus, "
          "then humilis with a flat base. And something odd: the base "
          "**rises** through the day, from 900 m in the morning to 1600 m "
          "in the afternoon. By fe-hebung $z_{LCL} = 125$ m/K $\\cdot(T - T_d)$, "
          "and the spread widens from both ends -- `T` rises because the "
          "sun heats, and $T_d$ **falls** because the deepening mixed layer "
          "entrains dry air from above. The cloud rides upward on its own "
          "condensation level.\n\n"
          "**13:00 to 15:00.** Mediocris, then congestus: towers taller "
          "than they are wide, with hard edges. Then the top turns "
          "fibrous -- it has glaciated, Bergeron–Findeisen sets in "
          "(wo-wachstum), and the shower starts. The **time scale** of a "
          "cell is depth over updraught: 3 km / 3 m/s = 17 min for the "
          "water to get up and come back as rain. The observed lifetime "
          "is 30 to 60 minutes (me-gewitter) -- twice as long, because the "
          "cell keeps resupplying as long as the updraught stands.\n\n"
          "**The chain of signs, with times.** In the morning altocumulus "
          "castellanus or floccus and a dew point above 16 °C: "
          "instability up into the middle level, thunderstorms likely. At "
          "midday hard cumulus edges and towers overshooting their "
          "neighbours. Then the anvil, whose fibres point **against the "
          "surface wind** -- shear, hence a cell that renews itself. A "
          "dark rain-free base with an arcus in front of it: the gust "
          "front, 10 to 20 km ahead of the rain (me-gewitter). Wind "
          "suddenly arriving from the wrong direction, and the "
          "temperature drop 15 minutes later. Mammatus on the back side "
          "means: over.\n\n"
          "**The counter-check.** Cumulus humilis that is no bigger at "
          "15:00 than at 13:00 is the most reliable fair-weather forecast "
          "available without a model: the lid is holding, the daily "
          "maximum is past, nothing will change.\n\n"
          "**The number to take along.** A cell travels roughly with the "
          "700 hPa wind. At 15 m/s that is 54 km/h; a cell standing 25 km "
          "off on the horizon arrives in 28 minutes, its gust front in 10 "
          "to 15. That is how long there is to fetch the washing in."),
        "cu-zyklus", [
        zahl(t("Über der Inversion liegt ein Deckel: 14 °C in 1500 m. "
               "Welche Bodentemperatur löst die Konvektion aus? (in °C, "
               "eine Nachkommastelle)",
               "A lid sits above the inversion: 14 °C at 1500 m. What "
               "surface temperature triggers the convection? (in °C, one "
               "decimal)"),
             rund(WL_T_TRIGGER, 1), t("°C", "°C"),
             t("Trockenadiabatisch herunter: `14 + 9,8 × 1,5 = 28,7 °C`. "
               "Darunter bleibt das Paket in 1500 m kälter als die "
               "Umgebung und sinkt zurück -- wolkenlos.",
               "Dry adiabatically back down: `14 + 9.8 × 1.5 = 28.7 °C`. "
               "Below that the parcel is colder than its surroundings at "
               "1500 m and sinks back -- no cloud."),
             toleranz=0.03),
        zahl(t("Eine Gewitterzelle steht 25 km entfernt und zieht mit dem "
               "700-hPa-Wind von 15 m/s heran. In wie vielen Minuten ist "
               "sie da? (in min)",
               "A thunderstorm cell stands 25 km away and travels with "
               "the 700 hPa wind of 15 m/s. In how many minutes does it "
               "arrive? (in min)"),
             rund(WL_ANKUNFT), t("min", "min"),
             t("`25 000 m / 15 m/s = 1667 s = 28 min`. Die Böenfront läuft "
               "10 bis 20 km voraus, ist also schon in 10 bis 15 Minuten "
               "da.",
               "`25 000 m / 15 m/s = 1667 s = 28 min`. The gust front "
               "runs 10 to 20 km ahead, so it arrives within 10 to 15 "
               "minutes."),
             toleranz=0.05),
        mc(t("Die Wolkenbasis liegt um 10 Uhr bei 900 m und um 15 Uhr bei "
             "1600 m. Warum steigt sie?",
             "The cloud base is at 900 m at 10:00 and at 1600 m at 15:00. "
             "Why does it rise?"),
           [t("Die Mischungsschicht wird tiefer: `T` steigt und $T_d$ sinkt, "
              "weil trockene Luft von oben eingemischt wird -- die "
              "Spreizung wächst von beiden Seiten.",
              "The mixed layer deepens: `T` rises and $T_d$ falls, because "
              "dry air is entrained from above -- the spread widens from "
              "both ends."),
            t("Der Luftdruck fällt im Tagesverlauf.",
              "The air pressure falls through the day."),
            t("Die Wolken werden vom Wind angehoben.",
              "The clouds are lifted by the wind."),
            t("Die Sonne steht höher, also ist die Wolke scheinbar "
              "höher.",
              "The sun is higher, so the cloud only appears higher.")], 0,
           t("$z_{LCL} = 125$ m/K $\\cdot(T - T_d)$: 7 K Spreizung geben 900 m, "
             "13 K geben 1600 m. Das Einmischen von oben ist der Grund, "
             "warum Thermik am späten Nachmittag höher **und** schwächer "
             "wird.",
             "$z_{LCL} = 125$ m/K $\\cdot(T - T_d)$: a spread of 7 K gives 900 m, "
             "13 K gives 1600 m. Entrainment from above is why thermals "
             "late in the afternoon get higher **and** weaker."),
           bild="cu-congestus"),
        ]),

    lektion("wb-sonde",
        t("Die Wolke als Messgerät: Kippen, Wellen, Billows",
          "The cloud as an instrument: tilt, waves, billows"),
        ["scherung-messen", "leewellen", "kelvin-helmholtz"],
        t("Über der Grenzschicht gibt es keine Messstation. Was dort "
          "geschieht, weiß man aus zwei Radiosonden am Tag, aus dem "
          "Modell -- oder vom Hinsehen, denn die Wolke ist ein Zeiger, "
          "den die Strömung selbst in die Luft hält. Drei Ablesungen "
          "lohnen sich, und alle drei ergeben eine Zahl.\n\n"
          "**Erstens: das Kippen misst die Scherung.** Ein Cumulusturm "
          "ist kein Körper, sondern ein Strom von Paketen, die an der "
          "Basis losgelassen werden. Jedes steigt mit `w` und treibt mit "
          "dem Wind seiner Höhe. Nimmt der Wind über die Turmdicke um "
          "$\\Delta U$ zu, dann hat die Achse am Oberrand die Neigung\n\n"
          r"$$\tan\alpha = \frac{\Delta U}{w}$$" "\n\n"
          "gegen die Senkrechte, und die Spitze steht um "
          "$\\Delta U\\,z/(2w)$ versetzt -- halb so viel, weil die Scherung "
          "unten noch nicht gewirkt hat. Ein Turm von 4 km Dicke mit "
          "8 m/s Aufwind, dessen Achse oben 63° gekippt ist, meldet "
          "$\\Delta U = 8\\cdot\\tan 63^\\circ = 16$ m/s über 4 km, und seine Spitze "
          "steht 4 km neben der Basis. Das ist genau die Scherung, die "
          "nach me-gewitter aus einer Einzelzelle eine langlebige macht: "
          "Der Regen fällt neben den Aufwind statt hinein. **Ein "
          "senkrechter Turm regnet sich in 30 Minuten selbst aus; ein "
          "schiefer hält durch.**\n\n"
          "**Zweitens: der Wellenabstand misst die Schichtung.** Hinter "
          "einem Gebirgskamm, oder an jeder Sprungschicht mit "
          "Höhenwind, stehen Wolken in regelmäßigen Abständen: "
          "Lenticularis-Bänke im Lee, Altocumulus *undulatus* als "
          "Wellblech. Die Wellenlänge einer stehenden Schwerewelle steht "
          "schon in der Herleitung zu th-stabilitaet: "
          "$\\lambda = 2\\pi U/N$. Das lässt sich umdrehen. Man schätzt $\\lambda$ "
          "an einer bekannten Strecke am Boden ab und nimmt `U` aus dem "
          "Höhenwind:\n\n"
          r"$$N = \frac{2\pi U}{\lambda}, \qquad \frac{d\theta}{dz} = \frac{N^2\,\theta}{g}$$" "\n\n"
          "Bei $\\lambda = 8{,}6$ km und $U = 15$ m/s ist $N = 0{,}011$ /s, und "
          "mit θ = 290 K folgt $d\\theta/dz = 3{,}6$ K/km. **Das ist die "
          "Schichtung in 3 km Höhe, abgelesen aus dem Abstand zweier "
          "Wolken.** Eine Radiosonde, die zehn Minuten später startet, "
          "gibt denselben Wert.\n\n"
          "**Drittens: Billows messen, ob es gleich ruckelt.** Auf der "
          "Oberseite einer Cirrus-Bank oder einer Stratocumulus-Decke "
          "steht manchmal eine Reihe brechender Wellen, wie Brandung von "
          "der Seite gesehen: **Kelvin-Helmholtz-Billows**. Sie entstehen, "
          "wenn die Scherung an einer dünnen Schicht die Stabilität "
          "überwindet. Das Maß dafür ist die **Richardson-Zahl**\n\n"
          r"$$\mathrm{Ri} = \frac{N^2}{(du/dz)^2}$$" "\n\n"
          "-- das Verhältnis der Arbeit, die ein Wirbel gegen die "
          "Schichtung leisten muss, zur Energie, die ihm die Scherung "
          "liefert. Nach Miles und Howard ist eine stabil geschichtete "
          "Scherströmung sicher stabil, solange $\\mathrm{Ri} > 1/4$ überall "
          "gilt; Instabilität verlangt also $\\mathrm{Ri} < 1/4$ irgendwo, das "
          "heißt $du/dz > 2N$. Mit $N = 0{,}011$ /s sind das 22 m/s je "
          "Kilometer. **Wer Billows sieht, sieht eine Schicht, in der die "
          "Scherung mindestens 22 m/s je Kilometer beträgt** -- und genau "
          "dort schüttelt es im Flugzeug, bei blauem Himmel.\n\n"
          "Drei Ablesungen, drei Zahlen: Scherung aus dem Kippen, "
          "$d\\theta/dz$ aus dem Wellenabstand, eine untere Grenze für "
          "$du/dz$ aus den Billows. Keine davon braucht ein Gerät; alle "
          "drei kommen aus Gleichungen, die in diesem Kurs schon "
          "hergeleitet sind.",
          "Above the boundary layer there is no weather station. What "
          "happens up there is known from two radiosondes a day, from "
          "the model -- or by looking, because a cloud is a pointer the "
          "flow itself holds up into the air. Three readings are worth "
          "taking, and each of them yields a number.\n\n"
          "**First: the tilt measures the shear.** A cumulus tower is not "
          "a body but a stream of parcels released at its base. Each "
          "rises at `w` and drifts with the wind at its own height. If "
          "the wind increases by $\\Delta U$ over the depth of the tower, "
          "the axis at the top has the slope\n\n"
          r"$$\tan\alpha = \frac{\Delta U}{w}$$" "\n\n"
          "against the vertical, and the top stands offset by "
          "$\\Delta U\\,z/(2w)$ -- half as much, because the shear had not yet "
          "acted lower down. A tower 4 km deep with an 8 m/s updraught "
          "whose axis leans 63° at the top reports "
          "$\\Delta U = 8\\cdot\\tan 63^\\circ = 16$ m/s over 4 km, and its top "
          "stands 4 km to the side of its base. That is precisely the "
          "shear which, by me-gewitter, turns a single cell into a "
          "long-lived one: the rain falls beside the updraught instead of "
          "into it. **An upright tower rains itself out in 30 minutes; a "
          "leaning one lasts.**\n\n"
          "**Second: the wave spacing measures the stratification.** "
          "Behind a mountain ridge, or at any discontinuity with wind "
          "aloft, clouds stand at regular intervals: lenticular banks in "
          "the lee, altocumulus *undulatus* like corrugated iron. The "
          "wavelength of a standing gravity wave is already in the "
          "derivation attached to th-stabilitaet: $\\lambda = 2\\pi U/N$. That "
          "can be turned around. Estimate $\\lambda$ against a known distance "
          "on the ground and take `U` from the wind aloft:\n\n"
          r"$$N = \frac{2\pi U}{\lambda}, \qquad \frac{d\theta}{dz} = \frac{N^2\,\theta}{g}$$" "\n\n"
          "With $\\lambda = 8.6$ km and $U = 15$ m/s, $N = 0.011$ /s, and with "
          "θ = 290 K that gives $d\\theta/dz = 3.6$ K/km. **That is the "
          "stratification at 3 km, read off the spacing of two clouds.** A "
          "radiosonde launched ten minutes later returns the same "
          "value.\n\n"
          "**Third: billows measure whether it is about to get bumpy.** "
          "On top of a cirrus bank or a stratocumulus sheet there is "
          "sometimes a row of breaking waves, like surf seen from the "
          "side: **Kelvin–Helmholtz billows**. They form when the shear "
          "across a thin layer overcomes the stability. The measure of "
          "that is the **Richardson number**\n\n"
          r"$$\mathrm{Ri} = \frac{N^2}{(du/dz)^2}$$" "\n\n"
          "-- the ratio of the work an eddy has to do against the "
          "stratification to the energy the shear supplies it. By Miles "
          "and Howard, a stably stratified shear flow is certainly stable "
          "as long as $\\mathrm{Ri} > 1/4$ everywhere; instability therefore "
          "requires $\\mathrm{Ri} < 1/4$ somewhere, that is $du/dz > 2N$. With "
          "$N = 0.011$ /s that is 22 m/s per kilometre. **Anyone who sees "
          "billows is seeing a layer in which the shear is at least "
          "22 m/s per kilometre** -- and that is exactly where an "
          "aircraft is shaken, under a blue sky.\n\n"
          "Three readings, three numbers: shear from the tilt, "
          "$d\\theta/dz$ from the wave spacing, a lower bound on $du/dz$ from "
          "the billows. None of them needs an instrument; all three come "
          "out of equations this course has already derived."),
        "wolkenlesen-sonde", [
        zahl(t("Ein Turm von 4 km Dicke, Aufwind 8 m/s, Scherung 16 m/s "
               "über die Turmdicke. Wie stark ist die Achse am Oberrand "
               "gegen die Senkrechte geneigt? (in Grad, eine "
               "Nachkommastelle)",
               "A tower 4 km deep, updraught 8 m/s, shear 16 m/s across "
               "its depth. How far does the axis lean from the vertical "
               "at the top? (in degrees, one decimal)"),
             rund(WL_KIPPWINKEL, 1), t("°", "°"),
             t("`tan α = ΔU/w = 16/8 = 2`, also `α = 63,4°`. Die Spitze "
               "steht dabei `ΔU·z/(2w) = 16 × 4000 / 16 = 4000 m` neben "
               "der Basis -- halb so weit, wie die Achsenneigung oben "
               "vermuten lässt.",
               "`tan α = ΔU/w = 16/8 = 2`, hence `α = 63.4°`. The top "
               "stands `ΔU·z/(2w) = 16 × 4000 / 16 = 4000 m` beside the "
               "base -- half as far as the slope at the top suggests."),
             toleranz=0.03),
        zahl(t("Wellenwolken in 8,6 km Abstand, Grundstrom 15 m/s, "
               "θ = 290 K. Welches dθ/dz zeigt das an? (in K/km, zwei "
               "Nachkommastellen)",
               "Wave clouds spaced 8.6 km apart, mean flow 15 m/s, "
               "θ = 290 K. What dθ/dz does that indicate? (in K/km, two "
               "decimals)"),
             rund(WL_DTHETA_DZ, 2), t("K/km", "K/km"),
             t("`N = 2π·15/8600 = 0,01096 /s`, `N² = 1,20·10⁻⁴ /s²`, "
               "`dθ/dz = N²θ/g = 1,20·10⁻⁴ × 290 / 9,81 = 3,55·10⁻³ /m "
               "= 3,55 K/km`. Normal geschichtete Troposphäre.",
               "`N = 2π·15/8600 = 0.01096 /s`, `N² = 1.20·10⁻⁴ /s²`, "
               "`dθ/dz = N²θ/g = 1.20·10⁻⁴ × 290 / 9.81 = 3.55·10⁻³ /m "
               "= 3.55 K/km`. A normally stratified troposphere."),
             toleranz=0.04),
        mc(t("Auf der Oberseite einer Cirrus-Bank steht eine Reihe "
             "brechender Wellen. Was weiß man damit über diese Schicht?",
             "A row of breaking waves stands on top of a cirrus bank. "
             "What does that tell you about the layer?"),
           [t("Dort ist der Höhenwind schwach.",
              "The wind aloft is weak there."),
            t("Die Schicht ist gesättigt und kondensiert gleich ganz "
              "aus.",
              "The layer is saturated and about to condense out "
              "entirely."),
            t("Es regnet in Kürze.", "Rain is about to start."),
            t("Dort ist $\\mathrm{Ri}$ unter 1/4 gefallen: die Scherung "
              "beträgt mindestens $2N$, rund 22 m/s je Kilometer -- "
              "Turbulenz in klarer Luft.",
              "$\\mathrm{Ri}$ has fallen below 1/4 there: the shear is at "
              "least $2N$, about 22 m/s per kilometre -- turbulence in "
              "clear air.")], 3,
           t("Billows sind ein Scherungsmesser mit Schwelle. Sie sagen "
             "nicht, wie groß die Scherung ist, aber dass sie mindestens "
             "$2N$ beträgt -- und das ist die Zahl, die eine "
             "Turbulenzmeldung auslöst.",
             "Billows are a shear meter with a threshold. They do not say "
             "how large the shear is, only that it is at least $2N$ -- and "
             "that is the number behind a turbulence report."),
           bild="cirrus"),
        ]),
    ])


# ===========================================================================
# 5b  Das Wolkenbuch
# ===========================================================================

# Die Zuggeschwindigkeit am Himmel taeuscht: der Wind waechst mit der Hoehe
# etwa so schnell wie die Hoehe selbst, also kuerzt sich z aus U/z heraus.
WB_WINKEL_CU = math.degrees(7.0 / 1500.0) * 60.0        # °/min, Cu in 1,5 km
WB_WINKEL_CI = math.degrees(40.0 / 10000.0) * 60.0      # °/min, Ci in 10 km
# Wo die Standardatmosphaere −40 °C erreicht: darueber ist jede Wolke Eis.
WB_EIS_HOEHE = (15.0 - (-40.0)) / 6.5                   # km
# Basishoehe aus dem Wolkenschatten, z = s·tan h
WB_SCHATTEN_S = 2500.0                                  # m
WB_SCHATTEN_H = 40.0                                    # °
WB_SCHATTEN_Z = WB_SCHATTEN_S * math.tan(math.radians(WB_SCHATTEN_H))
# Scheinbare Groesse der Ballen: Cirrocumulus unter 1°, Altocumulus 1-5°,
# Stratocumulus darueber. Ein Ballen von 600 m in 6 km Hoehe:
WB_BALLEN_WINKEL = math.degrees(600.0 / 6000.0)         # °
# Wellenlaenge einer undulatus-Reihe: die stehende Welle aus th-stabilitaet
WB_U_WELLE = 15.0                                       # m/s
WB_N_WELLE = 0.011                                      # 1/s
WB_UNDULATUS = 2 * math.pi * WB_U_WELLE / WB_N_WELLE    # m
# Mammatus: negativer Auftrieb b = g·ΔT/T bei 2 K Unterkuehlung
WB_MAMMATUS_B = G * 2.0 / 280.0                         # m/s²
WB_MAMMATUS_V = math.sqrt(2 * WB_MAMMATUS_B * 500.0)    # m/s nach 500 m
# Virga: Verdunsten ist Diffusionswachstum mit S < 0 (wo-wachstum), also
# r² = r₀² − 2·ξ·|S|·t. Ein Tropfen von 100 μm in 50 % untersaettigter Luft:
WB_VIRGA_R = 100.0e-6                                   # m
WB_VIRGA_T = WB_VIRGA_R ** 2 / (2 * XI_PROZENT * 50.0)  # s
WB_VIRGA_V = 0.7                                        # m/s, wo-wachstum
WB_VIRGA_WEG = WB_VIRGA_T * WB_VIRGA_V                  # m
# Schmidt-Appleman: die Steigung der Mischungsgerade von Abgas und Umgebung
WB_EI = 1.25        # kg Wasser je kg Kerosin
WB_Q = 43.0e6       # J/kg Heizwert
WB_ETA = 0.30       # Vortriebswirkungsgrad
WB_EPSILON = 0.622  # M_v/M_L
WB_P_FLUG = 25000.0                                     # Pa, rund 250 hPa
WB_G_APPLEMAN = WB_EI * C_P * WB_P_FLUG / (WB_EPSILON * WB_Q * (1 - WB_ETA))


def e_s_eis(T_celsius):
    """Magnus über Eis, hPa. Dieselbe Form, steilere Beiwerte, weil
    L_s = L_v + L_f eingeht."""
    return 6.112 * math.exp(22.46 * T_celsius / (272.62 + T_celsius))


def de_s_dT(T_celsius):
    """Steigung der Magnus-Kurve über Wasser, Pa/K."""
    return 100.0 * e_s(T_celsius) * 17.62 * 243.12 / (243.12 + T_celsius) ** 2


def wb_schwelle(steigung):
    """Die Temperatur, in der die Mischungsgerade die Sättigungskurve
    berührt: dort ist de_s/dT gleich der Steigung der Geraden."""
    tief, hoch = -70.0, -5.0
    for _ in range(80):
        mitte = 0.5 * (tief + hoch)
        if de_s_dT(mitte) > steigung:
            hoch = mitte
        else:
            tief = mitte
    return 0.5 * (tief + hoch)


WB_T_SCHWELLE = wb_schwelle(WB_G_APPLEMAN)              # °C
WB_Z_SCHWELLE = (15.0 - WB_T_SCHWELLE) / 6.5            # km, at-standard
WB_EIS_ANTEIL_15 = e_s_eis(-15.0) / e_s(-15.0) * 100.0  # %
WB_EIS_ANTEIL_45 = e_s_eis(-45.0) / e_s(-45.0) * 100.0  # %

K_WOLKENBUCH = kapitel(
    "wolkenbuch", t("Das Wolkenbuch: Arten, Beinamen, Sonderformen",
                    "The cloud book: species, supplementary features, "
                    "special forms"), 5,
    t("wo-gattungen gibt den zehn Wolken ihre Namen. Hier kommt die Ebene "
      "darunter: Arten, Unterarten, Begleit- und Sonderformen -- und die "
      "Frage, die einen Physiker daran interessiert: Was sagt diese Form "
      "über die Luft, in der sie steht? Jede Endung ist eine Aussage über "
      "einen Prozess, nicht über ein Aussehen.",
      "wo-gattungen gives the ten clouds their names. This is the level "
      "below it: species, varieties, accessory clouds and supplementary "
      "features -- and the question a physicist asks of them: what does "
      "this shape say about the air it stands in? Every ending is a "
      "statement about a process, not about an appearance."), [

    lektion("wb-stockwerke",
        t("Hoch, mittel, tief -- und wie man sich dabei irrt",
          "High, middle, low -- and how one gets it wrong"),
        ["stockwerke", "randschaerfe", "halo-oder-korona", "schattenhoehe"],
        t("Man tritt vor die Tür, sieht eine Wolke und soll sagen, in "
          "welchem Stockwerk sie hängt. Das beliebteste Kriterium ist "
          "ausgerechnet das untauglichste: **wie schnell sie zieht**. Ein "
          "Cumulus in 1,5 km Höhe, getragen von 7 m/s, überstreicht am "
          "Himmel die Winkelgeschwindigkeit $\\omega = U/z$, also 16°/min. "
          "Ein Cirrus in 10 km Höhe im 40 m/s starken Höhenwind: 14°/min. "
          "Praktisch dasselbe -- und das ist kein Zufall. Der thermische "
          "Wind (dy-thermisch) lässt `U` mit der Höhe wachsen, über der "
          "mittleren Breite grob so schnell wie `z` selbst, und dann kürzt "
          "sich die Höhe aus `U/z` heraus. Wer nach der Zuggeschwindigkeit "
          "geht, rät.\n\n"
          "**Der Rand.** Ein Wassertröpfchen am Wolkenrand verdunstet in "
          "Sekunden, sobald es in untersättigte Luft gerät; der Rand bleibt "
          "dort scharf, wo die Sättigung endet. Eiskristalle wachsen "
          "stattdessen weiter (Bergeron, wo-wachstum), werden groß, fallen "
          "und werden vom Höhenwind ausgekämmt: Der Rand franst zu Fasern "
          "aus. **Scharf heißt Wasser, faserig heißt Eis.** Und Eis heißt "
          "Höhe -- bei −10 °C gefriert reines Wolkenwasser noch nicht von "
          "selbst, erst bei −40 °C ist jeder Tropfen zwangsläufig Eis. In "
          "der Standardatmosphäre (at-standard, $T = 15 - 6{,}5\\,z$ in °C "
          "und km) liegt diese Linie bei 8,5 km. Darüber gibt es nur "
          "Eiswolken, darunter beides -- und daraus folgt die Asymmetrie "
          "des Schlusses: Ein **scharfer** Rand beweist, dass die Wolke "
          "unter 8,5 km steht; ein faseriger macht die Höhe nur "
          "wahrscheinlich, denn Eis gibt es auch tiefer.\n\n"
          "**Halo oder Korona.** Der 22°-Ring um Sonne oder Mond ist "
          "Brechung im sechseckigen Eisprisma (op-regenbogen) -- also Eis, "
          "also Cirrostratus. Ein enger bunter Ring von 2 bis 5°, innen "
          "weiß und außen rot, ist Beugung an Wassertröpfchen -- also "
          "Wasser, also Altocumulus oder dünner Stratus. Verwechseln kann "
          "man die beiden nur, wenn man nicht misst: Die Faust am "
          "ausgestreckten Arm deckt etwa 8°, der Halo liegt deutlich "
          "außerhalb, die Korona weit innerhalb.\n\n"
          "**Die Graustufe der Basis.** Grau ist optische Dicke, und "
          "optische Dicke ist Flüssigwasserweg. Der **Altostratus** lässt "
          "die Sonnenscheibe als Scheibe durch, aber kein Objekt wirft "
          "mehr Schatten -- das ist die Ansage: mittelhoch, einige hundert "
          "Meter dick. Wird die Scheibe unkenntlich und die Basis "
          "dunkelgrau und regnend, ist es **Nimbostratus**, und der steht "
          "nicht in einem Stockwerk, sondern durch alle drei. "
          "**Cirrostratus** dagegen löscht die Scheibe nie und macht die "
          "Schatten nur weich.\n\n"
          "**Der Schatten.** Der verlässlichste Griff, weil er rechnet "
          "statt zu schätzen. Steht die Sonne unter dem Höhenwinkel `h` "
          "und liegt der Schatten der Wolke um die Strecke `s` neben ihr "
          "am Boden, dann ist ihre Basis in der Höhe\n\n"
          r"$$z = s\,\tan h$$" "\n\n"
          "Bei $s = 2{,}5$ km und $h = 40^\\circ$ sind das 2100 m. Das ist "
          "die Gegenprobe zur 125-m-Regel aus fe-hebung: Wer am Boden "
          "24 °C und 12 °C Taupunkt gemessen hat, erwartet seine "
          "Cumulus-Basis in 1500 m. Kommen aus dem Schatten 2100 m heraus, "
          "dann stammt diese Wolke **nicht** aus der Bodenschicht -- sie "
          "ist über einer Inversion entstanden, aus feuchterer Luft weiter "
          "oben, und die 125-m-Regel gilt für sie nicht.\n\n"
          "Zuletzt das Stockwerk selbst, und dass es keine festen Zahlen "
          "hat. Die WMO staffelt nach Breite, weil die Tropopause nach "
          "Breite staffelt: tief überall 0 bis 2 km; mittel polar 2 bis 4, "
          "gemäßigt 2 bis 7, tropisch 2 bis 8 km; hoch polar 3 bis 8, "
          "gemäßigt 5 bis 13, tropisch 6 bis 18 km. Dieselbe Wolke in "
          "derselben Höhe heißt auf Spitzbergen Cirrus und in Jakarta "
          "Altocumulus. Der Grund steht in fe-hebung: Die feuchte "
          "Konvektion stellt die Troposphäre so hoch, wie sie Wärme "
          "hinaufträgt, und in den Tropen trägt sie 18 km hoch.",
          "You step outside, see a cloud and are supposed to say which "
          "level it hangs in. The most popular criterion is precisely the "
          "most useless one: **how fast it moves**. A cumulus at 1.5 km, "
          "carried along at 7 m/s, sweeps the sky at the angular rate "
          "$\\omega = U/z$, which is 16°/min. A cirrus at 10 km in a "
          "40 m/s upper wind: 14°/min. Practically the same -- and that is "
          "no accident. The thermal wind (dy-thermisch) makes `U` grow "
          "with height, in midlatitudes roughly as fast as `z` itself, and "
          "then the height cancels out of `U/z`. Judging by apparent speed "
          "is guessing.\n\n"
          "**The edge.** A water droplet at the cloud edge evaporates "
          "within seconds once it reaches subsaturated air; the edge stays "
          "sharp exactly where saturation ends. Ice crystals instead keep "
          "growing (Bergeron, wo-wachstum), get large, fall, and are "
          "combed out by the upper wind: the edge frays into fibres. "
          "**Sharp means water, fibrous means ice.** And ice means height "
          "-- at −10 °C pure cloud water still does not freeze by itself, "
          "and only at −40 °C is every droplet inevitably ice. In the "
          "standard atmosphere (at-standard, $T = 15 - 6.5\\,z$ in °C and "
          "km) that line sits at 8.5 km. Above it there are only ice "
          "clouds, below it both -- and hence the asymmetry of the "
          "inference: a **sharp** edge proves the cloud stands below "
          "8.5 km; a fibrous one only makes height likely, because there "
          "is ice lower down as well.\n\n"
          "**Halo or corona.** The 22° ring around sun or moon is "
          "refraction in the hexagonal ice prism (op-regenbogen) -- so "
          "ice, so cirrostratus. A tight coloured ring of 2 to 5°, white "
          "inside and red outside, is diffraction by water droplets -- so "
          "water, so altocumulus or thin stratus. The two can only be "
          "confused by someone who does not measure: a fist at arm's "
          "length covers about 8°, the halo lies well outside it, the "
          "corona far inside.\n\n"
          "**The grey of the base.** Grey is optical depth, and optical "
          "depth is liquid water path. **Altostratus** lets the sun "
          "through as a disc, but nothing casts a shadow any more -- that "
          "is the statement: middle level, a few hundred metres thick. "
          "Once the disc becomes unrecognisable and the base goes dark "
          "grey and rains, it is **nimbostratus**, and that one does not "
          "sit in a level at all but spans all three. **Cirrostratus**, by "
          "contrast, never extinguishes the disc and only softens "
          "the shadows.\n\n"
          "**The shadow.** The most reliable handle, because it computes "
          "instead of estimating. If the sun stands at elevation `h` and "
          "the cloud's shadow lies a distance `s` to the side of it on the "
          "ground, its base is at the height\n\n"
          r"$$z = s\,\tan h$$" "\n\n"
          "With $s = 2.5$ km and $h = 40^\\circ$ that is 2100 m. And that "
          "is the cross-check on the 125 m rule from fe-hebung: someone "
          "who measured 24 °C and a dew point of 12 °C at the ground "
          "expects his cumulus base at 1500 m. If the shadow gives 2100 m, "
          "then this cloud does **not** come from the surface layer -- it "
          "formed above an inversion, out of moister air higher up, and "
          "the 125 m rule does not apply to it.\n\n"
          "Finally the levels themselves, and the fact that they have no "
          "fixed numbers. The WMO grades them by latitude because the "
          "tropopause is graded by latitude: low everywhere 0 to 2 km; "
          "middle polar 2 to 4, temperate 2 to 7, tropical 2 to 8 km; high "
          "polar 3 to 8, temperate 5 to 13, tropical 6 to 18 km. The same "
          "cloud at the same height is called cirrus in Svalbard and "
          "altocumulus in Jakarta. The reason is in fe-hebung: moist "
          "convection sets the troposphere as high as it carries heat, and "
          "in the tropics it carries it 18 km up."),
        "wolkenbuch-stockwerke", [
        zahl(t("Der Schatten einer Wolke liegt 2500 m neben ihr, die Sonne "
               "steht 40° hoch. Wie hoch ist ihre Basis? (in m)",
               "A cloud's shadow lies 2500 m to the side of it, the sun "
               "stands 40° high. How high is its base? (in m)"),
             rund(WB_SCHATTEN_Z), t("m", "m"),
             t("`z = s·tan h = 2500 × tan 40° = 2500 × 0,839 = 2100 m`. "
               "Steht die Sonne tiefer, wird der Schatten länger und der "
               "Tangens kleiner -- das Produkt bleibt die Höhe.",
               "`z = s·tan h = 2500 × tan 40° = 2500 × 0.839 = 2100 m`. "
               "With a lower sun the shadow is longer and the tangent "
               "smaller -- the product stays the height."),
             toleranz=0.03),
        mc(t("Ein Cumulus in 1,5 km und ein Cirrus in 10 km Höhe ziehen "
             "mit fast derselben Winkelgeschwindigkeit über den Himmel. "
             "Warum?",
             "A cumulus at 1.5 km and a cirrus at 10 km sweep the sky at "
             "almost the same angular rate. Why?"),
           [t("Zufall -- Höhenwinde sind einfach sehr verschieden.",
              "Coincidence -- upper winds are simply very variable."),
            t("Weil der Wind wegen des thermischen Windes mit der Höhe "
              "ähnlich schnell wächst wie die Höhe selbst, und `U/z` "
              "deshalb stehen bleibt.",
              "Because the thermal wind makes the wind grow with height "
              "at about the same rate as the height itself, so `U/z` "
              "stays put."),
            t("Weil die Winkelgeschwindigkeit nicht von der Höhe abhängt.",
              "Because angular rate does not depend on height at all."),
            t("Weil Cirrus in Wirklichkeit viel tiefer hängt.",
              "Because cirrus actually hangs much lower.")], 1,
           t("16°/min gegen 14°/min: `7/1500` gegen `40/10000`. Das "
             "Verhältnis von Wind zu Höhe ist in der Troposphäre "
             "erstaunlich konstant, weil beide am Temperaturgefälle "
             "zwischen Pol und Äquator hängen (dy-thermisch). Deshalb "
             "taugt die Zuggeschwindigkeit nicht zum Schätzen des "
             "Stockwerks.",
             "16°/min against 14°/min: `7/1500` against `40/10000`. The "
             "ratio of wind to height is remarkably constant through the "
             "troposphere, because both hang on the pole-to-equator "
             "temperature gradient (dy-thermisch). That is why apparent "
             "speed is useless for guessing the level."),
           bild="cirrus"),
        mc(t("Um die Sonne steht ein enger bunter Ring von etwa 3°, innen "
             "weiß. In welcher Wolke stehen Sie?",
             "A tight coloured ring of about 3° surrounds the sun, white "
             "on the inside. What cloud are you looking through?"),
           [t("Cirrostratus -- das ist der 22°-Halo.",
              "Cirrostratus -- that is the 22° halo."),
            t("Cumulonimbus -- der Amboss streut.",
              "Cumulonimbus -- the anvil scatters."),
            t("Eine Wassertröpfchenwolke, Altocumulus oder dünner "
              "Stratus: 3° ist eine Korona, also Beugung, also "
              "Tropfen.",
              "A water droplet cloud, altocumulus or thin stratus: 3° is "
              "a corona, so diffraction, so droplets."),
            t("Nimbostratus -- Regen bricht das Licht.",
              "Nimbostratus -- rain refracts the light.")], 2,
           t("Beugung macht enge Ringe (Faust am ausgestreckten Arm = 8°, "
             "die Korona liegt weit innerhalb), Brechung im Eisprisma "
             "macht den weiten 22°-Ring. Die Korona ist also der "
             "Phasentest: Tröpfchen, kein Eis.",
             "Diffraction makes tight rings (a fist at arm's length = 8°, "
             "the corona lies far inside it), refraction in the ice prism "
             "makes the wide 22° ring. The corona is therefore the phase "
             "test: droplets, not ice.")),
        ]),

    lektion("wb-arten",
        t("Arten und Beinamen: das Bestimmungsschema",
          "Species and varieties: the key"),
        ["wolkenarten", "unterarten", "undulatus", "ballenwinkel"],
        t("Die Gattung ist der Nachname, die **Art** der Vorname -- und "
          "erst der Vorname sagt, was gerade passiert. Die WMO kennt "
          "vierzehn Arten, und jede ist die Aussage über einen Prozess. "
          "Wer sie liest, braucht keinen Wetterbericht für die nächste "
          "Stunde.\n\n"
          "**Beim Cumulus** steht die Art für das Verhältnis von Höhe zu "
          "Breite, also für die Stärke des Auftriebs: *humilis* breiter "
          "als hoch (Deckel kurz über der Basis), *mediocris* etwa so hoch "
          "wie breit, *congestus* höher als breit mit Blumenkohlrändern "
          "(kein Deckel mehr, der Turm nimmt sich, was die CAPE aus "
          "fe-emagram hergibt), *fractus* zerrissen ohne flache Basis "
          "(kein Kondensationsniveau mehr -- die Luft ist nicht mehr "
          "durchmischt, sondern turbulent).\n\n"
          "**Beim Cirrus** steht die Art für die Scherung. *fibratus* sind "
          "gerade Fasern ohne Haken: Die Kristalle fallen, aber der Wind "
          "ändert sich mit der Höhe nicht. *uncinus*, der Haken, ist "
          "genau diese Änderung: Der Kristall fällt aus seinem "
          "Entstehungsniveau in langsamere Luft darunter und bleibt "
          "zurück, der Fallstreifen krümmt sich -- ein Scherungsmesser aus "
          "Eis. *spissatus* ist dick und grau, meist der übrig gebliebene "
          "Amboss eines Gewitters von gestern.\n\n"
          "**Im Mittelstockwerk** trägt die Art die ganze Information: "
          "*stratiformis* heißt Hebung einer ganzen Schicht, *lenticularis* "
          "die stehende glatte Linse (laminare Welle, also sehr stabile "
          "Schichtung -- durchgerechnet in me-foehn), *castellanus* "
          "Türmchen auf gemeinsamer Basis (Labilität **in** dieser Höhe, "
          "das klassische Gewitterzeichen am Morgen), *floccus* "
          "flockenartig mit zerfaserter Unterseite (dieselbe Labilität, "
          "schon weiter: die Flocken regnen in sich hinein).\n\n"
          "Darunter die **Unterarten**, die nicht die Wolke, sondern das "
          "Feld beschreiben: *undulatus* in Wellen, *radiatus* in "
          "parallelen Bändern längs des Windes, *duplicatus* in zwei "
          "übereinanderliegenden Lagen, *perlucidus* mit Lücken, durch die "
          "man den Himmel sieht, *translucidus* so dünn, dass die Sonne "
          "durchkommt, *opacus* nicht mehr. Die Regel dahinter ist knapp: "
          "**-cumuliformis heißt Auftrieb von unten, -stratiformis heißt "
          "Hebung einer Schicht, undulatus heißt Welle an einer "
          "Sprungschicht.**\n\n"
          "Zwei Zahlen, mit denen man bestimmt, statt zu raten. Die erste "
          "ist der **Ballenwinkel**, und sie ist die amtliche "
          "Unterscheidung zwischen drei Gattungen, die gleich aussehen: "
          "Cirrocumulus hat Ballen unter 1°, Altocumulus 1 bis 5°, "
          "Stratocumulus über 5°. Man hält den kleinen Finger an "
          "ausgestrecktem Arm hoch -- er deckt etwa 1°. Ein Ballen von "
          "600 m Durchmesser in 6 km Höhe erscheint unter "
          "`arctan(600/6000) = 5,7°`: Bei dieser Größe ist die "
          "Wolke also tief, nicht mittelhoch, und man hat eben die "
          "Entfernung gemessen, ohne sie zu kennen.\n\n"
          "Die zweite ist die **Wellenlänge einer undulatus-Reihe**. Eine "
          "Welle an einer stabilen Sprungschicht steht still, wenn ihre "
          "Phasengeschwindigkeit den Wind aufhebt; das Paket schwingt mit "
          "der Brunt-Väisälä-Frequenz `N` und wird dabei mit `U` "
          "weitergetragen, also $\\lambda = 2\\pi U/N$ -- dieselbe "
          "Gleichung, die in th-stabilitaet den Abstand der "
          "Lenticularis-Wolken hinter einem Gebirgskamm liefert. Mit "
          "$U = 15$ m/s und $N = 0{,}011$ /s kommen 8,6 km heraus. Und das "
          "ist überprüfbar: Zählt man die Wellenberge einer "
          "Altocumulus-undulatus-Reihe über eine bekannte Strecke -- zwei "
          "Ortschaften, deren Abstand man weiß --, kommt man auf einige "
          "Kilometer je Welle und hat damit die Schichtungsstabilität "
          "mehrere Kilometer über sich gemessen, vom Boden aus, mit den "
          "Augen.",
          "The genus is the surname, the **species** the given name -- and "
          "only the given name says what is happening right now. The WMO "
          "lists fourteen species, and each one is a statement about a "
          "process. Whoever reads them needs no forecast for the next "
          "hour.\n\n"
          "**For cumulus** the species gives the ratio of height to "
          "width, hence the strength of the updraught: *humilis* wider "
          "than tall (a lid just above the base), *mediocris* about as "
          "tall as wide, *congestus* taller than wide with cauliflower "
          "edges (no lid left, the tower takes whatever CAPE from "
          "fe-emagram allows), *fractus* ragged with no flat base at all "
          "(no condensation level any more -- the air is no longer mixed "
          "but turbulent).\n\n"
          "**For cirrus** the species gives the shear. *fibratus* are "
          "straight fibres without hooks: the crystals fall, but the wind "
          "does not change with height. *uncinus*, the hook, is precisely "
          "that change: the crystal drops out of the level where it formed "
          "into slower air below and lags behind, so the fallstreak bends "
          "-- a shear meter made of ice. *spissatus* is thick and grey, "
          "usually the leftover anvil of yesterday's thunderstorm.\n\n"
          "**At middle level** the species carries all of the information: "
          "*stratiformis* means the lifting of a whole layer, "
          "*lenticularis* the smooth standing lens (a laminar wave, hence "
          "very stable stratification -- worked through in me-foehn), "
          "*castellanus* turrets on a common base (instability **at** that "
          "height, the classic morning sign of thunderstorms), *floccus* "
          "tufts with a frayed underside (the same instability, one step "
          "on: the tufts are raining into themselves).\n\n"
          "Below that the **varieties**, which describe not the cloud but "
          "the field: *undulatus* in waves, *radiatus* in parallel bands "
          "along the wind, *duplicatus* in two layers one above the other, "
          "*perlucidus* with gaps that show the sky, *translucidus* thin "
          "enough for the sun to come through, *opacus* no longer. The "
          "rule behind it is short: **-cumuliformis means buoyancy from "
          "below, -stratiformis means the lifting of a layer, undulatus "
          "means a wave on a stable interface.**\n\n"
          "Two numbers with which one identifies rather than guesses. The "
          "first is the **element angle**, and it is the official "
          "distinction between three genera that look alike: cirrocumulus "
          "has elements below 1°, altocumulus 1 to 5°, stratocumulus above "
          "5°. Hold up your little finger at arm's length -- it covers "
          "about 1°. An element 600 m across at 6 km appears at "
          "`arctan(600/6000) = 5.7°`: at that apparent size the "
          "cloud is low, not mid-level, and you have just measured a "
          "distance without knowing it.\n\n"
          "The second is the **wavelength of an undulatus train**. A wave "
          "on a stable interface stands still when its phase speed "
          "cancels the wind; the parcel oscillates at the Brunt-Väisälä "
          "frequency `N` while being carried along at `U`, hence "
          "$\\lambda = 2\\pi U/N$ -- the same equation that in "
          "th-stabilitaet gives the spacing of lenticular clouds behind a "
          "ridge. With $U = 15$ m/s and $N = 0.011$ /s that comes to "
          "8.6 km. And it is checkable: count the wave crests of an "
          "altocumulus undulatus train across a known distance -- two "
          "villages whose separation you know -- and you arrive at a few "
          "kilometres per wave, having thereby measured the stability of "
          "the stratification several kilometres above you, from the "
          "ground, with your eyes."),
        "lenticularis", [
        zahl(t("Eine Altocumulus-undulatus-Reihe steht in einer Schicht "
               "mit N = 0,011 /s, der Wind dort weht mit 15 m/s. "
               "Wellenlänge nach λ = 2πU/N? (in km, eine "
               "Nachkommastelle)",
               "An altocumulus undulatus train sits in a layer with "
               "N = 0.011 /s, where the wind blows at 15 m/s. Wavelength "
               "from λ = 2πU/N? (in km, one decimal)"),
             rund(WB_UNDULATUS / 1000.0, 1), t("km", "km"),
             t("`λ = 2π × 15 / 0,011 = 8570 m`. Dieselbe Rechnung wie für "
               "Lee-Wellen in th-stabilitaet; nur steht die Sprungschicht "
               "hier nicht hinter einem Berg, sondern im freien "
               "Luftraum.",
               "`λ = 2π × 15 / 0.011 = 8570 m`. The same calculation as "
               "for lee waves in th-stabilitaet; only here the interface "
               "is not behind a mountain but free in the air."),
             toleranz=0.04),
        mc(t("Morgens um 8 Uhr stehen im Mittelstockwerk Türmchen auf "
             "gemeinsamer Basis -- Altocumulus castellanus. Was folgt "
             "daraus für den Nachmittag?",
             "At 8 in the morning there are turrets on a common base at "
             "middle level -- altocumulus castellanus. What follows for "
             "the afternoon?"),
           [t("Die Luft in 3 bis 5 km ist labil geschichtet; erreicht die "
              "Bodenkonvektion diese Höhe, wächst sie durch -- Gewitter "
              "am Nachmittag.",
              "The air at 3 to 5 km is unstably stratified; once surface "
              "convection reaches that height it keeps going -- "
              "thunderstorms in the afternoon."),
            t("Beständiges Hochdruckwetter, die Türmchen sind "
              "Absinken.",
              "Settled high pressure; the turrets are subsidence."),
            t("Eine Warmfront in sechs Stunden.",
              "A warm front in six hours."),
            t("Nichts -- die Art sagt nur etwas über das Aussehen.",
              "Nothing -- the species only describes appearance.")], 0,
           t("Die Türmchen sind Auftrieb, und Auftrieb in 4 km heißt "
             "$d\\theta/dz < 0$ in 4 km. Der Deckel liegt dann nicht über, "
             "sondern unter der labilen Schicht: Was dort hineinstößt, "
             "steigt weiter. Im Emagramm (fe-emagram) sieht man dieselbe "
             "Aussage als Umgebungskurve, die steiler als die "
             "Feuchtadiabate verläuft.",
             "The turrets are buoyancy, and buoyancy at 4 km means "
             "$d\\theta/dz < 0$ at 4 km. The lid then lies below, not "
             "above, the unstable layer: whatever pushes into it keeps "
             "rising. On the emagram (fe-emagram) the same statement "
             "appears as an environmental curve steeper than the moist "
             "adiabat."),
           bild="ac-castellanus"),
        mc(t("Cirrus uncinus: Woher kommt der Haken am Ende der Faser?",
             "Cirrus uncinus: where does the hook at the end of the fibre "
             "come from?"),
           [t("Aus dem Gefrieren der Tropfen.",
              "From the freezing of droplets."),
            t("Aus der Scherung: Der fallende Kristall gerät in langsamere "
              "Luft unter seinem Entstehungsniveau und bleibt zurück.",
              "From shear: the falling crystal enters slower air below the "
              "level where it formed and lags behind."),
            t("Aus der Coriolis-Kraft am einzelnen Kristall.",
              "From the Coriolis force on the individual crystal."),
            t("Aus einer Welle im Höhenwind.",
              "From a wave in the upper wind.")], 1,
           t("Der Kopf der Faser ist das Entstehungsniveau, der Schweif "
             "der Fallstreifen. Seine Krümmung ist $du/dz$, mit dem Auge "
             "gelesen: ein starker Haken heißt starke Scherung, und "
             "starke Scherung in der Höhe heißt Jetstream in der Nähe. "
             "Cirrus fibratus ohne Haken heißt umgekehrt, dass sich der "
             "Wind über diese Schicht kaum ändert.",
             "The head of the fibre is the level where it formed, the "
             "tail is the fallstreak. Its curvature is $du/dz$, read by "
             "eye: a strong hook means strong shear, and strong shear "
             "aloft means a jet stream nearby. Cirrus fibratus without "
             "hooks conversely means the wind hardly changes across that "
             "layer.")),
        ]),

    lektion("wb-sonderformen",
        t("Sonderformen: mammatus, pileus, incus, virga",
          "Supplementary features: mammatus, pileus, incus, virga"),
        ["sonderformen", "mammatus", "pileus", "virga"],
        t("Die dritte Ebene unter Gattung und Art sind die "
          "**Sonderformen** und die **Begleitwolken** -- und sie sind die "
          "interessanteste, weil jede einzelne der sichtbare Abdruck eines "
          "Mechanismus ist, den der Kurs schon hergeleitet hat.\n\n"
          "**incus**, der Amboss. Der Turm steigt, bis er in eine Schicht "
          "kommt, in der die Temperatur mit der Höhe nicht mehr fällt: die "
          "Tropopause. Dort ist $N^2$ groß (th-stabilitaet), der Auftrieb "
          "kehrt sich um, und die Luft kann nur noch seitlich weg. Die "
          "flache Oberkante ist also ein direkt sichtbarer Höhenmesser -- "
          "sie liegt in gemäßigten Breiten bei 11 km, in den Tropen bei "
          "16. Schießt in der Mitte noch eine Kuppel darüber hinaus "
          "(eine überschießende Kuppel, *overshooting top*), dann hat "
          "der Aufwind mehr Schwung als der Deckel Widerstand -- das ist "
          "das Zeichen für eine schwere Zelle.\n\n"
          "**pileus**, die Mütze. Über der Spitze eines schnell steigenden "
          "Turms liegt eine glatte, dünne, linsenförmige Kappe, die der "
          "Turm Minuten später durchstößt und auffrisst. Sie entsteht, "
          "weil der Turm die **feuchte Schicht über sich** anhebt wie ein "
          "Kolben, und diese Schicht erreicht ihr Kondensationsniveau, "
          "bevor der Turm sie erreicht. Der pileus steht also genau am "
          "LCL der gehobenen Schicht (fe-hebung) und ist Hebung, bevor "
          "etwas da ist, das hebt. Ein pileus heißt: Dieser Turm ist "
          "schnell, und über ihm ist es feucht -- er wird weiterwachsen. "
          "Liegt die Kappe als dünner Schleier an der Seite statt oben, "
          "heißt sie *velum*.\n\n"
          "**mammatus**, die Beutel. An der Unterseite des Amboss hängen "
          "glatte, runde Säcke. Sie sind kein Aufwind, sondern das "
          "Gegenteil: In der trockenen Luft unter dem Amboss sublimieren "
          "die herausfallenden Eiskristalle, der Entzug der "
          "Sublimationswärme kühlt diese Luft, sie wird schwerer als ihre "
          "Umgebung und sinkt in Blasen. Der Auftrieb ist $b = g\\,\\Delta "
          "T/T$; bei 2 K Unterkühlung und 280 K sind das 0,070 m/s², "
          "0,7 % von `g`. Über 500 m Fallhöhe gäbe das $v = \\sqrt{2bh} = "
          "8{,}4$ m/s -- in Wirklichkeit weniger, weil die Blase mischt. "
          "Die Zahl erklärt aber das Aussehen: So sanft, dass die Beutel "
          "rund und glatt bleiben, statt zu zerreißen.\n\n"
          "**virga**, die Fallstreifen, die den Boden nicht erreichen. "
          "Unter der Basis hängen schräge Schleier, die in der Luft "
          "aufhören. Wie weit kommt ein Tropfen? Verdunsten ist "
          "Diffusionswachstum mit negativer Übersättigung, also dieselbe "
          "Gleichung wie in wo-wachstum, nur rückwärts: $r^2 = r_0^2 - "
          "2\\xi|S|t$. Ein Tropfen von 100 μm in Luft mit 50 % "
          "Untersättigung ist nach $t = r_0^2/(2\\xi|S|) = 167$ s "
          "verschwunden. Seine Fallgeschwindigkeit ist in diesem Bereich "
          "0,7 m/s (Stokes gilt da schon nicht mehr -- $Re \\approx 10$, "
          "und wo-wachstum rechnet den Wert vor), also kommt er rund "
          "120 m. Genau das ist die beobachtete Länge eines "
          "Fallstreifens, und genau deshalb erreicht Nieseln nur aus "
          "tiefen Wolken den Boden.\n\n"
          "Der Rest des Katalogs in je einem Satz. **praecipitatio**: der "
          "Niederschlag kommt an, der Streifen schließt bis zum Boden. "
          "**arcus**, die Böenwalze: Die ausfließende Kaltluft hebt an ihrer Vorderkante "
          "die warme Luft, und die kondensiert über der Front -- die Walze "
          "markiert die Kaltluftgrenze, nicht die Wolke. **murus** und "
          "**tuba**: die rotierende Wandwolke und der Schlauch darunter, "
          "sichtbar gemachte Drehung. **asperitas**: eine chaotisch "
          "gewellte Unterseite, meist unter einer zerfallenden "
          "Stratocumulus-Decke mit Scherung darin. **cavum**: das runde "
          "Loch in einer unterkühlten Altocumulus-Schicht, in dem ein "
          "Flugzeug oder ein Kristallschauer das Wasser auf einmal in Eis "
          "umgewandelt hat -- Bergeron-Findeisen in einem Zug, mit einem "
          "Fallstreifen in der Mitte.",
          "The third level below genus and species are the "
          "**supplementary features** and **accessory clouds** -- and they "
          "are the most interesting one, because each single one is the "
          "visible imprint of a mechanism the course has already "
          "derived.\n\n"
          "**incus**, the anvil. The tower rises until it reaches a layer "
          "in which temperature no longer falls with height: the "
          "tropopause. There $N^2$ is large (th-stabilitaet), the buoyancy "
          "reverses, and the air can only go sideways. The flat top is "
          "therefore a directly visible altimeter -- it sits at 11 km in "
          "midlatitudes and at 16 km in the tropics. If a dome still "
          "pushes through it in the middle (an overshooting top), the "
          "updraught has more momentum than the lid has resistance -- the "
          "sign of a severe cell.\n\n"
          "**pileus**, the cap. Above the top of a fast-rising tower lies "
          "a smooth, thin, lens-shaped cap which the tower punches through "
          "and eats minutes later. It forms because the tower lifts the "
          "**moist layer above itself** like a piston, and that layer "
          "reaches its condensation level before the tower reaches the "
          "layer. So the pileus stands exactly at the LCL of the lifted "
          "layer (fe-hebung) and is lifting made visible before there is "
          "anything there doing the lifting. A pileus says: this tower is "
          "fast, and it is moist above it -- it will keep growing. If the "
          "cap lies as a thin veil to the side instead of on top, it is "
          "called *velum*.\n\n"
          "**mammatus**, the pouches. Smooth round sacks hang from the "
          "underside of the anvil. They are not updraught but the "
          "opposite: in the dry air below the anvil the ice crystals "
          "falling out of it sublime, the withdrawal of the heat of "
          "sublimation cools that air, it becomes heavier than its "
          "surroundings and sinks in bubbles. The buoyancy is "
          "$b = g\\,\\Delta T/T$; at 2 K of cooling and 280 K that is "
          "0.070 m/s², 0.7 % of `g`. Over 500 m of descent that would give "
          "$v = \\sqrt{2bh} = 8.4$ m/s -- less in reality, because the "
          "bubble mixes. But the number explains the look: gentle enough "
          "that the pouches stay round and smooth instead of tearing "
          "apart.\n\n"
          "**virga**, the fallstreaks that never reach the ground. "
          "Slanting veils hang below the base and stop in mid-air. How far "
          "does a drop get? Evaporation is diffusional growth with "
          "negative supersaturation, so the same equation as in "
          "wo-wachstum, only backwards: $r^2 = r_0^2 - 2\\xi|S|t$. A drop "
          "of 100 μm in air 50 % subsaturated is gone after "
          "$t = r_0^2/(2\\xi|S|) = 167$ s. Its fall speed in that size "
          "range is 0.7 m/s (Stokes has already broken down there -- "
          "$Re \\approx 10$, and wo-wachstum works the value out), so it "
          "gets about 120 m. That is exactly the observed length of a "
          "fallstreak, and exactly why drizzle only reaches the ground "
          "from low clouds.\n\n"
          "The rest of the catalogue in one sentence each. "
          "**praecipitatio**: the precipitation arrives, the streak closes "
          "down to the ground. **arcus**, the shelf: the outflowing cold "
          "air lifts the warm air at its leading edge, and that condenses "
          "above the front -- the roll marks the edge of the cold air, not "
          "the cloud. **murus** and **tuba**: the rotating wall cloud and "
          "the funnel below it, rotation made visible. **asperitas**: a "
          "chaotically wavy underside, usually below a decaying "
          "stratocumulus deck with shear in it. **cavum**: the round hole "
          "in a supercooled altocumulus layer, where an aircraft or a "
          "shower of crystals turned the water into ice all at once -- "
          "Bergeron-Findeisen in one go, with a fallstreak in the "
          "middle."),
        "wolkenbuch-sonderformen", [
        zahl(t("Mammatus: Die absinkende Luft unter dem Amboss ist 2 K "
               "kälter als ihre Umgebung bei 280 K. Negativer Auftrieb "
               "b = g·ΔT/T? (in m/s², drei Nachkommastellen)",
               "Mammatus: the sinking air below the anvil is 2 K colder "
               "than its surroundings at 280 K. Negative buoyancy "
               "b = g·ΔT/T? (in m/s², three decimals)"),
             rund(WB_MAMMATUS_B, 3), t("m/s²", "m/s²"),
             t("`9,81 × 2 / 280 = 0,070 m/s²`, also 0,7 % von `g`. "
               "Dieselbe Formel, mit der th-stabilitaet den Auftrieb "
               "eines gehobenen Pakets ansetzt -- nur mit umgekehrtem "
               "Vorzeichen, weil hier gekühlt und nicht erwärmt wird.",
               "`9.81 × 2 / 280 = 0.070 m/s²`, i.e. 0.7 % of `g`. The "
               "same expression th-stabilitaet uses for the buoyancy of a "
               "lifted parcel -- only with the opposite sign, because "
               "here the air is cooled, not warmed."),
             toleranz=0.05),
        zahl(t("Ein Tropfen von 100 μm Radius fällt mit 0,7 m/s in Luft "
               "mit 50 % Untersättigung (ξ = 6·10⁻¹³ m²/s je Prozent). "
               "Wie lang wird sein Fallstreifen? (in m)",
               "A drop of 100 μm radius falls at 0.7 m/s through air 50 % "
               "subsaturated (ξ = 6·10⁻¹³ m²/s per per cent). How long "
               "does its fallstreak become? (in m)"),
             rund(WB_VIRGA_WEG), t("m", "m"),
             t("`t = r₀²/(2ξ|S|) = 10⁻⁸/(2 × 6·10⁻¹³ × 50) = 167 s`, "
               "mal 0,7 m/s sind 117 m. Die Gleichung ist das "
               "Diffusionswachstum aus wo-wachstum mit negativem `S`; "
               "beachtlich ist, wie gut die 100 bis 300 m herauskommen, "
               "die man unter einer Wolke sieht.",
               "`t = r₀²/(2ξ|S|) = 10⁻⁸/(2 × 6·10⁻¹³ × 50) = 167 s`, "
               "times 0.7 m/s is 117 m. The equation is the diffusional "
               "growth of wo-wachstum with negative `S`; what is "
               "remarkable is how well it reproduces the 100 to 300 m one "
               "sees below a cloud."),
             toleranz=0.05),
        mc(t("Über der Spitze eines schnell wachsenden Cumulus congestus "
             "liegt eine glatte Kappe, die er zwei Minuten später "
             "durchstößt. Was ist das?",
             "A smooth cap lies above the top of a fast-growing cumulus "
             "congestus, which punches through it two minutes later. What "
             "is it?"),
           [t("Eine Inversion, die den Turm deckelt.",
              "An inversion capping the tower."),
            t("Der vereiste Teil des Turms.",
              "The glaciated part of the tower."),
            t("Hochnebel, der zufällig darüber liegt.",
              "High fog that happens to lie above it."),
            t("Ein pileus: Der Turm hebt die feuchte Schicht über sich "
              "wie ein Kolben, und die erreicht ihr LCL, bevor der Turm "
              "sie erreicht.",
              "A pileus: the tower lifts the moist layer above itself "
              "like a piston, and that layer reaches its LCL before the "
              "tower reaches it.")], 3,
           t("Deshalb ist der pileus ein Vorzeichen, kein Hindernis: Er "
             "beweist, dass der Aufwind schnell ist (sonst würde die "
             "Schicht seitlich ausweichen statt zu kondensieren) und dass "
             "es darüber feucht ist. Beides heißt: Der Turm wächst "
             "weiter.",
             "That is why the pileus is an omen, not an obstacle: it "
             "proves that the updraught is fast (otherwise the layer "
             "would slip sideways instead of condensing) and that it is "
             "moist above. Both mean the tower will keep growing."),
           bild="cu-congestus"),
        ]),

    lektion("wb-kondensstreifen",
        t("Kondensstreifen: was ein Flugzeug über 10 km verrät",
          "Contrails: what an aircraft gives away about 10 km up"),
        ["kondensstreifen", "mischungsgerade", "schmidt-appleman",
         "eisuebersaettigung"],
        t("Zwei Flugzeuge in derselben Höhe, und hinter dem einen reißt "
          "der Streifen nach drei Flugzeuglängen ab, während der andere "
          "einen weißen Strich über den halben Himmel zieht, der in einer "
          "halben Stunde zu einem breiten Band auseinanderfließt. Beide "
          "haben dieselben Triebwerke. Der Unterschied steht nicht im "
          "Flugzeug, sondern in der Luft, und man kann ihn vom Boden aus "
          "ablesen.\n\n"
          "Zuerst, warum überhaupt etwas entsteht. Das Abgas ist heiß "
          "(600 K) und sehr feucht (Kerosin verbrennt zu Wasser: 1,25 kg "
          "Wasser je kg Treibstoff), die Umgebung ist kalt (−50 °C) und "
          "trocken. Beim Mischen gehen Temperatur **und** Dampfdruck "
          "linear mit dem Mischungsanteil -- beides sind Erhaltungsgrößen "
          "je Masse. Der Zustand der Mischung läuft deshalb im "
          "$(T, e)$-Diagramm auf einer **Geraden** zwischen den beiden "
          "Endpunkten. Die Sättigungskurve $e_s(T)$ aus fe-dampf ist "
          "dagegen **konvex** -- sie ist exponentiell. Und eine Sehne "
          "zwischen zwei Punkten unter einer konvexen Kurve kann über "
          "ihnen liegen: Die Mischung ist übersättigt, obwohl keiner der "
          "beiden Ausgangszustände es war. Nebel aus dem Auspuff, aus dem "
          "Atem an kalter Luft, über dem offenen Wasser im Winter -- "
          "immer dieselbe Figur.\n\n"
          "Die Steigung der Geraden hängt nur am Treibstoff und am Druck:\n\n"
          r"$$G = \frac{EI\,c_p\,p}{\varepsilon\,Q\,(1-\eta)}$$" "\n\n"
          "mit dem Emissionsindex $EI = 1{,}25$, dem Heizwert "
          "$Q = 43$ MJ/kg, $\\varepsilon = 0{,}622$ und dem "
          "Vortriebswirkungsgrad $\\eta \\approx 0{,}3$ (der Anteil der "
          "Energie, der als Schub weggeht statt die Luft zu heizen -- "
          "daher $1 - \\eta$). Bei 250 hPa sind das 1,68 Pa/K. Die "
          "**Schmidt-Appleman-Bedingung** ist nun, dass diese Gerade die "
          "Sättigungskurve überhaupt erreicht, und der Grenzfall ist die "
          "Berührung: $de_s/dT = G$. Mit der Magnus-Formel liegt dieser "
          "Punkt bei **−41,7 °C**, in der Standardatmosphäre (at-standard) "
          "also bei 8,7 km. Darunter ist es zu warm: Kein Triebwerk macht "
          "dort einen Streifen, wie feucht die Luft auch sei. Darüber "
          "macht jedes einen -- wenigstens kurz.\n\n"
          "Jetzt der Teil, der fürs Hinsehen zählt. Ob der Streifen "
          "**bleibt**, entscheidet nicht die Schmidt-Appleman-Bedingung, "
          "sondern die Umgebungsfeuchte. Die Eiskristalle verdunsten, "
          "sobald die Luft gegenüber **Eis** untersättigt ist; bei "
          "−45 °C liegt $e_s$ über Eis bei nur 65 % des Werts über Wasser "
          "(derselbe Bergeron-Unterschied wie in wo-wachstum, nur "
          "größer, weil es kälter ist). Eine Umgebung mit 70 % relativer "
          "Feuchte über Wasser ist dort also längst übersättigt gegenüber "
          "Eis -- es genügen 65 %. Und eine solche Luftmasse ist dabei, von selbst Cirrus zu "
          "bilden.\n\n"
          "Damit ist der Kondensstreifen ein Feuchtigkeitsmessgerät in "
          "10 km Höhe, das man geschenkt bekommt. **Kurzer Stummel**, der "
          "nach Sekunden abreißt: Die Höhenluft ist trocken, kein Cirrus "
          "zu erwarten, und wenn ein Hoch darüber liegt, hält das Wetter. "
          "**Langer, beständiger Streifen**, der sich verbreitert und nach "
          "einer Stunde noch da ist: eisübersättigt -- die Vorlaufzone "
          "einer Warmfront, nach wo-gattungen 12 bis 24 Stunden voraus, "
          "noch bevor der erste natürliche Cirrus steht. **Viele Streifen, "
          "die zu einem Schleier verschmelzen**: Cirrostratus auf Vorrat, "
          "der Halo kommt heute noch. **Streifen, die sich quer "
          "verbreitern und dabei kippen**: Das ist die Scherung $du/dz$, "
          "wie beim uncinus-Haken -- nur gerade und mit bekannter "
          "Entstehungszeit, also messbar.\n\n"
          "Ein ehrlicher Nachsatz: Aus derselben Rechnung folgt, dass "
          "Kondensstreifen-Cirrus den Strahlungshaushalt verschiebt -- er "
          "lässt die Sonne durch und hält die Infrarotstrahlung zurück "
          "(st-bilanz, st-treibhaus), also wärmt er netto, und zwar "
          "nachts am stärksten, weil dann der kurzwellige Anteil fehlt.",
          "Two aircraft at the same altitude, and behind one the trail "
          "breaks off after three fuselage lengths while the other draws a "
          "white line across half the sky that spreads into a broad band "
          "within half an hour. Both have the same engines. The difference "
          "is not in the aircraft but in the air, and it can be read off "
          "from the ground.\n\n"
          "First, why anything forms at all. The exhaust is hot (600 K) "
          "and very moist (kerosene burns to water: 1.25 kg of water per "
          "kg of fuel), the surroundings are cold (−50 °C) and dry. On "
          "mixing, temperature **and** vapour pressure both go linearly "
          "with the mixing fraction -- both are conserved quantities per "
          "unit mass. The state of the mixture therefore runs along a "
          "**straight line** in the $(T, e)$ plane between the two end "
          "points. The saturation curve $e_s(T)$ from fe-dampf, by "
          "contrast, is **convex** -- it is exponential. And a chord "
          "between two points below a convex curve can lie above it: the "
          "mixture is supersaturated although neither of the two original "
          "states was. Fog from an exhaust pipe, from your breath in cold "
          "air, over open water in winter -- always the same figure.\n\n"
          "The slope of the line depends only on the fuel and the "
          "pressure:\n\n"
          r"$$G = \frac{EI\,c_p\,p}{\varepsilon\,Q\,(1-\eta)}$$" "\n\n"
          "with the emission index $EI = 1.25$, the heating value "
          "$Q = 43$ MJ/kg, $\\varepsilon = 0.622$ and the propulsion "
          "efficiency $\\eta \\approx 0.3$ (the fraction of the energy "
          "that leaves as thrust instead of heating the air -- hence "
          "$1 - \\eta$). At 250 hPa that comes to 1.68 Pa/K. The "
          "**Schmidt-Appleman condition** is now that this line reaches "
          "the saturation curve at all, and the limiting case is tangency: "
          "$de_s/dT = G$. With the Magnus formula that point lies at "
          "**−41.7 °C**, hence in the standard atmosphere (at-standard) at "
          "8.7 km. Below that it is too warm: no engine makes a trail "
          "there, however moist the air. Above it every engine makes one "
          "-- at least briefly.\n\n"
          "Now the part that matters for looking. Whether the trail "
          "**stays** is decided not by the Schmidt-Appleman condition but "
          "by the ambient humidity. The ice crystals evaporate as soon as "
          "the air is subsaturated with respect to **ice**; at −45 °C "
          "$e_s$ over ice is only 65 % of the value over water (the same "
          "Bergeron difference as in wo-wachstum, only larger because it "
          "is colder). So a surrounding air mass at 70 % relative humidity "
          "over water is well past saturation with respect to ice -- 65 % "
          "is enough. And "
          "such an air mass is on its way to making cirrus by itself.\n\n"
          "That makes a contrail a free humidity instrument at 10 km. "
          "**A short stub** that breaks off after seconds: the upper air "
          "is dry, no cirrus to expect, and if a high sits above, the "
          "weather holds. **A long persistent trail** that spreads and is "
          "still there an hour later: ice-supersaturated -- the leading "
          "zone of a warm front, by wo-gattungen 12 to 24 hours ahead, "
          "before the first natural cirrus even stands there. **Many "
          "trails merging into a veil**: cirrostratus in advance, the halo "
          "will arrive today. **Trails that widen sideways and tilt at the "
          "same time**: that is the shear $du/dz$, as with the uncinus "
          "hook -- only straight and with a known starting time, hence "
          "measurable.\n\n"
          "An honest postscript: the same calculation implies that "
          "contrail cirrus shifts the radiation budget -- it lets the sun "
          "through and holds the infrared back (st-bilanz, st-treibhaus), "
          "so it warms on balance, and most strongly at night, when the "
          "short-wave part is missing."),
        "wolkenbuch-kondensstreifen", [
        zahl(t("Steigung der Mischungsgerade in 250 hPa: EI = 1,25, "
               "c_p = 1004 J/(kg K), ε = 0,622, Q = 43 MJ/kg, η = 0,30. "
               "G = EI·c_p·p/(ε·Q·(1−η))? (in Pa/K, zwei "
               "Nachkommastellen)",
               "Slope of the mixing line at 250 hPa: EI = 1.25, "
               "c_p = 1004 J/(kg K), ε = 0.622, Q = 43 MJ/kg, η = 0.30. "
               "G = EI·c_p·p/(ε·Q·(1−η))? (in Pa/K, two decimals)"),
             rund(WB_G_APPLEMAN, 2), t("Pa/K", "Pa/K"),
             t("`1,25 × 1004 × 25000 / (0,622 × 43·10⁶ × 0,70) = "
               "3,14·10⁷ / 1,87·10⁷ = 1,68 Pa/K`. In 200 hPa ist G "
               "kleiner, die Gerade flacher -- deshalb genügt dort eine "
               "noch wärmere Umgebung nicht, und die Schwelle wandert "
               "mit der Flughöhe.",
               "`1.25 × 1004 × 25000 / (0.622 × 43·10⁶ × 0.70) = "
               "3.14·10⁷ / 1.87·10⁷ = 1.68 Pa/K`. At 200 hPa G is "
               "smaller and the line flatter -- so an even warmer "
               "environment will not do there, and the threshold moves "
               "with flight level."),
             toleranz=0.04),
        mc(t("Weder das Abgas noch die Umgebungsluft ist gesättigt -- "
             "warum entsteht beim Mischen trotzdem eine Wolke?",
             "Neither the exhaust nor the ambient air is saturated -- why "
             "does mixing nevertheless make a cloud?"),
           [t("Weil der Druck im Nachstrom des Triebwerks fällt.",
              "Because the pressure falls in the engine's wake."),
            t("Weil beim Mischen T und e linear laufen, die Kurve "
              "$e_s(T)$ aber konvex ist: Die Sehne kann über der Kurve "
              "liegen.",
              "Because T and e both run linearly on mixing while the "
              "curve $e_s(T)$ is convex: the chord can lie above the "
              "curve."),
            t("Weil die Abgaspartikel die Oberflächenspannung "
              "aufheben.",
              "Because the exhaust particles cancel the surface "
              "tension."),
            t("Weil der Wasserdampf des Abgases schwerer ist als "
              "Luft.",
              "Because the water vapour in the exhaust is heavier than "
              "air.")], 1,
           t("Das ist derselbe Satz, der den Mischungsnebel über offenem "
             "Wasser erklärt: Zwei Zustände unter einer konvexen Kurve, "
             "gemischt, liegen darüber. Die Kerne aus dem Russ "
             "(wo-tropfen) senken dann noch die Kelvin-Schwelle, aber "
             "nötig ist sie nicht -- nötig ist die Konvexität von "
             "$e_s(T)$, also Clausius-Clapeyron.",
             "This is the same statement that explains mixing fog over "
             "open water: two states below a convex curve, mixed, lie "
             "above it. The soot nuclei (wo-tropfen) then lower the "
             "Kelvin threshold as well, but they are not necessary -- "
             "what is necessary is the convexity of $e_s(T)$, hence "
             "Clausius-Clapeyron.")),
        mc(t("Ein Kondensstreifen steht nach einer Stunde noch da und ist "
             "zu einem breiten Band geworden. Was schließen Sie für "
             "morgen?",
             "A contrail is still there after an hour and has become a "
             "broad band. What do you conclude for tomorrow?"),
           [t("Nichts -- die Beständigkeit hängt nur am Triebwerkstyp.",
              "Nothing -- persistence depends only on the engine type."),
            t("Es wird kälter, weil der Streifen die Sonne "
              "abschirmt.",
              "It will get colder, because the trail shades the sun."),
            t("Hochdruckwetter: Nur bei Absinken bleiben Streifen "
              "stehen.",
              "High pressure: trails only persist in subsiding air."),
            t("Die Höhenluft ist eisübersättigt -- sie bildet von selbst "
              "Cirrus. Das ist die Vorlaufzone einer Warmfront, 12 bis "
              "24 Stunden voraus.",
              "The upper air is ice-supersaturated -- it makes cirrus by "
              "itself. That is the leading zone of a warm front, 12 to "
              "24 hours ahead.")], 3,
           t("Der Streifen bleibt nur, wenn die Umgebung gegenüber Eis "
             "übersättigt ist, und das ist sie schon bei rund 65 % "
             "relativer Feuchte über Wasser (bei −45 °C liegt e_s über "
             "Eis bei 65 % des Werts über Wasser). Dieselbe Luftmasse "
             "macht nach wo-gattungen den Cirrus, der der Warmfront "
             "vorausgeht -- man sieht sie nur eher, weil das Flugzeug die "
             "Kerne mitbringt.",
             "The trail only stays if the surroundings are supersaturated "
             "with respect to ice, and they already are at about 65 % "
             "relative humidity over water (at −45 °C e_s over ice is "
             "65 % of the value over water). The same air mass makes the "
             "cirrus that precedes a warm front, by wo-gattungen -- one "
             "simply sees it sooner, because the aircraft brings the "
             "nuclei along."),
           bild="cirrus"),
        ]),
    ])


KAPITEL = [K_ATMOSPHAERE, K_THERMO, K_FEUCHTE, K_STRAHLUNG, K_BODEN, K_WOLKEN, K_WOLKENBUCH,
           K_DYNAMIK, K_WOLKENLESEN, K_ZIRKULATION, K_SYNOPTIK, K_MESOSKALA, K_OPTIK,
           K_HIMMEL, K_VORHERSAGE, K_SELBSTMESSEN]

# Alles Geplante ist geschrieben.
PLAN = []

THEMEN = {
    "atmosphaere": t("Aufbau und Hydrostatik", "Structure and hydrostatics"),
    "thermo": t("Thermodynamik", "Thermodynamics"),
    "feuchte": t("Feuchte Luft", "Moist air"),
    "strahlung": t("Strahlung", "Radiation"),
    "wolken": t("Wolken und Niederschlag", "Clouds and precipitation"),
    "dynamik": t("Dynamik", "Dynamics"),
    "zirkulation": t("Zirkulation und Synoptik", "Circulation and synoptics"),
    "mesoskala": t("Föhn, Seewind, Gewitter", "Foehn, sea breeze, storms"),
    "optik": t("Optik", "Optics"),
    "vorhersage": t("Vorhersage", "Forecasting"),
}


def frage(ident, stufe, thema, q, optionen, antwort, warum, bild=""):
    return {"id": ident, "stufe": stufe, "thema": thema, "q": q,
            "optionen": optionen, "antwort": antwort, "warum": warum,
            "bild": bild}


EINSTUFUNG = [
    # -- Stufe 1 -----------------------------------------------------------
    frage("e-skalenhoehe", 1, "atmosphaere",
          t("In welcher Höhe ist der Luftdruck etwa auf die Hälfte "
            "gefallen?",
            "At what height has the air pressure fallen to about half?"),
          [t("Etwa 5,5 km", "About 5.5 km"), t("Etwa 1 km", "About 1 km"),
           t("Etwa 15 km", "About 15 km"), t("Etwa 50 km", "About 50 km")], 0,
          t("Die Skalenhöhe ist 7-8 km (Druck auf 1/e); halbiert ist er "
            "nach `H·ln 2 ≈ 5,5 km`.",
            "The scale height is 7-8 km (pressure to 1/e); it halves after "
            "`H·ln 2 ≈ 5.5 km`.")),
    frage("e-stratosphaere", 1, "atmosphaere",
          t("Was heizt die Stratosphäre?",
            "What heats the stratosphere?"),
          [t("Ozon, das UV absorbiert.", "Ozone absorbing UV."),
           t("Der Boden.", "The ground."),
           t("Wasserdampf.", "Water vapour."),
           t("Reibung des Sonnenwinds.", "Friction of the solar wind.")], 0,
          t("Deshalb steigt dort die Temperatur mit der Höhe, und deshalb "
            "ist sie stabil geschichtet.",
            "That is why temperature rises with height there, and why it "
            "is stably stratified.")),

    # -- Stufe 2 -----------------------------------------------------------
    frage("e-adiabate", 2, "thermo",
          t("Ein trockenes Luftpaket steigt 1000 m. Um wie viel kühlt es "
            "sich ab?",
            "A dry parcel rises 1000 m. By how much does it cool?"),
          [t("Rund 10 K", "About 10 K"), t("Rund 6,5 K", "About 6.5 K"),
           t("Rund 2 K", "About 2 K"), t("Gar nicht", "Not at all")], 0,
          t("`g/c_p = 9,8 K/km`. Die 6,5 K/km sind der Umgebungsgradient, "
            "nicht der des Pakets.",
            "`g/c_p = 9.8 K/km`. The 6.5 K/km is the environmental lapse "
            "rate, not the parcel's.")),
    frage("e-theta", 2, "thermo",
          t("Welche Größe bleibt bei trockenadiabatischem Aufsteigen "
            "erhalten?",
            "Which quantity is conserved during dry adiabatic ascent?"),
          [t("Die potentielle Temperatur θ.", "The potential temperature θ."),
           t("Die Temperatur T.", "The temperature T."),
           t("Die Dichte ρ.", "The density ρ."),
           t("Der Druck p.", "The pressure p.")], 0,
          t("θ ist die Entropie in Temperatureinheiten; adiabatisch heißt "
            "isentrop.",
            "θ is entropy in temperature units; adiabatic means "
            "isentropic.")),

    # -- Stufe 3 -----------------------------------------------------------
    frage("e-clausius", 3, "feuchte",
          t("Um wie viel steigt der Sättigungsdampfdruck je 10 K "
            "Erwärmung, grob?",
            "By how much does the saturation vapour pressure rise per 10 K "
            "of warming, roughly?"),
          [t("Er verdoppelt sich.", "It doubles."),
           t("Um 10 %.", "By 10 %."),
           t("Er verzehnfacht sich.", "It increases tenfold."),
           t("Linear um 6 hPa.", "Linearly by 6 hPa.")], 0,
          t("Clausius-Clapeyron: rund 7 % je Kelvin, exponentiell.",
            "Clausius–Clapeyron: about 7 % per kelvin, exponential.")),
    frage("e-lcl", 3, "feuchte",
          t("Am Boden 20 °C, Taupunkt 10 °C. Wo liegt die Cumulus-Basis "
            "etwa?",
            "At the ground 20 °C, dew point 10 °C. Roughly where is the "
            "cumulus base?"),
          [t("1250 m", "1250 m"), t("250 m", "250 m"),
           t("4000 m", "4000 m"), t("Nicht abschätzbar.", "Cannot be "
             "estimated.")], 0,
          t("125 m je Kelvin Spreizung: `10 × 125 = 1250 m`.",
            "125 m per kelvin of spread: `10 × 125 = 1250 m`.")),

    # -- Stufe 4 -----------------------------------------------------------
    frage("e-255", 4, "strahlung",
          t("Die effektive Strahlungstemperatur der Erde beträgt 255 K. "
            "Was ist das?",
            "The Earth's effective radiative temperature is 255 K. What is "
            "that?"),
          [t("Die Temperatur, mit der die Erde von außen im Infrarot "
             "strahlt -- erreicht in etwa 5 km Höhe.",
             "The temperature at which the Earth radiates to space in the "
             "infrared -- found at about 5 km height."),
           t("Die mittlere Bodentemperatur.", "The mean surface "
             "temperature."),
           t("Die Temperatur der Tropopause.", "The tropopause "
             "temperature."),
           t("Die Temperatur ohne Sonne.", "The temperature without the "
             "sun.")], 0,
          t("`σT⁴ = S₀(1−A)/4`. Der Boden hat 288 K; die 33 K Differenz "
            "sind der Treibhauseffekt.",
            "`σT⁴ = S₀(1−A)/4`. The surface is at 288 K; the 33 K "
            "difference is the greenhouse effect.")),
    frage("e-nacht", 4, "strahlung",
          t("Warum sind klare Nächte kälter als bewölkte?",
            "Why are clear nights colder than cloudy ones?"),
          [t("Die Gegenstrahlung fehlt; der Boden verliert netto "
             "60-100 W/m².",
             "The back radiation is missing; the ground loses 60-100 W/m² "
             "net."),
           t("Wolken speichern Sonnenwärme.", "Clouds store solar heat."),
           t("Klare Luft leitet besser.", "Clear air conducts better."),
           t("Das stimmt nicht.", "That is not true.")], 0,
          t("Die Wolkenbasis strahlt fast so viel zurück, wie der Boden "
            "abgibt.",
            "The cloud base radiates back almost as much as the ground "
            "emits.")),

    # -- Stufe 5 -----------------------------------------------------------
    frage("e-kerne", 5, "wolken",
          t("Warum kondensiert Wasserdampf in der Atmosphäre nie ohne "
            "Aerosol?",
            "Why does water vapour in the atmosphere never condense "
            "without aerosol?"),
          [t("Ein winziger reiner Tropfen hat wegen der Krümmung einen "
             "viel höheren Dampfdruck (Kelvin) und verdampft sofort.",
             "A tiny pure drop has a much higher vapour pressure because "
             "of curvature (Kelvin) and evaporates at once."),
           t("Weil Luft zu trocken ist.", "Because air is too dry."),
           t("Weil Wasser Staub braucht, um schwer zu werden.",
             "Because water needs dust to become heavy."),
           t("Es kondensiert auch ohne.", "It condenses without it too.")], 0,
          t("Homogene Nukleation bräuchte 300 % Feuchte. Kerne senken "
            "die Schwelle auf 0,1 bis 1 %.",
            "Homogeneous nucleation would need 300 % humidity. Nuclei "
            "lower the threshold to 0.1 to 1 %.")),
    frage("e-bergeron", 5, "wolken",
          t("Woher kommt der meiste Regen der mittleren Breiten?",
            "Where does most mid-latitude rain come from?"),
          [t("Aus geschmolzenem Schnee: Eiskristalle wachsen auf Kosten "
             "unterkühlter Tropfen.",
             "From melted snow: ice crystals grow at the expense of "
             "supercooled drops."),
           t("Aus Tropfen, die durch Diffusion wachsen.",
             "From drops growing by diffusion."),
           t("Aus Tau.", "From dew."),
           t("Aus dem Meer, direkt.", "Straight from the sea.")], 0,
          t("Bergeron-Findeisen: Der Dampfdruck über Eis ist niedriger "
            "als über Wasser.",
            "Bergeron–Findeisen: the vapour pressure over ice is lower "
            "than over water."),
          bild="cumulonimbus"),

    # -- Stufe 6 -----------------------------------------------------------
    frage("e-geostroph", 6, "dynamik",
          t("Nordhalbkugel, Rücken zum Wind. Wo ist das Tief?",
            "Northern hemisphere, back to the wind. Where is the low?"),
          [t("Links.", "On the left."), t("Rechts.", "On the right."),
           t("Voraus.", "Ahead."), t("Hinten.", "Behind.")], 0,
          t("Buys-Ballot: geostrophischer Wind mit dem Tief zur Linken.",
            "Buys-Ballot: geostrophic wind with the low on its left.")),
    frage("e-coriolis-arbeit", 6, "dynamik",
          t("Wie groß ist die Coriolis-Beschleunigung für 10 m/s in 45° "
            "Breite?",
            "How large is the Coriolis acceleration for 10 m/s at 45° "
            "latitude?"),
          [t("Etwa 10⁻³ m/s²", "About 10⁻³ m/s²"),
           t("Etwa 1 m/s²", "About 1 m/s²"),
           t("Etwa 10⁻⁶ m/s²", "About 10⁻⁶ m/s²"),
           t("Null.", "Zero.")], 0,
          t("`f·v = 1,03·10⁻⁴ × 10 = 10⁻³ m/s²`. Winzig, aber stundenlang "
            "quer.",
            "`f·v = 1.03·10⁻⁴ × 10 = 10⁻³ m/s²`. Tiny, but sideways for "
            "hours.")),

    # -- Stufe 7 -----------------------------------------------------------
    frage("e-thermwind", 7, "dynamik",
          t("Der Wind nimmt mit der Höhe stark zu. Was folgt daraus?",
            "The wind increases strongly with height. What follows?"),
          [t("Ein waagrechter Temperaturgradient quer zum Wind "
             "(thermischer Wind).",
             "A horizontal temperature gradient across the wind (thermal "
             "wind)."),
           t("Die Luft ist labil.", "The air is unstable."),
           t("Es wird regnen.", "It will rain."),
           t("Der Druck fällt.", "The pressure is falling.")], 0,
          t("Windscherung und Temperaturgradient sind über die "
            "Hydrostatik gekoppelt -- der Jet liegt über der Polarfront.",
            "Wind shear and temperature gradient are coupled through "
            "hydrostatics -- the jet lies above the polar front.")),
    frage("e-hadley", 7, "zirkulation",
          t("Warum endet die Hadley-Zelle bei etwa 30° Breite?",
            "Why does the Hadley cell end at about 30° latitude?"),
          [t("Drehimpulserhaltung würde weiter polwärts unmögliche "
             "Windgeschwindigkeiten verlangen; die Strömung wird instabil.",
             "Angular momentum conservation would demand impossible wind "
             "speeds further poleward; the flow becomes unstable."),
           t("Weil dort die Wüsten sind.", "Because the deserts are "
             "there."),
           t("Weil die Sonne nicht weiter reicht.", "Because the sun does "
             "not reach further."),
           t("Weil die Erde dort am breitesten ist.", "Because the Earth "
             "is widest there.")], 0,
          t("134 m/s bei 30°, 700 m/s bei 60°: Barokline Wirbel übernehmen "
            "den Transport.",
            "134 m/s at 30°, 700 m/s at 60°: baroclinic eddies take over "
            "the transport.")),

    # -- Stufe 8 -----------------------------------------------------------
    frage("e-kaltfront", 8, "zirkulation",
          t("Windsprung von Südwest auf Nordwest, Druck steigt steil, "
            "Schauer. Was war das?",
            "Wind jump from south-west to north-west, pressure rising "
            "sharply, showers. What was that?"),
          [t("Eine Kaltfront.", "A cold front."),
           t("Eine Warmfront.", "A warm front."),
           t("Ein Hoch.", "A high."),
           t("Föhn.", "Foehn.")], 0,
          t("Der steile Kaltluftkeil hebt die Warmluft schnell.",
            "The steep cold wedge lifts the warm air quickly.")),
    frage("e-foehn", 8, "mesoskala",
          t("Woher kommt die Wärme des Föhns?",
            "Where does the foehn's warmth come from?"),
          [t("Aus der Kondensationswärme des Regens im Luv und dem "
             "trockenadiabatischen Abstieg im Lee.",
             "From the condensation heat of the rain on the windward side "
             "and the dry adiabatic descent in the lee."),
           t("Aus der Sahara.", "From the Sahara."),
           t("Aus der Reibung am Berg.", "From friction on the mountain."),
           t("Aus der Sonne auf den Südhängen.", "From the sun on the "
             "southern slopes.")], 0,
          t("Luv feucht mit 6 K/km hinauf, Lee trocken mit 10 K/km "
            "hinunter: Die Differenz ist die Föhnwärme.",
            "Up the windward side moist at 6 K/km, down the lee dry at "
            "10 K/km: the difference is the foehn warmth.")),

    # -- Stufe 9 -----------------------------------------------------------
    frage("e-scherung", 9, "mesoskala",
          t("Was macht aus einer einstündigen Gewitterzelle ein "
            "stundenlanges Unwetter?",
            "What turns a one-hour thunderstorm cell into an hours-long "
            "storm?"),
          [t("Windscherung: Der Aufwind kippt, Regen und Aufwind trennen "
             "sich.",
             "Wind shear: the updraught tilts, rain and updraught "
             "separate."),
           t("Mehr Feuchte.", "More moisture."),
           t("Eine höhere Tropopause.", "A higher tropopause."),
           t("Hagel.", "Hail.")], 0,
          t("Ohne Scherung erstickt der Niederschlag den eigenen Aufwind.",
            "Without shear the precipitation chokes its own updraught.")),
    frage("e-regenbogen", 9, "optik",
          t("Warum steht der Regenbogen bei 42° vom Sonnengegenpunkt?",
            "Why does the rainbow stand at 42° from the antisolar point?"),
          [t("Dort hat die Ablenkung im Tropfen ein Minimum, und die "
             "Strahlen häufen sich.",
             "There the deviation in the drop has a minimum, and the rays "
             "pile up."),
           t("Weil Wasser eine Brechzahl von 1,42 hat.",
             "Because water has a refractive index of 1.42."),
           t("Weil die Sonne bei 42° steht.", "Because the sun is at 42°."),
           t("Das ist Zufall.", "That is a coincidence.")], 0,
          t("Descartes: `cos i = √((n²−1)/3)`, Minimum der Ablenkung bei "
            "138°, also 42° vom Gegenpunkt.",
            "Descartes: `cos i = √((n²−1)/3)`, minimum deviation at 138°, "
            "hence 42° from the antisolar point.")),

    # -- Stufe 10 ----------------------------------------------------------
    frage("e-chaos", 10, "vorhersage",
          t("Warum endet die deterministische Wettervorhersage nach "
            "etwa zwei Wochen?",
            "Why does deterministic weather forecasting end after about "
            "two weeks?"),
          [t("Anfangsfehler wachsen exponentiell, Verdopplung alle zwei "
             "Tage; nach zwei Wochen ist jede Unsicherheit so groß wie "
             "das Wetter selbst.",
             "Initial errors grow exponentially, doubling every two days; "
             "after two weeks any uncertainty is as large as the weather "
             "itself."),
           t("Weil die Rechner zu langsam sind.", "Because the computers "
             "are too slow."),
           t("Weil die Satelliten nur zwei Wochen speichern.",
             "Because satellites store only two weeks."),
           t("Sie endet nicht, man rechnet nur nicht weiter.",
             "It does not end, one just stops computing.")], 0,
          t("Lorenz 1963: deterministisch und doch unvorhersagbar.",
            "Lorenz 1963: deterministic and yet unpredictable.")),
    frage("e-ensemble", 10, "vorhersage",
          t("'70 % Regenwahrscheinlichkeit' heißt in einem Ensemble mit "
            "50 Läufen:",
            "'70 % chance of rain' means in a 50-member ensemble:"),
          [t("35 von 50 Läufen lassen es regnen.",
             "35 of 50 runs produce rain."),
           t("Es regnet 70 % des Tages.", "It rains 70 % of the day."),
           t("70 % des Gebiets bekommen Regen.", "70 % of the area gets "
             "rain."),
           t("Der Mittelwert ist 0,7 mm.", "The mean is 0.7 mm.")], 0,
          t("Das Ensemble liefert eine Verteilung; die Wahrscheinlichkeit "
            "ist der Anteil der Mitglieder.",
            "The ensemble delivers a distribution; the probability is the "
            "fraction of members.")),

    # -- Beobachtungsfragen zu den neuen Kapiteln --------------------------
    frage("e-himmelsblick", 4, "strahlung",
          t("Nach einer klaren Nacht ist der Rasen nass, unter dem "
            "Apfelbaum aber trocken. Warum?",
            "After a clear night the lawn is wet, but dry under the "
            "apple tree. Why?"),
          [t("Der Baum nimmt dem Boden den Wasserdampf weg.",
             "The tree takes the vapour away from the ground."),
           t("Unter der Krone ist es wärmer, weil Blätter Wärme "
             "abgeben.",
             "It is warmer under the canopy because leaves give off "
             "heat."),
           t("Der Boden strahlt nur gegen den Teil des Himmels aus, "
             "den er sieht: Unter der Krone ist der Verlust auf etwa "
             "ein Drittel reduziert, die Oberfläche kommt nicht unter "
             "den Taupunkt.",
             "The ground radiates only against the part of the sky it "
             "sees: under the canopy the loss is cut to about a third, "
             "and the surface never reaches the dew point."),
           t("Das Laub hält den Tau ab, der Boden darunter ist "
             "trotzdem kalt.",
             "The foliage keeps the dew off; the ground underneath is "
             "cold all the same.")], 2,
          t("Derselbe Faktor macht den Unterschied zwischen freiem Feld "
            "und Straßenschlucht, und er heißt Himmelsblickfaktor: "
            "`L_netto = ψ·(σT⁴ − L↓)`, im Freien 70 W/m², unter der "
            "Krone 21 W/m².",
            "The same factor makes the difference between open field "
            "and street canyon, and it is called the sky view factor: "
            "`L_net = ψ·(σT⁴ − L↓)`, 70 W/m² in the open, 21 W/m² under "
            "the canopy.")),
    frage("e-landmarke", 9, "optik",
          t("Der entfernteste noch erkennbare Berggipfel steht 40 km "
            "weit. Was folgt daraus?",
            "The most distant still recognisable summit stands 40 km "
            "away. What follows?"),
          [t("Der Extinktionskoeffizient ist etwa 10⁻⁴ /m, aus "
             "V = 3,9/β -- leichter Dunst, zehnmal mehr als reine "
             "Luft.",
             "The extinction coefficient is about 10⁻⁴ /m, from "
             "V = 3.9/β -- light haze, ten times more than clean "
             "air."),
           t("Die Luft ist praktisch rein, β ≈ 10⁻⁵ /m.",
             "The air is practically clean, β ≈ 10⁻⁵ /m."),
           t("Nichts -- die Sichtweite hängt nur von der Größe des "
             "Bergs ab.",
             "Nothing -- visibility depends only on the size of the "
             "mountain."),
           t("Die Erdkrümmung begrenzt die Sicht auf 40 km.",
             "The curvature of the Earth limits the view to 40 km.")], 0,
          t("Koschmieder, umgekehrt gelesen: `β = 3,9/V = 3,9/40 000 m "
            "= 9,75·10⁻⁵ /m`. Eine benannte Landmarke in bekannter "
            "Entfernung ist ein Transmissometer.",
            "Koschmieder read backwards: `β = 3.9/V = 3.9/40 000 m = "
            "9.75·10⁻⁵ /m`. A named landmark at a known distance is a "
            "transmissometer.")),
    frage("e-drucktendenz", 10, "vorhersage",
          t("Das Barometer fällt gleichmäßig um 2 hPa je Stunde. Was "
            "misst man damit eigentlich?",
            "The barometer falls steadily by 2 hPa per hour. What is "
            "actually being measured?"),
          [t("Die Temperatur der Luftsäule.",
             "The temperature of the air column."),
           t("Das Produkt aus Druckgradient und Zuggeschwindigkeit des "
             "Musters: ∂p/∂t = −c·∂p/∂x.",
             "The product of pressure gradient and the travel speed of "
             "the pattern: ∂p/∂t = −c·∂p/∂x."),
           t("Die kommende Regenmenge.",
             "The amount of rain to come."),
           t("Die Höhe über dem Meer.",
             "The height above sea level.")], 1,
          t("Ein Druckfeld, das sich unverändert verlagert, gibt am "
            "festen Ort genau diese Tendenz. Wer den Gradienten aus der "
            "Karte kennt, bekommt die Zuggeschwindigkeit -- und damit "
            "die Ankunftszeit der Front.",
            "A pressure field travelling unchanged produces exactly "
            "this tendency at a fixed place. Whoever knows the gradient "
            "from the chart gets the travel speed -- and with it the "
            "arrival time of the front.")),
]
