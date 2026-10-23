# ZERO_FREE_HOLOMORPHIC, the result: on 23 940 new points beside the zero-free census's, the selected Higgs fits the pattern (six 1.67, nine 2.19, F_6 on the tick's line (2/5, 4/5)) but not specifically (3.4% and 1.05% against 1%); Z7 fails (S̃ is 3% better on the six, S 1.6 times better on the nine); over all lines main's ∂R read S̃ fits better and is specific; the menu's best line is again the tick's, by 2–4%

chat1, 2026-10-23. **SEALED; the cells as the rule states them; the read-outs after them labelled.** Rule
`ZERO_FREE_HOLOMORPHIC_RULE.md` (38e2b8062, committed and pushed before the script existed); script and comparison
76775054a (committed before the run); controls e00b0c682 (read when the run wrote them, before their commit; they read no
target), with C2′'s script (committed before its run) and its output 323867b0c (committed before it was read);
disclosures 9c8a9cbf6, before any output was read; a written prediction for a post hoc check, 31242d039, written while the
run was in progress, before its output was combined, committed or read (its own wording, "committed before the output it
concerns exists", is too strong: the chunks holding the tick's lines, 8–11 of 120, were on disk from early in the first
launch, unread); output f921f7253 and comparison output c8de16a57, each committed before
it was read (the comparison's printout was redirected unread); the prediction's check 5a8c874ea, committed before it was
read; post hoc read-outs `zero_free_holomorphic_posthoc.py` (62da3c665; output 5cccf8bfd) and, after the referee's report,
`zero_free_holomorphic_posthoc2.py` (1ad8f64c6; output 5d1fd99e2), each committed before its run and its output before it
was read. Refereed read-only before it left. 0 of 19.

## The question (from the rule)

Do three principles on record — PF1-W on the Higgs (a reading), holomorphy (W135) and three generations with one unit —
select a Higgs and a reading that do main's frame's work on points nobody had computed, with only the lepton factor by
hand? The menu they fix: F_6 (r = 12), F_−2 and F_22 (r = 20), read through S in every sector, c = 3. The grid: Re τ ∈
{0.15, 0.30, …, 0.90}, Im τ 2.05–3.45, B1713's 266 lines of order 1–12, both horocycles; 23 940 points, 143 640 menu rows.

## The cells

| cell | statement | prior | result |
| --- | --- | --- | --- |
| Z1 | six within 2.0 at the menu's best row | 70% | **holds:** 1.668 (F_6 at 0.45 + 2.35i on (2/5, 4/5), L_2) |
| Z2 | six specific, ≤ 1% (mean of 20 seeds) | 45% | **fails:** 3.38% (2.9–3.8%) |
| Z3 | nine within 2.5 | 65% | **holds:** 2.192 (F_6 at 0.45 + 2.25i on (2/5, 4/5), L_2) |
| Z4 | nine specific, ≤ 1% | 40% | **fails:** 1.05% (0.78–1.30%) |
| Z5 | D within 3σ of P-094 at the best six-row | 5% | **fails, as expected:** D = 9.000 (R2 = R1 = 3.000) |
| Z6 | \|J\| within a factor 3 of 3.08 × 10⁻⁵ at the best nine-row | 10% | **fails, as expected:** 4.2 × 10⁻⁷ |
| Z7 | S beats S̃ on both the six and the nine | 85% | **fails:** S̃ gives 1.622 (six, lower than S's 1.668) and 3.509 (nine, higher than S's 2.192) |
| Z8 | the best six-row's line has α = 2/5 | 75% | **holds:** (2/5, 4/5) |
| C1 | the instrument | 95% | holds (2.5 × 10⁻¹⁴) |
| C2 | T-covariance at the first grid point | 95% | **failed as written** (3.4 × 10⁻¹³ in the ratios, 1.9 in \|V\|): that point lies on the trivial line (0, 0), where V = 1 and \|V\| is rounding noise. Resolved before any output was read (9c8a9cbf6): C2′, at three non-trivial grid points for the four directions, holds to 1.1 × 10⁻¹⁰ |

**By the rule's own reading of this outcome** (fixed before the run):
- "Z1 and Z3 hold, Z2 or Z4 fails. The selected Higgs fits, but not specifically at this menu." Both Z2 and Z4 fail:
  Z2 clearly (no seed at or below 1%), Z4 narrowly (1.05% against 1%; 8 of 20 seeds at or below 1%).
- "Z7 fails. Holomorphy does not pick the reading the data want."
- Z5 and Z6 fail as expected (d = e on the order-5 line; the CKM phase open).
- The positive branch — the three principles select a Higgs and reading that do the frame's work, so that the sealed
  census's reading rule I2 is derived rather than chosen — does not apply. Nothing here derives any of the nineteen.

## The read-outs computed with the cells (sealed read-outs, not cells)

- **Per direction.** F_6 carries the menu's best rows. F_22: six 1.691 (0.75 + 2.75i on (2/5, 4/5), L_2), nine 2.428
  ((2/5, 1/2), L_max). F_−2 misses (129).
- **Z7's two halves.** S̃ gives the lower six (by 3%), S the lower nine (by a factor 1.6). S̃'s best six-row is F_6 at
  0.45 + 3.05i on (1/4, 3/8), L_max, where |V_cb| and |V_ub| are 0.003 and 0.006 of measured; S's is on (2/5, 4/5).
- **c = 1:** six 2.171, nine 2.428 (D = 1). The six needs the hand-set c = 3 to come within 2.0.
- **The reference, main's ∂R read S̃ with c = 3** (the sealed census's model) on the same points: six 1.434 at 0.78%,
  nine 1.899 at 0.29%, both on (2/5, 1/2) near 0.45 + 2.6i (L_2), D = 13.4 at its best six-row, J = 4.0 × 10⁻⁶ at its
  best nine-row. Over all lines it does better than the menu on both, and is specific on both. Without the factor
  (c = 1): 2.40 at 20.3%, 3.09 at 8.8%.
