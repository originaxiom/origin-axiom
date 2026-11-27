# CLAIM CARD — B2016: the whole's small group with the same six moves, on the cosets of every class of its subgroups (45 at mod 27, 100 at mod 81), halves in the whole's form on 4 and 8 of them, the whole's own orbit among them; so the halving is a property of the whole's orbit within its group, not of the group's action

- card id: new
- seat code: fam1-v1-unset-01
- seat, branch, commit: fam1-v1-unset-01, main, ff85df4c78d7f9b28d512a501fa9cf21eafbb8c1
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 30
- effect: adds — LISTENING 30
- scope: frame: no frame, G3 (mod 27, order 216) and G4 (mod 81, order 1944) acting on the cosets of every class of subgroups; object: on how many coset spaces the halving holds in the whole's form; reach: class; hypotheses: exact, by GAP's subgroup classes and coset actions and by FLINT
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N, L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x), C(x, y, z) = (y, z, x), sigma(x, y, z) = (y, x, xy - z), X(x, y, z) = (y, yz - x, z), and L^-1, R^-1, X^-1 their inverses (L = sigma C^2 and R = sigma C as maps, B2004); the orbit of a point is its orbit under L, R and their inverses; the leaf k mod N is the set of readings with x^2 + y^2 + z^2 - xyz = k mod N, the cusp's leaf being k = 0; G_k is the group that C and sigma generate acting on the orbit of (3,3,3) mod 3^k (G3 at mod 27, G4 at mod 81); for a subgroup H, C and sigma act on the right cosets G_k/H, and the moves, W, the sectors, p_neutral and S are taken there as on an orbit (the moves as words in C and sigma); category (a) is p_neutral(2x)/2^d = (x^2 - 9) x S(x), the whole's form; (a') is p_neutral(2x)/2^d = S(x); (b) is S dividing p_neutral(2x)/2^d otherwise; (c) is neither (B2016's cosets_gap.py); the whole's stabiliser is the stabiliser of (3,3,3) in G_k; rho is trivial on H when rho(C) = w and rho(sigma) = -1 give 1 on every element of H (B2016's cosets_export.py)
- imports: GAP's ConjugacyClassesSubgroups and coset actions, through sage
- premises on main: B2005 (G_k and its stabiliser); B2002 (the whole's form)
- decisive script: relays/claims/main_trial/decisive_b2016.py, SHA-256 fd066fe78ba4d9c4, depends on the standard library, sage, GAP, python-flint and sympy, run as python3 relays/claims/main_trial/decisive_b2016.py, output SHA-256 c8b56c5bebf5fad1, heavy
- decisive lines: 8 lines marked "DECISIVE:", SHA-256 1a7019700739d47f
- failing control: python3 relays/claims/main_trial/B2016_control.py
- second computation: none
- already on main?: the arc itself, B2016, landed at b11a892ca; this card is filed after the arc's run (post hoc to it)
- what would make it fail: a rerun of the subgroup classes giving other than 4 of 45 and 8 of 100 in the whole's form, or the whole's stabiliser class outside it
