# CLAIM CARD — P-589 (c): at B1838's exact horoball norms, B1701's degenerate spectrum (law-map row 315) holds on the nine lines read and B1729's coarser-line negative (row 324) stands on its sample; with the accessory parameter on its uniformising branch on Re τ = 0 (post hoc, not blind), B1712's order-12 electron zero holds on all 48 lines and B1711's order-9 lepton m1/m3 stays above 1e-12 on all 36 (above 1e-7, so below the sealed 1e-6 bar); the sealed run's P2 failed on both halves (the seat's card of 2026-11-25 in the queue's form, main's code copied in)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 9e9e61f926d720c6af9696cafb0c5f860d16aab0
- kind: computation
- touches: P-589, P-421; law-map rows 313, 315, 316 and 324 (B1701, B1711, B1712, B1729); the 19, through the values
  they would be read from: the frame's mass ratios m2/m3 and m1/m3 in each sector
- effect: supports — P-589 (c), in part: four rows' data-free statements re-read at the exact norms (315 and 324, and
  313's and 316's electron statements); rows 295, 311, 312 and 352 and 316's quark clause are not re-read here
- scope: frame: frame C's end at main's 88a1e9474, through B1838's exact-norm instrument (B1667's cell, horocycles,
  accessory parameter and small-cut column, with B1656's four twisted channels and B1691's end-data Higgs); object:
  the sector spectra on the rows' lines at the small-cut and the exact norms; reach: class; hypotheses: the sealed
  scripts' samples: row 315 on 9 of the 27 tied lines of period 6 (the first nine in the script's order) at 1.6i and
  0.5 + 2.4i; row 324 on 7 of B1729's orders (5, 10, 13, 15, 21, 24, 30), at most 16 lines each, seed 1729, at B1729's
  two points moved into the cell; rows 313 and 316 at one τ each (3.5i and 3.1i). On Re τ = 0, B1667's track() returns
  a stuck accessory parameter (8.19e-4 at every height) without error; the post hoc check takes c* as Re c at
  Re τ = 0.0025, printing the spread over 0.01, 0.005 and 0.0025 (5e-5 at 1.6i). The sealed P1 read row 315's 1.6i
  half at the stuck c, so that half rests on the post hoc Q1. The card's thresholds (1e-12 for row 315's degeneracy;
  for row 324 an order-5 bound of 1e-8 and a median more than 0.5 from log 3; 1e-12 for the electron statements) are
  the card's own, set with the outputs known; the sealed cells are required too, through their printed line. Main's
  code is copied verbatim into the card's folder, its loaders replaced, and two non-loader lines off the run's path
  (census.py line 113 and the_canonical_cusp.py line 335, imports of multiprocessing the rerun refuses; MANIFEST.md
  lists each). No data enter
- identifications: none of the card's own; "electron" is the law map's word for the lepton sector's m1
- definitions: a sector's spectrum is the singular values of its coupling, ordered m1 ≤ m2 ≤ m3; the small-cut norms are
  B1667's column at Re τ = 1/4, the exact norms B1838's horoball norms over B1667's Dirichlet cell minus the horoball
  at L_max(τ) or L_2(τ). Row 315 holds when max |m2/m3 − 1| is below 1e-12 at both norms on its lines; row 324 stands
  when the order-5 worst |R − 1| is below 1e-8 and the median log R2 on the 3|N lines is more than 0.5 from log 3
  (0.145 at the exact norms, 0.178 small-cut); the order-12 zero holds when every exact lepton m1/m3 is at most 1e-12
  on all 48 lines, both horocycles and both readings; the order-9 lift is read here as every exact lepton m1/m3 above
  1e-12 on all 36 (the post hoc threshold); the sealed cell P2 asked for above 1e-6, and fails that at c* too
  (1.05e-7), as it failed at the stuck c (1.89e-8)
- imports: none
- premises on main: B1667, B1656, B1838, B1691, B1701, B1711, B1712, B1729, and the code of B1838, B1726, B1667, B1654,
  B1723 and B1691 at 88a1e9474, as the card's folder copies it
- decisive script: relays/chat1_2026-11-28_p589c/card_p589c.py, SHA-256 782a8ec6315362dd, depends on the standard
  library, mpmath, numpy and scipy, run as python3 relays/chat1_2026-11-28_p589c/card_p589c.py, output SHA-256
  c906e191918a9ea4, heavy
- decisive lines: 11 lines marked "DECISIVE:", SHA-256 cf314917f2465b81
- failing control: python3 relays/chat1_2026-11-28_p589c/card_p589c.py --control
- second computation: none that shares no code with B1838's instrument. Within the sealed scripts every quantity is
  read at both norms, and P0 reproduces B1667's json to 8.4e-12. The copy reproduces both sealed outputs of 2026-11-25
  (p589c_exact_rows_out.txt, SHA-256 3f42cff85160b580, and p589c_posthoc3_out.txt, SHA-256 3581f09ea8a456ad) byte for
  byte, here and in main's sandboxed rerun, run here in full (REPRODUCED, 1 975 s, the stated output hash); the side
  json files equal the old ones here (not committed). The script prints those two checks outside its decisive lines,
  which departs from M88's wording: a float's last printed digit could differ on another machine. A rerun whose byte
  line reads False has failed the copy's test, and the card goes back to main, whatever its decisive lines say. Q0
  compares two four-digit strings of a residue from digit-losing theta sums, which is fragile across machines
- already on main?: topic_sweep.py "exact norms|exact horoball|stuck accessory" at be47862d1: 4 of 1760 arcs and 8
  register rows match the words; the old card's sweep found no arc that re-reads rows 313, 315, 316 or 324 at the exact
  norms, and B1816 records that the instrument's Newton is degenerate on Re τ = 0
- what would make it fail: an order-12 line lifted at the exact norms at the uniformising accessory parameter; a
  uniformising branch on Re τ = 0 other than the limit from Re τ > 0; row 315's spectrum not degenerate at the exact
  norms on its lines; or row 324's median moving to log 3. The control leaves the accessory parameter stuck on
  purpose at 3.1i, as at_tau() returns it: the largest exact order-12 lepton m1/m3 is then 8.8e-10, and the order-12
  check fails. It repeats Q0's computation and does not exercise the decisive script's parsing
