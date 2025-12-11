## Δα(θ) scans — 2025-12-11

Common setup:
- Script: lattice_theta/run_delta_alpha_theta_scan.py
- Weight power: p = 6.0
- Lattice: 4D integer, origin excluded
- Fit model: S_R ≈ A + B/R, A ≡ Δα(θ)

### Wide scan (theta_zoom_R10)
- R_max = 10, R_fit_min = 5
- θ range: [2.20, 2.80], n_theta = 25
- Rough minimum: θ* ≈ 2.62 ± 0.05 rad
- Δα(θ*) ≈ −8.79 ± 0.05
- Files:
  - data/processed/lattice_theta/delta_alpha_theta_zoom_R10.csv
  - figures/lattice_theta/delta_alpha_theta_zoom_R10.png

### Medium scan (theta_core_R14)
- R_max = 14, R_fit_min = 7
- θ range: [2.50, 2.65], n_theta = 13
- Rough minimum: θ* ≈ 2.60 ± 0.05 rad
- Δα(θ*) ≈ −8.76 ± 0.02
- Files:
  - data/processed/lattice_theta/delta_alpha_theta_core_R14.csv
  - figures/lattice_theta/delta_alpha_theta_core_R14.png

### High-R scan (theta_core_R16)
- R_max = 16, R_fit_min = 8
- θ range: [2.58, 2.63], n_theta = 21
- Flat minimum around: θ* ≈ 2.59–2.60 rad
- Representative value: Δα(θ*) ≈ −8.781 ± 0.010
- Files:
  - data/processed/lattice_theta/delta_alpha_theta_core_R16.csv
  - figures/lattice_theta/delta_alpha_theta_core_R16.png

All three runs are consistent with a broad minimum near θ* ≈ 2.6 rad.
