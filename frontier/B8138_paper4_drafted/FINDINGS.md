# B8138 — Paper IV is drafted — three no-gos, each with its exhaustive escape

**Date:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical identification; no Standard-Model quantity appears.

## What was done

Drafted **Paper IV**: `papers/series/paper4_what_cannot_be_supplied/` — 5pp, clean build,
verification **7/7**. This completes the four-paper series.

## The result — three failures shown to be theorems

**(i) Scale.** Mostow rigidity fixes shape, not size, and `vol(cover) = d·vol(base)` with no
distinguished degree, so **no dimensionful quantity** is determined by the isometry type.
**ESCAPE:** dimensionless quantities — ratios, phases, mixing angles, integer counts — are
**untouched**. Stated explicitly, because the theorem is easy to overstate into *nothing numerical
can be obtained*, which is **false** and would close the one lane the argument leaves open.

**(ii) Orbit position.** A `G`-invariant is constant on each `G`-orbit, so no function of it
distinguishes two points of one orbit, and **no refinement of the same invariant ever will**. A
failure here is **not weak evidence — it is proof the evidence is of the wrong type**, so sharpening
the invariant is provably wasted effort. **ESCAPE: exactly two, and exhaustive** — shrink the group,
or add non-invariant structure; exhaustive because any successful selector either fails
`G`-invariance or is invariant for a smaller group.

**(iii) Family versus object.** Of seven elementary invariants, **exactly one** separates `m004`
within the 14 orientable cusped census manifolds of shape field `ℚ(√−3)`: **`H₁ ≅ ℤ`**. Volume,
tetrahedron count, cusp count, torsion-freeness, amphichirality (**shared with all thirteen
others**) and `CS = 0` are all shared. Consequently **`vol(m004) = (3√3/2)·L(χ₋₃,2)` is a FAMILY
property** (shared with `m003`), and **any construction taking the invariant trace field as input
takes a family-level input**. **ESCAPE:** select on `H₁ ≅ ℤ` *first* — that step is genuinely
object-level — and a later trace-field step inherits the selection. What is forbidden is the
reverse order.

## Two errors reported in the paper, because both are general failure modes

- **Float equality on Chern–Simons.** Comparing by exact equality made `m004`'s `9e-17` look unique
  and manufactured a *second* separating property. Five other members have `CS = 0`. **The error
  inverted the conclusion in the direction that flattered it.**
- **Testing a neighbouring property.** Torsion-freeness is **not** the knot-complement condition;
  `m202` and `m203` are torsion-free with `H₁ ≅ ℤ⊕ℤ`. Substituting an easier-to-compute property is
  **undetectable within the computation**, because the computation is correct — it answers a
  different question.

## Verification

`verify/check_family.py`, 7 checks. The family is **regenerated from the census**, not read from a
stored list, and reproduces B8128's table exactly. Controls encode both errors above: `CS` is
compared with an **explicit stated tolerance** and the run **prints both answers** (4 others by
equality vs 5 by tolerance) so the difference is visible; torsion-freeness and `H₁ ≅ ℤ` are both
computed and reported separately. **A check was added for a claim the paper made and I had not
tested — that amphichirality is shared with all thirteen others. It holds.**

## SCOPE

Nothing here resolves `OA-C0016`, `OA-C0018`, `OA-C1063` or `OA-C1064` — **none is PROVED and this
paper does not change that.** Its contribution is to convert three surrounding failures from open
questions into theorems with named escape routes, which is a different and smaller thing.

**Gate 5 untouched.**
