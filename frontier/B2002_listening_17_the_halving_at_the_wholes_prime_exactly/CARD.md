# B2002 — Listening card 17: the halving at the whole's prime, exactly — which of the neutral sector's modes reappear at half strength in the charged pair, and over what fields

Written 2026-11-25, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

B2001 found, post hoc, that on the 3-tower (the orbit of (3,3,3) mod 27 and 81) the leading eigenvalues of the covariant
unfolding's charged sector are exactly half those of its neutral sector: 2√7 against √7 at mod 27, and 5.919… against 2.959…
at mod 81. At the primes 5 to 13 they are not.

Counting dimensions shows the pairing cannot be complete. At mod 27 the charged sector has 23 dimensions and the neutral one
has 25 eigenvalues below the top. So the question is exactly which modes pair, and over what fields they live.

## The system (nothing chosen)

- **The operators:** the symmetric six-move unfolding (B2001) on the orbit, mod 27 and 81 and, for contrast, on the leaf mod 5
  and 7.
- **The neutral operator:** on the C-orbits, as an integer matrix.
- **The full operator:** an integer matrix on the points.
- **FLINT, exactly:**
  - the characteristic polynomials of both;
  - the charged pair's polynomial as their quotient (it is the square of one charged sector's polynomial, B2001's G2);
  - the factorisations over ℤ.
- **The pairing test:** for each irreducible factor f of the neutral polynomial,
  whether the polynomial g(x) = f(2x)/lead, made monic, divides the charged polynomial.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| H1 | the charged polynomial is the square of a polynomial over ℤ (B2001's G2, exactly) | 0.9 |
| H2 | on the 3-tower, the factor carrying the neutral sector's slowest mode has its halved version dividing the charged polynomial | 0.85 |
| H3 | on the 3-tower, more than half of the neutral sector's non-top degree is paired this way | 0.4 |
| H4 | at mod 5 and 7 no neutral factor of degree ≥ 1, other than possibly x, has its halved version in the charged polynomial | 0.6 |
| H5 | the neutral slowest mode at mod 81 (5.919044…) generates a field containing cos(π/9), conductor 9 (as B1997's rate did) | 0.4 |

## What it means

- **If H2 and H3 hold:** the whole's prime ties the two sectors by an exact halving of a large part of the spectrum. That is a
  structural relation between what the whole remembers and what it forgets, with its reason still to be found.
- **If only H2 holds:** the tie is confined to the leading modes.
- **H5 tests whether the ninth roots of B1997 run through this sector too.**
- **Nothing is compared with data.**
