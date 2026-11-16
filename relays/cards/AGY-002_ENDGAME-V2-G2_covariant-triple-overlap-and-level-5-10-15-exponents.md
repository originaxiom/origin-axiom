# Card `AGY-002_ENDGAME-V2-G2` — Modular-Covariant Triple-Overlap Frame `D1`, Levels `5 / 10 / 15` Cusp Exponents, and Blind Level-`6` `M_H^2` Spectrum (`0 of 19`)

## 1. Package and Question

Addressing `P-861` (`SM-C18`) and `B1948` Step `2` under strict `0 of 19` isolation:
1. Respecting Stokes' theorem on `m004` vs `X_4`, does the closed-fibre Cremades–Ibáñez–Marchesano (`CIM`) triple overlap `Y_{ijk}(tau; zeta_L, zeta_R, zeta_H)` with flux conservation `I_L + I_R + I_H = (+3) + (+3) + (-6) = 0`, spin-structure conservation `(1/2, 1/2) + (1/2, 1/2) + (0, 0) == (0, 0) mod 1`, and hypercharge Wilson-line neutrality `3 zeta_L + 3 zeta_R - 6 zeta_H = 0` transform covariantly under **both** `T : tau -> tau + 1` and `S : tau -> -1/tau` to `< 1e-12` (`solving B1947's C2 covariance failure`)?
2. What are the exact `tau`-free cusp exponents `(e(m_2/m_3), e(m_1/m_3))` and lepton–down relations across exact-order torsion vacua at candidate levels `5`, `10`, and `15` (`B1948` Step `2`) in both Frame `C` and Frame `D1` (`CIM (3, 3, -6)`)?
3. Computed **blind to fermion masses**, does the `1`-loop scalar mass-squared matrix `M_H^2` on the `6`-dimensional level-`6` Higgs space `C^6` select a unique `0`-bit ground state, or leave a degeneracy whose discrete selection cost must be priced in bits (`Guardrail 1`)?

## 2. Deliverables and Definition of Done

1. **Explicit Wang / Stokes Flux Accounting (`m004` vs Closed Fibre / `X_4` Relative Defect):**
   - Prove from the integer Wang monodromy matrix `M - I_2 = [[1, 1], [1, 0]]` (`det = -1`) that `H_2(m004; Z) = 0` and `H^2(m004; Z) = 0`, and verify on an explicit simplicial/cellular complex that source-free `int_{partial bar{m004}} F / (2 pi) = 0`, whereas capping the cusp puncture (`or coupling to quantized relative defect classes in H^2(X_4, partial X_4; Z)`) admits `(I_L, I_R, I_H) = (+3, +3, -6)` iff `I_L + I_R + I_H = 0`, `spin sum in Z^2`, and `3 zeta_L + 3 zeta_R - 6 zeta_H = 0`.
2. **Modular Covariance Lock First (`T` and `S` to `< 1e-12`, Discharging `P-861` & `SM-C18`):**
   - Derive and cross-verify (`< 1e-13` agreement between `2D` torus quadrature on `E_tau` and the completed-square `1D` Riemann-theta identity) the `3 x 3 x 6` tensor `Y_{ijk}(tau; zeta_L, zeta_R, zeta_H)`.
   - **Before evaluating any singular values or mixings**, verify across all `3` SM hypercharge triples `up (1, -4, +3)`, `down (1, 2, -3)`, `lep (-3, 6, -3)` (`with zeta_L = q_L w, zeta_R = q_R w, zeta_H = (q_L + q_R) w / 2`) at `3` generic complex moduli `tau` and torsion points `w` that:
     - `Y(tau; zeta)` is doubly periodic on `E_tau` (`z -> z + 1` and `z -> z + tau` to `< 1e-12`), and
     - `Y` transforms covariantly under **both** `T : (tau, zeta) -> (tau + 1, zeta)` and `S : (tau, zeta) -> (-1/tau, zeta/tau)` via unitary Weil basis-transport matrices `(U_T^{(3)}, U_T^{(3)}, conj(U_T^{(6)}))` and `(U_S^{(3)}, U_S^{(3)}, conj(U_S^{(6)}))` to `< 1e-12`.
3. **Universal `tau`-Free Cusp Exponents Across Levels `5`, `10`, and `15` (`B1948` Step `2`):**
   - Across all exact-order torsion points at `N = 5` (`24` pts), `N = 10` (`72` pts), and `N = 15` (`192` pts), prove in exact `Fraction` arithmetic and verify against high-cusp extended-precision `mpmath` slopes (`within < 2e-3`):
     - **Level `5`:** Exact `1 : 1` lepton–down equality (`Frame C` minima: `S` `(1/5, 11/20)`, `St` `(1/5, 1/2)`).
     - **Level `10` (`SM-C13b`):** Pointwise lepton–down exponent swaps at `a = +-1/10 <-> +-3/10` (`via w' == -3 w mod 10`), **but exact `1 : 1` whole-orbit cusp-exponent equality** (`down = lep = (1/5, 1/2)` on both `S` and `St`, and exact multiset equality of `{Y^{(e)}(w)}` and `{Y^{(d)}(w')}` in `CIM (3, 3, -6)` via `w' == 9 w mod 20` to `< 1e-13`).
     - **Level `15` (`B1942`):** Exact colour-triality exponent split: `lep` collapses via `w -> 3w` onto level `5` (`(1/5, 11/20)` on `S`, `(1/5, 1/2)` on `St`), while `down` moves to `(2/15, 1/2)`, locking the `tau`-free rational ratio `e_lep(m_2/m_3) / e_down(m_2/m_3) = 3/2` (`and 11/10 for m_1/m_3 on S`).
