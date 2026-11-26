# `Card AGY-C62` (`2026-11-26`) — Pre-Execution Expectations: All-`k` Single-Orbit Proof (`M19`), Mixed `3^k * 2^m` vs Odd-Prime Towers, `2`-Adic Halves, Mordell `15`-Leaf Proof, & Vortex Completeness (`0 of 19`)

- **Seat / Branch / Base Commit:** `agy` / `origin/agy/cusp-action-2026-11-20` / `beeef839d`
  (frozen harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Synced Premises:** `origin/main @ 18c1b8ac2` (`M19`, `M20`, `B2011`–`B2014`, Review `87`),
  `agy-exp @ 3027116dc` (`X-EXHAUSTIVE-LISTENING`), `agy-002 @ fdbd7015f` (`A2-LISTENING-TOWER`),
  `chat1 @ 60840355a` (`V1`)
- **Strict Scope (`0 of 19`):** Pure `2 x 2` matrix `p`-adic valuation induction, finite-group stabilizer
  and CRT orbit decoupling without character tables, `2`-adic Hensel-obstruction and Kronecker-spin
  congruences, Mordell / Ghosh–Sarnak `L^1`-descent over `Z^3`, and exact `S_3 x Z_3` spectral LDOS
  decomposition. Zero empirical constants, zero added parameters, zero Standard Model pass/fail cells;
  order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E5`) and Falsification Controls (`Controls 1`–`5`)

1. **`E1` (`Constructive All-k Single-Orbit Proof S_k = O_{3^k} & Schur–Euler Assembly, Closing M19 / B2011 #3`):**
   - **Expectation `E1a`:** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts linearly on `[x, z]^T` by
     `M = [[0, 1], [-1, 3]]` (`and L(3, y, z) acts on [y, z]^T by the identical matrix M`), satisfying
     `M^4 = I_2 + 3 B` with `B = [[-3, 7], [-7, 18]]` and `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`.
     By the `3`-adic binomial bound `v_3(binom(3^{k-3}, j) * 3^{j+1}) >= k` for all `j >= 2`, for every
     `k >= 3` (`with e_k = 4 * 3^{k-3}`), `R^{e_k}(3, 3, 3) == (3, 3, 3) + 3^{k-1}(1, 0, -1) mod 3^k`
     and `L^{e_k}(3, 3, 3) == (3, 3, 3) + 3^{k-1}(0, 1, -1) mod 3^k`, so `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)`
     (`c_1, c_2 in {0, 1, 2}`) hits all `9` Hensel fiber lifts above `(3, 3, 3) mod 3^{k-1}`. By
     `<L, R>`-equivariance over the inductive base `k = 3`, `S_k = O_{3^k}` is a single `<L, R>`-orbit of
     size `8 * 3^{2k-4}` for **every** `k >= 3` (`explicitly verified through mod 59,049 = 3^{10}`).
   - **Expectation `E1b`:** For block-bipartite `B_q = [[0, A_q], [A_q^H, 0]]` with `d_+^{(0)} - d_-^{(0)} = +2`,
     `d_+^{(1)} - d_-^{(1)} = -1`, `d_{neu} = d_{chg} + 3`, and `spec(A_0^H A_0) = {36} U (4 spec(A_1^H A_1) \ {0})`,
     the bipartite Schur determinant identity yields `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)` identically.
   - **Control 1 (Planted Wrong `3`-Tower Exponent):** Replacing `4 * 3^{k-3}` by `2 * 3^{k-3}` fails to fix
     `(3, 3, 3) mod 9` (`moving x from 3 to 6 mod 9`).

2. **`E2` (`All-(k, m) Mixed 3^k * 2^m Halving Proof vs Odd-Prime 27 * p Failure, Closing B2012 Open #1`):**
   - **Expectation `E2a` (`All-(k, m) 2-Tower Survival`):** On `O_2` (`4` points), `G(O_2) ~= A_4` (`order 12`),
     whose abelianization `A_4 / V_4 ~= Z_3` is `chi_C`, so every `g` with `chi_C(g) != 1` acts as a `3`-cycle
     fixing `1` point on `O_2` and `O_4`; for `m >= 3`, `det(C - I|_{V_0(F_2)}) == 1 mod 2` lifts that fixed
     point uniquely to `O_{2^m}`. Moreover, `M^3 = I_2 + 4 K` with `K = [[-1, 2], [-2, 5]] == I_2 mod 2` gives
     `M^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m` (`m >= 3`). From base `|O_{432}| = 4,608 = 72 * 64`,
     decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and `E_2(k, m) = 3^{k-2} * 2^{m-3}` (`m >= 5`)
     prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}` and `|Fix_{O_{3^k * 2^m}}(g)| == |Fix_{O_{27}}(g)|` for all
     `chi_C(g) != 1`, establishing exact `Z[x]` halving for **every** `k >= 3, m >= 1` — certified over `Z[x]`
     at `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts, `d_{neu} = 386, d_{chg} = 383`)**.
   - **Expectation `E2b` (`Odd-Prime Mixed Failure Without Character Tables`):** `(L R)^3` acts trivially on
     `O_{27}`, while across **all `60` odd primes `5 <= p < 300`** (`scoped explicitly per Review 87`), a small
     power `(L R)^{3 m}` violates `|Fix_{O_p}((L R)^{3 m} C)| = 1`. By Gauss's Lemma in `y = 2 x`, exact
     unpaired charged polynomials in `Z[y]` are `(y^2 - 4 y - 8)(y^2 + 4 y - 8)(y^3 - 12 y - 8)(y^3 - 12 y + 8)`
     (`10` unpaired of `959` at `mod 135 = 27 * 5`) and `(y^2 - 2 y - 16)(y^2 + 2 y - 16)(y^2 - 2 y - 4)(y^2 + 2 y - 4)`
     (`8` unpaired of `671` at `mod 189 = 27 * 7`).
   - **Control 2:** Asserting `27 * p` preserves halving like `27 * 2^m` fails on all `60` primes `5 <= p < 300`
     and leaves `10` (`mod 135`) and `8` (`mod 189`) unpaired charged roots.

