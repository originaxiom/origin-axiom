# Card `AGY-002_FOUND-V2-U4` — `P-862` Selection-Free Universal Determinant Laws `UF-1..UF-4`, `W-P1c` Process Clocks, & `58`-Node Epistemic `DAG` `v2` (`0 of 19`)

## 1. Package and Question

Completing `AGY-002-FOUNDATIONS-V2` strictly blind to `web`'s `W-P1d` (`zero git fetch or log of web`, `0 of 19`):

1. **`P-862` Selection-Free Universal Determinant Laws (`UF-1..UF-4`):**
   - **Symbolic Cholesky Positivity Theorem (`SymPy`):** Prove for general `3 x 3` symmetric positive-definite matrices `G_3 = L_3 L_3^T` (`positive diagonals d_1, d_2, d_3`) and `G_2 = L_2 L_2^T` (`positive diagonals e_1, e_2, e_3`) that `det(G_3 + G_2) - det(G_3)` has strictly positive diagonal expansion in `(d_i^2, e_i^2)` (`with all terms non-negative for real Cholesky factors`), and for `M = L_3^{-1} L_2` diagonalized by orthogonal eigenvalues `lambda_1, lambda_2, lambda_3`, `det(I_3 + M M^T) = (1 + lambda_1^2)(1 + lambda_2^2)(1 + lambda_3^2) = 1 + e_1(lambda^2) + e_2(lambda^2) + e_3(lambda^2) > 1` strictly whenever `G_2 > 0`.
   - **Pointwise Fundamental-Domain Verification (`mpmath` `dps = 50`, `16` points x `4` `(m_gal, reading)` combos = `64` Fock states):**
     * Exact `16`-point rational grid `F_16` inside the fundamental domain `|Re tau| <= 1/2, |tau| >= 1, Im tau <= 6`:
       `[0 + 11/10 i, 0 + 3/2 i, 0 + 5/2 i, 0 + 5 i, 1/2 + i, -1/2 + 7/5 i, 1/2 + 2 i, -1/2 + 4 i, 5/13 + 12/13 i, -7/25 + 24/25 i, 13/100 + 17/10 i, -1/5 + 2 i, 1/3 + 3 i, -2/5 + 4 i, 1/10 + 5 i, 13/100 + 6 i]`.
     * **Exact Holomorphic Cancellation Identity:** Verify `max(|det Y_u / det Y_d - R_ud|, |det Y_e / det Y_d - R_ed|) < (1/10)^25` at all `64` `(tau, m_gal, reading)` points in **both** `base_w0` and `phased_sum`, where `R_ud = sqrt(det(G_{3,R} + G_{2,R}) / det(G_{3,R}))` and `R_ed = sqrt((det(G_{3,L} + G_{2,L}) det(G_{3,R} + G_{2,R})) / (det(3 G_{3,L} + G_{2,L}) det(G_{2,R})))`.
     * **`UF-1` (`Universal Positivity`):** `R_ud > 51/50` and `R_ed > 3/2` across all `64` evaluations.
     * **`UF-2` (`Global Weil-Class Separation`, `P-874(1)`):** Across all `16` FD points and both readings `(S, tilde_S)`, `m = 1` satisfies `R_ud > 3/2` and `3/2 < R_ed < 5`, while `m = 3` satisfies `1 < R_ud < 5/4` and `R_ed > 10`.
     * **`UF-3` (`Removable-Singularity Continuity at i and rho`, `P-874(2)`):** At `tau_orb in {i, -1/2 + sqrt(3)/2 i}`, `sigma_3(Y_{hol}) / sigma_1(Y_{hol}) < (1/10)^35` while `R_ud(tau_orb) > 3/2` (`m = 1, S`) and `|R_ud(tau_orb + (1/10)^6 i) - R_ud(tau_orb)| < (1/10)^4`.
     * **`UF-4` (`Modular T, S & Guardrail 3 Haar Invariance`):** `|R_ud(tau_0 + 1) - R_ud(tau_0)| < (1/10)^25`, `|R_ud(-1/tau_0) - R_ud(tau_0)| < (1/10)^25`, and `10`-trial random `Haar SU(3)^5` invariance of `|det Y_u / det Y_d|` and `|det Y_e / det Y_d|` `< (1/10)^30`.
