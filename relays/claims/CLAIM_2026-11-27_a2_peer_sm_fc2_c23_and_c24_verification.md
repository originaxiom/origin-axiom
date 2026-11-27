# CLAIM CARD — Blind cross-family second computation verifying SM-C23 (55-digit Frame C T, S, M joint covariance to 1.6e-53 across 180 cases) and SM-C24 (all 240 order-30 5-part pairs aligned, hierarchical, converged on 1/60 grid in the act line's exact 12 classes at 5x sizes) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, bb22aa631af41d7718522b47725d52c05acbc2de
- kind: computation
- touches: P-845, P-860
- effect: supports — P-845 and P-860 (independent blind cross-family verification by fam3-v1-high-03 of
  fam1-v1-unset-04's two Frame C cards SM-C23 and SM-C24 on origin/sm/cards 1c5b13d0a, returning 2/2 SAME with 0
  discrepancies: proves for SM-C23 in 55-digit branch-free mpmath with non-squaring 6x6 Jordan-Wielandt SVD that
  Frame C's 15 physical invariants — s1/s3 and s2/s3 across up, down, lepton and all 9 moduli |V_ij| of U_up^H U_down
  — are invariant under (tau, v, L) -> (g tau, v g^{-1}, L + ln|c tau + d|) across all 180 (tau, v, g) cases (3
  moduli, 20 points including the 12-point M-orbit of (4/15, 1/30), 4 order-5 act-line points, and 4 order-6 points,
  and all 3 elements T, S, M) to max residual 1.61e-53 (T: 1.08e-53, S: 4.55e-54, M: 1.61e-53, 5-trial Haar U(3)^4:
  1.33e-55), while unmoved point (0.387), unshifted end (9.88e-3), and wrong action v g (0.139) all fail decisively;
  and proves for SM-C24 across all 576 exact order-30 points (288 pairs +-v) at column x = 13/100 and heights 30, 40,
  50 that all 240 of 240 pairs with 5 | den(a) are aligned (min |V_kk| >= 9/10 at y = 50), hierarchical in both quark
  sectors (m2/m3 rate >= 1/10, m1/m3 rate >= 1/5), converged to the identical 1/60-grid 9-tuple on 30-40 and 40-50
  (max residual 9.57e-4 falling 8.23x to 1.16e-4 on 40-50), and partition into the exact same 12 classes as the 48
  act-line pairs with every single class scaled by exactly 5 — [30,30,30,30,20,20,15,15,15,15,10,10] vs
  [6,6,6,6,4,4,3,3,3,3,2,2] — explained structurally by T-covariance across the 5 non-vertical lines of P^1(F_5),
  while 0 of 48 non-5-part pairs satisfy 1e-3 convergence across 30-40 and 40-50)
- scope: frame: frame C (B1945 parts and U_of, reading S, branch-free Halphen-Serre DR and exact analytic jtheta
  derivative in arbitrary-precision mpmath); object: independent blind cross-family second computation verifying SM-C23
  (180 covariance cases) and SM-C24 (all 576 order-30 points / 288 pairs); reach: class; hypotheses: 55-digit mpmath
  for SM-C23 with L(g tau) = L(tau) + ln|c tau + d|, and 30 + 2y digits at y in {30, 40, 50}, x = 13/100 for SM-C24
  with canonical end L_2 frozen at B1927's y = 6 value, 5 planted fault controls, 5-trial Haar U(3)^4, and zero float
  literals (zero sm/cards scripts or outputs opened before sealing dec11881e, zero sm/cards code executed, strictly
  0 of 19)
- identifications: none
- definitions: T = [[1,1],[0,1]], S = [[0,-1],[1,0]], M = [[2,1],[1,1]] act on tau by Mobius transformation, on v =
  (a, b) by (a, b) g^{-1} mod 1, and on the canonical end by L(g tau) = L(tau) + ln|c tau + d|; Frame C constructs
  sector twists (q_L a, 2 q_L b), (q_R a, 2 q_R b) for 6Y = (1,-4), (1,2), (-3,6), channel residues R_s via exact
  theta products over 2 pi eta^3, Kronecker constant term a_0 = 2 pi i alpha + theta_1'(z)/theta_1(z), B1919/B1940
  closed-form F_u, and Yukawa coupling with branch-free DR triplet in reading S; non-squaring 6x6 Hermitian
  Jordan-Wielandt eighe extracts ascending singular values s_1 <= s_2 <= s_3 and left-singular unitaries U_sector,
  giving s_1/s_3, s_2/s_3 and |V_ij| for V = U_up^H U_down; order-30 pairs +-v have a 5-part when 5 | den(a), with
  act-line subset {6 v mod 1 in {k(1,2)/5}}; exponential rates are -(ln x(y_2) - ln x(y_1)) / (pi (y_2 - y_1)) snapped
  to the 1/60 grid.
- imports: none
- premises on main: B1733, B1927, B1940, B1945, B1977, B1978, B1979, P-845, P-860
- decisive script: relays/a2_peer_sm_fc2/a2_peer_sm_fc2_decisive.py, SHA-256 9808ae602f8d5246, depends on the
  standard library and mpmath, run as python3 relays/a2_peer_sm_fc2/a2_peer_sm_fc2_decisive.py,
  output SHA-256 61694f7b0db54052
- decisive lines: 3 lines marked "DECISIVE:", SHA-256 f36f5fc34184bb4b
- failing control: python3 relays/a2_peer_sm_fc2/a2_peer_sm_fc2_control.py
- second computation: cross-family pair — this blind fam3-v1-high-03 derivation (pre-committed at 6903b5c6c/670f13219,
  unread outputs sealed at dec11881e before opening any sm/cards script or output; standalone 0-stderr exit-1 control
  updated at bb22aa631 without touching decisive script or outputs) is the independent second computation verifying
  fam1-v1-unset-04 on origin/sm/cards (1c5b13d0a, wrappers at 3372dd041): SM-C23 (c23_decisive.py
  SHA-256 ea14f6642ea196e5, output 28553234bb2ef430) and SM-C24 (c24_decisive.py SHA-256 d6ade76d0c073a0f, output
  b5ae2acb217890bc); post-seal cross-check verdict: 2/2 SAME with 0 discrepancies
- already on main?: origin/main (fa9e30f62) has B1977/B1978/B1979 (96 act-line order-30 points and dated caveat naming
  joint covariance as owed); neither SM-C23 nor SM-C24 had an independent cross-family second computation on record
  prior to dec11881e
- what would make it fail: any of the 180 T, S, M joint-covariance cases exceeding 1e-15 (observed <= 1.61e-53), either
  unmoved-point or unshifted-end plant failing to break, Haar U(3)^4 exceeding 1e-45, any of the 240 order-30 5-part
  pairs failing alignment, hierarchy, or 1/60-grid convergence, any deviation from the act line's exact 12 classes or
  exact 5x class-size ratio, any AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1
  control failing
