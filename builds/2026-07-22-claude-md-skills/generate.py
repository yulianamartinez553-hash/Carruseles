# -*- coding: utf-8 -*-
"""Clone: Claude Code Skills (CLAUDE.md) → STLabs · blanco · #00FFB2 · español."""
from __future__ import annotations

import base64
import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package  # noqa: E402

CONTENT = json.loads((BUILD / "content.json").read_text(encoding="utf-8"))
TOTAL = int(CONTENT["slides"])
KEYWORD = CONTENT["keyword_portada"]
WORD_DIR = REPO / "Word"
VERDE = "#00FFB2"
INK = "#0A0A0A"

CLAUDE_PNG = REPO / "assets" / "claude.png"
CLAUDE_URI = "data:image/png;base64," + base64.b64encode(CLAUDE_PNG.read_bytes()).decode()
SEB_URI = f"data:image/jpeg;base64,{base64.b64encode((REPO / 'seb.jpg').read_bytes()).decode()}"


EXTRA_CSS = f"""
:root{{--acento:{VERDE};--ink:{INK};--orange:#E8916A;}}
.sheet{{background:#e8e8e8;}}
.slide{{
  color:var(--ink);
  background:
    radial-gradient(42% 30% at 92% 4%, rgba(0,255,178,.08), transparent 58%),
    radial-gradient(36% 26% at 8% 96%, rgba(10,10,10,.04), transparent 55%),
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='180' height='180'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.92 0 0 0 0 0.92 0 0 0 0 0.91 0 0 0 0.18 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    linear-gradient(180deg,#FFFFFF 0%, #F7F7F5 100%);
  background-blend-mode:normal,normal,overlay,normal;
}}
.web{{display:none!important;}}
.foot{{
  position:absolute;left:0;right:0;bottom:56px;z-index:10;text-align:center;
  font-family:var(--mono);font-size:20px;letter-spacing:1px;color:var(--verde);
}}
.swipe{{
  position:absolute;right:56px;bottom:120px;z-index:10;
  font-family:var(--mono);font-size:18px;letter-spacing:2px;color:#6a736e;
}}
.meta{{
  position:absolute;left:56px;right:56px;top:48px;z-index:8;
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--mono);font-size:16px;letter-spacing:1px;color:#8a918c;
}}
.meta .brand{{color:var(--verde);}}
.tag{{
  display:inline-block;background:#0A0A0A;color:#fff;
  font-family:var(--mono);font-size:18px;letter-spacing:2px;padding:10px 16px;border-radius:8px;
}}
.h1{{
  margin:0;font-family:var(--impact);font-weight:900;font-size:92px;line-height:0.95;
  letter-spacing:.5px;color:var(--ink);position:relative;z-index:5;
  -webkit-text-stroke:4px var(--ink);paint-order:stroke fill;
}}
.h1 .bar{{
  display:inline-block;background:var(--acento);color:var(--ink);
  -webkit-text-stroke:0;padding:6px 18px 10px;margin-top:10px;
  box-shadow:0 0 0 2px rgba(0,255,178,.25);
}}
.h1 .hl{{color:var(--acento);-webkit-text-stroke:4px var(--acento);}}
.sub{{
  margin-top:18px;font-family:var(--pop);font-weight:800;font-size:32px;
  color:var(--ink);line-height:1.25;max-width:920px;position:relative;z-index:5;
}}
.body{{
  margin-top:16px;font-family:var(--cond);font-size:30px;color:#3a3f3c;
  line-height:1.35;max-width:920px;position:relative;z-index:5;
}}
.body b{{color:var(--ink);font-weight:700;}}
.slash{{
  font-family:var(--mono);font-weight:700;font-size:56px;color:var(--ink);
  letter-spacing:-1px;position:relative;z-index:5;
}}
.slash .u{{
  display:inline;border-bottom:6px solid var(--acento);padding-bottom:2px;
}}
.pad{{padding:110px 64px 0;position:relative;z-index:5;text-align:left;}}
.center{{text-align:center;}}
.card{{
  background:#fff;border:1.5px solid rgba(10,10,10,.10);border-radius:18px;
  box-shadow:0 14px 36px rgba(10,10,10,.08);position:relative;
}}
.ba{{
  display:grid;grid-template-columns:1fr 1fr;gap:18px;position:relative;z-index:4;
}}
.ba .card{{padding:28px 24px;min-height:280px;}}
.ba .lab{{
  font-family:var(--mono);font-size:18px;letter-spacing:2px;color:var(--acento);
  margin-bottom:12px;
}}
.ba .t{{
  font-family:var(--impact);font-size:48px;line-height:1;
  -webkit-text-stroke:2px currentColor;paint-order:stroke fill;margin-bottom:14px;
}}
.ba .d{{font-family:var(--cond);font-size:26px;line-height:1.35;color:#3a3f3c;}}
.ba-arrow{{
  position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:44px;height:44px;border-radius:50%;background:var(--acento);color:var(--ink);
  display:grid;place-items:center;font-family:var(--pop);font-weight:800;font-size:22px;
  z-index:6;box-shadow:0 8px 18px rgba(0,255,178,.35);
}}
.step{{
  display:flex;align-items:flex-start;gap:18px;padding:22px 24px;margin-bottom:14px;
}}
.num{{
  width:52px;height:52px;border-radius:50%;background:var(--ink);color:#fff;
  display:grid;place-items:center;font-family:var(--pop);font-weight:800;font-size:24px;
  flex-shrink:0;
}}
.step-top{{
  display:flex;justify-content:space-between;align-items:center;width:100%;
  font-family:var(--mono);font-size:15px;letter-spacing:1px;color:#8a918c;margin-bottom:6px;
}}
.step-h{{font-family:var(--pop);font-weight:800;font-size:30px;color:var(--ink);}}
.step-d{{font-family:var(--cond);font-size:24px;color:#4a524e;margin-top:4px;}}
.cta-pill{{
  display:inline-block;background:var(--acento);color:var(--ink);
  font-family:var(--mono);font-size:28px;padding:22px 36px;border-radius:999px;
  box-shadow:0 12px 28px rgba(0,255,178,.35);
}}
.fix-pill{{
  display:inline-block;background:#fff;border:3px solid var(--acento);
  font-family:var(--cond);font-size:34px;font-weight:600;padding:18px 28px;border-radius:14px;
  color:var(--ink);
}}
.fix-pill u{{text-decoration-color:var(--acento);text-underline-offset:6px;}}
.claude{{
  display:block;margin:0 auto;object-fit:contain;
  filter:drop-shadow(0 14px 28px rgba(0,0,0,.16));
}}
.prop{{
  position:absolute;z-index:4;pointer-events:none;
}}
.burn{{
  width:120px;height:150px;background:#1a1a1a;border-radius:6px;
  box-shadow:0 10px 24px rgba(0,0,0,.2);
  font-family:var(--mono);font-size:11px;color:#9aa39c;padding:10px 8px;line-height:1.35;
  transform:rotate(8deg);
}}
.flame{{
  position:absolute;right:-8px;top:-18px;width:28px;height:36px;
  background:radial-gradient(circle at 50% 70%, #FF9D3C 0%, #FF5247 55%, transparent 70%);
  border-radius:50% 50% 40% 40%;
}}
.thought{{
  width:90px;height:56px;border:3px solid var(--ink);border-radius:40px;
  position:relative;
}}
.thought:after{{
  content:'';position:absolute;left:18px;bottom:-14px;width:14px;height:14px;
  border:3px solid var(--ink);border-radius:50%;
}}
.credit{{
  margin-top:10px;padding:16px 22px;border-radius:999px;background:#fff;
  border:1.5px solid rgba(10,10,10,.1);box-shadow:0 10px 24px rgba(10,10,10,.06);
  font-family:var(--cond);font-size:24px;color:#3a3f3c;text-align:center;
}}
.credit b{{color:var(--acento);}}
"""


