# B411 — the hint-sweep: the local/emergent dichotomy, and where to work

**Status: a synthesis finding from the negatives (owner-requested hint sweep). The naive
dictionary is KILLED but its failure localizes the productive direction. Firewalled.**

## What was tested and what died

Hypothesis (from the negatives' pattern — P68 local, all relabelings emergent): a cell's
full H-field-type (√5/√−3/√−15 active) is a FUNCTION of γ′ arithmetic invariants
(χ₋₃(det), χ₅(det), gcd(det,15)). VERDICT: **multi-valued on the generic (invertible-det)
cells** — 6 H-types share the class-1 label — so (det, char) does NOT determine the generic
field. It DOES determine the field on the BOUNDARY cells (gcd ∈ {3,5,15}: single-valued).

## The three things the failure reveals (the actual payload)

1. **The boundary/generic split is a field law, not just a value law.** On the boundary the
   field-type is arithmetic-determined (a partial dictionary, extending P68's gate); on the
   generic cells it is not — the generic cells carry field content BEYOND γ′.

2. **The missing ingredient is named: the CHARACTER VALUE χ = tr(W₁ʲW₂ˡJ⁻¹), not the group
   invariants.** P68 succeeded because it routed through χ's ORDER (root-of-unity), not
   det(γ′). The complete LOCAL invariant of a cell is the PAIR (γ′-class, χ-field-datum) —
   a sharper, still-derivable target than "hunt determinant laws."

3. **THE META-INSIGHT (the angle from all the negatives):** the object has two layers —
   a LOCAL/derivable layer (field-content laws: P68, the root-of-unity law, the boundary
   dictionary) and an EMERGENT/aggregate layer (every relabeling symmetry: the mirror M3,
   the class action 2b-i, the (2,3) stabilizer M5). **Π_H (averaging over Gal(ℚ(ζ₆₀)/H),
   order 4) is the BOUNDARY between them:** the "hard" emergent phenomena are Π_H-shadows
   of a simpler upstairs structure in ℚ(ζ₆₀). ACTIONABLE DIRECTION (would ease the job):
   study the raw table UPSTAIRS in ℚ(ζ₆₀) — before Π_H — where the relabeling symmetries
   are conjecturally cell-local; then the mirror / class-action / stabilizer negatives all
   become projection COROLLARIES of one positive upstairs theory. This converts 3+ banked
   negatives into one research target and gives Phase 2b's staged residual (the √5-
   withholding) its natural home (the full-field convolution IS the upstairs object).

**Provenance.** sweep.py → dictionary.json; a directional finding (no promotion). Locks:
tests/test_b411_dictionary.py (the boundary-determinism + generic-multivalence facts).


---

## UPDATE (TW4/B418): the 'work upstairs' hope is REFUTED for the mirror
The mirror is NOT cell-local even in the full ℚ(ζ₆₀) (no Galois element realizes it on the
raw table — B418). The emergent symmetries are INTRINSIC, not Π_H-artifacts. B411's meta-
insight (Π_H is the local/emergent boundary) stands as a DESCRIPTION, but the actionable
direction (unify the negatives by working upstairs) is closed for the mirror. Sharper truth:
the emergence is a genuine feature of the object.
