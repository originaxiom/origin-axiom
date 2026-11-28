# CLAIM CARD — Discriminant-15 Weil-lattice P_flip^(3) protection vs Heisenberg Z_3 chiral-flux J != 0 unlocking (breaking SL(2, Z) to T^3), coupled E_8 group (156,000, ab Z/2) and complete 15,625-point F_25 Markoff variety, and prime-2/3/5 B704 Galois seam (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 70fcaf1f963d859fb20adb55827ae9672a9a282e
- kind: theorem
- touches: P-882, P-876, P-374
- effect: conditions — P-882, P-876, and P-374 (bridges the 3^k Markoff-weave tower, the discriminant-15 Weil genus
  pair (L_15, L'_15), and the coupled E_8 two-register group G_E8 = SL(2, F_25) *_{Z/2} BD_5: proves at 45-digit
  branch-free mpmath precision with non-squaring 8x8 Hermitian Jordan-Wielandt SVD and 10-trial Haar U(3)_L x U(5)_Re x
  U(5)_Ro basis scrambling (max drift 2.47e-44) that every operator in C[rho_{3,2}(SL(2, F_3))] commutes with central
  P_flip^(3) = rho_{3,2}(-I) and strictly protects Jarlskog J = 0 (<= 1.57e-92) on L_15, L'_15, and cross-genus
  L_15^even x L'_15^odd, and mirror-symmetric Heisenberg Z_3 walk S_heis = T_3 + T_3^{-1} (flux angle 0) likewise
  protects J = 0 (<= 5.56e-93), whereas the B2008-type Heisenberg Z_3 Hermitian chiral flux H_Heis(pi/9) = e^{i pi/9}
  T_3 + e^{-i pi/9} T_3^{-1} (eigenvalues 2 cos(pi/9 + 2 pi q/3) to 3.94e-46) and its P_flip^(3)-anticommuting
  generator H_ch = -i(T_3 - T_3^{-1}) natively unlock J != 0 across both genus classes — parity-split unitary
  exp(+-i (pi/9) H_ch) gives |J| = 0.011776096316519 on L_15, 0.0055363298254893 on L'_15, and 0.0075956075064383
  cross-genus, and even the identical positive Hermitian operator 3I + H_Heis(pi/9) on both sectors gives |J| =
  0.00071640799684004 on L_15 and 0.00029057607996953 on L'_15 — at the exact Rung-3 cost of breaking T (dJ_T =
  1.77e-3, dV_T = 0.302) and S (dJ_S = 1.07e-2, dV_S = 0.629) while preserving T^3 (level-3 periodicity) identically
  to 2.22e-46 (dV_T3 = 2.41e-45); proves exact group structure |SL(2, F_25)| = 15,600 (perfect, -I_2 a single Q_8
  commutator), |G_E8| = 156,000, |Z(G_E8)| = 2, |[G_E8, G_E8]| = 78,000, and |G_E8^ab| = 2 (central identification
  collapsing BD_5^ab = Z/4 to Z/2); generalizes B1983 across all 15,625 points and all 25 leaves kappa in F_25 of
  x^2 + y^2 + z^2 - x y z = 2 + kappa, proving exact kappa conservation, exactly 2 global <L, R> fixed points ((0,0,0)
  on kappa = -2 and (2,2,2) on kappa = 2), swap-P orbit invariance across all 25 leaves, and the exact 4-orbit subgroup
  partition [600, 60, 40, 1] of the 701-point F_25 cusp leaf kappa = -2 into SL(2, F_25) (600, single connected orbit
  containing m004's Riley fiber point), 2I.2 = SL(2, F_5).2 (60, order 240), 2I = SL(2, F_5) (40, all nonzero F_5
  points), and Q_8 (1, origin), with Frobenius Gal(F_25/F_5) fixing all 4 orbits setwise; and proves exact finite-group
  Hom/Surj tables across Q_3 = S_3 x Z_3 (18), 2T (24), and BD_5 (20) showing Q_3 and BD_5 couple exclusively through
  Z/2 (img sizes {1, 2}), BD_5 and 2T both embed faithfully in SL(2, F_5) <= SL(2, F_25) while Q_3 is Lagrange-
  obstructed from embedding in SL(2, F_25) and G_E8 (v_3(156000) = 1 < 2), and symbolically proves over Q the B704
  multiquadratic Galois cube Gal(Q(sqrt(-3), sqrt(5), sqrt(-7))/Q) = (Z/2)^3 (irreducible deg-8 polynomial x^8 + 20 x^6
  + 382 x^4 - 3900 x^2 + 19881) and V_4 plane Q(sqrt(-3), sqrt(5)) (deg-4 polynomial x^4 - 4 x^2 + 64))
