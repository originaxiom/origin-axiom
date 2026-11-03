# HOSTILE REFEREE ZERO-TRUST AUDIT REPORT (`agy/audit-2026-11-02`)

- **Date:** 2026-11-03
- **Role:** Independent Zero-Trust Hostile Referee
- **Branch Audited:** `agy/audit-2026-11-02`
- **Target Files Audited:**
  - `relays/AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md` (Relay 1)
  - `relays/AGY_TO_CC_2026-11-02_ELEVATION_PLAN_AND_OPERATOR_GATE_EXECUTED.md` (Relay 2)
  - `src/origin_axiom/twisted_norms.py`
  - `src/origin_axiom/operator_gate.py`
  - `src/origin_axiom/stepb_audit.py`
  - `src/origin_axiom/parameter_ledger.py`
  - `tests/test_elevation_operator_gate.py`
  - `relays/agy_audit_2026_11_02/verify_twisted_norms_and_quaternion_yukawa.py`
  - `relays/agy_audit_2026_11_02/verify_stepb_and_census_audit.py`
- **Independent Referee Script & Output:**
  - `relays/agy_audit_2026_11_02/hostile_referee_audit.py`
  - `relays/agy_audit_2026_11_02/hostile_referee_audit_results.json`

---

## Executive Scorecard Across All 24 Audited Claims

