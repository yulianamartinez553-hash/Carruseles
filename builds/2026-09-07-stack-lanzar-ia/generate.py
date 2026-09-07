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


def logo_img(name: str, cls: str = "") -> str:
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{logo_uri(name)}" alt=""/>'


# SVG vectoriales (bordes lisos a cualquier escala)
def svg_wrap(inner: str, vb: str = "0 0 24 24") -> str:
    return (
        f'<svg class="logo-svg" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" '
        f'aria-hidden="true">{inner}</svg>'
    )


LOGO_SVG = {
    "reddit": svg_wrap(
        # burbuja naranja + snoo blanco (legible en fondo negro)
        '<circle cx="12" cy="12" r="11" fill="#FF4500"/>'
        '<path d="M19.2 12.9c0-1.1-.9-2-2-2-.5 0-1 .2-1.3.5-1.1-.7-2.5-1.1-4-1.2l.7-3.2 2.3.5c0 .8.7 1.5 1.5 1.5s1.5-.7 1.5-1.5S16.8 6 16 6c-.5 0-1 .3-1.3.7l-2.7-.6c-.2 0-.4.1-.4.3l-.8 3.6c-1.5.1-2.9.5-4 1.2-.3-.3-.8-.5-1.3-.5-1.1 0-2 .9-2 2 0 .8.5 1.5 1.2 1.8 0 .1 0 .3 0 .4 0 2.5 2.9 4.5 6.5 4.5s6.5-2 6.5-4.5c0-.1 0-.3 0-.4.7-.3 1.2-1 1.2-1.8z" fill="#fff"/>'
        '<circle cx="9.2" cy="13.6" r="1.15" fill="#FF4500"/>'
        '<circle cx="14.8" cy="13.6" r="1.15" fill="#FF4500"/>'
        '<path d="M9.8 16.1c.7.7 1.6 1 2.2 1s1.5-.3 2.2-1" fill="none" stroke="#FF4500" stroke-width="1.1" stroke-linecap="round"/>'
        '<circle cx="16.2" cy="7.5" r="1.15" fill="#FF4500"/>'
    ),
    "typeform": svg_wrap(
        '<rect x="3" y="3" width="7" height="18" rx="3.5" fill="#F2F2F2"/>'
        '<rect x="12" y="5" width="9" height="14" rx="3.2" fill="#F2F2F2"/>',
        "0 0 24 24",
    ),
    "vercel": svg_wrap('<path d="M12 2 L22 21 H2 Z" fill="#F2F2F2"/>'),
    "stripe": svg_wrap(
        '<path fill="#635BFF" d="M13.976 9.15c-2.172-.806-3.356-1.426-3.356-2.409 0-.831.683-1.305 1.901-1.305 2.227 0 4.515.858 6.09 1.631l.89-5.494C18.252.975 15.697 0 12.165 0 9.667 0 7.589.654 6.104 1.872 4.56 3.147 3.757 4.992 3.757 7.218c0 4.039 2.467 5.76 6.476 7.219 2.585.92 3.445 1.574 3.445 2.583 0 .98-.84 1.545-2.354 1.545-1.875 0-4.965-.921-6.99-2.109l-.9 5.555C5.175 22.99 8.385 24 11.714 24c2.641 0 4.843-.624 6.328-1.813 1.664-1.305 2.525-3.236 2.525-5.732 0-4.128-2.524-5.851-6.594-7.305h.003z"/>'
    ),
    "resend": svg_wrap(
        '<path fill="#F2F2F2" d="M2.023 0v24h5.553v-8.434h2.998L15.326 24h6.65l-5.372-9.258a7.652 7.652 0 0 0 3.316-3.016c.709-1.21 1.062-2.57 1.062-4.08 0-1.462-.353-2.767-1.062-3.91-.709-1.165-1.692-2.079-2.95-2.742C15.737.331 14.355 0 12.823 0Zm5.553 4.87h4.219c.731 0 1.349.125 1.851.376.526.252.925.618 1.2 1.098.274.457.412.994.412 1.611S15.132 9.12 14.88 9.6c-.229.48-.572.856-1.03 1.13-.434.252-.948.38-1.542.38H7.576Z"/>'
    ),
    "loom": svg_wrap(
        '<path fill="#625DF5" d="M24 10.665h-7.018l6.078-3.509-1.335-2.312-6.078 3.509 3.508-6.077L16.843.94l-3.508 6.077V0h-2.67v7.018L7.156.94 4.844 2.275l3.509 6.077-6.078-3.508L.94 7.156l6.078 3.509H0v2.67h7.017L.94 16.844l1.335 2.313 6.077-3.508-3.509 6.077 2.312 1.335 3.509-6.078V24h2.67v-7.017l3.508 6.077 2.312-1.335-3.509-6.078 6.078 3.509 1.335-2.313-6.077-3.508h7.017v-2.67H24zm-12 4.966a3.645 3.645 0 1 1 0-7.29 3.645 3.645 0 0 1 0 7.29z"/>'
    ),
    "meta": svg_wrap(
        '<path fill="#0081FB" d="M6.915 4.03c-1.968 0-3.683 1.28-4.871 3.113C.704 9.208 0 11.883 0 14.449c0 .706.07 1.369.21 1.973a6.624 6.624 0 0 0 .265.86 5.297 5.297 0 0 0 .371.761c.696 1.159 1.818 1.927 3.593 1.927 1.497 0 2.633-.671 3.965-2.444.76-1.012 1.144-1.626 2.663-4.32l.756-1.339.186-.325c.061.1.121.196.183.3l2.152 3.595c.724 1.21 1.665 2.556 2.47 3.314 1.046.987 1.992 1.22 3.06 1.22 1.075 0 1.876-.355 2.455-.843a3.743 3.743 0 0 0 .81-.973c.542-.939.861-2.127.861-3.745 0-2.72-.681-5.357-2.084-7.45-1.282-1.912-2.957-2.93-4.716-2.93-1.047 0-2.088.467-3.053 1.308-.652.57-1.257 1.29-1.82 2.05-.69-.875-1.335-1.547-1.958-2.056-1.182-.966-2.315-1.303-3.454-1.303zm10.16 2.053c1.147 0 2.188.758 2.992 1.999 1.132 1.748 1.647 4.195 1.647 6.4 0 1.548-.368 2.9-1.839 2.9-.58 0-1.027-.23-1.664-1.004-.496-.601-1.343-1.878-2.832-4.358l-.617-1.028a44.908 44.908 0 0 0-1.255-1.98c.07-.109.141-.224.211-.327 1.12-1.667 2.118-2.602 3.358-2.602zm-10.201.553c1.265 0 2.058.791 2.675 1.446.307.327.737.871 1.234 1.579l-1.02 1.566c-.757 1.163-1.882 3.017-2.837 4.338-1.191 1.649-1.81 1.817-2.486 1.817-.524 0-1.038-.237-1.383-.794-.263-.426-.464-1.13-.464-2.046 0-2.221.63-4.535 1.66-6.088.454-.687.964-1.226 1.533-1.533a2.264 2.264 0 0 1 1.088-.285z"/>'
    ),
    "posthog": svg_wrap(
        '<path fill="#F54E00" d="M9.854 14.5 5 9.647.854 5.5A.5.5 0 0 0 0 5.854V8.44a.5.5 0 0 0 .146.353L5 13.647l.147.146L9.854 18.5l.146.147v-.049c.065.03.134.049.207.049h2.586a.5.5 0 0 0 .353-.854L9.854 14.5zm0-5-4-4a.487.487 0 0 0-.409-.144.515.515 0 0 0-.356.21.493.493 0 0 0-.089.288V8.44a.5.5 0 0 0 .147.353l9 9a.5.5 0 0 0 .853-.354v-2.585a.5.5 0 0 0-.146-.354l-5-5zm1-4a.5.5 0 0 0-.854.354V8.44a.5.5 0 0 0 .147.353l4 4a.5.5 0 0 0 .853-.354V9.854a.5.5 0 0 0-.146-.354l-4-4zm12.647 11.515a3.863 3.863 0 0 1-2.232-1.1l-4.708-4.707a.5.5 0 0 0-.854.354v6.585a.5.5 0 0 0 .5.5H23.5a.5.5 0 0 0 .5-.5v-.6c0-.276-.225-.497-.499-.532zm-5.394.032a.8.8 0 1 1 0-1.6.8.8 0 0 1 0 1.6zM.854 15.5a.5.5 0 0 0-.854.354v2.293a.5.5 0 0 0 .5.5h2.293c.222 0 .39-.135.462-.309a.493.493 0 0 0-.109-.545L.854 15.501zM5 14.647.854 10.5a.5.5 0 0 0-.854.353v2.586a.5.5 0 0 0 .146.353L4.854 18.5l.146.147h2.793a.5.5 0 0 0 .353-.854L5 14.647z"/>'
    ),
    "claude": svg_wrap(
        # starburst tipo Claude (misma silueta que la ref)
        '<path fill="#D48C69" d="M12 1.2l1.6 6.2 5.9-2.6-2.6 5.9 6.2 1.6-6.2 1.6 2.6 5.9-5.9-2.6L12 22.8l-1.6-6.2-5.9 2.6 2.6-5.9L1.2 12l6.2-1.6-2.6-5.9 5.9 2.6z"/>'
    ),
    "bubble": svg_wrap(
        '<rect x="2" y="7" width="20" height="1.6" rx=".6" fill="#FF7828"/>'
        '<path fill="none" stroke="#FF7828" stroke-width="1.8" stroke-linecap="round" '
        'd="M7 14h10M7 14v5M17 14v5"/>',
        "0 0 24 24",
    ),
}


