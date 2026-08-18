# -*- coding: utf-8 -*-
"""Video reloj STLabs — 6:7, mayúsculas gruesas, blanco + verde."""
from pathlib import Path
import json
import math

B = Path(__file__).resolve().parent
FONTS = Path("/tmp/stlabs-fonts")
W, H = 1080, 1260  # 6:7
CX, CY = 540, 598
R_TICK_OUT = 312
R_TICK_IN = 286
R_TICK_HOUR_IN = 268
R_TEXT = 378
GREEN = "#00FFB2"
WHITE = "#F2F2F2"
BG = "#0A0A0A"
DURATION = 8.0
FPS = 30

# Anchos relativos de Poppins ExtraBold en caja alta (em).
CAP_W = {
    " ": 0.30, ",": 0.30, ".": 0.30,
    "I": 0.42, "J": 0.48, "L": 0.52, "T": 0.56, "F": 0.56,
    "E": 0.60, "S": 0.62, "Z": 0.62, "P": 0.64, "B": 0.66,
    "Y": 0.66, "V": 0.68, "X": 0.68, "K": 0.70, "R": 0.70,
    "A": 0.72, "Á": 0.72, "C": 0.72, "G": 0.74, "O": 0.76,
    "Q": 0.76, "D": 0.76, "H": 0.76, "U": 0.76, "N": 0.78,
    "Ñ": 0.78, "M": 0.92, "W": 0.94,
}


def ticks() -> str:
    parts = []
    for i in range(60):
        ang = math.radians(i * 6 - 90)
        inner = R_TICK_HOUR_IN if i % 5 == 0 else R_TICK_IN
        w = 7 if i % 5 == 0 else 2.6
        x1 = CX + inner * math.cos(ang)
        y1 = CY + inner * math.sin(ang)
        x2 = CX + R_TICK_OUT * math.cos(ang)
        y2 = CY + R_TICK_OUT * math.sin(ang)
        parts.append(
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{GREEN}" stroke-width="{w}" stroke-linecap="square"/>'
        )
    return "\n".join(parts)


def _esc(ch: str) -> str:
    return (
        ch.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def _advance_deg(ch: str, size: float, radius: float, tracking: float = 0.12) -> float:
    em = CAP_W.get(ch, 0.72)
    px = size * (em + tracking)
    return (px / radius) * (180.0 / math.pi)


def _letters(
    text: str,
    start_deg: float,
    size: int,
    fill: str,
    radius: float = R_TEXT,
    tracking: float = 0.12,
    flip: bool = False,
):
    """Coloca caja alta con avance por ancho real — evita amontonar el costado."""
    ang = start_deg
    parts = []
    extra = " rotate(180)" if flip else ""
    for ch in text:
        step = _advance_deg(ch, size, radius, tracking=tracking)
        ang += step / 2.0
        if ch != " ":
            cls = "circ green" if fill == GREEN else "circ white"
            parts.append(
                f'<text class="{cls}" x="0" y="0" font-size="{size}" '
                f'fill="{fill}" stroke="{fill}" '
                f'transform="translate({CX} {CY}) rotate({ang:.3f}) '
                f'translate(0 {-radius}){extra}" '
                f'text-anchor="middle" dominant-baseline="middle">{_esc(ch)}</text>'
            )
        ang += step / 2.0
    return parts, ang


def circular_text() -> str:
    """
    Arco como la referencia:
      arriba  DENTRO DE UN AÑO,     (blanco + AÑO verde)
      derecha AGRADECERÁS HABER EMPEZADO  (blanco, costado aireado)
      abajo   HOY                   (verde, grueso)
    """
    parts = []
    # Top: arranca ~9:30 y encadena AÑO en verde.
    top, ang = _letters("DENTRO DE UN ", -72, 46, WHITE)
    parts += top
    year, ang = _letters("AÑO", ang, 46, GREEN)
    parts += year
    comma, ang = _letters(",", ang, 46, WHITE)
    parts += comma

    # Costado derecho: aire entre letras, termina antes de HOY.
    side, _ = _letters(
        "AGRADECERÁS HABER EMPEZADO",
        ang + 10,
        43,
        WHITE,
        radius=R_TEXT + 4,
        tracking=0.10,
    )
    parts += side
    return "\n".join(parts)


def build_html() -> str:
    f = str(FONTS)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>DENTRO DE UN AÑO — STLabs</title>
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
  letter-spacing:0; paint-order:stroke fill;
  stroke-width:3.2px; stroke-linejoin:round;
}}
.circ.white {{ fill:{WHITE}; stroke:{WHITE}; }}
.circ.green {{ fill:{GREEN}; stroke:{GREEN}; }}
.hoy {{
  font-size:72px; letter-spacing:.08em;
  stroke-width:4px;
}}
.firma {{
  position:absolute; left:0; right:0; bottom:44px; text-align:center;
  font-family:'IBM Plex Mono', monospace; font-weight:500;
  font-size:20px; letter-spacing:.14em; color:{GREEN};
}}
</style>
</head>
<body>
<div class="stage" id="stage">
<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" aria-hidden="true">
  {ticks()}
  {circular_text()}
  <text class="circ green hoy" x="{CX}" y="{CY + R_TICK_OUT + 78}"
        text-anchor="middle" dominant-baseline="middle">HOY</text>
  <g id="hour">
    <rect x="{CX - 9}" y="{CY - 152}" width="18" height="168" rx="2" fill="{GREEN}"/>
  </g>
  <g id="minute">
    <rect x="{CX - 5}" y="{CY - 238}" width="10" height="252" rx="2" fill="{GREEN}"/>
  </g>
  <circle cx="{CX}" cy="{CY}" r="15" fill="{GREEN}"/>
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
        "formato": "video 6:7",
        "ancho": W,
        "alto": H,
        "duracion_s": DURATION,
        "fps": FPS,
        "fondo": BG,
        "acento": GREEN,
        "texto": WHITE,
        "firma": "sebastian.stlabs.ar",
        "origen": "clonado",
        "id": "2026-08-18-video-reloj-hoy",
        "fecha": "2026-08-18",
        "notas": "6:7 · caja alta extra gruesa · blanco en costados · AÑO y HOY verdes · agujas en loop.",
    }
    (B / "index.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote reloj.html · {W}x{H} · {DURATION}s loop")


if __name__ == "__main__":
    main()
