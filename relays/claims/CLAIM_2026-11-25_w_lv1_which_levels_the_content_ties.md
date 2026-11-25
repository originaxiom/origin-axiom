# CLAIM CARD — W-LV1: under B1976's unit rule, checked on frame C's coupling, the matter content ties sectors only at the levels 2, 3, 4, 5, 6, 7, 9 and 15; the lens's primes are 2, 3, 5 and 7, the charges coincide only at 2, 3 and 5; three principles give 210, 30 and 10, so the tie arithmetic does not single out level 30 (P-845 open). Over the whole level sectors tie by any unit, at one point only by ±1

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 3b44d1337 and its output at 168768e85. The relay
  is relays/CHAT1_TO_CC_2026-11-25_W-LV1_WHICH_LEVELS_THE_CONTENT_TIES.md.
- kind: computation (exact arithmetic, with controls on the frame's coupling)
- touches: P-845; B1976, B1977, B1978, B1979, B1949, B1945, B1953; agy-002's M33
- effect: conditions — P-845: the level is not fixed by the content's tie arithmetic; three candidate principles give
  three levels, each a counted choice
- imports: none
- premises on main: B1945 (the frame's coupling, `determinant_law.parts`), B1976 (the unit rule), B1943 (the act's
  line), the frame at be8c83d4f
- decisive script: relays/chat1_2026-11-25_level/w_lv1_level.py, SHA-256 7bd76733bf818225. It imports main's frame from
  a checkout at be8c83d4f, passed as its argument, and refuses any other commit. Run as
  `python3 -B w_lv1_level.py <main checkout>` (about 8 seconds). Output w_lv1_level_out.txt, SHA-256 f5639dec60f37e4b;
  values in w_lv1_level.json, SHA-256 acff2c0b39b33919.
- second computation: within the script, the unit rule against the frame's coupling (four kinds of tie, two points
  each, agreement to 1e-42 or better; a negative control). The bound beyond N = 420 is by hand. Not independent of
  main's coupling code.
- already on main?: B1976 applies the unit rule at N = 5, 6 and 30. No arc tabulates every level, names the lens's
  primes, or compares principles for the level.
- what would make it fail:
  - a coincidence of frame C's couplings at a level the table calls tie-free;
  - a sector charge in the frame other than B.SIXY's at be8c83d4f;
  - the Higgs entering the lens.

## What it means

- [E] Whole-level ties occur only at N = 2, 3, 4, 5, 6, 7, 9 and 15; pointwise (k = ±1) at the same levels except 15.
- [E] At N = 7 the leptons are the up quarks transposed at the negated point; that is the only tie at a prime above 5.
- [E] P1 (all the lens's primes) = 210, P2 (the charge coincidences) = 30, P3 (the least tie-free level on the act's
  line) = 10.
- [J] Level 30 is not singled out by the tie arithmetic. What 30 adds over 10 is the 3-part; if alignment picks it,
  the level is picked by a property wanted of the result.
- [J] The computation called for: B1976's checks and B1977's gates at order 10 (12 points) and order 210 (4608 points,
  or a declared sample), its rule sealed first.

0 of 19.
