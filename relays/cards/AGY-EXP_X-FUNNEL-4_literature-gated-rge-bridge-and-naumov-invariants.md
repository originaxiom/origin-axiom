# Card `X-FUNNEL-4` — Literature-Gated Three-Loop and Matrix Renormalization Group Solver, Exact Naumov-Like Commutator Invariant, and Dimensionless Ultraviolet-to-Infrared Bridge for `X-FUNNEL` Operators and `P-862` Universal Laws (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Fourth and final sealed stage of Campaign `X-FUNNEL` (`0 of 19` on all model runs). Before evolving any pure-math ultraviolet operator from `X-FUNNEL` (`Stages One through Three`) toward the infrared, `AST`-isolated benchmark gates verify our standalone renormalization group solver against analytic closed-form solutions, the three-loop Planck-extrapolation equations of Buttazzo et al. (`two thousand thirteen`), and the infrared-directed matrix evolution and exact commutator-determinant invariant of Xing and Zhou (`two thousand eighteen`). Once gated, the isolated model runner evolves pure-math dimensionless ultraviolet boundary conditions (`zero` imported empirical numbers, `AST`-enforced) across thirty logarithmic scale units to test `P-862`'s universal intra-sector and inter-sector renormalization group laws.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no script or output file in `relays/x_funnel_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19` on all model operator runs (`AST`-verified strict function isolation between the standalone literature solver benchmark gate and the pure-math model evolution).

---

## 1. The Package and the Questions

