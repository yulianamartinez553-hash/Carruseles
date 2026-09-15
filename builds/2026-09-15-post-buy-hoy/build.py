#!/usr/bin/env python3
"""Post motivacional 4:5 — hook + chart, fondo gym blur claro."""
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
        ("Lora", FONTS / "Lora-Italic-Variable.ttf", "400 700", "italic"),
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


def gym_bg_uri() -> str:
    path = ASSETS / "gym-blur-light.jpg"
    if not path.exists():
        raise FileNotFoundError(path)
    return f"data:image/jpeg;base64,{b64(path)}"


BARS = [
    (80, 220, 40),
    (160, 180, 80),
    (240, 140, 120),
    (320, 95, 165),
    (400, 55, 205),
    (480, 30, 230),
]


def bars_svg() -> str:
    parts = [
        f'<path d="M40 20 V260 H560" stroke="{VERDE}" stroke-width="3" fill="none"/>'
    ]
    for x, top, h in BARS:
        parts.append(
            f'<rect x="{x}" y="{top}" width="48" height="{h}" fill="{VERDE}"/>'
        )
    return "\n".join(parts)


CSS = f"""
:root{{
  --verde:{VERDE}; --ink:{INK}; --paper:{PAPER};
  --pop:'Poppins',Helvetica,sans-serif;
  --serif:'Lora',Georgia,serif;
  --mono:'IBM Plex Mono',monospace;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}}
.slide{{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--ink);
}}
.bg{{
  position:absolute;inset:0;z-index:0;width:100%;height:100%;
  object-fit:cover;object-position:center;display:block;
}}
/* Degradé a blanco puro — sin gris abajo; gym apenas en el centro */
.veil{{
  position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    linear-gradient(180deg,
      rgba(255,255,255,.55) 0%,
      rgba(255,255,255,.25) 28%,
      rgba(255,255,255,.35) 55%,
      rgba(255,255,255,.85) 82%,
      #ffffff 100%);
}}
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:10;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}}
.wrap{{
  position:relative;z-index:2;height:100%;
  padding:120px 80px 160px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;
}}
.hook{{
  font-family:var(--pop);font-weight:700;font-size:48px;line-height:1.15;
  color:var(--ink);max-width:900px;margin-bottom:48px;
}}
.hook em{{
  font-family:var(--serif);font-style:italic;font-weight:700;color:var(--verde);
  font-size:1.05em;
}}
.chart{{width:680px;height:300px;margin:8px 0 0;}}
"""


def build_html() -> Path:
    bg = gym_bg_uri()
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{font_faces()}{CSS}</style></head>
<body><div class="sheet">
<section class="slide">
  <img class="bg" src="{bg}" alt=""/>
  <div class="veil"></div>
  <div class="wrap">
    <div class="hook">No esperes a tener ganas.<br>Las ganas llegan <em>después</em> de empezar.</div>
    <svg class="chart" viewBox="0 0 600 280" fill="none">{bars_svg()}</svg>
  </div>
  <div class="web">{HANDLE}</div>
</section>
</div></body></html>"""
    path = BUILD / "carrusel.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML → {path}")
    return path


def main() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    build_html()
    print("Render…")
    pngs = render(BUILD)
    print(f"PNGs: {len(pngs)}")
    meta = {
        "titulo": "Post ganas / después de empezar",
        "fondo": "gym_blur_claro",
        "familia_visual": "dossier_editorial",
        "origen": "original",
        "slides": 1,
        "keyword_portada": "DESPUÉS",
        "id": "2026-09-15-post-buy-hoy",
        "fecha": "2026-09-15",
    }
    out = package(BUILD, "STLabs-Buy-HOY", meta=meta)
    print(f"Package → {out}")
    (BUILD / "CAPTION.txt").write_text(
        """No esperes a tener ganas.
Las ganas llegan después de empezar.

#hábitos #disciplina #acción #revops
""",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Post ganas

| Familia | Peso/estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Poppins | 700 Bold | Hook motivacional | `/workspace/fonts/Poppins-Bold.ttf` | `@font-face` base64 en `build.py` |
| Lora | 700 Italic (variable) | Acento “después” | `/workspace/fonts/Lora-Italic-Variable.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400 Regular | Footer sebastian.stlabs.ar | `/workspace/fonts/IBMPlexMono-Regular.ttf` | `@font-face` base64 |

**Fondo:** gym realista en blur + lavado blanco (`assets/gym-blur-light.jpg`) con velo blanco en CSS.
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
