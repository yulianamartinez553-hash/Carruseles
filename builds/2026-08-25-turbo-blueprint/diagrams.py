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
  <circle cx="0" cy="0" r="{r}" fill="none" stroke="{V}" stroke-width="2.5"/>
  <path d="M-4,-14 L8,0 L-2,0 L4,14 L-8,0 L2,0 Z" fill="{V}"/>
</g>"""


def diagram_01() -> str:
    return f"""
<div class="dia dia-01">
<svg viewBox="0 0 920 720" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{SVG_DEFS}
<circle cx="460" cy="360" r="250" fill="none" stroke="{V}" stroke-width="3" opacity=".35"/>
<path d="M460,110 A250,250 0 1,1 458,110" fill="none" stroke="{V}" stroke-width="3.5" marker-end="url(#arr)"/>
<marker id="arr" markerWidth="10" markerHeight="10" refX="7" refY="4" orient="auto">
  <path d="M0,0 L10,4 L0,8 Z" fill="{V}"/>
</marker>
{_turbo_icon(460, 360, 44)}
<g font-family="'Barlow Condensed',sans-serif" font-weight="700" font-size="28" fill="{TX}" text-anchor="middle">
  <g transform="translate(460,28)"><circle cx="0" cy="26" r="30" fill="none" stroke="{V}" stroke-width="2.5"/>
    <polygon points="-8,26 6,18 6,34" fill="{V}"/><text y="72" fill="{V}">HACÉ</text></g>
  <g transform="translate(670,175)"><circle cx="0" cy="26" r="30" fill="none" stroke="{V}" stroke-width="2.5"/>
    <rect x="-11" y="14" width="5" height="18" fill="{V}"/><rect x="-3" y="10" width="5" height="22" fill="{V}"/><rect x="6" y="6" width="5" height="26" fill="{V}"/>
    <text y="68" fill="{V}">MEDÍ</text></g>
  <g transform="translate(670,545)"><circle cx="0" cy="26" r="30" fill="none" stroke="{V}" stroke-width="2.5"/>
    <path d="M-9,30 L-1,16 L6,24 L13,8" fill="none" stroke="{V}" stroke-width="3" stroke-linecap="round"/>
    <text y="68" fill="{V}">PROBÁ</text></g>
  <g transform="translate(460,640)"><circle cx="0" cy="26" r="30" fill="none" stroke="{V}" stroke-width="2.5"/>
    <path d="M-6,20 L0,10 L6,20 L0,30 Z" fill="none" stroke="{V}" stroke-width="2.5"/><line x1="0" y1="30" x2="0" y2="38" stroke="{V}" stroke-width="2.5"/>
    <text y="68" fill="{V}">MEJORÁ</text></g>
  <g transform="translate(250,545)"><circle cx="0" cy="26" r="30" fill="none" stroke="{V}" stroke-width="2.5"/>
    <circle cx="0" cy="26" r="11" fill="none" stroke="{V}" stroke-width="2.5"/><path d="M-5,30 L0,38 L10,20" fill="none" stroke="{V}" stroke-width="3"/>
    <text y="68" fill="{V}">REFLEXIONÁ</text></g>
</g>
</svg>
</div>"""


def _box(label: str, icon: str, x: int, y: int) -> str:
    return f"""
<div class="dia-box" style="left:{x}px;top:{y}px">
  <span class="dia-ico">{icon}</span>
  <span class="dia-lbl">{label}</span>
</div>"""


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
    left = "".join(
        _box(k, icons[k], 0, i * 72)
        for i, k in enumerate(["TAREA", "ACCIÓN", "RESULTADO", "CONTEXTO"])
    )
    right = "".join(
        _box(k, icons[k], 0, i * 72)
        for i, k in enumerate(["QUÉ FUNCIONA", "QUÉ FALLÓ", "QUÉ MEJORÓ", "QUÉ CAMBIAR"])
    )
    return f"""