1. **Question `4A` (`Solver Verification Gate Before Any Model Integration`):** Does our standalone renormalization group integrator handle differential-variable conventions ($d/d\ln\mu = 2\,d/d\ln\mu^2$) accurately to `< (1/1000)^4`, reproduce all five published Planck-scale couplings and the quartic zero-crossing scale of Buttazzo et al. (`two thousand thirteen`) to at least three significant figures (`four` on all gauge and third-generation Yukawa couplings), reproduce the infrared-directed evolution factors ($I_1, I_2, I_3, \xi_3$) and exact Naumov-like commutator-determinant relation (`Equation Eighteen`) of Xing and Zhou (`two thousand eighteen`) to `< (1/1000)^4`, and match Buttazzo's diagonal two-loop Yukawa beta functions to machine precision?
2. **Question `4B` (`Dimensionless Model UV-to-IR Bridge and P-862 Universal RG Laws`):** Evolving `X-FUNNEL`'s pure-math dimensionless magnetized triple-overlap matrices (`from unified rational gauge coupling alpha_U = 1/42 and critical ultraviolet quartic lambda_UV = 0` across $\Delta\ln\mu = -30$):
   - Can two-loop renormalization group running alone generate opposite consecutive singular-value ratio skew between the second and third charged sectors starting from an order-`5` root-orbit boundary condition $w_5 = (1/5, 2/5) \in \mathcal{O}_4$, or does color-blindness of intra-sector ratios establish an **exact order-five RG skew no-go**?
   - Starting instead from the order-`15` chiral lift $w_{15} = (4/15, 8/15) = (3/5, 1/5) + (2/3, 1/3)$ (`at pure integer height Im tau = 3`), do **all** desired structural features — inter-sector color amplification $\sigma_3^{(2)}(\mathrm{IR}) / \sigma_3^{(3)}(\mathrm{IR}) > 5/2$, radiative scalar-to-condensate ratio $\sqrt{2\lambda_{\mathrm{IR}}} > 1/2$ from $\lambda_{\mathrm{UV}} = 0$, opposite consecutive skew ($r_{23}^{(2)} < r_{23}^{(3)}$ with $r_{12}^{(2)} > r_{12}^{(3)}$), $|V_{3, 3}^{\mathrm{IR}}| > 998/1000$, and non-zero $\mathcal{I}_{\mathrm{CP}}^{\mathrm{IR}}$ — survive full two-loop matrix evolution simultaneously?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A` — `AST`-Isolated Literature Solver Gate (`gate_rge_literature_solver_only`):**
   - Verify exact one-loop gauge closed-form agreement over $\Delta\ln\mu = 30$ (`< (1/1000)^4`, vs planted missing factor of `2` in $d/d\ln\mu^2$ failing by `> 1/10`).
   - Integrate the verbatim three-loop gauge, third-generation Yukawa, and scalar quartic equations (`including four-loop pure color running`) of Buttazzo et al. (`two thousand thirteen`) in $u = \ln\bar\mu^2 = 2\ln\bar\mu$ to the Planck scale, checking at least three-significant-figure agreement on $(g_1, g_2, g_3, y_3, \lambda)$ and verifying $\Lambda_\lambda / (2\Lambda_V) \in [9/10, 11/10]$.
   - Verify that our full two-loop $3 \times 3$ matrix Yukawa beta function matches Buttazzo's two-loop diagonal expressions to `< (1/1000)^5`.
   - Integrate Xing and Zhou (`two thousand eighteen`) **toward the infrared** ($\Delta t < 0$) across twelve decades, reproducing $I_1, I_2 \in [19/10, 22/10]$, $I_3, I_0 \in [9/10, 11/10]$, $\xi_3 \in [105/100, 118/100]$, and verifying their exact Naumov-like commutator-determinant relation (`Equation Eighteen`) to `< (1/1000)^4` (`vs planted wrong running direction failing by > 9/10`).
2. **`Part 4B` — Pure-Math Dimensionless UV-to-IR Bridge (`run_x_funnel_4_model_rge`, `0 of 19`):**
   - Enforce via `AST` inspection that `run_x_funnel_4_model_rge` neither calls `gate_rge_literature_solver_only` nor contains any empirical boundary float literals.
   - Evolve Case I (`order-5 root point (1/5, 2/5) at height 5/2`) and Case II (`order-15 root lift (4/15, 8/15) at integer height 3`) across $\Delta\ln\mu = -30$ from pure rational unified $\alpha_U = 1/42$, $\lambda_{\mathrm{UV}} = 0$, $\sigma_3^{(1)}(\mathrm{UV}) = 1/2$, and unified $\sigma_3^{(2)}(\mathrm{UV}) = \sigma_3^{(3)}(\mathrm{UV}) = 1/50$.
   - Verify `P-862`'s one-loop color cancellation in intra-sector ratios (`varying UV g_3 with negligible Yukawa traces changes intra-sector ratios by < (1/1000)^4 while shifting inter-sector sigma_3^{(2)}/sigma_3^{(3)} by > 1/2`), verify the order-`5` RG skew no-go (`both r_{23} and r_{12} in sec2 drop below sec3 in Case I`), and verify survival of opposite consecutive skew, inter-sector color amplification, radiative $\sqrt{2\lambda_{\mathrm{IR}}} > 1/2$, $|V_{3, 3}^{\mathrm{IR}}| > 998/1000$, and non-zero $\mathcal{I}_{\mathrm{CP}}^{\mathrm{IR}}$ in Case II.
3. **Four-Commit Seal:** Card (`Commit One`), standalone zero-import verifier + `SHA256` (`Commit Two`), unread raw output + `SHA256` (`Commit Three`), mask-clean report + complete four-stage Campaign `X-FUNNEL` synthesis + status update (`Commit Four`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_Literature_RGE_Solver_Gate` (`Part 4A`):**
   - Exact one-loop gauge closed-form error `< (1/1000)^4`; two-loop matrix vs Buttazzo diagonal Yukawa beta-function error `< (1/1000)^5`.
   - Three-loop Buttazzo Planck-scale couplings match $(g_1, g_2, g_3, y_3)$ to `< 2/1000` relative (`>= 3` significant figures) and $|\lambda_{\mathrm{comp}} - \lambda_{\mathrm{pub}}| < 5/10000$, with $|\log_{10}(\Lambda_\lambda / (2\Lambda_V))| < 1/20$.
   - Xing–Zhou infrared-directed evolution satisfies $19/10 < I_2 < I_1 < 22/10$, $9/10 < I_0 < I_3 < 105/100$, $105/100 < \xi_3 < 118/100$, and Naumov-like commutator-determinant relative error `< (1/1000)^4`.
   - *Falsified if:* any literature benchmark misses three-significant-figure accuracy or Equation Eighteen fails.
