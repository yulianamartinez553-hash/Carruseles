# -*- coding: utf-8 -*-
"""Carrusel STLabs — 10 reglas para no vivir en piloto automático.
Papel corrugado + blueprint · iconos SVG · manchas verdes puente.
"""
from __future__ import annotations

import json
import math
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package

DATA = json.loads((BUILD / "index.json").read_text(encoding="utf-8"))
CONSEJOS = DATA["consejos"]
CTA = DATA.get("cta", "CLARO")
TOTAL = int(DATA["slides"])
W, H = 1080, 1350
GRID = 45

BRIDGE = [
    {"y": 260, "rx": 320, "ry": 240, "op": 0.36},
    {"y": 1020, "rx": 280, "ry": 280, "op": 0.30},
    {"y": 480, "rx": 340, "ry": 200, "op": 0.34},
    {"y": 1100, "rx": 240, "ry": 240, "op": 0.28},
    {"y": 200, "rx": 300, "ry": 260, "op": 0.32},
    {"y": 780, "rx": 360, "ry": 220, "op": 0.36},
    {"y": 400, "rx": 300, "ry": 300, "op": 0.30},
    {"y": 980, "rx": 260, "ry": 220, "op": 0.28},
    {"y": 320, "rx": 280, "ry": 240, "op": 0.34},
    {"y": 860, "rx": 340, "ry": 260, "op": 0.32},
    {"y": 180, "rx": 300, "ry": 200, "op": 0.30},
    {"y": 700, "rx": 320, "ry": 280, "op": 0.36},
    {"y": 460, "rx": 340, "ry": 220, "op": 0.32},
    {"y": 1120, "rx": 240, "ry": 200, "op": 0.28},
    {"y": 240, "rx": 280, "ry": 260, "op": 0.34},
    {"y": 820, "rx": 300, "ry": 220, "op": 0.30},
    {"y": 520, "rx": 320, "ry": 240, "op": 0.32},
    {"y": 1000, "rx": 280, "ry": 260, "op": 0.34},
    {"y": 220, "rx": 300, "ry": 220, "op": 0.36},
    {"y": 740, "rx": 340, "ry": 240, "op": 0.30},
    {"y": 380, "rx": 280, "ry": 280, "op": 0.28},
    {"y": 920, "rx": 300, "ry": 220, "op": 0.34},
]


