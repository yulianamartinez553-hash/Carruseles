#!/usr/bin/env python3
"""Carrusel 11 slides — clones de referencias motivacionales → STLabs.
Fondo blanco. Verde marca 2 tonos más oscuro (#00A372) para contraste.
"""
from __future__ import annotations

import base64
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from stlabs_kit import package, render  # noqa: E402

BUILD = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"

# Marca #00FFB2 → ~dos tonos más oscuros para contraste sobre blanco
VERDE = "#007A56"
VERDE_DEEP = "#005C40"
INK = "#0A0A0A"
PAPER = "#FFFFFF"
HANDLE = "sebastian.stlabs.ar"


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_faces() -> str:
    faces = [
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-Bold.ttf", 700, "normal"),
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-BoldItalic.ttf", 700, "italic"),
        ("Playfair Display", FONTS / "playfair/PlayfairDisplay-Italic.ttf", 400, "italic"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Regular.ttf", 400, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Medium.ttf", 500, "normal"),
        ("IBM Plex Sans", FONTS / "ibm-plex-sans/IBMPlexSans-Light.ttf", 300, "normal"),
        ("IBM Plex Mono", FONTS / "IBMPlexMono-Regular.ttf", 400, "normal"),
        ("Poppins", FONTS / "Poppins-Bold.ttf", 700, "normal"),
        ("Lora", FONTS / "Lora-Italic-Variable.ttf", "400 700", "italic"),
    ]
    out = []
    for fam, path, w, style in faces:
        if not path.exists():
            continue
        d = b64(path)
        out.append(
            f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};"
            f"font-display:block;src:url(data:font/ttf;base64,{d}) format('truetype');}}"
        )
    return "".join(out)


CSS = f"""
:root{{
  --verde:{VERDE}; --verde-deep:{VERDE_DEEP}; --ink:{INK}; --paper:{PAPER};
  --serif:'Playfair Display',Georgia,serif;
  --sans:'IBM Plex Sans',Helvetica,sans-serif;
  --mono:'IBM Plex Mono',monospace;
  --pop:'Poppins',sans-serif;
  --lora:'Lora',Georgia,serif;
}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{background:#111;}}
.sheet{{display:flex;flex-direction:column;gap:40px;padding:40px;background:#111;}}
.slide{{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  background:var(--paper);color:var(--verde);
}}
.web{{
  position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:10;
  font-family:var(--mono);font-size:22px;letter-spacing:1.5px;color:var(--verde);
}}
.pill{{
  display:inline-block;border:1.5px solid var(--verde);border-radius:999px;
  padding:10px 28px;font-family:var(--mono);font-size:22px;color:var(--verde);
  letter-spacing:1px;
}}
"""


def foot() -> str:
    return f'<div class="web">{HANDLE}</div>'


def slide(inner: str) -> str:
    return f'<section class="slide">{inner}{foot()}</section>'


# ─── Slide builders ───────────────────────────────────────────────────────────

