# `Card AGY-C68` (`2026-11-27`) — Forward Remediation of Unpushed `AGY-C67`: Exact Cyclotomic Non-Commutative Two-Counts Weil Unfolding (`Mod-4` Mirror Dichotomy & All-`3^k` Chiral Index `+2`), Universal Outward Markoff Tree Jacobian Cubic, & Exact Resultant / Rational Ptolemy Proof of `P-775` Across Metallic Grounds (`0 of 19`)

- **Seat / Code / Branch / Base Commit:** `agy` (`fam3-v1-high-01`) / `origin/agy/cusp-action-2026-11-20` / `23b307560`
  (superseding unpushed local `AGY-C67` `e84fb2ab3..23b307560` forward without history rewrite per `M23` item `1`;
  remote `origin/agy/cusp-action-2026-11-20` stands at `76d9799df` [`AGY-C66`, harvest row `2041`]; frozen harvest branch
  `origin/agy/audit-2026-11-02` untouched at `4319f47e2`; sealed `AGY-C1..C67` files untouched)
- **Pre-Push Custody & Defect Disclosure (`AGY-C67` -> `AGY-C68`):** Pre-push hostile audit of unpushed `AGY-C67` verified
  all four theorems (`E1`–`E4`) in cold-room cyclotomic and symbolic arithmetic while catching three pre-push defects:
  (`D1`) blind-banking self-containment in the Claim Card required spelling out all `18` closed-form `E2` polynomials
  `P_q(x)` (`N in {3, 5, 7, 9, 15, 27}`), Heisenberg operators `(X_+, Z_r)` (`r = 1` in `hom_comm_ok`), right-to-left word
  composition `F_{c_1 ... c_n}`, geometric cycle selection, `D_{BW}(w)` (`avoiding symbol collision with Jacobian d(...)`),
  `Delta V_k`, and `u_{max} in (54, 55)`; (`D2`) `c67_countercheck.py` comments overstated cyclotomic ring / Chebyshev steps
  while running `48`-dps numerical checks; (`D3`) `E2` polynomials, Silver `V_2 = 4 * Catalan`, and the Bronze quartic are
  upgraded from rounded `mpmath` checks to **zero-float exact SymPy `DomainMatrix` cyclotomic proofs over `QQ(zeta_{lcm(N,3)})`,
  exact Silver anharmonic cross-ratio shapes `[1 + i, (1 + i)/2, i, (1 + i)/2]`, and exact symbolic `sp.resultant` over `ZZ[u]`**
  (both in `c68` producer and in `c68` countercheck via symmetric half-step `T_1^{-3} = T_2^3`).
- **Synced Premises:** `origin/main @ ae7defd04` (`M23`, `SEAT_CODES.json`, Review `88` `B2018`, `P-885`; mathematical
  premises strictly pre-trial `<= B2008`: `GENESIS`, `S02`, `B98`, `B371`, `B377`, `B381`, `B1876`, `B1881`, `B1983`,
  `B1985`, `B1993`, `B1994`, `B2000`, `B2001`, `B2004`, `B2008`, `P-374`, `P-630`, `P-775`, `P-882`, with zero dependency
  on trial cards `B2011..B2017`), `agy-exp @ f250ed349`, `agy-002 @ 765c453a7`, `chat1 @ 19bc14af9`
- **Strict Scope (`0 of 19`):** Exact integer, rational, cyclotomic/algebraic number-field, polynomial-resultant, and
  `45`-digit residual-certified listening on (`1`) the finite non-commutative two-counts Heisenberg–Weil register `C^N`
  (`odd N >= 3`), (`2`) the `3 x 3` Jacobian of `W_{6,tr}` across the positive Markoff tree (`B2000` Open `#2`), and (`3`)
  the birational blow-up `(u, v) = (x / z, y / z)` of `S_{kappa = -2}` across metallic grounds `L^m R^m` (`m in {1, 2, 3}`,
  `P-775`). Zero empirical constants, zero added parameters, zero post-hoc residue selection; order-`30` line held per `M18`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`PF1`–`PF5`)

