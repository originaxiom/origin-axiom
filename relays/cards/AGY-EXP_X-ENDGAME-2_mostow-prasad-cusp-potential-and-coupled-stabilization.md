# Card `X-ENDGAME-2` — Target-Free Mostow–Prasad Hyperbolic Gluing, Two-Route Cusp Rigidity, and Coupled Three-Dimensional plus Two-Dimensional Casimir Stabilization on `m004` (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Second sealed stage of Campaign `X-ENDGAME` (`five stages, twenty blind-sealed commits, 0 of 19`). Attacks the continuous modulus selection problem (`Selection`) without hand-embedded target coordinates by solving `m004`'s combinatorial ideal-tetrahedron gluing curve and knot-group parabolic holonomy from generic rational starting points, verifying `m004`'s complex volume and vanishing Chern–Simons invariant from explicit matrices and Rogers dilogarithms, and testing coupled three-dimensional Einstein–Hilbert + Maxwell flux + two-dimensional Casimir stabilization of `(z_1, z_2, A)`.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_endgame_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `2A` (`Target-Free Mostow–Prasad Rigidity, Two-Route Cusp Modulus, and Complex Volume`):** Starting purely from `m004`'s integer edge-gluing polynomial $z_1(z_1 - 1)z_2(z_2 - 1) = 1$ (`Route A`: minimizing $-\operatorname{Vol}(z_1, z_2)$ without even imposing completeness by hand!) and independently from the Wirtinger knot-group relation $w x = y w$ (`Route B`: parabolic $\mathrm{SL}(2, \mathbb{C})$ Newton solver), do arbitrary rational initial guesses converge to a unique complete hyperbolic structure, what cusp modulus $\tau_{\mathrm{cusp}}^{\mathrm{m004}}$ and Chern–Simons invariant emerge, and how does amphichiral knot-group conjugation intertwine $\rho$ with $\overline{\rho}$?
2. **Question `2B` (`Coupled 3D + 2D Modulus Stabilization & Critical Loop Threshold`):** When the two-dimensional one-loop Casimir energy $\mathcal{V}_{\mathrm{Cas}}(\tau_{\mathrm{NZ}}(z), w)$ on `w = (4/15, 8/15)` is coupled directly along `m004`'s Neumann–Zagier deformation curve $\tau_{\mathrm{NZ}}(z) = dv/du(z)$ to the three-dimensional Einstein–Hilbert action $-\operatorname{Vol}(z_1, z_2)$, does the complete point remain a strict local minimum at the standard one-loop coupling $\alpha_{\mathrm{loop}} = 1/(16\pi^2)$, and where is the critical instability bifurcation $\alpha_{\mathrm{crit}}$?
3. **Question `2C` (`Joint Horospherical Cusp Area + Shape Stabilization vs Runaway Controls`):** Coupling truncated hyperbolic cusp volume cost $+\frac{1}{2}A$, quantized $I = 3$ magnetic flux repulsion $+\frac{2\pi^2 I^2}{A}$, and one-loop Casimir density $+\frac{1}{16\pi^2 A^2}\mathcal{V}_{\mathrm{Cas}}(\tau_{\mathrm{NZ}}(z), w)$, does joint three-variable Newton optimization over $(\operatorname{Re} z_1, \operatorname{Im} z_1, A)$ converge from distinct initial seeds to a positive-definite local minimum $(z_1^*, A^*)$, and what ultraviolet barrier separates $A^*$ from short-distance Casimir attraction?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A` — AST-Verified Target-Free Hyperbolic Volume Minimization & Two-Route Cusp Equivalence:**
   - Enforce an `AST` source check confirming zero imports from `main` or other relays AND confirming that the optimization routines contain zero embedded irrational target literals (`no sqrt(3), no pi/3`).
   - **Route A (`3D Bloch–Wigner Variational Principle`):** Minimize $-\big(D_2(z_1) + D_2(z_2(z_1))\big)$ along $z_1(z_1 - 1)z_2(z_2 - 1) = 1$ from four distinct rational initial seeds `(1/4, 19/20)`, `(18/25, 13/20)`, `(41/100, 61/50)`, `(63/100, 27/25)`. Verify emergent completeness $|H(\mu) - 1| < (1/1000)^6$, $|H(\lambda) - 1| < (1/1000)^6$, positive-definite Hessian eigenvalues, Neumann–Zagier cusp modulus $\tau_{\mathrm{NZ}}(z^*)$, and vanishing Chern–Simons part $\operatorname{Im}\big[-i(L(z_1^*) - L(1 - z_2^*))\big]$ from Rogers dilogarithms (`zero literal 0 flags`).
   - **Route B (`Parabolic Knot-Group Holonomy & Amphichiral Intertwiner`):** Solve $w x - y w = 0$ by Newton's method from a rational complex seed `(3/10 + 9/10 i)`, extract the canonical commuting longitude matrix $\rho(\lambda^{-1})$, verify agreement between `Route A` $\tau_{\mathrm{NZ}}(z^*)$ and `Route B` $\rho(\lambda^{-1})_{0,1}/\rho(\lambda^{-1})_{0,0}$ to `< (1/1000)^8`, and solve explicitly for $C \in \mathrm{SL}(2, \mathbb{C})$ intertwining $\rho(\iota(g))$ with $\overline{\rho(g)}$ under $\iota(x) = x^{-1}, \iota(y) = y x^{-1} y^{-1}$.
2. **`Part 2B` — Coupled Cusp-Shape Stability & Critical Loop Bifurcation:**
   - Evaluate the $2 \times 2$ real Hessian of $-\operatorname{Vol}(z) + \alpha\,\mathcal{V}_{\mathrm{Cas}}(\tau_{\mathrm{NZ}}(z), (4/15, 8/15))$ at the converged variational root $z^*$. Verify strict positive-definiteness at both $\alpha = 0$ and $\alpha_{\mathrm{loop}} = 1/(16\pi^2)$, compute the exact critical coupling $\alpha_{\mathrm{crit}}$ where the lower Hessian eigenvalue crosses zero, and verify instability for $\alpha = 1/100 > \alpha_{\mathrm{crit}}$.
3. **`Part 2C` — Joint Three-Variable `(Re z_1, Im z_1, A)` Optimization & Ultraviolet Barrier Audit:**
   - Run full $3 \times 3$ Newton optimization of $\mathcal{S}_{\mathrm{eff}}(\operatorname{Re} z_1, \operatorname{Im} z_1, A)$ from multiple initial seeds `(Re z_1, Im z_1, A_0)`. Verify convergence to a common root $(z_1^*, A^*)$ with $A^* \in [18, 19]$, gradient norm `< (1/1000)^4`, and all three eigenvalues of the $3 \times 3$ Hessian strictly positive, while also locating and reporting the short-distance ultraviolet barrier $A_{\mathrm{UV}} \in [1/1000, 1/100]$ and its barrier height $\Delta\mathcal{S} > 25000$.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_TargetFree_Mostow_and_TwoRoute_Cusp` (`Part 2A`):**
   - All four rational initial seeds converge to the same $(z_1^*, z_2^*)$ within `< (1/1000)^6`, with emergent completeness $|H(\mu) - 1| < (1/1000)^6$ and $|H(\lambda) - 1| < (1/1000)^6$.
   - `Route A` $\tau_{\mathrm{NZ}}(z^*)$ and `Route B` parabolic longitude translation $\tau_{\mathrm{Riley}}$ agree to `< (1/1000)^8`, Rogers-dilogarithm Chern–Simons invariant satisfies $|\operatorname{CS}(z^*)| < (1/1000)^8$, and the explicit $\mathrm{SL}(2, \mathbb{C})$ amphichiral intertwiner satisfies $\|C\rho(\iota(g))C^{-1} - \overline{\rho(g)}\|_F < (1/1000)^{10}$ for both generators.
