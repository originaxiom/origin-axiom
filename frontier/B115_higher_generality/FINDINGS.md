# B115 — higher-rank + higher-genus generality of degree=rank (exploratory scoping)

**Status: `exploratory` / `scoped-open`.** Two questions about how far degree=rank (`L = c·Mⁿ`) and the off-locus
sector generalize — each an **honest scoping**: a tractable computed piece + the specific obstruction for the
rest. NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched. Script `probe.py`; test
`tests/test_b115_higher_generality.py`.

## #5 — the off-locus sector at SL(4)
B110 proved the off-locus sector is **empty for 4₁ at SL(3)** (all three irreducible components lie *on* the
forced locus `tr A = tr A⁻¹`). **Computed here:** the two known **SL(4) Dehn-filling reps** (B106 principal
`{1,1,ω,ω²}`, secondary the 8th roots) are **also on the forced locus** (`tr A = tr A⁻¹`: principal `1=1`,
secondary `0=0`). So — exactly as at SL(3) — the **known** SL(4) components are forced-locus; any off-locus SL(4)
content lives in **other, uncomputed components**. **Obstruction (OPEN):** there is **no SL(4) figure-eight
character-variety classification** (the SL(3) one is Heusener–Muñoz–Porti arXiv:1505.04451; no SL(4) analogue
exists in the literature), so whether off-locus SL(4) components *exist* is genuinely uncomputed.

## #4 — genus-2 generality (Task 6 / B91)
degree=rank `L = c·Mⁿ` is a **peripheral property of the once-punctured-torus (genus 1, `F₂`)** bundle,
**established** for the whole metallic family (`L = (−1)^{n−1} Mⁿ`, all `m`, B71/B83/B89). **Genus-2 generality**
asks whether the analogous relation holds for a **genus-2** surface bundle (`F₄`, a richer peripheral structure).
**Obstruction (OPEN):** this needs a **genus-2 SL(n) character-variety construction not in the repo** (the
trace-map machinery here is `F₂` / once-punctured-torus specific); the genus-2 peripheral structure has more
boundary curves and the longitude is no longer the single commutator `[A,B]`, so degree=rank's "`L` = power of
`M`" presumes the genus-1 meridian=monodromy / longitude=single-puncture pairing. Scoped as a future probe with
this obstruction named.

## Verdict
The known SL(4) Dehn-filling reps are **forced-locus** (like SL(3)); **off-locus SL(4)** and **genus-2
degree=rank** both need machinery not in the repo and are scoped **OPEN** with their specific obstructions named
(the missing SL(4) classification; the genus-2 peripheral structure). The established result remains the genus-1
metallic-family degree=rank (B71/B83/B89).

```bash
python frontier/B115_higher_generality/probe.py
python -m pytest tests/test_b115_higher_generality.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
