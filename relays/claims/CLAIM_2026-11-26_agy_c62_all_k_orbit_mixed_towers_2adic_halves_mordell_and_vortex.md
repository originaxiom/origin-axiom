# CLAIM CARD — Constructive all-k single-orbit proof S_k = O_{3^k} & Schur–Euler assembly (M19 / B2011 #3), all-(k, m) 3^k * 2^m halving proof vs odd-prime 27 * p failure (B2012 Open #1), exact 2-adic Hensel & Kronecker separator for k == 5 mod 8 (B2012 Open #2 & Review 87 C7), Mordell 15-leaf Z^3 proof (B2012 Open #3), and all-3^k vortex vs bulk LDOS (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, 1898d48a6
- kind: theorem
- touches: A01, A03, P-374, P-630, P-882
- effect: conditions — A01, A03, P-374, P-630, and P-882 (proves S_k = O_{3^k} for all k >= 3 via R^{4 * 3^{k-3}}, L^{4 * 3^{k-3}} and certifies Schur-Euler assembly; proves exact Z[x] halving at 3^k * 2^m for all k >= 3, m >= 1 including mod 216 while refuting 27 * p across all 60 primes 5 <= p < 300 with exact Z[y] unpaired polynomials at mod 135 and 189; proves beta_m = ((F - k) / 2^m) mod 2 separates the two halves for all k == 5 mod 8, m >= 3; proves zero Z^3 points on all 15 Hasse leaves via B_max <= 13; and proves LDOS_chg(Fix(C)) = 0 with 1 - 4 / n_k -> 1 in paired neutral bulk)
- imports: none (pure 2x2 matrix p-adic valuation induction, finite-group stabilizer and CRT orbit decoupling without character tables, 2-adic Hensel-obstruction and Kronecker-spin congruences, Mordell / Ghosh-Sarnak L^1-descent over Z^3, and S_3 x Z_3 spectral LDOS decomposition; zero Standard Model pass/fail cells; order-30 line kept on hold per M18; strictly 0 of 19)
- premises on main: B1983, B1991, B1992, B1994, B1995, B1999, B2002, B2003, B2008, B2009, B2010, B2011, B2012, B2013, B2014, P-374, P-630, P-882
- decisive script: relays/agy_2026-11-26_c62/c62_all_k_orbit_mixed_2adic_mordell_and_vortex_producer.py, SHA-256 2e3cc888f91c5a05, depends on only the standard library, sympy, and mpmath, run as `python3 -I relays/agy_2026-11-26_c62/c62_all_k_orbit_mixed_2adic_mordell_and_vortex_producer.py`, output SHA-256 e9c0659983c8036e (c62_out.json)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-26_c62/c62_countercheck.py (pre-committed @ 3daf91e33, SHA-256 d29af5e25ea219c7, output @ 1898d48a6 SHA-256 97611134995c57a5, Chebyshev doubling through 3^11, 8x8/5x5 Schur-Euler det check, union-find + bipartite Schur Danilevsky over disjoint 1,060-bit and 62-bit primes on mod 216/135/189, symbolic mod-16 identity + k = 37 leaf, wider [-30..|k|]^2 check on 15 Hasse leaves, and Krylov Jacobi tridiagonalization on O_81 certifying 1/324 top and 1/108 graphene LDOS, discrepancies_count == 0, agrees)
- already on main?: topic-sweep /B201[1-4]|M19|M20|G_135|G_189|k = 5 mod 8|15 leaves|S_k/ on main (18c1b8ac2): B2011/M19 checks C60 through mod 6,561 while noting S_k single-orbit and Schur-Euler assembly were unchecked on main; B2012/B2013 leave open B2012 Open #1 (why halving fails at 27*5 and 27*7 yet survives the 2-part without character tables), B2012 Open #2 & Review 87 C7 (what invariant separates the two 2-adic halves on k == 5 mod 8), and B2012 Open #3 (reduction-theory proof that the 15 Hasse leaves have no Z^3 point); B2014/M20 verifies C61 S1-S4
- what would make it fail: Controls 1-5 & RPF1-5 — exponent 2 * 3^{k-3} or 3^{k-3} moves (3,3,3) mod 9 to x = 6; asserting 27 * p preserves halving fails on all 60 primes 5 <= p < 300 and leaves 10 (mod 135) and 8 (mod 189) unpaired roots; k = 1 (!= 5 mod 8) splits into (18,18,6,6) at mod 8 while dropping -v_1 v_2 / 2 breaks eta_2; neighbor k = 54 has point (-3,-3,-3) while 6 solvable leaves scrambled past 3,400 digits descend inside [-B_max, B_max]^3; off-vortex (3,3,6) has charged LDOS 2/3 != 0 while unpaired exceptions carry only 4 / n_k (1/162 < 1% at mod 81)

## Claim (summary, plain words and exact integers/rationals/polynomials, `0 of 19`)

