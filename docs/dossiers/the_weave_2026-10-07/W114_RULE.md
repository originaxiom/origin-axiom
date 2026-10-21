# W114 — the tuned layer's fit: can θ̄ = 0 at every τ and the observed quarks coexist in the record's frame at all, at the cost of one tuned number per tuned sector? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's choice** (2026-10-21), after W113. Of the three candidates the goal page named
  (`THE_SKELETON_AND_THE_FLESH.md`), the owner took the first, the tuned layer's fit.
- **What W113 left.**
  - In the record's frame, θ̄ is constant for every coupling only at one weight per type. The one viable assignment
    there, every quark in T̄ at weight 3, does not fit the quarks (χ²_min = 104 for 2 dof).
  - Sixteen assignments up to weight 7 make θ̄ constant on a tuned sub-variety: one real condition per tuned sector.
    All sixteen keep J ≠ 0 (W113 T2). None was fitted.
- **The question.** Can the frame hold the observed quarks with θ̄ = 0 at every τ at all? A tuned number buys
  nothing in the count, so a fit cannot lower it. But if none fits, the frame is excluded by the quark data with
  θ̄ = 0 up to weight 7. That is a stronger negative than W113's.

## Weave or thread

**WEAVE-type, given the frame.** All sixteen viable tuned assignments up to weight 7 are taken, with none
hand-picked. Every coupling on each tuned variety and in each automatic space is allowed. The claim is about all of
them at once.

## The frame

