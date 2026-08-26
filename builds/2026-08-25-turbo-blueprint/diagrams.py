# -*- coding: utf-8 -*-
"""Diagramas nativos SVG/CSS — carrusel Turbo (sin overlays sobre refs)."""
from __future__ import annotations

import base64
from pathlib import Path

B = Path(__file__).resolve().parent
ELEM = B / "assets" / "elements"

V = "#00FFB2"
TX = "#F2F2F2"
GY = "#9aa39c"
RD = "#ff5252"
YL = "#ffc107"


def elem(name: str) -> str:
    p = ELEM / name
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/png;base64,{data}"


SVG_DEFS = """
<defs>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glowS" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>"""


def _turbo_icon(cx: int, cy: int, r: int = 28) -> str:
    return f"""
<g transform="translate({cx},{cy})" filter="url(#glow)">
  <circle cx="0" cy="0" r="{r}" fill="none" stroke="{V}" stroke-width="3"/>
  <path d="M-5,-18 L10,0 L-3,0 L5,18 L-10,0 L3,0 Z" fill="{V}"/>
</g>"""


def _node(x: int, y: int, icon_svg: str, label: str, r: int = 48) -> str:
    return f"""
<g transform="translate({x},{y})">
  <circle cx="0" cy="0" r="{r}" fill="rgba(0,255,178,.06)" stroke="{V}" stroke-width="3" filter="url(#glowS)"/>
  {icon_svg}
  <text y="{r + 36}" fill="{V}" font-family="'Barlow Condensed',sans-serif" font-weight="700"
    font-size="38" text-anchor="middle" letter-spacing=".06em">{label}</text>
</g>"""


def diagram_01() -> str:
    cx, cy, rad = 460, 455, 335
    nodes = [
        (cx, cy - rad,  # top — HACÉ
         '<polygon points="-12,0 10,-10 10,10" fill="' + V + '"/>', "HACÉ"),
        (cx + int(rad * 0.59), cy - int(rad * 0.81),  # ~2h — MEDÍ
         f'<rect x="-14" y="6" width="6" height="22" fill="{V}"/><rect x="-4" y="0" width="6" height="28" fill="{V}"/><rect x="8" y="-6" width="6" height="34" fill="{V}"/>',
         "MEDÍ"),
        (cx + int(rad * 0.59), cy + int(rad * 0.81),  # ~4h — PROBÁ
         f'<path d="M-14,12 L-2,-8 L8,2 L18,-14" fill="none" stroke="{V}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
         "PROBÁ"),
        (cx, cy + rad,  # bottom — MEJORÁ
         f'<path d="M-8,24 L0,8 L8,24 L0,36 Z" fill="none" stroke="{V}" stroke-width="3"/><line x1="0" y1="36" x2="0" y2="48" stroke="{V}" stroke-width="3"/>',
         "MEJORÁ"),
        (cx - int(rad * 0.59), cy + int(rad * 0.81),  # ~8h — REFLEXIONÁ
         f'<circle cx="0" cy="0" r="16" fill="none" stroke="{V}" stroke-width="3"/><path d="M-8,6 L0,18 L16,-4" fill="none" stroke="{V}" stroke-width="4" stroke-linecap="round"/>',
         "REFLEXIONÁ"),
    ]
    parts = ""
    for x, y, ico, lbl in nodes:
        parts += _node(x, y, ico, lbl)
    return f"""
<div class="dia dia-01">
<svg viewBox="0 0 920 900" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{SVG_DEFS}
<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="{V}" stroke-width="3.5" opacity=".3"/>
<path d="M{cx},{cy - rad} A{rad},{rad} 0 1,1 {cx - 2},{cy - rad}" fill="none" stroke="{V}" stroke-width="4.5" marker-end="url(#arr)"/>
<marker id="arr" markerWidth="14" markerHeight="14" refX="10" refY="5" orient="auto">
  <path d="M0,0 L14,5 L0,10 Z" fill="{V}"/>
</marker>
{_turbo_icon(cx, cy, 58)}
{parts}
</svg>
</div>"""


def _box(label: str, icon: str, y: int) -> str:
    return f"""
<div class="dia-box" style="top:{y}px">
  <span class="dia-ico">{icon}</span>
  <span class="dia-lbl">{label}</span>
</div>"""


def _arrow_row(y: int, reverse: bool = False) -> str:
    cls = "dia-arrow-h rev" if reverse else "dia-arrow-h"
    return f'<div class="{cls}" style="top:{y}px"></div>'