1. **`E1` — Constructive All-`k` Single-Orbit Proof `S_k = O_{3^k}` & Line-by-Line Schur–Euler Assembly (`Closing M19 /
   B2011 #3`):** Along `y = 3`, `R(x, 3, z) = (z, 3, 3 z - x)` acts linearly on `[x, z]^T` by `M = [[0, 1], [-1, 3]]` (`and
   L(3, y, z) acts on [y, z]^T by the identical matrix M`), satisfying `M^4 = I_2 + 3 B` with `B = [[-3, 7], [-7, 18]]` and
   `B [1, 1]^T = [4, 11]^T == [1, -1]^T mod 3`. Because `v_3(binom(3^{k-3}, j) * 3^{j+1}) >= k` for every `j >= 2`, setting
   `e_k = 4 * 3^{k-3}` gives `R^{e_k}(3, 3, 3) == (3, 3, 3) + 3^{k-1}(1, 0, -1) mod 3^k` and `L^{e_k}(3, 3, 3) == (3, 3, 3)
   + 3^{k-1}(0, 1, -1) mod 3^k` for **every `k >= 3`**, so `L^{c_2 e_k} R^{c_1 e_k}(3, 3, 3)` (`c_1, c_2 in {0, 1, 2}`) hits
   all `9` Hensel fiber lifts above `(3, 3, 3) mod 3^{k-1}` (`explicitly verified through mod 59,049 = 3^{10}` in producer
   and `mod 177,147 = 3^{11}` via Chebyshev doubling in countercheck). By `<L, R>`-equivariance from base `k = 3`, **`S_k =
   O_{3^k}` is a single `<L, R>`-orbit of size `8 * 3^{2k-4}` for every `k >= 3`**. Symbolically and numerically, for
   bipartite `B_q = [[0, A_q], [A_q^H, 0]]` with `d_+^{(0)} - d_-^{(0)} = +2`, `d_+^{(1)} - d_-^{(1)} = -1`, `d_{neu} =
   d_{chg} + 3`, and `spec(A_0^H A_0) = {36} U (4 spec(A_1^H A_1) \ {0})`, `det(x I - B_q) = x^{d_+ - d_-} det(x^2 I -
   A_q^H A_q)` assembles identically to `p_{neu}(2 y) == 2^{d_{neu}} y (y^2 - 9) S(y)`.

2. **`E2` — All-`(k, m)` Mixed `3^k * 2^m` Halving Survival vs Odd-Prime `27 * p` Failure Without Character Tables (`Closing
   B2012 Open #1`):**
   - **All-`(k, m)` `2`-Tower Survival (`k >= 3, m >= 1`):** `G(O_2) ~= A_4` (`order 12`) has abelianization `A_4 / V_4 ~=
     Z_3` equal to `chi_C`, so every `g` with `chi_C(g) != 1` acts as a `3`-cycle fixing `1` of the `4` points on `O_2` and
     `O_4`; for `m >= 3`, `det(C - I|_{V_0(F_2)}) == 1 mod 2` lifts that fixed point uniquely to `O_{2^m}`. Simultaneously,
     `M^3 = I_2 + 4 K` with `K = [[-1, 2], [-2, 5]] == I_2 mod 2` yields `M^{3 * 2^{m-3}} == I_2 + 2^{m-1} I_2 mod 2^m`
     (`m >= 3`). From base `|O_{432}| = 4,608 = 72 * 64`, decoupled exponents `E_3(k) = 16 * 3^{k-3}` (`k >= 4`) and
     `E_2(k, m) = 3^{k-2} * 2^{m-3}` (`m >= 5`) prove `O_{3^k * 2^m} = O_{3^k} x O_{2^m}`, forcing `|Fix_{O_{3^k * 2^m}}(g)|
     == |Fix_{O_{27}}(g)|` for all `chi_C(g) != 1` and **exact `Z[x]` halving for every `k >= 3, m >= 1`** — certified over
     `Z[x]` at `mod 54`, `mod 108`, and newly opened **`mod 216 = 27 * 8` (`1,152` pts, `d_{neu} = 386, d_{chg} = 383`, where
     `O_8` opens from `4` to `16` points)**.
   - **Odd-Prime `27 * p` Failure (`0` Character Tables):** `(L R)^3` lies in `ker(PSL(2, Z) ->> G_{27})`, while across **all
     `60` odd primes `5 <= p < 300`** (`scoped explicitly per Review 87`), a power `(L R)^{3 m}` (`m <= 3`) breaks
     `|Fix_{O_p}((L R)^{3 m} C)| = 1` (`e.g. Fix = 2 at p = 5, 11, 17, 83, 293; Fix = 0 at p = 7, 13; Fix = 4 at p = 193`),
     violating `B2009`'s stabilizer condition on `G_{27 p}`. By Gauss's Lemma in `y = 2 x`, exact unpaired charged polynomials
     in `Z[y]` are **`(y^2 - 4 y - 8)(y^2 + 4 y - 8)(y^3 - 12 y - 8)(y^3 - 12 y + 8)`** (`10` unpaired of `959` at `mod 135 =
     27 * 5`, `n = 2,880`) and **`(y^2 - 2 y - 16)(y^2 + 2 y - 16)(y^2 - 2 y - 4)(y^2 + 2 y - 4)`** (`8` unpaired of `671` at
     `mod 189 = 27 * 7`, `n = 2,016`, roots `x = (+-1 +- sqrt(5))/2` and `(+-1 +- sqrt(17))/2`).

