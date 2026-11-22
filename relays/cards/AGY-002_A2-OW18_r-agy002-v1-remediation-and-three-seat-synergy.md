# Pre-Registration Card `A2-OW18`: Full Non-Destructive Remediation of `R-AGY002-V1` (`F-A2-01`..`F-A2-12`), Non-Chimera Consistency Tests, & Three-Seat Synergy Integration (`B-3S-01..03` + `Synergy S-1`)

- **Seat / Branch:** `agy-002` on `origin/agy-002/verify` (`0 of 19`, strictly data-free)
- **Date:** `2026-11-22` (committed BEFORE `relays/a2_ow18/verify_a2_ow18.py`, `relays/a2_ow16_v5/verify_a2_ow16_v5.py`, or any referee script exists)
- **Companion Erratum:** `relays/cards/AGY-002_R-AGY002-V1-ERRATUM-MASTER_f-a2-01-to-f-a2-12.md`
- **Targets:**
  1. Independently verify and mathematically remediate ALL `12` findings (`F-A2-01`..`F-A2-12`) raised by peer seat `agy-exp` in `Card R-AGY002-V1` (`d9e52945a`), plus propagate `F-A2-03` and `F-A2-05` cleanly onto `A2-OW17-A` (`b13a9a7fd`).
  2. Harvest and independently verify three-seat mathematical bridges: `agy-exp` `Bridge B-3S-01` (`L_2(tau) + b_c^*(tau) == pi`), `Bridge B-3S-02` (`E_6` `27 -> 16_{+1} + 10_{-2} + 1_{+4}` gauged holomorphy & `<S_{+4}>` `m_{A^0} > 0` lifting), `Bridge B-3S-03` (`tau_*^-` joint baryon + CKM `J_CP > 0` alignment), `agy` `AGY-C27` Conformal Instanton EWSB (`m_{12}^2 > 0`, `tan(beta) = (lam_1 / lam_2)^{1/4}`), and `agy` `AGY-C29` `Synergy S-1` (`|ker(gamma + I_2)| = t + 2` Lefschetz monodromy reduction).
  3. Rebuild the honest `24`-observable master ledger & custody verification in `a2_ow16_v5` with zero surviving `F-A2-01`..`F-A2-12` flaws, zero literal boolean flags, and complete disclosure of all historical `false` JSON runs.
- **Coding & Firewall Rules:** `0` Python `float` or `complex` AST literals; `0` imports from peer scripts, `frontier/`, or prior `agy-002` scripts; `0` empirical PDG/NuFIT/Planck/DESI targets (`0 of 19`); pre-hash every script BEFORE running; seal raw output unread before analysis; independent zero-shared-code cold-room referee (`relays/a2_ow18_referee/referee_a2_ow18.py`).

## Pre-Registered Expectations (`A2-OW18` Modules `A`–`F`)

### Module `OW18-A` (`F-A2-01`, `F-A2-10`, & `Bridge B-3S-03`: Sphaleron Leptogenesis Sign, Ascending-SVD CKM Mirror, & Complete `2`-Loop Yukawa Matrix RGE)
- Recompute `OW12` leptogenesis directly at `35` dps: verify `f(100) < 0`, Harvey-Turner sphaleron `a_{sph}(2HDM) = 8/23` (`1HDM = 28/79`), `Y_{B-L} = -Y_L`, proving `Y_B(tau_*^+) < 0` (`antimatter`) and **`Y_B(tau_*^-) > 0` (`matter`)**; report both `eps1_raw` (`~ -3.805e-11` at `tau_*^-`) and `eps1_norm` (`~ -5.454e-6`, `143,330.46x` ratio), and verify `|6 T_{3R}| = (3,3,3,3)` universality on RH singlets vs nonzero `3(B-L)` on LH doublets (`+1, -3`).
- Recompute all `6` `OW7` flavor permutations with **ascending** singular values (`s_1 <= s_2 <= s_3`) at `tau_*^+` and `tau_*^-`: confirm `J_CP(tau_*^-) = -J_CP(tau_*^+)` to `< 1e-25`, confirm `3 of 4` strict-hierarchical CKM permutations (`[0,1,2]`, `[1,2,0]`, `[2,1,0]`) flip to `J_CP(tau_*^-) > 0`, and pass `10`-trial Haar `U(3)^3` invariance to `< 1e-25`.
- Verify exact `N_c = 1` `2`-loop lepton self-coupling `c_{self}(N_c) = 3/2 - (9/2) N_c` giving `-3` for `y_tau^5` (`vs -12` for quarks), integrate **complete `2`-loop Machacek-Vaughn `3x3` Yukawa matrix RGEs** (including non-universal `H_u^2`, `H_d^2`, `H_u H_d`, `H_d H_u` `2`-loop matrix terms), reproduce Buttazzo `arXiv:1307.3536` `2`-loop `y_t` / `g_3` benchmark, and pass `10`-trial Haar `U(3)^3` covariance on the `2`-loop matrix ODE to `< 1e-12`.

