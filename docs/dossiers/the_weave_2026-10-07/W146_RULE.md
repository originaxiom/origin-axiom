# W146 — P-357 data-free first: what can fix the Higgs's invariant ∣h·h∣/∣h∣²? A dichotomy for every holomorphic Higgs in the frame's representation, of any weight and any character, and the nine's target against it; with the web seat's Lemmas A, A′ and B on own code and its E₆ question (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's P-357.** The nine's target (B1743, S204) is a nearly null Higgs whose invariant I = ∣h·h∣/∣h∣² stays about
  0.017–0.020 on every good row, with an e₁ admixture about 0.3. Every form on record falls like e^{−π Im τ} instead
  (B1739). An exactly null Higgs zeroes the first generation and V_us, so the invariant carries them.
- **P-357's candidates, to examine data-free first:**
  - (a) a Higgs whose weight or multiplier leaves the cusp's null line at order one;
  - (b) a normalisation that fixes h·h;
  - (c) the Higgs as the vev of a field with a potential.
- **The web seat's relay** (CHAT1_TO_CC_AND_SM_2026-10-24_THE_READING_TEST, 521262a4d) asks this seat for:
  - a third opinion on its Lemmas A, A′ and B on own code;
  - whether the reading S̃ ↔ H̃ has an alternative in this seat's E₆ language under which one doublet could still
    carry the nine.
  All three lemmas concern the same invariant.
- **The owner said "start it",** then approved all of it in order ("lets go for all systematically", 2026-10-24).

## The objects

- **ρ(T) and its eigenlines** (B1739 part D; W133's line coordinates).
  - l₁ = x lies on e₁, of class 1/8. l₃ = y − iz lies on h₀ = (0, 1, i)/√2, of class 3/8. l₇ = y + iz lies on h̄₀, of
    class 7/8.
  - The classes are each component's q-exponent mod 1, up to one common shift.
  - So h·h = l₁² + l₃l₇ and ∣h∣² = ∣l₁∣² + (∣l₃∣² + ∣l₇∣²)/2.
- **A holomorphic Higgs in ρ ⊗ χ** is a vector-valued function with h(τ + 1) = λρ(T)h(τ) for a unimodular constant λ
  and holomorphic q-expansions. λ covers any weight's multiplier, any character χ (the twists ε_r, sgn, Γ₄'s ρ′ and
  ρ′ ⊗ sgn) and any level.
- **The record's Higgs directions:** R; ∂R (main's census Higgs, from direct theta sums as W138's); and every member
  F_a of W143's four spaces, a ∈ {−10, −6, −2, 2, 6, 10, 14, 18, 22, 26}.
- **The weight pencil** h_w = ∂R + (w/12)E₂*R, with E₂* = E₂ − 3/(π Im τ).
- **The nine's target:** main's committed `target.json` (B1743, the ten optima with τ and I), read once by the
  script.
