# CLAIM CARD — Exact B2017 rational census closure and mod-81 off-cusp halving orbits, B2016 subgroup-lattice and rho-intertwining theorems, B2015 float-free mod-243 new-fiber minimal polynomial, and maximal honeycomb-abelian quotient law (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, d8222d54b2ee6713f2ca7f33a73d9c216b8d9579
- kind: theorem
- touches: A01, A03, P-374, P-630, P-882
- effect: conditions — A01, A03, P-374, P-630, and P-882 (eliminates all 41 non-exact or left-out orbits of B2017 over Q
  and censuses all 489 orbits across all 531,441 mod-81 residues finding 18 halving orbits including 15 off the cusp leaf
  k = 0 on k in {9, 27, 36, 54, 63}; proves H <= ker(rho) <=> Category (a') and [<C>, M_6] <=> Category (a) with 0 strict
  (b) across all 45 G_3 and 100 G_4 subgroup classes; certifies the irreducible degree-36 Z[x] minimal polynomial and
  closed-walk ceiling Delta_64 < 35^32 at mod 243; and proves M_ab = ord_{O_ab}(L^2) / 2 = {3, 9, 9, 5, 25, 7} across the
  six computed cusp-cone levels with exact Z[u] division at mod 625)
- scope: frame: no frame (unweighted 6-move weave operator W_6 on finite Markoff orbits and G_k coset spaces); object: all
  <L, R>-orbits on (Z/NZ)^3 for N in {9, 27, 49, 81}, all subgroup conjugacy classes of G_3 and G_4, the mod-243 covering
  fiber over mod 81, and the six cusp-cone orbits N in {27, 81, 243, 125, 625, 343}; reach: class; hypotheses: exact
  integer and rational arithmetic over Z and Z[omega] scoped to the stated finite levels where not all-group
- identifications: none
- definitions: On (Z/NZ)^3, F(x, y, z) = x^2 + y^2 + z^2 - x y z mod N is preserved by L(x, y, z) = (x, z, x z - y),
  R(x, y, z) = (z, y, y z - x), C = R^-1 L : (x, y, z) -> (y, z, x), and sigma = R L^-1 R : (x, y, z) -> (y, x, x y - z).
  On any finite <L, R>-orbit X or coset space G/H of G = <C, sigma>, W_6 = sum_{j=0}^2 C^j (L + R) C^-j commutes with C
  and splits l^2(X) into C-neutral H_0 (dim d_0) and C-charged H_1 (+) H_2 (dim d_1 each, d_0 - d_1 = |Fix(C)|) with monic
  p_neu(x) = det(x I - W_6|_{H_0}) in Z[x], S(x) = det(x I - W_6|_{H_1}) in Z[x] when H_1 ~= H_2, and
  h(x) = 2^{-d_0} p_neu(2 x). Category (a) means H_1 ~= H_2 and h(x) = x(x^2 - 9) S(x) in Z[x], Category (a') means
  H_1 ~= H_2 and h(x) = S(x) in Z[x] (|Fix(C)| = 0), strict (b) means H_1 ~= H_2 with neither (a) nor (a'), and (c) means
  H_1 !~= H_2 or S(x) does not divide h(x). On G_k = Im(PSL(2, Z) -> Sym(O_{3^k})) where O_N is the <L, R>-orbit of
  (3, 3, 3) mod N, rho : G_k -> mu_6 satisfies rho(C) = omega, rho(sigma) = -1, and M_6 is the unique index-6
  <C>-overgroup class. At mod 243, S_N = (W_6|_{H_0})^2 / 4, v = (x / 2)^2,
  g_new(v) = v^18 - 63 v^17 + 1809 v^16 - 31359 v^15 + 366453 v^14 - 3053187 v^13 + 18711432 v^12 - 85809456 v^11
  + 296843940 v^10 - 775628381 v^9 + 1524253446 v^8 - 2231533503 v^7 + 2396964081 v^6 - 1846648809 v^5 + 986438304 v^4
  - 346325130 v^3 + 72709677 v^2 - 7444224 v + 180361, Delta_64 = tr(S_243^32) - tr(S_81^32), and
  K = <<[C^-1, sigma]^3>>_{G_5}. On any cusp-cone orbit O_N, O_{N,ab} = O_N / <<[L^2, R^2]>> and
  M_ab = ord_{O_{N,ab}}(L^2) / 2, with universal honeycomb torus gap
  6 - 2 sqrt(5 + 4 cos(pi / M)) = (2 / 3) pi^2 M^{-2} - (1 / 54) pi^4 M^{-4} + O(M^{-6}).
- imports: none
- premises on main: B2002, B2004, B2006, B2009, B2011, B2013, B2014, B2015, B2016, B2017, P-374, P-630, P-882
- decisive script: relays/agy_2026-11-26_c64/c64_b2017_mod81_census_b2016_subgroups_mod243_ceiling_and_cusp_producer.py,
  SHA-256 a3bdd98d0ed5b5d6, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-26_c64/c64_b2017_mod81_census_b2016_subgroups_mod243_ceiling_and_cusp_producer.py,
  output SHA-256 564e51251bd96b75
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 f82d52fb76de8f1e
- failing control: python3 relays/agy_2026-11-26_c64/c64_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-26_c64/c64_countercheck_v2.py
  (SHA-256 df0c2479de7afc05, output SHA-256 dc862c9f7f2bfa36, zero shared imports, remediating non-monic resultant
  content -8 at M = 7 from v1 79c21686f, agrees with 0 discrepancies)
- already on main?: topic_sweep.py "B2015|B2016|B2017|mod 81|mod 243|M_ab" on origin/main (a3494f066): closest arcs B2015
  (R1 mod-3-primes at mod 625 and R2 double-precision ceiling at mod 243), B2016 (coset row (b) conflating Category (a')
  with non-halving), and B2017 (41 non-exact or left-out orbits at mod 27 and mod 49, and mod-81 census unrun)
- what would make it fail: replacing 9 with 4 in x(x^2 - 9) moves (3, 3, 3) mod 27 and all 6 mod-81 Category-(a) orbits
  into (b) so c64_control.py exits 1, or any off-cusp mod-81 halving orbit failing Z[x] division, or any G_3/G_4 subgroup
  violating H <= ker(rho) <=> (a') or [<C>, M_6] <=> (a), or Delta_64 >= 35^32 at mod 243
