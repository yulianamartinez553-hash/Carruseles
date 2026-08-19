# Manifiesto de fuentes — Historias PROCESO (9:16)

| Nombre | Peso / estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Bebas Neue | 400 | Título display / keyword PROCESO | `/workspace/fonts/BebasNeue-Regular.ttf` (skill STLabs) | `@font-face{font-family:'Bebas Neue';src:url('file:///tmp/stlabs-fonts/BebasNeue-Regular.ttf') format('truetype');}` |
| Lora | italic variable 600 | Palabra-acento (cabeza, vos, escala, salva, operación, genere) | `/workspace/fonts/Lora-Italic-Variable.ttf` | `@font-face{font-family:'Lora';font-style:italic;font-weight:400 700;src:url('file:///tmp/stlabs-fonts/Lora-Italic-Variable.ttf') format('truetype');}` |
| Barlow Condensed | 500 | Apoyo / hint CTA | `/workspace/fonts/BarlowCondensed-Medium.ttf` | `@font-face{font-family:'Barlow Condensed';font-weight:500;src:url('file:///tmp/stlabs-fonts/BarlowCondensed-Medium.ttf') format('truetype');}` |
| IBM Plex Mono | SemiBold 600 / Medium 500 | Brand, kicker, firma `sebastian.stlabs.ar` | `/workspace/fonts/IBMPlexMono-*.ttf` | `@font-face` IBMPlexMono-SemiBold.ttf / IBMPlexMono-Medium.ttf |

Instalación local (sin red):

```bash
python3 .claude/skills/carrusel-stlabs/assets/install_fonts.py
cp /workspace/fonts/*.ttf /tmp/stlabs-fonts/
```
