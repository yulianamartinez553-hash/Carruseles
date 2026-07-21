# -*- coding: utf-8 -*-
"""Clone: MCP Servers tutorial → STLabs · blanco · #00FFB2 · español."""
from __future__ import annotations

import base64
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from stlabs_kit import chrome, write_html, render, package  # noqa: E402

KEYWORD = "MCP"
TOTAL = 9
WORD_DIR = REPO / "Word"
VERDE = "#00FFB2"
INK = "#04130b"

CLAUDE_PNG = REPO / "assets" / "claude.png"
CLAUDE_URI = "data:image/png;base64," + base64.b64encode(CLAUDE_PNG.read_bytes()).decode()
SEB_URI = f"data:image/jpeg;base64,{base64.b64encode((REPO / 'seb.jpg').read_bytes()).decode()}"

# Minimal inline SVG icons (mono, colored via currentColor)
ICO = {
    "github": """<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.52 2.87 8.35 6.84 9.71.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.37-3.37-1.37-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.06 1.53 1.06.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.37-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.27 2.75 1.05A9.3 9.3 0 0 1 12 6.8c.85 0 1.71.12 2.51.35 1.9-1.32 2.74-1.05 2.74-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.81 0 .26.18.58.69.48A10.03 10.03 0 0 0 22 12.26C22 6.58 17.52 2 12 2z"/></svg>""",
    "slack": """<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 15a2 2 0 1 1-2-2h2v2zm1 0a2 2 0 1 1 4 0v5a2 2 0 1 1-4 0v-5zm2-7a2 2 0 1 1 2-2v2H9zm0 1a2 2 0 1 1 0 4H4a2 2 0 1 1 0-4h5zm7 2a2 2 0 1 1 2 2h-2v-2zm-1 0a2 2 0 1 1-4 0V6a2 2 0 1 1 4 0v5zm-2 7a2 2 0 1 1-2 2v-2h2zm0-1a2 2 0 1 1 0-4h5a2 2 0 1 1 0 4h-5z"/></svg>""",
    "folder": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h6l2 2h10v10H3V7z"/></svg>""",
    "db": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg>""",
    "brain": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.5 4a3.5 3.5 0 0 0-3.4 4.2A3.5 3.5 0 0 0 4 11.5 3.5 3.5 0 0 0 6.2 15a3.5 3.5 0 0 0 3.3 4h.5M14.5 4a3.5 3.5 0 0 1 3.4 4.2A3.5 3.5 0 0 1 20 11.5 3.5 3.5 0 0 1 17.8 15a3.5 3.5 0 0 1-3.3 4h-.5M9 8.5h6M9 12h6M10 15.5h4"/></svg>""",
    "usb": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="2" width="6" height="8" rx="1"/><path d="M12 10v8M8 14h8M7 18h10v3H7z"/></svg>""",
    "plug": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 2v6M16 2v6M6 8h12v4a6 6 0 0 1-12 0V8zM12 18v4"/></svg>""",
    "wrench": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a4 4 0 0 0-5.6 5.6L3 18v3h3l6.1-6.1a4 4 0 0 0 5.6-5.6l-2.5 2.5-2.5-2.5 2.5-2.5z"/></svg>""",
    "mail": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>""",
    "search": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>""",
    "aws": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15c2 2 5 3 8 3s6-1 8-3"/><path d="M7 9h10M9 5h6v10H9z"/></svg>""",
    "code": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m8 8-4 4 4 4M16 8l4 4-4 4"/></svg>""",
    "cloud": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 18h11a4 4 0 0 0 0-8 6 6 0 0 0-11.5-1.5A4 4 0 0 0 7 18z"/></svg>""",
}


def ico(name: str, size: int = 36) -> str:
    return f'<span class="ico" style="width:{size}px;height:{size}px">{ICO[name]}</span>'


