# CLAIM CARD — Two-counts all-prime P^1(F_p) classification, unique p = 5 parabolic (3, 3, 3) systole split and Leg(5) golden walk, diagonal O_27 x Fiber_p bundles, and full-Bloch-sphere PF5 SOS systole selection (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, 2c03eb4feff2d080683b7e57d22349414b57691b
- kind: theorem
- touches: A01, A03, P-374, P-630, P-845, P-882
- effect: conditions — A01, A03, P-374, P-630, P-845, and P-882 (proves p = 5 is the unique prime where P^1(F_p) \ T_cusp
  forms a single C_omega-triplet T_sys and the unique prime where (3, 3, 3)'s three systoles become parabolic mod p fixing
  T_sys with W_{6,tr} Jacobian (14, 5, 5); proves 100% mirror charged pairing on Vecs(p), Rays(p), and P^1(F_p) for all p
  and certifies across p in {2..23} that p = 5 is unique with ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I) vanishing on P^1(F_p)
  and emerging in quadratic Leg(5); classifies diagonal O_27 x Fiber_p bundles across p in {2, 3, 5, 7} isolating unpaired
  (y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2 on O_27 x Leg(5); and proves exact full-Bloch-sphere CP^1 Sum-of-Squares identities for
  W_sys / W_cusp = phi^2, 3/10 - I_4 >= 0, and 11/90 - I_6 >= 0 selecting the 3-element mirror-even systole orbit on E_{phi^2})
- scope: frame: no frame (foundational two-counts updates L, R on (Z/pZ)^2 \ {(0, 0)} and direct diagonal SL(2, Z) action
  with O_27); object: P^1(F_p), Rays(p), and Vecs(p) across primes p >= 2 (explicitly p in {2, 3, 5, 7, 11, 13, 17, 19, 23}),
  diagonal bundles O_27 x Fiber_p for p in {2, 3, 5, 7}, and the full complex Bloch sphere CP^1 of the 2-dim golden eigenspace
  E_{phi^2} subset Leg(5); reach: class; hypotheses: exact integer, rational, and algebraic-number arithmetic scoped to the
  stated prime sets where not all-prime
