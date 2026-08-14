# -*- coding: utf-8 -*-
"""10 historias independientes — frases de impacto (estilo 04/07).
Fondos variados: roca · grilla verde · puntos ordenados.
Sin kicker NOTA · sin foto.
"""
from pathlib import Path
import base64
import json
import math

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent
TEX = OUT / "textures"


def rock_b64(name: str) -> str:
    return base64.b64encode((TEX / name).read_bytes()).decode("ascii")


# Mantener 04 (miedo) y 07 (imperfecto). Resto reescrito al mismo ritmo punchy.
STORIES = [
    {
        "id": "excusa",
        "bg": "rock",
        "rock": "rock-0.png",
        "lines": [
            {"t": "Tu excusa suena lógica.", "c": "w"},
            {"t": "Tu resultado,", "c": "muted"},
            {"t": "no.", "c": "g"},
        ],
        "apoyo": "La verdad duele menos que mentirte.",
        "align": "left",
        "accent": "tr",
        "size": "lg",
    },
    {
        "id": "manana",
        "bg": "grid",
        "lines": [
            {"t": "Mañana es un lugar", "c": "w"},
            {"t": "donde no vive nadie.", "c": "g"},
        ],
        "apoyo": "Lo que importa, se hace hoy.",
        "align": "left",
        "accent": "tl",
        "size": "lg",
    },
    {
        "id": "empujon",
        "bg": "dots",
        "lines": [
            {"t": "Nadie te debe", "c": "w"},
            {"t": "un empujón.", "c": "w"},
            {"t": "El primero", "c": "muted"},
            {"t": "lo das vos.", "c": "g"},
        ],
        "apoyo": "Esperar permiso es quedarte quieto.",
        "align": "left",
        "accent": "br",
        "size": "lg",
    },
    {
        "id": "miedo",
        "bg": "rock",
        "rock": "rock-2.png",
        "lines": [
            {"t": "Tu miedo", "c": "w"},
            {"t": "no es un freno.", "c": "w"},
            {"t": "Es una brújula", "c": "muted"},
            {"t": "mal leída.", "c": "g"},
        ],
        "apoyo": "Si te asusta, probablemente importa.",
        "align": "center",
        "accent": "bl",
        "size": "lg",
    },
    {
        "id": "achica",
        "bg": "grid",
        "lines": [
            {"t": "La zona de confort", "c": "w"},
            {"t": "no te protege:", "c": "muted"},
            {"t": "te achica.", "c": "g"},
        ],
        "apoyo": "Si no te incomoda, no te movés.",
        "align": "left",
        "accent": "tr",
        "size": "lg",
    },
    {
        "id": "dudar",
        "bg": "dots",
        "lines": [
            {"t": "Dudar no es pensar.", "c": "w"},
            {"t": "Es posponer", "c": "muted"},
            {"t": "con estilo.", "c": "g"},
        ],
        "apoyo": "Decidir limpia más que analizar.",
        "align": "left",
        "accent": "tl",
        "size": "lg",
    },
    {
        "id": "imperfecto",
        "bg": "rock",
        "rock": "rock-3.png",
        "lines": [
            {"t": "Empezá imperfecto.", "c": "g"},
            {"t": "Terminá imposible", "c": "w"},
            {"t": "si seguís esperando.", "c": "w"},
        ],
        "apoyo": "Lo perfecto es la excusa más cara.",
        "align": "center",
        "accent": "br",
        "size": "lg",
    },
    {
        "id": "talento",
        "bg": "grid",
        "lines": [
            {"t": "No te falta talento.", "c": "w"},
            {"t": "Te falta", "c": "muted"},
            {"t": "decidirte.", "c": "g"},
        ],
        "apoyo": "El talento sin acción no pesa.",
        "align": "left",
        "accent": "bl",
        "size": "lg",
    },
    {
        "id": "mapa",
        "bg": "dots",
        "lines": [
            {"t": "El mapa completo", "c": "w"},
            {"t": "no existe", "c": "muted"},
            {"t": "al principio.", "c": "g"},
        ],
        "apoyo": "Se dibuja mientras caminás.",
        "align": "left",
        "accent": "tr",
        "size": "lg",
    },
    {
        "id": "arriesgar",
        "bg": "rock",
        "rock": "rock-1.png",
        "lines": [
            {"t": "Arrepentirte duele más", "c": "w"},
            {"t": "que equivocarte.", "c": "g"},
        ],
        "apoyo": "El costo de mirar de lejos siempre sube.",
        "align": "center",
        "accent": "tl",
        "size": "lg",
    },
]