- scope: frame: CRT 3 x 5 Weil-theta matrices on discriminant-15 genus lattices L_15 and L'_15 coupled to level-3 Weil
  and Heisenberg Z_3 operators, finite group G_E8 = SL(2, F_25) *_{Z/2} BD_5 and the 15,625-point F_25 Fricke character
  variety, and finite-group/multiquadratic Galois coupling of Q_3, 2T, BD_5, SL(2, F_25), and B704; object: exact
  protection vs unlocking of Jarlskog J and T/T^3/S covariance on (L_15, L'_15), exact orbit and subgroup classification
  of all 25 F_25 Markoff leaves, and exact Hom/Surj, embedding, and Q-irreducibility certificates; reach: class;
  hypotheses: 45-digit branch-free mpmath with non-squaring 8x8 Jordan-Wielandt SVD, 10-trial Mezzadri QR Haar U(3)_L x
  U(5)_Re x U(5)_Ro scrambling, exact F_25 = F_5[d]/(d^2 - 2) and sympy Q arithmetic, 5 planted fault controls, zero
  float literals (independently cross-checked with 0 discrepancies at 9aa4873b9 by a zero-shared-code same-family
  Cold-Room Referee using 55-digit completed-square 1D mp.jtheta, mp.svd_c, mp.expm, Householder+Cayley Haar,
  F_5[t]/(t^2 - 3), Hurwitz-quaternion 2T, F_11-matrix BD_5, direct 8-conjugate symbolic expansion, and 5/5 RPF;
  strictly 0 of 19)
- identifications: none
- definitions: On L_15 (Gram [[2, 1], [1, 4]], Q(u, v) = u^2 + u v + 4 v^2, cosets j*(8/15, -1/15)) and L'_15 (Gram
  [[4, 1], [1, 4]], Q'(u, v) = 2 u^2 + u v + 2 v^2, cosets j*(4/15, -1/15)), Th^even(tau) and Th^odd(tau) are summed
  with branch-free exp(2 pi i tau Q) and reshaped via CRT M[j mod 3, j mod 5] = v_j into C^{3 x 5}; non-squaring 8x8
  Jordan-Wielandt SVD yields descending singular values and left unitaries U_e, U_o, overlap V = U_e^H U_o, and
  J = Im(V_00 V_11 conj(V_01 V_10)). On C^3, (P_flip^(3))_{(-j) mod 3, j} = 1, (T_3)_{(j+1) mod 3, j} = 1,
  S_heis = T_3 + T_3^H, H_ch = -i(T_3 - T_3^H), H_Heis(alpha) = e^{i alpha} T_3 + e^{-i alpha} T_3^H, and unitary flux
  U_ch(alpha) = exp(i alpha H_ch). Over F_25 = F_5[d]/(d^2 - 2), Fricke moves L(x, y, z) = (x, z, x z - y),
  R(x, y, z) = (z, y, y z - x), and P(x, y, z) = (y, x, z) conserve kappa = x^2 + y^2 + z^2 - x y z - 2; G_E8 =
  (SL(2, F_25) x BD_5)/<(-I_2, j^2)>; Q_3 = S_3 x Z_3 (order 18); 2T = SL(2, F_3) (order 24); BD_5 = Z_5 rtimes Z_4
  (order 20).
- imports: none
- premises on main: B704, B1983, B2008, P-374, P-876, P-882
- decisive script: relays/a2_weave_e8_weil_seam/a2_weave_e8_weil_seam_decisive.py, SHA-256 423abceeb86bb463, depends on
  the standard library, mpmath and sympy, run as python3 relays/a2_weave_e8_weil_seam/a2_weave_e8_weil_seam_decisive.py,
  output SHA-256 9280fba7e8779a76
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 9280fba7e8779a76
- failing control: python3 relays/a2_weave_e8_weil_seam/a2_weave_e8_weil_seam_control.py
- second computation: none
- already on main?: git grep across origin/main (be47862d1) finds B704 (multiquadratic Galois seam), B1983 (F_p Markoff
  orbits for prime p <= 47 only, not F_25), B2008 (open sourced-handedness question on the 3^k tower), and P-876; no
  arc on main couples Heisenberg Z_3 chiral flux to L_15/L'_15, computes the 15,625-point F_25 Markoff variety and
  [600, 60, 40, 1] cusp-leaf subgroup partition, or proves the Q_3/BD_5/2T/SL(2, F_25) coupling and Lagrange obstruction
- what would make it fail: any SL(2, F_3) or theta=0 Heisenberg operator producing |J| > 1e-35 on (L_15, L'_15), any
  Haar U(3)_L x U(5)^2 drift > 1e-30, any deviation from T^3 preservation (< 1e-40) or T/S breaking under Heisenberg
  chiral flux, any deviation from |G_E8| = 156,000, |G_E8^ab| = 2, 2 global fixed points, swap-P invariance across all
  25 F_25 leaves, or cusp-leaf [600, 60, 40, 1] subgroup partition [SL(2,F_25), 2I.2, 2I, Q_8] with m004 in the 600
  orbit, any Q_3 <-> BD_5 homomorphism with image size outside {1, 2} or failure of B704 deg-8/deg-4 irreducibility,
  any AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1 control failing
