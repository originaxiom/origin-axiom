# Card `AGY-002_FOUND-G10` — `Seifert` Spin-Bordism, `Bär` Essential-Spectrum Gap, `Rayleigh-Ritz` Refutation of Horn `Dirichlet` Bounds, and Cohomological `Branch B` Collar Minimum (`0 of 19`)

## 1. Package and Question

Resolving the hyperbolic cusp spectral foundation and target-free `Branch B` collar stabilization on `X_4 = m004 x~ [-L_4, L_4]` (`and auditing X-APEX-3's lambda_1 > 20 > 3 horn-box claim for P-865(b)`) on `origin/main` (`ff8e1ca57`) under strict `0 of 19` firewall, `Guardrails 1-6`, and `100%` mask-safe rational prose:
1. Does the exact `SL(2, Z[zeta_6])` `Culler` (`1986`) spin-lift of `pi_1(m004) = <x, y | w x = y w>` (`w = x y^{-1} x^{-1} y`) force `tr(rho_tilde(lambda)) = -2` along the canonical `Seifert`-surface boundary longitude `lambda = y x^{-1} y^{-1} x^2 y^{-1} x^{-1} y` for **both** spin structures on `m004`, excluding the periodic `(0, 0)` torus spin structure and proving `sigma_{ess}(D_{m004}^2) = empty` by `Bär` (`2000`)?
2. On the hyperbolic cusp horn `[0, oo)_y x T^2`, does imposing `Dirichlet` walls `phi(0) = phi(L_y) = 0` on `H_- = -d^2/dy^2 + mu^2 exp(2 y) - mu exp(y) = A^dag A` (`A = +d/dy + mu exp(y)`) give a `Rayleigh-Ritz` **upper** bound `lambda_1 <= lambda_1^{Dir}` rather than a lower bound, while opening `y = 0` (`D_0 subset D_{open}`) restores the exact normalizable cusp-to-bulk zero mode `psi_0(y) = exp(-mu (exp(y) - 1)) in L^2([0, oo))` (`lambda_1(D_{open}) = 0`)?
3. Using `m004`'s exact `Fox`-calculus `Betti` numbers `(b_0, b_1) = (1, 1)` (`with Alexander polynomial Delta_{4_1}(t) = t^2 - 3 t + 1` of discriminant `5`) for untwisted `3D` bosonic zero modes `N_{B,0}^{real} in {4, 27, 47, 68}` and `Gate 9`'s kink-gapped bulk spinors `M_0 in {1, 3}`, does `C_{IR} = -N_{B,0}^{real} < 0 < +189/2 = C_{UV}` produce a unique target-free global minimum `dV_{Cas}/dL_4(L_4^*) = 0` (`V(L_4^*) < 0, d^2V/dL_4^2(L_4^*) > 0`) across all `8` pairs?

## 2. Deliverables and Definition of Done

1. **Exact `SL(2, Z[zeta_6])` `Culler` Spin-Lift & `Bär` (`2000`) Cusp-Continuum Obstruction (`Guardrails 2 & 3`):**
   - Construct in exact `SymPy` over `Q(sqrt(-3))` (`zeta_6 = 1/2 + i sqrt(3)/2`) both `SL(2, C)` lifts `rho_tilde_+-` of `pi_1(m004)`; verify `rho_tilde_+-(w) rho_tilde_+-(x) - rho_tilde_+-(y) rho_tilde_+-(w) == 0`, `[rho_tilde_+-(x), rho_tilde_+-(lambda)] == 0`, exact peripheral trace pairs `(+2, -2)` and `(-2, -2)` (`with rho_tilde_+-(lambda) = [[-1, 2 sqrt(3) i], [0, -1]]` recovering `tau_{cusp} = 2 sqrt(3) i`), `mu_{min}^2(sigma_+) = pi^2 / 12 > 0`, `mu_{min}^2(sigma_-) = 13 pi^2 / 12 > 0`, and `10`-trial `SL(2, C)` conjugation invariance `< (1/10)^13`.