def s01() -> str:
    """Motivación vs Disciplina — charts."""
    wave = "M40,110 C70,40 100,180 130,110 C160,40 190,180 220,110 C250,40 280,160 310,90"
    stairs = "M40,200 L80,200 L80,160 L120,160 L120,120 L160,120 L160,90 L200,90 L200,60 L240,60 L240,35 L280,35 L280,20 L320,20"
    return slide(f"""
<style>
.s1{{padding:90px 70px 140px;display:flex;flex-direction:column;align-items:center;height:100%;}}
.s1 .top{{margin-bottom:36px;}}
.s1 h1{{font-family:var(--pop);font-weight:700;font-size:64px;color:var(--verde);text-align:center;margin:28px 0 70px;letter-spacing:-1px;}}
.s1 .row{{display:flex;gap:48px;width:100%;justify-content:center;}}
.s1 .col{{flex:1;max-width:420px;text-align:center;}}
.s1 svg{{width:100%;height:260px;}}
.s1 .lab{{font-family:var(--pop);font-weight:700;font-size:36px;color:var(--verde);margin-top:28px;}}
.s1 .sub{{font-family:var(--sans);font-size:26px;color:var(--verde-deep);margin-top:10px;font-style:italic;}}
</style>
<div class="s1">
  <div class="top"><span class="pill">{HANDLE}</span></div>
  <h1>Motivación vs. disciplina</h1>
  <div class="row">
    <div class="col">
      <svg viewBox="0 0 360 240" fill="none">
        <path d="M30 20 V220 H340" stroke="{VERDE}" stroke-width="3"/>
        <path d="{wave}" stroke="{VERDE}" stroke-width="10" stroke-linecap="round" fill="none"/>
      </svg>
      <div class="lab">Motivación</div>
      <div class="sub">“Hoy quiero, mañana no quiero”</div>
    </div>
    <div class="col">
      <svg viewBox="0 0 360 240" fill="none">
        <path d="M30 20 V220 H340" stroke="{VERDE}" stroke-width="3"/>
        <path d="{stairs}" stroke="{VERDE}" stroke-width="10" stroke-linecap="square" fill="none"/>
      </svg>
      <div class="lab">Disciplina</div>
      <div class="sub">“Lo hago porque lo decidí”</div>
    </div>
  </div>
</div>
""")


def s02() -> str:
    """No es Suerte — path with 6 nodes."""
    nodes = [
        (120, 280, "Son tus", "Decisiones", "right"),
        (860, 280, "Tus", "hábitos", "left"),
        (860, 560, "Tus", "rutinas", "left"),
        (120, 560, "Tus", "ganas", "right"),
        (120, 840, "tu", "capacidad", "right"),
        (860, 840, "tu", "determinación", "left"),
    ]
    # snake path: L→R, down-right curve, R→L, down-left curve, L→R
    path = "M120,280 H860 Q920,280 920,340 V500 Q920,560 860,560 H120 Q60,560 60,620 V780 Q60,840 120,840 H860"
    labels = ""
    for x, y, a, b, side in nodes:
        if side == "right":
            labels += f'<div class="nd" style="left:{x+36}px;top:{y-28}px;text-align:left"><span>{a}</span> <b>{b}</b></div>'
        else:
            labels += f'<div class="nd" style="right:{1080-x+36}px;top:{y-28}px;text-align:right"><span>{a}</span> <b>{b}</b></div>'
        labels += f'<div class="dot" style="left:{x-14}px;top:{y-14}px"></div>'
    return slide(f"""
<style>
.s2{{position:relative;height:100%;padding-top:100px;}}
.s2 h1{{font-family:var(--pop);font-weight:700;font-size:72px;font-style:italic;text-align:center;color:var(--verde);}}
.s2 svg.path{{position:absolute;left:0;top:0;width:1080px;height:1350px;}}
.s2 .dot{{position:absolute;width:28px;height:28px;border-radius:50%;background:var(--verde);z-index:3;}}
.s2 .nd{{position:absolute;z-index:3;font-family:var(--sans);font-size:28px;color:var(--verde);line-height:1.2;width:320px;}}
.s2 .nd b{{font-weight:700;}}
.s2 .nd span{{font-weight:400;}}
</style>
<div class="s2">
  <h1>No es Suerte</h1>
  <svg class="path" viewBox="0 0 1080 1350" fill="none">
    <path d="{path}" stroke="{VERDE}" stroke-width="5" fill="none" stroke-linecap="round"/>
  </svg>
  {labels}
</div>
""")


