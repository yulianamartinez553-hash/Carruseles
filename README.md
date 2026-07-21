# Carruseles STLabs

Creación de carruseles de Instagram para la marca Sebastián García (STLabs).

## Instalación

```bash
pip install -r requirements.txt
playwright install chromium
```

## Memoria operativa

Antes de cada carrusel:

```bash
python stlabs_memory.py suggest
python stlabs_memory.py status
python stlabs_memory.py list
python stlabs_memory.py list --estado publicado
```

Después de publicar:

```bash
python stlabs_memory.py feedback <id> --estado publicado --notas "opcional"
```

Plantillas de copy:

```bash
python stlabs_memory.py plantilla educativo ACCION=automatizar DOLOR=perder_leads N=1 TITULO=Setup
```

Demo sin Playwright:

```bash
python scripts/demo_memory.py
```

## Flujo de trabajo

1. Consultar memoria (`suggest`)
2. `write_html()` + `render()` con [stlabs_kit.py](stlabs_kit.py)
3. `package(build_dir, out_name, meta={...})` — registra en `resultados/<id>/` e `historial/`

Campos obligatorios en `meta`: `fondo`, `familia_visual`, `origen`, `slides`, `keyword_portada`.

## Dónde quedan los carruseles

Todos los carruseles viven en la carpeta [`resultados/`](resultados/) de la rama `main`.
**No se crea una rama por carrusel:** cada creación es una carpeta numerada secuencial
(`resultados/carrusel-1`, `resultados/carrusel-2`, …). El número lo asigna `package()`
automáticamente (id por defecto `carrusel-N`); para fijarlo manualmente pasá `meta["id"]`.
Los PNGs entregables se versionan en `main`; los `.zip` se ignoran (ver `.gitignore`).

## Documentación

- **Configuración visual predeterminada (fuente de verdad):** [sistema-carrusel-stlabs.json](sistema-carrusel-stlabs.json) — reglas permanentes y obligatorias (tamaños, pesos, colores, jerarquías, fondos, elementos, salida y caption) que se aplican a todos los slides de cualquier carrusel. Copia para el skill en [.claude/skills/carrusel-stlabs/references/00-sistema-visual-carrusel.json](.claude/skills/carrusel-stlabs/references/00-sistema-visual-carrusel.json).
- Sistema de diseño: [SISTEMA-DISENO-CARRUSELES-STLABS.md](SISTEMA-DISENO-CARRUSELES-STLABS.md)
- Plan de memoria: [docs/plans/2026-07-01-memoria-operativa-carruseles.md](docs/plans/2026-07-01-memoria-operativa-carruseles.md)

## Tests

```bash
python -m pytest tests/ -v
```
