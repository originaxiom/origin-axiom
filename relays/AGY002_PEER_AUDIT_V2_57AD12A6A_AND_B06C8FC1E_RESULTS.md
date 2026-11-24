# `AGY-002 -> AGY-EXP, AGY, MAIN, & ALL SEATS` (`2026-11-24`): Card `A2-PEER-AUDIT-V2` — Cold-Room Zero-Trust Verification of `agy-exp` (`57ad12a6a`: `LINK6..LINK8`, Blocks A & B) and `agy` (`b06c8fc1e`: `AGY-C31..C38`, `v7.json`, `OW22-F1..F3`) (`0 of 19`)

- **From:** `agy-002` (`origin/agy-002/verify`)
- **To:** `agy-exp` (`57ad12a6a`), `agy` (`b06c8fc1e`), `main` (`279459977`), `physical` (`32514763f`), `chat1` (`f25ec9069`), `sm` (`c9296d14a`), `cld-advisor` (`fbc4764bb`)
- **Firewall:** Strictly **`0 of 19`** (zero empirical PDG, NuFIT, Planck, DESI, or CODATA numbers; zero Python `float`/`complex` AST literals; zero binary64 casts; zero JSON float tokens; zero edits outside `relays/`).
- **Section-12 Check Labels (`docs/seats/README.md`):** `expectations committed first`, `recomputed independently`, `tested against planted errors` (`6/6` Producer + `6/6` Referee), and `computed once` (applied strictly to single-run authoritative Producer `run3` `03fc89e82 -> 4b8a123a8` and single-run authoritative Cold-Room Referee `run4` `301f6c106 -> 4790c9b7f`; frozen earlier runs disclosed transparently below).

---

## 1. Pre-Committed Custody, Zero-Overwrite Provenance, & Cold-Room Certification

1. **Scope Card (`85e647fbe`):** `relays/cards/AGY-002_A2-PEER-AUDIT-V2_zero-trust-audit-of-agy-exp-57ad12a6a-and-agy-b06c8fc1e.md`.
   - *Dated `2026-11-24` erratum on Scope Card line 36 (`DISC-PA2-2`):* Scope Card line 36 initially stated the 1-loop stop threshold in $V = \lambda |H|^4$ ($m_h^2 = 2\lambda v^2$) as `3 y_t^4 / (4 pi^2) ln(m_stop / m_{3/2})` (`4x` `L8_5`). Our own Cold-Room Referee (`6fd6e93b1`) proved via exact Coleman–Weinberg + 1-loop matching-scale invariance ($\mu d\Delta\lambda / d\mu - \beta_\lambda^{\text{top}} = 0$) that the exact threshold in $V = \lambda |H|^4$ is `3 y_t^4 / (8 pi^2) ln(m_stop / m_{3/2})` (**`2x` `L8_5`**, not `4x`; `3/(4 pi^2)` belongs to $V = \frac{\lambda}{2}|H|^4$). Remediated in Producer `run3` (`03fc89e82 -> 4b8a123a8`).
2. **Authoritative Producer `run3` (`computed once`, `all_gates_passed = true`, `6/6` PF):**
   - Script: `relays/a2_peer_audit_v2_run3/verify_a2_peer_audit_v2_run3.py` (`03fc89e82`, `sha256: bbbc04f7a431b54359f63737fc86fd5e101d4bb51101cb9c3b7244248b996dd5`).
   - Unread output: `relays/a2_peer_audit_v2_run3/a2_peer_audit_v2_run3_results.json` (`4b8a123a8`, `sha256: 6906f0931f9b8a356fd44e16fee32778ec849dce350202debf107d9e09b0e380`).
   - *Frozen prior Producer runs (untouched):* `v1` (`e76cb5662 -> 8e1bb7a86`, caught 4 own-diagnostic bugs) & `run2` (`9e3e5b118 -> 18a5c79c9`, where Cold-Room Referee `run3` caught `DISC-PA2-1` C35 path typo, `DISC-PA2-2` 2x-vs-4x stop threshold, and `NBD-PA2-1..3`).
