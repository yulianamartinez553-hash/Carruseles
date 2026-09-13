#!/usr/bin/env python3
"""Buy post feed 4:5 — COMENTÁ CRITERIO (mismo look del carrusel Prospectar)."""
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
FONTS = ROOT / "fonts"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_faces() -> str:
    faces = [
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-BoldItalic.ttf", 700, "italic"),
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-Italic.ttf", 400, "italic"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Regular.ttf", 400, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Regular.ttf", 400, "normal"),
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


def stipple() -> str:
    rng = random.Random(7)
    circles = []
    cx, cy, R = 860, 200, 220
    for _ in range(2800):
        ang = rng.random() * math.tau
        rad = R * (rng.random() ** 0.55)
        x = cx + rad * math.cos(ang)
        y = cy + rad * math.sin(ang)
        dens = 1 - rad / R
        if dens < 0.06:
            continue
        a = 0.04 + dens * 0.18
        s = 1.15 if dens > 0.45 else 0.85
        circles.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s}" fill="#00FFB2" fill-opacity="{a:.2f}"/>'
        )
    return (
        f'<svg class="stipple" viewBox="0 0 1080 1350" width="1080" height="1350">'
        f'{"".join(circles)}</svg>'
    )


CSS = r"""
:root{
  --verde:#00FFB2;
  --ink:#0A5C45;
  --paper:#FAFAF7;
  --serif:'Playfair Display',Georgia,serif;
  --sans:'IBM Plex Sans',Helvetica,sans-serif;
  --mono:'IBM Plex Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}
body{background:#111;}
.sheet{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}
.slide{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--ink);
}
.slide::before{
  content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.55;
  background-image:
    radial-gradient(circle at 20% 30%, rgba(0,0,0,.035) 0.6px, transparent 1.2px),
    radial-gradient(circle at 70% 60%, rgba(0,0,0,.03) 0.5px, transparent 1.1px);
  background-size:3px 3px, 4px 4px;
}
.slide::after{
  content:'';position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.5;mix-blend-mode:multiply;
  background:repeating-linear-gradient(90deg,
    rgba(0,0,0,.06) 0px, rgba(0,0,0,.06) 1.5px,
    transparent 3px, transparent 8px,
    rgba(0,40,30,.09) 10px, rgba(0,40,30,.09) 12px,
    transparent 14px);
}
.stains,.arcs,.stipple,.content,.web{position:absolute;z-index:3;}
.stains{inset:0;z-index:2;pointer-events:none;}
.stain{
  position:absolute;border-radius:50%;
  background:radial-gradient(circle, rgba(210,255,240,.12) 0%, rgba(160,255,220,.06) 45%, transparent 76%);
  filter:blur(4px);
}
.arcs{inset:0;z-index:2;pointer-events:none;}
.arcs svg,.stipple{width:100%;height:100%;}
.content{inset:0;z-index:5;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 70px;}
.kicker{
  font-family:var(--sans);font-weight:500;font-size:28px;letter-spacing:4px;
  color:var(--ink);text-transform:uppercase;margin-bottom:28px;
}
.kw{
  font-family:var(--serif);font-style:italic;font-weight:700;
  font-size:110px;line-height:0.95;letter-spacing:-2px;color:var(--verde);
  text-shadow:0 2px 0 rgba(0,0,0,.15);
}
.sub{
  margin-top:44px;font-family:var(--sans);font-size:30px;line-height:1.35;color:var(--ink);
  max-width:820px;
}
.web{
  left:0;right:0;bottom:70px;text-align:center;z-index:6;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}
"""


def build_html() -> Path:
    arcs = """
    <div class="arcs"><svg viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">
      <path d="M 100 180 A 140 140 0 0 1 380 180" fill="none" stroke="#00FFB2" stroke-width="2.2" stroke-opacity=".5"/>
      <path d="M 100 180 A 220 220 0 0 1 540 180" fill="none" stroke="#00FFB2" stroke-width="2" stroke-opacity=".4"/>
      <path d="M 100 180 A 320 320 0 0 1 740 180" fill="none" stroke="#00FFB2" stroke-width="1.6" stroke-opacity=".32"/>
      <path d="M 900 1120 A 120 120 0 0 0 660 1120" fill="none" stroke="#00FFB2" stroke-width="2" stroke-opacity=".4"/>
      <path d="M 900 1120 A 200 200 0 0 0 500 1120" fill="none" stroke="#00FFB2" stroke-width="1.6" stroke-opacity=".3"/>
    </svg></div>
    """
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{font_faces()}{CSS}</style></head>
<body><div class="sheet">
<section class="slide">
  {arcs}
  <div class="content">
    <div class="kicker">Comentá</div>
    <div class="kw">CRITERIO.</div>
    <div class="sub">Te paso el filtro de las tres preguntas<br>para dejar de confundir movimiento<br>con prospección real.</div>
  </div>
  <div class="web">sebastian.stlabs.ar</div>
</section>
</div></body></html>"""
    path = BUILD / "carrusel.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML → {path}")
    return path


def main() -> None:
    build_html()
    print("Render…")
    pngs = render(BUILD)
    print(f"PNGs: {len(pngs)}")
    meta = {
        "titulo": "Buy Post CRITERIO",
        "slides": 1,
        "fondo": "papel_arroz_manchas_verdes_buy",
        "familia_visual": "cta_editorial_didot",
        "origen": "original",
        "keyword_portada": "CRITERIO",
        "id": "2026-09-13-post-buy-criterio",
    }
    out = package(BUILD, "STLabs-Buy-CRITERIO", meta=meta)
    print(f"Package → {out}")
    (BUILD / "CAPTION.txt").write_text(
        """Prospectar y perder el tiempo se ven igual desde afuera.

Si querés el filtro de las tres preguntas
para saber con quién vale la pena hablar…

Comentá CRITERIO.

#prospección #ventas #pipeline #revops
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
