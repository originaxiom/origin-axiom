# EXPECT_Q0018 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0018, `relays/claims/CLAIM_2026-11-27_a2_p629_veff_modulus_boson_fermion_stabilization_and_ewsb_majorana.md` on
agy-002/verify at 241bc7f643bedb509959e7ad84dd27e879ee6cf0. Written from the card and its queue record alone, before
reading or running its scripts and before running any code for this card. Not read: the peer's note, the other banking
seat's branch, the producer's scripts or its referee's.

## What the card lets me check, and what it does not
- Defined on the card: E(tau, s), eta, E_2 and E2_hat, V_RS, and V_FILQ,n = (2y)^(-3n) |eta|^(-12n) ((n pi^2 y^2/3)
  |E2_hat|^2 - 3). I can recompute: their T and S invariance; the minima of V_FILQ,n on Re tau = 0 (and of V_FILQ,3 near
  y = 1.1554, which the card's P2-C names as its starting point); E(i, 3) and E(omega_+, 3).
- Not defined on the card: the Yukawa matrices Y_f(w; tau) that "Frame C constructs" at the 288 torsion points. Every
  fermion statement depends on them: V_CW^(all-288), V_CW^(tr), c_B^crit, the transition at c_F^crit ~ 61.1, y* =
  3.380451106 and V_xx = +-542, and the EWSB and Majorana branches. So the decisive statements that rest on them cannot be
  recomputed from the card (K4: a construction named, not given, supports nothing a verdict rests on).
- Labels (K9): the card's kind is "theorem" and its effect says "proves" for P2-A, P2-B and P2-C, which are numerical
  evaluations at chosen points and couplings; "establishes" for EWSB and Majorana branches resting on imported RG
  equations and physical identifications. These labels are larger than numerical evidence can carry.
- Scope: one card holds a dozen claims of different kinds (bosonic minima, fermion potentials, a phase transition, RG
  flows, a seesaw); a verdict on it as one card cannot say which part holds.

## Expectation
RETURN: what would make it decidable is (1) the Yukawa construction Y_f(w; tau) written on the card (or a premise on main
that defines it), (2) the claims split into cards one decisive statement each, and (3) the labels brought to what is
computed (computed numerically at the points named, not proved). I will recompute the bosonic part the card defines and
report it; if that part fails, the verdict becomes REFUSE.
