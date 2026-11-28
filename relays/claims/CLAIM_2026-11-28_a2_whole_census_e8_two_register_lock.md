# CLAIM CARD — Whole-census coupled E_8 two-register kernel-collapse theorem across all 1,199 orientable 1-cusped hyperbolic manifolds (<= 6 tetrahedra) and m000: C_4 iff 128-spinor silence, basis-invariant H^1(T^2; Z/2Z) 248-lock (38 of 1,041 2-gen, 10 with 2T, 6 with H_1 = Z and 2T == 2) (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 8353ff8544522264bb019f7f9abc39d35a9d176c
- kind: computation
- touches: P-876, P-581, I-9
- effect: supports — P-876 and conditions — P-581, I-9 (generalizes the coupled compact E_8 two-register mechanism
  from m004 to the entire 1,199-manifold orientable 1-cusped hyperbolic census at <= 6 tetrahedra plus non-orientable
  m000: proves across all 480 ordered F_5-bases of F_25 and all 160 commuting pairs in BD_5 x 3 non-trivial central
  signs — verified 100% invariant under 12 explicit SL(2, Z) peripheral basis-scrambling matrices — that for any
  full-2D parabolic SL(2, F_25) cusp lattice with non-trivial central spin sign alpha_Z in H^1(T^2; Z/2Z) \ {0}, the
  joined 128-dim spinor peripheral adjoint kernel collapses 8 -> 0 across all 4 torus spin structures if and only if
  the BD_5 peripheral subgroup H_per is cyclic of order 4 (C_4 = <r^a j>), whereas C_1 and C_2 leave 8 and C_5 and
  C_10 leave 4 or 6; proves further that the full 248 = 120 (exterior square of the 16) + 128 peripheral adjoint
  kernel on the geometric spin structure alpha_Z and on both ker(beta_j)-antiperiodic spin structures collapses
  (8, 0) -> (0, 0) if and only if alpha_Z != beta_j in H^1(T^2; Z/2Z), while alpha_Z == beta_j silences the 128
  (8 -> 0) but activates 4 modes in the 120 (8 -> 4); proves across all 1,199 orientable manifolds that 431 admit D_5
  surjections, 151 of 431 are strictly obstructed from lifting to BD_5 (100% carrying even H_1 torsion), 280 lift to
  BD_5, and 163 (145 2-gen + 18 3-gen) realize H_per = C_4, separating m004 cleanly from both its sister m003 and
  non-orientable m000 (both have D_5 = BD_5 = 0 despite 2T == 2); proves via exhaustive triangulation-independent
  Fricke SL(2, F_25) character-variety search over all 14,999 irreducible triples plus exact Z/24Z Meet-in-the-Middle
  Thurston F_25 gluing (326 F_5, 634 strict F_25 of 1,199; catching mod-5 triangulation degeneracy on s758) that
  exactly 57 of 1,041 2-gen manifolds achieve the 128-spinor 8 -> 0 lock (plus <= 9 of 18 3-gen C_4 manifolds with
  strict F_25 gluing), splitting strictly into 38 full-248 locks (alpha_Z != beta_j; tet breakdown 1/0/2/7/28 at
  t = 2/3/4/5/6) and 19 cohomologically obstructed manifolds (alpha_Z == beta_j), narrowing to 10 with 2T and exactly
  6 integer-homology (H_1 = Z) 2T manifolds — m004, m266, s136, s447, s560, s850 — all 6 carrying 2T == 2, proving
  m004 is the unique minimal 2-tet member of a sparse 0.58% family rather than unique at <= 6 tetrahedra)
