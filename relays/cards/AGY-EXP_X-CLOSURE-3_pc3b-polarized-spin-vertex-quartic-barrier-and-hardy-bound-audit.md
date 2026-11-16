# Card `X-CLOSURE-3` — First Standalone Verification of `physical` `P-C3b` Proofs `4–5` (`d7d0bc320`: Polarized $Q_{\mathrm{em}}$ Spin Vertex, Wilson-Crossing Rank, Smooth Bulk Quartic Barrier $V(s) = B s^2(1-s)^2$, and $1/(8\ell^2)$ Gauge Hardy Bound, `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Third sealed stage of Campaign `X-CLOSURE` (`four stages, sixteen blind-sealed commits, 0 of 19`), delivering the first independent zero-import computational verification of `physical`'s two same-action continuation proofs (`d7d0bc320` on `e250dab15`), explicitly retaining the scope distinction between restricted affine-path energetics and full transverse `PDE` stationarity.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_closure_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `3A` (`Proof 4` — `ACTUAL_SPIN_VERTEX_CURRENT_AND_WILSON_CROSSING`):**
   - Do the opposite-charge colour-singlet spin zero lines (`with \delta_- = -\delta_+`) have a nonzero cubic superpotential coupling $\kappa(Q, [u_+, v_-] + [u_-, v_+]) = -q k \delta_+ s_+ s_-$ with the neutral $Q_{\mathrm{em}}$ mode $a_0 = \bar{\omega} Q$ that agrees identically with the trace-dual mass-operator variation $\delta M$?
   - Upon canonical normalization of $(a, t_+, t_-)$ and the $Q_{\mathrm{em}}$ vector current, do $(G, k, h_Q, q, c_+)$ cancel identically to yield $|y|^2 / e_Q^2 = 2 A_\omega A_g / I_\omega^2 > 2$ on a hyperbolic punctured-torus collar, with `full-E` scalar transport $(\bar{d}_e / |d_e|)(j_e / |j_e|)^2 = 1$, while a small nontrivial $Q$-Wilson twist lifts the spin pair (`rank 1`) and leaves the `2` form zero modes per charge intact?
2. **Question `3B` (`Proof 5` — `FINITE_BULK_CONNECTIONS_QUARTIC_AND_REAL_GAUSS`):**
   - Along an affine smooth-bundle interpolation $X_s = (A_0 + s a,\, q_0 + s u,\, r_0 + s v)$ ($0 \le s \le 1$) between two zero-residual parallel state backgrounds sharing a common tail connection, does the full nonlinear parent potential restrict identically to the exact quartic $V(X_s) = B\, s^2(1 - s)^2$ (`with B >= 0 given by eq. 3, and \mu_2 / \Omega^2 = 2(1 - \cos\theta) M_0 on an SU(2)-rotated tail`)?
   - Does the real longitudinal Gauss equation $L_s \alpha_s = b_s$ satisfy $\langle \epsilon, b_s\rangle = 0$ for $\epsilon \in \ker L_s$, yield $0 \le K(s) = K_0 - \langle b_s, L_s^+ b_s\rangle_v \le K_0$, and obey the sharp cusp-tail gauge Hardy lower bound $\langle \alpha, L_s \alpha\rangle \ge \|\alpha\|_v^2 / (8\ell^2)$ (`while spin-fermion density \Omega has zero Hardy threshold`)?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A`:** `60`-digit + exact `SymPy` verification of `eqs. (1)–(9)` of `ACTUAL_SPIN_VERTEX_CURRENT_AND_WILSON_CROSSING` (`polarized cubic bracket vs \delta M, exact G/k/h_Q cancellation in 2 A_\omega A_g / I_\omega^2 > 2, Wilson-crossing rank, and full-E phase cancellation`).
2. **`Part 3B`:** `60`-digit matrix + quadrature verification of `eqs. (1)–(9)` of `FINITE_BULK_CONNECTIONS_QUARTIC_AND_REAL_GAUSS` (`exact V(X_s) = B s^2(1-s)^2 across 9 rational nodes s in [0, 1], SU(2) tail identity, real Gauss projection K(s), and sharp 1/(8\ell^2) cusp Hardy bound`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_PolarizedSpinVertex_and_WilsonCrossing_Gate` (`Part 3A`):** Cubic superpotential minus $\delta M$ bilinear vanishes (`< (1/1000)^18`); symbolic cancellation in $|y|^2 / e_Q^2 - 2 A_\omega A_g / I_\omega^2$ is exact `0`; hyperbolic collar quadrature satisfies $2 A_\omega A_g / I_\omega^2 > 2 + 1/10$; odd and aligned seeds give identical $|y|/e_Q$; nearby $Q$-Wilson twist leaves `(0 spin, 2 form)` zero modes per charge; and `full-E` phase product equals `1` to `< (1/1000)^18`.
2. **`E2_AffineQuarticBarrier_and_RealGaussHardy_Gate` (`Part 3B`):** $\max_{s} |V_{\mathrm{parent}}(X_s) - B\, s^2(1 - s)^2| < (1/1000)^18$ with $B > 0$; $\mathrm{SU}(2)$ tail moment identity holds to `< (1/1000)^18`; real Gauss orthogonality $\langle \epsilon, b_s\rangle = 0$ (`< (1/1000)^18`) and $0 < K(s) < K_0$; and cusp gauge Hardy quotient $\langle \alpha, L_s \alpha\rangle / \|\alpha\|_v^2 \ge 1/(8\ell^2)$ across all compactly supported test profiles (`approaching 1/(8\ell^2) from above`).

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage3_Closure_Passed`:** `AST` check confirming zero disallowed imports, `0` float literals, and `0` complex literals module-wide.
2. **`PC_CL3_SameSignPolarizationAndSingleTermControls`:** Setting $\delta_- = +\delta_+$ (`or same-sign charge`) annihilates the polarized cubic vertex (`= 0`), and keeping only one polarization term halves $|Y_{\mathrm{raw}}|$ (`shifting |y|^2/e_Q^2 by factor 1/4`).
3. **`PC_CL3_NonVacuumEndpointBreaksQuartic`:** Perturbing $X_1$ off the zero-residual locus breaks $V(X_s) = B\, s^2(1 - s)^2$ (`deviation > 1/10`).
4. **`PC_CL3_MisappliedHardyToSpinFermionZeroInfimum`:** Evaluating the radial kinetic quotient against spin-fermion density $\Omega$ (`e^0 dt` instead of vector density $\Omega^2 \leftrightarrow e^{-t} dt$) drives the infimum below $1/(100\ell^2) \ll 1/(8\ell^2)$ on wide cusp-collar test functions, confirming the $1/(8\ell^2)$ Hardy gap belongs strictly to the vector gauge operator $L_s$.

`0 of 19.`
