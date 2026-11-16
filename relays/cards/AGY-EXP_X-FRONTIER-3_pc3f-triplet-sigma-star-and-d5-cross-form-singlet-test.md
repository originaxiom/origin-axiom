# Card `X-FRONTIER-3` — First Blind-Sealed Verification of `physical` `P-C3f` (`47e6078ae`), First Numerical Evaluation of the Triplet Mass Constant $\sigma_* > 0$, and Prospective $D_5$ `(2, 2)` Cross-Form `3rd`-Singlet Lifting Test (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Third sealed stage of Campaign `X-FRONTIER` (`four stages, sixteen blind-sealed commits, 0 of 19`), delivering the first standalone zero-import verification of `physical`'s `P-C3f` (`47e6078ae`), the first numerical computation of the previously unevaluated colour-triplet quadratic mass coefficient $\sigma_* > 0$ via elliptic Kronecker–Dolbeault Green operators $G_B, G_C$, and the prospective test of `physical`'s stated next push (`whether the two retained neutral D_5 (2, 2) cross-forms (B_1, B_2) lift the remaining massless charge-1 singlet pair`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_frontier_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `3A` (`P-C3f` — Exact `3`-Pivot Cyclic Spinor Corner Contraction & `(18, 16, 8)` Kernel Table):**
   - Does the `3`-pivot homotopy on $Q_z = \begin{psmallmatrix} 0 & c_1 & 0 & 0 \\ 0 & 0 & c_2 & 0 \\ 0 & 0 & 0 & c_3 \\ f_z & 0 & 0 & 0 \end{psmallmatrix}$ satisfy $h \circ \mathrm{corner} = \mathrm{corner} \circ h = 0$ (`contracting 16 -> 32 -> 16 to A --(f_1, f_2)--> B + C --(-f_2, f_1)--> D with zero higher HPT corners and zero division by f_1, f_2`)?
   - Do radial $L^2$ pole bounds at $a \in \{-3, 1, 1, 5\}$ give compact degrees `(-2, 0, 0, 2)`, and do the divisor/Koszul sheaf lengths reproduce `(18, 16, 8)` on coherent odd/aligned vs `(16, 16, 8)` on misaligned across `(origin, single-axis, generic z_0 z_1 != 0)`?
2. **Question `3B` (`P-C3f` — First Numerical Computation of the Colour-Triplet Mass Constant $\sigma_* > 0$):**
   - On $E_{\tau = i\sqrt{3}}$ with nontrivial order-`3` Wilson character $\chi_3 = (\omega_3, 1)$ (`so both middle lines \bar{B} and \bar{C} = \bar{B} \otimes \xi are acyclic`), does $K_* = F_0 G_C F_1 - F_1 G_B F_0$ evaluated between unit-norm bases of $H^1(\bar{A})$ (`dim = 2`) and $H^0(\bar{D})$ (`dim = 2`) have **exact rank `1`** (`\sigma_2(K_*) / \sigma_1(K_*) < (1/1000)^3`) and yield a convergent positive singular value $\sigma_* = \sigma_1(K_*) > 0$ across torus Fourier grids $M \in \{16, 24, 32\}$?
3. **Question `3C` (`Prospective Test — Coupled D_5 (2, 2) Cross-Forms (B_1, B_2) on the Massless 3rd Singlet Pair`):**
   - When the two retained neutral $D_5$ `(2, 2)` cross-form zero modes $(B_1, B_2)$ (`weight w = 4`) are turned on alongside the cyclic neutral spin modes $(N_+, N_-)$ (`weight w = -3`), how do they act in the `16D` $V_{3/2} \otimes V_{3/2}$ spinor-product mass operator and endpoint quotient: do they lift the `3rd` charge-`1` singlet pair at higher order (`giving 3 nonzero singular values`) or encounter an exact weight/slot selection rule (`preserving 1 exact zero mode`), and what is the exact algebraic mechanism?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A`:** Symbolic `SymPy` proof of `16 -> 32 -> 16` `3`-pivot cyclic corner contraction, compact pole degrees `(-2, 0, 0, 2)`, and `(18, 16, 8)` vs `(16, 16, 8)` Koszul kernel counts.
2. **`Part 3B`:** Spectral Dolbeault Green-operator construction of $G_B = \bar{\partial}_B^{-1}$ and $G_C = \bar{\partial}_C^{-1}$ on $E_{\tau = i\sqrt{3}}$ across $M \in \{16, 24, 32\}$, proving $\operatorname{rank}(K_*) = 1$ and determining $\sigma_* > 0$ (`with single-axis control K_* = 0`).
3. **`Part 3C`:** Explicit `248` / `16D` spinor-product weight-and-slot operator evaluation of $(B_1, B_2) + (N_+, N_-)$ on the `3`-pair charge-`1` singlet subspace, certifying either the exact lifting order or the exact selection rule without pre-biasing the outcome.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_CyclicCornerContraction_and_KoszulTable_Gate` (`Part 3A`):** `SDR` and zero-higher-corner identities hold symbolically (`exact 0`), generic fibre ranks equal `(16, 16)` vs `(15, 15)` at common zeros, compact degrees equal `[-2, 0, 0, 2]`, and `128`-block counts equal `[18, 16, 8]` (`aligned/odd`) and `[16, 16, 8]` (`misaligned`).
2. **`E2_TripletGreenOperator_RankOne_and_SigmaStar_Gate` (`Part 3B`):** Minimum $|\lambda_{\bar{\partial}}|$ on $\bar{B}, \bar{C}$ is strictly positive (`> 1/2`), $\sigma_2(K_*) / \sigma_1(K_*) < (1/1000)^3$ (`confirming rank 1`), $\sigma_*(32) > 0$, and multi-grid convergence $|\sigma_*(32) - \sigma_*(24)| / \sigma_*(32) < 1/20$.
3. **`E3_ProspectiveCrossForm_SingletMechanism_Gate` (`Part 3C`):** Exact symbolic/numerical matrix construction of the $D_5$ `(2, 2)` highest-weight action on $V_{3/2} \otimes V_{3/2}$ (`verifying w = +4 maps (-3/2, -3/2) / (-1/2, -3/2) -> (+1/2, +1/2) / (+3/2, +1/2) in the form-to-spin Dolbeault/Clifford channel`), deterministically certifying the resulting `3`-singlet singular-value rank (`3` if lifted vs `2` if protected) to `< (1/1000)^4` basis-invariance precision.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage3_Frontier_Passed`:** `AST` check confirming zero disallowed imports, `0` float literals, and `0` complex literals module-wide.
2. **`PC_FR3_SingleAxisVanishingKStar`:** Setting either $\nu_0 = 0$ or $\nu_1 = 0$ forces $K_* = 0$ identically (`Frobenius norm = 0`), restoring `2` colour-triplet zero modes on the coordinate axes.
3. **`PC_FR3_TrivialSingletMiddleLinePole`:** Removing the order-`3` colour twist $\chi_3 \to (1, 1)$ produces a zero Fourier eigenvalue `(m, n) = (0, 0)` on $\bar{B} = \mathcal{O}$, proving $G_B$ does not exist without projecting out the singlet spin zero mode.
4. **`PC_FR3_SwappedKoszulSignBreaksHolomorphicity`:** Flipping the Koszul sign in $K_{\mathrm{bad}} = F_0 G_C F_1 + F_1 G_B F_0$ breaks $\bar{\partial}(K_* \alpha) = 0$ (`\bar{\partial}-residual > 1/10`), destroying cohomology well-definedness.

`0 of 19.`
