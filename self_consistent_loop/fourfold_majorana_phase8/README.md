# Phase 8: Axion Isocurvature Branch Shootout, `E_8` Singlet `(1, 3)` Majorana Portal, & Elliptic Fourfold `X_8` Tadpole Audit (`105` of `105` Controls)

Clean-room two-track (`0 of 19` empirical inputs in Track A) implementation of Phase 8 under `self_consistent_loop/fourfold_majorana_phase8`.

## Package Layout

- `PREREGISTRATION_PHASE8.md` & `SEAL_SHA256.txt` — Cryptographically sealed pre-registration specification locked prior to engine execution.
- `src/phase8_toe/p8_1_isocurvature_shootout.py` — **Gate P8-1 (Track A, `0 of 19`):** Fox–Pierce–Thomas & Germani–Kehagias benchmarks, large-radius `11D` Gauss–Bonnet & `10D` Hořava–Witten Green–Schwarz kinetic mixing (`Branch 1A`), and small-radius T-dual self-dual Casimir cusp-cap Klein–Gordon Hubble-flow plateau (`Branch 1B-SD`: $R_{\mathrm{sd}} M_7 = 1$, $V_0 = |V_{\mathrm{Cas}}(R_0)|$, $\mu = M_7$).
- `src/phase8_toe/p8_2_e8_majorana_portal.py` — **Gate P8-2 (Track A, `0 of 19`):** Exact `248 = 45 + 15 + 60 + 64 + 64` $E_8 \supset \mathrm{Spin}(10) \times \mathrm{SU}(4)$ root enumeration, `50`-digit `9x9` Malinský–Romão–Valle Schur-complement sign identity, and chiral negative-torsion Shell-2 one-leg Linear Seesaw operator (`L_neg_full`) for the $D_5$-invariant singlet $S \in (\mathbf{1}, \mathbf{15})$.
- `src/phase8_toe/p8_3_cy4_tadpole_bp.py` — **Gate P8-3 (Track A, `0 of 19`):** Klemm–Lian–Roan–Yau Weierstrass CY4 benchmarks ($\mathbb{P}^3$, $\mathbb{P}^1 \times \mathbb{P}^2$), Freed–Witten $c_2(X_8) \pmod 2$ parity check, and critical del Pezzo blow-up rank $r_{\mathrm{crit}} = 8$ on $B_6 = \mathbb{P}^1 \times dP_r$ under strict M2-tadpole positivity $N_{M2} \ge 0$.
- `src/phase8_toe/p8_4_joint_consistency.py` — **Gate P8-4 (Track A, `0 of 19`):** Rational anomaly cancellation with $S \in (\mathbf{1}, \mathbf{15})$, explicit `brentq` Strong-CP minimization on `Y_weave`, and strict `10`-step Track-A dimensionless scale ordering.
- `src/phase8_toe/track_b_phase8_scorecard.py` — **Gate P8-5 (Track B):** Explicitly priced empirical comparison boundary (`1` unit anchor + `3` continuous comparison inputs) evaluating `v10_e8_weave` across all `24` dimensionless SM observables (`12` Tier-1 + `12` Tier-2, `0` Tier-3 misses, `10`-trial `SU(3)^5` Haar invariance `< 1e-11`), CMB + isocurvature ($\beta_{\mathrm{iso}}^{(1\text{B-SD})} = 0.00784 < 0.038$), and CY4 tadpole flux spacing.
- `src/phase8_toe/phase8_engine.py` — Composite engine & Phases 1–8 seal verifier producing `outputs/phase8_results.json`.
- `scripts/referee_phase8.py` — AST-isolated zero-import referee verifying `105` of `105` cumulative planted-fault controls (`85` Phases 1–7 + `20` Phase 8) into `outputs/referee_phase8_verdict.json`.
- `tests/test_phase8.py` — Unit and `pytest` verification suite.

## Reproduction

```bash
cd self_consistent_loop/fourfold_majorana_phase8
PYTHONPATH=src python3 -m phase8_toe.phase8_engine
python3 scripts/referee_phase8.py
python3 -m unittest discover -s tests -v
```
