# B1808 (P-419, frame F2h) — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back (the referee could not write report files). Its checks are q1–q6 beside this
file; they are independent of main's code (a sympy and PARI matrixqz kernel; its own wedge; points counted exactly from
Gram matrices).

**Verdict:** BLOCK on one finding (the hand clause). The NEGATIVE passes. PASS WITH CORRECTIONS once B1 is reworded and
C1–C7 are applied.

## Verified

- Λ_A: rank 4; det t² − 4 (5, 12, 21, 32, 45); signature (2, 2); U ⊂ Λ_A.
- The class counts (184 / 194 / 156 / 72 / 76) are exact.
- The six LR example points match exact solutions to 10⁻¹⁰.
- **The period map** is the Segre map: injective, onto D(Λ_A, Q) = ℍ × ℍ ∪ ℍ⁻ × ℍ⁻. The mixed components form
  D(Λ_A, −Q).
- Conjugation preserves orientation in complex dimension 2.
- The § 3 point argument has no gap: NS_A has rank ≤ 2; points are never in a mixed component; distinct planes give
  distinct points.
- Mumford's index: h⁰ = h² = 0 and h¹ = 3, so no vector-like pairs inside the bundle.
- The first-launch disclosure is correct.

## BLOCKING

**B1. "The chirality's sign is opposite between the two components" is false for χ.**
- In each component's complex orientation the invariant (1,1) plane is negative definite on all four components ℍ^± × ℍ^±,
  so χ(L) = c₁²/2 < 0 everywhere. If c₁² > 0, ±L would be an A-invariant polarisation, which a positive-entropy A forbids.
- What flips between components is Q(w)/2, the index in the fixed orientation e₀₁₂₃.
- For LR, γ = M ⊗ E_xx + I ⊗ E_yy (M = [[0, 1], [1, 1]], M² = LR, det γ = −1) commutes with LR ⊗ I and maps ℍ × ℍ onto
  ℍ × ℍ⁻, acting on Λ_A as an anti-isometry.
- For B₄–B₇, Λ_A ≇ Λ_A(−1), and ℤ[B_t] has no unit of norm −1. In the coefficient box the Q = −6 and Q = +6 counts are
  92/92 for LR and unequal for each null matrix.
- "The hand is CHOSEN" survives.

## CORRECTIONS

- **C1. The last column counts pairs (w, u), not points.** Exact recount:
  - LR: 168 pairs → 48 points, 14 saturated NS determinants (3–60);
  - B₄: 138 → 62, 21 (3–159);
  - B₅: 364 → 110, 36 (11–252);
  - B₆: 430 → 135, 37 (12–383);
  - B₇: 442 → 141, 46 (11–540).

  B₇'s "40 distinct" was a `[:40]` truncation.
- **C2. The index bound uses index²:** det NS = 6∣Q(u′)∣/k², with k dividing 6.
- **C3. Physics scope.**
  - The T⁴ index as the 4D generation number is CHOSEN (cf. I-34).
  - On T⁴ alone 8D SYM's bulk matter is vector-like (N = 2). A chiral count needs a completion, to be read at source.
  - Generation numbers between stacks are Q(F_a − F_b)/2.
  - Three or more independent invariant fluxes have no common (1,1) point (rank ≤ 2).
- **C4. "Exact" overstates.** The points came from floating-point roots.
  - The first launch's B₄ count of 160 included 22 spurious degenerate pairs.
  - The card's steps 3–4 were not run by main.
  - The first launch's script was not kept.
- **C5.** det M_w = −(det Λ_A/2)·Q(w) is an identity. Only its sign is invariant under the f± normalisation.
- **C6. § 4's wording:** "where LR-invariant flux pairs force isolated CM points (B1804; the integers choose)".
- **C7. Seen first.**
  - The sweep returns 3 rows (P-095, P-401, P-419).
  - Add I-34, B1800 and THE_WEAVE's W46.

## NOTES

- **N1. "Three" plays no role.** U ⊂ Λ_A represents every even integer. The NEGATIVE is a short corollary of B1804 § 4
  plus U ⊂ Λ_A. The (1,1) condition is the supersymmetric F-term choice.
- **N2. The Hirzebruch–Zagier form.** aτ₁τ₂ + μ′τ₁ + μτ₂ + b = 0 with μ ∈ ℤ[φ] and Q = 2(μμ′ − ab). In van der Geer's
  normalisation N = det M_w = 15, i.e. T₁₅ = T_{3D}. A lead to check at source.
- **N3. B1804's ℚ(√5, √−3) point** (NS = A₂(−1), the least saturated determinant, 3, on w's curve) lies on Q = −6
  curves. A₂(−1) holds three pairs of norm −6 vectors. Not a selection; bears on P-425.
- **N4. The D-term obstruction.** The real-multiplication plane is (1,1) on the whole family, orthogonal to Λ_A, and
  contains Kähler classes, so J·F = 0 holds for invariant fluxes. What fails is only A-invariance of J.
- **N5.** The frame card (08:55) predates the script (09:01).

## Main's verification

- q1–q4 regenerate byte-identically on main.
- q5 and q6 rerun, with their stdout kept.
- B1 was checked by hand: Hodge index in each component's own complex orientation.
- All corrections applied in B1808's FINDINGS.
