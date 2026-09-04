# -*- coding: utf-8 -*-
"""Carrusel STLabs — 10 reglas de un padre.
Fondo negro + retícula verde + manchas puente · sebastian.stlabs.ar
"""
from __future__ import annotations

import base64
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
REGLAS = DATA["reglas"]
CTA = DATA.get("cta", "PADRE")
TOTAL = int(DATA["slides"])
W, H = 1080, 1350
GRID = 45

COVER_B64 = base64.b64encode((BUILD / "assets" / "cover_photos.jpg").read_bytes()).decode()
COVER_URI = f"data:image/jpeg;base64,{COVER_B64}"

# 2 manchas por costura (13 costuras × 2 = 26)
BRIDGE = [
    {"y": 240, "rx": 340, "ry": 260, "op": 0.40},
    {"y": 980, "rx": 280, "ry": 300, "op": 0.34},
    {"y": 500, "rx": 360, "ry": 220, "op": 0.38},
    {"y": 1120, "rx": 240, "ry": 260, "op": 0.30},
    {"y": 180, "rx": 300, "ry": 280, "op": 0.36},
    {"y": 740, "rx": 340, "ry": 200, "op": 0.40},
    {"y": 380, "rx": 320, "ry": 340, "op": 0.34},
    {"y": 1060, "rx": 260, "ry": 220, "op": 0.32},
    {"y": 300, "rx": 260, "ry": 260, "op": 0.38},
    {"y": 880, "rx": 380, "ry": 240, "op": 0.36},
    {"y": 160, "rx": 320, "ry": 200, "op": 0.34},
    {"y": 660, "rx": 300, "ry": 320, "op": 0.40},
    {"y": 440, "rx": 340, "ry": 240, "op": 0.36},
    {"y": 1180, "rx": 240, "ry": 220, "op": 0.30},
    {"y": 220, "rx": 300, "ry": 300, "op": 0.34},
    {"y": 800, "rx": 320, "ry": 200, "op": 0.38},
    {"y": 540, "rx": 280, "ry": 280, "op": 0.32},
    {"y": 1020, "rx": 340, "ry": 240, "op": 0.36},
    {"y": 200, "rx": 300, "ry": 220, "op": 0.40},
    {"y": 720, "rx": 360, "ry": 260, "op": 0.36},
    {"y": 360, "rx": 320, "ry": 240, "op": 0.32},
    {"y": 940, "rx": 280, "ry": 300, "op": 0.38},
]


def _ellipse(cx, cy, rx, ry, op, rot=0) -> str:
    t = f' transform="rotate({rot} {cx:.0f} {cy:.0f})"' if rot else ""
    return (
        f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="{rx:.0f}" ry="{ry:.0f}"'
        f' fill="url(#blobGrad)" opacity="{op:.2f}"{t}/>'
    )


def _interior(idx: int) -> str:
    rng = random.Random(200 + idx * 19)
    presets = [
        (120, 80, 280, 180, 0.34, -18),
        (960, 110, 260, 200, 0.30, 22),
        (90, 1280, 300, 180, 0.32, 12),
        (990, 1240, 260, 200, 0.28, -25),
        (540, 70, 360, 120, 0.20, 0),
        (540, 1300, 380, 110, 0.20, 0),
        (70, 520, 200, 240, 0.26, 28),
        (1010, 680, 210, 250, 0.26, -18),
    ]
    start = idx % len(presets)
    parts = []
    for k in range(4):
        cx, cy, rx, ry, op, rot = presets[(start + k) % len(presets)]
        parts.append(
            _ellipse(
                cx + rng.uniform(-30, 30),
                cy + rng.uniform(-20, 20),
                rx * rng.uniform(0.92, 1.1),
                ry * rng.uniform(0.92, 1.1),
                op,
                rot,
            )
        )
    parts.append(
        _ellipse(
            180 + (idx * 75) % 720,
            300 + (idx * 100) % 700,
            210 + (idx % 5) * 20,
            150 + (idx % 4) * 18,
            0.24,
            (idx * 41) % 360,
        )
    )
    return "".join(parts)


