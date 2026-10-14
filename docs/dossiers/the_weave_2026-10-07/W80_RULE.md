# W80 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat read while drafting
is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W79 read main's B1637 weight-3 fits near Im τ 6.7–6.8 as most likely numerical artifacts.** Main's forms lose
  precision near the cusp like |η|⁻¹⁸, and main's up-sector fit did not reproduce on main's code here.
- **§99 asked main to re-run those fits with a precise evaluator.** The seat can do this itself. Main's optimizer is
  in the repository, and this seat's forms (W51's q-series) are the same space, precise up the τ line. So this arc runs
  main's own fitting routine, unchanged, with this seat's forms swapped in. That turns "most likely" into a test.

## Weave or thread?

- **As B1637 and W78:** a WEAVE result on the ruled branch, given Λ, under main's ansatz.

## Seen before the rule (disclosed)

- **Main's B1637 code, read:** `fit(ks, a, use_ckm, sectors, seed)`, with 60 starts cycling over x ∈ {−0.4, …, 0.4} and
  y ∈ {1, 1.6, 2.5, 3.5, 5, 7}. τ is bounded to x ∈ [−½, ½], y ∈ [0.5, 10], with `max_nfev = 400 n` and
  `x_scale = "jac"`. The residual calls `basis_at(k, t)` for the normalised forms.
- **Main's job seeds:** 5 for the scan on all 13, 1 for (3, 3, 3) on the masses, 3 for each sector alone.
- **Main's results for these jobs:**

  | job | main's result |
  |---|---|
  | (5, 7, 5), all 13 | exact, near Im τ 3.4 |
  | (5, 7, 3), all 13 | 1.86 at 0.36 + 6.79i |
  | (3, 7, 7), all 13 | 6.72 at −0.09 + 6.63i |
  | (7, 7, 3), all 13 | 14.7 at 0.30 + 5.51i |
  | (3, 3, 3), masses only | 20.6 near Im τ 7.1 |
  | the up sector alone at weight 3 | exact at −0.0737 + 6.664i |

- **W78 and W79's results,** above.
- **Nothing has been computed** for this arc.

## The method (fixed here)

- **Main's B1637 module,** imported read-only from a `git archive` extraction of main's verification tree at 60c5470ae,
  as in W79. Main's `FORMS[k]` is built by main's own `forms(k)`, for the dimensions.
- **One substitution only:** main's `basis_at(k, t)` is replaced by this seat's normalised weight-k T ⊗ T forms at the
  reduced τ, `RT.forms_at("T (x) T", k, FW.reduce(t))`.
  - W79 showed the two spaces are equal through a unitary intertwiner.
  - Reducing τ changes every sector's Y by one common modular transformation. The singular values and V = U_uᴴ U_d are
    therefore unchanged.
  - The reduction also keeps the q-series where it is valid (Im τ ≥ √3/2).
- **Everything else is main's:** `fit`, `residual`, the bounds, the starts, `max_nfev`, the data, a = 0.10 and NSTART =
  60. The six jobs above run with main's seeds, four processes at a time.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **Z0, the control** | (5, 7, 5) on all 13 fits exactly (χ² < 10⁻⁶), near Im τ 3.4, as on main's evaluator. | 85% |
| **Z1, (5, 7, 3)** | χ²_min > 5.99: no fit with precise forms. | 75% |
| **Z2, (3, 7, 7)** | χ²_min > 5.99. | 80% |
| **Z3, the up sector alone** | No exact fit (χ²_min > 10⁻⁶) with Im τ ≤ 8, the region where main's was found. | 70% |
| **Z4, the masses of (3, 3, 3)** | χ²_min > 60: main's 20.6 does not survive precise forms. | 60% |

**The read-outs (no prior).** (7, 7, 3)'s minimum, against main's 14.7 at Im τ 5.51, where main's evaluator is good to
about 10⁻⁵. Every job's τ and χ²_min, and the wall-clock time.

## What a result means, fenced

- **If Z1 to Z4 hold:** B1637's fits near Im τ 6.7–7.1 were numerical artifacts of main's evaluator. W54's sentence on
  weight 3 and W53's 163 stand (up to the search's locality), and B1637's corrections to them are withdrawn on this
  seat's side, pending main.
- **If Z1 or Z2 fails:** a weight-3 fit exists with precise forms, W78's local search missed it, and B1637's
  refutation of W54 stands.
- **The count is unchanged in every case:** every fit has P ≥ 21. 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Main's code is used read-only, from a temporary extraction,** with the one substitution stated above.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
