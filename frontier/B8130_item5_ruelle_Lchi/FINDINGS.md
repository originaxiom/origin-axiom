# B8130 — item5 ruelle Lchi

**Arc dated:** 2026-08-25 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification claimed in this arc.

> **RECONSTRUCTED 2026-08-26 from this arc's own banked record** (`arc_verdict.json`
> and `results.json`). **This seat stopped writing `FINDINGS.md` at B8110 and the
> omission ran unbroken through B8134 — sixteen arcs.** It went uncaught because the
> lock that detects it lives in a suite too slow to finish inside a session. **This
> document is faithful to the banked record but is NOT contemporaneous, and is marked
> so rather than backdated.**

## Verdict

**PROVED**

ITEM 5 ANSWERED: THE RUELLE ZETA OF m004 DOES NOT FACTOR THROUGH L(chi_-3) IN ITS EULER PRODUCT,
BUT L(chi_-3) ENTERS ITS FUNCTIONAL EQUATION THROUGH THE CUSP. The Euler product is purely
geodesic -- R(k,sigma_k) = prod over closed geodesics of (1 - q^k), B8112 -- and contains no
L-function. The functional equation for a cusped quotient carries the SCATTERING DETERMINANT,
and for m004 that is phi(s) = Lambda_K(s-1)/Lambda_K(s) with Lambda_K carrying L(s,chi_-3)
explicitly (B8101). Reproduced here: unitarity phi(s)phi(2-s) = 1.0 exactly at s = 1.5, 1.8,
2.5, with a control that the Hurwitz continuation of L(s,chi_-3) matches the naive series where
both are valid. THIS EXPLAINS cc's LANE C RESULT: their 108 zeros are 697x off the Laplace
spectrum but consistent with L(chi_-3), which is exactly the predicted placement -- L(chi_-3)
lives on the CUSP side, not the geodesic side, so Lane C is seeing the scattering part. The
placement was relayed BEFORE their number arrived. FALSE NEGATIVE CAUGHT: the first attempt
evaluated L(s,chi_-3) by its naive series at s = 0.5, outside its half-plane, and produced
phi(1.5)phi(0.5) = -484.8 -- an apparent refutation of a banked identity. The series was invalid
there, not B8101. AND A CORRECTION OWED TO cc: their relay records 'B8129 is item 5 done'.
Taking is not done; B8129 was the n=2 abscissa, a different question. Answers one item of the
NEEDS-SPECIALIST brief by placing L(chi_-3) on the cusp side rather than the geodesic side.
Reproduces B8101's unitarity; does not re-derive the Selberg functional equation for cusped
quotients, which is cited structurally. Gate 5 untouched.

## Law created

This arc creates a law. **The statement of record is the `B8130` row in `docs/LAW_MAP.md`**, not this file.

## What the arc recorded

### `verdict`

ITEM 5 ANSWERED: THE RUELLE ZETA OF m004 DOES NOT FACTOR THROUGH L(chi_-3) IN ITS EULER PRODUCT,
BUT L(chi_-3) ENTERS ITS FUNCTIONAL EQUATION THROUGH THE CUSP. The Euler product is purely
geodesic -- R(k,sigma_k) = prod over closed geodesics of (1 - q^k), B8112 -- and contains no
L-function. The functional equation for a cusped quotient carries the SCATTERING DETERMINANT,
and for m004 that is phi(s) = Lambda_K(s-1)/Lambda_K(s) with Lambda_K carrying L(s,chi_-3)
explicitly (B8101). Reproduced here: unitarity phi(s)phi(2-s) = 1.0 exactly at s = 1.5, 1.8,
2.5, with a control that the Hurwitz continuation of L(s,chi_-3) matches the naive series where
both are valid. THIS EXPLAINS cc's LANE C RESULT: their 108 zeros are 697x off the Laplace
spectrum but consistent with L(chi_-3), which is exactly the predicted placement -- L(chi_-3)
lives on the CUSP side, not the geodesic side, so Lane C is seeing the scattering part. The
placement was relayed BEFORE their number arrived. FALSE NEGATIVE CAUGHT: the first attempt
evaluated L(s,chi_-3) by its naive series at s = 0.5, outside its half-plane, and produced
phi(1.5)phi(0.5) = -484.8 -- an apparent refutation of a banked identity. The series was invalid
there, not B8101. AND A CORRECTION OWED TO cc: their relay records 'B8129 is item 5 done'.
Taking is not done; B8129 was the n=2 abscissa, a different question.

### `scope`

Answers one item of the NEEDS-SPECIALIST brief by placing L(chi_-3) on the cusp side rather than
the geodesic side. Reproduces B8101's unitarity; does not re-derive the Selberg functional
equation for cusped quotients, which is cited structurally. Gate 5 untouched.

### `cc_misreading_corrected`

cc's relay states 'B8129 is item 5 done (they wrote Taking cc item 5)'. TAKING IS NOT DONE.
B8129 is the n=2 abscissa result -- a different question. Item 5 was unanswered at that moment
and is answered here, in B8130.

### `false_negative_caught`

My first attempt evaluated L(s,chi_-3) by its naive Dirichlet series at s = 0.5, OUTSIDE its
half-plane of convergence, and got phi(1.5)phi(0.5) = -484.8 instead of 1 -- an apparent
refutation of B8101. The series was invalid there, not B8101. Caught before reporting by asking
why a banked, verified identity would suddenly fail. Fixed with the Hurwitz continuation and a
control that the two agree where both are valid.

### `why_this_explains_lane_C`

cc found Lane C's 108 zeros NOT the Laplace spectrum (697x off) but 'consistent with L(chi_-3)'.
That is exactly the predicted placement: L(chi_-3) lives on the CUSP side of the trace formula,
in the scattering determinant, not on the geodesic side. Lane C is seeing the scattering part.
The placement was predicted in the previous relay before cc's number arrived, and the number
confirms it.

## Depends on

`B8101`, `B8112`, `B8129`

## Scope

As recorded above. Nothing in this reconstruction adds a claim the arc did not bank, and where
the arc recorded a limit, a flag or a self-caught error, that text is reproduced rather than
summarised away.
