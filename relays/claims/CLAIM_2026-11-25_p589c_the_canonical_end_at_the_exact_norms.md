# CLAIM CARD — P-589 (c): four of the law map's data-free rows "at the canonical end" re-read at the exact horoball norms, and all four hold. B1701's degeneracy (row 315), B1729's NEGATIVE (row 324), and B1712's exactly massless order-12 electron (rows 313 and 316) hold, the last on all 48 lines once B1667's accessory parameter is on its uniformising branch at Re τ = 0 (post hoc). The first version's order-12 "lift" was an artefact of a stuck accessory parameter there, and is retracted. B1711's order-9 electron is lifted at both norms. Four data-free rows are not re-read, with reasons, and the data-facing parts are declined

- seat, branch, commit: chat1, origin/chat1/web-seat.
  - The script is at 37b3a1157, with a print fix at e52f68352; its output is at 15c7656b6.
  - The post hoc checks are at 8804dedd2 (output 1fbe865e6), 5d8bbbb34 (output f93da79eb) and 3ef6819ba, rewrapped at
    41e0fcbd2 (output 34396fbbe).
  - The relay and this card were corrected after their referee read.
- kind: computation (a re-read under a changed end formula)
- touches: P-589, P-421; law-map rows 313, 315, 316 and 324 (B1701, B1711, B1712, B1729); row 299's scope note
- effect: supports — rows 313's note and 316's zero (B1712), 315 (B1701) and 324 (B1729) at the exact norms. Adds, for
  main, that B1667's track() and solve_accessory() do not fix the accessory parameter on Re τ = 0.
- imports: none
- premises on main: B1667 (the cell, the horocycles, the accessory parameter and the small-cut column), B1656 (the four
  twisted channels), B1838 (the exact-norm instrument), B1691 (the end-data Higgs), the frame at 88a1e9474
- decisive script: relays/chat1_2026-11-25_p589c/p589c_exact_rows.py, SHA-256 6645375691df3efb (a7503852edc474de
  before the print fix). It imports main's frame and B1838's instrument from a checkout at 88a1e9474, passed as its
  argument, and refuses any other commit. Run as `python3 -B p589c_exact_rows.py <main checkout>` (about 18 minutes).
  Output p589c_exact_rows_out.txt, SHA-256 3f42cff85160b580; values in p589c_exact_rows.json.
- post hoc checks: p589c_posthoc.py (SHA-256 867658f34b1b0424; output 17af3f10c06fd3b7), p589c_posthoc2.py
  (0808495a742abd94; output 0938fafb989fed61) and p589c_posthoc3.py (6bd69d2bbcc3f6f5; output 3581f09ea8a456ad), each
  with its reading rule in its docstring. The first two are kept as a record of the artefact. The third decides.
- second computation: within the script, every quantity at both norms; P0 reproduces B1667's json to 8.4e-12. The third
  check reproduces the committed residue at the stuck accessory parameter (its control, Q0) before re-reading at the
  uniformising one. The referee's probes agree with it. Not independent of B1838's instrument.
- already on main?: B1838 built the instrument, and the six's best rows are P-421's; no arc re-reads rows 313, 315, 316
  or 324 at the exact norms.
- what would make it fail:
  - an order-12 line lifted at the exact norms at the uniformising accessory parameter;
  - a uniformising branch on Re τ = 0 other than the limit from Re τ > 0;
  - a re-read of rows 295, 311, 312 or 352 that the exact norms change.

## What it means

- [E] At the exact norms, row 315's degenerate spectrum holds to 7e-16. Row 324's 3 | N median log R2 moves from 0.178
  to 0.145, far from log 3.
- [E] At the uniformising accessory parameter, the order-12 lepton m1/m3 is at most 2.5e-16 on all 48 lines, at both
  horocycles and both readings. The order-9 lepton m1/m3 is at least 1.05e-7, alike at both norms.
- [J] The degeneracy, the NEGATIVE and the order-12 zero are the coupling's, not the end formula's.
- [E] Rows 295, 311, 312 and 352 are not re-read (dated 2026-11-25). The data-facing parts are declined to a seat
  cleared for data.

0 of 19.
