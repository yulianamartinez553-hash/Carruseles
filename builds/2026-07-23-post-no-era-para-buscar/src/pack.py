# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, "/workspace")
import stlabs_kit

# fuentes extra de este carrusel → también embebidas en el HTML final
stlabs_kit.FONT_FACES += [
    ("Press Start 2P", "/usr/share/fonts/truetype/extra/PressStart2P.ttf", 400, "normal"),
    ("Caveat", "/usr/share/fonts/truetype/extra/Caveat.ttf", "400 700", "normal"),
]

meta = {
    "titulo": "POST no era para buscar",
    "slides": 12,
    "fondo": "blanco_reticula_fina",
    "familia_visual": "pixel_protocol",
    "origen": "screenshot",
    "keyword_portada": "QUERY",
    "notas": (
        "Clon del carrusel RFC 10008/QUERY. Modo blanco pedido explícito. "
        "Robots pixel-art SVG: POST naranja idéntico a la referencia (#FF5A2E), "
        "QUERY en verde de marca, GET azul. Fuentes extra: Press Start 2P (labels robots), "
        "Caveat (firmas/nota adhesiva)."
    ),
}

out = stlabs_kit.package("/tmp/build-query", "STLabs-QUERY-RFC10008", meta=meta)
print("package →", out)
