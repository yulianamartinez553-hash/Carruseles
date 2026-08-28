# -*- coding: utf-8 -*-
"""Diagramas ricos estilo dashboard técnico — Turbo sistema (fondo negro)."""
from __future__ import annotations

import base64
from pathlib import Path

B = Path(__file__).resolve().parent
ELEM = B / "assets" / "elements"

V = "#00FFB2"
TX = "#F2F2F2"
GY = "#9aa39c"
BD = "#2A2A2A"
PN = "#121212"
RD = "#FF5247"


def elem(name: str) -> str:
    p = ELEM / name
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/png;base64,{data}"


def _ico(svg: str) -> str:
    return f'<span class="ico">{svg}</span>'


def card(icon: str, title: str, desc: str) -> str:
    return f"""<div class="vcard">
  {_ico(icon)}
  <div class="vcard-t">{title}</div>
  <div class="vcard-d">{desc}</div>
</div>"""


def flow_step(icon: str, label: str, arrow: bool = True) -> str:
    arr = '<span class="farr">→</span>' if arrow else ""
    return f"""<div class="fstep">{_ico(icon)}<span>{label}</span></div>{arr}"""


def side_item(icon: str, title: str, desc: str) -> str:
    return f"""<div class="sitem">
  <div class="sico">{_ico(icon)}</div>
  <div><div class="stit">{title}</div><div class="sdesc">{desc}</div></div>
</div>"""


# ── Iconos SVG inline ──
IC = {
    "wheel": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="12" cy="12" r="9" fill="none" stroke="{V}" stroke-width="2"/><circle cx="12" cy="12" r="3" fill="{V}"/><line x1="12" y1="3" x2="12" y2="7" stroke="{V}" stroke-width="2"/><line x1="12" y1="17" x2="12" y2="21" stroke="{V}" stroke-width="2"/><line x1="3" y1="12" x2="7" y2="12" stroke="{V}" stroke-width="2"/><line x1="17" y1="12" x2="21" y2="12" stroke="{V}" stroke-width="2"/></svg>',
    "search": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="10" cy="10" r="7" fill="none" stroke="{V}" stroke-width="2"/><line x1="15" y1="15" x2="21" y2="21" stroke="{V}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "chart": f'<svg viewBox="0 0 24 24" width="36" height="36"><rect x="4" y="12" width="4" height="8" fill="{V}"/><rect x="10" y="8" width="4" height="12" fill="{V}"/><rect x="16" y="4" width="4" height="16" fill="{V}"/></svg>',
    "eye": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z" fill="none" stroke="{V}" stroke-width="2"/><circle cx="12" cy="12" r="3" fill="{V}"/></svg>',
    "brain": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 4c-3 0-5 2-5 5 0 1 .5 2 1 3-1 1-2 2-2 4 0 2 2 4 4 4h4c2 0 4-2 4-4 0-2-1-3-2-4 1-1 1-2 1-3 0-3-2-5-5-5z" fill="none" stroke="{V}" stroke-width="2"/></svg>',
    "bolt": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" fill="{V}"/></svg>',
    "people": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="9" cy="8" r="3" fill="none" stroke="{V}" stroke-width="2"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6" fill="none" stroke="{V}" stroke-width="2"/><circle cx="17" cy="9" r="2.5" fill="none" stroke="{V}" stroke-width="1.5"/><path d="M14 20c0-3 2-4 5-4" fill="none" stroke="{V}" stroke-width="1.5"/></svg>',
    "rocket": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2c4 4 6 8 6 14-3-1-5-2-6-4-1 2-3 3-6 4 0-6 2-10 6-14z" fill="none" stroke="{V}" stroke-width="2"/><circle cx="12" cy="11" r="2" fill="{V}"/></svg>',
    "clip": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M8 12l8-8a4 4 0 016 6l-10 10a4 4 0 01-6-6l9-9" fill="none" stroke="{V}" stroke-width="2" stroke-linecap="round"/></svg>',
    "target": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="12" cy="12" r="9" fill="none" stroke="{V}" stroke-width="2"/><circle cx="12" cy="12" r="5" fill="none" stroke="{V}" stroke-width="2"/><circle cx="12" cy="12" r="1.5" fill="{V}"/></svg>',
    "db": f'<svg viewBox="0 0 24 24" width="36" height="36"><ellipse cx="12" cy="6" rx="8" ry="3" fill="none" stroke="{V}" stroke-width="2"/><path d="M4 6v12c0 2 4 3 8 3s8-1 8-3V6" fill="none" stroke="{V}" stroke-width="2"/></svg>',
    "shield": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 2l8 4v6c0 5-4 9-8 10C8 21 4 17 4 12V6l8-4z" fill="none" stroke="{V}" stroke-width="2"/></svg>',
    "check": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M4 12l6 6L20 6" fill="none" stroke="{V}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "x": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M6 6l12 12M18 6L6 18" stroke="{RD}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "up": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="{V}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "play": f'<svg viewBox="0 0 24 24" width="36" height="36"><polygon points="8,5 19,12 8,19" fill="{V}"/></svg>',
    "globe": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="12" cy="12" r="9" fill="none" stroke="{V}" stroke-width="2"/><ellipse cx="12" cy="12" rx="4" ry="9" fill="none" stroke="{V}" stroke-width="1.5"/><line x1="3" y1="12" x2="21" y2="12" stroke="{V}" stroke-width="1.5"/></svg>',
    "folder": f'<svg viewBox="0 0 24 24" width="36" height="36"><path d="M3 7h7l2 2h9v10H3V7z" fill="none" stroke="{V}" stroke-width="2"/></svg>',
    "msg": f'<svg viewBox="0 0 24 24" width="36" height="36"><rect x="3" y="5" width="18" height="13" rx="3" fill="none" stroke="{V}" stroke-width="2"/><path d="M8 18l-3 3v-3" fill="none" stroke="{V}" stroke-width="2"/></svg>',
    "clock": f'<svg viewBox="0 0 24 24" width="36" height="36"><circle cx="12" cy="12" r="9" fill="none" stroke="{V}" stroke-width="2"/><path d="M12 7v5l3 3" fill="none" stroke="{V}" stroke-width="2" stroke-linecap="round"/></svg>',
    "chip": f'<svg viewBox="0 0 24 24" width="36" height="36"><rect x="5" y="5" width="14" height="14" rx="2" fill="none" stroke="{V}" stroke-width="2"/><rect x="9" y="9" width="6" height="6" fill="{V}"/></svg>',
    "star": f'<svg viewBox="0 0 24 24" width="36" height="36"><polygon points="12,2 15,9 22,9 16,14 18,21 12,17 6,21 8,14 2,9 9,9" fill="none" stroke="{V}" stroke-width="2"/></svg>',
}