1. **`E1` (`Non-Commutative Two-Counts Weil Unfolding, Mod-4 Mirror Dichotomy, & All-3^k Chiral Index +2` — `B2008` Open `#1` & `P-374`):**
   - **Expectation `E1a` (`Stereo Commutation & Z_3 Equivariance`):** On `C^N` (`odd N >= 3`, `inv2 = (N + 1) / 2`,
     `zeta_N = exp(2 pi i / N)`), shift `(X_+ psi)_j = psi_{(j + 1) mod N}` and clock `(Z_r psi)_j = zeta_N^{r j} psi_j`
     (`r in (Z/NZ)^x`) satisfy `X_+ Z_r = zeta_N^r Z_r X_+`. With `G_{N,r} = sum_{b=0}^{N-1} zeta_N^{-r * inv2 * b^2}`,
     `rho_{N,r}(L) = diag(zeta_N^{r * inv2 * j^2})`, `(rho_{N,r}(S_{inv}))_{a,c} = G_{N,r}^{-1} zeta_N^{r a c}` representing
     `S^-1 = [[0, 1], [-1, 0]]`, `rho_{N,r}(R) = rho_{N,r}(S_{inv}) rho_{N,r}(L)^dagger rho_{N,r}(S_{inv})^dagger`,
     `rho_{N,r}(C_omega) = rho_{N,r}(L) rho_{N,r}(R)^dagger`, and order-`3` `rho_{N,r}(C_{3,omega}) = rho_{N,r}(S_{inv})^2
     rho_{N,r}(C_omega)`, the stereo walks `W_hat_+ = sum_{j=0}^2 C_omega^j L C_omega^{-j}` and `W_hat_- = sum_{j=0}^2
     C_omega^j R C_omega^{-j} = W_hat_+^dagger` satisfy `[W_hat_+, W_hat_-] = 0` and `[W_hat_6, rho_{N,r}(C_{3,omega})] = 0`
     (`exact in QQ(zeta_{lcm(N,3)}) for N in {3, 5, 7, 9, 15, 27}` and `<= 10^{-30}` across `p in {3..23}`).
   - **Expectation `E1b` (`Mod-4 Mirror Dichotomy` + `PF1`, `PF2`):** `conj(rho_{N,r}(g)) = rho_{N,-r}(g)` intertwines
     `H_1(rho_{N,r}) ~= H_2(rho_{N,-r})` and `(U_u psi)_j = psi_{u j mod N}` intertwines `rho_{N,r} ~= rho_{N, u^2 r}`.
     Across `p in {3, 5, 7, 11, 13, 17, 19, 23}` at fixed symplectic orientation `r = 1` (`S02`): `W_hat_6|_{H_1} ~=
     W_hat_6|_{H_2}` iff `p == 1 mod 4` (`p in {5, 13, 17}`), while every `p == 3 mod 4` (`p in {3, 7, 11, 19, 23}`)
     **natively splits `2 -> 1 + 1`** (`killed by commuting collapse r = 0 in PF1; inverted by r = -1 in PF2`).
   - **Expectation `E1c` (`All-3^k Chiral Index +2`):** `tr rho_{3^k,1}(C_{3,omega}) = +i sqrt(3)` (`exact in QQ(zeta_{3^k})`
     for `k <= 3` and certified across `k = 1..5`), locking `(d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1, 3^{k-1} - 1)` and
     **`d_1 - d_2 = +2`** for all `k >= 1`.

