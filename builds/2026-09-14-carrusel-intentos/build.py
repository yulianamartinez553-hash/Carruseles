#!/usr/bin/env python3
"""Carrusel 2 slides — cómic Intentos + CTA (refs @crece30x) → STLabs.
Fondo blanco. Verde marca #00FFB2. Cuenta en última imagen.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stlabs_kit import package, render  # noqa: E402

BUILD = Path(__file__).resolve().parent
ASSETS = BUILD / "assets"
FONTS = ROOT / "fonts"

VERDE = "#00FFB2"
INK = "#0A0A0A"
PAPER = "#FFFFFF"
HANDLE = "sebastian.stlabs.ar"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_faces() -> str:
    faces = [
        ("Poppins", FONTS / "Poppins-Bold.ttf", 700, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Regular.ttf", 400, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Regular.ttf", 400, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Medium.ttf", 500, "normal"),
    ]
    out = []
    for fam, path, w, style in faces:
        if not path.exists():
            continue
        d = b64(path)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{d}) format('truetype');}}"
        )
    return "".join(out)


def data_uri(path: Path) -> str:
    return f"data:image/png;base64,{b64(path)}"


CSS = f"""
:root{{
  --verde:{VERDE}; --ink:{INK}; --paper:{PAPER};
  --pop:'Poppins',Helvetica,sans-serif;
  --sans:'IBM Plex Sans',Helvetica,sans-serif;
  --mono:'IBM Plex Mono',monospace;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}}
.slide{{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--ink);
}}
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:10;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}}
"""


def foot() -> str:
    return f'<div class="web">{HANDLE}</div>'


def slide(inner: str) -> str:
    return f'<section class="slide">{inner}{foot()}</section>'


def s01() -> str:
    """Cómic 4 paneles — Uno de / Todos esos / Intentos / Va a SALIR."""
    src = data_uri(ASSETS / "comic-green.png")
    return slide(f"""
<style>
.s1{{position:absolute;inset:0;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:80px 48px 140px;}}
.s1 img{{width:100%;height:auto;display:block;}}
</style>
<div class="s1">
  <img src="{src}" alt="Uno de todos esos intentos va a salir"/>
</div>
""")


def s02() -> str:
    """CTA — Probablemente nunca volverás… + ilustración + cuenta."""
    ill = data_uri(ASSETS / "cta-ill-green.png")
    # Dotted globe (Americas-ish) as SVG halftone
    dots = []
    # Approximate western hemisphere with dots
    cx, cy, rx, ry = 720, 280, 420, 380
    for yi in range(-18, 14):
        for xi in range(-16, 18):
            x = cx + xi * 22
            y = cy + yi * 20
            # ellipse mask + Americas-ish indent
            nx = (x - cx) / rx
            ny = (y - cy) / ry
            if nx * nx + ny * ny > 1:
                continue
            # carve ocean / shape roughly
            if nx > 0.55 and ny < -0.2:
                continue
            if nx < -0.75:
                continue
            # denser on land-ish bands
            land = (nx > -0.55 and nx < 0.35 and ny > -0.7 and ny < 0.85)
            if not land and (xi + yi) % 2:
                continue
            r = 3.2 if land else 2.2
            # city accents
            fill = VERDE if (xi, yi) in {(2, -2), (-1, 1), (4, 3), (-3, -4), (1, 6), (-4, 4)} else "#D0D4D1"
            dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}"/>')
    dots_svg = "\n".join(dots)

    return slide(f"""
<style>
.s2{{position:absolute;inset:0;}}
.s2 .globe{{position:absolute;inset:0;pointer-events:none;opacity:.9;}}
.s2 .copy{{position:absolute;left:64px;top:220px;width:620px;z-index:3;}}
.s2 h1{{
  font-family:var(--pop);font-weight:700;font-size:64px;line-height:1.08;
  color:var(--ink);letter-spacing:-1.2px;margin-bottom:36px;
}}
.s2 .sub{{
  font-family:var(--sans);font-weight:400;font-size:32px;line-height:1.35;
  color:var(--ink);max-width:540px;
}}
.s2 .handle{{
  display:block;margin-top:18px;font-family:var(--mono);font-weight:500;
  font-size:30px;color:var(--verde);letter-spacing:0.5px;
}}
.s2 .ill{{
  position:absolute;right:72px;bottom:160px;width:300px;height:auto;z-index:4;
  border:3px solid var(--ink);background:#fff;
}}
.s2 .ill img{{width:100%;height:auto;display:block;}}
</style>
<div class="s2">
  <svg class="globe" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
    {dots_svg}
  </svg>
  <div class="copy">
    <h1>Probablemente nunca volverás a ver esta cuenta.</h1>
    <p class="sub">Así que seguime para aprender de los mejores.</p>
    <span class="handle">{HANDLE}</span>
  </div>
  <div class="ill"><img src="{ill}" alt=""/></div>
</div>
""")


def main() -> None:
    slides = [s01(), s02()]
    html = (
        f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
        f"<style>{font_faces()}{CSS}</style></head>"
        f'<body><div class="sheet">{"".join(slides)}</div></body></html>'
    )
    (BUILD / "carrusel.html").write_text(html, encoding="utf-8")
    print("HTML OK")
    pngs = render(BUILD)
    print("PNG", len(pngs))
    meta = {
        "titulo": "Uno de todos esos intentos va a salir",
        "slides": 2,
        "fondo": "blanco",
        "familia_visual": "comic_lineart_cta",
        "origen": "screenshot",
        "keyword_portada": "INTENTOS",
        "id": "2026-09-14-carrusel-intentos",
        "refs": ["crece30x comic 4 paneles", "crece30x CTA cuenta"],
    }
    package(BUILD, "STLabs-Intentos-Salir", meta=meta)
    print("DONE")


if __name__ == "__main__":
    main()
