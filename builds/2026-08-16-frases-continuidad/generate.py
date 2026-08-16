# -*- coding: utf-8 -*-
"""Carrusel 4 slides — vende un agente/sistema para la empresa
Fondo: piedra_roca · Familia: manifiesto · Modo: negro
Títulos: Poppins ExtraBold (grueso) · Acentos: Lora italic
"""
from pathlib import Path
import json

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
TOTAL = 4


def seam_nums(n: int, total: int = TOTAL) -> str:
    parts = []
    if n > 1:
        prev = n - 1
        pos = "top" if prev % 2 == 1 else "bot"
        parts.append(
            f'<div class="seam-num seam-in seam-{pos}" aria-hidden="true">{prev:02d}</div>'
        )
    if n < total:
        pos = "top" if n % 2 == 1 else "bot"
        parts.append(
            f'<div class="seam-num seam-out seam-{pos}" aria-hidden="true">{n:02d}</div>'
        )
    else:
        parts.append(
            f'<div class="seam-num seam-solo seam-bot" aria-hidden="true">{n:02d}</div>'
        )
    return "\n".join(parts)


def foot(arrow: bool = True) -> str:
    arr = ""
    if arrow:
        arr = (
            '<div class="nav-arrow" aria-hidden="true">'
            '<svg viewBox="0 0 40 24" width="34" height="20">'
            '<path d="M2 12 H30 M22 4 L34 12 L22 20" fill="none" stroke="#00FFB2" '
            'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
        )
    return f'<div class="firma">sebastian.stlabs.ar</div>{arr}'


def geo_circle_out():
    return '<div class="geo geo-circle geo-out" aria-hidden="true"></div>'


def geo_circle_in():
    return '<div class="geo geo-circle geo-in" aria-hidden="true"></div>'


def geo_ring_out():
    return '<div class="geo geo-ring geo-out-mid" aria-hidden="true"></div>'


def geo_ring_in():
    return '<div class="geo geo-ring geo-in-mid" aria-hidden="true"></div>'


def geo_arrow_out():
    return (
        '<div class="geo geo-arrow geo-arrow-out" aria-hidden="true">'
        '<svg viewBox="0 0 200 80" width="200" height="80">'
        '<path d="M8 40 H130 M100 12 L168 40 L100 68" fill="none" stroke="#00FFB2" '
        'stroke-width="14" stroke-linecap="square" stroke-linejoin="miter"/></svg></div>'
    )


def geo_arrow_in():
    return (
        '<div class="geo geo-arrow geo-arrow-in" aria-hidden="true">'
        '<svg viewBox="0 0 200 80" width="200" height="80">'
        '<path d="M-40 40 H90 M60 12 L128 40 L60 68" fill="none" stroke="#00FFB2" '
        'stroke-width="14" stroke-linecap="square" stroke-linejoin="miter"/></svg></div>'
    )


def geo_bar_out():
    return '<div class="geo geo-bar geo-bar-out" aria-hidden="true"></div>'


def geo_bar_in():
    return '<div class="geo geo-bar geo-bar-in" aria-hidden="true"></div>'


def stain_out(pos: str) -> str:
    """Mitad izquierda de mancha — sale por la derecha (continúa en la siguiente)."""
    return f'<div class="stain stain-out stain-{pos}" aria-hidden="true"></div>'


def stain_in(pos: str) -> str:
    """Mitad derecha de mancha — entra por la izquierda."""
    return f'<div class="stain stain-in stain-{pos}" aria-hidden="true"></div>'


def slide_01():
    return (
        '<section class="slide" data-id="01"><div class="tex"></div>'
        + stain_out('hi')
        + seam_nums(1) + geo_circle_out() + geo_arrow_out()
        + '<div class="mid">'
        '<p class="kicker">Para dueños que no dan abasto</p>'
        '<h1 class="display">TU EMPRESA<br>NECESITA<br>UN <span class="ac">AGENTE</span></h1>'
        '<p class="punch">No otra persona.<br><span class="ac xl">Uno que te ayude a armar procesos.</span></p>'
        '</div>' + foot() + '</section>'
    )


