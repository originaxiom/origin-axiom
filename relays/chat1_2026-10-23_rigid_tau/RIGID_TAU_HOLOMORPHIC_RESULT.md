# RIGID_TAU_HOLOMORPHIC, the result: under B1720's apex rule the zero-free holomorphic Higgs meets the four coarse cells at c = 3 (six 1.64 at 0.69%, nine 2.26 at 0.39%), but at two different apex configurations, each CP-self-conjugate (J = 0); the six repeats the tick line's known fit, which main's ∂R also reaches; the nine is a narrow feature at Re τ = 0; no row meets both bars, and the values fail (χ² 49 and 146)

chat1, 2026-10-23. **SEALED; the cells as the rule states them; the read-outs after them labelled.** Rule
`RIGID_TAU_HOLOMORPHIC_RULE.md` with `PRECISION_BAR.md` (51b05f7c7, committed and pushed before the script existed);
script and comparison 336c71280 (committed before the run); controls 483397c30 (committed before they were read); C2′'s
script 71be76a6d and its run 66de12830; C2's resolution fff2b28dd (post hoc, labelled, before any output was read); output
0361a70aa and comparison output dc49da132, each committed before it was read (the comparison's printout was redirected
unread). The referee's points were checked by `rigid_tau_posthoc.py` (c22323656, committed before its run; output
50b92e526, committed before it was read): post hoc, labelled, not cells. Refereed read-only twice before it left; the
referees' reports are not in the repository, and every point taken from them is checked in a committed read-out or
labelled as theirs. 0 of 19.

## The question (from the rule)

Does any of the record's rigid candidates for τ — values the object fixes, tested before only with main's ∂R — place τ
for the zero-free holomorphic Higgs, with no continuous number free?
- **Family A, B1720's apex rule:** 121 thread classes, τ at each class's apex, every line the class fixes up to sign:
  3 249 points (51 heights), both horocycles, the menu F_6, F_−2, F_22 read through S, c = 3: 19 494 rows.
- **Family B, the tick's own moduli:** its cusp shape 2√3 i (B1696) and the golden word's spin end curve ½ + √3 i
  (B1702), on the tick's eight lines. (The silver word's 2i, B1702, was left out: it is not the tick's.)

The rule quoted B1720's test on these points but not chat1's own THREADS_WITH_INGREDIENTS on the same points (see the
limits).

## The cells

Lines are given in the basis of the apex as stored; moved to 0 ≤ Re τ < 1 (τ ↦ τ − n, b ↦ b + nα) they read differently
(read-out R1).

