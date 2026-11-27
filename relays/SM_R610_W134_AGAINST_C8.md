# SM-R610 — W134 against C8: same object, same unit and same count; they part on E₈'s determinant alone, and K2 holds

*Page of the SM seat, 2026-11-26, for register row P-610 (main's page M53). The sealed card is
`relays/cards/SM_R610_w134-against-c8.md`. Script `relays/sm_r610/run.py`, SHA-256 d60e1f635336fb6a, sealed in
8a6f01fd6 before its run. One run (about 25 s). Its output `relays/sm_r610/r610_results.json` has SHA-256
93d98d5b25ec1b9a; the log is `relays/sm_r610/r610_run.txt`. No post-hoc file. Data-free. **0 of 19.***

## 1. Result against the sealed cells

The card's table holds the expectations word for word. Here each one is given in short.

| cell | sealed expectation (short) | prior | result |
|---|---|---|---|
| R0 | exact χ calibrated, equal to main's float χ | 95% | **held**: 318 comparisons, worst 1.8e-15 |
| R1 | ρ is Mp2(ℤ) and is main's multiplier and lift | 93% | **held**: part A 4e-30; one intertwiner, s_min 0.577 |
| R2 | C8's 3n by χ and by two q-series routes | 93% | **held**: 3n for n = 0..4; q-series 3 and 6, stable |
| R3 | admissible iff m ≡ 5 − r (mod 8); no whole unit | 95% | **held**: c(a) = 9 + 3a; r ∈ {0, …, 20}, \|m\| ≤ 24 |
| R4a | condition 0: the six threes; least \|m\| = 17 | 90% | **held** |
| R4b | all conditions: W134's twelve, none below 17 | 80% | **held**: \|I\| ≤ 1 at least datum, ≤ 2 to 16 |
| R4c | q-series dimension 3 at the positive-m data | 85% | **held**, stable under the pole allowance |
| R5 | same object, unit and count; parting = det | 85% | **held** |
| R6 | k ∈ {5, 13, 21}; 17/24 at k = 21 and k = 5 | 90% | **held** |
| R7 | indices 6 (27), 4 (16); K2's formula holds | 90% | **held**; the 10's index is 2 |
| P1 | unit as η⁻¹²: must fail both | 90% | **failed both**: dims 0, 1, 3, 4, 6; reads 17/12 |
| P2 | weight-only dressing: C8 yes, W134 no | 85% | **as predicted**: 0 admissible data |
| CT | conjugate hand: no weight-3/2 space | 92% | **held** |

Every cell held as sealed. No prediction failed.

## 2. Reading

- **The object is the same.**
  - W134's ρ (ζ₈P, ζ₈L⁻¹) is main's theta multiplier (B1730).
  - It is equivalent to main's lift ρ_T (B1641, B1634), C8's object.
- **The normalisation is the same.** The unit's multiplier χ_η²⁴ is trivial on S and T. So W134's m = 24n is C8's
  O(nδ) exactly, and I(r, 0, 24n) = −(χ_{3/2}(ρ ⊗ ε_r) + 3n) for every allowed r.
- **The count is the same.**
  - C8's three-dimensional space is W134's |I(0, 0, 24)|.
  - At positive dressed weight the index equals the dimension: the q-series gives 3 at W134's positive three-generation
    data.
- **They part on one condition that C8 does not impose: E₈'s family slot must be SU(3).**
  - At whole units the determinant stays χ_η^{9+3r}, never trivial. So no number of whole units is admissible.
  - The admissible data are m ≡ 5 − r (mod 8).
  - Three chiral 27s first occur at m = 17, under the twists ε₄ (k = 21, the cube's rotations of B1736) and ε₁₂
    (k = 5).
  - P2 shows the parting directly. A dressing that ignores the character reproduces C8 and kills W134, because C8's
    whole unit cannot see the character.
- **K2 is re-derived on an independent route.**
  - The 27's Dynkin index is 6 against every E₆ root, and the 16's is 4 against every D₅ root. So the (SU(3), SU(2))
    weights hold for any regular embedding, without W101's per-field weights.
  - With n_G = w_G · c and c = 9 + 3(r + m) computed exactly: n_SU3 = n_SU2 = 18(3 + r + m) and
    n_grav = 81(3 + r + m) (mod 24).
  - The full 27 is anomaly-free ⇔ the family part is det-1 ⇔ m ≡ 5 − r (mod 8). The 16 alone needs only m odd.
- **So the honest outcome is "scope C8", not a contradiction.** The cells support the scoping sentence drafted on the
  card. It is offered for main to adopt or not, through main's own amendment machinery:

  > GENESIS FK10 [v1.59]'s reduction holds for ρ_T outside E₈'s family slot. With the triplet as the family SU(3) of
  > E₈ ⊃ E₆ × SU(3) (P-302; B1736's ρ′ = ρ ⊗ χ_η^k, k ∈ {5, 13, 21}), the whole unit is excluded at every n by the
  > determinant condition, which is the full 27's anomaly (K2). The least uniform datum giving three chiral 27s is then
  > 17/24 of the unit (W134), at ε₄ or ε₁₂. Link 3 (uniform data) stands; link 4 (the least remainder) reads m = 17.
  > What fixes m ≡ 5 − r (mod 8) is open.

## 3. What is not checked

- **Flat U(1) lines inside E₆,** which could absorb the determinant and restore a whole unit. W134 left them out, and
  so does this page. This is the one route by which C8's whole unit could survive inside E₈.
- **Per-line fractional data.** C8's per-line formula is not redone.
- **Whether C8's Higgs/zero-mode space and the 27s' family space are one space inside E₈.** B1700 tags that as a
  reading.
- **The per-field SM weights:** only the 27, 16 and 10 indices are derived.
- **K2's definition n_G = w_G · c** is the record's (B1674), used as given, not derived as physics.
- **The float lanes.** V2, V4 and L6 rest on B1641's float pieces. That module's source was run up to its H section, so
  that it writes nothing.
- **No second seat has run this.**