| ID | Audit Area & Specific Claim | Referee Verdict | Summary of Independent Finding |
| :--- | :--- | :--- | :--- |
| **1.1** | `B1825` best-address $\chi^2_{\text{ten}}$ breakdown ($\chi^2_{\text{ten,fresh}} = 291.486662$, $\chi^2_{\text{six}} = 63.6450$, $\chi^2_{|V_{ub}|} = 158.8123$, $\chi^2_{|J|} = 51.3726$, $72.11\%$ in $|V_{ub}| + |J|$) | `VERIFIED EXACT (NOT FABRICATED)` | Recomputed from scratch via `scripts/stepb/stepb_core.py` + `b1656_funcs.py` to $|\Delta| = 0.00 \times 10^0$ against `run.json`. |
| **1.2** | Relay 1 §1.1 prose quotes for `run.json` (`L_six: 23.467113`, `C_six: 9.162624`, `bits_CKM: -206.202854`, `C_ten: -197.040229`, `least_chi2_nine: 82.600158`) | `REFUTED / FABRICATED` *(Stale Prose vs `run.json`)* | While `verify_stepb_and_census_audit_results.json` recorded the true `run.json` values, Relay 1 lines 22–24 printed stale numbers! In `run.json` lines 47–50, `C_six = -3.079845` bits (**negative**: the six do **not** compress), NOT `+9.162624` bits! |
| **1.3** | Lagrange multiplier compromise $(c_u, c_c, c_b) = (K^{-1/3}, K^{-1/3}, K^{+1/3}) = (0.7347, 0.7347, 1.3611)$ under $c_u c_c / c_b = 1/K$ | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | Exact for equal-weight log-space penalty ($K = 2.521302 \implies (0.734725, 0.734725, 1.361053)$). **Caveats:** (a) Relay 1 line 140 mis-rounded the last digit to `(0.7348, 0.7348, 1.3609)` (fixed in `operator_gate.py`); (b) weighting by $1/\sigma_i^2$ from `T9_LOCKED` shifts the compromise to $(0.741421, 0.733759, 1.372038)$. |
| **2.1** | Defect 4A Part 1: `choice = 30900` decodes to `((2/5, 0), D2R, L_max, ('S~', 'S', 'S'))` with $J = 0$ and `physical_choice[30900] == False` | `REFUTED / FABRICATED` *(Bug Exposed in `stepb_audit.py`)* | **`stepb_audit.py` line 29 used the wrong `KEPT_DIRECTIONS` ordering**, placing `"D2R"` at index 11! In `cm_zero_line.py` line 37 + `census_io.py`, index 6 (`"F_-2"`) is dropped and the 12th kept direction (`d_pos=11, d=12`) is **`"F_26"`**, NOT `"D2R"`. On `((2/5, 0), F_26, L_max, ('S~', 'S', 'S'))`, $|J| = 3.128 \times 10^{-4} \ne 0$ and `physical_choice[30900]` is **`True`**! |
| **2.2** | Defect 4A Part 2: `scripts/stepb/kten.py` line 172 calls `windowed(..., physical=False)` and lines 202–203 ignore `m["choice"] = 30900` when computing `lp_post` | `VERIFIED EXACT (NOT FABRICATED)` | Confirmed in `scripts/stepb/kten.py`: `six_mixture` omits `physical=True`, and `K_ten` sums `num` and `den` over all `29,063` rows instead of filtering to `m["choice"]`. |
| **2.3** | Two dead directions in `B1825` (`113,312` rows each with $J = 0$) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | The two dead directions in `census_structure.json` are **`R` (`d=2`) and `t=-5/288` (`d=3`)**, both of which satisfy $\vec{a}(\tau)\cdot\vec{a}(\tau) \equiv 0$ identically in `qseries.py`, forcing $\det Y_s = 0$ and $J = 0$ (whereas `stepb_audit.py` mislabeled `t=-5/288` as `D2R`). |
| **2.4** | Defect 4B: `48` order-12 lines (`7,680` choices = $19.2\%$ of `choices_physical = 40,000`) have $\det M_{\text{lep}} = 0$ ($m_e = 0$) yet pass `cells.py` | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | $48 \times 10 \times 2 \times 8 = 7,680$ ($19.2\%$ of $40,000$) is exact. **Caveat:** `parameter_ledger.py` line 145 and Relay 2 line 112 also cite `"36/5832"`, which comes from an older 5,832-row table rather than `B1825`'s 50,880-choice census. |
| **2.5** | Defect 4C: 2:1 CKM duplication across lepton readings (`S` vs `S~`) inflates `bits_CKM` sample size by $2\times$ | `VERIFIED EXACT (NOT FABRICATED)` | Confirmed in `scripts/stepb/stepb_core.py`: `V_CKM` depends only on `(r_u, r_d)` and is bitwise identical across `r_l in {0, 1}`. |
| **2.6** | Defect 4D: `the_exponents.py` executes entire workflow at import time; `F_-10` has `42,394` undefined rows; `F_6..F_26` collapse toward `a0` at $\text{Im}\,\tau \ge 2.5$ | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | Exact row decomposition in `run.json`: $610,560 - 341,526 = 269,034 = 113,312\,(R) + 113,312\,(t=-5/288) + 42,394\,(F_{-10}) + 16\,(DR)$. **Caveat:** In `verify_stepb_and_census_audit_results.json`, `r_num` was computed in `mpmath` before casting to `float`, so it returned $2.25 \times 10^{-28}$ rather than underflowing to `0.0`, though in IEEE-754 `float64` $1 + 2.25 \times 10^{-28} == 1.0$ to machine precision. |
| **3.1** | Theorem 1 (`closed_form_cA` in `twisted_norms.py`): 1D strip Parseval + Euler digamma + Hurwitz–Lerch closed form matches `b1656_funcs.py` `cA` and `cB` | `VERIFIED EXACT (NOT FABRICATED)` | Tested on 10 fresh adversarial/boundary cases ($\alpha = 0, 1/6, 1/3, 1/2, 5/8, 7/9$ and orders $8, 9, 11$): max $|\Delta| = 2.84 \times 10^{-12}$ vs `cA` and $9.83 \times 10^{-9}$ vs `cB`. Handles $\alpha = 0$, $\alpha = 1/2$, $\alpha > 1/2$, and returns `None` when $R_s = 0$. |
| **3.2** | Theorem 1 (`sector_higgs_twist_multiple`): $100\%$ sector independence of $c_s(\tau, w)$ across `up`, `down`, `lepton` via $|q_L + q_R| = 3$ | `VERIFIED EXACT (NOT FABRICATED)` | Max spread across `up`, `down`, `lepton` in `b1656_funcs.py` across all 10 adversarial test points is $5.46 \times 10^{-12}$ (quadrature tolerance). |
| **3.3** | Theorem 1 (`cusp_combination_D_inf`): $D^\infty(\alpha) = 0$ on $(0, 1/2)$ with $3\alpha \notin \frac{1}{2}\mathbb{Z}$ iff $\alpha \in \{1/12, 1/4, 5/12\}$ | `VERIFIED EXACT (NOT FABRICATED)` | Follows from strict monotonicity of $\psi(x) + \psi(1-x)$ on $(0, 1/2]$; on $(0, 1)$ the roots are $\{1/12, 1/4, 5/12, 7/12, 3/4, 11/12\}$. |
| **3.4** | Theorem 1 (`channel_pair_decay_exponents`): $E(c_1 - c_i) = \frac{1}{2}\|3\alpha\|_{\mathbb{Z}}$, $E(c_j - c_k) = \frac{1}{4} - E(c_1 - c_i)$ | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | Holds for generic $(\text{Re}\,\tau, b)$, but **two unstated mathematical exceptions were exposed**: (a) when $3\alpha \in \mathbb{Z}$ (e.g. $\alpha = 1/3$) and $\cos(6\pi b) = 0$ (e.g. $b = 1/12$), flipping $\eta \mapsto -\eta$ swaps $w_p \leftrightarrow w_m$ for all $n \ge 1$ and preserves $|1 + \eta e^{-6\pi i b}|^2 = 2$, so $c_1(\tau) - c_i(\tau) \equiv 0$ **identically for all $\tau \in \mathbb{H}$** (not $E = 0$); (b) on vertical phase slices where $\nu\,\text{Re}\,\tau - 3b \in \frac{1}{2}\mathbb{Z} + \frac{1}{4}$, the $(n=0, \nu)$ branch has purely imaginary odd powers and vanishes, jumping the decay exponent from $\nu/2$ to $(1-\nu)/2$ (e.g. $0.10 \to 0.40$ at $\alpha = 2/5, \text{Re}\,\tau = 0.35, b = -3/50$), or $c_1 - c_i \equiv 0$ identically when $\text{Re}\,\tau \in \frac{1}{2}\mathbb{Z}$. |
| **4.1** | Theorem 2 (`quaternionic_4d_yukawa` vs `direct_quaternion_coupling`): exact $3\times 3$ matrix representation of 4D quaternion multiplication | `VERIFIED EXACT (NOT FABRICATED)` | Verified on 200 fresh random complex 4D quaternions and symmetric $(m_1, \vec{m}_\perp)$ tensors to max error $2.66 \times 10^{-15}$. |
| **4.2** | Theorem 2 ($a_0 = 0$ CKM Corner-Inversion No-Go Theorem across all 8 readings) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | Relay 1 §3.2's proof assumes `up` and `down` share the same Higgs vector $\vec{h}_u = \vec{h}_d$ (same-reading pairs `SS` and `S~S~`, where $u_1^{(u)} \approx u_1^{(d)} \approx \hat{h}^*$ gives $|V_{ud}| = 0.979$ and $|V_{ub}|/|V_{td}| = 11.28$). For **mixed quark readings (`S~S` and `SS~`)**, $\vec{h}_d = \vec{h}_u^*$; on the null cone $\vec{h}\cdot\vec{h} \to 0$, $u_1^{(u)} \to \hat{h}^*$ and $u_1^{(d)} \to \hat{h}$ become **nearly orthogonal** ($\langle \hat{h}^*, \hat{h}\rangle = r \ll 1$), collapsing $|V_{ud}| \to 0.099$ (or $0.0175$ at small $r$) and $|V_{cb}| \to 0.989$! Thus all 8 readings fail at $a_0 = 0$: same-reading pairs by corner inversion, mixed-reading pairs by $(1,1)/(2,3)$ permutation collapse. |
| **5.1** | Theorem 3 (`theorem3_determinant_factorization`): $\det Y_s^{\text{4D}} = (a_0^2 + \vec{h}\cdot\vec{h})(m_1^2 + \vec{m}_\perp\cdot\vec{m}_\perp)(a_0 m_1 + \vec{h}\cdot\vec{m}_\perp)$ | `VERIFIED EXACT (NOT FABRICATED)` | Verified symbolically and on 200 fresh random complex trials to max relative error $7.51 \times 10^{-15}$. |
| **5.2** | Theorem 4 (`serre_dr_dot_dr_eta6_identity`): $DR\cdot DR = -R\cdot D^2R = \frac{1}{4}\eta(\tau)^6$ | `VERIFIED EXACT (NOT FABRICATED)` | Verified in **exact rational arithmetic** via `qseries.py` through $x^{240} = q^{30}$ (every rational coefficient of $DR\cdot DR - \frac{1}{4}\eta^6$ and $DR\cdot DR + R\cdot D^2R$ is identically `0/1`) and numerically across 20 random $\tau \in \mathbb{H}$ to $1.11 \times 10^{-13}$. |
| **6.1** | `m004` algebraic invariants (`det(LR - I) = -1`, $\|\Delta_{\text{m004}}(\omega)\| = 4$, $\|\tau_{\text{RS}}(\text{m004}; \omega)\| = 4/\sqrt{3}$) | `VERIFIED EXACT (NOT FABRICATED)` | Confirmed by direct matrix arithmetic on $LR = \begin{pmatrix}2&1\\1&1\end{pmatrix}$. |
| **6.2** | `m004` 3-fold cover $M_3 \to \text{m004}$ deck-group commutant claim (`commutant_dim == 1` in `operator_gate.py` line 224) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | **Crucial Group-Theoretic Distinction Exposed:** The pure 3-sheet deck permutation group $S_3 = \langle C_3, P_{\text{perm}}\rangle$ with $P_{\text{perm}} = \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$ (order 6) decomposes $\mathbb{R}^3 = \mathbf{1} \oplus \mathbf{2}_E$ and has a **2-dimensional** commutant $H = a I_3 + b J_3$ (allowing democratic mixing $b \ne 0$, as proved in `B1822` §3 Row 4). `operator_gate.py` line 224 obtained `commutant_dim == 1` ONLY because it defined `p_refl = [[1,0,0],[0,0,-1],[0,-1,0]]`, which multiplies $P_{\text{perm}}$ by the $\mathbb{Z}_2 \times \mathbb{Z}_2$ quaternion character sign flip $\text{diag}(1,-1,-1)$, generating the **24-element octahedral group $S_4 = (\mathbb{Z}_2 \times \mathbb{Z}_2) \rtimes S_3$** (`B1822` §3 Row 6: *"characters plus the order-3 automorphism | 1"*, not bare sheet permutation alone). |
| **7.1** | `evaluate_operator_gate("FR-COV")` CKM numbers at $a_0 = 0.20\,e^{7\pi i/8}$ ($|V_{ub}|/|V_{td}| = 0.6778$, $\sin\delta_{\text{CP}} = 0.6997$, $|J| = 5.43 \times 10^{-5}$) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | The CKM numbers at $a_0 = 0.20\,e^{7\pi i/8}$ on `B1825`'s address are numerically exact, **HOWEVER**: (a) $a_0 = 0.20\,e^{7\pi i/8}$ is a **hand-picked 2-real-parameter complex witness**, NOT the parameter-free canonical scalar $a_0(\tau) = \frac{1}{2}\eta(\tau)^3$ (which has modulus $0.05801$ at $\text{Im}\,\tau = 2.7426$, giving $|V_{ub}|/|V_{td}| = 5.8205$ and $\chi^2_{\text{ten}} = 510.90$); (b) at $a_0 = 0.20\,e^{7\pi i/8}$, $m_c/m_t$ jumps from $0.00455$ to $0.03816$ ($\chi^2_{c/t} = 507.33$), $m_e/m_\tau$ degrades to $\chi^2_{e/\tau} = 637.49$, and $|V_{us}|$ drops to $0.11158$ ($\chi^2_{|V_{us}|} = 49.15$), driving the **full 10-observable $\chi^2_{\text{ten}}$ from $291.49$ to $2029.24$**! |
| **7.2** | Reading mismatch between `operator_gate.py` (`S~S~S`) and `parameter_ledger.py` line 84 (`S~SS`) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | `parameter_ledger.py` line 84 states $U(1)_Y$ gauge invariance locks the reading to `S~SS` (`(1, 0, 0)`), whereas `operator_gate.py` evaluated `FR-COV` on `B1825`'s reading `S~S~S` (`(1, 1, 0)`). Evaluating $a_0 = 0.20\,e^{7\pi i/8}$ on `S~SS` at `B1825`'s address gives $|V_{cb}| = 0.9513$ and $\chi^2_{\text{ten}} = 6571.36$. |
| **7.3** | Torsion-line reduction $266 \to 6$ (`Fix((LR)^3)` vs `B1825`'s `(3/8, 3/8)` and `B1726`'s `(2/5, 1/10)`) | `VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED` | $\ker((LR)^3 - I) \cong (\mathbb{Z}/4\mathbb{Z})^2$ yields $5$ non-zero $\langle T, -I\rangle$-orbits of orders $2$ and $4$, plus $1$ projective order-5 eigen-orbit $(2/5, 1/5)$ ($5 + 1 = 6$; note `parameter_ledger.py` line 82 comment says `"4 + 1 = 5"` while code line 87 computes `5 + 1 = 6`). **Crucially, neither `B1825`'s order-8 line $(3/8, 3/8)$ nor `B1726`'s order-10 line $(2/5, 1/10)$ lies in `Fix((LR)^3)`.** |

