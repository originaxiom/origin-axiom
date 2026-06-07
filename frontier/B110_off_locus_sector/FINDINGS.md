# B110 — the off-locus irreducible sector of 4₁ at SL(3): EMPTY (Task 3 / S011)

**Status: `computer-assisted` + literature.** Executes the CC-web "Final Computation Arc" Task 3 (speculation
**S011**'s open fork). NO physics; no `CLAIMS.md` promotion; proven core P1–P16 untouched. Script `probe.py`;
test `tests/test_b110_off_locus_sector.py`.

## The question
S011's fork: genuinely independent (non-principal) content, if any, lives in the **irreducible** reps **off** the
forced locus `tr A = tr A⁻¹` (`x1=x4`) and `tr B = tr B⁻¹` (`x2=x5`). The B106 Dehn-filling reps live **on** that
locus (their `c`-values are forced by B95), so they are *not* the fork. **Does the figure-eight have an
irreducible SL(3) rep with `x1 ≠ x4` AND `x2 ≠ x5`?**

## The answer — NO (empty for 4₁ at SL(3))
The figure-eight `SL(3,ℂ)` character variety has **exactly three irreducible components** (Heusener–Muñoz–Porti,
arXiv:1505.04451: five components total — totally reducible, partially reducible, and **three irreducible**),
which coincide with B71's `Fix(T₁²)` decomposition:

| component | locus | on the forced locus? |
|---|---|---|
| **V0** (distinguished, `Sym²: SL(2)→SL(3)`) | `{x1=x4, x2=x5}` | yes — **both** |
| **W1** (exceptional Dehn filling) | `{x1=x4=1}` | yes — in `A` |
| **W2** (exceptional Dehn filling) | `{x2=x5=1}` | yes — in `B` |

**Every irreducible component lies ON the forced locus** (`x1=x4` OR `x2=x5`; verified over several `(p,q)`
samples and an exhaustive grid search over `V0 ∪ W1 ∪ W2` — **zero** points with `x1≠x4` AND `x2≠x5`). Since these
three are *all* the irreducible reps (HMP), **there is no figure-eight SL(3) irreducible rep off the forced
locus**: the off-locus sector is **EMPTY for 4₁ at SL(3)**.

This is exactly the outcome the handoff flagged as legitimate: *"such reps may not exist… that's also a clean
result — the figure-eight at SL(3) has no genuinely non-principal content."*

## Honest scope (what stays open)
This is **specific to the figure-eight (4₁) at SL(3)**. The broader S011 fork — off-principal **multichannel**
content at **higher rank** or for **other manifolds** — is **not** settled here and stays **OPEN**. What is
settled: 4₁ at SL(3) carries no genuinely non-principal irreducible content; all its irreducibles are
forced-locus (and the tower / degree=rank / single-golden-scale picture is therefore complete for it).

## Verdict
The off-locus sector is **empty for 4₁ at SL(3)** (a clean negative, literature-confirmed). The "where independent
content could live" fork must be sought at **higher rank or other manifolds**, not in the figure-eight at SL(3) —
S011 is narrowed accordingly, its general form still open.

```bash
python frontier/B110_off_locus_sector/probe.py
python -m pytest tests/test_b110_off_locus_sector.py -q
```
No physics claim; proven core P1–P16 untouched.
