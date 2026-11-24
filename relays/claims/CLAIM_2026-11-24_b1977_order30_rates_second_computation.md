# CLAIM CARD — B1977's order-30 rates, reproduced by a second assembly to double precision; between heights 30 and 40 every rate lies within 4.2e-4 of a multiple of 1/60, and V₂₃'s rate at the five slow points moves to 0.0332, towards 1/30

- seat, branch, commit: chat1, origin/chat1/web-seat. The outputs are at 580bb80a1 (all 96 points) and 5e4db6850 (the
  addendum at 16 points).
- kind: computation
- touches: P-860, P-845
- effect: supports — B1977's G1 to G5, on P-860 (d)
- imports: none
- premises on main: B1977 and B1976. The frame is B1940's frame_mp: its F_u norms, the canonical end's table
  (B1927), the triplet's q-series, and the charges.
- decisive script: relays/chat1_2026-11-24_chk1/chk1b_independent.py, SHA-256 9d6b83741d9c6715. It depends on mpmath
  and on main's B1940 frame_mp for the four items above, so it is not free of dependencies. Run as `python3 -I -u
  chk1b_independent.py <a checkout of main>`. Output chk1b_out.txt, SHA-256 785d259ba76449fb.
- second computation: this card is itself the second computation for B1977. Its assembly is W-D2's referee's code: its
  own theta sums, η by product, coupling, and masses from the eigenproblem of Y Yᴴ at 40 + 4y digits. At 16 points (the
  five slow ones and every eighth), heights 20 and 30, the nine rates and the least diagonal agree with B1977's json to
  double precision. The full run, chk1_run.py (SHA-256 5d2fcd65b076c434), at all 96 points uses W-D2's transcription of
  fbar and agrees to the last bit. It also adds the rates between 30 and 40 and at the column 0.31.
- already on main?: B1977 itself (71a416796); no second computation is recorded there.
- what would make it fail: any of the 96 points with a rate differing from B1977's json by more than 1e-6, or the rates
  between 30 and 40 leaving the grid of 1/60.

0 of 19.
