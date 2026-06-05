# B77 — the degree=rank mechanism (Phase 1a)

What is the precise degree=rank relation, and is it the geometric shadow of the Dickson tower's top
factor `char(Mⁿ)` (the A↔D unification hypothesis)?

- **`probe.py`** — on the principal Dehn-filling reps (SL(3) `{1,i,−i}`, SL(4) `{1,1,ω,ω²}`), computes
  the scalar `c` in `[A,B]=c·μⁿ` (meridian `μ=A⁻¹t`) and the spread of `eig(μ)` across reps.
- **`FINDINGS.md`** — the two findings.

**Result.** (1) **Refined law:** `[A,B] = (−1)ⁿ⁻¹·μⁿ` — `c=+1` at n=3, `c=−1` at n=4 (scalar-dev
~1e-10…1e-14); `c` is forced to an `n`-th root of unity by determinants. Prediction for n=5: `c=+1`.
(2) **Unification REFUTED:** the meridian/longitude eigenvalues are generic and vary across the
component — *not* the fixed Dickson `char(Mⁿ)` roots. degree=rank is a **peripheral** identity, a
different object from the trace-ring Jacobian spectrum; the sign `(−1)ⁿ⁻¹` echoes the tower's parity but
is not an eigenvalue match.

```bash
python frontier/B77_degree_rank_mechanism/probe.py
python -m pytest tests/test_b77_degree_rank_mechanism.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
