# -*- coding: utf-8 -*-
"""Carrusel STLabs — Cómo funciona Turbo (8 slides).
Diagramas nativos SVG/CSS + elementos 3D aislados · fondo negro · CTA TURBO.
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
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(ellipse 70% 45% at 88% 4%, rgba(0,255,178,.06), transparent 55%),
             radial-gradient(ellipse 55% 40% at 4% 96%, rgba(0,255,178,.03), transparent 50%);}}
.frame{{position:absolute;inset:36px;border:1.5px solid rgba(255,255,255,.08);z-index:4;pointer-events:none;}}
.firma{{position:absolute;left:0;right:0;bottom:52px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;color:{V};}}
.content{{position:absolute;left:56px;right:56px;top:56px;bottom:100px;z-index:8;
  display:flex;flex-direction:column;}}
.meta{{display:flex;align-items:center;gap:12px;margin-bottom:14px;}}
.meta .n{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;letter-spacing:.08em;
  color:{TX};border:1.5px solid rgba(255,255,255,.22);padding:8px 12px;line-height:1;}}
.meta .tag{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.16em;
  text-transform:uppercase;color:{GY};}}
.meta .dot{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 10px rgba(0,255,178,.6);}}
.title{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:76px;line-height:.92;
  letter-spacing:.01em;text-transform:uppercase;text-align:left;color:{TX};}}
.title .g{{color:{V};}}
.title.md{{font-size:68px;}}
.title.sm{{font-size:60px;}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:30px;line-height:1.22;
  color:{GY};margin-top:8px;max-width:960px;}}
.lead.compact{{font-size:26px;margin-top:4px;}}
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:4px;overflow:visible;}}
.graphic.hero{{margin-top:0;align-items:stretch;overflow:visible;}}
.slide-hero .title{{font-size:54px;line-height:.88;margin-bottom:0;}}
.slide-hero .meta{{margin-bottom:6px;}}
.slide-hero .content{{bottom:84px;}}
.slide-hero .lead.compact{{font-size:22px;margin-top:2px;line-height:1.15;}}
.graphic.compact{{max-height:none;flex:1 1 auto;}}
.badge{{display:inline-block;margin-top:10px;padding:12px 18px;border:2px solid {V};
  font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:17px;letter-spacing:.14em;
  text-transform:uppercase;color:{TX};background:rgba(0,255,178,.1);}}
.cta{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.08);padding:18px 22px;text-align:center;}}
.cta .kw{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:72px;letter-spacing:.06em;color:{V};line-height:1;}}
.cta .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:24px;color:{GY};margin-top:8px;}}
.slide-last .graphic{{flex:0 1 auto;margin-bottom:8px;}}
{DIAGRAM_CSS}
"""


def chrome() -> str:
    return '<div class="frame"></div><div class="firma">sebastian.stlabs.ar</div>'


def slide(
    num: int,
    tag: str,
    title: str,
    lead: str = "",
    diagram_n: int | None = None,
    compact: bool = False,
    hero: bool = False,
    extra: str = "",
) -> str:
    dhtml = ""
    if diagram_n:
        cls = "graphic"
        if compact:
            cls += " compact"
        if hero:
            cls += " hero"
        dhtml = f'<div class="{cls}">{diagram(diagram_n)}</div>'
    lead_html = ""
    if lead:
        lcls = "lead compact" if hero else "lead"
        lead_html = f'<div class="{lcls}">{lead}</div>'
    slide_cls = "slide slide-hero" if hero else ("slide slide-last" if num == 8 else "slide")
    return f"""<div class="{slide_cls}">{chrome()}<div class="content">
  <div class="meta"><div class="n">{num:02d}</div><div class="tag">{tag}</div><div class="dot"></div></div>
  <div class="title">{title}</div>
  {lead_html}
  {dhtml}
  {extra}
</div></div>"""


SLIDES = [
    slide(
        1,
        "TURBO · SISTEMA",
        'TE ARMO UN <span class="g">TURBO</span><br>QUE SE MEJORA<br><span class="g">SOLO</span>',
        "Mejora todos los días. <b>24/7.</b>",
        1,
        hero=True,
    ),
    slide(
        2,
        "TURBO · SISTEMA",
        'RECUERDA<br><span class="g">CADA BÚSQUEDA</span>',
        "Cada corrida se convierte en dato que Turbo usa para aprender.",
        2,
    ),
    slide(
        3,
        "TURBO · SISTEMA",
        'MIDE SU<br><span class="g">RENDIMIENTO</span>',
        "En vez de adivinar, puntúa cada resultado con tus criterios.",
        3,
    ),
    slide(
        4,
        "TURBO · SISTEMA",
        'SE <span class="g">CRITICA</span><br>SOLO',
        "Un crítico revisa cada corrida sin sesgo.",
        4,
    ),
    slide(
        5,
        "TURBO · SISTEMA",
        'ENCUENTRA<br><span class="g">SUS ERRORES</span>',
        "Un fallo no importa. Un <b>patrón</b> cambia todo.",
        5,
    ),
    slide(
        6,
        "TURBO · SISTEMA",
        'SE CONSTRUYE<br><span class="g">MEJOR</span>',
        "Convierte la retroalimentación en mejoras reales del sistema.",
        6,
    ),
    slide(
        7,
        "TURBO · SISTEMA",
        'TIENE QUE<br><span class="g">PROBARLO</span>',
        "Cada mejora se prueba antes de quedarse en producción.",
        7,
    ),
    slide(
        8,
        "TURBO · SISTEMA",
        'ARMÁ TU<br><span class="g">TURBO</span>',
        "Corré, aprendé, evolucioná — sin que tu equipo persiga leads a mano.",
        8,
        extra="""
  <div class="cta">
    <div class="kw">TURBO</div>
    <div class="hint">Comentá la palabra y te escribo para mapear tu mercado</div>
  </div>""",
    ),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Cómo funciona Turbo</title>
<style>{CSS}</style>
</head><body>
<div class="sheet">
{''.join(SLIDES)}
</div>
</body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")

    meta = {
        "id": "2026-08-25-turbo-blueprint",
        "fecha": "2026-08-25",
        "titulo": "Cómo funciona Turbo — busca clientes 24/7",
        "slides": 8,
        "fondo": "gradiente_profundo",
        "familia_visual": "blueprint",
        "origen": "clonado",
        "keyword_portada": "TURBO",
        "modo": "negro",
        "cta": "TURBO",
        "notas": "Diagramas SVG/CSS nativos ES; robots/cerebro recortados como elementos 3D",
    }
    (B / "manifest.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
