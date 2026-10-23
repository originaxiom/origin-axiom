# TICK_LINE_HIGGS — the rule, sealed before the script exists

chat1, 2026-10-23. **SEALED.** This file is committed and pushed before the script that reads it exists. Nothing here is
a result. 0 of 19.

## The claim under test

Principles on record select every discrete datum of main's fibre frame, and the frame still fits:

1. **The line, by the tick** (main's B1698): the tick's sign-fixed lines, the order-5 points fixed up to sign by L·R and
   by R·L (det(LR + I) = 5): S₁ = {(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)} and S₂ = {(1/5, 3/5), (2/5, 1/5),
   (3/5, 4/5), (4/5, 2/5)}, with w = ατ + b as in B1698 and the census.
2. **The Higgs and its reading, by PF1-W, holomorphy and three generations with one unit** (the sealed rule
   ZERO_FREE_HOLOMORPHIC, 38e2b8062): the menu F_6 (r = 12), F_−2 and F_22 (r = 20), each as its unit direction
   (εθ₂^a, εθ₄^a, iθ₃^a)/norm with ε = +1, read through S in every sector.

Left free: τ and the horocycle. By hand: the lepton factor c = 3 (m_μ/m_τ × 3, m_e/m_τ ÷ 3), as in the sealed census.

## What was seen before this rule (disclosed)

- **B1698** (main, sealed, NEGATIVE): ∂R with main's readings on the eight tick lines at Re τ ∈ {0, ½}, Im τ 1.5–3.5:
  six within 2.33 at (2/5, 4/5) and (3/5, 1/5), Re τ = ½, Im τ = 3.1; 1.7% of random hierarchies as good (bar 1%); the
  down quarks and leptons coincide on these lines (minimal SU(5)'s Y_e = Y_dᵀ), so D = c² exactly.
- **The zero-free census** (`relays/chat1_2026-10-23_zero_free_frame/`, Re τ ∈ {0.1, 0.4}, Im τ 1.0–4.0, 266 lines
  including the tick's): F_6 with S and c = 3 has its best six (1.50) at 0.4 + 2.4i and its best nine (2.30) at
  0.4 + 2.3i, both on (2/5, 4/5), the second horocycle. The new grid neighbours those points.
- **ZERO_FREE_HOLOMORPHIC** is running; its outputs are unread. Its grid (Re τ 0.15–0.90 step 0.15, Im τ 2.05–3.45 step
  0.1) contains the tick's lines; the grid below shares none of its values.
- Main's B1726 is sealed and not run; its Re τ values (0.05, 0.2, 0.35, 0.55, 0.7, 0.85) are avoided.

## The model

- **The frame:** main's B1720 instrument at 3412bf09d, unchanged, through `route_b_scan.py`'s channels and the zero-free
  census's `direction` and `rows_at` (both committed), exactly as ZERO_FREE_HOLOMORPHIC uses them.
- **Rows:** the menu's three directions, reading S in every sector, c = 3, the eight tick lines, the grid below, both
  horocycles.
- **Read-outs computed alongside, not cells:** the same with S̃ in every sector; c = 1; main's ∂R with S̃ in every
  sector and c = 3 (the sealed census's model) on the same points.

## The grid (nobody has computed it)

- Re τ ∈ {0.025, 0.075, …, 0.975} (20 values, step 0.05); Im τ ∈ {2.025, 2.125, …, 3.425} (15 values, step 0.1).
- None of these values is a value of chat1's earlier grids, of B1698's (Re 0, ½), of ZERO_FREE_HOLOMORPHIC's or of
  B1726's.
- 8 lines × 300 τ = 2 400 points; 4 800 rows per direction and reading; 14 400 menu rows.

## Measure and calibration (main's)

- Targets: Huang–Zhou 2021 at M_Z and PDG 2025's three moduli, the record's pinned files at main's 3412bf09d (sha256 as
  in the sealed census). "Six": the worst factor over the six ratios. "Nine": over the six and |V_us|, |V_cb|, |V_ub|.
- Random as good: for each seed s in 1720–1739, `random.Random(s)` draws 4 000 six-targets, then 4 000 nine-targets;
  the fraction that the menu's rows fit at least as well (Chebyshev distance in log). The cells use the mean over the
  20 seeds.

## The cells, with priors

| cell | statement | prior |
| --- | --- | --- |
| K1 | the six fit within 2.0 at the menu's best row | 70% |
| K2 | the six are specific: random as good ≤ 1% (mean over 20 seeds) | 55% |
| K3 | the nine fit within 2.5 at the menu's best row | 60% |
| K4 | the nine are specific: ≤ 1% | 50% |
| K5 | the reading: the best six and the best nine with S are both lower than with S̃ (same rows) | 85% |
| K6 | at the best nine-row, \|J\| is within a factor 3 of 3.08 × 10⁻⁵ | 5% |
| K7 | the best six-row lies on a line with α ∈ {2/5, 3/5} | 85% |
| C1 | the instrument: ∂R with S reproduces main's `TC.ratios_at` at ½ + 3.08i on (2/5, 1/10) to 10⁻⁹ in ln | 95% |
| C2 | covariance: with F_6, τ → τ + 1 and b → b − α change no ratio, and no \|V\| above 10⁻¹², by more than 10⁻⁹ in ln, at the first grid point (on (1/5, 2/5)) | 95% |

**P-094 is not a cell.** On the tick's lines d = e exactly (B1698), so D = c² = 9 at every row, against 10.58 ± 0.11.
That failure is fixed by construction and is recorded as such.

## What the outcomes mean (fixed now)

- **K1–K5 hold.** Principles on record select every discrete datum of main's frame: the line (the tick), the Higgs, its
  twist and its reading (PF1-W, holomorphy, three generations with one unit). The frame then fits the six and the nine
  specifically on points nobody had computed. What remains free is τ and the horocycle; by hand, the lepton factor,
  which P-094 says cannot be 3 on these lines; and the CKM phase. A positive at main's coarse measure; it derives none of
  the nineteen.
- **K1 and K3 hold, K2 or K4 fails.** The selected data fit, but not specifically.
- **K1 or K3 fails.** The census's fits do not carry to the tick's lines on a fresh grid.
- **K5 fails.** Holomorphy does not pick the reading on the tick's lines.
- **K7 fails.** The tick's α = 1/5 lines do better than its α = 2/5 lines, unlike B1698 and the census.
- **A control fails.** Nothing is read until it is resolved post hoc, labelled.

## Discipline

- One script, `tick_line_test.py`, and its comparison, `tick_line_compare.py`, are committed before the run. The run's
  outputs are committed before they are read. A failed launch is disclosed with its log kept. Any later check is
  labelled post hoc.

0 of 19.
