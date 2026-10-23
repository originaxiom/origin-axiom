# TICK_LINE_HIGGS, the result: on the tick's lines F_22, one of the zero-free holomorphic menu's three directions, fits all nine within 2.043 at its best row, with 0.11% of random targets as good; P-094 fails by construction and |J| is 15 times too small

chat1, 2026-10-23. **SEALED; the cells as the rule states them.** Rule `TICK_LINE_HIGGS_RULE.md` (e0c16e1cd, committed and
pushed before its script existed); script and comparison d860de099 (committed before the run); controls 78f27b9c0
(committed before they were read); disclosures 9c8a9cbf6 (before the comparison ran); output 908b40d1d and the
comparison's output 312c57c90 (each committed before it was read; the comparison's printout was redirected unread).
Refereed read-only twice before it left; every cell and every read-out on the tick grid was recomputed independently
by the referee. Post hoc
read-outs, labelled, are in `tick_line_readouts2.py` (33514acdd before its run; output 90b57158f before it was read).
0 of 19.

## The claim under test (from the rule)

Principles on record select every discrete datum of main's fibre frame, and the frame still fits:
- **the line, by the tick:** the order-5 lines fixed up to sign by L·R (S₁) and by R·L (S₂), main's B1698;
- **the Higgs, its twist and its reading, by PF1-W, holomorphy and three generations with one unit:** the menu F_6
  (r = 12), F_−2 and F_22 (r = 20), read through S in every sector (the sealed rule ZERO_FREE_HOLOMORPHIC).

Left free: τ and the horocycle. By hand: the lepton factor c = 3. The grid: 8 lines × 300 values of τ (Re τ
0.025–0.975, Im τ 2.025–3.425), none computed by anyone before, both horocycles; 14 400 menu rows.
- Up to the frame's symmetries the rows are fewer (post hoc, `tick_line_readouts2.py` (c)). Sign pairs (α, b) and
  (1 − α, 1 − b) agree in all 28 fields (to 3.5 × 10⁻¹⁸). S₂'s line at τ is S₁'s at τ + 1, by the T-covariance C2
  checks (recomputed at six points on (2/5, 1/5): log10 ratios to 2.3 × 10⁻⁷, the float32 storage; |V| and J not
  compared). S₁'s lines are mirror-symmetric about Re τ = ½, with J flipping sign (the other fields exactly, J to
  3.5 × 10⁻¹⁸). No cell changes.

## The cells

| cell | statement | prior | result |
| --- | --- | --- | --- |
| K1 | six within 2.0 | 70% | **holds:** 1.551 (F_22, 0.325 + 2.725i, (2/5, 4/5), L_2) |
| K2 | six specific, ≤ 1% (mean of 20 seeds) | 55% | **holds:** 0.15% (0.025–0.25%; every seed below 1%) |
| K3 | nine within 2.5 | 60% | **holds:** 2.043 (F_22, 0.825 + 2.725i, (2/5, 1/5), L_max) |
| K4 | nine specific, ≤ 1% | 50% | **holds:** 0.11% (0.025–0.20%; every seed below 1%) |
| K5 | S beats S̃ on both | 85% | **holds:** S̃ gives 6.69 and 26.9 |
| K6 | \|J\| within a factor 3 of 3.08 × 10⁻⁵ | 5% | **fails:** 2.08 × 10⁻⁶ (15 times too small) |
| K7 | best six-row on a line with α ∈ {2/5, 3/5} | 85% | **holds:** (2/5, 4/5) |
| C1 | the instrument | 95% | holds (2.5 × 10⁻¹⁴) |
| C2 | T-covariance at the first grid point | 95% | holds (24 of 24 ratios and 24 of 24 \|V\| compared; 4.1 × 10⁻¹³ and 8.0 × 10⁻¹³). The code also set aside ratios below 10⁻¹², which the rule exempts only for \|V\|; none was set aside. |

**P-094, not a cell, fixed by construction:** D = 9.0000 at the best six-row (R2 = R1 = 3.0000) and so at every row,
against 10.58 ± 0.11: 14σ at P-094's precision (Antusch, Hinze and Saad), 1.3σ with the record's own inputs (± 1.19,
HARVEST_LEDGER row 1100).

