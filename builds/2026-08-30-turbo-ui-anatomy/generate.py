# -*- coding: utf-8 -*-
"""Carrusel STLabs — Anatomía UI Turbo (2 slides, móvil + flechas)."""
from __future__ import annotations

import base64
from pathlib import Path

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
V = "#00FFB2"
BG = "#0A0A0A"
TX = "#F2F2F2"
GY = "#9aa39c"

# Phone frame in slide coords (1080×1350) — grande para lectura en IG
PH = {"x": 315, "y": 188, "w": 450, "h": 880}
ANN_W = 268
ANN_L_X = 20
ANN_R_X = 1080 - 20 - ANN_W  # 792
WIRE_L_X = ANN_L_X + ANN_W + 4
WIRE_R_X = ANN_R_X - 4


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode()


def img_uri(name: str) -> str:
    return f"data:image/jpeg;base64,{b64(B / 'assets' / name)}"


def font_css() -> str:
    faces = [
        ("Impact", "Impact.ttf", 400, "normal"),
        ("Anton", "Anton-Regular.ttf", 400, "normal"),
        ("Bebas Neue", "BebasNeue-Regular.ttf", 400, "normal"),
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
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{b64(fp)}) format('truetype');}}"
        )
    return "\n".join(out)


CSS = f"""
{font_css()}
*{{box-sizing:border-box;margin:0;padding:0;-webkit-font-smoothing:subpixel-antialiased;text-rendering:optimizeLegibility;}}
html,body{{background:#000;}}
.sheet{{display:flex;flex-direction:column;gap:36px;padding:28px;width:max-content;}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;background:{BG};color:{TX};}}
.slide::before{{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:linear-gradient(rgba(0,255,178,.10) 1px,transparent 1px),
    linear-gradient(90deg,rgba(0,255,178,.10) 1px,transparent 1px);
  background-size:52px 52px;opacity:.35;}}
.slide::after{{content:'';position:absolute;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(ellipse 500px 400px at 50% 42%, rgba(0,255,178,.08), transparent 70%);}}

.head{{position:absolute;left:40px;right:40px;top:32px;z-index:12;text-align:center;}}
.kicker{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.16em;color:{GY};text-transform:uppercase;}}
.title{{font-family:'Impact','Anton',sans-serif;font-size:38px;line-height:.92;letter-spacing:.02em;
  text-transform:uppercase;color:{TX};margin-top:6px;}}
.title .g{{color:{V};}}
.sub{{font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:18px;color:{GY};margin-top:6px;line-height:1.15;}}

.stage{{position:absolute;inset:0;z-index:8;}}
.wires{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible;}}
.wires path{{fill:none;stroke:rgba(242,242,242,.72);stroke-width:2.5;}}
.wires circle{{fill:{V};stroke:{BG};stroke-width:1.5;}}

.phone{{position:absolute;left:{PH['x']}px;top:{PH['y']}px;width:{PH['w']}px;height:{PH['h']}px;z-index:6;}}
.phone-shell{{width:100%;height:100%;padding:12px;border-radius:52px;
  background:linear-gradient(145deg,#3a3e44,#121316,#080809,#151618);
  box-shadow:0 48px 96px rgba(0,0,0,.7),0 0 0 1.5px rgba(255,255,255,.1),inset 0 1px 0 rgba(255,255,255,.28);}}
.phone-bezel{{width:100%;height:100%;border-radius:42px;background:#050505;padding:9px;overflow:hidden;position:relative;}}
.phone-island{{position:absolute;top:16px;left:50%;transform:translateX(-50%);width:108px;height:28px;background:#000;border-radius:16px;z-index:3;}}
.phone-screen{{width:100%;height:100%;border-radius:34px;overflow:hidden;background:#0A0A0A;}}
.phone-screen img{{width:100%;height:100%;object-fit:cover;object-position:top center;display:block;}}
.phone-shine{{position:absolute;inset:0;border-radius:42px;pointer-events:none;
  background:linear-gradient(120deg,rgba(255,255,255,.14),transparent 28%,transparent 72%,rgba(255,255,255,.06));}}

.ann{{position:absolute;z-index:10;width:{ANN_W}px;}}
.ann-l{{text-align:right;padding-right:2px;}}
.ann-r{{text-align:left;padding-left:2px;}}
.ann-t{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:22px;color:{TX};line-height:1.12;margin-bottom:5px;}}
.ann ul{{list-style:none;font-family:'Barlow Condensed',sans-serif;font-weight:500;font-size:17px;color:{GY};line-height:1.32;}}
.ann li{{position:relative;padding-left:0;}}
.ann-l li::before{{content:'· ';color:{V};}}
.ann-r li::before{{content:'· ';color:{V};}}

.firma{{position:absolute;left:0;right:0;bottom:48px;text-align:center;z-index:20;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:22px;letter-spacing:.14em;color:{V};}}
.badge{{position:absolute;bottom:88px;left:50%;transform:translateX(-50%);z-index:20;
  display:flex;align-items:center;gap:10px;font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:{GY};}}
.badge .dot{{width:28px;height:28px;border-radius:50%;background:{V};box-shadow:0 0 12px rgba(0,255,178,.45);}}
.slide-num{{position:absolute;top:44px;right:48px;z-index:20;font-family:'IBM Plex Mono',monospace;font-size:13px;color:{GY};letter-spacing:.1em;}}
"""