def wrap(idx: int, inner: str, swipe: bool = True) -> str:
    html = chrome(idx, inner, total=TOTAL, bridges=None, footer=False)
    extras = '<div class="foot">sebastian.stlabs.ar</div>'
    if swipe and idx < TOTAL:
        extras = '<div class="swipe">deslizá →</div>' + extras
    return html.replace("</section>", extras + "</section>", 1)


def meta_bar(n: int, right: str = "") -> str:
    r = right or f"{n:02d}/{TOTAL:02d}"
    return f"""
<div class="meta">
  <span>JULIO 2026</span>
  <span class="brand">sebastian.stlabs.ar</span>
  <span>{r}</span>
</div>
"""


def slide_cover(s: dict) -> str:
    return wrap(
        1,
        f"""
{meta_bar(1, "PORTADA")}
<div class="pad center" style="padding-top:150px;">
  <h1 class="h1" style="font-size:64px;line-height:1.05;">
    <span style="display:block;white-space:nowrap;">{s['linea1']}</span>
    <span class="bar" style="display:inline-block;white-space:nowrap;margin-top:14px;">{s['linea2']}</span>
  </h1>
</div>
<div style="position:absolute;left:0;right:0;top:480px;bottom:250px;z-index:4;display:flex;align-items:center;justify-content:center;">
  <div style="position:relative;width:440px;height:340px;">
    <img class="claude" src="{CLAUDE_URI}" alt="Claude" style="width:250px;height:234px;position:absolute;left:30px;bottom:30px;">
    <div class="prop burn" style="right:10px;bottom:60px;">
      <div class="flame"></div>
      def fix():<br>
      &nbsp;&nbsp;return True<br>
      # CLAUDE.md<br>
      rules = [...]
    </div>
    <div class="prop" style="left:200px;top:10px;font-family:var(--impact);font-size:64px;color:var(--ink);">?</div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:155px;text-align:center;z-index:5;">
  <div class="fix-pill">Este archivo lo <u>arregla</u>.</div>
</div>
""",
    )


