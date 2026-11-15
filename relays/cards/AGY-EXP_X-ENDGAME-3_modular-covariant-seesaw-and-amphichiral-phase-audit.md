# Card `X-ENDGAME-3` — Modular-Covariant Puncture-Jet Seesaw Operator on `q = 0`, Six-Unitary Haar Basis Invariance, Unified `V_{12}` vs `U_{34}` Mixing Contrast, and Amphichiral Determinant-Phase Audit (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Third sealed stage of Campaign `X-ENDGAME` (`five stages, twenty blind-sealed commits, 0 of 19`). Extends the three-sector Dirac dictionary on `m004` (`sec1`, `sec2`, `sec3`) to the fourth chiral sector `sec4` at charges `(-3, 0, +3)` coupled to a parameter-free $\mathrm{SL}(2, \mathbb{Z})$-covariant symmetric Majorana puncture-jet bilinear $M_R(\tau)$ on the unshifted singlet sector `q = 0`, contrasts `U_{34}` mixing against `V_{12}` mixing at the Stage `1`–`2` geometry $(\tau^* = 2\sqrt{3}\,i, w = (4/15, 8/15))$, and audits $\arg\det(Y_1 Y_2)$ on single chiral slices versus amphichiral parity-completed `m004`.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_endgame_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `3A` (`Exact SL(2, Z)-Covariant Symmetric Puncture-Jet Bilinear M_R(tau) & Full Rank`):** Because the right-handed singlet sector carries charge `q = 0`, its three Landau modes transform under $T$ and $S$ by constant Weil unitaries $(U_R(T), U_R(S))$ independent of $w$. Can a parameter-free, symmetric, weight-zero $3 \times 3$ Majorana matrix $M_R(\tau)$ transforming in $\operatorname{Sym}^2(U_R^*)$ be constructed purely from the puncture value $\vartheta(0, 3\tau)$, first $z$-derivative $\partial_z\vartheta(0, 3\tau)$, and Ramanujan–Serre covariant $\tau$-derivative $D_{3/2}(\partial_z\vartheta)(0, 3\tau)$ dressed by classical Eisenstein forms $(E_6, E_4)$, making the seesaw operator $\mathcal{W}_4(\tau, w) = Y_4(\tau, w) M_R(\tau)^{-1} Y_4(\tau, w)^T$ strictly $\mathrm{SL}(2, \mathbb{Z})$-covariant in **absolute** singular values?
2. **Question `3B` (`Six-Unitary U(3)^6 Haar Scrambling & Unified V_{12} vs U_{34} Mixing Contrast`):** Under six independent gauge-allowed chiral rotations $(U_Q, U_{1R}, U_{2R}, U_L, U_{3R}, U_{4R}) \in \mathrm{U}(3)^6$ (`with symmetric Majorana transformation M_R -> U_{4R}^* M_R U_{4R}^\dagger`), are all singular-value ratios and all nine entries of $|V_{12}|$ and $|U_{34}|$ strictly basis-invariant, and does unshifted `q = 0` puncture parity automatically generate near-maximal `U_{34}` off-diagonal mixing alongside small `V_{12}` mixing at $(\tau^*, (4/15, 8/15))$?
3. **Question `3C` (`Zero-Fudge Amphichiral Determinant-Phase Audit`):** Computing $\arg\det(Y_1 Y_2)$ directly from explicit matrices (`zero literal zero flags`), does `m004`'s orientation-reversing mirror pairing $w \oplus R(w)$ (`R(a, b) = (a, -b)` at $\operatorname{Re}\tau^* = 0$, where $\operatorname{CS}(m004) = 0$) cancel $\arg\det$ identically, while a single chiral `3x3` slice $w = (4/15, 8/15)$ retains an un-cancelled $O(1)$ phase?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A` — Weight-Zero Symmetric Puncture-Jet Operator $M_R(\tau)$ and Exact $T, S$ Covariance:**
   - Construct $M_R(\tau) = y^3 \overline{E_6(\tau)}\, v(\tau)v(\tau)^T + y^2 \overline{E_4(\tau)}\, w(\tau)w(\tau)^T + u(\tau)u(\tau)^T$ at `35`-digit precision, where $v, w, u$ are the spin-`(1/2, 3/2)` puncture value, $z$-gradient, and Serre derivative at $z = 0$.
   - Verify exact symmetry $\|M_R - M_R^T\|_F < (1/1000)^{10}$, full rank `3` (`\sigma_1(M_R)/\sigma_3(M_R) > (1/1000)^3` vs `< (1/1000)^{10}` when omitting $u(\tau)$), and exact $T$- and $S$-covariance of both $M_R(\tau)$ and the absolute singular values of $\mathcal{W}_4(\tau, w)$ at a generic bulk point $(\tau, w)$ to `< (1/1000)^8`.
