# B83 — the SL(n) figure-eight Dehn-filling A-polynomial family (Phase A)

The peripheral eigenvalue A-variety of the principal Dehn-filling component: **`L = (−1)ⁿ⁻¹ Mⁿ`**.

- **`probe.py`** — co-diagonalizes the meridian `μ=A⁻¹t` and longitude `[A,B]` on the SL(3)/SL(4)
  principal Dehn-filling reps (reusing B71/B73), and confirms each `(M,L)` eigenvalue pair satisfies
  `L=(−1)ⁿ⁻¹Mⁿ`.
- **`FINDINGS.md`** — the family + the mechanism.

**Result.** The figure-eight Dehn-filling A-polynomial family **`Aₙ: L=(−1)ⁿ⁻¹Mⁿ`** (`n≥3`): `n=3` →
`L=+M³` (Falbel, B71), **`n=4` → `L=−M⁴` (NEW — the first SL(4) figure-eight A-polynomial from the trace
map)**, `n=5` → `L=+M⁵` (predicted). SL(2) is degenerate (no Dehn-filling component). The exponent =
rank = the principal component's filling slope (the mechanism); the sign is fixed by `det`; the meridian
eigenvalues are generic. `j=1728` belongs to the m-axis (V53), not this n-axis.

```bash
python frontier/B83_sln_apolynomial/probe.py
python -m pytest tests/test_b83_sln_apolynomial.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