EXTRA_CSS = f"""
:root{{--acento:{VERDE};--ink:{INK};}}
.sheet{{background:#e8e8e8;}}
.slide{{
  color:#0A0A0A;
  background:
    radial-gradient(40% 28% at 88% 6%, rgba(0,255,178,.10), transparent 60%),
    linear-gradient(180deg,#FFFFFF 0%, #F6F6F4 100%);
}}
.web{{display:none!important;}}
.foot{{
  position:absolute;left:0;right:0;bottom:56px;z-index:10;text-align:center;
  font-family:var(--mono);font-size:20px;letter-spacing:1px;color:var(--verde);
}}
.swipe{{
  position:absolute;right:56px;bottom:120px;z-index:10;
  font-family:var(--mono);font-size:18px;letter-spacing:2px;color:#6a736e;
}}
.meta{{
  position:absolute;left:56px;right:56px;top:48px;z-index:8;
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--mono);font-size:16px;letter-spacing:1px;color:#8a918c;
}}
.meta .brand{{color:var(--verde);}}
.tag{{
  display:inline-block;margin-top:18px;background:#0A0A0A;color:#fff;
  font-family:var(--mono);font-size:16px;letter-spacing:2px;padding:8px 14px;border-radius:6px;
}}
.h1{{
  margin-top:18px;font-family:var(--impact);font-weight:900;font-size:112px;line-height:1.02;
  letter-spacing:.5px;color:#0A0A0A;position:relative;z-index:3;
  -webkit-text-stroke:6px #0A0A0A;paint-order:stroke fill;
  text-shadow:0 0 0 #0A0A0A;
}}
.h1 .hl{{
  display:inline-block;color:var(--acento);-webkit-text-stroke:6px var(--acento);
  margin-top:8px;
}}
.h1 .script{{
  display:block;margin-top:10px;font-family:var(--serif);font-style:italic;font-weight:700;
  font-size:100px;color:var(--acento);-webkit-text-stroke:3px var(--acento);letter-spacing:0;line-height:1.02;
}}
.app-lab{{
  font-family:var(--pop);font-weight:800;font-size:40px;color:#0A0A0A;margin-top:16px;
}}
.app-card{{
  background:#fff;border:2px solid rgba(10,10,10,.12);border-radius:24px;
  box-shadow:0 16px 40px rgba(10,10,10,.10);position:relative;text-align:center;padding:40px 28px;
}}
.sub{{margin-top:16px;font-family:var(--cond);font-size:34px;color:#3a3f3c;line-height:1.35;position:relative;z-index:3;}}
.sub b,.body b{{color:#0A0A0A;}}
.body{{margin-top:14px;font-family:var(--cond);font-size:30px;color:#4a524e;line-height:1.35;max-width:920px;position:relative;z-index:3;}}
.note{{
  font-family:var(--serif);font-style:italic;font-weight:600;font-size:30px;color:var(--acento);
}}
.tape{{
  position:absolute;background:rgba(180,180,170,.45);border:1px solid rgba(120,120,110,.25);
  box-shadow:0 2px 6px rgba(0,0,0,.08);transform:rotate(-6deg);z-index:6;pointer-events:none;
}}
.win{{
  position:relative;background:#141414;border-radius:18px;color:#F2F2F2;
  box-shadow:0 22px 50px rgba(10,10,10,.18);overflow:hidden;text-align:left;
}}
.win-bar{{
  display:flex;align-items:center;gap:8px;padding:14px 16px;background:#1E1E1E;border-bottom:1px solid #2a2a2a;
  font-family:var(--mono);font-size:15px;color:#9aa39c;
}}
.dot{{width:12px;height:12px;border-radius:50%;display:inline-block;}}
.dot.r{{background:#FF5F57;}}.dot.y{{background:#FEBC2E;}}.dot.g{{background:#28C840;}}
.win pre,.code{{
  margin:0;padding:18px 20px 22px;font-family:var(--mono);font-size:22px;line-height:1.45;
  white-space:pre-wrap;word-break:break-word;
}}
.k{{color:#FF7AD9;}}.s{{color:var(--acento);}}.c{{color:#9CDCFE;}}
.ok{{color:#00FFB2;}}
.card{{
  background:#fff;border:1.5px solid rgba(10,10,10,.10);border-radius:16px;
  box-shadow:0 14px 36px rgba(10,10,10,.08);position:relative;
}}
.ico{{display:inline-flex;align-items:center;justify-content:center;color:var(--acento);}}
.ico svg{{width:100%;height:100%;display:block;}}
.ghost{{
  position:absolute;right:24px;top:520px;z-index:0;pointer-events:none;
  font-family:var(--impact);font-weight:900;font-size:340px;line-height:1;
  color:rgba(0,255,178,.08);letter-spacing:-8px;
}}
.hand{{
  font-family:var(--serif);font-style:italic;font-weight:700;font-size:24px;color:var(--acento);
}}
.arrow{{color:var(--acento);font-size:28px;font-weight:700;}}
.pad{{padding:110px 64px 0;position:relative;z-index:3;text-align:left;}}
.center{{text-align:center;}}
"""


