# Phase 2 Claims → Artifacts Map (P2-S2)

This table is the canonical bridge:
CLAIMS.md ↔ paper sections ↔ figures ↔ run_id ↔ outputs/runs/<run_id>/meta.json

## Conventions
- `paper/figures/<FIG>.pdf` is the arXiv-packaged copy/symlink.
- `outputs/figures/<FIG>.run_id.txt` contains the canonical run_id.
- `outputs/runs/<RUN_ID>/meta.json` must exist and contain git hash + params + environment.

| Claim | Paper section | Figures (paper/figures) | Run-id sidecars (outputs/figures) | Run meta (outputs/runs) | Notes / Non-claims |
|------:|---------------|--------------------------|-----------------------------------|-------------------------|--------------------|
| C2.1  | sections/03_claim_C2_1_existence.tex | figA_mode_sum_residual.pdf | figA_mode_sum_residual.run_id.txt | runs/<run_id>/meta.json | Existence under constraint; NOT a physical constant prediction |
| C2.2  | sections/04_claim_C2_2_robustness.tex | figB_scaling_epsilon.pdf; figC_scaling_cutoff.pdf; figD_scaling_modes.pdf | figB_scaling_epsilon.run_id.txt; figC_scaling_cutoff.run_id.txt; figD_scaling_modes.run_id.txt | runs/<run_id>/meta.json | Robustness/suppression under sweeps; NOT universality |
| C2.3  | sections/05_claim_C2_3_frw_viability.tex | figE_frw_comparison.pdf | figE_frw_comparison.run_id.txt | runs/<run_id>/meta.json | FRW viability consistency test; NOT precision cosmology |
