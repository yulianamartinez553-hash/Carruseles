# -*- coding: utf-8 -*-
"""Carrusel STLabs — Turbo busca prospectos (8 slides, fondo negro).
Diagramas SVG nativos en español + identidad STLabs.
"""
from __future__ import annotations

import json
from pathlib import Path

from diagrams import DIAGRAM_CSS, diagram

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
V = "#00FFB2"
BG = "#0A0A0A"
TX = "#F2F2F2"
GY = "#9aa39c"


def b64(p: Path) -> str:
    import base64

    return base64.b64encode(p.read_bytes()).decode()


def font_css() -> str:
    faces = [
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Poppins", "Poppins-ExtraBold.ttf", 800, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
    ]
    out = []
    for fam, fn, w, st in faces:
        data = b64(FONTS / fn)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(out)


CSS = f"""
{font_css()}
{DIAGRAM_CSS}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background:
    repeating-linear-gradient(0deg, rgba(255,255,255,.018) 0 1px, transparent 1px 7px),
    repeating-linear-gradient(90deg, rgba(255,255,255,.014) 0 1px, transparent 1px 7px),
    radial-gradient(ellipse 70% 45% at 88% 4%, rgba(0,255,178,.055), transparent 55%),
    radial-gradient(ellipse 55% 40% at 4% 96%, rgba(0,255,178,.03), transparent 50%);
  mix-blend-mode:overlay;opacity:.95;}}
.frame{{position:absolute;inset:36px;border:1.5px solid rgba(255,255,255,.08);z-index:4;pointer-events:none;}}
.firma{{position:absolute;left:0;right:0;bottom:52px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;color:{V};}}
.content{{position:absolute;left:56px;right:56px;top:56px;bottom:100px;z-index:8;
  display:flex;flex-direction:column;}}
.meta{{display:flex;align-items:center;gap:12px;margin-bottom:8px;}}
.meta .n{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.08em;
  color:{TX};border:1.5px solid rgba(255,255,255,.22);padding:7px 11px;line-height:1;}}
.meta .tag{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.16em;
  text-transform:uppercase;color:{GY};}}
.meta .dot{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 10px rgba(0,255,178,.6);}}
.title{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:88px;line-height:.88;
  letter-spacing:.02em;text-transform:uppercase;text-align:left;color:{TX};}}
.title .g{{color:{V};}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:600;font-size:34px;line-height:1.2;
  color:{GY};margin-top:10px;max-width:960px;}}
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:2px;}}
.slide-hero .title{{font-size:112px;line-height:.84;letter-spacing:.015em;max-width:980px;}}
.slide-hero .lead{{font-size:40px;margin-top:14px;color:{TX};letter-spacing:.02em;}}
.slide-hero .lead b{{color:{V};}}
.slide-hero .graphic{{margin-top:0;}}
.slide-hero .meta{{margin-bottom:6px;}}
.slide-last .graphic{{flex:0 1 auto;max-height:500px;}}
.cta{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.08);padding:16px 20px;text-align:left;}}
.cta .kw{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:60px;letter-spacing:.06em;color:{V};line-height:1;}}
.cta .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:26px;color:{GY};margin-top:6px;line-height:1.25;}}
.cta .hint b{{color:{TX};font-weight:700;}}
/* Turbo mascot drop — sin cajas de foto genéricas */
.dia-robot{{background:transparent !important;border-radius:0 !important;}}
.dia-robot-wrap{{background:transparent !important;}}
"""


def chrome() -> str:
    return '<div class="frame"></div><div class="firma">sebastian.stlabs.ar</div>'


def slide(
    num: int,
    tag: str,
    title: str,
    lead: str = "",
    dia_n: int | None = None,
    hero: bool = False,
    extra: str = "",
) -> str:
    ghtml = f'<div class="graphic">{diagram(dia_n)}</div>' if dia_n else ""
    lead_html = f'<div class="lead">{lead}</div>' if lead else ""
    slide_cls = "slide slide-hero" if hero else ("slide slide-last" if num == 8 else "slide")
    return f"""<div class="{slide_cls}">{chrome()}<div class="content">
  <div class="meta"><div class="n">{num:02d}</div><div class="tag">{tag}</div><div class="dot"></div></div>
  <div class="title">{title}</div>
  {lead_html}
  {ghtml}
  {extra}
</div></div>"""


SLIDES = [
    slide(
        1,
        "TURBO · PROSPECTOS",
        'ARMÉ UN <span class="g">TURBO</span><br>QUE BUSCA<br><span class="g">CLIENTES</span>',
        "Se mejora solo. <b>24/7.</b>",
        1,
        hero=True,
    ),
    slide(
        2,
        "TURBO · PROSPECTOS",
        'RECUERDA<br><span class="g">CADA BÚSQUEDA</span>',
        "Cada corrida deja datos: a quién contactó, qué respondió, qué cerró.",
        2,
    ),
    slide(
        3,
        "TURBO · PROSPECTOS",
        'MIDE SI EL<br><span class="g">PROSPECTO SIRVE</span>',
        "Puntuá cada prospecto con tus criterios: ajuste, urgencia y monto.",
        3,
    ),
    slide(
        4,
        "TURBO · PROSPECTOS",
        'SE <span class="g">CRITICA</span><br>SOLO',
        "Un crítico revisa cada corrida sin sesgo: mensajes, filtros, resultados.",
        4,
    ),
    slide(
        5,
        "TURBO · PROSPECTOS",
        'ENCUENTRA<br><span class="g">SUS ERRORES</span>',
        "Un fallo no importa. Un <b>patrón</b> cambia cómo busca clientes.",
        5,
    ),
    slide(
        6,
        "TURBO · PROSPECTOS",
        'SE CONSTRUYE<br><span class="g">MEJOR</span>',
        "Convierte la retroalimentación en un Turbo más preciso para tu mercado.",
        6,
    ),
    slide(
        7,
        "TURBO · PROSPECTOS",
        'TIENE QUE<br><span class="g">PROBARLO</span>',
        "Cada mejora se prueba antes de salir a buscar prospectos de verdad.",
        7,
    ),
    slide(
        8,
        "TURBO · PROSPECTOS",
        'TURBO ES POTENTE.<br><span class="g">YO LO ESPECIALIZO.</span>',
        "Solo busca. Conmigo, queda calibrado para tu negocio.",
        8,
        extra="""
  <div class="cta">
    <div class="kw">TURBO</div>
    <div class="hint">Comentá la palabra y te armo el sistema de prospectos<br>especializado para <b>tu</b> mercado.</div>
  </div>""",
    ),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Turbo busca prospectos</title>
<style>{CSS}</style>
</head><body>
<div class="sheet">
{''.join(SLIDES)}
</div>
</body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")

    meta = json.loads((B / "content.json").read_text(encoding="utf-8"))
    meta["notas"] = (
        "Diagramas SVG nativos ES. Fondo negro lino_tela. "
        "Cierre 1ª persona Sebastián. Sin inglés."
    )
    (B / "manifest.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (B / "content.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
