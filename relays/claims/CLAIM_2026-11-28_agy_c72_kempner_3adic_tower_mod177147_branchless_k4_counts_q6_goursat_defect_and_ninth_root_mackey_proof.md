# CLAIM CARD — Kempner 3-adic tower law to mod 177147 (B2007), all-prime branchless K4 leaf counts (B1990), Q_6 Goursat halving defect (B2003/B2010), and K_4 Mackey proof of ninth roots (B1997) (0 of 19)

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, 4999c14f9d6a6c50ffbb73e42aa3e9e2bf9715f5
- kind: theorem
- touches: P-630, P-755, P-882
- effect: conditions — P-630, P-755, and P-882 (proves for B2007 Open #1 that every word in G_k acts on each sheet of the Klein-four
  Hensel section S_k ~= {1, 2} x (Z / 3^(k-2) Z)^2 by an integral power series obeying v_3(c_{r,s}) >= r + s - 1 for r + s >= 1,
  truncating exact action modulo 3^m (m = k - 2) at degree <= m where Kempner's falling-factorial null ideal adds +v_3(i!) + v_3(j!)
  rather than subtracting v_3(d!), and proves via complete Hall polycyclic presentation sifting (all 96 Schreier words, G_k-conjugates,
  cubes, and all 2278 basis commutators) that dims_k3_k11 = [2, 2, 3, 7, 7, 7, 12, 14, 14] through mod 177147 = 3^11 with |G_11| = 24 *
  3^68 = 6675081346648644270174858629562264 and unbounded rank growth refuting constant-rank 3-adic Lie saturation; proves for B1990 Open
  #1 via affine conic fibration the universal all-prime branchless quadratic-character law #X_kappa(F_p) = p^2 + ((kappa - 2)/p)(3 +
  ((kappa + 2)/p)) p + 1 across every odd prime p >= 3 and every kappa in F_p, showing 3((kappa - 2)/p)p sits on every leaf while ((kappa
  + 2)/p) = 0 at the cusp kappa = -2 unmasks the bare 3; proves for B2003 Open #3 and B2010 Open #1 that mod 63 pairs 8 of 74 modes as
  (x^2 - 1)^2(x^2 - 2x - 1)(x^2 + 2x - 1) and direct mod 189 (2016 vertices) pairs 663 of 671 modes leaving 8 unpaired, constructs the
  6-point quotient Q_6 = O_27 / N_3 (N_3 = (V_4 K_3) cap [G_3, G_3]), proves via Hensel pure translations of L_4 = L_3^3 that B_k (x) rho
  ~= B_k for all k >= 3 so the unpaired modes of Cartesian O_{3^k} x O_p equal those of Q_6 x O_p for every k >= 3 and every (L, R, C)-set
  O_p, and proves via Goursat's lemma (|Gamma_5 / Gamma_5'| = |Gamma_7 / Gamma_7'| = 2 and |O_{9p}| = 8|O_p|) that O_{3^k * p} = O_{3^k} x
  O_p holds for all k >= 3 whenever |O_{9p}| = 8|O_p| and 3 does not divide |Gamma_p / Gamma_p'|, locking 10 unpaired modes at p = 5 and 8
  unpaired modes at p = 7 for all k >= 3; and proves for B1997 Open #1 that K_4 ~= (Z / 9 Z)^2 acts regularly on the 8 fibers of O_81 ->
  O_9, splitting Dual(K_4) = Hom(K_4, mu_9) into 19 S_4-orbits of which strictly 3 inversion-closed (chi^(-1) in S_4 . chi) order-9 size-6
  orbits annihilate W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4 over Q(cos 2 pi / 9) with Mackey double-coset multiplicity 2 each)
