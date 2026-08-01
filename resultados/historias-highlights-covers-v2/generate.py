# -*- coding: utf-8 -*-
"""Portadas Highlight en formato Historia 9:16.
Tema independiente · sin líneas de esquina · puntos amplios con degradé · título impactante.
"""
from pathlib import Path
import math
import json

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

# Textos NUEVOS e impactantes (distintos a la tanda anterior)
COVERS = [
    {
        "id": "resultados",
        "highlight": "RESULTADOS",
        "kicker": "DESTACADA",
        "claim": "Menos tarjeta digital.\nMás máquina de ventas.",
        "apoyo": "Entrá y mirá casos reales de antes y después.",
        "glyph": "resultados",
        "accent": "tr",
        "dots": "bl",
    },
    {
        "id": "proceso",
        "highlight": "PROCESO",
        "kicker": "DESTACADA",
        "claim": "Cero humo.\nCinco pasos claros.",
        "apoyo": "Deslizá y conocé cómo trabajo de punta a punta.",
        "glyph": "proceso",
        "accent": "tl",
        "dots": "br",
    },
    {
        "id": "clientes",
        "highlight": "CLIENTES",
        "kicker": "DESTACADA",
        "claim": "Lo que escriben\ncuando funciona.",
        "apoyo": "Entrá a ver testimonios, plazos y permisos reales.",
        "glyph": "clientes",
        "accent": "br",
        "dots": "tl",
    },
    {
        "id": "servicios",
        "highlight": "SERVICIOS",
        "kicker": "DESTACADA",
        "claim": "Elegí qué comprar.\nSin dar vueltas.",
        "apoyo": "Landing, sitio, rediseño, mantenimiento o SEO.",
        "glyph": "servicios",
        "accent": "bl",
        "dots": "tr",
    },
    {
        "id": "contacto",
        "highlight": "CONTACTO",
        "kicker": "DESTACADA",
        "claim": "Dejá de pensarlo.\nEmpezá a medir.",
        "apoyo": "Entrá, comentá WEB o agendá 20 minutos.",
        "glyph": "contacto",
        "accent": "br",
        "dots": "tl",
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


def dots_gradient(corner: str, seed: int = 1, w: int = 1080, h: int = 1920) -> str:
    """Puntos amplios con degradé progresivo — sin líneas de esquina."""
    origins = {
        "tl": (0, 0),
        "tr": (w, 0),
        "bl": (0, h),
        "br": (w, h),
    }
    ox, oy = origins[corner]
    # radio máximo más amplio en formato historia
    max_r = 720
    rings = [
        (28, 9, 17, 0.98),
        (70, 13, 14, 0.88),
        (120, 17, 12, 0.74),
        (180, 21, 10, 0.58),
        (250, 26, 8, 0.44),
        (330, 30, 7, 0.32),
        (420, 34, 5.5, 0.22),
        (520, 36, 4.5, 0.14),
        (620, 32, 3.5, 0.08),
        (700, 26, 2.8, 0.045),
    ]
    html = ['<div class="dots">']

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

    n = 0
    for r_base, count, size_max, op_max in rings:
        for i in range(count):
            t = i / max(count - 1, 1)
            a = t * (math.pi / 2) * 0.95 + 0.03 + (seed % 7) * 0.008
            jitter = (((n * 41 + seed * 19) % 31) - 15) * 1.5
            r = max(10, r_base + jitter)
            dist_factor = max(0.0, 1.0 - r / max_r)
            size = size_max * (0.35 + 0.65 * dist_factor)
            op = op_max * (0.3 + 0.7 * dist_factor)
            x, y = xy(a, r)
            place(x, y, size, op)
            n += 1

    # relleno disperso más amplio
    for i in range(70):
        t = ((i * 17 + seed * 3) % 100) / 100
        a = t * (math.pi / 2) * 0.96 + 0.02
        r = 100 + ((i * 53 + seed * 11) % 600)
        dist_factor = max(0.0, 1.0 - r / (max_r + 40))
        size = 2.2 + 7.5 * dist_factor
        op = 0.025 + 0.32 * dist_factor
        x, y = xy(a, r)
        place(x, y, size, op)

    html.append("</div>")
    return "".join(html)


def nl(text: str) -> str:
    return "<br>".join(text.split("\n"))


def slide(c: dict, idx: int) -> str:
    return f'''
    <div class="slide accent-{c['accent']}" data-id="{c['id']}">
      <div class="bg">
        <div class="cross-lines"></div>
        <div class="grid"></div>
        <div class="wash"></div>
        <div class="stain"></div>
      </div>
      {dots_gradient(c["dots"], seed=idx + 5)}
      <div class="safe">
        {glyph_svg(c['glyph'])}
        <h1 class="claim">{nl(c['claim'])}</h1>
        <div class="rule"></div>
        <p class="apoyo">{c['apoyo']}</p>
      </div>
      <div class="firma">sebastian.stlabs.ar</div>
    </div>'''


CSS = f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype'); }}
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }}

* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1920px; overflow:hidden;
  background:#0A0A0A;
}}
.bg {{ position:absolute; inset:0; }}
.cross-lines {{
  position:absolute; inset:-30%;
  opacity:.55;
  background:
    repeating-linear-gradient(
      35deg,
      transparent 0 46px,
      rgba(0,255,178,.055) 46px 47px
    ),
    repeating-linear-gradient(
      -35deg,
      transparent 0 52px,
      rgba(0,255,178,.04) 52px 53px
    );
  pointer-events:none;
  mix-blend-mode:screen;
}}
.grid {{
  position:absolute; inset:0; opacity:.22;
  background-image:
    linear-gradient(rgba(0,255,178,.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.035) 1px, transparent 1px);
  background-size:64px 64px;
}}
.wash {{
  position:absolute; inset:0;
  background: linear-gradient(180deg, rgba(10,10,10,.15) 0%, rgba(10,10,10,.45) 55%, rgba(0,0,0,.7) 100%);
}}

.accent-tl .stain {{ left:-220px; top:-200px; }}
.accent-tr .stain {{ right:-220px; top:-200px; left:auto; }}
.accent-bl .stain {{ left:-220px; bottom:-180px; top:auto; }}
.accent-br .stain {{ right:-220px; bottom:-180px; left:auto; top:auto; }}
.stain {{
  position:absolute; width:780px; height:780px; border-radius:50%;
  background: radial-gradient(circle, rgba(0,255,178,.40) 0%, rgba(0,255,178,.13) 42%, transparent 72%);
  filter: blur(8px); pointer-events:none;
}}

/* SIN líneas de esquina */
.dots {{ position:absolute; inset:0; z-index:4; pointer-events:none; }}
.dots span {{
  position:absolute; border-radius:50%; background:#00FFB2;
  box-shadow:0 0 8px rgba(0,255,178,.22);
}}

.safe {{
  position:absolute; left:88px; right:88px; top:260px; bottom:360px;
  display:flex; flex-direction:column; justify-content:center; align-items:flex-start;
  z-index:6; text-align:left;
}}
.glyph {{
  width:160px; height:160px; margin-bottom:32px;
  filter: drop-shadow(0 0 16px rgba(0,255,178,.28));
}}
.claim {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:100px; line-height:.94;
  letter-spacing:.01em; color:#F2F2F2; max-width:900px;
}}
.rule {{
  width:120px; height:5px; background:#00FFB2; border-radius:2px;
  margin:28px 0 22px; box-shadow:0 0 14px rgba(0,255,178,.4);
}}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:34px;
  line-height:1.3; color:#9aa39c; max-width:820px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:7;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.12em; color:#00FFB2; opacity:.9;
}}
"""


def main():
    slides = "".join(slide(c, i + 1) for i, c in enumerate(COVERS))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Portadas Highlight Stories</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    (OUT / "covers.html").write_text(html, encoding="utf-8")
    (OUT / "index.json").write_text(json.dumps(COVERS, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(COVERS)} story-format highlight covers")


if __name__ == "__main__":
    main()
