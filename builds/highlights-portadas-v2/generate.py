# -*- coding: utf-8 -*-
"""Portadas Highlight Instagram — 5 temas independientes.
Sin líneas en esquinas. Puntos amplios con degradé progresivo.
Canvas 1080×1080 (recorte circular de Highlight).
"""
from pathlib import Path
import math
import json

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

COVERS = [
    {
        "id": "resultados",
        "label": "RESULTADOS",
        "kicker": "PORTFOLIO",
        "glyph": "resultados",
        "accent": "tl",
        "dots": "br",
    },
    {
        "id": "proceso",
        "label": "PROCESO",
        "kicker": "CÓMO TRABAJO",
        "glyph": "proceso",
        "accent": "tr",
        "dots": "bl",
    },
    {
        "id": "clientes",
        "label": "CLIENTES",
        "kicker": "PRUEBA SOCIAL",
        "glyph": "clientes",
        "accent": "bl",
        "dots": "tr",
    },
    {
        "id": "servicios",
        "label": "SERVICIOS",
        "kicker": "OFERTAS",
        "glyph": "servicios",
        "accent": "br",
        "dots": "tl",
    },
    {
        "id": "contacto",
        "label": "CONTACTO",
        "kicker": "EMPEZÁ",
        "glyph": "contacto",
        "accent": "tl",
        "dots": "br",
    },
]


