# B2015 — Listening card 29: agy-exp's six-move rate law, the freeze at mod 81, and the full spectrum at mod 729

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why

- **The claims:** agy-exp's X-EXHAUSTIVE-LISTENING (harvest row 2015, `origin/agy/self-consistent-loop-2026-11-11` @
  `3027116dc`) makes three claims checkable on main's code.
  - **EL-3:** the six-move sum W obeys Λ_W(M) = 2√(5 + 4cos(π/M)), with the values 2√7, 5.919044…, 2√(6 + √5), 5.989477…
    and 5.866473… at mod 27, 81, 125, 625 and 343.
  - **The freeze:** on the 3-tower the law freezes at mod 81. At mod 243 the largest eigenvalue on the new fibre is
    5.672086… < 5.919044….
  - **EL-2:** the halving holds on the full spectrum at mod 729 (17,498 neutral and 17,495 charged modes). B2007 checked it
    on the leading modes only.
- **The relation to what is known:** B2011 checked the companion law for P_L + P_R. agy's C60 gave 2√(5 + 4cos(π/9)) as the
  neutral rate at mod 81, and B2011 A7 checked it.

## The system and the checks (main's own code)

- **The operator:** W, the six-move sum, on the largest orbit over the common point: mod 27, 81, 243, 729 (this is the orbit
  of (3,3,3)), and mod 125, 343, 625.
- **R1:** the largest eigenvalue of W below 6, against 2√(5 + 4cos(π/M)) with M = 3, 9, 5, 7, 25. The test is exact: the
  minimal polynomial of the value, built from cos(π/M)'s, divides W's characteristic polynomial. Over ℤ for orbits up to
  1176 points; modulo three 62-bit primes at 625.
- **R2:** at mod 243, W's spectrum on the functions orthogonal to those pulled back from mod 81. Its largest eigenvalue, and
  whether 5.919044… stays W's largest below 6.
- **R3:** at mod 729, the neutral sector's eigenvalues, halved, against the charged sector's. Double-precision
  eigenvalues of the symmetric neutral matrix and the Hermitian charged matrix, matched to 10⁻⁷ after the three exceptions
  (±3 and 0, halved) are set aside; the counts of matched and unmatched.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| R1 | the law holds exactly at all five levels | 0.75 |
| R2 | 5.919044… stays the largest below 6 at mod 243; the new fibre's largest is 5.672086… | 0.75 |
| R3 | every charged eigenvalue at mod 729 matches a halved neutral one, and the neutral ones left over are exactly the three exceptions | 0.85 |

## What it means

- **If R1 holds:** the six-move sum's slow rate follows one formula at the primes 3, 5, 7 in the levels run, alongside the
  formula B2011 checked for P_L + P_R.
- **If R2 holds:** the 3-tower's rate is set at mod 81, and the layer above it adds only faster modes there.
- **If R3 holds:** the halving at mod 729 is checked on the whole spectrum, not only the leading modes (numerically).
- **Nothing is compared with data.**
