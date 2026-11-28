# CLAIM CARD — Kempner 3-adic tower law to mod 177147 (B2007), all-prime branchless K4 leaf counts (B1990), universal 6-point CRT halving defect quotient (B2003), and K_4 Mackey proof of ninth roots (B1997) (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, 18483c9e358c893d60ad68a920b814cd3a495683
- kind: theorem
- touches: P-630, P-755, P-882
- effect: conditions — P-630, P-755, and P-882 (proves for B2007 Open #1 that every word in G_k acts on each sheet of the Klein-four
  Hensel section S_k ~= {1, 2} x (Z / 3^(k-2) Z)^2 by an integral power series obeying v_3(c_{i,j}) >= i + j - 1 for i + j >= 1,
  truncating exact action modulo 3^m (m = k - 2) at degree <= m where Kempner's falling-factorial null ideal adds +v_3(i!) + v_3(j!)
  rather than subtracting v_3(d!), so k = 8 (mod 6561) stays flat at 7 across a three-rung plateau [7, 7, 7] before jumping to 12 at
  k = 9 and 14 at k = 10, 11 (dims_k3_k11 = [2, 2, 3, 7, 7, 7, 12, 14, 14], |G_11| = 24 * 3^68 = 6675081346648644270174858629562264,
  refuting finite-rank 3-adic Lie saturation); proves for B1990 Open #1 via affine conic fibration the universal all-prime branchless
  quadratic-character law #X_kappa(F_p) = p^2 + ((kappa - 2)/p)(3 + ((kappa + 2)/p)) p + 1 across every odd prime p >= 3 and every
  kappa in F_p, showing that 3((kappa - 2)/p)p sits on every leaf while ((kappa + 2)/p) = 0 at the cusp kappa = -2 unmasks the bare 3;
  proves for B2003 Open #3 that mod 45's 4 paired modes are x^2(x - 2)(x + 2) (and mod 63's 8 paired modes are (x^2 - 1)^2(x^2 - 2x -
  1)(x^2 + 2x - 1)), and constructs the 6-point quotient Q_6 = O_27 / ((V_4 K_3) cap [G_3, G_3]) proving that for all k >= 3 and primes
  p >= 5, the unpaired charged modes of O_{3^k * p} are strictly independent of k and equal those of Q_6 x O_p (degree 10 for p = 5,
  degree 8 for p = 7); and proves for B1997 Open #1 that K_4 ~= (Z / 9 Z)^2 acts regularly on the 8 fibers of O_81 -> O_9, splitting
  Dual(K_4) into 19 S_4-orbits of which strictly 3 inversion-closed (-m in S_4 . m) order-9 size-6 orbits annihilate the 3 Galois
  quartics W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4 over Q(cos 2 pi / 9) with Mackey double-coset multiplicity 2 each)
- scope: frame: no frame (3-adic Markoff congruence tower G_k through mod 177147 = 3^11, frustration leaf family X_kappa over F_p,
  composite CRT graphs O_{3^k * p}, and regular abelian fiber extension G_4 = K_4 . S_4 on O_81); object: polycyclic F_3-layers L_3 to
  L_11, affine conic bundles on X_kappa, symmetric 6-move walk spectra on composite levels and Q_6 x O_p, and Dual(K_4) Fourier blocks
  of W_+ = L + R on O_81; reach: class; hypotheses: 100% exact integer, polynomial, rational, and cyclotomic DomainMatrix arithmetic in
  stdlib and sympy (zero floating-point literals, strictly 0 of 19)
