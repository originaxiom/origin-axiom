# B1810 (P-432's table) — hostile referee report (read-only, 2026-10-29; no data read)

Saved by main from the referee's hand-back. Its scripts (rf_common, rf1–rf9) and their outputs are beside this file.

**Verdict:** BLOCK on two items. Neither needed the table rerun; the table's numbers are right.
- The referee reproduced every row it checked by an independent route (rf4) to 5 × 10⁻⁷.
- The four configurations are exactly the configuration-fixed points.
- The 40 exceptions are real.

## BLOCKING

- **B1. § 3's "distinct mass patterns" counted floating-point noise.**
  - With ∣x∣ < 10⁻⁹ set to 0 and 5-figure rounding: 97 / 2 / 12 / 2 mass patterns, and 130 of 512 distinct outputs
    (8 directions).
  - The two ω configurations give the same two outputs.
  - The 40 exceptions carry 8 distinct angles: the lepton reading doubles every row, the two split readings give the same
    angle, and a₀ ≡ F₆ there.
  - The effective counts feed the sealed test's look-elsewhere count.
- **B2. "Tabulated in full" and "the record's eight directions" are false.**
  - B1730's F_a family (a ≡ 2 mod 4) is infinite; its n = 1 basis is a ∈ {−10, −6, −2, 2, 6, 10, 14, 18, 22, 26}.
  - At τ = i every listed direction but DR is a ∝ (1, 1, iκ), with κ real (κ = 2^{a/4}·sign; a₀ κ = 2^{−1/2}; R and t
    ∓√2). The menu at i is a geometric ladder in κ.
  - The exception angle falls like 1/κ.
  - Any null must range over a.
  - F₆ and F₂₂ entered through B1742's data-informed fit; disclose it.

## CORRECTIONS

- **C1. Fact 1 is B1703** (u = d iff N ∣ 6; u = e iff N ∣ 2 or 7). "Coincide" means up to an overall phase
  (e^{−2πi/3} on the 3-torsion line). It holds on every line of order dividing 6, at every τ.
- **C2. F₆ at ω gives (0, 1), like DR.** Every direction lies on one of the stabiliser's eigenlines: (1, −1, 1) → (0, 1);
  the two complex lines → rank one, exactly. The residual ≤ 1.2 × 10⁻¹³ scales as 1/(2πL + c).
- **C3. J.** "J = 0 in every row" holds only where V is defined; over all rows the maximum is 5.8 × 10⁻¹⁸. J = 0 is
  implied by a vanishing V entry, and recorded in B1809 FR-FIB.
- **C4. "The stabiliser no-go, row by row" overstates** (an unearned identification: P-224 and B1620 live in the
  weave-group frame). Of the 200 permutation rows:
  - 120 are trivially V = 1;
  - 8 come from DR on (i, (½, ½)), real up to phase;
  - 56 at (i, 0) are one fact: Y(κ)'s left basis is κ-independent;
  - 16 are R and t at (i, (½, ½)).
- **C5. The 40 rows.**
  - They are robust: gaps ≥ 0.019; the smallest entry 0.0048; route B agrees; w → −w invariance.
  - The mechanism: tr(εSMᵀ) = 0 for every (1, 1, iκ) at (i, (½, ½)), so m₁ ≡ 0. The spectrum is even in κ and invariant
    under κ → 2/κ. The reading acts as κ → −κ, and cos θ = ∣⟨n(κ), n(−κ)⟩∣.
  - The scope: θ ≈ 0.23/L (0.101 at L₂, 0.0058 at L = 40, 9 × 10⁻⁵ at 2560). In the L-free coupling V is a permutation.
  - Report θ and the permutation separately.
  - Cite B1739, P-295, P-345, B1659 and B1716.
- **C6. Reproducibility.** The counts, the exceptions and max J must be computed in the script, and the controls
  asserted. The permutation test must use the full V; three entries cannot certify it.
- **C7.** "V defined in 240 rows" should read: every row at i except DR at (i, 0).
- **C8. Governance.**
  - The frame card and FORCED / ADMITTED / CHOSEN labels are missing.
  - There is no Disclosed section.
  - The VERDICT lines are missing (the referee's: 8 of 1 556 arcs and 2 rows; 55 for the 2-torsion regex; 7 for the
    sector-coincidence regex, including B1703).
  - Lam's no-go is not read on the bench.

## NOTES (checks that pass)

- **N1. The configurations.**
  - S fixes {0, (½, ½)} up to sign. The order-3 element fixes {0, ±(⅓, ⅔)} at e^{iπ/3}.
  - The frame's convention (τ, p, L) → (γτ, M⁻¹p, L + log∣cτ + d∣) holds to 3 × 10⁻¹⁴ (rf6b).
- **N2.** B1667's radii are line-independent, and no channel weight is silently zeroed.
- **N3. Route B** (B1653's bilinear, own residues and quadrature) agrees to ≤ 5 × 10⁻⁷.
- **N4.** The controls match. The first launch differs from the current output only in the flags.

## Main's response (2026-10-29)

- **The table extended** to B1730's complete n = 1 family: 13 directions, 832 rows.
- **The summaries computed in the script.** The counts (206 distinct outputs), the full-V permutation test (320 of 400),
  the exception list (80 rows, 24 distinct ∣V∣), max J where V is defined, the asserted controls, and the angle's
  1/L scope (0.101, 0.00584, 9.0 × 10⁻⁵).
- **Checked against the table and the arcs:** F₆ at ω gives (0, 1); a₀ ≡ F₆ at (i, (½, ½)); B1703's statement; B1730's
  one-unit list.
- **The referee's rf scripts regenerated on main** (main_rerun/).
- **All corrections applied** in B1810's FINDINGS.
