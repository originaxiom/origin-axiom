# B1087 — THE CHARGE COMPLEMENTARITY: the AW charge exists, is exactly balanced, and cannot be measured on any closed assembly — by non-commutativity

**Date:** 2026-08-19 · **Verdict: PROVED (the pre-registered OBSTRUCTED-O3 branch, which is a theorem)**
**Design:** pre-registered outcome grammar in `b1087_grading.py`'s header before execution
(GRADED-SYMMETRIC / GRADED-ASYMMETRIC / OBSTRUCTED-O1|O3, each branch banking). Machinery:
the B1086-verified module pipeline; all new computation exact over ℚ and ℚ(√−3).

## 1. The charge operator EXISTS (O1, O2)

Both θ-odd dial slots complete to exact Jacobson–Morozov sl₂-triples in e₆
([H,X] = 2X, [H,Y] = −2Y verified exactly). The charge spectra on the 27:

| slot | charges (charge, multiplicity) | pattern |
|---|---|---|
| hv8 | (−4,1) (−2,8) (0,9) (+2,8) (+4,1) | 1+8+9+8+1, trace 0 |
| hv16 | (−2,1) (−1,8) (0,9) (+1,8) (+2,1) | 1+8+9+8+1, trace 0 |

The two slots' charge lattices differ by exact doubling; the multiplicity pattern is
identical and sl₂-balanced. *(Observed echo, flagged not claimed: the 9-dimensional
neutral space; the corpus's 9-index structures (B1074's support-disjointness; the nine
menu rows) are noted for a future cell, not identified.)*

## 2. The obstruction (O3): charge does not commute with holonomy

**[ρ₂₇(H), ρ(μ)] ≠ 0 and [ρ₂₇(H), ρ(λ)] ≠ 0 — for BOTH slots.** The charge operator
fails to commute with the cusp holonomies, so no charge grading descends to the seam
cohomology h¹(T²; 27), and (with the fiber no-go, §3) to nothing built from the closed
object at all. **Charge and holonomy cannot be simultaneously diagonalized: the
uncertainty-principle shape the owner conjectured is a computed fact of this system.**

## 3. The fiber no-go and the family weight (O4, carried)

On any fixed twisted double: the θ-odd amalgam's closure is ALL of e₆ (B1086's sweep),
so only scalars commute with the image — no charge operator acts on H¹(D_t; 27). And
[H, X] = 2X means exp(sH) rescales the dial parameter: **the U(1) grades the FAMILY
{D_t}, mapping the t-fiber to the e^{2s}t-fiber** — the charge direction is the
deformation direction, not an internal quantum number of any single closed object.

## 4. THE THEOREM (the fourth language of the wall)

**The AW-U(1) charge is definable exactly where the object is NOT closed.** On a closed
assembly it is unmeasurable — not merely unbalanced (PD) but UNDEFINABLE, by
non-commutativity with the holonomies that closure forces. The wall's four languages:
PD-pairing (topology, B1086) = AW non-isolation (M-theory, B1084) = completion-kernel
(the rule, B1083) = **charge/holonomy non-commutativity (representation theory, this
arc)**. Where charge becomes measurable: the cut (B1085's edge; B1084's hatch — the
transversal isolated point, where the AW local model assigns exactly these 1-8-9-8-1
charges to localized matter). The laboratory lead (L173) inherits the sharpest framing:
an edge experiment is a charge measurement the closed object cannot perform on itself.

**Locks:** tests/test_b1087_charge_grading.py (the two JM triples' relations + the two
charge spectra + the O3 non-commutation, all exact and fast via the stored H vectors).
Full run record: `b1087_grading.py` + `b1087_results.json`.
