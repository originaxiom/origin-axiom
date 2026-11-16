# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-SYNTHESIS-1` Results (`PHYSICAL-C5 Hyperbolic Liouville Uniformization Metric, Analytic Cusp-Area Tail Closure, & Joint Multi-Grid (\lambda_+, \lambda_-) and \sigma_*^{\mathrm{hyp}} > 0, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 1–4` of `16`):**
  1. Card first ([AGY-EXP_X-SYNTHESIS-1_hyperbolic-liouville-metric-cusp-tail-and-multigrid-lambdas-sigma-star.md](cards/AGY-EXP_X-SYNTHESIS-1_hyperbolic-liouville-metric-cusp-tail-and-multigrid-lambdas-sigma-star.md))
  2. Standalone verifier + `SHA256`: `001540efe` ([verify_x_synthesis_1.py](x_synthesis_1_verify/verify_x_synthesis_1.py), [SCRIPT_SHA256.txt](x_synthesis_1_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `8d3ce172c` ([verify_x_synthesis_1_out.json](x_synthesis_1_verify/verify_x_synthesis_1_out.json), [OUTPUT_SHA256.txt](x_synthesis_1_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage1_Synthesis_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_1_gate_passed = True`** (`all_planted_controls_passed = True`).
- Directly resolves `physical` `PHYSICAL-C5` (`407583a8c`, `C5-02` & `C5-04`) on $E_{\tau = i\sqrt{3}} \setminus \{0\}$ (`keeping the 3D-to-2D marked-curve / parent-frame map explicitly scoped in Tier II`): solves the constant-curvature hyperbolic Liouville uniformization equation $\Delta \ln \Omega_{\mathrm{hyp}} = \Omega_{\mathrm{hyp}}^2 / \ell^2$ (`\ell = 3/2`), adds `physical`'s exact analytic cusp-area tail $\delta A(T)$ to match Gauss–Bonnet area $2\pi\ell^2 = \frac{9\pi}{2}$ to `< 6/10000`, replaces the sharp disk indicator with a smooth $C^\infty$ radial partition of unity, verifies `eq. (7)` metric-variation sensitivity, and refines **both** the harmonic Gram quadratures and Bloch–Fourier Green inverses across `(16, 24, 32)` with an enforced good-sign $|\bar{\partial}(K_*\alpha)| < (1/1000)^2 * (1/100)$ gate predicate.

---

## 2. Gate-by-Gate Audit Summary (`Mask-Clean`)

1. **`Part 1A` — Hyperbolic Liouville PDE & Gauss–Bonnet Area Tail (`E1_HyperbolicLiouville_and_GaussBonnetTail_Gate_passed = True`):**
   - Spectral Newton–Fourier with Robin matching $w(0) = 0$ solves the hyperbolic Liouville equation across $M_{\mathrm{hyp}} \in \{16, 24, 32\}$ to `< (1/1000)^4` (`interior curvature relative error < 2/100000` vs `> 4/5` on the uncorrected seed `PC_SY1_NonHyperbolicSeedCurvatureError`, converging $b_c^* \in (655/1000, 656/1000)$).
   - Truncating polar quadrature at $T = 18$ without the cusp tail misses Gauss–Bonnet area $2\pi\ell^2$ by `> 5/100` (`PC_SY1_OmittedCuspAreaTailMissesGaussBonnet`), whereas adding `physical`'s analytic cusp-area tail $\delta A(18) = \frac{2\pi\ell^2}{18 + \ln 4 + b_c^*}$ closes Gauss–Bonnet to `< 6/10000`.
2. **`Part 1B` — Hyperbolic $(\lambda_+, \lambda_-)$ & Sensitivity `eq. (7)` (`E2_HyperbolicLightCubic_and_MetricSensitivity_Gate_passed = True`):**
   - Smooth radial partition + analytic area tail across `n_gl in {16, 24, 32}` (`24 vs 32 relative shift < 3/10000`) gives $|\lambda_+| / e_Q \in (1810/1000, 1811/1000)$, $|\lambda_-| / e_Q \in (1558/1000, 1559/1000)$, and $|\lambda_+| / |\lambda_-| \in (1161/1000, 1162/1000)$; `eq. (7)` gives `< (1/1000)^4` constant-rescaling invariance and matches central differencing on a non-constant smooth deformation to `< 3 * (1/1000)^3 * (1/10)`.
3. **`Part 1C` — Joint Multi-Grid $\sigma_*^{\mathrm{hyp}} > 0$ & Enforced $\bar{\partial}$ Gate (`E3_RefinedTripletSigmaStar_and_DbarPredicate_Gate_passed = True`):**
   - Symbolic homotopy verifies exactness of $0 \to \bar{A}(p) \to \bar{B} \oplus \bar{C} \to \bar{D}(-p) \to 0$ (`supplying the analytical rank-1 proof alongside numerics`), joint `(16, 24, 32)` Gram+Fourier refinement converges $\sigma_*^{\mathrm{hyp}} \in (4041/10000, 4043/10000)$ at $\ell = 3/2$ (`\sqrt{2}\,\sigma_*^{\mathrm{hyp}} \in (5716/10000, 5717/10000)`, `24 vs 32 shift < 2/10000`), full $L^2(\Omega_{\mathrm{hyp}}^{-3})$ inner-product projection agrees with analytic residue factorization to `< (1/1000)^4`, and enforced good-sign $|\bar{\partial}(K_*\alpha)| < (1/1000)^3$ passes (`vs swapped-sign error > 8`).

`0 of 19.`
