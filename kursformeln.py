# -*- coding: utf-8 -*-
"""Die Formeln des Kurses, je Lektion: Textzeile, TeX, Untertitel,
Erklärung, Zeichen und -- wo es eine eigene gibt -- Skizze.

Gesetzt werden sie beim Bauen (tools/formeln.py, matplotlib.mathtext auf
dem Baurechner). Die Erklärung sagt in drei Sätzen, was dasteht und wo es
aufhört zu gelten; die Herleitung steht in herleitungen.py und hängt am
Lektionstext. Die Zeichenliste steht für sich, weil der Kasten beim
Durchblättern allein gesehen wird.
"""
from __future__ import unicode_literals


def t(de, en):
    return {"de": de, "en": en}


# Zu welcher Formel welche eigene Skizze gehört. Die Lektion zeigt ihre
# Hauptzeichnung ohnehin oben; hier stehen nur Zweitzeichnungen, die eine
# einzelne Formel braucht.
SKIZZEN = {
    "Der Coriolis-Parameter": "skizze-breite",
    "Der 22°-Halo aus dem 60°-Prisma": "skizze-halo",
}


def formel(zeile, tex, untertitel, erklaerung, zeichen):
    return {"code": zeile, "tex": tex, "untertitel": untertitel,
            "erklaerung": erklaerung, "zeichen": zeichen,
            "skizze": SKIZZEN.get(untertitel["de"], "")}


