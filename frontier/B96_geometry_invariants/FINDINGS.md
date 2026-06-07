# B96 — geometry invariants of the metallic mapping-torus manifolds

**Status: `computer-assisted` (SnapPy 3.3.2 + mpmath).** Neutral low-dim-topology / quantum-topology
mathematics; **no physics claim** — the physics readings are quarantined in
`speculations/archive/PHYSICS_RESONANCES.md` and are not used here. No Origin-core claim; proven core
P1–P16 untouched. Script `probe.py`; test `tests/test_b96_geometry_invariants.py`.

The metallic once-punctured-torus bundle for `m` is the mapping torus of the **square** monodromy `M_m²`
(orientation-preserving, det=+1): `m=1→[[2,1],[1,1]]=4_1` (figure-eight), `m=2→[[5,2],[2,1]]=m136`,
`m=3→[[10,3],[3,1]]=s464`.

## (1) The volume ordering — strictly monotone
```
   vol₁ = 2.0298832 (4_1)  <  vol₂ = 3.6638624 (m136)  <  vol₃ = 4.8138192 (s464)
```
(SnapPy, each cross-checked to ~1e-7 by the Bloch–Wigner dilogarithm of the tetrahedron shapes.) The
metallic family's complexity ordering **continues at the third point**, monotone. The smallest-volume
member is **m=1 (figure-eight, golden)** — which coheres with B92/MyCalc-5: `m=1` is the *systole* (the
shortest geodesic on `H/GL(2,ℤ)`). Two independent simplicity measures (geodesic length, hyperbolic
volume) agree that `m=1` is the simplest member.

## (2) The volume Hessian signature — DEFINITE (the decisive computation)
At the complete hyperbolic structure the volume is a strict **maximum** over Dehn fillings (Mostow
rigidity): of **156 nontrivial fillings** of `4_1` (`|(a,b)|²≤50`), **155 are strictly below `vol₀`, 0
exceed it** (the one tie is a near-complete filling). So the **Neumann–Zagier Hessian of the volume
functional at the complete structure is negative definite — signature `(0,2)`, not indefinite.**
Furthermore the figure-eight **A-variety boundary is 1-complex-dimensional** (the eigenvalue A-variety is
the curve `L=(−1)ⁿ⁻¹Mⁿ`, B83/B71), so the boundary deformation space is **2-real-dimensional**: there is
**no canonical 4×4 boundary Hessian**, and the natural NZ Hessian is `2×2` and definite.

## (3) Honest status of the secondary quantities
- **`|τ₃|` (adjoint Reidemeister torsion of `s464`):** algebraically **branch-ambiguous** (the
  `cs_invariant_family` fixed-locus `±√` branches give `−2.64` or `−52.08`); SnapPy's exact adjoint torsion
  requires **Sage** (unavailable standalone), and a from-scratch Dimofte–Garoufalidis 1-loop invariant
  **did not calibrate** to the known `τ₁=−3, τ₂=−16` here, so it is **not reported as a number** (the
  torsion ordering is left open). The **volume** ordering (clean) is the banked complexity result.
- **Chern–Simons amplitude:** at large level the dominant saddle `∝ exp(±k·vol/2π)` is volume-controlled;
  since the volume is monotone in `m`, the extremal-weight member is `m=1` (or `m=3`, by sign convention)
  — a restatement of (1), not new data.

## Scope (honest)
Pure quantum-topology invariants (hyperbolic volume; the NZ volume Hessian). **No physics promotion.** The
decisive result is the **definite (0,2) signature** — the "Lorentzian-emergence" reading (Phase Q) is
*closed by this computation*, not by assertion. `|τ₃|` is the lone open refinement (needs Sage).

```bash
python frontier/B96_geometry_invariants/probe.py
python -m pytest tests/test_b96_geometry_invariants.py -q
```
No physics claim; proven core P1–P16 untouched; outreach dormant.
