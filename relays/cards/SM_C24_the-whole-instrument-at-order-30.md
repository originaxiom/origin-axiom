# SM-C24 — the whole instrument at order 30: every point's reading over every cusp is one table of 576 points

*Card of the SM seat, 2026-11-25, following SM-C23. Committed and pushed with its script
(`relays/sm_c24/run_c24.py`, SHA-256 85256d17c8e952e9) before the script is run on any point of
order 30. Data-free: rates (cusp exponents) of frame C's mass ratios and mixing are computed; nothing is compared with a
measured number.*

## 0. Derived before any run

- **SM-C23:** frame(γτ, vγ⁻¹) = frame(τ, v), with the end shifted by its law. So the rates of the point v read at the
  cusp γ(∞) are the rates of the point vγ read at ∞.
- **Every cusp is γ(∞)** for some γ in SL(2, ℤ), and SL(2, ℤ) acts transitively on the points of exact order N in
  (ℤ/N)², which number N²∏(1 − 1/p²): 576 for N = 30.
- **So the table of one point of order 30 over all cusps is the same for every point of order 30:** the rates at ∞ of
  all 576 points. This depends only on the level. Which point is read stops being a choice, and the menu question
  becomes how the cusps' readings combine. The cusps of Γ(30) all have width 30, so the equal weight is the only one
  the level offers. That is an observation, not computed here.
- B1976 to B1979 read the 96 points whose 5-part lies on the act's line. That is a sixth of the table: the rest is the
  instrument's other cusps.

## 1. What is computed

- **The 576 points** of exact order 30, taken as 288 pairs ±v.
- **For each,** the rates of the six mass ratios and of |V₁₂|, |V₂₃|, |V₁₃|, read as B1977 reads them (main's `parts`,
  column 0.13, reading S), between heights 30 and 40 and between 40 and 50. Each rate is placed on the grid of 1/60
  (B1979), and the alignment, least |V_kk|, is taken at height 50.
- **Controls:** E4, v against −v on 12 pairs; K0, the frozen end. Above Im τ = 6 the frame is read with L₂ frozen at
  2.2505 (SM-C23's note). K0 moves L by ±0.05 on 12 points and measures how far the rates move.

## 2. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| E1 | under half of the 288 aligned and hierarchical (both quark sectors); all 48 on the act's line are | 55% |
| E2 | every 40–50 rate within 3e-3 of the 1/60 grid; at least 95% of points keep their class from 30–40 | 75% |
| E3 | more than 12 classes over the 288 | 80% |
| E4 | v and −v have equal rates (within 1e-6) | 95% |
| K0 | moving the end by 0.05 moves no rate by more than 1e-3 | 75% |

## 3. What it means

- **The table is the object's reading at order 30,** with no point chosen. Its class sizes are then the weights the
  level gives each class, if the cusps are weighted equally.
- **If E1 holds:** alignment and hierarchy are not properties of the level. They hold on the act's line, a sixth of the
  cusps, so a reading that keeps them must weight that sixth. Something in the object has to say why.
- **If E1 fails because nearly all are aligned and hierarchical:** the property is the level's own, and no weighting
  of the cusps can lose it.
- **If K0 fails:** the rates at these heights depend on the frozen end, and the end above Im τ = 6 must be computed
  before any rate at order 30 is read. That would hold for B1977 to B1979 as well.
- No outcome is a value of the 19.

## 4. Files

relays/sm_c24/: the script, `c24_run.txt` and `c24_results.json`. The page will be
relays/SM_C24_THE_WHOLE_INSTRUMENT.md.