ICONS = {
    "clock": """
<svg viewBox="0 0 120 120" class="ico"><circle cx="60" cy="60" r="44" fill="none" stroke="#00FFB2" stroke-width="4"/>
<circle cx="60" cy="60" r="6" fill="#00FFB2"/>
<path d="M60 30 V60 L82 72" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linecap="round"/>
</svg>""",
    "phone": """
<svg viewBox="0 0 120 120" class="ico"><rect x="38" y="16" width="44" height="88" rx="8" fill="none" stroke="#00FFB2" stroke-width="4"/>
<line x1="50" y1="28" x2="70" y2="28" stroke="#00FFB2" stroke-width="3" stroke-linecap="round"/>
<circle cx="60" cy="90" r="4" fill="#00FFB2"/>
<line x1="28" y1="28" x2="92" y2="92" stroke="#00FFB2" stroke-width="5" stroke-linecap="round"/>
</svg>""",
    "check": """
<svg viewBox="0 0 120 120" class="ico"><rect x="22" y="22" width="76" height="76" rx="12" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M38 62 L54 78 L84 42" fill="none" stroke="#00FFB2" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""",
    "moon": """
<svg viewBox="0 0 120 120" class="ico"><path d="M72 22a40 40 0 1 0 26 66 34 34 0 1 1-26-66z" fill="none" stroke="#00FFB2" stroke-width="4"/>
<circle cx="86" cy="38" r="3" fill="#00FFB2"/><circle cx="94" cy="54" r="2" fill="#00FFB2"/>
</svg>""",
    "move": """
<svg viewBox="0 0 120 120" class="ico"><circle cx="60" cy="28" r="12" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M60 44 L60 72 M60 54 L40 48 M60 54 L82 42 M60 72 L42 98 M60 72 L78 98" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linecap="round"/>
</svg>""",
    "chat": """
<svg viewBox="0 0 120 120" class="ico"><rect x="18" y="28" width="56" height="40" rx="10" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M34 68 L34 86 L50 68" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linejoin="round"/>
<rect x="48" y="48" width="54" height="38" rx="10" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M84 86 L84 102 L68 86" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linejoin="round"/>
</svg>""",
    "pen": """
<svg viewBox="0 0 120 120" class="ico"><rect x="30" y="20" width="60" height="80" rx="6" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M44 40 H76 M44 56 H76 M44 72 H64" fill="none" stroke="#00FFB2" stroke-width="3.5" stroke-linecap="round"/>
<path d="M78 86 L96 104 L104 96 L86 78 Z" fill="none" stroke="#00FFB2" stroke-width="3.5"/>
</svg>""",
    "no": """
<svg viewBox="0 0 120 120" class="ico"><circle cx="60" cy="60" r="44" fill="none" stroke="#00FFB2" stroke-width="4"/>
<line x1="34" y1="34" x2="86" y2="86" stroke="#00FFB2" stroke-width="6" stroke-linecap="round"/>
</svg>""",
    "steps": """
<svg viewBox="0 0 120 120" class="ico"><path d="M20 96 H44 V72 H68 V48 H92 V24 H100" fill="none" stroke="#00FFB2" stroke-width="4" stroke-linejoin="round"/>
<circle cx="100" cy="24" r="6" fill="#00FFB2"/>
</svg>""",
    "play": """
<svg viewBox="0 0 120 120" class="ico"><circle cx="60" cy="60" r="44" fill="none" stroke="#00FFB2" stroke-width="4"/>
<path d="M50 40 L84 60 L50 80 Z" fill="#00FFB2"/>
</svg>""",
}


def _ellipse(cx, cy, rx, ry, op, rot=0) -> str:
    t = f' transform="rotate({rot} {cx:.0f} {cy:.0f})"' if rot else ""
    return (
        f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}"'
        f' fill="url(#blobGrad)" opacity="{op:.2f}"{t}/>'
    )


def _interior(idx: int) -> str:
    rng = random.Random(300 + idx * 13)
    presets = [
        (100, 90, 260, 160, 0.28, -20),
        (980, 120, 240, 180, 0.24, 18),
        (80, 1260, 280, 160, 0.26, 10),
        (1000, 1220, 240, 180, 0.22, -22),
        (540, 80, 320, 100, 0.16, 0),
        (70, 560, 180, 220, 0.22, 25),
        (1010, 700, 190, 230, 0.22, -15),
    ]
    start = idx % len(presets)
    parts = []
    for k in range(3):
        cx, cy, rx, ry, op, rot = presets[(start + k) % len(presets)]
        parts.append(
            _ellipse(
                cx + rng.uniform(-25, 25),
                cy + rng.uniform(-20, 20),
                rx * rng.uniform(0.9, 1.1),
                ry * rng.uniform(0.9, 1.1),
                op,
                rot,
            )
        )
    return "".join(parts)


