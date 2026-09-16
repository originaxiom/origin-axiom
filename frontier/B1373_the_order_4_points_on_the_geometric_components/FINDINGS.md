# B1373 — THE ORDER-4 POINTS ON THE GEOMETRIC PATH: door 2's last residual needs a point of a free-cusp member's character variety where both peripheral eigenvalues on the free cusp are fourth roots of unity with non-unitary holonomy; along the deformation path of the hyperbolic structure through cone-manifolds, the point where one peripheral curve has eigenvalue ±i (cone angle π) is reached on 132 of the 166 (cusp, curve) pairs of the 35 candidates, and at every one of them the other curve's eigenvalue is non-unitary — Theorem B closes it; on the other 34 pairs (all meridians) the structure degenerates before the point is reached, with the other curve's translation length growing monotonically without bound — 23 within a sixteenth of cone angle π, 11 at cone angle 2π/3: ideal points of the real path, no representation there; no candidate on the geometric path anywhere, the rest of the character variety untouched

**Date:** 2026-09-16 · **Seat:** cc (the SM-derivation branch) · **Status:** NEGATIVE on the geometric path (numerical, SnapPy's cone-manifold continuation; the eigenvalues read to 10⁻⁶) · the remainder of door 2's residual OPEN (points off the real path and on other components of the character varieties, which the record cannot enumerate) · **Price: unchanged** · **Numbering:** B1373 (door 2's residual, B1372 §6).

## 0. Seen from above

B1372 left door 2 open in one place: a point of the SL(2,ℂ) character variety of one of the 35 free-cusp members at which both peripheral
eigenvalues on the free cusp are fourth roots of unity (Theorem C) while the representation is non-unitary. On the geometric
component — the deformations of the complete hyperbolic structure — the natural route to such a point is the cone-manifold path: fill
the free cusp along a curve with a real coefficient p, so that the curve acquires cone angle 2π/p, and let p decrease to 1 on the doubled
slope, where the curve's eigenvalue is ±i. This arc follows that path on both peripheral curves of every free cusp (166 pairs) and reads
the other curve's holonomy at the endpoint. Where the endpoint is reached — 132 pairs, all 83 longitude cases and 49 meridian cases — the
other eigenvalue is never unitary: Theorem B forbids simultaneous cusp-fixedness of the two halves there. Where it is not reached, the
structure degenerates: on 30 meridian cases the other holonomy grows without bound as the angle approaches π (an ideal point of the
component, at which no representation exists), and on 4 the solver stalls at cone angle 2π/3 with the same growth (o10_150684 cusp 1,
o10_150708 cusp 0, o10_150714 cusp 0, o10_150725 cusp 1). So along the geometric path door 2 never opens. What this does not cover is
stated plainly: points of the geometric component off the real path (a complex curve has more points over M = ±i than the real cone
path visits, and the A-polynomials of ten-tetrahedron manifolds are beyond the record's exact tools), and the non-geometric components.

## 1. Computed

`verification/order4_points.py` (seconds; record `order4_points_run.txt`).

| item | result |
|---|---|
| pairs (free cusp, peripheral curve) on the 35 candidates | 83 cusps × 2 curves = 166; continuation by fillings (2p, 0) or (0, 2p), p = 30 → 1, the other cusps complete |
| reached (the filled curve's holonomy = iπ, eigenvalue ±i, a non-degenerate solution) | **132**: every longitude case (83) and 49 meridian cases |
| the other curve's eigenvalue at the reached points | non-unitary at all 132 (\|L\| from 0.25 to 9.0; e.g. m412 0.414, t06828 9.01 and 0.34, o10_150688 0.687, o10_150725 3.99 and 0.25): **Theorem B closes all 132** |
| unitary-but-not-fourth-root (Theorem C) or surviving points | 0 and 0 |
| not reached on the coarse path | 34 meridian cases; on the fine real path (steps of 1/64 in p from p = 3, the original triangulation, deterministic): **all 34 degenerate before the point**, \|Re H(λ)\| monotone increasing on the approach (34 of 34) to 10.2–27.0 at the last non-degenerate step; the wall within 1/16 of p = 1 (cone angle π) on **23**, within 1/16 of p = 3/2 (cone angle 2π/3) on **11** (o10_150684 c1, o10_150688 c0, o10_150689 c0, o10_150708 c0, o10_150710 c0, o10_150713 c0, o10_150714 c0, o10_150716 c0, o10_150723 c1, o10_150724 c0, o10_150725 c1); converged 0, survivors 0 |

## 2. What it means

1. **Door 2 stays shut along the geometric path.** The cone-manifold deformations of the hyperbolic structure never pass through a point
   with both peripheral eigenvalues of order dividing 4: where one curve reaches cone angle π the other is loxodromic, and often the
   structure degenerates first. The generic expectation of B1372 §4.3 is confirmed on every free cusp of the family.
2. **The residual is now off the real path.** A geometric component is a complex curve; its fibre over M = ±i may contain finite points the
   real cone path does not visit, and the character variety may have other components (as m004's does not, being a two-bridge knot with an
   irreducible Riley polynomial). Deciding those needs the A-polynomial or a full solution of the Ptolemy variety of ten-tetrahedron
   manifolds — Magma or Sage, and the Ptolemy database does not reach these members (checked for t06828).
3. **Ideal points at angle π and 2π/3.** At an ideal point of the real path the meridian's eigenvalue stays finite while the longitude's
   goes to infinity, so the meridian is a boundary slope of an essential surface (Culler–Shalen); the wall at cone angle 2π/3 on eleven
   pairs — the meridian's eigenvalue e^{iπ/3} there — and at π on the other twenty-three is a fact about these members' slopes, recorded but
   not pursued. On the two-cusped m412 and on o10_150685/o10_150693 the volume also collapses toward zero at the π wall.

## 3. Caveats

1. Numerical: SnapPy's Newton continuation; "reached" means the filled curve's holonomy equals iπ to 10⁻⁶ with a non-degenerate solution
   type (positively or negatively oriented tetrahedra); "degenerates" means the solution type turns degenerate on the fine path with
   the other holonomy's real part monotone increasing over the last eight non-degenerate steps. Whether the wall sits exactly at the
   rational angle or a hair before it is not decided (the last steps are 1/64 apart); either way the real path reaches no representation
   with eigenvalue ±i on the meridian in those 34 cases.
2. The fine path is deterministic (the original triangulation only). SnapPy's `randomize()` is seeded by the wall clock, so results on
   randomised triangulations are not reproducible; an earlier draft of this arc used them and its 30/4 split of the same 34 pairs
   drifted between runs — that split is withdrawn, the classification above replaces it.
3. Only the free cusps are examined (door 2 needs a free cusp for the abelian Higgs field to be non-zero, B1372 §3).

## 4. Registered

Door 2's residual restated: order-4 non-unitary points off the real cone path or on other components of the character varieties of the 35
free-cusp members; instrument named (the A-polynomial or the full Ptolemy solution, or a complex continuation around the ideal points).
Nothing else new.

## Verification

`verification/order4_points.py` (seconds, deterministic; two runs diff-identical): the free cusps by peripheral rank (as B1369),
continuation on each curve, classification of the other holonomy, the fine-path resolution of the failures on the original
triangulation. Lock: `tests/test_b1373_the_order_4_points_on_the_geometric_components.py`.

**Sources.** B1372 (Theorems B and C), B1369 (the free cusps), SnapPy's Dehn filling with real coefficients (cone-manifolds), the
Ptolemy module (database coverage checked).
