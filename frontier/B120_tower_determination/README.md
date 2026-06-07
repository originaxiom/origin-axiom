# B120 — the trivial-point tower is determined by `(n; trace, det)`

Banks the Chat-2 exploration interlude (Q2/Q3) + the computed Supplement (S1–S5), verify-don't-trust. The tower
(the Sym two-sequence, B117/B103) is **one object** fixed by two inputs — the unfolding depth `n` and the
abelianization seed `(trace, det)`. Three of the handoff's formulas were wrong and are corrected. NO physics; no
`CLAIMS.md`; the `ρ_n` / Sym-`μ_d` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`tower_determined_by_trace_det()`** — Q3: distinct same-`(trace,det)` integer matrices → identical towers
    (n=3,4,5). The `(n; trace, det)` determination theorem.
  - **`m_universality_of_sym_content()`** — S2: the n=4 Sym content is identical for m=1,2,3; the `μ_d` are
    plethysm multiplicities of the `GL(2,ℤ)`-rep `ρ_n` (trace-blind). **Honest scope:** a reframing of the prize as
    a plethysm, **not** a closure (proved only n=3,4; same wall).
  - **`doubling_range_forced()`** — S1 (corrected): doubling-sum `= (n−4)(n+1)/2` (the handoff's `(n²−3n)/2` is off
    by 2); the band `{2..n−3}` is the unique fill ⇒ derives the two-sequence's doubling.
  - **`height_count_closed_form()`** — S3+S5 (corrected): heights run `0..n`; closed form `count(n,0)=n−1`,
    `2(n−2)` for h∈{1,2}, `2(n−h)` for 3≤h≤n−1, `2` for h=n; `Σ=n²−1`. Refutes the `2·max(1,n−h−1)` guess and the
    "no closed form" claim.
  - **`degree_rank_split()`** — Q2: (I) spectral `μ_n=1` all n / (II) geometric order `{4,3,2,∞}`, n∈{3,4}.
  - **`b116_factor_level_confirm()`** — S4: B116 is factor-level (the Chat-2 "n=3 divergence" was a units error).
- **`FINDINGS.md`** — the results + the three corrections + the honest m-universality scope.

**Result.** The tower factors as `tower(n ; trace, det)` — `n` = Sym unfolding depth, `(trace,det)` = the MCG-word
seed. degree=rank splits into (I) spectral (all n) and (II) geometric (n∈{3,4}). The prize is unchanged and
un-fused: prove the Sym two-sequence `μ_d` for all n (B103), now seen as a plethysm.

```bash
python frontier/B120_tower_determination/probe.py
python -m pytest tests/test_b120_tower_determination.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
