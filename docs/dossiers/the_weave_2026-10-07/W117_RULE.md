# W117 — a point on the line: do the weave's canonical functionals, extremized on each thread's closed geodesic, mark a point where the zero-dof quark assignments fit with two degrees of freedom, and is the tick's line special? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's choice** (2026-10-21), after W116: the three candidates in order, each done properly, then a pause to
  consolidate. This is the first: a point on the line. The first generation and a step beyond tree level come next,
  then the consolidation.
- **What W116 left.** With τ on any thread's closed geodesic up to length 8, W114's zero-dof quark assignments keep a
  fit with one degree of freedom to spare, on all 40 lines. A line is too weak a mark at the data's precision, so the
  seed would have to mark a point.
- **The question.** Does the weave mark a point on the seed's line?
- **What would count.** A quark fit with two degrees of freedom to spare at a point the principle marks on the tick's
  line, with a null in which the other threads' lines do worse. A fit alone would not count.

## The mechanism (fixed now)

- **Two ingredients, both on record.**
  - The seed's line (W116): τ lies on a thread's closed geodesic.
  - The weave's canonical functionals (W51), the functions of all three parities that every move keeps:
    - x_p = |θ_p/η|²;
    - e₁ = Σ x_p, e₂ = Σ x_p x_q, and e₃ = Π x_p = 4 (flat, so it marks nothing);
    - D = y|η|⁴;
    - N_T = y^{−1/2} Σ |θ_p²/η³|², and P_T = Π y^{−1/2} |θ_p²/η³|² = 16 D^{−3/2}.
- **Their direction is W51's.** e₁, e₂, N_T and P_T are energy-like: on F their least value is at ω. D is a partition
  function: its greatest value is at ω. P_T = 16 D^{−3/2}, so P_T's minima are D's maxima.
- **The marks.** On each line, a mark is every local minimum of e₁, e₂, N_T and P_T along the line, and every local
  maximum of D. These are the line's stable points under each functional: τ is held on the seed's line and settles
  where the weave's functional is extremal along it. The global ones are flagged.
- **Finding them.** One period of the line is sampled at 8000 points and each local extremum is refined by Brent's
  method. Marks closer than 10⁻⁶ on the modular surface count once: one period can cover a line's image twice, and
  functionals can share marks.
- **On a self-mirror line,** the two points where it meets a reflection line are CP-fixed, so every functional is
  critical there by symmetry, and J = 0 there (W116's S2). Its other marks come in CP-mirror pairs, whose fits are
  equal. One of each pair is fitted.
- **By hand, on the tick's line** (to be checked): F = Σ x_p² = 8 there (main's B1636). So e₂ = (e₁² − 8)/2 there, and
  e₁ and e₂ share their marks; and N_T = D^{−1/2} F = 8 D^{−1/2}, so N_T's minima are D's maxima. The tick's line
  therefore has two independent functionals, e₁ and D.

## Weave or thread

**A census of thread results, with weave functionals, labelled so.**
- **The functionals are the weave's** (W51: every move keeps them).
- **Condition 1 holds:** every thread up to length 8 is taken, as in W116 (69 words, 40 lines, 34 classes up to the
  CP mirror).
- **Condition 3 holds:** the claims (R4–R6) are about all the lines at once.
- **Condition 2 fails:** each mark depends on one thread's line.

## The fits (fixed now)

- **At a mark, τ is fixed.** W114's assignments 11, 13 and 14 then have 6 parameters for 8 observables, so 2 dof, and
  the pass mark is 5.99. Assignment 16 has 0 dof there and is read out at the tick's marks only, for compatibility.
- **The statistic of a line** is χ²_line, the least χ²_min over its marks and the three assignments. The null is p, the
  fraction of the 40 lines whose χ²_line is at or below the tick's. A line with more marks has more chances, so the
  null is conservative for a line with few.
- **The frame and the data** are W116's, unchanged: W114's frame, CP in the law (GENESIS GM5c, OPEN), W66's data and
  χ² at a = 0.10.