def wrap(idx: int, inner: str, swipe: bool = True) -> str:
    html = chrome(idx, inner, total=TOTAL, bridges=None, footer=False)
    extras = '<div class="foot">sebastian.stlabs.ar</div>'
    if swipe and idx < TOTAL:
        extras = '<div class="swipe">deslizá →</div>' + extras
    return html.replace("</section>", extras + "</section>", 1)


def meta_bar(n: int) -> str:
    return f"""
<div class="meta">
  <span>JULIO 2026</span>
  <span class="brand">sebastian.stlabs.ar</span>
  <span>{n:02d}/{TOTAL:02d}</span>
</div>
"""


def slide1():
    return wrap(
        1,
        f"""
{meta_bar(1)}
<div class="pad center">
  <div class="tag">TUTORIAL</div>
  <h1 class="h1">MCP<span class="script">Servers</span></h1>
  <p class="sub">Qué son + Cómo configurarlos</p>
</div>
<div style="position:absolute;left:56px;right:56px;bottom:150px;z-index:4;display:flex;gap:24px;align-items:flex-start;">
  <div class="win" style="flex:1.25;">
    <div class="tape" style="width:90px;height:28px;top:-12px;left:40px;"></div>
    <div class="tape" style="width:90px;height:28px;top:-10px;right:50px;transform:rotate(8deg);"></div>
    <div class="win-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
      <span style="margin-left:10px;">claude_desktop_config.json</span></div>
    <pre><span class="k">"mcpServers"</span>: {{
  <span class="k">"github"</span>: {{ <span class="c">...</span> }},
  <span class="k">"slack"</span>: {{ <span class="c">...</span> }},
  <span class="k">"filesystem"</span>: {{ <span class="c">...</span> }}
}}</pre>
  </div>
  <div style="display:flex;flex-direction:column;gap:16px;width:320px;padding-top:0;">
    <div class="app-card">{ico("github", 108)}<div class="app-lab">GitHub</div>
      <div class="tape" style="width:100px;height:28px;top:-12px;left:50%;margin-left:-50px;"></div></div>
    <div class="app-card">{ico("slack", 108)}<div class="app-lab">Slack</div>
      <div class="tape" style="width:100px;height:28px;top:-12px;left:50%;margin-left:-50px;transform:rotate(5deg);"></div></div>
    <div class="app-card">{ico("folder", 108)}<div class="app-lab">Archivos</div>
      <div class="tape" style="width:100px;height:28px;top:-12px;left:50%;margin-left:-50px;transform:rotate(-4deg);"></div></div>
  </div>
</div>
<div style="position:absolute;left:90px;bottom:250px;z-index:5;display:flex;align-items:center;gap:12px;">
  <img src="{CLAUDE_URI}" alt="Claude" style="width:72px;height:68px;object-fit:contain;filter:drop-shadow(0 8px 14px rgba(0,0,0,.15));">
  <span class="hand">el archivo que conecta todo</span>
</div>
""",
    )


def slide2():
    return wrap(
        2,
        f"""
{meta_bar(2)}
<div class="pad">
  <div class="tag">LO BÁSICO</div>
  <h1 class="h1">¿Qué es <span class="hl">MCP?</span></h1>
  <p class="sub"><b>Model Context Protocol.</b></p>
  <p class="body">Un estándar abierto de Anthropic que deja que la IA se conecte a cualquier herramienta, base de datos o API externa.</p>
  <p class="body">Pensalo como el <span class="note">USB-C de la IA.</span><br>Un conector, y todo funciona.</p>
</div>
<div style="position:absolute;left:56px;right:56px;bottom:160px;z-index:4;display:flex;align-items:center;justify-content:center;gap:24px;">
  <div class="card" style="padding:40px 42px;min-width:240px;text-align:center;">
    {ico("brain", 96)}
    <div style="margin-top:16px;font-family:var(--pop);font-weight:800;font-size:44px;">IA</div>
  </div>
  <div style="font-size:48px;color:var(--acento);">┄┄</div>
  <div class="card" style="padding:40px 36px;border:3px solid var(--acento);text-align:center;">
    {ico("usb", 96)}
  </div>
  <div style="font-size:48px;color:var(--acento);">┄</div>
  <div style="display:flex;flex-direction:column;gap:18px;min-width:340px;">
    <div class="card" style="padding:26px 32px;display:flex;align-items:center;gap:18px;">{ico("github", 60)}<span style="font-family:var(--pop);font-weight:800;font-size:38px;color:#0A0A0A;">GitHub</span></div>
    <div class="card" style="padding:26px 32px;display:flex;align-items:center;gap:18px;">{ico("slack", 60)}<span style="font-family:var(--pop);font-weight:800;font-size:38px;color:#0A0A0A;">Slack</span></div>
    <div class="card" style="padding:26px 32px;display:flex;align-items:center;gap:18px;">{ico("db", 60)}<span style="font-family:var(--pop);font-weight:800;font-size:38px;color:#0A0A0A;">Base de datos</span></div>
  </div>
</div>
""",
    )


