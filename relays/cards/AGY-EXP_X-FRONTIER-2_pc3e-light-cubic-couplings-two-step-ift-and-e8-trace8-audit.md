# Card `X-FRONTIER-2` — First Blind-Sealed Verification of `physical` `P-C3e` (`39c903c42`: `12`-Mode Kernel, Numerical Light Couplings $(\lambda_+, \lambda_-)$, Two-Step Nonlinear Moment `IFT`, and `248`-Dim $E_8$ Eighth-Power Trace Law, `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Second sealed stage of Campaign `X-FRONTIER` (`four stages, sixteen blind-sealed commits, 0 of 19`), delivering the first standalone zero-import computational verification of `physical`'s five `P-C3e` hand derivations (`39c903c42` on `47e6078ae`) and evaluating the previously unevaluated normalized light cubic couplings $(\lambda_+, \lambda_-)$ on the punctured elliptic curve $E_\tau$ (`while keeping the infinite-dimensional cusp Hölder/Schauder Banach inverse lemma explicitly scoped in Tier II`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_frontier_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `2A` (`Complete 12-Mode Fixed-Sector Kernel & Elliptic Evaluation of \lambda_+, \lambda_-`):**
   - Do the swapped $D_5$ $(j, 0) \oplus (0, j)$ signs $\beta_j = (-1)^{(j+1)/2}$ give `0` compact sections at $j = 1$ and `2` neutral spin zero modes $N_\pm \in H^0(S^4 L_\delta(p))$ at $j = 3$, alongside `2` $D_5$ `(2, 2)` cross-forms (`exterior sign +1`), `1` neutral $Q$ form, `1` $Q$ gaugino, and `3 + 3` (`vs 2 + 2` misaligned) charged chiral modes (`total 12 vs 10`)?
   - In $W_3 = y A S T + \lambda_+ N_c P_c T + \lambda_- N_d R_c S$, does the two-term polarized gauge bracket equal $2 C \delta_-$ (`for \delta_N = \delta_+, vanishing for \delta_N = -\delta_+`), and on $E_\tau$ (`at \tau = i\sqrt{3}`) do the canonical Jacobi-theta/Weierstrass sections of $\mathcal{O}(p)$ (`constant 1`) vs $\xi(p)$ (`\vartheta_3/\vartheta_1`) produce convergent, nonzero, and **distinct** physical couplings $|\lambda_+| \ne |\lambda_-|$?
2. **Question `2B` (`Balanced Charged-Form Quartic Cancellation & Two-Step Real-Analytic IFT`):**
   - Along $X_{\mathrm{raw}}(t, \rho) = (A_0 + t(p + \rho r),\, q_0,\, r_0)$ acted on by $g = \exp(-\psi)$, does $F(g \cdot X_{\mathrm{raw}}) = 0$ hold identically at all orders, does $\psi_2 = t^2 P_v^+ d_2$ reduce the balanced ($\rho = 1$) $\mathcal{O}(t^4)$ potential to $\mathcal{O}(t^6)$ or higher, does two-step Newton `IFT` solve $(\Pi m = 0,\, \langle v_Q, m\rangle = 0)$ to `< (1/1000)^17` nonlinear residual at finite $t$, and does the Higgsed vector mass satisfy $m_Q^2(t) / t^2 \to 4 e_Q^2$?
