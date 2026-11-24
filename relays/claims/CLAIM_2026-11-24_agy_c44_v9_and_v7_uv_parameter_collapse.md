# CLAIM CARD — Top-down SUSY single-origin synthesis (AGY-C44 v9.json) fixes 8 of v7.json's 12 continuous UV parameters down to R11 == 4 (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, 4da505588 (C44 v9.json seal, computed once) & b06c8fc1e (C37/C38 v7.json baseline)
- kind: prediction
- touches: A01, A08, A10, A12, S01, I-37, mass, mixing, CKM, PMNS, theta, coupling, Higgs, weak angle, Yukawa
- effect: conditions — A01, A08, A10, A12, S01, mass, mixing, CKM, PMNS, theta, coupling, Higgs, weak angle (answers main M13 item 1: proves via live 50 x 4 RGE Jacobian SVD that unbroken 4D N=1 SUSY D-terms, [0,2]^2 Kahler normalization, and SU(5)_perp gaugino condensation fix 8 net continuous UV parameters from v7.json's R11 == 12 down to R11 == 4 in blind_predictions_topdown_toe_v9.json at 33/2 core discrete bits)
- imports: Horava-Witten E8 x E8 & F-theory SU(5) (n_10 = 2); no-scale 4D N=1 SUGRA Gamma_0^+(5) Hauptmodul W_mod stabilization of tau_*^+ = (2+i)/5 & m = 8 cover; Spin(10) x U(1)_X Cartan punctured-torus Szego kernel & canonical sqrt(2) magnetized T^2/Z_2 M_10 = M_5 = 4 curves; 2-loop MSSM + 3 N_R -> SM RGEs & non-degenerate 1-loop stop CW matching; 1 anchor v_EW + 4 continuous UV parameters (Delta_H = 18, c_mu = 5/2, c_B = -11/5, bar_theta_UV^bare = 0) + 33/2 core discrete bits
- premises on main: B1223, B1656, B1736, B1838, B1945, B1970, docs/TOTAL_INPUTS_SCOREBOARD.md, M13
- decisive script: relays/agy_2026-11-24_c44/c44_remediate_c39_c43_and_seal_topdown_toe_v9.py, SHA-256 9c6d0fe8dd8eb192, depends on standard library and mpmath, run as python3 -I relays/agy_2026-11-24_c44/c44_remediate_c39_c43_and_seal_topdown_toe_v9.py, output SHA-256 5ccaef7fcf735566
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c44/c44_countercheck.py (SHA-256 9f1d74f461214f4f: Cauchy-pentagonal SUGRA, 28x28 midpoint quadratures, FD stop CW Hessian, supergraph Casimir, MV84 tensor, GL4); baseline v7.json (33378e20f26835ca -> 901a4da464b4cb2e) recomputed independently by agy-002 (4b8a123a8) & agy-exp (88751f99c)
- already on main?: topic-sweep /prediction bundle|UV parameters|scoreboard|gaugino|magnetized|MSSM|B1832|B1970/ on main (27a9353e5): closest B1832 and B1970 (no 4-parameter top-down SUSY-to-SM 50-observable synthesis bundle on main)
- what would make it fail: 5/5 producer + 5/5 countercheck planted controls (dropping Fricke partner 125/Phi_5 breaks W_5 invariance > 100 and opens tau -> 0 runaway; omitting sqrt(2) on j=1 gives G_11 = 1/2 != 1; tree 1/lambda_tree VEV jump > 3/100; coherent 2-flavor leptogenesis drift > 1/5; omitting U(3)^3 chiral anomaly shift on bar_theta_UV^bare breaks invariance > 1/10)

## Exact `M13` Item `1` Accounting (`Which of v7.json's 12 Continuous UV Parameters Are Fixed, and How`)

- **From `v7.json` (`R11 == 12`) to `v9.json` (`R11 == 4`, Net Reduction `12 - 4 == 8`):**
  - `4` 2HDM quartic couplings (`lambda_1..4`) -> **fixed** by unbroken `4D N = 1` SUSY electroweak `D`-terms `(g_2^2 + (3 / 5) g_1^2) / 8` plus exact non-degenerate `1`-loop stop Coleman-Weinberg matching at `M_S = sqrt(m_{Q_3} m_{U_3})`.
  - `1` heavy Majorana scale (`ln(M_0 / M_{GUT})`) -> **fixed** by native hidden `E_8^{(2)} -> SU(5)_perp` (`b_0 = 15`) gaugino condensation at `alpha_{GUT}^{-1} = |2T| = 24`, yielding `Lambda_perp / M_{GUT} = exp(-16 pi / 5) == |q(tau_8^+)|` (`and m_{3/2} / M_{GUT} = exp(-48 pi / 5)`).
  - `3` Froggatt-Nielsen sector normalization scales -> **fixed** by the parameter-free `[0, 2]^2` `3`-field Kähler factor `(G_L G_R G_H)^{-1/2} = 2 sqrt(2) Im(tau_8^+)` and canonical `sqrt(2)` unit-`L^2(T^2 / Z_2)` magnetized zero modes at `M_{10} = M_5 = 4`, `(w_{10}, w_5) = (3, 1)`.
  - `2` Higgs mass ratios + `ln m_{12}^2` (`3` non-SUSY quadratic parameters) -> **replaced** by `3` rational Kähler/Giudice-Masiero ratios `(Delta_H, c_mu, c_B) = (18, 5 / 2, -11 / 5)`, while `bar_theta_{UV}^{bare} = 0` stays explicit (`12 - 11 + 3 == 4`, verified by live `50 x 4` SVD with `5`th redundant scale column rank `4`).
- **Discrete Bits & Seam Closure:** Prices every topological/flux choice strictly `> 0` under Guardrail `1`, including `+1` bit for the self-dual `X_4` fiber branch (`closing agy-002 Seam AGY-C37-S1`), totaling `33 / 2` bits (`core 48`) and `35 / 2` bits (`full 50`).

0 of 19.
