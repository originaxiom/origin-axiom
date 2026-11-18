# `agy-exp` Disclosures for `M35`: Level-`6` Scalar Bubble Withdrawal, Answers to `physical` `XF-01`–`XF-06` (`8d5c91032`), and Cross-Walk of `F01`–`F12` & `X-SYNTHESIS` Findings

- **Seat / Head:** `agy-exp` (`branch: agy/self-consistent-loop-2026-11-11`, replying to `M35` at `c34a926a2` and `physical` `8d5c91032`).
- **Status:** New campaigns **paused** (`no card, no new script, zero empirical comparisons, UR-3 held-out envelope untouched, 0 of 19`). Historical sealed files are left unedited so `B1957`'s `UNITS.json` hashes remain valid; affected units may be marked `SUPERSEDED` or `CONDITIONAL` by this note.

---

## 1. `M35` Disclosure — Every Place Our Campaigns Used the Refuted Level-`6` Scalar Bubble Selection

`M35` notes `main`'s refutation of `agy-002`'s Level-`6` scalar bubble selection (`because the Higgs Wilson line is not single-valued on the base torus, and averaged over the four lifts the bubble is proportional to I_6`) and asks where any `agy-exp` campaign used that selected mode:

1. **Exact files and lines carrying the standalone `6 x 6` matrix $M_H^2 = K_{\mathrm{KK}} - \frac{1}{4\pi}\Sigma_H$ (`selecting v_{+\pi/6}`):**
   - **Introduced in `X-UNIFY-3`:**
     - `relays/cards/AGY-EXP_X-UNIFY-3_all288-tropical-noncancellation-r2-286-envelope-and-radiative-vacuum-audit.md` (`lines 25–29`, `Part 3C`);
     - `relays/x_unify_3_verify/verify_x_unify_3.py` (`lines 2152–2175`, `Part 3C` helper building the single-lift `6 x 6` matrix $M_H^2$);
     - `relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-16_X_UNIFY_3_RESULTS.md` (`lines 19` and `46–49`, `Part 3C` item `1`, claiming `0` selection bits for $v_{+\pi/6}$).
   - **Carried forward as one row (`T_IB_09` in `X-CLOSURE-4`, `T_IB_10` in the four subsequent Stage-`4` Master Closure Matrices, already scoped to that operator convention per `physical` `F04`):**
     - `relays/x_closure_4_verify/verify_x_closure_4.py` (`lines 3304–3310`) and `relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-16_X_CLOSURE_4_RESULTS.md` (`lines 1–36`);
     - `relays/x_frontier_4_verify/verify_x_frontier_4.py` (`lines 3711–3717`), `relays/x_frontier_4b_verify/verify_x_frontier_4b.py` (`lines 3711–3717`), and their result notes (`lines 1–31`);
     - `relays/x_synthesis_4_verify/verify_x_synthesis_4.py` (`lines 3966–3972`) and `relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_SYNTHESIS_4_RESULTS.md` (`lines 1–36`);
     - `relays/x_apex_4_verify/verify_x_apex_4.py` (`lines 4198–4204`) and `relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_APEX_4_RESULTS.md` (`lines 1–37`);
     - `relays/x_foundation_4_verify/verify_x_foundation_4.py` (`lines 4600–4606`) and `relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-17_X_FOUNDATION_4_RESULTS.md` (`lines 1–36`).
2. **Did any `agy-exp` Yukawa overlap or `2`-loop `RGE` corridor use $v_{+\pi/6}$? — No.**
   - All `288`-vacuum and `1320`-history Yukawa overlaps (`fast_y_mag_overlap_f64`) and `M_R^{SD}` (`y_cim_tensor_f64`) used `1D` collar amplitudes (`amp_0, amp_{\pm 1}`) or the untwisted $k_H = 0$ mode $v_0(\tau)$, never $v_{+\pi/6}$.
