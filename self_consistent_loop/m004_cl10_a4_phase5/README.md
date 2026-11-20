# Phase 5: `m004 × Cl(10) × A_4` Flavour, `Spin(11)` Hosotani/Collar, `7D` Radion, & `2`-Loop RGE Closure

Clean-room two-track implementation (`Track A`: `0 of 19` pre-registered blind baseline `v1`; `Track B`: explicitly separated post-unblinding zero-parameter structural completion `v7`), AST-isolated zero-import referee (`45 / 45` planted-fault controls caught), and `unittest`/`pytest` verification suite.

## Directory Layout

- `PREREGISTRATION_PHASE5.md` & `SEAL_SHA256.txt` — Pre-registration plan, gate definitions, and SHA-256 integrity seal.
- `src/phase5_loop/geometry_and_selection.py` — **Gate P5-1 (`0 of 19`):** Exact $\mathbb{Z}[\omega]$ `m004` geodesic shells, Margulis apex roots ($z_{\mathrm{apex}}(\gamma_1) < 1$ vs. $z_{\mathrm{apex}}(\text{"AAb"}) = 3^{1/4}$), $\pi_1(M^{(5)}) = \operatorname{Stab}_{D_5}(0)$ `1/5` covering-space systole lift, `2`-torsion Majorana conservation, and `B940` Selberg scales $(\epsilon_1, \epsilon_2, r_{\mathrm{sh}})$.
- `src/phase5_loop/clifford_hosotani_collar.py` — **Gate P5-2 (`0 of 19`):** `32 × 32` `Spin(11)` Kawamura `0`-triplet projection, non-abelian GHU `1/3` triangle (`[G_gluon, H_vev] = 0`), `Spin(10)` $6.59112\times$ Cartan interference, `50`-digit Clausen Hosotani EW minimum, flat-bundle `1`-loop collar $L_c^* = 3.804074\dots$, and `50`-digit UV–IR zero-mode mirror duality.
- `src/phase5_loop/gravity_radion_and_warping.py` — **Gate P5-3 (`0 of 19`):** `7D → 4D` Weyl reduction (`R^-3, +R^-5, -R^-6, +R^-9, R^-10`), pure curvature+Casimir hilltop no-go, flux-stabilized Minkowski radion, and symbolic `7D` warped Einstein `Clause N8`.
- `src/phase5_loop/rge_and_phase5_engine.py` — **Gate P5-4 (`0 of 19`) & Composite Engine:** Literature RGE benchmark gates (`Pendleton–Ross`, `Machacek–Vaughn`, `ADKLR`, `Contino–Pilo`), `Spin(11)` $\mathbb{Z}_2\times\mathbb{Z}_2'$ Dynkin indices, `Clause N6` Selberg QCD pole, `Clause N12` `50`-digit amphicheiral `m004` CP vanishing, and Phase 1–5 seal verifier.
- `src/phase5_loop/track_b_unblinded_scorecard.py` — **Gate P5-5 (`Track B`):** Side-by-side `24`-observable evaluation of frozen `v1` (`16 / 24` hits) vs. zero-parameter `v7` (`22 / 24 = 91.7%` hits, `12` Tier-1 Precision Hits) after calibrating the `2` $\overline{\mathrm{MS}}$ gauge macro-anchors $(\alpha_{\mathrm{em}}^{-1}(M_Z), \alpha_3(M_Z))$ with `10`-trial dynamic `SU(3)^5` Haar invariance (`< 1e-11`).
- `scripts/referee_phase5.py` — AST-isolated zero-import referee executing all **`45 / 45` planted-fault controls**.
- `outputs/` — Immutable `preregistered_blind_predictions_v1.json`, `preregistered_blind_lock_sha256.json`, `phase5_results.json`, and `referee_phase5_verdict.json`.
- `tests/test_phase5.py` — Automated verification test suite.

## Reproducing Phase 5

```bash
cd self_consistent_loop/m004_cl10_a4_phase5
PYTHONPATH=src python3 -m phase5_loop.rge_and_phase5_engine
python3 scripts/referee_phase5.py
python3 -m unittest discover -s tests -v
```
