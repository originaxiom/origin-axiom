# R56 — the object beyond its field: the full check (owner: "run a full check all you can")

**Date:** 2026-09-02. Script `r56.py`, output `r56_output.txt`, `r56_results.json`. SnapPy 3.3.2 + sympy. Every number
COMPUTED here; no banked verdict used.

## A. What varies across the 14 manifolds that share ℚ(√−3) (hence E6, hence everything the chain built)

| invariant | distinct values among the 14 | singles out m004? |
|---|---|---|
| volume | 3 (2V, 4V, 5V with V = V_tet) | no |
| H1 | 9 | **yes** (ℤ; every other member has torsion or rank 2) |
| cusp shape τ | 6 | **yes** (2√3 i; the others: (1+√−3)/2, √−3, (−1+2√−3·… )…) |
| cusp area (maximal) | 7 | no (m412 also 2√3) |
| symmetry group order | 5 (2, 4, 8, 12, 16) | no |
| amphichiral | 2 (6 yes, 8 no) | no |
| systole | 6 | no (m206, m207 share 1.0871) |
| short length spectrum (< 1.6) | 12 | no |
| Chern–Simons | 6 | no (m203, m206, m208, s595, s596 also 0) |
| **number of covers of degree 2…6** | **14** | **yes** ([1,1,2,4,11]; m003: [1,1,2,8,7]) |

Three invariants single out m004 inside its field class: H1 = ℤ (the det(A − I) = 1 identity of R53), the cusp shape
2√3 i, and the subgroup growth (covers by degree), which separates all 14 pairwise. Eight of the 14 are chiral
(R51 already found 74 of 112 in the wider family), so "the E6 family" is not an amphichiral family.

## B. m004 vs m003 under the closings (1, q)

| slope | m004: vol, CS, H1 | m003: vol, CS, H1 |
|---|---|---|
| (1,1) | flat (non-hyperbolic), H1 = 0 | non-hyperbolic, H1 = ℤ/15 |
| (1,2) | 1.39851, −0.24661, 0 | degenerate, H1 = ℤ/20 |
| (1,3) | 1.73198, −0.16542, 0 | 1.26371, +0.11414, ℤ/5 ⊕ ℤ/5 |
| (1,4) | 1.85814, −0.12443, 0 | 1.58865, +0.14214, ℤ/30 |
| (1,5) | 1.91860, −0.09969, 0 | 1.74012, +0.16090, ℤ/35 |
| (1,6) | 1.95206, −0.08315, 0 | 1.82434, +0.17419, ℤ/40 |

Every closing of the sister differs from the object's in volume, in the sign and size of CS, and in homology
(m004's (1,q) fillings are homology spheres; m003's carry ℤ/(5q+5)-type torsion). The closings are object-level.

## C. The triangulation data that define the object-level 3d theory

Both have two regular ideal tetrahedra; the gluing matrices differ:

    m004 edges/cusp (z1 z1' z1'' | z2 z2' z2''):  [2 1 0 | 1 0 2], [0 1 2 | 1 2 0], meridian [1 0 0 | 0 −1 0], longitude [0 0 0 | 0 −2 2]
    m003:                                          [2 0 1 | 2 0 1], [0 2 1 | 0 2 1], meridian [0 −2 0 | 2 0 0], longitude [0 −1 0 | 2 −1 0]

Eliminating the shapes (Gröbner, lex) gives the deformation curve in SnapPy's (meridian, longitude) eigenvalue
convention, verified to vanish (to 1e−15) at the (1,5) filling's holonomies:

    m004:  −l²m⁴ + l(m⁸ − 2m⁷ − 3m⁶ + 2m⁵ + 6m⁴ + 2m³ − 3m² − 2m + 1) − m⁴
    m003:  −l⁴m + 2l³m² + 2l³m + l²m⁴ − 5l²m³ + 2l²m² − 5l²m + l² + 2lm³ + 2lm² − m³

(m004's is the figure-eight A-polynomial in SnapPy's peripheral basis; the convention check shows the cusp-row product
equals exp(H), not exp(2H).) These two curves are the moduli spaces of the two DGG theories T[m004], T[m003]: each is
a 3d N = 2 theory with gauge U(1), two chirals, one internal-edge superpotential, defined by the gluing matrix above.
They differ. This is the first invariant after the shape field that belongs to the object and not to the field.

## D. What the full check says

1. The object has abundant content of its own: H1, cusp shape, subgroup growth, closings, deformation curve, T[M].
   None of it was used by the chain after step 3 (MISSTEP note). All of it varies across the E6 family.
2. The object-level theory at the fork is a 3d supersymmetric theory, not a 4d gauge theory. Nothing computed here
   moves it toward the Standard Model, and the seat does not claim it does.
3. The sister comparison is decisive for the record's language: "the object's E6", "the object's 27", "the object's
   gauge algebra" are all shared with m003, whose every object-level number above differs from m004's.

## E. What a physical restart would need, from this cell forward

A map from T[M] (or from the deformation curve, the covers, the closings) to a 4d statement with a scale. No such map
exists in the record, and the seat knows of none in the literature that reaches the Standard Model. The honest name
for the program after this check is: a study of the golden mapping torus and its arithmetic, with one falsifiable
sign structure (R55) and no dimensionful prediction.