3. **Question `2C` (`Full 248-Adjoint E_8 Nilpotent Pencil Ranks & Eighth-Power Trace Law`):**
   - Under $\mathfrak{so}(5)_+ \oplus \mathfrak{so}(5)_- \subset D_5 \subset E_8$, does `248` branch as `10 + 11×5 + 32×4 + 55×1 = 248`, giving `rank_248(ad(z_1 E_+ + z_2 E_-)) = 180` (`ker = 68`) for $z_1 z_2 \ne 0$ vs `148` (`ker = 100`) on a single factor, and on $X = a E_+ + b T_{(3, +)}$ do $\operatorname{Tr}_{248}(\operatorname{ad} X)^4 = 0$ and $\operatorname{Tr}_{248}(\operatorname{ad} X)^8 = \frac{15}{2}(\operatorname{Tr}_5 X^4)^2$ hold identically?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A`:** Exact character/divisor verification of the `12`-mode (`vs 10`-mode) fixed-sector kernel, `sp(4)` polarized gauge bracket verification, and multi-grid (`N_grid = 16 vs 24`) punctured-torus evaluation of $(\lambda_+, \lambda_-)$ on $E_{\tau = i\sqrt{3}}$.
2. **`Part 2B`:** `60`-digit finite-mode nonlinear Hermitian-gauge solver verifying $F = 0$, $\mathcal{O}(t^4)$ quartic cancellation at $\rho = 1$, exact all-orders `IFT` convergence $(\psi(t), \rho(t))$ at $t = 1/10$, and $m_Q^2(t) = 4 e_Q^2 t^2 + \mathcal{O}(t^3)$.
3. **`Part 2C`:** `60`-digit explicit $\mathfrak{sp}(4) \cong \mathfrak{so}(5)$ `248`-dimensional $E_8$ rank and eighth-power trace verification across `3` independent complex $(a, b)$ pairs.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_CompleteFixedKernel_and_LightCubic_Gate` (`Part 2A`):** $\beta_1 = -1, \beta_3 = +1$, `(2, 2)` exterior sign `= +1`, kernel counts `(12, 10)`, wrong-character $N_{-\delta_+}$ bracket `= 0`, and multi-grid convergence $|\lambda_\pm(24) - \lambda_\pm(16)| / |\lambda_\pm(24)| < 1/100$ with $|\lambda_+| > 0, |\lambda_-| > 0$, and $||\lambda_+| - |\lambda_-|| / |\lambda_+| > 1/20$.
2. **`E2_BalancedFormCancellation_and_TwoStepIFT_Gate` (`Part 2B`):** All-orders $F$-residual `= 0`, corrected $V(t) / V_{\mathrm{raw}}(t) < (1/1000)^2$ at $t = 1/100$, nonlinear two-step `IFT` residual `< (1/1000)^17` at $t = 1/10$, and $|m_Q^2(t)/(4 e_Q^2 t^2) - 1| < (1/1000)^5$ as $t \to 0$.
3. **`E3_FullE8PencilRanks_and_EighthPowerTrace_Gate` (`Part 2C`):** Branching sum `= 248`, ranks `(180, 148)` and kernels `(68, 100)` exact, $|\operatorname{Tr}_{248}(\operatorname{ad} X)^4| < (1/1000)^16$, and $|\operatorname{Tr}_{248}(\operatorname{ad} X)^8 - \frac{15}{2}(\operatorname{Tr}_5 X^4)^2| / |\frac{15}{2}(\operatorname{Tr}_5 X^4)^2| < (1/1000)^16$ across all `3` test points.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage2_Frontier_Passed`:** `AST` check confirming zero disallowed imports, `0` float literals, and `0` complex literals module-wide.
2. **`PC_FR2_WrongCharacterNeutralSpinCancelsCubic`:** Replacing $\delta_N = \delta_+$ by $-\delta_+$ annihilates the polarized $N P T$ cubic bracket (`= 0`).
3. **`PC_FR2_UnbalancedFormTangentLeavesQMoment`:** Setting $\rho = 2 \ne 1$ leaves a nonzero $Q$-moment projection $\langle v_Q, d_2\rangle \ne 0$, preventing $P_v^+$ from cancelling the $\mathcal{O}(t^4)$ potential (`ratio > 1/5` vs `< (1/1000)^2` on the balanced tangent).
4. **`PC_FR2_WrongE8BranchingBreaksTrace4And8`:** Omitting the `32` spinor `4`-plets from the `248` branching makes $\operatorname{Tr}(\operatorname{ad} X)^4 \ne 0$ and breaks the `15/2` eighth-power ratio (`rel err > 1/20`).

`0 of 19.`
