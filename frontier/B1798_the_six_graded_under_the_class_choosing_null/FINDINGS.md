# B1798 — THE SIX GRADED UNDER THE CLASS-CHOOSING NULL (R71-1; P-381, P-384): NEITHER B1753 NOR B1749 IS PASSED. THE CLASS-CHOOSING NULL ALONE GIVES B1753 m·r = 0.0084–0.0088 (m = 39–41), BUT THE LEPTON FACTOR c = 3 WAS CHOSEN ON THE SAME SIX NUMBERS AND THAT NULL HOLDS IT FIXED. A NULL THAT LETS EACH RANDOM TARGET CHOOSE c AS THE DATA DID GIVES ABOUT 4× THE RATE (m·r 0.035–0.079); COUNTED PER DECISIVE CELL, THE LOOKS ALSO EXCEED THE BREAK-EVEN

**Verdict: NEGATIVE** for "B1753 (or B1749) is PASSED under THE_BAR". The regrade's computation is verified on main and
reproduced by the referee. cc (main), 2026-10-28, Review 71's R71-1.
- The computation is a background agent's draft, run under `DESIGN.md`, which was written before any computation.
- Main verified it (§ 3).
- The hostile referee overturned the grade the draft proposed (§ 4).
- No grade was banked before the referee.

**0 of 19.**

## 1. What was owed

**The two arcs.** B1749 (sealed; 16 of 80 000 random hierarchies as good) and B1753 (sealed; 7 of 80 000, on the lines whose
order is divisible by 5) were left ungraded at Review 70.

**What THE_BAR requires.** Its rule of 2026-10-27 (P-389): a null must repeat "every free direction, reading, line class,
extremum and tie rule". Every variant examined outside the calibration counts as a look.

**What blocked the grade.** B1753's line class was chosen on the same data. Its committed census holds only its 48 lines,
so a class-choosing null could not be computed from it.

## 2. The class-choosing regrade (`DESIGN.md`; `verification/`)

**B1753's census completed:** its 223 apexes × the other 218 lines (48 614 points). It was computed with B1726's sealed
`compute()` through B1753's own `point()`, giving every (apex, line) pair exactly once (59 318). The extension is stored
as `b1753_all266/*.jsonl.gz`, with the raw sha256 in `RAW_SHA256.txt`.

**The data on the new lines** (post hoc, read once): the best line outside the five-ality class gives 120.8. So the
class-choosing statistic equals the minimum over all 266 lines, for any covering family of classes, on the null side as on
the data side.

