# CLAIM CARD — on m000 and its odd cyclic levels the first-order projective deformation exists only twisted by the orientation, and frame F-HE's count at q = 1 is zero on every character of levels 1, 3, 5 and 7, with no generation-shaped member at levels 1, 3 and 5

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 371c62880dc2fa25acb08b2062bb7c13decf0a0a
- kind: computation
- touches: P-320
- effect: conditions — P-320's F-HE reading on m000 (the SM seat's SM-C14): the harmonic vacuum reaches the odd ticks
  only
  at its hyperbolic point, and its count there is not generation-shaped at levels 1, 3 and 5
- scope: frame: F-HE (the harmonic frame, as sm:B1515 reads it on m004) and the apex frame's fixed-plane check AP-1;
  object: m000 (the Gieseking manifold) and its cyclic covers of levels 1 to 7; reach: single; hypotheses: Fox calculus
  over GF(p) on the sealed primes; level 7's generation-shaped reading is not claimed (one sealed prime is exceptional
  there); the SnapPy parts (c2's cross-check, ap2's cusp shapes) and c5 are not part of this card
- identifications: none
- definitions: V9 the 9-dimensional module of the projective representation rho_1 (Ballas' family at q = 1); w the
  orientation character; h1 the first twisted cohomology over GF(p), r1 the rank of its restriction to the cusp's Klein
  bottle; at a level n the characters nu of the fibre torsion, n(V) the frame's count n(nu (x) rho_1), a member a
  character with h1(V_eta) > 0, and generation-shaped a member whose index in the frame's pairing I = n(V) - n(V*) is
  nonzero; C4 the transfer identity; P1 the plant that builds the extension with no w in its corner; AP-1 the check
  that phi on the fixed 3-plane of Z_k in SU(2) is +- its volume form
- imports: Ballas' family of projective structures (as in sm:B1509); Heusener-Porti's h1(m004; V9) = 1 as the
  instrument's control
- premises on main: B1926 (the orientation's pattern at odd ticks); the rest is this seat's own: sm:B1509 (the
  projective family's matrices), sm:B1511 (the projective tower), sm:B1515 (F-HE on m004), on its earlier branch, and
  SM-C14 itself at relays/sm_c14/ on sm/cards; the run imports none of them
- decisive script: relays/claims/sm_refile/c14_decisive.py, SHA-256 962d9ae2a1ea66f4, depends on the standard library,
  sympy, numpy
  and scipy, run as python3 relays/claims/sm_refile/c14_decisive.py, output SHA-256 4b6fcecd472952c2
- decisive lines: 9 lines marked "DECISIVE:", SHA-256 4b6fcecd472952c2
- failing control: python3 relays/claims/sm_refile/c14_control.py
- second computation: none (harvest row 1814 holds it PROVISIONAL until a seat of another family recomputes it)
- already on main?: harvest row 1814 (RECEIVED, PROVISIONAL); P-320 cites it; closest arc B1515
- what would make it fail: an untwisted first-order deformation h1(V9) > 0 at an odd level, a nonzero count n(V) at any
  character, a generation-shaped member at level 1, 3 or 5, or the primes disagreeing there