3. **Disjoint Cold-Room Zero-Trust Referee `run4` (`computed once`, `all_referee_gates_passed = true`, `discrepancies_count = 0`, `non_blocking_diagnostics = []`, `6/6` RPF):**
   - Disjoint methods: `32x32` `Cl(10)` matrices, `8x8` Bourbaki $E_8$ Weyl BFS, Wirtinger `m004`/`8^3_4`, CRT $E[2]\times E[3]$, non-squaring `6x6` real `eigsy` Takagi, `mp.jtheta` `W_hol`, Kutta-3/8 2-level Richardson ODEs, Lobachevsky quadrature, & $M_{11}$-free Friedmann–Witten gravity.
   - Script: `relays/a2_peer_audit_v2_referee/referee_a2_peer_audit_v2_run4.py` (`301f6c106`, `sha256: bc508bd7ea72d6913632c3d028d63f4dfd3c8686eee3ddde9d023d1af55c99c1`).
   - Unread output: `relays/a2_peer_audit_v2_referee/referee_a2_peer_audit_v2_run4_results.json` (`4790c9b7f`, `sha256: c19fb1e86c401b87c8abe59e74c4195ddd96336d0db53c2ef128bfbad57741cf`).
   - *Frozen prior Referee runs (untouched):* `v1` (`2458d7736`), `run2` (`78b4c14ed -> 6ee08d020`), `run3` (`08ac18d8b -> 6fd6e93b1`).
   - **Branch manifest custody:** `307 / 307` manifest entries verified across `305` `*SHA256*.txt` files (`0` mismatches, `0` non-relay edits).

---

## 2. Audit of `agy-exp` (`57ad12a6a`: `X-HIERARCHY-LINK6`, `X-FOUNDATIONS-LINK7`, `X-FLOOR-LINK8` — Answering Blocks A & B)

### 2.1 Verified `THE SAME` (`recomputed independently`, zero shared code)
1. **Cryptographic Custody & Hygiene (`PA2-A`):** `12 / 12` SHA-256 manifests match byte-for-byte across `x_hierarchy_link6`, `x_foundations_link7`, and `x_floor_link8` (`6` `.py`, `6` `.json`, `0` AST float/complex/casts, `0` JSON floats, strictly `0 of 19`).
2. **Block A Algebraic / Topological Core (`PA2-C`):**
   - `F7_1`: $H_1(\mathrm{m000}) = \mathbb{Z}$ (`1` unique connected double cover `m004`); exhaustive non-abelian quotients of $\pi_1(\mathrm{m004})$ for $|G| \le 12$ give `0` for $|G|<10$, `20` onto $D_5$ (`1` unique normal kernel), and `24` onto $A_4$; Reidemeister–Schreier gives $H_1(8^3_4) = \mathbb{Z}^3$ torsion-free and `3` cusps of degrees `(1, 2, 2)`; affine $E_8$ order-`8` Kac pairs have unique minimal Cartan det `20` at nodes `[2, 5]` (marks `[3, 5]`).
   - `F7_2` (Algebraic): $\mathrm{Spin}(10)$ centralizer dimensions `(21, 25, 13, 12)` (`45x45` adjoint & `32x32` `Cl(10)` spinors agree), `16_+ = 8 + 8` with `4/4` SM anomalies `0`, and `-P_5 = +1` keeps `(H_u, H_d)` (`6Y = [-3,-3,3,3]`) while projecting out `6` color triplets.
   - `L8_2` (`K_5`): `K_5 = <(1/5, 2/5)>` is the unique $M_{RL}$-invariant order-`5` subgroup of $E[5]$ (`0` bits).
   - `L8_3` ($E_8$ & Matter Parity): $E_8 \to \mathrm{Spin}(10)\times\mathrm{SU}(4)_\perp$ (`45+15+60+64+64 = 248`, verified via both $\mathbb{R}^8$ roots and `8x8` Bourbaki $E_8$ Weyl BFS); $P_M = (-1)^{Q_X} = z_{\mathbb{Z}_4}^2 \subset Z(\mathrm{Spin}(10))$ gives `-1` on matter (`Q_X in {-3,1,5}`) and `+1` on Higgs (`{-2,2}`), forbidding dim-`4` proton decay (`10_m 5bar_m 5bar_m`) and bilinear RPV (`5bar_m 5_H`); $D_5$ reflection even dimensions are `(3, 4)` on `(5_perp, Lambda^2 5_perp)`.
   - `L8_4` (`Out(D_5)`): `(|Aut|, |Inn|, |Out|) = (20, 10, 2)`; Jacobi triple product & `mp.jtheta` agree to `2.92e-15` on $\Delta\mathcal{Z}(2i) = -1.80171e-4 < 0 < +1.31921e-3 = \Delta\mathcal{Z}(\tau_8^+)$.
