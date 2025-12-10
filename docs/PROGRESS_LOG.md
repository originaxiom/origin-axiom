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

## 2025-12-10 — Volume scan of toy universe (linear regime)

Scripts:
- `src/run_toy_universe_volume_scan.py`
- `notebooks/06_volume_scan_analysis.py`

Setup:
- 3D scalar lattice on an N×N×N 3-torus with periodic BC.
- Mass m = 0.1, c = 1, dt = 0.005, n_steps = 500.
- Lattice sizes: N ∈ {16, 24, 32}.
- Quartic coupling: λ ∈ {0, 1}.
- Origin Axiom parameters: θ* = π (bookkeeping only), ε = 0.05, A_ref = 0.
- Initial conditions: small complex Gaussian noise with mean explicitly subtracted, so A(0) ≈ 0.

Result summary (time-averaged energy density ρ̄ = ⟨E(t)/V⟩):
- For all N and both λ = 0, 1:
  - ρ̄_no ≈ 6.0×10⁻⁶,
  - Δρ̄ = ρ̄_with − ρ̄_no is O(10⁻⁸),
  - `constraint_hits_with = 0` (constraint never activates).
- Δρ̄ fluctuates in sign with N and is essentially identical for λ = 0 and λ = 1.

Interpretation:
- In this scan the Origin Axiom constraint is effectively inactive; the “with” and “without” runs follow the same dynamics.
- The nonzero Δρ̄ values therefore reflect numerical / stochastic differences between runs rather than a physical non-cancelling energy shift.
- This gives us a useful noise baseline (~10⁻⁸ in ρ̄) and confirms that, when the constraint is off, the toy model behaves like a standard weakly excited scalar field on a 3-torus.

Next:
- Focus subsequent scans on parameter regimes where the constraint is known to fire frequently (nonzero `constraint_hits`) so that any measured Δρ̄ cannot be attributed to pure numerical noise.

## 2025-12-10 — Two-field toy model with composite non-cancelling constraint

Setup:
- Implemented `TwoFieldToyUniverse` (φ and χ) with quartic self-couplings λ_φ = λ_χ = 1 and no cross-coupling (g = 0).
- Defined composite field ψ = φ + χ and applied the Origin Axiom constraint only to ψ:
  - hard floor |A_ψ(t)| ≥ ε with ε = 0.05,
  - same lattice + timestep as previous 3D toy runs (N = 16, dt = 0.005, n_steps = 500).

Results:
- No-constraint run:
  - |A_ψ(t)| stays ~10^{-11}, i.e. φ and χ almost perfectly cancel globally.
  - Energy E(t) hovers around ~4.93×10^{-2} with small oscillations.
  - Constraint hits = 0 by construction.
- With-constraint run:
  - As soon as the evolution tries to keep |A_ψ| ≈ 0, the constraint activates and pins |A_ψ(t)| = ε for the rest of the simulation.
  - Total energy jumps to ~7.5×10^{-2} and shows a mild drift upward, but remains well-behaved.
  - ψ-constraint hit counter = 500 out of 500 steps: the axiom is “on” throughout the evolution.

Interpretation:
- This is the first explicit demo of a composite non-cancelling field:
  - φ and χ can almost cancel individually, but the constrained combination ψ = φ + χ is forbidden from vanishing.
  - The system pays an energy cost to maintain a minimal global amplitude in ψ.
- Conceptually, this mirrors the single-field toy-universe behaviour, but now in a larger field space:
  - The axiom acts on a chosen linear combination (ψ) rather than on a single bare field.
  - This is the minimal prototype for a “cancellation system”: many underlying degrees of freedom can interfere and almost cancel, yet a protected composite mode cannot be driven to zero.

Artifacts:
- Code: `src/two_field_lattice.py`, `src/run_two_field_compare_constraint.py`
- Analysis: `notebooks/07_two_field_analysis.py`
- Figures:
  - `figures/two_field_compare_Apsi.png`
  - `figures/two_field_compare_energy.png`
