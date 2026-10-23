# TWO_HIGGS, the result: with two holomorphic Higgs directions from the zero-free menu (the pair chosen by the data out of six: H_u = F_6, H_d = F_22), main's frame meets the six's precision bar (H5, χ²_six 1.19; all six within 10% at the best row near 0.56 + 2.6i; with d = e and c = 3 by hand, four of the six are independent, and at the fitted best row those four quark ratios are within 1σ of their measured values, post hoc); the nine's bar fails (χ²_nine 154), so by PRECISION_BAR this is a match of the six, not of the values; the heaviest states stay aligned but the mixing is too small, D = 9 and J is too small

chat1, 2026-10-23. **SEALED; the cells as the rule states them; the read-outs after them labelled.** Rule
`TWO_HIGGS_RULE.md` (0b192e458, committed and pushed before the script existed); script and comparison 219e1bb65
(committed and pushed before the run); controls b2005340b (committed before they were read); output 158d33df5 and
comparison output aa7e2b5d2, each committed before it was read (the comparison's printout was redirected unread). Post
hoc read-outs `two_higgs_posthoc.py` (f84ec9a84; output b489138fd) and, after the referee's report,
`two_higgs_posthoc2.py` (006134efc; output 13794b4dd), each committed before its run and its output before it was read.
One code-path test of the script's `point()` ran at a stand-in point off the grid (0.3 + 2.25i on (2/5, 1/2)) before the
script's commit, printing only the shape, finiteness and time; it is disclosed in 219e1bb65. Refereed
read-only before it left. 0 of 19.

## The question (from the rule)

If S stands for the Higgs doublet, holomorphy in every sector (W135) needs two doublets: H_u for the up quarks and H_d
for the down quarks and the leptons, each with its own direction. The sealed menu tests gave both one direction. Do
independent holomorphic directions, each from the menu (F_6, F_−2, F_22), both read S, with c = 3, fit better than one
direction for both, and does any of them fit the six and the mixing at the same row? The grid: the ten α = 2/5 lines,
Re τ ∈ {0.0625, …, 0.9375} (8 values), Im τ 2.0–3.5 (16 values), both horocycles: 1 280 points, 15 360 rows for the six
off-diagonal pairs and 7 680 for the three diagonal ones.

## The cells

| cell | statement | prior | result |
| --- | --- | --- | --- |
| H1 | best off-diagonal six below the best diagonal six | 50% | **holds:** 1.099 against 1.466 |
| H2 | best off-diagonal nine below the best diagonal nine | 30% | **fails:** 2.320 against 2.010 |
| H3 | six specific on the off-diagonal rows (≤ 1%) | 25% | **holds:** 0 of 80 000 random six-target sets fit as well (below 3/80 000, about 4 × 10⁻⁵, at 95%) |
| H4 | nine specific on the off-diagonal rows (≤ 1%) | 15% | **holds:** 0.57% (0.33–0.80%) |
| H5 | some off-diagonal row with χ²_six below 16.75 | 10% | **holds:** 1.19 (F_6 \| F_22 at 0.5625 + 2.6i on (2/5, 1/10), L_2) |
| H6 | some off-diagonal row with χ²_nine below 21.67 | 3% | **fails:** 154.1 |
| H7 | at the off-diagonal best six-row the nine within 2.5 | 15% | **fails:** 5.35 |
| H8 | \|J\| within a factor 3 of 3.08 × 10⁻⁵ at the off-diagonal best nine-row | 5% | **fails:** 9.9 × 10⁻⁷ |
| C1 | each diagonal pair against the zero-free census code's S fields | 95% | holds (0.0: the same code path, so it cannot catch a swap of the sectors; P2 and the referee's independent recomputation do) |
| C2 | ∂R with S in every sector against main's TC.ratios_at | 95% | holds (2.5 × 10⁻¹⁴) |

