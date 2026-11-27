# CLAIM CARD — frame C, read with its canonical end, is covariant under T, S and the act M acting on the modulus and the point together, the point carried as (a, b)g^-1, so the act's change of rate class is a change of cusp

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-845, P-860 (d)
- effect: conditions — P-845's orbit reading (B1978's dated caveat): a point's rates read at the cusp g(inf) are the
  rates of the point carried by g read at inf, so B1978's change of rate class under the act is a change of cusp
- scope: frame: frame C (B1945's parts and U_of, reading S); object: the invariants of frame C (sorted singular-value
  ratios per sector, the moduli of the mixing) at (tau, v, L) and at (g tau, v g^-1, L + log|c tau + d|); reach: single;
  hypotheses: three moduli, twenty points and three group elements, mpmath at 50 digits, the canonical end supplied
  by its covariance law (B1927) since B1927's table covers the fundamental domain only
- identifications: none
- definitions: T = [[1, 1], [0, 1]], S = [[0, -1], [1, 0]], the act M = [[2, 1], [1, 1]], acting on tau by Mobius
  transformation; a point v = (a, b) with first coordinate a multiplying tau, carried by (a, b) g^-1 (row convention,
  B1733); the end L(g tau) = L(tau) + log|c tau + d| (B1927); the invariants are s1/s3 and s2/s3 per sector (up, down,
  lepton) and |V_ij| for V = U_up^H U_down; moduli 0.13 + 1.2i, 0.31 + 1.5i, -0.2 + 2.0i; points: the act's orbit of
  (4/15, 1/30) at order 30, the four order-5 points on the act's line, four order-6 points
- imports: none
- premises on main: B1945 (parts, U_of), B1927 (the end's covariance law), B1733 (the row convention), B1978
- decisive script: relays/claims/sm_refile/c23_decisive.py, SHA-256 ea14f6642ea196e5, depends on the standard library
  and
  mpmath, run as python3 relays/claims/sm_refile/c23_decisive.py, output SHA-256 7ebba5dc7622171a
- decisive lines: 5 lines marked "DECISIVE:", SHA-256 28553234bb2ef430
- failing control: python3 relays/claims/sm_refile/c23_control.py
- second computation: none
- already on main?: grep -il "joint covarian" frontier/*/FINDINGS.md: B1978 and B1979, both name it as owed; closest arc
  B1978
- what would make it fail: under (a, b)g^-1 the invariants at the image differing from those at the source by more than
  1e-15 for S or the act at any of the three moduli, or the plants (point unmoved; end unshifted) not failing
