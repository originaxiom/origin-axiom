# B126 — the ladder to physics: how far does the metallic rigidity propagate?

A foundational-question investigation (direct computation + a five-agent literature fleet). **Answer:** the metallic
object's rigidity propagates **exactly two floors, provably**, then hits a *nameable* wall.

`probe.py` verifies the two in-house facts:
- **(A)** `H₁(M_m) = ℤ ⊕ (ℤ/m)²` — the metallic `m` is the *order of the homology torsion* (Smith normal form of
  `M_m²−I = m·M_m`; SnapPy-confirmed `m=1..7`).
- **(B)** the **arithmetic ⟺ A-poly-simplicity** correlation: `κ`-degree over `ℚ(z)` on the geometric component =
  `[1,1,3,3,7,6]` (`m=1..6`); rational exactly for the arithmetic members `m=1,2`. **Family-specific, not a law.**

`FINDINGS.md` carries the **ladder map**: Floor 1 (arithmetic → quantization field; *proven* for our family, Yoon
arXiv:2110.11003), Floor 2 (Mostow → no marginal couplings; `M` selects the SUSY phase; Gang–Yonekura arXiv:1803.04009 (2007.01532 mis-attach fixed, B127)),
the **wall** (3d→4d = data of the 2d *boundary*, not `M`; SUSY scale orthogonal; ceiling N=4 SYM / N=2\*).

```
python frontier/B126_ladder_to_physics/probe.py
python -m pytest tests/test_b126_ladder_to_physics.py -q
```

The SnapPy homology cross-check **skips** when SnapPy is absent (the SNF proof + the κ-pattern always run).

**Tier.** MATH / number-theory. The physics *readings* are firewalled: `speculations/S029` (the `H₁`-torsion →
center-symmetry reading, POSTULATED, fenced with kill conditions), `philosophy/P007` (the reframe), and the
five-agent citation map `speculations/LADDER_LITERATURE.md`. Nothing to `CLAIMS.md`; P1–P16 and the functorial
`Sym(W)→trace-ring` wall untouched. Ledger **V115**.
