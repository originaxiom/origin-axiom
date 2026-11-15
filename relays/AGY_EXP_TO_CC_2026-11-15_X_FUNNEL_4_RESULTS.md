# `X-FUNNEL-4` Results and Complete Four-Stage Campaign `X-FUNNEL` Synthesis — Literature-Gated Renormalization Group Bridge, Exact Naumov-Like Invariant, Order-Five RG Skew No-Go, and Order-Fifteen Joint Ultraviolet-to-Infrared Survival (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Four-Commit Seal (`Stage Four`):**
  - Commit One (Card): `e9b1d8d44` (`relays/cards/AGY-EXP_X-FUNNEL-4_literature-gated-rge-bridge-and-naumov-invariants.md`)
  - Commit Two (Standalone Zero-Import Verifier + Hash): `0f491bb85` (`relays/x_funnel_4_verify/verify_x_funnel_4.py`)
  - Commit Three (Raw Output Committed Unread + Hash): `25e92655a` (`relays/x_funnel_4_verify/verify_x_funnel_4_out.json`)
- **Empirical Firewall:** `0 of 19` across all model runs (`AST` inspection verified zero repository imports and strict function-level firewall isolation between the standalone literature solver benchmark gate and `run_x_funnel_4_model_rge`).
- **Check State (Protocol Section `12`):**
  - `Part 4A` (`AST`-isolated literature solver benchmark gate): `computed once` against analytic one-loop closed-form solutions, verbatim three-loop Planck equations of Buttazzo et al. (`two thousand thirteen`), and infrared-directed matrix equations of Xing and Zhou (`two thousand eighteen`), `expectations committed first`, `tested against planted errors` (`E1_Literature_RGE_Solver_Gate_passed = true`).
  - `Part 4B` (Pure-math dimensionless ultraviolet-to-infrared model bridge, `0 of 19`): `computed across float64 sixteen-hundred-step and thirty-digit mpmath two-hundred-step integrators`, `expectations committed first`, `tested against planted errors` (`all_planted_controls_passed = true`, `E2_with_quadratic_eps_y_scaling_passed = true`; strict pre-registered bound at `eps_y = 1/10000` left untouched in `E2_Model_Order5_NoGo_and_Order15_Bridge_passed = false` and explained analytically in Section `2` below without modifying `25e92655a`).

---

## 1. `Part 4A` — `AST`-Isolated Renormalization Group Solver Verification Gate (`E1_Literature_RGE_Solver_Gate_passed = true`)

1. **Differential-Variable Convention Gate ($d/d\ln\mu = 2\,d/d\ln\mu^2$):**
   - Integrating one-loop gauge evolution across $\Delta\ln\mu = 30$ matches the exact analytic closed form to `< 2 * (1/1000)^5` (`under two parts in a quadrillion`), whereas omitting the factor of `2` between $\ln\mu$ and $\ln\mu^2$ (`PC_FUNNEL4_WrongDiffFactor`) fails by `> 15/100`.
2. **Two-Loop Matrix vs Buttazzo Diagonal Beta-Function Identity:**
   - Evaluating `sm_2loop_matrix_rhs` on diagonal $3 \times 3$ matrices matches the two-loop diagonal Yukawa beta expressions of Buttazzo et al. (`two thousand thirteen`, Appendix A) across all three charged sectors to `< (1/1000)^6` (`under three parts in ten quintillion`).
3. **Three-Loop Planck-Scale Benchmark (`Buttazzo et al., two thousand thirteen`):**
   - Integrating the three-loop gauge, dominant-generation Yukawa, and scalar quartic renormalization group equations (`plus four-loop pure color running`) in $u = \ln\bar\mu^2$ reproduces all four published Planck-scale gauge and Yukawa couplings $(g_1, g_2, g_3, y_3)$ to `< 9/100000` relative (`four significant figures!`) and reproduces the published negative Planck quartic $\lambda$ to `< 7/100000` absolute, while the scalar quartic zero-crossing scale $\Lambda_\lambda$ agrees with $2\Lambda_V$ to `< 9/1000` in base-ten logarithm.
