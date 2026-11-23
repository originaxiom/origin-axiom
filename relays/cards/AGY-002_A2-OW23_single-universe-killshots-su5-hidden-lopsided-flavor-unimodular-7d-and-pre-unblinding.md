# Pre-Registration Card A2-OW23 & A2-OW16 v10: Single-Universe Kill-Shot Campaign (`8 / 8` Hidden-`SU(5)` Window, `240`-Root `E_8` Doublet-Triplet Splitting & Multi-Axion Strong CP, McKay `2I`, `\tau_0` vs. `8\tau_0` Covering Bridge, Lopsided `SU(5)` + `M_R = W_sym` Seesaw, `7D` `R^2` Ghost No-Go vs. `R_{MN}^2` + `4D` Unimodular Anti-Decompactification, CP Domain-Wall Erasure, & Pre-Unblinding Readiness) (`0 of 19`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (base `27f5d89fa`)
- **Date:** `2026-11-23`
- **Firewall:** strictly `0 of 19` (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere).
- **Coding & Custody Standard:** `0` Python `float`/`complex` AST literals, `0` binary64 `float()`/`complex()` casts, `0` JSON float tokens (`assert_no_json_floats`), `0` peer/`frontier/` imports, pre-hashed `SCRIPT_SHA256.txt` committed before execution, raw unread `OUTPUT_SHA256.txt` committed before analysis, zero in-place overwrites, single-run `A2-OW16 v10` (`computed once`), followed by an isolated cold-room zero-shared-code referee (`relays/a2_ow23_referee/referee_a2_ow23.py`).

---

## 1. Pre-Registered Modules & Acceptance Gates (`A2-OW23`)

### Module `OW23-A`: Exact `E_8` Algebra, `8 / 8` Hidden-`SU(5)` UV Gravity Window, `240`-Root Doublet-Triplet Splitting, Multi-Axion Strong CP, & McKay `2I` Unity
1. **Exact `N = 1` SUSY Double-Sided Gravity Window (`0 < N_C - N_V <= 10`):**
   - Compute `a_1(xi = 0) = (N_C - N_V) / 2`, `M_g^{DEP} = 3(N_C - N_V)`, and `M_g^{DP} = (3/2) N_C - (9/2) N_V` directly from explicit multiplet counts at the UV `SU(5)_vis x SU(5)_hid` scale (`N_V = 48`).
   - Scan `N_gen in {1, 2, 3, 4, 5}` (`16`-plets + `H_u, H_d` and `+ 5_H, 5bar_H`) plus `3 x 27` `E_6`: test whether `N_gen = 3` is the **unique integer survivor** satisfying both `a_1(xi=0) > 0` and `M_g^{DEP} < 31` (`N_C = 52 -> a_1 = +2, DEP = +12, DP = -138`; `N_C = 58 -> a_1 = +5, DEP = +30, DP = -129`), upgrading `B4_UV` to **`8 / 8`** in the `M_GUT < mu < M_KK` 4D-EFT window while computing the exact light hidden chiral cap (`<= 6` for `52`, `0` for `58`).
2. **Explicit `240`-Root `E_8` Construction, `Z_5` Breaking, Doublet-Triplet Splitting (`d = 5` Proton Stability), & Hidden-Charge Obstruction:**
   - Explicitly construct all `240` roots of `E_8` in exact `Fraction` `\mathbb{R}^8` coordinates (`112` `D_8` + `128` spinor, every `|r|^2 == 2`).
   - Apply the exact Kac `Z_5` shift `V_5 = \omega_{mark=5} / 5`, proving `48` untwisted (`24 + 24` = `SU(5)_vis x SU(5)_hid`) and `200` twisted (`(10,5) + (10bar,5bar) + (5,10bar) + (5bar,10)`).
   - Apply the `Z_2` weak-hypercharge parity (`SU(5)_vis -> G_SM`: `12` unbroken SM gauge bosons + `12` broken `X, Y`) directly on the `5` and `5bar` roots, verifying exact **doublet-triplet splitting** (`H_u, H_d` parity `+1` vs. colored triplets `H_C, Hbar_C` parity `-1`, forbidding tree-level `d = 5` proton decay `H_C Hbar_C` mixing!).
   - **Honest Kill-Shot 1 Obstruction Audit:** Verify directly on all `200` coset roots that every bulk `(10, 5)` and `(5bar, 10)` root carries non-zero `SU(5)_hid` Cartan charge—proving that `3` visible `SU(5)_hid`-singlet generations MUST come from localized/twisted cycles (`b_1 = 3`) or `SU(5)_hid` breaking.
