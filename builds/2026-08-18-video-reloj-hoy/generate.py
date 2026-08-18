# -*- coding: utf-8 -*-
"""Video reloj STLabs — fondo negro, todo verde, agujas en loop."""
from pathlib import Path
import json
import math

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
W, H = 1080, 1920
CX, CY = 540, 900
R_TICK_OUT = 338
R_TICK_IN = 312
R_TICK_HOUR_IN = 292
R_TEXT = 418
GREEN = "#00FFB2"
BG = "#0A0A0A"
DURATION = 8.0
FPS = 30


def ticks() -> str:
    parts = []
    for i in range(60):
        ang = math.radians(i * 6 - 90)
        inner = R_TICK_HOUR_IN if i % 5 == 0 else R_TICK_IN
        w = 6 if i % 5 == 0 else 2.4
        x1 = CX + inner * math.cos(ang)
        y1 = CY + inner * math.sin(ang)
        x2 = CX + R_TICK_OUT * math.cos(ang)
        y2 = CY + R_TICK_OUT * math.sin(ang)
        parts.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{GREEN}" stroke-width="{w}" stroke-linecap="square"/>'
        )
    return "\n".join(parts)


def _arc(text: str, center_deg: float, arc_deg: float, size: int, radius: float = R_TEXT) -> str:
    """Coloca letras en arco horario. 0° = 12 en punto."""
    n = max(len(text) - 1, 1)
    start = center_deg - arc_deg / 2.0
    step = arc_deg / n
    parts = []
    for i, ch in enumerate(text):
        if ch == " ":
            continue
        ang = start + i * step
        parts.append(
            f'<text class="circ" x="{CX}" y="{CY}" font-size="{size}" '
            f'transform="rotate({ang:.3f} {CX} {CY}) translate(0 -{radius})" '
            f'text-anchor="middle" dominant-baseline="middle">{_esc(ch)}</text>'
        )
    return "\n".join(parts)


def circular_text() -> str:
    # Como la referencia: arriba / derecha / hoy abajo.
    return "\n".join(
        [
            _arc("Dentro de un año,", 0, 132, 40),
            _arc("agradecerás haber empezado", 118, 108, 38),
            _arc("hoy", 180, 34, 58, radius=R_TEXT + 6),
        ]
    )


def _esc(ch: str) -> str:
    return (
        ch.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_html() -> str:
    f = str(FONTS)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Dentro de un año — STLabs</title>
<style>
@font-face {{
  font-family:'Poppins';
  src:url('file://{f}/Poppins-ExtraBold.ttf') format('truetype');
  font-weight:800;
}}
@font-face {{
  font-family:'IBM Plex Mono';
  src:url('file://{f}/IBMPlexMono-Medium.ttf') format('truetype');
  font-weight:500;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
html, body {{ background:{BG}; width:{W}px; height:{H}px; overflow:hidden; }}
.stage {{
  position:relative; width:{W}px; height:{H}px; background:{BG};
}}
svg {{ position:absolute; inset:0; }}
.circ {{
  font-family:'Poppins', sans-serif; font-weight:800;
  fill:{GREEN}; letter-spacing:0;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:72px; text-align:center;
  font-family:'IBM Plex Mono', monospace; font-weight:500;
  font-size:22px; letter-spacing:.14em; color:{GREEN};
}}
</style>
</head>
<body>
<div class="stage" id="stage">
<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true">
  {ticks()}
  {circular_text()}
  <g id="hour">
    <rect x="{CX - 8}" y="{CY - 168}" width="16" height="186" rx="2" fill="{GREEN}"/>
  </g>
  <g id="minute">
    <rect x="{CX - 4.5}" y="{CY - 262}" width="9" height="278" rx="2" fill="{GREEN}"/>
  </g>
  <circle cx="{CX}" cy="{CY}" r="14" fill="{GREEN}"/>
</svg>
<div class="firma">sebastian.stlabs.ar</div>
</div>
<script>
const CX = {CX}, CY = {CY}, DURATION = {DURATION};
function setClock(t) {{
  const u = ((t % DURATION) + DURATION) % DURATION;
  const min = (u / DURATION) * 360;
  const hour = (u / DURATION) * 30;
  document.getElementById('minute').setAttribute('transform', `rotate(${{min}} ${{CX}} ${{CY}})`);
  document.getElementById('hour').setAttribute('transform', `rotate(${{hour}} ${{CX}} ${{CY}})`);
}}
window.setClock = setClock;
let start = null;
function loop(ts) {{
  if (start === null) start = ts;
  setClock((ts - start) / 1000);
  requestAnimationFrame(loop);
}}
if (!new URLSearchParams(location.search).has('still')) requestAnimationFrame(loop);
else setClock(0);
</script>
</body>
</html>
"""


def main():
    html = build_html()
    (B / "reloj.html").write_text(html, encoding="utf-8")
    meta = {
        "titulo": "Dentro de un año, agradecerás haber empezado hoy",
        "formato": "video 9:16",
        "duracion_s": DURATION,
        "fps": FPS,
        "fondo": BG,
        "acento": GREEN,
        "firma": "sebastian.stlabs.ar",
        "origen": "clonado",
        "id": "2026-08-18-video-reloj-hoy",
        "fecha": "2026-08-18",
        "notas": "Agujas en movimiento constante. Loop 8s. Minutero 1 vuelta/8s, horario 1 vuelta/96s.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote reloj.html · {W}x{H} · {DURATION}s loop")


if __name__ == "__main__":
    main()