def slide_02():
    return (
        '<section class="slide" data-id="02"><div class="tex"></div>'
        + stain_in('hi') + stain_out('lo')
        + seam_nums(2) + geo_circle_in() + geo_arrow_in() + geo_ring_out() + geo_bar_out()
        + '<div class="mid mid-r">'
        '<h1 class="display">TE AYUDA A<br><span class="sm">ARMAR</span><br><span class="ac">PROCESOS</span></h1>'
        '<p class="punch soft">Diseñá. Documentá. Delegá.<br>'
        '<span class="ac">Paso a paso, con el agente.</span></p>'
        '</div>' + foot() + '</section>'
    )


def slide_03():
    return (
        '<section class="slide" data-id="03"><div class="tex"></div>'
        + stain_in('lo') + stain_out('mid')
        + seam_nums(3) + geo_ring_in() + geo_bar_in()
        + '<div class="geo geo-circle geo-out geo-lo" aria-hidden="true"></div>'
        + '<div class="mid">'
        '<h1 class="display">PROCESOS<br><span class="sm">QUE ANDEN</span><br><span class="ac">SIN VOS</span></h1>'
        '<p class="punch">Claros. Documentados.<br>Con responsables.</p>'
        '<p class="sub">El agente te ayuda a armarlos<br>para que la empresa no dependa de vos.</p>'
        '</div>' + foot() + '</section>'
    )


def slide_04():
    return (
        '<section class="slide" data-id="04"><div class="tex"></div>'
        + stain_in('mid')
        + seam_nums(4)
        + '<div class="geo geo-circle geo-in geo-lo" aria-hidden="true"></div>'
        + geo_arrow_in()
        + '<div class="mid mid-cta">'
        '<p class="cta-pre">Comentá</p>'
        '<h1 class="cta-kw">PROCESOS</h1>'
        '<p class="cta-mid">y te muestro cómo un agente<br>te ayuda a armar los procesos<br>'
        '<span class="ac">de tu empresa.</span></p>'
        '</div>' + foot(arrow=False) + '</section>'
    )