| cell | statement | prior | result |
| --- | --- | --- | --- |
| A1 | six within 2.0 | 45% | **holds:** 1.635 (F_22; L⁵R⁴'s apex 3.5 + 2.7386i, line (2/5, 3/5); L_2) |
| A2 | six specific, ≤ 1% (mean of 20 seeds) | 20% | **holds:** 0.69% (0.40–0.925%) |
| A3 | nine within 2.5 | 30% | **holds:** 2.256 (F_22; L⁴RLRLR's apex 3.0 + 2.6220i, line (2/5, 4/5); L_max) |
| A4 | nine specific, ≤ 1% | 15% | **holds:** 0.39% (0.18–0.55%) |
| A5 | χ²_six below 16.75 | 3% | **fails:** 48.9 |
| A6 | χ²_nine below 21.67 | 2% | **fails:** 145.7 |
| A7 | S beats S̃ on both | 80% | **holds:** S̃ gives 2.12 and 4.16 |
| A8 | \|J\| within a factor 3 of 3.08 × 10⁻⁵ at the best nine-row | 10% | **fails:** 3 × 10⁻¹⁹ |
| A9 | D within 3σ of P-094 at the best six-row | 8% | **fails:** D = 9.000 |
| B1 | τ = 2√3 i: six within 2.0 | 5% | **fails:** 26.6 |
| B2 | τ = ½ + √3 i: six within 2.0 | 3% | **fails:** 43.0 |
| C1 | the instrument | 95% | holds (2.5 × 10⁻¹⁴) |
| C2 | T-covariance at the first family-A point | 95% | **failed as written** (9.0 × 10⁻⁸ in the ratios, 1.4 × 10⁻⁷ in \|V\|, against 10⁻⁹); resolved post hoc as the instrument's precision at these points (`C2_RESOLUTION.md`, with its erratum; C2′ covered F_6 and ∂R only) |
| C3 | the points are B1720's | 90% | holds (B1720's stored six reproduced to 2.0 × 10⁻¹²) |

**By the rule's own reading of this outcome.** A1–A4 hold: with no continuous number free — τ at a thread's apex, the
line the thread fixes, the Higgs and its reading by PF1-W, holomorphy and three generations, the lepton factor c = 3 by
hand — main's frame meets the coarse cells for the six and for the nine. A5 and A6 fail, so it derives none of the
nineteen. B1 and B2 fail, as expected: the tick's own rigid moduli do not place τ.

**What that reading leaves out** (post hoc, after the referee; read-outs R1–R7 below). The rule's reading ("B1720's
apex rule, negative with ∂R, works with the zero-free holomorphic Higgs") says more than the cells test.
- **The six is not the menu's gain.** B1720's negative was at c = 1. On these points main's ∂R at c = 3 fits the six
  as well and as specifically: 1.614, as good as 0.24% of random targets in main's split reading (up S̃, down and
  leptons S), 0.46% with the up quarks read S or S̃. This was on record before the rule: THE_SELECTION_MAP's Clebsch
  table gives 1.61 at 0.53% for B1720's rows and readings at c = 3. On these points the menu's gain is the nine: 2.26
  at 0.39%, against ∂R's 22.2 (split), 4.71 (S in every sector, 8.9%) and 3.51 (S̃ in every sector, 4.7%).
- **The six repeats a known fit.** Moved, the best six-row is the tick's line (2/5, 4/5) at ½ + 2.7386i, 0.03 from
  TICK_LINE_HIGGS's grid points that gave 1.556, read before this rule.
- **The six and the nine are met at different apexes, and no row meets both bars.**
- **Both best rows are CP-self-conjugate**, so J vanishes there by symmetry; the nine's fit is a narrow feature at that
  symmetric point.

## The read-outs (not cells)

- **R1, where the best rows lie.** In the stored bases both lie on α = 2/5 lines of order 5 (one T-orbit). Moved to
  0 ≤ Re τ < 1, as B1698's lines and family B are read:
  - the best six-row is (2/5, 4/5) at ½ + 2.7386i (L_2): the tick's S₁ line on its mirror axis, Re τ = ½;
  - the best nine-row is (2/5, 0) at 2.6220i (L_max): Re τ = 0, not a tick line;
  - F_6's best row (L³RL²R's apex; (2/5, 0) at 2.5 + 2.2361i in `rigid_tau_compare.json`) moves to the tick's (2/5, 4/5)
    at ½ + 2.2361i.
  - Each ties with its mirror: L⁵R⁴ with L⁴R⁵, L⁴RLRLR with LRLRLR⁴, L³RL²R with LR²LR³.
  - Being order-5 lines, both give d = e exactly: D = 9.000 at the best six-row.
- **R2, main's ∂R at c = 3 on the same points** (same seeds; mean of 20, seed 1720 in brackets):

  | ∂R, c = 3 | rows | six | as good | nine | as good |
  | --- | --- | --- | --- | --- | --- |
  | split: up S̃, down and leptons S | 6 498 | 1.614 | 0.24% (0.25%) | 22.2 | 32.6% |
  | up S or S̃, down and leptons S | 12 996 | 1.614 | 0.46% (0.45%) | 4.71 | 8.9% |
  | S in every sector | 6 498 | 2.15 | 3.3% | 4.71 | 8.9% |
  | S̃ in every sector | 6 498 | 3.22 | 25.6% (26.6%) | 3.51 | 4.7% (5.1%) |

  The last row reproduces THREADS_WITH_INGREDIENTS's sealed result (rule 40079f41d, result e446c8b6d; six 3.22 at 26.6%,
  nine 3.51 at 5.1%, seed 1720). THE_SELECTION_MAP's read-out had ∂R at c = 3 on these apexes at six 1.614 and nine
  22.2 before this rule. ∂R's best six-row is at L⁵R²'s apex, moved to the same tick line at ½ + 2.958i. B1720 itself
  (∂R, three up readings, c = 1, one seed): six 1.80 at 1.65%, nine 6.51 at 39.0%.