def logo_mark(key: str) -> str:
    if key in LOGO_SVG:
        return LOGO_SVG[key]
    return logo_img(key)


def logo_grid_html() -> str:
    keys = ["reddit", "typeform", "claude", "vercel", "stripe", "resend", "loom", "meta", "posthog"]
    cells = "".join(f'<div class="gcell">{LOGO_SVG[k]}</div>' for k in keys)
    return f'<div class="logo-grid"><div class="gline"></div><div class="gcells">{cells}</div><div class="gline"></div></div>'


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
.hero img{{max-width:100%;max-height:100%;object-fit:contain;display:block;
  image-rendering:auto;-webkit-backface-visibility:hidden;transform:translateZ(0);}}
.hero.logo img,.hero.logo .logo-svg{{max-height:320px;max-width:480px;width:280px;height:280px;}}
.hero.grid img{{max-width:900px;max-height:600px;}}
.hero.cover img{{max-height:660px;}}
.logo-svg{{display:block;overflow:visible;shape-rendering:geometricPrecision;}}
.logo-grid{{display:flex;flex-direction:column;align-items:center;gap:22px;width:min(900px,100%);}}
.logo-grid .gline{{width:100%;height:6px;background:#FF7828;border-radius:3px;opacity:.9;}}
.logo-grid .gcells{{display:grid;grid-template-columns:repeat(3,1fr);gap:36px 48px;width:100%;align-items:center;justify-items:center;}}
.logo-grid .gcell{{width:140px;height:140px;display:flex;align-items:center;justify-content:center;}}
.logo-grid .gcell .logo-svg{{width:120px;height:120px;}}

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


def slide_tool(num_label: str, name: str, tagline: str, logo_key: str, bullets: list[str], note: str) -> str:
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title step">{num_label} {name}<br><span class="g uline">{tagline}</span></div>
    <div class="hero logo">{logo_mark(logo_key)}</div>
    <div class="box"><ul>{lis}</ul></div>
    <div class="note">{note}<span class="arr">→</span></div>
  </div>{foot()}</div>"""


def slide_grid() -> str:
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title step">UNA SOLA PERSONA<br><span class="g uline">LANZA TODO ESTO</span></div>
    <div class="hero grid">{logo_grid_html()}</div>
    <div class="note">sin equipo, sin inversión,<br>sin permiso<span class="arr">→</span></div>
  </div>{foot()}</div>"""


def slide_cta() -> str:
    return f"""<div class="slide">{sparks()}
  <div class="content">
    <div class="title cta">COMENTÁ<br><span class="g uline">STACK</span></div>
    <div class="hero logo">{logo_mark('bubble')}</div>
    <div class="box cta-box">y te paso la guía: cómo conectar cada herramienta para manejarlas desde un solo lugar, cuáles no se pueden y en qué orden hacerlo.</div>
    <div class="note">deslizá y guardalo<span class="arr">↓</span></div>
  </div>{foot()}</div>"""


SLIDES = [
    slide_cover(),
    slide_tool("1.", "REDDIT", "PARA ENCONTRAR EL DOLOR", "reddit",
               ["gente real quejándose", "buscá los foros de tu nicho", "sus palabras son tu copy"],
               "empezá acá, no construyendo"),
    slide_tool("2.", "TYPEFORM", "PARA LA LISTA DE ESPERA", "typeform",
               ["primero recolectá los mails", "probá que lo quieren", "toma diez minutos"],
               "una lista de espera es prueba, no esperanza"),
    slide_tool("3.", "CLAUDE CODE", "LA CONSTRUYE", "claude",
               ["describís y construye", "frontend y backend", "sin equipo de desarrollo"],
               "construir ya es la parte fácil"),
    slide_tool("4.", "VERCEL", "LA PONE ONLINE", "vercel",
               ["tu app queda online", "gratis hasta que escales", "despliega en diez segundos"],
               "hacés push y ya está online"),
    slide_tool("5.", "STRIPE", "COBRA EL DINERO", "stripe",
               ["cobrá desde el día uno", "suscripciones resueltas", "los pagos llegan solos"],
               "cobrá antes de sentirte listo"),
    slide_tool("6.", "RESEND", "LE ESCRIBE A LA LISTA", "resend",
               ["calienta la lista de espera", "el lanzamiento llega a la bandeja", "la lista es tuya"],
               "el mail le gana a cualquier algoritmo"),
    slide_tool("7.", "LOOM", "PARA LA DEMO", "loom",
               ["grabá sesenta segundos", "mostralo, no lo expliques", "un link, sin edición"],
               "la gente compra lo que puede ver"),
    slide_tool("8.", "META ADS", "TRAE LA GENTE", "meta",
               ["llegás a quien no te sigue", "probás con poco presupuesto", "el pago dice si sirve"],
               "la distribución se compra, no se espera"),
    slide_tool("9.", "POSTHOG", "MUESTRA LA VERDAD", "posthog",
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