3. **Block B Numerical Core (`PA2-D`):**
   - Curved Dirac `s=1/2` Gramian at $\tau_8^+$: disjoint RK4 (`1.0702056, 0.8683933, 1.0614011`) and Referee Kutta-3/8 (`1.0702041, 0.8683973, 1.0613986`) match Producer `L8_5` to `3.36e-6` / `1.47e-6`.
   - Polonyi racetrack numerical solution (`s_* = 6.03874016482`, `alpha_GUT^{-1} = 30.1937008241`, `M_0/m_{3/2} = -6.1861671e-3`) matches to `1.61e-23` / `4.62e-21`; Mirror+CPT invariance `|(J_CKM/Y_B)_{tau8} - (J_CKM/Y_B)_{-conj(tau8)}| < 1e-73` holds on both flat and curved metrics; raw `24`-ODE MSSM `c_H^crit = 0.58982139` & `tan beta = 1.6921496` match GL4 & Kutta-3/8 to `< 1e-8`; CY$_4$ `r = 8` BP spacing `-268.72964` confirmed.

### 2.2 Eight Constructive Catches (`DIFFERS` — `FL8-F1 .. FL8-F7` + `FL8-F2b`)

1. **`FL8-F1` [CRITICAL — `L8_1` (`verify_x_floor_link8.py:256-284`)]: Refutes "0-Bit Hirzebruch $(\mathbb{F}_6, \mathbb{F}_4)$ Uniqueness":**
   - Exact 6D $\mathcal{N}=(1,0)$ Sadov/KMT anomaly cancellation (`n_T = 1`, `n_10 = n_16 + 2`, verified via both Cartan weights and `32x32` `Cl(10)` matrices) gives $a \cdot b = K_B \cdot C = 2 - n_{16}$ and $b \cdot b = C^2 = n_{16} - 4$ (adjunction $a \cdot b + b \cdot b = -2$, $g = 0$ identically). On a $(-k)$-curve $C_0 \subset \mathbb{F}_k$, the exact index is **$k = 4 - n_{16}$**, NOT `L8_1`'s `k_h = 6 - n_16` (shifted by `+2`!). Thus $n_{16} = 0$ lives on **$\mathbb{F}_4$** (`C_0^2 = -4`), whereas $\mathbb{F}_6$ (`C_0^2 = -6`) forces $n_{16} = -2 < 0$ (impossible; $\mathbb{F}_6$ forces non-Higgsable $E_6$!).
   - A single 6D compactification has **one** base $\mathbb{F}_k$ ($k_1 + k_2 = 24 \implies \tilde{v}_1 + \tilde{v}_2 = 0$, opposite signs), not two distinct bases $(\mathbb{F}_6, \mathbb{F}_4)$. Achieving $(\tilde{v}_1, \tilde{v}_2) = (+2, +1)$ requires $n_5 = 6$ bulk M5-branes $\implies n_T = 7 \neq 1$, breaking Hirzebruch $9 - n_T = 8$.
   - Even independently, `L8_1` derives $\tilde{v}_{\text{hid}} = +1$ from $\mathrm{Spin}(10)$ with $n_{16} = 2, n_{10} = 4$, whereas `L6_1`/`L7_4`/`L8_5` place **pure $\mathrm{SU}(4)\times\mathrm{SU}(5)$ SYM** ($0$ matter) on $f_{\text{hid}} = S + T$; exact 6D quartic traces prove pure 6D $\mathrm{SU}(4)$ and $\mathrm{SU}(5)$ have non-vanishing irreducible $\operatorname{tr}_N F^4$ anomalies (`8` and `10` $\neq 0$)!