**By the rule's own reading of this outcome** (fixed before the run):
- **H5 holds:** "a values-level match of the six (or the nine) for principled Higgs directions, with τ the only
  continuous number and c = 3 by hand; read at M_Z, with the scale caveat." PRECISION_BAR, committed before the rule,
  governs that wording (next bullet): with one bar met this is a match of the six at its precision bar. At the best row the six ratios over their measured values are
  1.010, 0.910, 0.983, 0.938, 0.938 and 1.052 (m_c/m_t, m_u/m_t, m_s/m_b, m_d/m_b, m_μ/m_τ, m_e/m_τ). H5 is the first
  sealed χ²_six cell on record to hold (main's B1698 H3 and B1720 T3, and RIGID_TAU's A5, failed).
- **PRECISION_BAR's commitment** ("no ingredient is described as reaching the values unless a sealed test finds it below
  both bars"): H6 fails (χ²_nine 154.1), so the two-doublet ingredient does not reach the values. The match is of the
  six.
- **H3 and H4 hold:** specific on its rows. On this grid the other models pass the 1% bar too (the diagonal pairs 0.14%
  and 0.13%, ∂R read S̃ 0.28% and 0.11%, ∂R split's six 0.004%), except ∂R split's nine (16%), so H3 and H4 do not
  discriminate here; the α = 2/5 restriction inflates every model's specificity.
- **H1 holds and H2 fails:** independent directions fit the six better, not the nine (H1 carries the rule's trials factor
  of 2). Neither of the rule's two joint branches applies.
- **H7 fails:** "the tension survives this extension": no off-diagonal row has the six within 2.0 and the nine within
  2.5 together (P4, post hoc; 8 diagonal rows do).
- **H8 fails, as expected.**
- None of the nineteen is derived: τ is chosen by the fit, the pair by the data, c = 3 by hand, and the mixing, D and J
  fail.

## The read-outs computed with the cells (sealed read-outs, not cells)

- **Per pair.** Only F_6 | F_22 (H_u = F_6, H_d = F_22) reaches the six's bar: six 1.099, nine 2.320. The swapped pair
  F_22 | F_6 gives 3.07; every pair with F_−2 misses (25–167). The diagonal pairs: F_6 | F_6 six 1.466, nine 2.229;
  F_22 | F_22 six 1.571, nine 2.010.
- **The best nine-row** (F_6 | F_22 at 0.0625 + 2.7i on (2/5, 7/10), L_2): model over measured 0.51, 2.32, 0.80, 0.64,
  0.76, 0.71, and |V_us| 0.49, |V_cb| 0.49, |V_ub| 0.46.
- **The diagonal rows' calibration:** 0.14% and 0.13% (7 680 rows); their best χ²_six is 33.8.
- **The references on the same points:**
  - main's ∂R in its split reading: six 1.203, matched by 0.004% of random six-target sets (min χ²_six 6.1, at a
    neighbouring row), nine 23.5 (16%); at its best six-row |V_cb| is 23.8 times measured, the near-permutation of the
    one-conjugate readings;
  - main's ∂R read S̃: six 1.522 (χ²_six 32.9), nine 1.938, at 0.28% and 0.11%.
- **The left vectors.** At both the best six-row and the best nine-row the up and down sectors' heaviest left states are
  the same equal j–k mix (weights about 0.498 on QJ and on QK, below 0.005 on QI, in both sectors). The comparison's
  read-out "same block above ½" prints False for any such mix; the coincidence shows in |V_tb| = 0.9997 (Q5).

## Post hoc read-outs (labelled; `two_higgs_posthoc.py` and `two_higgs_posthoc2.py`)

- **P1, the rows below the six's bar.** 14 off-diagonal rows, all F_6 | F_22, all at Im τ 2.6 on L_2 (rows at 2.5 and 2.7
  miss), on (2/5, 1/10), (2/5, 1/2) and (2/5, 4/5), the last at all eight Re τ values; mirror pairs map (2/5, 1/10) at
  Re τ to (2/5, 1/2) at 1 − Re τ and (2/5, 4/5) to itself, with J changing sign. χ²_six runs from 1.19 to 12.4. At all of
  them:
  - D = 9.000;
  - the nine is 4.19–15.8: |V_us| is 4–16 times too small, |V_cb| 1.6–2.0 times, |V_ub| 1.9–3.3 times;
  - |J| ≤ 1.23 × 10⁻⁶;
  - both sectors' heaviest left states are the same j–k mix.