- **Model over measured.** At the best six-row: m_c/m_t 1.67, m_u/m_t 1.33, m_s/m_b 1.27, m_d/m_b 0.83, m_μ/m_τ 1.21,
  m_e/m_τ 0.93; |V_us| 0.43, |V_cb| 0.83, |V_ub| 1.02. At the best nine-row: 2.19, 1.43, 1.46, 1.20, 1.39, 1.34; 0.47,
  0.92, 1.29.

## The written prediction (31242d039; a post hoc check, not a cell)

`line_selection_control.py holo` on this output:
- **(2/5, 4/5), the tick's line, ranks 1st of 266 for both the six (1.668) and the nine (2.192).** The tick's other
  α = 2/5 line, (2/5, 1/5), ranks 7th on both; its α = 1/5 lines rank 134th–172nd.
- The prediction — one of the tick's α = 2/5 lines is the best for the six, and one for the nine (priors 45% and 40%) —
  **holds on both.**
- **What it is worth.** The margins are small: for the six the runners-up are (2/5, 1/10) at 1.702 and (2/5, 1/2) at
  1.711 (2% and 3% worse); for the nine, (2/5, 1/2) at 2.281 (4% worse). This grid and the census scan the same 266
  lines at points 0.05 apart, and this grid's best rows are 0.07 from the census's (F_6 at 0.4 + 2.4i and 0.4 + 2.3i on
  (2/5, 4/5), L_2), so the two rank-1s are not independent: the check confirms the census's rank 1 by continuity. Four
  lines drawn at random include the best with probability 1.5%, but that is not the chance that matters: the nine best
  lines for the six and the ten best for the nine all have α = 2/5 (as Z8 expected), two of those ten are the tick's,
  and the prediction was drawn from the census.

## Post hoc read-outs (labelled)

