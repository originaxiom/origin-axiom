# `Card AGY-C67` (`2026-11-27`) — Non-Commutative Two-Counts Weil Unfolding (`Mod-4` Mirror Dichotomy & All-`3^k` Chiral Index `+2`), Universal Outward Markoff Tree Jacobian Cubic, & Rational Ptolemy Proof of `P-775` Across Metallic Grounds (`0 of 19`)

- **Seat / Code / Branch / Base Commit:** `agy` (`fam3-v1-high-01`) / `origin/agy/cusp-action-2026-11-20` / `76d9799df`
  (`AGY-C66` received on `origin/main` in `M23` at harvest row `2041`; frozen harvest branch `origin/agy/audit-2026-11-02`
  untouched at `4319f47e2`; sealed `AGY-C1..C66` files untouched)
- **Synced Premises:** `origin/main @ ae7defd04` (`M23`, `SEAT_CODES.json`, Review `88` `B2018`, `P-885`; mathematical
  premises strictly pre-trial `<= B2008`: `GENESIS`, `S02`, `B98`, `B371`, `B377`, `B381`, `B1876`, `B1881`, `B1983`,
  `B1985`, `B1993`, `B1994`, `B2000`, `B2001`, `B2004`, `B2008`, `P-374`, `P-630`, `P-775`, `P-882`, with zero
  dependency on trial cards `B2011..B2017`), `agy-exp @ f250ed349`, `agy-002 @ 765c453a7`, `chat1 @ 19bc14af9`
