# Origin Axiom - Simulation Log

This file records all simulations/experiments in a consistent format.

Use the template below for each new entry.

---

## Template

```markdown
## [SIM-YYYYMMDD-XX] short_name

- Date:
- Code:
- Notebook:
- Parameters:
- Question:
- Output files:
- Sanity checks:
- Result summary (1-3 sentences):
- Next questions:
```

---

## [SIM-2025XXXX-C01] toy_universe_compare_constraint

- Date:
- Code: `src/run_toy_universe_compare_constraint.py`
- Notebook: `notebooks/03_compare_constraint_effect.py`
- Parameters:
  - 3D complex scalar field on periodic lattice
  - Two runs: without constraint, with non-cancellation bound |A| >= epsilon
  - Example: epsilon ~= 0.05, mean-zero initial data
- Question:
  - Does imposing |A| >= epsilon on a global amplitude A(t) keep |A| away from 0
    while preserving sensible energy behaviour?
- Output files (expected):
  - `data/processed/toy_v0_1_compare_Amod_epsilon005_meanzero.png`
  - `data/processed/toy_v0_1_compare_energy_epsilon005_meanzero.png`
- Sanity checks:
  - With constraint: |A(t)| never dips below epsilon (floor behaviour)
  - Without constraint: |A(t)| spends most time near 0
  - Energy E(t) remains stable and comparable in both runs
- Result summary (1-3 sentences):
- Next questions:

---

## [SIM-2025XXXX-C02] constraint_scan_eps_lambda

- Date:
- Code: `src/run_toy_universe_constraint_scan.py`
- Notebook: `notebooks/05_constraint_scan_analysis.py`
- Parameters:
  - 3D complex scalar field on periodic lattice
  - Scan over non-cancellation scale epsilon and self-interaction lambda
- Question:
  - How do epsilon and lambda control (a) the typical non-cancellation scale <|A|>,
    and (b) the activity level of the constraint (hit counts)?
- Output files (expected):
  - `data/processed/constraint_scan_Amean_vs_eps_lambda*.png`
  - `data/processed/constraint_scan_hits_vs_eps_lambda*.png`
- Sanity checks:
  - <|A|> increases with epsilon (epsilon sets a non-cancellation floor)
  - Hit counts behave smoothly over (epsilon, lambda) and energy remains stable in
    physically interesting regions
- Result summary (1-3 sentences):
- Next questions:



## [SIM-2025XXXX-T01] 1d_twisted_vacuum_scan

- Date: 2025-12-10
- Code: `src/run_1d_twisted_vacuum_scan.py`
- Notebook: `notebooks/02_1d_twisted_analysis.py` (to be created; see below)
- Parameters:
  - N = 256 sites, c = 1.0, m0 = 0.1
  - 1D scalar chain with twisted boundary condition (angle theta_star)
  - theta_star scanned over [0, 2π] (as in script)
- Question:
  - Does the total vacuum energy depend nontrivially on the twist angle
    theta_star, or is it numerically flat (null result)?
- Output files (expected):
  - `data/processed/twisted_1d_vacuum_scan.npz`
  - PNG(s) of E0(theta_star) vs theta_star
- Sanity checks:
  - Printed values show E0(theta_star) = 1.639690e+02 for all sampled
    theta_star
  - Any plotted E0(theta_star) curve should be flat within numerical error
- Result summary (1–3 sentences):
  - The vacuum energy of the twisted 1D scalar chain is numerically constant
    across theta_star. No anomalous twist dependence is observed to within
    our numerical precision.
- Next questions:
  - Repeat the same analysis with a defect to test robustness.
  - Use this as a baseline null model for any future claims about twist- or
    phase-dependent vacuum structure.




## [SIM-2025XXXX-T02] 1d_defected_vacuum_scan

- Date: 2025-12-10
- Code: `src/run_1d_defected_vacuum_scan.py`
- Notebook: `notebooks/02b_1d_defected_twist_analysis.py`
- Parameters:
  - N = 256 sites, c = 1.0, m0 = 0.1
  - Single defect bond with defect_strength = 0.5
  - theta_star scanned over [0, 2π] with n_theta = 181
- Question:
  - Does introducing a defect bond produce any nontrivial theta_star
    dependence in the total vacuum energy, or is it still numerically flat?
- Output files:
  - `data/processed/defected_1d_vacuum_scan.npz`
  - `data/processed/defected_1d_E0_vs_theta.png`
  - `data/processed/defected_1d_deltaE_vs_theta.png`
- Sanity checks:
  - Reported min(E0) = max(E0) = 1.640787e+02 across all theta_star
  - ΔE(theta_star) fluctuates only at the ~10^-13 level around zero
    (numerical noise)
  - Plots show a flat E0(theta_star) curve and a tiny, structureless
    ΔE(theta_star)
- Result summary (1–3 sentences):
  - Even with a defect bond, the vacuum energy remains independent of
    theta_star within numerical precision. The defect does not introduce any
    meaningful twist dependence; ΔE(theta_star) is at the level of
    10^-13, consistent with rounding noise.
- Next questions:
  - Treat this as a robustness check that our twisted boundary setup does
    not secretly encode a nontrivial phase-dependence in the vacuum.
  - Use these 1D null results as a constraint on any stronger phi/phase
    claims in higher-dimensional or more complex models.




## [SIM-2025XXXX-M01] mode_spectrum_1d_constraint

- Date: 2025-12-10
- Code: `src/run_mode_spectrum_with_constraint.py`
- Notebook: `notebooks/06_mode_spectrum_analysis.py`
- Parameters:
  - N = 256, dt = 0.05, steps = 4096
  - m0 = 0.1
  - k_index = 1
  - initial cosine amplitude = 1e-3
  - non-cancelling scale epsilon = 1e-3
- Question:
  - Does imposing a small non-cancelling bound on the global mean field
    significantly modify the oscillation frequency omega(k) of a chosen mode?
- Output files:
  - `data/processed/mode_spectrum_1d.npz`
  - `data/processed/mode_spectrum_timeseries.png`
  - `data/processed/mode_spectrum_power.png`
- Sanity checks:
  - Time series for free vs constrained runs overlap almost perfectly.
  - Power spectra share the same dominant peak.
  - Extracted omega_free and omega_constrained are equal within numerical
    tolerance and both are reasonably close to the linear-theory omega(k).
- Result summary (1–3 sentences):
  - For k_index = 1 and epsilon = 1e-3, the non-cancelling constraint on the
    global mean field does not visibly distort the mode dispersion: the
    extracted frequencies for free and constrained runs coincide to within
    numerical precision. The basic lattice Klein–Gordon spectrum remains
    intact.
- Next questions:
  - Explore other k indices and larger epsilon to see when the constraint
    begins to significantly shift omega(k).
  - Move from linear modes to localized lumps to search for proto-particle
    structures under the constraint.