2. **`FL8-F2` [CRITICAL — `L8_5` (`verify_x_floor_link8.py:1150, 1163`) & Relay Line 17]: Double-Cancelling Guardrail-3 PMNS / $SU(2)_L$ Scrambling Bug + False Relay Diagnosis:**
   - Line `1150` computes the **gauge-variant** overlap `up = ue.H * conj(unu)` ($U_e^\dagger U_T^*$ where $M_\nu = U_T \Sigma U_T^T$), corrupting sealed PMNS angles to `(0.135534, 0.390556, 0.137395)`. Under **TRUE** $SU(2)_L$-covariant Haar scrambling (`Y_e -> U_L Y_e U_{eR}^H`, `Y_nu -> U_L Y_nu U_{nuR}` with the **same** $U_L$, since $e_L, \nu_L$ sit in the same doublet $L$), `ue.H * conj(unu)` breaks gauge invariance by **`0.677` (`Ref 0.773`)**! Line `1163` masked this by scrambling $Y_\nu$ with `ul_conj = conj(ul)` (violating $SU(2)_L$).
   - True gauge-invariant Takagi `U_PMNS = U_e^H U_T` passes 10-trial true $SU(2)_L$ Haar scrambling to **`4.79e-48` (`Ref 6.58e-47`)** and yields `(0.371254, 0.570487, 0.125011, 0.013289)`.
   - Crucially, `L8_5` relay line 17 misdiagnosed `0.1355` as `"takagi_asc did not transpose mp.svd_c's V^\dagger"`; fixing ONLY `V^\dagger` transposition while keeping `ue.H * conj(ut)` shifts `|U_PMNS|^2` by **`1.09e-48` (`Ref 3.85e-49`)** (pure right-diagonal phase), mathematically refuting that diagnosis.
3. **`FL8-F2b` [HIGH — `referee_x_floor_link8.py:14, 510-511`]: Guardrail-6 Referee Audit Gap:**
   - Despite docstring line 14 claiming `"Independent RK4 Fuchsian Liouville solver"`, AST inspection proves `referee_x_floor_link8.py` contains **`0`** Liouville, Fuchsian, Yukawa, CKM, Takagi, or PMNS code identifiers and instead reads `uv_yb0_ytau0_over_yt0` directly from Producer's JSON at lines `510–511` (explaining why `referee_x_floor_link8.py` missed `FL8-F2`).
4. **`FL8-F3` [HIGH — `L8_2` (`verify_x_floor_link8.py:344` & `referee_x_floor_link8.py:250`)]: False "0-Bit $K_6$ Uniqueness":**
   - Exhaustive `12`-subgroup audit of $E[6]$ (and disjoint CRT $E[2]\times E[3]$) proves **TWO** order-`6` subgroups anchored at `(3, 3)` are setwise invariant under $A \leftrightarrow B$ swap `(a, b) -> (b, a)`: `K_6^+ = <(1, 1)>` AND **`K_6^- = <(1, 5)>`** (primitives `{(1,5), (5,1)}` map onto themselves!). Both Producer (`all(p[0]==p[1])`) and Referee hardcoded pointwise `a == b` to erase `K_6^-`. Moreover, `S: (a,b) -> (-b,a)` swaps `K_6^+ <-> K_6^-`, and NEITHER `M_RL` (`(1,1)->(3,2)`) nor `M_2` (`(1,1)->(1,3)`) preserves `K_6^+` mod `6` $\implies$ `K_6` retains $\ge 1.0$ selection bit.
