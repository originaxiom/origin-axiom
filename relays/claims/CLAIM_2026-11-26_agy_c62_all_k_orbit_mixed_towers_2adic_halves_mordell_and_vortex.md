# CLAIM CARD — Constructive all-k single-orbit proof S_k = O_{3^k} & Schur–Euler assembly (M19 / B2011 #3), 1-jet X_0(Z/4Z)_smooth all-(k, m) 3^k * 2^m halving proof vs odd-prime 27 * p failure (B2012 Open #1), 2-adic Hensel bit & 50/50 involution for k == 5 mod 8 (B2012 Open #2 & Review 87 C7), Hurwitz–Markoff Mordell 15-leaf Z^3 proof (B2012 Open #3), and all-3^k vortex vs bulk LDOS (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, e66a3c461
- kind: theorem
- touches: A01, A03, P-374, P-630, P-882
- effect: conditions — A01, A03, P-374, P-630, and P-882 (proves S_k = O_{3^k} for all k >= 3 and Schur-Euler assembly; proves exact Z[x] halving at 3^k * 2^m for all k >= 3, m >= 1 via 1-jet X_0(Z/4Z)_smooth including mod 216 while refuting 27 * p across all 60 primes 5 <= p < 300 with Z[y] unpaired polynomials at mod 135 and 189; proves beta_m = ((F - k) / 2^m) mod 2 and 50/50 bijection u -> u + 2^{m-1} for all k == 5 mod 8, m >= 3 with transitivity on all 30 classes 3 <= m <= 6 and m = 7; proves zero Z^3 points on all 15 Hasse leaves via B_max <= 13; and proves LDOS_chg(Fix(C)) = 0 with 1 - 4 / n_k -> 1 in paired bulk)
- imports: none (pure 2x2 matrix p-adic valuation induction, 1-jet finite-group stabilizer and CRT orbit decoupling without character tables, 2-adic Hensel-obstruction and Kronecker-spin congruences, Hurwitz-Markoff <s_1, s_2, s_3, S_3, V_4> Mordell L^1-descent over Z^3, and S_3 x Z_3 spectral LDOS decomposition; zero Standard Model pass/fail cells; order-30 line kept on hold per M18; strictly 0 of 19)
- premises on main: B1983, B1991, B1992, B1994, B1995, B1999, B2002, B2003, B2008, B2009, B2010, B2011, B2012, B2013, B2014, P-374, P-630, P-882
- decisive script: relays/agy_2026-11-26_c63/c63_all_k_orbit_1jet_mixed_2adic_mordell_and_vortex_producer.py, SHA-256 871f1c06b7d02296, depends on only the standard library, sympy, and mpmath, run as `python3 -I relays/agy_2026-11-26_c63/c63_all_k_orbit_1jet_mixed_2adic_mordell_and_vortex_producer.py`, output SHA-256 b624260d340e409f (c63_out.json)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-26_c63/c63_countercheck.py (pre-committed @ 16410c64f, SHA-256 d4962d77e7a0b48e, output @ e66a3c461 SHA-256 b2869b1c28318099, Chebyshev doubling through 3^11, Schur-Euler det check, BFS group order 864 on O_27 x X_0(Z/4Z)_smooth + bipartite Schur Danilevsky over disjoint 1,060-bit and 62-bit primes on mod 216/135/189, mod-16 identity + k = 37 leaf, wider [-30..|k|]^2 + D1 k = -8/-4/-2 check on 15 Hasse leaves, and Krylov Jacobi tridiagonalization on O_81 certifying 1/324 top and 1/108 graphene LDOS, discrepancies_count == 0, agrees)
- already on main?: topic-sweep /B201[1-4]|M19|M20|G_135|G_189|k = 5 mod 8|15 leaves|S_k/ on main (18c1b8ac2): B2011/M19 checks C60 through mod 6,561 while noting S_k single-orbit and Schur-Euler assembly were unchecked on main; B2012/B2013 leave open B2012 Open #1 (why halving fails at 27*5 and 27*7 yet survives the 2-part without character tables), B2012 Open #2 & Review 87 C7 (what invariant separates the two 2-adic halves on k == 5 mod 8), and B2012 Open #3 (reduction-theory proof that the 15 Hasse leaves have no Z^3 point); B2014/M20 verifies C61 S1-S4
- what would make it fail: Controls 1-5 & RPF1-5 — exponent 2 * 3^{k-3} moves (3,3,3) mod 9 to x = 6; L^2 fixes 0 points on O_8 (and O_27) while 27 * p fails halving on all 60 primes 5 <= p < 300 and leaves 10 (mod 135) and 8 (mod 189) unpaired roots; k = 1 splits into (18,18,6,6) at mod 8 while dropping -v_1 v_2 / 2 breaks eta_2; k = -2 has (3,3,4) and k = 54 has (-3,-3,-3) while 9 seeds scrambled past 5,000 bits descend inside [-B_max, B_max]^3 (0 false empties on [-500, 500] \ {0, 4}); off-vortex (3,3,6) has charged LDOS 2/3 != 0 while exceptions carry 4 / n_k