3. **`E3` — Exact `2`-Adic Hensel-Obstruction Bit & Mod-`8` Kronecker Spin (`Closing B2012 Open #2 & Unscoping Review 87
   C7`):** Whenever `F(x, y, z) == 5 mod 8`, `(x, y, z)` has one odd coordinate `u` and two even coordinates `v_1, v_2`,
   forcing `grad F == (0, 0, 0) mod 2` and the exact congruence `(u - v_1 v_2 / 2)^2 == F(x, y, z) - 4 mod 16` (`checked on
   all 1,152 solutions in (Z/16Z)^3`). Because `grad F == 0 mod 2`, `F(v + 2^m d) == F(v) mod 2^{m+1}`, so **for every `k ==
   5 mod 8` and every `m >= 3`**, the `2`-adic Hensel-obstruction bit **`beta_m(v) := ((F(v) - k) / 2^m) mod 2 in {0, 1}`** is
   well-defined on `(Z/2^m Z)^3` and `<L, R, C, tau>`-invariant, separating the two equal-size transitive `<L, R>`-halves of
   size `9 * 2^{2m-3}` (`verified across m = 3..7, mod 8 through mod 128 = 36,864 pts, and unsearched k = 37 in countercheck`).
   At base `m = 3` (`mod 8`), the two `72`-point halves carry opposite Kronecker spin `eta_2(v) = (2 / (u - v_1 v_2 / 2)) in
   {-1, +1}`; for `m >= 4`, `beta_{m-1} = 1` dies (`0` lifts to `2^m`), while `beta_{m-1} = 0` (`with fixed spin eta_2`) splits
   into `beta_m = 0` and `beta_m = 1` — leaving a single projective-limit `2`-adic orbit in `X_k(Z_2)`.

4. **`E4` — Rigorous Mordell / Ghosh–Sarnak `L^1`-Descent Proof on All `15` Hasse-Violating Leaves Over `Z^3` (`Closing B2012
   Open #3`):** For any integer solution `(x, y, z) in Z^3` minimal under `|x| + |y| + |z|` along its Vieta `<L, R>`-orbit:
   when `x y z > 0` (`3 <= a <= b <= z <= a b / 2`), concavity `z(a b - z) >= b(a b - b)` bounds `a^2 (a - 3) <= -k` (`giving
   a <= 4 and z <= B_max(k) <= 12` for `k >= -54`); when `x y z < 0`, flipping two negative signs reduces to `(-r, -s, -t)`
   with `k >= 3 u^2 + u^3 > 0` (`u <= 4` for `k <= 126`); `|x| <= 1` reduces to positive-definite `y^2 +- y z + z^2 = k - x^2`
   (`max <= sqrt(4(k - 1)/3) + 1 <= 13`); and `|x| = 2` requires `k - 4 = (y - z)^2` (`none of the 15 leaves has k - 4 =
   square`). Exhaustive check on `[-B_max(k), B_max(k)]^3` (`max B_max = 13`) proves **zero integer points over all `Z^3`** on
   all `15` locally solvable leaves `[-54, -47, -44, -38, -26, -19, -18, -14, -8, -4, 46, 56, 86, 124, 126]`.

5. **`E5` — Wavefunction Listening Blind Spot: All-`3^k` Topological Vortex Zero vs Neutral Bulk Completeness:** For every
   `k >= 3` (`n_k = 8 * 3^{2k-4}`), `Pi_1 + Pi_2` annihilates `delta_v` on all `3` `C`-fixed points (`100%` of charged
   eigenvectors vanish identically on `Fix(C)`), whereas on `(3, 3, 3)` the `3` unpaired `S_3 x Z_3` neutral modes (`+6`,
   `-6`, and `2 x psi_0` null mode, certified over `Q(omega)` with `||P_{2 x psi_0} delta_{(3,3,3)}||^2 == 1/36` at `mod 27`)
   carry exact total LDOS `(1 + 1 + 2) / n_k = 4 / n_k`, forcing **`1 - 4 / n_k -> 1`** (`17/18` at `mod 27`, `161/162` at
   `mod 81`, `1457/1458` at `mod 243`) of `delta_{(3,3,3)}` into paired neutral bulk modes (`with graphene slow-decay mode
   carrying exact LDOS 1/12 at mod 27 [< 10^{-35}] and 1/108 at mod 81 [< 10^{-30}]`).

0 of 19.
