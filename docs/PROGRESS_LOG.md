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

## 2025-12-09 — 1D defected chain with twist: second null result

Model:
- 1D complex scalar on a ring with N = 256 sites.
- Nearest-neighbour coupling c = 1.0, mass m0 = 0.1.
- Single defect bond between sites N-1 and 0 with strength factor 0.5.
- Twist θ* applied on the defect bond only.

Experiment:
- Implemented Hermitian mass matrix M(N, c, m0, θ*, defect_strength) and
  computed ω_j(θ*) from its eigenvalues.
- Vacuum energy defined as E0(θ*) = 1/2 Σ_j ω_j(θ*).
- Scanned θ* ∈ [0, 2π] with 181 points.

Results:
- E0(θ*) ≈ 1.640787×10^2 for all θ*.
- ΔE0(θ*) = E0(θ*) - E0(0) remains at the ~10^{-13} level (numerical noise).
- Plots:
  - defected_1d_E0_vs_theta.png
  - defected_1d_deltaE_vs_theta.png

Interpretation:
- Even with a single weaker bond, the quadratic scalar vacuum energy on
  a closed ring remains effectively independent of the twist θ*.
- Together with the uniform-ring case, this suggests that in these
  highly symmetric quadratic models, θ* is spectrally trivial at the
  level of the summed vacuum energy.
- Nontrivial θ*-dependence may require:
  - different boundary conditions (open chains, mixed BC),
  - more structured defects or interactions,
  - or moving beyond the simple quadratic scalar vacuum (e.g. finite
    fillings, currents, or additional fields).

## 2025-12-09 — Nonlinear 3D toy universe with Origin Axiom constraint

Model:
- 3D complex scalar on a 16^3 periodic lattice (discrete T^3).
- Parameters: c = 1.0, m = 0.1, lambda = 1.0 (nonlinear self-coupling),
  dt = 0.005, n_steps = 500.
- Global amplitude A(t) = sum_n Phi_n(t).
- Mean-subtracted random initial field so that A(0) ≈ 0.
- Origin Axiom constraint: hard circle |A - A_ref| >= epsilon with
  epsilon = 0.05, A_ref = 0, theta_star = pi.

Experiments:
1. Unconstrained run:
   - |A(t)| remains very close to zero, drifting up to ~6×10^{-5}.
   - Energy E(t) shows mild oscillations around ~2.46 and is stable.

2. Constrained run (same initial data, same parameters):
   - After the first step, the global amplitude is projected to
     |A(t)| = epsilon = 0.05 and stays there.
   - The constraint fires at every time step (constraint_hits = 500).
   - Despite this, E(t) closely tracks the unconstrained evolution; the
     two energy curves are visually indistinguishable.

Outputs:
- toy_v0_1_nonlinear_no_constraint_epsilon005_meanzero.npz
- toy_v0_1_nonlinear_with_constraint_epsilon005_meanzero.npz
- toy_v0_1_nonlinear_compare_Amod_epsilon005_meanzero.png
- toy_v0_1_nonlinear_compare_energy_epsilon005_meanzero.png

Interpretation:
- In both the linear and nonlinear 3D scalar toy universes, the Origin
  Axiom constraint can enforce a minimal global amplitude |A| = epsilon
  without introducing any obvious energetic instability.
- The constraint behaves as intended: it forbids near-cancelling
  global configurations (|A| ≈ 0) while leaving the coarse-grained
  energy dynamics essentially unchanged, even when lambda != 0.
