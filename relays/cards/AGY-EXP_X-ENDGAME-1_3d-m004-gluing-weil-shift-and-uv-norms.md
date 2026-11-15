# Card `X-ENDGAME-1` — Global Three-Dimensional Mapping-Torus Cohomology on `m004`, Exact Level-Three Metaplectic Weil Monodromy, Intrinsic Order-Fifteen Cover Emergence, and Derived Ultraviolet Normalizations (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** First sealed stage of Campaign `X-ENDGAME` (`five stages, twenty blind-sealed commits, 0 of 19`). Lifts `X-FUNNEL`'s two-dimensional punctured-torus magnetized overlap onto the three-dimensional mapping torus `m004` ($M_3 = (E^\times \times S^1)_M$, $M = LR = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$), resolving global flux extension, computing the exact level-three metaplectic Weil monodromy on the three chiral Landau generations, deriving why order fifteen emerges canonically without external prime selection, and replacing hand-entered ultraviolet coupling ratios with derived three-dimensional Kaluza–Klein overlap norms.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_endgame_1_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `1A` (`Global 3D Flux Extension & Exact Level-Three Weil Monodromy`):** Does integer magnetic flux $I = \pm 3$ on the torus fiber $E$ extend uniquely to a global $\mathrm{U}(1)$ bundle over `m004` ($M_3$), how does `m004`'s orientation-reversing amphichiral involution $J = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ act on chirality ($I = +3 \leftrightarrow -3$), and what is the exact $3 \times 3$ unitary metaplectic Weil monodromy $\mathcal{U}_M$ acting on the three spin-`(1/2, 1/2)` Landau zero modes around `m004`'s base circle?
2. **Question `1B` (`Intrinsic Emergence of Order Fifteen & Superselection vs Incoherent Sum`):** What minimal cyclic cover of `m004` is forced by requiring all three chiral Landau generations to close periodically around the base ($\mathcal{U}_M^n = I_3$), what is its flat holonomy kernel $\ker(M^{-n} - I_2)$ on $(\mathbb{R}/\mathbb{Z})^2$, and does discrete holonomy act as a spontaneous symmetry-breaking superselection vacuum or an incoherent `32`-point sum?
3. **Question `1C` (`Derived 3D Kaluza–Klein Gauge and Yukawa Ultraviolet Normalizations`):** Removing `X-FUNNEL-4`'s hand-chosen test ratios (`1/42`, `1/2`, `1/50`), what ultraviolet gauge ratios and undivided Yukawa singular-value ratios emerge directly from the rank-five $\mathrm{S}(\mathrm{U}(3) \times \mathrm{U}(2))$ bundle trace and three-dimensional cusp-collar normalization at $L_{\mathrm{cusp}} = 2\sqrt{3}$?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A` — Mayer–Vietoris Cohomology & Two-Route Level-Three Weil Monodromy:**
   - Verify explicitly from integer matrices (`zero literal boolean flags`) that $|\det(M^T - I_2)| = 1$ (`vanishing base-to-fiber H^2 torsion cokernel`) and $M^*([dx \wedge dy]) = +[dx \wedge dy]$ (`\det M = +1`), establishing $H^2(M_3; \mathbb{Z}) \xrightarrow{\sim} H^2(E; \mathbb{Z}) \cong \mathbb{Z}$, while amphichiral $J$ ($\det J = -1, J^2 = M$) sends $c_1 \mapsto -c_1$.
   - Verify the exact $\mathrm{SL}(2, \mathbb{Z})$ group-commutator factorization $M = LR = [T, S^{-1}] = T S^{-1} T^{-1} S$.
   - Compare **Route A** (closed-form twelfth-root algebraic matrices $(\mathcal{U}_T)_{r, c} = \delta_{r, c}\exp(i\pi(2r + 1)^2/12)$ and $(\mathcal{U}_S)_{r, c} = 3^{-1/2}\exp(-i\pi/6)\omega_3^{-(r+1)c}$) against **Route B** (direct `50`-digit `mpmath` theta-basis linear solver across independent $(\tau, z)$ evaluation points), verifying $\det\mathcal{U}_M = +1$, $\operatorname{Spec}(\mathcal{U}_M) = \{1, +i, -i\}$, and exact order `4` ($\mathcal{U}_M^4 = I_3$, $\|\mathcal{U}_M^2 - I_3\| > 1$).
2. **`Part 1B` — Minimal Generation-Closing Cover $M_3^{(4)}$, Cayley–Hamilton Order-Fifteen Theorem, and Superselection Audit:**
   - Prove and verify via Cayley–Hamilton ($\operatorname{tr} M = 3, \det M = 1 \implies M^2 + I_2 = 3M$) that on the minimal generation-closing cover $M_3^{(4)}$ (`degree 4`, forced by $\operatorname{Ord}(\mathcal{U}_M) = 4$), $|\det(M^4 - I_2)| = 45 = 5 \times 3^2$, decomposing $\ker(M^{-4} - I_2 \text{ on } (\mathbb{R}/\mathbb{Z})^2)$ into `1` trivial + `4` order-`5` ($\mathcal{O}_4$) + `8` non-zero order-`3` ($E[3]\setminus\{0\}$) + `32` primitive order-`15` ($\mathcal{O}_{32}$) points.
   - Verify that one-loop Casimir energy attains its global maximum on $\ker(M^{-4} - I_2)$ at $w = (0, 0)$ (`dynamically destabilizing trivial holonomy`), while incoherent averaging of $H_f$ over all `32` points of $\mathcal{O}_{32}$ washes the lighter singular-value ratio above `98/100` (`establishing superselection vacuum selection and recording the exact discrete bit cost`).