def diagram_02() -> str:
    icons = {
        "TAREA": "📋",
        "ACCIÓN": "▶",
        "RESULTADO": "📈",
        "CONTEXTO": "◎",
        "QUÉ FUNCIONA": "★",
        "QUÉ FALLÓ": "✕",
        "QUÉ MEJORÓ": "↗",
        "QUÉ CAMBIAR": "💡",
    }
    left_keys = ["TAREA", "ACCIÓN", "RESULTADO", "CONTEXTO"]
    right_keys = ["QUÉ FUNCIONA", "QUÉ FALLÓ", "QUÉ MEJORÓ", "QUÉ CAMBIAR"]
    ys = [52, 142, 232, 322]
    left = "".join(_box(k, icons[k], y) for k, y in zip(left_keys, ys))
    right = "".join(_box(k, icons[k], y) for k, y in zip(right_keys, ys))
    arr_in = "".join(_arrow_row(y + 22) for y in ys)
    arr_out = "".join(_arrow_row(y + 22) for y in ys)
    return f"""
<div class="dia dia-02">
  <div class="dia-side"><div class="dia-hd">ENTRADA</div><div class="dia-boxes">{left}</div></div>
  <div class="dia-arrows in">{arr_in}</div>
  <div class="dia-mem">
    <div class="dia-hd mem">MEMORIA</div>
    <div class="dia-cylinder">
      <div class="cyl-stack">
        <div class="cyl-ring"></div><div class="cyl-ring"></div>
        <div class="cyl-ring"></div><div class="cyl-ring"></div>
        <div class="cyl-ring"></div>
      </div>
      <img class="cyl-brain" src="{elem('cerebro.png')}" alt=""/>
      <div class="cyl-base"></div>
      <div class="cyl-glow"></div>
    </div>
  </div>
  <div class="dia-arrows out">{arr_out}</div>
  <div class="dia-side"><div class="dia-hd">SALIDA</div><div class="dia-boxes">{right}</div></div>
</div>"""


def diagram_03() -> str:
    bars = [
        ("PRECISIÓN", "91%", 0.91),
        ("CALIDAD", "8.7/10", 0.87),
        ("ERRORES", "3", 0.15),
    ]
    rows = ""
    for lbl, val, pct in bars:
        rows += f"""
<div class="met-row">
  <div class="met-lbl">{lbl}</div>
  <div class="met-bar"><div class="met-fill" style="width:{pct*100:.0f}%"></div></div>
  <div class="met-val">{val}</div>
</div>"""
    return f"""
<div class="dia dia-03">
  <div class="dia-panel agent">
    <div class="dia-panel-hd">AGENTE TURBO</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-metricas.png')}" alt="" class="dia-robot"/></div>
  </div>
  <div class="dia-arrow-col">
    <div class="dia-arrow-line"></div>
    <div class="dia-arrow-tip"></div>
    <div class="dia-arrow-txt">EVALÚA<br/>CADA CORRIDA</div>
  </div>
  <div class="dia-panel score">
    <div class="dia-panel-hd">📊 PUNTUACIÓN</div>
    {rows}
    <div class="met-row goal">
      <div class="met-lbl">OBJETIVO CUMPLIDO</div>
      <div class="met-check">✓</div>
    </div>
    <div class="met-foot">Las puntuaciones usan tus criterios.</div>
  </div>
  <div class="dia-tag">⚡ DATOS → INSIGHT → MEJORA</div>
</div>"""


def diagram_04() -> str:
    checks = [
        ("✓", "¿QUÉ FUNCIONÓ?", V),
        ("✕", "¿QUÉ FALLÓ?", RD),
        ("→", "¿POR QUÉ FALLÓ?", V),
        ("↗", "¿QUÉ CAMBIAR?", V),
    ]
    clist = "".join(
        f'<div class="chk"><span class="chk-ico" style="color:{c}">{i}</span><span>{t}</span></div>'
        for i, t, c in checks
    )
    return f"""
<div class="dia dia-04">
  <div class="dia-panel agent">
    <div class="dia-panel-hd">AGENTE</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-agent.png')}" alt="" class="dia-robot sm"/></div>
    <div class="dia-subbox">
      <div class="dia-subhd">TRABAJO ENTREGADO</div>
      <div class="dia-subtxt">Resultados, acciones y decisiones de la corrida.</div>
    </div>
  </div>
  <div class="dia-arrow-col wide">
    <div class="dia-arrow-line long"></div>
    <div class="dia-arrow-tip"></div>
    <div class="dia-arrow-txt">ENVÍA TODO<br/>A REVISIÓN</div>
  </div>
  <div class="dia-panel critic">
    <div class="dia-panel-hd">CRÍTICO</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-critico.png')}" alt="" class="dia-robot md"/></div>
    <div class="dia-checklist">{clist}</div>
  </div>
</div>"""


