# -*- coding: utf-8 -*-
"""Carrusel STLabs — El stack para lanzar apps (clon 12 slides, blanco/lino).
Recortes exactos de logos/ilustraciones desde las referencias adjuntas.
"""
from __future__ import annotations

import base64
from pathlib import Path

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
LOGOS = B / "assets" / "logos"

# Modo NEGRO STLabs
BG = "#0A0A0A"
TX = "#F2F2F2"
GY = "#9aa39c"
V = "#00FFB2"  # acento STLabs (reemplaza naranja de la ref)
TOTAL = 12


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def logo_uri(name: str) -> str:
    p = LOGOS / name
    return f"data:image/png;base64,{b64(p)}"


def font_css() -> str:
    faces = [
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
        ("Poppins", "Poppins-ExtraBold.ttf", 800, "normal"),
        ("Poppins", "Poppins-Bold.ttf", 700, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Medium.ttf", 500, "normal"),
        ("Barlow Condensed", "BarlowCondensed-Bold.ttf", 700, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500, "normal"),
        ("IBM Plex Mono", "IBMPlexMono-SemiBold.ttf", 600, "normal"),
        ("Lora", "Lora-Italic-Variable.ttf", "400 700", "italic"),
    ]
    out = []
    for fam, fn, w, st in faces:
        fp = FONTS / fn
        if not fp.exists():
            continue
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{b64(fp)}) format('truetype');}}"
        )
    return "\n".join(out)


CSS = f"""
{font_css()}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:subpixel-antialiased;text-rendering:optimizeLegibility;}}
html,body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
/* Textura piedra/roca + retícula sutil */
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;opacity:.45;
  background-image:
    linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),
    linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);
  background-size:48px 48px;}}
.slide::after{{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(ellipse 70% 50% at 50% 30%, rgba(0,255,178,.06), transparent 70%);}}
.spark{{position:absolute;z-index:2;pointer-events:none;color:rgba(0,255,178,.45);font-size:14px;}}

.content{{position:absolute;inset:0;z-index:5;display:flex;flex-direction:column;align-items:center;
  padding:72px 64px 120px;}}

.title{{font-family:'Poppins',sans-serif;font-weight:800;font-size:64px;line-height:.95;
  letter-spacing:-.01em;text-transform:uppercase;text-align:center;color:{TX};}}
.title .g{{color:{V};}}
.title .uline{{display:inline-block;border-bottom:8px solid {V};padding-bottom:2px;line-height:1;}}
.title.cover{{font-size:72px;}}
.title.step{{font-size:56px;}}
.title.cta{{font-size:80px;}}

.hero{{margin-top:28px;display:flex;align-items:center;justify-content:center;flex:1;min-height:0;}}
.hero img{{max-width:100%;max-height:100%;object-fit:contain;display:block;}}
.hero.logo img{{max-height:280px;max-width:420px;}}
.hero.grid img{{max-width:860px;max-height:560px;}}
.hero.cover img{{max-height:620px;}}

.box{{margin-top:28px;border:3px solid {V};border-radius:18px;padding:28px 36px;background:rgba(20,20,20,.85);
  max-width:820px;width:100%;box-shadow:0 0 24px rgba(0,255,178,.08);}}
.box ul{{list-style:none;font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:28px;
  line-height:1.55;color:{TX};}}
.box li::before{{content:'- ';color:{V};}}
.box.cta-box{{font-family:'IBM Plex Mono',monospace;font-size:24px;line-height:1.45;text-align:left;color:{TX};}}

.note{{margin-top:22px;font-family:'Lora',serif;font-style:italic;font-weight:600;font-size:26px;
  color:{GY};text-align:center;max-width:780px;line-height:1.3;}}
.note .arr{{display:inline-block;margin-left:10px;color:{V};font-style:normal;font-size:28px;}}

.foot{{position:absolute;left:56px;right:56px;bottom:48px;z-index:10;
  display:flex;justify-content:space-between;align-items:center;}}
.foot .save{{font-family:'Lora',serif;font-style:italic;font-size:20px;color:{GY};}}
.firma{{position:absolute;left:0;right:0;bottom:78px;text-align:center;z-index:12;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.12em;color:{V};}}
"""


def sparks() -> str:
    pts = [(90, 200), (980, 240), (120, 700), (960, 780), (200, 1100), (880, 1050)]
    return "".join(f'<div class="spark" style="left:{x}px;top:{y}px">✦</div>' for x, y in pts)


