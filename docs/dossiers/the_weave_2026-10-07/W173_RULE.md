# W173 — THE RIDDLE, horn 3 at the record's best rows: is the six's fit carried by the frame's forced exponent pattern with one height, or by the chosen point (Re τ, the height) and point-dependent intercepts? (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **THE RIDDLE** (NOTE, "Reading: THE RIDDLE"; relay §316), program item 3. Horn 3 says the data are carried by
  choices, not by forced structure.
- The record's best rows match the six (χ²_six about 3), and that match is what the plan's chain rested on. Two pieces
  of evidence are not yet measured:
  - the web seat's arithmetic, that the first generation's prefactors at the best rows are near 30;
  - the nulls, which pass random targets.
- **The constructive question inside horn 3: is there a skeleton?** If each feature at a row is mostly its forced
  exponent times the height, with intercepts of order one, then the frame's skeleton carries the six with one number,
  as the owner's goal of 2026-10-21 asks. If the intercepts are large and the six sweep many σ as Re τ moves, the point
  carries the fit.

## The computation (fixed now)

- **The rows.** W158's 38 strip rows (W167's row lists): the line, Re τ, Im τ, L_max, the readings (S̃, S, S), c = 3.
- **The frame.** B1726's own instrument as this seat rebuilt it (`the_third_opinion_b1726.py`, `own_point`). It covers
  the residues, the kernel norms, the horocycle from B1667's column, and the Higgs section DR.
- **The six.** For each sector, ln(m₂/m₃) and ln(m₁/m₃), with ln c added to the lepton features as in the census.
  χ²_six and σ are B1741's, with the targets read once.
- **The decomposition at each row.**
  - The local exponents e_i = −f_i′(y)/2π, from a central difference in Im τ (h = 0.01, at fixed Re τ, the
    horocycle following the column).
  - The intercepts P_i = f_i − y f_i′(y). So f_i = −2π y e_i + P_i: the exponent part is the forced slope times the
    height, and the intercept is the rest.
- **The Re τ sweep at each row.** 60 points of Re τ spanning one period of the line's T-orbit (5 for the slope-2/5
  lines), at the row's Im τ. Each feature's range is recorded in units of its σ, with χ²_six's range.
- **The line sweep** (a read-out). At the four rows with the least χ²_six (two from each list), all 266 census lines at
  the row's τ: χ²_six per line, and each feature's spread in σ.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| Q0 | **The instrument.** At every row the own frame's χ²_six reproduces the stored row's χ²_six to 10⁻⁶ relative | 95% |
| Q1 | **Re τ is a strong knob.** At every row, some feature sweeps more than 10σ over Re τ on the orbit at the row's height | 90% |
| Q2 | **The intercepts carry part of the fit (the skeleton test, decisive).** At every row at least one of the six has \|P_i\| > ln 3, so the forced exponents times one height do not carry the six with intercepts of order one | 70% |
| R | **Read-outs** (no predictions): e_i and P_i per row; the data's own exponents −d_i/(2πy) at each row's height; the height that moves χ²_six by 10; the CKM moduli's sweep over Re τ; the line sweep's per-line χ²_six | — |

## What the outcomes mean (fixed now)

- **Q1 and Q2 hold (the expected outcome).** Horn 3 is confirmed by measurement.
  - The rows' match is a selection of a point on a continuum where the six sweep many σ.
  - The hierarchy at the rows is partly carried by intercepts that depend on the point, not by the forced exponents
    with one height.
  - That is why random targets also find rows: the menu's capacity is the continuum of Re τ and the height.
- **Q2 fails** (every |P_i| ≤ ln 3 at some row): at that row the frame's exponents carry the six with one number and
  intercepts of order one. That is the skeleton the owner's goal names.
  - The rows where it fails are named, with their line classes, and become the next arc's target, rule first.
  - It would be the record's first sign that the structure, not the point, carries the six.
- **Q1 fails:** Re τ is a weak knob at that row, and the match there is not a fine selection in Re τ.

## Weave or thread

- A frame result at data-chosen rows: a thread-and-frame look, labelled so. The line sweep at four rows covers every
  line on the census.

## What stays out

- The CKM's fit and J. The CKM's sweep is a read-out only.
- Other readings, the horocycle L₂, c ≠ 3, any refit.

## Looks (charter viii)

- One look at the six: the decomposition and sweeps at the 38 rows read the targets once. It tests no fit and selects
  nothing, and it is counted.

## Seen before the rule (disclosed)

- The rows' stored χ²_six (about 2.7–3.6 at the best rows) and their positions.
- The web seat's arithmetic: first-generation prefactors near 30 at the best rows. It is not a sealed cell, and it is
  the source of Q2's prior.
- One timing call of `own_point` at a point that is not a row ((1/7, 2/7) at 0.123 + 2.345i; about 1 s). No value was
  read.
- Not computed: no exponent, intercept or sweep. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run, on four workers. Its output is committed before it is read. The only checks before that are the exit,
  failures, NaN, paths and warnings.
- Any later check is labelled post hoc.

0 of 19.
