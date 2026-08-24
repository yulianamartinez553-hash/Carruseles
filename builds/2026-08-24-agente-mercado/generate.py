# -*- coding: utf-8 -*-
"""Carrusel STLabs — Agente a medida (8 slides).
Modo negro · foto Turbo + degradé · familia manifiesto · CTA AGENTE.
"""
from __future__ import annotations

import base64
import json
from pathlib import Path

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
ASSETS = B / "assets"
V = "#00FFB2"
BG = "#0A0A0A"
TX = "#F2F2F2"
GY = "#9aa39c"
CARD = "#141414"
CARD2 = "#1E1E1E"
BDR = "rgba(255,255,255,.14)"


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def font_css() -> str:
    faces = [
        ("Poppins", "Poppins-ExtraBold.ttf", 800, "normal"),
        ("Poppins", "Poppins-Bold.ttf", 700, "normal"),
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


TURBO_URI = f"data:image/png;base64,{b64(ASSETS / 'turbo.png')}"

# Piedra/roca oscura
STONE = (
    "url(\"data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'>"
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='4' stitchTiles='stitch'/>"
    "<feColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.07 0'/></filter>"
    "<rect width='100%25' height='100%25' filter='url(%23n)'/></svg>\")"
)


CSS = f"""
{font_css()}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    radial-gradient(ellipse 70% 45% at 90% 0%, rgba(0,255,178,.07), transparent 55%),
    radial-gradient(ellipse 55% 40% at 0% 100%, rgba(0,255,178,.04), transparent 50%),
    {STONE};
  mix-blend-mode:overlay;opacity:.85;}}
.frame{{position:absolute;inset:36px;border:1.5px solid rgba(255,255,255,.1);z-index:4;pointer-events:none;}}
.firma{{position:absolute;left:0;right:0;bottom:56px;text-align:center;z-index:30;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;letter-spacing:.14em;color:{V};}}
.content{{position:absolute;left:72px;right:72px;top:88px;bottom:120px;z-index:8;
  display:flex;flex-direction:column;}}

/* Turbo: marca de agua chica, arriba-derecha, discreta pero legible */
.turbo{{position:absolute;z-index:3;right:54px;top:96px;width:152px;height:152px;
  pointer-events:none;opacity:.30;
  -webkit-mask-image:radial-gradient(ellipse 75% 75% at 50% 48%, #000 25%, transparent 72%);
  mask-image:radial-gradient(ellipse 75% 75% at 50% 48%, #000 25%, transparent 72%);}}
.turbo img{{width:100%;height:100%;object-fit:contain;display:block;
  filter:brightness(.62) contrast(1.05) saturate(.7);}}
.turbo::after{{content:'';position:absolute;inset:-12%;pointer-events:none;
  background:radial-gradient(ellipse 48% 48% at 50% 48%, rgba(0,255,178,.07), transparent 70%);}}
.slide.has-photo .frame{{border-color:rgba(255,255,255,.12);}}
.slide.has-photo .content{{z-index:8;}}

.kicker{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:18px;letter-spacing:.2em;
  text-transform:uppercase;color:{V};margin-bottom:20px;}}
.title{{font-family:'Poppins',sans-serif;font-weight:800;font-size:76px;line-height:.94;
  letter-spacing:-.03em;text-transform:uppercase;text-align:left;color:{TX};}}
.title.md{{font-size:64px;}}
.title.sm{{font-size:56px;}}
/* @degradé en display */
.grad{{background:linear-gradient(180deg,#B0FFE8 0%,#00FFB2 42%,#007A52 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.grad2{{background:linear-gradient(180deg,#FFFFFF 0%,#E0FFF6 22%,#00FFB2 62%,#009E6E 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.lead{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:34px;line-height:1.25;
  color:{GY};margin-top:22px;max-width:900px;text-align:left;}}
.lead b{{color:{TX};font-weight:700;}}
.spacer{{flex:1 1 auto;min-height:12px;}}
.badge{{display:inline-block;margin-top:18px;padding:14px 20px;border:2px solid {V};
  font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:18px;letter-spacing:.14em;
  text-transform:uppercase;color:{TX};background:rgba(0,255,178,.12);}}
.chips{{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px;}}
.chip{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.1em;
  text-transform:uppercase;padding:12px 16px;border:1.5px solid {BDR};background:rgba(20,20,20,.85);}}
.chip.on{{border-color:{V};background:rgba(0,255,178,.12);color:{TX};}}
.list{{display:flex;flex-direction:column;gap:14px;}}
.row{{display:flex;gap:16px;align-items:flex-start;padding:18px 20px;border:1.5px solid {BDR};background:{CARD};}}
.row .ix{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:18px;color:{V};
  letter-spacing:.08em;min-width:40px;padding-top:4px;}}
.row .t{{font-family:'Poppins',sans-serif;font-weight:800;font-size:26px;line-height:1.12;
  text-transform:uppercase;letter-spacing:-.015em;}}
.row .d{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:26px;line-height:1.25;
  color:{GY};margin-top:4px;}}
.stat{{display:flex;gap:18px;align-items:flex-start;padding:8px 0;}}
.stat .n{{font-family:'Poppins',sans-serif;font-weight:800;font-size:54px;line-height:1;color:{V};min-width:70px;}}
.stat .t{{font-family:'Poppins',sans-serif;font-weight:800;font-size:26px;line-height:1.12;text-transform:uppercase;letter-spacing:-.015em;}}
.stat .d{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:26px;line-height:1.25;color:{GY};margin-top:4px;}}
.rule{{height:1.5px;background:rgba(255,255,255,.12);margin:10px 0;}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:14px;}}
.panel{{border:1.5px solid {BDR};background:{CARD};padding:20px 22px;}}
.panel .lab{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.16em;
  text-transform:uppercase;color:rgba(242,242,242,.42);margin-bottom:8px;}}
.panel .t{{font-family:'Poppins',sans-serif;font-weight:800;font-size:26px;line-height:1.1;
  text-transform:uppercase;letter-spacing:-.02em;}}
.panel .d{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:24px;line-height:1.25;
  color:{GY};margin-top:8px;}}
.warn{{border-left:5px solid {V};padding:20px 24px;background:rgba(0,255,178,.1);margin-top:8px;}}
.warn .t{{font-family:'Poppins',sans-serif;font-weight:800;font-size:28px;line-height:1.15;text-transform:uppercase;}}
.warn .d{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:28px;line-height:1.28;color:{GY};margin-top:8px;}}
.cta{{margin-top:auto;border:2.5px solid {V};background:rgba(0,255,178,.1);padding:32px 28px;text-align:center;}}
.cta .kw{{font-family:'Poppins',sans-serif;font-weight:800;font-size:78px;letter-spacing:.06em;line-height:1;
  background:linear-gradient(180deg,#B0FFE8 0%,#00FFB2 42%,#007A52 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.cta .hint{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:30px;color:{GY};margin-top:14px;}}
"""


def chrome() -> str:
    return '<div class="frame"></div><div class="firma">sebastian.stlabs.ar</div>'


def slide(body: str, photo: bool = False) -> str:
    cls = "slide has-photo" if photo else "slide"
    turbo = (
        f'<div class="turbo" aria-hidden="true"><img src="{TURBO_URI}" alt=""/></div>'
        if photo
        else ""
    )
    return f'<div class="{cls}">{turbo}{chrome()}<div class="content">{body}</div></div>'


SLIDES = [
    slide(
        """
<div class="kicker">SEÑAL DE MERCADO</div>
<div class="title">TU EMPRESA<br>DECIDE A<br><span class="grad">CIEGAS</span></div>
<div class="lead">Mientras el mercado se mueve, vos seguís operando con intuición y reportes viejos.</div>
<div class="spacer"></div>
<div class="badge">AGENTE</div>
<div class="chips">
  <div class="chip on">A MEDIDA</div>
  <div class="chip">LEE TU MERCADO</div>
  <div class="chip">MEJORA LO DE HOY</div>
</div>
""",
        photo=True,
    ),
    slide(
        """
<div class="kicker">EL PROBLEMA</div>
<div class="title md">NO TE FALTA<br>DATO.<br><span class="grad">TE FALTA LECTURA</span></div>
<div class="spacer"></div>
<div class="list">
  <div class="row"><div class="ix">01</div><div><div class="t">Info atrasada</div><div class="d">Cuando llega al comité, la ventana ya se cerró.</div></div></div>
  <div class="row"><div class="ix">02</div><div><div class="t">Señales sueltas</div><div class="d">CRM, anuncios, soporte y finanzas no conversan entre sí.</div></div></div>
  <div class="row"><div class="ix">03</div><div><div class="t">Decisión a ojo</div><div class="d">Priorizás por costumbre, no por presión real del mercado.</div></div></div>
</div>
"""
    ),
    slide(
        """
<div class="kicker">EL COSTO DE NO VER</div>
<div class="title md">CADA SEMANA<br>SIN LECTURA<br><span class="grad">TE SALE CARA</span></div>
<div class="spacer"></div>
<div class="stat"><div class="n">01</div><div><div class="t">Oportunidades que se van</div><div class="d">Un competidor se mueve y vos te enterás cuando el cierre ya está perdido.</div></div></div>
<div class="rule"></div>
<div class="stat"><div class="n">02</div><div><div class="t">Presupuesto mal apuntado</div><div class="d">Invertís donde “siempre funcionó”, no donde hoy hay demanda.</div></div></div>
<div class="rule"></div>
<div class="stat"><div class="n">03</div><div><div class="t">Equipo reaccionando</div><div class="d">Apagan incendios en vez de anticipar la siguiente jugada.</div></div></div>
"""
    ),
    slide(
        """
<div class="kicker">LA SOLUCIÓN</div>
<div class="title md">TE ARMO UN<br><span class="grad2">AGENTE A MEDIDA</span></div>
<div class="lead">No un asistente genérico. Un sistema entrenado en <b>tu</b> mercado, <b>tus</b> datos y <b>tu</b> forma de vender.</div>
<div class="spacer"></div>
<div class="grid2">
  <div class="panel"><div class="lab">CAPA 01</div><div class="t">Mercado</div><div class="d">Competencia, demanda, precios, momento.</div></div>
  <div class="panel"><div class="lab">CAPA 02</div><div class="t">Situación</div><div class="d">Embudo, fricción, capacidad, caja.</div></div>
  <div class="panel"><div class="lab">CAPA 03</div><div class="t">Prioridad</div><div class="d">Qué mover esta semana y qué dejar.</div></div>
  <div class="panel"><div class="lab">CAPA 04</div><div class="t">Acción</div><div class="d">Recomendación clara para el equipo.</div></div>
</div>
"""
    ),
    slide(
        """
<div class="kicker">CAPA MERCADO</div>
<div class="title md">LEE LO QUE<br>PASA AFUERA<br><span class="grad">ANTES QUE VOS</span></div>
<div class="spacer"></div>
<div class="list">
  <div class="row"><div class="ix">→</div><div><div class="t">Movimientos del sector</div><div class="d">Cambios de oferta, precio y posicionamiento de competidores.</div></div></div>
  <div class="row"><div class="ix">→</div><div><div class="t">Demanda real</div><div class="d">Qué están buscando tus clientes ahora, no el trimestre pasado.</div></div></div>
  <div class="row"><div class="ix">→</div><div><div class="t">Ventanas de momento</div><div class="d">Cuándo conviene empujar, pausar o reposicionar.</div></div></div>
</div>
"""
    ),
    slide(
        """
<div class="kicker">CAPA SITUACIÓN</div>
<div class="title md">CRUZA ESO<br>CON LO QUE<br><span class="grad">PASA ADENTRO</span></div>
<div class="spacer"></div>
<div class="grid2">
  <div class="panel"><div class="lab">EMBUDO</div><div class="t">Dónde se traba</div><div class="d">Etapas lentas, oportunidades muertas, tasa de cierre por segmento.</div></div>
  <div class="panel"><div class="lab">OPERACIÓN</div><div class="t">Capacidad real</div><div class="d">Qué puede absorber el equipo sin romper calidad.</div></div>
  <div class="panel"><div class="lab">COMERCIAL</div><div class="t">Fricción de venta</div><div class="d">Objeciones, ciclos largos, traspaso roto.</div></div>
  <div class="panel"><div class="lab">RESULTADO</div><div class="t">Prioridad única</div><div class="d">Una jugada clara para esta semana.</div></div>
</div>
"""
    ),
    slide(
        """
<div class="kicker">EL RESULTADO</div>
<div class="title md">DEJÁS DE<br>ADIVINAR.<br><span class="grad2">EMPEZÁS A MEJORAR</span></div>
<div class="spacer"></div>
<div class="warn">
  <div class="t">Cada mañana: qué cambió y qué hacer</div>
  <div class="d">El agente te deja prioridades accionables sobre mercado + situación interna — no otro tablero para mirar.</div>
</div>
<div class="rule"></div>
<div class="chips">
  <div class="chip on">MEJOR FOCO</div>
  <div class="chip on">MEJOR MOMENTO</div>
  <div class="chip on">MEJOR MARGEN</div>
</div>
"""
    ),
    slide(
        """
<div class="kicker">PRÓXIMO PASO</div>
<div class="title md">¿QUERÉS UN<br>AGENTE QUE<br><span class="grad">LEA TU REALIDAD?</span></div>
<div class="lead">Te armo uno a medida de tu mercado y de cómo opera tu empresa hoy.</div>
<div class="spacer"></div>
<div class="cta">
  <div class="kw">AGENTE</div>
  <div class="hint">Comentá la palabra y te escribo para mapear tu caso</div>
</div>
""",
        photo=True,
    ),
]


def main() -> None:
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Agente a medida</title>
<style>{CSS}</style>
</head><body>
<div class="sheet">
{''.join(SLIDES)}
</div>
</body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")

    meta = {
        "id": "2026-08-24-agente-mercado",
        "fecha": "2026-08-24",
        "titulo": "Agente a medida que lee tu mercado",
        "slides": 8,
        "fondo": "roca_volcanica",
        "familia_visual": "manifiesto",
        "origen": "original",
        "keyword_portada": "AGENTE",
        "modo": "negro",
        "cta": "AGENTE",
        "notas": "Foto Turbo + degradé en títulos display; portada y CTA con scrim",
    }
    (B / "manifest.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("OK 8 slides negro+turbo →", B / "carrusel.html")


if __name__ == "__main__":
    main()
