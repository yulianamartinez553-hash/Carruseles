# -*- coding: utf-8 -*-
"""Carrusel STLabs — 12 repos de GitHub (clon @juanbertorello.ia).
Identidad negro + verde · sebastian.stlabs.ar
Fondos: retícula verde + manchas que se continúan entre slides.
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
REPOS = DATA["repos"]
CTA = DATA.get("cta", "AHORRO")
TOTAL = 14
W, H = 1080, 1350
GRID = 45  # 1080 / 45 = 24 → costuras alineadas

MONTHS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# Manchas puente entre slides consecutivos (centro en la costura vertical).
# y, rx, ry, opacity — la mitad derecha va al slide i, la mitad izquierda al i+1.
BRIDGE_BLOBS = [
    # entre 1→2
    {"y": 220, "rx": 320, "ry": 240, "op": 0.42},
    {"y": 980, "rx": 260, "ry": 300, "op": 0.34},
    # 2→3
    {"y": 480, "rx": 360, "ry": 220, "op": 0.40},
    {"y": 1100, "rx": 220, "ry": 260, "op": 0.30},
    # 3→4
    {"y": 160, "rx": 280, "ry": 280, "op": 0.38},
    {"y": 720, "rx": 340, "ry": 200, "op": 0.42},
    # 4→5
    {"y": 360, "rx": 300, "ry": 340, "op": 0.36},
    {"y": 1050, "rx": 260, "ry": 220, "op": 0.32},
    # 5→6
    {"y": 280, "rx": 240, "ry": 260, "op": 0.40},
    {"y": 860, "rx": 380, "ry": 240, "op": 0.38},
    # 6→7
    {"y": 140, "rx": 320, "ry": 200, "op": 0.34},
    {"y": 640, "rx": 280, "ry": 320, "op": 0.42},
    # 7→8
    {"y": 420, "rx": 340, "ry": 240, "op": 0.38},
    {"y": 1180, "rx": 240, "ry": 220, "op": 0.30},
    # 8→9
    {"y": 200, "rx": 300, "ry": 300, "op": 0.36},
    {"y": 780, "rx": 320, "ry": 200, "op": 0.40},
    # 9→10
    {"y": 520, "rx": 260, "ry": 280, "op": 0.34},
    {"y": 1000, "rx": 340, "ry": 240, "op": 0.36},
    # 10→11
    {"y": 180, "rx": 280, "ry": 220, "op": 0.42},
    {"y": 700, "rx": 360, "ry": 260, "op": 0.38},
    # 11→12
    {"y": 340, "rx": 320, "ry": 240, "op": 0.32},
    {"y": 920, "rx": 260, "ry": 300, "op": 0.40},
    # 12→13
    {"y": 260, "rx": 340, "ry": 220, "op": 0.40},
    {"y": 1080, "rx": 280, "ry": 240, "op": 0.30},
    # 13→14
    {"y": 400, "rx": 300, "ry": 320, "op": 0.38},
    {"y": 880, "rx": 320, "ry": 200, "op": 0.44},
]


def github_graph_svg() -> str:
    random.seed(42)
    cols, rows = 52, 7
    cells = []
    for r in range(rows):
        for c in range(cols):
            lvl = random.choices([0, 1, 2, 3, 4], weights=[35, 25, 20, 12, 8])[0]
            colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
            x = 4 + c * 15
            y = 28 + r * 15
            cells.append(
                f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="{colors[lvl]}"/>'
            )
    month_labels = "".join(
        f'<text x="{4 + i * 44}" y="16" fill="#9aa39c" font-family="IBM Plex Mono,monospace" font-size="11">{m}</text>'
        for i, m in enumerate(MONTHS)
    )
    legend = (
        '<text x="580" y="130" fill="#9aa39c" font-family="IBM Plex Mono,monospace" font-size="11">Menos</text>'
        + "".join(
            f'<rect x="{640 + i * 16}" y="120" width="12" height="12" rx="2" fill="{c}"/>'
            for i, c in enumerate(["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"])
        )
        + '<text x="720" y="130" fill="#9aa39c" font-family="IBM Plex Mono,monospace" font-size="11">Más</text>'
    )
    return (
        f'<svg viewBox="0 0 780 145" xmlns="http://www.w3.org/2000/svg" class="gh-graph">'
        f"{month_labels}{''.join(cells)}{legend}</svg>"
    )


def _ellipse(cx, cy, rx, ry, op, rotate=0) -> str:
    t = f' transform="rotate({rotate} {cx} {cy})"' if rotate else ""
    return (
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}"'
        f' fill="url(#blobGrad)" opacity="{op:.3f}"{t}/>'
    )


def _interior_blobs(slide_idx: int) -> str:
    """Manchas propias del slide (no en la costura), distintas por índice."""
    rng = random.Random(100 + slide_idx * 17)
    parts = []
    # Esquinas / bordes superior e inferior — visibles alrededor de la card
    presets = [
        # (cx, cy, rx, ry, op, rot) — esquinas / bordes visibles alrededor de la card
        (140, 70, 260, 180, 0.36, -18),
        (940, 100, 240, 200, 0.32, 22),
        (100, 1280, 280, 180, 0.34, 12),
        (980, 1240, 250, 200, 0.30, -25),
        (540, 60, 340, 130, 0.22, 0),
        (540, 1300, 360, 120, 0.22, 0),
        (80, 500, 180, 220, 0.28, 30),
        (1000, 650, 190, 240, 0.28, -20),
    ]
    start = slide_idx % len(presets)
    chosen = [presets[(start + k) % len(presets)] for k in range(4)]
    for cx, cy, rx, ry, op, rot in chosen:
        jx = rng.uniform(-35, 35)
        jy = rng.uniform(-25, 25)
        parts.append(
            _ellipse(
                cx + jx,
                cy + jy,
                rx * rng.uniform(0.92, 1.12),
                ry * rng.uniform(0.92, 1.12),
                op,
                rot,
            )
        )
    angle = (slide_idx * 37) % 360
    parts.append(
        _ellipse(
            160 + (slide_idx * 70) % 760,
            280 + (slide_idx * 95) % 750,
            200 + (slide_idx % 5) * 24,
            150 + (slide_idx % 4) * 20,
            0.26,
            angle,
        )
    )
    return "".join(parts)


def _bridge_for_seam(seam_idx: int) -> list[dict]:
    """2 manchas por costura (índice 0 = entre slide 1 y 2)."""
    i = seam_idx * 2
    if i + 1 >= len(BRIDGE_BLOBS):
        return []
    return [BRIDGE_BLOBS[i], BRIDGE_BLOBS[i + 1]]


def bg_layer(slide_idx: int) -> str:
    """Fondo creativo: retícula verde alineada + manchas puente entre slides.

    slide_idx: 1..14
    """
    i = slide_idx - 1  # 0-based
    # Grid offset continuo: cada slide desplaza la retícula en X por W
    # (mismas líneas verticales al pasar de slide a slide)
    ox = -(i * W) % GRID

    blobs = []

    # Mitad derecha de la costura con el slide anterior (centro en x=0)
    if i > 0:
        for b in _bridge_for_seam(i - 1):
            blobs.append(_ellipse(0, b["y"], b["rx"], b["ry"], b["op"]))

    # Mitad izquierda de la costura con el siguiente (centro en x=W)
    if i < TOTAL - 1:
        for b in _bridge_for_seam(i):
            blobs.append(_ellipse(W, b["y"], b["rx"], b["ry"], b["op"]))

    blobs.append(_interior_blobs(slide_idx))

    # Líneas de acento diagonales sutiles distintas por slide
    diag = ""
    rng = random.Random(50 + slide_idx)
    for k in range(4):
        x1 = rng.randint(-100, W + 100)
        y1 = rng.randint(0, H)
        length = rng.randint(240, 560)
        ang = math.radians(rng.choice([25, -25, 40, -40, 15, -55]))
        x2 = x1 + length * math.cos(ang)
        y2 = y1 + length * math.sin(ang)
        diag += (
            f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'stroke="rgba(0,255,178,{0.10 + (k * 0.03):.2f})" stroke-width="2"/>'
        )

    return f"""