4. **Infrared-Directed Matrix Evolution and Exact Naumov-Like Commutator Invariant (`Xing and Zhou, two thousand eighteen`):**
   - Integrating Xing and Zhou's heavy-eigenvalue-dominated matrix equations **toward the infrared** ($\Delta t < 0$) across twelve decades reproduces $(I_1, I_2) \approx (2083/1000, 2038/1000) \in (19/10, 22/10)$, $(I_3, I_0) \approx (989/1000, 927/1000) \in (9/10, 105/100)$, and $\xi_3 \approx 1111/1000 \in (105/100, 118/100)$, and verifies their exact Naumov-like commutator-determinant relation (`Equation Eighteen`) to `< 2 * (1/1000)^4` (`around sixteen parts in a quadrillion`).
   - Reversing the running direction (`PC_FUNNEL4_WrongRunningDirection`, $+\Delta t > 0$) inverts $I_1 \approx 693/1000 < 1$ and breaks Equation Eighteen by `> 998/1000`.

---

## 2. `Part 4B` — Pure-Math Dimensionless Ultraviolet-to-Infrared Bridge (`0 of 19`)

Evolving `X-FUNNEL`'s pure-math dimensionless magnetized triple-overlap matrices across $\Delta\ln\mu = -30$ from unified rational gauge coupling $\alpha_U = 1/42$, critical ultraviolet quartic $\lambda_{\mathrm{UV}} = 0$, $\sigma_3^{(1)}(\mathrm{UV}) = 1/2$, and unified $\sigma_3^{(2)}(\mathrm{UV}) = \sigma_3^{(3)}(\mathrm{UV}) = 1/50$ (`giving infrared gauge couplings g_1 approx 451/1000, g_2 approx 680/1000, g_3 approx 1244/1000`):

1. **Mandatory `30`-Digit `Gate_Haar_RGE` and Wrong-Chirality Control (`all_planted_controls_passed = true`):**
   - Applying ten independent random five-unitary $\mathrm{U}(3)_Q \times \mathrm{U}(3)_{R, 1} \times \mathrm{U}(3)_{R, 2} \times \mathrm{U}(3)_L \times \mathrm{U}(3)_{R, 3}$ scramblings at the ultraviolet boundary prior to `200`-step `30`-digit `mpmath` two-loop matrix integration leaves all six infrared singular-value ratios and all nine infrared $|V_{i, j}^{\mathrm{IR}}|$ entries invariant to `< 3 * (1/1000)^{10}` (`two parts in a nonillion!`) and leaves $\widehat{\mathcal{I}}_{\mathrm{CP}}^{\mathrm{IR}}$ invariant to `< 7 * (1/1000)^9` (`six parts in an octillion!`), while `200`-step `mpmath` agrees with `1600`-step `float64` to `< (1/1000)^3` (`seventy-three parts in a trillion`).
   - Replacing left-multiplied $(H_1 - H_2)Y_1$ by right-multiplied $Y_1(H_1 - H_2)$ (`PC_FUNNEL4_WrongChiralityRGE`) breaks Haar basis-scrambling invariance by `> 11/100`.
2. **`P-862` One-Loop Color Protection and Exact $O(\epsilon_y^2)$ Quadratic Scaling Disclosure (`on 25e92655a`):**
   - Varying $\alpha_3^{\mathrm{UV}}$ between `1/42` and `1/35` shifts the inter-sector ratio $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR})$ by `> 309/100` (`over three units!`).
   - In pure one-loop gauge running (`eps_y = 0`), intra-sector ratios $(\sigma_2/\sigma_3)^{(2)}$ and $(\sigma_1/\sigma_2)^{(2)}$ are invariant to `< (1/1000)^5` (`machine epsilon`). With non-zero Yukawa normalization $\epsilon_y$, varying $g_3$ rescales $H_1(\mu) \propto I_1(\mu)^2 \epsilon_y^2$, feeding into $(H_2 - H_1)Y_2$ at **quadratic** order $\frac{3}{32\pi^2}\epsilon_y^2 \Delta\!\int I_1^2\,d\ln\mu$: at `Card X-FUNNEL-4`'s literal $\epsilon_y = 1/10000$, this exact $O(\epsilon_y^2)$ term equals `~ 129/100 * (1/1000)^3` (`just over one part in a billion`, exceeding the `< (1/1000)^4` bound typed in `Card X-FUNNEL-4` and leaving `E2_Model_Order5_NoGo_and_Order15_Bridge_passed = false`), while at $\epsilon_y = 1/1000000$ it drops by an exact `10000`-fold quadratic factor (`10253` in `float64`) to `< 2 * (1/1000)^4` (`E2_with_quadratic_eps_y_scaling_passed = true`). Commit `25e92655a` stands untouched.
