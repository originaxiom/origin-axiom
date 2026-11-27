# CLAIM CARD — Two-counts all-prime P^1(F_p) classification, unique p = 5 parabolic (3, 3, 3) systole split and Leg(5) golden walk, diagonal O_27 x Fiber_p bundles, and PF5 sixth-order systole selection (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, 20e72c3782e02f90dfb24dcfbfa2adff16faeec3
- kind: theorem
- touches: A01, A03, P-374, P-630, P-845, P-882
- effect: conditions — A01, A03, P-374, P-630, P-845, and P-882 (proves p = 5 is the unique prime where P^1(F_p) \ T_cusp
  forms a single C_omega-triplet T_sys and the unique prime where (3, 3, 3)'s three systoles become parabolic mod p fixing
  T_sys with W_{6,tr} Jacobian (14, 5, 5); proves 100% mirror charged pairing on (Z/pZ)^2 \ {(0, 0)} for all p and certifies
  across p in {2..23} that p = 5 is the unique prime where ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I) vanishes on P^1(F_p)
  and emerges in quadratic Leg(5); classifies diagonal O_27 x Fiber_p bundles across p in {2, 3, 5, 7} isolating unpaired
  (y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2 on O_27 x Leg(5); and proves W_sys / W_cusp = phi^2, quartic I_4 = 3/10 equator
  degeneracy, and sixth-order I_6 = 1/9 + cos(6 theta)/90 selection of the 3-element mirror-even systole orbit on E_{phi^2})
- scope: frame: no frame (foundational two-counts updates L, R on (Z/pZ)^2 \ {(0, 0)} and diagonal SL(2, Z) action with
  O_27); object: P^1(F_p), Rays(p), and Vecs(p) across primes p >= 2 (explicitly p in {2, 3, 5, 7, 11, 13, 17, 19, 23}),
  diagonal bundles O_27 x Fiber_p for p in {2, 3, 5, 7}, and the 2-dim golden eigenspace E_{phi^2} of Leg(5); reach: class;
  hypotheses: exact integer, rational, and algebraic-number arithmetic scoped to the stated prime sets where not all-prime