def build_css():
    f = str(FONTS)
    return f"""
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'Lora'; src:url('file://{f}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}

* {{ box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1350px; overflow:hidden;
  background:#0A0A0A; color:#F2F2F2;
}}
.tex {{
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background: transparent;
}}
.tex::before,
.tex::after {{
  content:''; position:absolute; inset:0; pointer-events:none;
  background-image:
    linear-gradient(rgba(0,255,178,.38) 2px, transparent 2px),
    linear-gradient(90deg, rgba(0,255,178,.38) 2px, transparent 2px);
  background-size:40px 40px;
}}
/* Cuadrícula más grande y notoria — esquina superior derecha */
.tex::before {{
  -webkit-mask-image: radial-gradient(ellipse 72% 58% at 100% 0%, #000 30%, transparent 82%);
  mask-image: radial-gradient(ellipse 72% 58% at 100% 0%, #000 30%, transparent 82%);
}}
/* Cuadrícula más grande y notoria — esquina inferior izquierda */
.tex::after {{
  -webkit-mask-image: radial-gradient(ellipse 72% 58% at 0% 100%, #000 30%, transparent 82%);
  mask-image: radial-gradient(ellipse 72% 58% at 0% 100%, #000 30%, transparent 82%);
}}

/* Manchas verdes grandes y continuas entre slides */
.stain {{
  position:absolute; z-index:0; pointer-events:none;
  width:820px; height:820px; border-radius:50%;
  background: radial-gradient(circle at 50% 50%,
    rgba(0,255,178,.55) 0%,
    rgba(0,255,178,.34) 28%,
    rgba(0,255,178,.16) 48%,
    rgba(0,255,178,.06) 62%,
    transparent 74%);
}}
.stain-out {{ right:-410px; }}
.stain-in  {{ left:-410px; }}
.stain-hi  {{ top:-40px; }}
.stain-lo  {{ bottom:-20px; }}
.stain-mid {{ top:28%; }}

.seam-num {{
  position:absolute; z-index:2; pointer-events:none;
  font-family:'Poppins', sans-serif; font-weight:800;
  font-size:260px; line-height:.8; letter-spacing:-.04em;
  color:rgba(0,255,178,.18);
  width:340px; text-align:center;
}}
.seam-out {{ left:900px; }}
.seam-in  {{ left:-180px; }}
.seam-solo {{ left:auto; right:40px; color:rgba(0,255,178,.28); font-size:200px; }}
.seam-top {{ top:28px; }}
.seam-bot {{ bottom:180px; }}

.geo {{ position:absolute; z-index:1; pointer-events:none; }}
.geo-circle {{
  width:380px; height:380px; border-radius:50%;
  border:16px solid #00FFB2; background:transparent;
}}
.geo-circle.geo-out {{ right:-190px; top:58%; transform:translateY(-50%); }}
.geo-circle.geo-in  {{ left:-190px; top:58%; transform:translateY(-50%); }}
/* Círculo bajo en costura 03↔04: no tapa el CTA */
.geo-circle.geo-lo {{
  top:auto; bottom:140px; transform:none;
  width:300px; height:300px;
}}
.geo-circle.geo-out.geo-lo {{ right:-160px; }}
.geo-circle.geo-in.geo-lo {{ left:-160px; }}

.geo-ring {{
  width:560px; height:560px; border-radius:50%;
  border:3px solid rgba(0,255,178,.2); background:transparent;
}}
.geo-ring.geo-out-mid {{ right:-280px; bottom:120px; }}
.geo-ring.geo-in-mid  {{ left:-280px; bottom:120px; }}

.geo-arrow {{ z-index:3; }}
.geo-arrow-out {{ right:-40px; top:210px; }}
.geo-arrow-in  {{ left:-100px; top:210px; }}

.geo-bar {{ width:280px; height:18px; background:#00FFB2; }}
.geo-bar-out {{ right:-140px; bottom:380px; transform:rotate(-18deg); }}
.geo-bar-in  {{ left:-140px; bottom:380px; transform:rotate(-18deg); }}

.firma {{
  position:absolute; left:0; right:0; bottom:56px; text-align:center; z-index:6;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.14em; color:#00FFB2;
}}
.nav-arrow {{ position:absolute; right:64px; bottom:118px; z-index:6; }}

.mid {{
  position:absolute; left:72px; right:120px; top:160px; bottom:180px; z-index:4;
  display:flex; flex-direction:column; justify-content:center;
}}
.mid-r {{ align-items:flex-start; padding-left:168px; }}
.mid-cta {{ justify-content:center; padding-left:72px; }}

.kicker {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:26px; color:#00FFB2; margin-bottom:18px;
}}
.display {{
  font-family:'Poppins', sans-serif; font-weight:800;
  font-size:92px; line-height:.92; letter-spacing:-.035em;
  color:#F2F2F2; text-align:left;
}}
.display .sm {{
  font-size:.55em; letter-spacing:-.02em;
  font-weight:800; color:#9aa39c;
}}
.ac {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:700;
  color:#00FFB2;
}}
.xl {{ font-size:1.12em; }}

.punch {{
  margin-top:32px; font-family:'Poppins', sans-serif; font-weight:800;
  font-size:40px; line-height:1.15; color:#F2F2F2;
}}
.punch.soft {{ color:#c5cdc6; font-size:34px; }}
.sub {{
  margin-top:24px; font-family:'Poppins', sans-serif; font-weight:700;
  font-size:26px; line-height:1.35; color:#9aa39c;
}}

.cta-pre {{
  font-family:'Poppins', sans-serif; font-weight:800;
  font-size:38px; color:#F2F2F2;
}}
.cta-kw {{
  font-family:'Poppins', sans-serif; font-weight:800;
  font-size:96px; line-height:.9; letter-spacing:-.03em;
  color:#00FFB2; margin:4px 0 18px;
}}
.cta-mid {{
  font-family:'Poppins', sans-serif; font-weight:700;
  font-size:32px; line-height:1.3; color:#F2F2F2; max-width:720px;
}}
"""


def main():
    slides = [slide_01(), slide_02(), slide_03(), slide_04()]
    css = build_css()
    html = (
        "<!DOCTYPE html>\n<html lang=\"es\"><head><meta charset=\"UTF-8\">\n"
        "<title>Tu empresa necesita un agente — STLabs</title>\n"
        f"<style>{css}</style></head>\n"
        f"<body><div class=\"sheet\">{''.join(slides)}</div></body></html>"
    )
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Un agente que te ayuda a armar procesos",
        "slides": 4,
        "fondo": "piedra_roca",
        "familia_visual": "manifiesto",
        "origen": "original",
        "keyword_portada": "PROCESOS",
        "modo": "negro",
        "id": "2026-08-16-frases-continuidad",
        "fecha": "2026-08-16",
        "notas": "Agente = armar procesos. Prohibido pitch de leads. Círculo CTA abajo.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(slides)} slides · agente arma procesos")


if __name__ == "__main__":
    main()
