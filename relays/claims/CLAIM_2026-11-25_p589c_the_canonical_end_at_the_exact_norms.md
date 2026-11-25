# CLAIM CARD — P-589 (c): three of the law map's six data-free rows "at the canonical end" re-read at the exact horoball norms. B1701's degeneracy (row 315) and B1729's NEGATIVE (row 324) hold. B1712's exactly massless order-12 electron (row 313's note) holds at the exact norms only on the 16 lines with 6a in ℤ, and is lifted by about 1e-10 of the heaviest lepton on the other 32 (post hoc). B1711's order-9 electron is lifted at both norms. Three data-free rows are not re-read, with reasons, and the data-facing rows are declined

- seat, branch, commit: chat1, origin/chat1/web-seat.
  - The script is at 37b3a1157, with a print fix at e52f68352; its output is at 15c7656b6.
  - The post hoc checks are at 8804dedd2 (output at 1fbe865e6) and 5d8bbbb34 (output at f93da79eb).
- kind: computation (a re-read under a changed end formula)
- touches: P-589, P-421; law-map rows 313, 315 and 324 (B1701, B1711, B1712, B1729); row 299's scope note
- effect: conditions — row 313's note from B1712: "exactly massless at order 12" holds at the small-cut end. At the
  exact end it holds only on the lines with 6a in ℤ. Supports rows 315 and 324 at the exact norms.
- imports: none
- premises on main: B1667 (the cell, the horocycles and the small-cut column), B1656 (the four twisted channels), B1838
  (the exact-norm instrument), B1691 (the end-data Higgs), the frame at 88a1e9474
- decisive script: relays/chat1_2026-11-25_p589c/p589c_exact_rows.py, SHA-256 6645375691df3efb (a7503852edc474de
  before the print fix). It imports main's frame and B1838's instrument from a checkout at 88a1e9474, passed as its
  argument, and refuses any other commit. Run as `python3 -B p589c_exact_rows.py <main checkout>` (about 18 minutes).
  Output p589c_exact_rows_out.txt, SHA-256 3f42cff85160b580; values in p589c_exact_rows.json.
- post hoc checks: p589c_posthoc.py (SHA-256 867658f34b1b0424; output 17af3f10c06fd3b7) and p589c_posthoc2.py
  (SHA-256 0808495a742abd94; output 0938fafb989fed61), each with its reading rule in its docstring.
- second computation: within the script, every quantity at both norms; P0 reproduces B1667's json to 8.4e-12. The
  order-12 residue is followed at three quadratures. Not independent of B1838's instrument.
- already on main?: B1838 built the instrument, and the six's best rows are P-421's; no arc re-reads rows 313, 315 or
  324 at the exact norms.
- what would make it fail:
  - the order-12 residue on the 32 lines falling to rounding when the instrument's other parameters are refined (it
    would then be numerical, and the zero would hold);
  - a line with 6a in ℤ lifted at the exact norms;
  - a re-read of rows 295, 312 or 352 that the exact norms change.

## What it means

- [E] At the exact norms, row 315's degenerate spectrum holds to 7e-16. Row 324's 3 | N median log R2 moves from 0.178
  to 0.145, far from log 3.
- [E] At order 12 the exact norms give m1/m3 converging, as the quadrature is refined, to 8.7e-11 to 1.7e-10 on the
  32 lines whose a has order 4 or 12. It stays at 1e-16 on the 16 lines with 6a in ℤ.
- [J] The order-12 electron's exact masslessness is partly the small-cut formula's.
- [E] Rows 295, 312 and 352 are not re-read (dated 2026-11-25). The data-facing rows are declined to a seat cleared
  for data.

0 of 19.