- identifications: none
- definitions: On Z^2, L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]], C_omega = L R^-1 = [[0, 1], [-1, 1]] (C_omega^3 = -I_2),
  order-3 charge generator C_{3,omega} = -C_omega = C_omega^4 = [[0, -1], [1, -1]], and mirror tau = [[0, 1], [1, 0]]. For
  prime p, Vecs(p) = F_p^2 \ {(0, 0)} (size p^2 - 1), Rays(p) = Vecs(p) / {+-1}, and P^1(F_p) = Vecs(p) / F_p^x (size p + 1,
  reps [1 : 0], [0 : 1], and [1 : b] for 1 <= b < p). Cusp shears P_1 = L, P_2 = C_omega L C_omega^-1 = R^-1, and P_3 =
  C_omega^2 L C_omega^-2 = [[2, -1], [1, 0]] fix T_cusp = {[1 : 0], [0 : 1], [1 : 1]}, leaving R_p = P^1(F_p) \ T_cusp;
  (3, 3, 3) systoles U_1 = L R = [[2, 1], [1, 1]], U_2 = C_omega U_1 C_omega^-1 = [[2, -1], [-1, 1]], and U_3 = C_omega^2
  U_1 C_omega^-2 = [[0, 1], [-1, 3]] are parabolic mod p iff U_i != +-I_2 mod p and (U_i + I_2)^2 == 0 or (U_i - I_2)^2 == 0
  mod p. On A^3, L_tr(x, y, z) = (x, z, x z - y), R_tr(x, y, z) = (z, y, y z - x), C_tr = R_tr^-1 o L_tr : (x, y, z) ->
  (y, z, x), and W_{6,tr} = sum_{j=0}^2 C_tr^j (L_tr + R_tr) C_tr^-j. On Vecs(p), Rays(p), and P^1(F_p), W_{6,omega} =
  sum_{j=0}^2 C_omega^j (L + R) C_omega^-j commutes with C_{3,omega}, giving monic P_neu(x) = det(x I - W_{6,omega}|_{H_0})
  and P_chg(x) = det(x I - W_{6,omega}|_{H_1}) = det(x I - W_{6,omega}|_{H_2}) in Z[x] (via tau); at p = 5, Leg(5) is the
  6-dim quadratic-character block on Rays(5) spanned by e_i = (|r_i^+> - |r_i^->) / sqrt(2) over lines ([1:0], [0:1], [1:1],
  [1:2], [1:3], [1:4]) where r_i^- = 2 r_i^+ mod 5 ((2 / 5) = -1, (-1 / 5) = +1). On O_27 (<L_tr, R_tr>-orbit of (3, 3, 3)
  mod 27, 72 pts) times Fiber_p, C_0 = R^-1 L = L^-1 C_omega L, S = L R^-1 L (S^2 = -I_2), order-3 g_{C_3} = S^2 R^-1 L
  acts as (C_tr, -C_0), W_{6,diag} = sum_{j=0}^2 g_{C_3}^j (L_diag + R_diag) g_{C_3}^-j, y = 2 x, P_neu(y) = det(y I -
  W_{6,diag}|_{H_0}), P_{2,chg}(y) = 2^{d_1} det((y / 2) I - W_{6,diag}|_{H_1}) in Z[y], halved degree is deg gcd_{Z[y]}(
  P_neu(y), P_{2,chg}(y)), monic unpaired polynomial is P_{2,chg}(y) / gcd(P_neu(y), P_{2,chg}(y)) in Z[y], Category (a) is
  d_0 - d_1 = 3 with P_neu(y) = y(y^2 - 36) P_{2,chg}(y), Category (a') is d_0 = d_1 > 0 with P_neu(y) = P_{2,chg}(y), and
  the odd-parity spinor sector of O_27 x Vecs(5) is {f(v, -u) = -f(v, u)} (dim 864, d_0 = d_1 = 288). On E_{phi^2} =
  ker(W_{6,omega}|_{Leg(5)} - ((3 + sqrt(5)) / 2) I_6) with orthonormal tau-eigenbasis (e_+, e_-) (T_leg e_+ = +e_+ peaked
  on [1:4] at theta = 0, T_leg e_- = -e_-), psi(theta) = cos(theta) e_+ + sin(theta) e_-, chiral poles psi_{q=1,2} =
  (e_+ +- i e_-) / sqrt(2), line weights p_i(psi) = |psi_i|^2, W_cusp = p_1 + p_2 + p_3, W_sys = p_4 + p_5 + p_6,
  I_4(psi) = sum_{i=1}^6 p_i(psi)^2, and I_6(psi) = sum_{i=1}^6 p_i(psi)^3.
- imports: none
- premises on main: B1983, B1989, B1993, B1994, B1995, B1998, B2000, B2002, B2004, B2009, B2011, B2012, B2013, B2014,
  B2017, P-374, P-630, P-845, P-882
- decisive script: relays/agy_2026-11-27_c65/c65_two_counts_prime5_parabolic_systoles_and_diagonal_bundle_producer.py,
  SHA-256 576d5f38b4455e52, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-27_c65/c65_two_counts_prime5_parabolic_systoles_and_diagonal_bundle_producer.py,
  output SHA-256 de81e07b07597d6a
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 e82ef16d7b495a4c
- failing control: python3 relays/agy_2026-11-27_c65/c65_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-27_c65/c65_countercheck.py
  (SHA-256 d3cb3ca2bf655e5d, output SHA-256 04bbde959113a798, zero shared imports, Faddeev-LeVerrier trace recursion,
  contragredient J-conjugate bipartite Schur CRT, and 12-ray Bloch evaluation, agrees with 0 discrepancies)
- already on main?: topic_sweep.py "P-845|B1983|B1993|B2000|P\\^1\\(F_5\\)|Leg\\(5\\)" on origin/main (64cc951b3): closest
  arcs B1983 (notes level 5 divides t^2 - 4 at t = 3 while scalar cusp leaf connects at p >= 5), B1989 and B2000 (2I bound
  states and 14 : 5 split at (3, 3, 3)), and B2011/B2017 (scalar trace mod 5 and mod 135 fail pairing/halving; two-counts
  W_{6,omega} Leg(5) golden emergence, O_27 x Fiber_p diagonal bundles, and E_{phi^2} I_4/I_6 hierarchy unrun)
- what would make it fail: replacing trace-3 L R and x^2 - 3 x + 1 with trace-4 L^2 R and x^2 - 4 x + 1 yields empty prime
  matches so c65_control.py exits 1, or any prime p != 5 satisfying 3 + 3 systole parabolicity, or O_27 x Leg(5) failing to
  isolate (y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2, or I_4 varying along the real equator of E_{phi^2}
