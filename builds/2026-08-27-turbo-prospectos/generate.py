# -*- coding: utf-8 -*-
"""Carrusel STLabs — Turbo busca prospectos (8 slides, fondo negro).
Portada alineada a referencia profesional + mascota oficial Turbo.
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
        ("Impact", "Impact.ttf", 400, "normal"),
        ("Anton", "Anton-Regular.ttf", 400, "normal"),
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Poppins", "Poppins-ExtraBold.ttf", 800, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
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
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 75% 50% at 80% 8%, rgba(0,255,178,.07), transparent 58%),
    radial-gradient(ellipse 55% 40% at 8% 92%, rgba(0,255,178,.035), transparent 52%);}}
.frame{{position:absolute;inset:36px;border:1.5px solid rgba(255,255,255,.08);z-index:4;pointer-events:none;}}
.firma{{position:absolute;left:0;right:0;bottom:52px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;color:{V};}}
.content{{position:absolute;left:56px;right:56px;top:56px;bottom:100px;z-index:8;
  display:flex;flex-direction:column;}}
.meta{{display:flex;align-items:center;gap:12px;margin-bottom:10px;}}
.meta .n{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;letter-spacing:.08em;
  color:{TX};border:1.5px solid rgba(255,255,255,.25);padding:8px 12px;line-height:1;}}
.meta .tag{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.16em;
  text-transform:uppercase;color:{GY};}}
.meta .dot{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 10px rgba(0,255,178,.6);}}
.title{{font-family:'Impact','Anton','Bebas Neue',sans-serif;font-weight:400;font-size:100px;line-height:.88;
  letter-spacing:.02em;text-transform:uppercase;text-align:left;color:{TX};}}
.title .g{{color:{V};}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:36px;line-height:1.25;
  color:{GY};margin-top:12px;max-width:980px;}}
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:6px;}}

/* —— PORTADA (referencia profesional) —— */
.slide-hero .content{{top:48px;bottom:92px;}}
.slide-hero .meta{{margin-bottom:8px;}}
.slide-hero .title{{font-size:124px;line-height:.8;letter-spacing:.01em;max-width:1000px;}}
.slide-hero .title .line-24{{display:block;font-size:140px;line-height:.8;color:{V};margin-top:2px;}}
.slide-hero .lead{{font-size:36px;margin-top:16px;max-width:920px;color:#c8c8c8;font-weight:500;}}
.slide-hero .graphic{{margin-top:8px;align-items:flex-start;}}
.slide-hero .dia-01{{width:100%;max-width:980px;min-height:720px;}}
.slide-hero .dia-01 svg{{max-height:700px;width:100%;}}

.slide-last .graphic{{flex:0 1 auto;max-height:500px;}}
.cta{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.08);padding:16px 20px;text-align:left;}}
.cta .kw{{font-family:'Impact','Anton',sans-serif;font-weight:400;font-size:64px;letter-spacing:.06em;color:{V};line-height:1;}}
.cta .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;color:{GY};margin-top:6px;line-height:1.25;}}
.cta .hint b{{color:{TX};font-weight:700;}}
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
        "TURBO · PLANO",
        'TE ARMO <span class="g">TURBO</span><br>BUSCA CLIENTES<br><span class="line-24">24/7</span>',
        "Un sistema que sale a buscar prospectos y se mejora solo, todos los días.",
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
        "Portada estilo referencia (Impact + 24/7 grande). "
        "Mascota oficial Turbo al centro. Solo español."
    )
    meta["keyword_portada"] = "TURBO"
    (B / "manifest.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (B / "content.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
