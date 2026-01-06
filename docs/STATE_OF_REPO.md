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
- Phase 3: flavor-sector calibration add-on (CKM/PMNS-based theta filter; corridor-compatible add-on to Phase 2; no OA proof).

## Reproducibility entry points
- Phase 0: compile paper in `phase0/paper/` (see `phase0/REPRODUCIBILITY.md` if present).
- Phase 1: `cd phase1 && snakemake -c 1 all`
- Phase 2: `cd phase2 && snakemake -c 1 all`
- Phase 3: snakemake -s phase3/workflow/Snakefile -c 1 all

## Claims indexing
- Global claims map: `docs/CLAIMS_INDEX.md`
- Phase 0 method claims: (to be formalized as P0-Cxx in Phase 0 claim ledger)
- Phase 1 physics claims: `phase1/CLAIMS.md`
- Phase 2 physics claims: `phase2/CLAIMS.md`
- Phase 3 physics claims: `phase3/CLAIMS.md`

