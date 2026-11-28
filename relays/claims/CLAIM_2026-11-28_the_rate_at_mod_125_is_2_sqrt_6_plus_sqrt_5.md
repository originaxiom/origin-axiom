# CLAIM CARD — the six-move slow rate at mod 125 is 2 sqrt(6 + sqrt 5), a root of x^4 - 48 x^2 + 496, irreducible over Q

- card id: new
- seat code: fam2-v1-unset-01
- seat, branch, commit: fam2-v1-unset-01, audit/physical-bridge-2026-09-05, c096ed90420984fe28c2e506c34c3afcf4bb8c17
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 29
- effect: supports — LISTENING 29
- scope: frame: no frame, the six-move slow rate at mod 125; object: its minimal polynomial over Q; reach: single; hypotheses: B2015's double-precision value at mod 125, a polynomial accepted at an absolute value below 1e-9 there
- identifications: none
- definitions: the six-move slow rate at mod 125 is the largest eigenvalue below 6 of W = L + R + L^-1 + R^-1 + X + X^-1 on the largest orbit over the common point mod 125, as B2015 defines it (its R1), with the value its run prints in double precision; P(x) = x^4 - 48 x^2 + 496
- imports: none
- premises on main: B2015 (its value at mod 125, from its run on main)
- decisive script: relays/claims/rate125/rate125.py, SHA-256 f921dd19d59d2422, depends on the standard library and sympy, run as python3 relays/claims/rate125/rate125.py, output SHA-256 1d495263277f6ce6
- decisive lines: 2 lines marked "DECISIVE:", SHA-256 2e787a2bf76379c1
- failing control: python3 relays/claims/rate125/rate125.py --control
- second computation: none
- already on main?: B2015 gives the value at mod 125; its minimal polynomial is not on main
- what would make it fail: P not vanishing at the value, or P reducible over Q