def slide_skill(idx: int, s: dict, claude_extra: str = "") -> str:
    title = f"""{s.get('titulo_a','')}<span class="bar">{s.get('titulo_b','')}</span>"""
    if s.get("titulo_a", "").startswith("/"):
        # slash style like surgical
        a = s["titulo_a"]
        b = s.get("titulo_b", "")
        title = f"""<span class="slash"><span class="u">{a.rstrip('-')}</span>{'-' if a.endswith('-') or a.endswith('/') else ''}{b}</span>"""
        # Actually for skill 3/5 we use slash style
    sub = f'<p class="sub">{s["subtitulo"]}</p>' if s.get("subtitulo") else ""
    return wrap(
        idx,
        f"""
{meta_bar(idx)}
<div class="pad">
  <div class="tag">{s['tag']}</div>
  <h1 class="h1" style="margin-top:22px;font-size:84px;">{title}</h1>
  {sub}
  <p class="body">{s['cuerpo']}</p>
</div>
{claude_extra}
""",
    )


def slide_skill01(s: dict) -> str:
    claude = f"""
<div style="position:absolute;left:0;right:0;bottom:170px;z-index:4;text-align:center;">
  <div style="position:relative;display:inline-block;">
    <div class="thought" style="position:absolute;left:50%;top:-70px;margin-left:-45px;"></div>
    <img class="claude" src="{CLAUDE_URI}" alt="Claude" style="width:220px;height:206px;">
  </div>
</div>
"""
    title = f"""{s['titulo_a']}<br><span class="bar">{s['titulo_b']}</span>"""
    return wrap(
        2,
        f"""
{meta_bar(2)}
<div class="pad">
  <div class="tag">{s['tag']}</div>
  <h1 class="h1" style="margin-top:22px;font-size:88px;">{title}</h1>
  <p class="body" style="margin-top:22px;">{s['cuerpo']}</p>
</div>
{claude}
""",
    )


def slide_skill02(s: dict) -> str:
    return wrap(
        3,
        f"""
{meta_bar(3)}
<div class="pad">
  <div class="tag" style="background:#fff;color:#0A0A0A;border:2px solid #0A0A0A;">{s['tag']}</div>
  <div class="slash" style="margin-top:22px;"><span class="u">/simplicidad</span>-primero</div>
  <p class="sub">{s['subtitulo']}</p>
  <p class="body">{s['cuerpo']}</p>
</div>
<div class="ba" style="position:absolute;left:64px;right:64px;bottom:160px;">
  <div class="ba-arrow">→</div>
  <div class="card" style="background:#1E1E1E;border:none;">
    <div class="lab">ANTES</div>
    <div class="t" style="color:#fff;">{s['before_t']}</div>
    <div class="d" style="color:#b8beb9;">{s['before_d']}</div>
  </div>
  <div class="card" style="background:#141414;border:2px solid var(--acento);">
    <div class="lab">DESPUÉS</div>
    <div class="t" style="color:#fff;">{s['after_t']}</div>
    <div class="d" style="color:#b8beb9;">{s['after_d']}</div>
  </div>
</div>
""",
    )


