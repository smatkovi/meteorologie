#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Das Startbild: Wolke und Sonne in der Squircle-Form der Harmattan-Apps.

Die Silhouette kommt wie bei allen MeeGo-Apps aus meego-icon-tool/squircle.py
(Alphakanal eines Stock-Icons), das Zeichen selbst wird hier gezeichnet: eine
Haufenwolke vor einer Sonne. Das liest sich auf 80 Pixeln noch als "Wetter",
ein Buchstabe nicht.

    tools/icon.py            # -> icons/icon-80.png, icons/icon-64.png
"""
import math
import os
import sys

from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.dirname(HIER)
sys.path.insert(0, os.path.join(os.path.dirname(WURZEL), "meego-icon-tool"))
import squircle  # noqa: E402

S = squircle.SIZE


def wolke_sonne():
    sonne = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(sonne)
    cx, cy, r = S * 0.62, S * 0.40, S * 0.15
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 214, 92, 255))
    for i in range(8):
        a = i * math.pi / 4
        x1, y1 = cx + math.cos(a) * r * 1.3, cy + math.sin(a) * r * 1.3
        x2, y2 = cx + math.cos(a) * r * 1.75, cy + math.sin(a) * r * 1.75
        d.line([(x1, y1), (x2, y2)], fill=(255, 214, 92, 255), width=int(S * 0.035))

    wolke = Image.new("L", (S, S), 0)
    w = ImageDraw.Draw(wolke)
    grund = S * 0.72
    for (x, y, r) in ((0.30, 0.60, 0.13), (0.44, 0.52, 0.17), (0.60, 0.58, 0.14),
                      (0.70, 0.64, 0.10)):
        w.ellipse([S * x - S * r, S * y - S * r, S * x + S * r, S * y + S * r],
                  fill=255)
    w.rectangle([S * 0.18, S * 0.62, S * 0.80, grund], fill=255)
    # Die flache Basis: unten glatt abgeschnitten, wie eine echte Basis.
    w.rectangle([0, grund, S, S], fill=0)
    # Ecken der Basis abrunden
    w.ellipse([S * 0.18 - S * 0.06, grund - S * 0.12, S * 0.18 + S * 0.06, grund], fill=255)
    w.ellipse([S * 0.80 - S * 0.06, grund - S * 0.12, S * 0.80 + S * 0.06, grund], fill=255)
    w.rectangle([0, grund, S, S], fill=0)
    weiss = Image.new("RGBA", (S, S), (250, 251, 255, 255))
    weiss.putalpha(wolke)
    return Image.alpha_composite(sonne, weiss)


def main():
    icon = squircle.gloss(squircle.gradient("#5aa9ff", "#1d4fa8")).convert("RGBA")
    icon = Image.alpha_composite(icon, wolke_sonne())
    maske = squircle.squircle()
    icon.putalpha(Image.composite(icon.split()[3], Image.new("L", (S, S), 0), maske))
    stock = Image.open(squircle.MASK).convert("RGBA").split()[3]
    ziel = os.path.join(WURZEL, "icons")
    os.makedirs(ziel, exist_ok=True)
    for groesse in (80, 64):
        klein = icon.resize((groesse, groesse), Image.LANCZOS)
        klein.putalpha(stock if groesse == stock.size[0]
                       else stock.resize((groesse, groesse), Image.LANCZOS))
        klein.save(os.path.join(ziel, "icon-%d.png" % groesse))
        print("icons/icon-%d.png" % groesse)


if __name__ == "__main__":
    main()
