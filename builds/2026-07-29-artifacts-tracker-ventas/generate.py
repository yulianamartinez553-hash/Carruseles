# -*- coding: utf-8 -*-
"""Clone: Artifacts tracker de ventas → STLabs · blanco · #00FFB2 · español."""
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


def _font_face(name: str, path: Path, weight: str = "400", style: str = "normal") -> str:
    if not path.exists():
        return ""
    b64 = base64.b64encode(path.read_bytes()).decode()
    return (
        f"@font-face{{font-family:'{name}';font-style:{style};font-weight:{weight};"
        f"font-display:block;src:url(data:font/ttf;base64,{b64}) format('truetype');}}"
    )


FONT_EXTRA = "".join(
    [
        _font_face("Impact", REPO / "fonts" / "Impact.ttf", "900"),
        _font_face("Impact", REPO / "fonts" / "impact.ttf", "400"),
        _font_face("Anton", REPO / "fonts" / "Anton-Regular.ttf", "400"),
    ]
)

CLAUDE_URI = ""
if (REPO / "assets" / "claude.png").exists():
    CLAUDE_URI = "data:image/png;base64," + base64.b64encode(
        (REPO / "assets" / "claude.png").read_bytes()
    ).decode()

EXTRA_CSS = FONT_EXTRA + f"""
:root{{--acento:{VERDE};--ink:{INK};
  --impact:'Impact','Anton','Bebas Neue',sans-serif;
  --title:'Impact','Anton',sans-serif;}}
.sheet{{background:#e8e8e8;}}
.slide{{
  color:var(--ink);
  background:
    linear-gradient(rgba(10,10,10,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(10,10,10,.04) 1px, transparent 1px),
    radial-gradient(50% 36% at 0% 100%, rgba(0,255,178,.16), transparent 62%),
    radial-gradient(50% 36% at 100% 100%, rgba(0,255,178,.14), transparent 62%),
    linear-gradient(180deg,#FFFFFF 0%, #F4F7F5 100%);
  background-size:52px 52px,52px 52px,auto,auto,auto;
}}
.web{{display:none!important;}}
.foot{{
  position:absolute;left:0;right:0;bottom:52px;z-index:12;text-align:center;
  font-family:var(--mono);font-size:20px;letter-spacing:1px;color:var(--verde);
}}
.swipe{{
  position:absolute;right:56px;bottom:110px;z-index:12;
  font-family:var(--mono);font-size:17px;letter-spacing:1px;color:#7a847e;
}}
.brand-tr{{
  position:absolute;top:48px;right:56px;z-index:10;
  font-family:var(--mono);font-size:16px;letter-spacing:1px;color:var(--verde);
}}
.corner{{
  position:absolute;z-index:6;pointer-events:none;width:48px;height:48px;
  border:3px solid var(--acento);
}}
.corner-bl{{left:36px;bottom:36px;border-right:none;border-top:none;}}
.corner-br{{right:36px;bottom:36px;border-left:none;border-top:none;}}
.tag{{
  display:inline-block;background:rgba(0,255,178,.18);color:#067a56;
  font-family:var(--mono);font-size:20px;font-weight:600;letter-spacing:2px;
  padding:12px 22px;border-radius:999px;border:1.5px solid var(--acento);
}}
.tag-dark{{
  display:inline-block;background:var(--acento);color:#04130b;
  font-family:var(--mono);font-size:18px;font-weight:700;letter-spacing:1px;
  padding:12px 18px;border-radius:12px;
}}
.h1{{
  margin:0;font-family:var(--title);font-weight:900;font-size:92px;line-height:0.92;
  letter-spacing:-1px;color:var(--ink);text-transform:none;
  -webkit-text-stroke:2px var(--ink);paint-order:stroke fill;
}}
.h1.slant{{font-style:italic;transform:skewX(-7deg);transform-origin:left center;}}
.h1 .bar{{
  display:inline-block;background:var(--acento);color:#04130b;
  -webkit-text-stroke:0;padding:8px 18px 12px;margin-top:8px;
}}
.h1 .gr{{color:var(--acento);-webkit-text-stroke:2px var(--acento);}}
.body{{
  font-family:var(--cond);font-size:34px;line-height:1.35;color:#2a322e;
}}
.body b{{color:var(--acento);font-weight:700;}}
.card{{
  background:#fff;border-radius:28px;
  box-shadow:0 18px 40px rgba(10,10,10,.08);
  border:1.5px solid rgba(10,10,10,.06);
}}
.chatbar{{
  display:flex;align-items:center;gap:12px;padding:14px 16px;
  background:#F3F5F4;border-radius:18px;border:1.5px solid rgba(10,10,10,.08);
}}
.chatbar .plus{{
  width:36px;height:36px;border-radius:50%;background:#fff;border:1.5px solid #ddd;
  display:grid;place-items:center;font-size:22px;color:#666;
}}
.chatbar .txt{{
  flex:1;font-family:var(--cond);font-size:24px;color:#3a4340;text-align:left;
}}
.chatbar .meta{{
  font-family:var(--mono);font-size:14px;color:#6a736e;white-space:nowrap;
}}
.chatbar .send{{
  width:44px;height:44px;border-radius:12px;background:var(--acento);color:#04130b;
  display:grid;place-items:center;font-size:22px;font-weight:800;
}}
.star{{
  position:absolute;color:var(--acento);font-size:48px;line-height:1;
  text-shadow:0 0 18px rgba(0,255,178,.45);
}}
.progress{{
  position:absolute;left:64px;bottom:140px;width:220px;height:10px;
  background:rgba(0,255,178,.2);border-radius:8px;overflow:hidden;z-index:8;
}}
.progress span{{display:block;height:100%;width:28%;background:var(--acento);}}
.bubble{{
  display:inline-block;background:rgba(0,255,178,.12);border:2px solid var(--acento);
  border-radius:22px;padding:18px 22px;font-family:var(--cond);font-size:28px;
  color:var(--ink);box-shadow:0 0 20px rgba(0,255,178,.12);max-width:920px;
}}
.quote{{
  background:#fff;border-radius:20px;padding:28px 30px;margin-bottom:18px;
  border:1.5px solid rgba(10,10,10,.08);box-shadow:0 10px 28px rgba(10,10,10,.06);
  font-family:var(--cond);font-size:32px;font-style:italic;color:var(--ink);
}}
.item{{
  background:#fff;border-radius:20px;padding:28px 30px;margin-bottom:16px;
  border:1.5px solid rgba(10,10,10,.08);box-shadow:0 10px 28px rgba(10,10,10,.06);
  font-family:var(--pop);font-weight:800;font-size:32px;color:var(--ink);
}}
.dash{{
  background:#111;border-radius:20px;padding:22px;color:#fff;
  box-shadow:0 20px 48px rgba(0,0,0,.25);border:1px solid #2a2a2a;
}}
.dash h3{{font-family:var(--pop);font-size:28px;margin:0 0 16px;}}
.dash .metrics{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:14px;}}
.dash .m{{
  background:#1a1a1a;border-radius:12px;padding:12px;font-family:var(--mono);font-size:13px;color:#9aa39c;
}}
.dash .m b{{display:block;font-family:var(--pop);font-size:22px;color:#fff;margin-top:6px;}}
.dash .m .win{{color:var(--acento);}}
.dash table{{width:100%;border-collapse:collapse;font-family:var(--mono);font-size:12px;}}
.dash th{{text-align:left;color:#6a736e;padding:8px 4px;border-bottom:1px solid #2a2a2a;}}
.dash td{{padding:8px 4px;border-bottom:1px solid #222;color:#ddd;}}
.pill{{
  display:inline-block;padding:4px 10px;border-radius:999px;font-size:11px;font-weight:700;
}}
.prompt-box{{
  background:#fff;border-radius:24px;padding:28px 28px 18px;
  box-shadow:0 16px 40px rgba(10,10,10,.08);border:1.5px solid rgba(10,10,10,.07);
}}
.prompt-box pre{{
  margin:0 0 18px;white-space:pre-wrap;font-family:var(--mono);font-size:18px;
  line-height:1.45;color:#1a221f;max-height:620px;overflow:hidden;
}}
.line-accent{{
  width:160px;height:8px;background:var(--acento);border-radius:6px;
  box-shadow:0 0 16px rgba(0,255,178,.4);margin:18px 0;
}}
"""


