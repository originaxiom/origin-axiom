# Phase 0 – Reproducibility

Phase 0 is mostly governance and documentation, but it still has concrete artifacts
that must be reproducible.

## Artifacts

- `phase0/paper/main.tex` – source of the Phase 0 paper.
- `phase0/artifacts/phase0-paper.pdf` – compiled PDF (canonical).
- `phase0/phase_outputs/` – theta filters and corridor JSON files.
- `phase0/schemas/` – JSON Schemas for filters and corridors.
- `phase0/scripts/` – scripts that generate or update Phase 0 artifacts.

## Environment

Phase 0 reuses the repo-level Python environment described in `README.md`
and `docs/REPRODUCIBILITY.md`. No heavy numerical dependencies are required.

## How to rebuild Phase 0 artifacts

1. **Clone and set up the environment**  
   See the root `README.md` for instructions.

2. **Rebuild the Phase 0 paper**

   ```bash
   cd phase0/paper
   latexmk -pdf main.tex