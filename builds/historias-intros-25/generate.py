# -*- coding: utf-8 -*-
"""25 Historias STLabs — carrusel continuo por sección (sin ellipsis).

Fondo profesional negro + mancha verde degradé en una esquina,
líneas en bordes, muchos puntos verdes chicos en la esquina opuesta.
"""
from pathlib import Path
import json

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

# Copy CONTINUO por sección (se lee como un carrusel). SIN puntos suspensivos.
# Nunca nombrar RESULTADOS / PROCESO / CLIENTES / SERVICIOS / CONTACTO.
STORIES = [
    # ── 01 evidencia ───────────────────────────────────────────────────────
    {
        "tema": "01-evidencia", "id": "ev-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "01 / 05",
        "claim": "Tu web ya existe.",
        "apoyo": "Tener sitio no alcanza si no genera consultas.",
    },
    {
        "tema": "01-evidencia", "id": "ev-02", "n_seq": 2,
        "layout": "dato", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "02 / 05",
        "dato": "8.4s",
        "dato_sub": "carga actual típica",
        "claim": "Si tarda,\nla gente se va.",
        "apoyo": "La misma marca puede cargar en menos de 2 segundos.",
    },
    {
        "tema": "01-evidencia", "id": "ev-03", "n_seq": 3,
        "layout": "split", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "03 / 05",
        "left_label": "ANTES",
        "left_text": "El formulario\nno llega",
        "right_label": "DESPUÉS",
        "right_text": "Lead en el CRM\nen segundos",
        "apoyo": "También se pierde la venta cuando el mensaje no llega.",
    },
    {
        "tema": "01-evidencia", "id": "ev-04", "n_seq": 4,
        "layout": "dato", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "04 / 05",
        "dato": "+27%",
        "dato_sub": "consultas · 60 días",
        "claim": "Con estructura,\nla conversión responde.",
        "apoyo": "Copy, recorrido y peso alineados al objetivo.",
    },
    {
        "tema": "01-evidencia", "id": "ev-05", "n_seq": 5,
        "layout": "claim", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "05 / 05",
        "claim": "Así tu web\nvende de verdad.",
        "apoyo": "Live, midiendo y trayendo consultas reales.",
    },

    # ── 02 método ──────────────────────────────────────────────────────────
    {
        "tema": "02-metodo", "id": "me-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "accent": "tr", "dots_corner": "bl",
        "kicker": "01 / 05",
        "claim": "Si me contratás,\nno arrancamos diseñando.",
        "apoyo": "Primero hay que ver dónde se frena la venta.",
    },
    {
        "tema": "02-metodo", "id": "me-02", "n_seq": 2,
        "layout": "claim", "align": "left",
        "accent": "tr", "dots_corner": "bl",
        "kicker": "02 / 05",
        "claim": "Miramos web,\nmensajes y embudo.",
        "apoyo": "Salís con un mapa de prioridades, sin humo.",
    },
    {
        "tema": "02-metodo", "id": "me-03", "n_seq": 3,
        "layout": "claim", "align": "left",
        "accent": "tr", "dots_corner": "bl",
        "kicker": "03 / 05",
        "claim": "Después viene\nel esqueleto.",
        "apoyo": "Recién cuando el recorrido cierra, diseñamos lo lindo.",
    },
    {
        "tema": "02-metodo", "id": "me-04", "n_seq": 4,
        "layout": "pasos", "align": "left",
        "accent": "tr", "dots_corner": "bl",
        "kicker": "04 / 05",
        "claim": "Diseño y desarrollo\nvan juntos.",
        "steps": ["Diagnóstico", "Estructura", "Diseño + dev", "Al aire", "Entrega"],
        "apoyo": "Cinco momentos claros desde el día uno.",
    },
    {
        "tema": "02-metodo", "id": "me-05", "n_seq": 5,
        "layout": "claim", "align": "left",
        "accent": "tr", "dots_corner": "bl",
        "kicker": "05 / 05",
        "claim": "Al final,\nte lo dejo funcionando.",
        "apoyo": "Accesos, checklist y próximos pasos. Cerrado.",
        "visual": "check",
    },

    # ── 03 confianza ───────────────────────────────────────────────────────
    {
        "tema": "03-confianza", "id": "co-01", "n_seq": 1,
        "layout": "cita", "align": "left",
        "accent": "bl", "dots_corner": "tr",
        "kicker": "01 / 05",
        "cita": "Por fin entiendo\nqué hace mi web.",
        "apoyo": "Eso aparece cuando el sitio ordena el negocio.",
    },
    {
        "tema": "03-confianza", "id": "co-02", "n_seq": 2,
        "layout": "dato", "align": "left",
        "accent": "bl", "dots_corner": "tr",
        "kicker": "02 / 05",
        "dato": "14",
        "dato_sub": "días · con foco",
        "claim": "Son plazos reales\ny alcance claro.",
        "apoyo": "Sin milagros. Con prioridades definidas.",
    },
    {
        "tema": "03-confianza", "id": "co-03", "n_seq": 3,
        "layout": "claim", "align": "left",
        "accent": "bl", "dots_corner": "tr",
        "kicker": "03 / 05",
        "claim": "Los logos aparecen\nsolo con permiso.",
        "apoyo": "Nada inventado. Nada prestado sin autorización.",
    },
    {
        "tema": "03-confianza", "id": "co-04", "n_seq": 4,
        "layout": "cita", "align": "left",
        "accent": "bl", "dots_corner": "tr",
        "kicker": "04 / 05",
        "cita": "El formulario\nempezó a llegar.",
        "apoyo": "Capturas reales, con datos sensibles tapados.",
    },
    {
        "tema": "03-confianza", "id": "co-05", "n_seq": 5,
        "layout": "claim", "align": "left",
        "accent": "bl", "dots_corner": "tr",
        "kicker": "05 / 05",
        "claim": "La confianza se construye\ncon entregas.",
        "apoyo": "No con promesas enormes en un story.",
        "visual": "seal",
    },

    # ── 04 oferta ──────────────────────────────────────────────────────────
    {
        "tema": "04-oferta", "id": "of-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "accent": "br", "dots_corner": "tl",
        "kicker": "01 / 05",
        "claim": "No hace falta\nun hilo eterno por DM.",
        "apoyo": "Hay caminos claros según lo que necesitás.",
    },
    {
        "tema": "04-oferta", "id": "of-02", "n_seq": 2,
        "layout": "claim", "align": "left",
        "accent": "br", "dots_corner": "tl",
        "kicker": "02 / 05",
        "claim": "Si querés vender una cosa,\nuna landing alcanza.",
        "apoyo": "Una página, un objetivo, formularios conectados.",
    },
    {
        "tema": "04-oferta", "id": "of-03", "n_seq": 3,
        "layout": "split", "align": "left", "split_mode": "choice",
        "accent": "br", "dots_corner": "tl",
        "kicker": "03 / 05",
        "left_label": "LANDING",
        "left_text": "Una página\nque convierte",
        "right_label": "SITIO",
        "right_text": "Marca ordenada\nen varias páginas",
        "apoyo": "Si necesitás más espacio, armamos el sitio completo.",
    },
    {
        "tema": "04-oferta", "id": "of-04", "n_seq": 4,
        "layout": "claim", "align": "left",
        "accent": "br", "dots_corner": "tl",
        "kicker": "04 / 05",
        "claim": "Cuando ya está al aire,\nno se puede caer.",
        "apoyo": "Mantenimiento: updates, backups y cambios chicos.",
    },
    {
        "tema": "04-oferta", "id": "of-05", "n_seq": 5,
        "layout": "dato", "align": "left",
        "accent": "br", "dots_corner": "tl",
        "kicker": "05 / 05",
        "dato": "SEO",
        "dato_sub": "+ velocidad real",
        "claim": "Si el freno es\nvisibilidad, lo atacamos.",
        "apoyo": "Core Web Vitals y peso bajo control.",
    },

    # ── 05 siguiente ───────────────────────────────────────────────────────
    {
        "tema": "05-siguiente", "id": "si-01", "n_seq": 1,
        "layout": "claim", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "01 / 05",
        "claim": "Trabajo con negocios\nque ya tienen demanda.",
        "apoyo": "Y una web floja, o ninguna.",
    },
    {
        "tema": "05-siguiente", "id": "si-02", "n_seq": 2,
        "layout": "claim", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "02 / 05",
        "claim": "No es para quien busca\nlo más barato sin brief.",
        "apoyo": "Sin claridad de oferta, mejor no arrancar.",
        "visual": "warn",
    },
    {
        "tema": "05-siguiente", "id": "si-03", "n_seq": 3,
        "layout": "cta", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "03 / 05",
        "claim": "Si esto te suena,\ncomentá WEB.",
        "apoyo": "Te mando el diagnóstico y cómo arrancar.",
    },
    {
        "tema": "05-siguiente", "id": "si-04", "n_seq": 4,
        "layout": "dato", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "04 / 05",
        "dato": "20'",
        "dato_sub": "sin compromiso",
        "claim": "También podés\nagendar y salir con claridad.",
        "apoyo": "Calendly o WhatsApp, como te quede mejor.",
    },
    {
        "tema": "05-siguiente", "id": "si-05", "n_seq": 5,
        "layout": "faq", "align": "left",
        "accent": "tl", "dots_corner": "br",
        "kicker": "05 / 05",
        "pregunta": "¿Cuánto tarda?",
        "respuesta": "Landing típica: 10–14 días.\nSitio: 3–5 semanas.\nDepende del brief y tus vueltas.",
        "apoyo": "Dos rondas de revisión incluidas. Empezá cuando quieras.",
    },
]


