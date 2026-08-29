# -*- coding: utf-8 -*-
"""Carrusel STLabs — Cómo construí Turbo (10 slides, manifiesto/lino, blueprint)."""
from __future__ import annotations

import json
from pathlib import Path

from diagrams import DIAGRAM_CSS, diagram

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
O = "#C9562F"
BG = "#EDE8DC"
TX = "#1C1814"
GY = "#6E6258"
BD = "#B8A898"
TOTAL = 10
SERIES = "SISTEMA TURBO · LA CONSTRUCCIÓN EN 4 PASOS"
NAV = ["RECIBE", "DIVIDE", "ASIGNA", "MEJORA"]


def b64(p: Path) -> str:
    import base64

    return base64.b64encode(p.read_bytes()).decode()


def font_css() -> str:
    faces = [
        ("Impact", "Impact.ttf", 400, "normal"),
        ("Anton", "Anton-Regular.ttf", 400, "normal"),
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
        ("Lora", "Lora-Italic-Variable.ttf", "400 700", "italic"),
    ]
    out = []
    for fam, fn, w, st in faces:
        fp = FONTS / fn
        if not fp.exists():
            continue
        data = b64(fp)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(out)


CSS = f"""
{font_css()}
{DIAGRAM_CSS}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:subpixel-antialiased;text-rendering:optimizeLegibility;}}
html,body{{background:#d8d0c4;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}

/* Textura lino + retícula técnica */
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    repeating-linear-gradient(0deg,rgba(28,24,20,.03) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(28,24,20,.03) 0 1px,transparent 1px 4px),
    linear-gradient(rgba(28,24,20,.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(28,24,20,.06) 1px, transparent 1px);
  background-size:auto,auto,48px 48px,48px 48px;}}
.slide::after{{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(ellipse 80% 60% at 50% 40%, rgba(255,255,255,.25), transparent 70%);}}

/* Marco técnico blueprint */
.tech-frame{{position:absolute;inset:28px;border:1.5px solid rgba(28,24,20,.22);z-index:4;pointer-events:none;border-radius:2px;}}
.crop{{position:absolute;width:18px;height:18px;z-index:5;pointer-events:none;}}
.crop::before,.crop::after{{content:'';position:absolute;background:rgba(28,24,20,.35);}}
.crop-tl{{top:22px;left:22px;}}.crop-tr{{top:22px;right:22px;}}.crop-bl{{bottom:22px;left:22px;}}.crop-br{{bottom:22px;right:22px;}}
.crop-tl::before,.crop-tr::before,.crop-bl::before,.crop-br::before{{width:18px;height:1px;top:8px;left:0;}}
.crop-tl::after,.crop-tr::after,.crop-bl::after,.crop-br::after{{width:1px;height:18px;left:8px;top:0;}}
.ruler{{position:absolute;top:80px;bottom:100px;width:28px;z-index:5;pointer-events:none;
  font-family:'IBM Plex Mono',monospace;font-size:9px;color:rgba(28,24,20,.35);letter-spacing:.06em;}}
.ruler-l{{left:8px;border-right:1px solid rgba(28,24,20,.12);padding-right:6px;text-align:right;}}
.ruler-r{{right:8px;border-left:1px solid rgba(28,24,20,.12);padding-left:6px;}}
.ruler span{{display:block;margin:120px 0;}}

.top-bar{{position:absolute;top:36px;left:48px;right:48px;z-index:20;display:flex;align-items:center;gap:16px;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:11px;letter-spacing:.14em;color:{GY};text-transform:uppercase;}}
.pill-n{{border:1.5px solid {O};border-radius:999px;padding:6px 14px;color:{TX};font-weight:600;background:rgba(255,255,255,.35);flex-shrink:0;}}
.series{{flex:1;text-align:center;}}
.bottom-bar{{position:absolute;bottom:88px;left:48px;right:48px;z-index:20;display:flex;justify-content:space-between;align-items:center;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:10px;letter-spacing:.12em;color:{GY};text-transform:uppercase;
  border-top:1px solid {BD};padding-top:10px;}}
.bottom-bar .nav em{{font-style:normal;color:{O};font-weight:600;}}
.firma{{position:absolute;left:0;right:0;bottom:48px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:22px;letter-spacing:.14em;color:{O};}}

.content{{position:absolute;left:52px;right:52px;top:96px;bottom:128px;z-index:8;
  display:flex;flex-direction:column;}}
.title{{font-family:'Impact','Anton','Bebas Neue',sans-serif;font-weight:400;font-size:58px;line-height:.92;
  letter-spacing:.01em;text-transform:uppercase;text-align:left;color:{TX};flex:0 0 auto;}}
.title .g{{color:{O};}}
.title.center{{text-align:center;}}
.title-u{{display:block;width:100%;max-width:320px;height:5px;background:{O};margin:10px auto 0;border-radius:2px;opacity:.85;}}
.title.left-u{{margin-left:0;margin-right:auto;}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:24px;line-height:1.22;
  color:{GY};margin-top:8px;max-width:920px;flex:0 0 auto;}}
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:10px;overflow:visible;}}
.graphic .dia{{width:100%;max-width:100%;}}
.graphic-stack{{align-items:flex-start;justify-content:flex-start;padding-top:6px;}}
.slide-hero .title{{font-size:54px;line-height:.9;text-align:center;}}
.slide-hero .title-u{{margin:10px auto 0;}}
.slide-hero .lead{{text-align:center;margin-left:auto;margin-right:auto;font-size:22px;}}
.slide-hero .graphic{{margin-top:14px;}}
.slide-step .step-label{{display:inline-block;background:{O};color:#fff;font-family:'IBM Plex Mono',monospace;
  font-weight:600;font-size:12px;letter-spacing:.14em;padding:6px 14px;border-radius:999px;margin-bottom:8px;flex:0 0 auto;}}
.slide-last .graphic{{flex:0 1 auto;}}
"""


