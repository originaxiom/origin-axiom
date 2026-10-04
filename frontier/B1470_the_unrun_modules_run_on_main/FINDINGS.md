# B1470 — THE UNRUN MODULES RUN ON MAIN: B1418's 3 325 modules of t12835 completed with the budget lifted, no three anywhere, the lane's table confirmed row by row

**Verdict: NEGATIVE** (the completion carries no three; scope: frame F-CI's one-cusped index I = t₀ − r₁ of B1418 on
t12835's reducible non-split locus over ℚ(ζ₁₂), m ≤ 3, every twist of the record's set; reach *single* — one manifold,
one field, one instrument). cc (main), 2026-10-04. Pays L222 (iii) and the first entry of L245 (xB031).

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "t12835|3 325|unrun modules|NOT RUN|budget"`: *VERDICT topic-sweep: 34 of 1342 arcs on main match (NEGATIVE 10, OPEN 5, PROVED 19)*. Read:
  B1418 (the family as the object; its table row for t12835: 3 110 modules run, 3 325 NOT RUN on the 1 800 s budget,
  |I| = 2 at m = 3 at four order-signatures, "NOT RUN is never folded into zero"), L222 (iii) ("the single most
  informative unrun computation in the record"), and the sep16 lane's xB031 at `3205984b` (B1418's instrument, byte-copied,
  with the budget removed: 6 435 run, no 3; and an X3 at m = 4, 5, 6 saying the index dies by m = 6 — read, not re-run
  here). **Literature:** none; the instrument is the record's.

## 1. What was run

`c2_run.run('t12835', K = ℚ(ζ₁₂), S = μ₁₂, m ∈ {1, 2, 3}, budget 10⁷ s)` — B1418's own driver, imported from its
directory, nothing changed but the budget — on main, 4 234 s. **6 435 modules, 0 NOT RUN.** Index multiset: 0 × 6 003,
−1 × 252, +1 × 156, −2 × 24; by m: m = 1 {0: 1989, −1: 102, +1: 54}, m = 2 {0: 1893, −1: 150, +1: 102}, m = 3
{0: 2121, −2: 24}. **Max |I| = 2; no 3.**

## 2. Against the record and the lane (`compare.py`)

- **B1418's 3 110 banked rows: 3 110 of 3 110 agree** (the same instrument, so a reproduction, as it should be).
- **The 3 325 formerly NOT RUN:** 3 070 zero, 150 at −1, 90 at +1, 15 at −2 — the pattern of the run half, no new value.
- **The sep16 lane's xB031 table (6 435 rows): 6 435 of 6 435 agree, key by key.** The lane's X2 claim ("completing the
  3 325 produced no 3") is confirmed on main; its X3 (m = 4, 5, 6: the index dies) is the lane's, read.

## 3. What it means

L222 (iii) is paid: the one unrun computation the record kept pointing at holds no three. The index on t12835 reaches
|I| = 2 at m = 3 and nowhere higher at m ≤ 3; B1427's bound |I| ≤ ⌊rank/2⌋ (B1440) is not touched. The same instrument
on both benches means this is a completeness and numbers check, not an independent route; an independent route would be
the index by `index_num` on the same modules in the fibred presentation (owed if anyone needs it). **The imported
expectation, stated separately:** none. Nothing selects a state. **0 of 19.**

## 4. Errors in this arc

None found. Seventy minutes of compute were spent on the half of a table that a budget had cut in September; the record
should prefer "run to completion overnight" to "NOT RUN, honestly labelled" when the population is this size.