def nl(text: str) -> str:
    return "<br>".join(text.split("\n"))


def dots_cluster(corner: str) -> str:
    """Muchos puntos verdes pequeños en una esquina."""
    # origen por esquina + offsets densos
    origins = {
        "tl": (36, 36),
        "tr": (1044, 36),
        "bl": (36, 1884),
        "br": (1044, 1884),
    }
    ox, oy = origins[corner]
    # patrón determinístico de puntos chicos (4–11px)
    pattern = [
        (0, 0, 10), (18, 8, 6), (8, 22, 5), (32, 18, 7), (22, 34, 4),
        (44, 6, 5), (52, 28, 6), (14, 48, 4), (38, 46, 8), (60, 42, 4),
        (70, 14, 5), (28, 60, 4), (48, 62, 6), (66, 54, 5), (80, 32, 4),
        (12, 70, 5), (36, 78, 4), (58, 74, 7), (76, 68, 4), (88, 48, 5),
        (4, 40, 4), (42, 12, 4), (64, 8, 6), (84, 18, 4), (92, 36, 5),
        (20, 86, 4), (50, 90, 5), (72, 84, 4), (90, 72, 6), (98, 56, 4),
        (8, 96, 4), (30, 100, 5), (54, 104, 4), (78, 98, 5), (96, 88, 4),
        (104, 24, 4), (110, 44, 5), (106, 64, 4), (100, 80, 4), (16, 12, 5),
    ]
    sx = 1 if corner in ("tl", "bl") else -1
    sy = 1 if corner in ("tl", "tr") else -1
    html = ['<div class="dots">']
    for dx, dy, s in pattern:
        x = ox + sx * dx - (0 if sx > 0 else s)
        y = oy + sy * dy - (0 if sy > 0 else s)
        html.append(f'<span style="left:{x}px;top:{y}px;width:{s}px;height:{s}px;"></span>')
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
    return "\n".join(parts)


