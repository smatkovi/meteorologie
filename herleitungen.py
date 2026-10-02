# -*- coding: utf-8 -*-
"""Die Herleitung jeder Formel des Kurses, deutsch und englisch.

Drei Regeln für jeden Eintrag:

1. **Jedes Formelzeichen wird definiert**, bevor es auftaucht.
2. **Jede Formel wird hergeleitet** -- auch die, die erst in einer
   Herleitung auftaucht. Eine Begründung, die ihrerseits eine
   unbegründete Formel benutzt, hat nichts erklärt, sondern verschoben.
   Deshalb stehen hier auch die Ableitungen der Einheitsvektoren im
   rotierenden System, bevor die Coriolis-Kraft daraus folgt.
3. **Jede sagt, wo sie aufhört zu gelten.**

Die Formeln stehen in TeX zwischen $...$ (in der Zeile) und $$...$$ (als
eigener Absatz); tools/formeln.py setzt sie beim Bauen. Die Texte sind
rohe Zeichenketten, damit die Backslashes bleiben, wie sie sind.
"""
from __future__ import unicode_literals


def t(de, en):
    return {"de": de, "en": en}


HERLEITUNGEN = {

# ---------------------------------------------------------------------------
"at-aufbau": t(r"""## Herleitung: die Gaskonstante der Mischung

Für jedes Gas $i$ gilt $p_i V = n_i R^* T$. Die Partialdrücke addieren sich (Dalton), also $pV = (\sum n_i)\,R^* T$. Mit der Masse $m = \sum n_i M_i$ und $\rho = m/V$:

$$p = \rho\,\frac{R^*}{M}\,T, \qquad M = \frac{\sum n_i M_i}{\sum n_i}$$

Die mittlere Molmasse ist also der mit den Stoffmengenanteilen gewogene Mittelwert: $0{,}78\cdot 28{,}01 + 0{,}21\cdot 32{,}00 + 0{,}0093\cdot 39{,}95 = 28{,}96$ g/mol. Daraus $R_L = 8{,}314/0{,}02896 = 287{,}1$ J/(kg·K).

**Wo es aufhört zu gelten:** Oberhalb von 100 km (Homopause) entmischt die Schwerkraft die Gase schneller, als Turbulenz sie mischt; dort hat jedes Gas seine eigene Skalenhöhe und $M$ fällt mit der Höhe. Darunter ist die Mischung konstant -- bis auf den Wasserdampf, der von 0 bis 4 % schwankt und $M$ um bis zu 1,5 % senkt. Das fängt die virtuelle Temperatur auf.""",
r"""## Derivation: the gas constant of the mixture

For each gas $i$, $p_i V = n_i R^* T$. Partial pressures add (Dalton), so $pV = (\sum n_i)\,R^* T$. With the mass $m = \sum n_i M_i$ and $\rho = m/V$:

$$p = \rho\,\frac{R^*}{M}\,T, \qquad M = \frac{\sum n_i M_i}{\sum n_i}$$

The mean molar mass is thus the mole-fraction-weighted mean: $0.78\cdot 28.01 + 0.21\cdot 32.00 + 0.0093\cdot 39.95 = 28.96$ g/mol. Hence $R_L = 8.314/0.02896 = 287.1$ J/(kg·K).

**Where it stops holding:** above 100 km (homopause) gravity separates the gases faster than turbulence mixes them; there each gas has its own scale height and $M$ falls with height. Below, the mixture is constant -- except for water vapour, which varies from 0 to 4 % and lowers $M$ by up to 1.5 %. The virtual temperature takes care of that."""),

# ---------------------------------------------------------------------------
"at-hydrostatik": t(r"""## Herleitung: Hydrostatik und Höhenformel

Eine Luftscheibe der Fläche $A$ und Dicke $dz$ hat die Masse $\rho A\,dz$. Von unten drückt $p(z)A$, von oben $p(z+dz)A$, nach unten zieht $\rho A\,dz\,g$. Ruhe (oder vernachlässigbare Vertikalbeschleunigung) verlangt

$$p(z)A - p(z+dz)A - \rho g A\,dz = 0 \quad\Rightarrow\quad \frac{dp}{dz} = -\rho g$$

Ob die Beschleunigung vernachlässigbar ist, sagt die Skalenanalyse: $w$ ändert sich um höchstens 10 m/s über 1000 s, also $dw/dt \approx 10^{-2}$ m/s², gegen $g = 10$. Selbst im Gewitter ist der Fehler ein Promille.

Jetzt die Zustandsgleichung $\rho = p/(R_L T)$ einsetzen:

$$\frac{dp}{p} = -\frac{g}{R_L T}\,dz$$

Für $T = \mathrm{const}$ integriert sich das zu $\ln(p/p_0) = -gz/(R_L T)$, also $p = p_0\,e^{-z/H}$ mit $H = R_L T/g$. Für beliebiges $T(z)$ bleibt

$$p(z) = p_0\exp\!\left(-\int_0^z \frac{g}{R_L T(z')}\,dz'\right)$$

-- die Skalenhöhe ist dann eine lokale Größe, und die Höhenformel ein Integral über $1/T$.

**Die Masse der Säule:** $\int_0^\infty \rho\,dz = \int_{p_0}^{0}\frac{-dp}{g} = p_0/g$. Unabhängig vom Temperaturprofil -- das Barometer wiegt die Luft.

**Ein Hektopascal in Metern:** $dz = -dp/(\rho g)$. Mit $\rho = 1{,}225$: $100/(1{,}225\cdot 9{,}81) = 8{,}3$ m. In 5,5 km ist $\rho = 0{,}7$: 14,6 m.

**Wo es aufhört zu gelten:** In Gewitteraufwinden, Lee-Wellen und auf Skalen unter 10 km verlangt die Vertikalgleichung einen Beschleunigungsterm; dort rechnet man nicht-hydrostatisch. Die Höhenformel mit konstantem $T$ ist auf 10 % genau; mit dem Standardgradienten exakt im Rahmen der Vereinbarung.""",
r"""## Derivation: hydrostatics and the barometric formula

A slab of air with area $A$ and thickness $dz$ has mass $\rho A\,dz$. From below $p(z)A$ pushes, from above $p(z+dz)A$, downward pulls $\rho A\,dz\,g$. Rest (or negligible vertical acceleration) requires

$$p(z)A - p(z+dz)A - \rho g A\,dz = 0 \quad\Rightarrow\quad \frac{dp}{dz} = -\rho g$$

Whether the acceleration is negligible is told by scale analysis: $w$ changes by at most 10 m/s over 1000 s, so $dw/dt \approx 10^{-2}$ m/s², against $g = 10$. Even in a thunderstorm the error is a tenth of a per cent.

Now insert the equation of state $\rho = p/(R_L T)$:

$$\frac{dp}{p} = -\frac{g}{R_L T}\,dz$$

For $T = \mathrm{const}$ this integrates to $\ln(p/p_0) = -gz/(R_L T)$, so $p = p_0\,e^{-z/H}$ with $H = R_L T/g$. For arbitrary $T(z)$ what remains is

$$p(z) = p_0\exp\!\left(-\int_0^z \frac{g}{R_L T(z')}\,dz'\right)$$

-- the scale height is then a local quantity, and the barometric formula an integral over $1/T$.

**The mass of the column:** $\int_0^\infty \rho\,dz = \int_{p_0}^{0}\frac{-dp}{g} = p_0/g$. Independent of the temperature profile -- the barometer weighs the air.

**One hectopascal in metres:** $dz = -dp/(\rho g)$. With $\rho = 1.225$: $100/(1.225\cdot 9.81) = 8.3$ m. At 5.5 km $\rho = 0.7$: 14.6 m.

**Where it stops holding:** in thunderstorm updraughts, lee waves and on scales below 10 km the vertical equation needs an acceleration term; there one computes non-hydrostatically. The formula with constant $T$ is accurate to 10 %; with the standard lapse rate exact within the convention."""),

# ---------------------------------------------------------------------------
"at-standard": t(r"""## Herleitung: Druck bei linearem Gradienten

Mit $T(z) = T_0 - \Gamma z$ wird die hydrostatische Gleichung

$$\frac{dp}{p} = -\frac{g}{R_L}\,\frac{dz}{T_0 - \Gamma z}$$

Die rechte Seite ist $\frac{g}{R_L\Gamma}\,\frac{d(T_0 - \Gamma z)}{T_0 - \Gamma z}$, also

$$\ln\frac{p}{p_0} = \frac{g}{R_L\Gamma}\,\ln\frac{T_0 - \Gamma z}{T_0} \quad\Rightarrow\quad p = p_0\left(1 - \frac{\Gamma z}{T_0}\right)^{g/(R_L\Gamma)}$$

Der Exponent: $9{,}80665/(287{,}05\cdot 0{,}0065) = 5{,}256$. Für $\Gamma \to 0$ wird $(1 - \Gamma z/T_0)^{1/\Gamma} \to e^{-z/T_0}$, und die Exponentialform kommt zurück -- die Probe, dass beide Formeln dieselbe Physik sind.

**Umgekehrt**, Höhe aus Druck (so rechnet der Höhenmesser):

$$z = \frac{T_0}{\Gamma}\left[1 - \left(\frac{p}{p_0}\right)^{R_L\Gamma/g}\right] = 44\,331\,\mathrm{m}\cdot\left[1 - \left(\frac{p}{p_0}\right)^{0{,}1903}\right]$$

**Der Temperaturfehler:** Ist die wirkliche Luft um $\Delta T$ kälter als Standard, sind alle Schichtdicken um den Faktor $T/T_{std}$ kleiner. Die angezeigte Höhe $z_i$ und die wahre $z_w$ verhalten sich wie $z_w \approx z_i\,(1 - \Delta T/T_{std})$: bei 20 K und 288 K sind das 7 %. Die Faustregel „4 % je 10 K" stimmt also auf die Hälfte genau.

**Wo es aufhört zu gelten:** Über 11 km ist $\Gamma = 0$, und es gilt wieder die Exponentialformel mit $T = 216{,}65$ K ab $p = 226{,}3$ hPa. Und die wirkliche Atmosphäre hat nie genau 6,5 K/km -- die Vereinbarung ist eine Rechengrundlage, kein Messwert.""",
r"""## Derivation: pressure for a linear lapse rate

With $T(z) = T_0 - \Gamma z$ the hydrostatic equation becomes

$$\frac{dp}{p} = -\frac{g}{R_L}\,\frac{dz}{T_0 - \Gamma z}$$

The right-hand side is $\frac{g}{R_L\Gamma}\,\frac{d(T_0 - \Gamma z)}{T_0 - \Gamma z}$, hence

$$\ln\frac{p}{p_0} = \frac{g}{R_L\Gamma}\,\ln\frac{T_0 - \Gamma z}{T_0} \quad\Rightarrow\quad p = p_0\left(1 - \frac{\Gamma z}{T_0}\right)^{g/(R_L\Gamma)}$$

The exponent: $9.80665/(287.05\cdot 0.0065) = 5.256$. For $\Gamma \to 0$, $(1 - \Gamma z/T_0)^{1/\Gamma} \to e^{-z/T_0}$, and the exponential form returns -- the check that both formulas are the same physics.

**Inverted**, height from pressure (this is how the altimeter computes):

$$z = \frac{T_0}{\Gamma}\left[1 - \left(\frac{p}{p_0}\right)^{R_L\Gamma/g}\right] = 44\,331\,\mathrm{m}\cdot\left[1 - \left(\frac{p}{p_0}\right)^{0.1903}\right]$$

**The temperature error:** if the real air is colder than standard by $\Delta T$, all thicknesses are smaller by the factor $T/T_{std}$. Indicated height $z_i$ and true height $z_w$ relate as $z_w \approx z_i\,(1 - \Delta T/T_{std})$: for 20 K and 288 K that is 7 %. The rule of thumb "4 % per 10 K" is thus accurate to within a factor of two.

**Where it stops holding:** above 11 km $\Gamma = 0$, and the exponential formula applies again with $T = 216.65$ K from $p = 226.3$ hPa. And the real atmosphere never has exactly 6.5 K/km -- the convention is a basis for calculation, not a measurement."""),

# ---------------------------------------------------------------------------
"th-adiabate": t(r"""## Herleitung: der erste Hauptsatz für ein Luftpaket

Für ein Kilogramm Luft lautet der erste Hauptsatz $\delta q = du + p\,d\alpha$ mit der inneren Energie $u = c_v T$ und dem spezifischen Volumen $\alpha = 1/\rho$. Mit $p\alpha = R_L T$ ist $p\,d\alpha = R_L\,dT - \alpha\,dp$, also

$$\delta q = (c_v + R_L)\,dT - \alpha\,dp = c_p\,dT - \alpha\,dp$$

Das ist die Form, in der die Meteorologie den ersten Hauptsatz benutzt: $c_p = c_v + R_L = 717 + 287 = 1004$ J/(kg·K). Die Ausdehnungsarbeit steckt im Übergang von $c_v$ zu $c_p$ -- und im Term $-\alpha\,dp$ steckt, was das Paket zusätzlich leistet, wenn sich sein Druck ändert.

Adiabatisch: $\delta q = 0$. Hydrostatisch (das Paket hat den Umgebungsdruck): $dp = -\rho g\,dz$, also $\alpha\,dp = -g\,dz$. Einsetzen:

$$c_p\,dT + g\,dz = 0 \quad\Rightarrow\quad \Gamma_d = -\frac{dT}{dz} = \frac{g}{c_p} = \frac{9{,}81}{1004} = 9{,}77\cdot 10^{-3}\,\mathrm{K/m}$$

Eine zweite Lesart: $c_p T + gz$ ist erhalten -- die **trockenstatische Energie**. Was das Paket an Höhe gewinnt, bezahlt es mit Temperatur, und $c_p$ ist der Wechselkurs.

**Wo es aufhört zu gelten:** Sobald Dampf kondensiert, ist $\delta q = -L_v\,dr_s \ne 0$ und die Feuchtadiabate übernimmt. Strahlung liefert etwa 1-2 K je Tag, also auf Zeitskalen von Stunden vernachlässigbar, über Tage nicht. Und das Paket muss klein genug sein, um dem Umgebungsdruck augenblicklich zu folgen -- bei Schallgeschwindigkeit ist das für alles unter 10 km erfüllt.""",
r"""## Derivation: the first law for a parcel

For one kilogram of air the first law reads $\delta q = du + p\,d\alpha$ with internal energy $u = c_v T$ and specific volume $\alpha = 1/\rho$. With $p\alpha = R_L T$, $p\,d\alpha = R_L\,dT - \alpha\,dp$, so

$$\delta q = (c_v + R_L)\,dT - \alpha\,dp = c_p\,dT - \alpha\,dp$$

That is the form in which meteorology uses the first law: $c_p = c_v + R_L = 717 + 287 = 1004$ J/(kg·K). The expansion work sits in the step from $c_v$ to $c_p$ -- and the term $-\alpha\,dp$ holds what the parcel does in addition when its pressure changes.

Adiabatic: $\delta q = 0$. Hydrostatic (the parcel has the ambient pressure): $dp = -\rho g\,dz$, so $\alpha\,dp = -g\,dz$. Substituting:

$$c_p\,dT + g\,dz = 0 \quad\Rightarrow\quad \Gamma_d = -\frac{dT}{dz} = \frac{g}{c_p} = \frac{9.81}{1004} = 9.77\cdot 10^{-3}\,\mathrm{K/m}$$

A second reading: $c_p T + gz$ is conserved -- the **dry static energy**. What the parcel gains in height it pays in temperature, and $c_p$ is the exchange rate.

**Where it stops holding:** as soon as vapour condenses, $\delta q = -L_v\,dr_s \ne 0$ and the moist adiabat takes over. Radiation supplies about 1-2 K per day, negligible on time scales of hours, not over days. And the parcel must be small enough to follow the ambient pressure instantly -- at the speed of sound that is satisfied for anything below 10 km."""),

# ---------------------------------------------------------------------------
"th-theta": t(r"""## Herleitung: Poisson und die potentielle Temperatur

Aus $c_p\,dT = \alpha\,dp = R_L T\,dp/p$ (adiabatischer erster Hauptsatz) folgt durch Trennung der Variablen

$$\frac{dT}{T} = \frac{R_L}{c_p}\,\frac{dp}{p} = \kappa\,\frac{dp}{p} \quad\Rightarrow\quad T\,p^{-\kappa} = \mathrm{const}$$

Das ist die Poisson-Gleichung; $\kappa = 287/1004 = 0{,}286 = 2/7$ für ein zweiatomiges Gas. Die Konstante wird festgelegt, indem man das Paket gedanklich auf $p_0 = 1000$ hPa bringt und die Temperatur dort $\theta$ nennt:

$$\theta = T\left(\frac{p_0}{p}\right)^{\kappa}$$

**Warum das die Entropie ist:** $ds = \delta q/T = c_p\,dT/T - R_L\,dp/p = c_p\,d(\ln T - \kappa\ln p) = c_p\,d\ln\theta$. Also $s = c_p\ln\theta + \mathrm{const}$. Adiabatisch heißt isentrop heißt $\theta = \mathrm{const}$ -- drei Namen für dieselbe Aussage.

**Warum $\theta$ mit der Höhe steigt:** $\frac{1}{\theta}\frac{d\theta}{dz} = \frac{1}{T}\frac{dT}{dz} - \frac{\kappa}{p}\frac{dp}{dz} = \frac{1}{T}\left(-\Gamma + \frac{\kappa\rho g T}{p}\right) = \frac{1}{T}\left(\Gamma_d - \Gamma\right)$, weil $\kappa\rho g T/p = \kappa g/R_L = g/c_p$. Also

$$\frac{d\theta}{dz} = \frac{\theta}{T}\,(\Gamma_d - \Gamma)$$

Mit $\Gamma = 6{,}5$ und $\theta \approx T$: 3,3 K/km. Die Stabilitätsfrage ist damit die Frage nach dem Vorzeichen von $d\theta/dz$.

**Wo es aufhört zu gelten:** Bei Kondensation ist $\theta$ nicht erhalten -- dann $\theta_e$. Bei $\kappa$ für feuchte Luft ($c_p$ und $R$ ändern sich um je 1 %) ist der Unterschied ein Zehntel Kelvin. Über 80 km ist $c_p$ nicht mehr konstant, weil die Luft dissoziiert.""",
r"""## Derivation: Poisson and the potential temperature

From $c_p\,dT = \alpha\,dp = R_L T\,dp/p$ (adiabatic first law) separation of variables gives

$$\frac{dT}{T} = \frac{R_L}{c_p}\,\frac{dp}{p} = \kappa\,\frac{dp}{p} \quad\Rightarrow\quad T\,p^{-\kappa} = \mathrm{const}$$

That is Poisson's relation; $\kappa = 287/1004 = 0.286 = 2/7$ for a diatomic gas. The constant is fixed by imagining the parcel brought to $p_0 = 1000$ hPa and calling its temperature there $\theta$:

$$\theta = T\left(\frac{p_0}{p}\right)^{\kappa}$$

**Why that is the entropy:** $ds = \delta q/T = c_p\,dT/T - R_L\,dp/p = c_p\,d(\ln T - \kappa\ln p) = c_p\,d\ln\theta$. So $s = c_p\ln\theta + \mathrm{const}$. Adiabatic means isentropic means $\theta = \mathrm{const}$ -- three names for the same statement.

**Why $\theta$ rises with height:** $\frac{1}{\theta}\frac{d\theta}{dz} = \frac{1}{T}\frac{dT}{dz} - \frac{\kappa}{p}\frac{dp}{dz} = \frac{1}{T}\left(-\Gamma + \frac{\kappa\rho g T}{p}\right) = \frac{1}{T}\left(\Gamma_d - \Gamma\right)$, because $\kappa\rho g T/p = \kappa g/R_L = g/c_p$. Hence

$$\frac{d\theta}{dz} = \frac{\theta}{T}\,(\Gamma_d - \Gamma)$$

With $\Gamma = 6.5$ and $\theta \approx T$: 3.3 K/km. The stability question is thus the question of the sign of $d\theta/dz$.

**Where it stops holding:** with condensation $\theta$ is not conserved -- then $\theta_e$. For $\kappa$ of moist air ($c_p$ and $R$ change by 1 % each) the difference is a tenth of a kelvin. Above 80 km $c_p$ is no longer constant because the air dissociates."""),

# ---------------------------------------------------------------------------
"th-stabilitaet": t(r"""## Herleitung: der Auftriebsoszillator

Ein Paket mit Dichte $\rho'$ in einer Umgebung $\rho$ erfährt je Masse die Beschleunigung (Archimedes) $g\,(\rho - \rho')/\rho'$. Bei gleichem Druck ist $\rho \propto 1/T$, also

$$\frac{d^2 z}{dt^2} = g\,\frac{T' - T}{T}$$

Das Paket werde aus der Höhe $z_0$ (wo $T' = T$) um $\delta z$ gehoben. Es kühlt mit $\Gamma_d$, die Umgebung hat $\Gamma$: $T' - T = -(\Gamma_d - \Gamma)\,\delta z$. Also

$$\frac{d^2\delta z}{dt^2} = -\frac{g}{T}\,(\Gamma_d - \Gamma)\,\delta z = -N^2\,\delta z$$

Ein harmonischer Oszillator mit $N^2 = \frac{g}{T}(\Gamma_d - \Gamma)$, und mit $d\theta/dz = \frac{\theta}{T}(\Gamma_d - \Gamma)$ aus der vorigen Lektion gleichbedeutend

$$N^2 = \frac{g}{\theta}\,\frac{d\theta}{dz}$$

Für $N^2 > 0$: Schwingung mit Periode $2\pi/N$ (Standardatmosphäre: $N^2 = 9{,}81/288\cdot 3{,}3\cdot 10^{-3} = 1{,}12\cdot 10^{-4}$, $N = 0{,}0106$ /s, 9,9 min). Für $N^2 < 0$: $\delta z \propto e^{|N|t}$, exponentielles Wachstum -- labil. Für $N = 0$: das Paket bleibt, wo man es hinlegt -- neutral.

**Was man daraus misst:** Lee-Wellen haben die Wellenlänge $\lambda = 2\pi U/N$; mit $U = 15$ m/s und $N = 0{,}01$: 9,4 km -- der Abstand der Lenticularis-Wolken hinter einem Gebirgskamm. Das ist die Brunt-Väisälä-Frequenz, mit dem Auge gemessen.

**Wo es aufhört zu gelten:** Die Rechnung linearisiert in $\delta z$ und vernachlässigt, dass das Paket Umgebungsluft mitreißen muss (dadurch schwingt es langsamer) und Luft einmischt. Für gesättigte Luft ist $\Gamma_s$ statt $\Gamma_d$ einzusetzen -- und dann kann dieselbe Schichtung stabil für trockene und labil für feuchte Pakete sein.""",
r"""## Derivation: the buoyancy oscillator

A parcel of density $\rho'$ in an environment $\rho$ experiences per mass the acceleration (Archimedes) $g\,(\rho - \rho')/\rho'$. At equal pressure $\rho \propto 1/T$, so

$$\frac{d^2 z}{dt^2} = g\,\frac{T' - T}{T}$$

Let the parcel be lifted from height $z_0$ (where $T' = T$) by $\delta z$. It cools at $\Gamma_d$, the environment has $\Gamma$: $T' - T = -(\Gamma_d - \Gamma)\,\delta z$. Hence

$$\frac{d^2\delta z}{dt^2} = -\frac{g}{T}\,(\Gamma_d - \Gamma)\,\delta z = -N^2\,\delta z$$

A harmonic oscillator with $N^2 = \frac{g}{T}(\Gamma_d - \Gamma)$, and with $d\theta/dz = \frac{\theta}{T}(\Gamma_d - \Gamma)$ from the previous lesson equivalently

$$N^2 = \frac{g}{\theta}\,\frac{d\theta}{dz}$$

For $N^2 > 0$: oscillation with period $2\pi/N$ (standard atmosphere: $N^2 = 9.81/288\cdot 3.3\cdot 10^{-3} = 1.12\cdot 10^{-4}$, $N = 0.0106$ /s, 9.9 min). For $N^2 < 0$: $\delta z \propto e^{|N|t}$, exponential growth -- unstable. For $N = 0$: the parcel stays wherever it is put -- neutral.

**What one measures from it:** lee waves have wavelength $\lambda = 2\pi U/N$; with $U = 15$ m/s and $N = 0.01$: 9.4 km -- the spacing of lenticular clouds behind a ridge. That is the Brunt–Väisälä frequency, measured by eye.

**Where it stops holding:** the calculation is linear in $\delta z$ and neglects that the parcel must drag ambient air along (which slows the oscillation) and entrains air. For saturated air $\Gamma_s$ replaces $\Gamma_d$ -- and then the same stratification can be stable for dry and unstable for moist parcels."""),

# ---------------------------------------------------------------------------
"fe-dampf": t(r"""## Herleitung: Clausius-Clapeyron

Im Gleichgewicht zweier Phasen sind ihre spezifischen freien Enthalpien gleich, $g_w = g_v$, und zwar entlang der ganzen Dampfdruckkurve: $dg_w = dg_v$. Mit $dg = -s\,dT + \alpha\,dp$ für jede Phase:

$$-s_w\,dT + \alpha_w\,de_s = -s_v\,dT + \alpha_v\,de_s \quad\Rightarrow\quad \frac{de_s}{dT} = \frac{s_v - s_w}{\alpha_v - \alpha_w} = \frac{L_v}{T\,(\alpha_v - \alpha_w)}$$

weil der Entropiesprung beim Verdampfen $L_v/T$ ist. Nun ist $\alpha_w = 10^{-3}$ m³/kg gegen $\alpha_v = R_v T/e_s \approx 200$ m³/kg bei 0 °C -- also $\alpha_w$ weglassen:

$$\frac{de_s}{dT} = \frac{L_v\,e_s}{R_v\,T^2}$$

Integration mit konstantem $L_v$: $\ln(e_s/e_0) = \frac{L_v}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)$. Die relative Steigung $\frac{1}{e_s}\frac{de_s}{dT} = \frac{L_v}{R_v T^2} = \frac{2{,}5\cdot 10^6}{461{,}5\cdot 288^2} = 0{,}065$ /K: **6,5 % je Kelvin**, Verdopplung alle 11 K.

Die Magnus-Formel ist eine Anpassung an Messungen, die die Temperaturabhängigkeit von $L_v$ (−2,4 kJ/kg je K) mit erledigt. Für Eis ist $L_s = L_v + L_f = 2{,}83$ MJ/kg einzusetzen; die Kurve ist steiler, und bei −12 °C liegt $e_s$ über Eis um 12 % unter dem über Wasser -- Bergeron.

**Mischungsverhältnis:** $r = \rho_v/\rho_d = \frac{e/(R_v T)}{(p-e)/(R_L T)} = \frac{R_L}{R_v}\,\frac{e}{p-e} = 0{,}622\,\frac{e}{p-e}$.

**Virtuelle Temperatur:** Die Dichte der Mischung ist $\rho = \frac{p-e}{R_L T} + \frac{e}{R_v T} = \frac{p}{R_L T}\left[1 - \frac{e}{p}\left(1 - \frac{R_L}{R_v}\right)\right]$. Man definiert $T_v$ so, dass $\rho = p/(R_L T_v)$: $T_v = T/[1 - 0{,}378\,e/p] \approx T\,(1 + 0{,}61\,r)$ nach Entwicklung in $r$.

**Wo es aufhört zu gelten:** Unter −40 °C ist flüssiges Wasser praktisch nicht mehr unterkühlbar; über Lösungen (Köhler) und über gekrümmten Flächen (Kelvin) gelten Korrekturen -- das nächste Kapitel.""",
r"""## Derivation: Clausius–Clapeyron

In equilibrium of two phases their specific free enthalpies are equal, $g_w = g_v$, and that along the whole vapour pressure curve: $dg_w = dg_v$. With $dg = -s\,dT + \alpha\,dp$ for each phase:

$$-s_w\,dT + \alpha_w\,de_s = -s_v\,dT + \alpha_v\,de_s \quad\Rightarrow\quad \frac{de_s}{dT} = \frac{s_v - s_w}{\alpha_v - \alpha_w} = \frac{L_v}{T\,(\alpha_v - \alpha_w)}$$

because the entropy jump on evaporation is $L_v/T$. Now $\alpha_w = 10^{-3}$ m³/kg against $\alpha_v = R_v T/e_s \approx 200$ m³/kg at 0 °C -- so drop $\alpha_w$:

$$\frac{de_s}{dT} = \frac{L_v\,e_s}{R_v\,T^2}$$

Integration with constant $L_v$: $\ln(e_s/e_0) = \frac{L_v}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)$. The relative slope $\frac{1}{e_s}\frac{de_s}{dT} = \frac{L_v}{R_v T^2} = \frac{2.5\cdot 10^6}{461.5\cdot 288^2} = 0.065$ /K: **6.5 % per kelvin**, doubling every 11 K.

The Magnus formula is a fit to measurements that also takes care of the temperature dependence of $L_v$ (−2.4 kJ/kg per K). For ice $L_s = L_v + L_f = 2.83$ MJ/kg is used; the curve is steeper, and at −12 °C $e_s$ over ice is 12 % below that over water -- Bergeron.

**Mixing ratio:** $r = \rho_v/\rho_d = \frac{e/(R_v T)}{(p-e)/(R_L T)} = \frac{R_L}{R_v}\,\frac{e}{p-e} = 0.622\,\frac{e}{p-e}$.

**Virtual temperature:** the density of the mixture is $\rho = \frac{p-e}{R_L T} + \frac{e}{R_v T} = \frac{p}{R_L T}\left[1 - \frac{e}{p}\left(1 - \frac{R_L}{R_v}\right)\right]$. One defines $T_v$ such that $\rho = p/(R_L T_v)$: $T_v = T/[1 - 0.378\,e/p] \approx T\,(1 + 0.61\,r)$ after expanding in $r$.

**Where it stops holding:** below −40 °C liquid water can practically no longer be supercooled; over solutions (Köhler) and over curved surfaces (Kelvin) corrections apply -- the next chapter."""),

# ---------------------------------------------------------------------------
"fe-hebung": t(r"""## Herleitung: Taupunktgradient, LCL und Feuchtadiabate

**Der Taupunkt beim Steigen.** Das Mischungsverhältnis bleibt erhalten, also $e/p = \mathrm{const}$ und $de/e = dp/p = -g\,dz/(R_L T)$. Der Taupunkt ist definiert durch $e = e_s(T_d)$, also $de/e = \frac{L_v}{R_v T_d^2}\,dT_d$ (Clausius-Clapeyron). Gleichsetzen:

$$\frac{dT_d}{dz} = -\frac{g\,R_v\,T_d^2}{R_L\,L_v\,T} \approx -\frac{9{,}81\cdot 461{,}5\cdot 285}{287\cdot 2{,}5\cdot 10^6} = -1{,}8\cdot 10^{-3}\,\mathrm{K/m}$$

Rund 1,7 bis 1,8 K/km. Die Spreizung $T - T_d$ schließt sich also mit $9{,}8 - 1{,}8 = 8{,}0$ K/km, und $z_{LCL} = (T - T_d)/8{,}0$ K/km $= 125$ m je Kelvin. Die Zahl ist kein Messwert, sondern $1000/(\Gamma_d - \Gamma_{T_d})$.

**Die Feuchtadiabate.** Jetzt ist $\delta q = -L_v\,dr_s$: Was kondensiert, heizt. Der erste Hauptsatz:

$$c_p\,dT - \alpha\,dp = -L_v\,dr_s \quad\Rightarrow\quad c_p\,dT + g\,dz = -L_v\,dr_s$$

$r_s(T, p)$ hängt von beidem ab: $dr_s = \frac{\partial r_s}{\partial T}dT + \frac{\partial r_s}{\partial p}dp$. Mit $r_s \approx 0{,}622\,e_s/p$: $\frac{\partial r_s}{\partial T} = r_s\frac{L_v}{R_v T^2}$ und $\frac{\partial r_s}{\partial p} = -r_s/p$, also $\frac{\partial r_s}{\partial p}dp = r_s\,g\,dz/(R_L T)$. Alles nach $dT/dz$ auflösen:

$$\Gamma_s = -\frac{dT}{dz} = \frac{g}{c_p}\;\frac{1 + \dfrac{L_v\,r_s}{R_L\,T}}{1 + \dfrac{0{,}622\,L_v^2\,r_s}{c_p\,R_L\,T^2}}$$

Der Zähler ist nahe 1 (die Druckabhängigkeit von $r_s$); der Nenner ist der eigentliche Effekt, die Wärme je Grad Abkühlung. Bei 0 °C, 1000 hPa: $r_s = 3{,}8$ g/kg, Zähler 1,12, Nenner 1,69, $\Gamma_s = 6{,}5$ K/km. Bei 20 °C: 4,2 K/km. Bei −40 °C: 9,5 K/km.

**$\theta_e$.** Teilt man den feuchten ersten Hauptsatz durch $T$ und nutzt $ds = c_p\,d\ln\theta$: $c_p\,d\ln\theta = -L_v\,dr_s/T$. Mit der Näherung, dass $L_v/T$ gegenüber $r_s$ langsam variiert, integriert sich das zu $c_p\ln\theta + L_v r_s/T = \mathrm{const}$, also

$$\theta_e = \theta\,\exp\!\left(\frac{L_v\,r_s}{c_p\,T}\right)$$

ausgewertet am Kondensationsniveau. Für ungesättigte Luft nimmt man $r$ statt $r_s$ und $T_{LCL}$ -- die Größe, die das Paket hätte, wenn es gehoben würde.

**Wo es aufhört zu gelten:** Die Pseudoadiabate lässt das Kondensat sofort ausfallen; behält man es im Paket (reversibel), ist $\Gamma_s$ um einige Zehntel K/km kleiner. Unter 0 °C müsste $L_s$ für die Eisbildung stehen -- in der Praxis friert die Wolke verzögert, und die Schmelzwärme bringt noch einmal 1 K.""",
r"""## Derivation: dew point lapse rate, LCL and the moist adiabat

**The dew point on ascent.** The mixing ratio is conserved, so $e/p = \mathrm{const}$ and $de/e = dp/p = -g\,dz/(R_L T)$. The dew point is defined by $e = e_s(T_d)$, so $de/e = \frac{L_v}{R_v T_d^2}\,dT_d$ (Clausius–Clapeyron). Equating:

$$\frac{dT_d}{dz} = -\frac{g\,R_v\,T_d^2}{R_L\,L_v\,T} \approx -\frac{9.81\cdot 461.5\cdot 285}{287\cdot 2.5\cdot 10^6} = -1.8\cdot 10^{-3}\,\mathrm{K/m}$$

About 1.7 to 1.8 K/km. The spread $T - T_d$ thus closes at $9.8 - 1.8 = 8.0$ K/km, and $z_{LCL} = (T - T_d)/8.0$ K/km $= 125$ m per kelvin. The number is not a measurement but $1000/(\Gamma_d - \Gamma_{T_d})$.

**The moist adiabat.** Now $\delta q = -L_v\,dr_s$: what condenses heats. The first law:

$$c_p\,dT - \alpha\,dp = -L_v\,dr_s \quad\Rightarrow\quad c_p\,dT + g\,dz = -L_v\,dr_s$$

$r_s(T, p)$ depends on both: $dr_s = \frac{\partial r_s}{\partial T}dT + \frac{\partial r_s}{\partial p}dp$. With $r_s \approx 0.622\,e_s/p$: $\frac{\partial r_s}{\partial T} = r_s\frac{L_v}{R_v T^2}$ and $\frac{\partial r_s}{\partial p} = -r_s/p$, so $\frac{\partial r_s}{\partial p}dp = r_s\,g\,dz/(R_L T)$. Solve everything for $dT/dz$:

$$\Gamma_s = -\frac{dT}{dz} = \frac{g}{c_p}\;\frac{1 + \dfrac{L_v\,r_s}{R_L\,T}}{1 + \dfrac{0.622\,L_v^2\,r_s}{c_p\,R_L\,T^2}}$$

The numerator is close to 1 (the pressure dependence of $r_s$); the denominator is the real effect, the heat per degree of cooling. At 0 °C, 1000 hPa: $r_s = 3.8$ g/kg, numerator 1.12, denominator 1.69, $\Gamma_s = 6.5$ K/km. At 20 °C: 4.2 K/km. At −40 °C: 9.5 K/km.

**$\theta_e$.** Divide the moist first law by $T$ and use $ds = c_p\,d\ln\theta$: $c_p\,d\ln\theta = -L_v\,dr_s/T$. With the approximation that $L_v/T$ varies slowly compared with $r_s$, this integrates to $c_p\ln\theta + L_v r_s/T = \mathrm{const}$, hence

$$\theta_e = \theta\,\exp\!\left(\frac{L_v\,r_s}{c_p\,T}\right)$$

evaluated at the condensation level. For unsaturated air one uses $r$ instead of $r_s$ and $T_{LCL}$ -- the value the parcel would have if lifted.

**Where it stops holding:** the pseudo-adiabat lets the condensate fall out at once; keeping it in the parcel (reversible) makes $\Gamma_s$ a few tenths of a K/km smaller. Below 0 °C, $L_s$ should stand for ice formation -- in practice the cloud freezes with delay, and the latent heat of fusion adds another 1 K."""),

# ---------------------------------------------------------------------------
"fe-emagram": t(r"""## Herleitung: CAPE als Arbeit des Auftriebs

Die Auftriebsbeschleunigung eines Pakets ist $b = g\,(T_v' - T_v)/T_v$ (Archimedes mit $\rho \propto 1/T_v$ bei gleichem Druck; die virtuelle Temperatur, weil das Paket feuchter ist als die Umgebung). Die Arbeit je Masse längs des Aufstiegs vom Niveau freier Konvektion (LFC, wo $b$ positiv wird) bis zum Gleichgewichtsniveau (EL, wo $b$ wieder null ist):

$$\mathrm{CAPE} = \int_{LFC}^{EL} b\,dz = \int_{LFC}^{EL} g\,\frac{T_v' - T_v}{T_v}\,dz$$

In Druckkoordinaten mit $dz = -R_L T_v\,dp/(g\,p)$: $\mathrm{CAPE} = R_L\int_{p_{EL}}^{p_{LFC}}(T_v' - T_v)\,d\ln p$ -- die Fläche zwischen Paket- und Umgebungskurve im Diagramm mit $\ln p$-Achse, in J/kg. Ein Grad Temperaturüberschuss über 10 km gibt $R_L\cdot 1\cdot\ln(1000/200) = 460$ J/kg: CAPE von 2000 J/kg heißt im Mittel 4 K wärmer als die Umgebung.

**$w_{max}$:** Ohne Reibung und Einmischung ist $\frac{dw}{dt} = b$, also $w\,\frac{dw}{dz} = b$ und $\frac{1}{2}w^2 = \int b\,dz = \mathrm{CAPE}$:

$$w_{max} = \sqrt{2\,\mathrm{CAPE}}$$

**CIN** ist dasselbe Integral vom Boden bis zum LFC, wo $b < 0$: die Energie, die ein Auslöser aufbringen muss. 50 J/kg sind leicht (Sonne am Mittag), 200 J/kg brauchen eine Front oder ein Gebirge.

**Wo es aufhört zu gelten:** Die Paketmethode nimmt an, dass das Paket nicht mischt (real halbiert Einmischung die CAPE), kein Wasser trägt (1 g/kg Flüssigwasser wiegt wie 0,3 K Kälte) und keine Druckstörung spürt (ein Aufwind muss die Luft über sich wegschieben). Deshalb $w \approx \frac{1}{2}w_{max}$. Und CAPE ist ein Potential, kein Ereignis: Eine labile Luftmasse ohne Auslöser bleibt den ganzen Tag ruhig.""",
r"""## Derivation: CAPE as the work of buoyancy

The buoyant acceleration of a parcel is $b = g\,(T_v' - T_v)/T_v$ (Archimedes with $\rho \propto 1/T_v$ at equal pressure; the virtual temperature because the parcel is moister than its surroundings). The work per mass along the ascent from the level of free convection (LFC, where $b$ turns positive) to the equilibrium level (EL, where $b$ is zero again):

$$\mathrm{CAPE} = \int_{LFC}^{EL} b\,dz = \int_{LFC}^{EL} g\,\frac{T_v' - T_v}{T_v}\,dz$$

In pressure coordinates with $dz = -R_L T_v\,dp/(g\,p)$: $\mathrm{CAPE} = R_L\int_{p_{EL}}^{p_{LFC}}(T_v' - T_v)\,d\ln p$ -- the area between parcel and environment curve on a diagram with $\ln p$ axis, in J/kg. One degree of excess over 10 km gives $R_L\cdot 1\cdot\ln(1000/200) = 460$ J/kg: a CAPE of 2000 J/kg means on average 4 K warmer than the surroundings.

**$w_{max}$:** without friction and entrainment $\frac{dw}{dt} = b$, so $w\,\frac{dw}{dz} = b$ and $\frac{1}{2}w^2 = \int b\,dz = \mathrm{CAPE}$:

$$w_{max} = \sqrt{2\,\mathrm{CAPE}}$$

**CIN** is the same integral from the ground to the LFC, where $b < 0$: the energy a trigger must supply. 50 J/kg is easy (midday sun), 200 J/kg needs a front or a mountain range.

**Where it stops holding:** the parcel method assumes no mixing (in reality entrainment halves the CAPE), no water loading (1 g/kg of liquid water weighs like 0.3 K of cold) and no pressure perturbation (an updraught must push the air above it aside). Hence $w \approx \frac{1}{2}w_{max}$. And CAPE is a potential, not an event: an unstable air mass without a trigger stays quiet all day."""),

# ---------------------------------------------------------------------------
"st-bilanz": t(r"""## Herleitung: Solarkonstante und Strahlungsgleichgewicht

**Stefan-Boltzmann aus Planck:** Die spektrale Ausstrahlung eines schwarzen Körpers ist $B_\lambda = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/(\lambda kT)} - 1}$. Über alle Wellenlängen und den Halbraum integriert ergibt das $M = \sigma T^4$ mit $\sigma = \frac{2\pi^5 k^4}{15\,h^3 c^2} = 5{,}67\cdot 10^{-8}$ W/(m²·K⁴). Das Maximum von $B_\lambda$ liegt bei $\lambda_{max} T = 2898$ μm·K (Wien).

**Die Solarkonstante:** Die Sonne strahlt $4\pi R_\odot^2\,\sigma T_\odot^4$ ab. In der Entfernung $d = 1$ AE verteilt sich das auf $4\pi d^2$:

$$S_0 = \sigma T_\odot^4\left(\frac{R_\odot}{d}\right)^2 = 5{,}67\cdot 10^{-8}\cdot 5772^4\cdot\left(\frac{6{,}96\cdot 10^8}{1{,}496\cdot 10^{11}}\right)^2 = 1361\,\mathrm{W/m^2}$$

**Das Gleichgewicht:** Die Erde fängt $S_0\,\pi R^2$ auf, reflektiert den Anteil $A$ und strahlt über $4\pi R^2$ mit $\sigma T_e^4$ ab. Gleichsetzen:

$$\sigma T_e^4 = \frac{S_0\,(1 - A)}{4} \quad\Rightarrow\quad T_e = \left(\frac{1361\cdot 0{,}70}{4\cdot 5{,}67\cdot 10^{-8}}\right)^{1/4} = 255\,\mathrm{K}$$

Die Empfindlichkeit: $\frac{dT_e}{T_e} = \frac{1}{4}\frac{dF}{F}$. Ein Prozent Albedo sind $1{,}4$ % weniger Absorption, also $0{,}36$ % oder 0,9 K.

**Wo es aufhört zu gelten:** $T_e$ ist eine Mitteltemperatur; die Erde strahlt am Äquator mehr ab als an den Polen, und wegen $T^4$ ist das Mittel der vierten Potenz nicht die vierte Potenz des Mittels. Die Sonne ist kein perfekter schwarzer Körper (Fraunhofer-Linien, UV-Defizit), und $S_0$ schwankt um 0,1 % mit dem 11-Jahres-Zyklus -- ein Zehntel der CO₂-Verdopplung.""",
r"""## Derivation: solar constant and radiative equilibrium

**Stefan–Boltzmann from Planck:** the spectral exitance of a black body is $B_\lambda = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/(\lambda kT)} - 1}$. Integrated over all wavelengths and the hemisphere this gives $M = \sigma T^4$ with $\sigma = \frac{2\pi^5 k^4}{15\,h^3 c^2} = 5.67\cdot 10^{-8}$ W/(m²·K⁴). The maximum of $B_\lambda$ lies at $\lambda_{max} T = 2898$ μm·K (Wien).

**The solar constant:** the sun emits $4\pi R_\odot^2\,\sigma T_\odot^4$. At distance $d = 1$ AU this is spread over $4\pi d^2$:

$$S_0 = \sigma T_\odot^4\left(\frac{R_\odot}{d}\right)^2 = 5.67\cdot 10^{-8}\cdot 5772^4\cdot\left(\frac{6.96\cdot 10^8}{1.496\cdot 10^{11}}\right)^2 = 1361\,\mathrm{W/m^2}$$

**The equilibrium:** the Earth intercepts $S_0\,\pi R^2$, reflects the fraction $A$ and radiates over $4\pi R^2$ at $\sigma T_e^4$. Equating:

$$\sigma T_e^4 = \frac{S_0\,(1 - A)}{4} \quad\Rightarrow\quad T_e = \left(\frac{1361\cdot 0.70}{4\cdot 5.67\cdot 10^{-8}}\right)^{1/4} = 255\,\mathrm{K}$$

The sensitivity: $\frac{dT_e}{T_e} = \frac{1}{4}\frac{dF}{F}$. One per cent of albedo is $1.4$ % less absorption, hence $0.36$ % or 0.9 K.

**Where it stops holding:** $T_e$ is a mean temperature; the Earth radiates more at the equator than at the poles, and because of $T^4$ the mean of the fourth power is not the fourth power of the mean. The sun is not a perfect black body (Fraunhofer lines, UV deficit), and $S_0$ varies by 0.1 % with the 11-year cycle -- a tenth of a CO₂ doubling."""),

# ---------------------------------------------------------------------------
"st-treibhaus": t(r"""## Herleitung: das Einschichtmodell

Eine Schicht mit Temperatur $T_a$, durchsichtig für Sonnenlicht, Emissionsgrad 1 im Infrarot. Sei $F = S_0(1-A)/4 = 238$ W/m² die absorbierte Sonnenleistung, ganz am Boden.

*Bilanz am Oberrand (ins All):* nur die Schicht strahlt nach oben, $\sigma T_a^4 = F$.

*Bilanz der Schicht:* sie absorbiert $\sigma T_s^4$ vom Boden und strahlt $2\sigma T_a^4$ (oben und unten): $\sigma T_s^4 = 2\sigma T_a^4$.

*Bilanz am Boden:* $\sigma T_s^4 = F + \sigma T_a^4$ -- dieselbe Aussage, die Probe stimmt.

$$T_s = 2^{1/4}\,T_a = 2^{1/4}\,T_e = 1{,}189\cdot 255 = 303\,\mathrm{K}$$

Mit $n$ Schichten wird daraus $T_s = (n+1)^{1/4}\,T_e$; mit Emissionsgrad $\varepsilon < 1$: $T_s^4 = T_e^4\cdot\frac{2}{2 - \varepsilon}$. Für die beobachteten 288 K bräuchte es $\varepsilon = 0{,}78$ -- was tatsächlich der mittleren Durchlässigkeit der Atmosphäre im Infrarot nahekommt. Mit Konvektion (100 W/m² vom Boden in die Schicht) wird die Bodenbilanz $\sigma T_s^4 = F + \sigma T_a^4 - 100$, und 288 K kommen auch mit $\varepsilon = 1$ heraus.

**Der Strahlungsantrieb:** Für ein Gas mit gesättigten Linien wächst die Absorption nur in den Linienflügeln, deren Breite mit $\ln C$ geht; Linie-für-Linie-Rechnungen ergeben $\Delta F = 5{,}35\,\mathrm{W/m^2}\cdot\ln(C/C_0)$ (Myhre 1998). Die Planck-Antwort folgt aus $\frac{d}{dT}(\sigma T^4) = 4\sigma T^3$:

$$\Delta T_0 = \frac{\Delta F}{4\sigma T_e^3} = \frac{3{,}7}{4\cdot 5{,}67\cdot 10^{-8}\cdot 255^3} = 1{,}0\,\mathrm{K}$$

Rückkopplungen $\lambda_i$ addieren sich zum Nenner: $\Delta T = \Delta F/(\lambda_0 - \sum\lambda_i)$ mit $\lambda_0 = 3{,}76$, Wasserdampf $+1{,}8$, Gradient $-0{,}6$, Eis $+0{,}3$, Wolken $+0{,}5\pm 0{,}5$ W/(m²·K). Das gibt $3{,}7/(3{,}76 - 2{,}0) \approx 2$ bis 4 K.

**Wo es aufhört zu gelten:** Das Modell ist grau (keine Spektralstruktur), hat keinen Tagesgang und keinen Ozean. Es erklärt den Mechanismus, nicht die Zahl. Die Zahl liefern Strahlungstransportmodelle mit 10⁵ Spektrallinien, und selbst die brauchen die Wolken von außen.""",
r"""## Derivation: the one-layer model

A layer at temperature $T_a$, transparent to sunlight, emissivity 1 in the infrared. Let $F = S_0(1-A)/4 = 238$ W/m² be the absorbed solar power, all of it at the ground.

*Balance at the top (to space):* only the layer radiates upward, $\sigma T_a^4 = F$.

*Balance of the layer:* it absorbs $\sigma T_s^4$ from the ground and emits $2\sigma T_a^4$ (up and down): $\sigma T_s^4 = 2\sigma T_a^4$.

*Balance at the ground:* $\sigma T_s^4 = F + \sigma T_a^4$ -- the same statement, the check works.

$$T_s = 2^{1/4}\,T_a = 2^{1/4}\,T_e = 1.189\cdot 255 = 303\,\mathrm{K}$$

With $n$ layers this becomes $T_s = (n+1)^{1/4}\,T_e$; with emissivity $\varepsilon < 1$: $T_s^4 = T_e^4\cdot\frac{2}{2 - \varepsilon}$. The observed 288 K would need $\varepsilon = 0.78$ -- which is indeed close to the atmosphere's mean infrared opacity. With convection (100 W/m² from the ground into the layer) the surface balance becomes $\sigma T_s^4 = F + \sigma T_a^4 - 100$, and 288 K comes out even with $\varepsilon = 1$.

**The radiative forcing:** for a gas with saturated lines absorption grows only in the line wings, whose width goes as $\ln C$; line-by-line calculations give $\Delta F = 5.35\,\mathrm{W/m^2}\cdot\ln(C/C_0)$ (Myhre 1998). The Planck response follows from $\frac{d}{dT}(\sigma T^4) = 4\sigma T^3$:

$$\Delta T_0 = \frac{\Delta F}{4\sigma T_e^3} = \frac{3.7}{4\cdot 5.67\cdot 10^{-8}\cdot 255^3} = 1.0\,\mathrm{K}$$

Feedbacks $\lambda_i$ add to the denominator: $\Delta T = \Delta F/(\lambda_0 - \sum\lambda_i)$ with $\lambda_0 = 3.76$, water vapour $+1.8$, lapse rate $-0.6$, ice $+0.3$, clouds $+0.5\pm 0.5$ W/(m²·K). That gives $3.7/(3.76 - 2.0) \approx 2$ to 4 K.

**Where it stops holding:** the model is grey (no spectral structure), has no diurnal cycle and no ocean. It explains the mechanism, not the number. The number comes from radiative transfer models with 10⁵ spectral lines, and even those need the clouds from outside."""),

# ---------------------------------------------------------------------------
"st-tagesgang": t(r"""## Herleitung: die nächtliche Abkühlung

**Die Gegenstrahlung** einer klaren Atmosphäre lässt sich mit einer effektiven Emissivität schreiben: $L_\downarrow = \varepsilon_a\,\sigma T_{2m}^4$ mit $\varepsilon_a \approx 0{,}7$ bis $0{,}8$, steigend mit dem Dampfdruck (Brunt: $\varepsilon_a = 0{,}52 + 0{,}065\sqrt{e/\mathrm{hPa}}$). Bei 10 °C und $e = 8$ hPa: $\varepsilon_a = 0{,}70$, $L_\downarrow = 0{,}70\cdot 5{,}67\cdot 10^{-8}\cdot 283^4 = 255$ W/m². Der Boden strahlt bei 10 °C $364$ W/m² ab. Netto: $-109$ W/m² -- eine kalte, trockene Nacht. Mit $e = 15$ hPa (feucht): $\varepsilon_a = 0{,}77$, netto $-84$ W/m². Unter einer Stratusdecke in 500 m ($T = 7$ °C, $\varepsilon = 1$): $L_\downarrow = 349$, netto $-15$ W/m².

**Die Abkühlung der Luft:** Der Boden kühlt zuerst, dann die Luft durch Leitung und schwache Turbulenz. In einer Schicht der Dicke $h$, die den ganzen Verlust $Q$ trägt:

$$\rho\,c_p\,h\,\frac{dT}{dt} = Q \quad\Rightarrow\quad \Delta T = \frac{Q\,\Delta t}{\rho\,c_p\,h}$$

Mit $Q = 60$ W/m², 8 h, $h = 200$ m: $\Delta T = 60\cdot 28\,800/(1{,}2\cdot 1004\cdot 200) = 7{,}2$ K. Real ist $h$ nicht konstant: Die Inversion wächst mit $\sqrt{t}$ (Diffusion), und die untersten Meter kühlen am stärksten.

**Die Taubildung:** Wenn $T_{Boden}$ unter $T_d$ fällt, kondensiert Dampf, und je Kilogramm 2,5 MJ Wärme werden frei. Das bremst die Abkühlung -- der Taupunkt ist eine Bremse. Deshalb gefriert es in feuchten Nächten seltener, und deshalb besprühen Obstbauern bei Frostgefahr die Blüten mit Wasser: Das Gefrieren liefert 0,33 MJ/kg und hält das Eis bei 0 °C.

**Wo es aufhört zu gelten:** Bei Wind über 3 m/s mischt die Turbulenz die Inversion weg, und die Abkühlung verteilt sich auf 500 m; dann sind es 2 K statt 7. Über Schnee ist $\varepsilon = 0{,}99$ und die Wärmeleitung in den Boden fast null: Die Oberfläche kann 20 K unter die Lufttemperatur fallen.""",
r"""## Derivation: nocturnal cooling

**The back radiation** of a clear atmosphere can be written with an effective emissivity: $L_\downarrow = \varepsilon_a\,\sigma T_{2m}^4$ with $\varepsilon_a \approx 0.7$ to $0.8$, rising with vapour pressure (Brunt: $\varepsilon_a = 0.52 + 0.065\sqrt{e/\mathrm{hPa}}$). At 10 °C and $e = 8$ hPa: $\varepsilon_a = 0.70$, $L_\downarrow = 0.70\cdot 5.67\cdot 10^{-8}\cdot 283^4 = 255$ W/m². The ground at 10 °C emits $364$ W/m². Net: $-109$ W/m² -- a cold, dry night. With $e = 15$ hPa (moist): $\varepsilon_a = 0.77$, net $-84$ W/m². Under a stratus deck at 500 m ($T = 7$ °C, $\varepsilon = 1$): $L_\downarrow = 349$, net $-15$ W/m².

**The cooling of the air:** the ground cools first, then the air by conduction and weak turbulence. In a layer of depth $h$ that carries the whole loss $Q$:

$$\rho\,c_p\,h\,\frac{dT}{dt} = Q \quad\Rightarrow\quad \Delta T = \frac{Q\,\Delta t}{\rho\,c_p\,h}$$

With $Q = 60$ W/m², 8 h, $h = 200$ m: $\Delta T = 60\cdot 28\,800/(1.2\cdot 1004\cdot 200) = 7.2$ K. In reality $h$ is not constant: the inversion grows as $\sqrt{t}$ (diffusion), and the lowest metres cool most.

**Dew formation:** when $T_{ground}$ falls below $T_d$, vapour condenses and 2.5 MJ of heat per kilogram is released. That slows the cooling -- the dew point is a brake. That is why frost is rarer in moist nights, and why fruit growers spray blossoms with water when frost threatens: freezing releases 0.33 MJ/kg and holds the ice at 0 °C.

**Where it stops holding:** with wind above 3 m/s turbulence mixes the inversion away and the cooling is spread over 500 m; then it is 2 K instead of 7. Over snow $\varepsilon = 0.99$ and heat conduction into the ground is almost nil: the surface can fall 20 K below the air temperature."""),

# ---------------------------------------------------------------------------
"wo-tropfen": t(r"""## Herleitung: Kelvin und Köhler

**Kelvin.** Ein Tropfen vom Radius $r$ hat die Oberflächenenergie $4\pi r^2\sigma$. Ein Molekül, das ihn verlässt, verkleinert ihn; die freie Enthalpie des Systems ändert sich also um die Oberflächenarbeit zusätzlich zur Verdampfung. Im Gleichgewicht ist das chemische Potential des Dampfes gleich dem des Wassers im Tropfen: $\mu_v(e) = \mu_w + \frac{dG_{Oberfl}}{dN}$. Mit $\mu_v(e) = \mu_v(e_s) + kT\ln(e/e_s)$ (ideales Gas) und $\frac{dG_{Oberfl}}{dN} = \sigma\,\frac{d(4\pi r^2)}{dN} = \sigma\cdot 8\pi r\cdot\frac{m_w}{\rho_w 4\pi r^2} = \frac{2\sigma m_w}{\rho_w r}$ (ein Molekül der Masse $m_w$ bringt das Volumen $m_w/\rho_w$):

$$\ln\frac{e_s(r)}{e_s(\infty)} = \frac{2\sigma\,m_w}{\rho_w\,k\,T\,r} = \frac{2\sigma}{\rho_w\,R_v\,T\,r}$$

weil $k/m_w = R_v$. Mit $\sigma = 0{,}0756$ N/m, $T = 273$ K: Exponent $= 1{,}2\cdot 10^{-9}\,\mathrm{m}/r$. Bei $r = 0{,}1$ μm: 1,2 %; bei 0,01 μm: 12 %; bei 1 nm (ein Dutzend Moleküle): 230 %.

**Raoult.** In einer Lösung ist der Dampfdruck um den Molenbruch des Lösungsmittels verringert: $e/e_s = n_w/(n_w + i\,n_s)$ mit $i$ dem Van-'t-Hoff-Faktor (2 für NaCl). Für kleine $n_s$: $e/e_s \approx 1 - i\,n_s/n_w$, und $n_w \propto r^3$, also $1 - b/r^3$ mit $b = \frac{3\,i\,n_s\,m_w}{4\pi\rho_w}$.

**Köhler.** Beide Faktoren multipliziert und für kleine Exponenten linearisiert:

$$S(r) = \frac{e}{e_s(\infty)} \approx 1 + \frac{a}{r} - \frac{b}{r^3}, \qquad a = \frac{2\sigma}{\rho_w R_v T}$$

Das Maximum: $dS/dr = 0$ gibt $r^* = \sqrt{3b/a}$ und $S^* - 1 = \sqrt{4a^3/(27b)}$. Für einen NaCl-Kern von $10^{-18}$ kg (etwa 0,1 μm, $1{,}2\cdot 10^{7}$ Moleküle, $i = 2$): $b = 1{,}7\cdot 10^{-22}$ m³, $S^* - 1 = 1{,}2\cdot 10^{-3}$, also 0,12 % -- und $r^* = 0{,}65$ μm. Alles unter $r^*$ ist ein Dunsttröpfchen im stabilen Gleichgewicht; alles darüber wächst, solange $S > S^*$.

**Wo es aufhört zu gelten:** Für unlösliche Kerne (Staub) fehlt der $b$-Term und es bleibt reiner Kelvin mit großem $r_0$; für organische Aerosole ist $\sigma$ kleiner; und bei $r < 5$ nm ist $\sigma$ selbst radiusabhängig. Die Form der Kurve ist universell, die Zahlen sind es nicht.""",
r"""## Derivation: Kelvin and Köhler

**Kelvin.** A drop of radius $r$ has surface energy $4\pi r^2\sigma$. A molecule that leaves it shrinks it; the free enthalpy of the system thus changes by the surface work in addition to the evaporation. In equilibrium the chemical potential of the vapour equals that of the water in the drop: $\mu_v(e) = \mu_w + \frac{dG_{surf}}{dN}$. With $\mu_v(e) = \mu_v(e_s) + kT\ln(e/e_s)$ (ideal gas) and $\frac{dG_{surf}}{dN} = \sigma\,\frac{d(4\pi r^2)}{dN} = \sigma\cdot 8\pi r\cdot\frac{m_w}{\rho_w 4\pi r^2} = \frac{2\sigma m_w}{\rho_w r}$ (one molecule of mass $m_w$ brings the volume $m_w/\rho_w$):

$$\ln\frac{e_s(r)}{e_s(\infty)} = \frac{2\sigma\,m_w}{\rho_w\,k\,T\,r} = \frac{2\sigma}{\rho_w\,R_v\,T\,r}$$

because $k/m_w = R_v$. With $\sigma = 0.0756$ N/m, $T = 273$ K: exponent $= 1.2\cdot 10^{-9}\,\mathrm{m}/r$. At $r = 0.1$ μm: 1.2 %; at 0.01 μm: 12 %; at 1 nm (a dozen molecules): 230 %.

**Raoult.** In a solution the vapour pressure is reduced by the mole fraction of the solvent: $e/e_s = n_w/(n_w + i\,n_s)$ with $i$ the van 't Hoff factor (2 for NaCl). For small $n_s$: $e/e_s \approx 1 - i\,n_s/n_w$, and $n_w \propto r^3$, hence $1 - b/r^3$ with $b = \frac{3\,i\,n_s\,m_w}{4\pi\rho_w}$.

**Köhler.** Both factors multiplied and linearised for small exponents:

$$S(r) = \frac{e}{e_s(\infty)} \approx 1 + \frac{a}{r} - \frac{b}{r^3}, \qquad a = \frac{2\sigma}{\rho_w R_v T}$$

The maximum: $dS/dr = 0$ gives $r^* = \sqrt{3b/a}$ and $S^* - 1 = \sqrt{4a^3/(27b)}$. For a NaCl nucleus of $10^{-18}$ kg (about 0.1 μm, $1.2\cdot 10^{7}$ molecules, $i = 2$): $b = 1.7\cdot 10^{-22}$ m³, $S^* - 1 = 1.2\cdot 10^{-3}$, i.e. 0.12 % -- and $r^* = 0.65$ μm. Everything below $r^*$ is a haze droplet in stable equilibrium; everything above grows as long as $S > S^*$.

**Where it stops holding:** for insoluble nuclei (dust) the $b$ term is missing and pure Kelvin with a large $r_0$ remains; for organic aerosols $\sigma$ is smaller; and at $r < 5$ nm $\sigma$ itself depends on radius. The shape of the curve is universal, the numbers are not."""),

# ---------------------------------------------------------------------------
"wo-wachstum": t(r"""## Herleitung: Diffusionswachstum und Stokes

**Diffusion.** Um einen Tropfen vom Radius $r$ stellt sich ein stationäres Dampfdichtefeld ein, das die Laplace-Gleichung löst: $\rho_v(R) = \rho_{v,\infty} - (\rho_{v,\infty} - \rho_{v,r})\,r/R$. Der Fluss zum Tropfen ist $4\pi r^2\,D\,\frac{d\rho_v}{dR}|_r = 4\pi r D\,(\rho_{v,\infty} - \rho_{v,r})$ -- proportional zu $r$, nicht zu $r^2$, weil der Gradient mit $1/r$ steiler wird. Die Massenänderung $\frac{dm}{dt} = 4\pi r^2\rho_w\frac{dr}{dt}$ gleichgesetzt:

$$r\,\frac{dr}{dt} = \frac{D}{\rho_w}\,(\rho_{v,\infty} - \rho_{v,r}) \approx \frac{D\,\rho_{v,s}}{\rho_w}\,S = \xi\,S$$

mit $S = e/e_s - 1$ der Übersättigung. Dasselbe für die Wärme: Die Kondensationswärme muss mit $4\pi r K\,(T_r - T_\infty)$ abfließen, und das erhöht $T_r$ und damit $e_s(T_r)$ -- der Tropfen wächst langsamer, als die reine Dampfdiffusion erlaubte. Beide Terme zusammen geben $\xi = \left[\frac{\rho_w R_v T}{D\,e_s} + \frac{\rho_w L_v^2}{K\,R_v T^2}\right]^{-1} = \left[9{,}4\cdot 10^{9} + 7{,}6\cdot 10^{9}\right]^{-1} = 5{,}9\cdot 10^{-11}$ m²/s bei 0 °C für $S$ als Bruchteil ($D = 2{,}2\cdot 10^{-5}$ m²/s, $K = 0{,}024$ W/(m·K)), also rund $6\cdot 10^{-13}$ m²/s je Prozent. Integriert: $r^2 = r_0^2 + 2\xi S t$ -- von 1 auf 10 μm bei 0,5 %: 165 s.

**Stokes.** Eine Kugel, die sich langsam durch ein zähes Medium bewegt ($Re = 2rv\rho/\eta \ll 1$), erfährt die Reibungskraft $6\pi\eta r v$. Gleichgewicht mit dem Gewicht $\frac{4}{3}\pi r^3\rho_w g$:

$$v = \frac{2\,\rho_w\,g\,r^2}{9\,\eta}$$

Bei $r = 10$ μm: $Re = 0{,}01$, Stokes gilt, $v = 1{,}2$ cm/s. Bei 100 μm: $Re = 10$, $v$ ist nicht mehr 1,2 m/s, sondern 0,7 m/s. Bei 1 mm: turbulenter Widerstand $\frac{1}{2}c_w\rho_L v^2\pi r^2$, $v = \sqrt{8\rho_w g r/(3 c_w\rho_L)} = 4$ m/s mit $c_w \approx 0{,}6$ -- und ab 3 mm wird der Tropfen flach und zerplatzt.

**Koaleszenz.** Ein Sammler vom Radius $R$ fällt mit $v(R)$ durch Tröpfchen der Konzentration $w$ (kg/m³) mit $v(r) \ll v(R)$: $\frac{dm}{dt} = \pi R^2\,v(R)\,w\,E$ mit der Einfangwirksamkeit $E$ (klein für $R < 20$ μm, weil die Luftströmung die Tröpfchen um den Sammler herumführt). Mit $v \propto R^2$ (Stokes) wächst $m$ wie $R^4$, mit $v \propto \sqrt{R}$ (turbulent) wie $R^{5/2}$ -- in jedem Fall schneller als linear: Wer groß ist, wird schnell größer.

**Wo es aufhört zu gelten:** Die Diffusionslösung nimmt ruhende Luft an; ein fallender Tropfen hat eine Ventilationskorrektur. Die Übersättigung in der Wolke ist nicht konstant, sondern stellt sich aus Aufwind und Tropfenzahl ein. Und Stokes gilt nur bis $Re \approx 1$, also $r \approx 40$ μm.""",
r"""## Derivation: diffusional growth and Stokes

**Diffusion.** Around a drop of radius $r$ a steady vapour density field forms that solves Laplace's equation: $\rho_v(R) = \rho_{v,\infty} - (\rho_{v,\infty} - \rho_{v,r})\,r/R$. The flux to the drop is $4\pi r^2\,D\,\frac{d\rho_v}{dR}|_r = 4\pi r D\,(\rho_{v,\infty} - \rho_{v,r})$ -- proportional to $r$, not $r^2$, because the gradient steepens as $1/r$. Equate to the mass change $\frac{dm}{dt} = 4\pi r^2\rho_w\frac{dr}{dt}$:

$$r\,\frac{dr}{dt} = \frac{D}{\rho_w}\,(\rho_{v,\infty} - \rho_{v,r}) \approx \frac{D\,\rho_{v,s}}{\rho_w}\,S = \xi\,S$$

with $S = e/e_s - 1$ the supersaturation. The same for heat: the condensation heat must flow away at $4\pi r K\,(T_r - T_\infty)$, and that raises $T_r$ and hence $e_s(T_r)$ -- the drop grows more slowly than pure vapour diffusion would allow. Both terms together give $\xi = \left[\frac{\rho_w R_v T}{D\,e_s} + \frac{\rho_w L_v^2}{K\,R_v T^2}\right]^{-1} = \left[9.4\cdot 10^{9} + 7.6\cdot 10^{9}\right]^{-1} = 5.9\cdot 10^{-11}$ m²/s at 0 °C for $S$ as a fraction ($D = 2.2\cdot 10^{-5}$ m²/s, $K = 0.024$ W/(m·K)), i.e. about $6\cdot 10^{-13}$ m²/s per per cent. Integrated: $r^2 = r_0^2 + 2\xi S t$ -- from 1 to 10 μm at 0.5 %: 165 s.

**Stokes.** A sphere moving slowly through a viscous medium ($Re = 2rv\rho/\eta \ll 1$) experiences the drag $6\pi\eta r v$. Balance with the weight $\frac{4}{3}\pi r^3\rho_w g$:

$$v = \frac{2\,\rho_w\,g\,r^2}{9\,\eta}$$

At $r = 10$ μm: $Re = 0.01$, Stokes holds, $v = 1.2$ cm/s. At 100 μm: $Re = 10$, $v$ is no longer 1.2 m/s but 0.7 m/s. At 1 mm: turbulent drag $\frac{1}{2}c_d\rho_L v^2\pi r^2$, $v = \sqrt{8\rho_w g r/(3 c_d\rho_L)} = 4$ m/s with $c_d \approx 0.6$ -- and from 3 mm the drop flattens and breaks up.

**Coalescence.** A collector of radius $R$ falls at $v(R)$ through droplets of concentration $w$ (kg/m³) with $v(r) \ll v(R)$: $\frac{dm}{dt} = \pi R^2\,v(R)\,w\,E$ with collection efficiency $E$ (small for $R < 20$ μm, because the airflow carries the droplets around the collector). With $v \propto R^2$ (Stokes) $m$ grows as $R^4$, with $v \propto \sqrt{R}$ (turbulent) as $R^{5/2}$ -- in either case faster than linearly: the big get bigger fast.

**Where it stops holding:** the diffusion solution assumes still air; a falling drop has a ventilation correction. The supersaturation in the cloud is not constant but set by updraught and drop number. And Stokes holds only to $Re \approx 1$, i.e. $r \approx 40$ μm."""),

# ---------------------------------------------------------------------------
"dy-coriolis": t(r"""## Herleitung: vom Inertialsystem ins rotierende

**1. Die Ableitung eines mitrotierenden Einheitsvektors.** Sei $\vec e$ ein Einheitsvektor, der im rotierenden System ruht -- einer der drei Achsenvektoren $\hat e_1, \hat e_2, \hat e_3$ des mitgedrehten Koordinatensystems. Von außen gesehen beschreibt seine Spitze einen Kreis um die Drehachse $\vec\Omega$. Ist $\alpha$ der Winkel zwischen $\vec\Omega$ und $\vec e$, hat dieser Kreis den Radius $\sin\alpha$. In der Zeit $dt$ dreht sich alles um den Winkel $\Omega\,dt$, die Spitze wandert also um die Strecke $|d\vec e| = \sin\alpha\cdot\Omega\,dt$ -- senkrecht zu $\vec\Omega$ (sie bleibt auf dem Kreis in der Ebene senkrecht zur Achse) und senkrecht zu $\vec e$ (ein Einheitsvektor ändert nur seine Richtung), im Drehsinn der rechten Hand. Ein Vektor mit genau diesem Betrag $\Omega\sin\alpha$ und dieser Richtung ist das Kreuzprodukt:

$$\frac{d\hat e_i}{dt} = \vec\Omega\times\hat e_i \qquad (i = 1, 2, 3)$$

Das ist der ganze Trick, und er gilt für jeden Vektor, der im rotierenden System fest ist.

**2. Die Ableitung eines beliebigen Vektors.** Sei $\vec A = \sum_i A_i\,\hat e_i$ mit Komponenten im rotierenden System. Produktregel:

$$\left.\frac{d\vec A}{dt}\right|_{in} = \sum_i\frac{dA_i}{dt}\,\hat e_i + \sum_i A_i\,\frac{d\hat e_i}{dt} = \frac{d'\vec A}{dt} + \vec\Omega\times\vec A$$

Der erste Term ist die Änderung, die der mitrotierende Beobachter sieht (nur die Komponenten ändern sich, Schreibweise $d'/dt$); der zweite kommt allein daher, dass seine Achsen sich drehen.

**3. Zweimal anwenden.** Auf den Ortsvektor $\vec r$ (gemessen von einem Punkt der Achse): $\vec v_{in} = \vec v + \vec\Omega\times\vec r$ mit $\vec v = d'\vec r/dt$ dem Wind, den wir messen. Noch einmal, jetzt auf $\vec v_{in}$, mit konstantem $\vec\Omega$:

$$\vec a_{in} = \frac{d'}{dt}\left(\vec v + \vec\Omega\times\vec r\right) + \vec\Omega\times\left(\vec v + \vec\Omega\times\vec r\right) = \frac{d'\vec v}{dt} + 2\,\vec\Omega\times\vec v + \vec\Omega\times(\vec\Omega\times\vec r)$$

Der mittlere Term entsteht **zweimal**: einmal aus $d'(\vec\Omega\times\vec r)/dt = \vec\Omega\times\vec v$, einmal aus $\vec\Omega\times\vec v$ -- daher die 2. Newton gilt für $\vec a_{in}$: $\vec a_{in} = -\nabla p/\rho + \vec g + \vec F$. Nach $d'\vec v/dt$ aufgelöst:

$$\frac{d'\vec v}{dt} = -\frac{1}{\rho}\nabla p - 2\,\vec\Omega\times\vec v - \vec\Omega\times(\vec\Omega\times\vec r) + \vec g + \vec F$$

Der Zentrifugalterm ist $-\vec\Omega\times(\vec\Omega\times\vec r) = \Omega^2\vec r_\perp$ (nach außen, von der Achse weg, mit $\vec r_\perp$ dem Abstand von der Achse) -- er hängt nur vom Ort ab, nicht von der Bewegung, und wird deshalb mit $\vec g$ zur effektiven Schwere $\vec g^* = \vec g + \Omega^2\vec r_\perp$ zusammengefasst. Am Äquator sind das $\Omega^2 a = 0{,}034$ m/s², 0,35 % von $g$; die Erde hat sich genau so abgeplattet, dass $\vec g^*$ überall senkrecht auf ihrer Oberfläche steht.

**4. Die lokalen Einheitsvektoren und $f$.** Am Ort mit der Breite $\varphi$ sei $\hat i$ nach Osten, $\hat j$ nach Norden, $\hat k$ nach oben. Die Erdachse liegt in der Ebene von $\hat j$ und $\hat k$ (der Meridianebene) und bildet mit der Senkrechten $\hat k$ den Winkel $90^\circ - \varphi$ (am Pol fallen sie zusammen, am Äquator stehen sie senkrecht). Also

$$\vec\Omega = \Omega\,(0,\;\cos\varphi,\;\sin\varphi)$$

Mit $\vec v = (u, v, w)$ wird das Kreuzprodukt

$$2\,\vec\Omega\times\vec v = 2\Omega\left(w\cos\varphi - v\sin\varphi,\;\; u\sin\varphi,\;\; -u\cos\varphi\right)$$

Die Horizontalkomponenten der Coriolis-Beschleunigung $-2\vec\Omega\times\vec v$ sind also $(+2\Omega\sin\varphi\,v,\; -2\Omega\sin\varphi\,u)$ plus dem Term $-2\Omega w\cos\varphi$, der wegen $w \ll u$ wegfällt. Mit

$$f = 2\,\Omega\,\sin\varphi$$

lautet die horizontale Coriolis-Beschleunigung $(f v, -f u) = -f\,\hat k\times\vec v_h$: senkrecht zum Wind, nach rechts (Nordhalbkugel, $f > 0$), Betrag $f|\vec v_h|$. Die Vertikalkomponente $+2\Omega u\cos\varphi$ ist bei $u = 10$ m/s $1{,}5\cdot 10^{-3}$ m/s² gegen $g = 9{,}8$ und wird vernachlässigt (Eötvös-Effekt; man spürt ihn in der Gravimetrie auf einem fahrenden Schiff).

**5. Nebenbei: die lokalen Achsen drehen sich auch beim Fortschreiten.** Wer sich nach Osten bewegt, dreht sein $\hat i$, $\hat j$, $\hat k$ um die Polachse mit. Dasselbe Argument wie in Schritt 1 mit der Polachse $\hat k_{pol} = \cos\varphi\,\hat j + \sin\varphi\,\hat k$ als Drehachse und der Winkelgeschwindigkeit $\dot\lambda = u/(a\cos\varphi)$:

$$\frac{d\hat i}{dt} = \dot\lambda\,\hat k_{pol}\times\hat i = \frac{u}{a\cos\varphi}\left(\sin\varphi\,\hat j - \cos\varphi\,\hat k\right)$$

Entsprechend für $\hat j$ und $\hat k$ bei Bewegung nach Norden ($\dot\varphi = v/a$, Drehung um $\hat i$). Diese **Krümmungsterme** erscheinen in den Bewegungsgleichungen als $uv\tan\varphi/a$, $u^2\tan\varphi/a$, $uw/a$: bei 10 m/s rund $10^{-5}$ m/s², ein Hundertstel der Coriolis-Beschleunigung. Für die Synoptik werden sie weggelassen; in globalen Modellen stehen sie drin.

**Wo es aufhört zu gelten:** Die Rechnung setzt $\vec\Omega$ konstant voraus -- die Präzession der Erdachse (26 000 Jahre) ist dafür irrelevant. Nahe dem Äquator ist $f \to 0$ und $\beta = df/dy$ übernimmt die Dynamik (äquatoriale Wellen). Und auf Skalen, wo die Zeit $1/f$ (3 Stunden) lang gegen die Bewegungsdauer ist -- Gewitter, Tornado, Badewanne --, ist die Coriolis-Kraft real, aber ohne Folgen.""",
r"""## Derivation: from the inertial frame to the rotating one

**1. The derivative of a co-rotating unit vector.** Let $\vec e$ be a unit vector at rest in the rotating frame -- one of the three axis vectors $\hat e_1, \hat e_2, \hat e_3$ of the co-rotating coordinate system. Seen from outside, its tip describes a circle around the rotation axis $\vec\Omega$. If $\alpha$ is the angle between $\vec\Omega$ and $\vec e$, this circle has radius $\sin\alpha$. In the time $dt$ everything turns by the angle $\Omega\,dt$, so the tip travels the distance $|d\vec e| = \sin\alpha\cdot\Omega\,dt$ -- perpendicular to $\vec\Omega$ (it stays on the circle in the plane perpendicular to the axis) and perpendicular to $\vec e$ (a unit vector changes only its direction), in the right-hand sense. A vector with exactly this magnitude $\Omega\sin\alpha$ and this direction is the cross product:

$$\frac{d\hat e_i}{dt} = \vec\Omega\times\hat e_i \qquad (i = 1, 2, 3)$$

That is the whole trick, and it holds for every vector that is fixed in the rotating frame.

**2. The derivative of an arbitrary vector.** Let $\vec A = \sum_i A_i\,\hat e_i$ with components in the rotating frame. Product rule:

$$\left.\frac{d\vec A}{dt}\right|_{in} = \sum_i\frac{dA_i}{dt}\,\hat e_i + \sum_i A_i\,\frac{d\hat e_i}{dt} = \frac{d'\vec A}{dt} + \vec\Omega\times\vec A$$

The first term is the change the co-rotating observer sees (only the components change, written $d'/dt$); the second arises solely because the axes turn.

**3. Apply twice.** To the position vector $\vec r$ (measured from a point on the axis): $\vec v_{in} = \vec v + \vec\Omega\times\vec r$ with $\vec v = d'\vec r/dt$ the wind we measure. Once more, now to $\vec v_{in}$, with constant $\vec\Omega$:

$$\vec a_{in} = \frac{d'}{dt}\left(\vec v + \vec\Omega\times\vec r\right) + \vec\Omega\times\left(\vec v + \vec\Omega\times\vec r\right) = \frac{d'\vec v}{dt} + 2\,\vec\Omega\times\vec v + \vec\Omega\times(\vec\Omega\times\vec r)$$

The middle term arises **twice**: once from $d'(\vec\Omega\times\vec r)/dt = \vec\Omega\times\vec v$, once from $\vec\Omega\times\vec v$ -- hence the 2. Newton holds for $\vec a_{in}$: $\vec a_{in} = -\nabla p/\rho + \vec g + \vec F$. Solved for $d'\vec v/dt$:

$$\frac{d'\vec v}{dt} = -\frac{1}{\rho}\nabla p - 2\,\vec\Omega\times\vec v - \vec\Omega\times(\vec\Omega\times\vec r) + \vec g + \vec F$$

The centrifugal term is $-\vec\Omega\times(\vec\Omega\times\vec r) = \Omega^2\vec r_\perp$ (outward, away from the axis, with $\vec r_\perp$ the distance from the axis) -- it depends only on position, not on motion, and is therefore folded into $\vec g$ as effective gravity $\vec g^* = \vec g + \Omega^2\vec r_\perp$. At the equator that is $\Omega^2 a = 0.034$ m/s², 0.35 % of $g$; the Earth has flattened exactly so that $\vec g^*$ is everywhere perpendicular to its surface.

**4. The local unit vectors and $f$.** At a place of latitude $\varphi$ let $\hat i$ point east, $\hat j$ north, $\hat k$ up. The Earth's axis lies in the plane of $\hat j$ and $\hat k$ (the meridian plane) and makes the angle $90^\circ - \varphi$ with the vertical $\hat k$ (at the pole they coincide, at the equator they are perpendicular). Hence

$$\vec\Omega = \Omega\,(0,\;\cos\varphi,\;\sin\varphi)$$

With $\vec v = (u, v, w)$ the cross product becomes

$$2\,\vec\Omega\times\vec v = 2\Omega\left(w\cos\varphi - v\sin\varphi,\;\; u\sin\varphi,\;\; -u\cos\varphi\right)$$

The horizontal components of the Coriolis acceleration $-2\vec\Omega\times\vec v$ are thus $(+2\Omega\sin\varphi\,v,\; -2\Omega\sin\varphi\,u)$ plus the term $-2\Omega w\cos\varphi$, which drops out because $w \ll u$. With

$$f = 2\,\Omega\,\sin\varphi$$

the horizontal Coriolis acceleration reads $(f v, -f u) = -f\,\hat k\times\vec v_h$: perpendicular to the wind, to the right (northern hemisphere, $f > 0$), magnitude $f|\vec v_h|$. The vertical component $+2\Omega u\cos\varphi$ is $1.5\cdot 10^{-3}$ m/s² at $u = 10$ m/s against $g = 9.8$ and is neglected (Eötvös effect; one notices it in gravimetry on a moving ship).

**5. Aside: the local axes also turn as one moves along.** Whoever moves east turns their $\hat i$, $\hat j$, $\hat k$ about the polar axis. The same argument as in step 1 with the polar axis $\hat k_{pol} = \cos\varphi\,\hat j + \sin\varphi\,\hat k$ as rotation axis and angular velocity $\dot\lambda = u/(a\cos\varphi)$:

$$\frac{d\hat i}{dt} = \dot\lambda\,\hat k_{pol}\times\hat i = \frac{u}{a\cos\varphi}\left(\sin\varphi\,\hat j - \cos\varphi\,\hat k\right)$$

Correspondingly for $\hat j$ and $\hat k$ when moving north ($\dot\varphi = v/a$, rotation about $\hat i$). These **curvature terms** appear in the equations of motion as $uv\tan\varphi/a$, $u^2\tan\varphi/a$, $uw/a$: about $10^{-5}$ m/s² at 10 m/s, a hundredth of the Coriolis acceleration. For synoptic work they are dropped; in global models they are kept.

**Where it stops holding:** the calculation assumes constant $\vec\Omega$ -- the precession of the Earth's axis (26 000 years) is irrelevant for this. Near the equator $f \to 0$ and $\beta = df/dy$ takes over the dynamics (equatorial waves). And on scales where the time $1/f$ (3 hours) is long compared with the duration of the motion -- thunderstorm, tornado, bathtub -- the Coriolis force is real but without consequence."""),

# ---------------------------------------------------------------------------
"dy-geostrophisch": t(r"""## Herleitung: Skalenanalyse und Gradientwind

Die horizontale Bewegungsgleichung in Komponenten (ohne Reibung, Krümmungsterme weggelassen):

$$\frac{du}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial x} + f v, \qquad \frac{dv}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial y} - f u$$

**Skalenanalyse** für ein Tief: $U = 10$ m/s, $L = 10^6$ m, $\Delta p = 10$ hPa, $f = 10^{-4}$. Dann ist $du/dt \sim U^2/L = 10^{-4}$ m/s², $fU = 10^{-3}$, $\Delta p/(\rho L) = 10^{-3}$. Die Beschleunigung ist zehnmal kleiner als die beiden anderen -- das Verhältnis ist die Rossby-Zahl $Ro = U/(fL) = 0{,}1$. In nullter Ordnung bleibt

$$f v_g = \frac{1}{\rho}\frac{\partial p}{\partial x}, \qquad f u_g = -\frac{1}{\rho}\frac{\partial p}{\partial y} \quad\Leftrightarrow\quad \vec v_g = \frac{1}{\rho f}\,\hat k\times\nabla p$$

Der Wind steht senkrecht auf $\nabla p$, also parallel zu den Isobaren, und $\hat k\times\nabla p$ zeigt bei $\nabla p$ nach Norden (Tief im Süden) nach Westen: Mit dem Tief zur Linken.

**Gradientwind.** Auf einer Kreisbahn mit Radius $R$ ist die Beschleunigung $v^2/R$ zum Zentrum. In natürlichen Koordinaten (Richtung $n$ nach links vom Wind, zum Zentrum eines zyklonalen Wirbels):

$$\frac{v^2}{R} + f v = \frac{1}{\rho}\frac{\partial p}{\partial n}$$

Für das Tief ($R > 0$, $\partial p/\partial n > 0$) löst die quadratische Gleichung $v = -\frac{fR}{2} + \sqrt{\frac{f^2R^2}{4} + \frac{R}{\rho}\frac{\partial p}{\partial n}}$: immer reell, und wegen des $v^2/R$-Terms kleiner als $v_g$ -- subgeostrophisch, um 10-20 % bei $R = 500$ km. Für das Hoch ($R < 0$, $\partial p/\partial n < 0$) steht unter der Wurzel $\frac{f^2R^2}{4} - \frac{|R|}{\rho}\left|\frac{\partial p}{\partial n}\right|$, und das wird negativ, sobald

$$\left|\frac{\partial p}{\partial n}\right| > \frac{\rho\,f^2\,|R|}{4}$$

Mit $\rho = 1{,}2$, $f = 10^{-4}$, $|R| = 1000$ km: $3\cdot 10^{-3}$ Pa/m, also 3 hPa je 100 km -- mehr kann ein Hoch dieser Größe nicht halten. Ein Hurrikan hat 100 hPa je 100 km.

**Zyklostrophisch.** Für $Ro \gg 1$ fällt $f$ weg: $v^2/R = \frac{1}{\rho}\partial p/\partial n$, der Tornado und der Staubteufel -- die drehen in beide Richtungen, weil nichts die Richtung vorgibt.

**Wo es aufhört zu gelten:** In Bodennähe (Reibung dreht den Wind zum Tief), am Äquator ($f = 0$, Ro beliebig groß), in Fronten und Jetstreaks (Beschleunigungen von der Größe $fU$, ageostrophischer Wind), und überall, wo $\partial p/\partial t$ nicht mehr klein ist -- in der Zyklogenese.""",
r"""## Derivation: scale analysis and gradient wind

The horizontal equation of motion in components (no friction, curvature terms dropped):

$$\frac{du}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial x} + f v, \qquad \frac{dv}{dt} = -\frac{1}{\rho}\frac{\partial p}{\partial y} - f u$$

**Scale analysis** for a low: $U = 10$ m/s, $L = 10^6$ m, $\Delta p = 10$ hPa, $f = 10^{-4}$. Then $du/dt \sim U^2/L = 10^{-4}$ m/s², $fU = 10^{-3}$, $\Delta p/(\rho L) = 10^{-3}$. The acceleration is ten times smaller than the other two -- the ratio is the Rossby number $Ro = U/(fL) = 0.1$. At zeroth order what remains is

$$f v_g = \frac{1}{\rho}\frac{\partial p}{\partial x}, \qquad f u_g = -\frac{1}{\rho}\frac{\partial p}{\partial y} \quad\Leftrightarrow\quad \vec v_g = \frac{1}{\rho f}\,\hat k\times\nabla p$$

The wind is perpendicular to $\nabla p$, hence parallel to the isobars, and $\hat k\times\nabla p$ points west when $\nabla p$ points north (low to the south): low on the left.

**Gradient wind.** On a circular path of radius $R$ the acceleration is $v^2/R$ toward the centre. In natural coordinates (direction $n$ to the left of the wind, toward the centre of a cyclonic vortex):

$$\frac{v^2}{R} + f v = \frac{1}{\rho}\frac{\partial p}{\partial n}$$

For the low ($R > 0$, $\partial p/\partial n > 0$) the quadratic solves to $v = -\frac{fR}{2} + \sqrt{\frac{f^2R^2}{4} + \frac{R}{\rho}\frac{\partial p}{\partial n}}$: always real, and because of the $v^2/R$ term smaller than $v_g$ -- subgeostrophic, by 10-20 % at $R = 500$ km. For the high ($R < 0$, $\partial p/\partial n < 0$) the root contains $\frac{f^2R^2}{4} - \frac{|R|}{\rho}\left|\frac{\partial p}{\partial n}\right|$, which turns negative as soon as

$$\left|\frac{\partial p}{\partial n}\right| > \frac{\rho\,f^2\,|R|}{4}$$

With $\rho = 1.2$, $f = 10^{-4}$, $|R| = 1000$ km: $3\cdot 10^{-3}$ Pa/m, i.e. 3 hPa per 100 km -- more than that a high of this size cannot hold. A hurricane has 100 hPa per 100 km.

**Cyclostrophic.** For $Ro \gg 1$, $f$ drops out: $v^2/R = \frac{1}{\rho}\partial p/\partial n$, the tornado and the dust devil -- they spin either way, because nothing prescribes the direction.

**Where it stops holding:** near the ground (friction turns the wind toward the low), at the equator ($f = 0$, Ro arbitrarily large), in fronts and jet streaks (accelerations of order $fU$, ageostrophic wind), and wherever $\partial p/\partial t$ is no longer small -- in cyclogenesis."""),

# ---------------------------------------------------------------------------
"dy-thermisch": t(r"""## Herleitung: Hypsometrie und thermischer Wind

**Hypsometrische Gleichung.** Aus $dp/p = -g\,dz/(R_L T_v)$, integriert zwischen zwei Druckflächen:

$$z_2 - z_1 = \frac{R_L}{g}\int_{p_2}^{p_1} T_v\,\frac{dp}{p} = \frac{R_L\,\overline{T_v}}{g}\,\ln\frac{p_1}{p_2}$$

mit $\overline{T_v}$ dem logarithmisch über den Druck gemittelten $T_v$. Für 1000/500 hPa: $\Delta z = 20{,}3\,\mathrm{m/K}\cdot\overline{T_v}$. Jedes Kelvin Mitteltemperatur ist 20 m Schichtdicke.

**Geostrophie in Druckkoordinaten.** Auf einer Druckfläche ist $\nabla_p p = 0$, und der horizontale Druckgradient bei festem $z$ wird zum Höhengradienten bei festem $p$: $\frac{1}{\rho}\nabla_z p = g\,\nabla_p z = \nabla_p\Phi$ mit dem Geopotential $\Phi = gz$. Die Dichte verschwindet aus der Gleichung:

$$\vec v_g = \frac{1}{f}\,\hat k\times\nabla_p\Phi$$

Das ist der Grund, warum Höhenkarten die Höhe einer Druckfläche zeigen und nicht den Druck in einer Höhe.

**Thermischer Wind.** Die Differenz des geostrophischen Windes zwischen zwei Druckflächen:

$$\vec v_{g,2} - \vec v_{g,1} = \frac{1}{f}\,\hat k\times\nabla_p(\Phi_2 - \Phi_1) = \frac{R_L}{f}\,\ln\frac{p_1}{p_2}\;\hat k\times\nabla_p\overline{T_v}$$

mit der hypsometrischen Gleichung für $\Phi_2 - \Phi_1$. Differentiell: $\frac{\partial\vec v_g}{\partial\ln p} = -\frac{R_L}{f}\,\hat k\times\nabla_p T$. Der thermische Windvektor steht senkrecht auf $\nabla T$, mit der kalten Luft zur Linken -- genau wie der geostrophische Wind senkrecht auf $\nabla\Phi$ mit dem Tief zur Linken steht. Mit $|\nabla T| = 10^{-5}$ K/m (1 K je 100 km), $f = 10^{-4}$: $\Delta v = 287\cdot 10^{-5}\cdot 0{,}693/10^{-4} = 20$ m/s zwischen 1000 und 500 hPa.

**Der Jet.** Von 1000 bis 250 hPa ist $\ln(p_1/p_2) = 1{,}39$: 40 m/s bei 1 K/100 km. An der Polarfront mit 2 K/100 km über 500 km Breite: 80 m/s -- der Jetstream im Winter. Oberhalb der Tropopause kehrt $\nabla T$ um, der Wind nimmt wieder ab: Der Jet liegt an der Tropopause, weil dort das Vorzeichen wechselt.

**Advektion.** Dreht der Wind mit der Höhe nach rechts, zeigt $\vec v_{g,2} - \vec v_{g,1}$ nach rechts vom Bodenwind; die kalte Luft liegt links davon, also hinter dem Bodenwind -- er bringt Warmluft. Linksdrehung: Kaltluftadvektion.

**Wo es aufhört zu gelten:** Überall, wo der Wind nicht geostrophisch ist -- in der Grenzschicht, in Fronten, in der Konvektion. Der thermische Wind ist eine Aussage über das Gleichgewicht, nicht über die Ursache: Ob der Temperaturgradient den Wind erzeugt oder umgekehrt, sagt die Gleichung nicht.""",
r"""## Derivation: hypsometry and thermal wind

**Hypsometric equation.** From $dp/p = -g\,dz/(R_L T_v)$, integrated between two pressure surfaces:

$$z_2 - z_1 = \frac{R_L}{g}\int_{p_2}^{p_1} T_v\,\frac{dp}{p} = \frac{R_L\,\overline{T_v}}{g}\,\ln\frac{p_1}{p_2}$$

with $\overline{T_v}$ the $T_v$ averaged logarithmically over pressure. For 1000/500 hPa: $\Delta z = 20.3\,\mathrm{m/K}\cdot\overline{T_v}$. Every kelvin of mean temperature is 20 m of thickness.

**Geostrophy in pressure coordinates.** On a pressure surface $\nabla_p p = 0$, and the horizontal pressure gradient at fixed $z$ becomes the height gradient at fixed $p$: $\frac{1}{\rho}\nabla_z p = g\,\nabla_p z = \nabla_p\Phi$ with geopotential $\Phi = gz$. The density disappears from the equation:

$$\vec v_g = \frac{1}{f}\,\hat k\times\nabla_p\Phi$$

That is why upper-air charts show the height of a pressure surface and not the pressure at a height.

**Thermal wind.** The difference of the geostrophic wind between two pressure surfaces:

$$\vec v_{g,2} - \vec v_{g,1} = \frac{1}{f}\,\hat k\times\nabla_p(\Phi_2 - \Phi_1) = \frac{R_L}{f}\,\ln\frac{p_1}{p_2}\;\hat k\times\nabla_p\overline{T_v}$$

using the hypsometric equation for $\Phi_2 - \Phi_1$. Differentially: $\frac{\partial\vec v_g}{\partial\ln p} = -\frac{R_L}{f}\,\hat k\times\nabla_p T$. The thermal wind vector is perpendicular to $\nabla T$, with the cold air on its left -- just as the geostrophic wind is perpendicular to $\nabla\Phi$ with the low on its left. With $|\nabla T| = 10^{-5}$ K/m (1 K per 100 km), $f = 10^{-4}$: $\Delta v = 287\cdot 10^{-5}\cdot 0.693/10^{-4} = 20$ m/s between 1000 and 500 hPa.

**The jet.** From 1000 to 250 hPa, $\ln(p_1/p_2) = 1.39$: 40 m/s at 1 K/100 km. At the polar front with 2 K/100 km over 500 km of width: 80 m/s -- the winter jet stream. Above the tropopause $\nabla T$ reverses and the wind decreases again: the jet sits at the tropopause because the sign changes there.

**Advection.** If the wind veers with height, $\vec v_{g,2} - \vec v_{g,1}$ points to the right of the surface wind; the cold air lies to its left, i.e. behind the surface wind -- it brings warm air. Backing: cold advection.

**Where it stops holding:** wherever the wind is not geostrophic -- in the boundary layer, in fronts, in convection. The thermal wind is a statement about balance, not about cause: whether the temperature gradient produces the wind or vice versa, the equation does not say."""),

# ---------------------------------------------------------------------------
"dy-reibung": t(r"""## Herleitung: die Ekman-Spirale

Turbulente Reibung je Masse als Diffusion von Impuls: $\vec F = K\,\partial^2\vec v/\partial z^2$ mit konstantem $K$. Stationär und mit geostrophischem Druckgradienten ($\frac{1}{\rho}\nabla p = f\,\hat k\times\vec v_g$) lautet die Horizontalgleichung

$$f\,(v - v_g) + K\frac{\partial^2 u}{\partial z^2} = 0, \qquad -f\,(u - u_g) + K\frac{\partial^2 v}{\partial z^2} = 0$$

Lege $x$ in Richtung von $\vec v_g$ ($v_g = 0$). Mit der komplexen Abweichung $w = (u - u_g) + i\,v$ werden beide Gleichungen zu einer: $K\,w'' = i f\,w$. Lösung $w = A\,e^{-(1+i)z/D_E}$ mit $D_E = \sqrt{2K/f}$, und der Bedingung $u = v = 0$ am Boden ($A = -u_g$):

$$u = u_g\left(1 - e^{-z/D_E}\cos\frac{z}{D_E}\right), \qquad v = u_g\,e^{-z/D_E}\sin\frac{z}{D_E}$$

Am Boden ($z \to 0$): $v/u \to 1$, der Wind weht 45° links von $\vec v_g$, zum tiefen Druck. Bei $z = \pi D_E$ ist $v = 0$ und $u = u_g(1 + e^{-\pi}) \approx u_g$: die Oberkante der Ekman-Schicht, $D = \pi\sqrt{2K/f}$. Mit $K = 10$ m²/s, $f = 10^{-4}$: 1400 m.

**Ekman-Pumpen.** Der Massentransport quer zum geostrophischen Wind, integriert über die Schicht: $M_v = \int_0^D v\,dz = u_g D_E/2$ -- zum tiefen Druck hin. Ist der geostrophische Wind nicht gleichförmig, sondern hat er die Wirbelstärke $\zeta_g = \partial v_g/\partial x - \partial u_g/\partial y$, konvergiert dieser Transport, und die Kontinuität zwingt zu

$$w_E = \frac{D_E}{2}\,\zeta_g = \zeta_g\sqrt{\frac{K}{2f}}$$

Mit $\zeta_g = 10^{-5}$ /s: $w_E = 2$ mm/s, 190 m am Tag. Für eine Spindown-Zeit: Die Wirbelstärke oberhalb der Grenzschicht nimmt durch Streckung ab, $d\zeta/dt = -f\,w_E/H$, also $\tau = H/(f D_E/2) = \frac{2H}{f}\sqrt{\frac{f}{2K}}$: mit $H = 10$ km etwa 4 Tage. Das ist die Lebensdauer eines Tiefs ohne Nachschub.

**Wo es aufhört zu gelten:** $K$ ist nicht konstant -- es wächst mit der Höhe und mit der Labilität, und nachts bricht die Turbulenz zusammen. Reale Winddrehungen sind 10-30°, nicht 45°. Über dem Ozean mit $K = 1$: $D = 450$ m. In der konvektiven Grenzschicht am Nachmittag ist das Bild einer Spirale ganz falsch; da mischt die Konvektion den Impuls in einem Schlag bis zur Inversion.""",
r"""## Derivation: the Ekman spiral

Turbulent friction per mass as diffusion of momentum: $\vec F = K\,\partial^2\vec v/\partial z^2$ with constant $K$. Steady and with a geostrophic pressure gradient ($\frac{1}{\rho}\nabla p = f\,\hat k\times\vec v_g$) the horizontal equation reads

$$f\,(v - v_g) + K\frac{\partial^2 u}{\partial z^2} = 0, \qquad -f\,(u - u_g) + K\frac{\partial^2 v}{\partial z^2} = 0$$

Put $x$ along $\vec v_g$ ($v_g = 0$). With the complex departure $w = (u - u_g) + i\,v$ both equations become one: $K\,w'' = i f\,w$. Solution $w = A\,e^{-(1+i)z/D_E}$ with $D_E = \sqrt{2K/f}$, and the condition $u = v = 0$ at the ground ($A = -u_g$):

$$u = u_g\left(1 - e^{-z/D_E}\cos\frac{z}{D_E}\right), \qquad v = u_g\,e^{-z/D_E}\sin\frac{z}{D_E}$$

At the ground ($z \to 0$): $v/u \to 1$, the wind blows 45° to the left of $\vec v_g$, toward low pressure. At $z = \pi D_E$, $v = 0$ and $u = u_g(1 + e^{-\pi}) \approx u_g$: the top of the Ekman layer, $D = \pi\sqrt{2K/f}$. With $K = 10$ m²/s, $f = 10^{-4}$: 1400 m.

**Ekman pumping.** The mass transport across the geostrophic wind, integrated over the layer: $M_v = \int_0^D v\,dz = u_g D_E/2$ -- toward low pressure. If the geostrophic wind is not uniform but has vorticity $\zeta_g = \partial v_g/\partial x - \partial u_g/\partial y$, this transport converges, and continuity forces

$$w_E = \frac{D_E}{2}\,\zeta_g = \zeta_g\sqrt{\frac{K}{2f}}$$

With $\zeta_g = 10^{-5}$ /s: $w_E = 2$ mm/s, 190 m a day. For a spin-down time: the vorticity above the boundary layer decreases by stretching, $d\zeta/dt = -f\,w_E/H$, so $\tau = H/(f D_E/2) = \frac{2H}{f}\sqrt{\frac{f}{2K}}$: with $H = 10$ km about 4 days. That is the lifetime of a low without resupply.

**Where it stops holding:** $K$ is not constant -- it grows with height and with instability, and at night the turbulence collapses. Real wind turnings are 10-30°, not 45°. Over the ocean with $K = 1$: $D = 450$ m. In the convective boundary layer of the afternoon the picture of a spiral is entirely wrong; there convection mixes the momentum in one go up to the inversion."""),

# ---------------------------------------------------------------------------
"zi-hadley": t(r"""## Herleitung: Drehimpuls auf der Kugel

Der Drehimpuls je Masse um die Erdachse ist $M = (\Omega\,a\cos\varphi + u)\,a\cos\varphi$: der Abstand von der Achse $a\cos\varphi$ mal der absoluten Zonalgeschwindigkeit (Mitrotation der Erde plus Relativwind $u$). Ohne Drehmoment -- keine Reibung, kein zonaler Druckgradient -- bleibt $M$ erhalten. Ein Paket, das am Äquator mit $u = 0$ startet, hat $M = \Omega a^2$. In der Breite $\varphi$:

$$(\Omega a\cos\varphi + u)\,a\cos\varphi = \Omega a^2 \quad\Rightarrow\quad u = \Omega a\,\frac{1 - \cos^2\varphi}{\cos\varphi} = \Omega a\,\frac{\sin^2\varphi}{\cos\varphi}$$

$\Omega a = 465$ m/s ist die Umfangsgeschwindigkeit des Äquators. Bei 10°: 8 m/s. 20°: 58. 30°: 134. 45°: 329. 60°: 697. Die Hadley-Zelle kann so weit reichen, wie der entstehende Jet stabil bleibt -- und das ist bei etwa 30° vorbei: Held und Hou (1980) zeigen, dass die Breite der Zelle mit $\sqrt{gH\Delta\theta/(\theta\,\Omega^2 a^2)}$ geht, rund 30° für die Erde. Auf der langsam rotierenden Venus reicht die Zelle bis zum Pol.

**Der Wärmetransport.** Die Massenzirkulation der Hadley-Zelle ist $\Psi \approx 10^{11}$ kg/s. Oben strömt Luft mit feuchtstatischer Energie $h = c_pT + gz + L_v r \approx 340$ kJ/kg polwärts (trocken, hoch), unten mit 310 kJ/kg zurück (feucht, aber warm und tief -- die feuchtstatische Energie ist unten *kleiner*, weil $gz$ fehlt). Transport: $\Psi\,\Delta h = 10^{11}\cdot 3\cdot 10^4 = 3\cdot 10^{15}$ W.

**Wo es aufhört zu gelten:** Reibung und die Wirbel der Breiten über 30° führen Drehimpuls ab, deshalb hat der Subtropenjet 40 statt 134 m/s. Die Zelle ist nicht achsensymmetrisch (Monsune) und nicht stationär (sie wandert mit der Jahreszeit und wird im Winter der jeweiligen Hemisphäre viel stärker).""",
r"""## Derivation: angular momentum on the sphere

The angular momentum per mass about the Earth's axis is $M = (\Omega\,a\cos\varphi + u)\,a\cos\varphi$: the distance from the axis $a\cos\varphi$ times the absolute zonal velocity (co-rotation of the Earth plus relative wind $u$). Without torque -- no friction, no zonal pressure gradient -- $M$ is conserved. A parcel starting at the equator with $u = 0$ has $M = \Omega a^2$. At latitude $\varphi$:

$$(\Omega a\cos\varphi + u)\,a\cos\varphi = \Omega a^2 \quad\Rightarrow\quad u = \Omega a\,\frac{1 - \cos^2\varphi}{\cos\varphi} = \Omega a\,\frac{\sin^2\varphi}{\cos\varphi}$$

$\Omega a = 465$ m/s is the speed of the equator. At 10°: 8 m/s. 20°: 58. 30°: 134. 45°: 329. 60°: 697. The Hadley cell can reach as far as the resulting jet stays stable -- and that ends at about 30°: Held and Hou (1980) show that the width of the cell goes as $\sqrt{gH\Delta\theta/(\theta\,\Omega^2 a^2)}$, about 30° for the Earth. On slowly rotating Venus the cell reaches the pole.

**The heat transport.** The mass circulation of the Hadley cell is $\Psi \approx 10^{11}$ kg/s. Aloft air flows poleward with moist static energy $h = c_pT + gz + L_v r \approx 340$ kJ/kg (dry, high), below it returns with 310 kJ/kg (moist, but warm and low -- the moist static energy is *smaller* below because $gz$ is missing). Transport: $\Psi\,\Delta h = 10^{11}\cdot 3\cdot 10^4 = 3\cdot 10^{15}$ W.

**Where it stops holding:** friction and the eddies of latitudes above 30° carry angular momentum away, which is why the subtropical jet has 40 rather than 134 m/s. The cell is not axisymmetric (monsoons) and not stationary (it migrates with the season and becomes much stronger in the winter of the respective hemisphere)."""),

# ---------------------------------------------------------------------------
"zi-rossby": t(r"""## Herleitung: die Vorticity-Gleichung und ihre Welle

**Absolute Wirbelstärke.** Die vertikale Komponente der Rotation des Windes relativ zur Erde ist $\zeta = \partial v/\partial x - \partial u/\partial y$; die der Erdrotation selbst ist $2\Omega\sin\varphi = f$ (die Vertikalkomponente von $2\vec\Omega$, siehe Coriolis). Nimmt man die Rotation der horizontalen Bewegungsgleichung (mit $\partial/\partial x$ der $v$-Gleichung minus $\partial/\partial y$ der $u$-Gleichung) und lässt Divergenz, Reibung und Vertikalbewegung weg, bleibt

$$\frac{d}{dt}(\zeta + f) = 0$$

Das ist die barotrope Vorticity-Gleichung: Die absolute Wirbelstärke eines Luftpakets ist erhalten. Der Druckgradient fällt heraus, weil $\nabla\times\nabla p = 0$.

**Die Welle.** Grundstrom $U$ nach Osten, kleine Störung $\psi$ mit $u' = -\partial\psi/\partial y$, $v' = \partial\psi/\partial x$, $\zeta' = \nabla^2\psi$. Linearisiert, mit $df/dt = v'\,df/dy = \beta\,v'$:

$$\left(\frac{\partial}{\partial t} + U\frac{\partial}{\partial x}\right)\nabla^2\psi + \beta\,\frac{\partial\psi}{\partial x} = 0$$

Ansatz $\psi = \psi_0\,e^{i(kx + ly - \omega t)}$: $(-i\omega + iUk)(-k^2 - l^2) + i\beta k = 0$, also

$$\omega = Uk - \frac{\beta k}{k^2 + l^2}, \qquad c = \frac{\omega}{k} = U - \frac{\beta}{k^2 + l^2}$$

Für $l = 0$ die Formel der Lektion. Stationär bei $k_s^2 = \beta/U$, also $L_s = 2\pi\sqrt{U/\beta}$. Mit $\beta = 2\Omega\cos\varphi/a = 1{,}6\cdot 10^{-11}$ in 45° und $U = 15$ m/s: 6000 km, Wellenzahl 4,7 um den Breitenkreis.

**Gruppengeschwindigkeit:** $c_g = \partial\omega/\partial k = U + \beta(k^2 - l^2)/(k^2+l^2)^2$ -- für $l = 0$ ist $c_g = U + \beta/k^2 > c$: Energie läuft nach Osten, auch wenn die Phase nach Westen läuft. So pflanzt sich eine Störung über dem Pazifik in drei Tagen nach Europa fort, ohne dass die Welle selbst dorthin wandert.

**Wo es aufhört zu gelten:** Barotrop heißt: keine vertikale Struktur, keine Temperaturadvektion -- die Zyklogenese fehlt (barokline Instabilität). Linearisiert heißt: kleine Amplitude; ein Blocking ist nichtlinear. Und $\beta$ konstant ($\beta$-Ebene) stimmt nur über wenige zehn Breitengrade.""",
r"""## Derivation: the vorticity equation and its wave

**Absolute vorticity.** The vertical component of the curl of the wind relative to the Earth is $\zeta = \partial v/\partial x - \partial u/\partial y$; that of the Earth's rotation itself is $2\Omega\sin\varphi = f$ (the vertical component of $2\vec\Omega$, see Coriolis). Taking the curl of the horizontal equation of motion ($\partial/\partial x$ of the $v$ equation minus $\partial/\partial y$ of the $u$ equation) and dropping divergence, friction and vertical motion leaves

$$\frac{d}{dt}(\zeta + f) = 0$$

That is the barotropic vorticity equation: the absolute vorticity of a parcel is conserved. The pressure gradient drops out because $\nabla\times\nabla p = 0$.

**The wave.** Mean flow $U$ eastward, small perturbation $\psi$ with $u' = -\partial\psi/\partial y$, $v' = \partial\psi/\partial x$, $\zeta' = \nabla^2\psi$. Linearised, with $df/dt = v'\,df/dy = \beta\,v'$:

$$\left(\frac{\partial}{\partial t} + U\frac{\partial}{\partial x}\right)\nabla^2\psi + \beta\,\frac{\partial\psi}{\partial x} = 0$$

Ansatz $\psi = \psi_0\,e^{i(kx + ly - \omega t)}$: $(-i\omega + iUk)(-k^2 - l^2) + i\beta k = 0$, hence

$$\omega = Uk - \frac{\beta k}{k^2 + l^2}, \qquad c = \frac{\omega}{k} = U - \frac{\beta}{k^2 + l^2}$$

For $l = 0$ the lesson's formula. Stationary at $k_s^2 = \beta/U$, i.e. $L_s = 2\pi\sqrt{U/\beta}$. With $\beta = 2\Omega\cos\varphi/a = 1.6\cdot 10^{-11}$ at 45° and $U = 15$ m/s: 6000 km, wavenumber 4.7 around the latitude circle.

**Group velocity:** $c_g = \partial\omega/\partial k = U + \beta(k^2 - l^2)/(k^2+l^2)^2$ -- for $l = 0$, $c_g = U + \beta/k^2 > c$: energy travels east even when the phase travels west. That is how a disturbance over the Pacific propagates to Europe in three days without the wave itself moving there.

**Where it stops holding:** barotropic means: no vertical structure, no temperature advection -- cyclogenesis is missing (baroclinic instability). Linearised means: small amplitude; a block is nonlinear. And constant $\beta$ ($\beta$-plane) holds only over a few tens of degrees of latitude."""),

# ---------------------------------------------------------------------------
"sy-fronten": t(r"""## Herleitung: die Margules-Formel

Zwei Luftmassen, kalt (1) unter warm (2), getrennt von einer Fläche mit Neigung $\alpha$. Beide seien geostrophisch mit frontparallelem Wind $u_1$, $u_2$. Entlang der Front ($x$-Richtung) herrscht in beiden derselbe Druck -- sonst wäre die Fläche nicht stationär. Quer dazu (in $y$, zur kalten Seite) gilt in jeder Luftmasse Geostrophie, $\partial p/\partial y = -\rho f u$, und senkrecht Hydrostatik, $\partial p/\partial z = -\rho g$.

Auf der Frontfläche ist $p_1 = p_2$ überall, also auch $dp_1 = dp_2$ längs der Fläche:

$$\frac{\partial p_1}{\partial y}dy + \frac{\partial p_1}{\partial z}dz = \frac{\partial p_2}{\partial y}dy + \frac{\partial p_2}{\partial z}dz$$

Einsetzen und nach $dz/dy = \tan\alpha$ auflösen:

$$\tan\alpha = \frac{f\,(\rho_2 u_2 - \rho_1 u_1)}{g\,(\rho_1 - \rho_2)}$$

Mit $\rho = p/(R_L T)$ bei gleichem Druck: $\rho_1 - \rho_2 \approx \rho\,(T_2 - T_1)/T$, und für $\rho_1 \approx \rho_2$ im Zähler:

$$\tan\alpha \approx \frac{f\,T}{g}\,\frac{u_2 - u_1}{T_2 - T_1}$$

Damit die kalte Luft als Keil **unter** der warmen liegt und $\tan\alpha > 0$, muss $u_2 > u_1$ sein: Die warme Luft strömt schneller nach Osten (mit der kalten Luft zur Linken, Nordhalbkugel) -- das ist der thermische Wind in konzentrierter Form. Ohne Rotation ($f = 0$) wäre $\alpha = 0$: Die schwere Luft würde sich flach ausbreiten, wie Wasser unter Öl.

**Zahlen:** $f = 10^{-4}$, $T = 280$ K, $\Delta u = 10$ m/s, $\Delta T = 10$ K: $\tan\alpha = 2{,}9\cdot 10^{-3}$, 1:340. Mit $\Delta u = 30$ m/s (Jet über der Front): 1:110.

**Wo es aufhört zu gelten:** Reale Fronten sind keine Unstetigkeitsflächen, sondern 50-100 km breite Zonen, und nicht stationär. In der Grenzschicht bremst Reibung die Kaltluft am Boden, der Keil wird dort steiler (Kaltfront 1:50) oder flacher (Warmfront, die über ihrer eigenen Bodenreibung aufgleitet). Die Formel gibt die Größenordnung und den Zusammenhang mit der Scherung -- nicht die Form.""",
r"""## Derivation: the Margules formula

Two air masses, cold (1) beneath warm (2), separated by a surface of slope $\alpha$. Let both be geostrophic with front-parallel wind $u_1$, $u_2$. Along the front ($x$ direction) both have the same pressure -- otherwise the surface would not be stationary. Across it (in $y$, toward the cold side) geostrophy holds in each air mass, $\partial p/\partial y = -\rho f u$, and vertically hydrostatics, $\partial p/\partial z = -\rho g$.

On the frontal surface $p_1 = p_2$ everywhere, hence also $dp_1 = dp_2$ along the surface:

$$\frac{\partial p_1}{\partial y}dy + \frac{\partial p_1}{\partial z}dz = \frac{\partial p_2}{\partial y}dy + \frac{\partial p_2}{\partial z}dz$$

Substitute and solve for $dz/dy = \tan\alpha$:

$$\tan\alpha = \frac{f\,(\rho_2 u_2 - \rho_1 u_1)}{g\,(\rho_1 - \rho_2)}$$

With $\rho = p/(R_L T)$ at equal pressure: $\rho_1 - \rho_2 \approx \rho\,(T_2 - T_1)/T$, and for $\rho_1 \approx \rho_2$ in the numerator:

$$\tan\alpha \approx \frac{f\,T}{g}\,\frac{u_2 - u_1}{T_2 - T_1}$$

For the cold air to lie as a wedge **beneath** the warm and $\tan\alpha > 0$, we need $u_2 > u_1$: the warm air flows faster eastward (with the cold air on its left, northern hemisphere) -- that is the thermal wind in concentrated form. Without rotation ($f = 0$), $\alpha = 0$: the heavy air would spread out flat, like water under oil.

**Numbers:** $f = 10^{-4}$, $T = 280$ K, $\Delta u = 10$ m/s, $\Delta T = 10$ K: $\tan\alpha = 2.9\cdot 10^{-3}$, 1:340. With $\Delta u = 30$ m/s (jet above the front): 1:110.

**Where it stops holding:** real fronts are not discontinuities but zones 50-100 km wide, and not stationary. In the boundary layer friction slows the cold air at the ground, the wedge becomes steeper there (cold front 1:50) or shallower (warm front gliding over its own surface friction). The formula gives the order of magnitude and the link to the shear -- not the shape."""),

# ---------------------------------------------------------------------------
"sy-zyklone": t(r"""## Herleitung: warum barokline Wellen wachsen, und wie groß sie sind

**Verfügbare potentielle Energie.** Die Flächen gleicher potentieller Temperatur neigen sich vom Äquator (hoch) zum Pol (tief). Vertauscht man zwei Pakete gleicher Masse, das warme nach oben-polwärts, das kalte nach unten-äquatorwärts, so sinkt der Schwerpunkt, wenn die Vertauschungsbahn *flacher* ist als die Isentropen: Das warme Paket kommt dann in eine Umgebung, die kälter ist als es selbst, und ist leichter -- es steigt weiter. Die Steigung der Isentropen ist $s_\theta = -\frac{\partial\theta/\partial y}{\partial\theta/\partial z}$; mit $\partial\theta/\partial y = -3\cdot 10^{-6}$ K/m (30 K über 10 000 km) und $\partial\theta/\partial z = 3\cdot 10^{-3}$ K/m: $s_\theta = 10^{-3}$, also 10 km auf 10 000 km. Störungen mit Bahnneigung zwischen 0 und $s_\theta$ gewinnen Energie; am meisten bei $s_\theta/2$.

**Eadys Modell** (1949): Grundstrom $U(z) = \Lambda z$ zwischen zwei starren Deckeln im Abstand $H$, konstantes $N$ und $f$, $\beta = 0$. Die quasi-geostrophische potentielle Wirbelstärke ist dann im Inneren erhalten und die Dynamik sitzt an den Rändern. Die Wachstumsrate einer Welle mit Wellenzahl $k$ ergibt sich aus einer Dispersionsrelation, deren instabiler Ast bei

$$k\,L_R < 2{,}4, \qquad L_R = \frac{N\,H}{f}$$

liegt, mit dem maximalen Wachstum bei $k L_R = 1{,}6$, also $L_{max} = 2\pi L_R/1{,}6 = 3{,}9\,L_R$. Die zugehörige Wachstumsrate ist $\sigma_{max} = 0{,}31\,\frac{f}{N}\,\Lambda = 0{,}31\,\frac{f\,\Delta U}{N\,H}$. Mit $N = 0{,}01$, $H = 10$ km, $f = 10^{-4}$: $L_R = 1000$ km, $L_{max} = 3900$ km, und mit $\Delta U = 30$ m/s über die Troposphäre: $\sigma = 0{,}31\cdot 10^{-4}\cdot 30/(0{,}01\cdot 10^4) = 9{,}3\cdot 10^{-6}$ /s, Verdopplung in $\ln 2/\sigma = 21$ Stunden.

**Warum lange Wellen nicht wachsen:** Eine Welle länger als $2\pi L_R/2{,}4$ hat zu wenig vertikale Kopplung zwischen den Rändern; kürzere als $L_R$ sind zu flach gegen die Isentropen -- die Rossby-Länge ist genau die Skala, auf der Rotation und Schichtung gleich wichtig sind, $f L \sim N H$.

**Der Trog voraus.** Im wachsenden Modus ist die Welle mit der Höhe nach Westen geneigt, um etwa ein Viertel der Wellenlänge zwischen Boden und Tropopause. Nur so kann sie Wärme polwärts transportieren ($v'$ und $T'$ in Phase) und die Energie aus dem Grundstrom ziehen.

**Wo es aufhört zu gelten:** Eady hat weder $\beta$ (das bringt Charney) noch Feuchte (die Kondensation in der Warmluft verdoppelt die Wachstumsrate -- deshalb explosive Zyklonen über dem warmen Golfstrom) noch die nichtlineare Sättigung, bei der die Welle bricht und okkludiert. Nach 2-3 Verdopplungen ist das lineare Modell am Ende; danach beginnt die Synoptik.""",
r"""## Derivation: why baroclinic waves grow, and how large they are

**Available potential energy.** Surfaces of equal potential temperature slope from the equator (high) to the pole (low). Exchange two parcels of equal mass, the warm one up and poleward, the cold one down and equatorward: the centre of mass drops if the exchange path is *shallower* than the isentropes: the warm parcel then arrives in surroundings colder than itself and is lighter -- it keeps rising. The slope of the isentropes is $s_\theta = -\frac{\partial\theta/\partial y}{\partial\theta/\partial z}$; with $\partial\theta/\partial y = -3\cdot 10^{-6}$ K/m (30 K over 10 000 km) and $\partial\theta/\partial z = 3\cdot 10^{-3}$ K/m: $s_\theta = 10^{-3}$, i.e. 10 km over 10 000 km. Disturbances with path slope between 0 and $s_\theta$ gain energy; most at $s_\theta/2$.

**Eady's model** (1949): mean flow $U(z) = \Lambda z$ between two rigid lids a distance $H$ apart, constant $N$ and $f$, $\beta = 0$. The quasi-geostrophic potential vorticity is then conserved in the interior and the dynamics sits at the boundaries. The growth rate of a wave with wavenumber $k$ follows from a dispersion relation whose unstable branch lies at

$$k\,L_R < 2.4, \qquad L_R = \frac{N\,H}{f}$$

with maximum growth at $k L_R = 1.6$, i.e. $L_{max} = 2\pi L_R/1.6 = 3.9\,L_R$. The corresponding growth rate is $\sigma_{max} = 0.31\,\frac{f}{N}\,\Lambda = 0.31\,\frac{f\,\Delta U}{N\,H}$. With $N = 0.01$, $H = 10$ km, $f = 10^{-4}$: $L_R = 1000$ km, $L_{max} = 3900$ km, and with $\Delta U = 30$ m/s across the troposphere: $\sigma = 0.31\cdot 10^{-4}\cdot 30/(0.01\cdot 10^4) = 9.3\cdot 10^{-6}$ /s, doubling in $\ln 2/\sigma = 21$ hours.

**Why long waves do not grow:** a wave longer than $2\pi L_R/2.4$ has too little vertical coupling between the boundaries; shorter than $L_R$ they are too shallow against the isentropes -- the Rossby length is exactly the scale on which rotation and stratification are equally important, $f L \sim N H$.

**The trough ahead.** In the growing mode the wave tilts westward with height, by about a quarter wavelength between the ground and the tropopause. Only so can it transport heat poleward ($v'$ and $T'$ in phase) and draw energy from the mean flow.

**Where it stops holding:** Eady has neither $\beta$ (Charney adds that) nor moisture (condensation in the warm air doubles the growth rate -- hence explosive cyclones over the warm Gulf Stream) nor the nonlinear saturation in which the wave breaks and occludes. After 2-3 doublings the linear model is at its end; after that synoptics begins."""),

# ---------------------------------------------------------------------------
"me-foehn": t(r"""## Herleitung: die Föhnrechnung Schritt für Schritt

Luv: $T_0 = 20$ °C, $T_{d,0} = 12$ °C in $z_0 = 500$ m, $p \approx 950$ hPa. Mischungsverhältnis aus dem Taupunkt: $e = e_s(12^\circ\mathrm{C}) = 14{,}0$ hPa, $r = 0{,}622\cdot 14{,}0/(950 - 14) = 9{,}3$ g/kg. Relative Feuchte $14{,}0/23{,}3 = 60$ %.

**Trocken bis zum LCL.** $z_{LCL} - z_0 = 125\,\mathrm{m/K}\cdot 8\,\mathrm{K} = 1000$ m, also 1500 m. Dort $T = 20 - 9{,}8\cdot 1{,}0 = 10{,}2$ °C -- und $T_d = 12 - 1{,}8 = 10{,}2$ °C, die Probe stimmt: gesättigt.

**Feucht bis zum Kamm.** $\Gamma_s$ bei 5 °C und 850 hPa: $r_s = 6{,}4$ g/kg, Formel aus Kapitel 3: 5,5 K/km; bei 0 °C, 750 hPa: 6,2 K/km. Mittel rund 6 K/km über 1500 m: $T_{Kamm} = 10{,}2 - 9 = 1{,}2$ °C. Dort $r_s(1{,}2^\circ\mathrm{C}, 700\,\mathrm{hPa}) = 0{,}622\cdot 6{,}7/693 = 6{,}0$ g/kg. **Ausgeregnet:** $9{,}3 - 6{,}0 = 3{,}3$ g/kg -- nicht 9, wie es die runde Zahl in der Lektion sagt; die Lektion rechnet grob, hier steht die Buchhaltung.

**Trocken ins Lee.** 2500 m abwärts mit 9,8 K/km: $T_{Lee} = 1{,}2 + 24{,}5 = 25{,}7$ °C. Das Mischungsverhältnis bleibt 6,0 g/kg; bei 25,7 °C und 950 hPa ist $r_s = 21{,}9$ g/kg: relative Feuchte **27 %** (die Lektion sagt 10 % -- das gilt, wenn mehr ausregnet oder die Luft aus Kammhöhe stammt).

**Die Bilanz in $\theta$ und $\theta_e$:** $\theta$ im Luv: $293{,}15\cdot(1000/950)^{0{,}286} = 297{,}5$ K. Im Lee: $298{,}85\cdot(1000/950)^{0{,}286} = 303{,}3$ K. Zuwachs 5,8 K. Latent frei geworden: $L_v\,\Delta r/c_p = 2{,}5\cdot 10^6\cdot 0{,}0033/1004 = 8{,}2$ K -- mehr als die 5,8, weil ein Teil der Kondensationswärme in der Höhe bleibt, wo die Feuchtadiabate schon mit kleinerem $\Gamma$ gerechnet hat. $\theta_e$ ist in beiden gleich, bis auf die Näherungen: das ist die Probe auf die Rechnung.

**Wo es aufhört zu gelten:** Die ganze Rechnung ist Thermodynamik ohne Dynamik. Ob die Luft überhaupt über den Kamm steigt oder sich staut (Froude-Zahl $Fr = U/(Nh) < 1$: Blockierung, die Luft fließt um das Gebirge herum), und ob sie im Lee bis zum Boden absinkt oder in Kammhöhe weiterströmt (hydraulischer Sprung, Schwerewellenbrechen), entscheidet die Schichtung oberhalb des Kamms. Der "trockene Föhn" ohne Niederschlag ist häufiger als der Lehrbuchföhn.""",
r"""## Derivation: the foehn calculation step by step

Windward: $T_0 = 20$ °C, $T_{d,0} = 12$ °C at $z_0 = 500$ m, $p \approx 950$ hPa. Mixing ratio from the dew point: $e = e_s(12^\circ\mathrm{C}) = 14.0$ hPa, $r = 0.622\cdot 14.0/(950 - 14) = 9.3$ g/kg. Relative humidity $14.0/23.3 = 60$ %.

**Dry to the LCL.** $z_{LCL} - z_0 = 125\,\mathrm{m/K}\cdot 8\,\mathrm{K} = 1000$ m, hence 1500 m. There $T = 20 - 9.8\cdot 1.0 = 10.2$ °C -- and $T_d = 12 - 1.8 = 10.2$ °C, the check works: saturated.

**Moist to the crest.** $\Gamma_s$ at 5 °C and 850 hPa: $r_s = 6.4$ g/kg, formula from chapter 3: 5.5 K/km; at 0 °C, 750 hPa: 6.2 K/km. Mean about 6 K/km over 1500 m: $T_{crest} = 10.2 - 9 = 1.2$ °C. There $r_s(1.2^\circ\mathrm{C}, 700\,\mathrm{hPa}) = 0.622\cdot 6.7/693 = 6.0$ g/kg. **Rained out:** $9.3 - 6.0 = 3.3$ g/kg -- not 9, as the round number in the lesson says; the lesson is rough, here is the bookkeeping.

**Dry into the lee.** 2500 m down at 9.8 K/km: $T_{lee} = 1.2 + 24.5 = 25.7$ °C. The mixing ratio stays 6.0 g/kg; at 25.7 °C and 950 hPa, $r_s = 21.9$ g/kg: relative humidity **27 %** (the lesson says 10 % -- which holds if more rains out or the air comes from crest level).

**The balance in $\theta$ and $\theta_e$:** $\theta$ on the windward side: $293.15\cdot(1000/950)^{0.286} = 297.5$ K. In the lee: $298.85\cdot(1000/950)^{0.286} = 303.3$ K. Gain 5.8 K. Latent heat released: $L_v\,\Delta r/c_p = 2.5\cdot 10^6\cdot 0.0033/1004 = 8.2$ K -- more than the 5.8, because part of the condensation heat stays aloft, where the moist adiabat already computed with a smaller $\Gamma$. $\theta_e$ is the same on both sides, up to the approximations: that is the check on the calculation.

**Where it stops holding:** the whole calculation is thermodynamics without dynamics. Whether the air rises over the crest at all or is blocked (Froude number $Fr = U/(Nh) < 1$: blocking, the air flows around the range), and whether it sinks to the ground in the lee or flows on at crest height (hydraulic jump, gravity wave breaking), is decided by the stratification above the crest. The "dry foehn" without precipitation is more common than the textbook foehn."""),

# ---------------------------------------------------------------------------
"me-seewind": t(r"""## Herleitung: der Zirkulationssatz

Die Zirkulation um eine geschlossene materielle Kurve $C$ (die mit der Strömung mitschwimmt) ist $\Gamma_C = \oint\vec v\cdot d\vec l$. Ihre Zeitableitung:

$$\frac{d\Gamma_C}{dt} = \oint\frac{d\vec v}{dt}\cdot d\vec l + \oint\vec v\cdot\frac{d(d\vec l)}{dt}$$

Der zweite Term ist $\oint\vec v\cdot d\vec v = \oint d(v^2/2) = 0$ auf einer geschlossenen Kurve. In den ersten die Bewegungsgleichung ohne Rotation und Reibung eingesetzt, $d\vec v/dt = -\nabla p/\rho + \vec g$: Das Schwerefeld ist ein Gradient ($\vec g = -\nabla\Phi$), sein Ringintegral verschwindet. Bleibt

$$\frac{d\Gamma_C}{dt} = -\oint\frac{\nabla p}{\rho}\cdot d\vec l = -\oint\frac{dp}{\rho}$$

**Barotrop**, $\rho = \rho(p)$: Dann ist $dp/\rho$ ein totales Differential und das Integral null -- Kelvins Satz, Zirkulation ist erhalten. **Baroklin**, $\rho = \rho(p, T)$: Das Integral ist die Zahl der Solenoide, der Maschen aus Isobaren und Isosteren ($\alpha = 1/\rho$ konstant), die die Kurve umschließt; mit Stokes: $-\oint\alpha\,dp = \int\!\!\int\nabla\alpha\times\nabla p\cdot d\vec A$.

**Der Seewind.** Kurve: am Boden von See (S) nach Land (L), über Land hinauf auf $h$, oben zurück, über See hinunter. Druck am Boden gleich; in der Höhe $h$ über Land $p_L(h)$, über See $p_S(h)$. Mit $\rho = p/(R_L T)$:

$$-\oint\frac{dp}{\rho} = -\oint R_L T\,\frac{dp}{p} = R_L\,(T_L - T_S)\,\ln\frac{p_0}{p_h}$$

(die beiden senkrechten Wege liefern je $R_L T\ln(p_0/p_h)$ mit umgekehrtem Vorzeichen, die waagrechten nichts, wenn der Druck dort konstant ist). Mit $T_L - T_S = 5$ K, $p_0/p_h = 1000/900$ (1 km): $287\cdot 5\cdot 0{,}105 = 151$ m²/s². Verteilt auf eine Kurve von 2·20 km + 2·1 km = 42 km: Beschleunigung $151/42\,000 = 3{,}6\cdot 10^{-3}$ m/s², nach einer Stunde 13 m/s -- die Reibung begrenzt es real auf 5 m/s, und der Drehsinn ist festgelegt: unten zum Land, oben zur See, über Land auf.

**Mit Rotation** kommt $-2\Omega\,dA_e/dt$ hinzu, mit $A_e$ der Projektion der eingeschlossenen Fläche auf die Äquatorebene (Bjerknes' vollständiger Satz); das dreht den Seewind im Tagesverlauf nach rechts.

**Wo es aufhört zu gelten:** Die Kurve muss materiell sein -- mit Reibung und Mischung ist sie es nicht mehr, und die Zirkulation sättigt. Das Argument liefert Antrieb und Drehsinn, nicht die Geschwindigkeit.""",
r"""## Derivation: the circulation theorem

The circulation around a closed material curve $C$ (one that floats with the flow) is $\Gamma_C = \oint\vec v\cdot d\vec l$. Its time derivative:

$$\frac{d\Gamma_C}{dt} = \oint\frac{d\vec v}{dt}\cdot d\vec l + \oint\vec v\cdot\frac{d(d\vec l)}{dt}$$

The second term is $\oint\vec v\cdot d\vec v = \oint d(v^2/2) = 0$ on a closed curve. Into the first insert the equation of motion without rotation and friction, $d\vec v/dt = -\nabla p/\rho + \vec g$: gravity is a gradient ($\vec g = -\nabla\Phi$), its loop integral vanishes. What remains is

$$\frac{d\Gamma_C}{dt} = -\oint\frac{\nabla p}{\rho}\cdot d\vec l = -\oint\frac{dp}{\rho}$$

**Barotropic**, $\rho = \rho(p)$: then $dp/\rho$ is an exact differential and the integral is zero -- Kelvin's theorem, circulation is conserved. **Baroclinic**, $\rho = \rho(p, T)$: the integral is the number of solenoids, the meshes of isobars and isosteres ($\alpha = 1/\rho$ constant), that the curve encloses; with Stokes: $-\oint\alpha\,dp = \int\!\!\int\nabla\alpha\times\nabla p\cdot d\vec A$.

**The sea breeze.** Curve: at the ground from sea (S) to land (L), up over land to $h$, back aloft, down over sea. Surface pressure equal; at height $h$ over land $p_L(h)$, over sea $p_S(h)$. With $\rho = p/(R_L T)$:

$$-\oint\frac{dp}{\rho} = -\oint R_L T\,\frac{dp}{p} = R_L\,(T_L - T_S)\,\ln\frac{p_0}{p_h}$$

(the two vertical legs each give $R_L T\ln(p_0/p_h)$ with opposite sign, the horizontal ones nothing if the pressure is constant there). With $T_L - T_S = 5$ K, $p_0/p_h = 1000/900$ (1 km): $287\cdot 5\cdot 0.105 = 151$ m²/s². Spread over a curve of 2·20 km + 2·1 km = 42 km: acceleration $151/42\,000 = 3.6\cdot 10^{-3}$ m/s², after an hour 13 m/s -- friction limits it in reality to 5 m/s, and the sense is fixed: toward the land below, toward the sea aloft, up over the land.

**With rotation** a term $-2\Omega\,dA_e/dt$ is added, with $A_e$ the projection of the enclosed area onto the equatorial plane (Bjerknes' full theorem); that turns the sea breeze to the right over the day.

**Where it stops holding:** the curve must be material -- with friction and mixing it no longer is, and the circulation saturates. The argument gives the drive and the sense, not the speed."""),

# ---------------------------------------------------------------------------
"me-gewitter": t(r"""## Herleitung: Hagel, Böenfront und Blitzentfernung

**Hagel.** Gewicht $\frac{\pi}{6}D^3\rho_{Eis}\,g$ gleich turbulentem Widerstand $\frac{1}{2}c_w\,\rho_{Luft}\,v^2\,\frac{\pi}{4}D^2$:

$$v = \sqrt{\frac{4\,\rho_{Eis}\,g\,D}{3\,c_w\,\rho_{Luft}}}$$

Für $D = 2$ cm, $c_w = 0{,}6$, $\rho_{Luft} = 0{,}9$ (in 3 km): 21 m/s. Für 5 cm: 33 m/s. Für 10 cm (Rekordkörner): 47 m/s. Die Wachstumsrate durch Bereifung ist $\frac{dm}{dt} = E\,\frac{\pi}{4}D^2\,v\,w_l$ mit $w_l$ dem Flüssigwassergehalt (2-5 g/m³ in einer Superzelle) und $E \approx 0{,}8$: Ein 2-cm-Korn gewinnt $0{,}8\cdot 3\cdot 10^{-4}\cdot 21\cdot 3\cdot 10^{-3} = 1{,}5\cdot 10^{-5}$ kg/s, also seine eigene Masse (3,8 g) in vier Minuten. Fünf Minuten im Aufwind sind ein Zentimeter Durchmesser.

**Die Böenfront** ist eine Dichteströmung: Kaltluft der Dicke $h$ und Temperaturdefizit $\Delta T$ unter Warmluft läuft mit

$$v \approx k\sqrt{g\,h\,\frac{\Delta T}{T}}$$

($k \approx 0{,}7$ bis 1, Benjamin 1968). Mit $h = 1000$ m, $\Delta T = 8$ K: $\sqrt{9{,}81\cdot 1000\cdot 0{,}027} = 16$ m/s. Das ist die Geschwindigkeit, mit der der Kaltluftkeil der Zelle vorausläuft -- und seine Vorderkante hebt die Warmluft um $h$, oft genug für die nächste Zelle.

**Der Donner.** Lichtlaufzeit vernachlässigbar; Schall mit $c = \sqrt{\gamma R_L T} = \sqrt{1{,}4\cdot 287\cdot 288} = 340$ m/s. Entfernung $d = c\,\Delta t$: 3 Sekunden sind ein Kilometer. Donner ist nach 20 km nicht mehr zu hören, weil der Schall nach oben gebrochen wird (Temperatur fällt, $c$ fällt, Strahlen krümmen sich aufwärts) -- "Wetterleuchten" ist ein Gewitter, dessen Donner nicht ankommt.

**Wo es aufhört zu gelten:** $c_w$ hängt von der Form ab (Hagel ist nicht rund, 0,5-0,8). Die Dichteströmungsformel gilt für eine stationäre Front über flachem Grund. Und das Vertikalprofil des Aufwinds ist nicht konstant: Ein Korn kann im schwächeren Rand des Aufwinds fallen und im Kern wieder aufsteigen -- die Schichten im Hagelkorn.""",
r"""## Derivation: hail, gust front and lightning distance

**Hail.** Weight $\frac{\pi}{6}D^3\rho_{ice}\,g$ equals turbulent drag $\frac{1}{2}c_d\,\rho_{air}\,v^2\,\frac{\pi}{4}D^2$:

$$v = \sqrt{\frac{4\,\rho_{Eis}\,g\,D}{3\,c_w\,\rho_{Luft}}}$$

For $D = 2$ cm, $c_d = 0.6$, $\rho_{air} = 0.9$ (at 3 km): 21 m/s. For 5 cm: 33 m/s. For 10 cm (record stones): 47 m/s. The growth rate by riming is $\frac{dm}{dt} = E\,\frac{\pi}{4}D^2\,v\,w_l$ with $w_l$ the liquid water content (2-5 g/m³ in a supercell) and $E \approx 0.8$: a 2 cm stone gains $0.8\cdot 3\cdot 10^{-4}\cdot 21\cdot 3\cdot 10^{-3} = 1.5\cdot 10^{-5}$ kg/s, i.e. its own mass (3.8 g) in four minutes. Five minutes in the updraught are a centimetre of diameter.

**The gust front** is a density current: cold air of depth $h$ and temperature deficit $\Delta T$ beneath warm air runs at

$$v \approx k\sqrt{g\,h\,\frac{\Delta T}{T}}$$

($k \approx 0.7$ to 1, Benjamin 1968). With $h = 1000$ m, $\Delta T = 8$ K: $\sqrt{9.81\cdot 1000\cdot 0.027} = 16$ m/s. That is the speed at which the cold wedge runs ahead of the cell -- and its leading edge lifts the warm air by $h$, often enough for the next cell.

**Thunder.** Light travel time negligible; sound at $c = \sqrt{\gamma R_L T} = \sqrt{1.4\cdot 287\cdot 288} = 340$ m/s. Distance $d = c\,\Delta t$: 3 seconds are one kilometre. Thunder is inaudible beyond 20 km because the sound is refracted upward (temperature falls, $c$ falls, rays curve upward) -- "heat lightning" is a thunderstorm whose thunder does not arrive.

**Where it stops holding:** $c_d$ depends on shape (hail is not round, 0.5-0.8). The density-current formula holds for a steady front over flat ground. And the vertical profile of the updraught is not constant: a stone can fall in the weaker edge of the updraught and rise again in the core -- the layers in the hailstone."""),

# ---------------------------------------------------------------------------
"op-streuung": t(r"""## Herleitung: Rayleigh und Koschmieder

**Rayleigh.** Ein Molekül im Feld $E = E_0 e^{-i\omega t}$ bekommt das Dipolmoment $p = \alpha E$ (Polarisierbarkeit $\alpha$, von $\omega$ unabhängig, solange $\omega$ weit unter den Resonanzen im UV liegt). Ein schwingender Dipol strahlt die Leistung $P = \frac{\omega^4|p|^2}{12\pi\varepsilon_0 c^3}$ (Larmor). Der Streuquerschnitt ist $P$ durch die einfallende Intensität $\frac{1}{2}\varepsilon_0 c E_0^2$:

$$\sigma_R = \frac{\omega^4\alpha^2}{6\pi\varepsilon_0^2 c^4} = \frac{8\pi^3}{3}\,\frac{(n^2-1)^2}{N^2\lambda^4}$$

mit der Lorentz-Lorenz-Beziehung $\alpha = \varepsilon_0(n^2-1)/N$ für die Zahldichte $N$. Für Luft ($n - 1 = 2{,}9\cdot 10^{-4}$, $N = 2{,}5\cdot 10^{25}$ /m³) bei 550 nm: $\sigma_R = 4{,}5\cdot 10^{-31}$ m², und die optische Dicke der ganzen Atmosphäre $\tau = \sigma_R N H = 0{,}1$ -- 10 % des grünen Lichts werden bei senkrechtem Stand gestreut, 40 % des Blauen bei 400 nm, bei 10° Sonnenhöhe (Weg sechsmal länger) ist das Blau praktisch weg.

Das Verhältnis zweier Wellenlängen ist $(\lambda_1/\lambda_2)^4$: $(650/450)^4 = 4{,}4$. Die Streuung geht in Vorwärts- und Rückwärtsrichtung gleich stark und seitlich halb so stark ($1 + \cos^2\vartheta$-Verteilung) -- und seitlich ist das Licht vollständig polarisiert, was Bienen zur Navigation nutzen und ein Polfilter zum Abdunkeln des Himmels.

**Mie.** Für $r \geq \lambda$ wird der Streuquerschnitt $\approx 2\pi r^2$ (das Doppelte der geometrischen Fläche -- Beugung kommt dazu), unabhängig von $\lambda$: weiß. Die Vorwärtsstreuung dominiert (Hofeffekt, Glanz um die Sonne).

**Koschmieder.** Ein schwarzes Objekt in der Entfernung $x$ hat den Kontrast $C(x) = C_0\,e^{-\beta x}$ gegen den Horizont, weil auf dem Weg Streulicht in die Sichtlinie gestreut wird (und die Horizontleuchtdichte selbst konstant ist). Mit der Schwelle $C = 0{,}02$:

$$V = \frac{\ln(1/0{,}02)}{\beta} = \frac{3{,}91}{\beta}$$

$\beta$ ist die Summe aus Rayleigh (10⁻⁵ /m), Aerosol und Tröpfchen ($\beta = 2\pi r^2 N$: bei $r = 5$ μm und $N = 10^8$ /m³ -- Nebel -- $\beta = 1{,}6\cdot 10^{-2}$, $V = 250$ m).

**Wo es aufhört zu gelten:** Rayleigh gilt für $r < \lambda/10$; die Formel vernachlässigt Mehrfachstreuung, die bei $\tau > 1$ zählt. Koschmieder setzt gleichmäßige Beleuchtung und ein schwarzes Ziel voraus; nachts und bei Lichtern gilt Allard mit einer Schwellenbeleuchtungsstärke.""",
r"""## Derivation: Rayleigh and Koschmieder

**Rayleigh.** A molecule in the field $E = E_0 e^{-i\omega t}$ acquires the dipole moment $p = \alpha E$ (polarisability $\alpha$, independent of $\omega$ as long as $\omega$ is far below the resonances in the UV). An oscillating dipole radiates the power $P = \frac{\omega^4|p|^2}{12\pi\varepsilon_0 c^3}$ (Larmor). The scattering cross-section is $P$ divided by the incident intensity $\frac{1}{2}\varepsilon_0 c E_0^2$:

$$\sigma_R = \frac{\omega^4\alpha^2}{6\pi\varepsilon_0^2 c^4} = \frac{8\pi^3}{3}\,\frac{(n^2-1)^2}{N^2\lambda^4}$$

with the Lorentz–Lorenz relation $\alpha = \varepsilon_0(n^2-1)/N$ for number density $N$. For air ($n - 1 = 2.9\cdot 10^{-4}$, $N = 2.5\cdot 10^{25}$ /m³) at 550 nm: $\sigma_R = 4.5\cdot 10^{-31}$ m², and the optical depth of the whole atmosphere $\tau = \sigma_R N H = 0.1$ -- 10 % of green light is scattered at the zenith, 40 % of blue at 400 nm; at 10° solar elevation (path six times longer) the blue is practically gone.

The ratio of two wavelengths is $(\lambda_1/\lambda_2)^4$: $(650/450)^4 = 4.4$. Scattering is equally strong forward and backward and half as strong sideways ($1 + \cos^2\vartheta$ distribution) -- and sideways the light is fully polarised, which bees use for navigation and a polarising filter to darken the sky.

**Mie.** For $r \geq \lambda$ the scattering cross-section becomes $\approx 2\pi r^2$ (twice the geometric area -- diffraction adds to it), independent of $\lambda$: white. Forward scattering dominates (the glare around the sun).

**Koschmieder.** A black object at distance $x$ has contrast $C(x) = C_0\,e^{-\beta x}$ against the horizon, because along the path scattered light enters the line of sight (while the horizon luminance itself is constant). With the threshold $C = 0.02$:

$$V = \frac{\ln(1/0.02)}{\beta} = \frac{3.91}{\beta}$$

$\beta$ is the sum of Rayleigh (10⁻⁵ /m), aerosol and droplets ($\beta = 2\pi r^2 N$: at $r = 5$ μm and $N = 10^8$ /m³ -- fog -- $\beta = 1.6\cdot 10^{-2}$, $V = 250$ m).

**Where it stops holding:** Rayleigh holds for $r < \lambda/10$; the formula neglects multiple scattering, which matters for $\tau > 1$. Koschmieder assumes uniform illumination and a black target; at night and for lights Allard's law with a threshold illuminance applies."""),

# ---------------------------------------------------------------------------
"op-regenbogen": t(r"""## Herleitung: Descartes und das Prisma

**Der Strahlengang im Tropfen.** Einfall unter $i$ gegen die Normale, Brechung auf $r$ mit $\sin i = n\sin r$: Ablenkung $i - r$. Innen trifft der Strahl die Rückwand wieder unter $r$ (gleichschenkliges Dreieck) und wird reflektiert: Ablenkung $\pi - 2r$. Austritt wieder unter $r \to i$: Ablenkung $i - r$. Summe:

$$\delta(i) = 2(i - r) + (\pi - 2r) = \pi + 2i - 4r$$

**Das Minimum.** $\frac{d\delta}{di} = 2 - 4\frac{dr}{di} = 0$, also $\frac{dr}{di} = \frac{1}{2}$. Aus $\sin i = n\sin r$ folgt $\cos i\,di = n\cos r\,dr$, also $\frac{dr}{di} = \frac{\cos i}{n\cos r}$. Gleichsetzen: $n\cos r = 2\cos i$. Quadrieren und $\cos^2 r = 1 - \sin^2 i/n^2$ einsetzen: $n^2 - \sin^2 i = 4\cos^2 i$, also $n^2 - 1 + \cos^2 i = 4\cos^2 i$:

$$\cos i_{min} = \sqrt{\frac{n^2 - 1}{3}}$$

Für $n = 1{,}333$: $\cos i = 0{,}5075$, $i = 59{,}5^\circ$, $\sin r = 0{,}8616/1{,}333 = 0{,}6464$, $r = 40{,}3^\circ$, $\delta = 180 + 119{,}0 - 161{,}2 = 137{,}8^\circ$. Der Beobachter sieht den Strahl aus der Richtung $180^\circ - \delta = 42{,}2^\circ$ vom Sonnengegenpunkt.

**Warum das Minimum hell ist:** Die Strahlen treffen den Tropfen gleichmäßig über den Querschnitt, also gleichmäßig in $\sin i$. Die Intensität je Winkel $\delta$ ist proportional zu $|d(\sin i)/d\delta|$, und bei $d\delta/di = 0$ wird das unendlich -- eine Kaustik. Real begrenzt durch Beugung: Bei kleinen Tropfen (Nebel, $r < 50$ μm) verschmiert sie den Bogen zum weißen Nebelbogen.

**Dispersion.** $n_{rot} = 1{,}331$: 42,4°. $n_{blau} = 1{,}343$: 40,6°. Rot außen, 1,8° breit. **Nebenbogen** mit zwei inneren Reflexionen: $\delta = 2\pi + 2i - 6r$, Minimum bei $\cos i = \sqrt{(n^2-1)/8}$, $i = 71{,}9^\circ$, $\delta = 230{,}4^\circ$, Bogen bei $\delta - 180^\circ = 50{,}4^\circ$ -- umgekehrte Farbfolge, weil $\delta$ jetzt mit $n$ wächst statt fällt.

**Das Prisma.** Symmetrischer Durchgang durch ein Prisma mit Winkel $A$: Innen $r_1 = r_2 = A/2$, außen $i_1 = i_2 = \arcsin(n\sin(A/2))$, Ablenkung $\delta = i_1 + i_2 - A$. Dass der symmetrische Gang das Minimum ist, folgt aus derselben Rechnung wie oben (oder aus der Umkehrbarkeit des Lichtwegs: Wäre das Minimum unsymmetrisch, gäbe es ein zweites bei umgekehrtem Gang). Mit $A = 60^\circ$, $n_{Eis} = 1{,}31$: $\delta = 2\arcsin(0{,}655) - 60^\circ = 81{,}8 - 60 = 21{,}8^\circ$. Für $A = 90^\circ$ (Säulenende gegen Seitenfläche): $2\arcsin(0{,}926) - 90 = 46^\circ$.

**Wo es aufhört zu gelten:** Geometrische Optik; für Tropfen unter 100 μm braucht es Mie oder Airy (Überzählige Bögen, Nebelbogen). Die Fresnel-Reflexion ist nicht enthalten -- sie macht den Hauptbogen 4 % hell und den Nebenbogen ein Zehntel davon.""",
r"""## Derivation: Descartes and the prism

**The ray path in the drop.** Incidence at $i$ to the normal, refraction to $r$ with $\sin i = n\sin r$: deviation $i - r$. Inside, the ray meets the back wall again at $r$ (isosceles triangle) and is reflected: deviation $\pi - 2r$. Exit again at $r \to i$: deviation $i - r$. Sum:

$$\delta(i) = 2(i - r) + (\pi - 2r) = \pi + 2i - 4r$$

**The minimum.** $\frac{d\delta}{di} = 2 - 4\frac{dr}{di} = 0$, so $\frac{dr}{di} = \frac{1}{2}$. From $\sin i = n\sin r$ follows $\cos i\,di = n\cos r\,dr$, so $\frac{dr}{di} = \frac{\cos i}{n\cos r}$. Equate: $n\cos r = 2\cos i$. Square and insert $\cos^2 r = 1 - \sin^2 i/n^2$: $n^2 - \sin^2 i = 4\cos^2 i$, so $n^2 - 1 + \cos^2 i = 4\cos^2 i$:

$$\cos i_{min} = \sqrt{\frac{n^2 - 1}{3}}$$

For $n = 1.333$: $\cos i = 0.5075$, $i = 59.5^\circ$, $\sin r = 0.8616/1.333 = 0.6464$, $r = 40.3^\circ$, $\delta = 180 + 119.0 - 161.2 = 137.8^\circ$. The observer sees the ray from the direction $180^\circ - \delta = 42.2^\circ$ from the antisolar point.

**Why the minimum is bright:** rays hit the drop uniformly over its cross-section, i.e. uniformly in $\sin i$. The intensity per angle $\delta$ is proportional to $|d(\sin i)/d\delta|$, and at $d\delta/di = 0$ that becomes infinite -- a caustic. In reality limited by diffraction: for small drops (fog, $r < 50$ μm) it smears the bow into the white fogbow.

**Dispersion.** $n_{red} = 1.331$: 42.4°. $n_{blue} = 1.343$: 40.6°. Red outside, 1.8° wide. **Secondary bow** with two internal reflections: $\delta = 2\pi + 2i - 6r$, minimum at $\cos i = \sqrt{(n^2-1)/8}$, $i = 71.9^\circ$, $\delta = 230.4^\circ$, bow at $\delta - 180^\circ = 50.4^\circ$ -- reversed colour order, because $\delta$ now grows with $n$ instead of falling.

**The prism.** Symmetric passage through a prism of angle $A$: inside $r_1 = r_2 = A/2$, outside $i_1 = i_2 = \arcsin(n\sin(A/2))$, deviation $\delta = i_1 + i_2 - A$. That the symmetric passage is the minimum follows from the same calculation as above (or from the reversibility of the light path: if the minimum were asymmetric, there would be a second one for the reversed path). With $A = 60^\circ$, $n_{ice} = 1.31$: $\delta = 2\arcsin(0.655) - 60^\circ = 81.8 - 60 = 21.8^\circ$. For $A = 90^\circ$ (column end against side face): $2\arcsin(0.926) - 90 = 46^\circ$.

**Where it stops holding:** geometrical optics; for drops below 100 μm one needs Mie or Airy (supernumerary bows, fogbow). Fresnel reflection is not included -- it makes the primary bow 4 % bright and the secondary a tenth of that."""),

# ---------------------------------------------------------------------------
"vo-numerik": t(r"""## Herleitung: die CFL-Bedingung

Die einfachste Transportgleichung, $\partial\phi/\partial t + c\,\partial\phi/\partial x = 0$, hat die exakte Lösung $\phi(x - ct)$: Das Profil wandert mit $c$. Diskretisiert mit Vorwärtsschritt in der Zeit und Rückwärtsdifferenz im Raum (Upwind):

$$\phi_j^{n+1} = \phi_j^n - \frac{c\,\Delta t}{\Delta x}\left(\phi_j^n - \phi_{j-1}^n\right) = (1 - \nu)\,\phi_j^n + \nu\,\phi_{j-1}^n, \qquad \nu = \frac{c\,\Delta t}{\Delta x}$$

Für $0 \leq \nu \leq 1$ ist der neue Wert ein gewichtetes Mittel der alten -- beschränkt, stabil. Für $\nu > 1$ sind die Gewichte negativ und größer als eins: Jede Störung wächst je Schritt um den Faktor $|1 - \nu| + \nu > 1$, exponentiell. Von-Neumann-Analyse mit $\phi_j^n = \xi^n e^{ikj\Delta x}$: $\xi = 1 - \nu(1 - e^{-ik\Delta x})$, und $|\xi| \leq 1$ für alle $k$ genau dann, wenn $\nu \leq 1$. Das ist Courant, Friedrichs und Lewy (1928):

$$\Delta t \leq \frac{\Delta x}{c}$$

Anschaulich: Der numerische Abhängigkeitsbereich (eine Zelle je Schritt) muss den physikalischen (die Strecke $c\,\Delta t$) enthalten, sonst fehlt dem Schema die Information, die die Lösung braucht.

**Welches $c$ zählt:** das schnellste Signal im System. In den vollständigen Gleichungen ist das der Schall (340 m/s), in den hydrostatischen Gleichungen die externe Schwerewelle ($\sqrt{gH} = 300$ m/s bei $H = 10$ km), in beiden Fällen weit über dem Wind. Deshalb behandelt man diese Wellen **implizit** (das Schema löst ein Gleichungssystem, das den Wellen erlaubt, mehrere Zellen je Schritt zu laufen, ohne instabil zu werden) und bleibt für die Advektion bei $\Delta t < \Delta x/U$, mit $U = 100$ m/s im Jet: 100 s bei 10 km. **Semi-Lagrange** verfolgt die Trajektorie rückwärts zum Startpunkt und interpoliert dort -- unbedingt stabil, Zeitschritte von 15-30 Minuten bei 10 km.

**Wo es aufhört zu gelten:** CFL ist notwendig, nicht hinreichend -- das zentrale Schema in Raum und Zeit ist trotz $\nu < 1$ instabil, das Leapfrog-Schema hat eine Rechenmode. Und Stabilität heißt nicht Genauigkeit: Upwind mit $\nu = 0{,}5$ verschmiert jede Front in wenigen Schritten (numerische Diffusion $\frac{1}{2}c\Delta x(1-\nu)$).""",
r"""## Derivation: the CFL condition

The simplest transport equation, $\partial\phi/\partial t + c\,\partial\phi/\partial x = 0$, has the exact solution $\phi(x - ct)$: the profile travels at $c$. Discretised with a forward step in time and a backward difference in space (upwind):

$$\phi_j^{n+1} = \phi_j^n - \frac{c\,\Delta t}{\Delta x}\left(\phi_j^n - \phi_{j-1}^n\right) = (1 - \nu)\,\phi_j^n + \nu\,\phi_{j-1}^n, \qquad \nu = \frac{c\,\Delta t}{\Delta x}$$

For $0 \leq \nu \leq 1$ the new value is a weighted mean of the old -- bounded, stable. For $\nu > 1$ the weights are negative and larger than one: every disturbance grows per step by the factor $|1 - \nu| + \nu > 1$, exponentially. Von Neumann analysis with $\phi_j^n = \xi^n e^{ikj\Delta x}$: $\xi = 1 - \nu(1 - e^{-ik\Delta x})$, and $|\xi| \leq 1$ for all $k$ exactly when $\nu \leq 1$. That is Courant, Friedrichs and Lewy (1928):

$$\Delta t \leq \frac{\Delta x}{c}$$

Intuitively: the numerical domain of dependence (one cell per step) must contain the physical one (the distance $c\,\Delta t$), or the scheme lacks the information the solution needs.

**Which $c$ counts:** the fastest signal in the system. In the full equations that is sound (340 m/s), in the hydrostatic equations the external gravity wave ($\sqrt{gH} = 300$ m/s at $H = 10$ km), in both cases far above the wind. Hence these waves are treated **implicitly** (the scheme solves a system of equations that lets the waves travel several cells per step without going unstable) and advection stays at $\Delta t < \Delta x/U$, with $U = 100$ m/s in the jet: 100 s at 10 km. **Semi-Lagrangian** schemes trace the trajectory backward to its origin and interpolate there -- unconditionally stable, time steps of 15-30 minutes at 10 km.

**Where it stops holding:** CFL is necessary, not sufficient -- the scheme centred in space and time is unstable despite $\nu < 1$, the leapfrog scheme has a computational mode. And stability is not accuracy: upwind with $\nu = 0.5$ smears every front within a few steps (numerical diffusion $\frac{1}{2}c\Delta x(1-\nu)$)."""),

# ---------------------------------------------------------------------------
"vo-chaos": t(r"""## Herleitung: Lorenz und die Fehlerverdopplung

**Das Lorenz-System** (1963) ist eine auf drei Moden gestutzte Rayleigh-Bénard-Konvektion:

$$\dot x = \sigma(y - x), \qquad \dot y = x(\rho - z) - y, \qquad \dot z = xy - \beta z$$

mit $\sigma = 10$, $\beta = 8/3$, $\rho = 28$. $x$ ist die Stärke der Konvektionswalze, $y$ der Temperaturunterschied zwischen auf- und absteigender Luft, $z$ die Abweichung des Profils vom linearen. Die Lösung ist beschränkt (die Divergenz des Flusses ist $-(\sigma + 1 + \beta) < 0$, Volumen schrumpft) und doch nicht periodisch: Sie springt unregelmäßig zwischen zwei Flügeln.

**Lyapunov-Exponent.** Zwei Trajektorien im Abstand $\delta_0$ entfernen sich im Mittel wie $\delta(t) = \delta_0\,e^{\lambda t}$. Für das Lorenz-System ist $\lambda = 0{,}906$ je Zeiteinheit, Verdopplung in $\ln 2/\lambda = 0{,}77$. Nach 20 Zeiteinheiten ist ein Fehler von $10^{-6}$ auf 1 gewachsen -- genau das, was Lorenz mit seinen abgerundeten Anfangswerten erlebte.

**In der Atmosphäre** misst man $\lambda$ aus Zwillingsexperimenten (zwei Modellläufe mit minimal verschiedenen Anfangswerten): Verdopplung in 1,5-2,5 Tagen auf der synoptischen Skala, in 10 Stunden auf der Skala von Gewittern, in Minuten in der Turbulenz. Der Fehler wandert dabei von klein nach groß: Lorenz' zweite Arbeit (1969) zeigt, dass für ein Spektrum mit $k^{-5/3}$ (Turbulenz) die Vorhersagbarkeitsgrenze **endlich bleibt, selbst wenn der Anfangsfehler gegen null geht** -- weil die Verdopplungszeit mit der Skala kleiner wird und die Summe $\sum t_n$ konvergiert. Das ist der harte Kern der zwei Wochen.

**Zahlen.** $t_2 = 2$ Tage, Anfangsfehler 10 % der Klimavarianz: Nach $\log_2 10 \cdot 2 = 6{,}6$ Tagen ist der Fehler so groß wie die Varianz selbst -- die Vorhersage ist nicht besser als die Klimatologie. Zehnmal bessere Beobachtungen (1 %): 13 Tage. Hundertmal: 20 Tage. Der Gewinn je Dekade Verbesserung schrumpft, und die Skalenkaskade setzt bei etwa zwei Wochen den Deckel.

**Das Ensemble** macht aus der Verteilung der Anfangsfehler eine Verteilung der Vorhersagen. Die Streuung der Mitglieder nach $t$ Tagen sollte gleich dem mittleren Fehler nach $t$ Tagen sein -- ist sie kleiner, ist das Ensemble „überkonfident", und die Störungen werden nachgeschärft (stochastische Physik). Die Zuverlässigkeit prüft man am Reliabilitätsdiagramm: Von allen Fällen mit „70 %" sollten 70 % eintreten.

**Wo es aufhört zu gelten:** Der Lyapunov-Exponent ist ein Mittelwert; an manchen Tagen (Blocking) wächst der Fehler kaum, an anderen (Zyklogenese) in Stunden. Die Vorhersagbarkeit ist selbst vorhersagbar -- das ist der zweite Nutzen des Ensembles.""",
r"""## Derivation: Lorenz and error doubling

**The Lorenz system** (1963) is Rayleigh–Bénard convection truncated to three modes:

$$\dot x = \sigma(y - x), \qquad \dot y = x(\rho - z) - y, \qquad \dot z = xy - \beta z$$

with $\sigma = 10$, $\beta = 8/3$, $\rho = 28$. $x$ is the strength of the convection roll, $y$ the temperature difference between rising and sinking air, $z$ the deviation of the profile from linear. The solution is bounded (the divergence of the flow is $-(\sigma + 1 + \beta) < 0$, volume shrinks) and yet not periodic: it jumps irregularly between two wings.

**Lyapunov exponent.** Two trajectories a distance $\delta_0$ apart separate on average as $\delta(t) = \delta_0\,e^{\lambda t}$. For the Lorenz system $\lambda = 0.906$ per time unit, doubling in $\ln 2/\lambda = 0.77$. After 20 time units an error of $10^{-6}$ has grown to 1 -- exactly what Lorenz experienced with his rounded initial values.

**In the atmosphere** $\lambda$ is measured from twin experiments (two model runs with minimally different initial values): doubling in 1.5-2.5 days on the synoptic scale, in 10 hours on the scale of thunderstorms, in minutes in turbulence. The error migrates from small to large: Lorenz's second paper (1969) shows that for a spectrum with $k^{-5/3}$ (turbulence) the predictability limit **stays finite even as the initial error goes to zero** -- because the doubling time shrinks with scale and the sum $\sum t_n$ converges. That is the hard core of the two weeks.

**Numbers.** $t_2 = 2$ days, initial error 10 % of the climate variance: after $\log_2 10 \cdot 2 = 6.6$ days the error is as large as the variance itself -- the forecast is no better than climatology. Ten times better observations (1 %): 13 days. A hundred times: 20 days. The gain per decade of improvement shrinks, and the scale cascade puts the lid on at about two weeks.

**The ensemble** turns the distribution of initial errors into a distribution of forecasts. The spread of the members after $t$ days should equal the mean error after $t$ days -- if it is smaller, the ensemble is "overconfident", and the perturbations are sharpened (stochastic physics). Reliability is checked on the reliability diagram: of all cases with "70 %", 70 % should occur.

**Where it stops holding:** the Lyapunov exponent is an average; on some days (blocking) the error hardly grows, on others (cyclogenesis) within hours. Predictability is itself predictable -- that is the second use of the ensemble."""),
}