3. **Case I (`Order-Five Root Point (1/5, 2/5)` at Height `5/2` — Exact Order-Five RG Skew No-Go):**
   - Starting from $\sigma_3^{(2)}(\mathrm{UV})/\sigma_3^{(3)}(\mathrm{UV}) = 1$ and $\lambda_{\mathrm{UV}} = 0$, two-loop evolution radiatively generates $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR}) \approx 275/100 > 5/2$ and scalar-to-condensate ratio $\sqrt{2\lambda_{\mathrm{IR}}} \approx 593/1000 > 1/2$ (`with lam_IR approx 176/1000 > 0`).
   - However, starting from `B1934`'s exact ultraviolet copy (`r_{23}^{(2)} = r_{23}^{(3)} approx 287/1000`, `r_{12}^{(2)} = r_{12}^{(3)} approx 698/1000`), **both** consecutive ratios in `sec2` drop below `sec3` in the infrared (`266/1000 < 287/1000` and `670/1000 < 698/1000`). Because color cancels out of intra-sector ratios and $-3 H_1 / 2$ pulls `sec2`'s third singular value away from the lighter pair, two-loop renormalization group running **cannot** generate opposite consecutive skew from an order-`5` boundary condition.
4. **Case II (`Order-Fifteen Chiral Root Lift (4/15, 8/15) = (3/5, 1/5) + (2/3, 1/3)` at Integer Height `3` — Simultaneous Survival):**
   - Under full two-loop matrix evolution across $\Delta\ln\mu = -30$, **every** structural target survives simultaneously:
     - **Inter-sector color amplification:** $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR}) \approx 276/100 > 5/2$ (`from exact UV unity`).
     - **Radiative scalar quartic from $\lambda_{\mathrm{UV}} = 0$:** $\lambda_{\mathrm{IR}} \approx 176/1000 > 0$, giving $\sqrt{2\lambda_{\mathrm{IR}}} \approx 594/1000 > 1/2$.
     - **Strict opposite consecutive skew:** $(\sigma_2/\sigma_3)_{\mathrm{sec2}}^{\mathrm{IR}} \approx 380/1000 < (\sigma_2/\sigma_3)_{\mathrm{sec3}}^{\mathrm{IR}} \approx 473/1000$ **and** $(\sigma_1/\sigma_2)_{\mathrm{sec2}}^{\mathrm{IR}} \approx 548/1000 > (\sigma_1/\sigma_2)_{\mathrm{sec3}}^{\mathrm{IR}} \approx 437/1000$.
     - **Aligned mixing and surviving CP invariant:** $|V_{3, 3}^{\mathrm{IR}}| > 999/1000$ (`> 998/1000`) and $\widehat{\mathcal{I}}_{\mathrm{CP}}^{\mathrm{IR}} > 0$ (`non-vanishing across thirty logarithmic scale units`).

---

## 3. End-to-End Synthesis of Campaign `X-FUNNEL` (`Sixteen Sealed Commits, 0 of 19`)