- **R3, the menu's specificity and its model space** (20 seeds):
  - sealed (menu, S, c = 3): 0.69% and 0.39%; seed 1720 alone 0.825% and 0.325%; standard errors 0.03% and 0.02%;
  - c = 1: six 2.22 at 8.9%, nine 2.80 at 2.6% (χ²_six 145.6);
  - S and S̃ rows: 1.19% and 0.58%; menu and ∂R (split) rows: 0.82% and 0.39%; F_22 alone: 0.33% and 0.19%.
- **R4, CP.** 843 of the 3 249 family-A points are CP-self-conjugate: the configuration maps to itself under
  τ ↦ −τ̄, b ↦ −b, up to T, sign and integer shifts. At all of them |J| ≤ 1.7 × 10⁻¹² (menu, S). Both best rows are
  among them (J = 2 × 10⁻¹⁶ and 3 × 10⁻¹⁹ as stored).
  - Among the 83 menu rows with nine ≤ 5 the largest |J| is 1.4 × 10⁻⁶, 21 times too small.
  - Elsewhere CP is generally broken: the median |J| over the other points is 2.3 × 10⁻⁴ (F_22; most of them have τ off
    the CP lines).
  - For the menu read S this sharpens THE_SELECTION_MAP's remark that main's hypercharge line breaks the reflection
    (B1713: J ≠ 0 at Re τ ∈ {0, ½}): J vanishes where the configuration (τ with its line) is self-conjugate, as both best
    rows' are. ∂R and the other readings were not checked here.
- **R5, both bars.** Two rows have six ≤ 2.0 (one configuration and its mirror); four have nine ≤ 2.5 (two
  configurations, F_22's and F_6's, each with its mirror); none has both. The nine at the best six-row is 2.83; the six
  at the best nine-row is 2.17. χ²_nine at the best nine-row is 262; its minimum, 145.7, is at a third point: F_6 on
  (9/23, 2/23) at the apex of L⁴RLR², 3.1 + 2.4920i (L_2). χ²_six's minimum, 48.9, is at the best six-row.
- **R6, the six's neighbours read before.** TICK_LINE_HIGGS's grid points 0.475 and 0.525 + 2.725i on (2/5, 4/5), F_22,
  L_2, gave 1.556 (L_max: 2.31). The best nine-row's configuration, (2/5, 0) at Re τ = 0, was not read before: the
  zero-free census read Re τ = 0.1 and 0.4 only (its nearest points on (2/5, 0) are 0.1 away), and TICK_LINE_HIGGS only
  the tick's lines.
- **R7, off the symmetric points** (main's frame, recomputed at the moved configurations; the stored six and nine of the
  two rows are reproduced to 5 × 10⁻⁸ in ln):
  - the best nine-row, Re τ = 0, 0.01, 0.02, 0.05: nine 2.26, 2.27, 3.32, 7.18, its rise driven by m_u/m_t (1.78, 2.27,
    3.32, 7.18), with J 5 × 10⁻⁸, 1.0 × 10⁻⁷, 2.5 × 10⁻⁷ off the point. The narrowness and J = 0 share a cause: at the
    self-conjugate point m_u/m_t is at its lowest in the scan and J vanishes; the nine there is set by |V_ub|, m_s/m_b
    and m_c/m_t, which barely move;
  - the best six-row, Re τ = ½ to 0.55: six 1.634–1.635, nine 2.83–2.85, |J| at most 7.7 × 10⁻⁸.
- **Model over measured.** At the best six-row: m_c/m_t 1.39, m_u/m_t 0.62, m_s/m_b 0.90, m_d/m_b 0.61, m_μ/m_τ 0.86,
  m_e/m_τ 0.69 (|V_us| 0.35, |V_cb| 0.52, |V_ub| 0.58). At the best nine-row: 2.16, 1.78, 2.17, 0.85, 2.07, 0.95, and
  |V_us| 0.58, |V_cb| 1.49, |V_ub| 2.26.
