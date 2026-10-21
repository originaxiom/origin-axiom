# W116 — the seed's marks: does putting τ on a thread's closed geodesic leave a quark fit with a degree of freedom to spare, and is the tick's geodesic special among the threads'? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's choice** (2026-10-21), after W115: the seed sets the departure.
- **What W112–W115 left.** Every forced choice in the record's frames lands on a symmetric point, and the data live in
  the departure from it. Main's P-224 (no stabilizer point fits) and P-225 (the seed as the non-stabilizer resource)
  say the same from the other side.
- **The question.** Does the seed, entering through a mechanism fixed here before any comparison, set the departure?
- **What would count.** A quark fit with a degree of freedom to spare on the seed's own mark, and a null in which the
  other threads' marks do worse. A fit alone would not count.

## The mechanism (fixed now)

- **A thread's mark is its closed geodesic.** A thread is a word w in the grammar's moves L = ((1,0),(1,1)) and
  R = ((1,1),(0,1)) (the record's matrices, as in `the_arena_check.py`). Its matrix M(w), the product in the word's
  order, is hyperbolic once both letters occur.
- **The axis** of M(w) is the one geodesic in the upper half-plane that M(w) maps to itself. Its image on the modular
  surface is the thread's closed geodesic, of length ℓ(w) = 2 arccosh(|tr M(w)|/2).
- **The constraint.** τ lies on that line. It removes one of τ's two real numbers. The point along the line is one
  fitted real number.
- **Why the line and not a point.** An axis has no point of its own. The points the line meets the reflection lines
  Re τ = 0, Re τ = ½ and |τ| = 1 at are CP-fixed, so J = 0 there (cell S2). Any CP-violating fit on the line is
  therefore a departure from those points, set by a fitted number. The seed fixes the line, not the point.
- **The tick's line.** The word LR (main's B1629: the lowest closed geodesic; B1630: through the tick's point i).
  Its axis is the circle of centre ½ and radius √5/2. In the fundamental domain F it is the arc
  τ(x) = x + i·√(5/4 − (|x| − ½)²), x ∈ [−½, ½], with Im τ between 1 and √5/2, covered twice by one period of length
  4 ln φ. B1636 found the golden spectrum there.

## Weave or thread

**A census of thread results, labelled so.**
- **Condition 1 holds.** Every thread up to length 8 is taken under the stated rule below, with none hand-picked.
- **Condition 3 holds.** The claims (S4–S6) are about all the lines at once.
- **Condition 2 fails.** The quantity, a fit on one line, is defined by one thread's matrix, not by the joint action.
- **Why it cannot be a weave result (a READING).** The joint action of every move has no invariant line: the closed
  geodesics of all the threads together are dense on the modular surface. So the weave as a whole marks no line, and
  only a thread does. The minimum over all lines up to a length is a constraint taken from every thread at once, but
  it has no canonical cutoff, and as the cutoff grows it becomes no constraint at all. The run reports it as a read-out.
- **The tick's line read alone** would be a thread result: LR is the figure-eight's monodromy, the glossary's object.
  Here it is one row of the census, and the null asks whether it is special.

## The census (fixed now)

- **The words.** Every primitive cyclic word in L and R with both letters, of length 2 to 8. Primitive means not a
  proper power, and cyclic means up to rotation. By hand there are 69 (2: 1, 3: 2, 4: 3, 5: 6, 6: 9, 7: 18, 8: 30).
  Words with one letter are parabolic and have no closed geodesic.
- **The lines.** M(w)ᵀ is the matrix of the reversed mirror word (L ↔ R, read backwards), and Mᵀ is conjugate to M⁻¹
  in SL(2, ℤ). So w and its reversed mirror trace the same line with opposite orientations. A sign ±w does not move
  the axis either. By hand the 69 words trace **40 distinct lines**. Each line counts once.
- **The CP mirror.** Under τ ↦ −τ̄ the line of w goes to the line of its mirror. CP in the law makes every observable
  equal at mirror points, so mirror lines have equal fits. By hand 28 lines are their own mirrors and 6 pairs are not,
  which gives **34 classes**.
  - One line per class is fitted: the one whose least rotation is lexicographically least, with L < R.
  - Its mirror takes its values. The run checks the equality pointwise on one pair (S0).
- **The parametrization.** On the axis with centre c and radius ρ, τ(s) = c + ρ·e^{iθ(s)}, with θ(s) = 2 arctan(e^{−s}),
  where s is the hyperbolic arc length from the top. The observables are SL(2, ℤ)-invariant, so they are periodic in s
  with period ℓ(w). The fit takes s modulo ℓ(w) and evaluates at the image of τ(s) in F.

## The frame (unchanged)

W114's, as W115 used it: W101's hypotheses, CP in the law (GENESIS GM5c, OPEN), the Dedekind counterterm, tree level,
the ruled branch's holomorphic couplings, the quark sector, W66's data and χ² at a = 0.10.

## The assignments (fixed now)

- **Fitted on every line:** W114's three compatible assignments with no degree of freedom, 11, 13 and 14.
  - With τ on a line they have 7 parameters for 8 observables, so 1 dof, and the pass mark is 3.84.
  - **The family statistic** of a line is χ²_fam = the least χ²_min over the three. It is taken on every line alike,
    so the null below carries the look-elsewhere count over the assignments.
- **Read-out on every line:** assignment 16, which has −1 dof on a line, scored for compatibility only.
- **Not fitted, by implication (cell S3).** Restricting τ to a line can only raise a minimum, and it adds one degree
  of freedom, so the pass marks rise to 7.81 (3 dof) and 11.07 (5 dof).
  - W114's assignments with dof ≥ 1 had χ²_min ≥ 47.9, and its assignment 15 had 8.18 for 0 dof.
  - W113's forced assignment had 104 for 2 dof.
  - Each stays above its new pass mark on every line. This rests on those searches. W115 found that one of them
    (W114's 14) had stopped at a local minimum, so the implication is only as strong as the searches.

## The instrument (the script, written after this rule)

- **It reuses W113's and W114's code** (`the_strong_angle.py`, `the_tuned_fit.py`, imported), with W114's sectors
  replayed exactly (seed 114, in its order).
- **The warm starts.** W115's solutions are replayed exactly: W114's searches (seeds 1150 + n), then W115's (seeds
  115 + n). That gives every solution's coefficients for 11, 13 and 14, and W114's best point for 16. For each
  solution and each line, the point of the line nearest to the solution in F gives one start, at the solution's
  coefficients.
- **The search, per line and assignment** (the census budget). The seed is 116 000 + 10·(class index) + j, with
  j = 0, 1, 2 and 3 for 11, 13, 14 and 16; the tick's larger read-out uses 117 000 + j.
  - 6000 random points: s uniform in one period, the free vectors normal as in W114;
  - Nelder–Mead from the best 15 random points and from every warm start (at most 6000 evaluations each), then again
    from the best 3 endpoints.
- **The tick's line, read out again** with five times the random points and four times the starts. The null uses the
  census budget on every line, the tick's included, so that no line is searched harder than another.
- **Computation.** Searches run in parallel processes, each with its own fixed seed, so the result does not depend on
  the order they finish in.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| S0 | the structure: the census has 69 words, 40 lines and 34 classes; each axis is invariant under its word's matrix (to 10⁻¹⁰); M(w)ᵀ equals the reversed mirror's matrix exactly; B1636's golden spectrum (1 : φ⁻¹ : φ⁻² for T⊗T at 1) holds at 64 points of the tick's line to 10⁻¹⁰; on one mirror pair the observables of assignment 14, at a random coupling, agree at mirror points to 10⁻⁹ | 95% |
| S1 | the controls: W115's solutions and W114's point for 16 are reproduced (τ to 10⁻⁶); synthetic quark data from assignment 14 at a random point of a random line other than the tick's (seed 1161) is fitted back on that line by the census budget to χ² ≤ 0.01 | 80% |
| S2 | the line's own points: at the tick's two CP-fixed points, i and ½ + i√5/2, J = 0 (to 10⁻¹⁴) for 20 random couplings of each of 11, 13 and 14 | 97% |
| S3 | the implication: every assignment not fitted here (W113's forced one; W114's 1–10, 12 and 15) has a recorded χ²_min above its pass mark on a line | 99% |
| S4 | **the tick:** no assignment passes on the tick's line (χ²_min > 3.84 for each of 11, 13 and 14, at either budget) | 85% |
| S5 | the census: at least one line passes for the family (χ²_fam ≤ 3.84); read-out: the number of lines that pass, each line's χ²_fam and its distance in F to the nearest W115 solution | 70% |
| S6 | **the null:** p ≥ 0.05, where p is the fraction of the 40 lines, the tick's included, whose χ²_fam is at or below the tick's (at the census budget) | 85% |
| S7 | read-out: assignment 16 on every line (the number of lines with χ²_min ≤ 10⁻⁶) | — |

## What the outcomes mean (fixed now)

- **S4 holds.** The seed's own line does not hold the observed quarks with a degree of freedom to spare in this frame.
  The tick sets no departure here. S5 and S6 then say whether any thread's line does.
  - If lines pass, they are other threads' marks. Choosing one would be a hand-pick, a thread result, unless the
    principle names it. Nothing is claimed.
  - If none passes, no thread's mark up to length 8 holds the quarks with a dof to spare.
- **S4 fails and S6 holds** (p ≥ 0.05). The tick's line holds the quarks, but so do enough other lines. That is no
  evidence, as in W112.
- **S4 fails and S6 fails** (p < 0.05). The seed's own line holds the quarks with one degree of freedom to spare, and
  better than the other threads' lines.
  - That would be the frame's first quark fit with a degree of freedom confirmed on a place the principle marks: a
    candidate for one of the nineteen.
  - It goes to main for an independent check. The count stays 0 until main banks it.
- **In every case the point along the line is one fitted number, and θ̄ = 0 stays tuned** (W114). The most this arc
  can do is remove one of τ's two numbers.

## Seen before the rule (disclosed)

- **W115's whole record,** including every quark solution's τ.
- **A hand computation.** At each W115 solution's Re τ, the tick's line in F lies below it in Im τ. The nearest is
  assignment 11's solution at 0.0513 + 1.0679i, which is 0.044 above the line. The others are 0.06 to 0.57 away. So
  the tick misses every solution the record has, and S4's prior reflects that. No other line was located against the
  solutions.
- **Main's B1636,** read today: the golden spectrum on the tick's line, and its controls on five other lines.
- **The census counts** (69, 40, 34) were computed in scratch, on words alone.
- **No quark fit with τ on any line** has been run, by this seat or, as far as this seat knows, anywhere on record.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