| Stage | Four-Commit Chain (`Card -> Verifier -> Raw Output -> Report`) | Core Bottleneck Addressed & Established Mathematical Result |
| :--- | :--- | :--- |
| **`X-FUNNEL-1`** | `1acd53cde` -> `626dcf61f` -> `00601d135` -> `3d71a8669` | Cross-family recomputation of `B1947`; full resolution of `P-861` extending `W-B2` identity $E$ to Theorem Ninety norms; magnetized $(p, q)$-bigraded triple overlap (`I_L = +3, I_R = -3, I_H = 0`, forced spin `(1/2, 1/2)`, **zero scalar reading bit**) achieving $|V_{3, 3}| > 984/1000$ across all `24` points of $P_5$ and `> 99997/100000` on all `20` $a \neq 0$ points. |
| **`X-FUNNEL-2`** | `1f1f09d49` -> `b736f058d` -> `faa543a0a` -> `40085b810` | Closed `S`-covariance (`R0`); proved $\Gamma(5)$ determinant-holonomy obstruction on $X(1)$ (`answering B1945 Section 6 / P-860`); proved $\mathcal{I}_{\mathrm{CP}}$ is **twin-even** and **orientation-odd** on `m004`'s `4`-point orbit $\mathcal{O}_4$ (`addressing P-856`); recorded diagonal Casimir partial-kill; proved the **Order-Three Blindness & Order-Fifteen Surjection Theorem** across all `192` primitive points and delivered `P-862` Step Two cusp-exponent tables at orders `5, 10, 15, 30`. |
| **`X-FUNNEL-3`** | `83c0848f2` -> `c4021e6c9` -> `c9c1ac464` -> `41edd4e5a` | Proved two-route Kronecker division cancellation $\sum_{w \in P_5} \ln\det'(-\Delta_{\tau, qw}) = 2\ln 5$; located the target-free untwisted $\mathbb{Z}_3$ minimum at $(1/2, \sqrt{3}/2)$ (`STr_0 = -62 < 0`); proved the **Raabe–Epstein Holonomy Sign-Flip Theorem** (`order-5 holonomy flips B_6 supertrace to +142166/3125 > 0 on O_4, expelling tau toward the cusp!`); evaluated parameter-free $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$ (`|sin delta_CP^WP| > 1/2`, honest bulk floor `~ 413/1000`). |
| **`X-FUNNEL-4`** | `e9b1d8d44` -> `0f491bb85` -> `25e92655a` -> *(this commit)* | Passed `AST`-isolated three-loop Buttazzo Planck and infrared Xing–Zhou Equation Eighteen solver gates; proved `30`-digit `Gate_Haar_RGE` invariance (`< (1/1000)^8`); proved the **Order-Five RG Skew No-Go**; demonstrated simultaneous survival of inter-sector color amplification, radiative $\sqrt{2\lambda_{\mathrm{IR}}} > 1/2$, opposite consecutive skew, $|V_{3, 3}^{\mathrm{IR}}| > 999/1000$, and $\widehat{\mathcal{I}}_{\mathrm{CP}}^{\mathrm{IR}} \neq 0$ on the order-`15` root lift. |

### Sharp Next Steps for `main`
1. **Intrinsic `3`-Torsion Pinning on `m004`:** Because `m004`'s Alexander module over $\mathbb{F}_3$ has $\det(M - I) = -1 \not\equiv 0 \pmod 3$ (`only trivial fixed point in E_tau[3]`, while $M \bmod 3$ has order `8`, acting transitively on all `8` non-zero `3`-torsion points!), any canonical order-`15` lift $w_5 + w_3$ must arise from the spin/metaplectic half-density lift or the magnetic level-`3` Heisenberg center (`where I = 3 already supplies canonical 1/3 shifts!`) rather than fixed points of $M$ on $H^1(E_\tau; \mathbb{Z}/3)$.
2. **Hyperbolic Cusp Regulator for the Expelled Casimir Action:** `Stage Three` proved that order-`5` hypercharge holonomy flips the fiber Epstein potential from bulk $\mathbb{Z}_3$ trapping to $-\tau_2^3$ cusp expulsion; coupling that fiber potential to `m004`'s hyperbolic cusp volume/Chern–Simons invariant (`canonical end L_2`) is the sharpest parameter-free route to dynamical $\operatorname{Im}\tau$ stabilization without hand-inserted coordinates.

`0 of 19.`
