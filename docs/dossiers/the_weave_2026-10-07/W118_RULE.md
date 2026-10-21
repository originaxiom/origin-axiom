# W118 — the first generation: does the composite field, the fermions' own bilinear, lift the first generation's zero with a forced power and a forced coefficient the data accept? (the rule, committed before the code)

The SM-derivation seat, 2026-10-21. Committed before the script that reads it exists. Nothing here is a result.

## Why

- **The owner's order** (2026-10-21): three arcs, each done properly, then a pause to consolidate. This is the
  second: the first generation, stage 3 of the goal page (`THE_SKELETON_AND_THE_FLESH.md`).
- **What the record leaves.** In the frame of W64–W69 (B1644's coupling, the Higgs and the coupling among the
  parameter-free sections of ρ_R), every forced pairing leaves the first generation massless, or fixes m₁m₃/m₂² near ω
  at 15 or 1 (W68). The data give 0.54 (up), 2.7 (down) and 0.081 (leptons).
- **The candidates** (the reading after W69):
  - (c), end data at the puncture;
  - (d), a composite field, the fermions' own bilinear;
  - (e), an exponential sector.
- **Only (d) has an object on record.**
  - (c) needs P-108's parent map, still owed.
  - (e) needs the exponential sector of L201, never built.
  - This arc tests (d), and the record keeps (c) and (e) open by name.
- **What would count.** A forced coefficient for the first generation that matches a sector's data, with the
  look-elsewhere count stated. A match is a candidate only: the count drops only if a later arc confirms it in a
  coherent assignment across the sectors and the CKM.

## The composite (fixed now)

- **The fermions' sections.** At weight 3/2 the three placements with one unit, u = (1, 0, 0), (0, 1, 0) and
  (0, 0, 1), each give one section (W68 G1). Call them S₁, S₂ and S₃. They span the uniform unit's space, the chiral
  three (W64 K5).
- **The composite Higgs directions** are their cross products, P₁ = S₂ × S₃, P₂ = S₃ × S₁ and P₃ = S₁ × S₂. The
  record's reading (d) names this bilinear: the cross product M ⊗ M → M is O-equivariant. Each Pₗ is a weight-3
  vector-valued form, and the basis is canonical, being the one-unit sections.
- **The hypothesis H-comp:** the Higgs is one of the Pₗ. It joins W68's hypotheses: B1644's form
  Y(a; c) = acᵀ + caᵀ − (a·c)𝟙, H-sec, and H-pair′, with the coupling c among the sections.

## The pairings (fixed now)

- **The new pairings** are every Pₗ with each of W68's seven sections (E, R and R′ at −½; S₁, S₂ and S₃ at 3/2; the
  one section X at 7/2), and every pair of composites (Pₗ, Pₗ′), the same composite included. That is 21 + 6 = 27.
  B1644's form is symmetric in a and c, so a pair is unordered.
- **By hand: which pairings lift the zero** (to be checked).
  - det Y(a; c) = (a·c)(a·a)(c·c), because Y(a × c) = −(a·c)(a × c) and Y acts on span{a, c} as ((0, c·c), (a·a, 0)).
  - So m₁ = 0 exactly when a·c = 0, or a or c is isotropic.
  - R and R′ are isotropic at every τ (W68 G2), so their 6 pairings keep m₁ ≡ 0.
  - Pₗ is orthogonal to the two sections it is made from, so those 6 pairings keep m₁ ≡ 0 too.
  - The other 15 lift it generically: Pₗ with E, X or the third S, and the 6 composite pairs. The identities used
    are Lagrange's, Pₗ·Pₗ = (Sₘ·Sₘ)(Sₙ·Sₙ) − (Sₘ·Sₙ)², and Pₗ·Sₗ = det(S₁, S₂, S₃); neither vanishes for generic
    sections.
