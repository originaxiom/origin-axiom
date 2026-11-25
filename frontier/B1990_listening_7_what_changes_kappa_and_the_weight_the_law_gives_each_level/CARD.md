# B1990 card — listening 7: what changes κ, and the weight the law's own counting gives each frustration level

Written 2026-11-25, before the run, in the author's /loop "continue the listening line". The mathematics decides; no
choice is offered. Data-free. 0 of 19.

## The question

- **B1988 and B1989:** the one self-consistent outcome is the common point at κ = −2, and the whole's bound states sit
  at quantised κ. The flow away from the common point stays on its leaf if nothing in the grammar changes κ.
- **What changes κ?** And if nothing does, what weight does the law ("everything allowed happens, it does not weigh
  them") give each level?

## The checks (exact)

- **K1:** every move the grammar has or leaves open conserves κ: L, R, their inverses, the swap P (GM5c), and the
  central sign actions (GM5b's candidate). Checked symbolically.
- **K2:** the non-invertible endomorphisms (B497's strata 2 to 4: squaring, period doubling, Thue–Morse, degenerate)
  change κ by κ′ − 2 = (κ − 2)·M. These are B497's laws, recomputed symbolically. None is a move of the grammar
  (GENESIS § 2; the words are Sturmian, B1676).
- **K3:** κ − 2 = tr[a, b] − 2 is the remainder of cancelling ab·a⁻¹b⁻¹ (PF1's frustrated cancellation; P008). Checked
  symbolically: tr(aba⁻¹b⁻¹) = x² + y² + z² − xyz − 2.
- **K4, the law's counting:** with every reading counted once, a level's weight is its number of readings. For every
  prime p ≤ 47 and every κ ∈ 𝔽_p, count #X_κ(𝔽_p), the points with x² + y² + z² − xyz − 2 = κ.
  - Describe the distribution: which κ carry the most and the fewest readings.
  - Describe the cusp's and "nothing"'s counts against p², and the correction's form.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| K1 to K3 | hold exactly | 0.97 |
| K4a | the cusp's leaf has p² + 3(−1/p)p + 1 points (the Legendre symbol (−1/p) = ±1) | 0.6 (from B1983's counts 41, 29, 89, 209) |
| K4b | none: the table of counts is the result | — |

## What it means

- **If K1 to K3 hold:** nothing in the grammar changes κ. Each frustration level is a sector of the whole, and the whole
  is all of them at once (κ ≠ 2).
- **K4:** the weight the law itself gives each sector, with nothing chosen.
- **Nothing is read as physical, and nothing is compared with data.**