def slide3():
    return wrap(
        3,
        f"""
{meta_bar(3)}
<div class="pad center">
  <div class="tag">ARQUITECTURA</div>
  <h1 class="h1">Cómo funciona <span class="hl">MCP</span></h1>
</div>
<div style="position:absolute;left:100px;right:100px;top:320px;bottom:150px;z-index:4;display:flex;flex-direction:column;align-items:center;gap:12px;">
  <div class="card" style="width:620px;padding:32px 36px;display:flex;align-items:center;justify-content:space-between;">
    <div class="tape" style="width:90px;height:26px;top:-10px;left:30px;"></div>
    <div><div style="font-family:var(--pop);font-weight:800;font-size:44px;">HOST</div>
    <div style="font-family:var(--cond);font-size:30px;color:#6a736e;">Tu app de IA</div></div>
    {ico("brain", 80)}
  </div>
  <div class="hand" style="font-size:30px;">pide ↓</div>
  <div class="card" style="width:620px;padding:32px 36px;display:flex;align-items:center;justify-content:space-between;">
    <div class="tape" style="width:90px;height:26px;top:-10px;right:40px;transform:rotate(7deg);"></div>
    <div><div style="font-family:var(--pop);font-weight:800;font-size:44px;">CLIENT</div>
    <div style="font-family:var(--cond);font-size:30px;color:#6a736e;">El conector</div></div>
    {ico("plug", 80)}
  </div>
  <div style="align-self:flex-end;margin-right:40px;" class="hand" style="font-size:28px;">← un cliente por servidor</div>
  <div class="hand" style="font-size:30px;">llama ↓</div>
  <div class="card" style="width:620px;padding:32px 36px;display:flex;align-items:center;justify-content:space-between;">
    <div class="tape" style="width:90px;height:26px;top:-10px;left:50px;transform:rotate(-5deg);"></div>
    <div><div style="font-family:var(--pop);font-weight:800;font-size:44px;">SERVER</div>
    <div style="font-family:var(--cond);font-size:30px;color:#6a736e;">La herramienta</div></div>
    {ico("wrench", 80)}
  </div>
  <div style="display:flex;gap:20px;margin-top:12px;">
    <div class="card" style="padding:22px 30px;border-radius:999px;font-family:var(--pop);font-weight:800;font-size:34px;color:#0A0A0A;display:flex;align-items:center;gap:14px;">{ico("github", 48)} GitHub</div>
    <div class="card" style="padding:22px 30px;border-radius:999px;font-family:var(--pop);font-weight:800;font-size:34px;color:#0A0A0A;display:flex;align-items:center;gap:14px;">{ico("code", 48)} Slack</div>
    <div class="card" style="padding:22px 30px;border-radius:999px;font-family:var(--pop);font-weight:800;font-size:34px;color:#0A0A0A;display:flex;align-items:center;gap:14px;">{ico("cloud", 48)} Archivos</div>
  </div>
  <div class="hand" style="position:absolute;left:20px;top:120px;transform:rotate(-90deg);transform-origin:left center;">devuelve resultados ↑</div>
</div>
""",
    )


