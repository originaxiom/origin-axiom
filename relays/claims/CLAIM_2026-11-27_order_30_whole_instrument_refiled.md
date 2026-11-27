# CLAIM CARD — at order 30 the 240 pairs of points whose first coordinate has a 5-part are all aligned and hierarchical, converged, in exactly the act's line's 12 classes at 5 times its sizes

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-845, P-860 (d)
- effect: supports — P-860 (d)'s menu of 12 classes (B1979) as the level's own where the cusp sees the 5-part, with no
  point chosen
- scope: frame: frame C (B1945's parts and U_of, reading S, column 0.13, rates between heights as B1977 reads them, the
  end as main's table gives it); object: the rates of all 576 points of exact order 30, as 288 pairs +-v; reach: single;
  hypotheses: order 30 only; the rates read between heights 30-40 and 40-50 and placed on the grid of 1/60; the 48 pairs
  whose a has no 5-part are not claimed (their rates do not converge by height 50, and at a = 0 they depend on the end
  above Im tau = 6, which main's table freezes)
- identifications: none
- definitions: a point (a, b) of exact order 30 in (Q/Z)^2; "a has a 5-part" when 5 divides the denominator of a; a rate
  is -(ln x(y2) - ln x(y1)) / (pi (y2 - y1)) for a mass ratio or |V_ij|; aligned: least |V_kk| >= 0.9 at height 50;
  hierarchical in both quark sectors: up and down m2/m3 rates >= 0.1 and m1/m3 rates >= 0.2; a class is the tuple of the
  nine rates rounded to the grid of 1/60; the act's line: the 96 points whose 5-part lies on {k(1, 2)/5}
- imports: none
- premises on main: B1945 (parts, U_of), B1977 (the read-out), B1979 (the grid of 1/60 and its 12 classes); the seat's
  SM-C23 (joint covariance, which makes the 576 points one point's reading over every cusp), its own card
- decisive script: relays/claims/sm_refile/c24_decisive.py, SHA-256 d6ade76d0c073a0f, depends on the standard library and
  mpmath, run as python3 relays/claims/sm_refile/c24_decisive.py, output SHA-256 45e648b04ae9eeec
- decisive lines: 6 lines marked "DECISIVE:", SHA-256 b5ae2acb217890bc
- failing control: python3 relays/claims/sm_refile/c24_control.py
- second computation: none
- already on main?: B1976 to B1979 read the 96 points on the act's line; none reads the other 480
- what would make it fail: a pair with a 5-part that is unaligned, not hierarchical, unconverged, or in a class the
  act's line lacks, or class sizes not 5 times the line's