def phone_html(img: str) -> str:
    return f"""<div class="phone">
  <div class="phone-shell">
    <div class="phone-bezel">
      <div class="phone-island"></div>
      <div class="phone-screen"><img src="{img}" alt=""/></div>
      <div class="phone-shine"></div>
    </div>
  </div>
</div>"""


def ann_html(side: str, top: int, title: str, bullets: list[str]) -> str:
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    cls = "ann ann-l" if side == "l" else "ann ann-r"
    x = ANN_L_X if side == "l" else ANN_R_X
    return f'<div class="{cls}" style="left:{x}px;top:{top}px"><div class="ann-t">{title}</div><ul>{lis}</ul></div>'


def wire_path(side: str, box_y: int, ax: float, ay: float) -> str:
    """Curved connector from annotation box to phone anchor (ax, ay are 0–1 in phone)."""
    px = PH["x"] + PH["w"] * ax
    py = PH["y"] + PH["h"] * ay
    if side == "l":
        x1, y1 = WIRE_L_X, box_y + 34
        cx, cy = x1 + 36, (y1 + py) / 2
    else:
        x1, y1 = WIRE_R_X, box_y + 34
        cx, cy = x1 - 36, (y1 + py) / 2
    return f'<path d="M{x1},{y1} Q{cx},{cy} {px},{py}"/><circle cx="{px}" cy="{py}" r="5.5"/>'


def wires_svg(items: list[tuple]) -> str:
    paths = "".join(wire_path(s, top, ax, ay) for s, top, ax, ay, _, _ in items)
    return f'<svg class="wires" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{paths}</svg>'


def anatomy_slide(
    num: int,
    total: int,
    kicker: str,
    title: str,
    sub: str,
    img: str,
    items: list[tuple],
) -> str:
    """item: (side, top_px, ax, ay, title, [bullets])"""
    anns = "".join(ann_html(s, top, t, bs) for s, top, ax, ay, t, bs in items)
    return f"""<div class="slide">
  <div class="slide-num">{num:02d} / {total:02d}</div>
  <div class="head">
    <div class="kicker">{kicker}</div>
    <div class="title">{title}</div>
    <div class="sub">{sub}</div>
  </div>
  <div class="stage">
    {wires_svg(items)}
    {anns}
    {phone_html(img)}
  </div>
  <div class="badge"><span class="dot"></span> SISTEMA TURBO · sebastian.stlabs.ar</div>
  <div class="firma">sebastian.stlabs.ar</div>
</div>"""


SLIDE_1_ITEMS = [
    ("l", 208, 0.50, 0.06, "Navegación", ["Menú e inicio", "Acceso al tablero"]),
    ("l", 288, 0.28, 0.28, "Pendientes", ["Sin contactar", "Tu cola de trabajo"]),
    ("l", 378, 0.28, 0.42, "Contactados", ["Ya respondieron", "Seguimiento activo"]),
    ("r", 288, 0.72, 0.28, "Vencidos", ["Seguimientos atrasados", "Pedís acción"]),
    ("r", 378, 0.72, 0.42, "Ganados", ["Ventas cerradas", "Conversión"]),
    ("r", 478, 0.50, 0.56, "Esta semana", ["Nuevos vs anterior", "Contactos"]),
    ("r", 578, 0.50, 0.82, "Tendencia", ["Por día · 30 días", "Nuevos y contactos"]),
]

SLIDE_2_ITEMS = [
    ("l", 208, 0.50, 0.10, "Turbo · chat", ["Qué vendés y a quién", "Define tu mercado"]),
    ("l", 308, 0.50, 0.26, "Sugerencias", ["Ejemplos para arrancar", "Un tap y seguís"]),
    ("l", 408, 0.50, 0.36, "Tu mensaje", ["Escribí el brief", "Turbo arma el plan"]),
    ("r", 288, 0.72, 0.48, "Aprobar y buscar", ["Lanza prospección", "Cuando cierra"]),
    ("r", 398, 0.50, 0.58, "Plan de caza", ["Dónde · cuántos", "Costo y tiempo"]),
    ("r", 508, 0.50, 0.74, "Requisitos extra", ["Solo WhatsApp", "Web · rubro"]),
    ("r", 618, 0.50, 0.88, "Filtros", ["Sacá lo que no cierra", "Pedile cambios"]),
]


def main() -> None:
    slides = [
        anatomy_slide(
            1,
            2,
            "TURBO · PANEL DE INICIO",
            'ESTRUCTURA DEL<br><span class="g">TABLERO</span>',
            "Así leés el estado de tu prospección en segundos.",
            img_uri("screen-inicio.jpg"),
            SLIDE_1_ITEMS,
        ),
        anatomy_slide(
            2,
            2,
            "TURBO · PROSPECCIÓN",
            'ESTRUCTURA DEL<br><span class="g">FLUJO</span>',
            "Brief, chat y filtros en un solo flujo.",
            img_uri("screen-prospeccion.jpg"),
            SLIDE_2_ITEMS,
        ),
    ]
    html = f"""<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<title>STLabs — Anatomía UI Turbo</title>
<style>{CSS}</style>
</head><body><div class="sheet">{''.join(slides)}</div></body></html>"""
    (B / "carrusel.html").write_text(html, encoding="utf-8")
    print("OK", len(slides), "slides →", B / "carrusel.html")


if __name__ == "__main__":
    main()