def diagram_05() -> str:
    fails = {4, 6, 7, 10, 13, 19}
    cards = ""
    for n in range(1, 21):
        ok = n not in fails
        mark = "✓" if ok else "✕"
        cls = "ok" if ok else "bad"
        cards += f'<div class="task-card {cls}"><span class="tn">{n:02d}</span><span class="tm">{mark}</span></div>'
    steps = [
        ("✕", "6 FALLAS DETECTADAS", "Turbo no solo las registró.", RD),
        ("🔍", "ANALIZANDO CAUSAS", "Compara entradas, acciones y resultados.", TX),
        ("📊", "4 MISMA CAUSA RAÍZ", "Tareas distintas. Mismo problema.", TX),
        ("⚠", "PATRÓN ENCONTRADO", "Sigue fallando el <b>Paso #3</b> del flujo.", V),
    ]
    shtml = ""
    for ico, title, sub, col in steps:
        glow = ' glow' if col == V else ""
        shtml += f"""
<div class="flow-step{glow}">
  <span class="fs-ico">{ico}</span>
  <div><div class="fs-title" style="color:{col}">{title}</div><div class="fs-sub">{sub}</div></div>
</div>"""
    return f"""
<div class="dia dia-05">
  <div class="dia-history">
    <div class="dia-panel-hd">HISTORIAL DE TAREAS</div>
    <div class="task-grid">{cards}</div>
    <div class="task-foot">20 CORRIDAS | <span class="g">6 FALLAS</span></div>
  </div>
  <div class="dia-flow">{shtml}</div>
</div>"""


def diagram_06() -> str:
    v1_items = ["PIERDE CONTEXTO", "OLVIDA PASOS CLAVE", "SALIDAS INCONSISTENTES"]
    v2_items = ["MEJOR CONTEXTO", "MENOS ERRORES", "MÁS CONSISTENTE", "MAYOR CALIDAD"]
    imp = ["PROMPT ACTUALIZADO", "REGLAS REFINADAS", "MEMORIA EXPANDIDA", "FLUJO OPTIMIZADO", "HERRAMIENTAS MEJORADAS"]
    l1 = "".join(f'<div class="ver-item bad"><span>✕</span>{t}</div>' for t in v1_items)
    l2 = "".join(f'<div class="ver-item good"><span>✓</span>{t}</div>' for t in v2_items)
    limp = "".join(f'<div class="imp-item"><span>•</span>{t}</div>' for t in imp)
    return f"""
<div class="dia dia-06">
  <div class="dia-ver v1">
    <div class="dia-ver-hd">TURBO V1</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-v1.png')}" alt="" class="dia-robot sm"/></div>
    {l1}
  </div>
  <div class="dia-mid">
    <div class="dia-ver-hd">REFLEXIÓN</div>
    <div class="dia-big-arrow">→</div>
    <div class="imp-hd">MEJORAS APLICADAS:</div>
    <div class="imp-list">{limp}</div>
  </div>
  <div class="dia-ver v2 glow">
    <div class="dia-ver-hd g">TURBO V2</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-v2.png')}" alt="" class="dia-robot sm"/></div>
    {l2}
  </div>
</div>"""


