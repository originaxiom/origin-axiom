# Expectation, Q0001 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-28. Card: relays/claims/CLAIM_2026-11-27_B2011_main_trial.md on main at 0fd0a70f43722056a17992667016a31b34cfb1d3
(the queue's record). Read: the card, its decisive wrapper and the recorded output of the arc's script that it selects
from, the intake's record check, and the queue record. Disclosed: this seat read the same card once on 2026-11-27, as a
model of the new form, before it was handed to banking; and the queue record's history line about the peer stage was in
view. The peer note was not opened. No code run yet.*

## The claim

At mod 135 the orbit of (3, 3, 3) under L, R and their inverses has 2 880 points; C fixes 3; the neutral sector has
dimension 962 and the charged sector (q = 1) 959; gcd(p_neutral(2x)/2^d, S) has degree 949, so 10 charged roots are
unpaired, and they are exactly the roots of (x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1); the reduction mod 27
maps the mod-135 orbit onto the mod-27 orbit.

## How this seat will recompute

Own code: the orbit by breadth-first search; the neutral sector on the C-orbit sums and the charged sector on the
w-twisted sums, built from the six moves' action; their characteristic polynomials, the gcd and the quotient computed
modulo several primes p = 1 mod 3 with w a cube root of unity in F_p (python-flint's nmod_poly and nmod_mat). This is a
multi-prime check, not an exact computation over Z by the CRT, and the verdict will say so.

## Expectations

| | expectation | prior |
|---|---|---|
| X1 | 2 880 points, C fixes 3, dimensions 962 and 959 | 90% |
| X2 | the gcd has degree 949 at every prime used | 80% |
| X3 | the unpaired part equals the four named factors' product at every prime used | 80% |
| X4 | the mod-135 orbit reduces onto the mod-27 orbit | 90% |
| V | ACCEPT | 70% |