def diagram_01() -> str:
    turbo = elem("turbo.png")
    cards = "".join(
        [
            card(IC["wheel"], "BUSCA", "Prospectos 24/7 en tu mercado"),
            card(IC["chart"], "MIDE", "Puntúa ajuste, urgencia y monto"),
            card(IC["eye"], "CRITICA", "Revisa cada corrida sin sesgo"),
            card(IC["up"], "MEJORA", "Se construye mejor solo"),
        ]
    )
    flow = (
        flow_step(IC["brain"], "PIENSA")
        + flow_step(IC["people"], "DELEGA")
        + flow_step(IC["rocket"], "EJECUTA", False)
    )
    return f"""
<div class="dia dia-01">
  <div class="dia-hero">
    <div class="dia-hero-num">24/7</div>
    <div class="dia-hero-img">
      <img src="{turbo}" alt="Turbo"/>
      <div class="dia-glow"></div>
    </div>
  </div>
  <div class="focus-box">
    <div class="focus-ico">{IC['target']}</div>
    <div><div class="focus-t">ENFOQUE DEL SISTEMA</div>
    <div class="focus-d">Un agente que busca, aprende y se especializa para tu negocio.</div></div>
  </div>
  <div class="vcard-row">{cards}</div>
  <div class="flow-bar">{flow}</div>
</div>"""


def diagram_02() -> str:
    turbo = elem("turbo.png")
    nodes = [
        ("VENTAS", IC["target"]),
        ("LINKEDIN", IC["globe"]),
        ("EMAIL", IC["msg"]),
        ("CRM", IC["db"]),
        ("MERCADO", IC["search"]),
        ("SEÑALES", IC["bolt"]),
        ("DATOS", IC["folder"]),
    ]
    orbit = ""
    import math

    cx, cy, r = 230, 210, 155
    for i, (lbl, ico) in enumerate(nodes):
        ang = -math.pi / 2 + i * (2 * math.pi / len(nodes))
        x = cx + int(r * math.cos(ang))
        y = cy + int(r * math.sin(ang))
        orbit += f"""<div class="onode" style="left:{x}px;top:{y}px">
          <div class="onico">{ico}</div><div class="olbl">{lbl}</div></div>"""
    side = "".join(
        [
            side_item(IC["clip"], "RECIBE", "Tu brief de mercado ideal"),
            side_item(IC["people"], "DELEGA", "Divide la búsqueda en tareas"),
            side_item(IC["eye"], "SUPERVISA", "Controla cada corrida"),
            side_item(IC["wheel"], "COORDINA", "Prioriza prospectos"),
        ]
    )
    return f"""
<div class="dia dia-02">
  <div class="dia-orbit-wrap">
    <svg class="orbit-lines" viewBox="0 0 400 360"><circle cx="200" cy="180" r="130" fill="none" stroke="{V}" stroke-width="1.5" stroke-dasharray="6 4" opacity=".5"/>
    <line x1="200" y1="180" x2="200" y2="50" stroke="{V}" stroke-width="1" opacity=".3"/>
    <line x1="200" y1="180" x2="330" y2="180" stroke="{V}" stroke-width="1" opacity=".3"/>
    <line x1="200" y1="180" x2="200" y2="310" stroke="{V}" stroke-width="1" opacity=".3"/>
    <line x1="200" y1="180" x2="70" y2="180" stroke="{V}" stroke-width="1" opacity=".3"/>
    </svg>
    <div class="ocenter">
      <img src="{turbo}" alt="Turbo"/>
      <div class="ocap">AGENTE TURBO</div>
    </div>
    {orbit}
  </div>
  <div class="dia-side-list"><div class="side-hd">QUÉ HACE</div>{side}</div>
  <div class="flow-bar mini">{flow_step(IC['clip'],'RECIBE')}{flow_step(IC['people'],'DIVIDE')}{flow_step(IC['target'],'ASIGNA',False)}</div>
</div>"""