2. **`E2` (`Exact Zero-Error Cyclotomic Characteristic Polynomials P_q(x) at N in {3, 5, 7, 9, 15, 27}`):**
   - **Expectation `E2`:** Exact `DomainMatrix` equality `(P_q * W_hat_6).charpoly() == x^{N - d_q} P_q(x)` over
     `QQ(zeta_{lcm(N,3)})` holds with zero remainder for all `18` polynomials:
     - `N = 3`: `P_0 = x`, `P_1 = x^2 - 9`, `P_2 = 1`;
     - `N = 5`: `P_0 = x + 2 sqrt(5)`, `P_1 = P_2 = (x - (3 - sqrt(5))/2)(x + (3 + 3 sqrt(5))/2)`;
     - `N = 7`: `P_0 = x^2 (x + 4)`, `P_1 = x^2 - 2 x + (-9 + sqrt(21))/2`, `P_2 = x^2 - 2 x + (-9 - sqrt(21))/2`;
     - `N = 9`: `P_0 = x (x - 4)(x - 6)`, `P_1 = (x^2 - x - 3)(x^2 - 3 x - 9)`, `P_2 = (x - 1)(x - 3)`;
     - `N = 15` (`dims (5, 6, 4)`): `P_0 = x^3 (x - sqrt(5) + 1)(x + sqrt(5) + 3)`, `P_1 = (x - (3 + sqrt(5))/2)(x - (3 - 3
       sqrt(5))/2)(x^2 - (21 - 3 sqrt(5))/2)(x^2 + (1 - sqrt(5)) x - (3 + 3 sqrt(5))/2)`, `P_2 = (x + sqrt(5))(x - (1 -
       sqrt(5))/2)(x^2 - ((3 + 3 sqrt(5))/2) x - (3 - 3 sqrt(5))/2)`;
     - `N = 27` (`dims (9, 10, 8)`): `P_0 = x^5 (x^4 - 24 x^2 - 16 x + 48)`, `P_1 = x^2 (x^8 - 30 x^6 - 10 x^5 + 300 x^4 +
       126 x^3 - 1179 x^2 - 324 x + 1620)`, `P_2 = x^8 - 27 x^6 + 14 x^5 + 174 x^4 - 180 x^3 - 171 x^2 + 270 x - 81`.

3. **`E3` (`Universal Outward Markoff Tree Jacobian Cubic & AM–GM Theorem` — Closing `B2000` Open `#2`):**
   - **Expectation `E3` + `PF3`:** `D^{-1}(J_{W_6}(x, y, z) - 2 I_3) D` (`D = diag(sqrt(x), sqrt(y), sqrt(z))`) has `3`-square
     `SOS` form and exact charpoly `(t - 2)(t - 2 - (x + y + z))^2 - 4 x y z` with peak `(4 / 27)((x + y + z)^3 - 27 x y z)`,
     making `(3, 3, 3)` the unique degenerate positive Markoff triple (`(14, 5, 5)`), splitting at `(3, 3, 6)` to `(t - 8)(t^2 -
     22 t + 76)` (`PF3`) and `(3, 6, 15)` to `(t - 32)(t^2 - 22 t + 76)`, with `3` simple roots `> 2` across all `64` non-root
     sorted triples to depth `7` and fixed-`x` ray limits `lambda_1 / lambda_2 -> 1`, `lambda_3 -> (6 x + 4)/(x + 2)`.

4. **`E4` (`Rational Blow-Up, Exact Anharmonic Silver 4 * Catalan, & Exact Resultant Bronze Quartic for P-775`):**
   - **Expectation `E4` + `PF4`, `PF5`:** `(u, v) = (x / z, y / z)` blows up `(0, 0, 0)` on `S_{kappa=-2}`, preserving
     Goldman–Poincaré `Omega = -du ^ dv / (u v)` with shapes `w_L = v^2 / (v^2 + 1)`, `w_R = 1 / (u^2 + 1)` and amphichirality
     `S^{-1}(L^m R^m) S = (L^m R^m)^{-1}`; proves Golden `t^2 - 5 t + 1 = 0` (`rate (5 + sqrt(21))/2`, `PF4`), Silver `t^2 -
     18 t + 1 = 0` (`rate 9 + 4 sqrt(5) = phi^6`) with exact symbolic `RRLL` shapes **`[1 + i, (1 + i)/2, i, (1 + i)/2] =
     [1 - 1/i, 1/(1 - i), i, 1/(1 - i)]`** proving **`V_2 = 4 * Catalan`** symbolically, and exact symbolic Groebner resultant
     **`(u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359)^2`** for Bronze `tr(d(F_L^3 o F_R^3))` (`PF5`, `u_{max} in (54, 55)`),
     with `< 10^{-7}` step-ratio settling across all three metallic grounds (`zero SnapPy`).

0 of 19.
