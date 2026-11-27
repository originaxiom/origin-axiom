# CLAIM CARD — All-odd-N quadratic-reciprocity Weil chiral index and parity-split theorem, explicit Leg(5) Weil-triplet intertwiner and O_27 x Weil_N chiral freezing, analytic lattice Weil-theta interior stabilization at L_15, and discriminant-15 genus rank-2 duality (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 0da7aeaef9d9848eba6e18bb59b4a49756bb5bdd
- kind: theorem
- touches: S02, P-629, P-630, P-845, P-882
- effect: conditions — S02, P-629, P-630, P-845, and P-882 (proves for every odd integer N >= 3 and every r in
  (Z/NZ)^x that tr rho_{N,r}(C_{3,omega}) = G_{N,3r} / conj(G_{N,r}) equals Jacobi(-3/N) if 3 does not divide N
  (d_1 - d_2 = 0) and +i sqrt(3) (r/3) if 3 | N (d_1 - d_2 = +2 (r/3)), with Gauss quadratic reciprocity
  (-3/m)(m/3) = +1 cancelling all m- and k-dependence across 220 checked (N, r) pairs through N = 49; proves the
  universal flip-trace identity tr(P_flip rho_{N,r}(C_{3,omega})) = +1 splitting d_1 - d_2 identically half-and-half
  between H_N^even and H_N^odd with spinor parity rho_{N,r}(-I)|_{H_N^even} = (-1/N) I; proves the complete all-odd-N
  mod-4 mirror dichotomy via anti-unitary M_a = U_a K commuting with W_hat_6 and C_{3,omega} iff every prime p | N
  satisfies p == 1 mod 4 (iso-spectral [5, 13, 17, 25, 29] vs split [3, 7, 9, 11, 15, 19, 21, 23, 27, 31, 33, 35])
  plus exact CRT rho_{15,1} ~= rho_{3,2} (x) rho_{5,2} and rho_{15,4} ~= rho_{15,1}; constructs the explicit unitary
  intertwiner Leg(5) ~= H_{5,2}^even (+) H_{5,1}^even from the PSL(2, F_5) central class sum K_5 (eigenvalues
  2 +- 2 sqrt(5)), proving exact SL(2, Z)-invariant Weil-triplet ratios R_5^wp(omega_+) = 1/4 (4/5 : 1/5) and
  R_5^wp(i) = 7/23 (23/30 : 7/30) and universal non-commutative chiral freezing of O_{27}^{(3,3,3)} x Weil_N onto
  Q_6 x Weil_N across G_3 (216 elements, 0 character defects) and m = 0..4 for N in {3, 5, 7, 15} with exact
  Q_6 x Weil_N moments m = 0..6 (including -108 sqrt(21) and -720 sqrt(21) at N = 7); constructs SL(2, Z)-equivariant
  even (weight 1) and odd-harmonic cusp (weight 2) lattice Weil-modular forms on L_N = [[2, 1], [1, (N+1)/2]] for
  N in {3, 7, 11, 15, 19} and non-principal genus partner L'_15 = [[4, 1], [1, 4]] (h(-15) = 2), proving exact
  equianharmonic chiral-sector locking at omega_+ (even -> q = 2, odd -> q = 1) and zero-parameter boundary-to-interior
  stabilization of V_odd(tau) = y^2 ||Th^odd(tau)||^2 (boundary max at omega_+ for L_7 and L'_15 vs strict 2D
  interior global max on Re(tau) = 0 with saddle on Re(tau) = 1/2 for L_11 at y* = 1.510994739, minimal chiral L_15
  at y* = 2.267789662 with V* = 0.1043626076, and L_19 at y* = 2.910076101); and proves exact discriminant-15 Genus
  Rank-2 Duality on CRT 3 x 5 SL(2, Z)- and Haar-invariant matrices (L_15: M_even rank 3, M_odd exact rank 2 via exact
  Q[[q^{1/15}]] A_2 x S_1(2I) identities A D + B C = 0, B T_{A2,0} = D T_{A2,1}, A T_{A2,0} = -C T_{A2,1}
  through q^4; L'_15: M_odd rank 3, M_even exact rank 2 via swap isometry j -> -4j = P_flip^{(3)}) together with the
  exact P_flip^{(3)} block-diagonal (J = 0) left-singular overlap obstruction on both classes)
- scope: frame: no frame (finite non-commutative Weil representations rho_{N,r} on C^N, signed-line representation
  Leg(5), Markoff trace orbit O_{27}^{(3,3,3)} and its 6-point quotient Q_6, and SL(2, Z)-equivariant rank-2 even
  lattice Weil-theta forms on H); object: all odd N in {3..49} for Gauss-sum chiral-index and flip-trace laws, all
  17 odd N in {3..35} for mod-4 spectral splitting, Leg(5) and Q_6 x Weil_N / O_{27}^{(3,3,3)} x Weil_N bundles,
  rank-2 lattices L_N (N in {3, 7, 11, 15, 19}) and L'_15 (h(-15) = 2), and CRT 3 x 5 Weil-theta matrices on F;
  reach: class; hypotheses: exact integer, rational, Q[[q^{1/15}]] polynomial, and 30-to-45-digit mpmath arithmetic
  with 5 planted fault controls, 10-trial Haar U(3) x U(5) basis scrambling, and zero float literals (strictly 0 of 19)
- identifications: none
- definitions: For odd N >= 3, inv2 = (N + 1)/2, zeta_N = exp(2 pi i / N), and r in (Z/NZ)^x, define the Gauss sum
  G_{N,a} = sum_{b=0}^{N-1} zeta_N^{a b^2}, G_r = G_{N, -r * inv2}, Weil shear L = diag_j(zeta_N^{r * inv2 * j^2}),
  symplectic transform (S_{inv})_{a,c} = G_r^{-1} zeta_N^{r a c}, R = S_{inv} L^H S_{inv}^H, order-3 operator
  C_{3,omega} = S_{inv}^H L^H, flip involution (P_flip)_{(-j) mod N, j} = 1, chiral projectors Pi_q = (I + omega^{-q}
  C_{3,omega} + omega^q C_{3,omega}^H)/3 (omega = exp(2 pi i/3)), W_hat_+ = sum_{j=0}^2 C_{3,omega}^j L C_{3,omega}^{-j},
  W_hat_- = W_hat_+^H, W_hat_6 = W_hat_+ + W_hat_-, W_hat_{ch} = -i(W_hat_+ - W_hat_-), and anti-unitary mirror
  M_a = U_a K where U_a |j> = |a j mod N> for a^2 == -1 mod N and K is complex conjugation. On P^1(F_5) ordered as
  l_1..l_6 = ((1,0),(0,1),(1,1),(1,2),(1,3),(1,4)), Leg(5) acts by M e_j = (s/5) e_i when M l_j = s l_i mod 5; K_5 =
  sum_{g in [L]_{PSL(2,F_5)}} rho_{Leg(5)}(g) yields orthogonal projectors P_a = (K_5 - (2 - 2 sqrt(5)) I)/(4 sqrt(5))
  and P_b = ((2 + 2 sqrt(5)) I - K_5)/(4 sqrt(5)), intertwining H_{5,2}^even (+) H_{5,1}^even with Leg(5), and
  SL(2, Z)-invariant Weil-triplet ratios R_5^wp(tau) = ||P_b Phi^wp(tau)||^2 / ||P_a Phi^wp(tau)||^2 and
  R_5^Siegel(tau) = ||P_b Phi^Siegel(tau)||^2 / ||P_a Phi^Siegel(tau)||^2 where Phi(tau) = rho(S) v(tau) with
  v_i = (F(l_i/5; tau) - F(2 l_i/5; tau))/sqrt(2) for F_Siegel(a,b;tau) = -ln|g_{a,b}(tau)| and F_wp(a,b;tau) =
  wp(a tau + b; tau). On (Z/27Z)^3, L_tr(x,y,z) = (x, z, x z - y), R_tr(x,y,z) = (z, y, y z - x), C_tr(x,y,z) =
  (y, z, x), Sig_tr(x,y,z) = (y, x, x y - z) generate G_3 (order 216) on O_{27}^{(3,3,3)} (72 points) with unique
  6-point block quotient Q_6 (|Fix(C_tr)| = 3), character rho: (L_tr, R_tr, C_tr, Sig_tr) -> (1, 5, 2, 3) mod 6, and
  diagonal bundle operators g_L = P_L (x) L, g_R = P_R (x) R, g_C = P_C (x) C_{3,omega}, W_6 = sum_{j=0}^2 g_C^j
  (g_L + g_R) g_C^{-j} on B x Weil_N (r = 1). For N == 3 mod 4, L_N has Gram matrix [[2, 1], [1, (N+1)/2]],
  Q(u, v) = u^2 + u v + c v^2 (c = (N+1)/4), dual cosets j e* = (2 c j/N, -j/N) mod Z^2, r_eff = (N+1)/2, even
  weight-1 form Th_{L_N, j}^even(tau) = sum_{(u,v) in L_N + j e*} q^{Q(u,v)} (q = exp(2 pi i tau)), odd weight-2
  cusp form Th_{L_N, j}^odd(tau) = sum_{(u,v) in L_N + j e*} (u + v alpha) q^{Q(u,v)} (alpha = (1 + i sqrt(N))/2),
  and V_odd(tau) = (Im tau)^2 ||Th^odd(tau)||^2; non-principal L'_15 has Gram [[4, 1], [1, 4]], Q'(u, v) =
  2 u^2 + u v + 2 v^2, cosets j e'* = (4 j/15, -j/15) mod Z^2, r_eff = 4, and P^odd(u, v) = u + v beta (beta =
  (1 + i sqrt(15))/4). CRT reshaping maps v in C^{15} to M in C^{3 x 5} via M[j mod 3, j mod 5] = v_j, with descending
  singular values and left-singular overlap V_{3x3} = U_even^H U_odd, Jarlskog J = Im(V_00 V_11 conj(V_01 V_10)), and
  L_15 odd q-series ser[j] = Th_{L_15, j}^odd / (i sqrt(15)/2) with A = ser[6], B = ser[3], C = ser[1] - ser[4],
  D = ser[7] + ser[2], and A_2 lattice series T_{A2, 0}, T_{A2, 1}.