4. **Blind `1`-Loop Level-`6` Scalar Mass Matrix `M_H^2` & Degeneracy Bit Ledger (`Guardrail 1`):**
   - Prove `(U_M^{(6)})^{12} = I_6` (`to < 1e-13`) with `6` simple eigenphases `{-5pi/6, -pi/3, -pi/6, +pi/6, +pi/3, +5pi/6}`.
   - Compute `M_H^2` **blind to fermion masses** across its three structural regimes and price ground-state degeneracy `log_2(d)` explicitly:
     - Pure `1`-loop chiral fermion bubble `Sigma_H` (`geodesic-integrated over [0, 4 ln phi]` and at Riley cusp `tau = 2 sqrt(3) i`): `d = 3` Heisenberg degeneracy (`log_2(3) = 1.58496...` bits);
     - Pure base-`S^1` Kaluza–Klein holonomy kinetic operator `K_KK = (theta_m / L_M)^2`: `d = 2` doublet `{v_{-pi/6}, v_{+pi/6}}` (`1` bit);
     - Combined `M_H^2 = K_KK - kappa_1 Sigma_H` (`given fixed chiral flux I_H = -6`): strictly simple `6`-eigenvalue spectrum (`d = 1`, `0` additional discrete bits beyond `sgn(I_H)`), uniquely selecting `v_{+pi/6}`, with `U(3)^6` Haar invariance `< 1e-12` on the resulting dimensionless Yukawa observables.

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Failure of `2D` quadrature vs `1D` theta identity (`>= 1e-13`), torus double periodicity (`>= 1e-12`), or `T` / `S` modular covariance (`>= 1e-12`).
- Any discrepancy between exact `Fraction` cusp exponents and high-cusp `mpmath` numerical slopes (`>= 2e-3`) across levels `5, 10, 15`.
- Assigning `0` bits to any `d > 1` degenerate eigenspace (`Guardrail 1`), or `U(3)^6` Haar drift `>= 1e-12`.
- Failure to catch any of the `5` planted fault controls below.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF2.1` (`Flux-Violating Untwisted Scalar I_H = 0`):** Setting `I_H = 0` (`3 + 3 + 0 != 0`) must break `z -> z + tau` periodicity on `E_tau` by `> 0.5`.
2. **`PF2.2` (`B1947 Naive Phase-Twisted Point Coupling`):** Multiplying by `exp(2 pi i q_H w)` without closed-fibre Gaussian/theta shift must fail `T : tau -> tau + 1` covariance by `> 0.1`.
3. **`PF2.3` (`Spin-Characteristic Violation`):** Setting `(alpha_H, beta_H) = (1/2, 0)` must break `z -> z + 1` periodicity on `E_tau` by `> 0.5`.
4. **`PF2.4` (`Corrupted Lepton Doublet Charge q_L = -2 at Level 15`):** Replacing `q_L = -3` with `-2` (`3 does not divide -2`) must break the level-`15`-to-level-`5` lepton collapse by `> 0.02`.
5. **`PF2.5` (`Degenerate Pure-Bubble Bit-Pricing Control`):** Turning off `K_KK` must return ground-state degeneracy `d = 3` (`log_2(3) > 1.58` bits, catching any `0`-bit mispricing).

## 5. Dependencies and Firewall Boundaries

Rests on `P-861`, `B1942`, `B1945`, `B1948`, and `Cremades-Ibanez-Marchesano (2004)`. Strict `0 of 19` firewall; touches only files under `relays`. Expectations committed first (`0 of 19`).