- **P2, the best six-row under the other models.** The diagonal pairs fail there: F_6 | F_6 gives m_d/m_b 0.33 and
  m_e/m_τ 0.37 of measured (six 3.05); F_22 | F_22 gives m_u/m_t 3.51 times measured. The up quarks want F_6, the down
  quarks and leptons F_22. |V_us| there is 0.19 of measured, smaller than with either direction alone (0.27 for F_6,
  0.32 for F_22).
  - With c = 1 the six is 3.20: the hand-set factor is essential.
  - Against the targets run to 2 × 10¹⁶ GeV in the SM (`framing_readouts.json`, F2), χ²_six at this row is 5.8, still
    below the bar (model over target 1.14, 1.03, 0.87, 0.83, 0.94, 1.05). For a holomorphic two-doublet (supersymmetric)
    structure the running differs and depends on tan β.
- **P3, main's frame around the best six-row** (F_6 | F_22, recomputed, one coordinate at a time): moving Re τ or Im τ by
  up to 0.05, the six stays within 1.07–1.30 and χ²_six within 1.04–10.3 (the lowest, 1.04, at 0.5425 + 2.6i). Within
  10% holds from Re τ − 0.05 up to the best row (1.07–1.10) and at Im τ − 0.01 (1.09), but not at Re τ + 0.01 (1.13) or
  Im τ ± 0.02 (1.12, 1.17); below the bar holds over about ±0.05. The nine stays at 4.8–6.0 and J near −1 × 10⁻⁶.
- **P4, both coarse bars.** No off-diagonal row has the six within 2.0 and the nine within 2.5 at once; 8 diagonal rows do.
- **Q1, d = e.** With F_22 as H_d, D = 9 on every row of the ten lines (to 5.5 × 10⁻⁷ in ln); with F_6 or F_−2 as H_d it
  ranges 8.4–9.5 and 7.3–10.7.
- **Q2–Q4, what the calibration measures.** With d = e and c = 3 the lepton ratios are the down ratios times 3 and divided
  by 3 (the Georgi–Jarlskog relations), so the six are four independent numbers.
  - Only 0.05% of random six-target sets have both lepton ratios within the best row's worst factor (1.0985) of three
    times and a third of their own down ratios (0.25% within its square); the data meet the relations to 5% (m_μ/m_τ
    against 3 m_s/m_b) and 11% (m_e/m_τ against m_d/3m_b), which is D = 9 against 10.58. Much of H3's "0 of 80 000" is
    those relations.
  - The four quark ratios alone: the off-diagonal rows' best worst factor is 1.097, and 0.15% of random four-target sets
    are fitted as well; in χ², 0.035% at the data's errors and 0.065% with the 10% allowance (seeds 1720–1724).
  - At the measurements' own errors, with no allowance, the four quark ratios at the best row are within 1σ: +0.36,
    −0.55, −0.19, −0.90σ (χ² 1.27, at M_Z). The two lepton ratios miss by 230σ and 54σ; PRECISION_BAR's 10% allowance is
    what admits them.
- **Q5, the two directions.** At the best row |⟨F_6|F_22⟩| = 0.99996. Both lie close to the isotropic direction
  v0 = (0, 1, i)/√2 (0.0034 and 0.0125 from it, phase-aligned), and their departures from it are nearly parallel (cosine
  0.998), in the ratio 3.66, close to 22/6. At leading order that ratio follows from a itself (θ₃^a − θ₄^a ≈ 4a·e^{iπτ},
  ZERO_FREE_FRAME_EXPLORATION §1), so it is not a choice separate from a = 6 and a = 22. The mixing there is small
  (|V_us| 0.042, |V_cb| 0.023, |V_ub| 0.0015), but about as small with either direction alone at that row (P2), so the
  near-coincidence is not its cause: aligned readings give small mixing here.
- **Q6, a matched comparison.** At the diagonal pairs' best worst factor (1.466), 0.16% of random six-target sets are
  fitted by the off-diagonal rows and 0.14% by the diagonal rows: the off-diagonal rows come closer to the data, not by
  being less generic.

## What it shows, and what it does not

