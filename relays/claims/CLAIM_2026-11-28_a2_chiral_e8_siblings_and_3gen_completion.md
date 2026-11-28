# CLAIM CARD — Arithmeticity-vs-Chirality Dilemma across the coupled E_8 two-register census (<= 6 tetrahedra), universal Ad(2T) parabolic rigidity, finite-field mod-5 cusp reflection breaking, and 100% 3-generator census closure discovering chiral 7th survivor s754 (0 of 19)

- card id: new
- seat code: fam3-v1-high-03
- seat, branch, commit: fam3-v1-high-03, agy-002/verify, 4dcbc2c7e84edf0e0ee120940808eb865ad9f1ff
- kind: theorem
- touches: P-876, P-581, I-9, P-374
- effect: conditions — P-876, P-581, I-9, and P-374 (resolves the chirality and 3-generator seams across all 1,199
  orientable 1-cusped hyperbolic census manifolds at <= 6 ideal tetrahedra plus m000: proves via 420-digit gluing
  Newton refinement, exact LLL minimal polynomials, exact symbolic Thurston gluing verification in Q[X]/(P_M(X)),
  Sturm real-place counts, and 420-digit canonical-parabolic SL(2, C) squared-trace integrality across all 10 2-gen
  lock_248_2T survivors plus m003 that all 44/44 checked pi_1(M)^(2) traces are algebraic integers, while m004
  (deg = 2, P = X^2 - X + 1, r1 = 0) is the unique arithmetic manifold in both the 10-manifold 2-gen lock_248_2T set
  and the 6-manifold 2-gen H_1 = Z + 2T set — every chiral H_1 = Z sibling carries a high-degree non-arithmetic
  invariant trace field (m266: 15, s136: 13, s447: 14, s560: 14, s850: 10), establishing an exact Arithmeticity-vs-
  Chirality Dilemma at <= 6 tetrahedra; proves via exact rational Fox calculus on Ad(2T) = A_4 subset SO(3) — verified
  100% invariant under 10 unimodular SL(3, Z) basis-scrambling matrices — that all 6 of 6 2-gen H_1 = Z + 2T survivors
  (and all 12 tested manifolds including m003 and m000) are parabolically rigid with dim H^0 = 0 and dim H^1_par = 0
  on every Aut(2T)-orbit (dim H^1 = 1 on all 11 orientable cusps, 0 on Klein-bottle m000, with asymmetric [6, 3]
  peripheral 2T orders on s447 and s850); proves across all 6 2-gen H_1 = Z survivors that all 5 chiral siblings break
  mirror symmetry on topology (is_amphicheiral = False, sym = Z/2), Chern-Simons (4 CS not in Z), and complex cusp
  lattice (2 Re(tau_cusp) not in Z), and further that 4 of the 5 (s136, s447, s560, s850) break finite-field reflection
  tau -> -tau^5 directly inside the exact F_25 parabolic cusp spectrum (whereas m004 is mirror-locked to {+-2d} and
  m266 retains symmetric {+-1 +- d}); and closes 100% of all 18 3-generator BD_5 C_4 manifolds via exact shape fields,
  F_25 Thurston gluing, canonical-parabolic 420-digit geometric mod-5 reductions with all Hom(pi_1, {+-1}) sign lifts
  (yielding 6 geometric 248-locks: m201, m207, s556, s754, s882, s961; 4 with 2T: m207, s556, s754, s882), and a 100%
  exhaustive presentation-level SL(2, F_25) parabolic search on all 3 3-gen H_1 = Z + 2T manifolds (s573: 0 hits;
  s890: 0 hits; s754: 4 hits, kills_128 = kills_248 = True, sign_pairs = [[-1,-1], [1,-1]], mod-5 reflection-broken
  cusp spectrum {2 +- d}, non-arithmetic deg = 27, chiral sym = Z/2), proving that across all 1,199 orientable 1-cusped
  manifolds <= 6 tetrahedra, exactly 7 satisfy H_1 = Z + 2T + full 248: 8 -> 0 lock — unique amphicheiral arithmetic
  m004 plus 6 non-arithmetic chiral siblings m266, s136, s447, s560, s850, and 3-gen s754)
