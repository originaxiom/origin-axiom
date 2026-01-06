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

## 2026-01-05 — Phase 3 baseline fixed-offset selected (b_PMNS = pi)
- Used discrete hypothesis sweep (theta_offset_sweep.csv) to select the baseline fixed offset.
- Winner: b_PMNS = pi (lowest chi2); locked into phase3/fit/targets.yaml as ansatz v1b-baseline-bpmns-pi.
- Added note: phase3/notes/offset_model_selection.md

## 2026-01-05 — Phase 3 baseline fixed-offset selected (b_PMNS = pi)
- Used discrete hypothesis sweep (theta_offset_sweep.csv) to select the baseline fixed offset.
- Winner: b_PMNS = pi (lowest chi2); locked into phase3/fit/targets.yaml as ansatz v1b-baseline-bpmns-pi.
- Added note: phase3/notes/offset_model_selection.md


## 2026-01-06 — Rung 1: Phase 3 Snakemake emits canonical PDF

- Updated `phase3/workflow/Snakefile` so that `build_phase3_paper_pdf` writes both:
  - `phase3/outputs/paper/phase3_paper.pdf` (staging)
  - `phase3/artifacts/origin-axiom-phase3.pdf` (canonical)
- Updated `rule all` to require the canonical artifact at `phase3/artifacts/origin-axiom-phase3.pdf`.
- Ran `snakemake -s phase3/workflow/Snakefile -c 1 build_phase3_paper_pdf` and confirmed both `phase3/outputs/paper/phase3_paper.pdf` and `phase3/artifacts/origin-axiom-phase3.pdf` were produced with matching sizes.
- Next: align global docs and Phase 3 paper text with this canonical artifact and existing claim IDs as defined in `phase3/CLAIMS.md`.


## 2026-01-06 — Rung 3: Phase 3 paper reproducibility appendix

- Expanded `phase3/paper/appendix/B_reproducibility.tex` to summarize the Phase 3 gate levels (A/B/C),
  the Snakemake entry point, and the paper bundle location, while keeping `phase3/REPRODUCIBILITY.md`
  as the authoritative contract.
- No changes to claim IDs (`C3.1`–`C3.3`) or physics content; this is purely an exposition improvement
  for reproducibility and audit clarity.


## 2026-01-06 - Rung 5: Phase 3 gate B (full rebuild + bundle verification)

- Ran `bash scripts/phase3_gate.sh --level B` to perform a full Phase 3 rebuild via Snakemake
  and verify the Phase 3 paper bundle.
- Confirmed that `phase3/outputs/tables/`, `phase3/outputs/figures/`, `phase3/artifacts/origin-axiom-phase3.pdf`,
  and `phase3/outputs/paper_bundle/run_index.json` + `bundle_manifest.json` were present and consistent.
- No changes to the ansatz, targets, or claim IDs; this rung only records that Gate B passed on this
  repository state.


## 2026-01-06 - Rung 6: Phase 0 ledger sees Phase 3 theta_filter

- Created a symlink `phase0/phase_outputs/phase_03_theta_filter.json` pointing to
  `../phase3/outputs/theta_filter/phase_03_theta_filter.json` so that the Phase 0 ledger
  can consume the Phase 3 theta filter without copying the file.
- This keeps Phase 0 corridor aggregation reading filters from a single phase_outputs/
  namespace while preserving Phase 3 as the source of truth for the Phase 3 theta filter.
- (Planned verification) Run:
  - `cd phase0 && python scripts/phase0_ledger.py update`
  - `cd phase0 && python scripts/phase0_ledger.py status`
  to confirm the corridor now includes Phase 3 as `phase_03_theta_filter.json`.