def diagram_03() -> str:
    brain = elem("cerebro.png")
    left = "".join(
        [
            _box("TAREA", "◇", 0),
            _box("ACCIÓN", "▶", 88),
            _box("RESULTADO", "■", 176),
            _box("CONTEXTO", "◎", 264),
        ]
    )
    right = "".join(
        [
            _box("QUÉ FUNCIONA", "★", 0),
            _box("QUÉ FALLÓ", "✕", 88),
            _box("QUÉ MEJORÓ", "↗", 176),
            _box("QUÉ CAMBIAR", "◇", 264),
        ]
    )
    return f"""
<div class="dia dia-03">
  <div class="dia-side"><div class="dia-hd">ENTRADA</div><div class="dia-boxes">{left}</div></div>
  <div class="dia-arrows in">{_arrows(4)}</div>
  <div class="dia-mem">
    <div class="dia-hd mem">MEMORIA</div>
    <div class="dia-cylinder">
      <div class="cyl-stack"><div class="cyl-ring"></div><div class="cyl-ring"></div><div class="cyl-ring"></div><div class="cyl-ring"></div></div>
      <img class="cyl-brain" src="{brain}" alt=""/>
      <div class="cyl-base"></div>
    </div>
  </div>
  <div class="dia-arrows out">{_arrows(4, rev=True)}</div>
  <div class="dia-side"><div class="dia-hd">SALIDA</div><div class="dia-boxes">{right}</div></div>
</div>"""


def _box(label: str, icon: str, y: int) -> str:
    return f'<div class="dia-box" style="top:{y}px"><span class="dia-ico">{icon}</span><span class="dia-lbl">{label}</span></div>'


def _arrows(n: int, rev: bool = False) -> str:
    ys = [28 + i * 88 for i in range(n)]
    cls = "dia-arrow-h rev" if rev else "dia-arrow-h"
    return "".join(f'<div class="{cls}" style="top:{y}px"></div>' for y in ys)


def diagram_04() -> str:
    bars = [("AJUSTE", "92%", 0.92), ("URGENCIA", "8.4", 0.84), ("MONTO", "$48K", 0.72)]
    rows = ""
    for lbl, val, pct in bars:
        rows += f"""<div class="met-row">
  <div class="met-lbl">{lbl}</div>
  <div class="met-bar"><div class="met-fill" style="width:{pct*100:.0f}%"></div></div>
  <div class="met-val">{val}</div></div>"""
    chips = "".join(
        [
            card(IC["star"], "HOT", "Responde en 24h"),
            card(IC["target"], "FIT", "Encaja con tu ICP"),
            card(IC["chart"], "SCORE", "Puntaje compuesto"),
        ]
    )
    return f"""
<div class="dia dia-04">
  <div class="dia-panel score">
    <div class="dia-panel-hd">PANEL DE PUNTAJE</div>
    {rows}
    <div class="score-big"><span class="score-n">91</span><span class="score-u">/100</span></div>
  </div>
  <div class="vcard-col">{chips}</div>
  <div class="mini-stats">
    <div class="mstat"><div class="mstat-n">847</div><div class="mstat-l">PROSPECTOS</div></div>
    <div class="mstat"><div class="mstat-n">23%</div><div class="mstat-l">RESPONDEN</div></div>
    <div class="mstat"><div class="mstat-n">12</div><div class="mstat-l">HOT LEADS</div></div>
  </div>
</div>"""