- **P1, precision** (PRECISION_BAR.md's χ², sealed after this rule, so a read-out here). The menu: min χ²_six 36.5 and
  min χ²_nine 112.7, both at the best six-row, against 16.75 and 21.67. The reference: 22.4 and 100.7. Neither the menu
  nor the reference matches the values. (Main's ∂R in its split reading reaches χ²_six 3.8 on this grid, with a best nine
  of 22 over the grid and 23.9 at that row; `relays/chat1_2026-10-23_framing/framing_readouts.json` and
  `framing_readouts2.json`.)
- **P2, the tick's lines alone** (written after the sealed cells were read, with Z2 and Z4 failing and the best rows on
  (2/5, 4/5); `zero_free_holomorphic_posthoc.py` and `_posthoc2.py`):
  - the menu on the tick's four lines (360 points, 2 160 rows): six 1.668 at 0.28%, nine 2.192 at 0.14% — the same best
    rows on 66.5 times fewer rows;
  - **four lines that contain the best line give fractions as low or lower:** (2/5, 4/5) with three random others,
    median 0.25% and 0.09% (200 draws; middle half 0.20–0.33% and 0.07–0.11%). Four lines built on a runner-up instead,
    (2/5, 1/10) or (2/5, 1/2), give 0.36% and 0.16–0.29%, and the ten α = 2/5 lines 0.44% and 0.29%: higher than the
    tick's four, still below 1%. P2 restates the rank-1 result; it is not specificity of its own;
  - TICK_LINE_HIGGS sampled these lines more densely: every point here on the tick's lines is 0.035 from one of its
    points. Here the values are worse (1.668, 2.192) and come from F_6; F_22, its best direction, gives nine 2.63 here.
    A continuity check, not a replication;
  - the reference on its own best four lines ((2/5, 1/2), (2/5, 1/10), (2/5, 9/10), (2/5, 7/10), chosen on this grid by its
    best six):
    0.07% and 0.05%; on the tick's four, which are not its best, it fits worse (2.66 at 3.0%, 3.18 at 1.5%; 3.49 on
    (2/5, 4/5)).
- **F_6 alone** (a direction chosen after seeing the results): 2.5% and 0.73% on all lines. It has the reference's row
  count (47 880) and is still less specific (0.78%, 0.29%), so the row count is part of the gap, not all of it: at the
  same best rows, a third of the rows lowers 3.4% to 2.5% and 1.05% to 0.73%; the rest is the reference's better fit.
- **P3, CP.** No row that fits the nine within 3 has |J| within a factor 3 of 3.08 × 10⁻⁵:
  - the menu: 66 such rows, the largest |J| 6.5 × 10⁻⁶ (13 rows within 2.5: at most 2.8 × 10⁻⁶);
  - the reference: 23 rows, at most 7.05 × 10⁻⁶;
  - J is small where the nine fits, not everywhere: 20 913 of the menu's 143 640 rows and 7 916 of the reference's
    47 880 have |J| within a factor 3 of 3.08 × 10⁻⁵, but the best nine among them is 5.09 and 4.51
    (`framing_readouts.json`, F1).
  TICK_LINE_HIGGS's menu rows with nine ≤ 4 (at most 2.1 × 10⁻⁶, `tick_line_cp.json`) and RIGID_TAU_HOLOMORPHIC's
  family-A menu rows with nine ≤ 5 (at most 1.4 × 10⁻⁶) do not reach it either. Across the day's four scans and four
  models, no row with nine ≤ 3 has |J| within a factor 3 (`framing_readouts.json`, F1; the closest is 4.4 times too
  small). The cut matters: with nine ≤ 5, this grid's reference reaches 1.26 × 10⁻⁵ and the census's menu 1.27 × 10⁻⁵.

## What it shows, and what it does not

- **The selection, as far as it goes.** The principles fix a menu that reaches main's frame's pattern on new points
  beside the census's best rows, with its best rows on the tick's line. Over all 266 lines it is not specific (Z2, Z4).
  The principles do not fix the line; the tick's line is the menu's best, by 2–3% on the six over two order-10 lines and
  4% on the nine over one, as on the census beside these points. Restricted to the tick's lines (P2) the fractions fall
  below 1%, but so they do for four lines containing the best line or a runner-up, so P2 adds nothing to the rank-1
  result.
