
## Phase 3A — Flavor-sector θ-filter (experimental add-on, archived negative result)


This module was originally implemented under `phase3/` as a flavor-sector
calibration add-on. It exports a θ-filter derived from CKM/PMNS snapshots and
feeds into the Phase 0 corridor ledger. In its locked configuration, the
Phase 0 ledger reports an empty combined corridor once this filter is applied,
so it is treated as a negative result for that ansatz/target combination.

The full implementation and its paper are now archived under:
`experiments/phase3_flavor_v1/`.

This experiment is **not** the "Phase III: principled mechanism" described in
the Phase 0 contracts; `phase3/` is reserved for that mechanism.


| Claim ID | Short claim | Artifact(s) | Script(s) | Run ID(s) | Status |
|---|---|---|---|---|---|
| C3.1 | θ fit reproducible (within declared 1-θ ansatz) | `phase3/outputs/tables/theta_fit_summary.csv`; `phase3/outputs/tables/theta_fit_summary.meta.json`; `phase3/outputs/tables/theta_fit_diagnostics.json`; `phase3/outputs/figures/fig1_theta_fit_diagnostics.pdf` | `phase3/src/phase3/fit/run_fit.py`; `phase3/fit/targets.yaml` | bundle-manifested | **bootstrap placeholder** |
| C3.2 | θ injection → Δρ_vac(θ) curve (conditional on Phase 2 mechanism hook) | `phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.pdf`; `phase3/outputs/figures/fig2_delta_rho_vac_vs_theta.meta.json` | `phase3/src/phase3/inject/run_injection.py` | bundle-manifested | **bootstrap placeholder** |
| C3.3 | Falsifiability conditions documented | Phase 3 paper Sec 4 + Appendix | Phase 3 paper sources | n/a | planned |