2. **`Rayleigh-Ritz` Domain-Monotonicity Theorem & Normalizable Horn Zero Mode (`Symbolic + 96-Node Clenshaw-Curtis Spectral Solver`):**
   - Prove symbolically in `SymPy` `(-d/dy + mu exp(y))(+d/dy + mu exp(y)) f(y) == (-d^2/dy^2 + mu^2 exp(2 y) - mu exp(y)) f(y)` and `A psi_0 == 0, H_- psi_0 == 0` for `psi_0(y) = exp(-mu (exp(y) - 1))`; verify on `[0, 6]` at `Adams` `mu = pi / (2 sqrt(3))` with strictly positive `Clenshaw-Curtis` weights `w_y > 0` that `lambda_1^{Dir}(D_0) > 5` whereas `lambda_1(D_{open}) < (1/10)^22` and `||A psi_0||_{L^2} / ||psi_0||_{L^2} < (1/10)^12` (`proving 3D bulk spinor gapping requires global 4D kink/collar mass or global core matching, never a local horn Dirichlet box`).
3. **`Fox`-Calculus Cohomology `(b_0, b_1) = (1, 1)` & `45`-Digit Analytical-`K_3` `Branch B` Collar Minimum (`Guardrails 1 & 5`):**
   - Derive `Delta_{4_1}(t) = t^2 - 3 t + 1` (`discriminant 5`) and `b_1(m004) = 1, b_0(m004) = 1` directly from `Fox` free derivatives of `w x w^{-1} y^{-1}`; verify `C_{UV} = +189/2` and solve `dV_{Cas}/dL_4(L_4^*) = 0` via exact `-K_3` derivative in `45`-digit `mpmath` across all `8` pairs `(M_0, N_{B,0}^{real}) in {1, 3} x {4, 27, 47, 68}`, confirming `|dV/dL_4(L_4^*)| < (1/10)^30`, `V(L_4^*) < 0`, `d^2V/dL_4^2(L_4^*) > 0`, `3/5 < L_4^* < 17/10`, `9/10 < ln(4 L_4^*) < 2`, and `13 / 13` prior `Gate 8-9` `SHA-256` manifests matched (`while explicitly keeping curved-m004 counterterm renormalization scoped`).

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PF10.1` (`Forbidden Trivial (0, 0) Torus Spin Structure`):** Setting `epsilon(lambda) = +1` gives `mu_{min}^2((0, 0)) = 0` (`opening continuous essential spectrum [0, oo)` and contradicting `tr rho_tilde_+-(lambda) = -2`).
2. **`PF10.2` (`Non-Peripheral Commutator Word`):** Replacing `lambda` by `[x^{-1}, y][x, y^{-1}]` fails `[rho_tilde_+(x), M_{fake}] = 0` by `> 3`.
3. **`PF10.3` (`X-APEX-3 Dirichlet-Wall Lower-Bound Fallacy`):** Clamping `phi(0) = 0` gives `lambda_1^{Dir} > 5` while opening `y = 0` gives `lambda_1(D_{open}) < (1/10)^22` (`gap > 5`).
4. **`PF10.4` (`Wrong-Chirality Growing Horn Operator A^dag`):** Replacing `A = +d/dy + mu exp(y)` by `A^dag = -d/dy + mu exp(y)` on `D_{open}` destroys the normalizable zero mode (`lambda_1(A^dag|_{D_{open}}) > 5 > 3`).
5. **`PF10.5` (`Un-Gapped Branch-A Runaway & Hand-Embedded Target Term`):** Leaving bulk spinors massless (`C_{IR} = +28 > 0`) makes `dV/dL_4 < 0` on `L_4 in [1/4, 4]`, while injecting `(L_4 - 2)^2` violates `Guardrail 1` (`dV/dL_4(3) > 1`).

## 4. Dependencies and Firewall Boundaries

Builds on `Gates 8-9` (`29dfeda86`, `5e0b7f65a`) on `origin/main` (`ff8e1ca57`) and discharges the `X-APEX-3` spectral audit for `P-865(b)`. Strict `0 of 19` firewall; touches only `relays/` (`0` repo imports, `0` float/complex literals). Expectations committed first (`0 of 19`).
