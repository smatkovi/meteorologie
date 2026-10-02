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
# Zusammenstellung
# ===========================================================================

KAPITEL = [K_ATMOSPHAERE, K_THERMO, K_FEUCHTE, K_STRAHLUNG, K_WOLKEN,
           K_DYNAMIK, K_ZIRKULATION, K_SYNOPTIK, K_MESOSKALA, K_OPTIK,
           K_VORHERSAGE]

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
]
