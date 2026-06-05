# B79 — the two-parameter (m,n) degree table (Phase 1c)

The degree table `d(m,n)` for degree=rank (`[A,B]=(−1)ⁿ⁻¹μⁿ`, B77).

- **`probe.py`** — tabulates the computed cells (all `= rank`) and the open cells, with a live
  re-confirmation of `d(3,3)=3`.
- **`FINDINGS.md`** — the table + the honest opens.

**Result.** Every **computed** cell has `d = rank`: `d(1,3)=d(3,3)=3`, `d(1,4)=4`. The **even-m**
(`d(2,3)`) and **rank-4 metallic** (`d(2,4),d(3,4)`) cells are **open** — the Dehn-filling reps elude
`least_squares` across odd-order (B75), broad (B78), and even-order (B79) finite-order spectra (same
rep-search fragility as the SL(5) wall in B78 / the gauge-corruption in B81). No cell contradicts
`d=rank`; closing the open cells needs the symbolic trace-map fixed-locus (B71-style) per cell.

```bash
python frontier/B79_mn_table/probe.py
python -m pytest tests/test_b79_mn_table.py -q
```

No Origin-core claim; proven core P1–P16 untouched.
