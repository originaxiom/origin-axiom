# B78 — the n=5 degree=rank test (Phase 1b)

Does a principal SL(5) Dehn-filling component give `M⁵=L` with `c=+1` (the third point of the
`[A,B]=(−1)ⁿ⁻¹μⁿ` sign law, B77)?

- **`probe.py`** — an **n-generic** figure-eight Dehn-filling rep finder (`A²B,AB`; `μ=A⁻¹t`), validated
  to reproduce n=3 (`M³`, `c=+1`) and n=4 (`M⁴`, `c=−1`); then the n=5 irreducibility check.
- **`FINDINGS.md`** — the honest method-limit.

**Outcome.** The finder is **validated** at n=3,4. At **n=5**, across the natural finite-order spectra,
the bundle condition is solvable to machine precision but yields **only reducible reps** (~100
converged, 0 irreducible per spectrum) — the irreducible principal Dehn-filling rep is **not
numerically locatable** via `least_squares` (the documented SL(5) rank-loss/gauge difficulty, B61–B66).
**The decisive n=5 point is OPEN** (neither confirmed nor refuted); it needs the symbolic SL(5)
trace-map (B71-style, 24 coords) or a continuation rep-finder. degree=rank stays confirmed at n=3,4.

```bash
python frontier/B78_degree_rank_n5/probe.py
python -m pytest tests/test_b78_degree_rank_n5.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