<div class="dia dia-02">
  <div class="dia-col"><div class="dia-hd">ENTRADA</div>{left}</div>
  <div class="dia-mem">
    <div class="dia-hd mem">MEMORIA</div>
    <div class="dia-cylinder">
      <div class="cyl-stack">
        <div class="cyl-ring"></div><div class="cyl-ring"></div>
        <div class="cyl-ring"></div><div class="cyl-ring"></div>
      </div>
      <img class="cyl-brain" src="{elem('cerebro.png')}" alt=""/>
      <div class="cyl-base"></div>
    </div>
  </div>
  <div class="dia-col right"><div class="dia-hd">SALIDA</div>{right}</div>
  <svg class="dia-wires" viewBox="0 0 920 320" preserveAspectRatio="none">
    <path d="M200,40 C280,40 300,160 380,160" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M200,112 C280,112 300,160 380,160" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M200,184 C280,184 300,160 380,160" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M200,256 C280,256 300,160 380,160" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M540,160 C620,160 640,40 720,40" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M540,160 C620,160 640,112 720,112" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M540,160 C620,160 640,184 720,184" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
    <path d="M540,160 C620,160 640,256 720,256" fill="none" stroke="{V}" stroke-width="2" opacity=".7"/>
  </svg>
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
    fails = {4, 7, 10, 13, 19}
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
    nodes = [
        (460, 30, "⚡", "HACÉ", "Ejecutá la tarea"),
        (680, 120, "📊", "MEDÍ", "Puntúa cada resultado"),
        (720, 300, "🔍", "REFLEXIONÁ", "Critica y detecta fallas"),
        (460, 420, "↗", "MEJORÁ", "Aplicá upgrades"),
        (200, 300, "✓", "PROBÁ", "Demostrá que funciona"),
        (240, 120, "🚀", "DESPLEGÁ", "Liberá la mejor versión"),
    ]
    dots = ""
    for x, y, ico, title, sub in nodes:
        dots += f"""
<g transform="translate({x},{y})">
  <circle r="28" fill="none" stroke="{V}" stroke-width="2" filter="url(#glowS)"/>
  <text text-anchor="middle" y="6" font-size="18">{ico}</text>
  <text text-anchor="middle" y="48" fill="{V}" font-family="'Barlow Condensed',sans-serif" font-weight="700" font-size="18">{title}</text>
  <text text-anchor="middle" y="68" fill="{GY}" font-family="'Barlow Condensed',sans-serif" font-size="13">{sub}</text>
</g>"""
    return f"""
<div class="dia dia-08">
<svg viewBox="0 0 920 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
{SVG_DEFS}
<circle cx="460" cy="240" r="175" fill="none" stroke="{V}" stroke-width="2" opacity=".4"/>
<path d="M460,65 A175,175 0 1,1 458,65" fill="none" stroke="{V}" stroke-width="2.5" opacity=".8"/>
<image href="{elem('cerebro.png')}" x="395" y="175" width="130" height="100" preserveAspectRatio="xMidYMid meet"/>
<text x="460" y="310" text-anchor="middle" fill="{V}" font-family="'Bebas Neue',sans-serif" font-size="42">24/7</text>
<text x="460" y="335" text-anchor="middle" fill="{TX}" font-family="'Barlow Condensed',sans-serif" font-size="14" letter-spacing=".12em">SIEMPRE MEJORANDO</text>
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
.dia svg{{width:100%;height:auto;max-height:560px;display:block;}}
.dia-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.14em;color:{V};margin-bottom:12px;text-transform:uppercase;}}
.dia-col{{position:relative;z-index:2;width:200px;min-height:300px;}}
.dia-col.right{{margin-left:auto;}}
.dia-box{{position:absolute;display:flex;align-items:center;gap:10px;width:190px;padding:10px 12px;
  border:1.5px solid rgba(0,255,178,.45);border-radius:10px;background:rgba(0,0,0,.5);}}
.dia-ico{{font-size:16px;color:{V};width:22px;text-align:center;flex-shrink:0;}}
.dia-lbl{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:15px;letter-spacing:.04em;color:{TX};line-height:1.1;}}
.dia-02{{display:grid;grid-template-columns:200px 1fr 200px;gap:8px;align-items:center;width:100%;max-width:920px;position:relative;}}
.dia-mem{{display:flex;flex-direction:column;align-items:center;z-index:2;}}
.dia-mem .mem{{text-align:center;}}
.dia-cylinder{{position:relative;width:180px;height:200px;display:flex;align-items:center;justify-content:center;}}
.cyl-stack{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:6px;}}
.cyl-ring{{height:28px;border:2px solid {V};border-radius:50%;opacity:.55;box-shadow:0 0 12px rgba(0,255,178,.25);}}
.cyl-brain{{position:relative;z-index:3;width:90px;height:90px;object-fit:contain;filter:drop-shadow(0 0 8px rgba(0,255,178,.6));}}
.cyl-base{{position:absolute;bottom:8px;width:140px;height:8px;border:2px solid {V};border-radius:50%;opacity:.6;}}
.dia-wires{{position:absolute;inset:0;width:100%;height:100%;z-index:1;pointer-events:none;}}
.dia-03,.dia-04{{display:flex;align-items:center;justify-content:center;gap:16px;width:100%;max-width:920px;flex-wrap:nowrap;}}
.dia-panel{{border:2px solid rgba(0,255,178,.5);border-radius:14px;padding:14px;background:rgba(0,0,0,.35);flex:0 0 auto;}}
.dia-01{{min-height:760px;align-items:stretch;}}
.dia-01 svg{{max-height:none;min-height:720px;height:100%;width:100%;}}
.dia-panel.agent{{width:240px;text-align:center;}}
.dia-panel.critic{{width:320px;}}
.dia-panel.score{{width:340px;}}
.dia-panel-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.12em;color:{V};margin-bottom:10px;text-transform:uppercase;}}
.dia-robot-wrap{{display:flex;align-items:center;justify-content:center;min-height:240px;padding:4px 0;}}
.dia-robot{{max-width:100%;max-height:280px;width:auto;height:auto;object-fit:contain;object-position:center;display:block;margin:0 auto;
  filter:drop-shadow(0 4px 16px rgba(0,255,178,.15));}}
.dia-robot.sm{{max-height:250px;}}.dia-robot.md{{max-height:280px;}}.dia-robot.xs{{max-height:250px;min-width:140px;}}
.dia-ver .dia-robot-wrap{{min-height:220px;overflow:visible;}}
.dia-verbox .dia-robot-wrap{{min-height:220px;overflow:visible;}}
.dia-panel.agent .dia-robot-wrap{{min-height:260px;overflow:visible;}}
.dia-arrow-col{{display:flex;flex-direction:column;align-items:center;gap:6px;flex:0 0 100px;}}
.dia-arrow-col.wide{{flex-basis:120px;}}
.dia-arrow-line{{width:70px;height:4px;background:linear-gradient(90deg,{V},rgba(0,255,178,.3));border-radius:2px;box-shadow:0 0 10px rgba(0,255,178,.5);}}
.dia-arrow-line.long{{width:90px;}}
.dia-arrow-tip{{width:0;height:0;border-top:7px solid transparent;border-bottom:7px solid transparent;border-left:12px solid {V};margin-left:4px;align-self:flex-end;margin-right:20px;}}
.dia-arrow-txt{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:13px;letter-spacing:.06em;color:{TX};text-align:center;line-height:1.25;margin-top:4px;}}
.met-row{{display:grid;grid-template-columns:1fr 120px 60px;align-items:center;gap:8px;margin:8px 0;font-family:'Barlow Condensed',sans-serif;font-size:14px;color:{TX};}}
.met-lbl{{font-weight:600;letter-spacing:.04em;}}
.met-bar{{height:8px;background:rgba(255,255,255,.08);border-radius:4px;overflow:hidden;}}
.met-fill{{height:100%;background:{V};border-radius:4px;box-shadow:0 0 8px rgba(0,255,178,.5);}}
.met-val{{font-weight:700;text-align:right;}}
.met-row.goal{{grid-template-columns:1fr 40px;margin-top:12px;}}
.met-check{{width:32px;height:32px;border-radius:50%;border:2px solid {V};color:{V};display:flex;align-items:center;justify-content:center;font-weight:700;}}
.met-foot{{font-size:12px;color:{GY};margin-top:10px;font-family:'Barlow Condensed',sans-serif;}}
.dia-tag{{position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);padding:8px 16px;border:1.5px solid {V};border-radius:999px;
  font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.08em;color:{V};white-space:nowrap;background:rgba(0,0,0,.6);}}
.dia-subbox{{margin-top:10px;padding:10px;border-top:1px solid rgba(0,255,178,.25);text-align:left;}}
.dia-subhd{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:{V};letter-spacing:.1em;margin-bottom:4px;}}
.dia-subtxt{{font-family:'Barlow Condensed',sans-serif;font-size:13px;color:{GY};line-height:1.3;}}
.dia-checklist{{margin-top:8px;border-top:1px solid rgba(255,255,255,.08);}}
.chk{{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.06);
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14px;letter-spacing:.04em;color:{TX};}}
.chk-ico{{width:24px;text-align:center;font-weight:700;}}
.dia-05{{display:flex;gap:20px;width:100%;max-width:920px;align-items:flex-start;}}
.dia-history{{flex:0 0 340px;border:2px solid rgba(0,255,178,.45);border-radius:14px;padding:14px;background:rgba(0,0,0,.35);}}
.task-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:10px 0;}}
.task-card{{border:1px solid rgba(255,255,255,.12);border-radius:8px;padding:6px 4px;text-align:center;font-family:'IBM Plex Mono',monospace;font-size:11px;}}
.task-card.ok .tm{{color:{V};}}.task-card.bad .tm{{color:{RD};}}
.tn{{display:block;color:{GY};font-size:10px;}}.tm{{display:block;font-size:14px;font-weight:700;}}
.task-foot{{font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.06em;color:{TX};border-top:1px solid rgba(255,255,255,.1);padding-top:8px;}}
.task-foot .g{{color:{V};}}
.dia-flow{{flex:1;display:flex;flex-direction:column;gap:10px;}}
.flow-step{{display:flex;gap:12px;align-items:flex-start;padding:12px;border:1.5px solid rgba(255,255,255,.1);border-radius:12px;background:rgba(0,0,0,.3);}}
.flow-step.glow{{border-color:{V};box-shadow:0 0 20px rgba(0,255,178,.15);}}
.fs-ico{{font-size:20px;width:28px;text-align:center;}}
.fs-title{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:16px;letter-spacing:.04em;margin-bottom:2px;}}
.fs-sub{{font-family:'Barlow Condensed',sans-serif;font-size:13px;color:{GY};line-height:1.3;}}
.fs-sub b{{color:{V};}}
.dia-06{{display:flex;gap:14px;width:100%;max-width:920px;align-items:stretch;}}
.dia-ver{{flex:1;border:2px solid rgba(255,255,255,.15);border-radius:14px;padding:14px;text-align:center;background:rgba(0,0,0,.3);}}
.dia-ver.glow{{border-color:{V};box-shadow:0 0 24px rgba(0,255,178,.12);}}
.dia-ver-hd{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.12em;color:{TX};margin-bottom:8px;}}
.dia-ver-hd.g{{color:{V};}}
.dia-mid{{flex:0 0 200px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}}
.dia-big-arrow{{font-size:48px;color:{V};text-shadow:0 0 20px rgba(0,255,178,.6);margin:8px 0;}}
.imp-hd{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:{V};letter-spacing:.1em;margin:8px 0 4px;}}
.imp-list{{text-align:left;width:100%;}}
.imp-item{{font-family:'Barlow Condensed',sans-serif;font-size:12px;color:{TX};padding:4px 0;border-bottom:1px dotted rgba(255,255,255,.08);}}
.imp-item span{{color:{V};margin-right:6px;}}
.ver-item{{display:flex;align-items:center;gap:8px;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:13px;color:{TX};padding:6px 0;text-align:left;}}
.ver-item.bad span{{color:{RD};}}.ver-item.good span{{color:{V};}}
.dia-07{{display:flex;flex-wrap:wrap;gap:12px;width:100%;max-width:920px;justify-content:center;align-items:flex-start;position:relative;padding-bottom:70px;}}
.dia-verbox{{flex:0 0 280px;border:2px solid rgba(255,255,255,.2);border-radius:14px;padding:14px;text-align:center;background:rgba(0,0,0,.35);}}
.dia-verbox.glow{{border-color:{V};}}
.dia-vs{{flex:0 0 60px;display:flex;align-items:center;justify-content:center;align-self:center;}}
.vs-ring{{width:52px;height:52px;border-radius:50%;border:2px solid {V};color:{V};display:flex;align-items:center;justify-content:center;
  font-family:'Bebas Neue',sans-serif;font-size:22px;box-shadow:0 0 16px rgba(0,255,178,.4);}}
.met-list{{text-align:left;margin:10px 0;font-family:'Barlow Condensed',sans-serif;font-size:14px;color:{TX};}}
.met-list div{{display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.06);}}
.met-list.g b{{color:{V};}}
.score-bar{{margin-top:10px;padding:10px;border-radius:8px;font-family:'IBM Plex Mono',monospace;font-size:13px;background:rgba(255,255,255,.04);}}
.score-bar.bad b{{color:{RD};}}.score-bar.good b{{color:{V};}}
.dia-decisions{{position:absolute;bottom:0;left:0;right:0;display:flex;gap:10px;justify-content:center;}}
.dec{{flex:1;max-width:280px;text-align:center;padding:8px;}}
.d-ico{{display:inline-flex;width:32px;height:32px;border-radius:50%;align-items:center;justify-content:center;font-weight:700;margin-bottom:4px;}}
.d-ico.g{{background:rgba(0,255,178,.15);color:{V};border:1px solid {V};}}
.d-ico.r{{background:rgba(255,82,82,.12);color:{RD};border:1px solid {RD};}}
.d-ico.y{{background:rgba(255,193,7,.12);color:{YL};border:1px solid {YL};}}
.d-txt{{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:13px;margin-bottom:6px;}}
.d-txt.g{{color:{V};}}.d-txt.r{{color:{RD};}}.d-txt.y{{color:{YL};}}
.d-btn{{display:inline-block;padding:6px 14px;border-radius:999px;font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.06em;}}
.d-btn.g{{border:1px solid {V};color:{V};}}
.d-btn.r{{border:1px solid {RD};color:{RD};}}
.d-btn.y{{border:1px solid {YL};color:{YL};}}
.dia-08 svg{{max-height:520px;}}
"""