---

## Detailed Findings by Audit Area

### Area 1: `B1825` Readout Audit & Lagrange Multiplier CKM Compromise

1. **Best-Address Observable & $\chi^2$ Breakdown (`VERIFIED EXACT (NOT FABRICATED)`):**
   - Independently running `scripts/stepb/stepb_core.py` and `b1656_funcs.py` at `B1825`'s readout address (`line = (3/8, 3/8)`, `direction = DR`, `radius = L_2`, `reading = ('S~', 'S~', 'S')`, $\tau = 0.093359375 + 2.742578125i$) reproduces `run.json`'s `chi2_ten_fresh = 291.4866623550638` to machine zero ($|\Delta| = 0.0$).
   - The per-observable $\chi^2$ contributions are:
     - Six mass ratios: $\chi^2_{\text{six}} = 63.644970$ ($\chi^2_{c/t} = 4.1583$, $\chi^2_{u/t} = 33.7259$, $\chi^2_{s/b} = 8.2313$, $\chi^2_{d/b} = 3.2476$, $\chi^2_{\mu/\tau} = 13.8359$, $\chi^2_{e/\tau} = 0.4460$).
     - Four CKM observables: $\chi^2_{\text{CKM}} = 227.841692$ ($\chi^2_{|V_{us}|} = 1.0840$, $\chi^2_{|V_{cb}|} = 16.5728$, $\chi^2_{|V_{ub}|} = 158.812292$, $\chi^2_{|J|} = 51.372646$).
     - $|V_{ub}|$ and $|J|$ account for $(158.812292 + 51.372646) / 291.486662 = 72.1079\%$ of the total $\chi^2_{\text{ten}}$.

