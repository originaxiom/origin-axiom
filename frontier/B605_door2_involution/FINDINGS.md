# B605 — Door 2 settled: the amphichiral involutions are FREE (Gieseking
deck transformations), not reflections

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
The incoming Door-2 handoff verified and resolved mechanically. Lock
`tests/test_b605_door2.py` (OA_SLOW, ~5 min). Run:
`python3 door2_involution.py`.**

## Verification of the incoming handoff (verify-don't-trust)

- **CONFIRMED:** the gluing-polynomial factorization (banked P12), the
  2-regular-ideal-tetrahedra decomposition (Φ₆ shape; SnapPy 2
  tetrahedra), |Isom(M)| = 8 = D₄, amphichirality.
- **REFUTED-AS-INCOMPLETE (the exclusion argument):** the tetrahedron
  point-group argument covers symmetries FIXING each tetrahedron; an
  involution SWAPPING the two tetrahedra can a priori have isolated
  fixed points on the shared faces (rotation-by-π × normal-flip = the
  −I local model). The type had to be computed.
- **REFUTED (the conclusion):** τ is NOT a reflection, and Fix(τ) is NOT
  a totally geodesic surface — see the verdict.

## The mechanical verdict (exact intertwiners + the Γ-lift census)

From the step-1 certified rep over ℚ(√−3): the four orientation-reversing
families of Isom(M) = D₄, with exact intertwiners U (certified over K):

- φ(a) = a family: U = [[1, ζ̄₆],[0,1]], τ² = the meridian ∈ Γ ⇒ an
  INVOLUTION of M; the cusp-level lift is a GLIDE.
- φ(a) = b family: τ² = baB ∈ Γ ⇒ the second involution; also a glide.
- φ(a) = A and φ(a) = B families: τ² = the half-longitude isometry
  (∉ Γ, = the r² of D₄) ⇒ ORDER-4 elements, exactly matching D₄'s
  coset structure (two order-2 + two order-4 orientation-reversing).
- **THE CENSUS:** over all reduced Γ-lifts to word length 6 (1457 lifts
  × 4 families): ZERO reflection-type (UŪ = +λI) and ZERO antipodal-type
  (−λI) lifts. Every lift is a glide. Bounded-search framing: this is
  not a proof of freeness by itself, but—
- **THE COMPUTED IDENTIFICATION closes it:** m000 (the Gieseking
  manifold) is non-orientable, one ideal regular tetrahedron, volume =
  vol(4₁)/2 EXACTLY, and **4₁ is its unique degree-2 cover** (SnapPy,
  computed). The free orientation-reversing involution is the Gieseking
  deck transformation; the "2 regular tetrahedra" of the handoff are the
  double of Gieseking's one. The free answer is therefore exact, not
  merely census-bounded, for that involution class.

## The Door-2 consequence (the handoff's sharpening, inverted)

> **τ acts freely: Fix(τ) = ∅. There is no totally geodesic fixed
> surface and no fixed point. M₃⋊_τS¹ is a SMOOTH 4-manifold (a twisted
> mapping torus; the fiber quotient M/τ is the Gieseking-type
> non-orientable hyperbolic manifold), NOT an orbifold. The handoff's
> "Lorentzian question on a singular 4-orbifold" dissolves; the question
> returns to the smooth setting, where free quotients are the
> well-behaved case.**

The handoff's honest-calibration instinct was right: the classical
reasoning was strong but the conclusion was wrong at the last step — the
missing case (glide/free) is the one that holds, and it was invisible to
both the tetrahedron argument (swap gap) and the trace-field heuristic.
