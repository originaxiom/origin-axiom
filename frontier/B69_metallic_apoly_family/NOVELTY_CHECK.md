# B69 novelty check — the cusp-torsion law is NOT new (within established theory)

**Date:** 2026-06-04. **Status:** literature check, committed. Resolves the "novelty OPEN" flag on
B69 (V35/V39). Verdict: **STANDARD_REPACKAGE** — the cusp-torsion law is within the well-established
character-variety theory of once-punctured torus bundles; it is **not a new theorem**.

## What the literature says

The metallic mapping tori `φ_m²` are **once-punctured torus bundles with tunnel number one** — exactly
the class whose character varieties are determined in:

> **K. Baker, K. Petersen, "Character varieties of once-punctured torus bundles with tunnel number
> one," Internat. J. Math. (2013), arXiv:1211.4479.**

They determine the SL₂(ℂ) and PSL₂(ℂ) character varieties of these bundles as **plane-curve models in
trace coordinates**, identify them up to birational equivalence with smooth models, **compute the
genera of the canonical components**, and **determine the minimal polynomials of the trace fields**.
This is the same framework B69 / V33 operate in (the `F_m(x,κ)` plane curves, their genus, and the
trace fields). Ideal points of such character varieties are the standard objects of **Culler–Shalen
theory** (and Tillmann's limiting characters), which detect essential surfaces / boundary slopes.

## The verdict

- **The cusp-torsion law is an explicit instance, not a discovery.** The cusps of `F_m(x,κ)` (poles of
  the boundary trace κ, i.e. ideal points) at `x=2cos(π/k)` are: (i) ideal points of these character
  varieties (a Culler–Shalen object, already studied for this exact family by Baker–Petersen), located
  at (ii) the **torsion trace values** `2cos(π/k)` — the standard trace of an elliptic element of order
  `2k` (where the generator `a` becomes finite-order and the boundary trace degenerates). Both
  ingredients are textbook.
- So B69's `F_m`, its genus (V33), and the cusp-at-`2cos(π/k)` pattern are a clean **re-derivation
  within known theory** — at most a pedagogical/explicit observation, **not novel mathematics**.
- *(Caveat: the Baker–Petersen PDF would not parse for a line-by-line check of whether the exact
  `2cos(π/k)` cusp statement appears verbatim; but the framework — these character varieties, their
  ideal points, genera, and trace fields — is unambiguously established for this family, so no novelty
  claim is warranted regardless.)*

## Disposition

B69 is **re-labeled STANDARD_REPACKAGE**: a verified (m=1…6) computer-assisted observation that is a
**special case of the Baker–Petersen / Culler–Shalen theory** of once-punctured torus bundle character
varieties. Keep the computation (it's correct and a nice explicit cross-check); **drop any novelty
framing**. The m=1 figure-eight A-polynomial (B67) remains the one PROVED, genuinely-cross-validated
piece; the family extension is standard.

**Sources:**
- Baker–Petersen, *Character varieties of once-punctured torus bundles with tunnel number one*,
  arXiv:1211.4479 / Internat. J. Math. 24 (2013).
- (context) Projective rigidity of once-punctured torus bundles, arXiv:2411.04431; Tillmann limiting
  characters / Culler–Shalen ideal-point theory.
