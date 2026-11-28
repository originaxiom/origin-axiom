# Expectation, Q0014 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-28. Card: relays/claims/CLAIM_2026-11-28_p632_instability_spectrum_in_the_queue_form.md on chat1/web-seat at
8de29cc2ded4e79796fbc0de56cc041f939915ca (the queue's record). Read: the card, its recorded decisive output and the queue
record. Not read: the sealed p632_modes.py's body, the decisive wrapper's body, the peer note. No code run yet.*

## The claim

For (F_s f)(x) = (1 + x)^(-2s) [f(x/(1 + x)) + f(1/(1 + x))] on [0, 1]: at s = 0, lambda_1 = 2 with h constant; at
s = 0.1, ..., 0.9 (and 0.95) h_s is positive and strictly decreasing, so it has no interior extremum; lambda_1 falls
strictly, 1.848487, 1.710186, 1.584087, 1.469311, 1.365112, 1.270911, 1.186353, 1.111484, 1.047292, 1.020343; the mass of
h_s on [0, 0.05] rises strictly, 0.0546 to 0.2968; F_1(1/x) = 1/x.

## How this seat will recompute

Own code with numpy, by another discretisation than the card's: Nystrom-style power iteration with h held on
Gauss-Legendre nodes of [0, 1] and moved by barycentric interpolation, at three sizes; lambda_1 by the iteration's ratio,
h_s read on 2001 points, the mass by quadrature of the interpolant; the next eigenvalues of the same matrix reported,
not claimed. A second, discretisation-free check of lambda_1: the word sums Z_n over words in L and R holding both
letters, Z_(n+1)/Z_n, as the card defines them, computed with this seat's own enumeration.

## Expectations

| | expectation | prior |
|---|---|---|
| X1 | lambda_1 at the eleven s agrees with the recorded six decimals (to 1e-6, perhaps worse at s = 0.95) | 80% |
| X2 | h_s positive and strictly decreasing on the 2001 points at s = 0.1 to 0.95 | 85% |
| X3 | the masses agree with the recorded four decimals | 80% |
| X4 | the word-sum ratio within 1e-3 of lambda_1 at s = 0.25 and 0.5 | 75% |
| V | ACCEPT | 75% |
