# B433 — the 3d-3d dictionary calibrated at SL(2): Coulomb branch = the character variety, exactly

**Status: banked. Adjudicates Chat-1's 3d-3d handoff (2026-07-05): the frame is CONSISTENT and
its core dictionary entry now VERIFIED in-sandbox at SL(2); the E₆ assembly remains the priced
specialist gate (L50). Firewalled.**

## The calibration (leg 1 — verified exact)

From the raw DGG input (m004's 2-tetrahedron triangulation: snappy gluing + cusp equations),
eliminating the shape parameters under the standard holonomy convention (cusp rows = eigenvalue²)
gives the eliminant
    **−A_CL(M,L) · A_CL(M,−L)**
— the banked Cooper-Long A-polynomial (B67, trace-map route) times its sign-twisted partner =
exactly the two SL(2)-lifts of the geometric PSL(2) component. Two fully independent routes
(triangulation/DGG vs trace-map/B67) land on the same curve. The 3d-3d core entry "Coulomb
branch of T[M₃,SL(2)] = the SL(2) character variety" holds exactly for our object. Convention
control: the three wrong conventions (M²L, ML, ML²) all FAIL divisibility — the match is not
convention-flexible.

## The adjudication of the 3d-3d handoff (recorded)

- The layer frame (TQFT = topological sector, anyonic B428; fermions in the physical sector of
  T[M₃]) is CONSISTENT with every banked theorem (B428/B429/B430) — credited.
- The "specific computation needed" (assemble T[4₁,E₆]) is NOT new: it is the registered L50 /
  class-S specialist gate (V238 arc). Recorded as the named terminal gate, not progress.
- §3's θ-partition typo corrected in place: F₄ = {1,5,7,11}, coset = {4,8} (B347).
- Scale enters only via the external embedding (R / CY) — convergent with the banked scale wall
  (B426: no invariant functional grows; λ=0 both towers).
- Leg 2 (the Dimofte–Garoufalidis 1-loop = the torsion −3) DEFERRED: needs the exact NZ-datum
  formula; flagged, not rushed — the standing next calibration step.

**Provenance.** calibration.sage (reproducer; requires snappy/sage); lock
tests/test_b433_calibration.py (locks the banked eliminant factorization exactly, pure sympy).
