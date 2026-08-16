# -*- coding: utf-8 -*-
"""Carrusel 4 slides — frases impacto + continuidad geométrica
Fondo: piedra_roca · Familia: manifiesto · Modo: blanco
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


def slide_01():
    return (
        '<section class="slide" data-id="01"><div class="tex"></div>'
        + seam_nums(1) + geo_circle_out() + geo_arrow_out()
        + '<div class="mid">'
        '<p class="kicker">La trampa del dueño</p>'
        '<h1 class="display">SI TODO<br>DEPENDE<br>DE <span class="ac">VOS</span></h1>'
        '<p class="punch">no tenés empresa.<br><span class="ac xl">Tenés un puesto.</span></p>'
        '</div>' + foot() + '</section>'
    )


def slide_02():
    return (
        '<section class="slide" data-id="02"><div class="tex"></div>'
        + seam_nums(2) + geo_circle_in() + geo_arrow_in() + geo_ring_out() + geo_bar_out()
        + '<div class="mid mid-r">'
        '<h1 class="display">ATENDER<br>TODO<br><span class="sm">NO ES</span><br><span class="ac">LIDERAR</span></h1>'
        '<p class="punch soft">Es tapar agujeros<br>con tu tiempo.</p>'
        '</div>' + foot() + '</section>'
    )


def slide_03():
    return (
        '<section class="slide" data-id="03"><div class="tex"></div>'
        + seam_nums(3) + geo_ring_in() + geo_bar_in() + geo_circle_out()
        + '<div class="mid">'
        '<h1 class="display">EL CONTROL<br><span class="sm">NO ESTÁ</span><br><span class="ac">EN MIRAR</span></h1>'
        '<p class="punch">Se <span class="ac xl">diseña.</span></p>'
        '<p class="sub">Procesos que corrigen solos<br>antes de llegar a vos.</p>'
        '</div>' + foot() + '</section>'
    )


def slide_04():
    return (
        '<section class="slide" data-id="04"><div class="tex"></div>'
        + seam_nums(4) + geo_circle_in() + geo_arrow_in()
        + '<div class="mid mid-cta">'
        '<p class="cta-pre">Comentá</p>'
        '<h1 class="cta-kw">SISTEMA</h1>'
        '<p class="cta-mid">y te mando el mapa<br>para que tu empresa<br>'
        '<span class="ac">ande sin vos encima.</span></p>'
        '</div>' + foot(arrow=False) + '</section>'
    )


def build_css():
    f = str(FONTS)
    return f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{f}/BebasNeue-Regular.ttf') format('truetype'); font-weight:400; }}
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Poppins'; src:url('file://{f}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'Lora'; src:url('file://{f}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{f}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}

* {{ box-sizing:border-box; margin:0; padding:0; -webkit-font-smoothing:antialiased; }}
html, body {{ background:#ddd; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1350px; overflow:hidden;
  background:#F2F2F2; color:#0A0A0A;
}}
.tex {{
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background:
    radial-gradient(ellipse 90% 70% at 80% 18%, rgba(0,255,178,.08), transparent 55%),
    radial-gradient(ellipse 70% 55% at 8% 88%, rgba(0,0,0,.045), transparent 50%),
    repeating-linear-gradient(0deg, transparent, transparent 3px, rgba(0,0,0,.02) 3px, rgba(0,0,0,.02) 4px),
    repeating-linear-gradient(90deg, transparent, transparent 3px, rgba(0,0,0,.015) 3px, rgba(0,0,0,.015) 4px);
}}

.seam-num {{
  position:absolute; z-index:2; pointer-events:none;
  font-family:'Bebas Neue', sans-serif; font-weight:400;
  font-size:280px; line-height:.8; letter-spacing:-.02em;
  color:rgba(10,10,10,.12);
  width:340px; text-align:center;
}}
.seam-out {{ left:900px; }}
.seam-in  {{ left:-180px; }}
.seam-solo {{ left:auto; right:40px; color:rgba(10,10,10,.18); font-size:220px; }}
.seam-top {{ top:28px; }}
.seam-bot {{ bottom:180px; }}

.geo {{ position:absolute; z-index:1; pointer-events:none; }}
.geo-circle {{
  width:380px; height:380px; border-radius:50%;
  border:16px solid #00FFB2; background:transparent;
}}
.geo-circle.geo-out {{ right:-190px; top:58%; transform:translateY(-50%); }}
.geo-circle.geo-in  {{ left:-190px; top:58%; transform:translateY(-50%); }}

.geo-ring {{
  width:560px; height:560px; border-radius:50%;
  border:3px solid rgba(10,10,10,.14); background:transparent;
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
.mid-cta {{ justify-content:center; }}

.kicker {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:26px; color:#00FFB2; margin-bottom:18px;
}}
.display {{
  font-family:'Bebas Neue', sans-serif; font-weight:400;
  font-size:128px; line-height:.88; letter-spacing:.01em;
  color:#0A0A0A; text-align:left;
}}
.display .sm {{
  font-size:.48em; letter-spacing:.04em;
  font-family:'Poppins', sans-serif; font-weight:800; color:#3a3a3a;
}}
.ac {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  color:#00FFB2;
}}
.xl {{ font-size:1.15em; }}

.punch {{
  margin-top:36px; font-family:'Poppins', sans-serif; font-weight:800;
  font-size:42px; line-height:1.15; color:#0A0A0A;
}}
.punch.soft {{ color:#3a3a3a; font-size:36px; }}
.sub {{
  margin-top:28px; font-family:'Poppins', sans-serif; font-weight:700;
  font-size:28px; line-height:1.35; color:#5a5a5a;
}}

.cta-pre {{
  font-family:'Poppins', sans-serif; font-weight:800;
  font-size:40px; color:#0A0A0A;
}}
.cta-kw {{
  font-family:'Bebas Neue', sans-serif;
  font-size:148px; line-height:.9; letter-spacing:.03em;
  color:#00FFB2; margin:4px 0 20px;
}}
.cta-mid {{
  font-family:'Poppins', sans-serif; font-weight:700;
  font-size:34px; line-height:1.3; color:#0A0A0A; max-width:720px;
}}
"""


def main():
    slides = [slide_01(), slide_02(), slide_03(), slide_04()]
    css = build_css()
    html = (
        "<!DOCTYPE html>\n<html lang=\"es\"><head><meta charset=\"UTF-8\">\n"
        "<title>Si todo depende de vos — STLabs</title>\n"
        f"<style>{css}</style></head>\n"
        f"<body><div class=\"sheet\">{''.join(slides)}</div></body></html>"
    )
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Si todo depende de vos, no tenés empresa",
        "slides": 4,
        "fondo": "piedra_roca",
        "familia_visual": "manifiesto",
        "origen": "original",
        "keyword_portada": "SISTEMA",
        "modo": "blanco",
        "id": "2026-08-16-frases-continuidad",
        "fecha": "2026-08-16",
        "notas": "4 slides. Continuidad: círculos/flechas/barras partidos + números seam. Bebas display.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(slides)} slides · manifiesto blanco · continuidad geométrica")


if __name__ == "__main__":
    main()
