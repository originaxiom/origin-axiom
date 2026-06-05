# B88 — the SL(4) Dehn-filling census (Task 2)

Which degrees appear at rank 4? Sweep finite-order A-spectra, find the clean Dehn-filling components.

- **`probe.py`** — realizes SL(4) bundle reps (reuse B73) on candidate spectra and records the clean
  degree `k` in `[A,B]=c·μᵏ`, with a non-component control.
- **`FINDINGS.md`** — the census + two clarifications.

**Result.** Exactly **two** clean Dehn-filling components over the searched finite-order spectra:
`{1,1,ω,ω²}` (tr=1) → **`M⁴=L`** (degree 4 = rank, principal, `c=−1`) and `{prim 8th roots}` (tr=0) →
**`M³=L`** (degree 3). So **degrees {3,4} at rank 4** — consistent with "rank `n` exposes degrees ~3..n".
**Clarifications:** the *degree* is the invariant (the scalar `c` is a root of unity only on the
principal `{det μ=1}` component); and **not every irreducible bundle rep is on a Dehn-filling component**
(some spectra give reps with no clean relation). Completeness needs the symbolic `Fix(T_1²)` (Task 1a).

```bash
python frontier/B88_sl4_census/probe.py
python -m pytest tests/test_b88_sl4_census.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