<div class="bg-layer" aria-hidden="true">
  <svg class="bg-svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <defs>
      <radialGradient id="blobGrad" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#00FFB2" stop-opacity="1"/>
        <stop offset="40%" stop-color="#00FFB2" stop-opacity="0.55"/>
        <stop offset="100%" stop-color="#00FFB2" stop-opacity="0"/>
      </radialGradient>
      <pattern id="grid{slide_idx}" width="{GRID}" height="{GRID}" patternUnits="userSpaceOnUse" x="{ox}" y="0">
        <path d="M {GRID} 0 L 0 0 0 {GRID}" fill="none" stroke="rgba(0,255,178,0.18)" stroke-width="1.2"/>
      </pattern>
      <pattern id="gridFine{slide_idx}" width="{GRID // 3}" height="{GRID // 3}" patternUnits="userSpaceOnUse" x="{ox}" y="0">
        <path d="M {GRID // 3} 0 L 0 0 0 {GRID // 3}" fill="none" stroke="rgba(0,255,178,0.07)" stroke-width="0.7"/>
      </pattern>
      <filter id="blurSoft" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="22"/>
      </filter>
    </defs>
    <rect width="{W}" height="{H}" fill="#0A0A0A"/>
    <rect width="{W}" height="{H}" fill="url(#gridFine{slide_idx})"/>
    <rect width="{W}" height="{H}" fill="url(#grid{slide_idx})"/>
    <g filter="url(#blurSoft)">{''.join(blobs)}</g>
    {diag}
  </svg>
