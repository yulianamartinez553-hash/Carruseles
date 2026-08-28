# -*- coding: utf-8 -*-
"""Carrusel STLabs — Sistema Turbo (10 slides, fondo negro, dashboard técnico)."""
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
BD = "#2A2A2A"
PN = "#141414"
TOTAL = 10


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
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:subpixel-antialiased;text-rendering:optimizeLegibility;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}

/* Retícula verde + manchas blur */
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(rgba(0,255,178,.18) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.18) 1px, transparent 1px);
  background-size:52px 52px;opacity:1;}}
.slide::after{{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background:
    radial-gradient(ellipse 420px 320px at 12% 18%, rgba(0,255,178,.16), transparent 70%),
    radial-gradient(ellipse 380px 300px at 88% 12%, rgba(0,255,178,.12), transparent 68%),
    radial-gradient(ellipse 500px 360px at 78% 72%, rgba(0,255,178,.10), transparent 70%),
    radial-gradient(ellipse 360px 280px at 18% 82%, rgba(0,255,178,.08), transparent 68%);
  filter:blur(28px);opacity:.9;}}

/* HUD marco técnico */
.hud-tl{{position:absolute;top:44px;left:48px;z-index:20;display:flex;align-items:center;gap:10px;
  font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;color:{TX};letter-spacing:.06em;}}
.hud-tl .sun{{color:{V};font-size:20px;}}
.hud-tr{{position:absolute;top:44px;right:48px;z-index:20;font-family:'IBM Plex Mono',monospace;font-weight:600;
  font-size:13px;letter-spacing:.1em;color:{GY};display:flex;align-items:center;gap:8px;}}
.hud-tr .dot{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 8px rgba(0,255,178,.6);}}
.hud-br{{position:absolute;bottom:108px;left:48px;right:48px;z-index:20;display:flex;justify-content:space-between;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:12px;letter-spacing:.12em;color:{GY};opacity:.85;}}
.corner{{position:absolute;width:32px;height:32px;border:2px solid rgba(0,255,178,.45);z-index:19;pointer-events:none;}}
.corner-tl{{top:36px;left:36px;border-right:none;border-bottom:none;}}
.corner-tr{{top:36px;right:36px;border-left:none;border-bottom:none;}}
.corner-bl{{bottom:96px;left:36px;border-right:none;border-top:none;}}
.corner-br{{bottom:96px;right:36px;border-left:none;border-top:none;}}
.prog{{position:absolute;left:48px;right:48px;bottom:88px;height:4px;background:#1a1a1a;z-index:18;border-radius:2px;overflow:hidden;}}
.prog span{{display:block;height:100%;background:{V};box-shadow:0 0 10px rgba(0,255,178,.5);}}

.frame{{position:absolute;inset:32px;border:1.5px solid rgba(255,255,255,.08);z-index:4;pointer-events:none;border-radius:4px;}}
.firma{{position:absolute;left:0;right:0;bottom:52px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;color:{V};}}
.content{{position:absolute;left:48px;right:48px;top:82px;bottom:118px;z-index:8;
  display:flex;flex-direction:column;}}
.meta{{display:flex;align-items:center;gap:12px;margin-bottom:6px;flex:0 0 auto;}}
.meta .n{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;letter-spacing:.08em;
  color:{TX};border:1.5px solid rgba(0,255,178,.35);padding:8px 12px;line-height:1;background:rgba(0,0,0,.5);}}
.meta .tag{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.14em;
  text-transform:uppercase;color:{GY};}}
.meta .dot{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 10px rgba(0,255,178,.6);}}
.title{{font-family:'Impact','Anton','Bebas Neue',sans-serif;font-weight:400;font-size:64px;line-height:.9;
  letter-spacing:.01em;text-transform:uppercase;text-align:left;color:{TX};flex:0 0 auto;}}
.title .g{{color:{V};}}
.title-u{{display:block;width:220px;height:6px;background:{V};margin-top:8px;border-radius:2px;box-shadow:0 0 12px rgba(0,255,178,.4);}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;line-height:1.22;
  color:{GY};margin-top:6px;max-width:960px;flex:0 0 auto;}}
.lead b{{color:{TX};font-weight:700;}}
.graphic{{flex:1 1 auto;display:flex;align-items:center;justify-content:center;min-height:0;margin-top:4px;overflow:visible;}}
.graphic .dia{{width:100%;max-width:100%;}}

