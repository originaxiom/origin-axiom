# B125 — SnapPy arithmeticity of the metallic `R^m L^m` bundles

**Overturns K009.** Arithmeticity does *not* uniquely select `m=1`; it selects **{m=1 golden `ℚ(√−3)`, m=2 silver
`ℚ(i)`}** and kills `m≥3`. The B123 audit flagged exactly this gap (Reid 1991 is about *knots*; the `m≥2` metallic
manifolds are *bundles*). The two arithmetic fields are distinct → not commensurable → two genuinely distinct
arithmetic metallic manifolds (the "exactly two arithmetic punctured-torus bundles" K009 already cited).

`probe.py`:
- **the spine** (pure numpy): `M_m² = R^m L^m`, `tr = m²+2` — the orientable metallic members are the `R^m L^m`
  once-punctured-torus bundles (`m=1` = the figure-eight).
- **the verdict record** (SnapPy 3.3.2 + cypari, verified in-sandbox) + a **live recomputation** guarded on SnapPy
  being importable (shape field via Neumann–Reid; degree + imaginary-quadratic test).

Run:

```
pip install snappy --break-system-packages          # SnapPy 3.3.2 + cypari 2.5.6 (in-sandbox)
python frontier/B125_snappy_arithmeticity/probe.py   # spine always; live recompute if SnapPy present
python -m pytest tests/test_b125_snappy_arithmeticity.py -q
```

The test recomputes live when SnapPy is available and **skips** the live part otherwise (so the suite stays green on
machines without SnapPy); the spine + the recorded verdict always run.

**Scope.** MATH tier only; physics POSTULATED/quarantined, untouched; nothing to `CLAIMS.md`; `P1–P16` untouched; the
functorial `Sym(W)→trace-ring` wall is not touched. Honest: the two arithmetic verdicts + the non-arithmetic verdict
(`m≥3` not imaginary quadratic) are robust; the *exact* `m≥3` field degrees are precision-sensitive and not
over-claimed. See `FINDINGS.md`; ledger **V114**. Status **TESTED-POSITIVE** (the SnapPy gate is lifted).
