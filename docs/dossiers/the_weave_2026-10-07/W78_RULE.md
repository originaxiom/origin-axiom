# W78 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat read while drafting
is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **Main asked for it.** Main's relay `CC_TO_SM_AND_CODEX_2026-10-14_B1637_GRADED_AND_YOUR_W54.md` refutes one
  sentence of W54: "every structure with a sector at weight 3 fails".
  - Main's B1637 fits T ⊗ T (5, 7, 3) at χ² = 1.86 near τ ≈ 0.36 + 6.79i.
  - It finds (3, 7, 7) at 6.72 near τ ≈ −0.09 + 6.63i.
  - It asks: "Can your grid be refined near Im τ ≈ 6–7 to check (5, 7, 3) independently?"
- **The refuted sentence covers every structure with a sector at weight 3,** sixteen in T ⊗ T. So this arc checks all
  sixteen in the region W54 never searched, with main's two as named cells.

## Weave or thread?

- **As W54:** a WEAVE result on the ruled branch, given Λ. The modular structure, the data and the predicate are W54's.

## Seen before the rule (disclosed; this matters here)

- **Main's numbers,** above, from its relay and commit message. They include the τ of both fits.
- **W54's stored output.** Its (5, 7, 3) minimum is χ² = 140.2 at τ ≈ −0.096 + 1.867i, not on its box's edge.
- **W54's box.** Its search, like W53's, stopped at Im τ = 6 (`FW.YMAX = 6.0` in `the_fit_at_the_geometrys_weight.py`).
  Main's search ran to Im τ = 10.
  - So W54 could not have found main's fits at any grid resolution: they lie outside its box. The refutation comes
    from the box, not the grid. This is the seat's reading, from the code, before any run.
- **Nothing has been computed** for Im τ > 6.

## The method (fixed here)

- **W54's model, data, tolerance and residuals, imported unchanged** from `the_rank_thirteen_structures.py` and
  `the_fit_at_the_geometrys_weight.py`. The threshold is a = 0.10, and a structure fits if χ²_min ≤ 5.99.
- **The sixteen structures:** T ⊗ T with (k_u, k_d, k_e) ∈ {3, 5, 7}³, at least one weight 3, and (k_u, k_d) ≠ (3, 3).
- **The window:** x ∈ [−0.5, 0.5] in 11 steps, and y ∈ [5, 10] in 16 geometric steps, giving 176 grid points. It
  overlaps W54's box on [5, 6] and extends to main's bound.
- **Stage 1, as W54's.** At each grid τ, fit the quark part for each of the eight quark pairs (k_u, k_d) ≠ (3, 3) with
  16 starts, and the lepton part for each weight 3, 5 and 7 with 8 starts. The seeds are (7800, the pair's or
  weight's index, the grid index). Each structure's grid value is Q + E.
- **Stage 2, as W54's.** Refine τ and every α jointly with bounded least squares (x ∈ [−0.5, 0.5], y ∈ [5, 10],
  max_nfev 1500), from each structure's 8 best grid points. Keep the best.
- **A read-out using main's result, labelled.** For (5, 7, 3) and (3, 7, 7), refine once more from main's τ, with the
  α of the nearest grid point's best. This is not the independent check: the grid route is.
- **The control.** W54's ten shape observables for (5, 7, 3) at random α, at τ = 0.2 + 6.5i, −0.3 + 8i and 0.4 + 9.5i,
  unchanged under τ → τ + 1 and τ → −1/τ to 10⁻⁸. This checks the forms far up the τ line.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **N0, the control** | The shape observables are unchanged under both moves to 10⁻⁸ at the three points. | 90% |
| **N1, (5, 7, 3) fits** | By the grid route alone, χ²_min ≤ 5.99, at Im τ in [6.3, 7.3]. | 80% |
| **N2, (5, 7, 3) as low as main's** | By the grid route alone, χ²_min ≤ 2.9 (main's 1.86 plus one). | 65% |
| **N3, (3, 7, 7)** | By the grid route alone, χ²_min > 5.99 in the window: it does not fit. | 55% |
| **N4, the quarks at weight 3** | No structure with a quark sector at weight 3 has χ²_min ≤ 5.99 in the window, other than (3, 7, 7) if N3 fails. | 60% |

**The read-outs (no prior).** Every structure's χ²_min, τ, P, its pulls and the grid's best; whether any minimum is on
the window's edge; and the refinements from main's τ.

## The reading, written before the run (predicted)

- **W54's sentence fails, as main found:** with the leptons at weight 3, (5, 7, 3) fits far up the τ line. The reason
  is W54's box, not its grid.
- **Whether the geometry's weight is excluded as the quarks' weight** depends on N3 and N4. (3, 7, 7) sits near the
  threshold on main's search.
- **The count is unchanged either way.** Every fit has P ≥ 21 for 13 numbers, so it predicts nothing. 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