W113's, unchanged:
- W101's hypotheses H-T, H-W, H-H and H-θ;
- CP in the law (§158's level 4, the swap; GENESIS GM5c, OPEN), so the coefficients are real in a real basis;
- the Dedekind counterterm with N = 6K;
- tree level, the ruled branch's holomorphic couplings, the quark sector only.

## The assignments and their parameters (fixed now)

- **A sector's free real parameters** are its dimension minus 1 (the scale), minus 1 if it is tuned.
  - T⊗T at 1: 0.
  - T⊗T at 5, tuned: 2.
  - T̄⊗T̄ at 3: 2.
  - T̄⊗T̄ at 7, tuned: 4.
  - Mixed at 4, tuned: 2.
- **An assignment's parameters** are those two sectors' plus 2 for τ. Its degrees of freedom are 8 minus that.

| # | hand (s_Q, s_u, s_d) | up | down | parameters | dof | pass mark |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | (+, +, +) | T⊗T 1 | T⊗T 5t | 4 | 4 | 9.49 |
| 2 | (+, +, +) | T⊗T 5t | T⊗T 1 | 4 | 4 | 9.49 |
| 3 | (+, +, +) | T⊗T 5t | T⊗T 5t | 6 | 2 | 5.99 |
| 4 | (+, +, −) | T⊗T 1 | mixed 4t | 4 | 4 | 9.49 |
| 5 | (+, +, −) | T⊗T 5t | mixed 4t | 6 | 2 | 5.99 |
| 6 | (+, −, +) | mixed 4t | T⊗T 1 | 4 | 4 | 9.49 |
| 7 | (+, −, +) | mixed 4t | T⊗T 5t | 6 | 2 | 5.99 |
| 8 | (+, −, −) | mixed 4t | mixed 4t | 6 | 2 | 5.99 |
| 9 | (−, +, +) | mixed 4t | mixed 4t | 6 | 2 | 5.99 |
| 10 | (−, +, −) | mixed 4t | T̄⊗T̄ 3 | 6 | 2 | 5.99 |
| 11 | (−, +, −) | mixed 4t | T̄⊗T̄ 7t | 8 | 0 | 3.84 (compatibility only) |
| 12 | (−, −, +) | T̄⊗T̄ 3 | mixed 4t | 6 | 2 | 5.99 |
| 13 | (−, −, +) | T̄⊗T̄ 7t | mixed 4t | 8 | 0 | 3.84 (compatibility only) |
| 14 | (−, −, −) | T̄⊗T̄ 3 | T̄⊗T̄ 7t | 8 | 0 | 3.84 (compatibility only) |
| 15 | (−, −, −) | T̄⊗T̄ 7t | T̄⊗T̄ 3 | 8 | 0 | 3.84 (compatibility only) |
| 16 | (−, −, −) | T̄⊗T̄ 7t | T̄⊗T̄ 7t | 10 | −2 | 3.84 (compatibility only) |

- **The pass marks.** For dof ≥ 1, the 95% point of χ² with that many degrees of freedom. For dof ≤ 0 the model has at
  least as many parameters as observables, so a low χ² predicts nothing. Those five are scored for compatibility
  only, at the one-dof mark 3.84.

## The instrument (the script, written after this rule)

- **It reuses W113's code** (`the_strong_angle.py`, imported): the exact spaces, their real bases, the fast
  evaluation, the observables, the data and the χ² (W66's, at a = 0.10, with read-outs at 0.05 and 0.20).
- **The variety.**
  - In a tuned sector of type σ and weight k, α(c) is the E₄³ part of det Y/η^a.
  - α is a real cubic form, computed exactly as a tensor: by multilinearity in the rows, from the exact q-series at
    the order a/24 + m/8.
- **The parametrization.** A fixed real direction e with α(e) ≠ 0 is drawn from the seed. A free vector v maps to
  c = v + s*·e, where s* is the real root of the cubic α(v + s·e) of least |s|. So every evaluated point lies on the
  variety, and θ̄ = 0 there exactly.
- **The search, per assignment** (fixed seed 114):
  - 20 000 random points: τ uniform in F with Im τ ≤ 6, and the free vectors normal;
  - Nelder–Mead from the best 50 (at most 8000 evaluations each), then again from the best 5;
  - a point whose image in F has Im τ > 8 scores ∞.
- **At each assignment's best point** (read-outs, mpmath at 30 digits):
  - det(Y_u)·det(Y_d)/η^{6K} real and constant across three τ, so θ̄ ∈ {0, π} there, with the bit;
  - J, δ to the nearest elliptic point, the eight observables and their pulls.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| U0 | the control: synthetic data from a random point on assignment 12's variety (fixed seed) is fitted back by the same search to χ² ≤ 0.01 | 75% |
| U1 | at every assignment's best point, det(Y_u)·det(Y_d)/η^{6K} is real and constant across three τ to 10⁻¹² | 95% |
| U2 | the four assignments with T⊗T at 1 (1, 2, 4 and 6) fail their pass marks: B1636's sum rule keeps that sector's m₂/m₁ ≥ ½ | 98% |
| U3 | no assignment with dof ≥ 1 passes its pass mark | 90% |
| U4 | no assignment with dof ≤ 0 reaches χ²_min ≤ 3.84 | 65% |
| U5 | read-out only: every assignment's χ²_min at the three allowances, its best point, and J there | — |

## What the outcomes mean (fixed now)

- **U3 and U4 hold.** No assignment up to weight 7 holds the observed quarks with θ̄ = 0 at every τ, even at one
  tuned number per tuned sector. In the record's frame, θ̄ = 0 at every τ and the quark data are incompatible up to
  weight 7. The frame is excluded by the data on this route.
- **U3 holds and U4 fails.** Only assignments with as many parameters as observables reach the data. θ̄ = 0 is then
  compatible with the quarks in the frame, but the fit predicts nothing.
- **U3 fails.** Some assignment with dof ≥ 1 fits the quarks with θ̄ = 0 at every τ. That would be the record's first
  quark fit in any frame (W69's best χ² was 100, W113's 104). It still costs a tuned number for θ̄, so the count does
  not move. Its free numbers would then be compared with the Standard Model's ten quark numbers and θ̄.
- **In every case, nothing here lowers the count.** 0 of 19.

## Seen before the rule (disclosed)

- **W113's whole record:**
  - the census and its classes;
  - the one forced assignment's fit (χ²_min = 104) and its best point on Re τ = 0;
  - T1's varieties and their rank-two exceptions (post hoc);
  - T2's J ≠ 0 in all sixteen tuned assignments;
  - T3's smallest hierarchy measure per tuned assignment, from 6.6 × 10⁻⁴ (assignment 3) to 0.64 (with T⊗T at 1).
- **No tuned assignment has been fitted**, by this seat or, as far as this seat knows, anywhere on record.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
