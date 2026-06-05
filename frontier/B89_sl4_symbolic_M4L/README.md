# B89 — M⁴ = L PROVED symbolic-exact at SL(4) (Task 1a)

Upgrades V54/B73's `M⁴=L` (degree=rank on the principal `{1,1,ω,ω²}` figure-eight Dehn-filling
component) from `high-precision-numerical` (~1e-31) to a **PROVED exact identity over ℚ(ω)** — the
SL(4) analogue of B71's exact SL(3) `M³=L`.

- **`probe.py`** — the proof. Eliminating `B` collapses the bundle relations to one matrix equation
  `tA⁻²tA = A⁻¹tAt`; with `A³=I` this is a 10-equation exact ideal; the centralizer gauge + the
  rank-drop locus `t11=ω·t22` give an explicit **4-parameter family** over ℚ(ω); and
  `[A,B]·det(t)² = −det(t)·μ⁴` is checked as a **pure polynomial identity** (no division, no numerics).
- **`FINDINGS.md`** — the reduction, the family, the controls, and the honest scope.

**Result.** `[A,B] = −(1/det t)·μ⁴`, so on SL(4) (`det t=1`) **`M⁴ = L`** with `c=−1`, `c⁴=1`. The
`k=3,5` controls (`M³`, `M⁵` not scalar), the bundle relations, irreducibility, and the m=1 SL(2)
baseline are in the test.

```bash
python frontier/B89_sl4_symbolic_M4L/probe.py
python -m pytest tests/test_b89_sl4_symbolic_M4L.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
