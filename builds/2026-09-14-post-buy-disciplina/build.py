#!/usr/bin/env python3
"""Buy post 4:5 — COMENTÁ DISCIPLINA (visual Motivación vs Disciplina)."""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stlabs_kit import package, render  # noqa: E402

BUILD = Path(__file__).resolve().parent
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
        ("Barlow Condensed", FONTS / "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("Barlow Condensed", FONTS / "BarlowCondensed-Regular.ttf", 400, "normal"),
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


WAVE = "M40,110 C70,40 100,180 130,110 C160,40 190,180 220,110 C250,40 280,160 310,90"
STAIRS = (
    "M40,200 L80,200 L80,160 L120,160 L120,120 L160,120 L160,90 "
    "L200,90 L200,60 L240,60 L240,35 L280,35 L280,20 L320,20"
)

CSS = f"""
:root{{
  --verde:{VERDE}; --ink:{INK}; --paper:{PAPER};
  --pop:'Poppins',Helvetica,sans-serif;
  --serif:'Lora',Georgia,serif;
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
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:10;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}}
.wrap{{
  position:absolute;inset:0;padding:90px 70px 150px;
  display:flex;flex-direction:column;align-items:center;
}}
.charts{{
  display:flex;gap:40px;width:100%;justify-content:center;margin-bottom:48px;
}}
.col{{flex:1;max-width:400px;text-align:center;}}
.col svg{{width:100%;height:200px;}}
.lab{{
  font-family:var(--pop);font-weight:700;font-size:28px;color:var(--verde);margin-top:12px;
}}
.kicker{{
  font-family:var(--sans);font-weight:500;font-size:34px;letter-spacing:4px;
  text-transform:uppercase;color:var(--ink);margin-top:8px;
}}
.kw{{
  font-family:var(--serif);font-style:italic;font-weight:700;
  font-size:100px;line-height:0.95;letter-spacing:-2px;color:var(--verde);
  margin-top:18px;
}}
.sub{{
  margin-top:36px;font-family:var(--sans);font-weight:400;font-size:36px;line-height:1.3;
  color:var(--ink);text-align:center;max-width:820px;
}}
"""


def build_html() -> Path:
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{font_faces()}{CSS}</style></head>
<body><div class="sheet">
<section class="slide">
  <div class="wrap">
    <div class="charts">
      <div class="col">
        <svg viewBox="0 0 360 240" fill="none">
          <path d="M30 20 V220 H340" stroke="{VERDE}" stroke-width="3"/>
          <path d="{WAVE}" stroke="{VERDE}" stroke-width="10" stroke-linecap="round" fill="none"/>
        </svg>
        <div class="lab">Motivación</div>
      </div>
      <div class="col">
        <svg viewBox="0 0 360 240" fill="none">
          <path d="M30 20 V220 H340" stroke="{VERDE}" stroke-width="3"/>
          <path d="{STAIRS}" stroke="{VERDE}" stroke-width="10" stroke-linecap="square" fill="none"/>
        </svg>
        <div class="lab">Disciplina</div>
      </div>
    </div>
    <div class="kicker">Comentá</div>
    <div class="kw">DISCIPLINA.</div>
    <div class="sub">Te paso la rutina mínima de 7 días<br>para avanzar aunque no tengas ganas.</div>
  </div>
  <div class="web">{HANDLE}</div>
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
        "titulo": "Buy Post DISCIPLINA",
        "fondo": "blanco",
        "familia_visual": "cta_buy_charts",
        "origen": "original",
        "slides": 1,
        "keyword_portada": "DISCIPLINA",
        "id": "2026-09-14-post-buy-disciplina",
        "fecha": "2026-09-14",
    }
    out = package(BUILD, "STLabs-Buy-DISCIPLINA", meta=meta)
    print(f"Package → {out}")
    (BUILD / "CAPTION.txt").write_text(
        """La motivación sube y baja.
La disciplina construye aunque no tengas ganas.

Si querés la rutina mínima de 7 días
para arrancar igual…

Comentá DISCIPLINA.

#disciplina #hábitos #sistemas #revops
""",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Buy DISCIPLINA

| Familia | Peso/estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Lora | 700 Italic (variable) | Keyword DISCIPLINA | `/workspace/fonts/Lora-Italic-Variable.ttf` | `@font-face` base64 en `build.py` |
| Poppins | 700 Bold | Labels Motivación / Disciplina | `/workspace/fonts/Poppins-Bold.ttf` | `@font-face` base64 |
| Barlow Condensed | 500 Medium | Kicker COMENTÁ | `/workspace/fonts/BarlowCondensed-Medium.ttf` | `@font-face` base64 |
| Barlow Condensed | 400 Regular | Subtítulo CTA | `/workspace/fonts/BarlowCondensed-Regular.ttf` | `@font-face` base64 |
| IBM Plex Mono | 400 Regular | Footer sebastian.stlabs.ar | `/workspace/fonts/IBMPlexMono-Regular.ttf` | `@font-face` base64 |
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
