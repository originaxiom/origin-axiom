# B1024 PREREGISTRATION — L153: are the torsor bits the frame bits? (sealed before compute)

**Date sealed:** 2026-08-10 · **Seat:** cc (corpus lane; the L153 cell this seat owes from
Phase 2's Blocker 1). Gate 5-Q; zero anchors; no measured value.

## The question, exactly

B782's observer-torsor generators (conjugation, reversal; golden branch spent on A7) versus
B936's H¹(⟨τ⟩, T_ad[2]) = (ℤ/2)² Hermitian-frame classes (indexed by E₆'s τ-fixed Dynkin nodes).
**Do the torsor generators' 27-shadows generate the H¹ classes?**

## Method, fixed now

From the banked artifacts only (B936's `results.json` Q_A blocks; B928's torsor theorem
H(σ_χ∘τ) = H₊·ρ₂₇(σ_{χ·χ₊}); B939's shadow map σ₋₁→D, σ_χ₋→D₂, σ_c→D_c; the B961 frame
instrument for any recomputation): compute the H¹ class of each torsor generator's shadow —
coboundary (trivial class) or which nonzero class. **The reversal generator's shadow must be
constructed if not banked** (B939 names σ₋₁, σ_χ₋, σ_c; reversal's image under the shadow map is
part of the cell, from the banked machinery, not assumed).

## Outcomes, sealed

- **SAME (deficit 2):** the two shadows generate H¹ = (ℤ/2)² — the frame bits ARE the torsor
  bits in a second presentation; R11's T1 tightens to d = 2 and the input list stands.
- **INDEPENDENT (deficit 4):** the shadows land in coboundaries (or generate a proper subgroup)
  — the frame classes are NEW discrete inputs; the counted input list undercounts by up to two
  bits, and THE_CLAIM's hypothesis line gains them. **This outcome makes the interface bigger and
  must be stated as such, not smoothed.**
- **PARTIAL (deficit 3):** exactly one class generated — mixed; stated exactly.

## Declared prior

**Honest: uncertain, lean SAME** — B939's shadow map exists precisely because the frame and the
torsor talk to each other, and D₂'s coboundary status (B936) shows the map reaches the
coboundary/class distinction. But the lean is weak: the τ-fixed-node indexing smells intrinsic to
the 27, not to the observer. Non-weakening applies.