- identifications: none
- definitions: In scaled Markoff coordinates a_i = x_i / 3 mod 3^(k-1) on a_1^2 + a_2^2 + a_3^2 = 3 a_1 a_2 a_3 mod 3^(k-1) (k >= 2),
  O_{3^k} is the orbit of (1, 1, 1) under L_s(a_1, a_2, a_3) = (a_1, a_3, 3 a_1 a_3 - a_2) and R_s(a_1, a_2, a_3) = (a_3, a_2, 3 a_2
  a_3 - a_1), G_k = <L_s, R_s> <= Sym(O_{3^k}) (G_2 ~= S_4 of order 24), K_k = ker(G_k -> G_2), and L_k = ker(G_k -> G_{k-1}) ~=
  F_3^(d_k) for k >= 3. Modulo V_4 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}, S_k = {a in O_{3^k} : a_1 = 1, a_2 = 1 mod 3} ~= {1,
  2} x (Z / 3^m Z)^2 (m = k - 2) via a = (1 + 3 t_1, 1 + 3 t_2, eps + 3 Phi_eps(t_1, t_2)). Expanding each sheet component P(t_1, t_2)
  = sum_{0 <= r+s <= m} c_{r,s} t_1^r t_2^s in falling factorials t_1^{\underline{i}} t_2^{\underline{j}} via Stirling numbers S(r, i)
  gives Kempner canonical residues d_tilde_{i,j} mod 3^max(0, m - v_3(i!) - v_3(j!)), which vanish iff P = 0 on all of (Z / 3^m Z)^2.
  Here hensel_exact asserts exact satisfaction of the scaled Markoff congruence mod 3^10, v_3(coeff t^alpha) >= |alpha| - 1 (|alpha| >=
  1), formal series L_s^(-1) o L_s = R_s^(-1) o R_s = id on S_11, sheet invariance of all 48 Reidemeister-Schreier generators, and
  |G_2| = 24; dims_k3_k11 = [d_3, ..., d_11]; cubing_k3_k10 = [rk(L_3^3 in L_4), ..., rk(L_10^3 in L_11)]; log3K11 = sum_{k=3}^11 d_k;
  and G11 = |G_11| = 24 * 3^(log3K11). On X_kappa : x^2 + y^2 + z^2 - x y z = kappa + 2 over F_p (odd prime p >= 3), conic_id asserts
  exact polynomial identity (2 z - x y)^2 - (x^2 - 4)(y^2 - 4) - 4(kappa - 2) = 4(x^2 + y^2 + z^2 - x y z - (kappa + 2)) in Z[x, y, z,
  kappa]; with Legendre symbol (u / p) in {-1, 0, 1} ((0 / p) = 0), branchless_exact asserts across all 17 odd primes 3 <= p <= 61
  (primes = 17, sectors = 499 pairs (p, kappa)) that #X_kappa(F_p) = p^2 + ((kappa - 2)/p)(3 + ((kappa + 2)/p)) p + 1 and p3_cusp =
  #X_{-2}(F_3) = 1. On unscaled O_M (orbit of (3 mod M, 3 mod M, 3 mod M) under L_tr(x, y, z) = (x, z, x z - y) and R_tr(x, y, z) = (z,
  y, y z - x)), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, x y - z), W = sum_{j=0}^2 (C^j L_tr C^(-j) + C^j L_tr^(-1) C^(-j)), p_0
  (resp. p_1) is the monic characteristic polynomial of W on ker(C - I) (resp. ker(C - omega I), omega = exp(2 pi i / 3)), paired_deg
  is deg gcd(p_0(2 x), p_1(x)), and unpaired_deg = deg p_1 - paired_deg. On O_27 (72 points, G_3 of order 216), N_3 = (V_4 K_3) cap
  [G_3, G_3] (order N3 = 12) yields the quotient graph Q_6 = O_27 / N_3 (size Q6 = 6, |Fix(C)| = fixC_Q6 = 3); mod45_paired and
  mod63_paired record paired_deg on O_45 and O_63, while unp_p5 and unp_p7 record unpaired_deg on Q_6 x O_5 and Q_6 x O_7 (equal to
  unpaired_deg on O_{3^k * p} for every k >= 3 by B2009 and B2010). On O_81 (648 points, G_4 of order 1944), K_4 = ker(G_4 -> G_2) ~=
  (Z / 9 Z)^2 (order 81) acts regularly on the 8 fibers of O_81 -> O_9; dual_orbs counts S_4-orbits on Dual(K_4) = Hom((Z / 9 Z)^2,
  mu_9) under g . m = (A_g^(-1))^T m; p12_prod asserts prod_{r in {1, 2, 4}} (x^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) x^2 + 4) = x^12 - 3
  x^10 + 3 x^8 - 21 x^6 + 12 x^4 - 48 x^2 + 64 over Q(zeta_9); inv_ord9 counts size-6 order-9 S_4-orbits in Dual(K_4) closed under m ->
  -m; q_hits lists [r, dim ker Q_r(W_+)] across those inv_ord9 orbits on their 48-dimensional fiber blocks where W_+ = L_tr + R_tr and
  Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4; mackey_dc = |S \ S_4 / H_chi| with S = Stab_{S_4}(x_0) (order 3) and
  H_chi = Stab_{S_4}(m) (order 4); and pf counts verification of the 5 planted-fault controls (PF1: 8 in [2 d + 1 - v_3(d!)] while d_6
  = d_7 = d_8 = 7 and d_9 = 12; PF2: d_3 < d_5 < d_6 < d_9 < d_10 = 14 refuting constant-rank Lie saturation; PF3: flipping 3 + ((kappa
  + 2)/p) to 3 - ((kappa + 2)/p) fails at every odd prime 5 <= p <= 61; PF4: replacing Q_6 by unshifted S_3 module 1 (+) sgn (+) E_2
  gives 52 != 10 unpaired modes at p = 5; PF5: all 16 Dual(K_4) orbits outside the 3 inversion-closed order-9 size-6 orbits have 0
  nullity across Q_1, Q_2, Q_4).
