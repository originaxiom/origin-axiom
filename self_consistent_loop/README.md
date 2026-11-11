# Self-Consistent Loop (`Phi(X*) = X*`): Phases 1–3 & Phase 4 Plan

Clean-room (`0 of 19` empirical inputs) pre-registered implementations, outputs, unit tests, and AST-isolated zero-import referee suites testing the self-consistent geometric loop across Phases 1–3, together with the Phase 4 design specification.

## Directory Layout

- `self_consistent_loop_phi/` — **Phase 1:** Self-consistent Sol/anisotropic torus & modular feedback fixed-point engine (`PREREGISTRATION_PLAN.md`, `SEAL_SHA256.txt`, solver, referee, and tests).
- `cusped_3d_loop_phase2/` — **Phase 2:** 3D cusped hyperbolic Mostow-rigidity, Margulis-throat Laplacian, and chiral-boundary index engine (`PREREGISTRATION_PHASE2.md`, `SEAL_SHA256.txt`, solver, referee, and tests).
- `relational_yukawa_phase3/` — **Phase 3:** Relational weak-compass quotient (`0.0` enantiomer collapse), 2-component coupled spin-flux Klein-four palindrome protection audit, 3D hyperbolic trilinear Yukawa & Jarlskog CP theorem (`(6)` vs. chiral irreversible `[5, 1, 2, 2]`), and unrigged $E_8$ instanton tadpole audit (`PREREGISTRATION_PHASE3.md`, `SEAL_SHA256.txt`, solver, referee, and tests).
- `reports/` — Phase 1–3 comprehensive reports and the Phase 4 implementation plan (`phase4_vacuum_cap_lepton_plan.md`).

## Reproducing All Suites & Zero-Import Referees

```bash
# Phase 1
cd self_consistent_loop/self_consistent_loop_phi
python3 -m unittest discover -s tests -v

# Phase 2
cd ../cusped_3d_loop_phase2
python3 -m unittest discover -s tests -v

# Phase 3
cd ../relational_yukawa_phase3
python3 -m unittest discover -s tests -v
```
