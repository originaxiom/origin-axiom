# R68 — I-14 COLLAPSES TO A POINT: of E₆'s 40 trinification subsystems, exactly one is stable under the founding ratio acting from both sides

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report, not banked. Exact over ℚ(√5); script `computations/r68_g_stable_a2cubed.py` (on R64's rebuilt icosian E₈). Follows R65 (85 → 40) and R66/R67 (the class is computed, not assumed).

## 0. Result

A trinification grading of the 27 (I-14, L3) is the same datum as an **A₂³ root subsystem of E₆** — the centralizer of its grading element — and E₆ has exactly **40** of them (|W(E₆)|/|W(A₂)³ ⋊ S₃| = 51840/1296; enumerated here: 120 A₂ subsystems, 40 mutually orthogonal triples), the 40 colourings of R65. On the icosian E₆ = ℤ[g]^⊥ the founding ratio g acts by **left** multiplication (B1270's action) and, commuting with it, by **right** multiplication; both preserve E₆. Counted directly over the 40:

| condition on an A₂³ ⊂ E₆ | how many |
|---|---|
| stable under left multiplication by g | **4** |
| stable under right multiplication by g | **4** |
| stable under **both** | **1** |

> **Exactly one trinification subsystem of E₆ is a two-sided ℤ[g]-frame.** Each of its three planes is itself a two-sided ℤ[g]-submodule. **I-14's multiplicity, measured at 85 (B1264), falls 85 → 40 (R65) → 4 (left-stable) → 1.** The object supplies the point.

The structure behind the numbers: every left-g-orbit of E₆ roots spans an A₂ plane (B(r, gr) = Re(g) = −½ for every root); the 24 orbits give 12 planes; these 12 planes partition into **4** orthogonal frames (each plane in exactly one), which are the 4 left-stable A₂³'s. Right multiplication by g permutes the 4 frames as a **3-cycle plus a fixed point**; the fixed frame is the two-sided one. The mirror (quaternion conjugation) does not act on left-frames at all — it exchanges left- and right-stability — but it preserves the unique two-sided frame: **invariant under conjugation: True**. So the selected subsystem is mirror-even, as a structure the object supplies about itself should be (H5: the bit is elsewhere).

## 1. What it is, concretely

The two-sided frame's first plane contains the root φ⁻¹·1 = ((−1+√5)/2, 0, 0, 0) — the golden-conjugate copy of the family plane {1, g}: under the Conway–Sloane form, 1 and φ⁻¹ are orthogonal, and φ⁻¹·ℤ[g] is the Galois partner of the Eisenstein plane inside the icosians. The other two planes are the two-sided ℤ[g]-modules in the i, j, k directions. Together with the family plane, E₈ = ℤ[g]⁴ decomposes into **four** two-sided Eisenstein planes, uniquely: the family plane, its golden conjugate, and two more. That is the "quadrification" A₂⁴ ⊂ E₈ the object carries, and the trinification A₂³ ⊂ E₆ is its E₆ part.

## 2. Status of the ledger row, as this seat reads it

I-14 asks for a map from L3 (the grading) to L4 (the commensurator's ω) that **acts**. R64 showed L3 and L4 are the two factors of one element; R65 cut the admissible gradings to the trinification class; this report cuts the class to one subsystem by the object's own two-sided action. What is exhibited: the subsystem and the element that selects it. What is not exhibited: that the physical trinification (the SU(3)³ the record's chain uses at Step 8 of the journey) *is* this subsystem rather than one of the other 39 — that identification is the listener-map half of the row and is unchanged. In the record's own terms this is the third measured H5 multiplicity to become a point (after I-6 at B1272/B1273 and I-25 at B1274), and the largest.

## 3. Controls

- The 40 is reproduced from the 120 A₂ subsystems by orthogonality, matching the group-theoretic count.
- Left- and right-stability are tested on the full 18-root subsystem, not on planes.
- The 4 left-stable frames are exhibited as a partition of the 12 g-planes (each plane in exactly one triple), and right-g's action on them is computed as a permutation.
- Conjugation's failure to act on left-frames is a caught exception in the script, recorded, not assumed.

*Sweep: "two-sided", "right multiplication", and any A₂³-selection by g appear nowhere on main or the SM-derivation branch; B1270 uses left multiplication only.*