3. **`Part 1C` — Derived Ultraviolet Gauge and Yukawa Normalizations:**
   - Verify exact rank-five $\mathrm{S}(\mathrm{U}(3) \times \mathrm{U}(2))$ trace unification $\operatorname{Tr}_{\mathbf{5}}(T_3^a T_3^b) = \operatorname{Tr}_{\mathbf{5}}(T_2^i T_2^j) = \frac{1}{2}\delta^{ab}$ and $\operatorname{Tr}_{\mathbf{5}}(Y_{\mathrm{diag}}^2) = \frac{5}{6} = \frac{5}{3} \cdot \frac{1}{2}$.
   - Compute undivided triple-overlap norms at $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$: verify automatic raw `sec2`–`sec3` unification $\sigma_3^{(2)}/\sigma_3^{(3)} \in [1, 106/100]$, expose the flat-base single-doublet tension ($\sigma_3^{(1)}/\sigma_3^{(2)} \in [7/10, 9/10]$), and verify that three-dimensional cusp-collar localization on $[0, L_{\mathrm{cusp}}]$ coupled to $T_{3R} = Y - (B - L)/2$ preserves exact `sec2`–`sec3` unification while generating $\sigma_3^{(1)}/\sigma_3^{(2)} = r_{\mathrm{raw}}\exp(L_{\mathrm{cusp}}) \in [25, 32]$ (`whereas pure hypercharge localization breaks sec2/sec3 by > 50`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_Global_Cohomology_and_Weil_Order4` (`Part 1A`):**
   - $|\det(M^T - I_2)| = 1$, $\det M = +1$, $\det J = -1$, $J^2 = M$, and $M = T S^{-1} T^{-1} S$ hold identically.
   - `Route A` and `Route B` agree on $\mathcal{U}_T, \mathcal{U}_S, \mathcal{U}_M$ across two distinct bulk/cusp moduli and independent $z$-test points to `< (1/1000)^{13}`.
   - $|\det\mathcal{U}_M - 1| < (1/1000)^{13}$, eigenvalues of $\mathcal{U}_M$ match $\{1, +i, -i\}$ to `< (1/1000)^{13}`, $\|\mathcal{U}_M^4 - I_3\|_F < (1/1000)^{13}$, while $\|\mathcal{U}_M - I_3\|_F > 1$ and $\|\mathcal{U}_M^2 - I_3\|_F > 1$.
2. **`E2_Cayley_Hamilton_Order15_and_Superselection` (`Part 1B`):**
   - Exact enumeration of $w \in \frac{1}{45}\mathbb{Z}^2 / \mathbb{Z}^2$ satisfying $w M^{-4} \equiv w \pmod 1$ yields `45` points (`1` of order `1`, `4` of order `5`, `8` of order `3`, `32` of primitive order `15`), with $M^2 + I_2 = 3M$ verified entrywise.
   - At $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$, $\mathcal{V}_{\mathrm{Cas}}(\tau_{\mathrm{cusp}}, (0, 0))$ strictly exceeds all `44` non-zero points of $\ker(M^{-4} - I_2)$ by `> 60`, while incoherent `32`-point averaging yields $(\sigma_1/\sigma_2)_{\mathrm{sec1}} > 98/100$ vs single-vacuum $(\sigma_1/\sigma_2)_{\mathrm{sec1}} < 35/100$ on `(4/15, 8/15)`.
3. **`E3_Derived_UV_Gauge_and_Yukawa_Norms` (`Part 1C`):**
   - Rank-five trace ratios satisfy $g_1^2 / g_2^2 = 1$ and $g_2^2 / g_3^2 = 1$ (`with hypercharge normalization factor 5/3`) to `< (1/1000)^5`.
   - At $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$ and `(4/15, 8/15)`, undivided $\sigma_3^{(2)}/\sigma_3^{(3)} \in [1, 106/100]$, flat-base $\sigma_3^{(1)}/\sigma_3^{(2)} \in [8/10, 9/10]$, and $T_{3R}$ cusp-collar localization at $L_{\mathrm{cusp}} = 2\sqrt{3}$ gives $\sigma_3^{(1)}/\sigma_3^{(2)} \in [25, 32]$ while keeping $\sigma_3^{(2)}/\sigma_3^{(3)}$ unchanged to `< (1/1000)^5` (`vs pure hypercharge localization breaking sec2/sec3 by > 50`).

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar_Stage1`:** Ten random gauge-allowed $\mathrm{U}(3)^5$ basis scramblings leave all derived undivided singular-value ratios and inter-sector ratios invariant to `< (1/1000)^4`.
2. **`PC_ENDGAME1_EvenSpinWeil`:** Replacing spin `(1/2, 1/2)` by spin `(0, 0)` in the level-three theta basis breaks $\mathrm{SL}(2, \mathbb{Z})$ closure of the `3`-dimensional space under $T$ (`residual > 1/10` at test $z$).
3. **`PC_ENDGAME1_Degree2Cover`:** Restricting from the `4`-fold generation-closing cover $M_3^{(4)}$ (`M^4 - I_2`) to the `2`-fold cover (`M^2 - I_2`) drops $|\det(M^2 - I_2)|$ to `5` (`zero` order-`15` points!).
4. **`PC_ENDGAME1_PureHyperchargeCollar`:** Replacing $T_{3R} = Y - (B - L)/2$ by raw hypercharge $Y = q/6$ in the cusp-collar profile destroys `sec2`–`sec3` unification (`\sigma_3^{(2)}/\sigma_3^{(3)} > 50`).

`0 of 19.`
