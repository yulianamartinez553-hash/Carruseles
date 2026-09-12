# Manifiesto de fuentes — Los procesos no son lineales

| Tipografía | Peso | Rol | Origen | Carga |
|---|---|---|---|---|
| Inter | 800 / Bold | Título display | apt / macOS fonts (`/usr/share/fonts/truetype/macos/Inter-Bold.ttf`) | `@font-face` file:// en HTML del build |
| Inter | 700 / Bold | Labels del gráfico | idem | idem |
| Inter | 600 / SemiBold | Subtítulo en pill | Inter-Bold.ttf como 600/800 fallback | idem |
| IBM Plex Mono | 500 / Medium | Handle + footer | `/workspace/fonts/IBMPlexMono-Medium.ttf` (kit STLabs) | embebida base64 vía `stlabs_kit.package` / FONT_FACES |

Instalación local Inter (si falta):
```bash
# ya presente en el entorno cloud:
ls /usr/share/fonts/truetype/macos/Inter-*.ttf
```

IBM Plex Mono:
```bash
python .claude/skills/carrusel-stlabs/assets/install_fonts.py
```