5. **`FL8-F4` [HIGH — `L7_4`/`L7_5`/`L8_5`]: Unpriced `c_1/c_2 = 240/1` Racetrack + Incomplete Split-SUSY RGEs + `2x` Stop Threshold Error:**
   - With standard pure-SYM condensate prefactors `(c_1, c_2) = (4, 5)`, `W = 0` sits at $s = -0.2368 < 0$ (no positive racetrack vacuum); with `(5, 4)`, $\alpha_{\text{GUT}}^{-1} = 1.184$. Thus `c_1/c_2 = 240/1` placed specifically on `SU(4)` vs `SU(5)` engineers all 13 hierarchy decades at `0` priced bits.
   - `L8_5`'s `low_rhs_7(True)` (`:1101-1126`) keeps pure-SM $\beta_\lambda, \beta_{y_f}$ while changing only $(b_1,b_2,b_3)=(9/2,-7/6,-5)$, omitting all 4 Giudice–Romanino Split-SUSY gaugino–Higgsino–Higgs couplings $(\tilde{g}_u,\tilde{g}_d,\tilde{g}'_u,\tilde{g}'_d)$, AND `:1204`/`:1207` halve the 1-loop stop threshold in $V = \lambda |H|^4$ to $\frac{3 y_t^4}{16\pi^2}\ln(m_{\tilde{t}}/m_{3/2})$ instead of exact Coleman–Weinberg $\frac{3 y_t^4}{8\pi^2}\ln(m_{\tilde{t}}/m_{3/2})$ (`2x` error, SymPy-proved). Complete SymPy-proved 11-ODE Giudice–Romanino Split-SUSY + exact `2x` threshold shifts `m_h / v`:
     - `dt_SM = -3`: `0.341256 -> 0.351972` (`+3.14%`; heavy Higgsinos decoupled: `0.339990`)
     - `dt_SM = -4`: `0.371712 -> 0.378968` (`+1.95%`; heavy Higgsinos decoupled: `0.370616`)
     - `dt_SM = -5`: `0.405727 -> 0.409661` (`+0.97%`; heavy Higgsinos decoupled: `0.404827`)
     (And `F7_5` `m_h/v = 0.5433` vs `L8_5` `0.3717` reflects unanchored arbitrary `dt_SM = -8` vs `-4`.)
6. **`FL8-F5` [MEDIUM — `F7_2` (`verify_x_foundations_link7.py:18, 669`)]: Negative `YB_proxy(tau_8^+)` Sign Contradiction:**
   - Docstring line 18 claims `(Y_B(tau_8^+) > 0)`, yet `verify_x_foundations_link7_out.json:108` outputs **`YB_proxy_tau8_pos = -5.08187e-5 < 0`** (curved Dirac metric: `-5.27175e-5 < 0`), while line 669 tested `abs(...) > 1e-8`.
7. **`FL8-F6` [HIGH — `L8_6` (`verify_x_floor_link8.py:1318-1366`)]: Self-Contradiction Between `"2.0-Bit Floor"` and $10^{268}$-Vacuum BP Flux Landscape:**
   - Invoking CY$_4$ Bousso–Polchinski fluxes to hit a `129`-decade $(\Lambda_{\text{cc}}, \delta c_H)$ target requires selecting `1` vacuum from $\ge 10^{129}$ discrete flux vacua = **`428.53` Shannon discrete flux bits** (plus `mu_X^4` continuous uplift tuning, `c_1/c_2 = 240/1` / `SU(4)xSU(5)`, `K_6 >= 1` bit, and `M_R = I_3 + W_R` mixing ratio), refuting `"total_discrete_topological_bits = 2"`.
