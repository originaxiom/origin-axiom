# B110 — the off-locus irreducible sector of 4₁ at SL(3) (Task 3 / S011)

Is there a genuinely irreducible figure-eight SL(3) rep **off** the forced locus `tr A = tr A⁻¹` / `tr B = tr B⁻¹`
— the place S011 hoped independent (non-principal) content might live? NO physics; no `CLAIMS.md` promotion;
P1–P16 untouched.

- **`probe.py`**
  - **`components_on_forced_locus()`** — V0 (`x1=x4, x2=x5`), W1 (`x1=x4=1`), W2 (`x2=x5=1`) each lie **on** the
    forced locus.
  - **`off_locus_search()`** — an exhaustive grid over `V0 ∪ W1 ∪ W2` (= `Fix(T₁²)` = HMP's 3 irreducibles) finds
    **zero** points with `x1≠x4` AND `x2≠x5`.
  - **`verdict()`** — off-locus **empty for 4₁ at SL(3)**; scope note.
- **`FINDINGS.md`** — the table, the HMP citation, the honest scope.

**Result.** The figure-eight `SL(3,ℂ)` variety has exactly **three irreducible components** (Heusener–Muñoz–Porti
arXiv:1505.04451 = B71's V0, W1, W2), all **on** the forced locus — so the **off-locus sector is EMPTY for 4₁ at
SL(3)** (a clean negative). **Honest scope:** the broader S011 fork — off-principal multichannel content at
**higher rank** or for **other manifolds** — stays **OPEN**; it is just not in 4₁ at SL(3).

```bash
python frontier/B110_off_locus_sector/probe.py
python -m pytest tests/test_b110_off_locus_sector.py -q
```
No physics claim; proven core P1–P16 untouched.