## The instrument (the script, written after this rule)

- **It reuses** W113's, W114's and W116's code, with W114's sectors replayed exactly (seed 114, in its order) and
  W115's solutions replayed exactly (seeds 1150 + n, then 115 + n), closed under the CP mirror as in W116.
- **The search at a mark, per assignment** (the census budget; seed 117 000 + 1000·(class index) + 10·(mark index)
  + j, with j = 0, 1 and 2 for 11, 13 and 14):
  - 3000 random coefficient vectors, drawn as in W114;
  - Nelder–Mead from the best 8 and from every warm start (the replayed solutions' coefficients), with at most 4000
    evaluations each, then again from the best 2 endpoints.
- **The tick's marks** are also read out with four times the random vectors and the starts. The null uses the census
  budget on every line.
- **Computation.** Worker processes, each search with its own fixed seed, so the result does not depend on the order
  in which they finish.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| R0 | the structure: the census as in W116; W51's closed forms at i and ω reproduced (to 10⁻⁸); e₃ = 4 at every mark (to 10⁻¹⁰); F = 8 on the tick's line (to 10⁻¹⁰); every mark is a critical point along its line (central difference at h = 10⁻⁵ below 10⁻⁶ of the functional's value) | 95% |
| R1 | the controls: W115's solutions are reproduced (τ to 10⁻⁶); synthetic quark data from assignment 14 at a mark of a line other than the tick's (seed 1171) is fitted back at that mark by the census budget to χ² ≤ 0.01 | 80% |
| R2 | J = 0 at every CP-fixed mark (\|J\| ≤ 10⁻¹⁴ for 20 random couplings of each of 11, 13 and 14) | 97% |
| R3 | the tick's marks are only its CP-fixed points, i and ½ + i√5/2 | 70% |
| R4 | **the tick fails:** no assignment reaches χ² ≤ 5.99 at any of the tick's marks, at either budget | 90% |
| R5 | the census: at least one line passes (χ²_line ≤ 5.99); read-out: every line's marks, which are CP-fixed, their family χ², and each passing mark's τ, J and functional | 40% |
| R6 | **the null:** p ≥ 0.05 | 90% |
| R7 | read-out: assignment 16 at the tick's marks (0 dof) | — |

## What the outcomes mean (fixed now)

- **R4 holds.** The seed's own line, settled by the weave's functionals, gives no quark fit. If R3 holds too, the
  reason is structural: the tick's marks are CP-fixed, and J = 0 there. A clean negative for the tick.
  - If other lines pass (R5), they are other threads' marks. Choosing one would be a hand-pick, a thread result,
    unless the principle names the thread. The pass rate is reported, and nothing is claimed.
  - If no line passes, no thread's line up to length 8, settled by the weave's functionals, holds the quarks with two
    degrees of freedom to spare.
- **R4 fails and R6 holds** (p ≥ 0.05). A mark on the tick's line holds the quarks, but so do enough other lines'
  marks. That is no evidence.
- **R4 fails and R6 fails** (p < 0.05). τ fixed by the principle (the seed's line and the weave's functional) holds
  the quarks with two degrees of freedom to spare, better than the other threads' lines.
  - That would remove τ's two numbers from the count: a candidate for two of the nineteen.
  - It goes to main for an independent check. The count stays 0 until main banks it.
- **In every case θ̄ = 0 stays tuned** (W114), and the coupling coefficients stay fitted.

## Seen before the rule (disclosed)

- **W116's whole record.** All 40 lines pass with one dof. The tick's best fits sit next to i (11 at 0.072 + 1.033i),
  and every line comes within 0.062 of a W115 solution.
- **W51's table** (the functionals' values at i and ω, and no other critical point on F), and main's B1636 (F = 8 on
  the tick's line).
- **The by-hand coincidences on the tick's line** stated above, from W51's definitions and B1636.
- **No functional has been evaluated along any line** by this seat, and no mark has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