- **The web seat's lemmas** (its READING_TEST_RULE.md, sealed at d58a4dbdb). For B1736's coupling
  Y = u hᵀ + h uᵀ − (u·h)1 + w[h]_×:
  - **A:** Y h = Yᵀh = (h·h)u, and the light left state lies within sin θ ≤ ∣g·g∣‖u‖/m₂ of ḡ;
  - **A′:** ‖S‖_F² = 2‖u‖² + 2∣⟨u, h⟩∣² − ∣u·h∣² for S = (Y + Yᵀ)/2 and unit h, so ‖u‖ ≤ √3 m₃;
  - **B:** α(x) = ½ arccos∣x·x∣ is the Fubini–Study distance to the real directions, and
    ∣⟨x, y⟩∣ ≤ cos(α(x) − α(y)).
  Each is written again here and checked on own code. Their row thresholds (1.112 × 10⁻³ and the bar's limits)
  involve the data and are not rechecked.

## Weave or thread

**WEAVE-type.** The quantity is the moves' joint representation ρ on the Higgs. The claims are about every holomorphic
Higgs section at once, at every weight, character and twist.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K1 | **The classes, exact (sympy).** x² + y² + z² = l₁² + l₃l₇ and ∣x∣² + ∣y∣² + ∣z∣² = ∣l₁∣² + (∣l₃∣² + ∣l₇∣²)/2. h₀ lies on l₃ and h̄₀ on l₇. The two terms of h·h share one class, since 2·(1/8) ≡ 3/8 + 7/8 ≡ 1/4 (mod 1), while 2·(3/8) ≡ 2·(7/8) ≡ 3/4. On the record's forms the leading exponents of l₁, l₃ and l₇ lie in these classes up to one common shift | 99% |
| K2 | **The dichotomy, by hand and checked on the record.** For every holomorphic h in ρ ⊗ χ, either l₁ leads and I → 1, or a null line leads and I = C∣q∣^{1/2+n}(1 + o(1)) with n ≥ 0 an integer. So I ≤ C′e^{−π Im τ}, and no weight, character or level moves the rate. On every record direction, the local slope −d ln I/(π d Im τ) at Im τ 3–6 (Re τ 0.25 and 0.4) tends to an odd integer for the null-led (1 for R, ∂R and F_a with a > 0), and 1 − I → 0 for the e₁-led (F_a with a < 0) | 95% |
| K3 | **Normalisation and the weight pencil, exact.** I(fh) = I(h) for every nonzero scalar f (Petersson factors, powers of Im τ or ∣η∣). R·∂R = ½∂(R·R) = 0, so h_w·h_w = ∂R·∂R for every w. Checked at 12 points and w ∈ {−4, 0, 2, 4, 12} to 10⁻²⁰ relative | 99% |
| K4 | **The target against the dichotomy** (a read-out of main's committed target.json). The log-slope of I across the L₂ optima, Im τ 2.0–2.3, lies between −1 and +1, against at most −π for any null-led holomorphic Higgs; by hand from B1743's table it is about +0.25. The value, about 0.018, is far below the e₁-led forms' I ≈ 1. So no holomorphic Higgs in ρ ⊗ χ follows the target across its band | 90% |
| L1 | **Lemma A on own code.** Y h = Yᵀh = (h·h)u exactly (sympy, generic symbols). On 20 000 random (w, u, h), the light left state's sin θ to ḡ never exceeds ∣g·g∣‖u‖/m₂ (by more than 10⁻¹²) | 99% |
| L2 | **Lemma A′ on own code.** The Frobenius identity holds exactly (sympy, h of unit norm), and ‖u‖/m₃ ≤ √3 on 20 000 random draws and on 200 local maximisations from random starts. A read-out: the largest ratio found | 97% |
| L3 | **Lemma B on own code.** On 2 000 random unit x, the maximal real overlap found by optimisation equals (1 + ∣x·x∣)/2 to 10⁻⁹, so α is the distance to the real directions. ∣⟨x, y⟩∣ ≤ cos(α(x) − α(y)) holds on 20 000 random pairs and 200 local maximisations, to 10⁻¹² | 97% |
| K5 | **What can (exact condition, by hand).** A T-equivariant real-analytic h = Σ c q^m q̄^n has I → c ∈ (0, 1) at the cusp only if its least ∣q∣-order part has a null component and a second component of another class, with m − n carrying the class. That needs a factor q̄^n with n ≠ 0, so the Higgs is not holomorphic. A read-out, no prediction: none of the record's directions is of that kind | 95% |

## What the outcomes mean (fixed now)

- **K1 and K2 hold.** P-357's candidate (a) is closed inside the frame's representation. No weight, multiplier
  character, twist or level gives a holomorphic Higgs whose invariant leaves the null cone at order one without going
  all the way to I ≈ 1. Every null-led one falls at least like e^{−π Im τ}.
- **K3 holds.** Candidate (b) as a normalisation cannot move I, which is scale-free. As a condition h·h = c(h, h̄) on
  the direction it is the same question as (a), and K2 closes it for holomorphic h. The weight pencil leaves h·h
  untouched.
- **K4 holds.** The nine's target is incompatible with every holomorphic Higgs in ρ ⊗ χ across its band.
- **K5 holds.** What remains is a Higgs that is not holomorphic in τ, or a representation other than the frame's.
  Candidate (c), a field's vev, is one such. This is a pointer, not a construction.
- **K2 fails** (a record direction with a non-odd limiting slope, or an e₁-led one with I not tending to 1): the
  dichotomy's proof or the class bookkeeping is wrong. That is the finding, diagnosed first.
- **L1–L3 hold.** The web seat's three lemmas are confirmed on a second code. A failure is reported to it as found.
- **The E₆ question (a READING, from this seat's record, no new cell).** In E₆ the up quarks couple through one
  doublet component of the 27 and the down quarks and leptons through another, in the holomorphic cubic (W139), which
  has no conjugate H̃. A single 27 vev forces M_l = −(1⊗Jᵀ)M_qᵀ(1⊗J), so D ≡ 1 (W139, W137), and the data exclude
  that at 87σ. So E₆ gives no one-doublet way out. Its natural reading is two independent doublets, as the web seat's
  pointer says, with the lepton–down split from beyond the 27.
- **This is data-free except K4's read-out** of main's committed optima. It is not a test against data, and no trial.

## What stays out

- Non-holomorphic constructions beyond K5's condition; representations other than ρ ⊗ χ; the frame's other channels;
  B1741 (W145); the web seat's reading test.

## Seen before the rule (disclosed)

- **Read:**
  - B1739's FINDINGS §0–1, including ρ(T)'s eigenlines and phases;
  - B1743's FINDINGS §1–4, including the five optima printed in its table;
  - target.json's keys only;
  - P-352 and P-357;
  - S204's commit message;
  - B1746's summary in S210's message.
- **By hand:**
  - the class arithmetic and the dichotomy's proof sketch;
  - F₆'s rate from B1739's printed values (0.045 at Im τ 2.0 and 0.0093 at 2.5, a ratio of 0.207 against e^{−π/2} =
    0.208);
  - the target's slope, about +0.25, from B1743's table;
  - h_w·h_w = ∂R·∂R.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
