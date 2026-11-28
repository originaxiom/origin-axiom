# Expectation, Q0002 (banking seat V1, fam1-v1-unset-04), committed before any computation

*2026-11-28. Card: relays/claims/CLAIM_2026-11-27_B2012_main_trial.md on main at 0fd0a70f43722056a17992667016a31b34cfb1d3.
Read: the card, its decisive wrapper, the recorded output of the arc's script it selects from (the six "N1" lines), the
intake's record check and the queue record. Disclosed: the queue record's history line about the peer stage was in
view; the peer note was not opened. No code run yet.*

## The claim

On six orbits (the largest orbit on the leaves k = 5 mod 7, k = 6 mod 11, k = 9 mod 13, and the orbit of (3, 3, 3) mod 27,
81 and 135), T4 = L + R + L^-1 + R^-1 equals S(C + C^2) + (C + C^2)S point by point, and its characteristic polynomial is
R(x + 4) R(x + 2) (x - 4)^d1 (x + 4)^d2 (x + 2)^d3 (x - 2)^d4, with R and d1 to d4 read from A = 3 P(1 + S)P on the C-orbit
sums: exact over Z on the five smaller orbits, modulo three primes on the mod-135 orbit. The recorded sizes: 64, 60, 112,
72, 648 and 2 880 points; 22, 20, 38, 26, 218 and 962 C-orbits.

## How this seat will recompute

Own code: the leaves and their orbits by breadth-first search; T4, S and C as maps on points, the pointwise identity
checked on every point; A built on the C-orbit sums; the characteristic polynomials over Z with python-flint (fmpz_mat)
on the five smaller orbits, and modulo several primes on the largest; the factorisation compared coefficient by
coefficient.

## Expectations

| | expectation | prior |
|---|---|---|
| X1 | the six orbits' sizes, C-orbit counts and sigma's fixed counts as recorded | 85% |
| X2 | the pointwise identity on every point of every orbit | 90% |
| X3 | the factorisation exact on the five smaller orbits | 80% |
| X4 | the factorisation modulo every prime used on the mod-135 orbit | 80% |
| V | ACCEPT | 70% |
