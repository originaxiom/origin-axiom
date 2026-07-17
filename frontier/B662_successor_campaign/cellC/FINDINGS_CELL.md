# CELL C — L103: the golden σ*-matrix repair — GAP REPAIRED

**Date: 2026-07-17. Campaign prereg: `../CAMPAIGN_PREREGISTRATION.md`
(CELL C clause, sealed first). All 14 decisive gates PASS. Exact
arithmetic (Fraction pairs over K = ℚ(√−3)) in every decisive step.
Run: `l103_repair.py` → `cellC_output.txt` (~17 min; the b637 prefix +
double_Y dominate).**

## What was repaired

B638 computed the deck-swap action σ* on the five H¹(D;27) classes of
the golden unbent weld double in-flight (b638_output.txt G2, sha256
5b3fe1ae…) but never persisted the matrix; only the silver's
`sigma_matrix_L.json` existed, and B660/S2 sealed
`deck_swap_accessible: false` (lead L103, OPEN_LEADS row 558). This
cell re-ran the identical B638 machinery on the identical B637 class
basis and persisted **`sigma_matrix_golden.json`** (sha256 715bc5f1…).

## The matrix (exact, K = ℚ(√−3), row convention σ*(repᵢ) = Σⱼ M[i][j] repⱼ mod B¹; σ* ANTILINEAR)

| | rep₀ | rep₁ | rep₂ | rep₃ | rep₄ |
|---|---|---|---|---|---|
| σ*(rep₀) | ζ₆ | 0 | 0 | 0 | 0 |
| σ*(rep₁) | (√−3)/24 | ζ̄₆ | 0 | 0 | 0 |
| σ*(rep₂) | 1256617152000+1267793856000√−3 | 268240896000 | −ζ₆ | 0 | 0 |
| σ*(rep₃) | −46189483200/13+465696000√−3 | 11176704000−11176704000√−3 | 0 | −ζ̄₆ | 0 |
| σ*(rep₄) | 1068480−514080√−3 | −6652800−6652800√−3 | 0 | 0 | 1 |

Basis = double_Y(None)'s reps (the first five nullspace vectors
independent mod coboundaries, construction order — deterministic; the
SAME basis every banked Y[ijk] table uses). Lower-triangular with the
Eisenstein-unit diagonal (ζ₆, ζ̄₆, −ζ₆, −ζ̄₆, 1) — B638's G2, now
machine-readable.

## Laws verified (all exact)

- **σ*² = id mod coboundaries**, 5/5 classes (cocycle level); u·conj(u)
  = +1 at SL(2); σ*(repᵢ) are cocycles 5/5.
- **conj(M)·M = I = M·conj(M)** — the matrix form of the antilinear
  involution (the C·conj(C) = I analogue banked in B638/B649); re-checked
  independently from the persisted JSON alone (round-trip).
- **M == the B638 in-flight printout**, all 25 entries — the record gap
  is a pure persistence gap, not a computation gap.

## The invariant cross-check vs the B660/S4 evaluator

Different presentations (B637's 4-generator weld amalgam vs S4's
3-generator plain double; no banked class identification — S4's own
sealed NOTE), so the comparison is at the invariant level:

- **Golden side (recomputed live, not parsed):** the full 10-slot Y
  table reproduced exactly (024-silent); the unique normalization-free
  invariant, the B645 unit cross-ratio (Y[023]·Y[134])/(Y[034]·Y[123])
  **= 1 exactly**; both 24ζ₆ identities (core + spectator) re-verified.
- **S4 side (its sealed exact s4_matrices.json, sha256 5854a85e…):**
  the Y-type tensor W = antisym(κ_k·M_ij) computed on ALL 10 triples
  (the sealed record sampled 4, all zero — reproduced). W is NOT
  identically zero: support exactly {034, 124, 134}. Its
  normalization-free lattice is TRIVIAL (incidence rank 3 = support
  size), so **the cross-ratio is not evaluable in the S4 presentation**
  — no product-level invariant collision is possible.
- **The basis-free invariant evaluable on BOTH sides — GL(5,ℂ)-orbit
  genericity (dual 2-form B with B∧B ≠ 0) — AGREES exactly**: both
  trivectors generic rank-4 (matches B660/S2's banked orbit type for Y).
- A re-run of the S4 evaluator itself is blocked in-repo: it requires
  `cell3_double/stage1_classes.pkl` from the seat workdir (not in the
  repo); the sealed exact output is the S4 side of record.

## HINT rows (recorded, unjudged — raw ratios/entries, NOT normalization-free)

- **S4 W[034]/W[134] = 24ζ₆ exactly** — the SAME 24ζ₆, in the SAME slot
  labels, as the banked golden spectator identity Y[034] = 24ζ₆·Y[134]
  (B645). W[034]/W[124] = −ζ₆.
- S4 W[134] = 1/24 − (1/72)√−3 = **conj(Y[134])** exactly (same slot).
- These rescale under per-class normalization (c₀/c₁ etc.), hence hint
  ledger only.

## Outcome (per prereg two-outcome clause)

**GAP REPAIRED** — matrix persisted (machine-readable, basis
documented), laws verified exactly, one invariant cross-checked at the
invariant level. L103's "basis-matched numeric cross-check" sub-item is
resolved to its honest maximum: basis-matching remains impossible
without a class identification (S4's sealed NOTE), and the invariant
lattice on the S4 side is provably trivial, so the basis-free orbit
invariant + the golden-side unit law are the complete comparison.

## Files

- `l103_repair.py` (sha256 df638ba9…) — the full computation.
- `sigma_matrix_golden.json` (sha256 715bc5f1…) — the deliverable.
- `cellC_output.txt` (sha256 b11adc12…) — verbatim run output.