def diagram_07() -> str:
    return f"""
<div class="dia dia-07">
  <div class="dia-verbox old">
    <div class="dia-ver-hd">VERSIÓN 1 (ANTERIOR)</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-vs-old.png')}" alt="" class="dia-robot xs"/></div>
    <div class="met-list">
      <div><span>PRECISIÓN</span><b>82%</b></div>
      <div><span>CALIDAD</span><b>7.4/10</b></div>
      <div><span>TAREAS OK</span><b>164/200</b></div>
      <div><span>ERRORES</span><b>12</b></div>
    </div>
    <div class="score-bar bad">PUNTAJE: <b>82</b> / 100</div>
  </div>
  <div class="dia-vs"><div class="vs-ring">VS</div></div>
  <div class="dia-verbox new glow">
    <div class="dia-ver-hd g">VERSIÓN 2 (NUEVA)</div>
    <div class="dia-robot-wrap"><img src="{elem('robot-vs-new.png')}" alt="" class="dia-robot xs"/></div>
    <div class="met-list g">
      <div><span>PRECISIÓN</span><b>91%</b></div>
      <div><span>CALIDAD</span><b>8.9/10</b></div>
      <div><span>TAREAS OK</span><b>182/200</b></div>
      <div><span>ERRORES</span><b>4</b></div>
    </div>
    <div class="score-bar good">PUNTAJE: <b>91</b> / 100</div>
  </div>
  <div class="dia-decisions">
    <div class="dec"><span class="d-ico g">✓</span><div class="d-txt g">¿MEJOR? QUEDATE.</div><div class="d-btn g">🚀 DESPLEGAR</div></div>
    <div class="dec"><span class="d-ico r">↩</span><div class="d-txt r">¿PEOR? DESCARTÁ.</div><div class="d-btn r">🗑 DESCARTAR</div></div>
    <div class="dec"><span class="d-ico y">…</span><div class="d-txt y">¿IGUAL? SEGUÍ PROBANDO.</div><div class="d-btn y">↻ ITERAR</div></div>
  </div>
</div>"""


def diagram_08() -> str:
    cx, cy, rad = 460, 248, 195
    nodes = [
        (cx, cy - rad, "⚡", "HACÉ", "Ejecutá la tarea"),
        (cx + int(rad * 0.87), cy - int(rad * 0.5), "📊", "MEDÍ", "Puntúa cada resultado"),
        (cx + int(rad * 0.87), cy + int(rad * 0.5), "🔍", "REFLEXIONÁ", "Critica y detecta fallas"),
        (cx, cy + rad - 8, "↗", "MEJORÁ", "Aplicá upgrades"),
        (cx - int(rad * 0.87), cy + int(rad * 0.5), "✓", "PROBÁ", "Demostrá que funciona"),
        (cx - int(rad * 0.87), cy - int(rad * 0.5), "🚀", "DESPLEGÁ", "Liberá la mejor versión"),
    ]
    dots = ""
    for x, y, ico, title, sub in nodes:
        dots += f"""
<g transform="translate({x},{y})">
  <circle r="36" fill="rgba(0,255,178,.06)" stroke="{V}" stroke-width="2.5" filter="url(#glowS)"/>
  <text text-anchor="middle" y="8" font-size="22">{ico}</text>
  <text text-anchor="middle" y="58" fill="{V}" font-family="'Barlow Condensed',sans-serif" font-weight="700" font-size="22">{title}</text>
  <text text-anchor="middle" y="78" fill="{GY}" font-family="'Barlow Condensed',sans-serif" font-size="14">{sub}</text>
</g>"""
    brain = elem("cerebro.png")
    return f"""
<div class="dia dia-08">
<svg viewBox="0 0 920 500" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{SVG_DEFS}
<circle cx="{cx}" cy="{cy}" r="{rad}" fill="none" stroke="{V}" stroke-width="2.5" opacity=".35"/>
<path d="M{cx},{cy - rad} A{rad},{rad} 0 1,1 {cx - 2},{cy - rad}" fill="none" stroke="{V}" stroke-width="3" opacity=".85"/>
<image href="{brain}" x="{cx - 60}" y="{cy - 52}" width="120" height="95" preserveAspectRatio="xMidYMid meet"/>
<text x="{cx}" y="{cy + 68}" text-anchor="middle" fill="{V}" font-family="'Bebas Neue',sans-serif" font-size="46">24/7</text>
<text x="{cx}" y="{cy + 92}" text-anchor="middle" fill="{TX}" font-family="'Barlow Condensed',sans-serif" font-size="14" letter-spacing=".12em">SIEMPRE MEJORANDO</text>
{dots}
</svg>
</div>"""


DIAGRAMS = {
    1: diagram_01,
    2: diagram_02,
    3: diagram_03,
    4: diagram_04,
    5: diagram_05,
    6: diagram_06,
    7: diagram_07,
    8: diagram_08,
}


def diagram(n: int) -> str:
    return DIAGRAMS[n]()


