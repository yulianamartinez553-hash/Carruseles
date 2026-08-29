# -*- coding: utf-8 -*-
"""Diagramas estilo manifiesto/lino — Cómo construí Turbo (10 slides)."""
from __future__ import annotations

import base64
import math
from pathlib import Path

B = Path(__file__).resolve().parent
ELEM = B / "assets" / "elements"

O = "#C9562F"
TX = "#1C1814"
GY = "#6E6258"
BD = "#B8A898"
PN = "#2A2622"
CR = "#EDE8DC"
ST = "#F5E6B8"


def elem(name: str) -> str:
    return f"data:image/png;base64,{base64.b64encode((ELEM / name).read_bytes()).decode()}"


def _ico(svg: str) -> str:
    return f'<span class="ico">{svg}</span>'


IC = {
    "bolt": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z" fill="{O}"/></svg>',
    "brain": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M12 4c-3 0-5 2-5 5 0 1 .5 2 1 3-1 1-2 2-2 4 0 2 2 4 4 4h4c2 0 4-2 4-4 0-2-1-3-2-4 1-1 1-2 1-3 0-3-2-5-5-5z" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "wave": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M2 12c2-3 4-3 6 0s4 3 6 0 4-3 6 0" fill="none" stroke="{O}" stroke-width="2"/><path d="M2 16c2-3 4-3 6 0s4 3 6 0 4-3 6 0" fill="none" stroke="{O}" stroke-width="1.5" opacity=".6"/></svg>',
    "grid": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="4" y="4" width="7" height="7" rx="1" fill="none" stroke="{O}" stroke-width="2"/><rect x="13" y="4" width="7" height="7" rx="1" fill="none" stroke="{O}" stroke-width="2"/><rect x="4" y="13" width="7" height="7" rx="1" fill="none" stroke="{O}" stroke-width="2"/><rect x="13" y="13" width="7" height="7" rx="1" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "mic": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="9" y="3" width="6" height="11" rx="3" fill="none" stroke="{O}" stroke-width="2"/><path d="M5 11a7 7 0 0014 0M12 18v3" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "chip": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="5" y="5" width="14" height="14" rx="2" fill="none" stroke="{O}" stroke-width="2"/><rect x="9" y="9" width="6" height="6" fill="{O}"/></svg>',
    "mod": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="3" y="8" width="8" height="8" rx="2" fill="none" stroke="{O}" stroke-width="2"/><rect x="13" y="8" width="8" height="8" rx="2" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "list": f'<svg viewBox="0 0 24 24" width="32" height="32"><line x1="8" y1="6" x2="21" y2="6" stroke="{O}" stroke-width="2"/><line x1="8" y1="12" x2="21" y2="12" stroke="{O}" stroke-width="2"/><line x1="8" y1="18" x2="21" y2="18" stroke="{O}" stroke-width="2"/><circle cx="4" cy="6" r="1.5" fill="{O}"/><circle cx="4" cy="12" r="1.5" fill="{O}"/><circle cx="4" cy="18" r="1.5" fill="{O}"/></svg>',
    "shield": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M12 2l8 4v6c0 5-4 9-8 10C8 21 4 17 4 12V6l8-4z" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "clock": f'<svg viewBox="0 0 24 24" width="32" height="32"><circle cx="12" cy="12" r="9" fill="none" stroke="{O}" stroke-width="2"/><path d="M12 7v5l3 3" fill="none" stroke="{O}" stroke-width="2" stroke-linecap="round"/></svg>',
    "search": f'<svg viewBox="0 0 24 24" width="32" height="32"><circle cx="10" cy="10" r="7" fill="none" stroke="{O}" stroke-width="2"/><line x1="15" y1="15" x2="21" y2="21" stroke="{O}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "target": f'<svg viewBox="0 0 24 24" width="32" height="32"><circle cx="12" cy="12" r="9" fill="none" stroke="{O}" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="{O}" stroke-width="2"/><circle cx="12" cy="12" r="1.5" fill="{O}"/></svg>',
    "folder": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M3 7h7l2 2h9v10H3V7z" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "db": f'<svg viewBox="0 0 24 24" width="32" height="32"><ellipse cx="12" cy="6" rx="8" ry="3" fill="none" stroke="{O}" stroke-width="2"/><path d="M4 6v12c0 2 4 3 8 3s8-1 8-3V6" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "msg": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="3" y="5" width="18" height="13" rx="3" fill="none" stroke="{O}" stroke-width="2"/></svg>',
    "chart": f'<svg viewBox="0 0 24 24" width="32" height="32"><rect x="4" y="12" width="4" height="8" fill="{O}"/><rect x="10" y="8" width="4" height="12" fill="{O}"/><rect x="16" y="4" width="4" height="16" fill="{O}"/></svg>',
    "check": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M4 12l6 6L20 6" fill="none" stroke="{O}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "x": f'<svg viewBox="0 0 24 24" width="32" height="32"><path d="M6 6l12 12M18 6L6 18" stroke="{O}" stroke-width="2.5" stroke-linecap="round"/></svg>',
    "play": f'<svg viewBox="0 0 24 24" width="32" height="32"><polygon points="8,5 19,12 8,19" fill="{O}"/></svg>',
    "people": f'<svg viewBox="0 0 24 24" width="32" height="32"><circle cx="9" cy="8" r="3" fill="none" stroke="{O}" stroke-width="2"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6" fill="none" stroke="{O}" stroke-width="2"/></svg>',
}


