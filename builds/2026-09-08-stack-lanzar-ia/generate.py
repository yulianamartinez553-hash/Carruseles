# -*- coding: utf-8 -*-
"""Carrusel STLabs — El stack para lanzar aplicaciones con IA.
Clon de referencia: logos/ilustraciones recortados exactamente.
Fondo negro + retícula fina · guía editorial.
"""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
ASSETS = BUILD / "assets"
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package

DATA = json.loads((BUILD / "index.json").read_text(encoding="utf-8"))
TOOLS = DATA["tools"]
CTA = DATA["cta"]
TOTAL = int(DATA["slides"])


def img_b64(name: str) -> str:
    raw = (ASSETS / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(raw).decode("ascii")


EXTRA_CSS = """
.slide{background:#0A0A0A !important;}
.slide::before{
  content:"";position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(255,255,255,.016) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.016) 1px, transparent 1px);
  background-size:60px 60px;
  mix-blend-mode:overlay;
}
.slide::after{display:none !important;}

/* PORTADA */
.s-cover{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 align-items:center;padding:90px 56px 120px;text-align:center;}
.cover-title{font-family:var(--disp);font-size:92px;line-height:.92;letter-spacing:.02em;
 color:var(--blanco);text-transform:uppercase;max-width:980px;}
.cover-title .gr{color:var(--verde);}
.cover-under{display:block;width:280px;height:6px;background:var(--verde);margin:14px auto 0;
 border-radius:3px;transform:rotate(-1.2deg);}
.cover-hero{margin-top:28px;width:920px;max-width:100%;height:auto;object-fit:contain;}

/* TOOL */
.s-tool{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 align-items:center;padding:78px 64px 120px;text-align:center;}
.tool-name{font-family:var(--pop);font-weight:800;font-size:54px;line-height:1.05;
 color:var(--blanco);letter-spacing:-.01em;text-transform:uppercase;}
.tool-tag{margin-top:8px;font-family:var(--pop);font-weight:800;font-size:42px;line-height:1.1;
 color:var(--verde);text-transform:uppercase;letter-spacing:-.01em;}
.tool-under{width:420px;max-width:90%;height:5px;background:var(--verde);margin:12px auto 0;
 border-radius:3px;transform:rotate(-0.8deg);opacity:.95;}
.tool-under.d{margin-top:4px;width:380px;opacity:.7;transform:rotate(0.6deg);}
.tool-logo{margin-top:36px;width:280px;height:280px;object-fit:contain;display:block;}
.tool-box{margin-top:36px;width:860px;max-width:100%;border:2px solid var(--verde);
 border-radius:18px;padding:28px 36px;text-align:left;background:rgba(0,255,178,.03);}
.tool-box li{font-family:var(--mono);font-size:28px;line-height:1.55;color:var(--blanco);
 list-style:none;}
.tool-box li::before{content:"- ";color:var(--verde);}
.tool-note{margin-top:28px;align-self:flex-start;margin-left:40px;max-width:720px;
 font-family:var(--serif);font-style:italic;font-size:28px;line-height:1.25;color:var(--verde);
 text-align:left;position:relative;}
.tool-note::after{content:"";position:absolute;right:-70px;top:50%;width:54px;height:28px;
 background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 54 28' fill='none'%3E%3Cpath d='M2 20 C18 4, 36 4, 48 14' stroke='%2300FFB2' stroke-width='2.2' stroke-linecap='round'/%3E%3Cpath d='M42 8 L50 14 L42 20' stroke='%2300FFB2' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;}

/* GRID */
.s-grid{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 align-items:center;padding:90px 56px 120px;text-align:center;}
.grid-title{font-family:var(--pop);font-weight:800;font-size:58px;line-height:1.05;
 color:var(--blanco);text-transform:uppercase;}
.grid-title .gr{color:var(--verde);}
.grid-under{width:460px;height:5px;background:var(--verde);margin:14px auto 0;border-radius:3px;}
.grid-under.d{margin-top:5px;width:420px;opacity:.75;}
.grid-frame{margin-top:40px;width:900px;max-width:100%;border:2px solid var(--verde);
 border-radius:22px;padding:36px 28px;background:rgba(0,255,178,.03);}
.grid-img{width:100%;height:auto;display:block;}
.grid-note{margin-top:28px;font-family:var(--serif);font-style:italic;font-size:28px;
 color:var(--verde);}

/* CTA */
.s-cta{position:relative;z-index:5;height:100%;display:flex;flex-direction:column;
 align-items:center;justify-content:center;padding:80px 64px 120px;text-align:center;}
.cta-kicker{font-family:var(--pop);font-weight:800;font-size:52px;color:var(--blanco);
 text-transform:uppercase;letter-spacing:.02em;}
.cta-word{font-family:var(--disp);font-size:120px;line-height:.9;color:var(--verde);
 letter-spacing:.04em;margin-top:6px;}
.cta-under{width:360px;height:6px;background:var(--verde);margin:10px auto 0;border-radius:3px;}
.cta-under.d{margin-top:5px;width:320px;opacity:.7;}
.cta-ico{margin-top:36px;width:220px;height:auto;}
.cta-box{margin-top:36px;width:880px;max-width:100%;border:2px solid var(--verde);
 border-radius:18px;padding:28px 32px;font-family:var(--cond);font-size:30px;line-height:1.35;
 color:var(--blanco);background:rgba(0,255,178,.03);}
.cta-arrow{margin-top:28px;width:36px;height:56px;
 background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 36 56' fill='none'%3E%3Cpath d='M18 4 V44' stroke='%2300FFB2' stroke-width='3' stroke-linecap='round'/%3E%3Cpath d='M8 34 L18 48 L28 34' stroke='%2300FFB2' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat;}
"""


def _wrap(idx: int, inner: str) -> str:
    return chrome(idx, inner, total=TOTAL, bridges=None, footer=True, counter=False)


def slide_cover() -> str:
    src = img_b64("cover-hero.png")
    inner = f"""
<div class="s-cover">
  <h1 class="cover-title"><span class="gr">EL STACK</span><br>PARA LANZAR<br>APLICACIONES<br><span class="gr">CON IA</span></h1>
  <span class="cover-under"></span>
  <img class="cover-hero" src="{src}" alt=""/>
</div>"""
    return _wrap(1, inner)


def slide_tool(t: dict, idx: int) -> str:
    bullets = "".join(f"<li>{b}</li>" for b in t["bullets"])
    src = img_b64(t["logo"])
    inner = f"""
<div class="s-tool">
  <div class="tool-name">{t['n']}. {t['name']}</div>
  <div class="tool-tag">{t['tag']}</div>
  <div class="tool-under"></div>
  <div class="tool-under d"></div>
  <img class="tool-logo" src="{src}" alt=""/>
  <ul class="tool-box">{bullets}</ul>
  <div class="tool-note">{t['note']}</div>
</div>"""
    return _wrap(idx, inner)


def slide_grid() -> str:
    src = img_b64("grid-logos.png")
    inner = f"""
<div class="s-grid">
  <h2 class="grid-title">UNA SOLA PERSONA<br><span class="gr">LANZA TODO ESTO</span></h2>
  <div class="grid-under"></div>
  <div class="grid-under d"></div>
  <div class="grid-frame"><img class="grid-img" src="{src}" alt=""/></div>
  <p class="grid-note">sin equipo, sin inversión, sin permiso</p>
</div>"""
    return _wrap(11, inner)


def slide_cta() -> str:
    src = img_b64("cta-bubble.png")
    inner = f"""
<div class="s-cta">
  <div class="cta-kicker">COMENTÁ</div>
  <div class="cta-word">{CTA}</div>
  <div class="cta-under"></div>
  <div class="cta-under d"></div>
  <img class="cta-ico" src="{src}" alt=""/>
  <div class="cta-box">y te paso la guía: cómo conectar cada herramienta a Claude Code para manejarlas todas desde un solo lugar, cuáles no se pueden y en qué orden hacerlo.</div>
  <div class="cta-arrow" aria-hidden="true"></div>
</div>"""
    return _wrap(TOTAL, inner)


def build_slides() -> list[str]:
    slides = [slide_cover()]
    for i, t in enumerate(TOOLS, start=2):
        slides.append(slide_tool(t, i))
    slides.append(slide_grid())
    slides.append(slide_cta())
    return slides


def main():
    slides = build_slides()
    assert len(slides) == TOTAL, (len(slides), TOTAL)
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
    out = package(BUILD, "STLabs-Stack-Lanzar-IA", meta=meta)
    caption = (
        "El stack para lanzar aplicaciones con IA.\n\n"
        "Una sola persona. Sin equipo. Sin permiso.\n"
        "Reddit → Typeform → Claude Code → Vercel → Stripe → Resend → Loom → Meta → PostHog.\n\n"
        "Deslizá. Guardá. Aplicá.\n\n"
        f"Comentá {CTA} y te mando la guía de conexión.\n\n"
        "#ia #lanzamiento #productividad #stlabs #automatizacion"
    )
    (out / "caption.txt").write_text(caption, encoding="utf-8")
    (out / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Stack lanzar IA

| Familia | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Bebas Neue | 400 | Título portada / keyword CTA | `/workspace/fonts/BebasNeue-Regular.ttf` | `@font-face` base64 vía `stlabs_kit.embedded_fonts_css()` |
| Poppins | 800 | Títulos de herramienta / grid | `/workspace/fonts/Poppins-Bold.ttf` | idem |
| Barlow Condensed | 400–700 | Cuerpo CTA | `/workspace/fonts/BarlowCondensed-*.ttf` | idem |
| IBM Plex Mono | 400–600 | Bullets, firma | `/workspace/fonts/IBMPlexMono-*.ttf` | idem |
| Lora | Italic | Notas editoriales | `/workspace/fonts/Lora-Italic-Variable.ttf` | idem |

Ilustraciones y logos: recorte directo de las referencias (PIL), fondo crema → transparencia.
""",
        encoding="utf-8",
    )
    print("Package →", out)
    return out


if __name__ == "__main__":
    main()
