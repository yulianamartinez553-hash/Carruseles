# -*- coding: utf-8 -*-
"""10 historias — frases duras e impactantes.
Estilo unificado: negro + textura rocosa + mancha/puntos de esquina.
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


# Frases motivacionales, impactantes y duras. Mantener ritmo punchy.
STORIES = [
    {
        "id": "excusa",
        "rock": "rock-0.png",
        "lines": [
            {"t": "Tu excusa suena lógica.", "c": "w"},
            {"t": "Tu vida,", "c": "muted"},
            {"t": "no.", "c": "g"},
        ],
        "apoyo": "La mentira más cara es la que te contás vos.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "lg",
    },
    {
        "id": "manana",
        "rock": "rock-1.png",
        "lines": [
            {"t": "Mañana es el cementerio", "c": "w"},
            {"t": "de todo lo que", "c": "muted"},
            {"t": "podías hacer hoy.", "c": "g"},
        ],
        "apoyo": "Si lo postergás, ya lo enterraste.",
        "align": "left",
        "accent": "tl",
        "dots": "br",
        "size": "md",
    },
    {
        "id": "empujon",
        "rock": "rock-2.png",
        "lines": [
            {"t": "Nadie viene a salvarte.", "c": "w"},
            {"t": "Y eso", "c": "muted"},
            {"t": "te obliga a moverte.", "c": "g"},
        ],
        "apoyo": "La dependencia es otra forma de quedar quieto.",
        "align": "left",
        "accent": "br",
        "dots": "tl",
        "size": "lg",
    },
    {
        "id": "miedo",
        "rock": "rock-3.png",
        "lines": [
            {"t": "Tu miedo", "c": "w"},
            {"t": "no es un freno.", "c": "w"},
            {"t": "Es una brújula", "c": "muted"},
            {"t": "mal leída.", "c": "g"},
        ],
        "apoyo": "Si te asusta, probablemente importa.",
        "align": "center",
        "accent": "bl",
        "dots": "tr",
        "size": "lg",
    },
    {
        "id": "confort",
        "rock": "rock-4.png",
        "lines": [
            {"t": "Tu zona de confort", "c": "w"},
            {"t": "no es un refugio.", "c": "muted"},
            {"t": "Es una jaula.", "c": "g"},
        ],
        "apoyo": "Si no te incomoda, no estás avanzando.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "lg",
    },
    {
        "id": "dudar",
        "rock": "rock-0.png",
        "lines": [
            {"t": "Dudar no es inteligencia.", "c": "w"},
            {"t": "Es miedo", "c": "muted"},
            {"t": "disfrazado de cuidado.", "c": "g"},
        ],
        "apoyo": "Decidir limpia. Analizar infinito ensucia.",
        "align": "left",
        "accent": "tl",
        "dots": "br",
        "size": "md",
    },
    {
        "id": "imperfecto",
        "rock": "rock-2.png",
        "lines": [
            {"t": "Empezá imperfecto.", "c": "g"},
            {"t": "Terminá imposible", "c": "w"},
            {"t": "si seguís esperando.", "c": "w"},
        ],
        "apoyo": "Lo perfecto es la excusa más cara.",
        "align": "center",
        "accent": "br",
        "dots": "tl",
        "size": "lg",
    },
    {
        "id": "talento",
        "rock": "rock-1.png",
        "lines": [
            {"t": "No te falta potencial.", "c": "w"},
            {"t": "Te sobra", "c": "muted"},
            {"t": "cobardía elegante.", "c": "g"},
        ],
        "apoyo": "El talento sin decisión no pesa nada.",
        "align": "left",
        "accent": "bl",
        "dots": "tr",
        "size": "lg",
    },
    {
        "id": "paso",
        "rock": "rock-3.png",
        "lines": [
            {"t": "No necesitás más claridad.", "c": "w"},
            {"t": "Necesitás", "c": "muted"},
            {"t": "más coraje.", "c": "g"},
        ],
        "apoyo": "La claridad llega después del primer golpe.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "lg",
    },
    {
        "id": "arriesgar",
        "rock": "rock-4.png",
        "lines": [
            {"t": "Arrepentirte duele más", "c": "w"},
            {"t": "que equivocarte.", "c": "g"},
        ],
        "apoyo": "Mirar de lejos también es una decisión. La peor.",
        "align": "center",
        "accent": "tl",
        "dots": "br",
        "size": "lg",
    },
]


def dots_gradient(corner: str, seed: int = 1, w: int = 1080, h: int = 1920) -> str:
    origins = {
        "tl": (0, 0),
        "tr": (w, 0),
        "bl": (0, h),
        "br": (w, h),
    }
    ox, oy = origins[corner]
    max_r = 680
    rings = [
        (28, 8, 15, 0.92),
        (70, 12, 12, 0.80),
        (120, 15, 10, 0.66),
        (180, 18, 8, 0.50),
        (250, 22, 6.5, 0.36),
        (340, 24, 5, 0.24),
        (440, 22, 3.8, 0.14),
        (560, 18, 2.8, 0.07),
    ]
    html = ['<div class="dots">']

    def place(x, y, size, op):
        html.append(
            f'<span style="left:{x - size/2:.1f}px;top:{y - size/2:.1f}px;'
            f'width:{size:.1f}px;height:{size:.1f}px;opacity:{op:.3f};"></span>'
        )

    def xy(a, r):
        if corner == "tl":
            return ox + math.cos(a) * r, oy + math.sin(a) * r
        if corner == "tr":
            return ox - math.sin(a) * r, oy + math.cos(a) * r
        if corner == "bl":
            return ox + math.sin(a) * r, oy - math.cos(a) * r
        return ox - math.cos(a) * r, oy - math.sin(a) * r

    n = 0
    for r_base, count, size_max, op_max in rings:
        for i in range(count):
            t = i / max(count - 1, 1)
            a = t * (math.pi / 2) * 0.95 + 0.03 + (seed % 7) * 0.008
            jitter = (((n * 41 + seed * 19) % 31) - 15) * 1.5
            r = max(10, r_base + jitter)
            dist_factor = max(0.0, 1.0 - r / max_r)
            size = size_max * (0.35 + 0.65 * dist_factor)
            op = op_max * (0.3 + 0.7 * dist_factor)
            x, y = xy(a, r)
            place(x, y, size, op)
            n += 1

    for i in range(50):
        t = ((i * 17 + seed * 3) % 100) / 100
        a = t * (math.pi / 2) * 0.96 + 0.02
        r = 100 + ((i * 53 + seed * 11) % 520)
        dist_factor = max(0.0, 1.0 - r / (max_r + 40))
        size = 2.0 + 6.5 * dist_factor
        op = 0.02 + 0.28 * dist_factor
        x, y = xy(a, r)
        place(x, y, size, op)

    html.append("</div>")
    return "".join(html)


def claim_html(lines: list) -> str:
    parts = []
    for ln in lines:
        cls = {"w": "w", "g": "g", "muted": "muted"}[ln["c"]]
        parts.append(f'<span class="{cls}">{ln["t"]}</span>')
    return "<br>".join(parts)


def slide(c: dict, idx: int) -> str:
    b64 = rock_b64(c["rock"])
    return f'''
    <div class="slide accent-{c['accent']} align-{c['align']} size-{c['size']}" data-id="{c['id']}">
      <div class="bg">
        <div class="tex-rock" style="background-image:url('data:image/png;base64,{b64}');"></div>
        <div class="wash"></div>
        <div class="stain"></div>
        <div class="edge"></div>
      </div>
      {dots_gradient(c["dots"], seed=idx + 11)}
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
  filter: grayscale(1) contrast(1.18) brightness(.45);
  opacity:1;
}}
.wash {{
  position:absolute; inset:0; z-index:2;
  background:
    radial-gradient(ellipse 90% 55% at 50% 38%, rgba(0,255,178,.07) 0%, transparent 55%),
    linear-gradient(180deg, rgba(10,10,10,.42) 0%, rgba(10,10,10,.62) 50%, rgba(0,0,0,.86) 100%);
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
  background: radial-gradient(circle, rgba(0,255,178,.36) 0%, rgba(0,255,178,.10) 44%, transparent 72%);
  filter: blur(10px); pointer-events:none; z-index:2;
}}

.dots {{ position:absolute; inset:0; z-index:4; pointer-events:none; }}
.dots span {{
  position:absolute; border-radius:50%; background:#00FFB2;
  box-shadow:0 0 8px rgba(0,255,178,.2);
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
    slides = "".join(slide(c, i + 1) for i, c in enumerate(STORIES))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Historias frases impacto STLabs</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    (OUT / "historias.html").write_text(html, encoding="utf-8")
    (OUT / "index.json").write_text(json.dumps(STORIES, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(STORIES)} stories · estilo unificado + roca · frases duras")


if __name__ == "__main__":
    main()
