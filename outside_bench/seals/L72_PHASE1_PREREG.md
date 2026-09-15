# SEAL — L72 PHASE 1: the E₆-principal torsion, and what its six blocks obey

**Sealed before computing.** Object: the six twisted Alexander polynomials Δ_m(t) of the
figure-eight at Sym^{2m}(ρ_geo), m ∈ the E₆ exponents {1,4,5,7,8,11}, banked exactly by
B581 in `frontier/B581_six_torsions/six_torsions_results.json`.

## Why this seal exists, and what the record already says

`docs/OPEN_LEADS.md` L72 names the step: *"the E₆-PRINCIPAL torsion = the product of the
six Sym^{2m}-block torsions — start from B425's method."* B666 cell T's triage classifies
L72 **STILL-LIVE-UNVERIFIED**, noting *"phase 1 DONE = B581."* B581 banks the six
polynomials and the six τ_m; **it does not form the E₆-principal object, and no file in
`frontier/**` or `docs/**` contains the product** (searched: *"product of the six"*,
*"Pi tau_m"*, *"principal torsion ="* — two hits, both the L72 registration itself and
B579's handoff naming it as the step to take).

`already_banked.py` was run on *"asymptotic growth of the twisted torsion"*, *"log tau_m
quadratic in m"*, *"torsion growth law Sym 2m"*; the settled arcs it returned were read
and none addresses the growth of these six numbers.

**The fence that comes with CELL 3, adopted in advance from B1157** (which banked it):
*"the 'graviton in the analytic torsion / Vol common scale' reading is generic spectral
geometry, not object-specific physics … generic to all finite-volume hyperbolic
3-manifolds."* **Any Vol-scaling found in CELL 3 is therefore a check of B581's data
against generic hyperbolic geometry, and is NOT an object-specific finding.** This is
stated here so it cannot be discovered as a result.

## CELL 1 — the E₆-principal polynomial

Define `Δ_E6(t) := Π_m Δ_m(t)` over the six exponents, from B581's exact coefficients.

**Observed:** `deg Δ_E6` and the order of vanishing of `Δ_E6` at `t = 1`.

- **Outcome A:** the order of vanishing is **6**.
- **Outcome B:** it is not 6.

## CELL 2 — the two routes to the principal torsion agree

**Observed:** whether `Δ_E6^{(6)}(1) / 6!` equals `Π_m τ_m` **exactly as integers**, where
`τ_m := Δ'_m(1)`.

- **Outcome A:** exactly equal.
- **Outcome B:** not equal.

## CELL 3 — what the six torsions obey

Let `Vol := Vol(4₁) = 2·Cl₂(π/3)` at 30 decimal places, and
`R_m := log|τ_m| − (Vol/π)·m(m+1)`.

**Observed:** the six `R_m`, and the **spread** `max R_m − min R_m` over
`m ∈ {4,5,7,8,11}` (m = 1 reported separately, not included in the spread).

- **Outcome A:** spread **< 0.05**.
- **Outcome B:** spread **≥ 0.05**.

## Controls (all must pass before any cell is read)

- **C1 — B581's own table reproduced.** All six `τ_m` recomputed from the JSON
  coefficients must equal B581's banked values: −3, 260736, −165110400, −3257341296168960,
  100636318520821923840, and the m = 11 value, with the banked factorizations.
- **C2 — the analytic gate B581 itself required.** `Δ_1(t)` must factor as
  `(t−1)(t² − 5t + 1)` and give `τ_1 = −3` — **B425's banked value**.
- **C3 — structure.** Every Δ_m: integer coefficients (imaginary parts all zero),
  skew-palindromic (`c_k = −c_{deg−k}`), and `Δ_m(1) = 0`.
- **C4 — MB12 transversality for CELL 3.** The same statistic against a **wrong** power
  law, `R'_m := log|τ_m| − (Vol/π)·m²`, must show a spread **≥ 0.05** over the same set.
  If the wrong law also comes out flat, the statistic does not discriminate and **CELL 3
  may not be read** (memo 164).
- **C5 — the sign law.** `sign(τ_m) = (−1)^m` must hold **6 of 6**.

## Declared priors

- CELL 1: **Outcome A** — each block has a simple zero at t = 1 (B581 states dim H¹ = 1 per
  block), so the product should vanish to order 6. A reproduction, not a discovery.
- CELL 2: **Outcome A** — Leibniz. This cell exists to catch an arithmetic slip, not to
  learn something.
- CELL 3: **no prior declared.** The bench has not computed these residuals.

## Interpretation is not preregistered

Per bench rule #21 the outcomes state only what will be **observed**. What CELL 3's number
means — and in particular the B1157 genericity fence above — is written after, in the memo.
