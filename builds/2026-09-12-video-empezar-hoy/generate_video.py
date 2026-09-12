# -*- coding: utf-8 -*-
"""Video STLabs: Dentro de un año desearás haber empezado hoy.

Fondo blanco. Arcos concéntricos que se despliegan desde el punto.
"""
from __future__ import annotations

import math
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

W, H = 1080, 1350
SCALE = 2
WW, HH = W * SCALE, H * SCALE

VERDE = (0, 255, 178)  # #00FFB2
NEGRO = (10, 10, 10)
BLANCO = (255, 255, 255)

FONT_DIR = REPO / "fonts"
MAC_DIR = Path("/usr/share/fonts/truetype/macos")
HANDLE = "sebastian.stlabs.ar"

OX = 0.18 * WW
OY = 0.38 * HH

# (radio, start_deg, end_deg) — horario desde start → end.
# Sale del punto hacia arriba-derecha (≈85°) y barre a la derecha/abajo (forma C).
ARCS = [
    (0.07 * WW, 88, -8),
    (0.13 * WW, 92, -28),
    (0.20 * WW, 95, -42),
    (0.28 * WW, 98, -52),
    (0.37 * WW, 100, -60),
    (0.47 * WW, 102, -66),
    (0.58 * WW, 104, -70),
]

FPS = 30
T_DOT = 0.20
T_DRAW0 = 0.35
T_DRAW = 2.5
T_TEXT0 = T_DRAW0 + T_DRAW + 0.1
T_TEXT = 0.7
T_HOLD = 2.0
DUR_TOTAL = T_TEXT0 + T_TEXT + T_HOLD


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), int(size * SCALE))


def ease_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return 1.0 - (1.0 - t) ** 3


def lerp_color(a, b, t: float):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def angle_clockwise(start: float, end: float, t: float) -> float:
    span = (start - end) % 360.0
    if span == 0:
        span = 360.0
    return start - span * t


def pt(cx: float, cy: float, r: float, deg: float) -> tuple[float, float]:
    rad = math.radians(deg)
    return cx + r * math.cos(rad), cy - r * math.sin(rad)


def draw_arc(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    r: float,
    start: float,
    end: float,
    t: float,
    width: int,
) -> None:
    if t <= 0.001:
        return
    t = ease_out(t)
    span_total = (start - end) % 360.0 or 360.0
    cur_span = span_total * t
    steps = max(12, int(cur_span * 2.5))
    pts = [
        pt(cx, cy, r, angle_clockwise(start, end, t * i / steps))
        for i in range(steps + 1)
    ]
    if len(pts) == 1:
        x, y = pts[0]
        rr = width / 2 + 0.5
        draw.ellipse([x - rr, y - rr, x + rr, y + rr], fill=NEGRO)
        return
    draw.line(pts, fill=NEGRO, width=width, joint="curve")
    for x, y in (pts[0], pts[-1]):
        rr = width / 2
        draw.ellipse([x - rr, y - rr, x + rr, y + rr], fill=NEGRO)


def text_centered(draw, text, y, fnt, fill, cx=None):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    base = WW / 2 if cx is None else cx
    x = base - tw / 2 - bbox[0]
    draw.text((x, y - bbox[1]), text, font=fnt, fill=fill)


def render_frame(t: float) -> Image.Image:
    img = Image.new("RGB", (WW, HH), BLANCO)
    d = ImageDraw.Draw(img)

    f_mono = font(FONT_DIR / "IBMPlexMono-Medium.ttf", 22)
    f_hoy = font(FONT_DIR / "Lora-Italic-Variable.ttf", 20)
    f_q = font(MAC_DIR / "Inter-Regular.ttf", 38)
    f_qi = font(FONT_DIR / "Lora-Italic-Variable.ttf", 40)

    text_centered(d, HANDLE, 56 * SCALE, f_mono, VERDE)

    if t >= T_DOT:
        fade = min(1.0, (t - T_DOT) / 0.25)
        col = lerp_color(BLANCO, NEGRO, fade)
        rd = 8 * SCALE
        d.ellipse([OX - rd, OY - rd, OX + rd, OY + rd], fill=col)
        hb = d.textbbox((0, 0), "hoy", font=f_hoy)
        hx = OX - (hb[2] - hb[0]) / 2 - hb[0]
        hy = OY + 18 * SCALE - hb[1]
        d.text((hx, hy), "hoy", font=f_hoy, fill=lerp_color(BLANCO, NEGRO, fade))

    if t >= T_DRAW0:
        p = max(0.0, min(1.0, (t - T_DRAW0) / T_DRAW))
        stroke = max(3, int(2.2 * SCALE))
        for r, a0, a1 in ARCS:
            draw_arc(d, OX, OY, r, a0, a1, p, stroke)

    if t >= T_TEXT0:
        tf = ease_out((t - T_TEXT0) / T_TEXT)
        cx = 0.62 * WW
        y0 = 0.55 * HH
        gap = 52 * SCALE
        lines = [
            ("Dentro de un año", f_q, NEGRO),
            ("desearás haber", f_q, NEGRO),
            ("empezado hoy.", f_qi, NEGRO),
        ]
        for i, (txt, fnt, base) in enumerate(lines):
            text_centered(
                d, txt, y0 + i * gap, fnt, lerp_color(BLANCO, base, tf), cx=cx
            )

        accent_y = HH - 100 * SCALE
        aw = 48 * SCALE
        d.rectangle(
            [WW / 2 - aw / 2, accent_y, WW / 2 + aw / 2, accent_y + 3 * SCALE],
            fill=lerp_color(BLANCO, VERDE, tf),
        )
        text_centered(
            d, HANDLE, HH - 72 * SCALE, f_mono, lerp_color(BLANCO, VERDE, tf)
        )

    return img