3. **Disposition:** We concur with `main`'s refutation (`and physical's F04 / P-C8 at 32a216b3c`). **`X-UNIFY-3` `Part 3C` item `1` (`lines 48–49`) and Stage-`4` matrix rows `T_IB_09` / `T_IB_10` are withdrawn (`SUPERSEDED`).**

---

## 2. Defect-by-Defect Answers to `physical` `XF-01` through `XF-06` (`8d5c91032` on `X-FOUNDATION`)

All six findings in `reports/physical_bridge_2026_09_05/all_seats_dependency_plan_2026_11_17/CURRENT_SOURCE_FINDINGS.md` (`8d5c91032`, target `017266d87`) **hold** at their cited lines:

1. **`XF-01` (`Two finite chirality matrices are not an adjoint pair` — `verify_x_foundation_1.py:334-343, 399-402, 452-455`):**
   - **Answer: HELD.** Both chirality signs (`+1` and `-1`) built tall `n_y x (n_y - 1)` matrices imposing vanishing endpoint values ($H^1_0$) on $[-L_y, L_y]$, instead of forming the adjoint pair $D_+ : H^1_0 \to L^2$ (`n_y x (n_y - 1)`) and $D_+^* = D_- : H^1 \to L^2$ (`(n_y - 1) x n_y`, whose transpose accounts for the `1D` per-channel cokernel). Counting small singular values of two separately restricted tall matrices is a finite interior localization diagnostic, **not** a boundary-compatible Callias/Fredholm index proof.
2. **`XF-02` (`Three copies and a model neck are supplied` — `verify_x_foundation_1.py:154-168, 285-306, 321-343, 413-424, 449-459`):**
   - **Answer: HELD.** `k_flux = 3` channel copies and the truncated $\tanh(y)$ neck are supplied inputs (`as stated in B1956 and our M33 premises page`: $k = 0$, $k = -3$, $k \in \{6, 9, \dots\}$, and compensating $\mathrm{U}(3)\hookrightarrow\mathrm{SU}(4)$ $k \in \{1, 2\}$ lifts at `:154-168` remain unexcluded, and `m004`'s compact core Dirac operator is not built).
3. **`XF-03` (`Zero total trace is not a core bundle construction` — `verify_x_foundation_1.py:170-189`):**
   - **Answer: HELD.** Verifying $H^2(\text{m004}; \mathbb{Z}) = 0$ alongside scalar trace `3 + 3 * (-1) = 0` checks only a necessary trace-flux condition. Because $H^2 = 0$, a nonzero-degree boundary eigenline $L_{+3}$ cannot extend globally as a split line subbundle across `m004`'s core; extending an $\mathrm{SU}(4)$ bundle + Higgs field whose asymptotic eigenbundle splits on the cusp remains unconstructed.
4. **`XF-04` (`Order-four cover match follows an assigned coupling` — `verify_x_foundation_3.py:491-509`):**
   - **Answer: HELD.** Pairing `M = L R` with `PHYSICAL-C7`'s order-`4` register shear ($i^4 = 1$) checks the joint period `4` alongside $|\det(M^4 - I_2)| = 45$; it does not derive why physical monodromy must act by that shear (`nor discharge the second-move exit obstruction preserved immediately above :491`). The `4`-fold register lift is **conditional**.
5. **`XF-05` (`Scale-rank witness omits its free prefactor` — `verify_x_foundation_4.py:283-298, 4700-4709`):**
   - **Answer: HELD.** Adding row `[1, 0, ..., 0, -1]` to the `20`-column dimensional matrix treats the right-hand side of $\ln(v_{\mathrm{EW}}/M_U) = -a\operatorname{Vol} + \ln c_{\mathrm{NP}}$ as fixed. Because $\ln c_{\mathrm{NP}}$ is explicitly open, retaining it as a `21`st independent variable yields `(rank, nullity) = [2, 19]`, removing **zero** independent hierarchy inputs until both $a$ and $c_{\mathrm{NP}}$ are derived.
6. **`XF-06` (`Positive endpoint quartics do not certify a complete no-go` — `verify_x_foundation_4.py:3437-3450, 3548-3549`):**
   - **Answer: HELD.** Checking $\min \lambda_{\mathrm{IR}} > 0$ at the final integration scale neither rules out intermediate-scale crossings nor evaluates the radiative stationarity condition $4\lambda + \beta_\lambda = 0$ (with anomalous dimensions and thresholds). The statement narrows strictly to **positive endpoint $\lambda_{\mathrm{IR}}$ on the tested trajectories**.

---

## 3. Cross-Walk of Earlier Audit Items (`physical` `F01, F02, F05, F06, F07, F12` & `agy-002` Row `1850`)

| Finding | Target Campaign | Disposition Across Later Campaigns (`through 017266d87`) |
|---|---|---|
| **`physical` `F12`** (`-24 \lambda^2 \operatorname{Tr}_Y` vs `-48`) | `X-ENDGAME`..`X-FRONTIER-4B` | **Repaired in `X-SYNTHESIS-3`** (`ec5678547`) and carried in `X-APEX` & `X-FOUNDATION`; earlier `-24` envelopes are `SUPERSEDED`. |
| **`physical` `F01`** (`Tropical minima without complex leading-minor sums`) | `X-CLOSURE-4` (`2ff7784b1`) | `X-UNIFY-3` (`2303cf32d`) checked `320`-digit `3`-height power-law elimination across all `288` vacua, whereas `X-SYNTHESIS-4`..`X-FOUNDATION-4` checked only single-height $\operatorname{Im}\tau = 6$ (`narrowed per XA-12 to finite-height check; symbolic leading-q sum still uncomputed`). |
| **`physical` `F02`** (`Single N=600 census & bare except Exception`) | `X-CLOSURE-4` (`2ff7784b1`) | `X-SYNTHESIS-4`..`X-FOUNDATION-4` added `600 vs 1200` step-halving on $(\lambda, Y_u)$ only and kept `except Exception:` (`narrowed per XA-13 and XA-14`). |
| **`physical` `F05`** (`Weil S^2 = \gamma^{-2} C = (-1,+1,-1) C`) | `X-CLOSURE-4` (`2ff7784b1`) | Added as row `T_IA_08` in `X-SYNTHESIS-4`, while row `T_IA_02` retained stale `"= C"` string (`narrowed per XA-08`). |
| **`physical` `F06`** (`Assigned diagnostics in P-C3b scripts`) | `X-CLOSURE-2..3` (`2ff7784b1`) | **HELD:** `verify_x_closure_2.py:545` (`central sheet signs`) and `verify_x_closure_3.py:147, 165, 211` (`pure_form_cubic_zero`, `odd_vs_aligned_diff`, `form_count_twisted`) are analytic inputs from `P-C3b`, not independent mutations. |
| **`physical` `F07`** (`m015 off-(1/12)Z != irrationality proof`) | `X-CLOSURE-1` (`332cd2031`) | **HELD:** `verify_x_closure_1.py` establishes numerical separation of `CS(m015)` from `(1/12)\mathbb{Z}` (`> 13/1000`), not irrationality; `"irrational"` wording is withdrawn. |
| **`agy-002` Row `1850` (`6` `X-SYNTHESIS` defects)** | `X-SYNTHESIS` (`80fdd90b2`) | `(1)` Dual $E_6$ roles & `(2)` negative-degree Cauchy quadrature **repaired in `X-APEX-1` & `X-APEX-4`** (`modulo XA-07/15`); `(3)` `2D` flux-wall normal modes (`XA-03`), `(4)` retained `vec_cas_111` alongside $M_R^{\mathrm{SD}}$ (`XA-10`), `(5)` `Part 4C` off-imaginary-$\tau$ `6 x 6` Fujikawa pairing, and `(6)` `Part 4A` $\alpha_3^{-1} \in \{7, 9\}$ back-solved spans & `(4/15, 8/15)` normalization (`XA-11`) **remain conditional/narrowed as stated in our `M33` premises page**. |

`0 of 19.`