- scope: frame: no frame (3-adic Markoff congruence tower G_k through mod 177147 = 3^11, frustration leaf family X_kappa over F_p,
  Cartesian and composite CRT graphs O_{3^k} x O_p and O_{3^k * p}, and regular abelian fiber extension G_4 = K_4 . S_4 on O_81); object:
  Hall-sifted polycyclic F_3-layers L_3 to L_11, affine conic bundles on X_kappa, symmetric 6-move walk spectra on O_63, O_189, and Q_6 x
  O_p, and Dual(K_4) Fourier blocks of W_+ = L + R on O_81; reach: class; hypotheses: 100% exact integer, polynomial, rational,
  permutation-group, and cyclotomic DomainMatrix arithmetic in stdlib and sympy (zero floating-point literals, strictly 0 of 19)
- identifications: none
- definitions: In scaled Markoff coordinates a_i = x_i / 3 mod 3^(k-1) on a_1^2 + a_2^2 + a_3^2 = 3 a_1 a_2 a_3 mod 3^(k-1) (k >= 2),
  O_{3^k} is the orbit of (1, 1, 1) under L_s(a_1, a_2, a_3) = (a_1, a_3, 3 a_1 a_3 - a_2) and R_s(a_1, a_2, a_3) = (a_3, a_2, 3 a_2
  a_3 - a_1), G_k = <L_s, R_s> <= Sym(O_{3^k}) (G_2 ~= S_4 of order 24), K_k = ker(G_k -> G_2), and L_k = ker(G_k -> G_{k-1}) ~=
  F_3^(d_k) for k >= 3. Modulo V_4 = {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)}, S_k = {a in O_{3^k} : a_1 = 1, a_2 = 1 mod 3} ~= {1,
  2} x (Z / 3^m Z)^2 (m = k - 2) via a = (1 + 3 t_1, 1 + 3 t_2, eps + 3 Phi_eps(t_1, t_2)). Expanding each sheet component P(t_1, t_2)
  = sum_{0 <= r+s <= m} c_{r,s} t_1^r t_2^s in falling factorials t_1^{\underline{i}} t_2^{\underline{j}} via Stirling numbers S(r, i)
  gives Kempner canonical residues d_tilde_{i,j} mod 3^max(0, m - v_3(i!) - v_3(j!)), which vanish iff P = 0 on all of (Z / 3^m Z)^2.
  Here hensel_exact asserts exact satisfaction of the scaled Markoff congruence mod 3^10, v_3(c_{r,s}) >= r + s - 1 (r + s >= 1), formal
  series L_s^(-1) o L_s = R_s^(-1) o R_s = id on S_11, sheet invariance across all 96 forward and inverse Reidemeister-Schreier words,
  and |G_2| = 24; hall_comms = 2278 is the number of unordered basis-pair commutators [b_1, b_2] sifted alongside all 96 Schreier words,
  G_k-conjugates, and cubes in Hall polycyclic closure; dims_k3_k11 = [d_3, ..., d_11]; cubing_k3_k10 = [rk(L_3^3 in L_4), ...,
  rk(L_10^3 in L_11)]; log3K11 = sum_{k=3}^11 d_k; and G11 = |G_11| = 24 * 3^(log3K11). On X_kappa : x^2 + y^2 + z^2 - x y z = kappa + 2
  over F_p (odd prime p >= 3), conic_id asserts exact polynomial identity (2 z - x y)^2 - (x^2 - 4)(y^2 - 4) - 4(kappa - 2) = 4(x^2 + y^2
  + z^2 - x y z - (kappa + 2)) in Z[x, y, z, kappa]; with Legendre symbol (u / p) in {-1, 0, 1} ((0 / p) = 0), branchless_exact asserts
  across all 17 odd primes 3 <= p <= 61 (primes = 17, sectors = 499 pairs (p, kappa)) that #X_kappa(F_p) = p^2 + ((kappa - 2)/p)(3 +
  ((kappa + 2)/p)) p + 1 and p3_cusp = #X_{-2}(F_3) = 1. On unscaled O_M (orbit of (3 mod M, 3 mod M, 3 mod M) under L_tr(x, y, z) = (x,
  z, x z - y) and R_tr(x, y, z) = (z, y, y z - x)), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, x y - z), tau(x, y, z) = (y, x, z),
  W = sum_{j=0}^2 (C^j L_tr C^(-j) + C^j L_tr^(-1) C^(-j)), p_0 (resp. p_1) is the monic characteristic polynomial of W on ker(C - I)
  (resp. ker(C - omega I), omega = exp(2 pi i / 3), equivalently ker(I + C + C^2) cap ker(tau - I)), paired_deg is deg gcd(p_0(2 x),
  p_1(x)), and unpaired_deg = deg p_1 - paired_deg. With pi_k : G_k -> G_3 (k >= 3) the canonical mod-27 reduction homomorphism, rho : G_k
  -> mu_6 (B2009, mu_6 = <-omega>) the order-6 character with rho(sigma) = -1 and rho(C) = omega, Gamma_p = <L_tr, R_tr> <= Sym(O_p) with
  commutator subgroup Gamma_p' = [Gamma_p, Gamma_p] for prime p >= 5, and B_k = ker(C[O_{3^k}] -> C[Q_6]) where N_3 = (V_4 K_3) cap [G_3,
  G_3] (order N3 = 12) on O_27 (72 points, G_3 of order 216) yields Q_6 = O_27 / N_3 (size Q6 = 6, |Fix(C)| = fixC_Q6 = 3): mod63_paired
  and mod189_paired record paired_deg on O_63 and O_189; unp_p5 and unp_p7 record unpaired_deg on Q_6 x O_5 and Q_6 x O_7; and
  all_k_goursat asserts |O_15| = |O_5|, |O_45| = 8|O_5|, |O_63| = 8|O_7|, |O_189| = 72|O_7|, |Gamma_5 / Gamma_5'| = |Gamma_7 / Gamma_7'| =
  2, pure-translation 2-jet mod 9 of L_4 on S_4, |Fix_{O_{3^k}}(g)| = |Fix_{Q_6}(g)| across all 204 elements of G_3 \ N_3 (with the 48
  fix-3 elements equal to the G_3-conjugacy class of {C, C^(-1)}) and all 1836 elements of G_4 \ pi_4^(-1)(N_3), and equality of unpaired
  factors between direct O_189 and Q_6 x O_7. On O_81 (648 points, G_4 of order 1944), with zeta_9 = exp(2 pi i / 9) and mu_9 = <zeta_9>,
  K_4 = ker(G_4 -> G_2) ~= (Z / 9 Z)^2 (order 81) acts regularly on the 8 fibers of O_81 -> O_9; dual_orbs counts S_4-orbits on Dual(K_4)
  = Hom(K_4, mu_9) under (g . chi)(k) = chi(g^(-1) k g); p12_prod asserts prod_{r in {1, 2, 4}} (x^4 - (1 -
  2(zeta_9^r + zeta_9^(-r))) x^2 + 4) = x^12 - 3 x^10 + 3 x^8 - 21 x^6 + 12 x^4 - 48 x^2 + 64 over Q(zeta_9); inv_ord9 counts size-6
  order-9 S_4-orbits in Dual(K_4) closed under chi -> chi^(-1); q_hits lists [r, dim ker Q_r(W_+)] across those inv_ord9 orbits on their
  48-dimensional fiber blocks where W_+ = L_tr + R_tr and Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4; mackey_dc = |S \
  S_4 / H_chi| with S = Stab_{S_4}(x_0) (order 3 at basepoint x_0 = (3, 3, 3) mod 9 in O_9) and H_chi = Stab_{S_4}(chi) (order 4); and
  pf counts verification of the 5 planted-fault controls (PF1: 8 in [2 d + 1 - v_3(d!)] while d_6 = d_7 = d_8 = 7 and d_9 = 12; PF2: d_3
  < d_5 < d_6 < d_9 < d_10 = 14 refuting constant-rank Lie saturation; PF3: flipping 3 + ((kappa + 2)/p) to 3 - ((kappa + 2)/p) fails at
  every odd prime 5 <= p <= 61; PF4: replacing Q_6 by unshifted S_3 module 1 (+) sgn (+) E_2 gives 52 != 10 unpaired modes at p = 5; PF5:
  all 16 Dual(K_4) orbits outside the 3 inversion-closed order-9 size-6 orbits have 0 nullity across Q_1, Q_2, Q_4).