def main() -> None:
    out = BUILD / "out"
    out.mkdir(parents=True, exist_ok=True)
    frames = BUILD / "_frames"
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir()

    n = int(DUR_TOTAL * FPS)
    print(f"frames={n} dur={DUR_TOTAL:.1f}s")
    for i in range(n):
        fr = render_frame(i / FPS)
        fr.resize((W, H), Image.Resampling.LANCZOS).save(frames / f"f_{i:05d}.png")
        if i % 30 == 0:
            print(f"  {i}/{n}")

    mp4 = out / "STLabs-Video-Empezar-Hoy.mp4"
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-framerate",
            str(FPS),
            "-i",
            str(frames / "f_%05d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-crf",
            "17",
            "-preset",
            "medium",
            "-movflags",
            "+faststart",
            str(mp4),
        ],
        check=True,
        capture_output=True,
    )
    print("mp4", mp4.stat().st_size)

    last = render_frame(DUR_TOTAL - 0.05)
    last.resize((W, H), Image.Resampling.LANCZOS).save(
        out / "STLabs-Video-Empezar-Hoy-poster.png"
    )
    last.save(out / "STLabs-Video-Empezar-Hoy-poster@2x.png")

    step = max(1, n // 20)
    gifs = [
        Image.open(frames / f"f_{i:05d}.png").resize(
            (360, 450), Image.Resampling.LANCZOS
        )
        for i in range(0, n, step)
    ]
    gifs[0].save(
        out / "preview.gif",
        save_all=True,
        append_images=gifs[1:],
        duration=int(1000 * step / FPS),
        loop=0,
    )
    shutil.rmtree(frames)

    (BUILD / "caption.txt").write_text(
        """Dentro de un año desearás haber empezado hoy.

No hace falta el plan perfecto.
Hace falta el primer paso.

Si estás dando vueltas con la operación, el CRM o los agentes:
empezá hoy. El sistema se ordena en movimiento.

sebastian.stlabs.ar

—
Comentá HOY y te paso el primer paso para tu operación.
""",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        """# Manifiesto de fuentes — Video Empezar Hoy

| Familia | Peso | Rol | Origen |
|---|---|---|---|
| IBM Plex Mono | Medium | Handle + footer | `/workspace/fonts/IBMPlexMono-Medium.ttf` |
| Inter | Regular | Quote líneas 1–2 | `/usr/share/fonts/truetype/macos/Inter-Regular.ttf` |
| Lora | Italic | Label «hoy» + «empezado hoy.» | `/workspace/fonts/Lora-Italic-Variable.ttf` |

1080×1350 @ 30fps · H.264 CRF 17 · master interno 2160×2700.
""",
        encoding="utf-8",
    )

    try:
        from stlabs_memory import registrar_carrusel

        registrar_carrusel(
            BUILD,
            {
                "id": "2026-09-12-video-empezar-hoy",
                "fecha": "2026-09-12",
                "titulo": "Dentro de un año desearás haber empezado hoy",
                "slides": 1,
                "fondo": "lino_tela",
                "familia_visual": "before_after",
                "origen": "screenshot",
                "keyword_portada": "HOY",
            },
        )
    except Exception as e:
        print("memoria:", e)

    print("OK", mp4)


if __name__ == "__main__":
    main()