def slide4():
    return wrap(
        4,
        f"""
{meta_bar(4)}
<div class="pad">
  <div class="tag">POR QUÉ IMPORTA</div>
  <h1 class="h1" style="font-size:92px;line-height:1.08;">¿Por qué te tiene<br><span class="hl">que importar?</span></h1>
</div>
<div style="position:absolute;left:56px;right:56px;top:340px;display:grid;grid-template-columns:1fr 1fr;gap:24px;z-index:4;">
  <div class="card" style="padding:26px;">
    <div style="font-family:var(--mono);font-size:18px;color:#FF5247;margin-bottom:14px;">✗ ANTES DE MCP</div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:12px;">
      <div class="card" style="padding:18px 24px;display:flex;align-items:center;gap:12px;font-family:var(--pop);font-weight:800;font-size:32px;">{ico("brain", 52)} IA</div>
      <div style="font-size:28px;color:#666;line-height:1.15;text-align:center;">╳ ╳ ╳<br>cables enredados</div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
        <span class="card" style="padding:16px;">{ico("github", 44)}</span>
        <span class="card" style="padding:16px;">{ico("slack", 44)}</span>
        <span class="card" style="padding:16px;">{ico("db", 44)}</span>
        <span class="card" style="padding:16px;">{ico("folder", 44)}</span>
        <span class="card" style="padding:16px;">{ico("mail", 44)}</span>
      </div>
    </div>
  </div>
  <div class="card" style="padding:26px;border:2.5px solid var(--acento);">
    <div style="font-family:var(--mono);font-size:18px;color:var(--acento);margin-bottom:14px;">✓ CON MCP</div>
    <div style="display:flex;flex-direction:column;align-items:center;gap:12px;">
      <div class="card" style="padding:18px 24px;display:flex;align-items:center;gap:12px;font-family:var(--pop);font-weight:800;font-size:32px;">{ico("brain", 52)} IA</div>
      <div style="color:var(--acento);font-size:36px;">↓</div>
      <div style="background:var(--acento);color:var(--ink);padding:16px 26px;border-radius:14px;font-family:var(--pop);font-weight:800;font-size:32px;">Conector MCP</div>
      <div style="color:var(--acento);font-size:28px;">┊ ┊ ┊ ┊ ┊</div>
      <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
        <span class="card" style="padding:16px;border-color:var(--acento);">{ico("github", 44)}</span>
        <span class="card" style="padding:16px;border-color:var(--acento);">{ico("slack", 44)}</span>
        <span class="card" style="padding:16px;border-color:var(--acento);">{ico("db", 44)}</span>
        <span class="card" style="padding:16px;border-color:var(--acento);">{ico("mail", 44)}</span>
        <span class="card" style="padding:16px;border-color:var(--acento);">{ico("folder", 44)}</span>
      </div>
    </div>
  </div>
</div>
<div style="position:absolute;left:56px;right:56px;bottom:150px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;z-index:4;">
  <div class="card" style="padding:26px;text-align:center;">
    <div class="tape" style="width:70px;height:20px;top:-8px;left:50%;margin-left:-35px;"></div>
    <div style="font-family:var(--impact);font-size:72px;color:var(--acento);-webkit-text-stroke:3.5px var(--acento);">2,300+</div>
    <div style="font-family:var(--cond);font-size:28px;font-weight:600;">Servidores MCP</div>
  </div>
  <div class="card" style="padding:26px;text-align:center;">
    <div class="tape" style="width:70px;height:20px;top:-8px;left:50%;margin-left:-35px;transform:rotate(4deg);"></div>
    <div style="font-family:var(--impact);font-size:72px;color:var(--acento);-webkit-text-stroke:3.5px var(--acento);">3</div>
    <div style="font-family:var(--cond);font-size:28px;font-weight:600;">Grandes empresas de IA lo soportan</div>
  </div>
  <div class="card" style="padding:26px;text-align:center;">
    <div class="tape" style="width:70px;height:20px;top:-8px;left:50%;margin-left:-35px;transform:rotate(-5deg);"></div>
    <div style="font-family:var(--impact);font-size:72px;color:var(--acento);-webkit-text-stroke:3.5px var(--acento);">1</div>
    <div style="font-family:var(--cond);font-size:28px;font-weight:600;">Un protocolo para gobernarlos a todos</div>
  </div>
</div>
""",
    )