- imports: none
- premises on main: B1990, B1996, B1997, B2001, B2002, B2003, B2004, B2005, B2006, B2007, B2009, B2010, P-630, P-755, P-882
- decisive script: relays/agy_2026-11-28_c72/c72_kempner_3adic_tower_k4_counts_q6_goursat_and_ninth_roots_producer.py,
  SHA-256 8cdfdde2199cc5d0, depends on the standard library and sympy, run as
  python3 relays/agy_2026-11-28_c72/c72_kempner_3adic_tower_k4_counts_q6_goursat_and_ninth_roots_producer.py,
  output SHA-256 885aa7576e676be3
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 2a0f0e5a1d942c6a
- failing control: python3 relays/agy_2026-11-28_c72/c72_control.py
- second computation: fam3-v1-high-01 disjoint cold-room countercheck relays/agy_2026-11-28_c72/c72_countercheck.py
  (SHA-256 cef8f02a2ee97d5e, output SHA-256 ec2ee07a9b3a1189, zero shared imports, disjoint Klein-four section a_2 = 1, a_3 = 1 mod 3
  solving a_1 = delta + 3 Psi_delta(t_2, t_3) with base-3 digit-sum Legendre valuations, direct Kempner poised-grid evaluation without
  Stirling numbers, and full 2278-commutator Hall polycyclic closure through mod 177147 = 3^11, O(p) 1D affine conic-bundle character
  sums across 20 odd primes 3 <= p <= 73, B2004 sigma-reduced C-orbit operators plus tau-symmetrized Schur-Wielandt Hecke intertwiner on
  O_189 and abstract 6D rational S_3 x Z_3 representation 1 (+) sgn (+) (E_2 (x) A_2) without O_27/N_3 quotienting, and conjugate
  zeta_9^(-1) sparse SDM Fourier blocks plus Burnside double-coset Mackey index, agrees with 0 discrepancies and 5/5 referee controls
  caught)
