[2025-12-11] 4D lattice Δα(θ) preliminary scans (θ-agnostic)

1) Coarse θ-grid:
   - Script: src/lattice_theta/run_delta_alpha_theta_scan.py
   - Settings: p = 6.0, R_max = 12, R_fit_min = 6
   - θ-range: 0.5–3.5, n_theta = 16 (uniform grid)
   - Key result: Δα(θ) is convex and crosses from positive to negative,
     with a broad minimum in the 2.2–2.8 region.

   Files:
   - data/processed/lattice_theta/delta_alpha_theta_grid_R12.csv
   - figures/lattice_theta/delta_alpha_theta_grid_R12.png

2) Zoomed θ-grid around minimum:
   - Same script/settings (p = 6.0, R_max = 12, R_fit_min = 6)
   - θ-range: 2.2–2.8, n_theta = 25 (uniform grid)
   - Result: smooth convex minimum near
       θ* ≈ 2.576 ± 0.01
       Δα(θ*) ≈ -8.78  (from simple quadratic fit around the minimum)
   - This θ* is obtained without bias toward any special constant
     (no φ, φ^φ, π, etc. used in the scan definition).

   Files:
   - data/processed/lattice_theta/delta_alpha_theta_zoom_R12.csv
   - figures/lattice_theta/delta_alpha_theta_zoom_R12.png

Next planned steps:
- Stability check: repeat zoom scan at a different R_max (e.g. 10 or 14)
  to test θ* stability.
- Feed θ* into 1D cancellation chain residual scans for an independent
  test of cancellation behaviour.
