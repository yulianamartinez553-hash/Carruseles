#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reel STLabs — Cómo funciona Turbo (workflow multi-agente animado)."""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

BUILD = Path(__file__).resolve().parent
REPO = BUILD.parents[1]
FONTS_DIR = REPO / "fonts"
OUT = BUILD / "out"
FRAMES = BUILD / "frames"

W, H = 1080, 1920
FPS = 20
DURATION = 30.0

BG = (12, 12, 14)
GREEN = (0, 255, 178)
GREEN_DIM = (0, 150, 110)
WHITE = (242, 242, 242)
GRAY = (150, 150, 158)
ORANGE = (255, 140, 40)
BLUE = (70, 145, 255)
CARD = (28, 28, 32)
CARD_LINE = (58, 58, 66)


def load_font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS_DIR / name), size)


def sh(cmd: list[str]) -> None:
    print("+", " ".join(map(str, cmd[:12])), "...")
    subprocess.run(cmd, check=True)


def tc(draw: ImageDraw.ImageDraw, xy, text, fnt, fill) -> None:
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((xy[0] - tw / 2, xy[1] - th / 2), text, font=fnt, fill=fill)


def bezier(p0, p1, p2, p3, t):
    u = 1 - t
    return (
        u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1],
    )


def wire(draw, p0, p3, progress=1.0, pulse=None, color=GREEN_DIM, width=3):
    mid = (p0[0] + p3[0]) / 2
    c1, c2 = (mid, p0[1]), (mid, p3[1])
    steps = max(8, int(32 * max(progress, 0.05)))
    pts = [bezier(p0, c1, c2, p3, (i / steps) * progress) for i in range(steps + 1)]
    if len(pts) > 1:
        draw.line(pts, fill=color, width=width)
    if pulse is not None and progress > 0.08:
        tt = pulse % 1.0
        if tt <= progress:
            x, y = bezier(p0, c1, c2, p3, tt)
            draw.ellipse([x - 6, y - 6, x + 6, y + 6], fill=GREEN)


def box(draw, cx, cy, w, h, accent, title, subtitle, fonts, active=False):
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    outline = GREEN if active else CARD_LINE
    draw.rounded_rectangle(
        [x0, y0, x0 + w, y0 + h],
        radius=16,
        fill=CARD,
        outline=outline,
        width=3 if active else 2,
    )
    draw.rounded_rectangle([x0 + 8, y0 + 8, x0 + w - 8, y0 + 14], radius=3, fill=accent)
    tc(draw, (cx, cy - (8 if subtitle else 0)), title, fonts["lab"], WHITE)
    if subtitle:
        tc(draw, (cx, cy + 20), subtitle, fonts["tiny"], GRAY)