def diagram_05() -> str:
    turbo = elem("turbo.png")
    checks = [
        ("Mensajes enviados", "OK", True),
        ("Filtros de mercado", "REVISAR", False),
        ("Tasa de respuesta", "OK", True),
        ("Calidad del ICP", "MEJORAR", False),
    ]
    rows = ""
    for lbl, st, ok in checks:
        c = V if ok else RD
        rows += f"""<div class="crit-row">
  <span>{lbl}</span><span class="crit-badge" style="border-color:{c};color:{c}">{st}</span></div>"""
    return f"""
<div class="dia dia-05">
  <div class="dia-panel critic">
    <div class="dia-panel-hd">CRÍTICO AUTOMÁTICO</div>
    {rows}
    <div class="crit-note">Sin sesgo · cada corrida · log completo</div>
  </div>
  <div class="dia-robot-wrap">
    <img class="dia-robot" src="{turbo}" alt=""/>
    <div class="robot-tag">REVISIÓN 24/7</div>
  </div>
  <div class="vcard-col sm">
    {card(IC['eye'], 'OBSERVA', 'Lee cada acción')}
    {card(IC['x'], 'DETECTA', 'Marca desvíos')}
    {card(IC['check'], 'VALIDA', 'Aprueba o corrige')}
  </div>
</div>"""


def diagram_06() -> str:
    patterns = [
        ("Mensaje genérico", "3x", RD),
        ("Filtro muy amplio", "2x", RD),
        ("Horario incorrecto", "1x", "#FF9D3C"),
        ("ICP desalineado", "2x", RD),
    ]
    items = ""
    for lbl, cnt, col in patterns:
        items += f"""<div class="pat-row"><span class="pat-dot" style="background:{col}"></span>
        <span class="pat-l">{lbl}</span><span class="pat-c">{cnt}</span></div>"""
    return f"""
<div class="dia dia-06">
  <div class="dia-panel err">
    <div class="dia-panel-hd">PATRONES DETECTADOS</div>
    {items}
  </div>
  <div class="err-viz">
    <div class="err-ring"><span>8</span><small>ERRORES</small></div>
    <div class="err-callout">Un fallo no importa.<br>Un <b>patrón</b> cambia<br>cómo busca.</div>
  </div>
  <div class="vcard-row sm">
    {card(IC['x'], 'FALLA', 'Registra el error')}
    {card(IC['brain'], 'ANALIZA', 'Busca repetición')}
    {card(IC['up'], 'AJUSTA', 'Modifica la búsqueda')}
  </div>
</div>"""


def diagram_07() -> str:
    v1 = elem("turbo.png")
    return f"""
<div class="dia dia-07">
  <div class="ver-col old">
    <div class="ver-tag">V1</div>
    <div class="dia-robot-wrap sm"><img class="dia-robot xs gray" src="{v1}" alt=""/></div>
    <div class="ver-scores">
      <div class="vs-row"><span>Precisión</span><span class="bad">62%</span></div>
      <div class="vs-row"><span>Calidad</span><span class="bad">5.1</span></div>
      <div class="vs-row"><span>Errores</span><span class="bad">18</span></div>
    </div>
  </div>
  <div class="ver-mid"><div class="ver-arrow">→</div><div class="ver-lbl">FEEDBACK<br>LOOP</div></div>
  <div class="ver-col new">
    <div class="ver-tag gr">V2</div>
    <div class="dia-robot-wrap sm"><img class="dia-robot xs" src="{v1}" alt=""/></div>
    <div class="ver-scores">
      <div class="vs-row"><span>Precisión</span><span class="good">91%</span></div>
      <div class="vs-row"><span>Calidad</span><span class="good">8.7</span></div>
      <div class="vs-row"><span>Errores</span><span class="good">3</span></div>
    </div>
  </div>
  <div class="flow-bar mini">{flow_step(IC['x'],'ERROR')}{flow_step(IC['brain'],'APRENDE')}{flow_step(IC['up'],'MEJORA',False)}</div>
</div>"""


def diagram_08() -> str:
    brain = elem("cerebro.png")
    stores = [
        (IC["db"], "PROSPECTOS"),
        (IC["msg"], "HISTORIAL"),
        (IC["folder"], "CONTEXTO"),
        (IC["target"], "ICP"),
        (IC["shield"], "REGLAS"),
    ]
    chips = "".join(f'<div class="store-chip"><div class="store-ico">{ico}</div><span>{lbl}</span></div>' for ico, lbl in stores)
    return f"""
<div class="dia dia-08">
  <div class="vault-wrap">
    <div class="vault">
      <div class="vault-door left"></div>
      <div class="vault-core">
        <img src="{brain}" alt="" class="vault-brain"/>
        <div class="vault-cap">NÚCLEO DE MEMORIA</div>
      </div>
      <div class="vault-door right"></div>
    </div>
    <div class="vault-glow"></div>
  </div>
  <div class="store-row">{chips}</div>
  <div class="flow-bar mini">{flow_step(IC['db'],'GUARDA')}{flow_step(IC['brain'],'CONTEXTUALIZA')}{flow_step(IC['msg'],'RESPONDE',False)}</div>
</div>"""