def s03() -> str:
    """LOGROS — Venn hábitos / perseverancia."""
    return slide(f"""
<style>
.s3{{height:100%;display:flex;flex-direction:column;align-items:center;padding-top:120px;}}
.s3 h1{{font-family:var(--serif);font-weight:700;font-size:92px;letter-spacing:6px;color:var(--verde);margin-bottom:40px;}}
.s3 .venn{{position:relative;width:780px;height:520px;margin-top:20px;}}
.s3 .c{{position:absolute;width:420px;height:420px;border:4px solid var(--verde);border-radius:50%;top:40px;}}
.s3 .c.l{{left:40px;}}
.s3 .c.r{{right:40px;}}
.s3 .overlap{{
  position:absolute;left:50%;top:120px;transform:translateX(-50%);
  width:200px;height:280px;background:rgba(0,163,114,.35);
  border-radius:50%;clip-path:ellipse(45% 50% at 50% 50%);
  /* simpler: use SVG below */
  display:none;
}}
.s3 .lab{{position:absolute;top:220px;font-family:var(--sans);font-size:34px;font-weight:500;letter-spacing:2px;color:var(--verde);}}
.s3 .lab.l{{left:90px;}}
.s3 .lab.r{{right:40px;text-align:right;width:220px;}}
.s3 .arrow{{position:absolute;left:50%;top:20px;transform:translateX(-50%);}}
</style>
<div class="s3">
  <h1>LOGROS</h1>
  <div class="venn">
    <svg width="780" height="520" viewBox="0 0 780 520">
      <defs>
        <clipPath id="leftC"><circle cx="260" cy="280" r="200"/></clipPath>
      </defs>
      <circle cx="260" cy="280" r="200" fill="none" stroke="{VERDE}" stroke-width="4"/>
      <circle cx="520" cy="280" r="200" fill="none" stroke="{VERDE}" stroke-width="4"/>
      <circle cx="520" cy="280" r="200" fill="{VERDE}" fill-opacity="0.38" clip-path="url(#leftC)"/>
      <line x1="390" y1="160" x2="390" y2="70" stroke="{VERDE}" stroke-width="3"/>
      <polygon points="390,55 378,78 402,78" fill="{VERDE}"/>
      <text x="160" y="290" text-anchor="middle" fill="{VERDE}" font-family="IBM Plex Sans" font-size="32" font-weight="500" letter-spacing="2">HÁBITOS</text>
      <text x="600" y="275" text-anchor="middle" fill="{VERDE}" font-family="IBM Plex Sans" font-size="28" font-weight="500" letter-spacing="1">PERSEVERANCIA</text>
    </svg>
  </div>
</div>
""")


def s04() -> str:
    """Esto es trabajo / suerte."""
    bars = "".join(
        f'<div class="bar" style="height:{20+i*12}px"></div>' for i in range(16)
    )
    return slide(f"""
<style>
.s4{{height:100%;display:flex;align-items:flex-end;justify-content:center;gap:80px;padding:180px 60px 200px;}}
.s4 .col{{display:flex;flex-direction:column;align-items:center;width:420px;}}
.s4 .bars{{display:flex;align-items:flex-end;gap:8px;height:420px;}}
.s4 .bar{{width:18px;background:var(--verde);border-radius:2px;}}
.s4 .luck{{position:relative;height:420px;width:280px;display:flex;align-items:flex-end;justify-content:center;}}
.s4 .luck .line{{width:10px;height:380px;background:var(--verde);border-radius:2px;}}
.s4 .luck .dots{{position:absolute;bottom:0;left:20px;right:20px;display:flex;gap:14px;justify-content:center;}}
.s4 .luck .dots i{{width:6px;height:6px;background:rgba(0,163,114,.35);border-radius:50%;display:block;}}
.s4 .lab{{margin-top:40px;text-align:center;font-family:var(--sans);color:var(--verde);}}
.s4 .lab .sm{{font-size:22px;font-weight:400;letter-spacing:2px;}}
.s4 .lab .big{{font-size:42px;font-weight:700;letter-spacing:2px;margin-top:6px;font-family:var(--pop);}}
</style>
<div class="s4">
  <div class="col">
    <div class="bars">{bars}</div>
    <div class="lab"><div class="sm">ESTO ES</div><div class="big">TRABAJO</div></div>
  </div>
  <div class="col">
    <div class="luck">
      <div class="line"></div>
      <div class="dots">{''.join('<i></i>' for _ in range(10))}</div>
    </div>
    <div class="lab"><div class="sm">ESTO ES</div><div class="big">SUERTE</div></div>
  </div>
</div>
""")


