# B115 — higher-rank + higher-genus generality of degree=rank (exploratory scoping)

How far do degree=rank (`L=c·Mⁿ`) and the off-locus sector generalize? Two honest scopings. NO physics; no
`CLAIMS.md`; P1–P16 untouched.

- **`sl4_dehn_filling_on_forced_locus()` (#5)** — the known SL(4) Dehn-filling reps (B106) are **on the forced
  locus** `tr A = tr A⁻¹` (like SL(3), B110), so off-locus SL(4) content is in **uncomputed** components.
  **Obstruction:** no SL(4) figure-eight character-variety classification exists (the SL(3) one is HMP
  1505.04451) → genuinely open.
- **`genus2_scope()` (#4 / Task 6)** — degree=rank is established for the genus-1 metallic family (B71/B83/B89);
  **genus-2** needs a genus-2 SL(n) character-variety construction not in the repo. **Obstruction:** the genus-2
  peripheral structure (the longitude is no longer the single commutator `[A,B]`). Scoped open.

**Result.** Both generalizations are scoped **OPEN** with their specific obstructions named; the established
result remains the genus-1 metallic-family degree=rank.

```bash
python frontier/B115_higher_generality/probe.py
python -m pytest tests/test_b115_higher_generality.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