2. **Prose vs `run.json` Discrepancies in Relay 1 Lines 22–24 (`REFUTED / STALE PROSE NUMBERS EXPOSED`):**
   - While `relays/agy_audit_2026_11_02/verify_stepb_and_census_audit_results.json` stored the exact numbers from `run.json`, the narrative prose in `relays/AGY_TO_CC_2026-11-02_FULL_AUDIT_BLIND_SPOTS_AND_REFRAMING.md` lines 22–24 contains stale/mismatched numbers:

| Metric in `B1825` `run.json` | True `run.json` Value | Relay 1 Prose (Lines 22–24) | Discrepancy |
| :--- | ---: | ---: | ---: |
| `readout_least_chi2_nine` | `82.6047634064222` (`a0`) | `82.600158 (at F_26)` | `-0.004605` (wrong direction label) |
| `K.L_six` (bits) | `36.8289582678940` | `23.467113` | `-13.361845` bits |
| `K.C_six` (bits) | **`-3.0798445035254`** | **`+9.162624`** | **`+12.242469` bits (sign flip!)** |
| `K.bits_CKM` (bits) | `-193.9567150989045` | `-206.202854` | `-12.246139` bits |
| `K.C_ten` (bits) | `-197.0365596024299` | `-197.040229` | `-0.003669` bits |
| `min_chi2_six` | `1.3582125046184` | `1.358308` | `+0.000095` |

   - Most importantly, in `run.json` line 48, `C_six = 33.749114 - 36.828958 = -3.079845` bits is **negative** (even the six mass ratios do not compress against the prior in cell `K`), whereas Relay 1 line 23 printed `C_six: 9.162624 bits`.

