# B99 — the SL(3) trace-map Jacobian at the GEOMETRIC representation (Probe 1c)

**Status: `computer-assisted`.** Strengthens B98 (Probe 1) to SL(3). Neutral low-dim topology; the
3d-3d / Daly framework is **cited**, not claimed. No Origin-core claim; proven core P1–P16 untouched.
Script `probe.py`; test `tests/test_b99_geometric_jacobian_sl3.py`.

## The computation
The SL(3) geometric rep is `Sym²` of the SL(2) geometric figure-eight rep, on the V0 component (B71). The
SL(3) figure-eight trace map `T₁` acts on the 8 trace coordinates; at the geometric `Sym²` point
`c₀=sym2_groundtruth_coords(x_geom)`, `x_geom=(3+√−3)/2`:

```
   char(D T₁²)|_geom = (t−1)² · [ 3 reciprocal pairs (t²−cᵢ t+1) ],   cᵢ = μ+1/μ ∈ {5,  4.5±4.664 i}
```
- **2 eigenvalues `=1`** — tangent to the 2-dimensional fixed component V0.
- **6 transverse eigenvalues** in 3 reciprocal pairs (product 1). One pair has `c=5` — exactly the
  **SL(2) torsion pair** `(5±√21)/2` (B98), carried up by `Sym²`; the other two are complex.

## Verdict (with B98)
This is **not** the trivial-point Dickson SL(3) tower `char(M⁻¹)char(M²)char(M³)(t−1)(t+1)`, whose
pair-sums are the *real* `c∈{−1,3,4}`. So at SL(3) too, **the geometric rep carries a torsion-type
(twisted-Alexander) spectrum, not the tower** — the SL(2) torsion pair `c=5` reappears at SL(3) via `Sym²`.
Together with B98: the Dickson **tower is a trivial-rep phenomenon** (SL(2) and SL(3)), while the
**geometric rep carries the adjoint-torsion / twisted-Alexander spectrum** — *consistent with* Daly
(arXiv:2411.04431) and the 3d-3d framework (cited, not claimed). The two trace-map fixed points are
genuinely different objects, which is precisely why Task T degenerated at the trivial rep.

## Scope (honest)
SL(3), numerical (finite-difference Jacobian at the exact geometric `Sym²` point; deterministic). The two
complex pair-sums `4.5±4.664 i` are the `Sym²`-deformation eigenvalues; their exact algebraic form is not
pursued here (the decisive point is "torsion-type, not tower"). The connection to Daly / 3d-3d is a
citation; the match is *consistent with* the published results, not a new claim.

```bash
python frontier/B99_geometric_jacobian_sl3/probe.py
python -m pytest tests/test_b99_geometric_jacobian_sl3.py -q
```
No physics claim; proven core P1–P16 untouched; outreach dormant.
