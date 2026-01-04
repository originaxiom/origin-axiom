# Reproducibility entrypoint

## Stage 0 baseline freeze
The repository baseline corresponding to the initial clean-build freeze is tagged:

- `stage0-freeze-2026-01-03`

This tag guarantees:
- Phase 0 + Phase 1 papers compile cleanly,
- PDFs are committed as convenience artifacts,
- LaTeX build artifacts are ignored (not tracked),
- progress logs reflect the freeze state.

## Canonical paper build command
From repo root:

- `./scripts/build_papers.sh`

Expected outputs:
- `phase0/paper/main.pdf`
- `phase0/paper/appendices.pdf`
- `phase1/paper/main.pdf`