def ordered_dots_field(cols: int = 14, rows: int = 26) -> str:
    """Campo de puntos ordenados sutiles en toda la historia."""
    html = ['<div class="dots-field">']
    pad_x, pad_y = 56, 72
    usable_w, usable_h = 1080 - pad_x * 2, 1920 - pad_y * 2
    for r in range(rows):
        for c in range(cols):
            x = pad_x + (c + 0.5) * (usable_w / cols)
            y = pad_y + (r + 0.5) * (usable_h / rows)
            # sutil: más tenues hacia el centro del texto
            cx, cy = 540, 900
            dist = math.hypot(x - cx, y - cy) / 1100
            op = 0.16 + 0.28 * min(1.0, dist)
            size = 2.8 + 1.6 * min(1.0, dist)
            html.append(
                f'<span style="left:{x - size/2:.1f}px;top:{y - size/2:.1f}px;'
                f'width:{size:.1f}px;height:{size:.1f}px;opacity:{op:.3f};"></span>'
            )
    html.append("</div>")
    return "".join(html)


def claim_html(lines: list) -> str:
    parts = []
    for ln in lines:
        cls = {"w": "w", "g": "g", "muted": "muted"}[ln["c"]]
        parts.append(f'<span class="{cls}">{ln["t"]}</span>')
    return "<br>".join(parts)


def bg_layers(c: dict) -> str:
    kind = c["bg"]
    if kind == "rock":
        b64 = rock_b64(c["rock"])
        return f'''
        <div class="tex-rock" style="background-image:url('data:image/png;base64,{b64}');"></div>
        <div class="wash rock-wash"></div>
        <div class="stain"></div>
        <div class="edge"></div>'''
    if kind == "grid":
        return '''
        <div class="reticula"></div>
        <div class="wash"></div>
        <div class="stain"></div>
        <div class="edge"></div>'''
    # dots ordenados
    return f'''
        <div class="wash soft"></div>
        <div class="stain"></div>
        {ordered_dots_field()}
        <div class="edge"></div>'''


def slide(c: dict) -> str:
    return f'''
    <div class="slide accent-{c['accent']} align-{c['align']} size-{c['size']} bg-{c['bg']}" data-id="{c['id']}">
      <div class="bg">
        {bg_layers(c)}
      </div>
      <div class="safe">
        <h1 class="claim">{claim_html(c['lines'])}</h1>
        <div class="rule"></div>
        <p class="apoyo">{c['apoyo']}</p>
      </div>
      <div class="firma">sebastian.stlabs.ar</div>
    </div>'''


