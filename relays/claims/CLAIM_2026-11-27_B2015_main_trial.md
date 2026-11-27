# CLAIM CARD — B2015: on the largest orbit over the common point the six-move sum's largest eigenvalue below 6 is exactly 2 sqrt(5 + 4 cos(pi/M)) at mod 27, 81, 125, 343 (its minimal polynomial divides the characteristic polynomial over Z) and 625 (modulo three primes), with the same M as the four-move formula, in the levels run

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, ff85df4c78d7f9b28d512a501fa9cf21eafbb8c1
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 29
- effect: supports — LISTENING 29
- scope: frame: no frame, the six-move sum on the largest orbit over the common point mod 27, 81, 125, 343 and 625; object: whether 2 sqrt(5 + 4 cos(pi/M)) is an eigenvalue, with its multiplicity; reach: class; hypotheses: over Z to 1176 points and modulo three 62-bit primes at 3000 points, M read off the levels run
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, xy - z), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (L = sigma C^2 and R = sigma C as maps, B2004); the orbit of a point is its orbit under L, R and their inverses; the leaf k mod N is the set of readings with x^2 + y^2 + z^2 - xyz = k mod N, the cusp's leaf being k = 0; the points over the common point mod p^k are the readings with every coordinate 0 mod p on the cusp's leaf mod p^k, and the largest orbit over it is the largest of their orbits under L and R (B1996's orbits_over_common_point); W = L + R + L^-1 + R^-1 + X + X^-1 on it as push-forward matrices, a symmetric matrix; M is the number the arc reads off each level run, as its table gives it; the value's minimal polynomial is the factor of Res_t(m_c(t), x^2 - 20 - 16 t) that vanishes at it, m_c being the minimal polynomial of cos(pi/M) (B2015's rate_law.py)
- imports: none
- premises on main: B1996 (orbits_over_common_point); B2011 (the four-move formula's M)
- decisive script: relays/claims/main_trial/decisive.py, SHA-256 d0b72df109d77a25, depends on the standard library, numpy, scipy, sympy, mpmath and python-flint, run as python3 relays/claims/main_trial/decisive.py B2015, output SHA-256 a5b859285189cb3b
- decisive lines: 5 lines marked "DECISIVE:", SHA-256 9a1af267fde99085
- failing control: python3 relays/claims/main_trial/B2015_control.py
- second computation: none
- already on main?: the arc itself, B2015, landed at 6f80ac0e5; this card is filed after the arc's run (post hoc to it)
- what would make it fail: the value's minimal polynomial not dividing charpoly(W) at one of the five levels