def slide5():
    return wrap(
        5,
        f"""
{meta_bar(5)}
<div class="ghost">1</div>
<div class="pad">
  <div class="tag">PASO 01</div>
  <h1 class="h1" style="font-size:100px;">Instalá un servidor</h1>
  <p class="sub">La mayoría se instala con un solo comando npm o pip.</p>
</div>
<div class="win" style="position:absolute;left:80px;right:80px;top:440px;z-index:4;">
  <div class="tape" style="width:100px;height:28px;top:-12px;left:60px;"></div>
  <div class="tape" style="width:100px;height:28px;top:-10px;right:70px;transform:rotate(9deg);"></div>
  <div class="win-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span style="margin-left:10px;">terminal</span></div>
  <pre>$ npm install -g @modelcontextprotocol/server-github

added 47 packages in 3s
<span class="ok">✓ Servidor instalado</span></pre>
</div>
<div style="position:absolute;right:100px;top:580px;z-index:5;" class="hand">← un solo comando</div>
<div style="position:absolute;left:0;right:0;bottom:170px;display:flex;justify-content:center;gap:24px;z-index:4;">
  <div class="card" style="padding:18px 28px;font-family:var(--mono);font-weight:700;color:#CB3837;border-color:#CB3837;">npm</div>
  <div class="card" style="padding:18px 28px;font-family:var(--mono);font-weight:700;color:#3775A9;border-color:#3775A9;">pip</div>
</div>
""",
    )


def slide6():
    return wrap(
        6,
        f"""
{meta_bar(6)}
<div class="ghost">2</div>
<div class="pad">
  <div class="tag">PASO 02</div>
  <h1 class="h1" style="font-size:100px;">Agregá tu config</h1>
  <p class="sub">Meté el servidor en tu archivo de config. Acá un ejemplo con Claude Desktop.</p>
</div>
<div class="win" style="position:absolute;left:70px;right:70px;top:430px;z-index:4;">
  <div class="tape" style="width:110px;height:30px;top:-12px;right:80px;transform:rotate(8deg);"></div>
  <div class="win-bar"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span style="margin-left:10px;">{{ }} claude_desktop_config.json</span></div>
  <pre>{{
  <span class="k">"mcpServers"</span>: {{
    <span class="k">"github"</span>: {{
      <span class="k">"command"</span>: <span class="s">"npx"</span>,
      <span class="k">"args"</span>: [<span class="s">"-y"</span>, <span class="s">"@modelcontextprotocol/server-github"</span>],
      <span class="k">"env"</span>: {{
        <span class="k">"GITHUB_TOKEN"</span>: <span class="s">"ghp_xxx"</span>
      }}
    }}
  }}
}}</pre>
</div>
<div style="position:absolute;right:90px;top:550px;z-index:5;" class="hand">← nombre del servidor</div>
<div style="position:absolute;right:90px;top:800px;z-index:5;" class="hand">← tu API key</div>
""",
    )


def slide7():
    return wrap(
        7,
        f"""
{meta_bar(7)}
<div class="ghost">3</div>
<div class="pad">
  <div class="tag">PASO 03</div>
  <h1 class="h1" style="font-size:100px;">Hablá con tu IA</h1>
  <p class="sub">Reiniciá la app. Tu IA ya ve las herramientas nuevas. Pedile que haga cosas.</p>
</div>
<div class="win" style="position:absolute;left:90px;right:90px;top:420px;bottom:210px;z-index:4;display:flex;flex-direction:column;">
  <div class="tape" style="width:120px;height:32px;top:-14px;right:60px;transform:rotate(10deg);"></div>
  <div class="win-bar" style="justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:10px;">
      <img src="{CLAUDE_URI}" alt="Claude" style="width:36px;height:34px;object-fit:contain;">
      <span style="color:#F2F2F2;font-family:var(--pop);font-weight:700;">Claude Desktop</span>
    </div>
    <span>─ □ ×</span>
  </div>
  <div style="flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:14px;">
    <div style="align-self:flex-end;background:#2a2a2a;border-radius:16px 16px 4px 16px;padding:14px 16px;max-width:78%;font-family:var(--cond);font-size:24px;">
      Creá un issue en mi repo por el bug del login
      <div style="font-family:var(--mono);font-size:13px;color:#8a918c;margin-top:6px;">10:42</div>
    </div>
    <div style="align-self:flex-start;display:flex;gap:10px;max-width:85%;">
      <img src="{CLAUDE_URI}" alt="" style="width:40px;height:38px;object-fit:contain;flex-shrink:0;">
      <div style="background:#1E1E1E;border-radius:16px 16px 16px 4px;padding:14px 16px;font-family:var(--cond);font-size:24px;">
        Listo. Creé el issue #247 “Fix login redirect bug” en your-repo con el detalle que me pasaste.
        <div style="font-family:var(--mono);font-size:13px;color:#8a918c;margin-top:6px;">10:42</div>
      </div>
    </div>
    <div style="align-self:flex-start;margin-left:50px;border:1.5px solid var(--acento);color:var(--acento);border-radius:999px;padding:8px 14px;font-family:var(--mono);font-size:16px;">
      ✓ Usó herramienta: github_create_issue
    </div>
  </div>
  <div style="padding:12px 16px;border-top:1px solid #2a2a2a;color:#8a918c;font-family:var(--cond);font-size:22px;">Escribile a Claude…</div>
</div>
<div style="position:absolute;right:70px;top:740px;z-index:5;" class="hand">MCP en acción →</div>
<div style="position:absolute;left:70px;right:70px;bottom:140px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;z-index:4;text-align:center;">
  <div class="hand" style="font-size:20px;">“Creá un issue en GitHub”</div>
  <div class="hand" style="font-size:20px;">“Traé mensajes de Slack”</div>
  <div class="hand" style="font-size:20px;">“Consultá mi base de datos”</div>
</div>
""",
    )