def diagram_09() -> str:
    turbo = elem("turbo.png")
    tags = [
        ("MEMORIA", "100%"),
        ("CORRIDAS", "24/7"),
        ("AGENTES", "1+N"),
        ("DATOS", "LOCAL"),
    ]
    tag_html = "".join(f'<div class="htag"><span>{k}</span><b>{v}</b></div>' for k, v in tags)
    side = "".join(
        [
            side_item(IC["clock"], "CORRE", "Sin pausas ni fines de semana"),
            side_item(IC["chip"], "LOCAL", "Tus datos bajo control"),
            side_item(IC["shield"], "SEGURO", "Sin filtraciones"),
        ]
    )
    return f"""
<div class="dia dia-09">
  <div class="hw-wrap">
    <div class="hw-base"></div>
    <img class="hw-turbo" src="{turbo}" alt=""/>
    <div class="hw-screen">
      <div class="hw-hd">SISTEMA TURBO</div>
      {tag_html}
      <div class="hw-status"><span class="dot-on"></span> OPERANDO</div>
    </div>
  </div>
  <div class="dia-side-list"><div class="side-hd">QUÉ TE DA</div>{side}</div>
  <div class="flow-bar mini">{flow_step(IC['play'],'INICIA')}{flow_step(IC['search'],'BUSCA')}{flow_step(IC['check'],'CONTROLA',False)}</div>
</div>"""


def diagram_10() -> str:
    turbo = elem("turbo.png")
    includes = [
        (IC["wheel"], "BUSCA", "Prospectos en tu mercado"),
        (IC["brain"], "MEMORIA", "Contexto de cada corrida"),
        (IC["chart"], "MÉTRICAS", "Puntaje por prospecto"),
        (IC["up"], "MEJORA", "Loop 24/7 automático"),
    ]
    row = "".join(f'<div class="cta-chip"><div class="cta-ico">{ico}</div><div class="cta-t">{t}</div><div class="cta-d">{d}</div></div>' for ico, t, d in includes)
    return f"""
<div class="dia dia-10">
  <div class="cta-hero">
    <img src="{turbo}" alt="" class="cta-turbo"/>
    <div class="cta-kw">TURBO</div>
  </div>
  <div class="cta-box">
    <div class="cta-box-hd">QUÉ INCLUYE</div>
    <div class="cta-grid">{row}</div>
  </div>
  <div class="flow-bar">{flow_step(IC['msg'],'COMENTÁ')}{flow_step(IC['clip'],'RECIBÍ')}{flow_step(IC['rocket'],'ARRANCAMOS',False)}</div>
</div>"""


