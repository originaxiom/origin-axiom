# Card `X-SYNTHESIS-1` — Hyperbolic Liouville Uniformization Metric on $E_{\tau = i\sqrt{3}} \setminus \{0\}$, Analytic Cusp-Area Tail Enclosure, and Multi-Grid Refinement of $(\lambda_+, \lambda_-)$ & $\sigma_* > 0$ (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-17`
- **Context:** First sealed stage of Campaign `X-SYNTHESIS` (`four stages, sixteen blind-sealed commits, 0 of 19`), addressing `physical` `PHYSICAL-C5` (`407583a8c`, `C5-02` & `C5-04`) by solving the nonlinear elliptic hyperbolic uniformization equation $\Delta \ln \Omega_{\mathrm{hyp}} = \Omega_{\mathrm{hyp}}^2 / \ell^2$ on $E_{\tau = i\sqrt{3}} \setminus \{0\}$, incorporating the exact analytic cusp-area tail $\delta A(T)$ to match Gauss–Bonnet area $2\pi\ell^2$, verifying the metric-sensitivity identity (`eq. 7`), and refining **both** the physical harmonic Gram matrices (`n_gl in {16, 24, 32}`) and Bloch–Fourier Green inverses ($M \in \{16, 24, 32\}$) with a smooth radial partition of unity and an enforced good-sign $\bar{\partial}(K_*\alpha)$ gate predicate.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_synthesis_1_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `1A` (`Hyperbolic Liouville Uniformization PDE & Gauss–Bonnet Cusp-Tail Closure`):**
   - Replacing the non-smooth $|{\ln R}|$ cusp comparator by the real-analytic cusp seed $\Omega_{\mathrm{seed}}(z; b_c) = \frac{\ell}{R(z)\big(b_c + \frac{1}{2}\ln(e^2 + R(z)^{-2})\big)}$ times $e^{w(z)}$, does spectral Newton–Raphson on $E_{\tau = i\sqrt{3}}$ ($M_{\mathrm{hyp}} \in \{16, 24, 32\}$) solve $-\Delta w + \frac{1}{\ell^2}\Omega_{\mathrm{seed}}^2(e^{2w}-1) = \Delta \ln \Omega_{\mathrm{seed}} - \frac{1}{\ell^2}\Omega_{\mathrm{seed}}^2$ to `< (1/1000)^4`, converge the Robin constant $b_c^*$, and match Gauss–Bonnet area $\int_{E_\tau} \Omega_{\mathrm{hyp}}^2\,d^2z = 2\pi\ell^2$ to `< 5/1000` once `physical`'s exact analytic cusp-area tail $\delta A(T) = \frac{2\pi\ell^2}{T + \ln(1/r_0) + b_c^*}$ is added (`whereas omitting \delta A(T) misses 2\pi\ell^2 by > 4/100`)?
2. **Question `1B` (`True Hyperbolic (\lambda_+, \lambda_-) & Metric-Variation Identity eq. (7)`):**
   - Using a smooth $C^\infty$ radial partition of unity (`eliminating the sharp-disk indicator jump`) + analytic cusp tail across quadrature grids `n_gl in {16, 24, 32}`, what are the hyperbolic uniformization values of $|\lambda_+|/e_Q$, $|\lambda_-|/e_Q$, and $|\lambda_+|/|\lambda_-|$ (`converging across n_gl = 24 vs 32 to < 2/1000`), and does `physical`'s metric-sensitivity derivative (`METRIC_TAIL_AND_NORMALIZATION.md` `eq. (7)`) vanish identically under constant rescaling while matching central differencing to `< (1/1000)^3` on a non-constant smooth deformation?
3. **Question `1C` (`Multi-Grid Gram + Fourier Refinement of \sigma_*^{\mathrm{hyp}} > 0 & Enforced \bar{\partial} Gate`):**
   - Refining **both** the $\Omega_{\mathrm{hyp}}^{-3}$ harmonic Gram quadratures (`n_gl in {16, 24, 32}`) and Bloch–Fourier Dolbeault Green inverses ($M \in \{16, 24, 32\}$), does $\sigma_*^{\mathrm{hyp}}$ converge across `(24, 24)` vs `(32, 32)` to `< 2/1000`, agree between $L^2$-inner-product extraction and analytic residue factorization to `< (1/1000)^2`, and satisfy the enforced good-sign holomorphicity gate $|\bar{\partial}(K_*\alpha)| < (1/1000)^2 * (1/100)$ (`while symbolic connecting-map exactness proves rank = 1 analytically`)?

---

## 2. Pre-Registered Expectations and Mandatory Controls

1. **`E1_HyperbolicLiouville_and_GaussBonnetTail_Gate` (`Part 1A`):** Pointwise spectral PDE residual `< (1/1000)^4` across $M_{\mathrm{hyp}} \in \{16, 24, 32\}$, interior finite-difference curvature check $|K_{\mathrm{Gauss}}(z_{\mathrm{test}}) + 1/\ell^2| / (1/\ell^2) < 5/1000$, and tail-completed area $|A_{\mathrm{num}}(T) + \delta A(T) - 2\pi\ell^2| / (2\pi\ell^2) < 5/1000$.
2. **`E2_HyperbolicLightCubic_and_MetricSensitivity_Gate` (`Part 1B`):** Smooth-partition `n_gl = 24 vs 32` relative shift `< 2/1000` on $|\lambda_\pm|/e_Q$, $|\lambda_+| / |\lambda_-| > 1$, constant-rescaling sensitivity `= 0`, and non-constant `eq. (7)` sensitivity error `< (1/1000)^3`.
3. **`E3_RefinedTripletSigmaStar_and_DbarPredicate_Gate` (`Part 1C`):** Symbolic connecting-map `0 -> \bar{A}(p) -> \bar{B}+\bar{C} -> \bar{D}(-p) -> 0` exactness holds, `(24, 24)` vs `(32, 32)` Gram+Fourier relative shift `< 2/1000`, $L^2$-extraction vs analytic residue relative error `< (1/1000)^2`, and enforced good-sign $|\bar{\partial}(K_*\alpha)| < (1/1000)^2 * (1/100)$.
4. **Mandatory Rejecting Controls:** `Gate_AST_Stage1_Synthesis_Passed` (`0` float literals, `0` complex literals module-wide), `PC_SY1_OmittedCuspAreaTailMissesGaussBonnet` (`relative area error > 4/100` without $\delta A(T)$), `PC_SY1_NonHyperbolicSeedCurvatureError` (`seed curvature error > 1/5` before Liouville solve), and `PC_SY1_SwappedKoszulSignBreaksHolomorphicity` (`> 1/10`).

`0 of 19.`