2. **`E2_Coupled_Modulus_Stability_at_OneLoop` (`Part 2B`):**
   - At $\alpha_{\mathrm{loop}} = 1/(16\pi^2)$, the coupled $2 \times 2$ Hessian at $z^*$ has minimum eigenvalue `> 1/10` (`strict local minimum`), with critical bifurcation threshold $\alpha_{\mathrm{crit}} \in [6/1000, 7/1000]$.
3. **`E3_Joint_Shape_and_Area_Stabilization` (`Part 2C`):**
   - Three-variable Newton optimization from distinct initial seeds converges to a unique $(z_1^*, A^*)$ with $A^* \in [18, 19]$, $\|\nabla\mathcal{S}_{\mathrm{eff}}\| < (1/1000)^4$, and minimum $3 \times 3$ Hessian eigenvalue `> 5/100`, separated from $A \to 0$ by an ultraviolet barrier of height `> 25000`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_ZeroTargetLiterals`:** `AST` inspection verifies zero disallowed imports and zero embedded irrational target constants inside the root-finders and potential definitions.
2. **`PC_ENDGAME2_OvercoupledCasimir`:** Increasing the loop weight to $\alpha = 1/100 > \alpha_{\mathrm{crit}}$ flips the lower cusp-shape Hessian eigenvalue strictly negative (`< -1/2`), proving Mostow stiffness can be overwhelmed if quantum backreaction is too large.
3. **`PC_ENDGAME2_ZeroFluxCollapse`:** Setting magnetic flux $I = 0$ removes the $+2\pi^2 I^2 / A$ repulsion and destroys the positive-definite minimum in $A \in [1, 50]$ (`dS/dA > 0` across `[1, 50]`, driving $A \to 0$).
4. **`PC_ENDGAME2_ZeroVolumeCutoffRunaway`:** Removing the hyperbolic cusp truncation cost (`setting c_vol = 0`) eliminates the confining $+A/2$ term (`dS/dA < 0` for all $A > 1$, driving decompactification $A \to \infty$).

`0 of 19.`
