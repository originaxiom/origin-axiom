# CLAIM CARD — Blind cross-family second computation verifying SM-R384 (2/5 cusp and universal Galois bit), SM-R614 (E_6 27 singlet discrete remnant and Spin(10)/SU(5) stabilizers), and SM-R635 (boundary-free ad Q_8 cohomology, kappa Hessian diag(8,8,8), and all-4-lift m004 monodromy) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, e4bc5685ebd54e6af1491e1edbca744fb52bb112
- kind: theorem
- touches: P-384, P-845, P-614, P-414, P-157, P-635, P-567
- effect: supports — P-384, P-845, P-614, P-414, P-157, P-635, and P-567 (independent blind cross-family verification
  by fam3-v1-high-03 of fam1-v1-unset-04's three pure-math cards SM-R384, SM-R614, and SM-R635 on origin/sm/cards
  1c5b13d0a, returning 3/3 SAME with 0 discrepancies and discharging door rule D7 cross-family on negative card
  SM-R384: proves on all 266 lines of order <= 12 and 36 lines of order 10 that K = {(2/5, odd/10)} of size 5 is one
  <T, -I>-cusp, is NOT unit-closed because u = 3 in (Z/10Z)^x universally maps K onto K' = {(1/5, odd/10)} giving unit
  closure size 10, least_level = 10 breaks (L, e) = (Q, d)^T mod N, Pi selects exact K (5), Pi_inv selects K union K'
  (10, 1 Galois bit), and 0/14 unit-invariant rules select K; proves from an independent Bourbaki E_6 Cartan (72 roots,
  78-dim adjoint, 27 weights) exact eta = (3 chi - 5 psi)/4 with nu^c = N = -5, trivial exact Smith Normal Form
  discrete residual (order 1) in V_5 = V_SM + R*eta (and full R^6) for {nu^c}, {N}, and {nu^c, N}, exp(2 pi i eta/5) in
  G_SM, zero V_5 matter-parity solutions because L and H_d carry identical (1, 2, -1/2, +1) charges under SM x U(1)_eta
  (vs 20 in full R^6 for N alone and 0 for nu^c or both), compact E_6 stabilizers Spin(10) (dim 45, rank 5, 40 roots)
  for N and for nu^c (with w_N - w_{nu^c} an E_6 root preserving Spin(10) on any single-27 combination) vs SU(5)
  (dim 24, rank 4, 20 roots) for St(nu^c) cap St(N), and E5 mod-2 census 16 total (15 nontrivial), 2 SM-commuting (1
  nontrivial), 0 matter parity; and proves via exact symbolic SymPy Fox calculus on rho(a) = Q_I, rho(b) = Q_J,
  rho(c) = -I_2 that dim H^0 = 0, dim H^1(Z^2; ad Q_8) = 0, dim H^1(F_2; ad Q_8) = 3, dim H^1_par = 0, boundary
  restriction rank is 3 on ad Q_8 vs 0 on trivial u(1) lines, symbolic kappa(s) satisfies kappa(0) = -2,
  grad kappa(0) = 0, and H_kappa(0) = diag(8, 8, 8) positive definite, and m004 monodromy a -> ab, b -> bab yields
  characteristic polynomial t^3 - 1 and dim ker(phi^* - I) = 1 across all 4/4 SO(3) conjugators P)
- scope: frame: no frame (lines of (Q/Z)^2/{+-1} of order <= 12, Bourbaki E_6 root system and fundamental 27, and flat
  SU(2) representation rho(a) = Q_I, rho(b) = Q_J on Z^2 and F_2 with m004 monodromy); object: independent blind
  cross-family second computation verifying SM-R384, SM-R614, and SM-R635 from origin/sm/cards (1c5b13d0a); reach:
  class; hypotheses: exact Fraction, integer Smith Normal Form, and symbolic SymPy arithmetic with 5 planted fault
  controls and zero float literals (zero sm/cards scripts or outputs opened before sealing e4bc5685e, zero sm/cards
  code executed, strictly 0 of 19)