3. **Lagrange Multiplier Compromise (`VERIFIED WITH CAVEAT`):**
   - Minimizing $(\ln c_u)^2 + (\ln c_c)^2 + (\ln c_b)^2$ subject to $\ln c_u + \ln c_c - \ln c_b = -\ln K$ yields $c_u = c_c = K^{-1/3}$ and $c_b = K^{+1/3}$.
   - For $K = (0.22501 \times 0.04183) / 0.003732 = 2.521302$, $K^{-1/3} = 0.734725$ and $K^{+1/3} = 1.361053$ (matching `operator_gate.py`'s `(0.7347, 0.7347, 1.3611)`; note Relay 1 line 140 had a 1-digit rounding slip `(0.7348, 0.7348, 1.3609)`).
   - If weighted by $1/\sigma_i^2$ from `T9_LOCKED` ($\sigma_{|V_{us}|} = 0.10004$, $\sigma_{|V_{cb}|} = 0.10180$, $\sigma_{|V_{ub}|} = 0.10293$), the optimum shifts slightly to $(c_u, c_c, c_b) = (0.741421, 0.733759, 1.372038)$.

---

### Area 2: `Step B` Code Defects (`scripts/stepb/` and `src/origin_axiom/stepb_audit.py`)

1. **Defect 4A Part 1 — Decoding of `choice = 30900` (`REFUTED / BUG EXPOSED IN stepb_audit.py`):**
   - In `src/origin_axiom/stepb_audit.py` line 29, `agy` defined:
     `KEPT_DIRECTIONS = ("DR", "a0", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26", "F_-6", "F_-10", "R", "D2R")`,
     placing `"D2R"` at index `d_pos = 11`.
   - However, in untouched `main`-branch `frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py` line 37, the 13 census directions are indexed in the order:
     `DIRS = ["DR", "a0", "R", "t=-5/288", "F_-10", "F_-6", "F_-2", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26"]`.
   - When `scripts/stepb/census_io.py` line 18 drops index `6` (`DROP_DIRECTION_INDEX = 6`, which is `"F_-2"`) and maps the remaining 12 integer indices in ascending order via `np.searchsorted(kept_d, d)`, the 12 kept directions are:
     `("DR", "a0", "R", "t=-5/288", "F_-10", "F_-6", "F_6", "F_10", "F_14", "F_18", "F_22", "F_26")`.
   - Therefore, for `choice = 30900` (`l = 160 -> (2/5, 0)`, `d_pos = 11`, `rad = 1 -> L_max`, `r_idx = 4 -> ('S~', 'S', 'S')`), the true direction at `d_pos = 11` (`d = 12`) is **`"F_26"`**, NOT `"D2R"`!
   - Direct evaluation of `((2/5, 0), F_26, L_max, ('S~', 'S', 'S'))` at $\tau = 0.08 + 2.50i$ gives $|J| = 3.1276 \times 10^{-4} > 10^{-30}$, so **`choice = 30900` IS a physical choice (`physical_choice[30900] == True`)**!
   - Meanwhile, what ARE the two dead directions (`113,312` rows each with $J = 0$) in `census_structure.json`? They are `d = 2` (`"R"`) and `d = 3` (`"t=-5/288"`), where `"t=-5/288"` is $D^2R - \frac{5}{288}E_4 R$. In exact rational `qseries.py` arithmetic, BOTH $\vec{R}\cdot\vec{R} \equiv 0$ AND $(D^2R - \frac{5}{288}E_4 R)\cdot(D^2R - \frac{5}{288}E_4 R) \equiv 0$ identically! By Theorem 3 at $a_0 = 0$, $\vec{a}\cdot\vec{a} \equiv 0 \implies \det Y_s = 0$, forcing $m_1 = 0$ and locking $u_1^{(u)} = u_1^{(d)} = \hat{a}^*$, which makes $V_{\text{CKM}} = 1 \oplus U(2)$ and $J \equiv 0$.

2. **Defect 4A Part 2 — `scripts/stepb/kten.py` Lines 172 & 202–203 (`VERIFIED EXACT (NOT FABRICATED)`):**
   - In `scripts/stepb/kten.py` line 172, `six_mixture` calls `windowed(arrays, ..., physical=False)`, omitting the `physical=True` filter that `nine_mixture` uses on line 140.
   - And in `K_ten` (lines 182–205), `m = six_mixture(...)` returns `m["choice"] = 30900`, but lines 202–203 compute `num = float(np.sum(w * p))` and `den = float(np.sum(w))` over **all `29,063` rows in the $\tau$-window across all choices**, completely ignoring `m["choice"]`!

3. **Defect 4B — `48` Order-12 Lines (`7,680` Massless-Electron Choices in `choices_physical = 40,000`) (`VERIFIED WITH CAVEAT`):**
   - Out of the $266$ $\langle T, -I\rangle$-reduced torsion lines of order $N \le 12$, exactly $48$ have order $12$ and satisfy $3w \in (\frac{1}{2}\mathbb{Z})\tau + \frac{1}{2}\mathbb{Z}$, where a channel residue $R_s$ vanishes and $M_{\text{lep}}$ is rank-2 ($\det M_{\text{lep}} = 0 \implies m_e = 0$).
   - Because `scripts/stepb/cells.py` line 144 checks only the 4 CKM columns `np.all(F[:, 6:10] > math.log(FLOOR), axis=1)`, all $48 \times 10 \times 2 \times 8 = 7,680$ non-null-direction choices on those 48 lines ($19.2\%$ of `choices_physical = 40,000`) are admitted into `physical_choice`.
   - *Caveat:* `parameter_ledger.py` line 145 and Relay 2 line 112 also mention `"36/5832"`, which comes from an older 5,832-row table rather than `B1825`'s 50,880-choice census.

4. **Defect 4C & 4D (`VERIFIED WITH CAVEAT`):**
   - `V_CKM` is independent of the lepton reading `r_l in {0, 1}`, duplicating every CKM vector 2:1 in `bits_CKM`.
   - `the_exponents.py` has no `if __name__ == "__main__":` guard and runs at import time.
   - In `run.json`, `rows - rows_defined = 610,560 - 341,526 = 269,034 = 113,312 (R) + 113,312 (t=-5/288) + 42,394 (F_-10) + 16 (DR)` is exact to the single row.

---

### Area 3: Theorem 1 — Closed-Form $c_s(\tau, w)$ (`src/origin_axiom/twisted_norms.py`)

1. **Adversarial Verification Against `b1656_funcs.py` `cA` and `cB` (`VERIFIED EXACT (NOT FABRICATED)`):**
   - Across 10 fresh adversarial and boundary cases (`(3/11, 7/11)`, `(2/9, 5/9)`, `(1/8, 5/8)` at negative $\text{Re}\,\tau$, boundary $\alpha = 0$ on `(0, 2/5)`, integer-twist $\alpha = 1/3$ on `(1/3, 1/7)`, half-integer twist $\alpha = 1/6$ on `(1/6, 1/5)`, boundary $\alpha = 1/2$ on `(1/2, 1/3)`, $\alpha > 1/2$ on `(5/8, 3/8)` and `(7/9, 2/9)`, and degenerate $R_i = 0$ on `(1/3, 1/6)`), `closed_form_cA` matches `b1656_funcs.py` Route A (`cA`) to max absolute error **$2.84 \times 10^{-12}$** and Route B (`cB`) to **$9.83 \times 10^{-9}$** (limited only by numerical quadrature accuracy in `b1656_funcs.py`), with a $\sim 3900\times$ speedup.
   - `closed_form_cA` properly handles $\alpha = 0$, $\alpha = 1/2$, and $\alpha > 1/2$ via `nu_frac = (3 * a_frac + a_s) % 1`, and accurately returns `None` whenever a channel residue vanishes ($|1 + \eta_s e^{-6\pi i b}|^2 = 0$ at $\nu_s = 0$).

2. **Two Mathematical Caveats Exposed on `channel_pair_decay_exponents(alpha)` (`VERIFIED WITH CAVEAT EXPOSED`):**
   - **Caveat 3A (Identical vanishing when $3\alpha \in \mathbb{Z}$ and $\cos(6\pi b) = 0$):** When $3\alpha \in \mathbb{Z}$ (e.g. $\alpha = 1/3$, where $\nu_1 = \nu_i = 0$), `channel_pair_decay_exponents(1/3)` returns $E(c_1 - c_i) = 0$ (linear growth in $\text{Im}\,\tau$). However, whenever $\cos(6\pi b) = 0$ ($6b \in \mathbb{Z} + 1/2$, e.g. $b = 1/12, 1/4$), $e^{-6\pi i b} = -e^{+6\pi i b} = \mp i$. Flipping $\eta_s \mapsto -\eta_s$ between channel `1` ($\eta = -1$) and channel `i` ($\eta = +1$) swaps $w_p \leftrightarrow w_m$ for **every** $n \ge 1$ and leaves $|1 + \eta_s e^{-6\pi i b}|^2 = 2$ invariant! Consequently, at $\alpha = 1/3, b = 1/12$,
     $$c_1(\tau, \tfrac{1}{3}\tau - \tfrac{1}{12}) - c_i(\tau, \tfrac{1}{3}\tau - \tfrac{1}{12}) = 0 \quad \text{identically for ALL } \tau \in \mathbb{H}!$$
   - **Caveat 3B (Nodal vertical slices in $\text{Re}\,\tau$):** For $3\alpha \notin \frac{1}{2}\mathbb{Z}$, the $(n=0, \nu)$ branch has phase $\nu\,\text{Re}\,\tau - 3b$. Along vertical lines where $\nu\,\text{Re}\,\tau - 3b \in \frac{1}{2}\mathbb{Z} + \frac{1}{4}$:
     - If $\text{Re}\,\tau \in \frac{1}{2}\mathbb{Z}$ (e.g. $\text{Re}\,\tau = 0, b = 1/12$, or $\text{Re}\,\tau = 1/2, \alpha = 2/5, b = -1/20$), both $w_p$ and $w_m$ are purely imaginary for all $n \ge 0$, so $c_1(\tau) - c_i(\tau) \equiv 0$ **identically for all $\text{Im}\,\tau > 0$**!
     - If $\text{Re}\,\tau \notin \frac{1}{2}\mathbb{Z}$ (e.g. $\text{Re}\,\tau = 0.35, \alpha = 2/5, b = -3/50$), the entire $(n=0, \nu=1/5)$ branch has purely imaginary odd powers and vanishes, so the cusp decay exponent jumps from $E = \nu/2 = 0.10$ to $E' = (1-\nu)/2 = 0.40$ (measured $0.39968$ between $\text{Im}\,\tau = 2$ and $3$).

---

### Area 4 & 5: Theorems 2, 3, and 4 (`src/origin_axiom/operator_gate.py`)

1. **Theorem 2 — 4D Quaternionic Yukawa Representation (`VERIFIED EXACT (NOT FABRICATED)`):**
   - Across 200 fresh random complex 4D quaternions $a = (a_0, \vec{h})$ and symmetric $M$, `quaternionic_4d_yukawa` matches `direct_quaternion_coupling` to max absolute error **$2.66 \times 10^{-15}$**, and $Y_h^\dagger Y_h = (\|\vec{h}\|^2 I_3 - \vec{h}\vec{h}^\dagger)^T$ holds to **$8.88 \times 10^{-15}$**.

2. **Theorem 2 — $a_0 = 0$ CKM Failure Across All 8 Readings (`VERIFIED WITH CAVEAT EXPOSED`):**
   - Relay 1 §3.2 proves that at $a_0 = 0$, $u_1^{(s)} \to \hat{h}_s^*$ as $r = |\vec{h}\cdot\vec{h}|/\|\vec{h}\|^2 \to 0$, and then writes $u_1^{(u)} \approx u_1^{(d)} \approx \hat{h}^*$, concluding that $|V_{ub}|/|V_{td}| \approx \sin\theta_{12}^{(u)}/\sin\theta_{12}^{(d)} \gg 1$.
   - **Caveat Exposed:** That step assumes $\vec{h}_u = \vec{h}_d$, which holds only for the 4 **same-quark-reading** triples (`SSS`, `SSS~`, `S~S~S`, `S~S~S~`). What happens on the 4 **mixed-quark-reading** triples (`S~SS`, `S~SS~`, `SS~S`, `SS~S~`) where $\vec{h}_d = \vec{h}_u^*$?
   - When $\vec{h}_d = \vec{h}_u^*$, $u_1^{(u)} \to \hat{h}_u^*$ while $u_1^{(d)} \to \hat{h}_d^* = \hat{h}_u$. Their inner product is:
     $$\langle u_1^{(u)}, u_1^{(d)} \rangle \to \langle \hat{h}_u^*, \hat{h}_u \rangle = \frac{\vec{h}_u \cdot \vec{h}_u}{\|\vec{h}_u\|^2} = O(r) \ll 1!$$
     That is, on the null cone $\vec{h}\cdot\vec{h} \to 0$, $\hat{h}_u^*$ and $\hat{h}_u$ are **nearly orthogonal**!
   - Direct evaluation at `B1825`'s best address confirms all 4 quark reading pairs fail at $a_0 = 0$:
     - `S~S~` (`B1825` readout): $|V_{ud}| = 0.9791$, $|V_{us}| = 0.2028$, $|V_{cb}| = 0.0633$, $|V_{ub}|/|V_{td}| = 11.2797$ (corner inversion).
     - `SS`: $|V_{ud}| = 0.0824$, $|V_{us}| = 0.9888$, $|V_{ub}|/|V_{td}| = 7.4033$ (Cabibbo inversion + corner inversion).
     - `S~S` (mixed): $|V_{ud}| = 0.0992$, $|V_{us}| = 0.9944$, $|V_{cb}| = 0.9890$, $|V_{td}| = 0.9845$ (catastrophic permutation collapse).
     - `SS~` (mixed): $|V_{ud}| = 0.9590$, $|V_{cb}| = 0.9951$, $|V_{td}| = 0.2789$ ($(2,3)$-block collapse).

3. **Theorem 3 — Exact Determinant Factorization (`VERIFIED EXACT (NOT FABRICATED)`):**
   - $\det Y_s^{\text{4D}} = (a_0^2 + \vec{h}\cdot\vec{h})(m_1^2 + \vec{m}_\perp\cdot\vec{m}_\perp)(a_0 m_1 + \vec{h}\cdot\vec{m}_\perp)$ holds across 200 random complex trials to max relative error **$7.51 \times 10^{-15}$**.

4. **Theorem 4 — Exact Modular Identity $DR\cdot DR = -R\cdot D^2R = \frac{1}{4}\eta(\tau)^6$ (`VERIFIED EXACT (NOT FABRICATED)`):**
   - Verified in **exact rational arithmetic** using `qseries.py` up to $x^{240} = q^{30}$ (every rational coefficient of $DR\cdot DR - \frac{1}{4}\eta^6$ and $DR\cdot DR + R\cdot D^2R$ is identically `0/1`) and numerically at 20 random $\tau \in \mathbb{H}$ to max relative error **$1.11 \times 10^{-13}$**.

---

### Area 6: 3-Fold Cover $M_3 \to \text{m004}$ Commutant & Torsion (`src/origin_axiom/operator_gate.py`)

1. **Monodromy & Reidemeister–Franz Torsion (`VERIFIED EXACT (NOT FABRICATED)`):**
   - For $LR = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, $\det(LR - I) = -1$ (so $H_1(\text{m004}; \mathbb{Z}) = \mathbb{Z}$), $|\Delta_{\text{m004}}(\omega)| = |\det(LR - \omega I)| = |3 - 3\omega| = 4$, and $|\tau_{\text{RS}}(\text{m004}; \omega)| = 4/|1 - \omega| = 4/\sqrt{3}$.

2. **`commutant_dim == 1` Claim (`VERIFIED WITH CAVEAT / OVERSTATEMENT EXPOSED`):**
   - In `operator_gate.py` lines 223–224 and `parameter_ledger.py` line 9, `agy` attributes `commutant_dim == 1` ($H = c\,I_3$) to the 3-fold cover deck group $S_3 = \mathbb{Z}_3 \rtimes \mathbb{Z}_2$.
   - **Independent Matrix Audit:**
     - Under the **pure 3-sheet permutation action** of $S_3 = \langle C_3, P_{\text{perm}} \rangle$ with $C_3 = \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}$ and $P_{\text{perm}} = \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$ (group order **6**), the representation on $\mathbb{R}^3$ is the reducible permutation representation $\mathbf{1} \oplus \mathbf{2}_E$. Its real symmetric (and complex Hermitian) commutant is **2-dimensional**:
       $$H = a\,I_3 + b\,J_3 \quad (J_3 = \mathbf{1}\mathbf{1}^T),$$
       which allows non-zero democratic off-diagonal sheet mixing $b \ne 0$! This matches `frontier/B1822_t_norm_on_the_frames_matter/FINDINGS.md` §3 Row 4 (`"order-3 automorphism cycling i -> j -> k | 2"`).
     - Why did `operator_gate.py` line 224 get `commutant_dim == 1`? Because line 200 defined:
       `p_refl = [[1, 0, 0], [0, 0, -1], [0, -1, 0]]`,
       which is NOT a pure sheet permutation: it multiplies $P_{\text{perm}}$ by $\text{diag}(1, -1, -1)$ (a $\mathbb{Z}_2 \times \mathbb{Z}_2$ quaternion character sign flip on `BLOCKS = [QJ, QI, QK]`).
     - The group generated by $C_3$ and `p_refl` has order **24** — it is the full octahedral group $S_4 = (\mathbb{Z}_2 \times \mathbb{Z}_2) \rtimes S_3$, where $\mathbb{R}^3$ is the irreducible 3D representation $\mathbf{3}_{T_1}$ (`B1822` §3 Row 6: `"characters plus the order-3 automorphism | 1"`).
     - Thus, killing the democratic mixing term $b\,J_3$ to get $H = c\,I_3$ (`commutant_dim == 1`) requires **both** the $S_3$ cover-sheet symmetry **and** the $\mathbb{Z}_2 \times \mathbb{Z}_2$ quaternion character grading, not the bare 3-sheet deck group $S_3$ alone.

