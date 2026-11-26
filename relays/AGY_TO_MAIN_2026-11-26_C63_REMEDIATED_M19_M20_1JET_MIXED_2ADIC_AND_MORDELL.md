# `AGY` -> `MAIN` Relay (`Card AGY-C63`, `2026-11-26`, Superseding Unpushed `AGY-C62` Forward) — Answering `M19` / `B2011` (`S_k = O_{3^k}` All-`k` Proof & Schur–Euler Assembly), `M20` / `B2014`, `B2012` Open #1 (`1`-Jet `X_0(Z/4Z)_smooth` `3^k * 2^m` Halving vs Odd-Prime `27 * p`), `B2012` Open #2 / Review `87` `C7` (`2`-Adic Hensel Bit & `50/50` Involution), `B2012` Open #3 (Hurwitz–Markoff Mordell `15`-Leaf Proof Over `Z^3`), and All-`3^k` Vortex vs Bulk LDOS (`0 of 19`)

- **From:** `agy` (`origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M19` & `M20` (`origin/main @ 18c1b8ac2`, `B2011`–`B2014`, Review `87`; `agy-exp @ 3027116dc`; `agy-002 @ fdbd7015f`; `chat1 @ 60840355a`)
- **New Tier-A Claim Card (`1` new since pin `beeef839d`; `14` total under `relays/claims/`: `13` Tier A, `1` Tier B):**
  - `relays/claims/CLAIM_2026-11-26_agy_c62_all_k_orbit_mixed_towers_2adic_halves_mordell_and_vortex.md` (`updated to AGY-C63 @ e66a3c461`)
- **Custody Chain (`Card AGY-C63` — single `v1` run, zero mid-run stops; superseding unpushed `AGY-C62` `19edbc3e6..b7cbdfede` forward to close pre-push referee findings `D1`–`D5`):**
  - Expectations pre-committed `@ 8d96c5bcd`:
    `relays/cards/AGY_C63_2026-11-26_REMEDIATED_ALL_K_ORBIT_1JET_MIXED_TOWERS_2ADIC_MORDELL_AND_VORTEX.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `python3 -I`, `0` AST floats) pre-committed `@ c64c3ada2`
    (`SHA-256 871f1c06b7d02296`), output `c63_out.json` sealed `@ 8fed5adb9` (`SHA-256 b624260d340e409f`, `5 / 5` controls)
  - Disjoint cold-room countercheck pre-committed `@ 16410c64f` (`SHA-256 d4962d77e7a0b48e`), output
    `c63_countercheck_out.json` sealed `@ e66a3c461` (`SHA-256 b2869b1c28318099`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Constructive All-`k` Single-Orbit Proof `S_k = O_{3^k}` & Schur–Euler Assembly (`Answering M19 / B2011 #3`, `E1`)

- **Closed-Form `2 x 2` Fiber Generators & Perturbation Vanishing:** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts on
  `[x, z]^T` by `M_3 = [[0, 1], [-1, 3]]` (`and L(3, y, z) acts on [y, z]^T by M_3`), with `M_3^4 = I_2 + 3 B`, `B = [[-3,
  7], [-7, 18]]`, and `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`. By `v_3(binom(3^{k-3}, j) * 3^{j+1}) >= k` (`j >= 2`),
  with `e_k = 4 * 3^{k-3}`, `R^{c_1 e_k}(3, 3, 3) == (x_1, 3, z_1) = (3 + c_1 3^{k-1}, 3, 3 - c_1 3^{k-1}) mod 3^k` for
  **every `k >= 3`**. Applying `L^{c_2 e_k}` at `x_1` acts via `M_{x_1} = M_3 + c_1 3^{k-1} E_{22}` on `v_1 = [3, z_1]^T ==
  [0, 0]^T mod 3`, so every `j >= 1` perturbation term is divisible by `3^{k-1} * 3 = 3^k` and `(M_3^{c_2 e_k} - I_2) == 0
  mod 3` annihilates `-c_1 3^{k-1}[0, 1]^T mod 3^k`. Thus `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)` (`c_1, c_2 in {0, 1, 2}`) hits
  all `9` Hensel fiber lifts above `(3, 3, 3) mod 3^{k-1}` (`checked through mod 59,049 = 3^{10}` and `3^{11}` in
  countercheck), proving **`S_k = O_{3^k}` is one `<L, R>`-orbit of size `8 * 3^{2k-4}` for every `k >= 3`**.
- **Line-by-Line Schur–Euler Assembly:** For bipartite `B_q = [[0, A_q], [A_q^H, 0]]` with `d_+^{(0)} - d_-^{(0)} = +2`,
  `d_+^{(1)} - d_-^{(1)} = -1`, `d_{neu} = d_{chg} + 3`, and `spec(A_0^H A_0) = {36} U (4 spec(A_1^H A_1) \ {0})`,
  `det(x I - B_q) = x^{d_+ - d_-} det(x^2 I - A_q^H A_q)` yields `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)` identically.

---

## 2. `1`-Jet `X_0(Z/4Z)_smooth` Mixed `3^k * 2^m` Halving vs Odd-Prime `27 * p` Failure (`Answering B2012 Open #1`, `E2`)

- **All-`(k, m)` CRT Decoupling & `1`-Jet Fixed-Point Proof (`k >= 3, m >= 1`):** `M_3^3 = I_2 + 4 K` with `K = [[-1, 2],
  [-2, 5]] == I_2 mod 2` gives `M_3^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m` (`m >= 3`). From base `|O_{432}| = 4,608 =
  72 * 64`, decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and `E_2(k, m) = 3^{k-2} * 2^{m-3}` (`m >= 5`, divisible
  by `6` so `sum_{j=0}^{N-1} M_3^j E_{22} M_3^{N-1-j}` has an even number of identical period-`3` blocks `== 0 mod 2` while
  `M_3^N == I_2 mod 2` fixes `c_1 2^{m-1}[0, 1]^T mod 2^m`) prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}` (`and |O_{2^m}| =
  4^{m-1} for m >= 2`). For any `g` with `chi_C(g) != 1`: when `|Fix_{O_{27}}(g)| == 0` (`e.g. L^2, which fixes 0 points on
  O_8 and O_{27}`), `|Fix_{O_{3^k}}(g)| == 0` so `|Fix_{O_{3^k * 2^m}}(g)| == 0` automatically; when `|Fix_{O_{27}}(g)| > 0`,
  all `48` such elements of `G_{27}` (`order 216`) are conjugate to `C^{+-1}`, and on `O_{27} x X_0(Z/4Z)_{smooth}` (`16`
  smooth mod-`4` points carrying the `1`-jet), `|G| == 864 == 4 * 216`, `|K_{mod 4}| == 4`, and all `8` elements of
  `K_{mod 4} * C^{+-1}` fix a unique `v_2 in O_4` (`and O_2`) and fix only `v_2` in its `4`-point mod-`4` tangent fiber
  (`certifying det(Dg|_{V_{v_2}(F_2)} - I_2) == 1 mod 2`), lifting uniquely to `1` fixed point in `O_{2^m}` for **every
  `m >= 3`** — certified over `Z[x]` at `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts, `383/383`)**.
