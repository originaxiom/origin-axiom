# B98 — the trace-map Jacobian at the GEOMETRIC representation (Probe 1)

The handoff's #1 priority: compute the Jacobian spectrum at the *geometric* rep (the hyperbolic holonomy),
not the trivial fixed line where the tower lives and Task T degenerated.

- **`probe.py`** — the figure-eight `char(D T₁²)` on the geometric component V0; the geometric fixed point
  `x_geom=(3+√−3)/2 ∈ ℚ(√−3)` (the trace field); `char|_geom = (t−1)(t²−5t+1)`, whose transverse pair gives
  the **adjoint torsion `τ=−3`** (= `τ₁`, Porti / Daly). Plus Probe 5b (tower ≠ Kostant branching).
- **`FINDINGS.md`** — the result, the literature citations, the honest scope.

**Result (`computer-assisted`, exact SL(2)).** **The Dickson tower does not appear at the geometric rep —
it is a trivial-rep phenomenon.** At the geometric rep the monodromy Jacobian gives the **adjoint-torsion
/ twisted-Alexander** object (`t²−5t+1`, `τ=−3`), *consistent with* Daly (arXiv:2411.04431) and the 3d-3d
framework (DGG; Terashima–Yamazaki; Gang et al.) — a **citation**, not our claim. The two fixed points
carry different invariants (trivial → tower; geometric → torsion), which explains Task T's degeneration.
And Probe 5b: the tower is **not** the Kostant even-only `Sym^{2k}` branching.

```bash
python frontier/B98_geometric_jacobian/probe.py
python -m pytest tests/test_b98_geometric_jacobian.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