def s05() -> str:
    """Procrastinando / Sobrepensando / Haciendo."""
    return slide(f"""
<style>
.s5{{padding:110px 90px 160px;display:flex;flex-direction:column;gap:70px;}}
.s5 .block{{text-align:center;}}
.s5 h2{{font-family:var(--pop);font-weight:700;font-size:48px;color:var(--verde);margin-bottom:28px;}}
.s5 svg{{width:100%;height:90px;}}
</style>
<div class="s5">
  <div class="block">
    <h2>Procrastinando</h2>
    <svg viewBox="0 0 900 90" fill="none">
      <path d="M40 50 H300 V15 H420 V50 H820" stroke="{VERDE}" stroke-width="4" stroke-linecap="round"/>
      <polygon points="820,50 800,40 800,60" fill="{VERDE}"/>
      <circle cx="360" cy="32" r="22" fill="{VERDE}"/>
      <path d="M350 32 L358 40 L372 24" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
      <!-- X instead of check for bad -->
    </svg>
    <svg viewBox="0 0 900 90" fill="none" style="margin-top:-90px">
      <circle cx="360" cy="32" r="22" fill="{VERDE}"/>
      <path d="M352 24 L368 40 M368 24 L352 40" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="block">
    <h2>Sobrepensando</h2>
    <svg viewBox="0 0 900 120" fill="none">
      <path d="M40 60 H280" stroke="{VERDE}" stroke-width="4"/>
      <path d="M280 60 A40 40 0 1 1 279 59" stroke="{VERDE}" stroke-width="4" fill="none"/>
      <path d="M300 60 A20 20 0 1 1 299 59" stroke="{VERDE}" stroke-width="4" fill="none"/>
      <circle cx="300" cy="60" r="18" fill="{VERDE}"/>
      <path d="M292 52 L308 68 M308 52 L292 68" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="block">
    <h2>Haciendo</h2>
    <svg viewBox="0 0 900 90" fill="none">
      <path d="M40 50 H780" stroke="{VERDE}" stroke-width="4" stroke-linecap="round"/>
      <polygon points="780,50 760,40 760,60" fill="{VERDE}"/>
      <circle cx="820" cy="50" r="26" fill="{VERDE}"/>
      <path d="M808 50 L818 60 L836 40" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
""")