def slide8():
    servers = [
        ("github", "GitHub", "Repos, issues, PRs"),
        ("slack", "Slack", "Leer + enviar mensajes"),
        ("folder", "Filesystem", "Leer + escribir archivos locales"),
        ("db", "PostgreSQL", "Consultá tu base de datos"),
        ("aws", "AWS", "15.000+ APIs"),
        ("search", "Brave Search", "Búsqueda web desde la IA"),
    ]
    cards = ""
    for name, title, desc in servers:
        cards += f"""
        <div class="card" style="padding:38px 30px;display:flex;gap:24px;align-items:center;">
          <div class="tape" style="width:70px;height:22px;top:-10px;left:28px;"></div>
          <div class="tape" style="width:70px;height:22px;top:-10px;right:28px;transform:rotate(6deg);"></div>
          {ico(name, 84)}
          <div>
            <div style="font-family:var(--pop);font-weight:800;font-size:46px;color:#0A0A0A;">{title}</div>
            <div style="font-family:var(--cond);font-size:30px;color:#6a736e;">{desc}</div>
          </div>
        </div>"""
    return wrap(
        8,
        f"""
{meta_bar(8)}
<div class="pad">
  <div class="tag">DESTACADOS</div>
  <h1 class="h1" style="font-size:90px;line-height:1.05;">Servidores que<br><span class="hl">valen la pena</span></h1>
</div>
<div style="position:absolute;left:48px;right:48px;top:340px;display:grid;grid-template-columns:1fr 1fr;gap:22px;z-index:4;">
  {cards}
</div>
<p class="hand" style="position:absolute;left:0;right:0;bottom:140px;text-align:center;z-index:4;">+2.300 más en mcp.directory</p>
""",
    )


def slide9():
    return wrap(
        9,
        f"""
{meta_bar(9)}
<div class="pad center" style="padding-top:200px;">
  <div class="tape" style="width:140px;height:36px;top:160px;left:80px;"></div>
  <div class="tape" style="width:140px;height:36px;top:160px;right:80px;transform:rotate(8deg);"></div>
  <div class="tape" style="width:120px;height:32px;bottom:200px;right:100px;transform:rotate(-6deg);"></div>
  <h1 class="h1" style="font-size:120px;line-height:1.02;"><span class="hl">Guardá esto</span><br>para después</h1>
  <p class="sub">Seguime para más tutoriales de IA + Dev</p>
  <div style="margin:36px auto 0;display:inline-block;background:#0A0A0A;color:#fff;border-radius:999px;padding:16px 28px;font-family:var(--mono);font-size:24px;">
    sebastian.stlabs.ar
  </div>
  <div style="margin-top:28px;display:flex;justify-content:center;gap:40px;color:var(--acento);font-family:var(--mono);font-size:20px;letter-spacing:1px;">
    <span style="border:2px solid var(--acento);padding:10px 14px;border-radius:8px;">GUARDAR</span>
    <span style="border:2px solid var(--acento);padding:10px 14px;border-radius:8px;">COMPARTIR</span>
    <span style="border:2px solid var(--acento);padding:10px 14px;border-radius:8px;">ME GUSTA</span>
  </div>
  <div style="margin-top:36px;">
    <img src="{CLAUDE_URI}" alt="Claude" style="width:90px;height:84px;object-fit:contain;filter:drop-shadow(0 10px 18px rgba(0,0,0,.15));">
  </div>
  <div class="card" style="margin:22px auto 0;display:inline-flex;align-items:center;gap:16px;padding:14px 18px;text-align:left;">
    <img src="{SEB_URI}" alt="Sebastian" style="width:64px;height:64px;border-radius:50%;object-fit:cover;">
    <div>
      <div style="font-family:var(--pop);font-weight:800;font-size:22px;">Sebastian Garcia</div>
      <div style="font-family:var(--cond);font-size:18px;color:#6a736e;">sebastiangarcia.ar · 420 seguidores</div>
    </div>
  </div>
</div>
""",
        swipe=False,
    )




