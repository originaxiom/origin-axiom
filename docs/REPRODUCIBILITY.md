# Reproducibility (Repository-level)

## What we track vs regenerate

Tracked:
- canonical figure PDFs in `phase*/outputs/figures/`
- figure pointer files (`*.run_id.txt`, signatures, meta where needed)
- phase configs in `phase*/config/`
- papers in `phase*/paper/`
- claims/assumptions/repro docs in `phase*/`

Regenerated (not tracked):
- `**/outputs/runs/` (full run directories)
- `**/.snakemake/` (Snakemake cache)
- LaTeX build artifacts (`*.aux`, `*.log`, etc.)

## Environment (recommended)

Create one repo-level virtualenv and use it across phases:

1) Create venv
2) Install dependencies
3) Run phase Snakemake pipelines

(We can tighten this into a single lockfile later.)

## Canonical builds

### Phase 1
From repo root:
- `cd phase1 && snakemake -c 1 all`

### Phase 2
From repo root:
- `cd phase2 && snakemake -c 1 all`

### Phase 0
Phase 0 is governance + schemas. It should remain lightweight and deterministic.

