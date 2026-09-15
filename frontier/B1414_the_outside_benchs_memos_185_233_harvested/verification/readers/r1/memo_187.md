# Reader r1 — Memo 187 (THE_ERRATUM_LOCALISED.md)

## 1. HEADLINE
"THE ERRATUM IS LOCALISED, AND IT IS FAIRER TO PARK THAN MEMO 183 COULD SAY: eq (32) as
printed annihilates nothing, the consequences he prints from it are exactly right, and the
operator file that was meant to settle it is for the wrong knot." Date **2026-09-09**.

## 2. CLAIMS
1. `rec.twist.knot.2.m` (order 4) annihilates **6₁ = K₋₂**, not 5₂ — "the same lost minus
   sign as memo 186's tables." Grade: **B (localised finding)**.
2. arXiv:1201.3314 §4's order-3 recursion annihilates **5₂** at n=1..6, verified against the
   bench's own R-matrix colored Jones — "a VERIFIED non-commutative A-polynomial for 5₂ is
   now held." Grade: **verified / CELL closes fetch item B''**.
3. CELL 1: Park's eq (32) as printed annihilates NO colored Jones of five knots in 60
   conventions (5 knots × 2 normalisations × 2 mirrors × 3 shifts). Verdict **→ B** (fails),
   an independent second witness to memo 183's defect on a different object (colored Jones,
   not F⁺).
4. T3: the "wrong twist-knot file" hypothesis (K₋₂ vs K₂) tested and **REFUTED** — ratio
   `a_i(6₁)/a_i(eq 32)` is not constant in `i`.
5. CELL 2: Park's printed `f₂`, `f₃` (as ℚ(q)-combinations of `f₀,f₁`) **MATCH** the bench's
   independently computed blocks on 16 and 15 exact coefficients respectively. Verdict
   **→ B**: "the computation behind the paper was right"; the defect is a transcription, not
   a math error.
6. T4: uploaded `A_polynomial_5_2.txt` VERIFIED against the classical (q→1) limit of the
   verified order-3 operator (reciprocal-longitude convention `w ↔ 1/w`), exact match.
7. §7 named open item (**not solved, not claimed**): converting the verified colored-Jones
   operator into the `x`-block recursion for `F⁺` fails by the naive ansatz in all four
   q-/x-mirror orientations — disagrees with known blocks at the first or second coefficient.
8. §8: arXiv:2106.03942 (Park Conjecture 2, the inverted Habiro series) arrived; memo 185 §8's
   convention note identified as its bridge. **Not tested here** — named as follow-up F187-1.

## 3. CERTIFICATE
- `certificates/park_eq32_localised.py` — **EXISTS**.
- `outputs/park_eq32_localised_out.txt` — **EXISTS**. Tail agrees with the memo's headline
  verbatim: "THE COMPUTATION BEHIND THE PAPER WAS RIGHT... Whatever went wrong, went wrong
  between his computation and the printed operator," and closes with the named open item
  ("NOT SOLVED, NOT CLAIMED") word-for-word matching the memo's §7.
- No seal is named for this memo (none checked).

## 4. ON MAIN ALREADY?
Main's `frontier/B1306_the_older_debt/` (slice B, sealed `d9d61f4b`, same day 2026-09-09)
independently re-derived the *closely related* memo-183 material from Park's own arXiv
LaTeX source (`FKexamples.tex`):
- **(a) already on main, independently reproduced**: memo 187's CELL-1-adjacent finding that
  eq (32) as printed does not vanish as required — main's own series code shows "the x^{7/2}
  coefficient equals q¹³f₀(q)... not zero" using Park's *own* closed-form f₀,f₁,f₂,f₃
  (`frontier/B1306_the_older_debt/FINDINGS_B.md:83-92`, `verification/sliceB/b1306_park_eq32.py`).
  This is consistent with (not contradicting) memo 187's CELL 2 ("the computation behind the
  paper was right") — main finds Park's own f₀..f₃ formulas self-consistent through the
  x^{5/2} row, and only the eq(32)-as-recursion's implied f₃ differs from Park's printed f₃,
  starting at q³ — the same "transcription, not math" shape memo 187 reports.
- **(c) NOT on main**: the specific localisation that `rec.twist.knot.2.m` is the operator for
  6₁=K₋₂ rather than 5₂ (no hits for `rec.twist.knot` or `K_{-2}` outside `outside_bench/`),
  and the citation/verification of arXiv:1201.3314 §4's order-3 recursion for 5₂ (no hits for
  `1201.3314` outside `outside_bench/`). Main's B1306 slice B works from the *arXiv source of
  Park's own paper* (`FKexamples.tex`), a different primary source than memo 187's survey
  citation — the two are complementary corroborations, not duplicates.
- No contradiction found between memo 187 and main's B1306 slice B; they corroborate each
  other from two different documents (survey vs. paper source).

## 5. NEEDS COMPUTATION HERE
1. Claim 3/1 (CELL 1, 60-conventions negative): recompute the R-matrix colored Jones for
   `3₁,4₁,6₁,9₂,5₂` at `n=1..6` (state-sum on Park's braid word per memo 185 addendum 3) and
   re-run the 60-conventions annihilation test of eq (32) against them; expect all 60 to fail
   exactly as reported, matching main's independent `b1306_park_eq32.py` result on a
   different (survey-sourced vs. arXiv-source) operator.
2. Claim 2 (order-3 recursion annihilates 5₂): recompute the order-3 recursion's action on
   the bench's own colored-Jones values at n=1..6 directly from arXiv:1201.3314 §4's printed
   coefficients; expect exact annihilation (all six residuals zero).
3. Claim 6 (classical-limit check): take `q→1` of the verified order-3 operator, strip the
   `(m−1)³(m+1)³(m²+1)²` factor, and compare to `A_polynomial_5_2.txt` under `w↔1/w`; expect
   an exact polynomial identity.

## 6. SUPERSESSION
No later memo in INDEX.md is recorded as superseding memo 187 (it has no addenda of its own
in the excerpts read). §7's open item is explicitly still open as of memo 187's writing
("this is memo 183 addendum 4's blocker, still standing"). No arc on main claims to have
solved the F⁺ block-recursion conversion either — main's B1306 slice B independently hit the
same eq(32) defect and did not attempt the conversion.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** — the CELL-1/CELL-2 computations are cheap, exact-arithmetic, and
independently corroborated by main's own B1306; the specific 1201.3314/rec.twist.knot.2.m
localisation is a genuinely new documentary+computational fact not yet on main and is worth
a harvest row (recipe in §5.1–5.2 above), even though the substantive "eq(32) fails but Park's
math is right" conclusion is already independently confirmed on main via a different route.
