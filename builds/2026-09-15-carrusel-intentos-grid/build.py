#!/usr/bin/env python3
"""Carrusel 2 slides — Intentos / Va a SALIR + CTA.
Clon refs @crece30x → STLabs. Fondo blanco + retícula + líneas verdes + manchas sutiles.
"""
from __future__ import annotations

import base64
import math
import random
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
        ("Barlow Condensed", FONTS / "BarlowCondensed-Regular.ttf", 400, "normal"),
        ("Barlow Condensed", FONTS / "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Regular.ttf", 400, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Medium.ttf", 500, "normal"),
    ]
    out = []
    for fam, path, w, style in faces:
        if not path.exists():
            raise FileNotFoundError(path)
        d = b64(path)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{d}) format('truetype');}}"
        )
    return "".join(out)


def data_uri(path: Path, mime: str = "image/png") -> str:
    return f"data:{mime};base64,{b64(path)}"


def stains_svg() -> str:
    """Manchas verdes muy sutiles."""
    rng = random.Random(42)
    blobs = []
    for _ in range(14):
        x = rng.uniform(40, 1040)
        y = rng.uniform(60, 1280)
        rx = rng.uniform(60, 160)
        ry = rng.uniform(40, 120)
        a = rng.uniform(0.03, 0.07)
        blobs.append(
            f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" '
            f'fill="{VERDE}" fill-opacity="{a:.3f}"/>'
        )
    return f'<svg class="stains" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{"".join(blobs)}</svg>'


def arcs_svg() -> str:
    """Líneas verdes curvas sutiles (esquinas)."""
    return f"""<svg class="arcs" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
      <path d="M 70 160 A 130 130 0 0 1 340 160" fill="none" stroke="{VERDE}" stroke-width="2" stroke-opacity=".38"/>
      <path d="M 70 160 A 210 210 0 0 1 500 160" fill="none" stroke="{VERDE}" stroke-width="1.6" stroke-opacity=".28"/>
      <path d="M 70 160 A 300 300 0 0 1 680 160" fill="none" stroke="{VERDE}" stroke-width="1.3" stroke-opacity=".2"/>
      <path d="M 1010 1180 A 110 110 0 0 0 780 1180" fill="none" stroke="{VERDE}" stroke-width="1.8" stroke-opacity=".32"/>
      <path d="M 1010 1180 A 190 190 0 0 0 620 1180" fill="none" stroke="{VERDE}" stroke-width="1.4" stroke-opacity=".22"/>
    </svg>"""


def globe_dots() -> str:
    """Globo punteado sutil (CTA)."""
    dots = []
    cx, cy, rx, ry = 720, 280, 420, 380
    for yi in range(-18, 14):
        for xi in range(-16, 18):
            x = cx + xi * 22
            y = cy + yi * 20
            nx = (x - cx) / rx
            ny = (y - cy) / ry
            if nx * nx + ny * ny > 1:
                continue
            if nx > 0.55 and ny < -0.2:
                continue
            if nx < -0.75:
                continue
            land = -0.55 < nx < 0.35 and -0.7 < ny < 0.85
            if not land and (xi + yi) % 2:
                continue
            r = 3.0 if land else 2.0
            fill = VERDE if (xi, yi) in {(2, -2), (-1, 1), (4, 3), (-3, -4), (1, 6)} else "#D8DCD9"
            op = ".55" if fill == VERDE else ".45"
            dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{fill}" fill-opacity="{op}"/>')
    return "\n".join(dots)


CSS = f"""
:root{{
  --verde:{VERDE}; --ink:{INK}; --paper:{PAPER};
  --pop:'Poppins',Helvetica,sans-serif;
  --sans:'Barlow Condensed',Helvetica,sans-serif;
  --mono:'IBM Plex Mono',monospace;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}}
.slide{{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--ink);
}}
/* Retícula cuadricular sutil */
.slide::before{{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.5;
  background-image:
    linear-gradient(rgba(0,255,178,.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.07) 1px, transparent 1px);
  background-size:40px 40px;
}}
.stains,.arcs,.globe{{position:absolute;inset:0;z-index:1;pointer-events:none;width:100%;height:100%;}}
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:10;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}}
.s1{{
  position:relative;z-index:2;height:100%;
  display:flex;align-items:center;justify-content:center;
  padding:90px 48px 140px;
}}
.s1 img{{width:100%;height:auto;display:block;}}
.s2{{position:relative;z-index:2;height:100%;}}
.s2 .copy{{position:absolute;left:64px;top:230px;width:620px;z-index:3;}}
.s2 h1{{
  font-family:var(--pop);font-weight:700;font-size:62px;line-height:1.08;
  color:var(--verde);letter-spacing:-1.1px;margin-bottom:32px;
}}
.s2 .sub{{
  font-family:var(--sans);font-weight:400;font-size:34px;line-height:1.35;
  color:var(--ink);max-width:540px;
}}
.s2 .handle{{
  display:block;margin-top:18px;font-family:var(--mono);font-weight:500;
  font-size:28px;color:var(--verde);letter-spacing:.5px;
}}
.s2 .ill{{
  position:absolute;right:72px;bottom:160px;width:300px;z-index:4;
  border:3px solid var(--ink);background:#fff;
}}
.s2 .ill img{{width:100%;height:auto;display:block;}}
"""


def slide(inner: str) -> str:
    return (
        f'<section class="slide">{stains_svg()}{arcs_svg()}'
        f"{inner}"
        f'<div class="web">{HANDLE}</div></section>'
    )


def s01() -> str:
    src = data_uri(ASSETS / "comic-green.png")
    return slide(f"""
<div class="s1">
  <img src="{src}" alt="Uno de todos esos intentos va a salir"/>
</div>
""")


def s02() -> str:
    ill = data_uri(ASSETS / "cta-ill-green.png")
    return slide(f"""
<svg class="globe" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{globe_dots()}</svg>
<div class="s2">
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
        "fondo": "blanco_reticula_lineas_manchas",
        "familia_visual": "comic_cta_editorial",
        "origen": "screenshot",
        "keyword_portada": "INTENTOS",
        "id": "2026-09-15-carrusel-intentos-grid",
        "fecha": "2026-09-15",
    }
    package(BUILD, "STLabs-Intentos-Grid", meta=meta)
    (BUILD / "CAPTION.txt").write_text(
        """Uno de todos esos intentos va a salir.

No es magia: es insistir hasta que aparece el que sirve.

Si estás construyendo, seguí.

sebastian.stlabs.ar

#RevOps #sistemas #disciplina #stlabs
""",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Intentos Grid

| Familia | Peso/estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Poppins | 700 Bold | Título CTA | `/workspace/fonts/Poppins-Bold.ttf` | `@font-face` base64 |
| Barlow Condensed | 400 Regular | Subtítulo CTA | `/workspace/fonts/BarlowCondensed-Regular.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400/500 | Footer + handle | `/workspace/fonts/IBMPlexMono-*.ttf` | `@font-face` base64 |

**Nota:** textos del cómic (slide 1) vienen en la ilustración (`assets/comic-green.png`), recoloreados a verde marca.
""",
        encoding="utf-8",
    )
    print("DONE")


if __name__ == "__main__":
    main()