def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8(), slide9()]

    write_html(slides, BUILD / "carrusel.html", extra_css=EXTRA_CSS)
    print("HTML:", BUILD / "carrusel.html")
    pngs = render(BUILD)
    print(f"Render OK: {len(pngs)}")

    meta = {
        "titulo": "Tutorial Servidores MCP",
        "slides": TOTAL,
        "fondo": "papel_corrugado",
        "familia_visual": "manifiesto",
        "origen": "screenshot",
        "keyword_portada": KEYWORD,
        "modo_fondo": "blanco",
        "idioma": "es",
        "acento": VERDE,
        "feedback": {"estado": "borrador"},
    }
    out = package(BUILD, "STLabs-MCP-Servers", meta=meta)
    print("Package:", out)

    KEEP = {".ttf", ".otf", ".woff", ".woff2"}
    KEEP_NAMES = {"befonts-license.txt", "impact-font.zip"}
    WORD_DIR.mkdir(parents=True, exist_ok=True)
    for p in list(WORD_DIR.iterdir()):
        if p.is_file() and p.suffix.lower() not in KEEP and p.name.lower() not in KEEP_NAMES:
            p.unlink()
    for fname in ("impact.ttf", "impacted.ttf", "unicodeimpact.ttf", "Befonts-License.txt"):
        src = REPO / "fonts" / fname
        if src.exists():
            shutil.copy2(src, WORD_DIR / fname)

    for name in (
        "STLabs-MCP-Servers.html",
        "STLabs-MCP-Servers.zip",
        "_preview-tira.png",
        "manifest.json",
        *[f"slide-{i:02d}.png" for i in range(1, TOTAL + 1)],
    ):
        src = out / name
        if src.exists():
            shutil.copy2(src, WORD_DIR / name)

    shutil.copy2(CLAUDE_PNG, WORD_DIR / "claude.png")

    (WORD_DIR / "MANIFIESTO-FUENTES.md").write_text(
        """# Font manifesto — MCP Servers Tutorial

| Font | Weight | Role | Source |
|---|---|---|---|
| Impact | 900 | Titles | `fonts/impact.ttf` |
| Lora Italic | 600–700 | Accent script / notes | `fonts/Lora-Italic-Variable.ttf` |
| Barlow Condensed | 400–700 | Body | `fonts/BarlowCondensed-*.ttf` |
| IBM Plex Mono | 400–600 | Code / meta / footer | `fonts/IBMPlexMono-*.ttf` |
| Poppins | 800 | Card titles | `fonts/Poppins-Bold.ttf` |

Accent: `#00FFB2` (replaces orange). Idioma: español.
Claude: `assets/claude.png` (default orange mascot).
Identity: sebastian.stlabs.ar · white scrapbook clone.
""",
        encoding="utf-8",
    )
    (WORD_DIR / "LEEME.txt").write_text(
        f"""STLabs Carousel — MCP Servers Tutorial
Clone of @fullstackparody MCP tutorial → sebastian.stlabs.ar
Background: WHITE · Texture: papel_corrugado · Family: manifiesto
Slides: {TOTAL} · Keyword: {KEYWORD} · Idioma: español
Accent: #00FFB2 · Claude: assets/claude.png
""",
        encoding="utf-8",
    )
    print("Word/:", WORD_DIR)


if __name__ == "__main__":
    main()
