# R53 — does the object select E6, or does the route only ever emit E6?

**Date:** 2026-09-02. **Seat cell** (fresh-eyes follow-up to B8118 / B206 / B210 / B282 / B1136).
**Script:** `r53.py` (SnapPy 3.3.2 + PARI via snappy; ~3 min). **Output:** `r53_output.txt`, `r53_results.json`.
**Status of every number below:** COMPUTED on this bench, this run.

## The question

The record attaches E6 to m004 by one route (B8118, structure-genesis head; B210 and B282 on main):

    shape/trace field disc  ->  conductor N = |disc|  ->  SL(2, Z/N)  ->  binary polyhedral?  ->  McKay label

and attaches E8 to the golden monodromy by the same route on the real side (B206: field Q(sqrt5), disc 5,
SL(2,F5) = 2I). B8118 showed E6 is a function of the field (14 census manifolds share it). The fresh-eyes
question is one step further back: **what is the image of this route at all?** If the route can only ever
emit E6 or E8, then "hits the exceptional McKay primes" is not a property of the object; it is the only thing
the instrument does when it emits anything.

## Q1 — the image of the route (conductors N = 1..24, exhaustive enumeration of SL(2,Z/N))

| N | |SL(2,Z/N)| | involutions | max element order | SU(2)-type | McKay |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | cyclic | A_0 (trivial) |
| 2 | 6 | 3 | 3 | none | NO LABEL |
| 3 | 24 | 1 | 6 | 2T | **E6** |
| 4 | 48 | 7 | 6 | none | NO LABEL |
| 5 | 120 | 1 | 10 | 2I | **E8** |
| 6–24 | — | ≥1 | — | none | NO LABEL |

Test used: a finite group embeds in SU(2) only if it has at most one involution, and the finite subgroups of
SU(2) are C_n, Dic_n (order 4n, which has an element of order 2n), 2T, 2O, 2I (element-order spectra
{1,2,3,4,6}, {1,2,3,4,6,8}, {1,2,3,4,5,6,10}). Every N in 6..24 fails: the odd primes 7, 11, 13, 17, 19, 23
have one involution but are perfect groups of the wrong order (B206 already noted p ≤ 5 for primes); every
composite N has ≥ 3 involutions or the wrong order spectrum (N = 9: one involution, order 648, no element of
order 324 — not dihedral, not exceptional).

**Consequence.** The route's image over all conductors is {A_0, E6, E8}. Conductors of imaginary quadratic
fields are 3, 4, 7, 8, 11, 15, 19, 20, 23, 24, ...; of these **only N = 3 emits**. A hyperbolic manifold's
shape field is never real, so on the geometry side the route has a one-element image: **E6 or nothing**.
E8 (N = 5) is reachable only through a real field, i.e. only on the monodromy side.

## Q2 — census base rate of the instrument (first 1200 orientable cusped manifolds)