- identifications: none
- definitions: For V1 (SM-R384): a line is v = (a, b) in (Q/Z)^2 modulo +-1 of order lcm(den(a), den(b)); T(a, b) =
  (a, b - a) generates <T, -I>-cusps; K = {(2/5, odd/10)} and K' = {(1/5, odd/10)} = 3 K; a rule is unit-invariant if
  its selected set is closed under v -> u v for all u in (Z/NZ)^x; least_level is the least multiple of 5 where
  (-3, 6) is not (1, 2) transposed mod N; Pi selects order 10 with 3a == +-1/5 mod 1 and Pi_inv selects order 10 with
  3a in (1/5)Z/Z \ {0}. For V2 (SM-R614): Bourbaki E_6 Cartan matrix constructs all 72 roots and the 27 weights of
  V(omega_1); psi = 3 * coweight(node 1), chi and Y are solved as Cartan directions of SU(5) in D_5 and SU(3) x SU(2)
  in SU(5) matching B1303, and eta = (3 chi - 5 psi)/4 (-2 on Q, u^c, e^c; +1 on d^c, L, H_d, Dbar; -5 on nu^c, N; +4
  on H_u, D); V_SM = SU(3) x SU(2) coroots + R Y and V_5 = V_SM + R eta; discrete residual is {x in V : w.x in Z} /
  ((V cap ker w) + (V cap Z^6)) computed by exact integer Smith Normal Form; matter parity is a torus element commuting
  with SU(3) x SU(2), fixing the vev set, -1 on Q, u^c, d^c, L, e^c and +1 on H_u, H_d; compact E_6 stabilizers are
  computed from explicit Chevalley root-space actions on the 27; E5 enumerates h in F_2^6 with h.nu^c = h.N = 0 mod 2.
  For V3 (SM-R635): flat SU(2) holonomy rho(a) = Q_I = -i sigma_1, rho(b) = Q_J = -i sigma_2, rho(c) = rho(a b a^{-1}
  b^{-1}) = -I_2 acts on su(2) = R^3 by Ad rho; Z^1, B^1, H^1 = Z^1/B^1, and H^1_par = {u in Z^1 : u(c) in (Ad rho(c)
  - I)R^3}/B^1 are computed by exact Fox derivatives; A(s) = Q_I exp(s_1 Q_I) exp(s_3 Q_K), B(s) = Q_J exp(s_2 Q_J),
  kappa(s) = tr(A B A^{-1} B^{-1}); monodromy phi(a) = ab, phi(b) = bab induces phi^*(u)(x) = P u(phi(x)) on H^1(F_2;
  ad Q_8) for each P in SO(3) solving P Ad rho(phi(x)) P^{-1} = Ad rho(x).
- imports: none
- premises on main: B299, B1303, B1415, B1656, B1723, B1733, B1753, B1805, B1836, B1934, B1943, P-157, P-384,
  P-414, P-567, P-614, P-635, P-845
- decisive script: relays/a2_peer_sm_pure3/a2_peer_sm_pure3_decisive.py, SHA-256 dc8eaa5218af0d7e, depends on
  the standard library and sympy, run as python3 relays/a2_peer_sm_pure3/a2_peer_sm_pure3_decisive.py,
  output SHA-256 8f726fa2e192247f
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 8f726fa2e192247f
- failing control: python3 relays/a2_peer_sm_pure3/a2_peer_sm_pure3_control.py
- second computation: cross-family pair — this blind fam3-v1-high-03 derivation (pre-committed at 819fe7129, unread
  outputs sealed at e4bc5685e before opening any sm/cards script or output) is the independent second computation
  verifying fam1-v1-unset-04 on origin/sm/cards (1c5b13d0a, wrappers at 3372dd041): SM-R384 (r384_decisive.py
  SHA-256 34577bcb3df465e7, output e5d72a6aacd26824, kind: negative, D7 discharged), SM-R614 (r614_decisive.py
  SHA-256 f2917147ad628e55, output 1277c472aa46f61e), and SM-R635 (r635_decisive.py SHA-256 75501d78f067cd24, output
  619e5931ac37bf8c); post-seal cross-check verdict: 3/3 SAME with 0 discrepancies
- already on main?: origin/main (fa9e30f62) has B1753/B1934 (lines without the single-cusp or universal u=3 Galois-bit
  proof), B1303/B1805 (27 table without the SNF discrete residual, E_6 stabilizers, or E5 census), and B1836 (0/0/3
  dimensions without boundary restriction rank, symbolic kappa Hessian, or m004 monodromy); none of SM-R384, SM-R614,
  or SM-R635 had an independent cross-family second computation on record prior to e4bc5685e
- what would make it fail: any count mismatch in V1 (total != 266, ord-10 != 36, |K| != 5, K not a single cusp, K
  unit-closed, least_level != 10, Pi != K, Pi_inv != 10, or any unit-invariant rule selecting K), any failure in V2
  (27 table mismatch, eta(nu^c) != eta(N), nontrivial V_5 SNF residual, exp(2 pi i eta/5) outside G_SM, matter parity
  in V_5, stabilizer dims/ranks deviating from (45, 5)/(24, 4), or E5 != (16, 0)), any failure in V3 (cohomology dims
  deviating from (0, 0, 3, 0), boundary restriction rank != 3 on ad Q_8 or != 0 on lines, kappa(0) != -2, H_kappa(0)
  != diag(8, 8, 8), or any of the 4 SO(3) conjugators giving dim ker(phi^* - I) != 1), any AST or JSON float literal,
  or any of 5/5 planted controls or the standalone exit-1 control failing