def s06() -> str:
    """La vida es un juego — chess pieces as simple SVG silhouettes."""
    # simplified chess: rook, queen, king, queen, rook
    pieces = [
        ("rook", VERDE_DEEP, 0.85),
        ("queen", VERDE, 1.0),
        ("king", "#E8F5F0", 1.15),
        ("queen", VERDE, 1.0),
        ("rook", VERDE_DEEP, 0.85),
    ]

    def piece_svg(kind: str, fill: str, scale: float) -> str:
        h = int(220 * scale)
        w = int(90 * scale)
        if kind == "rook":
            body = f'<rect x="28" y="70" width="34" height="110" rx="4" fill="{fill}"/><path d="M20 70 H70 V50 H60 V60 H50 V50 H40 V60 H30 V50 H20 Z" fill="{fill}"/><rect x="22" y="180" width="46" height="16" rx="3" fill="{fill}"/>'
        elif kind == "queen":
            body = f'<path d="M25 80 L30 50 L40 70 L45 40 L55 70 L65 50 L70 80 Z" fill="{fill}"/><rect x="30" y="80" width="35" height="100" rx="8" fill="{fill}"/><rect x="22" y="180" width="51" height="16" rx="3" fill="{fill}"/><circle cx="45" cy="32" r="8" fill="{fill}"/>'
        else:  # king
            body = f'<rect x="42" y="20" width="10" height="28" fill="{fill}"/><rect x="34" y="28" width="26" height="10" fill="{fill}"/><path d="M28 70 Q45 45 62 70" fill="{fill}"/><rect x="30" y="70" width="34" height="110" rx="8" fill="{fill}"/><rect x="20" y="180" width="54" height="16" rx="3" fill="{fill}"/>'
        return f'<svg width="{w}" height="{h}" viewBox="0 0 90 210">{body}</svg>'

    row = "".join(f'<div class="pc">{piece_svg(k,f,s)}</div>' for k, f, s in pieces)
    return slide(f"""
<style>
.s6{{height:100%;display:flex;flex-direction:column;align-items:center;padding:110px 60px 160px;}}
.s6 h1{{font-family:var(--serif);font-weight:700;font-size:64px;color:var(--verde);text-align:center;}}
.s6 .row{{display:flex;align-items:flex-end;justify-content:center;gap:28px;margin:80px 0 60px;min-height:280px;}}
.s6 .pc{{filter:drop-shadow(0 12px 18px rgba(0,0,0,.12));}}
.s6 .quote{{font-family:var(--serif);font-size:30px;line-height:1.45;text-align:center;color:var(--verde);max-width:820px;}}
.s6 .quote i{{font-style:italic;}}
.s6 .rule{{width:80px;height:2px;background:var(--verde);margin:36px auto 0;opacity:.6;}}
</style>
<div class="s6">
  <h1>La vida es un juego</h1>
  <div class="row">{row}</div>
  <div class="quote">No podemos deshacer un movimiento,<br>pero podemos hacer que <i>el siguiente</i> sea mejor.</div>
  <div class="rule"></div>
</div>
""")


def s07() -> str:
    """A veces se necesitan diez años…"""
    pts = [(1, 40), (2, 42), (3, 41), (4, 43), (5, 42), (6, 44), (7, 45), (8, 48), (9, 70), (10, 200)]
    # map to svg coords
    coords = []
    for x, y in pts:
        sx = 80 + (x - 1) * 85
        sy = 280 - y
        coords.append((sx, sy, x))
    poly = " ".join(f"{x},{y}" for x, y, _ in coords)
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="{VERDE}"/>' for x, y, _ in coords)
    labels = "".join(f'<text x="{x}" y="310" text-anchor="middle" fill="{VERDE}" font-size="22" font-family="IBM Plex Sans">{n}</text>' for x, y, n in coords)
    return slide(f"""
<style>
.s7{{height:100%;padding:120px 70px 160px;display:flex;flex-direction:column;align-items:center;}}
.s7 svg{{width:100%;height:360px;margin-bottom:50px;}}
.s7 .quote{{font-family:var(--serif);font-size:40px;line-height:1.4;text-align:center;color:var(--verde);max-width:860px;}}
.s7 .quote i{{font-style:italic;}}
.s7 .rule{{width:80px;height:2px;background:var(--verde);margin:40px auto 0;opacity:.6;}}
</style>
<div class="s7">
  <svg viewBox="0 0 940 340" fill="none">
    <line x1="60" y1="20" x2="60" y2="290" stroke="{VERDE}" stroke-width="2"/>
    <line x1="60" y1="290" x2="920" y2="290" stroke="{VERDE}" stroke-width="2"/>
    <polyline points="{poly}" stroke="{VERDE}" stroke-width="3.5" fill="none"/>
    {dots}
    {labels}
  </svg>
  <div class="quote">A veces se necesitan diez años<br>para obtener ese año que <i>cambia tu vida.</i></div>
  <div class="rule"></div>
</div>
""")


