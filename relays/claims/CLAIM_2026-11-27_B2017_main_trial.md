# CLAIM CARD — B2017: over every orbit of the moves on every leaf at mod 27, 25, 49 and the primes 5 to 13 (417 orbits; 21 at mod 49 above 2400 points left out), the six-move sum's halving holds on exactly three, the 72-point sisters on the cusp's leaf mod 27; with B2016 the halving is the whole's, at its own leaf and its own prime

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, ff85df4c78d7f9b28d512a501fa9cf21eafbb8c1
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 31
- effect: adds — LISTENING 31
- scope: frame: no frame, every orbit of L, R and their inverses on every leaf at mod 27, 25, 5, 7, 11, 13 and 49; object: where the six-move sum's halving holds; reach: class; hypotheses: exact to 1200 points, double precision from 1201 to 2400, 21 orbits above 2400 points left out, and higher levels not censused
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, xy - z), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (L = sigma C^2 and R = sigma C as maps, B2004); the orbit of a point is its orbit under L, R and their inverses; the leaf k mod N is the set of readings with x^2 + y^2 + z^2 - xyz = k mod N, the cusp's leaf being k = 0; the six moves are L, R, L^-1, R^-1, X and X^-1 (B2011's sectors_exact.py writes them as L, R and their conjugates by C and C^-1), and the six-move sum W sends e_v to the sum of e_m(v) over them; the neutral sector is W on the C-invariant functions, its characteristic polynomial p_neutral of degree d; the charged sector q = 1 is W on the span of b_o = sum_j w^-j e_(C^j v) over the size-3 C-orbits o (w a primitive cube root of 1), its characteristic polynomial S(x); the paired degree is the degree of gcd(p_neutral(2x)/2^d, S(x)), and the rest of S's roots are unpaired; the halving in the whole's form is p_neutral(2x)/2^d = (x - 3)(x + 3) x S(x) (B2002); category (a) is p_neutral(2x)/2^d = (x^2 - 9) x S(x), the whole's form; (a') is p_neutral(2x)/2^d = S(x); (b) is S dividing p_neutral(2x)/2^d otherwise; (c) is neither (B2016's cosets_gap.py); the three sisters are the three 72-point orbits on the cusp's leaf mod 27 (B2014)
- imports: none
- premises on main: B2011 (sectors_exact.py, imported); B2016 and B2014 (the categories)
- decisive script: relays/claims/main_trial/decisive.py, SHA-256 d0b72df109d77a25, depends on the standard library, numpy, python-flint and sympy, run as python3 relays/claims/main_trial/decisive.py B2017, output SHA-256 777e696ced8354e7
- decisive lines: 22 lines marked "DECISIVE:", SHA-256 2c0c673075f3382e
- failing control: python3 relays/claims/main_trial/B2017_control.py
- second computation: none
- already on main?: the arc itself, B2017, landed at 38dfb2f78; this card is filed after the arc's run (post hoc to it)
- what would make it fail: an orbit other than the three sisters in category (a), (a') or (b), or a sister leaving it
