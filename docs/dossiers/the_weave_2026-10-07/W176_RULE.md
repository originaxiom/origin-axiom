# W176 — the web seat's question 3, as the weave sees it: a forced condition on the line can see only its order N, so the class is chosen, if at all, by the dynamics. Given N, where does the frame's own potential put (τ, line) over every line of order N: at finite height, CP-fixed or not, and in the six's band? (the rule, committed before the script)

The SM-derivation seat, 2026-10-28, at the owner's "GO" on this seat's open items. Committed and pushed before the
script that reads it exists. Nothing here is a result.

## Why

- **The web seat's question 3** ("THE CLASS AND THE END", 422cd8ecd; relays §322 and §323). Is there a consistency
  condition that selects the line's class? Its candidates are a bundle condition over the mapping torus, θ's monodromy,
  and a Green–Schwarz-type cancellation.
- **What the record already fixes (W140, C1).** The moves jointly fix only the trivial line, and they act transitively
  on the lines of each exact order N.
  - So any condition on the line that the weave forces sees only N.
  - The bundle condition over the whole weave, that every thread fixes the line, gives N = 1. A single thread γ fixes
    lines whose order divides |tr γ − 2|, which is a thread result.
  - W101's anomaly constrains the dictionary and the weights, not the line.
- **So within an order, the class is the dynamics' to choose.** The frame's potential is modular-invariant when τ and
  the line move together. Over every line of order N and τ in the fundamental domain F, its least is its least on the
  order-N modular curve.
  - W175 held the class fixed and found the height pushed down to the domain's edge. Below that edge the same
    configurations are other lines at other τ. Letting the line move within its order is the weave's own form of the
    question.
- **For THE RIDDLE's open items:**
  - if the least sits at finite height, the potential holds the height given N, which is P-287's C6 in its weave form;
  - if it is CP-fixed, horn 1 returns at the weave level;
  - if it sits in the six's band, the band is selected.

## The computation (fixed now)

- **The orders.** N = 1 to 12, 15, 20, 25 and 30. For each, every line (a, b) ∈ (ℚ/ℤ)² of exact order N, up to sign.
- **The potential.** W172's kernel and content: W59's joint-parity kernel at s = 3, N_lat = 48, W67's fields with the
  bosons' weight 1, ψ = (−a, b).
- **The domain.** τ ∈ F: |Re τ| ≤ ½, |τ| ≥ 1, Im τ ≤ 4. A grid in steps of 0.05 in Re τ and 0.1 in Im τ, plus the arc
  |τ| = 1 at 21 points, on every line. Then, per N, a bounded refinement (L-BFGS-B, staying in F) from the five least
  grid points.
- **The CP test at the least, exact.** The mirror sends (τ, ψ₁, ψ₂) to (−τ̄, ψ₁, −ψ₂) (W172's lemma).
  - The least is CP-fixed when the mirror image is the same configuration up to SL(2, ℤ) and the sign of the line.
  - Inside F that needs τ on Re τ = 0, on Re τ = ±½ (with T) or on |τ| = 1 (with S), within 10⁻⁶. The line must then
    map to itself up to sign. Here V(γτ; ψ) = V(τ; ψ̃) with ψ̃ = (pψ₁ − rψ₂, −qψ₁ + sψ₂) for γ = (p q; r s), from
    the kernel's lattice sum, and the test is done exactly in Fractions.
  - **The test's controls** (instrument checks, not cells): (0, 1/N) at Re τ = 0 must test CP-fixed, and a mirror-free
    slope-2/5 line at Re τ = 0.3 must test not fixed.
  - At i and ω the stabiliser's elements are tried too.
- **J at the least,** where the frame's column covers it (Im τ ∈ [1, 4]): `own_point` at the least's line and τ,
  L_max, readings (S̃, S). Otherwise it is recorded as not defined in the frame.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **Transitivity (exact).** For each N listed, the orbit of the line (0, 1/N) under L and R on (ℤ/N)² is every point of exact order N | 99% |
| K1 | **A mirror-fixed configuration at every order (exact).** The line (0, 1/N) at Re τ = 0 is mirror-fixed: (0, 1/N) ↦ (0, −1/N), its own negative. So no condition on the line alone can exclude CP-conserving configurations at any order | 99% |
| K2 | **The height is held given N.** For every N ≥ 2 listed, the least over F and the order's lines lies below Im τ = 3.9, away from the cusp edge | 85% |
| K3 | **The least is CP-fixed (decisive).** For every N listed, the least configuration is mirror-fixed by the exact test | 50% |
| K4 | **Not in the six's band.** For no N does the least lie at 2 ≤ Im τ ≤ 4 | 85% |
| R | **Read-outs** (no predictions): per N, τ*, the line, V*, the CP status, J where defined, the second-least distinct configuration and its gap; the order with the least V* overall; whether any least sits on a slope-2/5 line | — |

## What the outcomes mean (fixed now)

- **K0 and K1 hold:** the answer to question 3 at the consistency level is exact. A weave-forced condition sees only
  the order and cannot prefer a mirror-free class. Within an order the class is the dynamics' choice.
- **K2 holds:** given N, the frame's own potential holds τ at a finite height on the modular curve. That is a holder of
  P-287's C6 kind, conditional on N, which the weave does not force (only N = 1 by the bundle condition).
- **K3 holds:** horn 1 returns at the weave level. Given only the order, the potential chooses a CP-conserving
  configuration.
- **K3 fails at some N:** the potential with only the order given breaks CP spontaneously there, an orbit of two. That
  is the strongest form of W175's finding: no class is chosen by hand.
- **K4 fails at some N:** the potential, given only N, places τ in the six's band. That N becomes the next arc's
  target, sealed, with its line compared with the data's carriers.

## Weave or thread

- Per N, a WEAVE result. It takes every line of order N, none hand-picked, which is the only distinction the moves make
  (W140). Its quantity is the potential, which is weave-type. Its claim is about all lines of the order at once.
- The order N is a stated parameter reported separately for each value. It is not forced: the bundle condition over
  the whole weave gives only N = 1.

## What stays out

- s = 4, other contents, and W172's variations.
- Orders other than those listed.
- Any data comparison: no target is read, and the six's band enters only as an interval of Im τ.

## Seen before the rule (disclosed)

- W140's C1, W175's output and its post hoc, the web seat's relay, and W101's cells.
- K0 and K1 were derived by hand.
- Not computed: no potential on any line at Im τ < 1.2, and no joint least over lines.

## Discipline

- This rule is committed and pushed before the script exists.
- One run. Its output is committed before it is read. The only checks before that are the exit, failures, NaN, paths
  and warnings.
- Any later check is labelled post hoc.

0 of 19.