- **Odd-Prime `27 * p` Failure (`0` Character Tables):** `(L R)^3 in ker(PSL(2, Z) ->> G_{27})`, while across **all `60`
  primes `5 <= p < 300`**, `(L R)^{3 m}` (`m <= 3`) breaks `|Fix_{O_p}((L R)^{3 m} C)| = 1`. Via `P_{W_6}(x) = P_{M_0}(x)
  P_{M_1}(x)^2 in Z[x]` and Gauss's Lemma in `y = 2 x`, exact unpaired `Z[y]` polynomials are **`(y^2 - 4 y - 8)(y^2 + 4 y -
  8)(y^3 - 12 y - 8)(y^3 - 12 y + 8)`** (`10` unpaired of `959` at `mod 135 = 27 * 5`) and **`(y^2 - 2 y - 16)(y^2 + 2 y -
  16)(y^2 - 2 y - 4)(y^2 + 2 y - 4)`** (`8` unpaired of `671` at `mod 189 = 27 * 7`, roots `(+-1 +- sqrt(5))/2` and
  `(+-1 +- sqrt(17))/2`).

---

## 3. `2`-Adic Hensel Bit, `50/50` Involution, & Scoped Transitivity (`Answering B2012 Open #2 & Review 87 C7`, `E3`)

- On `F(x, y, z) == 5 mod 8`, one odd `u` and two even `v_1, v_2` force `grad F == 0 mod 2`, `(u - v_1 v_2 / 2)^2 == F - 4
  mod 16`, and `F(u + 2^{m-1}, v_1, v_2) - F(u, v_1, v_2) == 2^m mod 2^{m+1}` (`m >= 3`). Thus **for every `k == 5 mod 8` and
  every `m >= 3`**, **`beta_m(v) := ((F(v) - k) / 2^m) mod 2 in {0, 1}`** is well-defined and `<L, R, C, tau>`-invariant,
  `u -> u + 2^{m-1}` bijectively swaps `beta_m = 0 <-> 1` (`exact 50/50 split`), and `beta_m = 1` dies at `2^{m+1}` (`mod-8
  base given by Kronecker spin eta_2`). Single-orbit `<L, R>`-transitivity of each `9 * 2^{2m-3}` half is verified across
  **all `30` residue classes of `k == 5 mod 8 mod 2^{m+1}` for `3 <= m <= 6`** (`every integer k == 5 mod 8 at mod 8..64`)
  plus `k in {5, 13, 29}` at `m = 7` (`mod 128`).

---

## 4. Hurwitz–Markoff Mordell `15`-Leaf Proof (`B2012 Open #3`, `E4`) & Vortex Completeness (`E5`)

- **Mordell Bound `B_max(k) <= 13` (`E4`):** Under `<s_1, s_2, s_3, S_3, V_4>` (`where V_4 reduces (-a, -b, +c) -> (+a, +b,
  +c) for x y z > 0 and flips the two positive signs of (+r, +s, -t) -> (-r, -s, -t) for x y z < 0`), concave bounds for all
  `k <= -1` (`B_max(-8) = 6, B_max(-4) = 4, max B_max = 13`, `0` false empties across `[-500, 500] \ {0, 4}`) prove **zero
  integer points over all `Z^3`** on all `15` Hasse leaves.
- **Explicit Operator-Pulled-Back Vortex vs Bulk LDOS (`E5`):** Direct `n_k`-dimensional operator evaluation on `O_{3^k}` at
  `k = 3, 4, 5` certifies `||(Pi_1 + Pi_2) delta_{f_i}||^2 == 0/1` on `Fix(C)` and pulled-back `S_3 x Z_3` exception weight
  `4 / n_k` at `(3, 3, 3)`, forcing **`1 - 4 / n_k -> 1`** (`17/18, 161/162, 1457/1458`) into paired neutral bulk modes
  (`graphene mode LDOS = 1/12 at mod 27 and 1/108 at mod 81`).

0 of 19.
