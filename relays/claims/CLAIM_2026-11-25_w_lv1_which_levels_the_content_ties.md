# CLAIM CARD — W-LV1: under B1976's unit rule, checked on frame C's coupling, couplings tie only at the levels 2, 3, 4, 5, 6, 7, 9 and 15; the charges coincide only at the primes 2, 3 and 5, and the lens also ties at 7; three principles fixed before the run give 210, 30 and 10, so the tie arithmetic does not single out level 30 (P-845 open). The leptons are the down sector, its doublet's charge negated, at the point 3w at every level (B1949, confirmed on the coupling), so over the whole level a lepton–down split needs a level divisible by 3

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 3b44d1337 and its output at 168768e85; the post
  hoc check is at 2a5fb5e17 and its output at 49ffc3438. The relay is
  relays/CHAT1_TO_CC_2026-11-25_W-LV1_WHICH_LEVELS_THE_CONTENT_TIES.md; it and this card were corrected after their
  referee read.
- kind: computation (exact arithmetic, with controls on the frame's coupling)
- touches: P-845; B1976, B1977, B1978, B1979, B1949, B1945, B1946, B1953, B1971; agy-002's M33
- effect: conditions — P-845: the level is not fixed by the content's tie arithmetic; four candidate principles (one
  post hoc) give three levels, each a counted choice; under the units' reading of the level, frame C's leptons
  split from its down quarks only at levels divisible by 3 (the act's own orbits differ: § 8 of the relay)
- imports: none
- premises on main: B1945 (the frame's coupling, `determinant_law.parts`), B1976 (the unit rule), B1949 (the leptons
  and the point 3w), B1943 (the act's line), the frame at be8c83d4f
- decisive script: relays/chat1_2026-11-25_level/w_lv1_level.py, SHA-256 7bd76733bf818225. It imports main's frame from
  a checkout at be8c83d4f, passed as its argument, and refuses any other commit. Run as
  `python3 -B w_lv1_level.py <main checkout>` (about 8 seconds). Output w_lv1_level_out.txt, SHA-256 f5639dec60f37e4b;
  values in w_lv1_level.json, SHA-256 acff2c0b39b33919. Three statements of its sealed docstring are wrong and are
  corrected in the relay (the self relations, the "same characteristics", the control bar).
- post hoc check: relays/chat1_2026-11-25_level/w_lv1_posthoc.py, SHA-256 89bb5f677daec985, written after the referee
  read; output w_lv1_posthoc_out.txt, SHA-256 7272f1f0b45df15b.
- second computation: the referee re-ran the script byte for byte and recomputed the table, the primes, the principles
  and the counts on its own code; its scripts are not committed. Not independent of main's coupling code.
- already on main?: B1976 applies the unit rule at N = 5, 6 and 30; B1949 proves the leptons' relation to the point
  3w. No arc tabulates every level, names the lens's primes, compares principles for the level, or reads the
  lepton–down split over the whole level.
- what would make it fail:
  - a coincidence of frame C's couplings, below the working precision, at a level the table calls tie-free;
  - a sector charge in the frame other than B.SIXY's at be8c83d4f;
  - the Higgs entering the lens.

## What it means

- [E] Couplings tie only at N = 2, 3, 4, 5, 6, 7, 9 and 15; with k = ±1 only, at the same levels except 15. Swapped
  ties are transposes.
- [E] P1 = 210, P2 = 30, P3 = 10; post hoc, P4 = 30.
- [E] Y_lep(w) ∝ Y_dn(3w) at every point checked (orders 10 and 30); at order 30, Y_lep(w) ∝ Y_lep(11w).
- [J] Level 30 is not singled out by the tie arithmetic. Over the whole level the leptons can differ from the down
  quarks only at levels divisible by 3; at one point they differ at 10 as at 30. The record has not fixed which
  reading frame C takes.
- [J] The computation called for: B1976's checks and B1977's gates at order 10 (12 points) and order 210 (4608 points,
  or a declared sample), each read at one point and over the level, its rule sealed first. (Superseded by the relay's
  § 8.)
- [J] Correction of 2026-11-25 (afternoon; relay § 8, no referee read yet). The record did not leave "one point or the
  level" open as a choice. The object's own grouping is the act's orbits (B1978). The factor 3 is the number of
  colours: the anomaly-fixed hypercharges give (L, e) = N_c·(−1, d) only for N_c = 3. By a hand argument, not yet
  sealed, the act multiplies its line by −1 mod 5, so 3w is never on the orbit of ±w. On the act's orbits, then, the
  leptons read another orbit at every level on the act's line, 10 included. A sealed card is owed.

0 of 19.
