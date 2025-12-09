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

## 2025-12-09 — 3D toy universe: enforcing a minimal global amplitude

- Updated Origin Axiom constraint to use a gentle additive shift of Φ instead of a global rescale.
- Constructed mean-subtracted initial field so that the unconstrained run has nearly perfect global cancellation: |A(0)| ~ 10^{-16}.
- Used ε = 0.05 and ran `run_toy_universe_compare_constraint.py`:

  - No-constraint run:
    - |A(t)| stays ~10^{-16} (global cancellation persists).
    - E(t) remains in a narrow band around 2.46 × 10^{-2}.
    - constraint_hits = 0.

  - With Origin Axiom constraint:
    - |A(t)| is pinned at |A| = ε = 0.05 throughout the evolution.
    - E(t) closely tracks the unconstrained energy (same values to plotted precision).
    - constraint_hits = 501 (one at t=0 plus one per time step to keep |A| on the ε-circle).

- Plots:
  - `toy_v0_1_compare_Amod_epsilon005_meanzero.png`: |A(t)| with and without constraint (blue ~ 0, orange = 0.05).
  - `toy_v0_1_compare_energy_epsilon005_meanzero.png`: E(t) for both runs lying almost on top of each other.

Interpretation:
- The Origin Axiom constraint can be implemented as a gentle global projection that forbids the universe from entering a cancelling configuration (|A| ≈ 0) while leaving the local dynamics and total energy essentially unchanged.

## 2025-12-09 — 3D toy universe: enforcing a minimal global amplitude

- Updated Origin Axiom constraint to use a gentle additive shift of Φ instead of a global rescale.
- Constructed mean-subtracted initial field so that the unconstrained run has nearly perfect global cancellation: |A(0)| ~ 10^{-16}.
- Used ε = 0.05 and ran `run_toy_universe_compare_constraint.py`:

  - No-constraint run:
    - |A(t)| stays ~10^{-16} (global cancellation persists).
    - E(t) remains in a narrow band around 2.46 × 10^{-2}.
    - constraint_hits = 0.

  - With Origin Axiom constraint:
    - |A(t)| is pinned at |A| = ε = 0.05 throughout the evolution.
    - E(t) closely tracks the unconstrained energy (same values to plotted precision).
    - constraint_hits = 501 (one at t=0 plus one per time step to keep |A| on the ε-circle).

- Plots:
  - `toy_v0_1_compare_Amod_epsilon005_meanzero.png`: |A(t)| with and without constraint (blue ~ 0, orange = 0.05).
  - `toy_v0_1_compare_energy_epsilon005_meanzero.png`: E(t) for both runs lying almost on top of each other.

Interpretation:
- The Origin Axiom constraint can be implemented as a gentle global projection that forbids the universe from entering a cancelling configuration (|A| ≈ 0) while leaving the local dynamics and total energy essentially unchanged.
