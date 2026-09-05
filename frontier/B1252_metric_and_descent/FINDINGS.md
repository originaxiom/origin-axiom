# B1252 — THE CARTAN METRIC ON THE B854 BASIS, AND THE DESCENT TO ONE SM GENERATION

**Status: banked (frontier). Verdict PROVED.** `verification/cartan_metric_and_descent.py`,
selftest green (rc captured directly, E39). Gate 5 clean: no measured value.

## Why this exists — an instrument the repo lacked, and an error it caused

The **B854 coordinates** used throughout the E₆ work are **not orthonormal**, and the repo carried
**no metric for them**. A naive dot product gives **seven distinct root lengths in a simply-laced
algebra** — so every "orthogonality" conclusion drawn that way is invalid.

**This seat produced exactly such an invalid conclusion in-session** — a claimed *"480 candidate
SU(3)×SU(2) embeddings and the object supplies no selector"*, reported as a wall in the SM descent.
**It is RETRACTED here.** It was wrong twice over: the metric was broken, **and** B873 had already
banked the answer (*"Winners on the completed menus: SO(10)×U(1), SU(5)×U(1), SM — unchanged and
unique"*, every rival killed by computation, citation-free).

## The metric

E₆ is simply-laced, so the correct form is the **unique** symmetric M with `αᵀMα` constant on all 72
roots. That linear system has **one solution and zero free parameters**, and it validates on two
conditions neither of which was imposed:

- **all 72 roots → length² = 2** (simply-laced, as required)
- **all 27 weights → length² = 4/3** (the 27 is minuscule: one Weyl orbit, one length)

## The descent, on the object's own weight data

| step | how |
|---|---|
| E₆ → SO(10)×U(1) | **FORCED** by the D₂ character's stabiliser (**B1250**; metric-free) |
| SO(10) → SU(5)×U(1) | A₄ subsystem — 20 roots, one component, closed |
| SU(5) → SU(3)×SU(2) | A₂+A₁ — 8 roots, components (2,6); 10 such subsystems |
| → hypercharge | Y = the orthogonal complement of A₂+A₁ (3-dimensional) |

and **exactly one** direction in the searched space grades the **16** into the Standard Model:

> **Y = [0, −5, −4, 5, −2, 2]** (scale 1/6)
>
> | field | mult | Y |
> |---|---|---|
> | Q (3,2) | 6 | **1/6** |
> | u^c (3̄,1) | 3 | **−2/3** |
> | d^c (3̄,1) | 3 | **1/3** |
> | L (1,2) | 2 | **−1/2** |
> | e^c (1,1) | 1 | **1** |
> | ν^c (1,1) | 1 | **0** |

**One complete Standard Model generation with correct hypercharges, on the object's lattice.**

## What this is NOT — stated before the result was seen, and kept

**This is not "the SM derived."** Once SU(3)×SU(2) is fixed inside SU(5), **hypercharge is unique up
to scale by standard Lie theory** — exhibiting it confirms **consistency, not novelty** — and the
scale 1/6 is a normalisation convention (B919's addendum, same session). Steps 2 and 3 are the
**unique winners B873 already banked**. The genuinely new content is **(a)** the metric, which did
not exist, and **(b)** step 1, which was an **input** before B1250 and is now **forced**.

**A candidate for making the descent object-forced was tested and REFUTED here.** If the object's own
weights supplied the characters cutting each level, the "fixed by hand" caveat would die. All 27
weight-characters were computed and compared against the **exhaustive** population of 63 non-trivial
mod-2 characters — **not** against a pool containing them, which was a first attempt's flaw:

| level | weight-derived | non-weight | |
|---|---|---|---|
| so(10) | 15/27 = 56% | 12/36 = 33% | +22% |
| su(5) | 16/27 = 59% | 16/36 = 44% | +15% |
| su(3)+su(2) | 9/27 = 33% | 19/36 = 53% | **−19%** |

Fisher p = 0.122 / 0.311 / 0.200, none surviving Bonferroni — **but the p-values are the wrong
instrument, since the 63 are the entire population, not a sample.** What decides it is the **sign
reversal at level 3**: a genuine selector would not flip direction at the final step. **The descent
is not object-forced by mod-2 characters.** Consistent with **B1225**, whose corollary states a
selector must use **β-odd or dimensionful** data — a mod-2 character is neither, and the failure is
now *measured* as well as predicted.

## Still missing, unchanged

The **values** (route through I-13, unpriced); **three generations** (this is one 16; B307 closed the
cyclic-cubic route); **cosmology** (B1194's one genuinely blind region).

## Dependencies

B854 (the basis), B883 (the 27 and the e₆ rep), B1250 (step 1), B873 (the unique winners),
B1225 (the selector theorem), B919 (the normalisation convention).
