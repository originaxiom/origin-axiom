# EXPECT_Q0013 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0013, `relays/claims/CLAIM_2026-11-28_p631_two_loops_in_the_queue_form.md` on chat1/web-seat at
8de29cc2ded4e79796fbc0de56cc041f939915ca. Written from the card and its queue record alone, before reading or running its
script and before running any code for this card. Not read: the peer's note, the other banking seat's branch, the
producer's sealed module.

## By hand, before any run
- With E_s = a_s y^s + b_s y^(1-s) + (exponentially small), a_s = 2 zeta(2s)/pi^s: for large y, V = -alpha a_3 y^3 +
  beta a_2^2 y^4 has its stationary point at y* = 3 alpha a_3 / (4 beta a_2^2), where |V2/V1| = beta a_2^2 y*/(alpha a_3)
  = 3/4 > 1/3. For beta/alpha < 0 there is none at large y. So the claim is what I expect, and the card's control value
  0.75 is this asymptote.
- E_2^2 = a_2^2 y^4 + 2 a_2 b_2 y + b_2^2 y^-2 + ...; no E_s (s = 2..5) and no constant has a y^1 term, so E_2^2 is outside
  the span of 1, E_2 to E_5 as functions; the card says "numerically", which is weaker than this.

## What I will compute, my own code (numpy, mpmath)
1. E_s on both lines by the Fourier (Bessel) expansion, checked against a direct lattice sum at a few points.
2. C_111 by a direct lattice sum with growing cutoffs, extrapolated, against E_3 + zeta(3) at a few points (card: 2e-3).
3. The least-squares residual of E_2^2 on span(1, E_2..E_5) over points on the lines.
4. For many more values of beta/alpha than the card's 60 (K7: its 60 are not listed, so I take a dense log grid over
   +-[1e-4, 10]), every stationary point of -E_3 + r E_2^2 on Re tau = 0 and 1/2, Im tau in [1.2, 20] (and on the
   imaginary axis to 3/r for r = 1e-2, 1e-3, 1e-4), with the ratio |V2/V1| at each; the claim fails if any is <= 1/3.
5. Control: with the bound widened to 1 and the range to 300 at r = 1e-2, a point inside the bound must be found.

## Expectation
ACCEPT, the negative held as "no such point found on the lines, range and ratios searched" (NOT FOUND, K9), unless my
denser grid finds a stationary point with |V2/V1| <= 1/3 (then REFUSE), or C_111 differs from E_3 + zeta(3) beyond 2e-3.
The physical identifications (V1 proportional to -E_3, V2 to E_2^2, E_2^2 for the quartic figure-eight) are hypotheses I do
not check; the verdict will be conditional on them.