- scope: frame: one flat compact E_8 adjoint via Spin(13) x Spin(3) -> Spin(16) -> Ss(16) subset E_8 across all
  1,199 orientable 1-cusped hyperbolic census manifolds (<= 6 ideal tetrahedra) plus non-orientable m000; object:
  universal E_8 peripheral kernel classification over all F_5-bases and commuting BD_5 pairs, exhaustive D_5/BD_5/H_per
  census across all 1,200 manifolds, exhaustive triangulation-independent Fricke SL(2, F_25) parabolic search across all
  235 BD_5-surjective 2-gen manifolds plus m003 and m000, exact Thurston F_25 gluing across all 1,199 orientable
  manifolds, and 2T / H_1 cross-tabulation; reach: class; hypotheses: pure-integer SnapPy 3.3.2 presentation and
  rectangular gluing dataset (a2_census_1200_presentations_and_gluing.json, SHA-256 20eae058063b9c51), exact F_25 =
  F_5[d]/(d^2 - 2) and Z/20Z phase arithmetic, exact Dickson surjectivity criterion verified by BFS (> 240 implies
  SL(2, F_25) of order 15,600), 12-matrix SL(2, Z) peripheral basis-scrambling check, 5 planted fault controls,
  standard library only, zero float literals (independently cross-checked with 0 discrepancies by a zero-shared-code
  same-family Cold-Room Referee at 5bbbfd1de using F_5[t]/(t^2 - 3) companion matrices, disjoint B-gauge, 30-matrix
  SL(2, Z) scrambling, direct backtracking gluing, and live SnapPy verification; strictly 0 of 19)
- identifications: none
- definitions: F_25 = F_5[d]/(d^2 - 2) with Tr_{F_25/F_5}(a + b d) = 2 a mod 5; the 13-dim even Weil module on {0}
  union 12 pairs {+-x} in F_25^* lifts uniquely to order-5 Spin(13) half-weights +-4*(3w mod 5) mod 20 giving 64
  spinor weights; BD_5 = <r, j | r^5 = 1, j^2 = -1, j r j^{-1} = r^{-1}> (order 20) acts on 3 of SO(3) and 2 of
  Spin(3) inside Spin(13) x Spin(3) -> Ss(16) subset E_8 (adjoint 248 = 120 + 128). For any orientable torus cusp
  with full-2D parabolic SL(2, F_25) holonomy (tau_cusp in F_25 \ F_5) and non-trivial central signs (s_m, s_l) !=
  (+1, +1), alpha_Z in H^1(T^2; Z/2Z) \ {0} maps a peripheral curve c to 1 iff tr(rho_geo(c)) = -2; for a BD_5
  surjection with H_per = C_4, beta_j in H^1(T^2; Z/2Z) \ {0} maps c to 1 iff ord(rho_sh(c)) = 4, with unique
  primitive kernel slope c_0 = ker(beta_j). Fricke triple (x, y, z) = (tr A, tr B, tr AB) in F_25^3 is irreducible
  iff x^2 + y^2 + z^2 - x y z != 4 (14,999 triples).
- imports: none
- premises on main: B993, P-581, P-876, I-9
- decisive script: relays/a2_whole_census_e8_two_register/a2_whole_census_e8_decisive.py, SHA-256 03d81a3c2a2699a0,
  depends on the standard library, run as python3 relays/a2_whole_census_e8_two_register/a2_whole_census_e8_decisive.py,
  output SHA-256 e129994c40e98e16
- decisive lines: 5 lines marked "DECISIVE:", SHA-256 e129994c40e98e16
- failing control: python3 relays/a2_whole_census_e8_two_register/a2_whole_census_e8_control.py
- second computation: none
- already on main?: git grep across origin/main (60a39b1dc) finds B993 (400-manifold 2T/2O/2I census) and P-876
  (m004-only C8 two-register construction); no arc on main tests the coupled E_8 two-register lock, BD_5 lifting
  obstruction, or H^1(T^2; Z/2Z) 248-lock criterion across the 1,199-manifold census plus m000
- what would make it fail: any of the 480 F_5-bases deviating from {2: 12, 3: 12, 4: 1} w_64 multiplicities, any
  commuting BD_5 pair violating C_4 <-> k128==0 or alpha_Z != beta_j <-> k248(alpha_Z)==0, any SL(2, Z) peripheral
  basis change altering k128/k248/alpha_Z==beta_j, any D_5 -> BD_5 obstructed manifold lacking even H_1 torsion, any
  discrepancy in the census counts (D5=431, BD5=280, obst=151, BD5_C4=163, glueF5=326, glueF25=634, lock128=57,
  lock248=38, cohom120=19, lock248_2T=10, lock248_H1Z=29, lock248_H1Z_2T=6), m003 or m000 admitting BD_5, any
  AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1 control failing