- **Over all lines it does not beat the reference.** Main's ∂R read S̃ (not holomorphic in the Higgs; chosen by hand)
  fits both the six and the nine better and is specific (0.78%, 0.29%), on order-10 lines that no principle on record
  selects. The two prefer different lines: the menu fits the reference's best line almost as well as its own (1.711 on
  (2/5, 1/2) against 1.668), while the reference misses the menu's (3.49 on (2/5, 4/5) against 1.434).
- **Holomorphy's reading.** Z7 fails as sealed, and the rule's reading stands: holomorphy does not pick the reading the
  data want. S̃ gives the lower six (by 3%), S the lower nine (by a factor 1.6). On the census, read before the rule,
  the six went the other way (S 1.500, S̃ 1.701); each best row here is 0.07 from its census counterpart on the same line
  and horocycle, so the six's order is set at about the grid's resolution. The nine's is not: S is lower by a factor 1.6
  here and 1.67 on the census (2.297 against 3.841).
- **Values** fail for the menu and the reference (P1); **D = 9** on the tick's line (P-094 needs 10.58 ± 0.11); **J** is
  too small at every row of the day's scans that fits the nine within 3 (P3); looser fits can reach it.
- **The d = e lines.** As TICK_LINE_HIGGS noted, on the order-5 lines d = e ties the lepton ratios to the down ratios;
  part of any fit there comes from that structure and from c = 3, which was chosen to fit it.
- **Limits.**
  - The menu, its reading and c = 3 were fixed after the zero-free census (16 492 points at Re τ 0.1 and 0.4) and its
    read-out, which printed the menu's best rows (F_6 at 0.4 + 2.4i, six 1.500; 0.4 + 2.3i, nine 2.297; both on
    (2/5, 4/5), L_2). This grid avoids the census's points and B1726's but interleaves with the census's, 0.05 away in
    Re τ and Im τ; its best rows are 0.07 from the census's, on the same line and horocycle. Z1, Z3 and Z8 were tested
    beside a known optimum.
  - The calibration's nine-target stream is not main's (9c8a9cbf6).
  - TICK_LINE_HIGGS and RIGID_TAU_HOLOMORPHIC were run and read while this run was in progress (the disclosure 9c8a9cbf6
    expected this run to finish first). No cell here depends on them. The post hoc read-outs do: P1 on PRECISION_BAR, P2
    on TICK_LINE_HIGGS, P3 on `tick_line_cp.json`, `rigid_tau_posthoc.json` and `framing_readouts.json`.
  - The run took three launches (6 616 s, 6 759 s and 5 782 s, from the launch logs, which are not committed); the first
    two stopped at their time budget and were resumed; none failed.
  - PF1-W is a reading; holomorphy applies to the Higgs factor only; which menu direction is physical is not decided.

## Files

`ZERO_FREE_HOLOMORPHIC_RULE.md`, `zero_free_holomorphic_test.py`, `zero_free_holomorphic_compare.py`,
`zero_free_holomorphic_controls.json`, `zero_free_holomorphic_c2prime.py` with its JSON, `zero_free_holomorphic.npz`
with `zero_free_holomorphic_index.json`, `zero_free_holomorphic_compare.json` and `_run.txt`,
`zero_free_holomorphic_posthoc.py` and `zero_free_holomorphic_posthoc2.py` with their JSON, and the census read-out
`zero_free_readout.json`, in `relays/chat1_2026-10-23_zero_free_frame/`; the prediction and its check, `PREDICTION_BEFORE_ZERO_FREE_HOLOMORPHIC.md`,
`line_selection_control.py`, `line_selection_control_holo.json` and `line_selection_control_census.json`, with
`DISCLOSURES_BEFORE_READING.md` and `tick_line_cp.json`, in `relays/chat1_2026-10-23_tick_line/`; `PRECISION_BAR.md` and `rigid_tau_posthoc.json` in
`relays/chat1_2026-10-23_rigid_tau/`; `framing_readouts.json` and `framing_readouts2.json` in
`relays/chat1_2026-10-23_framing/`.

0 of 19.
