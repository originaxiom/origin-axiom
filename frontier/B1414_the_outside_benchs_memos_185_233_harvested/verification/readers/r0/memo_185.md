# Memo 185 — THE_CYCLOTOMIC_ROUTE_IS_CLOSED.md

## 1. HEADLINE

"THE NAIVE CYCLOTOMIC ROUTE TO `f_K` IS CLOSED, BY COMPUTATION, and a route this bench
floated one message earlier is withdrawn before it cost anything." Date 2026-09-09
(main memo + Addenda 1, 2, 3 all same day).

## 2. CLAIMS

1. **Withdrawal**: the "table of J_1..60 unlocks f_j via inverted Habiro series" idea is
   WITHDRAWN (not proved wrong elsewhere, just retracted by this memo before being acted on).
2. **CELL A (4₁)**: `C_K(x,q)` is NOT a Laurent power series — a single monomial `x⁰q⁰`
   receives unboundedly many, unboundedly large contributions. Grade: **OUTCOME B** (computed).
3. **CELL B (3₁)**: no `λ,A,B` exists with `C_K = λ x^A q^B f_K` — `C_K`'s x⁰ coefficients take
   32 distinct absolute values in 35 orders vs. f_K's constant `1/2`. Grade: **OUTCOME B** (computed).
4. **Consequence**: a colored-Jones table for n=1..60 does NOT unblock f_6+ (memo 183 addendum
   4's blocker survives). Grade: stated fact, not withdrawn.
5. Three other uses of such a table (stability fence 8→~60 coeffs; free K₋₁/K₁ controls; family
   4→30 knots) are UNTOUCHED / stand.
6. **Convention note**: GM's eq(20) basis gives `C_m(4₁) = (-1)^m q^{-m(m+1)/2}`, NOT "all 1's"
   (that's true only in a different, `c2_habiro.py` basis). Recorded so it isn't misread later.
7. **ADDENDUM 1**: GM §7.4's "we get the right answer for -1 surgery" is tested directly.
   At `p/r=-1` (Poincaré sphere): C_K route reproduces the entire false theta A(q) to q^120 and
   differs from true Ẑ_0 by exactly one additive monomial `2q^{-1}`. Grade: **OUTCOME B** (near
   miss, quantified). At `p/r=-1/2` (Σ(2,3,11)): NOT a near miss — f_K route sparse ±2 coefficients,
   C_K route dense into six figures. Grade: **OUTCOME B**.
8. **ADDENDUM 1 by-product**: Park's Table 4 line for Ẑ(Σ(2,3,11)) is now derived from the
   TREFOIL alone (via GM Thm 1.2+1.3), independent of Park's 5₂ machinery — so memo 183's erratum
   target no longer rests on a single paper. Grade: computed corroboration.
9. **ADDENDUM 2**: `C_K` converges (is a genuine power series) for twist knots with `p>0`
   (val C_m = m) and diverges for `p<0` (val C_m = -(2|p|-1)m(m+1)/2), exact for m=0..12 on four
   knots (3₁,9₂,4₁,6₁). Grade: **OUTCOME B / measured law**, with round-trip verification (C_m
   rebuilds J_1..J_7 exactly on all four knots).
10. **ADDENDUM 2 prediction**: `5₂ = K_2` (p=+2) should have val C_m(5₂) = m for all m — banked
    BEFORE the deciding file (`CJTwist.2`) arrives. Grade: falsifiable prediction, not yet tested
    at time of addendum 2.
11. **ADDENDUM 3**: prediction #10 tested via an independent route (R-matrix state sum on Park's
    braid word, not the missing table) — measured val C_m(5₂) = 0..8 matches predicted 0..8
    exactly. Grade: **OUTCOME A — the prediction holds.**
12. **ADDENDUM 3 negative control**: the tempting reading "C_m(5₂) nonzero-term counts are 2^m"
    (1,2,4,8) FAILS at m=4 (15, not 16) — recorded so nobody banks it. Grade: NEGATIVE, filed.
13. **ADDENDUM 3 scope**: CELL B (the "no λ,A,B" block) has still only been run on ONE positive
    knot (3₁), because f_K isn't known in closed form for 5₂ past f_5 — so what blocks 5₂'s
    naive route specifically is NOT settled as convergence-failure (5₂ converges) but the exact
    mechanism (the CELL-B-type obstruction) is unverified there. Grade: scope limit, explicit.

No addendum withdraws the main headline; addenda extend, sharpen, and predict-then-confirm it.

## 3. CERTIFICATE

All four certificate/output pairs exist:
- `outside_bench/certificates/cyclotomic_vs_fk.py` / `outputs/cyclotomic_vs_fk_out.txt` — EXISTS.
  Output's final VERDICT line: "The naive cyclotomic route to f_K is closed at both places it
  could be open. On 4_1 the object C_K is not a series at all... On 3_1... it is not f_K up to
  any monomial." Matches headline exactly.
- `outside_bench/certificates/gm_74_habiro_surgery.py` / `outputs/gm_74_habiro_surgery_out.txt` —
  EXISTS. Tail confirms the two-slope near-miss/not-near-miss split, matching Addendum 1.
- `outside_bench/certificates/cyclotomic_valuation.py` / `outputs/cyclotomic_valuation_out.txt` —
  EXISTS. Tail confirms the p>0/p<0 split and the 5₂ falsifiable prediction, matching Addendum 2.
- `outside_bench/certificates/cyclotomic_52_prediction.py` / `outputs/cyclotomic_52_prediction_out.txt`
  — EXISTS. Tail confirms "the prediction holds" and the 2^m-pattern failure note, matching
  Addendum 3.

No seal declared for this memo (Gate 5 exact-arithmetic only, no seal file named) — nothing to
hash-check.

## 4. ON MAIN ALREADY?

Grep of `docs/`, `frontier/`, `papers/`, `fetch/` (excluding `outside_bench/`) for "memo 185",
"THE_CYCLOTOMIC_ROUTE_IS_CLOSED", "naive cyclotomic": **zero hits**. A broader grep for
"cyclotomic|f_K|Habiro" hits many unrelated files (generic uses of "cyclotomic" elsewhere in the
corpus, not this memo's claims).

**(c) NOT on main.** This memo's findings (CELL A/B outcomes, the p-sign convergence law, the
5₂ prediction-and-confirmation) exist only inside `outside_bench/` (memos + certificates); they
have not been harvested into a `frontier/` arc or cited in any `docs/` file. They currently only
feed a still-open fetch item (Park's inverted-Habiro-series paper, tracked as fetch item B2 in
`fetch/FETCH_REQUEST_CEFF.md`, per the memo's own §6).

## 5. NEEDS COMPUTATION HERE

- **CELL A (claim 2)**: recompute `C_m(4₁) = (-1)^m q^{-m(m+1)/2}` for m=0..14 and sum
  contributions to the `x⁰q⁰` coefficient of `Σ C_m(q)(qx)_m(qx⁻¹)_m`; confirm partial sums do
  not stabilize (expect the printed sequence `1,1,3,1,9,-7,45,...`). Sympy/exact `Fraction`
  arithmetic in a few seconds.
- **CELL B (claim 3)**: recompute the x⁰ q-coefficients of `C_{3₁}` (C_m=q^m) for q-orders 0..34
  and compare against GM Thm 1.3's `f_{3₁}` coefficients (all ±1/2 on a sparse exponent set);
  confirm 32 distinct absolute values appear in the C_K side. Cheap, exact.
- **Addendum 2's law (claim 9)**: recompute Habiro `C_m` from colored Jones tables for 3₁, 9₂,
  4₁, 6₁ (Garoufalidis–Sun tables, or reproduce via GM eq(20) triangular solve) and check
  `val C_m = m` (p>0) vs `val C_m = -(2|p|-1)m(m+1)/2` (p<0) for m=0..12. Population: the four
  named twist knots.
- **Addendum 3's prediction (claim 11)**: rerun the R-matrix state sum on Park's braid word
  `β₂ = σ₂⁻³σ₁⁻¹σ₂σ₁⁻¹` for 5₂, solve `C_m` via GM eq(20) from J_1..J_9, check `val C_m(5₂) = m`
  for m=0..8, and check control C2 (this machine's J_2,J_3 for 3₁ match Garoufalidis-Sun's K_1
  entries) — chirality is the one thing that could invert this result.

## 6. SUPERSESSION

Not withdrawn. INDEX.md rows after 185 (checked up to 233, the highest indexed number) contain
no memo that revisits or retracts this one; the owner register carries no later addendum naming
memo 185. The memo's own three addenda extend rather than reverse the headline (Addendum 2
explicitly sharpens CELL A's wording so it isn't over-read as "C_K never converges" — that is a
clarification, not a withdrawal).

## 7. GRADE PROPOSAL

**REPRODUCE-AND-BANK.** This is a real, cheap (exact `Fraction`/integer arithmetic, seconds to
run), controlled computation with a falsifiable prediction later confirmed by an independent
machine (R-matrix state sum vs. tabulated Habiro coefficients) — exactly the shape of a frontier
arc row, and it currently sits un-banked outside `frontier/`.