3. **Pure-`SU(5)_hid` Gaugino Condensation Dimensional Transmutation:**
   - Compute exact `1`-loop `b_hid = 3 N_c = 15` (`SU(5)`) vs. `12` (`SU(4)`) and `9` (`SU(3)`), evaluating exact dimensionless condensation ratios `Lambda_hid / M_UV = exp(-2 pi / (b_hid alpha_UV))` and `m_{3/2} / M_Pl = (Lambda_hid / M_Pl)^3` on a pure theoretical integer grid `\alpha_{UV}^{-1} in {20, 24, 25, 30, 40}` (`0 of 19`).
4. **Exact Multi-Axion Strong-CP Matrix (`OBS-07` + `OBS-16` + `b_1 = 3` Kill-Shot 4):**
   - Minimize the `SU(3)_c + SU(5)_hid` instanton potential at `55`-dps with `Lambda_hid^4 / Lambda_QCD^4 = 10^{40}` and generic rational phases `(7/10, 19/10)`: prove that `1` single `E_8` axion (`rank 1`) fails (`|bar_theta_eff| = 6/5 + O(10^{-40})`), whereas `2+` linearly independent axions from `b_1(8^3_4) = 3` (`rank 2`, `det C != 0`) relax **both** `|bar_theta_QCD| < 10^{-50}` and `|theta_hid| < 10^{-50}` with positive-definite Hessian.
5. **Exact McKay `2I = SL(2, F_5) <-> E_8` Group Enumeration:**
   - Explicitly enumerate all `120` integer matrices `SL(2, F_5)` (`det == 1 mod 5`), verify exact order `120` (`|PSL(2, F_5)| = 60`), exact element-order distribution `{1:1, 2:1, 3:20, 4:30, 5:24, 6:20, 10:24}`, and prove maximal cyclic subgroup orders are **uniquely `{4, 6, 10}`** (`{2, 3, 5}` in `A_5`), uniting `E[2]`, `K_6`, and `K_5` inside one exact `E_8` McKay group.

### Module `OW23-B`: `\tau_0` vs. `8\tau_0` Covering Bridge, Mostow Cusp Rigidity, Lopsided `SU(5)` `10 / 5bar`, & Parameter-Free `M_R = W_sym(q_R, q_R)`
1. **Exact `\tau_0` vs. `8\tau_0` `j`-Invariant, Covering Map, & Mostow Cusp Audit:**
   - Verify at `60`-dps: `\tau_0 = (2+i)/5 = 1/(2-i)`, `-1/\tau_0 + 2 = i`, `5\tau_0 - 2 = i`, and `j(\tau_0) = j(5\tau_0) = j(i) = 1728` (`< 10^{-50}`), whereas `8\tau_0 - 3 = 1/5 + (8/5)i` lies strictly inside the `SL(2, \mathbb{Z})` fundamental domain (`|z| = \sqrt{65}/5 > 1`) with `|j(8\tau_0) - 1728| >> 1` (proving non-equivalence under `SL(2, \mathbb{Z})` and documenting the exact index-`8` sublattice covering matrix `[[8, 0], [0, 1]]`).
   - Verify `j(\omega) = 0` (`< 10^{-50}`, tetrahedral `m004` Eisenstein lattice `\mathbb{Z}[\omega]`) vs. `j(i) = 1728` (octahedral Gaussian lattice `\mathbb{Z}[i]`), documenting honestly that `\tau_0 \sim i` matches an **octahedral** `\mathbb{Z}[i]` cusp rather than tetrahedral `m004`.
2. **Lopsided `SU(5)` Unified Weights (`n_{10} = (3, 2, 0)` + `n_{5bar} in {(1,1,0), (1,0,0), (2,1,0)}`):**
   - Test `Y_u = D(n_{10}) W_u D(n_{10})`, `Y_d = D(n_{10}) W_d D(n_{5bar})`, `Y_e = D(n_{5bar}) W_e D(n_{10})` across **both** flat horosphere Kähler and curved `2D` hyperbolic `K_{E[2]}^{hyp}`.
   - Verify strict `|V_{12}| > |V_{23}| > |V_{13}|` CKM ordering, `5`-decade up-quark hierarchy, `K_6` down/lepton splitting, holomorphy (`|\bar\partial W|/|\partial W| < 10^{-25}`), `10`-trial SplitMix64 Haar `U(3)^3` invariance (`< 10^{-40}`, Guardrail 3), and compute explicit `1st/2nd`-gen squark soft-mass splitting on flat vs. curved `K_{E[2]}^{hyp}` (FCNC check).
