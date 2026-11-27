# SM-C24 — the whole instrument at order 30: where the cusp sees the 5-part, all aligned, the line's 12 classes

*The SM seat, 2026-11-25. Card `relays/cards/SM_C24_the-whole-instrument-at-order-30.md`, pushed with its script
before the run. Data-free. Main's frame (B1945's `parts`, `U_of`) is used unchanged and read as B1977 reads it.
Run: `relays/sm_c24/c24_run.txt` and `c24_results.json`. Post hoc, disclosed: `posthoc_k0_diagnosis_run.txt` and
`posthoc_split_by_a_run.txt` in the same folder.*

## What is read

By SM-C23, one point's rates over every cusp are the rates at ∞ of every point of its level. At order 30 that is all
576 points of exact order 30, taken here as 288 pairs ±v. B1976 to B1979 read 96 of them, the act's line.

## Result against the sealed expectations

| | expectation (prior) | outcome |
|---|---|---|
| E1 | under half aligned and hierarchical; all 48 on the line are (55%) | **fails the other way:** 282 of 288 |
| E2 | 40–50 rates within 3e-3 of 1/60; ≥ 95% keep class (75%) | **fails:** 8.2e-3; 242 of 288 keep it |
| E3 | more than 12 classes (80%) | **holds:** 27 |
| E4 | v and −v equal within 1e-6 (95%) | **holds:** 1.2e-7 |
| K0 | the end moved by 0.05 moves no rate by over 1e-3 (75%) | **fails:** up to 0.117 |

E1 in full: 288 of 288 hierarchical in both quark sectors, 282 of 288 also aligned, 48 of 48 on the act's line.

## Where the failures live (post hoc, from the sealed run's own rows and one diagnostic run)

- **Every failure sits on the 48 pairs whose first coordinate a has no 5-part:** a ∈ {0, 1/6, 1/3, 1/2, 2/3, 5/6}. These
  are the points whose order-5 part lies along the real direction, so the cusp at ∞ does not see it.
  - The six unaligned pairs all have a = 1/2.
  - Of the 46 pairs that change class between 30–40 and 40–50, all 46 are among these 48; only 2 of the 48 keep it.
  - K0's movement is at one point of its twelve, (0, 1/30): its m₁/m₃ rates move by up to 0.12. The other eleven, all
    with a 5-part, do not move by 1e-3. No channel of the coupling switches on or off.
- **The 240 pairs whose a has a 5-part are clean:**
  - all 240 aligned and hierarchical in both quark sectors;
  - every rate within 1.2e-4 of the grid of 1/60, and all 240 keep their class;
  - **exactly 12 classes, the same 12 as on the act's line, each 5 times as often** (line sizes 6, 6, 6, 6, 4, 4, 3, 3,
    3, 3, 2, 2 per pair, which doubled are B1979's 12, 12, 12, 12, 8, 8, 6, 6, 6, 6, 4, 4).

## Reading

- **The act's line was not a biased hole.** On the cusps that see the 5-part, which are five-sixths of the instrument,
  the whole level plays the act's line's twelve classes in the same proportions. B1979's menu of 12, with its sizes, is
  the level's own, and needs no chosen point.
- **Alignment and hierarchy are the level's property there,** at every one of the 480 points, not the act's.
- **The remaining sixth, the cusps that do not see the 5-part, is not yet read.** Its rates have not converged by
  height 50, and at a = 0 they depend on the end above Im τ = 6, which B1927's table freezes. Reading it needs the end
  computed above 6, then larger heights.
- **For main:** K0's sample suggests the frozen end does not move rates at points with a 5-part, which includes all of
  B1976 to B1979's points. It does at a = 0. Twelve points were sampled; this is not a proof for the 96.
- No value of the 19 is computed or compared.
