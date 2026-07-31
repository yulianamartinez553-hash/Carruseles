# -*- coding: utf-8 -*-
"""25 Historias introductorias STLabs — 5 por tema, SIN nombrar la sección."""
from pathlib import Path

FONTS = Path("/tmp/stlabs-fonts")
OUT = Path(__file__).resolve().parent

# Cada item: tema (carpeta), id, layout, copy. NUNCA usar RESULTADOS/PROCESO/CLIENTES/SERVICIOS/CONTACTO.
STORIES = [
    # ── Tema 1: portfolio / evidencia ──────────────────────────────────────
    {
        "tema": "01-evidencia",
        "id": "ev-01",
        "layout": "claim",
        "kicker": "AL AIRE",
        "claim": "Tu web ya existe.\nAhora que venda.",
        "apoyo": "Menos tarjeta digital. Más máquina de consultas.",
        "visual": None,
    },
    {
        "tema": "01-evidencia",
        "id": "ev-02",
        "layout": "dato",
        "kicker": "CARGA",
        "dato": "1.9s",
        "dato_sub": "antes: 8.4s",
        "claim": "Misma marca.\nOtra velocidad.",
        "apoyo": "Sin rediseñar todo. Sí, tocando lo que pesa.",
        "visual": None,
    },
    {
        "tema": "01-evidencia",
        "id": "ev-03",
        "layout": "split",
        "kicker": "CAMBIO REAL",
        "left_label": "ANTES",
        "left_text": "Formulario\nque no llega",
        "right_label": "DESPUÉS",
        "right_text": "Lead en el\nCRM en segundos",
        "apoyo": "Arreglos que se sienten en la facturación.",
        "visual": None,
    },
    {
        "tema": "01-evidencia",
        "id": "ev-04",
        "layout": "dato",
        "kicker": "CONVERSIÓN",
        "dato": "+27%",
        "dato_sub": "consultas en 60 días",
        "claim": "No fue magia.\nFue estructura.",
        "apoyo": "Copy, recorrido y peso: alineados.",
        "visual": None,
    },
    {
        "tema": "01-evidencia",
        "id": "ev-05",
        "layout": "claim",
        "kicker": "EN PRODUCCIÓN",
        "claim": "Live.\nMidiendo.\nVendiendo.",
        "apoyo": "Lo entregado se ve. No queda en un PDF.",
        "visual": "pulse",
    },

    # ── Tema 2: cómo se trabaja ────────────────────────────────────────────
    {
        "tema": "02-metodo",
        "id": "me-01",
        "layout": "claim",
        "kicker": "DÍA CERO",
        "claim": "Primero miramos\nqué frena tus ventas.",
        "apoyo": "Después sí: diseño y código.",
        "visual": None,
    },
    {
        "tema": "02-metodo",
        "id": "me-02",
        "layout": "pasos",
        "kicker": "SIN SORPRESAS",
        "claim": "Así arranca\nun proyecto.",
        "steps": ["Diagnóstico", "Estructura", "Diseño + dev", "Al aire", "Entrega"],
        "apoyo": "Un paso a la vez. Todo dicho de entrada.",
        "visual": None,
    },
    {
        "tema": "02-metodo",
        "id": "me-03",
        "layout": "claim",
        "kicker": "REGLA",
        "claim": "Primero el esqueleto.\nDespués lo lindo.",
        "apoyo": "Si el recorrido no cierra, el color no salva nada.",
        "visual": None,
    },
    {
        "tema": "02-metodo",
        "id": "me-04",
        "layout": "dato",
        "kicker": "CLARIDAD",
        "dato": "5",
        "dato_sub": "momentos definidos",
        "claim": "Sabés qué pasa\nsi me contratás.",
        "apoyo": "Cero humo a mitad de camino.",
        "visual": None,
    },
    {
        "tema": "02-metodo",
        "id": "me-05",
        "layout": "claim",
        "kicker": "ENTREGA",
        "claim": "Te lo dejo\nfuncionando.",
        "apoyo": "Accesos, checklist y próximos pasos. Listo.",
        "visual": "check",
    },

    # ── Tema 3: confianza ──────────────────────────────────────────────────
    {
        "tema": "03-confianza",
        "id": "co-01",
        "layout": "cita",
        "kicker": "POST LAUNCH",
        "cita": "Por fin entiendo\nqué hace mi web.",
        "apoyo": "Cuando el sitio ordena, el negocio respira.",
        "visual": None,
    },
    {
        "tema": "03-confianza",
        "id": "co-02",
        "layout": "dato",
        "kicker": "PLAZO REAL",
        "dato": "14",
        "dato_sub": "días · landing con foco",
        "claim": "Sin milagros.\nCon prioridades.",
        "apoyo": "Alcance claro = fecha que se cumple.",
        "visual": None,
    },
    {
        "tema": "03-confianza",
        "id": "co-03",
        "layout": "claim",
        "kicker": "SERIEDAD",
        "claim": "Logos con permiso.\nNada inventado.",
        "apoyo": "La confianza se presta. No se fabrica.",
        "visual": None,
    },
    {
        "tema": "03-confianza",
        "id": "co-04",
        "layout": "cita",
        "kicker": "EN SUS PALABRAS",
        "cita": "El formulario\nempezó a llegar.",
        "apoyo": "Capturas reales. Datos sensibles tapados.",
        "visual": None,
    },
    {
        "tema": "03-confianza",
        "id": "co-05",
        "layout": "claim",
        "kicker": "HECHO",
        "claim": "Confianza se construye\ncon entregas.",
        "apoyo": "No con promesas enormes en un story.",
        "visual": "seal",
    },

    # ── Tema 4: qué se puede comprar ───────────────────────────────────────
    {
        "tema": "04-oferta",
        "id": "of-01",
        "layout": "claim",
        "kicker": "UNA PÁGINA",
        "claim": "Un objetivo.\nUna landing.",
        "apoyo": "Para cuando necesitás vender una cosa bien.",
        "visual": None,
    },
    {
        "tema": "04-oferta",
        "id": "of-02",
        "layout": "split",
        "split_mode": "choice",
        "kicker": "ELEGÍ",
        "left_label": "LANDING",
        "left_text": "Una página\nque convierte",
        "right_label": "SITIO",
        "right_text": "Marca ordenada\nen varias páginas",
        "apoyo": "Dos caminos. Sin hilo eterno por DM.",
        "visual": None,
    },
    {
        "tema": "04-oferta",
        "id": "of-03",
        "layout": "claim",
        "kicker": "REHACER",
        "claim": "Rediseñar no es\npintar de nuevo.",
        "apoyo": "Es sacar fricción y hacer que alguien compre.",
        "visual": None,
    },
    {
        "tema": "04-oferta",
        "id": "of-04",
        "layout": "claim",
        "kicker": "DESPUÉS DEL LAUNCH",
        "claim": "Que no se te caiga\ncuando ya está al aire.",
        "apoyo": "Updates, backups y cambios chicos sin drama.",
        "visual": None,
    },
    {
        "tema": "04-oferta",
        "id": "of-05",
        "layout": "dato",
        "kicker": "VISIBILIDAD",
        "dato": "SEO",
        "dato_sub": "+ velocidad real",
        "claim": "Más rápido.\nMás visible.",
        "apoyo": "Core Web Vitals y peso bajo control.",
        "visual": None,
    },

    # ── Tema 5: dar el paso ────────────────────────────────────────────────
    {
        "tema": "05-siguiente",
        "id": "si-01",
        "layout": "claim",
        "kicker": "FILTRO",
        "claim": "Para negocios que\nya tienen demanda.",
        "apoyo": "Y una web floja — o ninguna.",
        "visual": None,
    },
    {
        "tema": "05-siguiente",
        "id": "si-02",
        "layout": "claim",
        "kicker": "NO ES PARA VOS SI",
        "claim": "Buscás lo más barato\no “para ayer” sin brief.",
        "apoyo": "Sin claridad de oferta, mejor no arrancar.",
        "visual": "warn",
    },
    {
        "tema": "05-siguiente",
        "id": "si-03",
        "layout": "cta",
        "kicker": "SIGUIENTE PASO",
        "claim": "Comentá WEB",
        "apoyo": "Te mando el diagnóstico y cómo arrancar.",
        "visual": None,
    },
    {
        "tema": "05-siguiente",
        "id": "si-04",
        "layout": "dato",
        "kicker": "AGENDA",
        "dato": "20'",
        "dato_sub": "minutos · sin compromiso",
        "claim": "Salís con claridad.",
        "apoyo": "Calendly o WhatsApp. Como te quede mejor.",
        "visual": None,
    },
    {
        "tema": "05-siguiente",
        "id": "si-05",
        "layout": "faq",
        "kicker": "DUDA RÁPIDA",
        "pregunta": "¿Cuánto tarda?",
        "respuesta": "Landing típica: 10–14 días.\nSitio: 3–5 semanas.\nDepende del brief y tus vueltas.",
        "apoyo": "Dos rondas de revisión incluidas.",
        "visual": None,
    },
]


