# -*- coding: utf-8 -*-
"""25 Historias STLabs — copy continuo por tema + fondo rocoso distinto + marco + puntos."""
from pathlib import Path
import json

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent
TEX_DIR = OUT / "textures"

# Copy CONTINUO: cada bloque de 5 se lee en secuencia (swipe).
# Nunca nombrar RESULTADOS / PROCESO / CLIENTES / SERVICIOS / CONTACTO.
STORIES = [
    # ── 01 evidencia (narrativa continua) ──────────────────────────────────
    {
        "tema": "01-evidencia", "id": "ev-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "rock": 0, "frame": "brackets", "dots": "tl-heavy",
        "kicker": "01 / 05",
        "claim": "Tu web ya existe.",
        "apoyo": "El problema no es “tener sitio”.",
        "cont": "El problema es lo que pasa después…",
    },
    {
        "tema": "01-evidencia", "id": "ev-02", "n_seq": 2,
        "layout": "dato", "align": "center",
        "rock": 1, "frame": "double", "dots": "br-scatter",
        "kicker": "02 / 05",
        "dato": "8.4s",
        "dato_sub": "así carga hoy",
        "claim": "…si tarda,\nla gente se va.",
        "apoyo": "Misma marca. Otra velocidad es posible.",
        "cont": "Y no es solo la carga…",
    },
    {
        "tema": "01-evidencia", "id": "ev-03", "n_seq": 3,
        "layout": "split", "align": "center",
        "rock": 2, "frame": "lines", "dots": "corners-mixed",
        "kicker": "03 / 05",
        "left_label": "ANTES",
        "left_text": "El formulario\nno llega",
        "right_label": "DESPUÉS",
        "right_text": "Lead en el CRM\nen segundos",
        "apoyo": "…también se pierde la consulta en el camino.",
        "cont": "Cuando ordenás eso…",
    },
    {
        "tema": "01-evidencia", "id": "ev-04", "n_seq": 4,
        "layout": "dato", "align": "left",
        "rock": 3, "frame": "brackets", "dots": "tr-heavy",
        "kicker": "04 / 05",
        "dato": "+27%",
        "dato_sub": "consultas · 60 días",
        "claim": "…la conversión\nresponde.",
        "apoyo": "Copy, recorrido y peso: alineados.",
        "cont": "Y el sitio deja de ser adorno…",
    },
    {
        "tema": "01-evidencia", "id": "ev-05", "n_seq": 5,
        "layout": "claim", "align": "center",
        "rock": 4, "frame": "double", "dots": "all-asymmetric",
        "kicker": "05 / 05",
        "claim": "…pasa a vender\nde verdad.",
        "apoyo": "Live. Midiendo. Con consultas reales.",
        "cont": None,
    },

    # ── 02 método ──────────────────────────────────────────────────────────
    {
        "tema": "02-metodo", "id": "me-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "rock": 1, "frame": "lines", "dots": "bl-heavy",
        "kicker": "01 / 05",
        "claim": "Si me contratás,\nno arrancamos\ndiseñando.",
        "apoyo": "Primero hay que ver dónde se frena la venta.",
        "cont": "Eso es el punto de partida…",
    },
    {
        "tema": "02-metodo", "id": "me-02", "n_seq": 2,
        "layout": "claim", "align": "center",
        "rock": 3, "frame": "brackets", "dots": "tl-scatter",
        "kicker": "02 / 05",
        "claim": "…miramos web,\nmensajes y embudo.",
        "apoyo": "Sin humo. Con un mapa de prioridades.",
        "cont": "Recién ahí armamos estructura…",
    },
    {
        "tema": "02-metodo", "id": "me-03", "n_seq": 3,
        "layout": "claim", "align": "left",
        "rock": 0, "frame": "double", "dots": "br-heavy",
        "kicker": "03 / 05",
        "claim": "…primero el esqueleto.\nDespués lo lindo.",
        "apoyo": "Si el recorrido no cierra, el color no salva nada.",
        "cont": "Diseño y desarrollo van juntos…",
    },
    {
        "tema": "02-metodo", "id": "me-04", "n_seq": 4,
        "layout": "pasos", "align": "left",
        "rock": 4, "frame": "lines", "dots": "corners-mixed",
        "kicker": "04 / 05",
        "claim": "…con avances\nque se ven.",
        "steps": ["Diagnóstico", "Estructura", "Diseño + dev", "Al aire", "Entrega"],
        "apoyo": "Cinco momentos. Todo dicho de entrada.",
        "cont": "Y al final…",
    },
    {
        "tema": "02-metodo", "id": "me-05", "n_seq": 5,
        "layout": "claim", "align": "center",
        "rock": 2, "frame": "brackets", "dots": "tr-scatter",
        "kicker": "05 / 05",
        "claim": "…te lo dejo\nfuncionando.",
        "apoyo": "Accesos, checklist y próximos pasos. Cerrado.",
        "cont": None,
        "visual": "check",
    },

    # ── 03 confianza ───────────────────────────────────────────────────────
    {
        "tema": "03-confianza", "id": "co-01", "n_seq": 1,
        "layout": "cita", "align": "left",
        "rock": 2, "frame": "double", "dots": "tl-heavy",
        "kicker": "01 / 05",
        "cita": "Por fin entiendo\nqué hace mi web.",
        "apoyo": "Eso aparece cuando el sitio ordena el negocio.",
        "cont": "No es marketing vacío…",
    },
    {
        "tema": "03-confianza", "id": "co-02", "n_seq": 2,
        "layout": "dato", "align": "center",
        "rock": 4, "frame": "brackets", "dots": "br-scatter",
        "kicker": "02 / 05",
        "dato": "14",
        "dato_sub": "días · con foco",
        "claim": "…son plazos reales\ny alcance claro.",
        "apoyo": "Sin milagros. Con prioridades.",
        "cont": "Y sin inventar credenciales…",
    },
    {
        "tema": "03-confianza", "id": "co-03", "n_seq": 3,
        "layout": "claim", "align": "left",
        "rock": 1, "frame": "lines", "dots": "tr-heavy",
        "kicker": "03 / 05",
        "claim": "…logos solo\ncon permiso.",
        "apoyo": "Nada inventado. Nada prestado sin autorización.",
        "cont": "Lo que escriben también cuenta…",
    },
    {
        "tema": "03-confianza", "id": "co-04", "n_seq": 4,
        "layout": "cita", "align": "center",
        "rock": 0, "frame": "double", "dots": "bl-scatter",
        "kicker": "04 / 05",
        "cita": "El formulario\nempezó a llegar.",
        "apoyo": "Capturas reales. Datos sensibles tapados.",
        "cont": "Al final la confianza…",
    },
    {
        "tema": "03-confianza", "id": "co-05", "n_seq": 5,
        "layout": "claim", "align": "center",
        "rock": 3, "frame": "brackets", "dots": "all-asymmetric",
        "kicker": "05 / 05",
        "claim": "…se construye\ncon entregas.",
        "apoyo": "No con promesas enormes en un story.",
        "cont": None,
        "visual": "seal",
    },

    # ── 04 oferta ──────────────────────────────────────────────────────────
    {
        "tema": "04-oferta", "id": "of-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "rock": 3, "frame": "lines", "dots": "tl-scatter",
        "kicker": "01 / 05",
        "claim": "No hace falta\nun hilo eterno\npor DM.",
        "apoyo": "Hay caminos claros según lo que necesitás.",
        "cont": "Si querés vender una cosa…",
    },
    {
        "tema": "04-oferta", "id": "of-02", "n_seq": 2,
        "layout": "claim", "align": "center",
        "rock": 0, "frame": "brackets", "dots": "br-heavy",
        "kicker": "02 / 05",
        "claim": "…una landing\nbasta.",
        "apoyo": "Una página. Un objetivo. Formularios conectados.",
        "cont": "Si tu marca necesita más espacio…",
    },
    {
        "tema": "04-oferta", "id": "of-03", "n_seq": 3,
        "layout": "split", "align": "center", "split_mode": "choice",
        "rock": 2, "frame": "double", "dots": "corners-mixed",
        "kicker": "03 / 05",
        "left_label": "LANDING",
        "left_text": "Una página\nque convierte",
        "right_label": "SITIO",
        "right_text": "Marca ordenada\nen varias páginas",
        "apoyo": "…armamos sitio corporativo. O rediseñamos el que ya tenés.",
        "cont": "Y cuando ya está al aire…",
    },
    {
        "tema": "04-oferta", "id": "of-04", "n_seq": 4,
        "layout": "claim", "align": "left",
        "rock": 4, "frame": "lines", "dots": "tr-scatter",
        "kicker": "04 / 05",
        "claim": "…que no se te caiga\ndespués del launch.",
        "apoyo": "Mantenimiento: updates, backups, cambios chicos.",
        "cont": "Si el freno es velocidad o visibilidad…",
    },
    {
        "tema": "04-oferta", "id": "of-05", "n_seq": 5,
        "layout": "dato", "align": "center",
        "rock": 1, "frame": "brackets", "dots": "bl-heavy",
        "kicker": "05 / 05",
        "dato": "SEO",
        "dato_sub": "+ velocidad real",
        "claim": "…lo atacamos\nde frente.",
        "apoyo": "Core Web Vitals y peso bajo control.",
        "cont": None,
    },

    # ── 05 siguiente ───────────────────────────────────────────────────────
    {
        "tema": "05-siguiente", "id": "si-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "rock": 4, "frame": "double", "dots": "tl-heavy",
        "kicker": "01 / 05",
        "claim": "Trabajo con negocios\nque ya tienen demanda.",
        "apoyo": "Y una web floja — o ninguna.",
        "cont": "Si buscás lo más barato…",
    },
    {
        "tema": "05-siguiente", "id": "si-02", "n_seq": 2,
        "layout": "claim", "align": "center",
        "rock": 1, "frame": "lines", "dots": "br-scatter",
        "kicker": "02 / 05",
        "claim": "…o “para ayer”\nsin brief,",
        "apoyo": "mejor no arrancamos. Sin claridad no hay buen sitio.",
        "cont": "Si esto te suena…",
        "visual": "warn",
    },
    {
        "tema": "05-siguiente", "id": "si-03", "n_seq": 3,
        "layout": "cta", "align": "center",
        "rock": 3, "frame": "brackets", "dots": "corners-mixed",
        "kicker": "03 / 05",
        "claim": "…comentá WEB.",
        "apoyo": "Te mando el diagnóstico y cómo arrancar.",
        "cont": "También podés agendar…",
    },
    {
        "tema": "05-siguiente", "id": "si-04", "n_seq": 4,
        "layout": "dato", "align": "left",
        "rock": 0, "frame": "double", "dots": "tr-heavy",
        "kicker": "04 / 05",
        "dato": "20'",
        "dato_sub": "sin compromiso",
        "claim": "…y salir\ncon claridad.",
        "apoyo": "Calendly o WhatsApp. Como te quede mejor.",
        "cont": "Una duda rápida, de paso…",
    },
    {
        "tema": "05-siguiente", "id": "si-05", "n_seq": 5,
        "layout": "faq", "align": "left",
        "rock": 2, "frame": "lines", "dots": "all-asymmetric",
        "kicker": "05 / 05",
        "pregunta": "¿Cuánto tarda?",
        "respuesta": "Landing típica: 10–14 días.\nSitio: 3–5 semanas.\nDepende del brief y tus vueltas.",
        "apoyo": "Dos rondas de revisión incluidas. Empezá cuando quieras.",
        "cont": None,
    },
]