---

### Area 7: `FR-COV` CKM Evaluation, Full 10-Observable $\chi^2_{\text{ten}}$, and Input Ledger (`operator_gate.py`, `parameter_ledger.py`)

1. **Full 10-Observable $\chi^2_{\text{ten}}$ at `evaluate_operator_gate("FR-COV")` (`VERIFIED WITH MAJOR CAVEAT / OVERSTATEMENT EXPOSED`):**
   - `evaluate_operator_gate("FR-COV")` evaluates the 4D operator at `B1825`'s best address (`(3/8, 3/8), DR, L_2, S~S~S`, $\tau = 0.093359375 + 2.742578125i$) using $a_0 = 0.20\,e^{7\pi i/8}$ and reports only $|V_{ub}|/|V_{td}| = 0.677838$, $\sin\delta_{\text{CP}} = 0.699711$, and $|J| = 5.4275 \times 10^{-5}$, without reporting the full 10-observable $\chi^2_{\text{ten}}$.
   - Our independent audit computed all 10 observables and their individual $\chi^2_i$ at that exact point across four configurations:

| Configuration at `B1825` Address ($\tau = 0.0934 + 2.7426i$) | Reading | $|a_0|$ | $|V_{ub}|/|V_{td}|$ | $\sin\delta_{\text{CP}}$ | $m_c/m_t$ | $|V_{us}|$ | $\chi^2_{\text{six}}$ | $\chi^2_{\text{CKM}}$ | **Total $\chi^2_{\text{ten}}$** |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **1. `FR-FIB` Baseline ($a_0 = 0$)** | `S~S~S` | `0.00000` | `11.2797` | `0.0842` | `0.00455` | `0.20275` | `63.64` | `227.84` | **`291.49`** |
| **2. `FR-COV` Hand-Picked Witness ($a_0 = 0.20\,e^{7\pi i/8}$)** | `S~S~S` | `0.20000` | **`0.6778`** | **`0.6997`** | `0.03816` | `0.11158` | `1820.49` | `208.74` | **`2029.24`** |
| **3. `FR-COV` Witness on Ledger's Reading (`S~SS`)** | `S~SS` | `0.20000` | `0.3015` | `0.4766` | `0.03816` | `0.42666` | `2059.66` | `4511.70` | **`6571.36`** |
| **4. Theorem 4 Canonical $a_0 = \frac{1}{2}\eta(\tau)^3$** | `S~S~S` | `0.05801` | `5.8205` | `0.1255` | `0.00787` | `0.27208` | `226.10` | `284.80` | **`510.90`** |

   - **Three Critical Caveats Exposed:**
     1. **$\chi^2_{\text{ten}}$ explodes from $291.49$ to $2029.24$ at the un-reoptimized address:** Injecting $a_0 = 0.20\,e^{7\pi i/8}$ without re-optimizing $(\text{line}, \tau)$ drives $m_c/m_t$ from $0.00455$ to $0.03816$ ($10.4\times$ PDG, $\chi^2_{c/t} = 507.33$), $m_e/m_\tau$ to $\chi^2_{e/\tau} = 637.49$, and $|V_{us}|$ down to $0.11158$ ($\chi^2_{|V_{us}|} = 49.15$).
     2. **$a_0 = 0.20\,e^{7\pi i/8}$ is a 2-real-parameter complex witness, NOT Theorem 4's parameter-free $a_0(\tau) = \frac{1}{2}\eta(\tau)^3$:** At $\tau = 0.0934 + 2.7426i$, $\frac{1}{2}|\eta(\tau)^3| = 0.058009$ ($3.45\times$ smaller than $0.20$), which only reduces $|V_{ub}|/|V_{td}|$ from $11.28$ to $5.8205$ ($\chi^2_{\text{ten}} = 510.90$).
     3. **Reading mismatch (`S~S~S` vs `S~SS`):** `parameter_ledger.py` line 84 claims $U(1)_Y$ gauge invariance forces reading `S~SS` (`(1, 0, 0)`), whereas `operator_gate.py` evaluated `FR-COV` on `S~S~S` (`(1, 1, 0)`). On `S~SS`, $a_0 = 0.20\,e^{7\pi i/8}$ gives $|V_{cb}| = 0.9513$ and $\chi^2_{\text{ten}} = 6571.36$.