3. **`E3` (`Exact 2-Adic Hensel-Obstruction Bit & Mod-8 Kronecker Spin, Closing B2012 Open #2 / Review 87 C7`):**
   - **Expectation `E3a`:** Whenever `F(x, y, z) == 5 mod 8`, `(x, y, z)` has one odd coordinate `u` and two
     even coordinates `v_1, v_2`, forcing `grad F == (0, 0, 0) mod 2` and the exact congruence
     `(u - v_1 v_2 / 2)^2 == F(x, y, z) - 4 mod 16` across all `1,152` solutions in `(Z/16Z)^3`.
   - **Expectation `E3b`:** Because `grad F == 0 mod 2`, `F(v + 2^m d) == F(v) mod 2^{m+1}`, so for **every**
     `k == 5 mod 8` and **every** `m >= 3`, `beta_m(v) = ((F(v) - k) / 2^m) mod 2 in {0, 1}` is well-defined on
     `(Z/2^m Z)^3` and `<L, R, C, tau>`-invariant, separating the two equal halves of size `9 * 2^{2m-3}`
     (`verified across m = 3..7, mod 8 through mod 128 = 36,864 pts`), with base `m = 3` given by Kronecker spin
     `eta_2(v) = (2 / (u - v_1 v_2 / 2)) in {-1, +1}`, while `beta_m = 1` has `0` lifts to `2^{m+1}`.
   - **Control 3:** On `k = 1` (`!= 5 mod 8`) at `mod 8`, `X_1(Z/8Z)` splits into `(18, 18, 6, 6)`, not `(72, 72)`.

4. **`E4` (`Mordell / Ghosh–Sarnak L^1-Descent Proof on All 15 Hasse-Violating Leaves, Closing B2012 Open #3`):**
   - **Expectation `E4`:** Concave Vieta reduction `z(a b - z) >= b(a b - b)` (`x y z > 0`), all-negative sign
     flip (`x y z < 0`), positive-definite binary bounds (`|x| <= 1`), and `k - 4 != square` (`|x| = 2`) bound
     any minimal integer solution in `Z^3` by `max(|x|, |y|, |z|) <= B_max(k) <= 13` across all `15` leaves
     `[-54, -47, -44, -38, -26, -19, -18, -14, -8, -4, 46, 56, 86, 124, 126]`, certifying **zero integer points
     over all `Z^3`** on all `15` leaves (`Control 4: 6 solvable leaves scrambled past 1,500 digits all descend
     back inside [-B_max, B_max]^3`).

5. **`E5` (`Wavefunction Listening Blind Spot — Topological Vortex Zero vs Neutral Bulk Completeness`):**
   - **Expectation `E5`:** For every `k >= 3` (`n_k = 8 * 3^{2k-4}`), charged projector `Pi_1 + Pi_2` vanishes
     identically on all `3` `C`-fixed points (`LDOS_{chg}(Fix(C)) == 0`), whereas on `(3, 3, 3)` the `3`
     `S_3 x Z_3` neutral exception modes (`+6`, `-6`, and `2 x psi_0` null mode, with `||P_{2 x psi_0} delta_{(3,3,3)}||^2
     == 1/36` at `mod 27`) carry exact total LDOS `(1 + 1 + 2) / n_k = 4 / n_k`, forcing **`1 - 4 / n_k -> 1`**
     (`17/18`, `161/162`, `1457/1458` at `mod 27, 81, 243`) into paired neutral bulk modes (`with graphene
     slow-decay mode carrying 1/12 at mod 27 and 1/108 at mod 81`; `Control 5: off-vortex (3, 3, 6) has charged
     LDOS 2/3 != 0`).

0 of 19.
