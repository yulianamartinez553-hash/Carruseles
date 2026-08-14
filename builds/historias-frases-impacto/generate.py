# -*- coding: utf-8 -*-
"""10 historias independientes — frases de impacto (vida / proyecto personal).
Sin foto · sin vínculo a destacadas · solo tipografía STLabs.
Fondo: reticula_fina · Familia: dossier_editorial
"""
from pathlib import Path
import math
import json
import re

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

# Cada frase = nota distinta. Vida personal / cualquier proyecto. Sin "hacé lo que yo".
STORIES = [
    {
        "id": "momento",
        "nota": "timing",
        "kicker": "NOTA 01",
        "lines": [
            {"t": "El momento perfecto", "c": "w"},
            {"t": "no existe.", "c": "w"},
            {"t": "El que arrancás, sí.", "c": "g"},
        ],
        "apoyo": "Dejá de esperar la señal. Sos vos.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "lg",
    },
    {
        "id": "manana",
        "nota": "procrastinación",
        "kicker": "NOTA 02",
        "lines": [
            {"t": "Dejarlo para mañana", "c": "w"},
            {"t": "es la forma más elegante", "c": "w"},
            {"t": "de no hacerlo nunca.", "c": "g"},
        ],
        "apoyo": "Hoy también cuenta como decisión.",
        "align": "left",
        "accent": "tl",
        "dots": "br",
        "size": "md",
    },
    {
        "id": "rescate",
        "nota": "autonomía",
        "kicker": "NOTA 03",
        "lines": [
            {"t": "Nadie viene", "c": "w"},
            {"t": "a rescatarte.", "c": "w"},
            {"t": "Eso también es", "c": "muted"},
            {"t": "una buena noticia.", "c": "g"},
        ],
        "apoyo": "La responsabilidad es poder, no castigo.",
        "align": "left",
        "accent": "br",
        "dots": "tl",
        "size": "lg",
    },
    {
        "id": "miedo",
        "nota": "miedo",
        "kicker": "NOTA 04",
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
        "id": "incomodidad",
        "nota": "crecimiento",
        "kicker": "NOTA 05",
        "lines": [
            {"t": "Si no te incomoda", "c": "w"},
            {"t": "un poco,", "c": "w"},
            {"t": "no estás creciendo:", "c": "muted"},
            {"t": "estás repitiendo.", "c": "g"},
        ],
        "apoyo": "La incomodidad es el peaje del salto.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "md",
    },
    {
        "id": "decidir",
        "nota": "decisión",
        "kicker": "NOTA 06",
        "lines": [
            {"t": "Lo que no decidís hoy,", "c": "w"},
            {"t": "lo decide el tiempo", "c": "w"},
            {"t": "por vos.", "c": "g"},
        ],
        "apoyo": "Elegir también es una forma de avanzar.",
        "align": "left",
        "accent": "tl",
        "dots": "br",
        "size": "lg",
    },
    {
        "id": "imperfecto",
        "nota": "perfeccionismo",
        "kicker": "NOTA 07",
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
        "id": "version",
        "nota": "identidad",
        "kicker": "NOTA 08",
        "lines": [
            {"t": "La versión de vos", "c": "w"},
            {"t": "que querés", "c": "w"},
            {"t": "ya existe.", "c": "g"},
            {"t": "Solo le falta", "c": "muted"},
            {"t": "que la elijas.", "c": "w"},
        ],
        "apoyo": "No es magia. Es elección repetida.",
        "align": "left",
        "accent": "bl",
        "dots": "tr",
        "size": "md",
    },
    {
        "id": "paso",
        "nota": "claridad",
        "kicker": "NOTA 09",
        "lines": [
            {"t": "No hace falta", "c": "w"},
            {"t": "tener todo claro.", "c": "w"},
            {"t": "Hace falta dar", "c": "muted"},
            {"t": "el próximo paso.", "c": "g"},
        ],
        "apoyo": "La claridad llega caminando.",
        "align": "left",
        "accent": "tr",
        "dots": "bl",
        "size": "lg",
    },
    {
        "id": "costo",
        "nota": "oportunidad",
        "kicker": "NOTA 10",
        "lines": [
            {"t": "El costo de", "c": "w"},
            {"t": "no intentarlo", "c": "g"},
            {"t": "siempre es más alto", "c": "w"},
            {"t": "de lo que pensás.", "c": "w"},
        ],
        "apoyo": "Intentarlo duele menos que arrepentirte.",
        "align": "center",
        "accent": "tl",
        "dots": "br",
        "size": "md",
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
    return f'''
    <div class="slide accent-{c['accent']} align-{c['align']} size-{c['size']}" data-id="{c['id']}">
      <div class="bg">
        <div class="reticula"></div>
        <div class="wash"></div>
        <div class="stain"></div>
        <div class="edge"></div>
      </div>
      {dots_gradient(c["dots"], seed=idx + 11)}
      <div class="safe">
        <div class="kicker">{c['kicker']}</div>
        <h1 class="claim">{claim_html(c['lines'])}</h1>
        <div class="rule"></div>
        <p class="apoyo">{c['apoyo']}</p>
      </div>
      <div class="firma">sebastian.stlabs.ar</div>
    </div>'''


CSS = f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype'); }}
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Lora'; src:url('file://{FONTS}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; font-weight:400 700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}
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
.reticula {{
  position:absolute; inset:0; z-index:1; opacity:.55;
  background-image:
    linear-gradient(rgba(0,255,178,.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.045) 1px, transparent 1px);
  background-size:48px 48px;
}}
.wash {{
  position:absolute; inset:0; z-index:2;
  background:
    radial-gradient(ellipse 90% 55% at 50% 38%, rgba(0,255,178,.06) 0%, transparent 55%),
    linear-gradient(180deg, rgba(10,10,10,.1) 0%, rgba(10,10,10,.35) 50%, rgba(0,0,0,.72) 100%);
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

.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  letter-spacing:.28em; color:#00FFB2; margin-bottom:36px; opacity:.92;
}}
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
    print(f"Wrote {len(STORIES)} impact phrase stories")


if __name__ == "__main__":
    main()