2. **Torsion-Line Compatibility (`Fix((LR)^3)` vs `(3/8, 3/8)` and `(2/5, 1/10)`) (`VERIFIED WITH CAVEAT EXPOSED`):**
   - Because $w = p_1\tau - p_2$ has a minus sign on $p_2$, $LR = \begin{pmatrix}2&1\\1&1\end{pmatrix}$ acts on $(p_1, p_2)^T \in (\mathbb{Q}/\mathbb{Z})^2$ by $M_{LR} = \begin{pmatrix}2&-1\\-1&1\end{pmatrix}$, and $(M_{LR})^3 = \begin{pmatrix}13&-8\\-8&5\end{pmatrix}$.
   - $\ker((M_{LR})^3 - I) \cong (\mathbb{Z}/4\mathbb{Z})^2$ consists of the 16 torsion points of orders $1, 2, 4$, which form **5** non-zero $\langle T, -I\rangle$-orbits (`(0, 1/2), (1/2, 0), (0, 1/4), (1/4, 0), (1/4, 1/2)`), plus **1** projective order-5 eigen-orbit `(2/5, 1/5)` where $M_{LR}\binom{2/5}{1/5} = \binom{3/5}{4/5} \equiv -\binom{2/5}{1/5} \pmod 1$, giving $5 + 1 = 6$ orbits (note `parameter_ledger.py` line 82 comment says `"4 + 1 = 5 orbits"` whereas line 87 computes `5 + 1 = 6`).
   - **Crucially, neither `B1825`'s best line `(3/8, 3/8)` (order 8) nor `B1726`'s best line `(2/5, 1/10)` (order 10) lies in `Fix((LR)^3)`!** Therefore, executing `FR-COV` on its cover-compatible torsion locus requires a fresh joint optimization over $\tau \in \mathbb{H}$ on the 6 cover-compatible orbits using the canonical scalar $a_0(\tau) = \frac{1}{2}\eta(\tau)^3$.