def s08() -> str:
    """Disciplina: perfección vs continuidad."""
    return slide(f"""
<style>
.s8{{height:100%;display:flex;align-items:center;justify-content:center;gap:50px;padding:80px 50px 140px;}}
.s8 .card{{width:420px;height:520px;position:relative;display:flex;align-items:center;justify-content:center;}}
.s8 .txt{{text-align:center;font-family:var(--serif);font-size:34px;line-height:1.35;color:var(--verde);z-index:2;padding:40px;}}
.s8 .txt i{{font-style:italic;}}
.s8 svg.ring{{position:absolute;inset:0;width:100%;height:100%;}}
</style>
<div class="s8">
  <div class="card">
    <svg class="ring" viewBox="0 0 420 520" fill="none">
      <path d="M80 260 A140 140 0 1 1 80.1 261" stroke="{VERDE}" stroke-width="3" stroke-linecap="round"
        stroke-dasharray="4 0" opacity=".9"/>
      <circle cx="80" cy="260" r="8" fill="{VERDE}"/>
      <!-- open arc bottom-left fade -->
      <path d="M90 380 A140 140 0 0 0 200 400" stroke="{VERDE}" stroke-width="3" opacity=".35"/>
    </svg>
    <div class="txt">La disciplina<br>no se trata de la<br><i>perfección.</i></div>
  </div>
  <div class="card">
    <svg class="ring" viewBox="0 0 420 520" fill="none">
      <circle cx="210" cy="260" r="150" stroke="{VERDE}" stroke-width="2.5" stroke-dasharray="14 10"/>
      <!-- arrows on dash -->
      <polygon points="210,100 202,118 218,118" fill="{VERDE}"/>
      <polygon points="350,300 330,292 336,312" fill="{VERDE}"/>
      <polygon points="90,320 108,308 98,330" fill="{VERDE}"/>
    </svg>
    <div class="txt">La disciplina<br>se trata de la<br><i>continuidad.</i></div>
  </div>
</div>
""")


def s09() -> str:
    """Nadie puede estar 100% cada día."""
    heights = [22, 42, 78, 18, 95, 52, 24]
    bars = "".join(
        f'<div class="day"><div class="fill" style="height:{h}%"></div></div>' for h in heights
    )
    return slide(f"""
<style>
.s9{{height:100%;padding:120px 80px 160px;display:flex;flex-direction:column;}}
.s9 h1{{font-family:var(--serif);font-size:44px;color:var(--verde);text-align:center;margin-bottom:80px;}}
.s9 .week{{display:flex;gap:22px;justify-content:center;align-items:flex-end;height:520px;}}
.s9 .day{{width:72px;height:100%;border:2.5px solid var(--verde);border-radius:8px;display:flex;align-items:flex-end;overflow:hidden;}}
.s9 .fill{{width:100%;background:var(--verde);opacity:.55;}}
.s9 .note{{margin-top:40px;text-align:right;padding-right:40px;font-family:var(--serif);font-size:36px;color:var(--verde);}}
.s9 .rule{{width:80px;height:2px;background:var(--verde);margin:50px auto 0;opacity:.6;}}
</style>
<div class="s9">
  <h1>Nadie puede estar 100% cada día</h1>
  <div class="week">{bars}</div>
  <div class="note">y está bien...</div>
  <div class="rule"></div>
</div>
""")