</div>"""


EXTRA_CSS = """
.slide{background:#0A0A0A !important;}
.slide::before{display:none !important;} /* apaga glow genérico del kit */
.bg-layer{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
.bg-svg{position:absolute;inset:0;width:100%;height:100%;display:block;}

/* ── PORTADA ── */
.s-cover{display:flex;flex-direction:column;height:100%;padding:72px 72px 120px;position:relative;z-index:5;}
.gh-pill{display:inline-flex;align-items:center;gap:10px;background:rgba(20,20,20,.92);border:1px solid rgba(0,255,178,.35);
 border-radius:999px;padding:10px 18px;width:fit-content;margin-bottom:28px;backdrop-filter:blur(8px);}
.gh-pill svg{width:22px;height:22px;fill:#F2F2F2;}
.gh-pill span{font-family:var(--mono);font-size:18px;color:var(--blanco);letter-spacing:.04em;}
.gh-wrap{background:rgba(20,20,20,.9);border:1px solid rgba(0,255,178,.22);border-radius:14px;padding:18px 20px 14px;
 margin-bottom:36px;box-shadow:0 24px 64px rgba(0,0,0,.55);backdrop-filter:blur(10px);}
.gh-graph{width:100%;height:auto;display:block;}
.cover-title{font-family:var(--pop);font-weight:800;font-size:62px;line-height:1.02;color:var(--blanco);max-width:920px;
 text-shadow:0 4px 28px rgba(0,0,0,.75);}
.cover-title .gr{color:var(--verde);}
.cover-sub{margin-top:18px;font-family:var(--cond);font-size:32px;color:var(--gray);}

/* ── CARD REPO ── */
.card-wrap{display:flex;align-items:center;justify-content:center;height:100%;padding:48px 56px 110px;position:relative;z-index:5;}
.repo-card{width:100%;max-width:920px;background:linear-gradient(165deg,rgba(22,22,22,.96) 0%,rgba(14,14,14,.97) 100%);
 border:1.5px solid rgba(0,255,178,.32);border-radius:22px;padding:36px 40px 32px;
 box-shadow:0 32px 80px rgba(0,0,0,.7),0 0 0 1px rgba(255,255,255,.04) inset;backdrop-filter:blur(12px);}
.card-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px;}
.win-dots{display:flex;gap:8px;}
.win-dots i{width:12px;height:12px;border-radius:50%;display:block;}
.win-dots i:nth-child(1){background:#FF5F57;}
.win-dots i:nth-child(2){background:#FEBC2E;}
.win-dots i:nth-child(3){background:#28C840;}
.card-num{font-family:var(--mono);font-size:22px;color:var(--verde);border:1.5px solid rgba(0,255,178,.45);
 border-radius:8px;padding:6px 12px;line-height:1;min-width:48px;text-align:center;}
.repo-org{font-family:var(--mono);font-size:20px;color:var(--gray);margin-top:18px;letter-spacing:.02em;}
.repo-name{font-family:var(--pop);font-weight:800;font-size:72px;line-height:.95;color:var(--blanco);margin-top:4px;}
.repo-vs{display:inline-block;margin-top:16px;font-family:var(--mono);font-size:15px;font-weight:600;
 letter-spacing:.12em;color:var(--verde);background:rgba(0,255,178,.08);border:1px solid rgba(0,255,178,.45);
 border-radius:999px;padding:8px 16px;}
.repo-stats{display:flex;margin-top:28px;padding:22px 0;border-top:1px solid rgba(255,255,255,.08);
 border-bottom:1px solid rgba(255,255,255,.08);}
.stat{flex:1;text-align:center;position:relative;}
.stat:not(:last-child)::after{content:'';position:absolute;right:0;top:10%;height:80%;width:1px;
 background:rgba(255,255,255,.1);}
.stat-lbl{font-family:var(--mono);font-size:13px;letter-spacing:.14em;color:var(--gray);margin-bottom:8px;}
.stat-val{font-family:var(--pop);font-weight:700;font-size:28px;color:var(--blanco);display:flex;align-items:center;
 justify-content:center;gap:8px;}
.stat-val .star{color:#FF9D3C;font-size:24px;}
.lang-dot{width:10px;height:10px;border-radius:50%;display:inline-block;}
.repo-hl{font-family:var(--pop);font-weight:800;font-size:34px;line-height:1.15;color:var(--verde);margin-top:28px;}
.repo-body{font-family:var(--cond);font-size:28px;line-height:1.38;color:var(--gray);margin-top:16px;}
.repo-url{margin-top:28px;font-family:var(--mono);font-size:17px;color:rgba(0,255,178,.75);display:flex;align-items:center;gap:8px;}
.repo-url::before{content:'';width:14px;height:14px;border:1.5px solid rgba(0,255,178,.5);border-radius:50%;}

/* ── CIERRE ── */
.close-wrap{display:flex;flex-direction:column;height:100%;padding:56px 64px 110px;position:relative;z-index:5;}
.close-kicker{font-family:var(--mono);font-size:16px;letter-spacing:.18em;color:var(--gray);text-transform:uppercase;margin-bottom:20px;}
.close-card{flex:1;background:linear-gradient(165deg,rgba(22,22,22,.96),rgba(14,14,14,.97));border:1.5px solid rgba(0,255,178,.28);
 border-radius:20px;padding:32px 36px;display:flex;flex-direction:column;backdrop-filter:blur(12px);
 box-shadow:0 32px 80px rgba(0,0,0,.7);}
.close-head{display:flex;align-items:center;gap:14px;margin-bottom:24px;padding-bottom:20px;border-bottom:1px solid rgba(255,255,255,.08);}
.close-avatar{width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,rgba(0,255,178,.3),rgba(0,255,178,.05));
 border:1.5px solid rgba(0,255,178,.4);display:flex;align-items:center;justify-content:center;
 font-family:var(--mono);font-size:14px;color:var(--verde);}
.close-handle{font-family:var(--mono);font-size:20px;color:var(--verde);}
.close-bio{font-family:var(--cond);font-size:22px;color:var(--gray);margin-top:4px;}
.repo-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 32px;flex:1;}
.repo-row{display:flex;align-items:center;justify-content:space-between;padding:14px 0;
 border-bottom:1px solid rgba(255,255,255,.06);}
.repo-row .num{font-family:var(--mono);font-size:16px;color:rgba(255,82,71,.85);min-width:32px;}
.repo-row .nm{font-family:var(--cond);font-weight:600;font-size:26px;color:var(--blanco);flex:1;margin-left:8px;}
.repo-row .st{font-family:var(--mono);font-size:18px;color:#FF9D3C;display:flex;align-items:center;gap:6px;}
.repo-row .st::before{content:'★';font-size:14px;}
.close-title{font-family:var(--pop);font-weight:800;font-size:44px;color:var(--blanco);margin-top:28px;}
.close-body{font-family:var(--cond);font-size:26px;line-height:1.35;color:var(--gray);margin-top:12px;max-width:880px;}
.close-cta{margin-top:28px;background:var(--verde);color:#04130b;border-radius:14px;padding:22px 32px;
 font-family:var(--pop);font-weight:800;font-size:32px;text-align:center;letter-spacing:.04em;
 box-shadow:0 0 48px rgba(0,255,178,.35);}
"""


def _wrap(idx: int, inner: str) -> str:
    html = chrome(idx, bg_layer(idx) + inner, total=TOTAL, bridges=None, footer=True, counter=False)
    return html


def slide_cover():
    gh_icon = (
        '<svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 '
        '0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.395-.135-.345-.72-1.395-1.23-1.665-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 '
        '1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 '
        '0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 '
        '0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>'
    )
    inner = f"""
<div class="s-cover">
  <div class="gh-pill">{gh_icon}<span>GitHub</span></div>
  <div class="gh-wrap">{github_graph_svg()}</div>
  <h1 class="cover-title">12 repos de GitHub que reemplazan apps<br><span class="gr">que vos ya pagás</span></h1>
  <p class="cover-sub">(gratis, open source y andan hoy)</p>
</div>"""
    return _wrap(1, inner)


def slide_repo(repo: dict, idx: int):
    inner = f"""
<div class="card-wrap">
  <article class="repo-card">
    <div class="card-top">
      <div class="win-dots"><i></i><i></i><i></i></div>
      <div class="card-num">{repo['num']}</div>
    </div>
    <div class="repo-org">{repo['org']} /</div>
    <h2 class="repo-name">{repo['name']}</h2>
    <span class="repo-vs">{repo['vs']}</span>
    <div class="repo-stats">
      <div class="stat"><div class="stat-lbl">STARS</div><div class="stat-val"><span class="star">★</span>{repo['stars']}</div></div>
      <div class="stat"><div class="stat-lbl">FORKS</div><div class="stat-val">{repo['forks']}</div></div>
      <div class="stat"><div class="stat-lbl">LANG</div><div class="stat-val"><span class="lang-dot" style="background:{repo['lang_color']}"></span>{repo['lang']}</div></div>
    </div>
    <h3 class="repo-hl">{repo['headline']}</h3>
    <p class="repo-body">{repo['body']}</p>
    <div class="repo-url">{repo['url']}</div>
  </article>
</div>"""
    return _wrap(idx, inner)


def slide_close():
    rows = ""
    for r in REPOS:
        rows += (
            f"""<div class="repo-row"><span class="num">{r['num']}</span>"""
            f"""<span class="nm">{r['name']}</span><span class="st">{r['stars']}</span></div>"""
        )
    inner = f"""
<div class="close-wrap">
  <div class="close-kicker">GitHub repos · lista completa</div>
  <div class="close-card">
    <div class="close-head">
      <div class="close-avatar">SG</div>
      <div>
        <div class="close-handle">sebastian.stlabs.ar</div>
        <div class="close-bio">RevOps · CRM · IA</div>
      </div>
    </div>
    <div class="repo-grid">{rows}</div>
    <h2 class="close-title">Guardá estos 12.</h2>
    <p class="close-body">Sumá lo que pagás por mes en apps y vas a entender por qué armé esta lista. Te la paso completa, con los links, gratis.</p>
    <div class="close-cta">Comentá {CTA}</div>
  </div>
</div>"""
    return _wrap(14, inner)


def build_slides():
    slides = [slide_cover()]
    for i, repo in enumerate(REPOS, start=2):
        slides.append(slide_repo(repo, i))
    slides.append(slide_close())
    return slides


def main():
    slides = build_slides()
    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML generado →", BUILD / "carrusel.html")
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
    out = package(BUILD, "STLabs-GitHub-Repos", meta=meta)
    print("Package →", out)
    caption = (
        "12 repos de GitHub que reemplazan apps que ya estás pagando todos los meses.\n\n"
        "Gratis, de código abierto y andan hoy. Deslizá y guardá los que te sirvan.\n\n"
        f"Comentá {CTA} y te paso la lista completa con todos los links.\n\n"
        "#github #opensource #automatizacion #ia #ahorro #stlabs"
    )
    (out / "caption.txt").write_text(caption, encoding="utf-8")
    manifiesto = """# Manifiesto de fuentes — 12 repos GitHub STLabs

| Familia | Peso | Rol | Origen |
|---|---|---|---|
| Poppins | 700/800 | Títulos de portada, nombres de repo, headlines | Google Fonts → `/workspace/fonts/Poppins-Bold.ttf` |
| Barlow Condensed | 400–700 | Cuerpo, subtítulos, bio | STLabs pack → `/workspace/fonts/BarlowCondensed-*.ttf` |
| IBM Plex Mono | 400–600 | Labels, stats, URLs, footer, firma | STLabs pack → `/workspace/fonts/IBMPlexMono-*.ttf` |
| Bebas Neue | 400 | Display alternativo (kit base) | STLabs pack |

Carga: embebidas en base64 vía `stlabs_kit.embedded_fonts_css()` al empaquetar.
"""
    (out / "MANIFIESTO-FUENTES.md").write_text(manifiesto, encoding="utf-8")
    return out


if __name__ == "__main__":
    main()
