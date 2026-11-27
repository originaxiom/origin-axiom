# CLAIM CARD — Blind cross-family second computation verifying SM-R581 (1,199 <=6-tet census manifolds independently extracted from SnapPy, 384/1199 = 0.3203 E_6/2T route rate, 400/400 B993 match, and manifold-independent Z_6, Y, 3/8 structural package) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 33e376ee4b69446cb553aecfcdd9143553b42df5
- kind: computation
- touches: P-581, I-9
- effect: supports — P-581 and I-9 (independent blind cross-family verification by fam3-v1-high-03 of fam1-v1-unset-04's
  card SM-R581 on origin/sm/cards 1c5b13d0a, returning SAME with 0 discrepancies: independently extracts all 1,199
  orientable one-cusped hyperbolic census manifolds with <= 6 ideal tetrahedra from SnapPy 3.3.2 — 1,041 two-generator
  and 158 three-generator presentations — and proves via exact multiplication tables and full automorphism groups
  |Aut(2T)| = 24, |Aut(2O)| = 48, |Aut(2I)| = 120 that exactly 384 of 1,199 (0.3203) admit a surjection onto 2T =
  SL(2, 3), 304 of 1,199 (0.2535) carry m004's exact count of 2 Aut(2T)-classes, 362 of 1,199 (0.3019) surject onto
  2O, 609 of 1,199 (0.5079) surject onto 2I = SL(2, 5), m004 has exact counts (2T=2, 2O=0, 2I=0), all 400 of 400 B993
  control manifolds match per-object, plant pi_1 ->> Z/3 holds on 1,199 of 1,199 with exact count 3^d - 1, and plant
  pi_1 ->> (Z/2)^3 fails on 1,041 of 1,041 two-generator presentations; independently proves all three post-E_6 steps
  take zero manifold input — kernel of SU(3) x SU(2) x U(1) -> S(U(3) x U(2)) is cyclic Z_6 (orders [1,2,3,3,6,6]),
  traceless commutant of su(3) (+) su(2) in su(5) is 1-dimensional and spanned by diag(2, 2, 2, -3, -3), and
  Tr(T_3^2)/Tr(Q^2) = 3/8 on the 5 — confirming all three structural grades collapse to the single 2T route rate
  384/1199)
- scope: frame: F-MC (McKay cascade at the group level, matching B993); object: independent blind cross-family second
  computation verifying SM-R581 across all 1,199 orientable one-cusped hyperbolic census manifolds with <= 6 ideal
  tetrahedra; reach: class; hypotheses: census presentations independently extracted from SnapPy 3.3.2 and frozen in
  relays/a2_peer_sm_r581/a2_r581_snappy_presentations.json, exact integer/Z[sqrt(2)] group tables and SymPy linear
  algebra with 5 planted fault controls and zero float literals (zero sm/cards scripts, presentations, or outputs
  opened before sealing 33e376ee4, zero sm/cards code executed, strictly 0 of 19)
- identifications: I-9 (structural package Z_6, hypercharge direction, and Tr(T_3^2)/Tr(Q^2) = 3/8 read as
  manifold-independent consequences of the E_6/2T route)
- definitions: Rule K is every orientable one-cusped hyperbolic census manifold with <= 6 ideal tetrahedra in census
  order (N = 1,199); 2T = SL(2, F_3) (order 24), 2O in exact Z[sqrt(2)]/2 quaternions (order 48), and 2I = SL(2, F_5)
  (order 120) have exact full automorphism groups Aut(G) of orders (24, 48, 120); surjections pi_1(M) ->> G are
  counted exhaustively modulo Aut(G) using Aut(G)-orbit symmetry breaking and exact relator evaluation; Z/3 plant
  counts nonzero homomorphisms to F_3 against 3^d - 1 with d = dim_{F_3} H_1(M; F_3); (Z/2)^3 plant tests dim_{F_2}
  H_1(M; F_2) >= 3; post-E_6 steps solve (a/3 + 2x, b/2 - 3x) in Z^2 for Z_6, exact SymPy nullspace [X, T_a] = 0 and
  Tr(X) = 0 in 5x5 matrices for diag(2, 2, 2, -3, -3), and exact Fraction Tr(T_3^2)/Tr(Q^2) on the 5 with T_3 =
  diag(0,0,0,1/2,-1/2) and Y = (-1/6) diag(2,2,2,-3,-3).
- imports: orientable one-cusped hyperbolic census presentations with <= 6 ideal tetrahedra independently extracted from
  SnapPy 3.3.2 and frozen in relays/a2_peer_sm_r581/a2_r581_snappy_presentations.json (SHA-256 b45e3ab7d860a3f7,
  standard library only at rerun time)
- premises on main: B727, B861, B862, B993, B996, B1160, P-581, I-9
- decisive script: relays/a2_peer_sm_r581/a2_peer_sm_r581_decisive.py, SHA-256 549c644b9b1ba459, depends on the
  standard library and sympy, run as python3 relays/a2_peer_sm_r581/a2_peer_sm_r581_decisive.py,
  output SHA-256 a1bdd0c377dac2e0
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 a1bdd0c377dac2e0
- failing control: python3 relays/a2_peer_sm_r581/a2_peer_sm_r581_control.py
- second computation: cross-family pair — this blind fam3-v1-high-03 derivation (pre-committed at 6c969e7a6/7e2208d35,
  unread outputs sealed at 33e376ee4 before opening any sm/cards file) is the independent second computation verifying
  fam1-v1-unset-04 on origin/sm/cards (1c5b13d0a, wrapper at 3372dd041): SM-R581 (r581_decisive.py
  SHA-256 38d9ba2d8c1427c7, output ee162149c5ac17e5); post-seal cross-check verdict: SAME with 0 discrepancies across
  all 1,199 manifolds (384/304/362/609), all 400/400 B993 controls, both plants, and all 3 post-E_6 steps
- already on main?: origin/main (fa9e30f62) has B993 (2T rate on the first 400 2-generator manifolds only, 37.2%) and
  B862/B1160 (Z_6 and hypercharge separately); SM-R581 had no independent cross-family second computation over the
  full 1,199 <=6-tet class prior to 33e376ee4
- what would make it fail: census size != 1,199, E_6/2T count != 384, m004 2T classes != 2, any discrepancy on the 400
  B993 control manifolds, Z/3 plant rate < 1 or off 3^d - 1, (Z/2)^3 holding on any 2-generator presentation, any
  failure of Z_6 kernel, 1D diag(2,2,2,-3,-3) commutant, or Tr(T_3^2)/Tr(Q^2) = 3/8, any AST/JSON float literal, or
  any of 5/5 planted controls or the standalone exit-1 control failing
