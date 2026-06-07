# B123 — m=1 arithmeticity (a third independent selection criterion)

The figure-eight (golden, m=1) is **arithmetic** — regular ideal triangulation, shape `z₀=e^{iπ/3}` (6th root,
`z²−z+1=Φ₆`), trace field `ℚ(√−3)` — and by Reid (1991) the *unique* arithmetic knot, so m≥2 are not. A third
independent reason m=1 is special (alongside the systole, B92, and the expansion threshold, P004): the figure-eight
is the unique metallic manifold that is both **simplest** and **most regular**. No physics; no `CLAIMS.md`; the
`ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`figure_eight_shape_is_cyclotomic()`** — `z²−z+1=Φ₆`, `z₀=e^{iπ/3}` (primitive 6th root); trace field
    `ℚ(√−3)` (arithmetic, Reid 1991). **Computed in-house.**
  - **`order6_echo_at_geometric_cusp()`** — the `(0,0,0)` Jacobian (B122) = 6th roots at **κ=−2** (the geometric
    cusp, B69/B109), same `ℚ(√−3)` as the shape. **OBSERVATION, not a connection.**
  - **`third_selection_criterion()`** — the three independent criteria; **SUPPORTED** (shape computed + Reid cited;
    the m≥2 SnapPy trace-field computation is the named confirmation — **not** TESTED-POSITIVE).
  - **`det_minus_one_is_b121()`** — the det=−1 middle eigenvalue is the proved B121 parity (cross-ref, not a kill).
- **`FINDINGS.md`** — the three criteria, the honest status split, the echo-as-observation.

**Result.** A genuine arithmetic-geometry fact banked at honest strength: m=1 is arithmetic (`ℚ(√−3)`, computed
shape + Reid), m≥2 are not (Reid; SnapPy confirmation named). The order-6 echo at the geometric cusp is recorded as
an observation. Nothing lowers the wall.

```bash
python frontier/B123_arithmeticity_m1/probe.py
python -m pytest tests/test_b123_arithmeticity_m1.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
