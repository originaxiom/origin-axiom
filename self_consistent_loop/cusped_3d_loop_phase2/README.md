# Phase 2: The 3D Cusped Hyperbolic & Chiral-Boundary Loop Engine

Clean-room verification suite testing the three unified 3D cusped & topological upgrades discovered in Phase 1 (`self_consistent_loop_phi`), strictly enforcing `0 of 19` empirical data imports and all six mathematical-physics guardrails.

## Structure
- `PREREGISTRATION_PHASE2.md` & `SEAL_SHA256.txt`: Pre-registered equations, calibration benchmarks, falsifiers, and planted negative controls locked prior to solver implementation.
- `src/cusped_loop/`:
  - `hyperbolic_fem_core.py`: Exact `SnapPyHP` Epstein–Penner Minkowski Gram builder, 24-cone cusp-desingularized Riemannian quadrature, $100\%$ $S_4$-symmetric Eulerian tetrahedral subdivision, and flat-bundle $\operatorname{U}(1)$ / $\operatorname{U}(2)$ 3D hyperbolic P1 finite-element solver.
  - `calibration_gate.py`: Textbook calibration benchmarks (`m004` volume `< 1e-12`, 5-fold cover FEM equivalence `< 1e-12`, and 2D magnetized Atiyah–Singer Dirac index $\operatorname{ind} = c_1$ with Haar basis invariance `< 1e-12`).
  - `gate1_3d_twisted_throat.py`: Gate 1 — True 3D hyperbolic pinched-throat twisted Laplacian across `(6)`, `(1,6)`, `(2,1,2,1,2)`, `(2,1,1,1,2)`, `(2,1^8,2)`, `LR`, negative control `L^2 R L R`, and all 18 extending histories in `A6` under both `b++` and `b+-`.
  - `gate2_mostow_rigidity_readout.py`: Gate 2 — Mostow–Prasad topological rigidity invariants (`tau_cusp`, Margulis throat complex length, volume, and Chern–Simons `CS`) under `A-one` and `A-all`.
  - `gate3_topological_chirality.py`: Gate 3 — Globally $E_8$-integral flux classification ($\Lambda_R(E_8)$), explicit 2D gauged Dirac & APS boundary defects, and 3D parity-even vs. Chern–Simons parity-odd weak handedness tests.
  - `phase2_engine.py`: Sealed composite orchestrator writing `outputs/phase2_results.json`.
- `scripts/referee_cusped_phase2.py`: AST-verified zero-import independent referee (`0` imports from `cusped_loop`/`src`) writing `outputs/referee_phase2_verdict.json`.
- `tests/test_cusped_phase2.py`: Comprehensive unit-test suite enforcing seal integrity, data firewall, precision gates, negative controls, and referee pass.

## Run
```bash
PYTHONPATH=src python3 -m cusped_loop.phase2_engine
python3 scripts/referee_cusped_phase2.py
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
