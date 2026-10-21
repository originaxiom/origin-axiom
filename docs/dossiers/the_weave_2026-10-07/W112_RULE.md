# W112 — the skeleton's significance: does the forced menu fit the data's hierarchy pattern better than chance? (the rule, committed before the code)

**Why.** This is stage 1 of the project goal (`THE_SKELETON_AND_THE_FLESH.md`, the owner's word of 2026-10-21).
- W69 scored its 21 952 forced assignments with a χ² at a 10% allowance. None passed: the best was 99.9, against a
  pass mark of 7.81.
- At the skeleton level, where each observable must come within a factor F with order-one coefficients left free, the
  same best assignment is already close. Its five observables are within a factor 1.85 of the data (seen, disclosed
  below).
- The question W69 never asked: is that closeness special, or would the same menu fit random data just as well?

**Weave or thread.** A WEAVE-type result, given Λ (GENESIS FK11) and W69's hypotheses (B1644's form, H-sec, H-pair′).
- It takes every one of W69's assignments and every τ on the stated grid, with none hand-picked.
- Its claim is about the whole menu at once.

## Seen before the rule (disclosed)

- **W69's committed read-out.** Its best assignment, ER / EE / RG at τ = 0.5 + 0.888i, gives m_c/m_t 0.0064, m_s/m_b
  0.0128, m_μ/m_τ 0.0415, |V_us| 0.122 and |V_cb| 0.061, against data of 0.0037, 0.0187, 0.0589, 0.225 and 0.042. The
  largest factor is 1.85, on |V_us|.
- **Its unfitted values.** m₁ = 0 in the up and lepton sectors; m_d/m_b = 1.6 × 10⁻⁴ against 9.4 × 10⁻⁴; |V_ub| =
  0.0075 against 0.0037; and |V_td| = 5 × 10⁻⁵ against 0.0086.
- Nothing else about the menu at the skeleton level is known to this seat. In particular, the number of assignments
  within a factor 2 is not known, and neither is any synthetic-target statistic.

## The instrument (the_skeleton.py, committed before its one run)

- **The menu.** W69's seven parameter-free sections and 28 pairs, with W69's own code imported: its sections, its
  pair matrices and its left rotations. That gives 28³ assignments of a pair to the up, down and lepton sectors.
- **The τ points.**
  - W66's grid: 41 × 40 points in the fundamental domain, up to y = 6.
  - Dense patches around the elliptic points ω, ω + 1 and i: radii from 10⁻³ to 0.12 (24, geometric) and 36 angles,
    kept where they lie in the closed fundamental domain.
- **The observables.** W66's five: m_c/m_t, m_s/m_b, m_μ/m_τ, |V_us| and |V_cb|. The data and its source are W66's
  (HZ2021 at M_Z; B1612's CKM).
- **The skeleton distance.**
  - For a target vector x, D(x) is the minimum, over every assignment and τ point, of the largest
    |ln(obs_i / x_i)| over the five observables.
  - F*(x) = e^{D(x)} is the best factor the menu reaches.
  - A zero observable counts as infinitely far.
- **The null, by target randomisation.**
  - **Box B1.** N = 4000 synthetic targets, each observable drawn log-uniformly in [x_i/10, 10 x_i], independently,
    from a fixed seed.
  - **Box B2.** Another 4000, in [x_i/√10, √10 x_i].
  - p_B = the fraction of synthetic targets with F*(target) ≤ F*(data).
  - A small p means the real data sits unusually close to the forced menu.
- **Read-outs, no prior.**
  - F*(data) on the grid, and refined by Nelder–Mead in τ for the ten best assignments.
  - The assignments within a factor 2 and within a factor 3, with their τ and their distance δ to the nearest
    elliptic point.
  - At the best point, the unfitted values: m₁/m₃ per sector, |V_ub| and |V_td|, against HZ2021 and B1612.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | the control: W69's best point (ER / EE / RG at 0.5 + 0.888i), evaluated by this instrument, gives W69's five observables to 1% | 95% |
| K1 | F*(data) ≤ 2 on the grid, so the data is fitted at the skeleton level | 70% |
| K2 | p_B1 < 0.05: the skeleton fit is special in the ±1-decade box | 20% |
| K3 | p_B2 < 0.05: the same in the ±½-decade box | 10% |
| K4 | at most 50 distinct assignments are within a factor 2 | 50% |
| K5 | every point within a factor 2 lies within δ ≤ 0.12 of an elliptic point | 60% |
| K6 | the first generation fails: at every point within a factor 2, some sector's m₁/m₃ is 0 or more than a factor 10 from the data | 85% |

## What the outcomes mean (fixed now)

- **K1 and K2 hold.** The forced skeleton sits on the data more closely than chance would put it. That is the first
  evidence for the vision's first half. Stage 2 (what sets δ) and stage 3 (the first generation) follow, rule first.
- **K1 holds and K2 fails.** The skeleton fits, but so would most data in the box. The fit is no evidence, and the
  vision's first half is not supported in this frame. That is recorded as a negative. The next frame is chosen with
  the owner.
- **K1 fails.** Even at a factor 2 the forced menu misses. That is a stronger negative.
- **K6** says whether the first generation is the open piece, as W68 found, at every skeleton fit.
- **Either way, nothing here lowers the count.** A fit is not a prediction. Only an unfitted, confirmed value would
  lower it.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- Any failed prediction is recorded as failed, and any later check is labelled post hoc.

0 of 19.