def wrap(idx: int, inner: str, swipe: bool = True) -> str:
    html = chrome(idx, inner, total=TOTAL, bridges=None, footer=False)
    extras = (
        '<span class="corner corner-bl"></span><span class="corner corner-br"></span>'
        '<div class="brand-tr">sebastian.stlabs.ar</div>'
        '<div class="foot">sebastian.stlabs.ar</div>'
    )
    if swipe and idx < TOTAL:
        extras = '<div class="swipe">deslizá →</div>' + extras
    return html.replace("</section>", extras + "</section>", 1)


def chat_bar(text: str) -> str:
    return f"""
<div class="chatbar">
  <div class="plus">+</div>
  <div class="txt">{text}</div>
  <div class="meta">Sonnet · Medium</div>
  <div class="send">↑</div>
</div>
"""


def slide_cover(s: dict) -> str:
    return wrap(
        1,
        f"""
<div style="position:absolute;left:0;right:0;top:120px;text-align:center;z-index:5;">
  <div class="tag">{s['tag']}</div>
</div>
<div class="card" style="position:absolute;left:72px;right:72px;top:230px;bottom:180px;padding:56px 48px 36px;z-index:5;">
  <h1 class="h1 slant" style="font-size:88px;color:var(--acento);-webkit-text-stroke:2px var(--acento);">
    {s['linea1']}<br>{s['linea2']}<br>{s['linea3']}
  </h1>
  <div class="star" style="right:70px;top:90px;">✦</div>
  <div class="star" style="right:120px;top:170px;font-size:28px;">✦</div>
  <div style="position:absolute;left:40px;right:40px;bottom:36px;">{chat_bar(s['chat'])}</div>
</div>
""",
    )


