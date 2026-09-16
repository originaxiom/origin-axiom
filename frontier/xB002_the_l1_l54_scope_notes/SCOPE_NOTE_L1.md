# Scope note — L1: the object's own selection

**Status: the scope-correction note X15 ranks (1) and records as owed ("still unwritten as of
B1101"). Written here by the xb seat on `sep16-branch`, 2026-09-16. This is a SCOPE NOTE, not a
reopening: no result below is withdrawn, and the corrected statement is stronger than the one it
replaces on its own ground.**

## What was banked

> "m004 is **the** selected object."

## What was proved

Three criteria were run. Taken together they do not reach that sentence:

1. **Extremality along the metallic diagonal** (m = 1..7). Proved. It selects the golden row, i.e.
   the *word* and hence the monodromy `LR` — not a manifold among manifolds.
2. **Volume minimality.** m004 does **not** win it. `vol(m003) = vol(m004) = 2.0298832128193…`
   exactly; the two are the minimal-volume one-cusped orientable cusped hyperbolic 3-manifolds.
   The criterion **ties**.
3. **Arithmeticity / the invariant trace field.** The invariant trace field is a
   **commensurability-class invariant**. It is constant on the class by theorem, so it
   **cannot discriminate between members at all** — not weakly, not in principle.

So of the three, one selects a *row*, one *ties*, and one is *constitutionally unable to
discriminate*. None selects the manifold.

## What does select it, exactly

B1136 ran the genericity control on the object's own wins and found the answer:
**exactly one elementary property separates m004 from its shape-field family — `H₁ = ℤ`.**

Re-derived independently here (`verification/shape_field_family.py`; own quadratic shape-field
test, own property table, no read of B1136's json), on the **corrected** family (see below):

| property | m004 | shared with | separates? |
|---|---|---|---|
| **H₁ = ℤ** | ℤ | **0 others** | **YES — the only one** |
| volume 2.0298832128 | ✓ | 1 (m003) | no |
| tetrahedron count 2 | ✓ | 1 (m003) | no |
| cusp count 1 | ✓ | 15 | no |
| torsion-free | ✓ | 2 | no |
| amphichirality | ✓ | 9 | no |
| CS = 0 | ✓ | 7 | no |

`H₁ = ℤ` is exactly the statement that **m004 is a knot complement in S³**.

## The corrected statement

> **The genesis selects a family; knot-ness selects the member.**
>
> m004 is extremal along the metallic diagonal, ties m003 on volume, and is not distinguished at
> all by the arithmetic — which is a class invariant. The single elementary property separating
> m004 from its shape-field family is `H₁ = ℤ`. Uniqueness statements that do hold of m004 —
> Reid's unique arithmetic *knot* complement, Callahan's unique torsion-free Jørgensen group —
> are themselves knot-ness-conditioned and are cited, not consumed by the chain.

## A defect in B1136's own scope, found while re-deriving it — and repaired

B1136's FINDINGS states its family as *"the orientable cusped census manifolds whose tetrahedron
shape field is ℚ(√−3) — exactly **14**"*. Its scan (`verify_genericity.py:28-30`) breaks at
**census index > 1200**. That qualifier is absent from the sentence.

Re-scanning by tetrahedron count instead (≤ 6 tetrahedra, the depth its own 14 already reach,
since s594/s595/s596 are 6-tetrahedron manifolds) returns **21**, not 14. The seven it misses —
`s955, s956, s957, s958, s959, s960, s961` — sit at census indices **1256–1262**, immediately past
the cutoff. Verified exactly; the whole discrepancy is the cutoff and nothing else.

**This is an instance of the very class X15 catalogues, inside the arc that supplies L1's
evidence.** It is recorded here rather than left to be found.

**The conclusion survives the repair and is strengthened:** on the corrected 21-member family the
separator set is still exactly `['h1_is_Z']`. L1's corrected statement rests on a family half
again as large as the one originally scanned.

Two of the seven missed members — **s958 and s959** — are manifolds the record discusses by name
(s958 among the five class members where the index fires; s959 among the three carrying chirality,
the arithmetic, the door and the count of three together). Their absence from the banked family
list is therefore not cosmetic.

## What is NOT claimed here

- No withdrawal of B1136, whose conclusion is confirmed and widened.
- No claim that the full-census family is 21: the paper's own figure is 112 over the whole census.
  21 is the count at **≤ 6 tetrahedra**, stated with its bound, which is the point of the note.
- No statement about whether a different selection criterion could single out m004. L1 is about
  the criteria the record actually ran.