def sphere_svg() -> str:
    pts = []
    lines = []
    rng = 42
    for lat in range(-3, 4):
        for lon in range(0, 8):
            ang1 = lon * math.pi / 4
            ang2 = lat * math.pi / 8
            x = 120 + rng * math.cos(ang2) * math.cos(ang1)
            y = 100 + rng * math.sin(ang2) * 0.85
            pts.append((x, y))
    for i, (x1, y1) in enumerate(pts):
        for j, (x2, y2) in enumerate(pts[i + 1 : i + 4], i + 1):
            if j < len(pts):
                lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{O}" stroke-width="1" opacity=".35"/>')
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="{O}" opacity=".75"/>' for x, y in pts[:28])
    return f"""<svg class="sphere" viewBox="0 0 240 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="120" cy="100" r="52" fill="rgba(201,86,47,.08)"/>
  {lines[:40]}
  {dots}
  <circle cx="120" cy="100" r="8" fill="{O}" opacity=".9"/>
</svg>"""


def term(title: str, lines: str, accent_last: bool = False) -> str:
    body = ""
    for i, ln in enumerate(lines.split("\n")):
        cls = "tl-acc" if accent_last and i == len(lines.split("\n")) - 1 else ""
        body += f'<div class="tl {cls}">{ln}</div>'
    return f"""<div class="term">
  <div class="term-bar"><span class="td r"></span><span class="td y"></span><span class="td g"></span><span class="term-t">{title}</span></div>
  <div class="term-body">{body}</div>
</div>"""


def sticky(text: str, tilt: str = "-3deg") -> str:
    return f'<div class="sticky" style="transform:rotate({tilt})"><div class="tape"></div><div class="sticky-t">{text}</div></div>'


def nav_bar(active: int, labels: list[str]) -> str:
    items = "".join(
        f'<span class="{"on" if i == active else ""}">{lbl}</span>' + ('<span class="dot">·</span>' if i < len(labels) - 1 else "")
        for i, lbl in enumerate(labels)
    )
    return f'<div class="nav-bar">{items}</div>'


def feat(icon: str, title: str, desc: str) -> str:
    return f"""<div class="feat"><div class="feat-ico">{_ico(icon)}</div>
    <div><div class="feat-t">{title}</div><div class="feat-d">{desc}</div></div></div>"""


