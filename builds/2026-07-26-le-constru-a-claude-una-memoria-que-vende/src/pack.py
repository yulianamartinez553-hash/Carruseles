# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, "/workspace")
import stlabs_kit

stlabs_kit.FONT_FACES += [
    ("Archivo Black", "/usr/share/fonts/truetype/extra/ArchivoBlack.ttf", 400, "normal"),
]

meta = {
    "titulo": "Le construí a Claude una memoria que vende",
    "slides": 7,
    "fondo": "blanco_constelacion",
    "familia_visual": "editorial_grotesca",
    "origen": "screenshot",
    "keyword_portada": "AGENTE",
    "notas": (
        "Clon del carrusel 'memoria que nunca olvida' (Obsidian×Hermes×Claude), traducido "
        "al español voseo y adaptado a un agente que vende la marca (CRM×Agente×Claude). "
        "Modo blanco pedido explícito. Estrella naranja de la referencia mantenida exacta "
        "(#E85A24, starburst de brazos redondeados). Título Archivo Black + Lora itálica."
    ),
}

out = stlabs_kit.package("/tmp/build-agente", "STLabs-Agente-Memoria", meta=meta)
print("package →", out)
