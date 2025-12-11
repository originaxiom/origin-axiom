# Origin Axiom Progress Log

Short, human-readable notes after each meaningful run or milestone.
Think of this as the lab notebook for the repo.

---

## 2025-12-09 — Initial scalar universe + constraint + 1D twist

- Set up repo, docs (`01_origin_axiom`, `02_research_program`, `03_toy_universe_v0_1`).
- Implemented 3D scalar toy universe on a discrete 3-torus with leapfrog integration.
- Added:
  - energy functional `ScalarToyUniverse.energy()`,
  - Origin Axiom hard constraint on global amplitude `A(t)`,
  - demo `run_toy_universe_with_constraint.py` logging `|A(t)|` and `E(t)` to `.npz`.
- Implemented 1D twisted scalar model:
  - twisted BC: $\Phi_{n+N} = e^{i\theta_\ast}\Phi_n$,
  - computed vacuum spectrum and $E_0(\theta_\ast)$,
  - result: for a perfectly symmetric ring, $E_0(\theta_\ast)$ is numerically flat
    (global twist is a relabeling at this level).

Data files:
- `data/processed/toy_v0_1_theta_pi_constraint.npz`
- `data/processed/twisted_1d_vacuum_scan.npz`

Notes:
- 3D model: constraint keeps $|A(t)|$ away from zero while energy stays ~constant.
- 1D model: good null result; shows we need boundaries/defects to make $\theta_\ast$ matter for $E_0$.

## 2025-12-09 — First toy-universe and 1D twist results

3D toy universe (θ* = π, ε = 0.01, small random initial field):
- Ran `run_toy_universe_with_constraint.py` and `run_toy_universe_compare_constraint.py`.
- For these parameters, the Origin Axiom constraint did not activate:
  - with and without constraint, |A(t)| curves are nearly identical,
  - energy E(t) is also almost identical in both runs and approximately conserved.
- Interpretation: with small initial noise and ε = 0.01, the global amplitude never approaches the forbidden region near A ≈ 0, so the constraint is effectively inactive. Good numerical sanity check.

1D twisted scalar model:
- Implemented `toy_universe_1d` with twisted BC Φ_{n+N} = e^{i θ*} Φ_n.
- Computed vacuum spectrum and E0(θ*) for N=256, c=1.0, m0=0.1.
- Result: E0(θ*) is numerically flat as a function of θ*; ΔE0(θ*) is at the ~10^{-13} level (pure numerical noise).
- Interpretation: on a perfectly symmetric ring, a global twist just relabels modes and leaves the total vacuum energy invariant. Nontrivial θ* effects require boundaries, defects, or extra structure.

### 2025-12-11 – 4D lattice Δα(θ) scans (Point B: θ*-agnostic check)

**Scripts**

- \`src/lattice_theta/lattice_delta_alpha.py\`
- \`src/lattice_theta/run_delta_alpha_theta_scan.py\`

**Global θ scan (0 → 2π)**

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 0.0 --theta-max 6.0 --n-theta 61 --R-max 12 --R-fit-min 6 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_global_R12_p6.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_global_R12_p6.png\`
- Result:
  - Smooth, non-flat Δα(θ) curve with a single broad minimum in the neighbourhood of θ ≈ 2.6.
  - This is a **θ*-agnostic** 4D lattice analogue of the earlier 1D twisted-chain checks.

**Focused scan around the minimum**

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 2.3 --theta-max 2.9 --n-theta 61 --R-max 16 --R-fit-min 8 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_min_focus.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_min_focus.png\`
- Result:
  - Parabolic minimum around θ ≈ 2.59 with Δα ≈ -8.78.
  - Error bars from the A + B/R fit at R ≥ 8 are ~1×10⁻², so the minimum location is stable at the ~10⁻³–10⁻² level.

**High-R confirmation of θ\*** (zoomed + higher cutoff)

- Command:
  - \`PYTHONPATH=src python3 -m lattice_theta.run_delta_alpha_theta_scan --theta-min 2.55 --theta-max 2.63 --n-theta 61 --R-max 24 --R-fit-min 12 --p 6.0\`
- Outputs:
  - \`data/processed/lattice_theta/delta_alpha_theta_star_R24.csv\`
  - \`figures/lattice_theta/delta_alpha_theta_star_R24.png\`
- Result:
  - Minimum confirmed near θ* ≈ 2.595 with Δα(θ*) ≈ -8.77.
  - Increasing R_max to 24 and fitting over R ≥ 12 does **not** shift the minimum significantly, only tightens σ_A.
- Interpretation:
  - This is our cleanest numerical estimate of the “preferred” twist angle in the 4D lattice Δα(θ) construction.
  - Next step (Point B → C): compare **cancelling vs non-cancelling** implementations at this θ* and tie back into the Origin Axiom (“universe avoids exact cancellation but can sit near a structured non-zero Δα”).


## 2025-12-11 — 4D lattice θ-scan and θ★ refinement

We scanned the 4D lattice remainder Δα(θ) over 0–2π and then zoomed in on the global minimum.

- Global scan: `R_max = 12`, `p = 6.0`, `R_fit_min = 6`, `n_theta = 61`  
  → `data/processed/lattice_theta/delta_alpha_theta_global_R12_p6.csv`  
  → `figures/lattice_theta/delta_alpha_theta_global_R12_p6.png`

- Core scan around the dip: `R_max = 20`, `R_fit_min = 7`, `θ ∈ [2.3, 2.9]`  
  → confirms a pronounced minimum near **θ ≈ 2.59 rad**.

- High-R refinement: `R_max = 24`, `R_fit_min = 12`, `θ ∈ [2.55, 2.63]`  
  → `data/processed/lattice_theta/delta_alpha_theta_star_R24.csv`  
  → `figures/lattice_theta/delta_alpha_theta_star_R24.png`  
  → stable minimum at **θ★ ≈ 2.595 ± 0.01 rad**, with  
    **Δα(θ★) ≈ −8.77 ± 0.01**.

This θ★ is now our reference angle for comparing cancelling vs non-cancelling dynamics on the same 4D lattice.