def diagram_01() -> str:
    turbo = elem("turbo.png")
    feats = "".join(
        [
            feat(IC["bolt"], "MOTOR TURBO", "La ejecución 24/7"),
            feat(IC["brain"], "MEMORIA CENTRAL", "El contexto"),
            feat(IC["search"], "CANALES", "LinkedIn · email · CRM"),
            feat(IC["grid"], "PANEL ÚNICO", "La interfaz"),
        ]
    )
    return f"""
<div class="dia dia-01">
  <div class="dia-row">
    <div class="dia-col">{feats}</div>
    <div class="dia-col ctr">
      {sphere_svg()}
      <img class="turbo-sm" src="{turbo}" alt=""/>
      {term("NÚCLEO · TURBO", "PROSPECTOS 847\nRESPONDEN 23%\nHOT LEADS 12")}
    </div>
  </div>
  {term("SISTEMA · ACTIVO", "> brief\n> buscar\n> recordar\n> MEJORA 24/7_", True)}
  <div class="script-note">Al final del proceso, busca prospectos solo →</div>
</div>"""


def diagram_02() -> str:
    rows = "".join(
        [
            feat(IC["mic"], "RECIBÍ", "Tu brief de mercado ideal. Una sola capa sobre todo."),
            feat(IC["chip"], "EJECUTÁ", "El motor Turbo corre. La memoria conectada recuerda."),
            feat(IC["shield"], "LOCAL", "Tus datos bajo control. Sin filtraciones."),
            feat(IC["mod"], "MODULAR", "Podés cambiar cualquier pieza del sistema."),
        ]
    )
    return f"""
<div class="dia dia-02">
  {sticky("Un agente.<br/>Cada canal.<br/><b>Cero pestañas.</b>")}
  <div class="dia-list">{rows}</div>
  {nav_bar(0, ["RECIBE", "DIVIDE", "ASIGNA", "MEJORA"])}
</div>"""


def diagram_03() -> str:
    return f"""
<div class="dia dia-03">
  <div class="dia-row">
    <div class="dia-col">
      <div class="cmp"><div class="cmp-h bad">Método anterior</div><div class="cmp-b">Búsqueda manual · sin memoria · sin métricas</div></div>
      <div class="cmp"><div class="cmp-h good">Método Turbo</div><div class="cmp-b">Agente 24/7 · memoria · crítico automático</div></div>
      <div class="cmp"><div class="cmp-h">El flujo</div><div class="cmp-b">Brief → busca → puntúa → mejora solo</div></div>
    </div>
    <div class="dia-col">
      <div class="adv-box"><div class="adv-h">LA VENTAJA</div>
        <div class="chk">Sin cambio de contexto</div><div class="chk">Memoria de cada corrida</div>
        <div class="chk">Puntaje por prospecto</div><div class="chk">Mejora continua</div>
      </div>
      <div class="script-sm">Llega con prospectos. No con pestañas abiertas.</div>
    </div>
  </div>
  <div class="dash-mini">
    <div class="dash-l"><div class="ds">PROSPECTOS <b>847</b></div><div class="ds">HOT LEADS <b>12</b></div></div>
    <div class="dash-c">{sphere_svg()}</div>
    <div class="dash-r"><div class="ds">AJUSTE <b>92%</b></div><div class="ds">SCORE <b>91</b></div></div>
  </div>
</div>"""