- identifications: none
- definitions: On Z^2, L = [[1, 1], [0, 1]], R = [[1, 0], [1, 1]], C_omega = L R^-1 = [[0, 1], [-1, 1]] (C_omega^3 = -I_2),
  order-3 charge generator C_{3,omega} = -C_omega = C_omega^4 = [[0, -1], [1, -1]], and mirror tau = [[0, 1], [1, 0]]. For
  prime p, Vecs(p) = F_p^2 \ {(0, 0)} (size p^2 - 1), Rays(p) = Vecs(p) / {+-1}, and P^1(F_p) = Vecs(p) / F_p^x (size p + 1,
  canonical reps [1 : 0], [0 : 1], and [1 : b] for 1 <= b < p). Cusp shears P_1 = L, P_2 = C_omega L C_omega^-1 = R^-1 =
  [[1, 0], [-1, 1]], and P_3 = C_omega^2 L C_omega^-2 = [[0, 1], [-1, 2]] fix T_cusp = {[1 : 0], [0 : 1], [1 : 1]}, leaving
  R_p = P^1(F_p) \ T_cusp (dual_triplet_primes are p in {2..23} where |R_p| = 3 as one C_omega-orbit). Systoles U_1 = L R =
  [[2, 1], [1, 1]], U_2 = C_omega U_1 C_omega^-1 = [[2, -1], [-1, 1]], and U_3 = C_omega^2 U_1 C_omega^-2 = [[0, 1], [-1, 3]]
  are parabolic mod p iff U_i != +-I_2 mod p and (U_i + I_2)^2 == 0 or (U_i - I_2)^2 == 0 mod p (parabolic_systole_primes,
  and exact_match_primes where each U_i fixes 1 line and their union equals R_p). On A^3, L_tr(x, y, z) = (x, z, x z - y),
  R_tr(x, y, z) = (z, y, y z - x), C_tr = R_tr^-1 o L_tr : (x, y, z) -> (y, z, x), and W_{6,tr} = sum_{j=0}^2 C_tr^j (L_tr +
  R_tr) C_tr^-j (with 3 x 3 Jacobian eigenvalues jacobian_333 at (3, 3, 3)). For any order-3 operator C_3 and omega =
  exp(2 pi i / 3), H_q = ker(C_3 - omega^q I) (d_q = dim H_q for q in {0, 1, 2}). On Vecs(p), Rays(p), and P^1(F_p),
  W_{6,omega} = sum_{j=0}^2 C_omega^j (L + R) C_omega^-j commutes with C_3 = C_{3,omega}, giving monic P_neu(x) = det(x I -
  W_{6,omega}|_{H_0}) and P_chg(x) = det(x I - W_{6,omega}|_{H_1}) = det(x I - W_{6,omega}|_{H_2}) in Z[x]; across p in
  {2, 3, 5, 7, 11, 13, 17, 19, 23}, golden_primes_2_to_23 have dim ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I) > 0 on Vecs(p),
  and pure_cover_golden_primes have dim = 0 on P^1(F_p) and dim > 0 on Rays(p). For ordered lines (l_1, ..., l_6) = ((1, 0),
  (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)) of P^1(F_5), r_i^+ = +-l_i in Rays(5) and r_i^- = +-2 l_i in Rays(5) ((2 / 5) = -1,
  (-1 / 5) = +1); Leg(5) subset C^(Rays(5)) has orthonormal basis e_i = (|r_i^+> - |r_i^->) / sqrt(2) (1 <= i <= 6) and
  mirror T_leg = tau|_{Leg(5)}. On O_27 (<L_tr, R_tr>-orbit of (3, 3, 3) mod 27, 72 pts) times Fiber_p (including signed-line
  Leg(5) where M(v, e_i) = (M_tr(v), (s / 5) e_j) for M l_i = s l_j mod 5, and odd-parity spinor {f(v, -u) = -f(v, u)} of
  O_27 x Vecs(5) with dim 864, d_0 = d_1 = 288), L_diag = (L_tr, L), R_diag = (R_tr, R), C_0 = R^-1 L = L^-1 C_omega L,
  S = L R^-1 L (S^2 = -I_2), order-3 g_{C_3} = S^2 R^-1 L acts as C_3 = (C_tr, -C_0), W_{6,diag} = sum_{j=0}^2 g_{C_3}^j
  (L_diag + R_diag) g_{C_3}^-j, y = 2 x, P_neu(y) = det(y I - W_{6,diag}|_{H_0}), P_{2,chg}(y) = 2^{d_1} det((y / 2) I -
  W_{6,diag}|_{H_1}) in Z[y], halved degree is deg gcd_{Z[y]}(P_neu(y), P_{2,chg}(y)), monic unpaired polynomial is
  P_{2,chg}(y) / gcd_{Z[y]}(P_neu(y), P_{2,chg}(y)), Category (a) is d_0 - d_1 = 3 with P_neu(y) = y(y^2 - 36) P_{2,chg}(y),
  and Category (a') is d_0 = d_1 > 0 with P_neu(y) = P_{2,chg}(y). On E_{phi^2} = ker(W_{6,omega}|_{Leg(5)} - phi^2 I_6)
  (phi^2 = (3 + sqrt(5)) / 2) with real orthonormal T_leg-eigenbasis (e_+, e_-) (T_leg e_+ = +e_+, e_{+,6} > 0, T_leg e_- =
  -e_-, e_{-,4} > e_{-,5}), every Bloch state is psi(theta, alpha) = cos(theta) e_+ + exp(i alpha) sin(theta) e_- ((theta,
  alpha) in R^2, real equator sin(alpha) = 0, chiral poles alpha = +-pi/2 and theta = pi/4), p_i(theta, alpha) =
  |<e_i | psi(theta, alpha)>|^2, W_cusp = p_1 + p_2 + p_3, W_sys = p_4 + p_5 + p_6, I_4 = sum_{i=1}^6 p_i^2 (with SOS
  deficit 3/10 - I_4 = (1/10) sin^2(alpha) sin^2(2 theta)), and I_6 = sum_{i=1}^6 p_i^3 (with SOS deficit 11/90 - I_6 =
  (1/45)[sin(theta)(4 cos^2(theta) - 1)]^2 + (2/15)(sin(alpha) sin(theta) cos(theta))^2 + (4/15)(sin(alpha) sin^2(theta)
  cos(theta))^2).
- imports: none
- premises on main: B1983, B1989, B1993, B1994, B1995, B1998, B2000, B2002, B2004, B2009, B2011, B2012, B2013, B2014,
  B2017, P-374, P-630, P-845, P-882
- decisive script: relays/agy_2026-11-27_c66/c66_two_counts_prime5_parabolic_systoles_and_bloch_sos_producer.py,
  SHA-256 997ad790a5a0e0fe, depends on the standard library, sympy and mpmath, run as
  python3 relays/agy_2026-11-27_c66/c66_two_counts_prime5_parabolic_systoles_and_bloch_sos_producer.py,
  output SHA-256 1b807c484e84f3f8
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 3e746c6518022440
- failing control: python3 relays/agy_2026-11-27_c66/c66_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-27_c66/c66_countercheck.py
  (SHA-256 48967b27e09d7183, output SHA-256 7dd334974d4b12ba, zero shared imports, 12-pair Faddeev-LeVerrier trace
  recursion, ray-involution Leg(5) projection, contragredient J-conjugate bipartite Schur CRT, and complex 12-ray Bloch
  evaluation, agrees with 0 discrepancies)
- already on main?: topic_sweep.py "P-845|B1983|B1993|B2000|P\\^1\\(F_5\\)|Leg\\(5\\)" on origin/main (1ac86a821): closest
  arcs B1983 (notes level 5 divides t^2 - 4 at t = 3 while scalar cusp leaf connects at p >= 5), B1989 and B2000 (2I bound
  states and 14 : 5 split at (3, 3, 3)), and B2011/B2017 (scalar trace mod 5 and mod 135 fail pairing/halving; two-counts
  W_{6,omega} Leg(5) golden emergence, O_27 x Fiber_p diagonal bundles, and full-CP^1 E_{phi^2} I_4/I_6 SOS hierarchy unrun)
- what would make it fail: shears_ok=False, or exact_match_primes or pure_cover_golden_primes differing from [5] across
  {2..23}, or O_27 x Leg(5) failing to isolate unpaired (y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2, or either full-Bloch-sphere
  SOS identity I4_sos or I6_sos evaluating to False
