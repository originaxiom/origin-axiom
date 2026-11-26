# `Card AGY-C63` (`2026-11-26`) — Forward Remediation of `AGY-C62` (`D1`–`D5`): All-`k` Single-Orbit Proof (`M19`), `1`-Jet `X_0(Z/4Z)_smooth` Mixed `3^k * 2^m` vs `27 * p` Proof, `2`-Adic Halves, Mordell `15`-Leaf `Z^3` Proof, & Vortex Completeness (`0 of 19`)

- **Seat / Branch / Base Commit:** `agy` / `origin/agy/cusp-action-2026-11-20` / `b7cbdfede`
  (superseding unpushed `AGY-C62` `19edbc3e6..b7cbdfede` forward to close pre-push referee findings `D1`–`D5`;
  frozen harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`; sealed `AGY-C1..C61` untouched)
- **Synced Premises:** `origin/main @ 18c1b8ac2` (`M19`, `M20`, `B2011`–`B2014`, Review `87`),
  `agy-exp @ 3027116dc` (`X-EXHAUSTIVE-LISTENING`), `agy-002 @ fdbd7015f` (`A2-LISTENING-TOWER`),
  `chat1 @ 60840355a` (`V1`)
- **Strict Scope (`0 of 19`):** Pure `2 x 2` matrix `p`-adic valuation induction, `1`-jet finite-group
  stabilizer and CRT orbit decoupling without character tables, `2`-adic Hensel-obstruction and Kronecker-spin
  congruences, Hurwitz–Markoff `<s_1, s_2, s_3, S_3, V_4>` Mordell `L^1`-descent over `Z^3`, and explicit
  operator-computed `S_3 x Z_3` spectral LDOS decomposition. Zero empirical constants, zero added parameters,
  zero Standard Model pass/fail cells; order-`30` line kept on hold per `M18` item `5`.

---

## Pre-Committed Expectations (`E1`–`E5`) and Falsification Controls (`Controls 1`–`5`)

1. **`E1` (`Constructive All-k Single-Orbit Proof S_k = O_{3^k} & Schur–Euler Assembly, Closing M19 / B2011 #3 & D3`):**
   - **Expectation `E1a`:** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts linearly on `[x, z]^T` by
     `M_3 = [[0, 1], [-1, 3]]` (`and L(3, y, z) acts on [y, z]^T by M_3`), satisfying `M_3^4 = I_2 + 3 B` with
     `B = [[-3, 7], [-7, 18]]` and `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`. By `v_3(binom(3^{k-3}, j) *
     3^{j+1}) >= k` for `j >= 2`, with `e_k = 4 * 3^{k-3}`, `R^{c_1 e_k}(3, 3, 3) == (x_1, 3, z_1) = (3 + c_1
     3^{k-1}, 3, 3 - c_1 3^{k-1}) mod 3^k` for every `k >= 3`. Subsequent application of `L^{c_2 e_k}` acts via
     `M_{x_1} = M_3 + c_1 3^{k-1} E_{22}` on `v_1 = [3, z_1]^T == [0, 0]^T mod 3`: every `j >= 1` perturbation
     term is divisible by `3^{k-1} * 3 = 3^k`, and `(M_3^{c_2 e_k} - I_2) == 0 mod 3` annihilates `-c_1 3^{k-1}
     [0, 1]^T mod 3^k`, so `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)` (`c_1, c_2 in {0, 1, 2}`) hits all `9` Hensel
     fiber lifts above `(3, 3, 3) mod 3^{k-1}`. By `<L, R>`-equivariance from base `k = 3`, `S_k = O_{3^k}` is
     one `<L, R>`-orbit of size `8 * 3^{2k-4}` for **every** `k >= 3` (`verified through mod 59,049 = 3^{10}`).
   - **Expectation `E1b` & Control 1:** Bipartite Schur identity `det(x I - B_q) = x^{d_+ - d_-} det(x^2 I - A_q^H A_q)`
     yields `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)` identically; wrong exponent `2 * 3^{k-3}` moves `x`
     from `3` to `6 mod 9`.

2. **`E2` (`All-(k, m) 1-Jet Mixed 3^k * 2^m Halving Proof vs Odd-Prime 27 * p Failure, Closing B2012 Open #1, D2 & D3`):**
   - **Expectation `E2a` (`1-Jet Proof on X_0(Z/4Z)_smooth & CRT Decoupling`):** `M_3^3 = I_2 + 4 K` with
     `K = [[-1, 2], [-2, 5]] == I_2 mod 2` gives `M_3^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m` (`m >= 3`).
     From base `|O_{432}| = 4,608 = 72 * 64`, decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and
     `E_2(k, m) = 3^{k-2} * 2^{m-3}` (`m >= 5`, a multiple of `6` so `sum_{j=0}^{N-1} M_3^j E_{22} M_3^{N-1-j}`
     contains an even number of identical period-`3` blocks `== 0 mod 2` while `M_3^N == I_2 mod 2` fixes
     `c_1 2^{m-1}[0, 1]^T mod 2^m`) prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}` (`and |O_{2^m}| = 4^{m-1} for
     m >= 2`). For any `g` with `chi_C(g) != 1`: if `|Fix_{O_{27}}(g)| == 0` (`e.g. L^2, which has 0 fixed
     points on O_8 and O_{27}`), then `|Fix_{O_{3^k}}(g)| == 0` so `|Fix_{O_{3^k * 2^m}}(g)| == 0` automatically;
     if `|Fix_{O_{27}}(g)| > 0`, all `48` such elements of `G_{27}` (`order 216`) are conjugate to `C^{+-1}`,
     and on `O_{27} x X_0(Z/4Z)_{smooth}` (`16` smooth mod-`4` points carrying the `1`-jet `(p, Dg|_{V_p(F_2)})`),
     `|G| == 864 == 4 * 216`, `|K_{mod 4}| == 4`, and all `8` elements of `K_{mod 4} * C^{+-1}` fix a unique
     `v_2 in O_4` (`and O_2`) and fix only `v_2` in its `4`-point mod-`4` tangent fiber (`certifying
     det(Dg|_{V_{v_2}(F_2)} - I_2) == 1 mod 2`), lifting uniquely to `1` fixed point in `O_{2^m}` for **every**
     `m >= 3` — certified over `Z[x]` at `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts)**.
   - **Expectation `E2b` & Control 2:** `(L R)^3 in ker(-> G_{27})`, while across **all `60` primes `5 <= p < 300`**,
     `(L R)^{3 m}` violates `|Fix_{O_p}((L R)^{3 m} C)| = 1`. Since `W_6 ~= M_0 (+) M_1 (+) conj(M_1)` gives
     `P_{W_6}(x) = P_{M_0}(x) P_{M_1}(x)^2 in Z[x]`, monic `P_{2 M_1}(y) in Z[y]` (`y = 2 x`) yields exact
     Gauss-Lemma `Z[y]` unpaired polynomials of degree `10` (`mod 135`) and degree `8` (`mod 189`).

