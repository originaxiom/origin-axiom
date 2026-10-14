# W79 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat read while drafting
is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **W78 found that the two seats' weight-3 models differ,** and asked main for its forms. Main's code is in the
  repository (`frontier/B1635_couplings_on_the_ruled_branch`, `frontier/B1637_fits_on_the_ruled_branch` on main
  @ 60c5470ae), so the seat can compare them itself rather than wait.
- **The question is which of three it is:** the same representation (then the difference is a search failure); the
  conjugate representation (q-exponents λ ↔ 1 − λ, a genuinely different space of holomorphic forms); or neither.
- **A correction to the seat's own words, owed here.** In its report to the owner after §97 the seat said that plain
  conjugation could not explain the gap, because conjugate fits are mirror images. That is wrong for holomorphic
  forms. τ ↦ −τ̄ carries a form for ρ to a form for γ ↦ conj ρ(εγε), not for ρ̄, and the forms for ρ̄ have
  q-exponents 1 − λ. §97's hypothesis stands.

## Weave or thread?

- **Neither: a comparison of two seats' instruments** for the same ansatz (one τ, holomorphic couplings, T ⊗ T).

## Seen before the rule (disclosed)

- **Main's code, read:**
  - ρ_θ (B1634) in the theta basis: ρ(S) = e^{−23iπ/4} P₁₃ and ρ(T) = e^{7iπ/4} diag(i, 1, 1) P₂₃. Its T-exponents by
    hand are ⅛, ⅞ and ⅜.
  - T ⊗ T is Y ↦ ρ^{−T} Y ρ^{−1}, with W = η¹⁸Y a matrix of degree-(k + 9) polynomials in the theta squares.
- **Main's stored single-sector fits at weight 3 (B1637's F3):** u exact at τ = −0.0737 + 6.6640i, d at
  −0.1931 + 5.0866i, and e at 0.1419 + 5.8547i. Main stores τ and χ², not the coefficients.
- **The seat's code, read:** W52's ρ_T is `PG.rho_T`, with S = tL tR⁻¹ tL and T = tL⁻¹ in the parity basis, and the
  coupling representation is kron(Ā, Ā).
- **W78's post hoc:** at τ free in Im τ ∈ [4, 8], this seat's up sector alone at weight 3 reached only 1.78.
- **Nothing has been computed** for this arc.

## The method (fixed here)

- **C1, the triplets (exact numerics).** Compare this seat's (ρ_T(S), ρ_T(T)) with main's (ρ(S), ρ(T)):
  - the T-eigenvalue exponents;
  - the characters at S, T, ST, (ST)², T², ST⁻¹ and T S T, each against main's and against main's conjugate.
  - Verdict: isomorphic to ρ_θ, to its conjugate, or to neither.
- **C2, the coupling action as each seat's forms actually transform.**
  - This seat's weight-3 forms (W54's `forms_at`) and main's (main's own code, extracted read-only by `git archive` of
    `frontier/B1632_w45_verified_on_main`, `frontier/B1635_couplings_on_the_ruled_branch`,
    `frontier/B1637_fits_on_the_ruled_branch` and `frontier/B1612_the_mixing_patterns_the_weave_fixes` at 60c5470ae
    into a temporary directory).
  - For each seat, the stated T-action on 3 × 3 matrices: this seat's Y ↦ X Y Xᵀ with X = conj ρ_T(T), and main's
    Y ↦ ρ(T)^{−T} Y ρ(T)^{−1}. It is checked on that seat's own weight-3 forms, Y(τ + 1) against the action on Y(τ),
    at τ = 0.1 + 3i, to 10⁻⁸ relative.
  - Compare the two 9-dimensional T-eigenvalue multisets (as exponents mod 1).
- **C3, the decisive fit (this seat's model only).** At each of main's three F3 τ, fit that sector alone at weight 3
  in this seat's model, with 300 starts (W54's `forms_at` and `mass_res`, a = 0.10).

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **C1, the triplets** | This seat's ρ_T is isomorphic to the conjugate of main's ρ_θ, not to ρ_θ: its T-exponents are ⅞, ⅛ and ⅝, and its characters are the conjugates of main's. | 55% |
| **C2, the coupling action** | Each seat's stated T-action holds on its own forms to 10⁻⁸, and the two 9-dimensional exponent multisets differ: one has 1/4 three times and 3/4 twice, the other the reverse. | 55% |
| **C3, the decisive fit** | In this seat's model, d and e reach χ² < 10⁻⁸ at main's τ, and u does not (χ² > 1). | 65% |

**The read-outs (no prior).** Both seats' T- and S-matrices' eigenvalues and the C3 fits' pulls.

## What a result means, fenced

- **If C1 to C3 hold:** the two seats fitted different representations: this seat T ⊗ T built on the conjugate of
  main's ρ_θ. W54 and W78's weight-3 statements are about that representation, and B1637's about main's. The seats
  must agree which is the record's (B1634's lift fixes ρ_θ on main). The weight-5 and weight-7 agreement would then
  be a coincidence of large spaces.
- **If C1 fails (the triplets are isomorphic) but C3 holds,** the difference is in the coupling construction or the
  automorphy convention, and C2 locates it.
- **If C3 fails (u fits at main's τ here),** W78's discrepancy was a search failure after all, and W78's reading is
  corrected.
- **The count is unchanged in every case.** 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Main's code is used read-only, from a temporary extraction,** and is not modified or committed here.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
