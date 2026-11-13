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
- **Owed, not done here:** *(all three done on 2026-11-13; see the next section)*
  - the read-out step on the whole (B1881, B1895);
  - the audit lane's criterion, re-derived on main;
  - level 2 of the word pairs.

## The owed steps, done (2026-11-13)

*Under the same card. Main at b1bcc7f50. No new card was needed: each step is one the card named. One change of
method (level 2) and one wording finding (step 4) are said below. Nothing was compared with a measured value. No height
value of the read-out is written anywhere.*

**Level 2 of the word pairs: outcome 1 holds there too.**
- **Files:** `relays/sm_c6/run_e1_level2.py`, `relays/sm_c6/e1_level2_results.json` and
  `relays/sm_c6/RUN_e1_level2.txt`.
- **The change of method.** The slopes are B1438's, line by line, but computed in F_p for two primes p ≡ 1 mod N,
  not exactly in ℚ(ζ_N). The map ℤ[ζ_N][1/d] → F_p keeps equal slopes equal. Two slopes are called equal only when
  they are equal mod both primes.
- **The check, before any level-2 number was read.**
  - At level 1, every slope mod p equals B1438's exact slope reduced mod p, for both primes.
  - The level-1 results reproduce this page's results exactly.
  - The two primes give the same slope classes everywhere.
- **The results** (N = 221 for the length-6 pair, N = 198 for the two length-7 pairs; 220 and 395 characters):
  - the labelled count differs on 6 of 6 tests (3 pairs, 2 signs);
  - the census is the same on 6 of 6.
- **The plant.** P1 changes the census on 12 of 12 entries.

**Step 3, the read-out on the whole: the heights drop the letters' order; the mark keeps it.**
- **Files:** `relays/sm_c6/run_e1_readout.py`, `relays/sm_c6/e1_readout_results.json` and
  `relays/sm_c6/RUN_e1_readout.txt`.
- **The instrument is main's own** (B1881's whole_and_value_on_main.py), imported unchanged from main's checkout.
- **The heights.** On all 16 275 run sequences of length 2, 4 and 6 with runs up to 5, a word and its reverse read the
  same heights, so the same apex.
  - This holds by construction: the height reads forward and backward symmetrically.
  - The plant, a read-out weighted to the forward reading, tells 13 860 words from their reverse.
- **The mark.** Whether a word keeps the mark's line is not invariant under reversal.
  - On 3 372 of the 16 275 sequences it differs.
  - Up to the rotations that keep the letters, some rotation keeps the line for a word but not for its reverse, or the
    other way, in 1 456 of 5 575 classes.
  - Keeping the line also depends on the starting run: it is constant over the rotations of only 10 931 of the
    16 275 sequences.
- **B1895's identity, seen again.** The seat's test and main's second test agree on all 16 275 sequences.
- **The pieces' order.** Every function of the read-out takes a run sequence only. No module and no count enters, so
  the pieces' order has no way in.
- **So:** the read-out repeats the pattern of step 1. The letters' order is visible through the mark, which is a
  marking and an input, and dropped by what is read unmarked. The pieces' order does not reach the read-out as
  instrumented.

**Step 4, the audit lane's criterion: sufficient, and exact in a narrower form.**
- **Files:** `relays/sm_c6/run_e1_criterion.py`, `relays/sm_c6/e1_criterion_results.json` and
  `relays/sm_c6/RUN_e1_criterion.txt`.
- **The criterion** (AR1, in B1457's harvest): along a surjection q, an update descends if q-equal states stay
  q-equal under it, and an output descends if it is constant on q's fibres. Both together preserve every finite
  future observation.
- **The lemma, checked exhaustively on 91 840 systems with their quotients** (up to 4 states with one update, or 3
  states with two updates, and a binary output):
  - **It is sufficient.** If every update and the output descend, every finite future observation descends, on all
    of them.
  - **The exact condition is narrower.** Every observation descends exactly when q's fibres lie inside the classes of
    observational equivalence, the largest bisimulation. This also holds on all 91 840.
  - **"Exactly when" fails as main's leads page words it.** The page says "the register survives exactly when both
    the updates and the declared outputs descend". On 8 664 systems every observation descends while an update does
    not.
  - **The smallest case:** 3 states, update (0, 0, 1), output constant, q merging states 0 and 2.
  - **What to correct.** AR1 itself claims only sufficiency. The paraphrase in main's leads page should read "when"
    or name the bisimulation condition. This is for main's word.
- **At the word → manifold step** (B1456's quotient: rotations and the reverse):
  - the update "append a letter" descends, on every word up to length 10 (4 052 tests);
  - the census descends on 12 of 12 tests at levels 1 and 2;
  - the labelled count descends on 0 of 12.
  - So the letters' order is lost at the manifold to every unlabelled output, while the act itself does not need it.
- **At the module → vacuum step** (forgetting which piece is the sub):
  - the fibre of V(ℓ, α) is {V(ℓ, α), V(1/ℓ, β)}, and E2 found that the second swaps (n, n*) on every level;
  - so the based count descends exactly on its n = n* modules: 118 164 of 136 176 on the census levels;
  - it does not descend on 18 012, the modules with I ≠ 0. There the pieces' order is lost at the vacuum, as B1438 and
    B1455 say.