- imports: none
- premises on main: B1990, B1996, B1997, B2001, B2002, B2003, B2004, B2005, B2006, B2007, B2009, B2010, P-630, P-755, P-882
- decisive script: relays/agy_2026-11-28_c71/c71_kempner_3adic_tower_k4_counts_crt_quotient_and_ninth_roots_producer.py,
  SHA-256 5eda4c7d5d2852be, depends on the standard library and sympy, run as
  python3 relays/agy_2026-11-28_c71/c71_kempner_3adic_tower_k4_counts_crt_quotient_and_ninth_roots_producer.py,
  output SHA-256 44e386a75c345507
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 64ce156dcc52bd49
- failing control: python3 relays/agy_2026-11-28_c71/c71_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-28_c71/c71_countercheck.py
  (SHA-256 93e915a59d68e617, output SHA-256 8bd9e858ddcb3f65, zero shared imports, disjoint Klein-four section a_2 = 1, a_3 = 1 mod 3
  solving a_1 = delta + 3 Psi_delta(t_2, t_3) with base-3 digit-sum Legendre valuations and direct Kempner poised-grid evaluation
  through mod 177147 = 3^11 without Stirling numbers, O(p) 1D affine conic-bundle character sums across 20 odd primes 3 <= p <= 73,
  B2004 sigma-reduced C-orbit operators plus abstract 6D rational S_3 x Z_3 representation 1 (+) sgn (+) (E_2 (x) A_2) without O_27 or
  N_3 enumeration, and conjugate zeta_9^(-1) sparse SDM Fourier blocks plus Burnside double-coset Mackey index, agrees with 0
  discrepancies and 5/5 referee controls caught)
- already on main?: topic_sweep.py "B2007|177147|Kempner|B1990.*K4|mod 45.*paired|B1997.*ninth" on origin/main (e6cb50af0): B2007
  stopped at k = 6 (mod 729) via GAP/Sage and AGY-C70 stopped at k = 7 (mod 2187) with a minus-sign wake-up list leaving k = 8..11 (mod
  6561 to mod 177147) and the Kempner +v_3 plateau [7, 7, 7] -> 12 -> 14 -> 14 open; B1990 left the all-prime proof and unified
  quadratic-character law of K4 open (#1); B2003 left mod 45's 4 paired modes and higher composite behavior open (#3); B1997 found the
  degree-12 polynomial post hoc and left the G_4 symmetry derivation of ninth roots Q(cos 2 pi / 9) and multiplicity 2 open (#1)
- what would make it fail: dims_k3_k11 differing from [2, 2, 3, 7, 7, 7, 12, 14, 14] or cubing_k3_k10 differing from [2, 2, 3, 7, 7, 7,
  12, 14] or log3K11 != 68 or hensel_exact=False, or conic_id=False or branchless_exact=False or p3_cusp != 1, or N3 != 12 or Q6 != 6
  or fixC_Q6 != 3 or mod45_paired != 4 or mod63_paired != 8 or unp_p5 != 10 or unp_p7 != 8, or dual_orbs != 19 or p12_prod=False or
  inv_ord9 != 3 or q_hits differing from [[1, 8], [2, 8], [4, 8]] or mackey_dc != 2, or pf != 5/5 or standalone exit-1 control failing