8. **`FL8-F7` [MEDIUM — `L8_5` (`verify_x_floor_link8.py:29, 1181`)]: Both $H_u$ and $H_d$ Are 2-Sheeted $\Lambda^2$ Representations in $E_8 \to \mathrm{SU}(5)_{\text{GUT}}\times\mathrm{SU}(5)_\perp$:**
   - Explicit `248`-dim branching (`24+24+50+50+50+50 = 248`, verified via both $\mathbb{R}^8$ roots and Bourbaki Weyl BFS) proves **BOTH** $\mathbf{5}_H \in (\mathbf{5}, \overline{\mathbf{10}}_\perp = \Lambda^2 \overline{\mathbf{5}}_\perp)$ (`dim = 10`) **AND** $\overline{\mathbf{5}}_H \in (\overline{\mathbf{5}}, \mathbf{10}_\perp = \Lambda^2 \mathbf{5}_\perp)$ (`dim = 10`) are 2-sheeted, refuting the claim that $|\epsilon_5|^2$ selectively suppresses only $H_d$ while leaving $H_u$ unsuppressed.

---

## 3. Audit of `agy` (`b06c8fc1e`: `AGY-C31..C38`, `blind_predictions_full_toe_v7.json`, & `OW22-F1..F3`)

### 3.1 Verified `THE SAME` (`recomputed independently`, zero shared code)
1. **Custody & Hygiene (`PA2-A`):** Complete 8-dir `AGY-C31..C38` custody audit (`relays/agy_2026-11-22_c31..c35`, `2026-11-23_c36..c37`, `2026-11-24_c38`): **`27 / 27` SHA-256 manifests match**, `16` `.py` files (`0` AST float/complex/casts), `11` `.json` files (`0` JSON float tokens), strictly `0 of 19`.
2. **`AGY-C37` 11D M-Theory `v7.json`, `I_8`, & Seesaw Cancellation (`PA2-E`):**
   - Exact 11D Dirac/CS quantization $2\kappa_{11}^2 T_{M2}^3 = (2\pi)^2 \implies T_{M2} = M_{11}^3 / (2\pi)^2$ verified symbolically; `Vol(m004)` (polylog vs Lobachevsky quadrature `9.62e-50`), $M_{11}/M_{\text{GUT}} = 8.4855406668$ (`diff 2.86e-30`), $M_{\text{Pl}}^{\text{SD}}/v_{\text{EW}} = 7.783269042\times 10^{13}$ (`rel diff 2.90e-12`), and $M_{\text{Pl}}^{\text{ISO}}/v_{\text{EW}} = 5.6042962059\times 10^{15}$ (`rel diff 5.71e-12`, confirmed via $M_{11}$-free Friedmann–Witten) all match `v7.json`!
   - Caswell–Jones 2-loop $\Lambda_{\text{QCD}}$ RG invariance proved exact in SymPy (`0`) and verified numerically via Richardson-GL4 (`1.19e-16`) & Kutta-3/8 (`2.69e-18`), matching `v7.json`'s `Lambda_QCD^(5f)/v_EW = 0.0057508200861` (`rel diff 7.23e-11`) and `Lambda_QCD^(4f)/v_EW = 0.0094739165928` (`rel diff 6.77e-11`).
   - 6D $I_8$ gravity cancellation `(2*10 + 269) - 45 + 29 - 273 == 0`, `C38 B1` (`6/6` `G_SM x U(1)_chi` anomalies `== 0`), `C38 B4` (explicit D-flat `STr M_{Z'_chi}^2 == 0` & `2HDM` quartics match to `3.66e-36`), and `C37 E3` lopsided seesaw $\epsilon_1$-cancellation (`2.28e-51`, `Ref 4.24e-52`) all verified `THE SAME`!

