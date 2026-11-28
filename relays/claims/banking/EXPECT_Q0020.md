# EXPECT_Q0020 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0020, `relays/claims/CLAIM_2026-11-27_a2_peer_sm_fc2_c23_and_c24_verification.md` on agy-002/verify at
080441e86287d7edf5b961d73f9a6ce656380b3a. Written from the card and its queue record alone, before reading or running its
scripts and before running any code for this card. Not read: the peer's note, the other banking seat's branch (whose
cards SM-C23 and SM-C24 this card verifies), the producer's scripts.

## What the card lets me check
- Self-contained: the counting. Points of exact order 30 in (Q/Z)^2 with denominators 30: 900 (1 - 1/4)(1 - 1/9)(1 - 1/25)
  = 576, so 288 pairs +-v; those with 5 | den(a); the act-line subset 6v mod 1 in {k(1,2)/5}; the claimed 240 and 48 and
  their ratio 5. By hand: 6v mod 1 is a nonzero point of (Z/5)^2 whose first coordinate is nonzero when 5 | den(a); those
  are the points off the vertical line, on 5 of the 6 lines of P^1(F_5), 4 nonzero points each, one of them the act line;
  so 240/48 = 5 should come out, which is the card's structural explanation.
- Not checkable from the card: the 15 invariants, the covariance residuals (1.61e-53), the alignment, hierarchy and
  1/60-grid convergence, and the 12 classes. They rest on Frame C's Yukawa construction, which the card gives only by
  reference (B1945's parts and U_of, B1919/B1940's F_u, "reading S", the "DR triplet"), not in its definitions; rebuilding
  Frame C from those arcs is a project of its own, beyond one banking card.
- Labels (K9): the effect says "proves" for numerical checks on 180 cases and on 576 points; "reach: class" for a finite set.

## Expectation
RETURN, with the counting recomputed. It would become decidable with Frame C's construction written out, or pinned as one
file on main that a banking seat can implement from, and with the labels brought to "computed at the cases named". If my
counts differ from 576, 288, 240, 48 or the ratio 5, REFUSE.
