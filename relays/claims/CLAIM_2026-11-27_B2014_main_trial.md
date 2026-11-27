# CLAIM CARD — B2014: the six moves are two walks, W+ = L + X + R^-1 and W- = R + L^-1 + X^-1, which commute exactly; mod 27 has three 72-point sister orbits, and on (3,3,15), with no fixed point of C, the halving holds with nothing left out; fixed points are unchanged up the tower on every element tried

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, 13977a25feb6d94d74c9ea9b72c6a9492b85eec1
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 28
- effect: adds — LISTENING 28
- scope: frame: no frame, the moves on the orbit of (3,3,3) mod 27, 81 and 243, a leaf mod 7 and the congruence surface mod 27; object: the six moves as two walks, their sector law, the sisters, fixed points up to mod 6561; reach: class; hypotheses: S1 exact, S2 in double precision, S5 on the elements tried
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, xy - z), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (L = sigma C^2 and R = sigma C as maps, B2004); the orbit of a point is its orbit under L, R and their inverses; the leaf k mod N is the set of readings with x^2 + y^2 + z^2 - xyz = k mod N, the cusp's leaf being k = 0; the six moves are L, R, L^-1, R^-1, X and X^-1 (B2011's sectors_exact.py writes them as L, R and their conjugates by C and C^-1), and the six-move sum W sends e_v to the sum of e_m(v) over them; the neutral sector is W on the C-invariant functions, its characteristic polynomial p_neutral of degree d; the charged sector q = 1 is W on the span of b_o = sum_j w^-j e_(C^j v) over the size-3 C-orbits o (w a primitive cube root of 1), its characteristic polynomial S(x); the paired degree is the degree of gcd(p_neutral(2x)/2^d, S(x)), and the rest of S's roots are unpaired; the halving in the whole's form is p_neutral(2x)/2^d = (x - 3)(x + 3) x S(x) (B2002); W+ = L + X + R^-1 and W- = R + L^-1 + X^-1 as push-forward matrices (e_v to e_g(v)); Pi_q = (1/3) sum_j w^-qj C^j, and sigma's compression in sector q is Pi_q sigma Pi_q; the congruence surface mod 27 is the cusp's leaf mod 27, and the sisters are its three 72-point orbits; a fixed point of an element g is a reading v of the orbit with g(v) = v (B2014's walks.py)
- imports: none
- premises on main: B2004 (the six moves as words in C and sigma); B2011 (sectors_exact.py)
- decisive script: relays/claims/main_trial/decisive.py, SHA-256 0f8f89e012cf7dfb, depends on the standard library, numpy, scipy, sympy and python-flint, run as python3 relays/claims/main_trial/decisive.py B2014, output SHA-256 216327de676709aa
- decisive lines: 21 lines marked "DECISIVE:", SHA-256 6f4a167bfd306138
- failing control: python3 relays/claims/main_trial/B2014_control.py
- second computation: none
- already on main?: the arc itself, B2014, landed at 18c1b8ac2; this card is filed after the arc's run (post hoc to it)
- what would make it fail: a non-zero entry of [W+, W-] or of C W+ C^-1 - W+ on an orbit run, or a sector-law residual above 1e-10 where the law says zero, or a fixed-point count that changes up the tower