2. **`Part 3B` — Six-Unitary $\mathrm{U}(3)^6$ Haar Gate and `V_{12}` vs `U_{34}` Mixing Evaluation at $(\tau^*, (4/15, 8/15))$:**
   - Evaluate $Y_1, Y_2, Y_3, Y_4, M_R$, and $\mathcal{W}_4 = Y_4 M_R^{-1} Y_4^T$ at $(\tau^* = 2\sqrt{3}\,i, w = (4/15, 8/15))$ (`including the exact T_{3R} cusp-collar factor on Y_4 matching Y_1`).
   - Run `10` independent random $\mathrm{U}(3)^6$ Haar basis scramblings in `35`-digit precision (`transforming M_R -> U_{4R}^* M_R U_{4R}^\dagger`), verifying invariance of all singular-value ratios and all `9` entries of $|V_{12}|$ and $|U_{34}|$ to `< (1/1000)^6`.
   - Record all `9` entries of $|V_{12}|$ and $|U_{34}|$ verbatim, testing whether maximal off-diagonal $|V_{12}|$ is `< 3/100` while maximal off-diagonal $|U_{34}|$ exceeds `65/100` (`sin^2(2 theta) > 99/100` in the parity-mixed `2x2` block, while honestly recording the smaller sequential third-mode angle).
3. **`Part 3C` — Amphichiral Determinant-Phase Audit (`Single Slice vs Parity Pair`):**
   - Compute $\arg\det(Y_1 Y_2)$ at $(\tau^*, (4/15, 8/15))$, at its amphichiral mirror $(4/15, -8/15)$, and on the `6x6` parity-completed direct sum $(Y_1(w) \oplus Y_1(R w))(Y_2(w) \oplus Y_2(R w))$, plus across all `4` points of $\mathcal{O}_4$.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_Symmetric_Seesaw_Modular_Covariance` (`Part 3A`):**
   - $\|M_R(\tau) - M_R(\tau)^T\|_F / \|M_R(\tau)\|_F < (1/1000)^{10}$, $\sigma_1(M_R(\tau^*))/\sigma_3(M_R(\tau^*)) > (1/1000)^3$, and both $T$- and $S$-covariance residuals of $M_R(\tau)$ and of the **absolute** singular values of $\mathcal{W}_4(\tau, w)$ are `< (1/1000)^8`.
2. **`E2_Haar_U3_6_and_Large_vs_Small_Mixing` (`Part 3B`):**
   - Across `10` random $\mathrm{U}(3)^6$ trials, maximum deviation across all singular-value ratios and all `18` mixing matrix moduli (`9` of $|V_{12}|$ + `9` of $|U_{34}|$) is `< (1/1000)^6` (`strictly < (1/1000)^4` guardrail).
   - At $(\tau^* = 2\sqrt{3}\,i, w = (4/15, 8/15))$, maximal off-diagonal $|V_{12}| < 3/100$, whereas maximal off-diagonal $|U_{34}| \in [65/100, 75/100]$ (`near-maximal 2-sector mixing > 20x larger than V_{12}`).
3. **`E3_Amphichiral_Determinant_Phase_Theorem` (`Part 3C`):**
   - Single-slice phase satisfies $|\arg\det(Y_1(\tau^*, w) Y_2(\tau^*, w))| \in [1/2, 1]$ (`non-zero`), mirror reflection satisfies $|\arg\det(w) + \arg\det(R w)| < (1/1000)^{10}$, and the `6x6` parity-completed block determinant has $|\arg\det| < (1/1000)^{10}$.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar_Stage3`:** Ten random $\mathrm{U}(3)^6$ scramblings (`including symmetric Majorana rotation on q = 0`) leave all physical observables invariant to `< (1/1000)^4`.
2. **`PC_ENDGAME3_DiracSesquilinearMismatch`:** Replacing $M_R(\tau)$ by the Hermitian zero-holonomy Dirac overlap $Y_{(0,0)}(\tau) P_C$ breaks $S$-covariance of $\mathcal{W}_4$ (`singular-value ratio error > 1/2`).
3. **`PC_ENDGAME3_Rank2JetSingularity`:** Dropping the Serre-derivative third jet vector $u(\tau)$ collapses $M_R(\tau^*)$ to rank `2` (`\sigma_1(M_R)/\sigma_3(M_R) < (1/1000)^{12}`).
4. **`PC_ENDGAME3_SingleSlicePhaseNonZero`:** Asserts from explicit determinants (`zero literal flags`) that single-slice $|\arg\det(Y_1 Y_2)| > 1/2$, preventing any false claim of single-slice determinant-phase vanishing without parity completion.

`0 of 19.`
