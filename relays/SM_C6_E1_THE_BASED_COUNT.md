# SM-C6 E1 — the based count: what the instrument of L241 (b) reads at the two steps where the order is dropped

*Step card `relays/cards/SM_C6_E1_the-based-count.md`, pushed before the run. SM-C5's entry E1, for GENESIS FK12 (i).
It uses B1438's own exact slopes, from main at f503b1f38, and is data-free. Run: `relays/sm_c6/run_e1.py` →
`relays/sm_c6/e1_results.json`; log `relays/sm_c6/RUN_e1.txt`.*

## The outcome: 1, as predicted, with two deviations and one failed plant, all said below

1. **The pieces' order is kept by the based count, and the class count loses it on the (1, 1) modules.**
   - On 18 of 24 census levels, some sector modules count 1 in both orders: n(V) = n(V*) = 1.
   - There the class index reads I = 0, and the based count reads that each order fires.
   - Among the modules where some order fires, these are between 1.6% and 33% (100% on +LLLR 1, which has two
     modules).
   - The census's (1, 0) and (0, 1) together reproduce B1434/B1438's "firing" counts exactly (for example 72, 488 and
     2 200 on +LR levels 3 to 5). So the instrument agrees with the record where the record looked, and adds the
     (1, 1) column, which no census on main holds.
2. **The letters' order is visible in coordinates and dropped at the manifold.** For every word whose reverse is not a
   rotation of it, at lengths 6 and 7 (three pairs, both signs, level 1):
   - the based-count function, labelled by the word's own coordinates, differs between the word and its reverse
     (6 of 6);
   - the census and the slopes, as multisets, are the same (6 of 6).

   That is exactly where B1456 puts the drop.
3. **What this says for GENESIS FK12 (i).**
   - **Two different orders are dropped at two different steps.** The letters' order goes at the manifold. The
     pieces' order survives the manifold, in the based count, and is lost only to the class count, and only on the
     (1, 1) modules.
   - **So no class invariant keeps the register of the pieces, and a based instrument does.** That is outcome 1 of
     SM-C5's entry: the register is a marking, and it must come from outside the class invariants, or from a relation
     (GENESIS FK12 (iii), SM-C5's E3).

## The census of the based count (n(V), n(V*)) on B1438's levels

| state | level | N | modules | (0,0) | (1,0) | (0,1) | (1,1) | (1,1) among firing |
|---|---|---|---|---|---|---|---|---|
| +LR | 1 | 1 | 0 | 0 | 0 | 0 | 0 | - |
| +LR | 2 | 5 | 12 | 4 | 4 | 4 | 0 | 0.0% |
| +LR | 3 | 4 | 210 | 108 | 36 | 36 | 30 | 29.4% |
| +LR | 4 | 15 | 1892 | 1396 | 244 | 244 | 8 | 1.6% |
| +LR | 5 | 11 | 14280 | 11900 | 1100 | 1100 | 180 | 7.6% |
| -LR | 1 | 5 | 12 | 4 | 4 | 4 | 0 | 0.0% |
| -LR | 2 | 5 | 12 | 4 | 4 | 4 | 0 | 0.0% |
| -LR | 3 | 10 | 342 | 208 | 64 | 64 | 6 | 4.5% |
| -LR | 4 | 15 | 1892 | 1396 | 244 | 244 | 8 | 1.6% |
| -LR | 5 | 25 | 15252 | 13044 | 1044 | 1044 | 120 | 5.4% |
| +LLR | 1 | 2 | 0 | 0 | 0 | 0 | 0 | - |
| +LLR | 2 | 6 | 110 | 76 | 16 | 16 | 2 | 5.9% |
| +LLR | 3 | 10 | 2352 | 1812 | 228 | 228 | 84 | 15.6% |
| +LLR | 4 | 24 | 36290 | 31796 | 2096 | 2096 | 302 | 6.7% |
| -LLR | 1 | 6 | 20 | 14 | 2 | 2 | 2 | 33.3% |
| -LLR | 2 | 6 | 110 | 76 | 16 | 16 | 2 | 5.9% |
| -LLR | 3 | 18 | 2756 | 2288 | 224 | 224 | 20 | 4.3% |
| -LLR | 4 | 24 | 36290 | 31796 | 2096 | 2096 | 302 | 6.7% |
| +LLLR | 1 | 3 | 2 | 0 | 0 | 0 | 2 | 100.0% |
| +LLLR | 2 | 21 | 380 | 294 | 42 | 42 | 2 | 2.3% |
| +LLLR | 3 | 18 | 11342 | 9534 | 786 | 786 | 236 | 13.1% |
| -LLLR | 1 | 7 | 30 | 18 | 6 | 6 | 0 | 0.0% |
| -LLLR | 2 | 21 | 380 | 294 | 42 | 42 | 2 | 2.3% |
| -LLLR | 3 | 28 | 12210 | 10764 | 708 | 708 | 30 | 2.1% |

The counts of (1, 0) and (0, 1) are equal on every level, because duality V ↦ V* exchanges them.

## Deviations, a failed plant, and what is owed

- **Level 2 was not run.** The card said levels 1 and 2. At level 2 these words have torsion N = 221 (cyclotomic
  degree 192), and exact arithmetic there is out of reach in this session. All 12 level-2 entries are listed as
  skipped in the results. The word step rests on level 1 only.
- **The 12 word pairs are 6.** A deduplication slip listed each pair in both orders. The page counts 6 distinct tests
  (3 pairs, 2 signs).
- **Plant P2 failed as designed (0 of 8).**
  - It paired each word with "an unrelated word of the same length". Every such word in this short list is the
    *mirror image* of another (swap L and R, then reverse). Mirror images share a census, so the plant could not
    fire.
  - **Post hoc, labelled as such** (`relays/sm_c6/posthoc_p2.py` → `relays/sm_c6/posthoc_p2.json`): four
    genuinely unrelated pairs, neither reverse nor mirror, both signs. The census and the slope multiset differ on
    8 of 8.
  - Their moduli N also differ, so this control is weaker than one at equal N would be.
- **Plant P1 held:** with the slope of α replaced by that of β, the census changes on 21 of 24 levels.
- **Owed, not done here:**
  - the read-out step on the whole (B1881, B1895);
  - the audit lane's criterion, re-derived on main;
  - level 2 of the word pairs.