- imports: none
- premises on main: B371, B377, B381, B1262, B1934, B1992, B1993, B2008, P-629, P-630, P-845, P-882
- decisive script: relays/a2_weil_chiral_lattice_bridge/a2_weil_chiral_lattice_bridge_decisive.py, SHA-256 8f04ea23e2b0a7e5,
  depends on the standard library, mpmath and sympy, run as
  python3 relays/a2_weil_chiral_lattice_bridge/a2_weil_chiral_lattice_bridge_decisive.py, output SHA-256 d3a8ef4748420938
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 d3a8ef4748420938
- failing control: python3 relays/a2_weil_chiral_lattice_bridge/a2_weil_chiral_lattice_bridge_control.py
- second computation: fam3-v1-high-03 disjoint cold-room referee
  relays/a2_weil_chiral_lattice_bridge_referee/referee_a2_weil_chiral_lattice_bridge.py (SHA-256 720de274d74b9099,
  output 4547948835979f46, stdout cf1a8609f3edee5d, cross-diff 823b94d05c5819cf, blind pre-commits a2e0ca679 and
  9011a5f26, unread output sealed at 905883933, verdict at 0da7aeaef) using SymPy Q[x]/(Phi_N(x)) cyclotomic proofs
  and 50-digit momentum-basis Weil sweeps, 12-ray involution Leg(5) with simultaneous (W_6, W_ch, C_3) intertwining,
  -d^2/dz^2 ln jtheta(1) Weierstrass and jtheta(1)/pentagonal-eta Siegel units, <C_tr, Sig_tr>-orbit Q_6 freezing,
  branch-free completed-square 1D Jacobi-theta lattice forms with golden-section + secant + 5-point Richardson 2D
  Hessians, SymPy Poly Q[[q^{1/15}]] factorization through t^60, non-squaring 8x8 Hermitian Jordan-Wielandt SVD, and
  10-trial LCG128 Householder Haar U(3) x U(5) scrambling: 322/322 matched, 0 discrepancies (VERDICT: PASS)
