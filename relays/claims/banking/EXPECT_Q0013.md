# Expectation, Q0013 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-28. Card: relays/claims/CLAIM_2026-11-28_p631_two_loops_in_the_queue_form.md on chat1/web-seat at
8de29cc2ded4e79796fbc0de56cc041f939915ca (the queue's record). Read: the card, its decisive wrapper card_p631.py and its
recorded output, and the queue record. Not read: the sealed p631_two_loop.py's body, the peer note. No code run yet.*

## The claim

K1 the Fourier and lattice evaluations of E_2 and E_3 agree; K2 the lattice sunset C111 equals E_3 + zeta(3) within 2e-3
at tau = i, omega, 0.2 + 1.7i; K3 E_2^2 is outside the span of 1, E_2, ..., E_5 (relative residual above 1e-8); K4 on the
imaginary axis at beta/alpha = 1e-2, 1e-3, 1e-4 one stationary point of -alpha E_3 + beta E_2^2, with |V_2/V_1| within 0.1
of 3/4 (at y about 102.7, 1030, 1.02e4); K5 on Re tau = 0 and 1/2, Im tau in [1.2, 20], beta/alpha in +-[1e-4, 10], no
stationary point with |V_2| <= |V_1|/3.

## How this seat will recompute

Own code with mpmath and numpy. E_s by its Fourier expansion (the constant terms 2 zeta(2s) y^s and the zeta(2s - 1)
y^(1-s) term, and the K-Bessel sum), checked against a direct lattice sum with a tail correction. C111 by its own lattice
sum over p1 + p2 + p3 = 0 at several square cutoffs, extrapolated in 1/N. K3 on this seat's own sample of points. K4 and
K5 not on a grid of beta/alpha but on the continuum: at each y the stationary condition fixes beta/alpha as
r(y) = E_3'(y) / (2 E_2(y) E_2'(y)), and there |V_2/V_1| = |r(y)| E_2(y)^2 / E_3(y); K5 holds for every beta/alpha in the
range if that ratio exceeds 1/3 wherever |r(y)| lies in [1e-4, 10], on both lines, on a fine mesh of y in [1.2, 20]. On
Re tau = 1/2 the series is real, as on Re tau = 0.

## Expectations

| | expectation | prior |
|---|---|---|
| X1 | E_2, E_3 Fourier and lattice agree to 1e-6 | 90% |
| X2 | C111 - (E_3 + zeta(3)) below 2e-3 at the three points | 80% |
| X3 | E_2^2 residual well above 1e-8 on this seat's points | 90% |
| X4 | one stationary point per K4 case near the recorded y, ratio near 0.75 | 85% |
| X5 | the ratio above 1/3 on the whole mesh where r(y) is in range (the continuum form of K5) | 75% |
| V | ACCEPT | 70% |