def chrome(num: int, nav_active: int | None = None) -> str:
    nav_html = ""
    for i, lbl in enumerate(NAV):
        if i > 0:
            nav_html += " · "
        nav_html += f"<em>{lbl}</em>" if nav_active == i else lbl
    return f"""<div class="tech-frame"></div>
<div class="crop crop-tl"></div><div class="crop crop-tr"></div><div class="crop crop-bl"></div><div class="crop crop-br"></div>
<div class="ruler ruler-l"><span>01</span><span>02</span><span>03</span></div>
<div class="ruler ruler-r"><span>01</span><span>02</span><span>03</span></div>
<div class="top-bar"><span class="pill-n">{num:02d} / {TOTAL:02d}</span><span class="series">{SERIES}</span></div>
<div class="bottom-bar"><span>PROSPECTOS · IA</span><span class="nav">{nav_html}</span><span>{num:02d} / {TOTAL:02d}</span></div>
<div class="firma">sebastian.stlabs.ar</div>"""


def slide(
    num: int,
    title: str,
    lead: str = "",
    dia_n: int | None = None,
    hero: bool = False,
    last: bool = False,
    step: str = "",
    center_title: bool = False,
    nav_active: int | None = None,
    graphic_cls: str = "",
) -> str:
    gcls = " ".join(p for p in ("graphic", graphic_cls) if p)
    ghtml = f'<div class="{gcls}">{diagram(dia_n)}</div>' if dia_n else ""
    lead_html = f'<div class="lead">{lead}</div>' if lead else ""
    step_html = f'<div class="step-label">{step}</div>' if step else ""
    cls = "slide slide-hero" if hero else ("slide slide-last" if last else "slide slide-step" if step else "slide")
    tcls = "title center" if center_title or hero else "title"
    uline = '<div class="title-u"></div>' if hero else ('<div class="title-u left-u"></div>' if num <= 3 else "")
    return f"""<div class="{cls}">{chrome(num, nav_active)}<div class="content">
  {step_html}
  <div class="{tcls}">{title}</div>
  {uline}
  {lead_html}
  {ghtml}
</div></div>"""


SLIDES = [
    slide(
        1,
        'CONSTRUYE TU<br><span class="g">AGENTE TURBO</span>',
        "Un agente que busca prospectos, recuerda cada corrida y se mejora solo.",
        1,
        hero=True,
        center_title=True,
        nav_active=3,
    ),
    slide(
        2,
        'QUÉ ES<br><span class="g">ESTO.</span>',
        "Recibí tu brief, conectá los canales y dejá que Turbo coordine la búsqueda.",
        2,
        graphic_cls="graphic-stack",
        nav_active=0,
    ),
    slide(
        3,
        'POR QUÉ<br><span class="g">FUNCIONA.</span>',
        "Un fallo no importa. Un <b>patrón</b> cambia cómo busca clientes.",
        3,
        nav_active=3,
    ),
    slide(
        4,
        'LAS 4 PARTES<br><span class="g">QUE NECESITÁS.</span>',
        "Motor, memoria, canales y panel. Cuatro piezas. Un sistema.",
        4,
        nav_active=1,
    ),
    slide(
        5,
        'CONECTÁ<br><span class="g">EL CEREBRO.</span>',
        "El motor Turbo más habilidades chicas. Mejor que un prompt gigante.",
        5,
        step="PASO 1",
        nav_active=1,
    ),
    slide(
        6,
        'CONSTRUÍ<br><span class="g">LA MEMORIA.</span>',
        "Cada corrida queda en archivos. Si no está en el archivo, no pasó.",
        6,
        step="PASO 2",
        nav_active=2,
    ),
    slide(
        7,
        'CONECTÁ<br><span class="g">LOS CANALES.</span>',
        "LinkedIn, email y CRM en un solo flujo. Nada se pierde.",
        7,
        step="PASO 3",
        nav_active=1,
    ),
    slide(
        8,
        'CONSTRUÍ<br><span class="g">EL PANEL.</span>',
        "Una sola pantalla con métricas, bandeja y señales en vivo.",
        8,
        step="PASO 4",
        nav_active=0,
    ),
    slide(
        9,
        'ASÍ SE VE<br><span class="g">UN DÍA REAL.</span>',
        "Busca de noche, fin de semana y feriados. Sin pausas.",
        9,
        nav_active=3,
    ),
    slide(
        10,
        '¿QUERÉS TU<br><span class="g">TURBO?</span>',
        "Turbo es potente. Conmigo queda calibrado para tu mercado.",
        10,
        last=True,
        center_title=True,
        nav_active=0,
    ),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Cómo construí Turbo</title>
<style>{CSS}</style>
</head><body>
<div class="sheet">
{''.join(SLIDES)}
</div>
</body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    print("OK", len(SLIDES), "slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