def nl(text: str) -> str:
    return "<br>".join(text.split("\n"))


def visual_block(kind):
    if kind == "pulse":
        return '<div class="viz pulse"><span></span><span></span><span></span></div>'
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

    if layout == "claim":
        parts.append(visual_block(s.get("visual")))
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
        parts.append(f'<div class="cta-pill">{s["claim"]}</div>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')

    elif layout == "faq":
        parts.append(f'<h1 class="claim claim-sm">{nl(s["pregunta"])}</h1>')
        parts.append(f'<p class="respuesta">{nl(s["respuesta"])}</p>')
        parts.append(f'<p class="apoyo">{s["apoyo"]}</p>')

    return "\n".join(parts)


def slide(s: dict, idx: int) -> str:
    return f'''
    <div class="slide" data-tema="{s['tema']}" data-id="{s['id']}" data-n="{idx}">
      <div class="bg">
        <div class="grid"></div>
        <div class="lines"></div>
        <div class="stain s1"></div>
        <div class="stain s2"></div>
        <div class="stain s3"></div>
        <div class="glow"></div>
        <div class="vignette"></div>
      </div>
      <div class="safe">
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
  position:absolute; inset:0;
  background-image:
    linear-gradient(rgba(0,255,178,.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,255,178,.07) 1px, transparent 1px);
  background-size:60px 60px;
  opacity:.85;
}}
.lines {{
  position:absolute; inset:-25%;
  background: repeating-linear-gradient(-32deg, transparent 0 22px, rgba(0,255,178,.06) 22px 23.5px);
  mix-blend-mode:screen;
}}
.stain {{ position:absolute; border-radius:50%; filter:blur(40px); pointer-events:none; }}
.s1 {{ width:560px; height:560px; left:-140px; top:-80px;
  background:radial-gradient(circle, rgba(0,255,178,.32) 0%, rgba(0,255,178,0) 70%); }}
.s2 {{ width:640px; height:480px; right:-180px; bottom:120px;
  background:radial-gradient(circle, rgba(0,255,178,.22) 0%, rgba(0,255,178,0) 68%); }}
.s3 {{ width:360px; height:360px; left:50%; top:42%; transform:translate(-50%,-50%);
  background:radial-gradient(circle, rgba(0,255,178,.12) 0%, rgba(0,255,178,0) 70%); }}
.glow {{
  position:absolute; inset:0;
  background:
    radial-gradient(ellipse at 50% 28%, rgba(0,255,178,.16) 0%, transparent 55%),
    linear-gradient(180deg, rgba(0,255,178,.05) 0%, transparent 35%, rgba(0,0,0,.55) 100%);
}}
.vignette {{
  position:absolute; inset:0;
  background:radial-gradient(ellipse at 50% 50%, transparent 40%, rgba(0,0,0,.55) 100%);
}}

.safe {{
  position:absolute; left:64px; right:64px; top:200px; bottom:320px;
  display:flex; flex-direction:column; justify-content:center; z-index:5;
}}
.kicker {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:26px;
  letter-spacing:.2em; color:#00FFB2; text-transform:uppercase; margin-bottom:36px;
}}
.claim {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:110px; line-height:.95;
  letter-spacing:.01em; color:#F2F2F2; text-shadow:0 0 40px rgba(0,255,178,.18);
  white-space:normal;
}}
.claim-sm {{ font-size:88px; }}
.rule {{
  width:140px; height:7px; background:#00FFB2; border-radius:2px;
  margin:32px 0 28px; box-shadow:0 0 18px rgba(0,255,178,.55);
}}
.apoyo {{
  font-family:'Barlow Condensed', sans-serif; font-weight:500; font-size:36px;
  line-height:1.3; color:#9aa39c; max-width:880px; margin-top:8px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:300px; text-align:center; z-index:6;
  font-family:'IBM Plex Mono', monospace; font-weight:500; font-size:24px;
  letter-spacing:.12em; color:#00FFB2; opacity:.92;
}}

.dato {{
  font-family:'Bebas Neue', Impact, sans-serif; font-size:220px; line-height:.85;
  color:#00FFB2; text-shadow:0 0 60px rgba(0,255,178,.35); margin-bottom:8px;
}}
.dato-sub {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:28px;
  letter-spacing:.12em; color:#9aa39c; text-transform:uppercase; margin-bottom:36px;
}}

.split {{
  display:flex; align-items:stretch; gap:18px; margin:12px 0 36px;
}}
.col {{
  flex:1; border-radius:24px; padding:36px 28px; min-height:280px;
  display:flex; flex-direction:column; justify-content:center;
  border:1px solid #2A2A2A; background:#141414;
}}
.col.bad {{ border-color:rgba(255,82,71,.45); }}
.col.good {{ border-color:rgba(0,255,178,.45); background:#0d1a14; }}
.col.choice {{ border-color:rgba(0,255,178,.35); background:#141414; }}
.col.choice.good {{ background:#0d1a14; }}
.col-lab {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:22px;
  letter-spacing:.18em; margin-bottom:18px;
}}
.col.bad .col-lab {{ color:#FF5247; }}
.col.good .col-lab {{ color:#00FFB2; }}
.col.choice .col-lab {{ color:#00FFB2; }}
.col-txt {{
  font-family:'Poppins', sans-serif; font-weight:800; font-size:34px;
  line-height:1.15; color:#F2F2F2;
}}
.vs {{
  align-self:center; width:72px; height:72px; border-radius:50%;
  background:#1A1A1A; border:1px solid #2A2A2A; color:#F2F2F2;
  font-family:'Poppins', sans-serif; font-weight:800; font-size:22px;
  display:flex; align-items:center; justify-content:center; flex-shrink:0;
}}

.pasos {{ list-style:none; margin:28px 0 32px; display:flex; flex-direction:column; gap:18px; }}
.pasos li {{
  display:flex; align-items:center; gap:22px;
  background:#141414; border:1px solid #2A2A2A; border-radius:18px; padding:22px 26px;
}}
.pasos .n {{
  font-family:'IBM Plex Mono', monospace; font-weight:600; font-size:22px;
  color:#00FFB2; letter-spacing:.08em; width:52px;
}}
.pasos .t {{
  font-family:'Poppins', sans-serif; font-weight:700; font-size:34px; color:#F2F2F2;
}}

.quote {{
  font-family:'Lora', Georgia, serif; font-style:italic; font-weight:600;
  font-size:72px; line-height:1.15; color:#F2F2F2;
}}
.quote::first-letter {{ color:#00FFB2; }}

.cta-pill {{
  display:inline-flex; align-self:flex-start; margin:36px 0 28px;
  background:#00FFB2; color:#04130b; font-family:'Poppins', sans-serif; font-weight:800;
  font-size:40px; letter-spacing:.04em; padding:22px 40px; border-radius:999px;
  box-shadow:0 0 28px rgba(0,255,178,.4);
}}
.respuesta {{
  font-family:'Barlow Condensed', sans-serif; font-weight:700; font-size:40px;
  line-height:1.35; color:#F2F2F2; margin:28px 0 24px; max-width:900px;
}}

.viz {{ margin-bottom:28px; }}
.viz.check svg {{ width:120px; height:120px; filter:drop-shadow(0 0 16px rgba(0,255,178,.4)); }}
.viz.seal, .viz.warn {{
  width:110px; height:110px; border-radius:50%; border:3px solid #00FFB2;
  display:flex; align-items:center; justify-content:center;
  font-family:'Bebas Neue', sans-serif; font-size:56px; color:#00FFB2;
  box-shadow:0 0 24px rgba(0,255,178,.35);
}}
.viz.warn {{ border-color:#FF5247; color:#FF5247; box-shadow:0 0 24px rgba(255,82,71,.35); }}
.viz.pulse {{ display:flex; gap:14px; align-items:flex-end; height:80px; }}
.viz.pulse span {{
  width:22px; background:#00FFB2; border-radius:6px;
  box-shadow:0 0 14px rgba(0,255,178,.45);
}}
.viz.pulse span:nth-child(1) {{ height:36px; opacity:.45; }}
.viz.pulse span:nth-child(2) {{ height:58px; opacity:.7; }}
.viz.pulse span:nth-child(3) {{ height:80px; }}
"""


def main():
    slides = "".join(slide(s, i + 1) for i, s in enumerate(STORIES))
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><title>Historias intros STLabs</title>
<style>{CSS}</style></head>
<body><div class="sheet">{slides}</div></body></html>"""
    path = OUT / "historias.html"
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {path} · {len(STORIES)} stories")
    # index for render naming
    (OUT / "stories_index.json").write_text(
        __import__("json").dumps(
            [{"n": i + 1, "tema": s["tema"], "id": s["id"], "layout": s["layout"], "kicker": s["kicker"]}
             for i, s in enumerate(STORIES)],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
