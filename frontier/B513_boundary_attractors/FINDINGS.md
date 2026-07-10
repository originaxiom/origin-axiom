# B513 — The boundary-type attractors (verified) + the filtered signature lead (tombstoned)
**A meditation-pass structural synthesis, 2026-07-11. What survived scrutiny is banked; what didn't
is recorded as a tombstone so it is not re-chased.**

## SOLID (verified, banked): the three verbs act on the object's BOUNDARY
κ = tr[A,B] is the commutator = the boundary curve of the once-punctured torus. Exact:
| verb | flows κ to | commutator [A,B] becomes | reading |
|---|---|---|---|
| **evolution F** | CONSERVES κ (home κ=−2) | **parabolic** (μ=−1 double) = the CUSP | the object stays the figure-eight (complete hyperbolic structure) |
| **decoherence M** | **κ=0** (β-zero attractor, exact g_M) | **order 4** ([A,B]⁴=I, verified) = pointer | the boundary closes to a finite 2π/4 cone |
| **decimation D** | **κ=2** (g_D<0 everywhere) | **reducible** (A,B commute) | the boundary degenerates → classical/abelian |

**The sharpened law (from the exact β-functions):** decoherence and coarse-graining have DIFFERENT
attractors — M→the pointer (κ=0, a specific quantum state), D→classical (κ=2). In a mix D wins (its
everywhere-negative g_D beats M's gentle slope near 0), matching D3.1. This makes S063's "decoherence
critical / coarse-graining classicalizes" SHARP: they flow to different fixed points. Compact/noncompact
split: |κ|<2 elliptic ("space"), |κ|>2 hyperbolic ("time"), κ=±2 parabolic (null); the object lives on
the null boundary κ=−2. Lock: `tests/test_b513.py`.

## TOMBSTONE (filtered out — do NOT re-chase): the (3,1) signature story
Tempting lead: the Hessian of κ has signature (3,0) Euclidean near the object and (2,1) Lorentzian on
the noncompact side — "the object on its light cone." **KILLED by the shell-constancy test:** the
signature is NOT κ-controlled — det(Hessian)=−2(x²+y²+z²+xyz−4), so the signature-change locus is the
surface x²+y²+z²+xyz=4, which cuts ACROSS κ-shells (κ=1 shell: 20 Euclidean/10 Lorentzian). Also the
geometric (Eisenstein) rep is COMPLEX, not on the SU(2) real locus where the signature lives. The 3d
(2,1) that appears is generic (any F₂ variety) and not object-specific; a genuine (3,1) needs the 4-dim
spacetime pairing (D2, uncomputed) and is NOT established by this. T-SIG remains OPEN, not supported.
