# Phase 3 Progress Log

## 2026-01-05
- Bootstrapped Phase 3 contract docs (scope/non-claims/assumptions/approx contract/claims table).
- Added Phase 3 gate skeleton and workflow skeleton.
- Next: implement θ-fit runner + injection runner; generate first paper bundle.

## 2026-01-05 — Phase 3 θ-fit contract lock (bootstrap placeholder)
- Added `phase3/fit/ANSATZ_CONTRACT.md` + `phase3/fit/targets.yaml` (placeholder_mode=true).
- Upgraded `run_fit.py` to be contract-driven (YAML targets, provenance, diagnostics).
- Promoted fit diagnostics + meta to first-class artifacts in Snakemake + paper bundle.
- Updated CLAIMS_TABLE to point to the new artifacts.