DIAGRAM_CSS = f"""
.dia{{position:relative;width:100%;height:100%;min-height:520px;display:flex;align-items:center;justify-content:center;}}
.dia svg{{width:100%;height:auto;max-height:620px;display:block;}}
.dia-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:17px;letter-spacing:.14em;color:{V};margin-bottom:14px;text-transform:uppercase;}}
.dia-side{{position:relative;z-index:2;width:250px;}}
.dia-boxes{{position:relative;height:400px;}}
.dia-box{{position:absolute;left:0;display:flex;align-items:center;gap:12px;width:100%;padding:14px 16px;
  border:2px solid rgba(0,255,178,.5);border-radius:12px;background:rgba(0,0,0,.55);
  box-shadow:0 0 16px rgba(0,255,178,.08);}}
.dia-ico{{font-size:22px;color:{V};width:28px;text-align:center;flex-shrink:0;}}
.dia-lbl{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:18px;letter-spacing:.04em;color:{TX};line-height:1.1;}}
.dia-02{{display:grid;grid-template-columns:250px 64px 240px 64px 250px;gap:4px;align-items:center;width:100%;max-width:960px;position:relative;min-height:460px;}}
.dia-arrows{{position:relative;height:400px;margin-top:36px;}}
.dia-arrow-h{{position:absolute;left:0;right:0;height:4px;background:linear-gradient(90deg,{V},rgba(0,255,178,.25));
  border-radius:2px;box-shadow:0 0 12px rgba(0,255,178,.45);}}
.dia-arrow-h::after{{content:'';position:absolute;right:-2px;top:50%;transform:translateY(-50%);
  border-top:7px solid transparent;border-bottom:7px solid transparent;border-left:11px solid {V};}}
.dia-arrow-h.rev{{background:linear-gradient(270deg,{V},rgba(0,255,178,.25));}}
.dia-arrow-h.rev::after{{right:auto;left:-2px;border-left:none;border-right:11px solid {V};}}
.dia-mem{{display:flex;flex-direction:column;align-items:center;z-index:2;}}
.dia-mem .mem{{text-align:center;font-size:18px;}}
.dia-cylinder{{position:relative;width:220px;height:260px;display:flex;align-items:center;justify-content:center;}}
.cyl-stack{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:8px;padding:0 12px;}}
.cyl-ring{{height:34px;border:2.5px solid {V};border-radius:50%;opacity:.6;box-shadow:0 0 16px rgba(0,255,178,.3);}}
.cyl-brain{{position:relative;z-index:3;width:120px;height:120px;object-fit:contain;
  filter:drop-shadow(0 0 14px rgba(0,255,178,.75));mix-blend-mode:screen;}}
.cyl-base{{position:absolute;bottom:10px;width:170px;height:10px;border:2.5px solid {V};border-radius:50%;opacity:.65;
  box-shadow:0 0 20px rgba(0,255,178,.35);}}
.cyl-glow{{position:absolute;inset:20px;border-radius:50%;background:radial-gradient(circle,rgba(0,255,178,.12),transparent 70%);pointer-events:none;}}
.dia-03,.dia-04{{display:flex;align-items:center;justify-content:center;gap:20px;width:100%;max-width:960px;flex-wrap:nowrap;min-height:620px;}}
.dia-panel{{border:2px solid rgba(0,255,178,.55);border-radius:16px;padding:18px;background:rgba(0,0,0,.4);flex:0 0 auto;
  box-shadow:0 0 24px rgba(0,255,178,.06);}}
.dia-01{{min-height:0;flex:1 1 auto;align-items:stretch;width:100%;}}
.dia-01 svg{{max-height:none;min-height:0;height:100%;width:100%;flex:1;}}
.dia-panel.agent{{width:260px;text-align:center;}}
.dia-panel.critic{{width:340px;}}
.dia-panel.score{{width:360px;}}
.dia-panel-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:16px;letter-spacing:.12em;color:{V};margin-bottom:14px;text-transform:uppercase;}}
.dia-robot-wrap{{display:flex;align-items:center;justify-content:center;min-height:260px;padding:6px 0;overflow:visible;}}
.dia-robot{{max-width:100%;max-height:300px;width:auto;height:auto;object-fit:contain;object-position:center;display:block;margin:0 auto;
  filter:drop-shadow(0 4px 20px rgba(0,255,178,.2));}}
.dia-robot.sm{{max-height:270px;}}.dia-robot.md{{max-height:300px;}}.dia-robot.xs{{max-height:280px;min-width:160px;}}
.dia-ver .dia-robot-wrap{{min-height:240px;}}
.dia-verbox .dia-robot-wrap{{min-height:240px;}}
.dia-panel.agent .dia-robot-wrap{{min-height:280px;}}
.dia-arrow-col{{display:flex;flex-direction:column;align-items:center;gap:8px;flex:0 0 110px;}}
.dia-arrow-col.wide{{flex-basis:130px;}}
.dia-arrow-line{{width:80px;height:5px;background:linear-gradient(90deg,{V},rgba(0,255,178,.3));border-radius:2px;box-shadow:0 0 12px rgba(0,255,178,.55);}}
.dia-arrow-line.long{{width:100px;}}
.dia-arrow-tip{{width:0;height:0;border-top:8px solid transparent;border-bottom:8px solid transparent;border-left:14px solid {V};margin-left:4px;align-self:flex-end;margin-right:22px;}}
.dia-arrow-txt{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:15px;letter-spacing:.06em;color:{TX};text-align:center;line-height:1.25;margin-top:4px;}}
.met-row{{display:grid;grid-template-columns:1fr 130px 70px;align-items:center;gap:10px;margin:10px 0;font-family:'Barlow Condensed',sans-serif;font-size:16px;color:{TX};}}
.met-lbl{{font-weight:600;letter-spacing:.04em;}}
.met-bar{{height:10px;background:rgba(255,255,255,.1);border-radius:5px;overflow:hidden;}}
.met-fill{{height:100%;background:{V};border-radius:5px;box-shadow:0 0 10px rgba(0,255,178,.55);}}
.met-val{{font-weight:700;text-align:right;font-size:17px;}}
.met-row.goal{{grid-template-columns:1fr 44px;margin-top:14px;}}
.met-check{{width:36px;height:36px;border-radius:50%;border:2px solid {V};color:{V};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;}}
.met-foot{{font-size:13px;color:{GY};margin-top:12px;font-family:'Barlow Condensed',sans-serif;}}
.dia-tag{{position:absolute;bottom:-4px;left:50%;transform:translateX(-50%);padding:10px 20px;border:2px solid {V};border-radius:999px;
  font-family:'IBM Plex Mono',monospace;font-size:13px;letter-spacing:.08em;color:{V};white-space:nowrap;background:rgba(0,0,0,.7);}}
.dia-subbox{{margin-top:12px;padding:12px;border-top:1px solid rgba(0,255,178,.25);text-align:left;}}
.dia-subhd{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:{V};letter-spacing:.1em;margin-bottom:4px;}}
.dia-subtxt{{font-family:'Barlow Condensed',sans-serif;font-size:14px;color:{GY};line-height:1.35;}}
.dia-checklist{{margin-top:10px;border-top:1px solid rgba(255,255,255,.08);}}
.chk{{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06);
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em;color:{TX};}}
.chk-ico{{width:26px;text-align:center;font-weight:700;font-size:17px;}}
.dia-05{{display:flex;gap:24px;width:100%;max-width:960px;align-items:stretch;min-height:680px;flex:1;}}
.dia-history{{flex:0 0 420px;border:2px solid rgba(0,255,178,.5);border-radius:16px;padding:22px;background:rgba(0,0,0,.4);}}
.task-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:16px 0;}}
.task-card{{border:1.5px solid rgba(255,255,255,.14);border-radius:10px;padding:14px 10px;text-align:center;font-family:'IBM Plex Mono',monospace;font-size:14px;}}
.task-card.ok .tm{{color:{V};}}.task-card.bad .tm{{color:{RD};}}
.tn{{display:block;color:{GY};font-size:13px;}}.tm{{display:block;font-size:20px;font-weight:700;}}
.task-foot{{font-family:'IBM Plex Mono',monospace;font-size:14px;letter-spacing:.06em;color:{TX};border-top:1px solid rgba(255,255,255,.1);padding-top:12px;}}
.task-foot .g{{color:{V};}}
.dia-flow{{flex:1;display:flex;flex-direction:column;gap:16px;justify-content:center;}}
.flow-step{{display:flex;gap:14px;align-items:flex-start;padding:18px;border:2px solid rgba(255,255,255,.12);border-radius:14px;background:rgba(0,0,0,.35);}}
.flow-step.glow{{border-color:{V};box-shadow:0 0 24px rgba(0,255,178,.18);}}
.fs-ico{{font-size:26px;width:34px;text-align:center;}}
.fs-title{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:20px;letter-spacing:.04em;margin-bottom:4px;}}
.fs-sub{{font-family:'Barlow Condensed',sans-serif;font-size:15px;color:{GY};line-height:1.35;}}
.fs-sub b{{color:{V};}}
.dia-06{{display:flex;gap:18px;width:100%;max-width:960px;align-items:stretch;min-height:560px;}}
.dia-ver{{flex:1;border:2px solid rgba(255,255,255,.18);border-radius:16px;padding:18px;text-align:center;background:rgba(0,0,0,.35);}}
.dia-ver.glow{{border-color:{V};box-shadow:0 0 28px rgba(0,255,178,.14);}}
.dia-ver-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.12em;color:{TX};margin-bottom:10px;}}
.dia-ver-hd.g{{color:{V};}}
.dia-mid{{flex:0 0 220px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
.dia-big-arrow{{font-size:56px;color:{V};text-shadow:0 0 24px rgba(0,255,178,.65);margin:10px 0;}}
.imp-hd{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:{V};letter-spacing:.1em;margin:10px 0 6px;}}
.imp-list{{text-align:left;width:100%;}}
.imp-item{{font-family:'Barlow Condensed',sans-serif;font-size:13px;color:{TX};padding:5px 0;border-bottom:1px dotted rgba(255,255,255,.08);}}
.imp-item span{{color:{V};margin-right:6px;}}
.ver-item{{display:flex;align-items:center;gap:10px;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14px;color:{TX};padding:8px 0;text-align:left;}}
.ver-item.bad span{{color:{RD};}}.ver-item.good span{{color:{V};}}
.dia-07{{display:flex;flex-wrap:wrap;gap:16px;width:100%;max-width:960px;justify-content:center;align-items:flex-start;position:relative;padding-bottom:80px;min-height:560px;}}
.dia-verbox{{flex:0 0 300px;border:2px solid rgba(255,255,255,.22);border-radius:16px;padding:18px;text-align:center;background:rgba(0,0,0,.4);}}
.dia-verbox.glow{{border-color:{V};box-shadow:0 0 28px rgba(0,255,178,.12);}}
.dia-vs{{flex:0 0 64px;display:flex;align-items:center;justify-content:center;align-self:center;}}
.vs-ring{{width:58px;height:58px;border-radius:50%;border:2.5px solid {V};color:{V};display:flex;align-items:center;justify-content:center;
  font-family:'Bebas Neue',sans-serif;font-size:24px;box-shadow:0 0 20px rgba(0,255,178,.45);}}
.met-list{{text-align:left;margin:12px 0;font-family:'Barlow Condensed',sans-serif;font-size:15px;color:{TX};}}
.met-list div{{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.08);}}
.met-list.g b{{color:{V};font-size:16px;}}
.score-bar{{margin-top:12px;padding:12px;border-radius:10px;font-family:'IBM Plex Mono',monospace;font-size:14px;background:rgba(255,255,255,.05);}}
.score-bar.bad b{{color:{RD};font-size:16px;}}.score-bar.good b{{color:{V};font-size:16px;}}
.dia-decisions{{position:absolute;bottom:0;left:0;right:0;display:flex;gap:12px;justify-content:center;}}
.dec{{flex:1;max-width:300px;text-align:center;padding:10px;}}
.d-ico{{display:inline-flex;width:36px;height:36px;border-radius:50%;align-items:center;justify-content:center;font-weight:700;margin-bottom:6px;font-size:16px;}}
.d-ico.g{{background:rgba(0,255,178,.15);color:{V};border:1px solid {V};}}
.d-ico.r{{background:rgba(255,82,82,.12);color:{RD};border:1px solid {RD};}}
.d-ico.y{{background:rgba(255,193,7,.12);color:{YL};border:1px solid {YL};}}
.d-txt{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14px;margin-bottom:8px;}}
.d-txt.g{{color:{V};}}.d-txt.r{{color:{RD};}}.d-txt.y{{color:{YL};}}
.d-btn{{display:inline-block;padding:8px 16px;border-radius:999px;font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.06em;}}
.d-btn.g{{border:1px solid {V};color:{V};}}
.d-btn.r{{border:1px solid {RD};color:{RD};}}
.d-btn.y{{border:1px solid {YL};color:{YL};}}
.dia-08{{min-height:440px;}}
.dia-08 svg{{max-height:500px;min-height:440px;}}
"""