- **Strict Scope (`0 of 19`):** Exact integer, rational, algebraic, and residual-certified arbitrary-precision listening
  on (`1`) the finite non-commutative two-counts Heisenberg–Weil register `C^N` (`odd N >= 3`), (`2`) the `3 x 3`
  Jacobian of the `6`-move trace walk `W_{6,tr}` across the positive Markoff tree (`B2000` Open `#2`), and (`3`) the
  birational blow-up `(u, v) = (x / z, y / z)` of the parabolic punctured-torus character surface `S_{kappa = -2}` across
  metallic grounds `L^m R^m` (`m in {1, 2, 3}`, `P-775`). Zero empirical constants, zero added parameters, zero post-hoc
  residue selection; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E4`) and Falsification Controls (`PF1`–`PF5`)

1. **`E1` (`Non-Commutative Two-Counts Weil Unfolding, Mod-4 Mirror Dichotomy, & All-3^k Chiral Index +2` — `B2008` Open `#1` & `P-374`):**
   - **Expectation `E1a` (`Stereo Commutation & Z_3 Equivariance`):** On `C^N` for odd `N >= 3` with `inv2 = (N + 1) / 2`,
     Heisenberg multiplier `r in (Z/NZ)^x` (`X Z = zeta_N^r Z X`, `zeta_N = exp(2 pi i / N)`), Gauss sum `G_{N,r} =
     sum_{b=0}^{N-1} zeta_N^{-r * inv2 * b^2}`, clock shear `rho_{N,r}(L) = diag(zeta_N^{r * inv2 * j^2})`, symplectic
     Fourier transform `(rho_{N,r}(S_{inv}))_{a,c} = G_{N,r}^{-1} zeta_N^{r a c}` representing `S^-1 = [[0, 1], [-1, 0]]`,
     `rho_{N,r}(R) = rho_{N,r}(S_{inv}) rho_{N,r}(L)^{-1} rho_{N,r}(S_{inv})^{-1}`, `rho_{N,r}(C_omega) = rho_{N,r}(L)
     rho_{N,r}(R)^{-1}`, and order-`3` `rho_{N,r}(C_{3,omega}) = rho_{N,r}(S_{inv})^2 rho_{N,r}(C_omega)`: the stereo
     walks `W_hat_+ = sum_{j=0}^2 C_omega^j L C_omega^{-j}` and `W_hat_- = sum_{j=0}^2 C_omega^j R C_omega^{-j}` satisfy
     `W_hat_- = W_hat_+^dagger`, `[W_hat_+, W_hat_-] = 0`, and `[W_hat_6, rho_{N,r}(C_{3,omega})] = 0` (`W_hat_6 = W_hat_+
     + W_hat_-`, `W_hat_{ch} = -i (W_hat_+ - W_hat_-)`).
   - **Expectation `E1b` (`Mod-4 Mirror Dichotomy Across Odd Primes` + `PF1`, `PF2`):** Complex conjugation satisfies
     `conj(rho_{N,r}(g)) = rho_{N,-r}(g)` (`intertwining H_1(rho_{N,r}) ~= H_2(rho_{N,-r})`), and coordinate scaling
     `(U_u psi)_j = psi_{u j mod N}` (`u in (Z/NZ)^x`) satisfies `U_u rho_{N,r}(g) U_u^{-1} = rho_{N, u^2 r}(g)`. Across
     all `8` odd primes `p in {3, 5, 7, 11, 13, 17, 19, 23}`:
     - **`p == 1 mod 4` (`p in {5, 13, 17}`):** `-1` is a square mod `p`, so `W_hat_6|_{H_1} ~= W_hat_6|_{H_2}` (`mirror
       paired`) and `W_hat_{ch}|_{H_1} ~= -W_hat_{ch}|_{H_2}`;
     - **`p == 3 mod 4` (`p in {3, 7, 11, 19, 23}`):** `-1` is a non-square mod `p`, so fixing the single symplectic
       orientation `r = 1` (`S02` / `SE2`) **natively splits `2 -> 1 + 1`** (`Spec(W_hat_6|_{H_1}) != Spec(W_hat_6|_{H_2})`).
     Collapsing `r = 1 -> r = 0` (`commuting limit`, `PF1`) kills the `p == 3 mod 4` split, while flipping `r = +1 -> -1`
     (`PF2`) swaps `H_1 <-> H_2` and inverts the chiral index `+2 -> -2`.
   - **Expectation `E1c` (`All-3^k Constant Chiral Index +2`):** Because `C_{3,omega} = S_{inv}^{-1} L^{-1}`,
     `tr rho_{3^k, 1}(C_{3,omega}) = G_+(3^k)^{-1} sum_{c=0}^{3^k - 1} zeta_{3^k}^{-3 * inv2 * c^2} = +i sqrt(3)` for
     every `k >= 1`, locking `(d_0, d_1, d_2) = (3^{k-1}, 3^{k-1} + 1, 3^{k-1} - 1)` and **constant chiral index
     `d_1 - d_2 = +2`** across `k in {1, 2, 3, 4, 5}` (`N = 3, 9, 27, 81, 243`).

2. **`E2` (`Exact Algebraic Weil Spectra at N in {3, 5, 7, 9, 15, 27}` — Bridging `CLAIMS P56–P63`):**
   - **Expectation `E2`:** Exact monic sector characteristic polynomials of `W_hat_{6,N,1}` hold to `< 10^{-30}`:
     - `N = 3`: `q = 0`: `x`; `q = 1`: `x^2 - 9`; `q = 2`: `1`;
     - `N = 5`: `q = 0`: `x + 2 sqrt(5)`; `q = 1, 2`: `(x - (3 - sqrt(5))/2)(x + (3 + 3 sqrt(5))/2)`;
     - `N = 7`: `q = 0`: `x^2 (x + 4)`; `q = 1`: `x^2 - 2 x + (-9 + sqrt(21))/2`; `q = 2`: `x^2 - 2 x + (-9 - sqrt(21))/2`;
     - `N = 9`: `q = 0`: `x (x - 4)(x - 6)`; `q = 1`: `(x^2 - x - 3)(x^2 - 3 x - 9)` (`golden roots 3 phi and -3 / phi at
       pure 3^2 = 9`); `q = 2`: `(x - 1)(x - 3)`;
     - `N = 15` (`dims (5, 6, 4)`, `d_1 - d_2 = +2`): `q = 1` isolates multiplicity-`1` `(3 + sqrt(5))/2 = phi^2` while
       `q = 2` isolates `(1 - sqrt(5))/2 = -1 / phi`;
     - `N = 27` (`dims (9, 10, 8)`): exact `Z[x]` factorizations on all three sectors.