def bg_layer(slide_idx: int) -> str:
    i = slide_idx - 1
    ox = -(i * W) % GRID
    blobs: list[str] = []
    if i > 0:
        a = (i - 1) * 2
        for b in BRIDGE[a : a + 2]:
            blobs.append(_ellipse(0, b["y"], b["rx"], b["ry"], b["op"]))
    if i < TOTAL - 1:
        a = i * 2
        for b in BRIDGE[a : a + 2]:
            blobs.append(_ellipse(W, b["y"], b["rx"], b["ry"], b["op"]))
    blobs.append(_interior(slide_idx))

    rng = random.Random(60 + slide_idx)
    diag = ""
    for k in range(4):
        x1 = rng.randint(-80, W + 80)
        y1 = rng.randint(0, H)
        length = rng.randint(220, 520)
        ang = math.radians(rng.choice([25, -25, 40, -40, 15, -55]))
        diag += (
            f'<line x1="{x1}" y1="{y1}" x2="{x1 + length * math.cos(ang):.0f}" '
            f'y2="{y1 + length * math.sin(ang):.0f}" '
            f'stroke="rgba(0,255,178,{0.09 + k * 0.025:.2f})" stroke-width="2"/>'
        )

    return f"""
<div class="bg-layer" aria-hidden="true">
  <svg class="bg-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <defs>
      <radialGradient id="blobGrad{slide_idx}" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#00FFB2" stop-opacity="1"/>
        <stop offset="45%" stop-color="#00FFB2" stop-opacity="0.5"/>
        <stop offset="100%" stop-color="#00FFB2" stop-opacity="0"/>
      </radialGradient>
      <pattern id="grid{slide_idx}" width="{GRID}" height="{GRID}" patternUnits="userSpaceOnUse" x="{ox}" y="0">
        <path d="M {GRID} 0 L 0 0 0 {GRID}" fill="none" stroke="rgba(0,255,178,0.16)" stroke-width="1.2"/>
      </pattern>
      <pattern id="gridFine{slide_idx}" width="{GRID // 3}" height="{GRID // 3}" patternUnits="userSpaceOnUse" x="{ox}" y="0">
        <path d="M {GRID // 3} 0 L 0 0 0 {GRID // 3}" fill="none" stroke="rgba(0,255,178,0.06)" stroke-width="0.7"/>
      </pattern>
      <filter id="blurSoft{slide_idx}" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="22"/>
      </filter>
    </defs>
    <rect width="{W}" height="{H}" fill="#0A0A0A"/>
    <rect width="{W}" height="{H}" fill="url(#gridFine{slide_idx})"/>
    <rect width="{W}" height="{H}" fill="url(#grid{slide_idx})"/>
    <g filter="url(#blurSoft{slide_idx})">{''.join(blobs).replace('url(#blobGrad)', f'url(#blobGrad{slide_idx})')}</g>
    {diag}
  </svg>
</div>"""


EXTRA_CSS = """
.slide{background:#0A0A0A !important;}
.slide::before{display:none !important;}
.bg-layer{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
.bg-svg{position:absolute;inset:0;width:100%;height:100%;display:block;}

.s-cover{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;}
.cover-photos{width:100%;height:720px;object-fit:cover;object-position:center top;display:block;flex-shrink:0;}
.cover-body{flex:1;display:flex;flex-direction:column;justify-content:center;padding:28px 56px 110px;text-align:center;}
.cover-kicker{font-family:var(--mono);font-size:15px;letter-spacing:.2em;color:var(--verde);text-transform:uppercase;margin-bottom:18px;}
.cover-title{font-family:var(--pop);font-weight:800;font-size:44px;line-height:1.1;color:var(--blanco);
 text-transform:uppercase;letter-spacing:-.01em;text-shadow:0 4px 28px rgba(0,0,0,.75);}
.cover-title .gr{color:var(--verde);}

.s-rule{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 justify-content:center;padding:80px 64px 130px;}
.rule-num{font-family:var(--mono);font-size:17px;letter-spacing:.2em;color:var(--verde);
 text-transform:uppercase;margin-bottom:26px;}
.rule-num span{display:inline-block;border:1.5px solid rgba(0,255,178,.45);border-radius:8px;
 padding:8px 14px;margin-right:12px;font-size:22px;letter-spacing:.08em;}
.rule-text{font-family:var(--pop);font-weight:800;font-size:48px;line-height:1.14;color:var(--blanco);
 max-width:940px;text-shadow:0 4px 24px rgba(0,0,0,.55);}
.rule-extra{margin-top:32px;font-family:var(--pop);font-weight:800;font-size:42px;line-height:1.2;color:var(--verde);}
.rule-extra p{margin-top:8px;}

.s-close{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 justify-content:center;align-items:center;padding:80px 64px 130px;text-align:center;}
.close-lead{font-family:var(--pop);font-weight:800;font-size:40px;line-height:1.15;color:var(--gray);margin-bottom:24px;}
.close-mid{font-family:var(--pop);font-weight:800;font-size:46px;line-height:1.12;color:var(--blanco);margin-bottom:24px;max-width:900px;}
.close-mid .gr{color:var(--verde);}
.close-end{font-family:var(--cond);font-size:30px;line-height:1.35;color:var(--gray);max-width:860px;margin:0 auto 36px;}
.close-cta{display:inline-block;background:var(--verde);color:#04130b;border-radius:14px;padding:22px 40px;
 font-family:var(--pop);font-weight:800;font-size:28px;letter-spacing:.04em;
 box-shadow:0 0 48px rgba(0,255,178,.35);}
"""


