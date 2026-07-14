# B587 — the tone mechanism SOLVED: the Weyl-twisted Weil factorization

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM
quantities. The FRAMEWORK is KNOWN and cited (Jeffrey 1992 CMP 147; the banked
B204 PROOF/V198 at SU(2) — no novelty claim on the mechanism). This arc
computes the open SU(3) reach (L24(c)) and ANSWERS L82. Preregistered; the
conductor menus were registered before the sweep; locks
`tests/test_b587_weil_mechanism.py`.**
Run: `python3 weil_mechanism.py` (pyenv, ~6 min).

## (D) The decomposition identity — exact

For every balanced word W (equal R,L — the framing offsets ±i per letter
cancel) and every κ = 4..20, verified against the banked B238 values for
golden/silver/bronze:
> **Z(W; SU(3)_k) = (1/6) Σ_{w ∈ W(A₂)} sign(w) · tr( ρ_Weil(W) ∘ P_w )**
on ℂ[P/κQ] (|G| = 3κ², S = the bare finite Fourier transform — S² = parity
exactly; T = e^{πi|μ|²/κ}). Inserting the stage's charge conjugation C
multiplies by sign(w₀) = −1 and moves the sum to the (−W)-coset, so
> **tr_odd = (1/12) Σ_w sign(w) (t₊w + t₋w)**, tr_even = the ±-difference,
with t±w(κ) = tr(ρ_Weil(W)∘P_{±w}). Twelve Gauss-sum terms carry everything.

## (M) The conductor menu — every locus as registered

Each term fires on divisibility of κ by (the square-free-relevant part of)
**det(A ⊗ (±w) − I₄) = Π(α_i β_j − 1)** — the object's monodromy eigenvalues
twisted by the stage's point group ±W(A₂):
- **golden (tr 3):** menu {+w₀: 1, −w₀: 25, +rot: 16, −rot: 4, refl: ±5}. The
  d=25 term fires +5 at 5|κ; the six d=−5 reflections fire √5 at 5|κ and
  oscillate as the Legendre symbol (κ/5) otherwise; the d=16 rotations fire +4
  at 4|κ; the d=4 rotations fire +2 at 2|κ; the d=1 identity is the constant 1.
- **silver (tr 6):** menu {16, 64, 49, 25, −32}. **The mystery tones solved:
  the 7 = the d=49 rotation terms N(α·ω − 1) = tr² + tr·(β+β̄)·… = 49, firing
  +7 exactly at 7|κ; the 5 = the d=25 (−rot) terms** — the object's unit as
  seen through the stage's own ℤ₃ symmetry. The κ=16 anomaly (1 − 2√2) comes
  from the d=−32 terms' √32-firing.
- **bronze (tr 11):** menu {81, 169, 144, 100, −117}. **The κ=10 silence is an
  exact arithmetic cancellation, exhibited term by term:**
  (1/12)[(3+1) − 3(3+1) + 2(−6+10)] = (4 − 12 + 8)/12 = 0.

## The laws derived

- **LAW-O re-derived at every κ (gate, green):** the ±-symmetrized assembly
  reproduces tr_odd(RL) = [4|κ] − [5|κ]/φ exactly. **The golden voice in closed
  form:** at 5|κ,
  > tr_odd = (1/12)[(1 + 5) − 6√5 + (2 − 2)] = **(1 − √5)/2 = −1/φ** —
  the identity term plus the 5²-conductor Gauss sum, minus six reflection
  Gauss sums √5; the rotations cancel. The recurring golden value is literally
  this Gauss-sum arithmetic.
- **LAW-E explained (why the B585 guess had to die):** the even channel is the
  ±-DIFFERENCE assembly, which mixes the divisor-gated terms with the
  unit-conductor terms that oscillate as quadratic characters (Legendre (κ/5)
  etc.) — it cannot satisfy any divisibility law. The banked even values
  (κ=6: −1, 7: +1, 8: +1, 10: −1, 12: +1, 13: +1, 14: −1, …) are all
  reproduced by the same twelve terms.
- **Why only the golden word is clean (B585's "golden is special", now a
  mechanism):** golden's off-identity conductors are {25, 16, 4, ±5} — powers
  of the two tones — and its unit identity-term det(A−I) = −1 makes the
  generic-κ contributions cancel exactly. Heavier words have non-unit
  det(A−I) (silver 16, bronze 81), so their generic terms don't cancel and
  their tones interfere (bronze at κ=10) — the clean two-tone chord is a
  consequence of the figure-eight's det(A∓I) = ∓1·5 unit structure, i.e. of
  minimality.

## Reading (firewalled)

L82 is answered: the stage hears the object through exactly twelve Gauss sums —
the object's eigenvalue pair twisted by every element of the stage's own point
group, ± its central mirror. The tones are the conductors det(A⊗(±w) − I); the
chiral channel is the ±-symmetric half of that arithmetic. What B585 saw as
"the stage's arithmetic gating the object's voice" is now literal: κ hears the
tone d exactly when it divides the twisted conductor.

## Residuals (registered)

- The closed-form PROOF (Landsberg–Schaar-type reciprocity per term, as B204
  did at SU(2)) — Wave 2; the numeric identity is exact over 3 words × 17 κ
  but the per-term evaluation is not yet a theorem at SU(3). → L24(a')-analog.
- The general-word / general-N reach (L24(c) proper) stays open beyond SU(3).

## Anchors

B204/L24/L33 (the SU(2) mechanism, PROVED; Jeffrey 1992 known — cited),
B585 (LAW-O + the hold-outs + M1's refuted naive mechanism), B586 (stage
verdicts), B238 (banked Z values, the (D) gate), L82 (answered), L24(c)
(the SU(3) reach, computed).