CSS = f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype'); }}
@font-face {{ font-family:'Lora'; src:url('file://{FONTS}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }}

* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1920px; overflow:hidden;
  background:#0A0A0A;
}}
.bg {{ position:absolute; inset:0; }}

.tex-rock {{
  position:absolute; inset:0; z-index:1;
  background-size:cover; background-position:center;
  filter: grayscale(1) contrast(1.15) brightness(.42);
  opacity:.95;
}}
.rock-wash {{
  position:absolute; inset:0; z-index:2;
  background:
    radial-gradient(ellipse 85% 50% at 50% 40%, rgba(0,255,178,.07) 0%, transparent 55%),
    linear-gradient(180deg, rgba(10,10,10,.55) 0%, rgba(10,10,10,.72) 45%, rgba(0,0,0,.88) 100%);
}}

.reticula {{
  position:absolute; inset:0; z-index:1;
  background-image:
    linear-gradient(rgba(0,255,178,.11) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.11) 1px, transparent 1px);
  background-size:56px 56px;
  opacity:.85;
}}
.wash {{
  position:absolute; inset:0; z-index:2;
  background:
    radial-gradient(ellipse 90% 55% at 50% 38%, rgba(0,255,178,.06) 0%, transparent 55%),
    linear-gradient(180deg, rgba(10,10,10,.12) 0%, rgba(10,10,10,.4) 50%, rgba(0,0,0,.75) 100%);
}}
.wash.soft {{
  background:
    radial-gradient(ellipse 80% 50% at 50% 42%, rgba(0,255,178,.05) 0%, transparent 60%),
    linear-gradient(180deg, rgba(10,10,10,.2) 0%, rgba(10,10,10,.45) 55%, rgba(0,0,0,.78) 100%);
}}

.edge {{
  position:absolute; inset:36px; z-index:3; pointer-events:none;
  border:1px solid rgba(0,255,178,.14);
}}
.accent-tl .stain {{ left:-240px; top:-220px; }}
.accent-tr .stain {{ right:-240px; top:-220px; left:auto; }}
.accent-bl .stain {{ left:-240px; bottom:-200px; top:auto; }}
.accent-br .stain {{ right:-240px; bottom:-200px; left:auto; top:auto; }}
.stain {{
  position:absolute; width:820px; height:820px; border-radius:50%;
  background: radial-gradient(circle, rgba(0,255,178,.32) 0%, rgba(0,255,178,.09) 44%, transparent 72%);
  filter: blur(10px); pointer-events:none; z-index:2;
}}
.bg-rock .stain {{ opacity:.55; }}

.dots-field {{ position:absolute; inset:0; z-index:4; pointer-events:none; }}
.dots-field span {{
  position:absolute; border-radius:50%; background:#00FFB2;
}}

.safe {{
  position:absolute; left:88px; right:88px; top:260px; bottom:360px;
  display:flex; flex-direction:column; justify-content:center;
  z-index:6;
}}
.align-left .safe {{ align-items:flex-start; text-align:left; }}
.align-center .safe {{ align-items:center; text-align:center; }}
.align-center .rule {{ margin-left:auto; margin-right:auto; }}

.claim {{
  font-family:'Bebas Neue', Impact, sans-serif;
  letter-spacing:.01em; color:#F2F2F2; max-width:920px;
}}
.size-lg .claim {{ font-size:104px; line-height:.92; }}
.size-md .claim {{ font-size:88px; line-height:.94; }}
.claim .w {{ color:#F2F2F2; }}
.claim .g {{
  color:#00FFB2;
  text-shadow:0 0 28px rgba(0,255,178,.28);
}}
.claim .muted {{
  color:#9aa39c;
  font-family:'Lora', Georgia, serif;
  font-style:italic;
  font-weight:600;
  font-size:0.72em;
  letter-spacing:0;
  display:inline-block;
  margin:6px 0 2px;
}}
.align-center .claim .muted {{ display:block; }}

.rule {{
  width:112px; height:5px; background:#00FFB2; border-radius:2px;
  margin:36px 0 24px; box-shadow:0 0 14px rgba(0,255,178,.4);
}}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:34px;
  line-height:1.35; color:#9aa39c; max-width:780px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:7;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.14em; color:#00FFB2; opacity:.92;
}}
"""


def main():
    slides = "".join(slide(c) for c in STORIES)
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Historias frases impacto STLabs</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    (OUT / "historias.html").write_text(html, encoding="utf-8")
    (OUT / "index.json").write_text(json.dumps(STORIES, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(STORIES)} stories · fondos: rock/grid/dots · sin NOTA")


if __name__ == "__main__":
    main()