3. **Parameter-Free Holomorphic Majorana `M_R = W_sym(q_R, q_R)` Seesaw & Leptogenesis Sign (`OBS-18` + `OBS-15`):**
   - Build `M_R^{(0)} = (W_hol(q_R, q_R) + W_hol(q_R, q_R)^T) / 2` directly from the same `K_5 + K_6` operator for `q_R in {0, +3, -5}`, paired with lopsided `n_{5bar}` and `n_{nu^c}`.
   - Verify `q_R = 0` triggers exact rank-`2` singular `M_R` collapse (`sv_0 < 10^{-40}`); for `q_R in {+3, -5}`, compute exact Type-I seesaw `M_nu = -W_nu M_R^{-1} W_nu^T` via `55`-dps Takagi SVD, verify `10`-trial Haar `U(3)_L x U(3)_R` invariance (`< 10^{-40}`), extract `(s_{12}^2, s_{23}^2, s_{13}^2, dm_{21}^2/dm_{31}^2, J_PMNS)`, and compute exact `1`-loop `2`-flavor leptogenesis CP asymmetry `\varepsilon_1` (SM & MSSM loop functions) at `\tau_8^+` vs. `\tau_8^-`, verifying exact CP oddness `\varepsilon_1(\tau_8^-) == -\varepsilon_1(\tau_8^+)` (`< 10^{-45}`).
4. **Single-Modulus Flavor Control at `\tau_0` and `i`:**
   - Evaluate the exact same Yukawa operator directly at `\tau_0 = (2+i)/5` and `\tau = i` to prove definitively whether flavor requires the `8`-sheeted cover `8\tau_0`.

### Module `OW23-C`: `7D` `R^2` Ghost No-Go vs. `R_{MN}^2` + `4D/7D` Unimodular Anti-Decompactification, Warped Hyperbolic Cusp Flatness, Canonical `m_\tau / H_inf` CP Domain-Wall Erasure, & Energy Vise
1. **Exact `3D` Gauss-Bonnet Vanishing & `7D` `R + \alpha_{R^2} R^2` Ghost vs. dS No-Go Theorem + `R_{MN}^2` Constructive Resolution:**
   - Prove symbolically in `sympy` that on ANY constant-curvature `3`-manifold `M^3` (`K = -1/R^2`), `\mathcal{G}_3 = \mathcal{R}_3^2 - 4 |\text{Ric}_3|^2 + |\text{Riem}_3|^2 == 0` identically, whereas `+\alpha_{R^2} \mathcal{R}_7^2` gives `V_{R^2} = -36 \alpha_{R^2} V_{hyp} R^{-7}` AND shifts the `4D` Einstein-Hilbert coefficient by `1/2 + 2 \alpha_{R^2} \mathcal{R}_3 = 1/2 - 12 \alpha_{R^2}/R^2`!
   - Prove the exact **Ghost vs. Bare-dS No-Go Theorem**: ghost-free `4D` gravity requires `u = 12 \alpha_{R^2}/R_*^2 < 1/2`, whereas a bare `3`-term `(5, 7, 10)` dS minimum requires `u in (25/21, 5/3) > 1` (disjoint intervals!).
   - Prove the exact **Constructive Resolution**: `+\beta R_{MN} R^{MN}` (or `R_{MNPQ}^2`) has **zero** `\mathcal{R}_4 \mathcal{R}_3` cross-term (`M_{Pl,eff}^2` strictly positive for all `R > 0`), generating `-12 \beta V_{hyp} R^{-7}` cleanly! Solve the exact real-action `3D` Newton problem at `55`-dps using topological `(V_{hyp}, \beta, C_6 = +567/5)` (zero toy placeholders `3000, 2900`!), and wire `1 / g_{4D}^2 \propto V_{hyp} R_*^3` directly to `R_*`.
2. **Exact `4D` (`p = 0`) vs. `7D` (`p = 3`) Unimodular Anti-Decompactification Theorem:**
   - Prove symbolically & at `55`-dps that `4D` unimodular `+\Lambda_{4D}` (`p = 0`) leaves `(R_min, \tau_0)` and all `3` Hessian eigenvalues invariant to `< 10^{-50}` while uplifting a generic `7D` AdS minimum (`V_{7D}(R_min) < 0`) to `V_tot(R_min) = +\epsilon > 0` with `V_tot(\infty) = +\Lambda_{4D} >> \epsilon` (**zero decompactification runaway**!).
   - Derive exact universal `3`-term dS window formula `(u_infl, u_Mink) = (p_1(p_3-p_1)/(p_2(p_3-p_2)), (p_3-p_1)/(p_3-p_2))` for `7D` unimodular `p_1 = 3`: `(3, 5, 10) -> (21/25, 7/5)` and `(3, 7, 10) -> (1, 7/3)`.