- scope: frame: exact number fields k(M) = Q(z_0, ..., z_{t-1}), rational Fox cohomology of Ad(2T) = A_4 subset SO(3),
  and coupled E_8 two-register SL(2, F_25) + BD_5 C_4 kernel collapse across the orientable 1-cusped hyperbolic census
  (<= 6 ideal tetrahedra) plus m000; object: all 10 2-gen lock_248_2T manifolds (m004, m247, m266, s070, s099, s136,
  s447, s560, s820, s850), m003, m000, and all 18 3-gen BD_5 C_4 manifolds (m201, m207, m235, m261, s051, s426, s556,
  s573, s640, s733, s754, s788, s837, s854, s882, s890, s942, s961); reach: class; hypotheses: zero-float SnapPy 3.3.2
  30-manifold dataset (a2_chiral_e8_siblings_input.json, SHA-256 f50211a4a0a00c2f), 420-digit mpmath Newton refinement
  for gluing and canonical-parabolic SL(2, C) holonomy, exact sympy QQ[X]/(P_M(X)) symbolic gluing certification, pure-
  Python F_5 square-free DDF, exact rational Fox calculus with 10 unimodular SL(3, Z) basis scramblings, exhaustive
  SL(2, F_25) search via 672 centralizer orbits and exact F_25 linear conjugators, 5 planted fault controls, zero float
  literals (independently cross-checked with 0 discrepancies at 80dc8baf1 by a zero-shared-code same-family Cold-Room
  Referee using log-Jacobian Newton, mpmath.pslq, Berlekamp mod-5, Hurwitz-quaternion 2T, 15 new SL(3, Z) matrices, and
  F_5[t]/(t^2 - 3); full custody disclosed: blind v10 caught on 29 non-core Family A/B fields by Referee FAIL 84427b9d2,
  independently remediated in pre-committed v11 25b166dfd -> 4dcbc2c7e, certified PASS 0 discrepancies at 80dc8baf1;
  strictly 0 of 19)
- identifications: none
- definitions: For a 1-cusped orientable hyperbolic 3-manifold M with rectangular Thurston gluing system
  prod_j z_j^{a_{ij}} (1 - z_j)^{b_{ij}} = sgn_i, k(M) = Q(z_0, ..., z_{t-1}) is the invariant trace field (Maclachlan-
  Reid Thm 3.3.4 / 4.2.3), and M is arithmetic iff [k(M) : Q] = 2 with r1 = 0 (imaginary quadratic) and all traces in
  pi_1(M)^{(2)} are algebraic integers (Maclachlan-Reid Thm 8.2.3). 2T = SL(2, F_3) (order 24) acts on su(2) = Q_8/{+-1}
  via exact 3x3 signed-permutation matrices Ad(2T) = A_4 subset SO(3); Fox derivatives d1: Q^{3 n_g} -> Q^{3 n_r} and
  d0: Q^3 -> Q^{3 n_g} define H^0 = ker(d0), H^1 = ker(d1)/im(d0), and H^1_par = ker(H^1(M) -> H^1(partial M)) over Q.
  F_25 = F_5[d]/(d^2 - 2) with Frobenius Frob(a + b d) = a - b d and finite-field reflection tau -> -Frob(tau) = -a + b d.
  For full-2D parabolic SL(2, F_25) holonomy (tau_cusp in F_25 \ F_5, |H| > 240, non-trivial central signs alpha_Z != 0)
  and BD_5 C_4 peripheral subgroup (order-4 character beta_j), kills_128 holds iff alpha_Z != 0 and kills_248 holds iff
  alpha_Z != beta_j in H^1(T^2; Z/2Z).
- imports: none
- premises on main: B993, B2008, P-374, P-581, P-876, I-9
- decisive script: relays/a2_chiral_e8_siblings/a2_chiral_e8_siblings_decisive.py, SHA-256 0fcb81e72b95b5af, depends
  on the standard library, mpmath and sympy, run as python3 relays/a2_chiral_e8_siblings/a2_chiral_e8_siblings_decisive.py,
  output SHA-256 611dbe6f835dbcd3
- decisive lines: 5 lines marked "DECISIVE:", SHA-256 611dbe6f835dbcd3
- failing control: python3 relays/a2_chiral_e8_siblings/a2_chiral_e8_siblings_control.py
- second computation: none
- already on main?: git grep across origin/main (59eead63d) finds B993 (400-manifold 2T/2O/2I census), B2008 (open
  sourced-handedness question on the 3^k Markoff tower), and P-876 (m004-only C8 two-register construction); no arc on
  main computes exact shape fields, Maclachlan-Reid arithmeticity, Ad(2T) Fox rigidity, mod-5 cusp reflection breaking,
  or complete 18-manifold 3-gen SL(2, F_25) closure across the coupled E_8 two-register census (including s754)
- what would make it fail: any symbolic gluing residual != 0 mod P_M(X) on any of the 29 hyperbolic manifolds, any
  mismatch in field degrees [2, 15, 13, 14, 14, 10] (6 2-gen H_1 = Z) or 27 (3-gen s754) or arithmeticity (m004 unique
  among the 6 2-gen and 7 total H_1 = Z + 2T + lock_248 manifolds), any SL(3, Z) basis-scrambling change in Ad(2T)
  cohomology or violation of h0 = 0, h1_par = 0 across the 6 H_1 = Z manifolds, any mismatch in Chern-Simons/cusp
  chirality or mod-5 reflection breaking (m004, m266 True vs s136, s447, s560, s850, s754 False), any discrepancy in
  the 18-manifold 3-gen closure (geom_lock248 = 6, exhaustive H_1 = Z + 2T hits s573 = 0, s890 = 0, s754 = 4), any
  AST/JSON float literal, or any of 5/5 planted controls or the standalone exit-1 control failing