def s10() -> str:
    """Ley de Pareto."""
    return slide(f"""
<style>
.s10{{height:100%;padding:110px 70px 160px;display:flex;flex-direction:column;align-items:center;}}
.s10 h1{{font-family:var(--serif);font-size:64px;color:var(--verde);margin-bottom:50px;}}
.s10 .pies{{display:flex;gap:70px;margin-bottom:50px;}}
.s10 .pie{{text-align:center;}}
.s10 .pie svg{{width:300px;height:300px;}}
.s10 .pie .lab{{font-family:var(--sans);font-size:28px;color:var(--verde);margin-top:18px;font-weight:500;}}
.s10 .body{{font-family:var(--serif);font-size:32px;line-height:1.45;text-align:center;color:var(--verde);max-width:820px;}}
.s10 .rule{{width:80px;height:2px;background:var(--verde);margin:40px auto 0;opacity:.6;}}
</style>
<div class="s10">
  <h1>Ley de Pareto</h1>
  <div class="pies">
    <div class="pie">
      <svg viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="54" fill="#E8F5F0"/>
        <!-- 20% wedge from top -->
        <path d="M60 60 L60 6 A54 54 0 0 1 92 18 Z" fill="{VERDE}"/>
        <text x="78" y="30" fill="#fff" font-size="12" font-family="IBM Plex Sans" font-weight="700">20%</text>
      </svg>
      <div class="lab">Esfuerzo</div>
    </div>
    <div class="pie">
      <svg viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="54" fill="#E8F5F0"/>
        <path d="M60 60 L60 6 A54 54 0 1 1 28 102 Z" fill="{VERDE}"/>
        <text x="48" y="70" fill="#fff" font-size="14" font-family="IBM Plex Sans" font-weight="700">80%</text>
      </svg>
      <div class="lab">Resultados</div>
    </div>
  </div>
  <div class="body">El 80% de los resultados proviene<br>del 20% de las acciones.<br>Priorizá y enfocáte en lo que es importante.</div>
  <div class="rule"></div>
</div>
""")


def s11() -> str:
    """Esto es progreso — circles with fill levels."""
    rows = [
        ("Esto es progreso.", [20, 35, 50, 65, 80, 95]),
        ("Esto también es progreso.", [15, 40, 25, 55, 30, 60]),
        ("Y esto también.", [10, 25, 18, 45, 22, 35]),
    ]
    blocks = ""
    for title, fills in rows:
        circles = "".join(
            f"""<div class="cir"><svg viewBox="0 0 80 80">
              <circle cx="40" cy="40" r="36" fill="none" stroke="{VERDE}" stroke-width="2.5"/>
              <path d="M8 40 A32 32 0 0 0 72 40 L72 72 L8 72 Z" fill="{VERDE}" fill-opacity="0.45"
                transform="translate(0,{(100-f)*0.64})" style="transform-origin:40px 40px"/>
            </svg></div>"""
            # simpler fill from bottom using clip
            .replace(
                f'transform="translate(0,{(100-f)*0.64})"',
                "",
            )
            if False
            else f"""<div class="cir"><div class="ring"><div class="fill" style="height:{f}%"></div></div></div>"""
            for f in fills
        )
        blocks += f'<div class="row"><div class="t">{title}</div><div class="circles">{circles}</div></div>'
    return slide(f"""
<style>
.s11{{height:100%;padding:110px 70px 160px;display:flex;flex-direction:column;gap:55px;}}
.s11 .t{{font-family:var(--serif);font-size:36px;color:var(--verde);margin-bottom:22px;}}
.s11 .circles{{display:flex;gap:22px;}}
.s11 .cir .ring{{
  width:88px;height:88px;border:2.5px solid var(--verde);border-radius:50%;
  overflow:hidden;display:flex;align-items:flex-end;
}}
.s11 .cir .fill{{width:100%;background:var(--verde);opacity:.5;}}
.s11 .rule{{width:80px;height:2px;background:var(--verde);margin:20px auto 0;opacity:.6;}}
</style>
<div class="s11">
  {blocks}
  <div class="rule"></div>
</div>
""")


def build_html() -> Path:
    slides = [s01(), s02(), s03(), s04(), s05(), s06(), s07(), s08(), s09(), s10(), s11()]
    # Fix s05 - I had messy duplicate SVG; rewrite cleanly later if needed
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{font_faces()}{CSS}</style></head>
<body><div class="sheet">{''.join(slides)}</div></body></html>"""
    path = BUILD / "carrusel.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML → {path} ({len(slides)} slides)")
    return path


def main() -> None:
    # Fix slide 5 properly before write
    global s05

    def s05_clean() -> str:
        return slide(f"""