def slide(s: dict, idx: int) -> str:
    accent = s["accent"]
    return f'''
    <div class="slide accent-{accent}" data-tema="{s['tema']}" data-id="{s['id']}" data-n="{idx}">
      <div class="bg">
        <div class="grid"></div>
        <div class="wash"></div>
        <div class="stain"></div>
      </div>
      <div class="frame"></div>
      {dots_cluster(s["dots_corner"])}
      <div class="safe align-{s.get("align","left")}">
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
.grid {{
  position:absolute; inset:0; opacity:.45;
  background-image:
    linear-gradient(rgba(0,255,178,.045) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.045) 1px, transparent 1px);
  background-size:64px 64px;
}}
.wash {{
  position:absolute; inset:0;
  background: linear-gradient(180deg, rgba(10,10,10,.2) 0%, rgba(10,10,10,.55) 70%, rgba(0,0,0,.75) 100%);
}}

/* Mancha verde degradé — una esquina, profesional (no chillona) */
.accent-tl .stain {{
  left:-180px; top:-160px;
  background: radial-gradient(circle, rgba(0,255,178,.38) 0%, rgba(0,255,178,.12) 38%, transparent 70%);
}}
.accent-tr .stain {{
  right:-180px; top:-160px; left:auto;
  background: radial-gradient(circle, rgba(0,255,178,.38) 0%, rgba(0,255,178,.12) 38%, transparent 70%);
}}
.accent-bl .stain {{
  left:-180px; bottom:-140px; top:auto;
  background: radial-gradient(circle, rgba(0,255,178,.34) 0%, rgba(0,255,178,.1) 40%, transparent 72%);
}}
.accent-br .stain {{
  right:-180px; bottom:-140px; left:auto; top:auto;
  background: radial-gradient(circle, rgba(0,255,178,.34) 0%, rgba(0,255,178,.1) 40%, transparent 72%);
}}
.stain {{
  position:absolute; width:720px; height:720px; border-radius:50%;
  filter: blur(8px); pointer-events:none;
}}

/* Marco con líneas en bordes */
.frame {{
  position:absolute; inset:52px 44px; z-index:4; pointer-events:none;
  border:1px solid rgba(0,255,178,.22);
  background:
    linear-gradient(#00FFB2,#00FFB2) top left / 64px 1.5px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) top left / 1.5px 64px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) top right / 64px 1.5px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) top right / 1.5px 64px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom left / 64px 1.5px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom left / 1.5px 64px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom right / 64px 1.5px no-repeat,
    linear-gradient(#00FFB2,#00FFB2) bottom right / 1.5px 64px no-repeat;
}}

.dots {{ position:absolute; inset:0; z-index:5; pointer-events:none; }}
.dots span {{
  position:absolute; border-radius:50%; background:#00FFB2;
  opacity:.85; box-shadow:0 0 6px rgba(0,255,178,.35);
}}

.safe {{
  position:absolute; left:96px; right:96px; top:220px; bottom:340px;
  display:flex; flex-direction:column; justify-content:center; z-index:6;
}}
.align-left {{ align-items:flex-start; text-align:left; }}
.align-center {{ align-items:center; text-align:center; }}
.align-center .rule, .align-center .cta-pill {{ margin-left:auto; margin-right:auto; align-self:center; }}

.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:24px;
  letter-spacing:.22em; color:#00FFB2; margin-bottom:32px;
}}
.claim {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:104px; line-height:.94;
  letter-spacing:.01em; color:#F2F2F2;
}}
.claim-sm {{ font-size:82px; }}
.rule {{
  width:110px; height:5px; background:#00FFB2; border-radius:2px;
  margin:26px 0 22px; box-shadow:0 0 12px rgba(0,255,178,.4);
}}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:34px;
  line-height:1.32; color:#9aa39c; max-width:860px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:7;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:22px;
  letter-spacing:.12em; color:#00FFB2; opacity:.9;
}}

.dato {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:190px; line-height:.85;
  color:#00FFB2; text-shadow:0 0 36px rgba(0,255,178,.22); margin-bottom:4px;
}}
.dato-sub {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:24px;
  letter-spacing:.12em; color:#9aa39c; text-transform:uppercase; margin-bottom:26px;
}}

.split {{ display:flex; align-items:stretch; gap:16px; margin:8px 0 26px; width:100%; }}
.col {{
  flex:1; border-radius:18px; padding:30px 22px; min-height:250px;
  display:flex; flex-direction:column; justify-content:center;
  border:1px solid #2A2A2A; background:rgba(20,20,20,.78);
}}
.col.bad {{ border-color:rgba(255,82,71,.45); }}
.col.good {{ border-color:rgba(0,255,178,.45); background:rgba(13,26,20,.8); }}
.col.choice {{ border-color:rgba(0,255,178,.35); }}
.col-lab {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  letter-spacing:.16em; margin-bottom:14px;
}}
.col.bad .col-lab {{ color:#FF5247; }}
.col.good .col-lab, .col.choice .col-lab {{ color:#00FFB2; }}
.col-txt {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:30px;
  line-height:1.15; color:#F2F2F2;
}}
.vs {{
  align-self:center; width:62px; height:62px; border-radius:50%;
  background:#1A1A1A; border:1px solid #2A2A2A; color:#F2F2F2;
  font-family:'Poppins', sans-serif; font-weight:800; font-size:18px;
  display:flex; align-items:center; justify-content:center; flex-shrink:0;
}}

.pasos {{ list-style:none; margin:20px 0 22px; display:flex; flex-direction:column; gap:12px; width:100%; }}
.pasos li {{
  display:flex; align-items:center; gap:16px;
  background:rgba(20,20,20,.8); border:1px solid #2A2A2A; border-radius:14px; padding:16px 20px;
}}
.pasos .n {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:20px;
  color:#00FFB2; width:46px;
}}
.pasos .t {{
  font-family:'Poppins', sans-serif; font-weight:700; font-size:28px; color:#F2F2F2;
}}

.quote {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:62px; line-height:1.15; color:#F2F2F2;
}}
.cta-pill {{
  display:inline-flex; margin:26px 0 20px;
  background:#00FFB2; color:#04130b; font-family:'Poppins', sans-serif; font-weight:800;
  font-size:34px; padding:18px 34px; border-radius:999px;
  box-shadow:0 0 20px rgba(0,255,178,.35);
}}
.respuesta {{
  font-family:'Barlow Condensed', sans-serif; font-weight:700; font-size:36px;
  line-height:1.35; color:#F2F2F2; margin:22px 0 18px; max-width:860px;
}}
.viz {{ margin-bottom:20px; }}
.viz.check svg {{ width:100px; height:100px; filter:drop-shadow(0 0 12px rgba(0,255,178,.35)); }}
.viz.seal, .viz.warn {{
  width:92px; height:92px; border-radius:50%; border:2.5px solid #00FFB2;
  display:flex; align-items:center; justify-content:center;
  font-family:'Bebas Neue', sans-serif; font-size:48px; color:#00FFB2;
}}
.viz.warn {{ border-color:#FF5247; color:#FF5247; }}
"""


def main():
    slides = "".join(slide(s, i + 1) for i, s in enumerate(STORIES))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Historias STLabs v3</title>
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
                    "claim": s.get("claim") or s.get("cita") or s.get("pregunta"),
                    "apoyo": s.get("apoyo"),
                }
                for i, s in enumerate(STORIES)
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    # sanity: no ellipsis in copy
    bad = []
    for s in STORIES:
        blob = " ".join(str(s.get(k, "")) for k in ("claim", "apoyo", "cita", "pregunta", "respuesta"))
        if "..." in blob or "…" in blob:
            bad.append(s["id"])
    print(f"Wrote {len(STORIES)} stories · ellipsis hits: {bad or 'NONE'}")


if __name__ == "__main__":
    main()