def diagram_04() -> str:
    rows = [
        ("Motor Turbo", IC["bolt"], "Ejecuta búsqueda y contacto 24/7"),
        ("Memoria central", IC["brain"], "Guarda contexto de cada corrida"),
        ("Canales", IC["search"], "LinkedIn, email y CRM conectados"),
        ("Panel único", IC["grid"], "Métricas, bandeja y señales"),
    ]
    tr = ""
    for part, ico, desc in rows:
        tr += f"""<div class="trow"><div class="tpart"><span class="tico">{_ico(ico)}</span>{part}</div><div class="tdesc">{desc}</div></div>"""
    return f"""
<div class="dia dia-04">
  {sticky("Cuatro partes.<br/>Un agente.<br/>Eso es todo.", "2deg")}
  <div class="table-box"><div class="thead"><span>Parte</span><span>Qué hace</span></div>{tr}</div>
  <div class="script-sm left">Enfocate en conectar, no en complicarte.</div>
  <div class="pill-cta">HACÉLO AHORA. SE ACUMULA.</div>
</div>"""


def diagram_05() -> str:
    turbo = elem("turbo.png")
    skills = """prospectos/HABILIDAD.md
metricas/HABILIDAD.md
bandeja/HABILIDAD.md
icp/HABILIDAD.md
critico/HABILIDAD.md"""
    return f"""
<div class="dia dia-05">
  <div class="dia-row">
    <div class="dia-col">
      <div class="step-tag">PASO 1</div>
      <div class="blk"><div class="blk-h">Qué es</div><div class="blk-b">El motor Turbo + carpeta de habilidades pequeñas.</div></div>
      <div class="blk"><div class="blk-h">Tus primeras cinco</div><div class="blk-b">Prospectos · métricas · bandeja · ICP · crítico.</div></div>
      <div class="blk"><div class="blk-h">La regla</div><div class="blk-b">Habilidades chicas y de una función. Mejor que un prompt gigante.</div></div>
    </div>
    <div class="dia-col">
      {sticky("<i>Las habilidades son las<br/>células de Turbo.</i>", "-2deg")}
      <img class="turbo-md" src="{turbo}" alt=""/>
      {term("carpeta de habilidades", skills + "\n\nINTENCIÓN → HABILIDAD → RESPUESTA")}
    </div>
  </div>
  <div class="script-sm right">Las buenas habilidades nacen de flujos reales.</div>
</div>"""


def diagram_06() -> str:
    tree = """archivo/
  capturas/ — todo lo capturado
  conocimiento/ — contexto destilado
  salidas/ — todo lo entregado"""
    return f"""
<div class="dia dia-06">
  <div class="dia-row">
    <div class="dia-col">
      <div class="step-tag">PASO 2</div>
      <div class="folder-box">{_ico(IC['folder'])}<pre class="tree">{tree}</pre></div>
    </div>
    <div class="dia-col">
      {sticky("Si no está en el archivo,<br/>no pasó.", "2deg")}
      <div class="num-list">
        <div class="nitem"><span class="nb">1</span>Guardá cada corrida en <b>markdown</b>.</div>
        <div class="nitem"><span class="nb">2</span>Conectá el <b>grafo</b> de contexto.</div>
        <div class="nitem"><span class="nb">3</span>Recuperación <b>rápida</b> por prospecto.</div>
        <div class="nitem"><span class="nb">4</span>Todo vive en <b>archivos</b> locales.</div>
      </div>
    </div>
  </div>
  {term("archivo · VISTA DE GRAFO", "1,284 NOTAS    5,902 ENLACES\n\n[grafo de memoria activo]")}
</div>"""


def diagram_07() -> str:
    return f"""
<div class="dia dia-07">
  <div class="step-tag">PASO 3</div>
  {sticky("Tus canales nunca<br/>salen del sistema.", "-2deg")}
  <div class="wave-box">
    <div class="wave-bar">CANALES · CONECTADOS · LINKEDIN · LISTO · EMAIL · LISTO · ● ACTIVO</div>
    <svg class="wave" viewBox="0 0 400 80"><path d="M0 40 Q50 10 100 40 T200 40 T300 40 T400 40" fill="none" stroke="{O}" stroke-width="3"/><path d="M0 50 Q50 70 100 50 T200 50 T300 50 T400 50" fill="none" stroke="{O}" stroke-width="2" opacity=".5"/></svg>
    <div class="wave-foot">ASIGNÁ POR CANAL · NADA SE PIERDE EN EL FLUJO</div>
  </div>
  <div class="feat-grid">
    {feat(IC["search"], "LINKEDIN", "Prospectos en tu mercado")}
    {feat(IC["msg"], "EMAIL", "Secuencias y respuestas")}
    {feat(IC["db"], "CRM", "Historial y etapas")}
    {feat(IC["clock"], "24/7", "Corre sin pausas")}
  </div>
</div>"""


