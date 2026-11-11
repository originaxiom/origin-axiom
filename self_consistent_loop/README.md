# Self-Consistent Loop (`Phi(X*) = X*`): Phases 1–4

Clean-room (`0 of 19` empirical inputs) pre-registered implementations, outputs, unit tests, and AST-isolated zero-import referee suites testing the self-consistent geometric loop across Phases 1–4.

## Directory Layout

- `self_consistent_loop_phi/` — **Phase 1:** Self-consistent Sol/anisotropic torus & modular feedback fixed-point engine (`self_consistent_loop_phi/PREREGISTRATION_PLAN.md`, `self_consistent_loop_phi/SEAL_SHA256.txt`, solver, referee, and tests).
- `cusped_3d_loop_phase2/` — **Phase 2:** 3D cusped hyperbolic Mostow-rigidity, Margulis-throat Laplacian, and chiral-boundary index engine (`cusped_3d_loop_phase2/PREREGISTRATION_PHASE2.md`, `cusped_3d_loop_phase2/SEAL_SHA256.txt`, solver, referee, and tests).
- `relational_yukawa_phase3/` — **Phase 3:** Relational weak-compass quotient (`0.0` enantiomer collapse), 2-component coupled spin-flux Klein-four palindrome protection audit, 3D hyperbolic trilinear Yukawa & Jarlskog CP theorem (`(6)` vs. chiral irreversible `[5, 1, 2, 2]`), and unrigged $E_8$ instanton tadpole audit (`relational_yukawa_phase3/PREREGISTRATION_PHASE3.md`, `relational_yukawa_phase3/SEAL_SHA256.txt`, solver, referee, and tests).
- `unification_cap_lepton_phase4/` — **Phase 4:** Unrestricted $|W| \le 12$ necklace census, 1-loop Fox–Wada Reidemeister acyclicity theorem ($\tau_{\text{Reid}}(k=0)=0$ vs. $\prod_{q=1}^4 \tau_{\text{Reid}}(k\ne 0)=5$), 4D $dP_9$ cusp-cap lattice $\mathbf{I}_{1,9}$ & mod-5 ramification audit, and parameter-free $SU(5)_{\text{GUT}}$ lopsided quark-vs.-lepton CKM/PMNS acid test (`unification_cap_lepton_phase4/PREREGISTRATION_PHASE4.md`, `unification_cap_lepton_phase4/SEAL_SHA256.txt`, solver, referee, and tests).
- `reports/` — Phase 1–4 comprehensive reports and the Phase 4 execution plan (`reports/phase4_vacuum_cap_lepton_plan.md` and `reports/phase4_unification_cap_lepton_report.md`).

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

# Phase 4
cd ../unification_cap_lepton_phase4
python3 -m unittest discover -s tests -v
```
