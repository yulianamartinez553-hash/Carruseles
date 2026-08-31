# -*- coding: utf-8 -*-
"""Genera HTML de íconos Highlight Instagram Stories — STLabs."""
from pathlib import Path

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

HIGHLIGHTS = [
    {
        "id": "resultados",
        "label": "RESULTADOS",
        "kicker": "PORTFOLIO",
        "glyph": "resultados",
    },
    {
        "id": "proceso",
        "label": "PROCESO",
        "kicker": "CÓMO TRABAJO",
        "glyph": "proceso",
    },
    {
        "id": "clientes",
        "label": "CLIENTES",
        "kicker": "PRUEBA SOCIAL",
        "glyph": "clientes",
    },
    {
        "id": "servicios",
        "label": "SERVICIOS",
        "kicker": "OFERTAS",
        "glyph": "servicios",
    },
    {
        "id": "contacto",
        "label": "CONTACTO",
        "kicker": "EMPEZÁ",
        "glyph": "contacto",
    },
]


def glyph_svg(kind: str) -> str:
    g = {
        "resultados": """
        <svg class="glyph" viewBox="0 0 200 200" aria-hidden="true">
          <rect x="28" y="110" width="36" height="54" rx="6" fill="none" stroke="#00FFB2" stroke-width="6"/>
          <rect x="82" y="78" width="36" height="86" rx="6" fill="none" stroke="#00FFB2" stroke-width="6" opacity=".55"/>
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
          <rect x="36" y="140" width="128" height="36" rx="10" fill="none" stroke="#00FFB2" stroke-width="6" opacity=".55"/>
          <circle cx="56" cy="62" r="5" fill="#00FFB2"/>
          <circle cx="56" cy="110" r="5" fill="#04130b"/>
          <circle cx="56" cy="158" r="5" fill="#00FFB2" opacity=".55"/>
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


def slide(h: dict) -> str:
    return f"""
    <div class="slide" data-id="{h['id']}">
      <div class="bg">
        <div class="grid"></div>
        <div class="lines"></div>
        <div class="stain s1"></div>
        <div class="stain s2"></div>
        <div class="stain s3"></div>
        <div class="glow"></div>
        <div class="ring"></div>
      </div>
      <div class="safe">
        <div class="kicker">{h['kicker']}</div>
        {glyph_svg(h['glyph'])}
        <div class="label">{h['label']}</div>
        <div class="rule"></div>
        <div class="firma">sebastian.stlabs.ar</div>
      </div>
    </div>
    """


CSS = f"""
@font-face {{
  font-family: 'Bebas Neue';
  src: url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype');
  font-weight: 400;
}}
@font-face {{
  font-family: 'IBM Plex Mono';
  src: url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype');
  font-weight: 600;
}}
@font-face {{
  font-family: 'IBM Plex Mono';
  src: url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype');
  font-weight: 500;
}}
@font-face {{
  font-family: 'Poppins';
  src: url('file://{FONTS}/Poppins-ExtraBold.ttf') format('truetype');
  font-weight: 800;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  background: #000;
  font-family: 'Poppins', sans-serif;
}}
.sheet {{
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding: 40px;
  width: max-content;
}}
.slide {{
  position: relative;
  width: 1080px;
  height: 1080px;
  overflow: hidden;
  background: #0A0A0A;
  isolation: isolate;
}}
.bg {{ position: absolute; inset: 0; }}
.grid {{
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(0,255,178,.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.08) 1px, transparent 1px);
  background-size: 54px 54px;
  mask-image: radial-gradient(circle at 50% 48%, #000 0%, #000 42%, transparent 72%);
}}
.lines {{
  position: absolute; inset: -20%;
  background:
    repeating-linear-gradient(
      -28deg,
      transparent 0 18px,
      rgba(0,255,178,.07) 18px 19.5px
    );
  mix-blend-mode: screen;
  opacity: .9;
}}
.stain {{
  position: absolute;
  border-radius: 50%;
  filter: blur(28px);
  pointer-events: none;
}}
.s1 {{
  width: 420px; height: 420px;
  left: -80px; top: -60px;
  background: radial-gradient(circle, rgba(0,255,178,.28) 0%, rgba(0,255,178,0) 70%);
}}
.s2 {{
  width: 520px; height: 380px;
  right: -120px; bottom: 40px;
  background: radial-gradient(circle, rgba(0,255,178,.22) 0%, rgba(0,255,178,0) 68%);
}}
.s3 {{
  width: 280px; height: 280px;
  left: 55%; top: 58%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle, rgba(0,255,178,.16) 0%, rgba(0,255,178,0) 70%);
}}
.glow {{
  position: absolute; inset: 0;
  background:
    radial-gradient(circle at 50% 42%, rgba(0,255,178,.18) 0%, rgba(0,255,178,.04) 28%, transparent 58%),
    linear-gradient(160deg, rgba(0,255,178,.08) 0%, transparent 40%, rgba(0,20,14,.9) 100%);
}}
.ring {{
  position: absolute;
  left: 50%; top: 50%;
  width: 760px; height: 760px;
  transform: translate(-50%, -50%);
  border-radius: 50%;
  border: 1.5px solid rgba(0,255,178,.22);
  box-shadow:
    inset 0 0 80px rgba(0,255,178,.06),
    0 0 0 1px rgba(0,255,178,.06);
}}
.ring::after {{
  content: '';
  position: absolute;
  inset: 28px;
  border-radius: 50%;
  border: 1px dashed rgba(0,255,178,.18);
}}
.safe {{
  position: absolute;
  left: 50%; top: 50%;
  width: 640px;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  z-index: 5;
}}
.kicker {{
  font-family: 'IBM Plex Mono', monospace;
  font-weight: 600;
  font-size: 22px;
  letter-spacing: .22em;
  color: #00FFB2;
  margin-bottom: 28px;
  text-transform: uppercase;
}}
.glyph {{
  width: 220px;
  height: 220px;
  margin-bottom: 22px;
  filter: drop-shadow(0 0 18px rgba(0,255,178,.35));
}}
.label {{
  font-family: 'Bebas Neue', Impact, sans-serif;
  font-size: 92px;
  line-height: .92;
  letter-spacing: .02em;
  color: #F2F2F2;
  text-shadow: 0 0 40px rgba(0,255,178,.2);
}}
.rule {{
  width: 120px;
  height: 6px;
  background: #00FFB2;
  margin: 22px 0 18px;
  border-radius: 2px;
  box-shadow: 0 0 16px rgba(0,255,178,.55);
}}
.firma {{
  font-family: 'IBM Plex Mono', monospace;
  font-weight: 500;
  font-size: 20px;
  letter-spacing: .12em;
  color: #00FFB2;
  opacity: .9;
}}
"""


def main():
    slides = "".join(slide(h) for h in HIGHLIGHTS)
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Highlights STLabs</title>
<style>{CSS}</style>
</head>
<body>
<div class="sheet">{slides}</div>
</body>
</html>
"""
    path = OUT / "highlights.html"
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