3. **`E3` (`Universal Outward Markoff Tree Jacobian Cubic & AM–GM Theorem` — Closing `B2000` Open `#2`):**
   - **Expectation `E3` + `PF3`:** For `W_{6,tr}(x, y, z)`, `D^{-1}(J_{W_6}(x, y, z) - 2 I_3) D` (`D = diag(sqrt(x),
     sqrt(y), sqrt(z))`) is symmetric positive-definite for `x, y, z > 0` with `3`-square `SOS` quadratic form `(sqrt(y) v_1
     + sqrt(x) v_2)^2 + (sqrt(z) v_1 + sqrt(x) v_3)^2 + (sqrt(z) v_2 + sqrt(y) v_3)^2` and exact characteristic polynomial
     `(t - 2)(t - 2 - (x + y + z))^2 - 4 x y z`. Its local maximum at `t = 2 + (x + y + z)/3` is `(4 / 27)((x + y + z)^3 -
     27 x y z)`, so by `AM-GM` `(3, 3, 3)` is the **unique** positive Markoff triple with repeated eigenvalues `(14, 5, 5)`,
     splitting at `(3, 3, 6)` to `(t - 8)(t^2 - 22 t + 76)` (`PF3`, sharing `t^2 - 22 t + 76` with `(3, 6, 15)` where
     `cp = (t - 32)(t^2 - 22 t + 76)`), with `3` distinct eigenvalues `> 2` across all `64` non-root sorted triples to tree
     depth `7` (`65` total), and universal outward ray limits `lambda_1 / lambda_2 -> 1` and `lambda_3 -> (6 x + 4)/(x + 2)`
     along fixed-`x` boundary rays (`22 / 5` at `x = 3`).

4. **`E4` (`Rational Blow-Up, Log-Canonical Symplectomorphism, & Metallic Ground Hierarchy for P-775`):**
   - **Expectation `E4` + `PF4`, `PF5`:** Setting `(u, v) = (x / z, y / z) <-> z = (u^2 + v^2 + 1)/(u v)` on `x^2 + y^2 +
     z^2 = x y z` blows up `(0, 0, 0)`, turns `T_1, T_2` into `F_L(u, v) = (u / (v^2 + 1), u v / (v^2 + 1))` and `F_R(u, v)
     = (u v / (u^2 + 1), v / (u^2 + 1))` preserving the Goldman–Poincaré `2`-form `Omega = -du ^ dv / (u v)` with Ptolemy
     shapes `w_L = v^2 / (v^2 + 1)`, `w_R = 1 / (u^2 + 1)`, while `S^{-1}(L^m R^m) S = (L^m R^m)^{-1}` makes every metallic
     ground amphichiral. Proves exact tangent polynomials & certifies Bloch–Wigner step-ratio convergence to `< 10^{-7}`:
     - **Golden (`m = 1`, `LR`):** `t^2 - 5 t + 1 = 0`, rate `(5 + sqrt(21))/2` (`vs flat phi^4 = (7 + 3 sqrt(5))/2`, `PF4`)
       across `LLLLLLR`, `LLRRLLR`, and `LLLRRRRLLLR` to `k = 12` (`zero SnapPy`);
     - **Silver (`m = 2`, `L^2 R^2`):** `t^2 - 18 t + 1 = 0`, rate `9 + 4 sqrt(5) = phi^6`, and exact period volume
       **`V_2 = 4 * Catalan`**;
     - **Bronze (`m = 3`, `L^3 R^3`):** irreducible `Z`-quartic **`u^4 - 114 u^3 + 4264 u^2 - 58910 u + 192359 = 0`** for
       `tr(D Phi_3)` (`PF5`), settling at `(u_{max} + sqrt(u_{max}^2 - 4))/2`.

0 of 19.
