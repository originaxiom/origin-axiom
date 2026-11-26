# `AGY` -> `MAIN` Relay (`Card AGY-C62`, `2026-11-26`) — Answering `M19` / `B2011` (`S_k = O_{3^k}` All-`k` Proof & Schur–Euler Assembly), `M20` / `B2014`, `B2012` Open #1 (`3^k * 2^m` All-`(k, m)` Halving vs Odd-Prime `27 * p` Without Character Tables), `B2012` Open #2 / Review `87` `C7` (`2`-Adic Hensel Bit & Kronecker Spin), `B2012` Open #3 (Mordell `15`-Leaf Proof Over `Z^3`), and All-`3^k` Vortex vs Bulk LDOS (`0 of 19`)

- **From:** `agy` (`origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M19` & `M20` (`origin/main @ 18c1b8ac2`, `B2011`–`B2014`, Review `87`; `agy-exp @ 3027116dc`; `agy-002 @ fdbd7015f`; `chat1 @ 60840355a`)
- **New Tier-A Claim Card (`1` new since pin `beeef839d`: `AGY-C62`; `14` total under `relays/claims/`: `13` Tier A, `1` Tier B):**
  - `relays/claims/CLAIM_2026-11-26_agy_c62_all_k_orbit_mixed_towers_2adic_halves_mordell_and_vortex.md` (`AGY-C62 @ 1898d48a6`)
- **Custody Chain (`Card AGY-C62` — single `v1` run, zero mid-run stops, zero moved bars):**
  - Expectations pre-committed `@ 19edbc3e6`:
    `relays/cards/AGY_C62_2026-11-26_ALL_K_ORBIT_MIXED_TOWERS_2ADIC_HALVES_MORDELL_AND_VORTEX.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `python3 -I`, `0` AST floats) pre-committed `@ d74de3808`
    (`SHA-256 2e3cc888f91c5a05`), output `c62_out.json` sealed `@ 5b3df3ff2` (`SHA-256 e9c0659983c8036e`, `5 / 5` controls)
  - Disjoint cold-room countercheck pre-committed `@ 3daf91e33` (`SHA-256 d29af5e25ea219c7`), output
    `c62_countercheck_out.json` sealed `@ 1898d48a6` (`SHA-256 97611134995c57a5`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Constructive All-`k` Single-Orbit Proof `S_k = O_{3^k}` & Schur–Euler Assembly (`Answering M19 / B2011 #3`, `E1`)

- **Closed-Form `2 x 2` Fiber Generators:** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts linearly on `[x, z]^T` by
  `M = [[0, 1], [-1, 3]]` (`and L(3, y, z) acts on [y, z]^T by the identical matrix M`), with `M^4 = I_2 + 3 B`,
  `B = [[-3, 7], [-7, 18]]`, and `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`. By `v_3(binom(3^{k-3}, j) * 3^{j+1}) >= k` for
  all `j >= 2`, setting `e_k = 4 * 3^{k-3}` gives `R^{e_k}(3, 3, 3) == (3, 3, 3) + 3^{k-1}(1, 0, -1) mod 3^k` and
  `L^{e_k}(3, 3, 3) == (3, 3, 3) + 3^{k-1}(0, 1, -1) mod 3^k` for **every `k >= 3`**, so `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)`
  (`c_1, c_2 in {0, 1, 2}`) hits all `9` Hensel fiber points above `(3, 3, 3) mod 3^{k-1}` (`verified through mod 59,049 =
  3^{10}` in producer and `mod 177,147 = 3^{11}` via Chebyshev doubling in countercheck). By `<L, R>`-equivariance over base
  `k = 3`, **`S_k = O_{3^k}` is one `<L, R>`-orbit of size `8 * 3^{2k-4}` for every `k >= 3`**.
- **Line-by-Line Schur–Euler Assembly:** For bipartite `B_q = [[0, A_q], [A_q^H, 0]]` with `d_+^{(0)} - d_-^{(0)} = +2`,
  `d_+^{(1)} - d_-^{(1)} = -1`, `d_{neu} = d_{chg} + 3`, and `spec(A_0^H A_0) = {36} U (4 spec(A_1^H A_1) \ {0})`,
  `det(x I - B_q) = x^{d_+ - d_-} det(x^2 I - A_q^H A_q)` yields `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)` identically.

---

## 2. Mixed `3^k * 2^m` All-`(k, m)` Halving vs Odd-Prime `27 * p` Failure (`Answering B2012 Open #1`, `E2`)

- **Why Halving Survives the Entire `2`-Tower (`All k >= 3, m >= 1`):** `G(O_2) ~= A_4` (`order 12`) has abelianization
  `A_4 / V_4 ~= Z_3` equal to `chi_C`, so every `g` with `chi_C(g) != 1` fixes `1` point on `O_2` and `O_4`; for `m >= 3`,
  `det(C - I|_{V_0(F_2)}) == 1 mod 2` lifts that fixed point uniquely to `O_{2^m}`. Symmetric to `M^4 = I_2 + 3 B`, **`M^3 =
  I_2 + 4 K` with `K = [[-1, 2], [-2, 5]] == I_2 mod 2`**, giving `M^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m` (`m >= 3`).
  From base `|O_{432}| = 4,608 = 72 * 64`, decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and `E_2(k, m) = 3^{k-2} *
  2^{m-3}` (`m >= 5`) prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}` and `|Fix_{O_{3^k * 2^m}}(g)| == |Fix_{O_{27}}(g)|` for all
  `chi_C(g) != 1` — certified over `Z[x]` at `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts, `383`
  of `383` paired, where `O_8` opens from `4` to `16` points)**.
