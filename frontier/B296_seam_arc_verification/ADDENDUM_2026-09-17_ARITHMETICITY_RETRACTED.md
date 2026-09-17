# ADDENDUM (2026-09-17, S15/B1422) — the arithmeticity reading here is RETRACTED (E82/B1419)

This arc's files stated that the min-volume closing `m004(5,1)` is **non-arithmetic**, citing B288. **That is false.**
`m004(5,1)` is the **Meyerhoff manifold** and is arithmetic (Chinburg 1987; reproduced on this bench with Hilbert
symbols in `frontier/B1419_the_arithmetic_fillings_corrected/`), invariant trace field x⁴ − x − 1, discriminant −283.

**The root cause (E82).** The predicate used was the *cusped* arithmeticity criterion — imaginary-quadratic invariant
trace field — conjoined with √−3-containment. On a **closed** manifold that conjunction can never be satisfied, so it
decided nothing. What the computation correctly establishes, and what this arc's verdict actually needs, is that the
min-volume closing **does not keep the object's field ℚ(√−3)**. `verdict.py` and `tests/test_b291_scale_extremal.py`
are corrected in place: the predicate is renamed to what it computes, and the arithmeticity constant now records the
true answer.

**What this costs the arc's finding 3.** "Selection is axis-stratified … no single closing is distinguished on all
axes" is **weakened**: under the corrected criterion the **scale axis and the arithmetic axis coincide** at
`m004(±5,1)` — it is simultaneously the minimum-volume closing and an arithmetic one. What survives is that it keeps
none of the object's own arithmetic, and that it is not the dynamical (fibre) closing, so the closings are still not
ranked by one order.

**Specific to this arc.** B296 is the adversarial pass over the seam family. It extended the defective test to
`|p|,|q| ≤ 12` (174 closings), obtained the guaranteed zero, and reported *"every probe SURVIVES; 0 refutations"*.
A red-team that re-runs a criterion which cannot fail on a larger grid confirms nothing; it launders the defect it
was built to catch. The extended count is kept, renamed to the quantity it measures (imaginary-quadratic invariant
trace fields), and the survival banner should be read as covering the other probes only.
