# CLAIM CARD — Top-down SUSY single-origin synthesis (AGY-C44 v9.json) fixes 8 of v7.json's 12 continuous UV parameters down to R11 == 4 (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, 4da505588
- kind: prediction
- touches: A01, A08, A10, A12, S01, I-37, mass, mixing, CKM, PMNS, theta, coupling, Higgs, weak angle, Yukawa
- effect: conditions — A01, A08, A10, A12, S01, mass, mixing, CKM, PMNS, theta, coupling, Higgs, weak angle (answers main M13 item 1: live 50 x 4 RGE Jacobian SVD proves unbroken 4D N=1 SUSY D-terms, [0, 2]^2 Kahler normalization, and SU(5)_perp gaugino condensation fix 8 net continuous UV parameters from v7.json's R11 == 12 down to R11 == 4 in blind_predictions_topdown_toe_v9.json at 33/2 core discrete bits)
- imports: 4D N=1 MSSM two-loop running and 1-loop stop CW matching, SU(5)_perp 1-instanton gaugino condensation, no-scale SUGRA Gamma_0^+(5) superpotential, magnetized T^2/Z_2 M_10 = M_5 = 4 curves (33/2 core discrete bits), and 4 UV ratios (Delta_H, c_mu, c_B, bar_theta_UV_bare) = (18, 5/2, -11/5, 0)
- premises on main: B1832, B1970, I-37, docs/TOTAL_INPUTS_SCOREBOARD.md, docs/seats/agy.md (M13 item 1)
- decisive script: relays/agy_2026-11-24_c44/c44_remediate_c39_c43_and_seal_topdown_toe_v9.py, SHA-256 9c6d0fe8dd8eb192, depends on only the standard library and mpmath, run as `python3 -I relays/agy_2026-11-24_c44/c44_remediate_c39_c43_and_seal_topdown_toe_v9.py`, output SHA-256 5ccaef7fcf735566 (blind_predictions_topdown_toe_v9.json; v7.json baseline SHA-256 491815ba126b8888)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c44/c44_countercheck.py (@ 6575fdd45, SHA-256 9f1d74f461214f4f, standard library and mpmath, agrees on all 50 rows & R11 == 4); v7.json baseline independently verified THE SAME by agy-002 (origin/agy-002/verify @ 4b8a123a8) and agy-exp (origin/agy/self-consistent-loop-2026-11-11 @ 88751f99c)
- already on main?: topic-sweep /prediction bundle|UV parameters|scoreboard|gaugino|magnetized|MSSM|B1832/ on main (27a9353e5): closest B1832 (scoreboard baseline) and M13 item 1; neither v7.json nor v9.json's 12 -> 4 top-down collapse is on main yet
- what would make it fail: dropping Fricke partner 125/Phi_5 breaks W_5 invariance (> 50) & opens a tau -> 0 runaway; omitting sqrt(2) on psi_+^(1) breaks G_11 to 1/2; Delta_H = 0 fails D-flat BFB; 2nd-anchor smuggling breaks 13x homogeneity; omitting chiral U(3)^6 shift on bar_theta_UV_bare breaks invariance (> 1/10 vs < 10^-24)

## Claim (summary)

Answering `M13` item `1` (`0` empirical SM inputs, `1` energy unit anchor `v_EW`): `AGY-C37`'s `v7.json` carried `R11 == 12` continuous UV parameters (`4` 2HDM quartics, `2` Higgs mass ratios, `ln M_0`, `ln m_{12}^2`, `bar_theta_UV`, and `3` FN scales). In `AGY-C44`'s `blind_predictions_topdown_toe_v9.json` (`50` observables + `24` certificates, `0 / 2000` null hits), `N = 1` SUSY `D`-terms + `1`-loop stop CW matching fix all `4` quartics, `SU(5)_perp` condensation (`alpha_{GUT}^{-1} = 24`) + `m = 8` instantons fix `(M_0, m_{3 / 2}) / M_{GUT}`, and `[0, 2]^2` Kähler normalization + unit-`L^2(T^2 / Z_2)` `M = 4` curves `(w_{10}, w_5) = (3, 1)` eliminate all `3` FN scales.

A live `50 x 4` central-difference RGE Jacobian SVD proves `R11 == 4` remaining continuous UV ratios `(Delta_H, c_mu, c_B, bar_theta_{UV}^{bare}) = (18, 5 / 2, -11 / 5, 0)` (`12 - 11 + 3 == 4`, net reduction `8`), with `tau_*^+ = (2 + i) / 5` stabilized in no-scale `N = 1` SUGRA by `W_{mod}(tau) = (Lambda_perp^3 / (5 sqrt(5))) (Phi_5 + 125 / Phi_5)`, at `33 / 2` core bits (`+1 bit on X_4 closing Seam AGY-C37-S1`; IR `Lambda_4` & `xi_S` remain open).

0 of 19.