- already on main?: topic_sweep.py "P_flip|L_15|L'_15|K_5.*Leg|Weil.*Leg\(5\)|Q_6 x Weil|O_27 x Weil|rank-2.*L_15" on
  origin/main (9c8b0a531): VERDICT 0 of 1759 arcs on main match (none) and 0 register rows match (none); B371, B377,
  B381, B1934 studied level-3 and level-5 Weil reps before the 6-move walk, B1262 settled h(-15) = 2 without Weil-theta
  modular forms or CRT rank duality, and B2008 studied classical mirror symmetry without non-commutative Weil lattices
- what would make it fail: any residual > 1e-35 on tr rho_{N,r}(C_{3,omega}), tr(P_flip C_{3,omega}) - 1, or CRT
  rho_{15,1} ~= rho_{3,2} (x) rho_{5,2}, or any mismatch with the all-odd-N mod-4 prime-factor criterion across
  N in {3..35}, or any Leg(5) intertwining error > 1e-38 or deviation from R_5^wp(omega_+) = 1/4 or R_5^wp(i) = 7/23,
  or any nonzero G_3 character defect or O_27 - Q_6 chiral-moment difference > 1e-25, or any lattice Weil-theta
  SL(2, Z) equivariance error or omega_+ sector leak > 1e-35, or any failure of boundary max (L_7, L'_15) vs strict 2D
  interior max at x = 0 and saddle at x = 1/2 (L_11, L_15, L_19), or any nonzero Q[[q^{1/15}]] residual or rank-duality
  or Haar invariance violation, or any of 5/5 planted controls or the standalone exit-1 control failing