## Claim (summary, plain words and exact integers/rationals/polynomials, `0 of 19`, `AGY-C63` remediating unpushed `AGY-C62` `D1`–`D5`)

1. **`E1` — Constructive All-`k` Single-Orbit Proof `S_k = O_{3^k}` & Line-by-Line Schur–Euler Assembly (`Closing M19 /
   B2011 #3`):** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts linearly on `[x, z]^T` by `M_3 = [[0, 1], [-1, 3]]`
   (`and L(3, y, z) acts on [y, z]^T by M_3`), satisfying `M_3^4 = I_2 + 3 B` with `B = [[-3, 7], [-7, 18]]` and
   `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`. Because `v_3(binom(3^{k-3}, j) * 3^{j+1}) >= k` for every `j >= 2`, setting
   `e_k = 4 * 3^{k-3}` gives `R^{c_1 e_k}(3, 3, 3) == (x_1, 3, z_1) = (3 + c_1 3^{k-1}, 3, 3 - c_1 3^{k-1}) mod 3^k` for
   **every `k >= 3`**. Subsequent application of `L^{c_2 e_k}` acts via `M_{x_1} = M_3 + c_1 3^{k-1} E_{22}` on `v_1 = [3,
   z_1]^T == [0, 0]^T mod 3`: every `j >= 1` perturbation term is divisible by `3^{k-1} * 3 = 3^k`, and `(M_3^{c_2 e_k} -
   I_2) == 0 mod 3` annihilates `-c_1 3^{k-1}[0, 1]^T mod 3^k`, so `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)` (`c_1, c_2 in {0, 1,
   2}`) hits all `9` Hensel fiber lifts above `(3, 3, 3) mod 3^{k-1}` (`verified through mod 59,049 = 3^{10}` in producer
   and `mod 177,147 = 3^{11}` in countercheck). By `<L, R>`-equivariance from base `k = 3`, **`S_k = O_{3^k}` is one
   `<L, R>`-orbit of size `8 * 3^{2k-4}` for every `k >= 3`**. Symbolically and numerically, for bipartite `B_q = [[0, A_q],
   [A_q^H, 0]]` with `d_+^{(0)} - d_-^{(0)} = +2`, `d_+^{(1)} - d_-^{(1)} = -1`, `d_{neu} = d_{chg} + 3`, and
   `spec(A_0^H A_0) = {36} U (4 spec(A_1^H A_1) \ {0})`, `det(x I - B_q) = x^{d_+ - d_-} det(x^2 I - A_q^H A_q)` assembles
   identically to `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)`.