- **The six at the precision bar, with the Higgs read S in every sector.** Two holomorphic Higgs directions from the
  zero-free menu, the up quarks' F_6 and the down quarks' and leptons' F_22, give all six charged-fermion mass ratios
  within 10% at the best row, and χ²_six below the bar on a band at Im τ 2.6, on L_2, with c = 3 by hand, at M_Z (at the
  best row also with SM running to 2 × 10¹⁶ GeV). The four quark ratios are within 1σ there (post hoc, Q4); the lepton
  ratios follow from the down ratios through the Georgi–Jarlskog relations (0.938 and 1.052 of measured), which the data
  meet to 5% and 11%.
- **Before this, with one direction**, only readings with the conjugate in exactly one sector reached the six's bar
  (post hoc): main's ∂R split (3.8) and the menu's own F_22 and F_6 read flipped (up S, down and leptons S̃; 3.8 and
  12.0) and F_22 split (14.9), each with |V_cb| about 24 times measured at its best row. No single direction read S or S̃
  in every sector went below 22.4 (`framing_readouts3.json`, K1). This is the first match of the six at the bar with the
  Higgs read S in every sector.
- **The masses-against-mixing tension survives (H7 fails, as the rule reads it), in a different form.** With one
  direction, the readings that reach the six's bar put the two sectors' heaviest states on different blocks, and every
  reading with S or S̃ in every sector keeps them aligned but misses the bar (χ²_six at least 22.4 on the day's scans,
  32.9 here for ∂R read S̃; the diagonal pairs 33.8). With these two directions the six reach the bar and the states stay
  aligned, as for every reading with S in every sector, but the mixing is too small: at the best row |V_us| is 0.19 of
  measured, |V_cb| 0.55 and |V_ub| 0.39; with either direction alone at that row they are 0.27 or 0.32, 0.54 or 0.55,
  and 0.39 or 0.71 (P2), so the near-coincidence of the two directions (Q5) is not what makes it small.
- **What it does not fix.** D = 9 exactly on these rows (P-094 needs 10.58 ± 0.11); J is 30 times too small; τ is chosen
  by the fit; c = 3 is by hand; for the nine one direction for both stays better (H2).
- **Limits.**
  - What the calibration does not count: the menu (fixed after the zero-free census), the α = 2/5 restriction (chosen
    after the earlier results), c = 3, and the two-doublet idea itself, which came from the framing read-outs showing
    main's one-doublet readings near the six's bar. It counts the rows: τ, the ten lines, the six pairs, the horocycles.
  - With F_22 as H_d, d = e holds on every row, so the six are four independent numbers fitted with τ (two real numbers)
    and the discrete choices (Q1–Q4).
  - The grid interleaves with earlier grids (0.03–0.06 away on these lines). Before the rule no off-diagonal pair had been
    computed anywhere; after it, only at the code-path test's stand-in point, unprinted.
  - Which pair is physical is chosen by the data: F_6 for H_u and F_22 for H_d, out of six. No principle on record assigns
    a = 6 (r = 12) to H_u and a = 22 (r = 20) to H_d (with them comes the ratio of departures, 3.66, close to 22 : 6,
    Q5).
  - "If S stands for the Higgs doublet" is a reading: if the frame's 2 × 2 index is internal, one reading for all is
    consistent with one doublet (THE_SELECTION_MAP §5), and the two-doublet structure is a choice, not a consequence.
  - The values are judged at M_Z, as PRECISION_BAR was sealed; at 2 × 10¹⁶ GeV in the SM m_c/m_t moves to 4.8σ (ln 1.143
    over its relative error 0.0278, from P2 and Q4; m_d/m_b to 2.6σ, m_s/m_b to 1.6σ), so the 1σ quark agreement holds at
    M_Z.
  - PF1-W is a reading; holomorphy applies to the Higgs factor only.

## Files

`TWO_HIGGS_RULE.md`, `two_higgs_test.py`, `two_higgs_compare.py`, `two_higgs_controls.json`, `two_higgs.npz` with
`two_higgs_index.json`, `two_higgs_compare.json` and `two_higgs_compare_run.txt`, `two_higgs_posthoc.py` and
`two_higgs_posthoc2.py` with their JSON, in `relays/chat1_2026-10-23_two_higgs/`; `framing_readouts.json`,
`framing_readouts2.json` and `framing_readouts3.json` in `relays/chat1_2026-10-23_framing/`.

0 of 19.