def render(t: float, fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(20, 20, 24), width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=(20, 20, 24), width=1)

    tc(draw, (W / 2, 78), "CÓMO FUNCIONA TURBO", fonts["title"], WHITE)
    tc(draw, (W / 2, 122), "Flujo multi-agente en paralelo", fonts["sub"], GREEN)

    pulse = (t * 0.9) % 1.0

    trigger = (220, 280)
    prompt = (720, 280)
    agents = [(200, 560), (540, 560), (880, 560)]
    models = [(200, 760), (540, 760), (880, 760)]
    parsed = [(200, 960), (540, 960), (880, 960)]
    recalls = [(200, 1165), (540, 1165), (880, 1165)]
    procs = [(200, 1385), (540, 1385), (880, 1385)]
    bundle = (540, 1585)
    success = (540, 1745)

    la = ["Agente Ventas", "Agente Marketing", "Agente Producto"]
    lr = ["Datos Ventas", "Datos Marketing", "Datos Producto"]
    lp = ["Procesar Ventas", "Procesar Marketing", "Procesar Producto"]

    if t >= 1.0:
        wire(draw, (trigger[0] + 75, trigger[1]), (prompt[0] - 90, prompt[1]), min(1, (t - 1) / 1.2), pulse)
    if t >= 3.2:
        for i, a in enumerate(agents):
            p = min(1.0, max(0.0, (t - 3.2 - i * 0.2) / 1.1))
            wire(draw, (prompt[0], prompt[1] + 48), (a[0], a[1] - 52), p, pulse + i * 0.12)
    if t >= 5.0:
        for i, (a, m) in enumerate(zip(agents, models)):
            p = min(1.0, max(0.0, (t - 5.0 - i * 0.15) / 1.0))
            wire(draw, (a[0], a[1] + 48), (m[0], m[1] - 42), p, pulse + 0.25, BLUE, 2)
    if t >= 9.5:
        for i, (m, pn) in enumerate(zip(models, parsed)):
            p = min(1.0, max(0.0, (t - 9.5 - i * 0.15) / 1.0))
            wire(draw, (m[0], m[1] + 42), (pn[0], pn[1] - 42), p, pulse + 0.4)
    if t >= 12.0:
        for i, (pn, r) in enumerate(zip(parsed, recalls)):
            p = min(1.0, max(0.0, (t - 12.0 - i * 0.15) / 1.0))
            wire(draw, (pn[0], pn[1] + 42), (r[0], r[1] - 48), p, pulse + 0.15, ORANGE)
    if t >= 16.5:
        for i, (r, pr) in enumerate(zip(recalls, procs)):
            p = min(1.0, max(0.0, (t - 16.5 - i * 0.12) / 1.0))
            wire(draw, (r[0], r[1] + 48), (pr[0], pr[1] - 48), p, pulse + 0.3, ORANGE)
    if t >= 22.0:
        for i, pr in enumerate(procs):
            p = min(1.0, max(0.0, (t - 22.0 - i * 0.12) / 1.1))
            wire(draw, (pr[0], pr[1] + 48), (bundle[0], bundle[1] - 42), p, pulse + i * 0.08, GREEN)
    if t >= 26.0:
        wire(
            draw,
            (bundle[0], bundle[1] + 42),
            (success[0], success[1] - 42),
            min(1.0, (t - 26.0) / 1.2),
            pulse,
            GREEN,
            4,
        )

    box(draw, *trigger, 155, 100, ORANGE, "Activador", "del flujo", fonts, True)
    if t >= 1.0:
        box(draw, *prompt, 200, 100, BLUE, "Crear prompt", "Disparador", fonts, 1 <= t < 8)

    if t >= 3.2:
        for i, a in enumerate(agents):
            box(draw, *a, 180, 100, GREEN_DIM, la[i], "Agente IA", fonts, t < 16)

    if t >= 5.0:
        for m in models:
            draw.ellipse([m[0] - 36, m[1] - 36, m[0] + 36, m[1] + 36], fill=CARD, outline=BLUE, width=3)
            tc(draw, m, "LLM", fonts["lab"], BLUE)
            tc(draw, (m[0], m[1] + 52), "Modelo chat", fonts["tiny"], GRAY)

    if t >= 9.5:
        for pn in parsed:
            draw.ellipse([pn[0] - 36, pn[1] - 36, pn[0] + 36, pn[1] + 36], fill=CARD, outline=GREEN, width=3)
            pts = [(pn[0] + i, pn[1] + int(7 * math.sin(i * 0.5))) for i in range(-14, 15)]
            draw.line(pts, fill=GREEN, width=3)
            tc(draw, (pn[0], pn[1] + 54), "Salida estructurada", fonts["tiny"], GRAY)

    if t >= 12.0:
        for i, r in enumerate(recalls):
            box(draw, *r, 170, 95, (70, 70, 80), lr[i], "Memoria", fonts, t < 22)

    if t >= 16.5:
        for i, pr in enumerate(procs):
            box(draw, *pr, 175, 95, ORANGE, lp[i], "Procesador", fonts, t < 26)

    if t >= 22.0:
        box(draw, *bundle, 240, 95, GREEN_DIM, "Empaquetar datos", "procesados", fonts, True)

    if t >= 26.0:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse(
            [success[0] - 90, success[1] - 70, success[0] + 90, success[1] + 70],
            fill=(0, 255, 178, 55),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(22))
        img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
        draw = ImageDraw.Draw(img)
        box(draw, *success, 250, 90, GREEN, "Estado de éxito", "Generado", fonts, True)

    tips = [
        (0.4, 3.0, "Turbo recibe el disparador y arma el prompt"),
        (3.2, 9.0, "Un prompt → tres agentes en paralelo"),
        (9.5, 16.0, "Cada agente estructura y recupera datos"),
        (16.5, 21.5, "Procesa ventas, marketing y producto"),
        (22.0, 25.8, "Empaqueta todo en un solo resultado"),
        (26.0, 30.0, "Listo: Turbo entrega el estado de éxito"),
    ]
    for a, b, msg in tips:
        if a <= t < b:
            bbox = draw.textbbox((0, 0), msg, font=fonts["tip"])
            tw = bbox[2] - bbox[0]
            x0 = (W - tw) // 2 - 22
            y0 = 165
            draw.rounded_rectangle(
                [x0, y0, x0 + tw + 44, y0 + 48],
                radius=14,
                fill=(0, 0, 0),
                outline=GREEN,
                width=2,
            )
            tc(draw, (W / 2, y0 + 24), msg, fonts["tip"], WHITE)
            break

    tc(draw, (W / 2, H - 64), "sebastian.stlabs.ar", fonts["foot"], GREEN)
    return img


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    for p in FRAMES.glob("f_*.png"):
        p.unlink()

    fonts = {
        "title": load_font("Poppins-Bold.ttf", 44),
        "lab": load_font("Poppins-Bold.ttf", 20),
        "sub": load_font("IBMPlexMono-Medium.ttf", 22),
        "tiny": load_font("IBMPlexMono-Medium.ttf", 14),
        "tip": load_font("Poppins-Bold.ttf", 24),
        "foot": load_font("IBMPlexMono-Medium.ttf", 30),
    }

    n = int(DURATION * FPS)
    for i in range(n):
        render(i / FPS, fonts).save(FRAMES / f"f_{i:05d}.png")
        if i % 40 == 0:
            print(f"frame {i}/{n}")

    mp4 = OUT / "STLabs-Reel-Turbo-Flujo.mp4"
    sh([
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", str(FRAMES / "f_%05d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17",
        "-movflags", "+faststart",
        str(mp4),
    ])
    for ss, name in [(1.2, "preview-01"), (5, "preview-05"), (13, "preview-13"), (24, "preview-24")]:
        sh([
            "ffmpeg", "-y", "-ss", str(ss), "-i", str(mp4),
            "-frames:v", "1", "-update", "1", str(OUT / f"{name}.png"),
        ])

    (BUILD / "caption.txt").write_text(
        "Así funciona Turbo.\n\n"
        "Un disparador. Un prompt.\n"
        "Tres agentes en paralelo: ventas, marketing y producto.\n"
        "Cada uno estructura, recupera y procesa.\n"
        "Todo se empaqueta en un solo resultado.\n\n"
        "Menos ida y vuelta. Más ejecución.\n\n"
        "Comentá TURBO y te muestro cómo aplicarlo a tu operación.\n\n"
        "#turbo #automatizacion #agentes #stlabs #revops\n",
        encoding="utf-8",
    )
    (BUILD / "index.json").write_text(
        "{\n"
        '  "id": "2026-09-11-reel-turbo-flujo",\n'
        '  "titulo": "Cómo funciona Turbo — flujo multi-agente",\n'
        '  "tipo": "reel",\n'
        '  "duracion_s": 30,\n'
        '  "formato": "1080x1920",\n'
        '  "fondo": "negro_nodos",\n'
        '  "familia_visual": "manifiesto",\n'
        '  "origen": "screenshot",\n'
        '  "keyword_portada": "TURBO"\n'
        "}\n",
        encoding="utf-8",
    )
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(
        "# Manifiesto de fuentes — Reel Turbo flujo\n\n"
        "| Familia | Peso | Rol | Origen |\n|---|---|---|---|\n"
        "| Poppins | 700 | Título / tips / nodos | `/workspace/fonts/Poppins-Bold.ttf` |\n"
        "| IBM Plex Mono | 500 | Labels / firma | `/workspace/fonts/IBMPlexMono-Medium.ttf` |\n",
        encoding="utf-8",
    )
    print("DONE →", mp4)


if __name__ == "__main__":
    main()