2. **`E2` — `1`-Jet `X_0(Z/4Z)_smooth` All-`(k, m)` Mixed `3^k * 2^m` Halving Proof vs Odd-Prime `27 * p` Failure (`Closing
   B2012 Open #1`):**
   - **All-`(k, m)` CRT Decoupling & `1`-Jet Fixed-Point Proof (`k >= 3, m >= 1`):** `M_3^3 = I_2 + 4 K` with `K = [[-1, 2],
     [-2, 5]] == I_2 mod 2` yields `M_3^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m` (`m >= 3`). From base `|O_{432}| = 4,608
     = 72 * 64`, decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and `E_2(k, m) = 3^{k-2} * 2^{m-3}` (`m >= 5`, a
     multiple of `6` so `sum_{j=0}^{N-1} M_3^j E_{22} M_3^{N-1-j}` contains an even number of identical period-`3` blocks `==
     0 mod 2` while `M_3^N == I_2 mod 2` fixes `c_1 2^{m-1}[0, 1]^T mod 2^m`) prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}`
     (`and |O_{2^m}| = 4^{m-1} for m >= 2`). For any `g` with `chi_C(g) != 1`: when `|Fix_{O_{27}}(g)| == 0` (`e.g. L^2,
     which fixes 0 points on O_8 and O_{27}`), `|Fix_{O_{3^k}}(g)| == 0` so `|Fix_{O_{3^k * 2^m}}(g)| == 0` automatically;
     when `|Fix_{O_{27}}(g)| > 0`, all `48` such elements of `G_{27}` (`order 216`) are conjugate to `C^{+-1}`, and on the
     `1`-jet bundle `O_{27} x X_0(Z/4Z)_{smooth}` (`16` smooth mod-`4` points), `|G| == 864 == 4 * 216`, `|K_{mod 4}| == 4`,
     and all `8` elements of `K_{mod 4} * C^{+-1}` fix a unique `v_2 in O_4` (`and O_2`) and fix only `v_2` in its `4`-point
     mod-`4` tangent fiber (`certifying det(Dg|_{V_{v_2}(F_2)} - I_2) == 1 mod 2`), lifting uniquely to `1` fixed point in
     `O_{2^m}` for **every `m >= 3`** — proving **exact `Z[x]` halving for all `k >= 3, m >= 1`** and certified over `Z[x]` at
     `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts, `383` of `383` paired)**.
   - **Odd-Prime `27 * p` Failure (`0` Character Tables):** `(L R)^3 in ker(PSL(2, Z) ->> G_{27})`, while across **all `60`
     odd primes `5 <= p < 300`** (`scoped explicitly per Review 87`), `(L R)^{3 m}` (`m <= 3`) breaks `|Fix_{O_p}((L R)^{3 m}
     C)| = 1` (`Fix = 2 at p = 5; Fix = 0 at p = 7`). Since `W_6 ~= M_0 (+) M_1 (+) conj(M_1)` gives `P_{W_6}(x) = P_{M_0}(x)
     P_{M_1}(x)^2 in Z[x]`, monic `P_{2 M_1}(y) in Z[y]` (`y = 2 x`) yields exact Gauss-Lemma `Z[y]` unpaired polynomials
     **`(y^2 - 4 y - 8)(y^2 + 4 y - 8)(y^3 - 12 y - 8)(y^3 - 12 y + 8)`** (`10` unpaired of `959` at `mod 135 = 27 * 5`, `n =
     2,880`) and **`(y^2 - 2 y - 16)(y^2 + 2 y - 16)(y^2 - 2 y - 4)(y^2 + 2 y - 4)`** (`8` unpaired of `671` at `mod 189 =
     27 * 7`, `n = 2,016`, roots `x = (+-1 +- sqrt(5))/2` and `(+-1 +- sqrt(17))/2`).