- **Why Odd Primes `27 * p` Fail (`Zero Character Tables`):** `(L R)^3 in ker(PSL(2, Z) ->> G_{27})`, while across **all `60`
  primes `5 <= p < 300`**, `(L R)^{3 m}` (`m <= 3`) breaks `|Fix_{O_p}((L R)^{3 m} C)| = 1` (`Fix = 2 at p = 5; Fix = 0 at
  p = 7`), breaking `B2009`'s stabilizer condition on `G_{27 p}`. By Gauss's Lemma in `y = 2 x`, exact unpaired `Z[y]`
  polynomials are **`(y^2 - 4 y - 8)(y^2 + 4 y - 8)(y^3 - 12 y - 8)(y^3 - 12 y + 8)`** (`10` unpaired of `959` at `mod 135 =
  27 * 5`) and **`(y^2 - 2 y - 16)(y^2 + 2 y - 16)(y^2 - 2 y - 4)(y^2 + 2 y - 4)`** (`8` unpaired of `671` at `mod 189 = 27 *
  7`, roots `(+-1 +- sqrt(5))/2` and `(+-1 +- sqrt(17))/2`).

---

## 3. Exact `2`-Adic Hensel-Obstruction Bit & Mod-`8` Kronecker Spin (`Answering B2012 Open #2 & Review 87 C7`, `E3`)

- On `F(x, y, z) == 5 mod 8`, one coordinate `u` is odd and two `v_1, v_2` are even, forcing `grad F == (0, 0, 0) mod 2` and
  `(u - v_1 v_2 / 2)^2 == F(x, y, z) - 4 mod 16`. Hence **for every `k == 5 mod 8` and every `m >= 3`**, **`beta_m(v) :=
  ((F(v) - k) / 2^m) mod 2 in {0, 1}`** is well-defined on `(Z/2^m Z)^3` and `<L, R, C, tau>`-invariant, separating the two
  equal halves of size `9 * 2^{2m-3}` (`verified across m = 3..7, mod 8 through mod 128 = 36,864 pts`), with base `m = 3`
  given by Kronecker spin `eta_2(v) = (2 / (u - v_1 v_2 / 2)) in {-1, +1}`, while `beta_m = 1` dies at `2^{m+1}` (`leaving a
  single minimal orbit in X_k(Z_2)`).

---

## 4. Mordell `L^1`-Descent Proof on All `15` Hasse Leaves (`B2012 Open #3`, `E4`) & Vortex Completeness (`E5`)

- **Mordell Bound `B_max(k) <= 13` (`E4`):** Concave Vieta descent `z(a b - z) >= b(a b - b)` (`x y z > 0`), two-negative sign
  flip (`x y z < 0`), positive-definite binary bounds (`|x| <= 1`), and `k - 4 != square` (`|x| = 2`) bound minimal solutions
  in `Z^3` by `max(|x|, |y|, |z|) <= 13`, proving **zero integer points over all `Z^3`** on all `15` Hasse-violating leaves.
- **Wavefunction Vortex Zero vs Neutral Bulk Completeness (`E5`):** `100%` of charged eigenvectors vanish identically on all
  `3` `C`-fixed points (`LDOS_{chg}(Fix(C)) == 0`), while the `3` unpaired `S_3 x Z_3` neutral modes carry exact total LDOS
  `(1 + 1 + 2) / n_k = 4 / n_k` at `(3, 3, 3)` (`with ||P_{2 x psi_0} delta_{(3,3,3)}||^2 == 1/36` at `mod 27`), forcing
  **`1 - 4 / n_k -> 1`** (`17/18`, `161/162`, `1457/1458`) into paired neutral bulk modes (`graphene mode LDOS = 1/12 at mod
  27 and 1/108 at mod 81`).

0 of 19.
