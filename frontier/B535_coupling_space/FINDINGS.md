# B535 — The Coupling Space: Findings

*The reframed program's stage 1 (owner directive 2026-07-12): the
structure/value split is not the end of the ToE question — explore the
coupling space entirely, quantify the one-measurement claim, catalog the
forced relations. Prereg committed before compute.*

## C1 — The census SATURATES: 6 Perron types, 7 canonical systems

All factor windows |u| = 1..8 (116 observation points, host depth 11):

| length | analyzed | cum. Perron types | cum. canonical systems |
|---|---|---|---|
| 1 | 4 | 3 | 4 |
| 2 | 7 | 4 | 5 |
| 3 | 10 | 5 | 6 |
| 4 | 13 | 5 | 6 |
| 5 | 17 | **6** | **7** |
| 6–8 | 69 | 6 | 7 |

**The coupling space is FINITE and now fully mapped**: 6 Perron types,
7 canonical induced systems, saturated at window length 5, with lengths
6–8 producing nothing new (Durand's theorem guarantees finiteness of
derived systems for primitive substitutive sequences; the census finds
the exact count). The canonical-system count 7 matches B530's independent
induction census exactly.

**Correction to B533's scope** (prereg falsifier honestly triggered): the
"exactly 5 types" of B533 Gate 1 was the length-≤4 statement. The SIXTH
type first appears at u = 'bABab': rc = 5, and it is the census's first
**q = 2 window** — its induced matrix has Perron eigenvalue β², the
M²⊕0 case of the banked B530 induction law. Its exact components are
{1/(1+τ), 2−2τ+3φ−2τ³, −2+τ−2φ+2τ³, 1+2φ−2τ³, τ−2φ+τ³}: the top
component is |λ₂| (shared with Type 2), three are shared with Type 4,
and one is new (τ−2φ+τ³ = 0.0941…). All in ℚ(τ), all half-integer-free
(Type 6 is integral; Type 5 remains the only half-integral type).

## C2 — The one-measurement test: measurement + grammar ⟹ σ, uniquely

**Matrix level (theorem, from the B533 audit):** measuring β fixes the
abelianization uniquely up to GL(4,ℤ) — ℤ[β] is the maximal order of
ℚ(√φ), class number 1, Latimer–MacDuffee.

**Word level (computed here):** the measured incidence matrix lifts to
60·6·24·2 = **17,280** substitutions (all words with σ's image Parikh
vectors). Over ALL of them:

| filter | survivors |
|---|---|
| the measurement alone (shared abelianization) | 17,280 lifts, **16,848 distinct languages** |
| + the object's bigram grammar (7 adjacencies) | **8** |
| + the full language (length-6 factor sets) | **2** |

The two survivors are σ itself and a→bAABa, b→ABa, A→bABa, B→Aa —
**proved to be exactly the conjugate a⁻¹σ(·)a** (every σ-image starts
with 'a'; rotating each image by one letter is the conjugation; verified
symbolically, not numerically). The 8 grammar-survivors are precisely
image-rotation combinations; only the two globally-consistent rotations
preserve the language.

**Verdict:** one measured number + the object's own grammar determines
the object **uniquely up to presentation** (conjugation — a gauge choice,
not a physical one). The information accounting: the matrix alone leaves
~14 bits of word-level freedom (16,848 languages); the grammar supplies
~11 of them; the language the rest, down to the conjugacy class.

## C3 — The read-out dictionary: one number in, all numbers out

Exact Perron eigenvectors for all 6 types (adjugate over ℚ(τ), handling
both clock rates q=1 and q=2). The 6 types share exactly **17 distinct
components**, and:

**Every one of the 17 is degree 4 over ℚ — a COMPLETE measurement.**
Zero degenerate read-outs (stronger than the prereg predicted). For each
component x there is an explicit cubic g ∈ ℚ[x] with τ = g(x), verified
exactly; e.g.

    x = f_a:                τ = 1 + x                        (Type 1/2/5)
    x = f_A:                τ = 1 + x/2 + x² − x³/2          (Type 1)
    x = |λ₂| = f_a+f_b:     τ = 3 − 5x + 2x² + x³            (Type 2/6)
    x = 0.0941… (Type 6):   τ = (28 − 71x + 34x² + 7x³)/17

Full 17-row dictionary in `c3_relations_catalog.py` output. Consequence:
**measure ANY single Perron read-out of ANY coupling type, and every other
read-out of every coupling type is an exactly computable number.** This is
the falsifiable prediction form the reframe promised: relations between
observations, forced; no values assumed.

## What this sets up (NOT done here — needs its own prereg + controls)

The SM comparison as RELATIONS: does any coupling type's read-out
dictionary match the relation structure among SM dimensionless
observables? That campaign must pre-register the relation-matching
criterion and its null model before touching SM numbers. The
value-matching door stays closed (B533 Gate 3).

Locks: `tests/test_b535.py`. Nothing here is physics; the dictionary is
exact algebra in ℚ(√φ).