**The null:**
- fresh seeds 5001–7500, 10⁷ random hierarchies (B1741's draws);
- B1741's seat-menu measure (c ∈ {1, 3}, four readings, both horocycles);
- a KD screen with margin 0.5, and B1741's arithmetic for every decision.

| arc | data | hits / 10⁷ | r (exact 97.5%) | m·r | break-even m |
|---|---|---|---|---|---|
| B1753 (223 apexes × 266 lines) | 2.739 | 2 058 | 2.149 × 10⁻⁴ | 0.0084 (m 39), 0.0088 (41), 0.0110 (51) | 46.5 |
| B1749 (125 apexes × 266 lines) | 3.574 | 2 749 | 2.854 × 10⁻⁴ | 0.0094 (33), 0.00999 (35), 0.0103 (36) | 35.04 |

**The 10⁷-target refinement moves B1749.** On its sealed 80 000 targets (r 3.25 × 10⁻⁴) it failed at every m above 30. The
sealed 16 hits sat at the 11th percentile of 80 000-target blocks.

## 3. Main's verification (`verification/main/`)

1. **The analyses regenerate byte-identically** from the stored candidates (E84). Rebuilding the features from the arc's own
   files also reproduces them (§ Files).
2. **60 extension rows recompute exactly:** 40 from the main file and 20 from the tail, through B1753's `point()`; maximum
   deviation 0.
3. **Main's own seeds agree.** On 12 seeds drawn at random (48 000 targets), B1741's direct `min_chi2` gives 10 hits and
   the KD pipeline 10. Main's check compared counts. The referee's check compared membership: on 48 seeds, 46 = 46, and no
   target within the margin missing.
4. **The look count by commit time:**
   - the web seat's THE UNIFICATION-SCALE TEST (ef08144e1, 14:45 on 2026-10-24) precedes B1753's seal (20:05), which
     makes m = 41;
   - B1749's seal (14:11) precedes it, so B1749 stays at 35.

## 4. Why neither is PASSED (the referee, `verification/referee/`)

**1. The lepton factor was chosen on the same data, and the class-choosing null holds it fixed.**
- **The evidence:** the web seat's GJ_FINDINGS says "The Clebsch 3 was chosen knowing the data's R2 = 3.14", after a scan
  of c ∈ {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}. Its ledger row says the scan informed c = 3 in every later test that uses it.
- **Why the null misses it:** the seat menu repeats only c ∈ {1, 3}. Review 70 counted the scan only for the web seat's
  tests. So for B1753 the choice of c is neither repeated nor priced.
- **A null that repeats it** (the referee's `cnull.py`; seeds 5001–5400, 1.6 × 10⁶ targets; its seat-menu control
  reproduces the 10⁷ run's rate):

  | c in the null | B1753 m·r (m = 41) | B1749 m·r (m = 35) |
  |---|---|---|
  | the scan's nine values | 0.037 | 0.041 |
  | {1/3, 1/2, 1, 2, 3, 4, 5} | 0.028–0.036 | about 0.03 |
  | continuous in [1/3, 5] (the data then reach 2.61 and 3.18) | 0.079 | 0.082 |

  Each is 3.8–8× above THE_BAR.
- **Pricing it in m instead** — the scan, three reading/Clebsch scans, B1735's change of statistic, and S215's order read
  below — gives m ≈ 47 for B1753, which fails (0.0101).

**2. The look count's convention is contested.**
- Review 70 counts each sealed test once (36).
- Main's preregistrations before B1753 carry about 47 separately calibrated decisive cells, e.g. B1741's P2, P2c and R2–R5.
- B1753's own referee completed the count at m ≈ 51–52, splitting the multi-look rows, and the SM seat's W157 cites the
  same.
- P-389 says "every variant examined outside that calibration counts".
- At 51 B1753 gives 0.0110, which fails. Any split count above 46.5 fails.

**3. Two adaptive steps not in the ledger:**
- **S215's synthesis** (e8ffd3888, 10:13 on 2026-10-24, before both seals): "the six fit specifically only on order-5 and
  order-10 lines". That is B1753's class, and its own FINDINGS names the omission. It makes m ≥ 42.
- **B1735's χ²_six statistic and its bar,** which B1749's decisive cell uses. Counting it puts B1749 at 36, which fails
  (0.0103).

**4. An opportunity that cannot be priced from the committed censuses:** the apex band Im τ ∈ [2.0, 3.6]. It was introduced
by B1748 after B1741's rows below the bar sat at Im τ 2.95–3.05.

**What stands, and what it means:**
- **The class-choosing computation stands.** It shows that the line-class choice costs B1753 little. The class-choosing
  rarity is 2 × 10⁻⁴, about four times the sealed class's 5.6 × 10⁻⁵ on fresh targets.
- **The lepton factor costs it about four times.** The six's specificity in this frame depends on c = 3 having been read
  from the data. That is consistent with main's ledger, where c is an input not derived (B1789, B1793).
- **B1753 would pass only with c held fixed and the looks counted per test.** Neither holds under THE_BAR as written.
- **The record's frame reaches the six with inputs set by hand and selected by the data,** at a rarity of order 10⁻³ once
  those selections are repeated. Its structure is real, but not rare enough after the look-elsewhere correction to grade.
- **No input removed. 0 of 19.**

## Disclosed

- **The computation is a background agent's.** Its long runs (the census extension, the 10⁷-target null) were checked by
  sample, seed and an independent referee, not rerun in full by main.
- **Both extension runs were stopped by hand** once the files covered every task. The broken-pipe tracebacks are from the
  killed workers. Every line parses, there is one writer per file, and the coverage is exact.
- **An interim null on a partial census** (`b1753_part`) was run at 04:53. Its outputs do not survive, and the record does
  not show whether it was read. The final numbers come from the full census and the full null.
- **feat_null.py and analyse.py were edited at 04:53,** after the first B1749 analysis was read at 04:28. B1749's
  regenerated output is byte-identical.
- **DESIGN.md's precedence rests on file times:** written 04:16:23, first output 04:18:33. It was not committed before the
  run.
- **The repository path.** The agent's and the checks' scripts named it absolutely. In the arc each is derived from the
  file's location; nothing else was changed.
- **The proposed grade** — the draft's "B1753 meets PASSED", to be held for the third opinion — was overturned by the hostile
  referee before any banking. The third opinion is no longer needed for a grade.
- **B1786's m at its seal** also omitted THE UNIFICATION-SCALE TEST and should be at least 43. Its grade (not PASSED) is
  unchanged.

## Seen first

`VERDICT topic-sweep /class.choosing|THE_BAR|PASSED|Bonferroni|look count|LOOK_LEDGER|B1749|B1753|R71-1|P-381|P-384/ (full text): 145 of 1544 arcs on main match (NEGATIVE 28, OPEN 9, PROVED 108); 24 register rows match (DECLINED 1, DONE 16, QUEUED 7)`.
- **Bearing on it:**
  - B1735, B1741, B1748, B1749, B1753 (its referee's m ≈ 51–52);
  - B1786 (the class-choosing null's first use);
  - B1789 and B1793 (c not derived);
  - Review 70's count (docs/LOOK_LEDGER.md);
  - THE_BAR's P-389 rule.
- **The web seat's GJ_FINDINGS and TWO_INGREDIENTS_RULE** (its branch, `relays/chat1_2026-10-22_selection_map/`).
- **Literature:** the look-elsewhere effect and Bonferroni's bound (standard); the Clopper–Pearson interval (exact binomial); THE_BAR's own sources (B1518, B1524).

## Files

- `DESIGN.md`: the agent's, written before any computation.
- **The census extension:**
  - `verification/census_ext.py` and `census_ext_tail.py` → `b1753_all266/census_ext.jsonl.gz` and
    `census_ext_tail.jsonl.gz`, with their run logs (paths redacted) and `RAW_SHA256.txt`;
  - `coverage.py`.
- **The null:**
  - `verification/feat_null.py` (`prep`, `valid`, `null`) → `kd_b1749_5001_7500.npz`, `kd_b1753_all_5001_7500.npz`,
    `null_*_run.txt`, `valid_*.txt`, `prep_b1753_all.txt`;
  - `analyse.py` → `analysis_*.txt`;
  - `crosscheck.py` → `cross_b1749.txt`.
- **To regenerate:** `gunzip -k b1753_all266/*.gz`, then `python3 -B feat_null.py prep b1749`, `prep b1753_all`, then
  `analyse.py`. Done once from the arc's own files, the outputs are identical.
- `verification/main/`: main's checks.
- `verification/referee/`: `cnull.py` (the c-choosing null), `direct_null.py`, `menu_null.py`, `check_census.py`, and their
  outputs.

The lock: `tests/test_b1798_the_six_graded_under_the_class_choosing_null.py`.