def glyph_svg(kind: str) -> str:
    g = {
        "resultados": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <rect x="28" y="110" width="36" height="54" rx="6" fill="none" stroke="#00FFB2" stroke-width="6"/>
          <rect x="82" y="78" width="36" height="86" rx="6" fill="none" stroke="#00FFB2" stroke-width="6" opacity=".5"/>
          <rect x="136" y="42" width="36" height="122" rx="6" fill="#00FFB2"/>
          <path d="M34 150 L96 96 L152 58" fill="none" stroke="#00FFB2" stroke-width="7" stroke-linecap="round"/>
          <circle cx="152" cy="58" r="10" fill="#00FFB2"/>
        </svg>""",
        "proceso": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <circle cx="40" cy="100" r="18" fill="none" stroke="#00FFB2" stroke-width="6"/>
          <circle cx="100" cy="100" r="18" fill="#00FFB2"/>
          <circle cx="160" cy="100" r="18" fill="none" stroke="#00FFB2" stroke-width="6"/>
          <path d="M60 100 H80 M120 100 H140" stroke="#00FFB2" stroke-width="6" stroke-linecap="round"/>
          <path d="M148 90 L162 100 L148 110" fill="none" stroke="#00FFB2" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="100" y="106" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="18" font-weight="700" fill="#04130b">02</text>
        </svg>""",
        "clientes": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <path d="M48 78 C48 52 72 42 100 42 C128 42 152 52 152 78 C152 108 118 122 100 148 C82 122 48 108 48 78 Z"
                fill="none" stroke="#00FFB2" stroke-width="7"/>
          <path d="M72 86 H128 M84 108 H116" stroke="#00FFB2" stroke-width="7" stroke-linecap="round" opacity=".85"/>
          <circle cx="156" cy="150" r="22" fill="#00FFB2"/>
          <path d="M148 150 L154 156 L166 142" fill="none" stroke="#04130b" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>""",
        "servicios": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <rect x="36" y="44" width="128" height="36" rx="10" fill="none" stroke="#00FFB2" stroke-width="6"/>
          <rect x="36" y="92" width="128" height="36" rx="10" fill="#00FFB2"/>
          <rect x="36" y="140" width="128" height="36" rx="10" fill="none" stroke="#00FFB2" stroke-width="6" opacity=".5"/>
          <circle cx="56" cy="62" r="5" fill="#00FFB2"/>
          <circle cx="56" cy="110" r="5" fill="#04130b"/>
          <circle cx="56" cy="158" r="5" fill="#00FFB2" opacity=".5"/>
        </svg>""",
        "contacto": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <path d="M40 52 H160 A16 16 0 0 1 176 68 V128 A16 16 0 0 1 160 144 H96 L64 172 V144 H40 A16 16 0 0 1 24 128 V68 A16 16 0 0 1 40 52 Z"
                fill="none" stroke="#00FFB2" stroke-width="7" stroke-linejoin="round"/>
          <circle cx="76" cy="100" r="8" fill="#00FFB2"/>
          <circle cx="100" cy="100" r="8" fill="#00FFB2" opacity=".7"/>
          <circle cx="124" cy="100" r="8" fill="#00FFB2" opacity=".4"/>
        </svg>""",
    }
    return g[kind]


def dots_gradient(corner: str, seed: int = 1) -> str:
    """Puntos amplios con degradé: cerca más opacos/grandes; afuera más chicos y transparentes."""
    origins = {
        "tl": (0, 0),
        "tr": (1080, 0),
        "bl": (0, 1080),
        "br": (1080, 1080),
    }
    ox, oy = origins[corner]
    # abanico amplio (~560px) con degradé suave de opacidad y tamaño
    rings = [
        # radio, count, size, opacity
        (24, 8, 16, 0.98),
        (60, 12, 13, 0.88),
        (105, 16, 11, 0.72),
        (155, 20, 9, 0.56),
        (215, 24, 7, 0.42),
        (280, 28, 6, 0.30),
        (350, 32, 5, 0.20),
        (430, 34, 4, 0.12),
        (510, 30, 3, 0.07),
        (580, 22, 2.5, 0.04),
    ]
    html = ['<div class="dots">']
    n = 0

    def place(x, y, size, op):
        html.append(
            f'<span style="left:{x - size/2:.1f}px;top:{y - size/2:.1f}px;'
            f'width:{size:.1f}px;height:{size:.1f}px;opacity:{op:.3f};"></span>'
        )

    def xy(a, r):
        if corner == "tl":
            return ox + math.cos(a) * r, oy + math.sin(a) * r
        if corner == "tr":
            return ox - math.sin(a) * r, oy + math.cos(a) * r
        if corner == "bl":
            return ox + math.sin(a) * r, oy - math.cos(a) * r
        return ox - math.cos(a) * r, oy - math.sin(a) * r

    for r_base, count, size_max, op_max in rings:
        for i in range(count):
            t = i / max(count - 1, 1)
            a = t * (math.pi / 2) * 0.95 + 0.025 + (seed % 7) * 0.008
            jitter = (((n * 41 + seed * 19) % 29) - 14) * 1.35
            r = max(8, r_base + jitter)
            # degradé extra por distancia real
            dist_factor = max(0.0, 1.0 - r / 620)
            size = size_max * (0.4 + 0.6 * dist_factor)
            op = op_max * (0.35 + 0.65 * dist_factor)
            x, y = xy(a, r)
            place(x, y, size, op)
            n += 1
    # relleno disperso adicional (más amplio, más suave)
    for i in range(55):
        t = ((i * 17 + seed * 3) % 100) / 100
        a = t * (math.pi / 2) * 0.96 + 0.02
        r = 90 + ((i * 53 + seed * 11) % 480)
        dist_factor = max(0.0, 1.0 - r / 640)
        size = 2.5 + 6 * dist_factor
        op = 0.03 + 0.35 * dist_factor
        x, y = xy(a, r)
        place(x, y, size, op)
    html.append("</div>")
    return "".join(html)


def slide(c: dict, idx: int) -> str:
    return f'''
    <div class="slide accent-{c['accent']}" data-id="{c['id']}">
      <div class="bg">
        <div class="grid"></div>
        <div class="wash"></div>
        <div class="stain"></div>
      </div>
      {dots_gradient(c["dots"], seed=idx + 3)}
      <div class="safe">
        <div class="kicker">{c['kicker']}</div>
        {glyph_svg(c['glyph'])}
        <div class="label">{c['label']}</div>
        <div class="rule"></div>
        <div class="firma">sebastian.stlabs.ar</div>
      </div>
    </div>'''


CSS = f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype'); }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}

* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:40px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1080px; overflow:hidden;
  background:#0A0A0A;
}}
.bg {{ position:absolute; inset:0; }}
.grid {{
  position:absolute; inset:0; opacity:.35;
  background-image:
    linear-gradient(rgba(0,255,178,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.04) 1px, transparent 1px);
  background-size:56px 56px;
  mask-image: radial-gradient(circle at 50% 48%, #000 0%, #000 42%, transparent 74%);
}}
.wash {{
  position:absolute; inset:0;
  background: radial-gradient(circle at 50% 48%, rgba(10,10,10,.15) 0%, rgba(0,0,0,.55) 78%);
}}

.accent-tl .stain {{ left:-200px; top:-180px; }}
.accent-tr .stain {{ right:-200px; top:-180px; left:auto; }}
.accent-bl .stain {{ left:-200px; bottom:-160px; top:auto; }}
.accent-br .stain {{ right:-200px; bottom:-160px; left:auto; top:auto; }}
.stain {{
  position:absolute; width:680px; height:680px; border-radius:50%;
  background: radial-gradient(circle, rgba(0,255,178,.42) 0%, rgba(0,255,178,.14) 40%, transparent 72%);
  filter: blur(6px); pointer-events:none;
}}

/* SIN líneas de esquina — solo puntos con degradé */
.dots {{ position:absolute; inset:0; z-index:4; pointer-events:none; }}
.dots span {{
  position:absolute; border-radius:50%; background:#00FFB2;
  box-shadow:0 0 8px rgba(0,255,178,.25);
}}

.safe {{
  position:absolute; left:50%; top:50%; width:640px;
  transform:translate(-50%,-50%);
  display:flex; flex-direction:column; align-items:center; text-align:center; z-index:5;
}}
.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:22px;
  letter-spacing:.2em; color:#00FFB2; margin-bottom:26px;
}}
.glyph {{
  width:200px; height:200px; margin-bottom:20px;
  filter: drop-shadow(0 0 16px rgba(0,255,178,.3));
}}
.label {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:88px; line-height:.92;
  letter-spacing:.02em; color:#F2F2F2;
}}
.rule {{
  width:110px; height:5px; background:#00FFB2; margin:20px 0 16px;
  border-radius:2px; box-shadow:0 0 14px rgba(0,255,178,.45);
}}
.firma {{
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:20px;
  letter-spacing:.12em; color:#00FFB2; opacity:.9;
}}
"""


def main():
    slides = "".join(slide(c, i + 1) for i, c in enumerate(COVERS))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Portadas Highlight</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    (OUT / "highlights.html").write_text(html, encoding="utf-8")
    (OUT / "index.json").write_text(
        json.dumps(COVERS, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(COVERS)} highlight covers")


if __name__ == "__main__":
    main()