def foot() -> str:
    return """<div class="firma">sebastian.stlabs.ar</div>
<div class="foot"><span class="save">guardar para después</span><span class="save">✦</span></div>"""


def slide_cover() -> str:
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title cover"><span class="g">EL STACK</span><br>PARA LANZAR APLICACIONES<br><span class="g uline">CON IA</span></div>
    <div class="hero cover"><img src="{logo_uri('01-hero.png')}" alt=""/></div>
  </div>{foot()}</div>"""


def slide_tool(num_label: str, name: str, tagline: str, logo: str, bullets: list[str], note: str) -> str:
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title step">{num_label} {name}<br><span class="g uline">{tagline}</span></div>
    <div class="hero logo"><img src="{logo_uri(logo)}" alt=""/></div>
    <div class="box"><ul>{lis}</ul></div>
    <div class="note">{note}<span class="arr">→</span></div>
  </div>{foot()}</div>"""


def slide_grid() -> str:
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title step">UNA SOLA PERSONA<br><span class="g uline">LANZA TODO ESTO</span></div>
    <div class="hero grid"><img src="{logo_uri('11-grid.png')}" alt=""/></div>
    <div class="note">sin equipo, sin inversión,<br>sin permiso<span class="arr">→</span></div>
  </div>{foot()}</div>"""


def slide_cta() -> str:
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title cta">COMENTÁ<br><span class="g uline">STACK</span></div>
    <div class="hero logo"><img src="{logo_uri('12-bubble.png')}" alt=""/></div>
    <div class="box cta-box">y te paso la guía: cómo conectar cada herramienta para manejarlas desde un solo lugar, cuáles no se pueden y en qué orden hacerlo.</div>
    <div class="note">deslizá y guardalo<span class="arr">↓</span></div>
  </div>{foot()}</div>"""


SLIDES = [
    slide_cover(),
    slide_tool("1.", "REDDIT", "PARA ENCONTRAR EL DOLOR", "02-reddit.png",
               ["gente real quejándose", "buscá los foros de tu nicho", "sus palabras son tu copy"],
               "empezá acá, no construyendo"),
    slide_tool("2.", "TYPEFORM", "PARA LA LISTA DE ESPERA", "03-typeform.png",
               ["primero recolectá los mails", "probá que lo quieren", "toma diez minutos"],
               "una lista de espera es prueba, no esperanza"),
    slide_tool("3.", "CLAUDE CODE", "LA CONSTRUYE", "04-claude.png",
               ["describís y construye", "frontend y backend", "sin equipo de desarrollo"],
               "construir ya es la parte fácil"),
    slide_tool("4.", "VERCEL", "LA PONE ONLINE", "05-vercel.png",
               ["tu app queda online", "gratis hasta que escales", "despliega en diez segundos"],
               "hacés push y ya está online"),
    slide_tool("5.", "STRIPE", "COBRA EL DINERO", "06-stripe.png",
               ["cobrá desde el día uno", "suscripciones resueltas", "los pagos llegan solos"],
               "cobrá antes de sentirte listo"),
    slide_tool("6.", "RESEND", "LE ESCRIBE A LA LISTA", "07-resend.png",
               ["calienta la lista de espera", "el lanzamiento llega a la bandeja", "la lista es tuya"],
               "el mail le gana a cualquier algoritmo"),
    slide_tool("7.", "LOOM", "PARA LA DEMO", "08-loom.png",
               ["grabá sesenta segundos", "mostralo, no lo expliques", "un link, sin edición"],
               "la gente compra lo que puede ver"),
    slide_tool("8.", "META ADS", "TRAE LA GENTE", "09-meta.png",
               ["llegás a quien no te sigue", "probás con poco presupuesto", "el pago dice si sirve"],
               "la distribución se compra, no se espera"),
    slide_tool("9.", "POSTHOG", "MUESTRA LA VERDAD", "10-posthog.png",
               ["qué hacen realmente", "dónde abandonan", "gratis por mucho tiempo"],
               "las opiniones terminan donde empiezan los datos"),
    slide_grid(),
    slide_cta(),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — El stack para lanzar apps</title>
<style>{CSS}</style>
</head><body><div class="sheet">{''.join(SLIDES)}</div></body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    print("OK", len(SLIDES), "slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