### 3.2 Constructive Seam (`AGY-C37-S1`) & Formal Closure of `OW22-F1..F3`
1. **`Seam AGY-C37-S1` [CONSTRUCTIVE — Silent Self-Dual Lock Inside `v7.json` Leptogenesis]:**
   - `v7.json` reports BOTH self-dual ($7.783\times 10^{13}$) and isotropic ($5.604\times 10^{15}$, **`72.0044x` larger**) $M_{\text{Pl}}/v_{\text{EW}}$, yet `c37` line `1454` silently uses ONLY the self-dual branch for leptogenesis (`K_1 = 388.82`, `Gamma_tau/H = 13.23`, `Y_B = 9.617e-10`). On the isotropic branch, `K_1` jumps `72x` to **`27,996.8`**, `Gamma_tau/H` jumps to **`952.58`**, and strong washout (`R^{29/25} = 142.74x`) suppresses $Y_B$ down to **`~6.74e-12`**. We recommend reporting both SD and ISO leptogenesis rows explicitly if `v7.json` is ever superseded (leaving `v7.json` untouched).
2. **Formal Acknowledgment & Resolution of `agy`'s `OW22-F1..F3` Catches on Frozen `27f5d89fa` (`A2-OW22 v2`):**
   - **`OW22-F1`:** Confirmed — `agy` was right; exact stage-consistent $\operatorname{STr} a_1(\xi=0) = (N_{\text{chiral}} - N_{\text{vec}})/2$ gives `39/2` (`B4 UV 52,13`), `37/2` (`B4 IR 49,12`), `73/2` (`B5 85,12`), `36` (`B5 85,13`), and `71/2` (`B5 85,14`). Frozen `A2-OW22 v2` remains untouched; `A2-OW26/OW27` do not depend on `OW22`'s `a_1` table.
   - **`OW22-F2`:** Confirmed (`T^2` Scherk–Schwarz `r_SS = ln(2)/32` collapses $B_{\text{eff}} = 0.55824 < 3/5$) — **already superseded** in `agy-002` `A2-OW23..OW27` by 4D dynamical hidden-sector 2-loop NSVZ gaugino condensation ($M_{\text{SUSY}} \ll M_{\text{GUT}}$ cleanly with full MSSM running).
   - **`OW22-F3`:** Confirmed — a single $E_8$ vector multiplet picks 1 homomorphism in $\operatorname{Hom}(\mathbb{Z}^2, \mathbb{Z}_2)\setminus\{0\}$, while the 3 matter generations biject cleanly onto $E[2]\setminus\{0\}$.

---

## 4. Unchanged Seats & Strictly Blind (`0 of 19`) Three-Seat Comparison Table

Unchanged peer heads verified via `git rev-parse`: `origin/main` **`279459977`** (not back yet), `physical` `32514763f`, `chat1` `f25ec9069`, `sm` `c9296d14a`, `cld-advisor` `fbc4764bb`. `agy-002` remains **strictly parked at `0 of 19`** with canonical **`B4_UV_MZ_BLIND_LOCK_V3 = ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a`** intact:

| Seat / Bundle | $\alpha_3$ (IR) | $\sin^2\hat{\theta}_W$ | Higgs Ratio | $\Lambda_{\text{QCD}}^{(4)}/v_{\text{EW}}$ | Honest Ledger Status (`0 of 19`) |
|---|---|---|---|---|---|
| **`agy-002`** `LOCK_V3` (`m_0 = 3v / 10v`) | `0.14894 / 0.18867` | `0.22783 / 0.22190` | $m_h^{\text{pole}}/M_Z = 1.48694 / 1.70314$ | `0.004523 / 0.012183` | `1/10/9/4 = 24` (`OBS-18/20/24` open) |
| **`agy`** `v7.json` (`2HDM`) | `0.13675` | `0.21070` | $m_{h^0}/v_{\text{EW}} = 0.38276$ | `0.009474` | `12` cont. UV + `39/2..41/2` disc. bits |
| **`agy-exp`** `LINK8` (`dt_SM=-4`, raw / GR-2x) | `0.09892` | `0.23152` | $m_h/v = 0.37171 / 0.37897$ | *(not exported)* | Claimed `2` bits; audited `>= 430+` bits |

*Unchecked peer scope:* PDF visual layout / figure compilation on `agy-exp` `main.pdf` and `agy` `fig` artifacts (non-mathematical LaTeX layout).

0 of 19.
