# -*- coding: utf-8 -*-
"""Carrusel STLabs — Cómo funciona Turbo (8 slides).
Gráficos recortados de referencia @seb.ai · fondo negro · CTA TURBO.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path

B = Path(__file__).resolve().parent
ASSETS = B / "assets"
FONTS = Path("/tmp/stlabs-fonts")
V = "#00FFB2"
BG = "#0A0A0A"
TX = "#F2F2F2"
GY = "#9aa39c"


def b64(p: Path) -> str:
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


def img_uri(n: int) -> str:
    p = ASSETS / f"graphic-{n:02d}.png"
    return f"data:image/png;base64,{b64(p)}"


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
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:6px;overflow:hidden;}}
.graphic img{{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;object-position:center;display:block;}}
.graphic.fill img{{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain;}}
.graphic.compact img{{max-height:640px;}}
.badge{{display:inline-block;margin-top:10px;padding:12px 18px;border:2px solid {V};
  font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:17px;letter-spacing:.14em;
  text-transform:uppercase;color:{TX};background:rgba(0,255,178,.1);}}
.cta{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.08);padding:22px 24px;text-align:center;}}
.cta .kw{{font-family:'Bebas Neue',sans-serif;font-weight:400;font-size:88px;letter-spacing:.06em;color:{V};line-height:1;}}
.cta .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;color:{GY};margin-top:10px;}}
"""


def chrome() -> str:
    return '<div class="frame"></div><div class="firma">sebastian.stlabs.ar</div>'


def slide(
    num: int,
    tag: str,
    title: str,
    lead: str = "",
    graphic_n: int | None = None,
    fill: bool = False,
    compact: bool = False,
    extra: str = "",
) -> str:
    ghtml = ""
    if graphic_n:
        cls = "graphic"
        if fill:
            cls += " fill"
        if compact:
            cls += " compact"
        ghtml = f'<div class="{cls}"><img src="{img_uri(graphic_n)}" alt=""/></div>'
    lead_html = f'<div class="lead">{lead}</div>' if lead else ""
    return f"""<div class="slide">{chrome()}<div class="content">
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
        'TE ARMO <span class="g">TURBO</span><br>BUSCA CLIENTES<br><span class="g">24/7</span>',
        "Un sistema que sale a buscar prospectos y se mejora solo, todos los días.",
        1,
        fill=True,
    ),
    slide(
        2,
        "MEMORIA",
        'RECUERDA<br><span class="g">CADA BÚSQUEDA</span>',
        "Cada corrida se convierte en dato que Turbo usa para aprender.",
        2,
        fill=True,
    ),
    slide(
        3,
        "MÉTRICAS",
        'MIDE SU<br><span class="g">RENDIMIENTO</span>',
        "En vez de adivinar, puntúa cada resultado con tus criterios.",
        3,
        fill=True,
    ),
    slide(
        4,
        "CRÍTICA",
        'SE <span class="g">CRITICA</span><br>SOLO',
        "Un segundo agente revisa cada corrida sin sesgo.",
        4,
        fill=True,
    ),
    slide(
        5,
        "PATRONES",
        'ENCUENTRA<br><span class="g">SUS ERRORES</span>',
        "Un fallo no importa. Un patrón cambia todo.",
        5,
        fill=True,
    ),
    slide(
        6,
        "EVOLUCIÓN",
        'SE CONSTRUYE<br><span class="g">MEJOR</span>',
        "Convierte la retroalimentación en mejoras reales del sistema.",
        6,
        fill=True,
    ),
    slide(
        7,
        "VALIDACIÓN",
        'TIENE QUE<br><span class="g">PROBARLO</span>',
        "Cada mejora se testea antes de quedarse en producción.",
        7,
        fill=True,
    ),
    slide(
        8,
        "PRÓXIMO PASO",
        'ARMÁ TU<br><span class="g">TURBO</span>',
        "Corre, aprende, evoluciona — sin que tu equipo persiga leads a mano.",
        8,
        fill=True,
        compact=True,
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
        "notas": "Gráficos recortados de referencia @seb.ai; copy Turbo STLabs",
    }
    (B / "manifest.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("OK 8 slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
