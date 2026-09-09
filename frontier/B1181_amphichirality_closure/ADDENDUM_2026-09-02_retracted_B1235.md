# Addendum (2026-09-02) — RETRACTED at B1235: the family is 38/112 amphichiral

**What this arc asserted:** 83 of 83 amphichiral, "spot-verified 5/5 by the reliable mirror-isometry method".

**What was wrong:** `M.is_isometric_to(mirror)` is orientation-blind — this repo's own `REPRODUCIBILITY.md:73` says
so. The "reliable method" was the unreliable one. Under `symmetry_group().is_amphicheiral()` the 112-family
(B1186) is **38 amphichiral / 74 chiral**; this arc's own spot-check witness **o10_150700 is chiral** (CS = −1/12,
H₁ = ℤ, symmetry order 2). Zero B1224 violations. 38 of the 74 chiral members are CS-silent (CS ∈ {0, ¼}), which is
why a CS-only screen could never have caught it. Full table: `frontier/B1235_two_seat_harvest/verification/chirality_112.json`.

**What stands:** the ONE-WAY FAMILY TEST method-law (LAW_MAP §G). Enlarging a family can only help a family-level
claim — and correcting the *method* can only hurt one. This retraction is the law's second instance.

**The lock:** `tests/test_b1181_amphichirality_closure.py` pinned the string "83 of 83" and asserted
`"is_isometric_to" in reproduce.sh` under the name `test_reproduce_uses_reliable_method`. E53's sub-mechanism, exact:
the lock certified the error. Re-pointed to the fact.

**Consequence for B1163:** the family-wide W₀ obstruction's "83-of-83" upgrade is withdrawn; "verified 4 of 14" was
the honest count and the no-sibling-escape conclusion must be re-argued on the 38, not asserted on 83. m004's own
theorem (B1224) is untouched.

Source: fab5cloud D9/D5, recomputed here (B1235 cell 1).