def slide_explain(s: dict) -> str:
    bullets = "".join(f"<div class='body' style='margin-top:18px;'>• {b}</div>" for b in s["bullets"])
    return wrap(
        2,
        f"""
<div style="padding:160px 72px 0;position:relative;z-index:5;">
  <h1 class="h1" style="font-size:78px;">
    {s['titulo_a']} <span class="gr">{s['titulo_b']}</span>
  </h1>
  <p class="body" style="margin-top:36px;font-size:38px;">{s['cuerpo']}</p>
  {bullets}
  <p class="body" style="margin-top:36px;font-weight:700;color:var(--ink);">{s['cierre']}</p>
</div>
<div class="progress"><span></span></div>
""",
    )


def slide_prompt(s: dict) -> str:
    prompt = s["prompt"].replace("<", "&lt;")
    return wrap(
        3,
        f"""
<div style="padding:130px 56px 0;position:relative;z-index:5;">
  <div style="background:rgba(0,255,178,.14);border:2px solid var(--acento);border-radius:18px;padding:22px 24px;
    font-family:var(--title);font-size:36px;line-height:1.15;color:var(--ink);font-style:italic;
    transform:skewX(-4deg);">
    {s['titulo']}
  </div>
  <div style="margin-top:18px;"><span class="tag-dark">✦ {s['badge']}</span></div>
  <div class="prompt-box" style="margin-top:22px;">
    <pre>{prompt}</pre>
    {chat_bar("Pegá el prompt y mandalo →")}
  </div>
</div>
""",
    )


def slide_result(s: dict) -> str:
    return wrap(
        4,
        f"""
<div style="padding:110px 56px 0;position:relative;z-index:5;">
  <div class="bubble">{s['bubble1']}</div>
  <div class="dash" style="margin-top:22px;">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <h3>Pipeline de Ventas</h3>
      <div style="background:#2b6cff;color:#fff;font-family:var(--mono);font-size:14px;padding:10px 14px;border-radius:10px;">+ Nueva Oportunidad</div>
    </div>
    <div class="metrics">
      <div class="m">TOTAL DE OPORTUNIDADES<b>5</b></div>
      <div class="m">VALOR TOTAL DEL PIPELINE<b>$625,000</b></div>
      <div class="m">VALOR GANADO<b class="win">$250,000</b></div>
    </div>
    <table>
      <tr><th>CLIENTE</th><th>EMPRESA</th><th>PRODUCTO</th><th>VALOR</th><th>ESTATUS</th></tr>
      <tr><td>Ana Torres</td><td>Grupo Delfin</td><td>IA</td><td>$180k</td><td><span class="pill" style="background:#ff8a3d;color:#111;">Negociación</span></td></tr>
      <tr><td>Luis Pérez</td><td>NovaTech</td><td>CRM</td><td>$95k</td><td><span class="pill" style="background:#f5d547;color:#111;">Propuesta</span></td></tr>
      <tr><td>María Gómez</td><td>Atlas</td><td>Agentes</td><td>$250k</td><td><span class="pill" style="background:#00FFB2;color:#04130b;">Ganado</span></td></tr>
      <tr><td>Diego Ruiz</td><td>Orbit</td><td>Ops</td><td>$60k</td><td><span class="pill" style="background:#4da3ff;color:#111;">Contactado</span></td></tr>
    </table>
  </div>
  <div class="bubble" style="margin-top:18px;">{s['bubble2']}</div>
  <div class="bubble" style="margin-top:12px;">{s['bubble3']}</div>
</div>
""",
    )


