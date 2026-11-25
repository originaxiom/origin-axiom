# B1988 card — the math decides PF5's loop: does the read-out act back, and which readings close?

Written 2026-11-25, before the run, at the author's word: "LET'S NOT CHOOSE AGAIN! LET THE MATH DECIDE". Main had asked
him whether PF5's "what is read from the whole takes part" means that the read-out acts back on the histories. That
was a choice main should not have offered. Data-free. 0 of 19.

## The statements to check (exact)

- **S1, the read-out acts back intrinsically.** The fibre's readings are the traces (x, y, z) = (tr a, tr b, tr ab).
  Each move forms the next reading from products of the current ones: L: (x, y, z) ↦ (x, z, xz − y), which is the trace
  identity tr(ab) = tr a · tr b − tr(ab⁻¹) (B18, B148). Checked symbolically on SL(2) matrices.
- **S2, the readings every history returns.** The points fixed by L and R together, over ℚ̄ (sympy) and over 𝔽_p for
  every prime p ≤ 47: exactly (0, 0, 0) (κ = −2, the common point) and (2, 2, 2) (κ = 2, "nothing").
- **S3, with the open moves carried both ways.** Adding the swap P (GM5c) leaves both points fixed. Adding the
  central sign actions on the characters (x, y, z) ↦ (−x, −y, z) and its two companions, which preserve κ (B28, B34; the
  weave's sign is GM5b, open), leaves only the common point.
- **S4, PF1.** κ = 2 is where cancelling completes (GENESIS §1, P008, B309), so existence excludes (2, 2, 2).

## Expectations

| id | expectation | prior |
|---|---|---|
| S1 to S4 | all hold | 0.97 (algebra done by hand before the card) |

## What it means if they hold

- **PF5's loop is decided by the math, not by a reading.** The read-out takes part and acts back by the moves' own
  form. The readings every history returns are exactly the common point and "nothing", and existence excludes
  "nothing". So the one self-consistent outcome is the common point, the whole's symmetric point.
- **It carries no values by itself** (B1881: a symmetric construction picks only the symmetric point). Values, if any,
  live in the unfolding around it, the flow away from it (P-630), which B1984 to B1987 described.
- **Nothing is compared with data.**