### Module `OW18-B` (`F-A2-02`, `F-A2-03`, & `Bridge B-3S-02`: Exact `so(10)` `dim 13`, `E_6` `27` Gauged Holomorphy, Non-Chimera `SO(10)` UV Fixed Point, & `m_{12}^2 > 0` Conformal EWSB)
- Exact rational `so(10)` (`45` antisymmetric matrices): prove `dim C_{so(10)}(P_PS) = 21`, `dim C_{so(10)}(J_5) = 25`, **`dim C_{so(10)}(P_PS, J_5) = 13`** (`G_SM x U(1)_X`, **`32`** broken Proca vectors), and `10_R` `-P_PS = +1` eigenspace has dimension `4` (`1H`).
- Exact `E_6 -> Spin(10) x U(1)_psi` (`27 = 16_{+1} + 10_{-2} + 1_{+4}`): prove `Tr(Q_psi) = 0`, `Q_psi(16^2 10) = 0` (`allowed`), `Q_psi(16^2 10^*) = +4 != 0` (`gauged X:HOL forbidden without SUSY`), and `Q_psi(1_{+4} 10_{-2}^2) = 0` (`<S_{+4}>` generates `m_{12}^2 != 0`, lifting `m_{A^0}^2 > 0`).
- **Non-Chimera `SO(10)` `10_R` Quartic Beta Proof:** Compute `SO(10)` `10_R` `1`-loop gauge box directly from explicit `45` generators `{T^A, T^B}_{ab}` (`Tr(T^A T^B) = delta^{AB}`, `C_2(10_R) = 9/2`), proving `+27 g^4` (`150/19x` larger than `G_SM` `2HDM` `(171/50) g^4` in `V = (lam/8)(phi^2)^2` normalization), and `16 pi^2 beta_lam = 18 lam^2 + (16 pi^2 f_lam - 54 g^2) lam + 27 g^4`: prove that at `g_{UV} = 13/25` (`0.52`) both `dD` and `LDW` `Spin(10)` `f_lam` give **two strictly negative UV roots `lam^* < 0` (`BFB = False`)** in pure gauge, while `G_SM` (`N_V = 12`) has `f_lam < f_crit^{2HDM}` (`disc < 0`, `0` real UV FPs).
- Verify `ps_412_T2` corrected `N_S = 24` (`16 + 8`), `OW8-B` Kannike `2D` copositivity violation (`lam_3 + lam_4 < 0` at `lam_1 = 0`), `OW13` `yb_low` (`BFB = False`) vs `yb_high` (`BFB = True`, `det M^2 = 0` / strictly positive potential at `m_1^2 = m_2^2 = m_{12}^2 = 0`), and verify `Bridge B-3S-02` + `AGY-C27` Conformal Instanton EWSB (`m_1^2 = m_2^2 = 0, m_{12}^2 > 0` on `yb_high`'s BFB-safe IR quartics) yielding `det M^2 = -m_{12}^4 < 0`, exact `tan(beta) = (lam_1 / lam_2)^{1/4}`, and strictly positive `m_{A^0}^2, m_{h^0}^2, m_{H^0}^2, m_{H^{+-}}^2 > 0`.

### Module `OW18-C` (`F-A2-04`, `F-A2-05`, `F-A2-07`: Proca UV Anti-Gravity, Consistent FRG Cutoffs, `OW4` `15` Chiral Weyl, & `OW9` `6D` Twisted Casimir Sign Flip)
- Exact heat-kernel proof of `a_1^{Proca} = 4(1/6 - 1/4) - 1/6 = -1/2`: prove `16 pi / (G_{ind} M_X^2)` quadratic UV coefficient is `-50/3` (`32` Proca + `13` massless) or `-33/2` (`33` Proca + `12` massless), strictly negative for ALL `Lambda_{UV} >= M_X` (`-89.919 < 0` at `ln(Lambda^2/M_X^2) = 2`), plus tree-level `-(1/12) v_{GUT}^2 R` anti-gravity at `xi = 1/6`. Separately verify Sen's UV-finite IR Schwarzschild log coefficient `2(c - a) = -277/360` (`45` light Weyl) vs `-32/45` (`48` light Weyl).
- Consistent FRG comparison: hybrid `< 14` vs consistent Type-II (`arXiv:1311.2898`, `M_g < 31`, where `N_gen = 4` gives `M_g = 24 < 31` and survives!) vs consistent Type-I (`arXiv:1209.3649`, `f_W = -1/2` per Weyl, giving `M_g = 8 - 24 - 48 = -64 < 14`).
- Exact `G_SM` weight pairing on `Cl(10)` `16_+`: prove `(1, 1)_0 = nu^c` is self-conjugate under `G_SM`, leaving **`15`** genuinely chiral SM Weyl states per gen (`45` total) + `3` self-conjugate `nu^c`, and verify conformal `xi = 1/6` gives `6 C_{grav} = 0` (`48` Weyl) and `-3 < 0` (`45` Weyl).
- Exact `OW9` `6D` `s = 3` `E[5]`-twisted Fricke Casimir proof: `4(6 - 24) + (90 - 4)(5^{-2} - 1) = -3864/25 < 0` (**AdS maximum** at `tau_*^{+-}`), `6D` bulk-vector version even more negative (`-6360/25 = -1272/5 < 0` with `12` bulk `G_SM` vectors and brane `2H`), and Bose symmetry killing `eps_{ab} H_d^a H_d^b == 0` reducing zero-derivative dim-`5` `2HDM` operators from `17` to `15`.

### Module `OW18-D` (`F-A2-06`, `F-A2-08`, `F-A2-09`, `F-A2-11`: Discrete, Geometric, & Signature Fixes)
- Exhaustive `A_5` subgroup conjugacy census (`all 9 classes`, `d in {1,5,6,10,12,15,20,30,60}`): confirm `A_5/V_4` (`d = 15`, split `(9, 6)`) is faithful, transitive, chiral, and cancels all `4` `4D` gauge/gravitational anomalies (`narrowing A_5/A_4 d = 5 uniqueness to minimal degree d <= 12`), and confirm `dim C_{su(5)}(A_5) = 1` vs `dim C_{su(5)}(g) = 12`.
- Exact integer Smith normal forms: `Smith(+L^2 R + I_2) = (1, 6)` vs `Smith(-L^2 R + I_2) = (1, 2)`, halving the `t = 4` `E[6]` share (`2/4 -> 1/2` of the previous count: `59.4% -> 29.7%`), plus explicit `2D` (`delta = 1`) vs `3D` (`delta = 2`) Selberg abscissa separation.
- Exact `Gate F-U3` `V_{CW}` UV sign verification (`+ln(Lambda^2/mu^2) Tr(H_f^2)`) and direct verification of `1560b2645:verify_found_v2_u3_v3_out.json` at `y = 6` (`[6, 0]` `-611.148 < -584.431` at `[4, 0]`).
- Exact `4D` signature classes modulo `g -> -g`: `3` physical classes `{(0,4), (1,3)~(3,1), (2,2)}`, unique Lorentzian class `{(1,3) ~ (3,1)}`.

### Module `OW18-E` (`Bridge B-3S-01` & `Synergy S-1` Three-Seat Harvest)
- **`Bridge B-3S-01` (`L_2(tau) + b_c^*(tau) == pi`):** Using a standalone `35`-dps `Order-24` Weierstrass-Taylor Fuchsian solver (`zero RK4 offset`), compute `L_2(tau)` at:
  1. `tau = i sqrt(3)`: confirm `pi - L_2(i sqrt(3)) = 0.654597772949...`, agreeing with `agy-exp` `X-SYNTHESIS-1` `2D` Liouville PDE Richardson extrapolate `0.65449431` within `2e-4`;
  2. `tau_0 = 13/100 + (17/10) i`: confirm exact `L_2(tau_0) = 2.45141225756...` vs `referee_a2_wg96.py`'s collapsed `1D` radial disk formula `pi - 1 - (1/2) ln(17 / (10 pi)) = 2.44864347098...`;
  3. `tau_8 = (16 + 8i)/5`: confirm exact `L_2(tau_8) = 2.5151881308899968867...`, matching `AGY-C27` to `< 2e-9`.
- **`Synergy S-1` (`|ker(gamma + I_2)| = t + 2` Lefschetz Kernel Reduction):** Independently enumerate all primitive hyperbolic `PSL(2, Z)` conjugacy classes with `3 <= t <= 30` (exact reduced `L, R` cyclic words), verify `151` primitive classes, prove `|ker(gamma + I_2)| = det(gamma + I_2) = t + 2` on `151 / 151` classes, verify `m004` `LR` (`t = 3`) kernel `span_{Z_5}((1/5, 2/5))` (`2` nonzero antipodal pairs) and `T^4 S` (`t = 4`) unique primitive order-`6` antipodal pair `+-(1/6, 1/6)` (`72 -> 2` antipodal pairs in `P_5 x P_6`, `7`-bit reduction).

### Module `OW18-F` (Planted Fault Controls — `6 / 6` Must Be Caught)
1. `PF-OW18-1`: Omit `-1` in `Delta(B - L) = -Delta L` -> flips `tau_*^-` matter selection back to antimatter `tau_*^+`.
2. `PF-OW18-2`: Copy `N_c = 3` (`-12`) onto `y_tau^5` in `2`-loop beta -> shifts `beta_{y_tau}^{(2)}` by `-9 y_tau^5`.
3. `PF-OW18-3`: Subtract `1` by hand from `dim C_{so(10)}(P_PS, J_5)` or omit Proca `-1/2` in `a_1` -> breaks rank-`5` / UV sign proof.
4. `PF-OW18-4`: Plug wrong Type-I sign `f_W = +2` instead of `-1/2` -> flips `M_g` from `-64` to `+56`.
5. `PF-OW18-5`: Use `+1` instead of `5^{-2} - 1 = -24/25` on `E[5]`-twisted `6D` `s = 3` modes -> flips `-3864/25` AdS maximum to false dS minimum.
6. `PF-OW18-6`: Use `Smith(+M + I_2)` for `-L^2 R` or drop `t + 2` kernel condition -> breaks `Smith = (1, 2)` and `72 -> 2` Lefschetz reduction.

## Pre-Registered Expectations (`A2-OW16 v5`: Honest `3 / 9 / 9 / 3 = 24` Ledger)
- `DERIVED_EXACT`: **`3`** (`OBS-01` `D = 4`, `OBS-02` Lorentzian class `{(1,3) ~ (3,1)}`, `OBS-07` `6D I_8` rank-`4` obstruction + `7D` CS `E/N = 8/3`).
- `CONDITIONAL_OR_QUALITATIVE`: **`9`** (`OBS-03` `G_SM x U(1)_X` + conditional `U(1)_X` breaking, `OBS-04` topological `N_gen = 3` without FRG uniqueness, `OBS-05` `4D` brane `2H` inside `E_6` `27_H`, `OBS-08` pure `PS` `r = 8/77`, `OBS-11` unimodular `a_0 = -64` decoupling, `OBS-12` CKM + `J_CP` ansatz, `OBS-13` `b-tau` proximity, `OBS-14` neutrino NO, `OBS-15` corrected `tau_*^-` leptogenesis + `eps1_raw` disclosure).
- `INTERNAL_WALL_OR_TENSION`: **`9`** (`OBS-06` untwisted vs `E[5]`-twisted `6D` `-3864/25` AdS wall, `OBS-09` Chimera RGE / `m_{A^0} = 0` / `yb_low` vs `yb_high` wall, `OBS-10` Proca `-50/3` / `-33/2` UV anti-gravity wall on `G_{ind}`, `OBS-16`..`OBS-21`).
- `OPEN_EXTERNAL_BOUNDARY`: **`3`** (`OBS-22`..`OBS-24`).
- **Zero literal boolean flags** (`guardrail5_anchor_limit_ok` computed dynamically from `len(anchors) <= 1`); `100%` of branch `SHA-256` manifests verified; all historical `false` JSON files explicitly enumerated; `6 / 6` planted faults caught.

0 of 19.
