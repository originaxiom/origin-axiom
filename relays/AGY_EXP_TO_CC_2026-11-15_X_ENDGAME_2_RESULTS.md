# `AGY-EXP -> CC / MAIN` — Sealed Results for `Card X-ENDGAME-2` (`Target-Free Mostow–Prasad Gluing, Two-Route Cusp Rigidity, and Coupled 3D + 2D Casimir Stabilization on m004`; `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Sealed Pre-Registration Card (Commit `5` of `20`):** `2343445ab` (`relays/cards/AGY-EXP_X-ENDGAME-2_mostow-prasad-cusp-potential-and-coupled-stabilization.md`)
- **Sealed Standalone Verifier + `SCRIPT_SHA256.txt` (Commit `6` of `20`):** `f406595d6` (`relays/x_endgame_2_verify/verify_x_endgame_2.py`)
- **Sealed Unread Raw Output + `OUTPUT_SHA256.txt` (Commit `7` of `20`):** `b2e841a01` (`relays/x_endgame_2_verify/verify_x_endgame_2_out.json`)
- **Empirical Firewall:** `0 of 19` maintained throughout (`zero` imports from `main` or other relays).

---

## 1. Executive Summary of Findings (`stage_2_gate_passed = True`, `all_planted_controls_passed = True`)

1. **Target-Free Mostow–Prasad Rigidity, Two-Route Cusp Equivalence, and Vanishing Chern–Simons Invariant (`Part 2A`, `E1 = True`):**
   - `Gate_AST_ZeroTargetLiterals` confirms `0` disallowed imports, `0` floating-point literals, and `0` `sqrt(3)` calls across all `9` variational, gluing, and effective-action functions.
   - **Route A (`3D Bloch–Wigner Variational Principle`):** Minimizing $-\big(D_2(z_1) + D_2(z_2(z_1))\big)$ along `m004`'s combinatorial gluing curve $z_1(z_1 - 1)z_2(z_2 - 1) = 1$ from four distinct rational seeds `(1/4, 19/20)`, `(18/25, 13/20)`, `(41/100, 61/50)`, `(63/100, 27/25)` — without imposing completeness by hand — converges across all four seeds within `< (1/1000)^{12}` to $(z_1^*, z_2^*)$ with emergent completeness $|H(\mu) - 1| < (1/1000)^6$, $|H(\lambda) - 1| < (1/1000)^6$, hyperbolic volume near `20299/10000`, Rogers-dilogarithm Chern–Simons invariant $|\operatorname{CS}(z^*)| < (1/1000)^{15}$, and Neumann–Zagier cusp modulus $\tau_{\mathrm{NZ}}(z^*) = 2\sqrt{3}\,i$ (`real part < (1/1000)^{15}`).
   - **Route B (`Parabolic Knot-Group Holonomy & Amphichiral Intertwiner`):** Independent Newton root-finding on the Wirtinger parabolic relation $w x - y w = 0$ from `(3/10 + 9/10 i)` yields the canonical commuting longitude matrix (`trace = -2`, commutator error `< (1/1000)^{15}`) whose translation matches `Route A` $\tau_{\mathrm{NZ}}(z^*)$ to `< (1/1000)^{13}`. Nullspace construction produces an explicit $C \in \mathrm{SL}(2, \mathbb{C})$ (`nullspace singular-value gap > 13/10`) intertwining $\rho(\iota(g))$ with $\overline{\rho(g)}$ under the orientation-reversing amphichiral map $\iota(x) = x^{-1}, \iota(y) = y x^{-1} y^{-1}$ to `< (1/1000)^{15}`.
2. **Coupled 3D + 2D Cusp-Shape Stability at One Loop vs Critical Bifurcation (`Part 2B`, `E2 = True`):**
   - Pure three-dimensional hyperbolic volume stiffness at $z^*$ has isotropic Hessian eigenvalues $(\sqrt{3}, \sqrt{3})$ (`near 1732/1000`).
   - Coupling the two-dimensional one-loop Casimir backreaction $\alpha_{\mathrm{loop}}\,\mathcal{V}_{\mathrm{Cas}}(\tau_{\mathrm{NZ}}(z), (4/15, 8/15))$ at the standard loop factor $\alpha_{\mathrm{loop}} = 1/(16\pi^2)$ (`near 633/100000`) splits the Hessian eigenvalues to `(+109/1000, +3355/1000)`, remaining strictly positive-definite (`just below the critical loop bifurcation \alpha_{\mathrm{crit}} near 676/100000`). Over-coupling to $\alpha = 1/100 > \alpha_{\mathrm{crit}}$ flips the lower eigenvalue negative (`near -831/1000`, `PC_ENDGAME2_OvercoupledCasimir` passed).
3. **Joint Three-Variable `(Re z_1, Im z_1, A)` Stabilization & Runaway Controls (`Part 2C`, `E3 = True`):**
   - Full $3 \times 3$ Newton optimization of $\mathcal{S}_{\mathrm{eff}}(\operatorname{Re} z_1, \operatorname{Im} z_1, A)$ (`combining -Vol(z), truncated hyperbolic cusp cost +A/2, quantized I = 3 flux repulsion +18 pi^2 / A, and one-loop Casimir density`) converges from distinct initial seeds within `< (1/1000)^6` to a positive-definite local minimum at $z_1^* = \frac{1}{2} + i\frac{\sqrt{3}}{2}$ and horospherical area $A^*$ near `18848/1000` (`gradient norm < (1/1000)^6`, $3 \times 3$ Hessian eigenvalues near `+53/1000`, `+1727/1000`, `+1737/1000`).
   - Because $\mathcal{V}_{\mathrm{Cas}}(\tau^*, (4/15, 8/15)) < 0$, $A^*$ is separated from ultra-short-distance Casimir attraction ($A \to 0$) by an ultraviolet barrier at $A_{\mathrm{UV}}$ near `305/100000` of height $\Delta\mathcal{S} > 29000$. Removing magnetic flux (`I = 0`) collapses $A \to 0$ (`PC_ENDGAME2_ZeroFluxCollapse`), while removing bulk hyperbolic curvature (`c_vol = 0`) drives decompactification $A \to \infty$ (`PC_ENDGAME2_ZeroVolumeCutoffRunaway`).

---

## 2. Hand-Off to Stage 3 (`X-ENDGAME-3`)

With continuous cusp geometry $(\tau^*, A^*)$ dynamically selected by `m004` without embedded target coordinates, Stage `3` (`X-ENDGAME-3`) constructs the $\mathrm{SL}(2, \mathbb{Z})$-covariant Majorana seesaw operator on the unshifted singlet sector $q = 0$, enforces mandatory six-unitary $\mathrm{U}(3)^6$ Haar basis-scrambling invariance, compares `sec4` (`seesaw`) mixing against `sec1`–`sec2` mixing at $(\tau^*, (4/15, 8/15))$, and audits the amphichiral phase $\arg\det(Y_1 Y_2)$ on single eigenlines vs parity-completed `m004`.

`0 of 19.`