2. **`W-P1c` Whole-Weave Process Clocks (`Move-Count`, `Hyperbolic Geodesic Length`, `Poincaré Area`):**
   - **Clock A (`Move-Count`):** All `64` length-`6` positive words in `L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]]` split into `2` parabolic (`L^6, R^6`, `Tr == 2`) and `62` hyperbolic (`Tr > 2, c > 0`, including the `2` exact Pell words `LRRLRR` and `RRLRRL` with `Tr == 14` and FD-reduced apex `1/2 + sqrt(3)/2 i == -conj(rho)`). Evaluate equal-weight average `<ln R_ud>` and `<ln R_ed>` over the `62` hyperbolic geodesic apices `((a - d) + i sqrt(Tr^2 - 4)) / (2 c)` reduced to the fundamental domain.
   - **Clock B (`Hyperbolic Geodesic Length`):** Weight the same `62` hyperbolic words by `ell(M) = 2 arccosh(Tr(M) / 2)`.
   - **Clock C (`Truncated Poincaré Area`):** `2D` numerical quadrature over `F_6 = {|x| <= 1/2, sqrt(1 - x^2) <= y <= 6}` with measure `dx dy / y^2`, normalized by exact area `pi/3 - 1/6` (`quadrature area error < 1/1000`).
   - **Sealed Clock Bars:** For `(m = 1, S)`, all `3` clocks satisfy `11/20 < <ln R_ud> < 3/4` (`pairwise clock spread < 1/20`) and `1 < <ln R_ed> < 7/5` (`pairwise clock spread < 3/20`); for `(m = 3, S)`, Clock A and Clock B satisfy `0 < <ln R_ud> < 1/4` and `<ln R_ed> > 5/2`.
3. **`58`-Node Foundational Epistemic `DAG` `v2` & Cumulative `SHA-256` Manifest Custody:**
   - Extend `Gate 11`'s `52`-node DAG (`8 ROOT, 7 OPERATOR, 8 SEAM, 10 RELATION, 19 SM_TARGET`) by `6` new foundational nodes (`G:D5_Irregular_Cover_8_3_4`, `OP:Fock_Exterior_Weil_Yukawa_Om`, `OP:Level6_Box_Quartic_vs_CW_Dichotomy`, `PR-11:P874_Weil_Class_Separation`, `PR-12:B1962_B1963_Cusp_Alignment_And_Lepton_Split`, `PR-13:P862_WP1c_Universal_Yu_Over_Yd_Law`) to `58` total nodes (`9 ROOT, 9 OPERATOR, 8 SEAM, 13 RELATION, 19 SM_TARGET`).
   - Verify exact acyclicity (`0` cycles), `Guardrail 1` seam honesty, `Guardrail 5` (`prop["S:EWSB_Scale_Anchor_vEW"] == 3`), monotone max-plus rank propagation, `relation_rank_histogram_0_1_2_3 == [2, 8, 3, 0]`, `sm_target_rank_histogram_0_1_2_3 == [0, 0, 1, 18]`, and unique Rank-`2` modulus-free SM parameter `SM19:bar_theta_QCD`.
   - Dynamically verify `100%` of committed `relays/agy002_found_v2_*/*SHA256.txt` manifests (`18` in producer including self `SCRIPT_SHA256.txt`; `20` in referee including self `SCRIPT_SHA256.txt`).

## 2. Deliverables and Definition of Done

- Both producer (`relays/agy002_found_v2_u4/verify_found_v2_u4.py`, using dyadic Volterra `L_2` and Gauss-Legendre `Clock C`) and cold-room referee (`relays/agy002_found_v2_u4_referee/referee_found_v2_u4.py`, using `RK4` Cauchy-Riemann `L_2`, Newton-Schulz/Jacobi `K^{-1/2}`, Clenshaw-Curtis / composite Simpson `Clock C`, and Tarjan SCC) pass `AST` zero-float/zero-complex-literal checks, `0` repo imports, and matching `SHA-256` seals (`A`-only commits).

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PFU4-1` (`Linear Casimir Trace`):** Replacing `2 G_{3,R} + 2 G_{2,R}` with linear `(T_3, T_2)` trace weights collapses `|ln R_ed^{lin}| < (1/10)^35` at `tau_0 = 13/100 + 17/10 i`.
2. **`PFU4-2` (`Swapped Hypercharge u_R^c <-> d_R^c`):** Inverting `(K_{uR}, K_{dR})` flips `<ln R_ud> < -1/2 < 0` across all `3` `W-P1c` clocks.
3. **`PFU4-3` (`Guardrail 1` `0`-Bit Seam Smuggling):** Lowering unstabilized seam `S:Torsion_Tau_SU2R_Break` to `irk = 0, stabilized = False` triggers a `Guardrail 1` seam-honesty violation.
4. **`PFU4-4` (`Guardrail 5` Circular Edge / Missing `v_EW` Anchor):** Adding feedback edge `SM18:v_EW -> G:m004_Mostow_Rigidity` triggers cycle failure, and detaching `S:EWSB_Scale_Anchor_vEW` drops `prop["SM18:v_EW"]` strictly below `3`.
5. **`PFU4-5` (`Guardrail 3` `Haar` Basis Test):** `10`-trial `Haar SU(3)^5` scrambling leaves `|det Y_u / det Y_d|` invariant (`< (1/10)^30`) while raw `|det(Re Y_u) / det(Re Y_d)|` shifts by `> 1/5`.

## 4. Firewall

Strict `0 of 19`; touches only `relays/`; zero imports from `frontier/` or other seats; strictly blind to `web`'s `W-P1d`.