def diagram_08() -> str:
    turbo = elem("turbo.png")
    return f"""
<div class="dia dia-08">
  <div class="dia-row top">
    <div class="dia-col">
      <div class="step-tag">PASO 4</div>
      {sticky("Una sola pantalla.<br/>Todo lo que sabe Turbo.", "2deg")}
      <div class="prompt-box"><div class="prompt-h">USÁ ESTE PROMPT:</div>
        <div class="prompt-b">Creá un panel oscuro tipo terminal para mi agente Turbo: signos vitales · bandeja · canales · datos en vivo desde la memoria.</div>
        <div class="prompt-a">Una sola pantalla. Sin pestañas.</div>
      </div>
    </div>
    <div class="dia-col acts">
      <div class="act">{_ico(IC['play'])} Ejecutalo. Abrilo.</div>
      <div class="act">{_ico(IC['wave'])} Ajustalo por corrida.</div>
      <div class="act">{_ico(IC['clock'])} Tiempo: <b>una tarde.</b></div>
    </div>
  </div>
  <div class="dash-big">
    <div class="term-bar only"><span class="td r"></span><span class="td y"></span><span class="td g"></span><span class="term-t">TURBO · ACTIVO · EN MARCHA</span><span class="clk">16:22</span></div>
    <div class="dash-inner">
      <div class="dash-l"><div class="ds">PROSPECTOS <b>847</b></div><div class="ds">HOT <b>12</b></div><div class="ds">SCORE <b>91</b></div></div>
      <div class="dash-c"><img class="turbo-xs" src="{turbo}" alt=""/>{sphere_svg()}</div>
      <div class="dash-r"><div class="cmd">Métricas</div><div class="cmd">Bandeja</div><div class="cmd">ICP</div><div class="cmd">Crítico</div></div>
    </div>
  </div>
</div>"""


def diagram_09() -> str:
    schedule = [
        ("7:00", IC["clock"], "Resumen matutino.", "Bandeja, hot leads y métricas del día."),
        ("10:00", IC["search"], "Búsqueda activa.", "Turbo prospecta en LinkedIn y email."),
        ("14:00", IC["chart"], "Puntaje del mediodía.", "Revisá ajuste, urgencia y monto."),
        ("18:00", IC["check"], "Cierre del día.", "Crítico automático y log completo."),
        ("22:00", IC["bolt"], "Corrida nocturna.", "Sigue buscando mientras dormís."),
    ]
    rows = ""
    for hora, ico, tit, desc in schedule:
        rows += f"""<div class="srow"><div class="sico-c">{_ico(ico)}</div><div class="sh">{hora}</div>
        <div class="sb"><b>{tit}</b> {desc}</div></div>"""
    return f"""
<div class="dia dia-09">
  {sticky("Turbo no duerme.<br/>Vos sí.", "-2deg")}
  <div class="sched-box"><div class="sched-h"><span>Hora</span><span>Qué sucede</span></div>{rows}</div>
  <div class="script-sm left">La constancia se acumula. →</div>
  {nav_bar(3, ["RECIBE", "DIVIDE", "ASIGNA", "MEJORA"])}
</div>"""


