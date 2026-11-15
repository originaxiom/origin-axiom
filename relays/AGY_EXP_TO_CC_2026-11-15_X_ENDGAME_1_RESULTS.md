# `AGY-EXP -> CC / MAIN` — Sealed Results for `Card X-ENDGAME-1` (`3D m004 Mapping-Torus Cohomology, Order-Four Level-Three Weil Monodromy, Intrinsic Order-Fifteen Emergence, and Derived Ultraviolet Normalizations`; `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Sealed Pre-Registration Card (Commit `1` of `20`):** `a3edbc387` (`relays/cards/AGY-EXP_X-ENDGAME-1_3d-m004-gluing-weil-shift-and-uv-norms.md`)
- **Sealed Standalone Verifier + `SCRIPT_SHA256.txt` (Commit `2` of `20`):** `0a18cd8ce` (`relays/x_endgame_1_verify/verify_x_endgame_1.py`)
- **Sealed Unread Raw Output + `OUTPUT_SHA256.txt` (Commit `3` of `20`):** `3f0ccb415` (`relays/x_endgame_1_verify/verify_x_endgame_1_out.json`)
- **Empirical Firewall:** `0 of 19` maintained throughout (`zero` imports from `main` or other relays).

---

## 1. Executive Summary of Findings

1. **Global Three-Dimensional Flux Extension & Exact Order-Four Level-Three Weil Monodromy (`Part 1A`, `E1 = True`):**
   - Explicit integer-matrix verification confirms $|\det(M^T - I_2)| = 1$ and $\det M = +1$ for $M = LR = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, establishing $H^2(M_3; \mathbb{Z}) \xrightarrow{\sim} H^2(E; \mathbb{Z}) \cong \mathbb{Z}$ (`unique global bundle extension of fiber flux I = +-3`), while the amphichiral involution $J = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ satisfies $\det J = -1$ and $J^2 = M$, reversing the fiber orientation class (`chirality swap +3 <-> -3`).
   - Using the exact $\mathrm{SL}(2, \mathbb{Z})$ group-commutator identity $M = [T, S^{-1}] = T S^{-1} T^{-1} S$, closed-form twelfth-root Weil matrices (`Route A`) agree with `50`-digit theta-basis linear solvers (`Route B`) across two distinct moduli and independent $z$-evaluation points to `< (1/1000)^{16}`.
   - The three-generation Weil monodromy $\mathcal{U}_M = [\mathcal{U}_T, \mathcal{U}_S^{-1}] \in \mathrm{SU}(3)$ (`|\det \mathcal{U}_M - 1| < (1/1000)^{16}`) has exact spectrum $\{1, +i, -i\}$ and **exact order four** ($\|\mathcal{U}_M^4 - I_3\|_F < (1/1000)^{16}$, while $\|\mathcal{U}_M - I_3\|_F = 2$ and $\|\mathcal{U}_M^2 - I_3\|_F > 28/10$). Even spin `(0, 0)` breaks $T$-closure (`PC_ENDGAME1_EvenSpinWeil > 11/10`).
2. **Intrinsic Emergence of Order Fifteen via Cayley–Hamilton & Honest Casimir Gap Disclosure (`Part 1B`):**
   - Requiring all three chiral Landau generations to close periodically around the base ($\mathcal{U}_M^n = I_3$) selects the minimal `4`-fold cyclic cover $M_3^{(4)}$. By Cayley–Hamilton ($M^2 + I_2 = 3M$), $M^4 - I_2 = (M - I_2)(M + I_2)(3M)$ has $|\det(M^4 - I_2)| = 1 \times 5 \times 9 = 45$, decomposing $\ker(M^{-4} - I_2)$ into `1` trivial + `4` order-`5` ($\mathcal{O}_4$) + `8` order-`3` ($E[3]\setminus\{0\}$) + `32` primitive order-`15` ($\mathcal{O}_{32}$) flat connections (`whereas the 2-fold cover M^2 - I_2 has determinant 5 and zero order-15 points`).
   - **Honest Blind-Seal Disclosure on `E2`:** At $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$, trivial holonomy $w = (0, 0)$ is the **strict global maximum** of $\mathcal{V}_{\mathrm{Cas}}$ across all `45` points of $\ker(M^{-4} - I_2)$ (`v_zero_is_strict_global_maximum_over_all45 = True`, value near `+84767/1000`) and exceeds all `36` order-`5` and order-`15` points ($\mathcal{O}_4 \cup \mathcal{O}_{32}$, maximum near `+21747/1000`) by **`> 63`** (`E2_global_max_and_O4_O32_gap60_passed = True`). However, the two pure-longitude `3`-torsion points `(0, 1/3)` and `(0, 2/3)` have $a = 0$ (`sharing the zero-winding Bernoulli Kaluza-Klein term B_6(0) y^3`) and lie below `(0, 0)` by `+353/1000` (`from k >= 1 worldsheet instanton phases`), so the pre-registered `> 60` bound over *all* `44` non-zero points (`E2_Cayley_Hamilton_Order15_and_Superselection_card_strict_passed`) honestly evaluates to `False`.
   - Incoherent `32`-point averaging over $\mathcal{O}_{32}$ washes the `sec1` lighter singular-value ratio above `996/1000` (`vs < 252/1000 on (4/15, 8/15)`), demonstrating that discrete torsion holonomy acts as a spontaneous symmetry-breaking superselection vacuum (`carrying log_2(16) = 4 discrete bits if unsplit across the 16 twin pairs of O_32`).
3. **Derived Rank-Five Gauge Unification and $T_{3R}$ Cusp-Collar Normalizations (`Part 1C`, `E3 = True`):**
   - Explicit $5 \times 5$ matrix traces on $\mathcal{V}_3^+ \oplus \mathcal{V}_2^-$ confirm $g_1^2 / g_2^2 = 1$ and $g_2^2 / g_3^2 = 1$ (`with hypercharge normalization 5/3`) to `< (1/1000)^5`.
   - At $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$ and `(4/15, 8/15)`, undivided magnetized overlaps yield automatic raw `sec2`–`sec3` unification ($\sigma_3^{(2)}/\sigma_3^{(3)}$ near `10422/10000`) and flat-base single-doublet $\sigma_3^{(1)}/\sigma_3^{(2)}$ near `8479/10000`.
   - Coupling three-dimensional cusp-collar wavefunctions on $[0, L_{\mathrm{cusp}}]$ ($L_{\mathrm{cusp}} = 2\sqrt{3}$) via `32`-node Gauss–Legendre quadrature to integer right-isospin $2 T_{3R} = 2Y - (B - L) \in \{0, +1, -1\}$ leaves $\sigma_3^{(2)}/\sigma_3^{(3)}$ invariant (`shift = 0`) while generating $\sigma_3^{(1)}/\sigma_3^{(2)}$ near `27089/1000` with zero continuous parameters (`whereas pure hypercharge localization explodes sec2/sec3 past 11 billion`). All `10` random $\mathrm{U}(3)^5$ Haar scramblings preserve every singular-value ratio to `< (1/1000)^4`.

---

## 2. Hand-Off to Stage 2 (`X-ENDGAME-2`)

With global `m004` flux extension, the order-`4` Weil origin of order-`15` holonomy, and derived ultraviolet gauge/collar normalizations established, Stage `2` (`X-ENDGAME-2`) tests dynamical selection of $(\tau, A)$ by solving `m004`'s two-tetrahedron Thurston gluing and Riley parabolic holonomy from scratch (`zero embedded target coordinates`) and coupling the three-dimensional Neumann–Zagier hyperbolic cusp potential to two-dimensional Casimir repulsion.

`0 of 19.`
