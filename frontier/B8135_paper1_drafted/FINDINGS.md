# B8135 — Paper I is drafted — the period-one locus, and a selection that sees only the trace

**Date:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical identification; no Standard-Model quantity appears.

## What was done

Drafted **Paper I** of the four-paper series: `papers/series/paper1_characterization/` — 7pp, builds
with 0 overfull boxes and 0 undefined references, verification **15/15**.

## The result, and how it improved on its source

The 52pp source paper proves `det(A²−I) = −m²` via `χ_A(1)·χ_A(−1)`. **That fixes only the ORDER of
the cokernel** — on that information the torsion could a priori be cyclic `ℤ/m²`.

Cayley–Hamilton gives the integer-matrix identity **`A² − I = mA`**, and since `A ∈ GL(2,ℤ)` is
invertible *over ℤ*, `A·ℤ² = ℤ²`, so

    coker(A² − I) = ℤ²/(mA)ℤ² = ℤ²/mℤ² ≅ ℤ/m ⊕ ℤ/m

**exactly** — the invariant factors, not merely the order. Unimodularity is what does the work.
**Found while rewriting a proof I had first written muddled.**

Also: the period-one locus is exactly `det = −1`; the primitive `GL(2,ℤ)` class is unique for
`m ≤ 5`, with **`m = 6` the first repetition**.

## Verification

`verify/check_locus.py`, 15 checks in four groups. The one that matters is C2: it enumerates
**every** integer matrix of determinant `−1` in a bounded box — **896 of them, traces 1–26** — not
only the representatives `X_m`. That is what makes the trace-only corollary a verified statement
rather than a restatement of the algebra. Control: the identity must **fail** for `det = +1`, and
does.

## SCOPE

- Says **nothing** about the passage from a substitution rule to an oriented 3-manifold; that step
  needs typed data and is `OA-C0003`, **CONDITIONAL**.
- Class uniqueness holds for `m ≤ 5` only.
- An independent count reports 2 primitive classes at `m = 12` where this gives 3. **UNRESOLVED,
  stated in the paper as a remark, not load-bearing** — both agree on `m = 1…11` and the threshold
  claim concerns the *first* repetition.

## Correction recorded

`SERIES_PLAN.md` claimed Paper I answers the question map's `geometry` domain (17 questions). **All
17 are algebraic geometry of heterotic bundles — not one is hyperbolic geometry.** I matched the
word and never opened the rows: *reading a label as a result*. Paper I's real anchors are
`OA-C0001` (REFUTED), `OA-C0002` and `OA-C0003` (CONDITIONAL) — **none PROVED**, and the paper's
Appendix B says so.

**Gate 5 untouched.** No physical identification anywhere in the paper.