# Variantes de textura rocosa (seed + frecuencia + overlay)
ROCKS = [
    {"rock_i": 0, "overlay": 0.62, "contrast": 1.2, "glow": "18% 22%", "rock_op": 0.85, "tile": "340px"},
    {"rock_i": 1, "overlay": 0.58, "contrast": 1.25, "glow": "78% 18%", "rock_op": 0.9, "tile": "280px"},
    {"rock_i": 2, "overlay": 0.64, "contrast": 1.15, "glow": "22% 72%", "rock_op": 0.82, "tile": "420px"},
    {"rock_i": 3, "overlay": 0.55, "contrast": 1.35, "glow": "70% 78%", "rock_op": 0.92, "tile": "240px"},
    {"rock_i": 4, "overlay": 0.66, "contrast": 1.18, "glow": "50% 40%", "rock_op": 0.8, "tile": "380px"},
]


def nl(text: str) -> str:
    return "<br>".join(text.split("\n"))


def dots_html(kind: str) -> str:
    """Puntos verdes en esquinas — tamaños y posiciones distintas por preset."""
    presets = {
        "tl-heavy": [
            (48, 48, 28), (86, 52, 12), (52, 92, 8), (110, 78, 6),
            (980, 60, 10), (1020, 100, 6),
            (56, 1780, 8), (1000, 1820, 14),
        ],
        "tr-heavy": [
            (1000, 52, 26), (960, 70, 11), (1020, 100, 7), (920, 48, 5),
            (60, 56, 9), (48, 1800, 12), (1010, 1810, 8),
        ],
        "bl-heavy": [
            (52, 1800, 30), (90, 1760, 12), (48, 1720, 7), (120, 1830, 6),
            (1000, 50, 9), (60, 56, 8), (1010, 1820, 10),
        ],
        "br-heavy": [
            (1008, 1790, 28), (960, 1830, 13), (1020, 1720, 8), (920, 1800, 6),
            (56, 48, 10), (1000, 60, 7), (70, 1810, 9),
        ],
        "tl-scatter": [
            (44, 44, 18), (78, 90, 7), (120, 50, 11), (50, 130, 5), (160, 100, 4),
            (1000, 1800, 16), (960, 1840, 6), (1020, 70, 8),
        ],
        "tr-scatter": [
            (1020, 44, 20), (960, 80, 8), (980, 120, 5), (900, 50, 12),
            (50, 1800, 14), (80, 60, 6), (1000, 1820, 9),
        ],
        "bl-scatter": [
            (46, 1820, 22), (90, 1760, 9), (130, 1840, 5), (60, 1700, 11),
            (1000, 50, 13), (1020, 1800, 7), (70, 50, 6),
        ],
        "br-scatter": [
            (1020, 1820, 24), (960, 1760, 10), (900, 1840, 6), (1000, 1700, 12),
            (50, 50, 14), (80, 1810, 7), (1000, 60, 5),
        ],
        "corners-mixed": [
            (50, 50, 22), (90, 70, 8), (70, 110, 5),
            (1010, 54, 14), (960, 90, 7),
            (54, 1810, 10), (100, 1760, 16),
            (1008, 1800, 20), (950, 1840, 6), (1020, 1720, 9),
        ],
        "all-asymmetric": [
            (40, 60, 26), (100, 40, 9), (70, 120, 5), (140, 80, 4),
            (1000, 40, 12), (1040, 90, 18), (960, 110, 6),
            (40, 1760, 8), (80, 1840, 20), (130, 1780, 5),
            (1000, 1820, 14), (940, 1760, 7), (1020, 1700, 10), (880, 1840, 4),
        ],
    }
    dots = presets.get(kind, presets["corners-mixed"])
    html = ['<div class="dots">']
    for x, y, s in dots:
        html.append(
            f'<span style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;"></span>'
        )
    html.append("</div>")
    return "".join(html)


