# CLAIM CARD — under one comparison class the structural package (ℤ₆, Y, 3/8) has one grade: the E₆ route's, 384/1199

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-581 (FL-26, Q-STRUCT); I-9; F-MC's structural grades in GENESIS § 5
- effect: conditions — P-581's structural grades: ℤ₆, the hypercharge direction and sin²θ_W = 3/8 carry one grade,
  the rate of π₁ ↠ 2T in rule K (384 of 1199, 0.3203), and none of their own (each has rate 1 given the route)
- scope: frame: F-MC (the McKay cascade frame), read at the group level as B993 read it; object: rule K, every
  orientable one-cusped hyperbolic census manifold with at most 6 ideal tetrahedra, in census order (1199, the root
  m004 among them); reach: class; hypotheses: the cascade's menu completeness (P5, B861); the class rule K, sealed
  before the run (card SM_R581 at 8a6f01fd6 on the seat's earlier branch); the census presentations as frozen
- identifications: none
- definitions: the E₆ route of a manifold M is a surjection π₁(M) ↠ 2T = SL(2, 3) (McKay: 2T gives E₆), counted
  up to Aut(2T) by exhaustive search over generator images with the relators checked in 2T's table; the E₇ and E₈
  labels are the same with 2O and 2I = SL(2, 5); after E₆ the construction takes no manifold: the B862 kernel of
  SU(3)×SU(2)×U(1) → S(U(3)×U(2)) must be ℤ₆, the traceless commutant of su(3) ⊕ su(2) in su(5) must be
  one-dimensional and ∝ diag(2, 2, 2, −3, −3) (the hypercharge direction), and sin²θ_W = Tr T₃² / Tr Q² on the 5
  along it must be 3/8; the package of M holds when the route and all three steps hold; a property's grade is its
  rate in K; plants: π₁ ↠ ℤ/3 must hold for every member (rate 1) with count 3^d − 1 (d the F₃-rank of H₁ from the
  relator matrix), and π₁ ↠ (ℤ/2)³ must fail on every two-generator presentation
- imports: the census triangulations and their π₁ presentations, frozen as relays/sm_r581/r581_presentations.json
  (made once with the census package; not needed to rerun); McKay's correspondence; the self-conjugacy of the least
  E₇ and E₈ representations (cited, enters no number)
- premises on main: B861 (the fused cascade, with P5); B862 (the ℤ₆ kernel, main's kernel_exact, run by the script);
  B1160 (hypercharge forced); B993 (the 2T base rate on the first 400, and its output, used as a per-object control);
  B996; B727; GENESIS F-MC v1.1; register row P-581
- decisive script: relays/claims/sm_refile/r581_decisive.py, SHA-256 38d9ba2d8c1427c7, depends on the standard library,
  numpy and sympy, run as python3 relays/claims/sm_refile/r581_decisive.py, output SHA-256 6792b9c92df73085
- decisive lines: 16 lines marked "DECISIVE:", SHA-256 ee162149c5ac17e5
- failing control: python3 relays/claims/sm_refile/r581_control.py
- second computation: none
- already on main?: `grep -l "Q-STRUCT" frontier/*/FINDINGS.md` on be8c83d4f: no match; closest arcs B993 (the first
  400, 37.2% reach 2T) and B862
- what would make it fail: a member of K with the route but without the package (some step after E₆ depending on
  the manifold); the ℤ/3 plant below rate 1 or its count off 3^d − 1; the 2T counts disagreeing with B993's on any of
  its 400 manifolds; m004 not at exactly 2 classes; or the kernel, the commutant or 3/8 coming out otherwise