def bg_layer(slide_idx: int) -> str:
    i = slide_idx - 1
    ox = -(i * W) % GRID
    blobs = []
    if i > 0:
        a = (i - 1) * 2
        for b in BRIDGE[a : a + 2]:
            blobs.append(_ellipse(0, b["y"], b["rx"], b["ry"], b["op"]))
    if i < TOTAL - 1:
        a = i * 2
        for b in BRIDGE[a : a + 2]:
            blobs.append(_ellipse(W, b["y"], b["rx"], b["ry"], b["op"]))
    blobs.append(_interior(slide_idx))

    # papel corrugado: líneas verticales sutiles
    corrug = "".join(
        f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="rgba(255,255,255,0.035)" stroke-width="2"/>'
        for x in range(0, W, 14)
    )

    return f"""
<div class="bg-layer" aria-hidden="true">
  <svg class="bg-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <defs>
      <radialGradient id="blobGrad{slide_idx}" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#00FFB2" stop-opacity="1"/>
        <stop offset="50%" stop-color="#00FFB2" stop-opacity="0.4"/>
        <stop offset="100%" stop-color="#00FFB2" stop-opacity="0"/>
      </radialGradient>
      <pattern id="grid{slide_idx}" width="{GRID}" height="{GRID}" patternUnits="userSpaceOnUse" x="{ox}" y="0">
        <path d="M {GRID} 0 L 0 0 0 {GRID}" fill="none" stroke="rgba(0,255,178,0.12)" stroke-width="1"/>
      </pattern>
      <filter id="blur{slide_idx}" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="20"/>
      </filter>
    </defs>
    <rect width="{W}" height="{H}" fill="#0A0A0A"/>
    {corrug}
    <rect width="{W}" height="{H}" fill="url(#grid{slide_idx})"/>
    <g filter="url(#blur{slide_idx})">{''.join(blobs).replace('url(#blobGrad)', f'url(#blobGrad{slide_idx})')}</g>
  </svg>
</div>"""


EXTRA_CSS = """
.slide{background:#0A0A0A !important;}
.slide::before{display:none !important;}
.bg-layer{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
.bg-svg{position:absolute;inset:0;width:100%;height:100%;display:block;}

/* PORTADA — tipografía + iconos, sin chips ni pills */
.s-cover{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 justify-content:center;padding:80px 64px 130px;}
.cover-kicker{font-family:var(--mono);font-size:18px;letter-spacing:.22em;color:var(--verde);
 text-transform:uppercase;margin-bottom:28px;}
.cover-title{font-family:var(--pop);font-weight:900;font-size:74px;line-height:.98;color:var(--blanco);
 max-width:940px;text-transform:uppercase;letter-spacing:-.02em;
 -webkit-text-stroke:0.4px rgba(242,242,242,.35);}
.cover-title .gr{color:var(--verde);-webkit-text-stroke:0.4px rgba(0,255,178,.35);}
.cover-sub{margin-top:28px;font-family:var(--cond);font-size:34px;line-height:1.3;color:var(--gray);max-width:820px;}
.cover-icons{margin-top:56px;display:flex;gap:28px;align-items:center;flex-wrap:wrap;}
.cover-icons .ico{width:72px;height:72px;opacity:.9;}

/* CONSEJO — número + icono + texto; sin cajas ni barras */
.s-tip{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 padding:72px 64px 130px;}
.tip-top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:28px;}
.tip-num{font-family:var(--mono);font-size:22px;letter-spacing:.18em;color:var(--verde);text-transform:uppercase;}
.tip-icon{width:160px;height:160px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.tip-icon .ico{width:140px;height:140px;display:block;}
.ico{width:88px;height:88px;display:block;}
.tip-body{flex:1;display:flex;flex-direction:column;justify-content:center;}
.tip-title{font-family:var(--pop);font-weight:900;font-size:54px;line-height:1.06;color:var(--blanco);
 max-width:920px;margin-bottom:24px;letter-spacing:-.015em;
 -webkit-text-stroke:0.35px rgba(242,242,242,.3);}
.tip-text{font-family:var(--cond);font-size:32px;line-height:1.35;color:var(--gray);max-width:880px;}

/* CIERRE — solo texto, sin botón */
.s-close{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 justify-content:center;align-items:center;padding:80px 64px 130px;text-align:center;}
.close-kicker{font-family:var(--mono);font-size:16px;letter-spacing:.2em;color:var(--verde);
 text-transform:uppercase;margin-bottom:28px;}
.close-title{font-family:var(--pop);font-weight:900;font-size:62px;line-height:1.04;color:var(--blanco);
 max-width:920px;margin-bottom:24px;letter-spacing:-.015em;
 -webkit-text-stroke:0.4px rgba(242,242,242,.3);}
.close-title .gr{color:var(--verde);-webkit-text-stroke:0.4px rgba(0,255,178,.35);}
.close-body{font-family:var(--cond);font-size:30px;line-height:1.35;color:var(--gray);
 max-width:820px;margin-bottom:36px;}
.close-line{font-family:var(--mono);font-size:22px;letter-spacing:.06em;color:var(--verde);}
.close-line span{color:var(--blanco);}
"""


