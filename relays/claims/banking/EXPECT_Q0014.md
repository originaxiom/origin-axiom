# EXPECT_Q0014 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0014, `relays/claims/CLAIM_2026-11-28_p632_instability_spectrum_in_the_queue_form.md` on chat1/web-seat at
8de29cc2ded4e79796fbc0de56cc041f939915ca. Written from the card and its queue record alone, before reading or running its
script and before running any code for this card. Not read: the peer's note, the other banking seat's branch, the
producer's sealed module.

## By hand, before any run
- s = 0: F_0 1 = 2, so lambda_1 = 2 with h constant (F_0 is positive; Perron-Frobenius for this positive operator).
- lambda_1 strictly decreasing in s: (1 + x)^(-2s) decreases strictly in s for x > 0, so F_s decreases as a positive
  operator, and its leading eigenvalue decreases; strictly, since the weight drops on all of (0, 1].
- As s -> 1 the operator tends to the Farey transfer operator, whose leading value is 1, with the non-integrable 1/x
  as its eigenfunction; so lambda_1(0.95) a little above 1 (the card's 1.0203) and h_s decreasing, steep near the cusp x = 0,
  is what I expect.

## What I will compute, my own code (numpy)
λ₁ and h_s by a method other than Chebyshev collocation: Nyström collocation at Gauss–Legendre nodes, with barycentric
interpolation, at N = 64, 128 and 256. I check the result by power iteration on the interpolant. Separately, λ₁ from my
own word sums Z_n(s) at a few values of s. Then h_s on a grid of 2001 points: positive, and constant at s = 0. At s = 0.1
to 0.9 I check it is strictly decreasing, and give the smallest step. I check that λ₁ falls strictly over the card's
values of s, and give λ₁(0.95) to 4 decimals.
Control (K8): the second eigenfunction at s = 0.5 must change sign and fail the monotonicity check.

## Expectation
ACCEPT, the negative read as "on the 11 values of s tried, h_s has no interior extremum" (K9: a finite set of s, not all
of [0, 1)). REFUSE if any h_s at s = 0.1 to 0.9 has an interior extremum or a sign change, or λ₁ fails to fall, or
λ₁(0.95) differs from 1.0203 beyond the discretisation's agreement. At s = 0.95 I expect convergence to be slow near
the cusp, and I will say how many digits my N's agree on there.
