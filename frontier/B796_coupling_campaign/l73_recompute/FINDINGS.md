# L73 RECOMPUTE — abelian invisibility is not a property, it is a SELECTOR

cc3 audit seat, 2026-08-08. Gate 5-Q. Nothing to `CLAIMS.md`. This is an
audit recomputation of a closure this seat flagged, not a new arc claim.

## Why

The relational re-read marked **L73 (abelian invisibility) REOPEN**. The
banked closure reads the property as belonging to the object: `det(A₁ − I) = −1`
is a unit mod every N, so the abelian theater has exactly one fixed point
everywhere and the object is invisible to abelian probes.

Under B803 the invariant trace field is a *commensurability* invariant, so a
property stated of "the object" must be checked against the object's relatives
before it may be banked as structural. It never was.

## What was computed

`|H₁ torsion|` direct from SnapPy 3.3.2 for the six manifolds B855 registers
as the family's two rows. Not derived via `|2 − tr M|` (which holds only for
once-punctured-torus bundles) — read off the homology directly, so it is valid
for every row member regardless of type.

| manifold | row | volume | cusps | H₁ | \|torsion\| |
|---|---|---|---|---|---|
| **m004** | golden, PSL(2,O₋₃) | 2.029883213 | 1 | ℤ | **1** |
| m003 | golden | 2.029883213 | 1 | ℤ/5 + ℤ | 5 |
| m206 | golden | 4.059766426 | 1 | ℤ/5 + ℤ | 5 |
| m136 | silver, PSL(2,O₋₁) | 3.663862377 | 1 | ℤ/2 + ℤ/2 + ℤ | 4 |
| m129 | silver | 3.663862377 | **2** | ℤ + ℤ | 1 |
| m135 | silver | 3.663862377 | 1 | ℤ/2 + ℤ/4 + ℤ | 8 |

## The result

**Among the one-cusped members of both rows, m004 is the unique manifold with
trivial H₁ torsion.** Five comparators, including three from the silver row —
a different field, ℚ(√−1) — and m004 stands alone.

m129 also has trivial torsion, and is excluded on a stated ground rather than a
convenient one: it has **two cusps**, so H₁ has free rank ≥ 2 and torsion-freeness
carries no information about an abelian probe of a one-cusped theater. The
comparison class is one-cusped members; m129 is not in it.

## What this does to the closure

The closure said abelian invisibility is a property of the object. It is not —
its own sister falsifies it *inside the commensurability class*, at **5**, the
hearing prime (m003: ℤ/5 + ℤ). But the recomputation does not merely narrow the
claim, it **inverts its type**:

> Invisibility is not a property the object HAS.
> It is a property that SEPARATES the object from every one-cusped relative it has.

A property shared with the family is structural background; a property that
holds for exactly one member is a **selection principle**. L73 was banked as the
first and is actually the second, which is the more valuable of the two — and
the single-object framing is precisely what hid it, because when the object is
the whole, "true of the object" and "true of its class" are the same sentence.

## Scope, stated exactly (the error this audit exists to catch)

Computed over **the six manifolds B855 registers as the two rows** — NOT over
the commensurability class, which is infinite, and NOT over all one-cusped
hyperbolic manifolds. The statement is: *within B855's registered family,
restricted to one-cusped members, m004 uniquely has trivial H₁ torsion.*
Anything wider is unproved here.

## THE CONTROL — RUN, AND IT KILLS THE SELECTOR

The section above originally ended by registering the base-rate control as a
*successor*. That is the exact move this audit exists to stop, so it was run
immediately instead. **It returns a null, and the null is against the reading
proposed one paragraph earlier.**

`snappy.OrientableCuspedCensus(cusps=1)`, |H₁ torsion| computed for every member:

| population | n | trivial torsion | rate |
|---|---|---|---|
| all one-cusped census manifolds | 203,123 | 123,538 | **60.8%** |
| one-cusped, volume < 4.1 (the rows' range) | 3,646 | 1,743 | **47.8%** |

**Trivial H₁ torsion is a coin flip.** Half of all comparable manifolds have it.
m004 having it is not a distinction; among six relatives you would *expect*
about three to be trivial.

The residual pattern — m004 trivial while all five relatives are non-trivial —
prices out at 0.478 × 0.522⁵ ≈ **1.9%** under an independence assumption that
does **not** hold (the six are commensurable or related, not independent draws)
and for a statistic **chosen after seeing the data**. Post-hoc, non-independent,
n=6. That is not a result. **No selection claim survives.**

## What actually stands

1. **The falsification stands** (it needed no base rate): the banked closure
   says abelian invisibility is a property of the object; its own sister m003
   has |torsion| = 5. A property that fails inside the commensurability class
   is not a property of the class. **L73's closure is over-wide as banked.**
2. **The selector does NOT stand.** The attractive inversion — "invisibility
   separates the object from its relatives" — is a base-rate artefact. Recorded
   here, refuted here, in the same file, so it cannot be re-registered later as
   a fresh idea by a seat that reads only the first half.

This is B855's warning firing on live material — *"the programme has never had
a valid control, so 'generic vs specific' has essentially never been TESTED"* —
and E20's failure mode (a base-rate-generic fact read as object-specific)
caught within minutes of being proposed, by the cheapest possible check.

**The lesson is the transferable part:** the day produced three surveys and one
computation, and the computation is the only thing that changed a verdict —
first by falsifying a closure, then by refuting the falsifier's own attractive
successor. Discovery was never the bottleneck.

Reproduce: `python3 l73_recompute.py` (rows) and `python3 l73_basrate.py` (control)
