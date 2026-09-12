# -*- coding: utf-8 -*-
"""Post buy/CTA: PROCESOS — feed 4:5, fondo blanco STLabs."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parents[2]
BUILD = Path(__file__).resolve().parent
FONTS = REPO / "fonts"

# Lienzo lógico 1080×1350; render master 4×
W, H = 1080, 1350
SCALE = 4
VERDE = (0, 255, 178)  # #00FFB2
NEGRO = (10, 10, 10)  # #0A0A0A
GRIS = (90, 90, 90)
BLANCO = (255, 255, 255)


def _font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size * SCALE)


def _reticula(img: Image.Image, step: int = 52, alpha: int = 14) -> None:
    """Retícula fina sobre blanco (familia dossier)."""
    overlay = Image.new("RGBA", img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(overlay)
    s = step * SCALE
    w, h = img.size
    col = (10, 10, 10, alpha)
    for x in range(0, w, s):
        d.line([(x, 0), (x, h)], fill=col, width=max(1, SCALE // 4))
    for y in range(0, h, s):
        d.line([(0, y), (w, y)], fill=col, width=max(1, SCALE // 4))
    img.alpha_composite(overlay)


def _center_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    font: ImageFont.FreeTypeFont,
    fill,
) -> tuple[int, int, int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (W * SCALE - tw) // 2 - bbox[0]
    draw.text((x, y - bbox[1]), text, font=font, fill=fill)
    return x, y, x + tw, y + th


def render() -> Image.Image:
    img = Image.new("RGBA", (W * SCALE, H * SCALE), (*BLANCO, 255))
    _reticula(img)
    d = ImageDraw.Draw(img)

    f_mono = _font("IBMPlexMono-Medium.ttf", 22)
    f_mono_sm = _font("IBMPlexMono-Medium.ttf", 18)
    f_eyebrow = _font("IBMPlexMono-Medium.ttf", 16)
    f_bebas_hero = _font("BebasNeue-Regular.ttf", 168)
    f_bebas_cta = _font("BebasNeue-Regular.ttf", 52)
    f_pop = _font("Poppins-Bold.ttf", 36)
    f_pop_sm = _font("Poppins-Bold.ttf", 24)

    # Top handle
    _center_text(d, "sebastian.stlabs.ar", 70 * SCALE, f_mono, VERDE)

    # Eyebrow
    _center_text(d, "SISTEMA · REVOPS · IA", 118 * SCALE, f_eyebrow, GRIS)

    # Hero keyword PROCESOS
    hero_y = 280 * SCALE
    x0, y0, x1, y1 = _center_text(d, "PROCESOS", hero_y, f_bebas_hero, VERDE)
    # Línea strike verde (como Turbo) a ~70% de la altura del glifo
    strike_y = y0 + int((y1 - y0) * 0.72)
    pad = 8 * SCALE
    d.rectangle(
        [x0 - pad, strike_y, x1 + pad, strike_y + max(3, 5 * SCALE // 2)],
        fill=NEGRO,
    )

    # Headline
    _center_text(d, "Los procesos", 520 * SCALE, f_pop, NEGRO)
    _center_text(d, "no son lineales.", 568 * SCALE, f_pop, NEGRO)

    # Support
    _center_text(
        d,
        "Y eso también es avanzar.",
        650 * SCALE,
        f_pop_sm,
        GRIS,
    )

    # CTA box
    cta = "COMENTÁ PROCESOS"
    cta_bbox = d.textbbox((0, 0), cta, font=f_bebas_cta)
    ctw, cth = cta_bbox[2] - cta_bbox[0], cta_bbox[3] - cta_bbox[1]
    box_w, box_h = ctw + 64 * SCALE, cth + 36 * SCALE
    box_x = (W * SCALE - box_w) // 2
    box_y = 780 * SCALE
    stroke = max(3, 3 * SCALE)
    d.rectangle(
        [box_x, box_y, box_x + box_w, box_y + box_h],
        outline=VERDE,
        width=stroke,
    )
    cx = box_x + (box_w - ctw) // 2 - cta_bbox[0]
    cy = box_y + (box_h - cth) // 2 - cta_bbox[1]
    d.text((cx, cy), cta, font=f_bebas_cta, fill=VERDE)

    # Micro copy
    _center_text(
        d,
        "y te mando el mapa para ordenar tu operación",
        920 * SCALE,
        f_mono_sm,
        GRIS,
    )

    # Footer
    _center_text(d, "sebastian.stlabs.ar", 1260 * SCALE, f_mono, VERDE)

    return img.convert("RGB")


CAPTION = """Los procesos no son lineales.

Y eso también es avanzar.

Decidís crecer, aparece la motivación, después los problemas.
Lo que funcionaba deja de funcionar. Volvés a fallar.
Y seguís — pero con más criterio.

Comentá PROCESOS y te mando el mapa para ordenar tu operación.

sebastian.stlabs.ar
"""

MANIFIESTO = """# Manifiesto de fuentes — Post Buy Procesos

| Familia | Peso | Rol | Origen |
|---|---|---|---|
| Bebas Neue | 400 | PROCESOS / COMENTÁ PROCESOS | `/workspace/fonts/BebasNeue-Regular.ttf` |
| Poppins | 700 | Headline / apoyo | `/workspace/fonts/Poppins-Bold.ttf` |
| IBM Plex Mono | 500 | Firma / eyebrow / micro | `/workspace/fonts/IBMPlexMono-Medium.ttf` |

Master: 4320×5400 (4×). Export feed 1080×1350 + @2x.
"""


def main() -> None:
    out = BUILD / "out"
    out.mkdir(parents=True, exist_ok=True)
    im = render()
    assert im.size == (4320, 5400), im.size
    im.save(out / "STLabs-Post-Buy-Procesos@4x.png", optimize=True)
    im.resize((2160, 2700), Image.Resampling.LANCZOS).save(
        out / "STLabs-Post-Buy-Procesos@2x.png", optimize=True
    )
    im.resize((1080, 1350), Image.Resampling.LANCZOS).save(
        out / "STLabs-Post-Buy-Procesos.png", optimize=True
    )

    meta = {
        "id": "2026-09-12-post-buy-procesos",
        "titulo": "Buy post Procesos — mapa de operación",
        "tipo": "post",
        "formato": "1080x1350",
        "fondo": "reticula_fina",
        "familia_visual": "dossier_editorial",
        "origen": "original",
        "keyword_portada": "PROCESOS",
        "slides": 1,
    }
    (BUILD / "index.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (BUILD / "caption.txt").write_text(CAPTION, encoding="utf-8")
    (BUILD / "MANIFIESTO-FUENTES.md").write_text(MANIFIESTO, encoding="utf-8")

    sys.path.insert(0, str(REPO))
    from stlabs_memory import registrar_carrusel

    registrar_carrusel(
        BUILD,
        {
            "id": meta["id"],
            "fecha": "2026-09-12",
            "titulo": meta["titulo"],
            "slides": 1,
            "fondo": meta["fondo"],
            "familia_visual": meta["familia_visual"],
            "origen": meta["origen"],
            "keyword_portada": meta["keyword_portada"],
        },
    )

    print("OK", out, im.size)


if __name__ == "__main__":
    main()
