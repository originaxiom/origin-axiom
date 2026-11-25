# SM-R610 — W134's 17/24 of the cusp unit against C8's whole unit: where they part, and K2 re-derived

*Card of the SM seat, 2026-11-25, for register row P-610 (main's page M53). Sealed with its script
(`relays/sm_r610/run.py`, SHA-256 d60e1f635336fb6a, first 16 hex) before the script runs on any real case. Only the
smoke path has run, on inputs outside the population, and it prints no result. Data-free: no measured value is read.*

## 0. The question (M53)

Reconcile W134 (three chiral 27s need 17/24 of the cusp unit, never the whole unit) with C8 (B1796, B1797, GENESIS
v1.59, which use the whole unit) on main, or scope C8. Also re-derive K2, which B1736's FINDINGS say was not re-derived
even though P-302 is DONE.

## 1. What the record already says (read before writing)

- **W134** (`docs/dossiers/the_weave_2026-10-07/W134_RULE.md`; relay §221 of
  `SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md`).
  - The object is the weave's triplet ρ (ρ(S) = ζ₈P, ρ(T) = ζ₈L⁻¹), placed in E₈'s family slot, E₈ ⊃ (E₆ × SU(3))/ℤ₃.
  - The datum is a uniform dressing η^m, which is m twenty-fourths of the unit because O(δ) = η⁻²⁴. W47's whole units
    are m = 24n.
  - The index is I = −χ_{3/2+m/2}(ρ ⊗ ε_r ⊗ χ_η^m) + Σ_{p ∈ cond} χ_{1+m/2}(p ⊗ …).
  - E₈ needs the family part in SU(3): det = χ_η^{9+3r+3m} = 1, that is, m ≡ 5 − r (mod 8). So m = 0 and m = ±24
    are never admissible.
  - Three occurs at twelve data. The least is m = 17 (ε₄ or ε₁₂, condition 0).
- **C8: B1796, B1797 and GENESIS FK10 [v1.59]** (main).
  - The object is ρ_T (= ρ, B1634 and B1730) at weight 3/2, with m units of end data on its eigenlines. The dimension
    is max(0, Σm). It is proved 3n for uniform O(nδ), n ≥ 0.
  - The unit reduces to four links, none derived: the field's existence, the type identification, uniform end data
    and the least remainder (n = 1).
  - B1796, B1797 and GENESIS never cite W134 and never place ρ_T in E₈'s family slot.
- **K2: W135's rule, cell K2** (`docs/dossiers/the_weave_2026-10-07/W135_RULE.md`).
  - The full 27's anomalies are n_SU3 = n_SU2 = 18(3 + r + m) and n_grav = 81(3 + r + m), mod 24. They vanish iff
    m ≡ 5 − r (mod 8). The 16 alone needs only m odd.
  - The seat's script took per-field weights from W101. B1736 rebuilt K0, K1, K3 and K4 on main, and uses
    ρ′ = ρ ⊗ χ_η^k with k ∈ {5, 13, 21} (det-1) as the family group. Its FINDINGS state that K2 was not re-derived.
- **Main's instruments used:**
  - B1632's χ formula (float);
  - B1641's lifts and its six-solution pieces V2 and V4;
  - B1730's exact q-series space() and its part A (the theta multiplier against ρ).
- **What M53 asks to locate:** whether the two use different objects, a different count (three 27s against something
  else), or a different cusp normalisation.

## 2. What is computed (`relays/sm_r610/run.py <main checkout>`)

- **R0, the instrument.**
  - χ_k in exact Fractions, on monomial matrices whose entries are roots of unity. Eigenvalue turns come from the
    permutation's cycles, so nothing is floating.
  - Calibrations: the trivial representation, η and η².
  - Agreement with main's float χ (B1632) at every allowed (k, twist), for k from −1/2 to 51/2.
- **R1, the object.**
  - ρ satisfies Mp2(ℤ)'s relations exactly, and its T-exponents are (1/8, 3/8, 7/8).
  - Main's theta multiplier equals ρ (B1730 part A).
  - Main's lift ρ_T (B1641) is equivalent to ρ: the intertwiner space is one-dimensional and invertible.
- **R2, C8's requirement re-derived.**
  - χ_{3/2+12n}(ρ) = 3n for n = 0 to 4, and W134's I(0, cond 0, 24n) = −3n.
  - B1730's own space(0, n) and a dressed variant of it (exact q-series; stable under the pole allowance) give 3n for
    n = 1, 2.
- **R3, W134's admissibility from the definition.**
  - The exponent c of det(ρ ⊗ χ_η^a) = χ_η^c is computed exactly on T and checked on S, not assumed.
  - The checks: admissible iff c ≡ 0 (mod 24); the twists allowing weight 3/2; never at 0 or ±24; never at any whole
    unit.
- **R4, W134's count.**
  - Condition 0 is computed exactly.
  - Conditions V2, V4 and L6 use B1641's pieces in float, under both valid identifications, with the T part on main's
    own lift.
  - The outputs: the |I| = 3 data, the least |m| giving three, and the bounds at the least datum and for |m| ≤ 16.
  - A second route by q-series dimension at the positive-m three-generation data of condition 0.
- **R5, the location.**
  - The unit's multiplier χ_η²⁴ is trivial, so W134's m = 24n is C8's O(nδ) exactly.
  - At whole units the determinant exponent stays 9 + 3r ≠ 0.
  - The dressing moves χ by the floors alone (W134's closed form).
  - C8's three equals |I(0, 0, 24)|.
- **R6, the joint frame:** k = r + m (mod 24) at each three-generation datum, against B1736's k ∈ {5, 13, 21}.
- **R7, K2 re-derived without per-field weights.**
  - The route: E₈'s 240 roots (exact), then E₆ (72 roots orthogonal to an A₂), then the 27 as a 27-root class
    projected off A₂, then D₅ (the roots orthogonal to a 27-weight) and the 16.
  - The 27's Dynkin index is computed against every E₆ root, and the 16's and 10's against every D₅ root. Because
    the index is the same for every root, the (SU(3), SU(2)) weights are fixed for any regular embedding.
  - n_G = w_G · c (mod 24), with c from R3. The checks: W135's formula, the full 27 anomaly-free ⇔ det-1 ⇔
    m ≡ 5 − r (mod 8), and the 16 alone ⇔ m odd.
- **Plants and control.**
  - **P1, a wrong normalisation:** the unit taken as η⁻¹² (n units = m = 12n). It must fail both:
    - on C8, by computation: χ at the plant's units is not 3n;
    - on W134, because the least three read in the plant's units is not 17/24. This half is a relabelling, and is
      disclosed as such.
  - **P2, a discriminating plant:** the dressing acts on the weight only, with no character.
    - It must reproduce C8, because χ_η²⁴ is trivial.
    - It must fail W134, because no datum is then admissible.
  - **CT, the control:** the conjugate hand allows weight 3/2 at no allowed twist and no whole unit (GENESIS v1.42,
    v1.59).

## 3. Expectations, written before any run

| cell | expectation | prior |
|---|---|---|
| R0 | the exact χ is calibrated and agrees with main's float χ everywhere (< 1e-9) | 95% |
| R1 | ρ is a genuine Mp2(ℤ) representation, equal to main's theta multiplier and equivalent to main's lift ρ_T | 93% |
| R2 | C8's 3n holds by χ and by both q-series routes (n = 1, 2), with W134's I(0, 0, 24n) = −3n | 93% |
| R3 | c(a) = 9 + 3a (mod 24); admissible iff m ≡ 5 − r (mod 8); no whole unit is ever admissible | 95% |
| R4a | condition 0: three at (4,17), (12,17), (12,−23), (0,21), (8,21), (8,−19); least \|m\| = 17 | 90% |
| R4b | all conditions: W134's twelve, none below \|m\| = 17; \|I\| ≤ 1 at the least datum, ≤ 2 for \|m\| ≤ 16 | 80% |
| R4c | the q-series dimension is 3 at the four positive-m data of R4a | 85% |
| R5 | same object, normalisation (m = 24n ⇔ O(nδ)) and count; the parting is E₈'s determinant alone | 85% |
| R6 | every three-generation datum has k ∈ {5, 13, 21}; the 17/24 data have k = 21 (r = 4) and k = 5 (r = 12) | 90% |
| R7 | the 27's index is 6 and the 16's 4 against every root; W135's K2 formula and equivalences hold | 90% |
| P1 | fails both | 90% |
| P2 | reproduces C8 and fails W134 | 85% |
| CT | no weight-3/2 space for the conjugate hand | 92% |

Seen before the card, by hand and disclosed:
- the closed form Δχ = Σ⌊λ + m/24⌋, which follows from the formula because the S and ST terms do not move;
- c = 3(3 + a), so 27c ≡ 0 (mod 24) ⇔ c ≡ 0 (mod 8) ⇔ det-1;
- the k values of W134's twelve data;
- P1 at n = 1 gives χ = 1, not 3.

Nothing has been computed by script on the real cases.

## 4. What the outcomes mean (fixed now)

- **R1 to R5 hold: they do not contradict each other; C8 is scoped.**
  - C8's reduction holds for ρ_T taken outside E₈'s family slot.
  - The parting is not a different object, count or normalisation. It is one extra condition that C8 does not impose:
    E₈'s determinant condition. By R7 that condition is K2, the anomaly of the full 27.
  - With the triplet as E₈'s family SU(3) (P-302; B1736's own frame uses ρ′ with det-1), the whole unit is excluded at
    every n. The least uniform datum with three chiral 27s is then 17/24.
  - So C8's links change inside that frame. Link 3 (uniform end data) stands. Link 4 (the least remainder, n = 1)
    becomes m = 17 under the same "least" rule. Separately, the frame must explain why m ≡ 5 − r (mod 8): W134's
    "what fixes m?".
  - The scoping sentence proposed for main, a GENESIS amendment by main only: "FK10 [v1.59] holds for ρ_T outside E₈'s
    family slot; in the E₆ × SU(3) frame of P-302 the unit is inadmissible (W134; K2) and the least three-generation
    datum is 17/24."
- **R5 fails** (the normalisations differ): the reconciliation is a units correction, which is recorded, and W134's
  reading is revised.
- **R4's pieces lane fails** while condition 0 holds: 17/24 stands at condition 0 only, and the claim "none below 17"
  is withdrawn for V2, V4 and L6.
- **R7 fails:** K2 stays unverified, and the failure is recorded as found.
- **No outcome removes an input. 0 of 19.**

## 5. Not checked, by design

- Flat U(1) lines inside E₆, which could absorb the determinant (W134 left them out; the seat's relay names them).
- Per-line (non-uniform) fractional data.
- Whether the field's three (C8, B1700's reading) and the 27s' three are one space inside E₈.
- The per-field SM weights. Only the 27 and the 16 are re-derived.
- K2's identification of the moves' anomaly as n_G = w_G · c. That is the record's definition (B1674), used as given.

## 6. Files

- `relays/sm_r610/run.py` (sealed);
- phase 2 adds r610_results.json, the run log and the page relays/SM_R610_W134_AGAINST_C8.md.
