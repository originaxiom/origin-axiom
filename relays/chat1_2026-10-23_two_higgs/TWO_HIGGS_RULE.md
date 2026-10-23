# TWO_HIGGS — the rule, sealed before the script exists

chat1, 2026-10-23. **SEALED.** This file is committed and pushed before the script that reads it exists. Nothing here is
a result. 0 of 19.

## The claim under test

In main's fibre frame the reading S̃ = εS̄εᵀ = S(v̄) has the form of the SU(2) conjugate H̃ = iσ₂H*. If S stands for the
Higgs doublet, one doublet needs the conjugate in exactly one of the two quark sectors, and holomorphy in every sector
(W135) needs two doublets, H_u for the up quarks and H_d for the down quarks and the leptons, each with its own
direction. The sealed menu tests (TICK_LINE_HIGGS, ZERO_FREE_HOLOMORPHIC, RIGID_TAU_HOLOMORPHIC) gave both the same
direction.

The framing read-outs found that in main's frame the masses and the mixing pull the two quark sectors' third generations
apart: the readings that fit the six best put the up and down sectors' heaviest states on different generation blocks
(a near-permutation CKM), and the readings that align them lose the masses.

This rule asks whether independent holomorphic directions for H_u and H_d, each from the menu that PF1-W, holomorphy
and three generations with one unit fix (F_6, F_−2, F_22), fit better than one direction for both, and whether any of
them fits the six and the mixing at the same row, on points nobody has computed.

## What was seen before this rule (disclosed)

- The three sealed menu tests, their post hoc read-outs, and the framing read-outs (`framing_readouts.py`,
  `framing_readouts2.py`); the zero-free census's read-out (`zero_free_readout.json`), which gives, for each single
  direction, the readings S, S̃ and the two mixed ones.
- **No pair with v_u ≠ v_d has been computed or read by anyone, at any point.** The stored outputs hold each direction's
  sector ratios, from which the six of such a pair at stored points could be read; chat1 has not read them, and will not
  before this rule's comparison is read.
- The diagonal pairs (v_u = v_d) are the sealed menu's model, known at nearby points (this grid interleaves with the
  earlier grids, 0.03–0.06 away on these lines).

## The model

- **Directions.** v_u, v_d ∈ {F_6, F_−2, F_22}, each the unit vector (εθ₂^a, εθ₄^a, iθ₃^a)/norm at τ (the zero-free
  census's `direction`), both read S (holomorphic). Nine pairs: six off-diagonal (v_u ≠ v_d), three diagonal.
  - Up quarks: Y_u = coupling(S(v_u), M_up).
  - Down quarks and leptons: Y_d = coupling(S(v_d), M_down), Y_e = coupling(S(v_d), M_lep).
  - The lepton factor c = 3 by hand on the stored ratios (m_μ/m_τ × 3, m_e/m_τ ÷ 3).
- **The frame.** Main's B1720 instrument at 3412bf09d, unchanged, through the zero-free census's code: `route_b_scan.py`'s
  channels, `B.coupling`, `two_ingredients_census`'s `ckm_left` (left singular vectors; Y's rows are Q's generations).
- **Stored per row:** the six log ratios, the three |V|, J, and each of the up and down sectors' heaviest left vector as
  weights on the generation blocks (QJ, QI, QK).
- **References computed alongside, not cells:** main's ∂R in its split reading (up S̃, down and leptons S) and with S̃
  in every sector, c = 3.

## The grid (nobody has computed it)

- The ten α = 2/5 lines (2/5, k/10), k = 0 … 9, of order 5 and 10. They hold every best row of the zero-free census, of
  ZERO_FREE_HOLOMORPHIC and of its reference. (This restriction is a choice made after those results; it is disclosed,
  and it inflates the specificity of every model on the grid alike.)
- Re τ ∈ {0.0625, 0.1875, …, 0.9375} (8 values), none a value of an earlier grid; Im τ ∈ {2.0, 2.1, …, 3.5} (16 values);
  both horocycles.
- 1 280 points; 2 560 rows per pair; 15 360 off-diagonal rows and 7 680 diagonal rows.

## Measure and calibration (main's), and the scale

- Targets: Huang–Zhou 2021 at M_Z and PDG 2025's moduli, the record's pinned files at 3412bf09d (sha256 as before).
  "Six" and "nine" are the worst factors. The comparison is at M_Z, as PRECISION_BAR was sealed; the scale is a framing
  choice (THE_FRAMING_CHECK §4a).
- Random as good: main's generator; seeds 1720–1739, each drawing 4 000 six-targets then 4 000 nine-targets; the
  fraction of targets fitted at least as well (Chebyshev distance in log) by the model's rows; the mean over the seeds.
- PRECISION_BAR.md's χ² (σ² = the data's relative error² + 0.1²; bars 16.75 for the six and 21.67 for the nine).

## The cells, with priors

| cell | statement | prior |
| --- | --- | --- |
| H1 | the best off-diagonal pair's six is lower than the best diagonal pair's six on the same points | 50% |
| H2 | the best off-diagonal pair's nine is lower than the best diagonal pair's nine | 30% |
| H3 | the six is specific on the off-diagonal rows: ≤ 1% of random targets as good, calibrated on all 15 360 | 25% |
| H4 | the nine is specific on the off-diagonal rows: ≤ 1%, the same rows | 15% |
| H5 | some off-diagonal row has χ²_six below 16.75 | 10% |
| H6 | some off-diagonal row has χ²_nine below 21.67 | 3% |
| H7 | the tension: at the off-diagonal best six-row the nine is within 2.5 | 15% |
| H8 | at the off-diagonal best nine-row \|J\| is within a factor 3 of 3.08 × 10⁻⁵ | 5% |
| C1 | the instrument: each diagonal pair reproduces the zero-free census code's S fields (`rows_at`: ratios and S\|S mixing) at the first grid point to 10⁻⁹ in ln (\|V\| above 10⁻¹²) | 95% |
| C2 | main's ∂R with S in every sector reproduces main's `TC.ratios_at` at ½ + 3.08i on (2/5, 1/10) to 10⁻⁹ in ln (as in the earlier rules) | 95% |

## What the outcomes mean (fixed now)

- **H1 and H2 hold.** Independent holomorphic directions fit the pattern better than one direction for both. The
  off-diagonal side has six pairs to the diagonal side's three (a trials factor of 2); a positive here is read with it.
- **H3 and H4 hold.** The two-doublet model is specific on its rows (with the α = 2/5 restriction's inflation, shared
  with every model on this grid).
- **H5 or H6 holds.** A values-level match of the six (or the nine) for principled Higgs directions, with τ the only
  continuous number and c = 3 by hand; read at M_Z, with the scale caveat.
- **H7 holds.** Two holomorphic doublets fit the six and the mixing at one row: the tension found in main's readings is
  not structural to the frame. **H7 fails:** the tension survives this extension.
- **H1 and H2 fail.** One direction for both is as good as two; the two-doublet freedom does not help at this menu.
- **H8 fails as expected** (the CP tension of THE_FRAMING_CHECK §3).
- **A control fails.** Nothing is read until it is resolved post hoc, labelled.

## Discipline

- One script, `two_higgs_test.py`, and its comparison, `two_higgs_compare.py`, are committed before the run; the run's
  output is committed before it is read; the comparison's printout is redirected unread and committed before it is read.
- A failed launch is disclosed with its log kept. Any later check is labelled post hoc.

0 of 19.
