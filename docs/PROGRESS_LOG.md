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
