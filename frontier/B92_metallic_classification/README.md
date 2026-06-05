# B92 — the metallic family as a classification (Paper 0, Layer 1)

Characterizes the metallic family by a condition (`m` free) instead of choosing the seed.

- **`probe.py`** — three equivalent forms (self-reference `x=m+1/x` / CF `[m;m,…]` / Möbius `M_m`); the
  census `det=−1 ⟺ purely-periodic-period-1` (entries ≤5); **MyCalc-2** (CF-period a conjugacy invariant;
  det=−1 ⇒ one class per trace `m` = the companion); **refinement (a)** (the naive premises admit det=+1);
  **MyCalc-5** (systole — `m=1` minimal, the member is contingent on a metric).
- **`FINDINGS.md`** — the classification, the census, the honest scope.

**Result (`proven`, computer-assisted).** The metallic family `{M_m : m≥1}` up to `GL(2,ℤ)` conjugacy is
exactly the `det=−1` / period-1 slice; `m` is free; the member `m=1` (golden) is distinguished only by a
metric (the systole). The bridge `det=−1 ⟺ the tower's parity` is B93; universality is B94.

The motivation (why the family, not the seed) lives in `paths/philosophical/METALLIC_FOUNDATIONS.md` and
is never used in the mathematics.

```bash
python frontier/B92_metallic_classification/probe.py
python -m pytest tests/test_b92_metallic_classification.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