def diagram_10() -> str:
    turbo = elem("turbo.png")
    steps = [
        ("Conectá el cerebro", "Motor Turbo + cinco habilidades chicas."),
        ("Construí la memoria", "Archivo, grafo y contexto por prospecto."),
        ("Conectá los canales", "LinkedIn, email y CRM en un flujo."),
        ("Armá el panel", "Una pantalla. Todo visible."),
    ]
    lis = "".join(f'<div class="cta-step"><span class="cn">{i}</span><div><b>{t}</b><br/>{d}</div></div>' for i, (t, d) in enumerate(steps, 1))
    return f"""
<div class="dia dia-10">
  <img class="turbo-md ctr-img" src="{turbo}" alt=""/>
  <div class="cta-box">{lis}</div>
  <div class="cta-kw-wrap"><div class="cta-lbl">COMENTÁ</div><div class="cta-kw">TURBO</div></div>
  <div class="script-sm ctr">y te armo el agente especializado para tu mercado.</div>
  <div class="save-hint">Guardalo para construirlo.</div>
</div>"""


DIAGRAM_CSS = """
.dia{{width:100%;}}
.dia svg{{display:block;max-width:100%;}}
.ico{{display:flex;align-items:center;justify-content:center;}}
.script-note,.script-sm{{font-family:'Lora',serif;font-style:italic;color:{O};font-size:18px;margin-top:8px;}}
.script-sm.left{{text-align:left;}}.script-sm.right{{text-align:right;}}.script-sm.ctr{{text-align:center;}}
.dia-row{{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:start;}}
.dia-col.ctr{{display:flex;flex-direction:column;align-items:center;gap:10px;}}
.feat{{display:flex;gap:14px;align-items:flex-start;padding:14px 0;border-bottom:1px solid {BD};}}
.feat:last-child{{border:none;}}
.feat-ico{{width:48px;height:48px;border:1.5px solid {O};border-radius:12px;display:flex;align-items:center;justify-content:center;background:rgba(201,86,47,.06);flex-shrink:0;}}
.feat-t{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.1em;color:{TX};text-transform:uppercase;}}
.feat-d{{font-size:17px;font-weight:500;color:{GY};margin-top:4px;line-height:1.25;}}
.sphere{{width:200px;height:auto;opacity:.9;}}
.turbo-sm{{width:72px;height:72px;object-fit:contain;margin:-20px 0 4px;}}
.turbo-md{{width:100px;height:100px;object-fit:contain;display:block;margin:8px auto;}}
.turbo-xs{{width:56px;height:56px;object-fit:contain;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:2;}}
.term{{background:{PN};border-radius:14px;overflow:hidden;color:#E8E4DC;margin-top:8px;width:100%;}}
.term-bar{{display:flex;align-items:center;gap:8px;padding:10px 14px;background:#1E1A16;border-bottom:1px solid #3A3530;}}
.term-bar.only{{border-radius:14px 14px 0 0;justify-content:space-between;}}
.td{{width:10px;height:10px;border-radius:50%;}}.td.r{{background:#E05A4F;}}.td.y{{background:#E6B84A;}}.td.g{{background:#6BCB77;}}
.term-t{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.08em;color:#A09890;margin-left:6px;}}
.term-body{{padding:14px 16px;font-family:'IBM Plex Mono',monospace;font-size:13px;line-height:1.55;}}
.tl{{color:#C8C0B8;}}.tl-acc{{color:{O};font-weight:600;}}
.sticky{{position:relative;background:{ST};padding:16px 18px;border-radius:4px;box-shadow:0 4px 14px rgba(28,24,20,.12);max-width:220px;margin-left:auto;margin-bottom:12px;}}
.tape{{position:absolute;top:-8px;left:50%;transform:translateX(-50%);width:52px;height:18px;background:rgba(255,255,255,.45);border:1px solid rgba(0,0,0,.08);}}
.sticky-t{{font-family:'Lora',serif;font-style:italic;font-size:17px;color:{TX};line-height:1.35;}}
.sticky-t b{{color:{O};font-weight:700;}}
.dia-list{{margin-top:8px;}}
.nav-bar{{display:flex;align-items:center;justify-content:center;gap:10px;padding:12px 16px;background:rgba(255,255,255,.35);border:1px solid {BD};border-radius:12px;margin-top:12px;font-family:'IBM Plex Mono',monospace;font-size:12px;letter-spacing:.1em;color:{GY};}}
.nav-bar .on{{color:{O};font-weight:600;}}
.nav-bar .dot{{opacity:.5;}}
.cmp{{padding:12px 0;border-bottom:1px solid {BD};}}
.cmp-h{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:12px;letter-spacing:.1em;color:{O};text-transform:uppercase;}}
.cmp-h.bad{{color:#A04030;}}.cmp-h.good{{color:{O};}}
.cmp-b{{font-size:16px;color:{TX};margin-top:4px;line-height:1.25;}}
.adv-box{{background:rgba(255,255,255,.45);border:1.5px solid {BD};border-radius:14px;padding:16px;}}
.adv-h{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:12px;letter-spacing:.12em;color:{O};margin-bottom:10px;}}
.chk{{padding:8px 0 8px 28px;position:relative;font-size:16px;color:{TX};border-bottom:1px solid rgba(184,168,152,.4);}}
.chk::before{{content:'✓';position:absolute;left:0;color:{O};font-weight:700;}}
.dash-mini,.dash-big{{background:{PN};border-radius:14px;padding:16px;color:#E8E4DC;margin-top:12px;}}
.dash-mini{{display:grid;grid-template-columns:1fr 1.2fr 1fr;gap:12px;align-items:center;}}
.dash-inner{{display:grid;grid-template-columns:1fr 1.4fr 1fr;gap:12px;padding:12px;align-items:center;}}
.ds{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.06em;color:#A09890;margin-bottom:8px;}}
.ds b{{display:block;font-size:22px;color:#fff;margin-top:2px;}}
.dash-c{{position:relative;display:flex;justify-content:center;}}
.table-box{{border:2px solid {O};border-radius:16px;overflow:hidden;background:rgba(255,255,255,.35);margin-top:8px;}}
.thead,.trow{{display:grid;grid-template-columns:200px 1fr;gap:12px;padding:14px 18px;border-bottom:1px solid {BD};align-items:center;}}
.thead{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.1em;color:{O};background:rgba(201,86,47,.08);}}
.tpart{{display:flex;align-items:center;gap:10px;font-weight:700;font-size:17px;color:{TX};}}
.tdesc{{font-size:16px;color:{GY};line-height:1.25;}}
.pill-cta{{display:inline-block;margin-top:12px;padding:12px 20px;border:2px solid {TX};border-radius:999px;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.12em;color:{TX};float:right;}}
.step-tag{{display:inline-block;background:{O};color:#fff;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:12px;letter-spacing:.12em;padding:6px 14px;border-radius:999px;margin-bottom:10px;}}
.blk{{padding:10px 0;border-bottom:1px solid {BD};}}
.blk-h{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:12px;color:{O};letter-spacing:.08em;text-transform:uppercase;}}
.blk-b{{font-size:16px;color:{TX};margin-top:4px;line-height:1.25;}}
.folder-box{{display:flex;gap:14px;align-items:flex-start;background:rgba(255,255,255,.4);border:1px solid {BD};border-radius:14px;padding:16px;}}
.tree{{font-family:'IBM Plex Mono',monospace;font-size:13px;line-height:1.5;color:{TX};white-space:pre-wrap;margin:0;}}
.num-list{{margin-top:12px;}}
.nitem{{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid {BD};font-size:16px;color:{TX};line-height:1.3;}}
.nb{{width:28px;height:28px;border-radius:50%;background:{O};color:#fff;display:flex;align-items:center;justify-content:center;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;flex-shrink:0;}}
.wave-box{{background:{PN};border-radius:14px;padding:16px;margin:12px 0;color:#C8C0B8;}}
.wave-bar{{font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:.06em;margin-bottom:10px;}}
.wave{{width:100%;height:60px;}}
.wave-foot{{font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:.08em;margin-top:8px;opacity:.8;}}
.feat-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px 16px;}}
.prompt-box{{border:2px solid {TX};border-radius:14px;padding:16px;background:rgba(255,255,255,.4);margin-top:8px;}}
.prompt-h{{font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:{GY};margin-bottom:8px;}}
.prompt-b{{font-size:16px;color:{TX};line-height:1.3;}}
.prompt-a{{margin-top:10px;padding:10px;background:{O};color:#fff;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:600;letter-spacing:.06em;border-radius:8px;}}
.act{{display:flex;align-items:center;gap:10px;font-family:'IBM Plex Mono',monospace;font-size:14px;color:{TX};padding:10px 0;}}
.dash-big{{margin-top:10px;padding:0;overflow:hidden;}}
.clk{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:#A09890;}}
.cmd{{font-family:'IBM Plex Mono',monospace;font-size:12px;color:#C8C0B8;padding:6px 0;border-bottom:1px solid #3A3530;}}
.sched-box{{border:2px solid {O};border-radius:16px;overflow:hidden;background:rgba(255,255,255,.35);width:100%;}}
.sched-h,.srow{{display:grid;grid-template-columns:56px 72px 1fr;gap:12px;padding:14px 18px;border-bottom:1px solid {BD};align-items:center;}}
.sched-h{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;letter-spacing:.1em;color:{O};background:rgba(201,86,47,.08);}}
.sico-c{{width:40px;height:40px;border:1.5px solid {O};border-radius:10px;display:flex;align-items:center;justify-content:center;background:rgba(201,86,47,.06);}}
.sh{{font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:13px;color:{TX};}}
.sb{{font-size:16px;color:{GY};line-height:1.25;}}
.dia-09 .sched-box{{max-width:960px;margin:0 auto;}}
.dia-10{{text-align:center;}}
.cta-box{{background:rgba(255,255,255,.45);border:1.5px solid {BD};border-radius:16px;padding:18px;text-align:left;margin:12px 0;}}
.cta-step{{display:flex;gap:14px;padding:12px 0;border-bottom:1px dashed {BD};font-size:16px;color:{TX};line-height:1.3;}}
.cn{{width:32px;height:32px;border-radius:50%;background:{O};color:#fff;display:flex;align-items:center;justify-content:center;font-family:'IBM Plex Mono',monospace;font-weight:600;flex-shrink:0;}}
.cta-kw-wrap{{margin:16px 0 8px;}}
.cta-lbl{{font-family:'IBM Plex Mono',monospace;font-size:13px;letter-spacing:.2em;color:{GY};margin-bottom:8px;}}
.cta-kw{{display:inline-block;background:{O};color:#fff;font-family:'Impact',sans-serif;font-size:56px;letter-spacing:.08em;padding:12px 36px;border-radius:16px;line-height:1;}}
.save-hint{{font-family:'IBM Plex Mono',monospace;font-size:13px;color:{GY};margin-top:8px;}}
.dia-01 .term{{max-width:420px;}}
.dia-01 .dia-row{{margin-bottom:12px;}}
.dia-02 .sticky{{float:right;margin-bottom:0;}}
.dia-04::after{{content:'';display:block;clear:both;}}
.dia-05 .dia-row{{align-items:center;}}
.dia-08 .dash-c .sphere{{width:140px;}}
.dia-08 .top{{margin-bottom:10px;}}
.ctr-img{{margin:0 auto 8px;}}
""".format(O=O, TX=TX, GY=GY, BD=BD, PN=PN, ST=ST)


def diagram(n: int) -> str:
    return {i: f for i, f in enumerate(
        [diagram_01, diagram_02, diagram_03, diagram_04, diagram_05,
         diagram_06, diagram_07, diagram_08, diagram_09, diagram_10], 1
    )}[n]()
