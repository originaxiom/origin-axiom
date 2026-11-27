# CLAIM CARD — B2012 N1: the four-move sum is 3(SP + PS) - 2S on every orbit, so its spectrum pairs lambda with lambda + 2 by the two-subspace theorem (exact on five orbits, modulo three primes at mod 135): a law of the modular group, not of the whole

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, 13977a25feb6d94d74c9ea9b72c6a9492b85eec1
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 27
- effect: adds — P-882 and LISTENING 27 (a pairing law of the four-move sum)
- scope: frame: no frame, the moves L and R on the readings, on six orbits (leaves mod 7, 11 and 13, and the orbit of (3,3,3) mod 27, 81 and 135); object: the four-move sum's characteristic polynomial; reach: class; hypotheses: exact over Z on five orbits and modulo three 62-bit primes at mod 135, the two-subspace reading cited and its plane computation checked by sympy
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, xy - z), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (L = sigma C^2 and R = sigma C as maps, B2004); the orbit of a point is its orbit under L, R and their inverses; the leaf k mod N is the set of readings with x^2 + y^2 + z^2 - xyz = k mod N, the cusp's leaf being k = 0; on an orbit of n points, T4 = L + R + L^-1 + R^-1 as push-forward matrices (e_v to e_g(v)), S the push-forward of sigma and P = (1 + C + C^2)/3; A = 3 P(1 + S)P on the basis of C-orbit sums (an integer matrix), d1 the multiplicity of 6 and d2 that of 0 in A, R(x) the characteristic polynomial of A without them, f_S the number of fixed points of sigma, d3 = (n + f_S)/2 - d1 - deg R and d4 = (n - f_S)/2 - d2 - deg R (B2012's blind_checks.py); the pairing of lambda with lambda + 2 is the factor R(x + 4) R(x + 2)
- imports: the two-subspace theorem for two projections, as cited in the arc
- premises on main: B2004 (the moves act through <C> * <sigma>, sigma the script's S)
- decisive script: relays/claims/main_trial/decisive.py, SHA-256 0f8f89e012cf7dfb, depends on the standard library, numpy, sympy and python-flint, run as python3 relays/claims/main_trial/decisive.py B2012, output SHA-256 fe3e62972e48200b
- decisive lines: 6 lines marked "DECISIVE:", SHA-256 d4d4ef2f16ce5210
- failing control: python3 relays/claims/main_trial/B2012_control.py
- second computation: none
- already on main?: the arc itself, B2012, landed at 18d0ed471; this card is filed after the arc's run (post hoc to it)
- what would make it fail: on any of the six orbits a characteristic polynomial other than R(x+4) R(x+2) (x-4)^d1 (x+4)^d2 (x+2)^d3 (x-2)^d4