| quantity | value |
|---|---|
| scanned | 1200 |
| all shapes in one quadratic field | 43 (Q(√−7): 20, Q(√−3): 14, Q(i): 9) |
| route emits a label | **14 (all E6)**; 1186 NO LABEL |
| E6 carriers | m003 m004 m202 m203 m206 m207 m208 m410 m412 s118 s119 s594 s595 s596 (= B8118's 14, set-identical) |
| shape degree over Q, first 300 (max over tetrahedra, PARI lindep at 64 digits) | 2: 18, 3: 32, 4: 40, 5: 34, 6: 32, 7: 32, 8: 20, 9: 20, 10: 23, 11: 16, 12: 17, unresolved (>12): 16 |

The 29 quadratic-field manifolds over Q(√−7) and Q(i) get nothing from the route (N = 7 and N = 4 both fail
Q1). So "carries E6" is coextensive with "shape field Q(√−3)" on the census, and with nothing narrower.

## Q3 — the sister bit (m004 = b++RL vs m003 = b+−RL)

| | m004 | m003 |
|---|---|---|
| bundle word (isometric, checked) | b++RL | b+−RL |
| monodromy in SL(2,Z) | A = [[2,1],[1,1]] (trace 3) | −A (trace −3) |
| H1 | Z | Z ⊕ Z/5 |
| det(A − I) / det(−A − I) | −1 → torsion 1 | 5 → torsion Z/5 |
| volume | 2.029883213 | 2.029883213 |
| shape field | Q(√−3) | Q(√−3) |
| symmetry group order / amphichiral | 8 / yes | 8 / yes |
| route label | E6 | E6 |

Identity: for A = [[2,1],[1,1]] = the φ² matrix, det(A − I) = (φ − φ⁻¹)² = 1 and det(A + I) = (φ + φ⁻¹)² = 5.
The sister's Z/5 is (√5)² = disc Q(√5): the same m² + 4 of B208, not an extra input.

Spin structures on the fibre T²: A mod 2 = [[0,1],[1,1]] has order 3, fixes exactly the Arf-1 quadratic
form and cycles the three Arf-0 forms. Since −A ≡ A mod 2, **the spin-structure action is identical for the
two sisters.** The bit that distinguishes m004 from m003 is invisible to the field, the volume, the
tetrahedra, amphichirality, the route label, and the spin action; it is seen by H1 and by the sign of the
SL(2,Z) lift only. (B1136 found H1 = Z to be the sole separator inside the 14-family; this says why: the
separator is det(A − I) = 1, a Fibonacci identity of the trace-3 monodromy.)

## Q4 — the 14 carriers are one commensurability class

covol PSL(2, O_{−3}) = 3^{3/2} ζ_K(2)/(4π²) with ζ_K(2) = ζ(2)·L(2, χ_{−3}) → 0.169156934402 = V_tet/6 exactly.

| index in PSL(2,O_{−3}) | carriers |
|---|---|
| 12 | m003, m004 |
| 24 | m202, m203, m206, m207, m208, s118, s119 |
| 30 | m410, m412, s594, s595, s596 |

All volume ratios are integers to 1e−6 (Humbert, as B147 used for bundles). The route lands on the Bianchi
group PSL(2, O_{−3}); m004 is one index-12 torsion-free subgroup of it, and the record prices that choice
nowhere except by the trace-3 / torsion-free sieve (B197, B1136), which is the Fibonacci identity above.

## What the record already had (swept before writing; owner rule 1)

- **B206** (main): "SL(2,F_p) is binary-polyhedral only for p ≤ 5"; the Q(√5) family is the odd-index Lucas
  family m ∈ {1, 4, 11, 29, 76, …} (R53 confirms m ≤ 200: 1, 4, 11, 29, 76, 199); the 2I shadow appears for
  every m ≡ ±1 mod 5; honest statement "golden is the minimal member".
- **B208** (main): det(γ + I) = m² + 4; "golden is the unique point where det(γ+I) is the McKay-E8 prime".
- **B210** (main): dual McKay, E6 at 3 and E8 at 5, E7 excluded; "golden is the unique metallic mean whose
  both arithmetics hit exceptional McKay primes".
- **B282** (main): the 2T surjection is present only for the arithmetic pair m004 / m003; E6 is arithmetic,
  not geometric.
- **B1136** (main) and **B8118** (structure-genesis): the 14-family; sole separator H1 = Z.
- **B197** (main): the m003 volume tie is broken by torsion-freeness.
- **B147** (main): Humbert volume/Bianchi-covolume integers for bundles. **B804**: Arf bordism on the cusp.

## What R53 adds

1. **The instrument has a two-element image** ({E6, E8}, plus the trivial A_0), and a one-element image on
   hyperbolic manifolds. B206 states p ≤ 5 for primes; the composite conductors 4, 8, 9, 12, 15, 16, 20, 24
   and the cyclic/dihedral branches had not been closed. They are closed here.
2. **The two sides use different conventions.** B208's uniqueness reduces by the integer det(γ+I) = m²+4
   (5 only at m = 1); B206 and B8118 reduce by the field discriminant (5 for the whole Lucas family). Under
   the field convention golden is not unique on the E8 side (B206 concedes this); under the integer
   convention the hyperbolic side has no analogue. B210's "unique metallic mean carrying both" therefore
   rests entirely on the E6 side, where it is true for the trivial reason that m = 1 is the only metallic
   bundle with shape field Q(√−3) (m = 2 gives Q(i), N = 4, no label; m ≥ 3 give degree ≥ 4, route not
   applicable).
3. **Census base rate:** 14 of 1200 (1.2 %) labelled, all E6, all one commensurability class, indices
   12 / 24 / 30 in the Bianchi group.
4. **The sister bit is spin-blind** (new): the Arf/spin machinery of B804 cannot see it either.

## Bearing on "the object selects E6"

The object does not select E6. The field Q(√−3) selects it, and the instrument could not have emitted
anything else on any hyperbolic manifold. The information content of "m004 carries E6" is exactly "m004's
shape field is Q(√−3)", which is exactly "m004 is a torsion-free finite-index subgroup of PSL(2, O_{−3})",
of which the census shows fourteen in the first 1200 alone. What is m004-specific reduces to two Fibonacci
identities of the trace-3 monodromy (det(A ∓ I) = (φ ∓ φ⁻¹)² = 1, 5) and the regular ideal tetrahedron's
field. No step of this joint uses the founding axiom, and no step produces a number a laboratory could test.

**Verdict:** B8118's own conclusion (E6 is a function of the field) STANDS and is sharpened: E6 is a function
of the instrument, which has nothing else to say. B210's "unique metallic mean" language and B208's
"unique point" language are convention-dependent and should be restated as B206 already restated them.