KURSFORMELN = {

# --- 1 Atmosphäre ------------------------------------------------------------

"at-aufbau": [
    formel("p = ρ · R_L · T",
        r"$p = \rho\,R_L\,T, \qquad R_L = \frac{R^*}{M} = 287\,\frac{\mathrm{J}}{\mathrm{kg\,K}}$",
        t("Zustandsgleichung der trockenen Luft",
          "Equation of state of dry air"),
        t("Das ideale Gas mit der spezifischen Gaskonstante der "
          "Mischung. Gilt für alles, was die Meteorologie braucht -- die "
          "Abweichungen vom idealen Verhalten liegen unter 0,1 %. Mit "
          "Wasserdampf ersetzt man `T` durch die virtuelle Temperatur.",
          "The ideal gas with the specific gas constant of the mixture. "
          "Holds for everything meteorology needs -- deviations from "
          "ideal behaviour are below 0.1 %. With water vapour, `T` is "
          "replaced by the virtual temperature."),
        t("`p` Druck, Pa. `ρ` Dichte, kg/m³. `T` Temperatur, K. `R*` "
          "universelle Gaskonstante, 8,314 J/(mol·K). `M` mittlere "
          "Molmasse, 0,02896 kg/mol.",
          "`p` pressure, Pa. `ρ` density, kg/m³. `T` temperature, K. `R*` "
          "universal gas constant, 8.314 J/(mol·K). `M` mean molar mass, "
          "0.02896 kg/mol.")),
],

"at-hydrostatik": [
    formel("dp/dz = −ρ·g",
        r"$\frac{dp}{dz} = -\rho\,g$",
        t("Die hydrostatische Grundgleichung",
          "The hydrostatic equation"),
        t("Der Druckgradient nach oben trägt das Gewicht der Luft "
          "darüber. Exakt für ruhende Luft, und auf 1 % genau für alles "
          "Großräumige, weil vertikale Beschleunigungen klein gegen `g` "
          "sind. Nur in Gewitteraufwinden (10 m/s auf 1 km) wird der "
          "Fehler spürbar.",
          "The upward pressure gradient carries the weight of the air "
          "above. Exact for air at rest, and accurate to 1 % for "
          "everything large-scale, because vertical accelerations are "
          "small against `g`. Only in thunderstorm updraughts (10 m/s "
          "over 1 km) does the error become noticeable."),
        t("`p` Druck, Pa. `z` Höhe, m. `ρ` Dichte, kg/m³. `g` "
          "Fallbeschleunigung, 9,81 m/s².",
          "`p` pressure, Pa. `z` height, m. `ρ` density, kg/m³. `g` "
          "gravitational acceleration, 9.81 m/s².")),
    formel("p = p0 · exp(−z/H),  H = R_L·T/g",
        r"$p(z) = p_0\,e^{-z/H}, \qquad H = \frac{R_L\,T}{g}$",
        t("Barometrische Höhenformel und Skalenhöhe",
          "Barometric formula and scale height"),
        t("Für konstante Temperatur. `H` ist die Höhe, über die der "
          "Druck auf 1/e fällt: 7,3 km bei 250 K, 8,4 km bei 288 K. Mit "
          "veränderlichem `T` wird daraus ein Integral über `1/T`, und "
          "die Standardatmosphäre löst es für linearen Gradienten.",
          "For constant temperature. `H` is the height over which the "
          "pressure falls to 1/e: 7.3 km at 250 K, 8.4 km at 288 K. With "
          "variable `T` it becomes an integral over `1/T`, and the "
          "standard atmosphere solves it for a linear lapse rate."),
        t("`p₀` Bodendruck, Pa. `H` Skalenhöhe, m. `R_L` 287 J/(kg·K). "
          "`T` Temperatur, K. `g` 9,81 m/s².",
          "`p₀` surface pressure, Pa. `H` scale height, m. `R_L` "
          "287 J/(kg·K). `T` temperature, K. `g` 9.81 m/s².")),
],

"at-standard": [
    formel("p = p0 · (1 − Γ·z/T0)^(g/(R_L·Γ))",
        r"$p(z) = p_0\left(1 - \frac{\Gamma z}{T_0}\right)^{g/(R_L\Gamma)}, \qquad \frac{g}{R_L\Gamma} = 5{,}26$",
        t("Druckverlauf bei linearem Temperaturgradienten",
          "Pressure profile for a linear lapse rate"),
        t("Die Lösung der Hydrostatik für `T = T₀ − Γz`; mit `Γ = 6,5 "
          "K/km` die ICAO-Standardatmosphäre. Für `Γ → 0` geht sie in "
          "die Exponentialfunktion über. Der Höhenmesser hat genau diese "
          "Kurve auf der Skala.",
          "The solution of hydrostatics for `T = T₀ − Γz`; with `Γ = 6.5 "
          "K/km` the ICAO standard atmosphere. For `Γ → 0` it turns into "
          "the exponential. The altimeter has exactly this curve on its "
          "scale."),
        t("`T₀` Bodentemperatur, 288,15 K. `Γ` Temperaturgradient, "
          "0,0065 K/m. `p₀` 1013,25 hPa. `R_L` 287 J/(kg·K). `g` "
          "9,81 m/s².",
          "`T₀` surface temperature, 288.15 K. `Γ` lapse rate, "
          "0.0065 K/m. `p₀` 1013.25 hPa. `R_L` 287 J/(kg·K). `g` "
          "9.81 m/s².")),
],

# --- 2 Thermodynamik ---------------------------------------------------------

"th-adiabate": [
    formel("Γ_d = g / c_p = 9,8 K/km",
        r"$\Gamma_d = -\frac{dT}{dz} = \frac{g}{c_p} = 9{,}8\,\frac{\mathrm{K}}{\mathrm{km}}$",
        t("Der trockenadiabatische Temperaturgradient",
          "The dry adiabatic lapse rate"),
        t("Erster Hauptsatz ohne Wärmezufuhr plus Hydrostatik. Weder "
          "Druck noch Temperatur kommen vor: Der Wert ist vom Boden bis "
          "zur Tropopause derselbe. Er gilt, bis Kondensation einsetzt "
          "-- dann übernimmt die Feuchtadiabate.",
          "First law without heat input plus hydrostatics. Neither "
          "pressure nor temperature appears: the value is the same from "
          "the ground to the tropopause. It holds until condensation "
          "starts -- then the moist adiabat takes over."),
        t("`Γ_d` trockenadiabatischer Gradient, K/m. `g` 9,81 m/s². "
          "`c_p` spezifische Wärme bei konstantem Druck, 1004 J/(kg·K).",
          "`Γ_d` dry adiabatic lapse rate, K/m. `g` 9.81 m/s². `c_p` "
          "specific heat at constant pressure, 1004 J/(kg·K).")),
],

"th-theta": [
    formel("θ = T · (p0/p)^κ,  κ = R_L/c_p = 0,286",
        r"$\theta = T\left(\frac{p_0}{p}\right)^{\kappa}, \qquad \kappa = \frac{R_L}{c_p} = 0{,}286$",
        t("Die potentielle Temperatur", "Potential temperature"),
        t("Die Temperatur nach adiabatischem Bringen auf 1000 hPa. "
          "Erhalten bei trockenadiabatischen Vorgängen, also ein Tracer "
          "für Luftpakete und zugleich die Entropie: `s = c_p ln θ`. "
          "Nimmt mit der Höhe zu, wenn die Schichtung stabil ist.",
          "The temperature after adiabatic transfer to 1000 hPa. "
          "Conserved in dry adiabatic processes, hence a tracer for "
          "parcels and at the same time the entropy: `s = c_p ln θ`. "
          "Increases with height when the stratification is stable."),
        t("`θ` potentielle Temperatur, K. `T` Temperatur, K. `p₀` "
          "1000 hPa. `p` Druck, hPa. `κ` Poisson-Konstante, 0,286.",
          "`θ` potential temperature, K. `T` temperature, K. `p₀` "
          "1000 hPa. `p` pressure, hPa. `κ` Poisson constant, 0.286.")),
],

"th-stabilitaet": [
    formel("N² = (g/θ) · dθ/dz",
        r"$N^2 = \frac{g}{\theta}\,\frac{d\theta}{dz} = \frac{g}{T}\left(\Gamma_d - \Gamma\right)$",
        t("Die Brunt-Väisälä-Frequenz", "The Brunt–Väisälä frequency"),
        t("Die Schwingungsfrequenz eines vertikal ausgelenkten Pakets. "
          "`N² > 0` stabil, `N² < 0` labil, der Übergang bei `Γ = Γ_d`. "
          "Typisch 0,01 /s in der Troposphäre, 0,02 /s in der "
          "Stratosphäre. Setzt die Zeitskala aller Schwerewellen.",
          "The oscillation frequency of a vertically displaced parcel. "
          "`N² > 0` stable, `N² < 0` unstable, the transition at "
          "`Γ = Γ_d`. Typically 0.01 /s in the troposphere, 0.02 /s in "
          "the stratosphere. Sets the time scale of all gravity waves."),
        t("`N` Brunt-Väisälä-Frequenz, 1/s. `θ` potentielle Temperatur, "
          "K. `Γ` Umgebungsgradient, K/m. `Γ_d` Trockenadiabate, K/m.",
          "`N` Brunt–Väisälä frequency, 1/s. `θ` potential temperature, "
          "K. `Γ` environmental lapse rate, K/m. `Γ_d` dry adiabat, "
          "K/m.")),
],

# --- 3 Feuchte ---------------------------------------------------------------

"fe-dampf": [
    formel("de_s/dT = L_v·e_s / (R_v·T²)",
        r"$\frac{de_s}{dT} = \frac{L_v\,e_s}{R_v\,T^2}$",
        t("Clausius-Clapeyron", "Clausius–Clapeyron"),
        t("Die Steigung der Dampfdruckkurve: rund 7 % je Kelvin, "
          "exponentiell. Hergeleitet aus dem Gleichgewicht der freien "
          "Enthalpie beider Phasen; die Näherung ist, dass das "
          "Flüssigvolumen gegen das Dampfvolumen vernachlässigt wird.",
          "The slope of the vapour pressure curve: about 7 % per "
          "kelvin, exponential. Derived from the balance of free "
          "enthalpy of both phases; the approximation is neglecting the "
          "liquid volume against the vapour volume."),
        t("`e_s` Sättigungsdampfdruck, Pa. `L_v` Verdampfungswärme, "
          "2,5·10⁶ J/kg. `R_v` Gaskonstante des Dampfes, 461,5 J/(kg·K). "
          "`T` Temperatur, K.",
          "`e_s` saturation vapour pressure, Pa. `L_v` latent heat of "
          "vaporisation, 2.5·10⁶ J/kg. `R_v` gas constant of vapour, "
          "461.5 J/(kg·K). `T` temperature, K.")),
    formel("r = 0,622·e/(p − e),  T_v = T·(1 + 0,61·r)",
        r"$r = 0{,}622\,\frac{e}{p - e}, \qquad T_v = T\,(1 + 0{,}61\,r)$",
        t("Mischungsverhältnis und virtuelle Temperatur",
          "Mixing ratio and virtual temperature"),
        t("Die 0,622 sind das Verhältnis der Molmassen von Wasser und "
          "Luft. Feuchte Luft ist leichter als trockene; `T_v` ist die "
          "Temperatur, bei der trockene Luft dieselbe Dichte hätte, und "
          "wird in der Zustandsgleichung an die Stelle von `T` gesetzt.",
          "The 0.622 is the ratio of molar masses of water and air. "
          "Moist air is lighter than dry air; `T_v` is the temperature "
          "at which dry air would have the same density, and replaces "
          "`T` in the equation of state."),
        t("`r` Mischungsverhältnis, kg/kg. `e` Dampfdruck, Pa. `p` "
          "Luftdruck, Pa. `T_v` virtuelle Temperatur, K.",
          "`r` mixing ratio, kg/kg. `e` vapour pressure, Pa. `p` air "
          "pressure, Pa. `T_v` virtual temperature, K.")),
],

"fe-hebung": [
    formel("z_LCL ≈ 125 m/K · (T − T_d)",
        r"$z_{LCL} \approx \frac{T - T_d}{\Gamma_d - \Gamma_{T_d}} \approx 125\,\frac{\mathrm{m}}{\mathrm{K}}\,(T - T_d)$",
        t("Das Hebungskondensationsniveau", "The lifting condensation level"),
        t("Temperatur fällt mit 9,8 K/km, Taupunkt mit 1,7 K/km; die "
          "Spreizung schließt sich mit 8,1 K/km. Gilt für ein Paket, das "
          "vom Boden aufsteigt, ohne sich zu mischen -- unter einer "
          "Inversion oder bei Advektion feuchter Luft liegt die Basis "
          "tiefer.",
          "Temperature falls at 9.8 K/km, dew point at 1.7 K/km; the "
          "spread closes at 8.1 K/km. Holds for a parcel rising from the "
          "ground without mixing -- under an inversion or with moist "
          "advection the base is lower."),
        t("`z_LCL` Höhe der Wolkenbasis über Grund, m. `T` Temperatur "
          "am Boden, °C. `T_d` Taupunkt am Boden, °C. `Γ_(T_d)` "
          "Taupunktgradient, 1,7 K/km.",
          "`z_LCL` cloud base height above ground, m. `T` temperature "
          "at the ground, °C. `T_d` dew point at the ground, °C. "
          "`Γ_(T_d)` dew point lapse rate, 1.7 K/km.")),
    formel("Γ_s = Γ_d · (1 + L·r_s/(R_L·T)) / (1 + L²·r_s·ε/(c_p·R_L·T²))",
        r"$\Gamma_s = \Gamma_d\;\frac{1 + \dfrac{L_v\,r_s}{R_L\,T}}{1 + \dfrac{\varepsilon\,L_v^2\,r_s}{c_p\,R_L\,T^2}}$",
        t("Der feuchtadiabatische Gradient", "The moist adiabatic lapse rate"),
        t("Die Kondensationswärme bremst die Abkühlung. 6,5 K/km bei "
          "0 °C, 4,2 K/km bei 20 °C, fast 9,8 K/km bei −40 °C. Das ist "
          "die Pseudoadiabate: Das Kondensat fällt sofort aus und nimmt "
          "seine Wärmekapazität mit; die reversible Feuchtadiabate "
          "unterscheidet sich um Zehntelgrade.",
          "The condensation heat slows the cooling. 6.5 K/km at 0 °C, "
          "4.2 K/km at 20 °C, almost 9.8 K/km at −40 °C. This is the "
          "pseudo-adiabat: the condensate falls out at once and takes "
          "its heat capacity with it; the reversible moist adiabat "
          "differs by tenths of a degree."),
        t("`Γ_s` feuchtadiabatischer Gradient, K/m. `r_s` "
          "Sättigungsmischungsverhältnis, kg/kg. `ε` 0,622. `L_v` "
          "2,5·10⁶ J/kg. `c_p` 1004 J/(kg·K). `R_L` 287 J/(kg·K).",
          "`Γ_s` moist adiabatic lapse rate, K/m. `r_s` saturation "
          "mixing ratio, kg/kg. `ε` 0.622. `L_v` 2.5·10⁶ J/kg. `c_p` "
          "1004 J/(kg·K). `R_L` 287 J/(kg·K).")),
    formel("θ_e ≈ θ · exp(L_v·r / (c_p·T))",
        r"$\theta_e \approx \theta\,\exp\!\left(\frac{L_v\,r}{c_p\,T}\right)$",
        t("Die äquivalentpotentielle Temperatur",
          "Equivalent potential temperature"),
        t("Die potentielle Temperatur, die das Paket hätte, wenn aller "
          "Dampf kondensiert und seine Wärme abgegeben hätte. Erhalten "
          "bei trockenen *und* feuchten adiabatischen Vorgängen -- das "
          "Etikett eines Luftpakets über den Alpenkamm hinweg.",
          "The potential temperature the parcel would have if all its "
          "vapour had condensed and given up its heat. Conserved in dry "
          "*and* moist adiabatic processes -- the label of a parcel "
          "across the Alpine crest."),
        t("`θ_e` äquivalentpotentielle Temperatur, K. `θ` potentielle "
          "Temperatur, K. `r` Mischungsverhältnis, kg/kg. `T` Temperatur "
          "am Kondensationsniveau, K.",
          "`θ_e` equivalent potential temperature, K. `θ` potential "
          "temperature, K. `r` mixing ratio, kg/kg. `T` temperature at "
          "the condensation level, K.")),
],

"fe-emagram": [
    formel("CAPE = ∫ g·(T_v' − T_v)/T_v dz,  w_max = √(2·CAPE)",
        r"$\mathrm{CAPE} = \int_{LFC}^{EL} g\,\frac{T_v' - T_v}{T_v}\,dz, \qquad w_{max} = \sqrt{2\,\mathrm{CAPE}}$",
        t("Konvektiv verfügbare potentielle Energie",
          "Convective available potential energy"),
        t("Die Arbeit, die der Auftrieb am Paket vom Niveau freier "
          "Konvektion bis zum Gleichgewichtsniveau leistet, in J/kg. "
          "Ganz in Bewegungsenergie umgesetzt ergäbe sie `w_max`; real "
          "bremsen Einmischung, Wasserlast und Druckstörungen auf die "
          "Hälfte.",
          "The work buoyancy does on the parcel from the level of free "
          "convection to the equilibrium level, in J/kg. Fully converted "
          "to kinetic energy it would give `w_max`; in reality "
          "entrainment, water loading and pressure perturbations halve "
          "it."),
        t("`T_v'` virtuelle Temperatur des Pakets, K. `T_v` die der "
          "Umgebung, K. `LFC` Niveau freier Konvektion. `EL` "
          "Gleichgewichtsniveau. `w_max` Aufwind, m/s.",
          "`T_v'` virtual temperature of the parcel, K. `T_v` that of "
          "the environment, K. `LFC` level of free convection. `EL` "
          "equilibrium level. `w_max` updraught, m/s.")),
],

# --- 4 Strahlung -------------------------------------------------------------

"st-bilanz": [
    formel("σ·T_e⁴ = S0·(1 − A)/4",
        r"$\sigma\,T_e^4 = \frac{S_0\,(1 - A)}{4} \quad\Rightarrow\quad T_e = 255\,\mathrm{K}$",
        t("Strahlungsgleichgewicht der Erde",
          "Radiative equilibrium of the Earth"),
        t("Absorbierte Sonnenleistung gleich abgestrahlte "
          "Infrarotleistung, beide je Quadratmeter Kugeloberfläche. Die "
          "4 ist Kugel durch Scheibe. Das Ergebnis ist die Temperatur, "
          "die man von außen misst -- nicht die am Boden.",
          "Absorbed solar power equals emitted infrared power, both "
          "per square metre of sphere. The 4 is sphere over disc. The "
          "result is the temperature measured from outside -- not the "
          "one at the ground."),
        t("`σ` Stefan-Boltzmann-Konstante, 5,67·10⁻⁸ W/(m²·K⁴). `T_e` "
          "effektive Temperatur, K. `S₀` Solarkonstante, 1361 W/m². `A` "
          "Albedo, 0,30.",
          "`σ` Stefan–Boltzmann constant, 5.67·10⁻⁸ W/(m²·K⁴). `T_e` "
          "effective temperature, K. `S₀` solar constant, 1361 W/m². "
          "`A` albedo, 0.30.")),
],

"st-treibhaus": [
    formel("T_s = 2^(1/4) · T_e",
        r"$T_s = 2^{1/4}\,T_e = 303\,\mathrm{K}$",
        t("Bodentemperatur im Einschichtmodell",
          "Surface temperature in the one-layer model"),
        t("Eine im Infrarot schwarze Schicht strahlt nach oben und "
          "unten; der Boden bekommt die Sonne und die Gegenstrahlung, "
          "also das Doppelte. Zu warm, weil das Modell das "
          "atmosphärische Fenster und die Konvektion nicht kennt; "
          "richtig ist der Mechanismus.",
          "A layer black in the infrared radiates up and down; the "
          "ground receives the sun and the back radiation, hence twice "
          "as much. Too warm because the model knows neither the "
          "atmospheric window nor convection; the mechanism is right."),
        t("`T_s` Bodentemperatur, K. `T_e` effektive Temperatur der "
          "Schicht, 255 K.",
          "`T_s` surface temperature, K. `T_e` effective temperature of "
          "the layer, 255 K.")),
    formel("ΔF = 5,35 W/m² · ln(C/C0)",
        r"$\Delta F = 5{,}35\,\frac{\mathrm{W}}{\mathrm{m^2}}\,\ln\frac{C}{C_0}, \qquad \Delta T_0 = \frac{\Delta F}{4\sigma T_e^3}$",
        t("Strahlungsantrieb und Planck-Antwort",
          "Radiative forcing and Planck response"),
        t("Logarithmisch, weil die Bandzentren gesättigt sind. Die "
          "Verdopplung gibt 3,7 W/m² und ohne Rückkopplungen 1,0 K; die "
          "Wasserdampf-, Wolken- und Eisrückkopplungen machen daraus "
          "2,5 bis 4 K. Die 5,35 sind eine Anpassung an "
          "Linie-für-Linie-Rechnungen, keine Naturkonstante.",
          "Logarithmic because the band centres are saturated. Doubling "
          "gives 3.7 W/m² and without feedbacks 1.0 K; the water "
          "vapour, cloud and ice feedbacks turn that into 2.5 to 4 K. "
          "The 5.35 is a fit to line-by-line calculations, not a "
          "constant of nature."),
        t("`ΔF` Strahlungsantrieb, W/m². `C` CO₂-Konzentration, `C₀` "
          "Bezugswert. `ΔT₀` Erwärmung ohne Rückkopplung, K. `T_e` 255 K.",
          "`ΔF` radiative forcing, W/m². `C` CO₂ concentration, `C₀` "
          "reference. `ΔT₀` warming without feedback, K. `T_e` 255 K.")),
],

"st-tagesgang": [
    formel("Q = (1 − A)·S + L↓ − σ·T_s⁴",
        r"$Q = (1 - A)\,S + L_\downarrow - \sigma\,T_s^4$",
        t("Die Strahlungsbilanz am Boden", "The surface radiation budget"),
        t("Was der Boden netto bekommt. Tagsüber positiv und von der "
          "Sonne beherrscht, nachts nur noch Gegenstrahlung minus "
          "Ausstrahlung: −60 bis −100 W/m² bei klarem Himmel, −10 W/m² "
          "unter Wolken. Die Bilanz, nicht die Einstrahlung, bestimmt "
          "den Temperaturgang.",
          "What the ground receives net. Positive by day and dominated "
          "by the sun, at night only back radiation minus emission: −60 "
          "to −100 W/m² under a clear sky, −10 W/m² under cloud. The "
          "budget, not the insolation, sets the temperature course."),
        t("`Q` Nettostrahlung, W/m². `A` Albedo des Bodens. `S` "
          "Sonnenstrahlung, W/m². `L↓` Gegenstrahlung der Atmosphäre, "
          "W/m². `T_s` Bodentemperatur, K.",
          "`Q` net radiation, W/m². `A` surface albedo. `S` solar "
          "radiation, W/m². `L↓` back radiation of the atmosphere, "
          "W/m². `T_s` surface temperature, K.")),
],

# --- 5 Wolken ----------------------------------------------------------------

"wo-tropfen": [
    formel("e_s(r)/e_s(∞) = exp(2σ/(ρ_w·R_v·T·r))",
        r"$\frac{e_s(r)}{e_s(\infty)} = \exp\!\left(\frac{2\sigma}{\rho_w\,R_v\,T\,r}\right)$",
        t("Die Kelvin-Gleichung", "The Kelvin equation"),
        t("Über einer gekrümmten Oberfläche ist der Dampfdruck höher. "
          "Bei 1 μm unmerklich, bei 0,01 μm 12 %. Deshalb entsteht kein "
          "Tropfen aus dem Nichts, und deshalb braucht jede Wolke "
          "Kondensationskerne.",
          "Over a curved surface the vapour pressure is higher. "
          "Negligible at 1 μm, 12 % at 0.01 μm. That is why no drop "
          "forms from nothing, and why every cloud needs condensation "
          "nuclei."),
        t("`r` Tropfenradius, m. `σ` Oberflächenspannung, 0,0756 N/m. "
          "`ρ_w` Dichte des Wassers, 1000 kg/m³. `R_v` 461,5 J/(kg·K). "
          "`T` Temperatur, K.",
          "`r` drop radius, m. `σ` surface tension, 0.0756 N/m. `ρ_w` "
          "water density, 1000 kg/m³. `R_v` 461.5 J/(kg·K). `T` "
          "temperature, K.")),
    formel("S(r) = 1 + a/r − b/r³",
        r"$S(r) = \frac{e}{e_s} \approx 1 + \frac{a}{r} - \frac{b}{r^3}, \qquad S_{krit} = 1 + \sqrt{\frac{4a^3}{27b}}$",
        t("Die Köhler-Kurve", "The Köhler curve"),
        t("Krümmung hebt den Dampfdruck (`a/r`), gelöstes Salz senkt ihn "
          "(`b/r³`, Raoult). Das Maximum ist die kritische Übersättigung: "
          "0,1 % für einen 0,1-μm-Salzkern. Darunter ist der Tropfen ein "
          "stabiler Dunsttropfen, darüber wächst er von selbst.",
          "Curvature raises the vapour pressure (`a/r`), dissolved salt "
          "lowers it (`b/r³`, Raoult). The maximum is the critical "
          "supersaturation: 0.1 % for a 0.1 μm salt nucleus. Below it "
          "the drop is a stable haze droplet, above it grows by "
          "itself."),
        t("`S` Sättigungsverhältnis. `a = 2σ/(ρ_w R_v T)`, m. `b` "
          "proportional zur gelösten Stoffmenge, m³. `r` Radius, m.",
          "`S` saturation ratio. `a = 2σ/(ρ_w R_v T)`, m. `b` "
          "proportional to the dissolved amount, m³. `r` radius, m.")),
],

"wo-wachstum": [
    formel("r·dr/dt = ξ·S  →  r² = r0² + 2·ξ·S·t",
        r"$r\,\frac{dr}{dt} = \xi\,S \quad\Rightarrow\quad r^2 = r_0^2 + 2\,\xi\,S\,t$",
        t("Diffusionswachstum eines Tropfens",
          "Diffusional growth of a drop"),
        t("Dampf diffundiert zum Tropfen, Wärme davon weg; beides geht "
          "mit `1/r`, also wächst `r²` linear. Schnell für kleine, "
          "hoffnungslos langsam für große Tropfen: Diffusion macht "
          "Wolken, keinen Regen.",
          "Vapour diffuses to the drop, heat away from it; both go as "
          "`1/r`, so `r²` grows linearly. Fast for small, hopelessly "
          "slow for large drops: diffusion makes clouds, not rain."),
        t("`r` Radius, m. `S` Übersättigung in Prozent. `ξ` "
          "Wachstumskoeffizient, etwa 6·10⁻¹³ m²/s je Prozent bei 0 °C.",
          "`r` radius, m. `S` supersaturation in per cent. `ξ` growth "
          "coefficient, about 6·10⁻¹³ m²/s per per cent at 0 °C.")),
    formel("v = 2·ρ_w·g·r² / (9·η)",
        r"$v_{Stokes} = \frac{2\,\rho_w\,g\,r^2}{9\,\eta}$",
        t("Fallgeschwindigkeit nach Stokes", "Stokes fall speed"),
        t("Gewicht gleich Reibung einer Kugel bei kleiner "
          "Reynolds-Zahl. Gilt bis etwa 50 μm; darüber wird der "
          "Widerstand turbulent, und ein Regentropfen von 1 mm fällt "
          "mit 4 m/s statt der 120 m/s, die Stokes verspräche.",
          "Weight equals the drag on a sphere at low Reynolds number. "
          "Holds up to about 50 μm; above that the drag turns "
          "turbulent, and a 1 mm raindrop falls at 4 m/s instead of "
          "the 120 m/s Stokes would promise."),
        t("`v` Fallgeschwindigkeit, m/s. `ρ_w` 1000 kg/m³. `r` Radius, "
          "m. `η` dynamische Viskosität der Luft, 1,8·10⁻⁵ Pa·s.",
          "`v` fall speed, m/s. `ρ_w` 1000 kg/m³. `r` radius, m. `η` "
          "dynamic viscosity of air, 1.8·10⁻⁵ Pa·s.")),
],

# --- 6 Dynamik ---------------------------------------------------------------

"dy-coriolis": [
    formel("dv/dt = −(1/ρ)∇p − 2Ω×v − Ω×(Ω×r) + g + F",
        r"$\frac{d\vec v}{dt} = -\frac{1}{\rho}\nabla p - 2\,\vec\Omega\times\vec v - \vec\Omega\times(\vec\Omega\times\vec r) + \vec g + \vec F$",
        t("Bewegungsgleichung im rotierenden System",
          "Equation of motion in the rotating frame"),
        t("Newton, umgeschrieben für einen mitrotierenden Beobachter. "
          "Die beiden neuen Terme sind Coriolis- und "
          "Zentrifugalbeschleunigung; letztere wird mit `g` zur "
          "effektiven Schwere zusammengefasst. Alles Weitere der "
          "Dynamik ist Skalenanalyse dieser Gleichung.",
          "Newton, rewritten for a co-rotating observer. The two new "
          "terms are Coriolis and centrifugal acceleration; the latter "
          "is folded into `g` as effective gravity. Everything else in "
          "dynamics is scale analysis of this equation."),
        t("`v` Wind relativ zur Erde, m/s. `Ω` Winkelgeschwindigkeit "
          "der Erde, 7,292·10⁻⁵ /s. `r` Ortsvektor von der Erdachse. "
          "`ρ` Dichte. `p` Druck. `F` Reibung je Masse.",
          "`v` wind relative to the Earth, m/s. `Ω` angular velocity "
          "of the Earth, 7.292·10⁻⁵ /s. `r` position vector from the "
          "axis. `ρ` density. `p` pressure. `F` friction per mass.")),
    formel("f = 2·Ω·sin φ",
        r"$f = 2\,\Omega\,\sin\varphi, \qquad Ro = \frac{U}{f\,L}$",
        t("Der Coriolis-Parameter", "The Coriolis parameter"),
        t("Die Vertikalkomponente von 2Ω -- nur sie lenkt waagrechten "
          "Wind waagrecht ab. Null am Äquator, 1,46·10⁻⁴ /s am Pol. Die "
          "Rossby-Zahl sagt, ob die Ablenkung zählt: unter 0,1 "
          "(Zyklonen) ja, über 10 (Gewitter, Badewanne) nein.",
          "The vertical component of 2Ω -- only it deflects horizontal "
          "wind horizontally. Zero at the equator, 1.46·10⁻⁴ /s at the "
          "pole. The Rossby number says whether the deflection "
          "matters: below 0.1 (cyclones) yes, above 10 (thunderstorms, "
          "bathtubs) no."),
        t("`f` Coriolis-Parameter, 1/s. `Ω` 7,292·10⁻⁵ /s. `φ` "
          "geographische Breite. `U` Windgeschwindigkeit, m/s. `L` "
          "Längenskala, m.",
          "`f` Coriolis parameter, 1/s. `Ω` 7.292·10⁻⁵ /s. `φ` "
          "latitude. `U` wind speed, m/s. `L` length scale, m.")),
],

"dy-geostrophisch": [
    formel("v_g = (1/(ρ·f)) · ∂p/∂n",
        r"$v_g = \frac{1}{\rho\,f}\,\frac{\partial p}{\partial n}, \qquad \vec v_g = \frac{1}{\rho f}\,\hat k\times\nabla p$",
        t("Der geostrophische Wind", "The geostrophic wind"),
        t("Druckgradient und Coriolis im Gleichgewicht, Wind parallel "
          "zu den Isobaren, Tief links (Nordhalbkugel). Gilt für `Ro ≪ 1`, "
          "gerade Isobaren und ohne Reibung -- also in der freien "
          "Atmosphäre auf 10-20 %, nicht in Bodennähe und nicht am "
          "Äquator.",
          "Pressure gradient and Coriolis in balance, wind parallel to "
          "the isobars, low on the left (northern hemisphere). Holds "
          "for `Ro ≪ 1`, straight isobars and no friction -- so in the "
          "free atmosphere to 10-20 %, not near the ground and not at "
          "the equator."),
        t("`v_g` geostrophischer Wind, m/s. `ρ` Dichte, kg/m³. `f` "
          "Coriolis-Parameter, 1/s. `∂p/∂n` Druckgradient quer zu den "
          "Isobaren, Pa/m. `k` Einheitsvektor nach oben.",
          "`v_g` geostrophic wind, m/s. `ρ` density, kg/m³. `f` "
          "Coriolis parameter, 1/s. `∂p/∂n` pressure gradient across "
          "the isobars, Pa/m. `k` unit vector upward.")),
    formel("v²/R + f·v = (1/ρ)·∂p/∂n",
        r"$\frac{v^2}{R} + f\,v = \frac{1}{\rho}\,\frac{\partial p}{\partial n}$",
        t("Die Gradientwindgleichung", "The gradient wind equation"),
        t("Mit Krümmung der Bahn (`R > 0` zyklonal, `R < 0` "
          "antizyklonal). Um das Tief subgeostrophisch, um das Hoch "
          "supergeostrophisch -- und für das Hoch nur lösbar, wenn der "
          "Druckgradient unter `ρf²|R|/4` bleibt: Hochs können keine "
          "Stürme sein.",
          "With curvature of the path (`R > 0` cyclonic, `R < 0` "
          "anticyclonic). Subgeostrophic around the low, "
          "supergeostrophic around the high -- and solvable for the "
          "high only if the pressure gradient stays below `ρf²|R|/4`: "
          "highs cannot be storms."),
        t("`v` Gradientwind, m/s. `R` Krümmungsradius der Bahn, m. `f` "
          "Coriolis-Parameter. `∂p/∂n` Druckgradient zum Tief hin.",
          "`v` gradient wind, m/s. `R` radius of curvature of the "
          "path, m. `f` Coriolis parameter. `∂p/∂n` pressure gradient "
          "toward the low.")),
],

"dy-thermisch": [
    formel("z2 − z1 = (R_L·T/g) · ln(p1/p2)",
        r"$z_2 - z_1 = \frac{R_L\,\overline{T}}{g}\,\ln\frac{p_1}{p_2}$",
        t("Die hypsometrische Gleichung", "The hypsometric equation"),
        t("Die Dicke einer Schicht zwischen zwei Druckflächen ist "
          "proportional zu ihrer mittleren (virtuellen) Temperatur. Das "
          "ist die Hydrostatik in Druckkoordinaten -- und der Grund, "
          "warum die 500-hPa-Fläche über warmer Luft höher liegt.",
          "The thickness of a layer between two pressure surfaces is "
          "proportional to its mean (virtual) temperature. That is "
          "hydrostatics in pressure coordinates -- and the reason the "
          "500 hPa surface lies higher over warm air."),
        t("`z` geopotentielle Höhe, m. `T` mittlere virtuelle Temperatur "
          "der Schicht, K. `p₁ > p₂` die beiden Druckflächen.",
          "`z` geopotential height, m. `T` mean virtual temperature of "
          "the layer, K. `p₁ > p₂` the two pressure surfaces.")),
    formel("∂v_g/∂ln p = −(R_L/f) · k × ∇T",
        r"$\frac{\partial \vec v_g}{\partial \ln p} = -\frac{R_L}{f}\,\hat k\times\nabla T$",
        t("Der thermische Wind", "The thermal wind"),
        t("Die Änderung des geostrophischen Windes mit der Höhe ist "
          "proportional zum horizontalen Temperaturgradienten und weht "
          "mit der kalten Luft zur Linken. Daraus folgt der Jetstream "
          "über der Polarfront und die Advektionsregel: rechtsdrehend "
          "warm, linksdrehend kalt.",
          "The change of the geostrophic wind with height is "
          "proportional to the horizontal temperature gradient and "
          "blows with the cold air on its left. From it follow the jet "
          "stream over the polar front and the advection rule: veering "
          "warm, backing cold."),
        t("`v_g` geostrophischer Wind, m/s. `p` Druck. `R_L` "
          "287 J/(kg·K). `f` Coriolis-Parameter. `∇T` horizontaler "
          "Temperaturgradient auf der Druckfläche, K/m.",
          "`v_g` geostrophic wind, m/s. `p` pressure. `R_L` "
          "287 J/(kg·K). `f` Coriolis parameter. `∇T` horizontal "
          "temperature gradient on the pressure surface, K/m.")),
],

"dy-reibung": [
    formel("D = π·√(2K/f),  w_E ≈ ζ_g·√(K/(2f))",
        r"$D = \pi\sqrt{\frac{2K}{f}}, \qquad w_E \approx \zeta_g\sqrt{\frac{K}{2f}}$",
        t("Ekman-Schicht und Ekman-Pumpen", "Ekman layer and Ekman pumping"),
        t("Die Dicke der Reibungsschicht und die Vertikalgeschwindigkeit "
          "an ihrer Oberkante, die die Bodenkonvergenz im Tief erzwingt. "
          "Ein konstantes `K` ist eine grobe Näherung; die Winddrehung "
          "von 45° wird real zu 10-30°. Die Größenordnungen stimmen.",
          "The depth of the friction layer and the vertical velocity at "
          "its top that the surface convergence in a low forces. A "
          "constant `K` is a crude approximation; the 45° wind turning "
          "becomes 10-30° in reality. The orders of magnitude hold."),
        t("`D` Ekman-Tiefe, m. `K` turbulenter Austauschkoeffizient, "
          "m²/s. `f` Coriolis-Parameter. `w_E` Vertikalgeschwindigkeit, "
          "m/s. `ζ_g` geostrophische Wirbelstärke, 1/s.",
          "`D` Ekman depth, m. `K` eddy diffusivity, m²/s. `f` "
          "Coriolis parameter. `w_E` vertical velocity, m/s. `ζ_g` "
          "geostrophic vorticity, 1/s.")),
],

# --- 7 Zirkulation -----------------------------------------------------------

"zi-hadley": [
    formel("u = Ω·a·sin²φ / cos φ",
        r"$u(\varphi) = \Omega\,a\,\frac{\sin^2\varphi}{\cos\varphi}$",
        t("Zonalwind aus Drehimpulserhaltung",
          "Zonal wind from angular momentum conservation"),
        t("Ein Paket, das am Äquator ohne Relativgeschwindigkeit startet "
          "und reibungsfrei polwärts wandert. 134 m/s bei 30°, 700 m/s "
          "bei 60°: unerreichbar, deshalb bricht die Hadley-Zelle bei "
          "30° in Wirbel auf. Reale Jets haben 40 m/s -- die Wirbel "
          "führen Drehimpuls ab.",
          "A parcel starting at the equator with no relative velocity "
          "and moving poleward without friction. 134 m/s at 30°, "
          "700 m/s at 60°: unreachable, so the Hadley cell breaks into "
          "eddies at 30°. Real jets have 40 m/s -- the eddies carry "
          "angular momentum away."),
        t("`u` Westwind relativ zur Erde, m/s. `Ω` 7,292·10⁻⁵ /s. `a` "
          "Erdradius, 6,371·10⁶ m. `φ` Breite.",
          "`u` westerly wind relative to the Earth, m/s. `Ω` "
          "7.292·10⁻⁵ /s. `a` Earth radius, 6.371·10⁶ m. `φ` "
          "latitude.")),
],

"zi-rossby": [
    formel("c = U − β/k²,  β = 2Ω·cos φ / a",
        r"$c = U - \frac{\beta}{k^2}, \qquad \beta = \frac{df}{dy} = \frac{2\,\Omega\cos\varphi}{a}$",
        t("Dispersionsrelation der Rossby-Welle",
          "Rossby wave dispersion relation"),
        t("Erhaltung der absoluten Wirbelstärke `ζ + f` in einer "
          "Strömung `U`. Die Wellen laufen relativ zur Strömung nach "
          "Westen, lange schneller als kurze; bei `k² = β/U` stehen sie "
          "still. Barotrop und linearisiert -- für die Mäander des "
          "Jetstreams die richtige Größenordnung.",
          "Conservation of absolute vorticity `ζ + f` in a flow `U`. "
          "The waves move westward relative to the flow, long ones "
          "faster than short; at `k² = β/U` they stand still. "
          "Barotropic and linearised -- the right order of magnitude "
          "for the jet stream's meanders."),
        t("`c` Phasengeschwindigkeit nach Osten, m/s. `U` Grundstrom, "
          "m/s. `k = 2π/L` Wellenzahl, 1/m. `β` Breitenänderung von `f`, "
          "1/(m·s). `a` Erdradius.",
          "`c` eastward phase speed, m/s. `U` mean flow, m/s. `k = 2π/L` "
          "wavenumber, 1/m. `β` latitudinal change of `f`, 1/(m·s). `a` "
          "Earth radius.")),
],

# --- 8 Synoptik --------------------------------------------------------------

"sy-fronten": [
    formel("tan α = (f·T/g) · Δu/ΔT",
        r"$\tan\alpha = \frac{f\,T}{g}\,\frac{\Delta u}{\Delta T}$",
        t("Margules: die Neigung einer Front",
          "Margules: the slope of a front"),
        t("Eine Frontfläche ist stationär, wenn der Windsprung quer zur "
          "Front den Dichtesprung geostrophisch trägt. 1:340 für "
          "10 m/s und 10 K in 45°. Je größer der Temperatursprung, "
          "desto flacher -- und ohne Rotation (`f = 0`) läge die Front "
          "flach am Boden.",
          "A frontal surface is stationary when the wind jump across "
          "the front carries the density jump geostrophically. 1:340 "
          "for 10 m/s and 10 K at 45°. The larger the temperature jump, "
          "the shallower -- and without rotation (`f = 0`) the front "
          "would lie flat on the ground."),
        t("`α` Neigungswinkel der Frontfläche. `f` Coriolis-Parameter. "
          "`T` mittlere Temperatur, K. `Δu` Sprung des frontparallelen "
          "Windes, m/s. `ΔT` Temperatursprung, K.",
          "`α` slope angle of the frontal surface. `f` Coriolis "
          "parameter. `T` mean temperature, K. `Δu` jump of the "
          "front-parallel wind, m/s. `ΔT` temperature jump, K.")),
],

"sy-zyklone": [
    formel("L ≈ 3,9 · N·H/f",
        r"$L_{max} \approx 3{,}9\,\frac{N\,H}{f}, \qquad L_R = \frac{N\,H}{f}$",
        t("Eady: die Wellenlänge der Zyklone",
          "Eady: the wavelength of the cyclone"),
        t("Die am schnellsten wachsende barokline Welle hat etwa die "
          "vierfache Länge des Rossby-Deformationsradius `L_R`: rund "
          "4000 km, Verdopplung in einem Tag. Eadys Modell ist "
          "linear, mit konstanter Scherung und ohne β -- und trifft "
          "die Größe der Tiefs trotzdem.",
          "The fastest-growing baroclinic wave has about four times "
          "the Rossby deformation radius `L_R`: about 4000 km, doubling "
          "in a day. Eady's model is linear, with constant shear and "
          "without β -- and still gets the size of lows right."),
        t("`L_max` Wellenlänge, m. `N` Brunt-Väisälä-Frequenz, 1/s. `H` "
          "Höhe der Troposphäre, m. `f` Coriolis-Parameter. `L_R` "
          "Rossby-Deformationsradius, m.",
          "`L_max` wavelength, m. `N` Brunt–Väisälä frequency, 1/s. `H` "
          "depth of the troposphere, m. `f` Coriolis parameter. `L_R` "
          "Rossby radius of deformation, m.")),
],

# --- 9 Mesoskala -------------------------------------------------------------

"me-foehn": [
    formel("ΔT_Föhn = (Γ_d − Γ_s) · (z_Kamm − z_LCL)",
        r"$\Delta T_{Foehn} = (\Gamma_d - \Gamma_s)\,(z_{Kamm} - z_{LCL})$",
        t("Der Temperaturgewinn des Föhns", "The temperature gain of the foehn"),
        t("Feucht hinauf mit `Γ_s`, trocken hinunter mit `Γ_d`; was "
          "bleibt, ist der Unterschied über die Strecke, auf der es "
          "geregnet hat. 1500 m Wolke mal 4 K/km geben 6 K. Gilt für "
          "das thermodynamische Bild; beim trockenen Föhn kommt die "
          "Wärme allein aus dem Absinken von Kammhöhe.",
          "Moist up at `Γ_s`, dry down at `Γ_d`; what remains is the "
          "difference over the distance it rained. 1500 m of cloud "
          "times 4 K/km gives 6 K. Holds for the thermodynamic picture; "
          "in dry foehn the warmth comes from descent from crest level "
          "alone."),
        t("`ΔT` Temperaturgewinn im Lee gegenüber dem Luv auf gleicher "
          "Höhe, K. `Γ_d` 9,8 K/km. `Γ_s` Feuchtadiabate, 5-6 K/km. "
          "`z_Kamm`, `z_LCL` Kammhöhe und Kondensationsniveau, m.",
          "`ΔT` temperature gain in the lee over the windward side at "
          "the same height, K. `Γ_d` 9.8 K/km. `Γ_s` moist adiabat, "
          "5-6 K/km. `z_Kamm`, `z_LCL` crest height and condensation "
          "level, m.")),
],

"me-seewind": [
    formel("dC/dt = −∮ dp/ρ",
        r"$\frac{dC}{dt} = -\oint \frac{dp}{\rho}, \qquad C = \oint \vec v\cdot d\vec l$",
        t("Der Zirkulationssatz von Bjerknes",
          "Bjerknes' circulation theorem"),
        t("Zirkulation entsteht nur, wo Druck- und Dichteflächen sich "
          "schneiden. Jede Masche aus Isobaren und Isosteren -- ein "
          "Solenoid -- treibt an, immer so, dass warme Luft steigt. "
          "Ohne Rotation; mit Erddrehung kommt ein Term für die "
          "Flächenänderung quer zu Ω hinzu.",
          "Circulation arises only where pressure and density surfaces "
          "intersect. Every mesh of isobars and isosteres -- a solenoid "
          "-- drives it, always so that warm air rises. Without "
          "rotation; with the Earth's spin a term for the area change "
          "across Ω is added."),
        t("`C` Zirkulation, m²/s. `v` Wind. `dl` Wegelement der "
          "geschlossenen Kurve. `p` Druck. `ρ` Dichte.",
          "`C` circulation, m²/s. `v` wind. `dl` path element of the "
          "closed curve. `p` pressure. `ρ` density.")),
],

"me-gewitter": [
    formel("v = √(4·ρ_Eis·g·D / (3·c_w·ρ_Luft))",
        r"$v_{Hagel} = \sqrt{\frac{4\,\rho_{Eis}\,g\,D}{3\,c_w\,\rho_{Luft}}}$",
        t("Fallgeschwindigkeit eines Hagelkorns",
          "Fall speed of a hailstone"),
        t("Gewicht gleich turbulentem Widerstand `½c_w ρ v² A`. 21 m/s "
          "für 2 cm, 33 m/s für 5 cm. Der Aufwind muss mindestens so "
          "stark sein, solange das Korn wächst -- deshalb braucht "
          "Großhagel CAPE über 2000 J/kg und die Scherung einer "
          "Superzelle.",
          "Weight equals turbulent drag `½c_d ρ v² A`. 21 m/s for 2 cm, "
          "33 m/s for 5 cm. The updraught must be at least that strong "
          "while the stone grows -- which is why giant hail needs CAPE "
          "above 2000 J/kg and the shear of a supercell."),
        t("`v` Fallgeschwindigkeit, m/s. `ρ_Eis` 900 kg/m³. `D` "
          "Durchmesser, m. `c_w` Widerstandsbeiwert, 0,6. `ρ_Luft` "
          "Luftdichte in Wolkenhöhe, 0,9 kg/m³.",
          "`v` fall speed, m/s. `ρ_Eis` 900 kg/m³. `D` diameter, m. "
          "`c_w` drag coefficient, 0.6. `ρ_Luft` air density at cloud "
          "level, 0.9 kg/m³.")),
],

# --- 10 Optik ----------------------------------------------------------------

"op-streuung": [
    formel("σ_Rayleigh ∝ 1/λ⁴,  V = 3,9/β",
        r"$\sigma_{R} \propto \frac{1}{\lambda^4}, \qquad V = \frac{-\ln 0{,}02}{\beta} = \frac{3{,}9}{\beta}$",
        t("Rayleigh-Streuung und Koschmieder-Sichtweite",
          "Rayleigh scattering and Koschmieder visibility"),
        t("Ein induzierter Dipol strahlt mit ω⁴: Blau 4,4-mal stärker "
          "als Rot. Gilt für Teilchen unter λ/10; Tröpfchen streuen "
          "nach Mie, farbneutral. Die Sichtweite folgt aus 2 % "
          "Restkontrast und exponentieller Abschwächung.",
          "An induced dipole radiates as ω⁴: blue 4.4 times more than "
          "red. Holds for particles below λ/10; droplets scatter by "
          "Mie, colour-neutral. Visibility follows from 2 % residual "
          "contrast and exponential attenuation."),
        t("`σ_R` Streuquerschnitt. `λ` Wellenlänge. `V` Sichtweite, m. "
          "`β` Extinktionskoeffizient, 1/m.",
          "`σ_R` scattering cross-section. `λ` wavelength. `V` "
          "visibility, m. `β` extinction coefficient, 1/m.")),
],

"op-regenbogen": [
    formel("δ = 180° + 2i − 4r,  cos i = √((n² − 1)/3)",
        r"$\delta = \pi + 2i - 4r, \qquad \cos i_{min} = \sqrt{\frac{n^2 - 1}{3}}$",
        t("Descartes: das Minimum der Ablenkung im Tropfen",
          "Descartes: the minimum deviation in the drop"),
        t("Zwei Brechungen und eine Reflexion. Bei `dδ/di = 0` häufen "
          "sich die Strahlen: 138° Ablenkung, der Bogen bei 42° vom "
          "Gegenpunkt der Sonne. Rot (n = 1,331) außen bei 42,4°, Blau "
          "(1,343) innen bei 40,6°. Mit zwei Reflexionen der Nebenbogen "
          "bei 51°.",
          "Two refractions and one reflection. At `dδ/di = 0` the rays "
          "pile up: 138° deviation, the bow at 42° from the antisolar "
          "point. Red (n = 1.331) outside at 42.4°, blue (1.343) inside "
          "at 40.6°. With two reflections the secondary bow at 51°."),
        t("`δ` Gesamtablenkung des Strahls. `i` Einfallswinkel, `r` "
          "Brechungswinkel (`sin i = n sin r`). `n` Brechzahl des "
          "Wassers, 1,33.",
          "`δ` total deviation of the ray. `i` angle of incidence, `r` "
          "angle of refraction (`sin i = n sin r`). `n` refractive "
          "index of water, 1.33.")),
    formel("δ_min = 2·arcsin(n·sin 30°) − 60°",
        r"$\delta_{min} = 2\arcsin\!\left(n\sin\frac{A}{2}\right) - A, \qquad A = 60^\circ$",
        t("Der 22°-Halo aus dem 60°-Prisma",
          "The 22° halo from the 60° prism"),
        t("Minimale Ablenkung eines Prismas bei symmetrischem "
          "Strahlengang. Mit `n = 1,31` für Eis: 21,8°. Die "
          "Eiskristalle sind zufällig orientiert, also wird jeder Winkel "
          "über 22° erreicht und 22° selbst am häufigsten -- der Ring "
          "ist innen scharf und rot, außen verwaschen.",
          "Minimum deviation of a prism with symmetric ray path. With "
          "`n = 1.31` for ice: 21.8°. The ice crystals are randomly "
          "oriented, so every angle above 22° occurs and 22° itself "
          "most often -- the ring is sharp and red inside, washed out "
          "outside."),
        t("`δ_min` kleinste Ablenkung. `A` Prismenwinkel, 60° zwischen "
          "zwei Seitenflächen des Sechsecks. `n` Brechzahl des Eises, "
          "1,31.",
          "`δ_min` smallest deviation. `A` prism angle, 60° between two "
          "side faces of the hexagon. `n` refractive index of ice, "
          "1.31.")),
],

# --- 11 Vorhersage -----------------------------------------------------------

"vo-numerik": [
    formel("Δt < Δx / c",
        r"$\Delta t < \frac{\Delta x}{c_{max}}$",
        t("Die CFL-Bedingung", "The CFL condition"),
        t("Ein expliziter Zeitschritt darf Information nicht weiter als "
          "eine Gitterzelle tragen, sonst explodiert die Lösung. Mit "
          "Schall 30 s auf 10 km; implizite Verfahren und hydrostatische "
          "Filterung schieben die Grenze zum Wind, semi-Lagrangesche "
          "Advektion hebt sie ganz auf.",
          "An explicit time step may not carry information further "
          "than one grid cell, or the solution blows up. With sound "
          "30 s on 10 km; implicit schemes and hydrostatic filtering "
          "move the limit to the wind, semi-Lagrangian advection "
          "removes it entirely."),
        t("`Δt` Zeitschritt, s. `Δx` Gitterweite, m. `c_max` schnellste "
          "Signalgeschwindigkeit im Modell, m/s.",
          "`Δt` time step, s. `Δx` grid spacing, m. `c_max` fastest "
          "signal speed in the model, m/s.")),
],

"vo-chaos": [
    formel("δ(t) = δ0 · exp(λ·t)",
        r"$\delta(t) = \delta_0\,e^{\lambda t}, \qquad t_{2} = \frac{\ln 2}{\lambda} \approx 2\ \mathrm{Tage}$",
        t("Exponentielles Fehlerwachstum", "Exponential error growth"),
        t("Der Lyapunov-Exponent der synoptischen Skala entspricht einer "
          "Verdopplung in etwa zwei Tagen. Zehnmal genauere "
          "Anfangsdaten kaufen `2·log₂10 = 6,6` Tage -- theoretisch; "
          "die Kaskade von den kleinen Skalen her macht die ersten "
          "Stunden schneller. Grenze: rund zwei Wochen.",
          "The Lyapunov exponent of the synoptic scale corresponds to a "
          "doubling in about two days. Ten times more accurate initial "
          "data buy `2·log₂10 = 6.6` days -- in theory; the cascade "
          "from the small scales makes the first hours faster. Limit: "
          "about two weeks."),
        t("`δ` Abstand zweier Modellzustände. `δ₀` Anfangsfehler. `λ` "
          "Lyapunov-Exponent, 1/s. `t₂` Verdopplungszeit.",
          "`δ` distance between two model states. `δ₀` initial error. "
          "`λ` Lyapunov exponent, 1/s. `t₂` doubling time.")),
],
}