def _wrap(idx: int, inner: str, bridges=None) -> str:
    return chrome(idx, bg_layer(idx) + inner, total=TOTAL, bridges=bridges, footer=True, counter=False)


def slide_cover() -> str:
    inner = f"""
<div class="s-cover">
  <img class="cover-photos" src="{COVER_URI}" alt="">
  <div class="cover-body">
    <div class="cover-kicker">10 reglas · para padres</div>
    <h1 class="cover-title">Un hombre perdió a su hijo de 3 años y escribió <span class="gr">10 reglas</span> que todos los padres deben seguir:</h1>
  </div>
</div>"""
    return _wrap(1, inner)


def slide_rule(regla: dict, idx: int) -> str:
    n = int(regla["n"])
    extra = ""
    if regla.get("extra"):
        lines = "".join(f"<p>{e}</p>" for e in regla["extra"])
        extra = f'<div class="rule-extra">{lines}</div>'
    inner = f"""
<div class="s-rule">
  <div class="rule-num"><span>{n:02d}</span> Regla {n}</div>
  <p class="rule-text">{regla['texto']}</p>
  {extra}
</div>"""
    return _wrap(idx, inner)


def slide_close() -> str:
    inner = f"""
<div class="s-close">
  <p class="close-lead">El 99% va a seguir de largo…</p>
  <p class="close-mid">Pero el <span class="gr">1%</span> que termine este post es el que va a hacer la diferencia.</p>
  <p class="close-end">Si no querés perderte esta página, ya sabés qué es lo único que tenés que hacer para seguir viéndonos todos los días.</p>
  <div class="close-cta">Seguí la cuenta · Comentá {CTA}</div>
</div>"""
    return _wrap(TOTAL, inner)


def build_slides() -> list[str]:
    slides = [slide_cover()]
    for i, r in enumerate(REGLAS, start=2):
        slides.append(slide_rule(r, i))
    slides.append(slide_close())
    return slides


def main():
    slides = build_slides()
    assert len(slides) == TOTAL, f"esperaba {TOTAL}, got {len(slides)}"
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
    out = package(BUILD, "STLabs-10-Reglas-Padre", meta=meta)
    caption = (
        "Un hombre perdió a su hijo de 3 años y dejó 10 reglas que todo padre debería leer.\n\n"
        "Deslizá. Guardá. Aplicá.\n\n"
        f"Comentá {CTA} si esto te pegó.\n\n"
        "#padre #familia #reglas #vida #stlabs"
    )
    (out / "caption.txt").write_text(caption, encoding="utf-8")
    (out / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — 10 reglas de un padre

| Familia | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Poppins | 800 | Títulos / reglas | `/workspace/fonts/Poppins-Bold.ttf` | `@font-face` base64 vía kit |
| Barlow Condensed | 400–700 | Cuerpo cierre | `/workspace/fonts/BarlowCondensed-*.ttf` | idem |
| IBM Plex Mono | 400–600 | Labels, kicker, firma | `/workspace/fonts/IBMPlexMono-*.ttf` | idem |
| Bebas Neue | 400 | Display kit | STLabs pack | idem |
""",
        encoding="utf-8",
    )
    print("Package →", out)
    return out


if __name__ == "__main__":
    main()
