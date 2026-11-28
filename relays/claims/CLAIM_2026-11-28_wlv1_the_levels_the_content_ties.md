# CLAIM CARD — W-LV1: on frame C's charges, under B1976's unit rule as this seat restates it (a sector against itself counts only swapped), for N = 2 to 420 the sectors tie over a whole level only at N = 2, 3, 4, 5, 6, 7, 9 and 15; the multiplets' charge differences have the primes 2, 3 and 5; the three principles fixed before the old run give P1 = 210, P2 = 30 and P3 = 10, which disagree, so they do not single out level 30 (P-845 stays open); the four ties tested agree on frame C's normalised spectra at two points each (the seat's card of 2026-11-25 in the queue's form, main's frame copied in)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, bd3ca8e9eeca701cb6a9c8574a16257482cfd326
- kind: computation
- touches: P-845
- effect: conditions — P-845: on this tie table the three principles fixed before the old run give three levels (210,
  30, 10), each a counted choice; they do not agree, and one of them (P2) gives 30
- scope: frame: frame C at main's be8c83d4f, its 6Y charge pairs up (1, −4), down (1, 2), lep (−3, 6) and its coupling
  through B1945's determinant_law.parts; object: the levels N at which two sectors tie by a unit of Z/N; reach: class;
  hypotheses: B1976's unit rule with this seat's one change, that a sector against itself counts only swapped
  (counting the unswapped self relations too, every multiple of 3 would tie, 30 and 210 among them; P1, P2 and P3 do
  not change); N = 2 to 420; the principles and the reading rule were fixed before the old run, but the seat's hand
  arithmetic had anticipated the table's levels, primes and P1, P2, P3, so the reading is not blind; the spectra
  checked at column 0.13, height 6, reading S, at two points for each of four ties; main's frame copied verbatim into
  the card's folder, its loaders replaced, and one non-loader line (covariance.py line 130, an import of
  multiprocessing the rerun refuses, off the run's path) made an exit (MANIFEST.md lists each replaced line)
- identifications: none
- definitions: sectors s and t tie at level N when a unit k of Z/N carries s's charge pair p to t's pair q, k p = q mod
  N, directly or with the pair swapped (a sector against itself only swapped); a whole-level tie allows every unit k,
  a pointwise tie only k = 1 or −1. P1 is the product of the primes with a tie at some power; P2 the product of the
  primes of the multiplets' charge differences (Q 1, u −4, d 2, L −3, e 6); P3 the least multiple of 5 that is not a
  tie level. The reading R2: the three principles do not agree. A tie's spectra agree when the singular values of Y_t
  at the point w and of Y_s at k w, each divided by its largest, differ by less than 1e-12 at both points; the tested
  ties agree to 3.6e-42 or better at about 42 working digits, while untied pairs have been seen to agree to 4e-14
  (the old card's post hoc, not this run), so the 1e-12 bar alone does not separate ties from near misses. The
  negative control at order 30 tells (down, lep) apart at one of its two points (8.6e-3 above its 1e-3 bar; the
  other, 9.3e-4, is below it)
- imports: none
- premises on main: B1945 (the frame's coupling, determinant_law.parts), B1976 (the unit rule), B1943 (the act's line),
  and the frame of B1940, B1932, B1928, B1927, B1924, B1724, B1716, B1691 and B1667 at be8c83d4f, as the card's folder
  copies them
- decisive script: relays/chat1_2026-11-28_wlv1/card_wlv1.py, SHA-256 15a663b14631979f, depends on the standard
  library, mpmath, numpy and scipy, run as python3 relays/chat1_2026-11-28_wlv1/card_wlv1.py, output SHA-256
  89f0f5ea410964a7
- decisive lines: 13 lines marked "DECISIVE:", SHA-256 89f0f5ea410964a7
- failing control: python3 relays/chat1_2026-11-28_wlv1/card_wlv1.py --control
- second computation: none that shares no code with main's frame. The old card's referee recomputed the table, the
  primes and the principles on its own code (not committed), and this card's referee did again: the same levels and
  P1, P2, P3. The copy reproduces the sealed output of 2026-11-25 (relays/chat1_2026-11-25_level/w_lv1_level_out.txt,
  SHA-256 f5639dec60f37e4b) byte for byte (the first decisive line), and its side json equals the old one. The
  script's first run (bc60158ca) exited 2: a parser bug read the label "T2" as a level, so its verdict read FAILS on
  the same twelve value lines; the one-line fix (61db75b12) came before the run this card states. The control's
  output is from the first run; control() was not touched by the fix. Not carried from the old card: the leptons at
  the point 3w, the post hoc fourth principle P4, and its relay's § 8 on the act's orbits
- already on main?: topic_sweep.py "unit rule|tie arithmetic|ties only at" at be47862d1: no arc, one register row;
  B1976 applies the unit rule at N = 5, 6 and 30, and no arc tabulates every level or compares principles for it
- what would make it fail: a level from 2 to 420 the table calls tie-free where a unit carries one sector's pair to
  another's under the rule as restated; a sector charge in the frame other than these; a tested tie whose normalised
  spectra differ by 1e-12 or more; or the copy failing to reproduce the sealed output. The control makes the lepton
  pair (−3, 5) on purpose: the whole-level ties then fall at 2 to 9, 11, 13, 15, 16 and 17, and the claim's check
  fails.
