# CLAIM CARD — under one comparison class the structural package (ℤ₆, Y, 3/8) has one grade: the E₆ route's, 384/1199

- seat, branch, commit: SM seat, this seat's branch (as on its page on main), the commit that adds this card; sealed
  card and scripts at 8a6f01fd6
- kind: computation
- touches: P-581 (FL-26, Q-STRUCT); I-9 (A6); F-MC's grades in GENESIS § 5
- effect: conditions — the structural grades: ℤ₆, the hypercharge direction and sin²θ_W = 3/8 carry one grade, the
  rate of π₁ ↠ 2T in rule K (0.3203), and no grade of their own (each has rate 1 given the route)
- imports: the census triangulations and their presentations, frozen as relays/sm_r581/r581_presentations.json
  (SHA-256 8c825d9c27295df6); McKay's correspondence; the self-conjugacy of E₇'s and E₈'s least representations (cited)
- premises on main: B861 (the cascade, with P5), B862 (kernel ℤ₆, main's kernel_exact), B1160, B993, B996, B727,
  GENESIS F-MC v1.1
- decisive script: relays/sm_r581/run.py, SHA-256 7307d284e7526972, depends on the standard library, numpy, sympy,
  and main's checkout (argv[1]: B862's module, B993's JSON); run as
  `python3 -I run.py MAIN_CHECKOUT r581_presentations.json .`; output r581_run.txt, SHA-256 0ca6caa4891c96ee
- second computation: none yet; main's B993 code agrees per object on the 400 it covers (same method, not independent)
- already on main?: `grep -l "Q-STRUCT" frontier/*/FINDINGS.md` on be8c83d4f: no match; closest arcs B993 (first 400,
  37.2%) and B862
- what would make it fail: the ℤ/3 plant below rate 1, or a member of K with the route and without the package (here
  1199/1199 and none); E6 of the card failed (2I at 0.5079 exceeds 2T), stated on the page