3. **`E3` — Exact `2`-Adic Hensel Bit, `50/50` Involution, & Scoped Transitivity (`Closing B2012 Open #2 & Review 87 C7`):**
   On `F(x, y, z) == 5 mod 8`, one odd coordinate `u` and two even `v_1, v_2` force `grad F == (0, 0, 0) mod 2`,
   `(u - v_1 v_2 / 2)^2 == F - 4 mod 16` (`checked on all 1,152 solutions in (Z/16Z)^3`), and `F(u + 2^{m-1}, v_1, v_2) -
   F(u, v_1, v_2) == 2^m mod 2^{m+1}` (`m >= 3`). Thus **for every `k == 5 mod 8` and every `m >= 3`**, **`beta_m(v) :=
   ((F(v) - k) / 2^m) mod 2 in {0, 1}`** is well-defined on `(Z/2^m Z)^3` and `<L, R, C, tau>`-invariant, the involution
   `u -> u + 2^{m-1}` bijectively swaps `beta_m = 0 <-> 1` (`exact 50/50 split`), and `beta_m = 1` has `0` lifts to `2^{m+1}`
   (`with mod-8 base given by Kronecker spin eta_2(v) = (2 / (u - v_1 v_2 / 2)) in {-1, +1}`). Per Review `87` `E22`,
   single-orbit `<L, R>`-transitivity of each `9 * 2^{2m-3}` half is verified exhaustively across **all `30` residue classes
   of `k == 5 mod 8 mod 2^{m+1}` for `3 <= m <= 6`** (`covering every integer k == 5 mod 8 at mod 8, 16, 32, 64`) plus `k in
   {5, 13, 29}` at `m = 7` (`mod 128`, `36,864` pts).

4. **`E4` — Hurwitz–Markoff `<s_1, s_2, s_3, S_3, V_4>` Mordell Proof on All `15` Hasse Leaves Over `Z^3` (`Closing B2012
   Open #3`):** Minimizing `|x| + |y| + |z|` over `<s_1, s_2, s_3, S_3, V_4>`: when `x y z > 0`, Klein-four double sign
   flips `V_4` reduce `(-a, -b, +c) -> (+a, +b, +c)` (`3 <= a <= b <= z <= a b / 2`), where concavity `z(a b - z) >= b(a b -
   b)` bounds `a^2 (a - 3) <= -k` for all `k <= -1` (`giving B_max(-8) = 6, B_max(-4) = 4, and B_max <= 12 for k >= -54`,
   verified with `0` false empties across all `999` leaves in `[-500, 500] \ {0, 4}`); when `x y z < 0`, flipping the two
   positive signs of `(+r, +s, -t)` gives `(-r, -s, -t)` with `k = r^2 + s^2 + t^2 + r s t > max(r, s, t)^2`; `|x| <= 1`
   reduces to `y^2 +- y z + z^2 = k - x^2` (`<= 13`); and `|x| = 2` requires `k - 4 = square`. Exhaustive search on
   `[-B_max(k), B_max(k)]^3` (`max B_max = 13`) proves **zero integer points over all `Z^3`** on all `15` leaves `[-54, -47,
   -44, -38, -26, -19, -18, -14, -8, -4, 46, 56, 86, 124, 126]`.

5. **`E5` — Wavefunction Listening Blind Spot: Explicit Operator-Pulled-Back Vortex Zero vs Neutral Bulk Completeness:**
   Direct `n_k`-dimensional operator evaluation (`zero literal flags`) on `O_{3^k}` (`n_k = 8 * 3^{2k-4}`) certifies
   `||(Pi_1 + Pi_2) delta_{f_i}||^2 == 0/1` on all `3` `C`-fixed points (`100%` charged vortex zero) and verifies on
   explicitly pulled-back `v_{+6}^{(k)}, v_{-6}^{(k)}, v_{2 x psi_0}^{(k)}` (`with ||P_{2 x psi_0} delta_{(3,3,3)}||^2 ==
   1/36` over `Q(omega)` at `mod 27`) that `W_6` acts by `+6, -6, 0` with summed `(3, 3, 3)` LDOS `(1 + 1 + 2) / n_k = 4 /
   n_k`, forcing **`1 - 4 / n_k -> 1`** (`17/18`, `161/162`, `1457/1458` at `mod 27, 81, 243`) into paired neutral bulk modes
   (`graphene slow-decay mode carrying exact LDOS 1/12 at mod 27 [< 10^{-35}] and 1/108 at mod 81 [< 10^{-30}]`).

0 of 19.