<style>
.s5{{padding:100px 80px 150px;display:flex;flex-direction:column;justify-content:space-evenly;height:100%;}}
.s5 .block{{text-align:center;}}
.s5 h2{{font-family:var(--pop);font-weight:700;font-size:48px;color:var(--verde);margin-bottom:22px;}}
.s5 svg{{width:92%;height:100px;}}
</style>
<div class="s5">
  <div class="block">
    <h2>Procrastinando</h2>
    <svg viewBox="0 0 900 100" fill="none">
      <path d="M50 55 H280 V20 H400 V55 H780" stroke="{VERDE}" stroke-width="4" stroke-linejoin="round"/>
      <polygon points="780,55 760,45 760,65" fill="{VERDE}"/>
      <circle cx="340" cy="37" r="24" fill="{VERDE}"/>
      <path d="M330 27 L350 47 M350 27 L330 47" stroke="#fff" stroke-width="4" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="block">
    <h2>Sobrepensando</h2>
    <svg viewBox="0 0 900 120" fill="none">
      <path d="M50 60 H260" stroke="{VERDE}" stroke-width="4"/>
      <path d="M300 60 m-45,0 a45,45 0 1,1 90,0 a45,45 0 1,1 -90,0" stroke="{VERDE}" stroke-width="4"/>
      <path d="M300 60 m-22,0 a22,22 0 1,1 44,0 a22,22 0 1,1 -44,0" stroke="{VERDE}" stroke-width="4"/>
      <circle cx="300" cy="60" r="18" fill="{VERDE}"/>
      <path d="M292 52 L308 68 M308 52 L292 68" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>
    </svg>
  </div>
  <div class="block">
    <h2>Haciendo</h2>
    <svg viewBox="0 0 900 100" fill="none">
      <path d="M50 50 H760" stroke="{VERDE}" stroke-width="4" stroke-linecap="round"/>
      <polygon points="760,50 740,40 740,60" fill="{VERDE}"/>
      <circle cx="820" cy="50" r="28" fill="{VERDE}"/>
      <path d="M806 50 L816 60 L836 38" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</div>
""")

    slides = [s01(), s02(), s03(), s04(), s05_clean(), s06(), s07(), s08(), s09(), s10(), s11()]
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<style>{font_faces()}{CSS}</style></head>
<body><div class="sheet">{''.join(slides)}</div></body></html>"""
    path = BUILD / "carrusel.html"
    path.write_text(html, encoding="utf-8")
    print(f"HTML → {path} ({len(slides)} slides)")

    print("Render retina…")
    pngs = render(BUILD)
    print(f"PNGs: {len(pngs)}")
    meta = {
        "titulo": "Disciplina · Hábitos · Progreso",
        "slides": 11,
        "fondo": "blanco_minimal_editorial",
        "familia_visual": "infografia_serif_minima",
        "origen": "screenshot",
        "keyword_portada": "DISCIPLINA",
        "id": "2026-09-14-carrusel-disciplina-minima",
    }
    out = package(BUILD, "STLabs-Disciplina-Minima", meta=meta)
    print(f"Package → {out}")
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        f"""# Manifiesto de fuentes — Disciplina · Hábitos · Progreso

| Tipografía | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Playfair Display | 700 / italic | Títulos serif | google/fonts | `@font-face` base64 |
| Poppins | 700 | Títulos sans display | pack STLabs | idem |
| IBM Plex Sans | 300–500 | Cuerpo / labels | pack STLabs | idem |
| IBM Plex Mono | 400 | Footer `{HANDLE}` | pack STLabs | idem |
| Lora | italic | Acentos | pack STLabs | idem |

## Color
- Verde marca oscurecido 2 tonos: `{VERDE}` (base marca `#00FFB2`)
- Fondo: blanco puro `{PAPER}`
""",
        encoding="utf-8",
    )
    (BUILD / "CAPTION.txt").write_text(
        """Motivación sube y baja.
Disciplina construye.

No es suerte: son tus decisiones, hábitos y rutinas.

Comentá DISCIPLINA si querés el marco completo.

#disciplina #hábitos #progreso #revops
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