def slide_skill03(s: dict) -> str:
    return wrap(
        4,
        f"""
{meta_bar(4)}
<div class="pad">
  <div class="tag">{s['tag']}</div>
  <div class="slash" style="margin-top:22px;font-size:64px;"><span class="u">/cambios</span>-quirúrgicos</div>
  <p class="sub">{s['subtitulo']}</p>
  <p class="body">{s['cuerpo']}</p>
</div>
<div style="position:absolute;left:0;right:0;bottom:160px;z-index:4;text-align:center;">
  <div style="position:relative;display:inline-block;">
    <div style="position:absolute;left:50%;top:-8px;margin-left:-70px;width:140px;height:36px;background:#9ED6FF;border-radius:18px 18px 8px 8px;z-index:5;"></div>
    <img class="claude" src="{CLAUDE_URI}" alt="Claude" style="width:200px;height:188px;position:relative;z-index:4;">
    <div style="position:absolute;left:50%;bottom:-10px;margin-left:-90px;width:180px;height:70px;background:#1a1a1a;border-radius:10px;border:2px solid var(--acento);z-index:3;
      font-family:var(--mono);font-size:12px;color:var(--acento);padding:10px;text-align:left;">
      def fixBug():<br>&nbsp;&nbsp;return ok
    </div>
  </div>
</div>
""",
    )


def slide_skill04(s: dict) -> str:
    return wrap(
        5,
        f"""
{meta_bar(5)}
<div class="pad">
  <div class="tag">{s['tag']}</div>
  <div class="slash" style="margin-top:22px;font-size:60px;"><span class="u">/ejecución</span>-con-meta</div>
  <p class="sub">{s['subtitulo']}</p>
  <p class="body">{s['cuerpo']}</p>
</div>
<div style="position:absolute;left:64px;right:64px;bottom:170px;z-index:4;">
  <div class="card" style="padding:28px 30px;">
    <div style="font-family:var(--mono);font-size:18px;color:var(--acento);margin-bottom:14px;">PLAN → VERIFICAR</div>
    <div style="font-family:var(--cond);font-size:28px;line-height:1.55;color:var(--ink);">
      1. Escribí el test → <b>falla</b><br>
      2. Implementá lo mínimo → <b>pasa</b><br>
      3. Repetí hasta cumplir el criterio
    </div>
  </div>
  <div style="margin-top:18px;text-align:center;">
    <img class="claude" src="{CLAUDE_URI}" alt="Claude" style="width:120px;height:112px;">
  </div>
</div>
""",
    )


def slide_install(s: dict) -> str:
    steps = ""
    for i, p in enumerate(s["pasos"], 1):
        steps += f"""
        <div class="card step">
          <div class="num">{i}</div>
          <div style="flex:1;">
            <div class="step-top"><span>CLAUDE CODE</span><span>{p['t']}</span></div>
            <div class="step-h">{p['h']}</div>
            <div class="step-d">{p['d']}</div>
          </div>
        </div>"""
    return wrap(
        6,
        f"""
{meta_bar(6, "INSTALAR")}
<div class="pad" style="padding-top:100px;">
  <div class="tag">{s['tag']}</div>
  <h1 class="h1" style="margin-top:18px;font-size:78px;">{s['titulo']}</h1>
</div>
<div style="position:absolute;left:56px;right:56px;top:340px;bottom:150px;z-index:4;overflow:hidden;">
  {steps}
  <div class="credit">Hecho por <b>Jiayuan</b> (multica-ai). MIT. Gratis.</div>
</div>
""",
    )