def visual_block(kind):
    if kind == "check":
        return '''<div class="viz check"><svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="50" fill="none" stroke="#00FFB2" stroke-width="6"/><path d="M36 62 L54 80 L86 42" fill="none" stroke="#00FFB2" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'''
    if kind == "seal":
        return '<div class="viz seal">OK</div>'
    if kind == "warn":
        return '<div class="viz warn">!</div>'
    return ""


def body_for(s: dict) -> str:
    layout = s["layout"]
    parts = [f'<div class="kicker">{s["kicker"]}</div>']
    if s.get("visual"):
        parts.append(visual_block(s["visual"]))

    if layout == "claim":
        parts.append(f'<h1 class="claim">{nl(s["claim"])}</h1>')
        parts.append('<div class="rule"></div>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "dato":
        parts.append(f'<div class="dato">{s["dato"]}</div>')
        parts.append(f'<div class="dato-sub">{s["dato_sub"]}</div>')
        parts.append(f'<h1 class="claim claim-sm">{nl(s["claim"])}</h1>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "split":
        mode = s.get("split_mode", "before_after")
        left_cls = "choice" if mode == "choice" else "bad"
        right_cls = "choice good" if mode == "choice" else "good"
        vs_txt = "O" if mode == "choice" else "VS"
        parts.append(f'''
        <div class="split">
          <div class="col {left_cls}">
            <div class="col-lab">{s["left_label"]}</div>
            <div class="col-txt">{nl(s["left_text"])}</div>
          </div>
          <div class="vs">{vs_txt}</div>
          <div class="col {right_cls}">
            <div class="col-lab">{s["right_label"]}</div>
            <div class="col-txt">{nl(s["right_text"])}</div>
          </div>
        </div>''')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "pasos":
        parts.append(f'<h1 class="claim claim-sm">{nl(s["claim"])}</h1>')
        items = "".join(
            f'<li><span class="n">{i:02d}</span><span class="t">{t}</span></li>'
            for i, t in enumerate(s["steps"], 1)
        )
        parts.append(f'<ol class="pasos">{items}</ol>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "cita":
        parts.append(f'<div class="quote">“{nl(s["cita"])}”</div>')
        parts.append('<div class="rule"></div>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "cta":
        parts.append(f'<h1 class="claim">{nl(s["claim"])}</h1>')
        parts.append('<div class="cta-pill">Comentá WEB</div>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')
    elif layout == "faq":
        parts.append(f'<h1 class="claim claim-sm">{nl(s["pregunta"])}</h1>')
        parts.append(f'<p class="respuesta">{nl(s["respuesta"])}</p>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')

    if s.get("cont"):
        parts.append(f'<p class="cont">{s["cont"]}</p>')
    return "\n".join(parts)


def rock_data_uri(cfg: dict, idx: int) -> str:
    """Textura piedra PNG — distinta por variante rock (file:// para render local)."""
    i = cfg.get("rock_i", idx % 5) % 5
    path = (TEX_DIR / f"rock-{i}.png").resolve().as_uri()
    return f'url("{path}")'


def frame_html(kind: str) -> str:
    return f'<div class="frame frame-{kind}"></div>'


def slide(s: dict, idx: int) -> str:
    rock = ROCKS[s["rock"] % len(ROCKS)]
    align = s.get("align", "left")
    rock_bg = rock_data_uri(rock, idx)
    return f'''
    <div class="slide rock-{s['rock']}" data-tema="{s['tema']}" data-id="{s['id']}" data-n="{idx}">
      <div class="bg">
        <div class="rock-tex" style='background-image:{rock_bg};opacity:{rock["rock_op"]};background-size:{rock["tile"]}'></div>
        <div class="rock-overlay" style="--ov:{rock['overlay']};--glow:{rock['glow']};--ctr:{rock['contrast']}"></div>
        <div class="grain-lines"></div>
        <div class="stain s1"></div>
        <div class="stain s2"></div>
      </div>
      {frame_html(s['frame'])}
      {dots_html(s['dots'])}
      <div class="safe align-{align}">
        {body_for(s)}
      </div>
      <div class="firma">sebastian.stlabs.ar</div>
    </div>'''


CSS = f"""
@font-face {{ font-family:'Bebas Neue'; src:url('file://{FONTS}/BebasNeue-Regular.ttf') format('truetype'); }}
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-ExtraBold.ttf') format('truetype'); font-weight:800; }}
@font-face {{ font-family:'Poppins'; src:url('file://{FONTS}/Poppins-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-SemiBold.ttf') format('truetype'); font-weight:600; }}
@font-face {{ font-family:'IBM Plex Mono'; src:url('file://{FONTS}/IBMPlexMono-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }}
@font-face {{ font-family:'Barlow Condensed'; src:url('file://{FONTS}/BarlowCondensed-Bold.ttf') format('truetype'); font-weight:700; }}
@font-face {{ font-family:'Lora'; src:url('file://{FONTS}/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; }}

* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ background:#000; }}
.sheet {{ display:flex; flex-direction:column; gap:48px; padding:40px; width:max-content; }}

.slide {{
  position:relative; width:1080px; height:1920px; overflow:hidden;
  background:#0A0A0A; isolation:isolate;
}}
.bg {{ position:absolute; inset:0; }}
.rock-tex {{
  position:absolute; inset:0; z-index:1; pointer-events:none;
  background-repeat: repeat;
  mix-blend-mode: normal;
  filter: contrast(1.25) brightness(.9);
}}
.rock-overlay {{
  position:absolute; inset:0; z-index:2;
  background:
    radial-gradient(ellipse at var(--glow), rgba(0,255,178,.18) 0%, transparent 48%),
    linear-gradient(180deg, rgba(7,7,7,.45) 0%, rgba(7,7,7,var(--ov)) 52%, rgba(0,0,0,.85) 100%);
}}
.grain-lines {{
  position:absolute; inset:-20%; z-index:3;
  background:
    repeating-linear-gradient(-34deg, transparent 0 20px, rgba(0,255,178,.09) 20px 21.5px),
    repeating-linear-gradient(18deg, transparent 0 30px, rgba(255,255,255,.04) 30px 31px);
  mix-blend-mode:overlay; opacity:1; pointer-events:none;
}}
.stain {{ position:absolute; border-radius:50%; filter:blur(48px); pointer-events:none; }}
.s1 {{ width:520px; height:520px; left:-120px; top:-40px;
  background:radial-gradient(circle, rgba(0,255,178,.22) 0%, transparent 70%); }}
.s2 {{ width:580px; height:420px; right:-160px; bottom:180px;
  background:radial-gradient(circle, rgba(0,255,178,.16) 0%, transparent 68%); }}

/* Marcos con líneas */
.frame {{ position:absolute; inset:56px 48px 56px 48px; pointer-events:none; z-index:4; }}
.frame-double {{
  border:1.5px solid rgba(0,255,178,.35);
  box-shadow: inset 0 0 0 6px rgba(10,10,10,.2), inset 0 0 0 7.5px rgba(0,255,178,.18);
}}
.frame-lines {{
  border:1px solid rgba(0,255,178,.22);
  background:
    linear-gradient(#00FFB2, #00FFB2) top left / 72px 2px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) top left / 2px 72px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) top right / 72px 2px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) top right / 2px 72px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) bottom left / 72px 2px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) bottom left / 2px 72px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) bottom right / 72px 2px no-repeat,
    linear-gradient(#00FFB2, #00FFB2) bottom right / 2px 72px no-repeat;
}}
.frame-brackets::before, .frame-brackets::after {{
  content:''; position:absolute; width:54px; height:54px;
  border:2px solid #00FFB2; opacity:.7;
}}
.frame-brackets::before {{ top:0; left:0; border-right:none; border-bottom:none; }}
.frame-brackets::after {{ bottom:0; right:0; border-left:none; border-top:none; }}
.frame-brackets {{
  border:1px solid rgba(0,255,178,.12);
}}
.frame-brackets {{
  background:
    linear-gradient(#00FFB2,#00FFB2) top right / 54px 2px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) top right / 2px 54px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom left / 54px 2px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom left / 2px 54px no-repeat;
}}

/* Puntos verdes en esquinas */
.dots {{ position:absolute; inset:0; z-index:5; pointer-events:none; }}
.dots span {{
  position:absolute; border-radius:50%; background:#00FFB2;
  box-shadow:0 0 10px rgba(0,255,178,.55);
  display:block;
}}

.safe {{
  position:absolute; left:96px; right:96px; top:220px; bottom:340px;
  display:flex; flex-direction:column; justify-content:center; z-index:6;
}}
.align-left {{ align-items:flex-start; text-align:left; }}
.align-center {{ align-items:center; text-align:center; }}
.align-center .rule {{ margin-left:auto; margin-right:auto; }}
.align-center .cta-pill {{ align-self:center; }}
.align-center .pasos {{ width:100%; }}

.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:24px;
  letter-spacing:.22em; color:#00FFB2; text-transform:uppercase; margin-bottom:32px;
}}
.claim {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:108px; line-height:.94;
  letter-spacing:.01em; color:#F2F2F2; text-shadow:0 0 36px rgba(0,255,178,.16);
}}
.claim-sm {{ font-size:84px; }}
.rule {{
  width:120px; height:6px; background:#00FFB2; border-radius:2px;
  margin:28px 0 24px; box-shadow:0 0 16px rgba(0,255,178,.5);
}}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:34px;
  line-height:1.3; color:#9aa39c; max-width:860px;
}}
.cont {{
  margin-top:36px; font-family:'Lora', Georgia, serif; font-style:italic;
  font-size:32px; color:#00FFB2; opacity:.9; max-width:820px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:7;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.12em; color:#00FFB2; opacity:.92;
}}

.dato {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:200px; line-height:.85;
  color:#00FFB2; text-shadow:0 0 50px rgba(0,255,178,.3); margin-bottom:6px;
}}
.dato-sub {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:26px;
  letter-spacing:.12em; color:#9aa39c; text-transform:uppercase; margin-bottom:28px;
}}

.split {{ display:flex; align-items:stretch; gap:16px; margin:8px 0 28px; width:100%; }}
.col {{
  flex:1; border-radius:20px; padding:32px 24px; min-height:260px;
  display:flex; flex-direction:column; justify-content:center;
  border:1px solid #2A2A2A; background:rgba(20,20,20,.82);
}}
.col.bad {{ border-color:rgba(255,82,71,.5); }}
.col.good {{ border-color:rgba(0,255,178,.5); background:rgba(13,26,20,.85); }}
.col.choice {{ border-color:rgba(0,255,178,.4); }}
.col-lab {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  letter-spacing:.16em; margin-bottom:16px;
}}
.col.bad .col-lab {{ color:#FF5247; }}
.col.good .col-lab, .col.choice .col-lab {{ color:#00FFB2; }}
.col-txt {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:30px;
  line-height:1.15; color:#F2F2F2;
}}
.vs {{
  align-self:center; width:64px; height:64px; border-radius:50%;
  background:#1A1A1A; border:1px solid #2A2A2A; color:#F2F2F2;
  font-family:'Poppins', sans-serif; font-weight:800; font-size:20px;
  display:flex; align-items:center; justify-content:center; flex-shrink:0;
}}

.pasos {{ list-style:none; margin:22px 0 24px; display:flex; flex-direction:column; gap:14px; width:100%; }}
.pasos li {{
  display:flex; align-items:center; gap:18px;
  background:rgba(20,20,20,.85); border:1px solid #2A2A2A; border-radius:16px; padding:18px 22px;
}}
.pasos .n {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  color:#00FFB2; letter-spacing:.08em; width:48px;
}}
.pasos .t {{
  font-family:'Poppins', sans-serif; font-weight:700; font-size:30px; color:#F2F2F2;
}}

.quote {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:64px; line-height:1.15; color:#F2F2F2;
}}
.cta-pill {{
  display:inline-flex; margin:28px 0 22px;
  background:#00FFB2; color:#04130b; font-family:'Poppins', sans-serif; font-weight:800;
  font-size:36px; letter-spacing:.04em; padding:20px 36px; border-radius:999px;
  box-shadow:0 0 24px rgba(0,255,178,.4);
}}
.respuesta {{
  font-family:'Barlow Condensed', sans-serif; font-weight:700; font-size:38px;
  line-height:1.35; color:#F2F2F2; margin:24px 0 20px; max-width:880px;
}}
.viz {{ margin-bottom:22px; }}
.viz.check svg {{ width:110px; height:110px; filter:drop-shadow(0 0 14px rgba(0,255,178,.4)); }}
.viz.seal, .viz.warn {{
  width:100px; height:100px; border-radius:50%; border:3px solid #00FFB2;
  display:flex; align-items:center; justify-content:center;
  font-family:'Bebas Neue', sans-serif; font-size:52px; color:#00FFB2;
  box-shadow:0 0 20px rgba(0,255,178,.35);
}}
.viz.warn {{ border-color:#FF5247; color:#FF5247; box-shadow:0 0 20px rgba(255,82,71,.35); }}
"""


def main():
    slides = "".join(slide(s, i + 1) for i, s in enumerate(STORIES))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Historias STLabs v2</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    (OUT / "historias.html").write_text(html, encoding="utf-8")
    (OUT / "stories_index.json").write_text(
        json.dumps(
            [
                {
                    "n": i + 1,
                    "tema": s["tema"],
                    "id": s["id"],
                    "layout": s["layout"],
                    "kicker": s["kicker"],
                    "rock": s["rock"],
                    "frame": s["frame"],
                    "dots": s["dots"],
                    "claim": s.get("claim") or s.get("cita") or s.get("pregunta"),
                    "cont": s.get("cont"),
                }
                for i, s in enumerate(STORIES)
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(STORIES)} continuous stories")


if __name__ == "__main__":
    main()