- **At ω** all three Sₖ lie on the real axis (1, −1, −1) (W68 G2), so every Pₗ vanishes there, to first order in
  δ = |τ − ω|.

## The tests (fixed now)

- **The displacement.** τ = ω + iδ with δ = 10⁻⁴, 10⁻³ and 10⁻², at 40 digits, as in W68.
- **The powers.** p₁ and p₂ are the slopes of log(m₁/m₃) and log(m₂/m₃) against log δ, between neighbouring δ.
- **The forced coefficient.** For a pairing with the full hierarchy (p₁ > p₂ > 0, both stable to 0.05 across the two
  intervals), the double ratio m₁m₃/m₂² is read at δ = 10⁻⁴ as its limit.
  - The limit is checked by its change from 10⁻³ to 10⁻⁴, which must be below 1%.
  - Otherwise the pairing is reported with its trend and is not scored.
- **The data's windows** (W66's data and allowance, a = 0.10).
  - The double ratio's log-error is σ = √(σ₁² + σ₂²), with σᵢ = hypot(relᵢ, 0.10) for the sector's two ratios.
  - The window is |ln(DR/DR_data)| ≤ 1.96σ. By hand:
    - up: 0.538, window 0.35 to 0.84;
    - down: 2.68, window 1.81 to 3.97;
    - leptons: 0.0807, window 0.061 to 0.107.
- **The look-elsewhere count.** The number of scored pairings times three sectors. Any hit is reported against that
  count.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| H0 | the control: W68's sections reproduced (residuals below 10⁻²⁰, the lines at ω as in W68 G2), and W68's double ratios for E with X (15) and for X with X (1) reproduced to 10⁻⁶ | 95% |
| H1 | the composites: each Pₗ vanishes at ω to first order (the slope of log\|Pₗ\| against log δ within 0.02 of 1), and Pₗ/δ tends to a vector on one of the two isotropic lines, l_ω or l_ω² (sine below 10⁻³ at δ = 10⁻⁴) | 80% |
| H2 | the lift as derived: the 12 pairings named above have m₁/m₃ below 10⁻³⁰ at all three δ and at 0.13 + 1.21i and −0.31 + 1.07i (W68's probe points), and the other 15 have m₁/m₃ above 10⁻²⁰ at those two points | 85% |
| H3 | read-out: every new pairing's powers (p₁, p₂) and, where scored, its double ratio | — |
| H4 | **the verdict:** no scored pairing's double ratio falls in any sector's window | 60% |

## What the outcomes mean (fixed now)

- **H4 holds.** The composite field lifts the first generation's zero, but no forced coefficient it gives near ω
  matches the data. Candidate (d) fails in W68's frame. (c) and (e) stay open, with no object on record.
- **H4 fails.** Some pairing's forced double ratio falls in a sector's window. That is a candidate, read against
  the look-elsewhere count.
  - It counts only if a later arc places it in a coherent assignment: the three sectors' pairings, one δ, and the
    CKM, as in W69, rule first.
  - It goes to main as a candidate. The count stays 0.
- **In every case** the first generation's power is forced (p₁) by the pairing, and the coefficient is a pure number.
  That is the kind of identity the reading of W49–W54 expected a principle to force.

## Weave or thread

**WEAVE-type, given Λ (GENESIS FK11) and the stated hypotheses (B1644's form, H-sec, H-pair′, H-comp).**
- The sections are the weave's matter representation ρ_R. Every pairing the hypotheses allow is taken, with none
  hand-picked.
- The claim (H4) is about all of them at once.
- The point ω is the weave's own fixed point, the quartic's minimum (W67).

## Seen before the rule (disclosed)

- **W64 to W69's records:** the sections, their lines at ω, W68's powers and coefficients (15 and 1), and W69's census.
- **The data's double ratios and windows,** computed by hand from W66's data and errors.
- **The identities above,** derived by hand.
- **No composite section has been evaluated** at any τ, by this seat or, as far as this seat knows, on record.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
