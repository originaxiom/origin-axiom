# CLAIM CARD — every orbit of L, R and their inverses on (Z/N)^3 meets the plane x = y, at N = 5, 7, 11, 13 and 25, so the census of orbits can be taken on the plane

- card id: new
- seat code: fam2-v1-unset-01
- seat, branch, commit: fam2-v1-unset-01, audit/physical-bridge-2026-09-05, c096ed90420984fe28c2e506c34c3afcf4bb8c17
- kind: computation
- touches: P-882 (the listening line); the law map's row LISTENING 31
- effect: adds — LISTENING 31, a census on N^2 points instead of N^3
- scope: frame: no frame, the action of L, R and their inverses on (Z/N)^3; object: whether every orbit holds a point of the plane x = y; reach: class; hypotheses: N = 5, 7, 11, 13 and 25, exact integer arithmetic
- identifications: none
- definitions: the readings are triples (x, y, z) of residues mod N; L(x, y, z) = (x, z, xz - y) and R(x, y, z) = (z, y, yz - x), with their inverses (B2004; the four moves of B2017's census); the orbit of a reading is its orbit under these four moves; the plane is the set of readings (x, x, z); an orbit meets the plane when it holds a reading of the plane
- imports: none
- premises on main: B2004 (the moves); B2017 (the census of orbits)
- decisive script: relays/claims/plane_census/plane_census.py, SHA-256 4f29a2dc7731b1b9, depends on the standard library, run as python3 relays/claims/plane_census/plane_census.py, output SHA-256 493673ca6849daf2
- decisive lines: 6 lines marked "DECISIVE:", SHA-256 493673ca6849daf2
- failing control: python3 relays/claims/plane_census/plane_census.py --control
- second computation: none
- already on main?: B2017's census counts the orbits at the levels it ran; the reduction to the plane is not on main
- what would make it fail: an orbit at one of the five levels with no reading on the plane x = y
