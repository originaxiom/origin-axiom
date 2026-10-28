# W169 — the plan's stage 4, the state: at the counted line, does the one-loop potential of the frame's own fields hold Re τ where the six pass? The minimum over Re τ on the line's whole T-orbit at the strip's heights, against W158's 38 rows; and the height (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The plan's stage 4** (`THE_NINETEEN_PLAN_2026-10-27.md`): τ comes from the effective action's minimum set. W154
  did this at the trivial line. The minimum sits on the imaginary axis at y* ≈ 7t/π², with t = B/|A| set by the
  content, and Re τ is almost free there (curvature 10⁻³–10⁻⁶ of the height's). The strip's rows are off the axis
  (Re τ 0.27–0.73).
- **What W167 changes.** The line is now a counted choice: the class (2/5, odd/10), where the six pass. At a nontrivial
  line the charged fields' potential depends on Re τ much more strongly than at the trivial line. For charge q the
  leading Re τ dependence is suppressed only by exp(−2π d_q y), with d_q the distance of q·a from the integers.
  - For a = 2/5 that is d = 0.2 for |q| = 2 and 3, about 0.02 at y ≈ 3.
  - So the line may hold Re τ. If it holds it where the six pass, Re τ is derived given the line, and is not a free
    number.

## The objects (fixed now)

- **The potential:** W167's, unchanged. V(τ; line) = Σ_f n_f K_{σ_f}(q_f ψ; τ), with:
  - W59's joint-parity kernel at s = 3, N = 48;
  - ψ = (−a, b) for the line (a, b);
  - the frame's own fields and weights, W167's table (three generations; H_u and H_d as bosons).
  - The script imports W167's `Kernel` and `Content` unchanged.
- **The line and its orbit.** The T-law (τ, b) ~ (τ + 1, b − a) takes the five lines (2/5, odd/10) into one another.
  - (2/5, 1/10) at Re τ = x + j is the line (2/5, 1/10 + 2j/5) at x.
  - So on the single line (2/5, 1/10), X ∈ [0, 5) covers the whole class, and V(X + 5) = V(X).
  - The mirror (2/5, b) ↔ (2/5, 3/5 − b) at 1 − x becomes X ↔ 2 − X on this orbit. Its fixed points are X = 1 and
    X = 3.5.
- **The rows** are W158's 38, read from W156's and W157's committed outputs. Each is mapped to its orbit coordinate
  X ∈ [0, 5) on (2/5, 1/10): X = x + j, with 1/10 + 2j/5 ≡ the row's b. All 38 rows lie on (2/5, 1/10) or
  (2/5, 1/2) (W157), so j ∈ {0, 1}.
- **The heights:** each row's own Im τ.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| S0 | **Controls.** At three rows' heights, V(X + 1; (2/5, 1/10)) = V(X; (2/5, 1/2)) (the T-step), V(X + 5) = V(X), and the mirror V(X) = V(2 − X), each to 10⁻⁶ relative at ten random x (the box's truncation, as in W167) | 95% |
| S1 | **The height is not held by the frame's own content.** On the line, at X = 1 and at X = 3.5, V(x + iy) decreases as y goes from 2 to 8: it runs to the cusp | 85% |
| S2 | **Re τ at the rows (decisive).** At each row's height, the global minimum of V over X ∈ [0, 5) on (2/5, 1/10), found on a 5 000-point grid and refined, lies within 0.05 of that row's X (the minimum set is closed under the mirror, so X* and 2 − X* both count) | 15% |
| S3 | **Re τ is held.** At each row's height, V's curvature in X at the minimum is at least 10⁻⁴ of its curvature in y there. That is, the line holds Re τ far more firmly than W154's trivial line | 70% |
| R | **Read-outs** (no predictions): per row, X* and \|X* − X_row\|, V(X*), V(X_row) − V(X*), and the curvatures; the set of X* over the heights; whether X* is a fixed point of the mirror (1 or 3.5) or one of a mirror pair; the same with the bosons' weight ×2 and ×5 | — |

## What the outcomes mean (fixed now)

- **S2 holds:** at the counted line, the frame's own one-loop potential puts Re τ where the six pass, at every row.
  Re τ is then derived given the line, a frame result. The stage-4 map reads "the line → Re τ; the content → t → the
  height".
- **S2 fails:** the line holds Re τ elsewhere, or not at all. The rows' Re τ is then a further free number (or is fixed
  by the six through the line's T-orbit), and it is counted. The stage-4 map reads "Re τ and t, two free numbers, given
  the line".
- **S1 holds:** the height needs a content beyond the frame's own (W154's t), counted as one free number. **S1 fails:**
  the frame's own content holds the height at the line. The minimum's height is then reported and compared with the
  rows'.
- **S3** says how firmly Re τ is held, whichever way S2 goes.

## Weave or thread

The potential is weave-type (all parities, every field of the frame). The line is a counted choice, and the heights
are the rows', which the data's six chose. So this is a frame result at a counted line. Its claim is about where the
frame's own potential holds Re τ there.

## Pre-mortem

The likeliest outcome is a minimum at a fixed point of the mirror, X = 1 or X = 3.5, where V must be stationary. The
strip's rows sit at X ≈ 0.27–0.39 and their mirrors 1.61–1.73, at least 0.6 from both. So S2's prior is low.

## What stays out

- The ρ_Q sector with a line (Fay's formula; W59, and W167's scope note), and any content beyond the frame's own.
- Any target. No target file is read; the rows are positions only.
- The Higgs (stage 3) and the score (stage 5).

## Seen before the rule (disclosed)

- **W154's result, W167's result and scope note,** and the rows' positions (W156, W157).
- **Reasoning, not computation:**
  - the Poisson picture of the Re τ dependence (d_q = 0.2 for |q| = 2, 3 at a = 2/5);
  - the T-orbit of the five odd/10 lines;
  - the mirror as X ↔ 2 − X.
- **A slip corrected in the draft, by hand.** The draft first put the (2/5, ½) rows at X = x + 4 and the mirror at
  X ↔ 5 − X. Rederiving the T-law's direction from W167's kernel identity gave x + 1 and 2 − X, before anything was
  computed.
- **Not computed:** no value of V at any τ on this line. No script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read. A failed part is a failed launch, kept and disclosed.
- Any later check is labelled post hoc.

0 of 19.
