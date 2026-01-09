# Repository State (Single Source of Truth)

This document summarizes the current phase status, canonical artifacts, and reproducibility entry points.

## Canonical policy
- Canonical PDFs live in `phase*/artifacts/`.
- Canonical figures live in `phase*/outputs/figures/`.
- Ephemeral runs are not tracked (e.g., `**/outputs/runs/`, `.snakemake/`).

## Phase status (high-level)
- Phase 0: governance/specification layer (no physics claims).
- Phase 1: toy-domain existence/robustness/scaling claims.
- Phase 2: mode-sum model + bounded FRW-style viability checks.
- Phase 3: mechanism module (toy non-cancellation floor + binding diagnostics;
  no flavor calibration in canonical `phase3/`).

## Stage 2 status (diagnostic belts)
- Stage 2 is in progress under `stage2/` and remains non-canonical:
  `frw_corridor_analysis`, `mech_measure_analysis`,
  `joint_mech_frw_analysis`, `frw_data_probe_analysis`.

## Reproducibility entry points
- Phase 0: compile paper in `phase0/paper/` (see `phase0/REPRODUCIBILITY.md` if present).
- Phase 1: `cd phase1 && snakemake -c 1 all`
- Phase 2: `cd phase2 && snakemake -c 1 all`
- Phase 3: snakemake -s phase3/workflow/Snakefile -c 1 all

## Claims indexing
- Global claims map: `docs/CLAIMS_INDEX.md`
- Phase 0 method claims: `phase0/CLAIMS.md`
- Phase 1 physics claims: `phase1/CLAIMS.md`
- Phase 2 physics claims: `phase2/CLAIMS.md`
- Phase 3 physics claims: recorded in the Phase 3 paper appendix
  (no standalone `phase3/CLAIMS.md` at this rung)