def slide_customize(s: dict) -> str:
    quotes = "".join(f'<div class="quote">“{q}”</div>' for q in s["quotes"])
    return wrap(
        5,
        f"""
<div style="padding:140px 64px 0;position:relative;z-index:5;">
  <div style="background:rgba(0,255,178,.14);border:2px solid var(--acento);border-radius:16px;padding:20px 22px;
    font-family:var(--mono);font-size:28px;font-weight:700;letter-spacing:1px;color:#067a56;">
    {s['titulo']}
  </div>
  <div style="margin-top:28px;">{quotes}</div>
  <div class="line-accent"></div>
  <div style="font-family:var(--cond);font-size:34px;font-weight:700;color:var(--acento);">{s['cierre']}</div>
</div>
""",
    )


def slide_benefits(s: dict) -> str:
    items = "".join(f'<div class="item">→ {it}</div>' for it in s["items"])
    return wrap(
        6,
        f"""
<div style="padding:150px 64px 0;position:relative;z-index:5;">
  <div style="background:rgba(0,255,178,.14);border:2px solid var(--acento);border-radius:22px;padding:28px 30px;
    font-family:var(--title);font-size:42px;line-height:1.15;color:var(--ink);font-style:italic;">
    {s['titulo']}
  </div>
  <div style="margin-top:34px;">{items}</div>
</div>
""",
    )


def slide_cta(s: dict) -> str:
    return wrap(
        7,
        f"""
<div style="position:absolute;left:0;right:0;top:120px;text-align:center;z-index:5;">
  <div class="tag">{s['badge']}</div>
</div>
<div class="card" style="position:absolute;left:72px;right:72px;top:230px;bottom:170px;padding:48px 44px 32px;z-index:5;">
  <h1 class="h1 slant" style="font-size:52px;line-height:1.05;color:var(--acento);-webkit-text-stroke:1.5px var(--acento);">
    {s['titulo']}
  </h1>
  <p class="body" style="margin-top:22px;font-size:32px;color:#3a4340;">{s['sub']}</p>
  <div style="margin-top:28px;padding:22px 24px;border-radius:18px;background:#0A0A0A;color:#fff;
    font-family:var(--cond);font-size:30px;line-height:1.35;border:2px solid var(--acento);
    box-shadow:0 0 28px rgba(0,255,178,.25);">
    <span style="color:var(--acento);font-family:var(--mono);font-size:16px;letter-spacing:1px;">CONCLUSIÓN</span><br>
    {s['conclusion']}
  </div>
  <div style="position:absolute;left:36px;right:36px;bottom:28px;">{chat_bar("Comentá AGENTE y te ayudo")}</div>
</div>
""",
        swipe=False,
    )


def main():
    data = CONTENT["slides_copy"]
    slides = [
        slide_cover(data[0]),
        slide_explain(data[1]),
        slide_prompt(data[2]),
        slide_result(data[3]),
        slide_customize(data[4]),
        slide_benefits(data[5]),
        slide_cta(data[6]),
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
    out = package(BUILD, "STLabs-Artifacts-Tracker", meta=meta)
    print("Package:", out)

    KEEP = {".ttf", ".otf", ".woff", ".woff2"}
    KEEP_NAMES = {"befonts-license.txt", "impact-font.zip", "linea-grafica-stlabs.md", "linea-grafica-stlabs.txt"}
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    for p in list(WORD_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() not in KEEP and p.name.lower() not in KEEP_NAMES:
            p.unlink()
    for fname in ("impact.ttf", "Impact.ttf", "impacted.ttf", "unicodeimpact.ttf", "Anton-Regular.ttf"):
        src = REPO / "fonts" / fname
        if src.exists():
            shutil.copy2(src, WORD_DIR / fname)

    for name in (
        "STLabs-Artifacts-Tracker.html",
        "STLabs-Artifacts-Tracker.zip",
        "_preview-tira.png",
        "manifest.json",
        *[f"slide-{i:02d}.png" for i in range(1, TOTAL + 1)],
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    shutil.copy2(BUILD / "content.json", WORD_DIR / "content.json")
    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Font manifesto — Artifacts Tracker

| Font | Role |
|---|---|
| Impact / Anton | Titles display |
| Poppins 800 | Feature items |
| Barlow Condensed | Body |
| IBM Plex Mono | Tags, prompt, firma, UI chat |

Accent: `#00FFB2`. Background: white + reticula_fina. Family: dossier_editorial.
Conclusion slide 7 only: first-person Sebastián pitch.
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""STLabs — Artifacts Tracker de Ventas (Claude)
Clone manuelnocode → sebastian.stlabs.ar
Slides: {TOTAL} · Keyword: {KEYWORD}
Accent #00FFB2 · Fondo blanco · Solo conclusión final reescrita en 1ª persona
""",
        encoding="utf-8",
    )
    print("Word/:", WORD_DIR)


if __name__ == "__main__":
    main()