2. **`E2_Model_Order5_NoGo_and_Order15_Bridge` (`Part 4B`, `0 of 19`):**
   - **One-loop color intra-sector cancellation (`P-862`):** At suppressed Yukawa normalization (`1/10000`), varying $\alpha_3^{\mathrm{UV}}$ between `1/42` and `1/35` shifts $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR})$ by `> 1/2` while leaving $(\sigma_2/\sigma_3)^{(2)}(\mathrm{IR})$ and $(\sigma_1/\sigma_2)^{(2)}(\mathrm{IR})$ invariant to `< (1/1000)^4`.
   - **Case I (`Order 5`, `(1/5, 2/5)` at height `5/2`):** Radiative running generates $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR}) > 5/2$ and $\sqrt{2\lambda_{\mathrm{IR}}} > 1/2$ from $\lambda_{\mathrm{UV}} = 0$, **but fails opposite consecutive skew**: both $(\sigma_2/\sigma_3)_{\mathrm{sec2}}^{\mathrm{IR}} < (\sigma_2/\sigma_3)_{\mathrm{sec3}}^{\mathrm{IR}}$ and $(\sigma_1/\sigma_2)_{\mathrm{sec2}}^{\mathrm{IR}} < (\sigma_1/\sigma_2)_{\mathrm{sec3}}^{\mathrm{IR}}$.
   - **Case II (`Order 15`, `(4/15, 8/15)` at integer height `3`):** Full two-loop infrared evolution simultaneously achieves $\sigma_3^{(2)}(\mathrm{IR})/\sigma_3^{(3)}(\mathrm{IR}) > 5/2$, $\sqrt{2\lambda_{\mathrm{IR}}} > 1/2$, **strict opposite consecutive skew** ($(\sigma_2/\sigma_3)_{\mathrm{sec2}}^{\mathrm{IR}} < (\sigma_2/\sigma_3)_{\mathrm{sec3}}^{\mathrm{IR}}$ AND $(\sigma_1/\sigma_2)_{\mathrm{sec2}}^{\mathrm{IR}} > (\sigma_1/\sigma_2)_{\mathrm{sec3}}^{\mathrm{IR}}$), $|V_{3, 3}^{\mathrm{IR}}| > 998/1000$, and $|\mathcal{I}_{\mathrm{CP}}^{\mathrm{IR}}| > 0$.
   - *Falsified if:* order-`5` RG running generates opposite consecutive skew, or order-`15` opposite consecutive skew collapses under two-loop running, or $\lambda_{\mathrm{IR}} \le 0$.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar_RGE`:** Ten independent random five-unitary $\mathrm{U}(3)_Q \times \mathrm{U}(3)_{R, 1} \times \mathrm{U}(3)_{R, 2} \times \mathrm{U}(3)_L \times \mathrm{U}(3)_{R, 3}$ scramblings applied at the ultraviolet boundary prior to two-loop matrix ODE integration leave all six infrared singular-value ratios and all nine infrared $|V_{i, j}^{\mathrm{IR}}|$ entries invariant to `< (1/1000)^4` (`< (1/1000)^4` relative on $\mathcal{I}_{\mathrm{CP}}^{\mathrm{IR}}$ as well).
2. **`PC_FUNNEL4_WrongChiralityRGE`:** Replacing left-multiplied $(H_1 - H_2) Y_1$ by right-multiplied $Y_1 (H_1 - H_2)$ breaks Haar basis-scrambling invariance of the infrared observables by `> 5/100`.
3. **`PC_FUNNEL4_WrongDiffFactor`:** Omitting the factor of `2` between $d/d\ln\mu$ and $d/d\ln\mu^2$ breaks the one-loop closed-form gauge benchmark by `> 1/10`.
4. **`PC_FUNNEL4_WrongRunningDirection`:** Reversing infrared-directed $\Delta t < 0$ to $+\Delta t > 0$ in the Xing–Zhou integrator inverts $I_1, I_2 < 1$ and breaks Equation Eighteen by `> 9/10`.

`0 of 19.`