def _wrap(idx: int, inner: str) -> str:
    return chrome(idx, bg_layer(idx) + inner, total=TOTAL, bridges=None, footer=True, counter=False)


def slide_cover() -> str:
    icons = "".join(ICONS.get(c["icon"], ICONS["check"]) for c in CONSEJOS[:5])
    inner = f"""
<div class="s-cover">
  <div class="cover-kicker">10 reglas · vida diaria</div>
  <h1 class="cover-title">10 reglas para no vivir en <span class="gr">piloto automático</span></h1>
  <p class="cover-sub">Consejos simples. Visuales. Para aplicar hoy, no para guardar y olvidar.</p>
  <div class="cover-icons">{icons}</div>
</div>"""
    return _wrap(1, inner)


def slide_tip(c: dict, idx: int) -> str:
    n = int(c["n"])
    icon = ICONS.get(c["icon"], ICONS["check"])
    inner = f"""
<div class="s-tip">
  <div class="tip-top">
    <div class="tip-num">{n:02d} · regla</div>
    <div class="tip-icon">{icon}</div>
  </div>
  <div class="tip-body">
    <h2 class="tip-title">{c['titulo']}</h2>
    <p class="tip-text">{c['texto']}</p>
  </div>
</div>"""
    return _wrap(idx, inner)


def slide_close() -> str:
    inner = f"""
<div class="s-close">
  <div class="close-kicker">Cierre</div>
  <h2 class="close-title">El piloto automático se apaga <span class="gr">con una decisión</span>.</h2>
  <p class="close-body">Elegí una sola regla de estas 10 y aplicála hoy. Mañana, otra. Así se sale del modo zombie.</p>
  <p class="close-line">Comentá <span>{CTA}</span> y te mando las 10</p>
</div>"""
    return _wrap(TOTAL, inner)


def build_slides() -> list[str]:
    slides = [slide_cover()]
    for i, c in enumerate(CONSEJOS, start=2):
        slides.append(slide_tip(c, i))
    slides.append(slide_close())
    return slides


def main():
    slides = build_slides()
    assert len(slides) == TOTAL
    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML →", BUILD / "carrusel.html")
    pngs = render(BUILD)
    print(f"Render OK — {len(pngs)} slides")
    meta = {
        "id": DATA["id"],
        "titulo": DATA["titulo"],
        "slides": DATA["slides"],
        "fondo": DATA["fondo"],
        "familia_visual": DATA["familia_visual"],
        "origen": DATA["origen"],
        "keyword_portada": DATA["keyword_portada"],
    }
    out = package(BUILD, "STLabs-Consejos-Visuales", meta=meta)
    caption = (
        "10 reglas para no vivir en piloto automático.\n\n"
        "Tiempo. Celular. Sueño. Movimiento. Un no a tiempo.\n"
        "Deslizá. Elegí una. Aplicála hoy.\n\n"
        f"Comentá {CTA} y te mando las 10 completas.\n\n"
        "#habitos #enfoque #disciplina #vida #stlabs"
    )
    (out / "caption.txt").write_text(caption, encoding="utf-8")
    (out / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Consejos visuales

| Familia | Peso | Rol | Origen |
|---|---|---|---|
| Poppins | 800 | Títulos / reglas | `/workspace/fonts/Poppins-Bold.ttf` |
| Barlow Condensed | 400–700 | Cuerpo | `/workspace/fonts/BarlowCondensed-*.ttf` |
| IBM Plex Mono | 400–600 | Labels, firma, kickers | `/workspace/fonts/IBMPlexMono-*.ttf` |

Carga: `@font-face` base64 vía `stlabs_kit.embedded_fonts_css()`.
""",
        encoding="utf-8",
    )
    print("Package →", out)
    return out


if __name__ == "__main__":
    main()
