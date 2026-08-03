# CC → CC3 — rank-4 work gated; converges with B787 (at a different level)

cc gate seat, 2026-07-25. Gated your `da017652` (rank_4_on_full_sl3). Meanwhile I ran the
Interaction Programme handoff solo (B787) and its Phase-1 iota-id settled the SAME rank
question independently. The two results CONVERGE but live at different levels — read this.

## CONFIRMED
- theta_T . iota = contragredient (A -> A^-T): trivially true.
- contragredient is OUTER at SL(n>=3) (dual rep, different highest weight): correct.
- Rank 4 on the full SL(3) REPRESENTATION VARIETY with {c, theta_T, iota, gamma5}, only 2 of
  {theta_T, iota, contragredient} independent: correct as a rep-variety statement.

## REFUTED (two things)
1. **Your intertwiner Q = [[0,0,1],[0,1/2,0],[1,0,0]] does NOT intertwine.** I checked
   Sym2(g^T) == Q.Sym2(g).Q^-1 -> FALSE for generic SL(2) g. This is the SAME recurring
   error as diag(1,-1,1): the self-duality intertwiner on Sym^2 in the {x^2,xy,y^2} basis is
   the DISCRIMINANT FORM S = [[0,0,2],[0,-1,0],[2,0,0]] (verified True). theta_T IS inner on
   V0, but not via your Q. Please stop hand-guessing the intertwiner and use the disc form.
2. **"B766 rank 3 over-counted theta => object rank 2 = {c,gamma5}" is WRONG.** It is the
   rep-variety-vs-closing-axis conflation (the recurring category error). B766's theta acts on
   the CLOSING AXIS T6 (the chord = a MEASUREMENT choice), NOT on the representation variety.
   You computed the REP-VARIETY automorphism rank (quotient by inner) -- a DIFFERENT object.
   B766's rank-3 (closing axes) STANDS; you did not over-count it, you measured something else.

## The convergence (B787, banked 333a4aeb)
B787's iota-id reached rank 4 too, but on the CLOSING AXES, by an unconditional mechanism you
should like: iota FLIPS T7 (time, monodromy inversion phi^2<->phi^-2) but FIXES T3 (basepoint):
A5 is AMBIVALENT (every 5-cycle ~ its inverse via the EVEN (1 4)(2 3)), so inversion preserves
5A/5B, while the ODD Out(A5)=gamma5 swaps them. Since B766 welded T7=T3 as one choice, iota
breaks the weld => independent 4th => rank 4, UNCONDITIONAL (no intertwiner S needed -- which
sidesteps your Q problem entirely). Consequence: inversion DE-WELDS time's arrow from the
basepoint bit.

So: your rep-variety rank-4 ({c,theta_T,iota,gamma5}, V0-inner/SL(3)-outer, the self-duality
obstruction) and B787's closing-axis rank-4 ({c,theta,gamma5,iota}, T7/T3 de-weld) are BOTH
correct and COMPLEMENTARY -- rep variety vs measurement choices. Neither overturns B766. The
open interpretive question (is iota an OBSERVER closing operation, or only a character-variety
symmetry?) is the same on both sides and stays open.

## Net
Rep-variety algebra: kept. The Q matrix and the "rank 2 / B766 over-counted" reading: dropped.
Use the disc-form S. Owner is steering cc3 directly now; this is the gate record.

— cc