.slide-hero .title{{font-size:62px;line-height:.88;}}
.slide-hero .lead{{font-size:26px;}}
.slide-last .graphic{{flex:0 1 auto;}}
.slide-last .cta-inline{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.08);padding:16px 20px;border-radius:14px;}}
.slide-last .cta-inline .kw{{font-family:'Impact',sans-serif;font-size:58px;color:{V};letter-spacing:.06em;line-height:1;}}
.slide-last .cta-inline .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;color:{GY};margin-top:8px;line-height:1.25;}}
.slide-last .cta-inline .hint b{{color:{TX};font-weight:700;}}
"""


def chrome(num: int) -> str:
    pct = int(num / TOTAL * 100)
    return f"""<div class="frame"></div>
<div class="corner corner-tl"></div><div class="corner corner-tr"></div>
<div class="corner corner-bl"></div><div class="corner corner-br"></div>
<div class="hud-tl"><span class="sun">✦</span> {num:02d} / {TOTAL:02d}</div>
<div class="hud-tr"><span class="dot"></span> ESTADO: TODOS LOS SISTEMAS OPERANDO</div>
<div class="prog"><span style="width:{pct}%"></span></div>
<div class="hud-br"><span>SISTEMA TURBO · PROSPECTOS</span><span>sebastian.stlabs.ar</span></div>
<div class="firma">sebastian.stlabs.ar</div>"""


def slide(
    num: int,
    tag: str,
    title: str,
    lead: str = "",
    dia_n: int | None = None,
    hero: bool = False,
    last: bool = False,
    extra: str = "",
) -> str:
    ghtml = f'<div class="graphic">{diagram(dia_n)}</div>' if dia_n else ""
    lead_html = f'<div class="lead">{lead}</div>' if lead else ""
    cls = "slide slide-hero" if hero else ("slide slide-last" if last else "slide")
    underline = '<div class="title-u"></div>' if num <= 3 else ""
    return f"""<div class="{cls}">{chrome(num)}<div class="content">
  <div class="meta"><div class="n">{num:02d}</div><div class="tag">{tag}</div><div class="dot"></div></div>
  <div class="title">{title}</div>
  {underline}
  {lead_html}
  {ghtml}
  {extra}
</div></div>"""


SLIDES = [
    slide(
        1,
        "TURBO · SISTEMA",
        'ASÍ FUNCIONA MI<br><span class="g">SISTEMA TURBO</span>',
        "Un agente que busca prospectos, aprende de cada corrida y se mejora solo.",
        1,
        hero=True,
    ),
    slide(
        2,
        "TURBO · AGENTE",
        'TODO EMPIEZA CON<br><span class="g">TURBO</span>',
        "Recibe tu brief, divide la búsqueda y coordina cada canal de prospección.",
        2,
    ),
    slide(
        3,
        "TURBO · MEMORIA",
        'RECUERDA<br><span class="g">CADA BÚSQUEDA</span>',
        "Cada corrida deja datos: a quién contactó, qué respondió, qué cerró.",
        3,
    ),
    slide(
        4,
        "TURBO · MÉTRICAS",
        'MIDE SI EL<br><span class="g">PROSPECTO SIRVE</span>',
        "Puntuá cada prospecto con tus criterios: ajuste, urgencia y monto.",
        4,
    ),
    slide(
        5,
        "TURBO · CRÍTICO",
        'SE <span class="g">CRITICA</span><br>SOLO',
        "Un crítico revisa cada corrida sin sesgo: mensajes, filtros, resultados.",
        5,
    ),
    slide(
        6,
        "TURBO · ERRORES",
        'ENCUENTRA<br><span class="g">PATRONES</span>',
        "Un fallo no importa. Un <b>patrón</b> cambia cómo busca clientes.",
        6,
    ),
    slide(
        7,
        "TURBO · MEJORA",
        'SE CONSTRUYE<br><span class="g">MEJOR</span>',
        "Convierte la retroalimentación en un Turbo más preciso para tu mercado.",
        7,
    ),
    slide(
        8,
        "TURBO · CEREBRO",
        'LA MEMORIA EVITA<br><span class="g">ALUCINACIONES</span>',
        "Todo vive en un solo lugar: prospectos, historial, contexto y reglas.",
        8,
    ),
    slide(
        9,
        "TURBO · 24/7",
        'CORRE <span class="g">TODO EL TIEMPO</span>',
        "Busca prospectos de noche, fin de semana y feriados. Sin pausas.",
        9,
    ),
    slide(
        10,
        "TURBO · CTA",
        'TURBO ES POTENTE.<br><span class="g">YO LO ESPECIALIZO.</span>',
        "Solo busca. Conmigo, queda calibrado para tu negocio.",
        10,
        last=True,
        extra="""
  <div class="cta-inline">
    <div class="kw">TURBO</div>
    <div class="hint">Comentá la palabra y te armo el sistema de prospectos<br>especializado para <b>tu</b> mercado.</div>
  </div>""",
    ),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Sistema Turbo (blanco)</title>
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
