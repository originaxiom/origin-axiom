# B621 — THE κ-GATING LAW (the conductor arc's final piece) + the object-naming correction

**Status: banked (frontier). Cell A of the conductor-endgame campaign
(seat: workflow agent; verified in-loop). Reproducer `scan2.py` (copied
from the agent's workspace); the machinery is B620's verbatim.**

## THE GATING RULE (derived + verified, zero exceptions κ = 4..27)

Write the torsion base t² − 4 = 3^v · m with gcd(m, 3) = 1. Then:

> **The reflection coset carries the object's field content if and only
> if m | κ.** The 3-part is never an independent gate: the A₂ lattice's
> own discriminant 3 (det of the Cartan matrix; the index [P:Q] = 3
> hard-wired into ℂ[P/κQ]) pre-supplies the 3 at every level, absorbing
> 3^v for free. And v is determined by elementary arithmetic:
> t² ≡ 1 (mod 3) unless 3 | t, so v = 0 exactly when 3 | t (the fig-8)
> and v = 1 otherwise (the trace-4 and trace-5 bundles).

Verified with the EXCLUSIVITY control (reflection-coset content present
AND identity/rotation-coset content absent): RL (base 5): bearing at
exactly {5,10,15,20,25}; the trace-4 R²L bundle (base 12 = 3·4): at
exactly {4,8,12,16,20,24} — the true gate is 4 | κ; the trace-5 R³L
bundle (base 21 = 3·7): at exactly {7,14,21}. The naive per-value √12
test is contaminated by the ambient √3 (= the lattice's own content) —
the exclusivity control is mandatory when 3 | base.

## Registered open reconciliation

B618's scan used a DIFFERENT observable (the SU(3)ₖ odd trace via
Kac–Peterson) and reported the trace-4 object's content at {12, 24}; the
Weil-coset gate here is 4 | κ (a superset). The two observables differ
by an antisymmetric projection; reconciling them is registered as the
arc's residual (the B618 prediction's PASS is unaffected — its sealed
criterion was d | 21 for the trace-5 object, which this rule confirms).

## THE OBJECT-NAMING CORRECTION (binding, propagates to B610/B616/B618/B619)

Cell C established (SnapPy isometry + the repo's own ledger): **the
census manifold m136 is the RRLL (trace-6, SILVER) bundle, not R²L.**
The R²L (trace-4, vol 2.6667) bundle used in B610/B616/B618/B619 is a
legitimate second object but was MISNAMED "m136" (inheriting chat-1's
handoff error through my adjudication, which corrected "5₂" but landed
on the wrong census name). ALL mathematics in those arcs stands — the
computed object was always the R²L bundle itself (its weld word, its
eigenvalue field ℚ(√3), its base 12); only the census label was wrong.
Corrected designations: "the R²L bundle" (trace 4) and "m136 = the
silver RRLL bundle" (trace 6). Notably B611/B612 already computed RRLL
as "the silver bundle" — those arcs are unaffected.