- **Per direction.** F_22 carries the menu's best rows. F_6 alone: six = nine = 2.259, nearly tying the nine (2.256).
  F_−2 misses (134).
- **Family B** misses by 26.6 (2√3 i) and 43.0 (½ + √3 i), with χ²_six above 1 500.

## What it does not show, and its limits

- **Values.** χ²_six 48.9 and χ²_nine 145.7 against bars of 16.75 and 21.67 (PRECISION_BAR.md): a pattern match, not a
  match of values. At the best nine-row four quantities are off by factors above 2 (m_c/m_t, m_s/m_b, m_μ/m_τ, |V_ub|).
- **No single point.** The six and the nine are met at different apexes, lines (after moving), Re τ and horocycles,
  and no row meets both bars.
- **The CKM phase** vanishes at both best rows by symmetry, and no menu row with all nine within a factor 5 (83 rows, R4)
  comes within a factor 21 of it. **P-094** fails by construction on the order-5 lines (D = c²).
- **The nine is a narrow feature.** It meets A3's bar within 0.01 of Re τ = 0 and fails it by 0.02 (2.27 and 3.32, R7).
  Every family-A row that meets the bar is self-conjugate (J = 0); at 0.01, where the bar is still met, J is 5 × 10⁻⁸.
- **The six was close to predictable** (R6), and main's ∂R at c = 3 fits it as well and as specifically (R2).
- **c = 3 is by hand.** It is one discrete number put in because the data sit near it (the data's (m_μ/m_τ)/(m_s/m_b)
  = 3.14 and (m_d/m_b)/(m_e/m_τ) = 3.37; THE_SELECTION_MAP). Part of A2 and A4 is c = 3 itself: on the d = e lines where
  the best rows lie, the lepton ratios are the down ratios × 3 and ÷ 3, while random targets' are independent. At c = 1
  the same rows give 8.9% and 2.6%.
- **What the calibration does not count.**
  - The choices made before: the menu, its reading and c were fixed after the zero-free census; the apex rule is main's
    (B1720, sealed for ∂R), but its use with this menu was decided after TICK_LINE_HIGGS was read.
  - The earlier tests on the same 3 249 points: B1720 (∂R, c = 1, negative; quoted in the rule) and chat1's
    THREADS_WITH_INGREDIENTS (40079f41d, sealed; ∂R read S̃, c = 3), which the rule does not mention, where H1–H4 failed
    (six 3.22 at 26.6%, nine 3.51 at 5.1%). This is the third Higgs-and-reading tried on these points. A trials factor
    of 1.45 takes the six over the 1% bar; 2.6 takes the nine over.
  - The model space: admitting S̃ rows takes the six to 1.19% (R3).
  - Family A is one of the record's rigid candidates for τ; family B holds the other two (B1696 and B1702 tested those τ
    values for ∂R on other lines, not the tick's).
- **The readings' caveats carry over from TICK_LINE_HIGGS:** PF1-W is a reading; holomorphy applies to the Higgs factor
  only; which direction of the menu is physical is not decided.
- **Read after this note was drafted:** ZERO_FREE_HOLOMORPHIC (the same menu on 23 940 new points). There the menu is
  not specific (3.4%, 1.05%), and ∂R read S̃ fits both the six and the nine better (1.43 at 0.78%, 1.90 at 0.29%).
- **C2 failed as written** and was resolved post hoc (`C2_RESOLUTION.md`, with an erratum); the calibration's
  nine-target stream is not main's (as disclosed for the earlier rules).

## Files

`RIGID_TAU_HOLOMORPHIC_RULE.md`, `PRECISION_BAR.md`, `rigid_tau_test.py`, `rigid_tau_compare.py`,
`rigid_tau_controls.json`, `rigid_tau_c2prime.py` with its JSON, `C2_RESOLUTION.md`, `rigid_tau.npz` with
`rigid_tau_index.json`, `rigid_tau_compare.json` and `rigid_tau_compare_run.txt`, `rigid_tau_posthoc.py` with its JSON,
in `relays/chat1_2026-10-23_rigid_tau/`.

0 of 19.
