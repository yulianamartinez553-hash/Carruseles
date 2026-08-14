# Manifiesto de fuentes — Historias frases de impacto

| Familia | Peso/estilo | Rol | Origen | Código de carga |
|---|---|---|---|---|
| Bebas Neue | 400 | Título display (claim) | skill `assets/fonts/BebasNeue-Regular.ttf` | `@font-face { font-family:'Bebas Neue'; src:url('file:///tmp/stlabs-fonts/BebasNeue-Regular.ttf') format('truetype'); }` |
| Lora | 600 italic | Línea puente editorial (muted) | skill `assets/fonts/Lora-Italic-Variable.ttf` | `@font-face { font-family:'Lora'; src:url('file:///tmp/stlabs-fonts/Lora-Italic-Variable.ttf') format('truetype'); font-style:italic; }` |
| Barlow Condensed | 500 | Apoyo / subtítulo | skill `assets/fonts/BarlowCondensed-Medium.ttf` | `@font-face { font-family:'Barlow Condensed'; src:url('file:///tmp/stlabs-fonts/BarlowCondensed-Medium.ttf') format('truetype'); font-weight:500; }` |
| IBM Plex Mono | 500 / 600 | Kicker NOTA · firma URL | skill `assets/fonts/IBMPlexMono-*.ttf` | `@font-face` Medium + SemiBold |
| Poppins ExtraBold | 800 | Disponible (stack) | skill `assets/fonts/Poppins-ExtraBold.ttf` | embebida en CSS del build |

Instalación: `python3 .claude/skills/carrusel-stlabs/assets/install_fonts.py` o `cp assets/fonts/*.ttf /tmp/stlabs-fonts/`.