DIAGRAM_CSS = """
/* ── Diagramas fondo negro (elementos grandes) ── */
.dia{{width:100%;max-width:976px;margin:0 auto;position:relative;}}
.dia svg{{display:block;max-width:100%;}}

/* Slide 01 portada dashboard */
.dia-01{{display:flex;flex-direction:column;gap:14px;align-items:stretch;}}
.dia-hero{{position:relative;height:340px;display:flex;align-items:center;justify-content:center;}}
.dia-hero-num{{position:absolute;right:-10px;top:-20px;font-family:'Impact',sans-serif;font-size:240px;line-height:1;
  color:rgba(0,255,178,.14);letter-spacing:-.04em;pointer-events:none;}}
.dia-hero-img{{position:relative;z-index:2;}}
.dia-hero-img img{{width:280px;height:280px;object-fit:contain;filter:drop-shadow(0 10px 32px rgba(0,255,178,.35));}}
.dia-glow{{position:absolute;inset:-40px;border-radius:50%;background:radial-gradient(circle,rgba(0,255,178,.15),transparent 70%);z-index:-1;}}
.focus-box{{display:flex;gap:16px;align-items:flex-start;padding:18px 22px;background:{PN};border:2px solid rgba(0,255,178,.5);
  border-radius:16px;box-shadow:0 0 24px rgba(0,255,178,.08);}}
.focus-ico{{flex-shrink:0;width:56px;height:56px;display:flex;align-items:center;justify-content:center;
  background:rgba(0,255,178,.08);border-radius:10px;border:1px solid rgba(0,255,178,.3);}}
.focus-t{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;letter-spacing:.12em;color:{V};}}
.focus-d{{font-size:22px;font-weight:600;color:{GY};margin-top:6px;line-height:1.3;}}
.vcard-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}}
.vcard-row.sm{{grid-template-columns:repeat(3,1fr);}}
.vcard{{background:{PN};border:2px solid rgba(0,255,178,.35);border-radius:16px;padding:18px 14px;text-align:center;
  box-shadow:0 0 16px rgba(0,255,178,.06);}}
.ico{{display:flex;align-items:center;justify-content:center;margin:0 auto 10px;}}
.vcard-t{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.1em;color:{TX};}}
.vcard-d{{font-size:17px;font-weight:600;color:{GY};margin-top:8px;line-height:1.25;}}
.vcard-col{{display:flex;flex-direction:column;gap:10px;}}
.vcard-col.sm .vcard{{padding:12px;}}
.flow-bar{{display:flex;align-items:center;justify-content:center;gap:8px;padding:12px 16px;
  background:{PN};border:1.5px solid {BD};border-radius:12px;margin-top:4px;}}
.flow-bar.mini{{padding:10px 14px;}}
.fstep{{display:flex;align-items:center;gap:8px;font-family:'IBM Plex Mono',monospace;font-weight:600;
  font-size:13px;letter-spacing:.08em;color:{TX};}}
.farr{{color:{V};font-size:20px;font-weight:700;margin:0 4px;}}

/* Slide 02 orbit */
.dia-02{{display:grid;grid-template-columns:1fr 240px;gap:16px;align-items:start;min-height:420px;}}
.dia-orbit-wrap{{position:relative;height:360px;}}
.orbit-lines{{position:absolute;inset:0;width:100%;height:100%;}}
.ocenter{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;z-index:3;}}
.ocenter img{{width:100px;height:100px;object-fit:contain;}}
.ocap{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.14em;color:{V};margin-top:6px;}}
.onode{{position:absolute;transform:translate(-50%,-50%);text-align:center;z-index:2;}}
.onico{{width:48px;height:48px;background:{PN};border:1.5px solid rgba(0,255,178,.45);border-radius:12px;
  display:flex;align-items:center;justify-content:center;margin:0 auto;box-shadow:0 2px 8px rgba(0,0,0,.06);}}
.olbl{{font-family:'IBM Plex Mono',monospace;font-size:10px;font-weight:600;letter-spacing:.08em;color:{TX};margin-top:4px;}}
.dia-side-list{{background:{PN};border:1.5px solid {BD};border-radius:14px;padding:16px;}}
.side-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.14em;color:{V};margin-bottom:12px;}}
.sitem{{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px solid {BD};}}
.sitem:last-child{{border:none;}}
.sico{{width:40px;height:40px;background:rgba(0,255,178,.06);border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}}
.stit{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;color:{TX};}}
.sdesc{{font-size:14px;font-weight:500;color:{GY};margin-top:2px;line-height:1.25;}}
.dia-02 .flow-bar{{grid-column:1/-1;}}

/* Slide 03 memoria */
.dia-03{{display:grid;grid-template-columns:220px 52px 200px 52px 220px;gap:4px;align-items:center;min-height:380px;}}
.dia-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.14em;color:{V};margin-bottom:12px;text-transform:uppercase;}}
.dia-side{{position:relative;}}
.dia-boxes{{position:relative;height:300px;}}
.dia-box{{position:absolute;left:0;display:flex;align-items:center;gap:10px;width:100%;padding:12px 14px;
  border:1.5px solid rgba(0,255,178,.4);border-radius:12px;background:{PN};box-shadow:0 2px 10px rgba(0,0,0,.04);}}
.dia-ico{{font-size:18px;color:{V};width:24px;text-align:center;}}
.dia-lbl{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:16px;color:{TX};}}
.dia-arrows{{position:relative;height:300px;margin-top:28px;}}
.dia-arrow-h{{position:absolute;left:0;right:0;height:3px;background:linear-gradient(90deg,{V},rgba(0,255,178,.2));border-radius:2px;}}
.dia-arrow-h::after{{content:'';position:absolute;right:-1px;top:50%;transform:translateY(-50%);
  border-top:6px solid transparent;border-bottom:6px solid transparent;border-left:9px solid {V};}}
.dia-arrow-h.rev{{background:linear-gradient(270deg,{V},rgba(0,255,178,.2));}}
.dia-arrow-h.rev::after{{right:auto;left:-1px;border-left:none;border-right:9px solid {V};}}
.dia-mem{{display:flex;flex-direction:column;align-items:center;}}
.dia-mem .mem{{text-align:center;}}
.dia-cylinder{{position:relative;width:180px;height:220px;display:flex;align-items:center;justify-content:center;}}
.cyl-stack{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:6px;padding:0 8px;}}
.cyl-ring{{height:28px;border:2px solid {V};border-radius:50%;opacity:.35;}}
.cyl-brain{{position:relative;z-index:3;width:130px;height:120px;object-fit:contain;
  filter:drop-shadow(0 4px 16px rgba(0,255,178,.35));}}
.cyl-base{{position:absolute;bottom:8px;width:140px;height:8px;border:2px solid {V};border-radius:50%;opacity:.4;}}

/* Slide 04 métricas */
.dia-04{{display:grid;grid-template-columns:1fr 200px;grid-template-rows:auto auto;gap:14px;}}
.dia-panel{{background:{PN};border:1.5px solid {BD};border-radius:16px;padding:18px;box-shadow:0 4px 16px rgba(0,0,0,.04);}}
.dia-panel-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.12em;color:{V};margin-bottom:14px;}}
.met-row{{display:grid;grid-template-columns:90px 1fr 60px;gap:10px;align-items:center;margin-bottom:12px;}}
.met-lbl{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;color:{TX};}}
.met-bar{{height:10px;background:#ECEAE4;border-radius:6px;overflow:hidden;}}
.met-fill{{height:100%;background:linear-gradient(90deg,{V},rgba(0,255,178,.6));border-radius:6px;}}
.met-val{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;color:{V};text-align:right;}}
.score-big{{text-align:center;margin-top:16px;padding-top:14px;border-top:1px solid {BD};}}
.score-n{{font-family:'Impact',sans-serif;font-size:72px;color:{V};line-height:1;}}
.score-u{{font-size:24px;color:{GY};font-weight:600;}}
.mini-stats{{grid-column:1/-1;display:grid;grid-template-columns:repeat(3,1fr);gap:10px;}}
.mstat{{background:{PN};border:1.5px solid {BD};border-radius:12px;padding:14px;text-align:center;}}
.mstat-n{{font-family:'Impact',sans-serif;font-size:36px;color:{V};}}
.mstat-l{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:{GY};margin-top:4px;}}

/* Slide 05 crítico */
.dia-05{{display:grid;grid-template-columns:1fr 200px 180px;gap:14px;align-items:center;}}
.crit-row{{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid {BD};font-size:16px;font-weight:600;color:{TX};}}
.crit-badge{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.08em;
  padding:4px 10px;border:1.5px solid;border-radius:6px;}}
.crit-note{{margin-top:12px;font-size:14px;color:{GY};font-weight:500;}}
.dia-robot-wrap{{position:relative;text-align:center;padding:12px;}}
.dia-robot{{max-height:180px;width:auto;object-fit:contain;filter:drop-shadow(0 6px 20px rgba(0,255,178,.2));}}
.dia-robot.xs{{max-height:120px;}}.dia-robot.gray{{filter:grayscale(1) opacity(.7);}}
.robot-tag{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.12em;color:{V};margin-top:8px;}}

/* Slide 06 errores */
.dia-06{{display:grid;grid-template-columns:1fr 180px;grid-template-rows:auto auto;gap:14px;}}
.pat-row{{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid {BD};}}
.pat-dot{{width:10px;height:10px;border-radius:50%;flex-shrink:0;}}
.pat-l{{flex:1;font-size:16px;font-weight:600;color:{TX};}}
.pat-c{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;color:{GY};}}
.err-viz{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;}}
.err-ring{{width:120px;height:120px;border-radius:50%;border:3px solid {RD};display:flex;flex-direction:column;
  align-items:center;justify-content:center;background:rgba(229,72,77,.06);}}
.err-ring span{{font-family:'Impact',sans-serif;font-size:48px;color:{RD};line-height:1;}}
.err-ring small{{font-family:'IBM Plex Mono',monospace;font-size:10px;color:{RD};letter-spacing:.1em;}}
.err-callout{{text-align:center;font-size:16px;font-weight:600;color:{TX};line-height:1.35;}}
.dia-06 .vcard-row{{grid-column:1/-1;}}

/* Slide 07 V1 V2 */
.dia-07{{display:grid;grid-template-columns:1fr 80px 1fr;gap:12px;align-items:center;}}
.ver-col{{background:{PN};border:1.5px solid {BD};border-radius:16px;padding:18px;text-align:center;}}
.ver-col.new{{border-color:rgba(0,255,178,.5);box-shadow:0 4px 20px rgba(0,255,178,.08);}}
.ver-tag{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.14em;color:{GY};}}
.ver-tag.gr{{color:{V};}}
.ver-scores{{margin-top:14px;text-align:left;}}
.vs-row{{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid {BD};font-size:16px;font-weight:600;color:{TX};}}
.vs-row .bad{{color:{RD};}}.vs-row .good{{color:{V};}}
.ver-mid{{text-align:center;}}
.ver-arrow{{font-size:36px;color:{V};font-weight:700;}}
.ver-lbl{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.1em;color:{GY};margin-top:6px;}}
.dia-07 .flow-bar{{grid-column:1/-1;}}

/* Slide 08 vault */
.dia-08{{display:flex;flex-direction:column;gap:14px;align-items:center;}}
.vault-wrap{{position:relative;width:100%;height:240px;display:flex;align-items:center;justify-content:center;}}
.vault{{display:flex;align-items:center;justify-content:center;position:relative;z-index:2;}}
.vault-door{{width:60px;height:180px;background:linear-gradient(180deg,#E8E6E0,#D0CEC8);border:2px solid {BD};border-radius:8px 0 0 8px;}}
.vault-door.right{{border-radius:0 8px 8px 0;}}
.vault-core{{width:200px;height:200px;background:{PN};border:2px solid rgba(0,255,178,.45);border-radius:16px;
  display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 8px 32px rgba(0,255,178,.12);}}
.vault-brain{{width:90px;height:80px;object-fit:contain;}}
.vault-cap{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.12em;color:{V};margin-top:8px;}}
.vault-glow{{position:absolute;inset:20px;background:radial-gradient(circle,rgba(0,255,178,.1),transparent 70%);z-index:0;}}
.store-row{{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;width:100%;}}
.store-chip{{display:flex;align-items:center;gap:8px;padding:10px 14px;background:{PN};border:1.5px solid {BD};border-radius:10px;}}
.store-ico{{width:32px;height:32px;display:flex;align-items:center;justify-content:center;}}
.store-chip span{{font-family:'IBM Plex Mono',monospace;font-size:11px;font-weight:600;letter-spacing:.08em;color:{TX};}}

/* Slide 09 hardware */
.dia-09{{display:grid;grid-template-columns:1fr 220px;gap:14px;}}
.hw-wrap{{position:relative;height:320px;display:flex;align-items:center;justify-content:center;}}
.hw-base{{position:absolute;bottom:40px;width:200px;height:20px;background:linear-gradient(180deg,{V},rgba(0,255,178,.3));border-radius:50%;filter:blur(2px);}}
.hw-turbo{{width:140px;height:140px;object-fit:contain;position:relative;z-index:2;filter:drop-shadow(0 8px 24px rgba(0,255,178,.25));}}
.hw-screen{{position:absolute;top:20px;right:0;width:220px;background:{PN};border:1.5px solid {BD};border-radius:14px;padding:16px;box-shadow:0 8px 24px rgba(0,0,0,.06);}}
.hw-hd{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.12em;color:{V};margin-bottom:12px;}}
.htag{{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid {BD};font-size:14px;color:{TX};}}
.htag b{{color:{V};font-family:'IBM Plex Mono',monospace;}}
.hw-status{{margin-top:12px;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;color:{V};display:flex;align-items:center;gap:8px;}}
.dot-on{{width:8px;height:8px;border-radius:50%;background:{V};box-shadow:0 0 8px rgba(0,255,178,.6);animation:pulse 2s infinite;}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.5}}}}
.dia-09 .flow-bar{{grid-column:1/-1;}}

/* Slide 10 CTA */
.dia-10{{display:flex;flex-direction:column;gap:14px;align-items:center;}}
.cta-hero{{position:relative;text-align:center;padding:10px 0;}}
.cta-turbo{{width:120px;height:120px;object-fit:contain;}}
.cta-kw{{font-family:'Impact',sans-serif;font-size:64px;color:{V};letter-spacing:.06em;line-height:1;margin-top:4px;}}
.cta-box{{width:100%;background:{PN};border:2px solid rgba(0,255,178,.5);border-radius:16px;padding:18px;}}
.cta-box-hd{{font-family:'IBM Plex Mono',monospace;font-size:13px;font-weight:600;letter-spacing:.14em;color:{V};margin-bottom:14px;}}
.cta-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}}
.cta-chip{{text-align:center;padding:12px 8px;background:rgba(0,255,178,.04);border:1px solid {BD};border-radius:12px;}}
.cta-ico{{display:flex;justify-content:center;margin-bottom:8px;}}
.cta-t{{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.08em;color:{TX};}}
.cta-d{{font-size:13px;font-weight:500;color:{GY};margin-top:4px;line-height:1.2;}}
.dia-10 .flow-bar{{width:100%;}}
""".format(PN=PN, V=V, TX=TX, GY=GY, BD=BD, RD=RD)


def diagram(n: int) -> str:
    fns = {
        1: diagram_01,
        2: diagram_02,
        3: diagram_03,
        4: diagram_04,
        5: diagram_05,
        6: diagram_06,
        7: diagram_07,
        8: diagram_08,
        9: diagram_09,
        10: diagram_10,
    }
    return fns[n]()