3. **`E3` (`2-Adic Hensel Bit, 50/50 Involution, & Scoped Transitivity, Closing B2012 Open #2, Review 87 C7 & D4`):**
   - **Expectation `E3`:** On `F == 5 mod 8`, one odd coordinate `u` and two even `v_1, v_2` force `grad F == 0
     mod 2`, `(u - v_1 v_2 / 2)^2 == F - 4 mod 16`, and `F(u + 2^{m-1}, v_1, v_2) - F(u, v_1, v_2) == 2^m mod
     2^{m+1}` (`m >= 3`). Thus **for every `k == 5 mod 8` and every `m >= 3`**, `beta_m(v) = ((F(v) - k) / 2^m)
     mod 2` is well-defined on `(Z/2^m Z)^3` and `<L, R, C, tau>`-invariant, the involution `u -> u + 2^{m-1}`
     bijectively swaps `beta_m = 0 <-> 1` (`exact 50/50 split`), and `beta_m = 1` has `0` lifts to `2^{m+1}`
     (`mod-8 base given by Kronecker spin eta_2`). Single-orbit `<L, R>`-transitivity of each `9 * 2^{2m-3}` half
     is verified exhaustively across **all `30` residue classes of `k == 5 mod 8 mod 2^{m+1}` for `3 <= m <= 6`**
     (`covering every integer k == 5 mod 8 at mod 8, 16, 32, 64`) plus `k in {5, 13, 29}` at `m = 7` (`mod 128`).

4. **`E4` (`Hurwitz–Markoff <s_1, s_2, s_3, S_3, V_4> Mordell Proof on All 15 Hasse Leaves, Closing B2012 Open #3 & D1`):**
   - **Expectation `E4`:** Minimizing `|x| + |y| + |z|` over the full `F`-preserving group `<s_1, s_2, s_3, S_3, V_4>`
     (`where Klein-four double sign flips V_4 reduce (-a, -b, +c) -> (+a, +b, +c) when x y z > 0, and flip the two
     positive signs of (+r, +s, -t) -> (-r, -s, -t) when x y z < 0 so k > max(r, s, t)^2`), concave reduction for
     all `k <= -1` (`remediating D1's k <= -9 cutoff; verified with 0 false empties across all 999 leaves in
     [-500, 500] \ {0, 4}`, giving `B_max(-8) = 6, B_max(-4) = 4`, and `max B_max = 13`) certifies **zero integer
     points over all `Z^3`** on all `15` Hasse leaves (`Control 4: 9 solvable seeds including (3,3,4), (-4,-3,3),
     (3,4,4) scrambled past 5,000 bits all descend inside [-B_max, B_max]^3`).

5. **`E5` (`Explicit Operator-Pulled-Back Vortex Zero & Neutral Bulk Completeness, Remediating D5`):**
   - **Expectation `E5`:** Direct `n_k`-dimensional operator evaluation (`zero literal flags`) on `O_{3^k}` at
     `k = 3, 4, 5` certifies `||(Pi_1 + Pi_2) delta_{f_i}||^2 == 0/1` on all `3` `C`-fixed points and verifies on
     explicitly pulled-back `v_{+6}^{(k)}, v_{-6}^{(k)}, v_{2 x psi_0}^{(k)}` that `W_6` acts by `+6, -6, 0` with
     summed `(3, 3, 3)` LDOS `4 / n_k`, forcing `1 - 4 / n_k -> 1` (`17/18, 161/162, 1457/1458`) into paired
     neutral bulk modes (`graphene mode LDOS 1/12 at mod 27, 1/108 at mod 81`; `Control 5: 2/3 at (3, 3, 6)`).

0 of 19.
