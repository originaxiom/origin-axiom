# B81 — the CRT/F_p route at SL(5): blocked by gauge-corruption (precise B58/B66 localization)

Does B80's first-principles CRT/F_p route (which proved the SL(4) tower) extend to SL(5)?

- **`probe.py`** — computes `char(DT_0(n,m=1))` over F_p for several seeds and compares (the char poly
  is conjugation-invariant, so it must agree across seeds iff the pinv-limit is well-defined); tags the
  SL(5) factors.
- **`FINDINGS.md`** — the precise localization.

**Result.** **No — blocked.** SL(4)'s `char(DT_0)` is **seed-invariant** (why B80 works); SL(5)'s
**scatters** across seeds (24/25 coeffs differ) — the ε-series pinv-limit is **gauge-corrupt** at SL(5),
so m-interpolation is invalid. The corruption is the **doubly-degenerate even-k sector** (`char(M²)`
resolves at multiplicity 1 not 2, `(t+1)` at 1 not 2 — the degree-3 gap), shown to be a genuine
gauge-corruption (not a tagging artifact). The route reaches exactly the seed-canonical
(multiplicity-≤1 even-k) sectors; the multiplicity-≥2 degeneracy is the residual `e₂/Λ²` barrier (B58).
The SL(4) result (B80/V62) stands as the rank where the route succeeds.

```bash
python frontier/B81_sl5_adproof/probe.py
python -m pytest tests/test_b81_sl5_adproof.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