- already on main?: topic_sweep.py "B2007|177147|Kempner|B1990.*K4|mod 63.*paired|B1997.*ninth" on origin/main (f476b4664): B2007
  stopped at k = 6 (mod 729) via GAP/Sage and B2014 verified k = 7 (mod 2187, |G_7| = 24 * 3^27) while registering k = 8, 9 = [7, 12]
  unchecked without the all-k Kempner valuation/truncation proof, complete Hall commutator closure, or k = 10, 11 = [14, 14] (mod
  177147); B1990 left the all-prime proof and unified quadratic-character law of K4 open (#1); B2003 left higher composite behavior open
  (#3), and B2011 checked mod 45 (4 paired) and mod 135 (10 unpaired) without mod 63 (8 paired), direct mod 189 (663 paired, 8 unpaired),
  Q_6 = O_27 / N_3, or the all-k >= 3 Hensel/character and Goursat proof (B2010 Open #1); B1997 found the degree-12 polynomial post hoc
  and left the G_4 symmetry derivation of ninth roots Q(cos 2 pi / 9) and multiplicity 2 open (#1)
- what would make it fail: dims_k3_k11 differing from [2, 2, 3, 7, 7, 7, 12, 14, 14] or cubing_k3_k10 differing from [2, 2, 3, 7, 7, 7,
  12, 14] or log3K11 != 68 or hall_comms != 2278 or hensel_exact=False, or conic_id=False or branchless_exact=False or p3_cusp != 1, or
  N3 != 12 or Q6 != 6 or fixC_Q6 != 3 or mod63_paired != 8 or mod189_paired != 663 or unp_p5 != 10 or unp_p7 != 8 or
  all_k_goursat=False, or dual_orbs != 19 or p12_prod=False or inv_ord9 != 3 or q_hits differing from [[1, 8], [2, 8], [4, 8]] or
  mackey_dc != 2, or pf != 5/5 or standalone exit-1 control failing