**By the rule's own reading of this outcome** (K1–K5 hold): principles on record select every discrete datum of
main's frame — the line (the tick), the Higgs, its twist and its reading (PF1-W, holomorphy, three generations with
one unit) — and the frame then fits the six and the nine specifically on points nobody had computed. What remains free
is τ and the horocycle; by hand, the lepton factor, which P-094 says cannot be 3 on these lines; and the CKM phase. A
positive at main's coarse measure; it derives none of the nineteen.

**Read literally, that says more than the cells test.** They test what the principles leave: three directions in two
twists on eight lines (four up to sign), with two horocycles. The fit then chooses F_22 (F_−2 misses by 183) and the
α = 2/5 lines (the α = 1/5 lines miss by 63–90). The horocycle is free and c = 3 is by hand. B1698 had concluded, for
∂R with main's readings, "In this frame the tick's lines do not select the line." The CKM phase is not free but
unreached (K6).

## The read-outs (not cells)

- **The best nine-row.** On S₂'s line (2/5, 1/5) (tied with its sign pair (3/5, 4/5)), at 0.825 + 2.725i in L_max,
  F_22 gives every one of the nine within a factor 2.043 (model over measured: m_c/m_t 1.70, m_u/m_t 1.64, m_s/m_b
  0.97, m_d/m_b 0.52, m_μ/m_τ 0.93, m_e/m_τ 0.59, |V_us| 0.49, |V_cb| 0.93, |V_ub| 1.16). The lepton entries are the
  down entries with c = 3 applied by hand. The best six-row (on S₁'s (2/5, 4/5)) has a nine of 3.04.
- **Per direction:** F_22 1.551 / 2.043; F_6 1.605 / 2.273 (F_6's best six- and nine-rows both on (2/5, 4/5), at
  0.375 + 2.425i and 0.475 + 2.325i, L_2); F_−2 misses (183, six and nine).
- **Per line:** S₁'s (2/5, 4/5) and (3/5, 1/5) give 1.551 / 2.273; S₂'s (2/5, 1/5) and (3/5, 4/5) give
  1.917 / 2.043. The α = 1/5 and 4/5 lines miss: six 63.5–63.6, nine 63.9 (S₂) and 90.4 (S₁). B1698's ∂R missed
  there too, by 7.9–8.8 at c = 1.
- **c = 1:** six 2.31, nine 2.72, with 2.7% / 1.0% of random targets as good (post hoc, `tick_line_readouts2.py`
  (d)). Neither meets K1's 2.0 or K3's 2.5; the fits need the hand-set c = 3.
- **Main's ∂R on the same points.**
  - With S̃ in every sector and c = 3 (the sealed census's model; 4 800 rows, one direction): six 2.48, nine 3.07,
    random as good 2.4% / 1.4%.
  - In main's split reading (up S̃, down S, leptons S) with c = 3 (post hoc, `tick_line_readouts2.py` (a)): six 1.45
    with 0.025% as good, but nine 23.6.
  - So on the tick's lines ∂R, read main's way, fits the six better than the menu does (1.45 at 0.025% against 1.551
    at 0.15%); the menu's gain is the nine, the mixing.
- **Against the record, not like for like.**
  - B1698 (∂R, main's three up readings, c = 1, Re τ ∈ {0, ½}, sealed): six 2.33, 1.7% as good (one draw of 4 000, no
    nine). At c = 1 the menu's six here is 2.31.
  - The sealed census (∂R with S̃, c = 3, 266 lines, 17 024 rows): six 1.51, nine 2.09, at 1.17% / 0.56% over seeds
    100–119 (post hoc, `chat1_2026-10-22_selection_map/seed_robustness.py`; 0.73% / 0.48% at the sealed seed 1720).
  - Here: 14 400 rows on eight lines chosen after the census. Fewer rows give a lower fraction at a given fit.

## What it does not show, and its limits

- **The hypothesis was formed after the zero-free census was seen, and its outcome was largely predictable.**
  - The tick's line was tested because F_6's best census rows lay on (2/5, 4/5). The menu and its reading (rule
    38e2b8062) were fixed after the census read-out (b10b6936f) showed the ε = +1 lines fitting with S. Both are
    disclosed in the rules.
  - The census's own rows on the four distinct tick lines (seen before the rule) already give six 1.500 and nine
    2.297, with 0.055% / 0.104% of random targets as good (post hoc, `tick_line_readouts2.py` (b)). So the census's
    own rows on these lines already met all four bars of K1–K4; the fresh grid confirms them by continuity, on lines
    chosen where the census fit.
  - The calibration counts all 14 400 menu rows, not the choice of the lines, the menu or the reading. The test
    checks the hypothesis on fresh points; it does not make it blind.
- **Fresh points, some near seen ones.** The zero-free census computed F_6 and F_22 on (2/5, 4/5) at Re τ = 0.4. The
  fresh best F_6 rows and the menu's best six-row (F_22, 0.325 + 2.725i) lie 0.035–0.079 from census points on the
  same line. The best nine-row, on S₂'s line at Re τ 0.825 (S₁'s at 1.825), lies between census points of the line:
  under T, the census's (2/5, 1/5) at 0.4 and (2/5, 3/5) at 0.1 are S₁'s line at Re τ 1.4 and 2.1, 0.275 from the
  nearer; with the mirror as well, its (2/5, 2/5) at 0.1 + 2.7i is S₁'s line at 1.9 + 2.7i, 0.079 away.
- **The measure is main's coarse one:** a worst factor of about 2 over nine quantities. Part of K2 and K4's
  specificity is c = 3 itself: the rows' lepton ratios are their down ratios × 3 and ÷ 3, while random targets' are
  independent, and 3 was chosen because the data sit near it (R2 3.14, R1 3.37; THE_SELECTION_MAP).
- **Three Higgs directions remain, in two twists.** The principles leave the menu F_6 (r = 12), F_−2 and F_22
  (r = 20); F_22 gives the best rows, F_6 nearly as good, F_−2 none. Which direction, and so which twist, is physical
  is not decided.
- **P-094 fails by construction, as known before the run.** On the tick's lines d = e exactly for every Higgs
  direction, reading, τ and horocycle (B1698 after its seal: Y_e = Y_dᵀ on order-5 lines; B1703; in the zero-free
  census the tick's four lines passed its 10⁻⁶ test for every direction and reading but F_2, where R2 is exact and
  the first generation massless, `zero_free_de_lines.py`). So R2 = R1 = c and
  D = c². With the hand-set c = 3, D = 9 against P-094's 10.58 ± 0.11; meeting it needs c ≈ 3.25, not
  Georgi–Jarlskog's 3. No Higgs on these lines can split d from e.
- **The CKM phase is not reached** (K6), and τ, the horocycle and c are not derived.
- **The principles enter main's frame as readings.** PF1-W is chat1's reading of PF1 (registered by the owner as a
  reading), and main's frame is outside it as written; the test uses its lines as Higgs directions. Holomorphy is
  applied to the Higgs factor only; the channels are not holomorphic in τ (ZERO_FREE_FRAME_EXPLORATION §6–7).
- **The calibration's nine-target stream is not main's** (DISCLOSURES_BEFORE_READING.md, item 1). The distributions and
  seed 1720 are main's; seeds 1721–1739 extend main's single draw.
- **ZERO_FREE_HOLOMORPHIC** (the same menu on all 266 lines) is still running, unread.

## Files

`TICK_LINE_HIGGS_RULE.md`, `DISCLOSURES_BEFORE_READING.md`, `tick_line_test.py`, `tick_line_compare.py`,
`tick_line_controls.json`, `tick_line.npz` with `tick_line_index.json`, `tick_line_compare.json` and
`tick_line_compare_run.txt`; post hoc: `tick_line_readouts2.py` with its JSON. In `relays/chat1_2026-10-23_tick_line/`.

0 of 19.
