# CLAIM CARD — on every p-tower the six-move slow rate depends on the prime only: from p^3 on it is 2 sqrt(5 + 4 cos(pi/p)), checked at mod 27, 125 and 343

- card id: new
- seat code: fam3-v1-high-01
- seat, branch, commit: fam3-v1-high-01, agy/cusp-action-2026-11-20, a3a372470d3ee9fc1e3acca2ec1bb91c322e3d42
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 29
- effect: adds — LISTENING 29, the rate as a law in the prime
- scope: frame: no frame, the six-move sum on the largest orbit over the common point mod p^k; object: the largest eigenvalue below 6 against 2 sqrt(5 + 4 cos(pi/p)); reach: general; hypotheses: every p-tower from p^3 on, checked at mod 27, 125 and 343 with B2015's own code for W, in double precision, agreement within 1e-9
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (B2004); the orbit of a point is its orbit under L, R and their inverses; the points over the common point mod p^k are the readings with every coordinate 0 mod p on the cusp's leaf x^2 + y^2 + z^2 - xyz = 0 mod p^k, and the largest orbit over it is the largest of their orbits (B1996's orbits_over_common_point); W = L + R + L^-1 + R^-1 + X + X^-1 on it as push-forward matrices (B2015's six); the slow rate is W's largest eigenvalue below 6
- imports: none
- premises on main: B1996 (orbits_over_common_point, tower_decay.py) and B2015 (rate_law.py, its W), both copied beside the script under their own paths
- decisive script: relays/claims/rate_prime/rate_prime.py, SHA-256 7ea928fc6b7d7125, depends on the standard library, numpy, scipy, sympy, mpmath and python-flint, run as python3 relays/claims/rate_prime/rate_prime.py, output SHA-256 c227b1ad972f9688
- decisive lines: 4 lines marked "DECISIVE:", SHA-256 50c295ffc1fa1f9c
- failing control: python3 relays/claims/rate_prime/rate_prime.py --control
- second computation: none
- already on main?: B2015 states the rate's value at each level it ran; the law in the prime alone is not on main
- what would make it fail: a level p^k with k at least 3 where W's largest eigenvalue below 6 differs from 2 sqrt(5 + 4 cos(pi/p)) by more than 1e-9