def slide_cta(s: dict) -> str:
    return wrap(
        7,
        f"""
{meta_bar(7, "FIN")}
<div class="pad center" style="padding-top:180px;">
  <h1 class="h1" style="font-size:88px;">{s['linea1']}<br>
    <span class="hl">{s['linea2']}</span>
  </h1>
  <div style="margin-top:40px;">
    <div class="cta-pill">{s['boton']}</div>
  </div>
</div>
<div style="position:absolute;left:0;right:0;bottom:200px;z-index:4;text-align:center;">
  <img class="claude" src="{CLAUDE_URI}" alt="Claude" style="width:180px;height:168px;">
</div>
<div style="position:absolute;left:0;right:0;bottom:140px;text-align:center;z-index:5;
  font-family:var(--mono);font-size:18px;color:#6a736e;">
  {s['footer_extra']}
</div>
""",
        swipe=False,
    )


def main():
    slides_data = CONTENT["slides_copy"]
    slides = [
        slide_cover(slides_data[0]),
        slide_skill01(slides_data[1]),
        slide_skill02(slides_data[2]),
        slide_skill03(slides_data[3]),
        slide_skill04(slides_data[4]),
        slide_install(slides_data[5]),
        slide_cta(slides_data[6]),
    ]

    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML:", BUILD / "carrusel.html")
    pngs = render(BUILD)
    print(f"Render OK: {len(pngs)}")

    meta = {
        "titulo": CONTENT["titulo"],
        "slides": TOTAL,
        "fondo": CONTENT["fondo"],
        "familia_visual": CONTENT["familia_visual"],
        "origen": CONTENT["origen"],
        "keyword_portada": KEYWORD,
        "modo_fondo": "blanco",
        "idioma": "es",
        "acento": VERDE,
        "feedback": {"estado": "borrador"},
    }
    out = package(BUILD, "STLabs-Claude-MD-Skills", meta=meta)
    print("Package:", out)

    KEEP = {".ttf", ".otf", ".woff", ".woff2"}
    KEEP_NAMES = {"befonts-license.txt", "impact-font.zip"}
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    for p in list(WORD_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() not in KEEP and p.name.lower() not in KEEP_NAMES:
            p.unlink()
    for fname in ("impact.ttf", "Impact.ttf", "impacted.ttf", "unicodeimpact.ttf", "Befonts-License.txt", "Anton-Regular.ttf"):
        src = REPO / "fonts" / fname
        if src.exists():
            shutil.copy2(src, WORD_DIR / fname)

    for name in (
        "STLabs-Claude-MD-Skills.html",
        "STLabs-Claude-MD-Skills.zip",
        "_preview-tira.png",
        "manifest.json",
        *[f"slide-{i:02d}.png" for i in range(1, TOTAL + 1)],
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    shutil.copy2(CLAUDE_PNG, WORD_DIR / "claude.png")
    shutil.copy2(BUILD / "content.json", WORD_DIR / "content.json")

    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Font manifesto — Claude MD Skills

| Font | Weight | Role | Source |
|---|---|---|---|
| Impact | 900 | Titles / display bars | `fonts/Impact.ttf` |
| Poppins | 800 | Subtitles / step titles | `fonts/Poppins-Bold.ttf` |
| Barlow Condensed | 400–700 | Body | `fonts/BarlowCondensed-*.ttf` |
| IBM Plex Mono | 400–600 | Tags / meta / footer / CTA | `fonts/IBMPlexMono-*.ttf` |

Accent bars: `#00FFB2` (replaces orange bars from reference).
Claude mascot: `assets/claude.png` (orange, unchanged).
Idioma: español (voseo). Identity: sebastian.stlabs.ar · white · piedra_roca · blueprint.
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""STLabs Carousel — Claude Code Skills (CLAUDE.md)
Clone of brodyautomates Karpathy skills carousel → sebastian.stlabs.ar
Background: WHITE · Texture: piedra_roca · Family: blueprint
Slides: {TOTAL} · Keyword: {KEYWORD} · Idioma: español
Accent: #00FFB2 · Claude: assets/claude.png (orange)
Source: content.json · repo multica-ai/andrej-karpathy-skills
""",
        encoding="utf-8",
    )
    print("Word/:", WORD_DIR)


if __name__ == "__main__":
    main()