3. **Exact Warped Hyperbolic Cusp Throat (`ds^2_{\mathbb{H}^3} = (dr^2 + |dz|^2)/r^2`) Horosphere Flatness:**
   - Compute symbolically the exact induced `2D` horosphere metric `h_{ab} = r^{-2} \delta_{ab}` and verify intrinsic Gaussian curvature `K_horo == 0` identically inside ambient `K_{\mathbb{H}^3} = -1`, plus exact redshift `e^{-L_{cusp}} = r_{UV} / r_{IR}`.
4. **Canonical `m_\tau / H_inf` CP Domain-Wall Erasure & Cosmological Energy Vise:**
   - From the exact canonically normalized `3D` Hessian (`g_{\tau\bar\tau} = 1/(4 y_0^2)`, canonical radion `b_{canon} = \sqrt{30}/15`), compute physical ratios `m_\tau / H_inf` and `m_R / H_inf` inside the `OW22-C` safe `60`-e-fold Starobinsky regime and on the real `7D` `R_{MN}^2` + `4D`-unimodular minimum, testing quantitatively whether `m_\tau / H_inf >> 1` erases spontaneous CP domain walls beyond the horizon.
   - Document `CS(m004) = 0` amphichirality vs. chiral `M^3` (`CS != 0`), and verify the dimensionless Cosmological Energy Vise (`M_{R,1} < T_reh < V_0^{1/4} < (V_0^{crit})^{1/4} ~ M_KK < M_Pl`) in Planck units (`0 of 19`).

### Module `OW23-D`: `12`-Gate Alpha vs. Beta Matrix, Honest Continuous + Discrete Bit Ledger (`OBS-22`), & Computed `ready_to_unblind` Gate
- Score **Candidate Alpha** (`Warped 7D E_8 Hyperbolic-Cusp GHU`) vs. **Candidate Beta** (`B4_UV`: `N = 1` SUSY `E_8 -> SU(5)_vis x SU(5)_hid` + `E[2]`-SS + lopsided `10/5bar` + `7D` `R_{MN}^2` + `4D` unimodular) across all `12` computed structural gates (`G1..G12`, zero hardcoded booleans).
- Audit every continuous parameter (`15 -> 8 -> 5 -> 2` levers) AND every discrete selection bit (`log_2` of candidate pools, comparing lopsided `SU(5)` `(n_{10}, n_{5bar})` vs. `9`-integer `FN(3,2,0)`).
- Compute `ready_to_unblind` strictly from the `5`-point readiness conjunction, listing every remaining blocker honestly.

### Module `OW23-E`: `6 / 6` Planted Fault Controls
1. **`PF-OW23-1`:** Set `N_gen = 4` (`N_C = 68`) in `B4_UV` (`N_V = 48`) -> violates `M_g^{DEP} = +60 > 31`.
2. **`PF-OW23-2`:** Remove `2nd` axion (`rank 1`) in `SU(3)_c + SU(5)_hid` potential -> leaves `|bar_theta_eff| = 6/5 >> 10^{-50}`.
3. **`PF-OW23-3`:** Claim `8\tau_0` is `SL(2, \mathbb{Z})`-equivalent to `\tau_0` -> caught by `|j(8\tau_0) - 1728| >> 1`.
4. **`PF-OW23-4`:** Set `q_R = 0` (`6Y`) in `M_R = W_sym(q_R, q_R)` -> exact rank-`2` singular `M_R` collapse caught (`sv_0 < 10^{-40}`).
5. **`PF-OW23-5`:** Apply `7D` (`p = 3`) uplift instead of `4D` (`p = 0`) and claim `(R_min, \tau_0)` is unchanged -> caught by `|\Delta R_min| >> 10^{-10}`.
6. **`PF-OW23-6`:** Omit `1` matrix from `SL(2, F_5)` or corrupt `E_8` root norm -> caught by exact `|SL(2, F_5)| != 120` / `|E_8| != 240` gate.

---

## 2. Updated Honest Master Scorecard (`A2-OW16 v10`)
- Single-run ledger (`computed once`), retaining `1` `DERIVED_EXACT` (`OBS-07` sole unconditional theorem; zero premature promotions!), updating `OBS-03`, `OBS-04`, `OBS-06`, `OBS-09`, `OBS-10`, `OBS-11`, `OBS-15`, `OBS-16`, `OBS-17`, `OBS-18`, `OBS-20`, `OBS-21`, and `OBS-22` strictly from `A2-OW23` outputs, adding `LOCK_16`, verifying `100%` of branch `*SHA256*.txt` manifests (`198+`), `0` AST/binary64/JSON floats, and `6 / 6` planted faults.
