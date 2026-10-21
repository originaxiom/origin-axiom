# B1691 — THE EXPONENTS AT THE TWO FIXED POINTS (P-227, PART 1): IF THE HIGGS'S DIRECTION IS A COVARIANT SECTION, THE MASS RATIOS NEAR THE CUSP ARE POWERS OF ONE |q| — m₂/m₃ ~ |q|^½ AND m₁/m₃ ~ Im τ·|q| AT EVERY WEIGHT — AND NEAR ω THEY FOLLOW THE RESIDUAL ℤ₃ CHARGE; W72'S HIGGS MODE IS η⁶R, EXACTLY ISOTROPIC

**Verdict: PROVED (exact identities, and a census of the covariant sections to weight 23/2 by two routes).** cc (main),
2026-10-21. POINT_REGISTER P-227 (its first half; the comparison with the measured masses is P-240, to be sealed). 0 of 19.
- **The question.** W62 (verified, B1686) says every content on record runs τ to a cusp. P-227 asked whether that run is
  the mechanism of the hierarchy rather than a failure: near the cusp (and near ω) do the record's mass ratios scale as
  powers of one small number, with the powers fixed by residual charges?
- **The tagged hypothesis (H-cov).** The Higgs's direction a in M is a covariant section: a vector-valued modular form for
  the matter's representation ρ_R (or ρ′ = ρ_R ⊗ χ_i). What fixes the direction is P-115, open; H-cov is a dictionary
  choice, not derived.
- **The record's formulas used (main's own arcs).** The coupling Y(a) = aRᵀ + Raᵀ − (a·R)𝟙 with the theta triplet
  R = (−θ₂², −θ₄², iθ₃²)/(πθ₂θ₃θ₄) (B1645); the massive pair's s₁s₂ = |R|²|a·a| and
  s₁² + s₂² = 2|R|²|a|² + 2|a·R̄|² − |a·R|² (B1646); the first generation's lift L·m₁/m₃ = |a·a||D||a·R|/(2πs₁²s₂)
  (B1654), so **m₁ = |D||a·R|/(2πL|R|²), independent of a·a**; |D|/|R|² ~ e^(−π Im τ)(8π² Im τ + K) at the cusp and
  |D| ~ |τ − ω| at ω (B1654); L of order one at both (B1667).
- **The sections.** ρ_R's forms are generated over the scalar forms by R (weight −½), ∂R and ∂²R (Serre derivatives):
  their Wronskian is exactly −(i/8)η⁹, which never vanishes on ℍ. At weight k = 2n − ½ a section is
  f₀R + f₁∂R + f₂∂²R with f_j holomorphic of weight 2n − 2j. ρ′'s sections are η⁶ times ρ_R's, which changes no ratio.
- **The identities (exact, in q^{1/8}-series over ℚ(i)).** R·R ≡ 0 (Jacobi), R·∂R ≡ 0, R·∂²R ≡ −∂R·∂R, and ∂R·∂R ≠ 0
  (leading ¼ x², x = q^{1/8}). So **a·R = −f₂(∂R·∂R)**: the first generation is lifted only through the ∂²R component.
- **At the cusp (the T-charges ⅛, ⅞, ⅜ of e_i, v₊, v₋).** For every weight from −½ to 23/2 (seven weights, two random
  sections each):

  | sections | m₂/m₃ | m₁/m₃ |
  |---|---|---|
  | a ∝ R (weight −½) | 0 | 0 |
  | no ∂²R component (weights 3/2, 11/2; f₂ = 0 at any weight) | ∝ \|q\|^½ | 0 |
  | **every section with a ∂²R component (weights 7/2, 15/2, 19/2, 23/2)** | **∝ \|q\|^½** | **∝ Im τ·\|q\|** |
  | the control: B1646's constant directions (not covariant) | → a constant (½ or 1; no hierarchy) | ∝ Im τ·\|q\|^½ |

  q = e^{2πiτ}. The second route, direct evaluation at τ = 3i, 4i, 5i, gives slopes 0.500 and 0.500 for m₂/m₃ and 0.945,
  0.959 for m₁/m₃, the Im τ factor's predicted shortfall from 1 (0.054, 0.041). The control's law, e^(−π Im τ) times the Im τ factor,
  has an effective slope of about −2.7 over Im τ ∈ [2.2, 3.6], consistent with B1667's measured −2.63 (T4), which also
  carries L's variation.
- **At ω (the ST-charges).** ρ(ST) = i·P L⁻¹ has one real axis (eigenvalue −i) and two isotropic eigenlines (eigenvalues e^{iπ/6} and
  e^{5iπ/6}), and a(ω) lies on the one fixed by k mod 6 (computed: the other two components vanish to 10⁻³⁹). With
  ε = τ − ω and D's linear zero:

  | k mod 6 | a(ω) | m₂/m₃ | m₁/m₃ |
  |---|---|---|---|
  | 7/2 (7/2, 19/2) | an isotropic eigenline | ∝ \|ε\| | ∝ \|ε\| |
  | −½ (23/2; at −½ and 11/2 m₁ = 0) | the other isotropic eigenline | ∝ \|ε\|² | ∝ \|ε\|³ |
  | 3/2 (15/2; at 3/2, m₁ = 0) | the real axis | → ½ (no hierarchy) | ∝ \|ε\|² |

  Slopes from ε = 10⁻⁵ and 10⁻⁶ along three directions and two sections each, equal to three decimals.
- **W72's Higgs mode is η⁶R.** The SM seat's surface mode h (weight 5/2 for ρ′, found by collocation) is η⁶R up to
  normalisation: its first nine coefficients on (v₊, e_i, v₋) are exactly the seat's (1, 4, −4, 1, −4, 12, −8, −20, −8).
  So h·h ≡ 0: as a Higgs direction in B1645's coupling it would leave two generations massless.
- **What it means.** Under H-cov, in the regime where W62 says τ runs, the hierarchy is discrete exponents times one
  departure: every sector's m₂/m₃ goes as |q|^½ and m₁/m₃ as Im τ·|q|, the same |q| for all sectors on one fibre, with
  O(1) coefficients set by the section. Equivalently m₁/m₃ ∝ Im τ·(m₂/m₃)² in every sector. Near ω the exponents are
  the weight's residual charge. Neither τ nor the coefficients are fixed: **this is a reduction to exponents and one
  scale, not a derivation of a number**, and nothing computed holds τ (W62). The mechanism is the one known in modular
  flavour models near fixed points (Novichkov–Penedo–Petcov; Feruglio and collaborators); the representation, the
  coupling and the first generation's lift are the record's.
- **What it does not do.** No comparison with measured masses (P-240, sealed first); no mixing; one Higgs direction per
  sector; B1654's lift formula is its large-L limit, within 17–25% of the exact canonical lift on B1667's grid.

## 0. Seen first

`VERDICT topic-sweep /near the cusp|near omega|near ω|q-expansion|residual (charge|symmetr)|exponents? (of|fixed by)|hierarch(y|ies) (from|as) (powers|exponents)|Froggatt|modular weight|discrete exponents/
(full text): 28 of 1462 arcs on main match` — chiefly B1637 (with one τ the modular structure fits the charged fermions
only with 21 or more parameters; its near-cusp fits were evaluator artifacts, P-144), B1617 and B1618 (τ = ω: degenerate
masses where the inner automorphisms act), B1629 and B1630 (the principle does not reach the cusp; the tick's point),
B1654 and B1667 (the lift and its cusp law), B1612 and B1620 (the finite mixing set; the breaking the weave allows).
None computes the exponents of the record's coupling under a covariant Higgs. **Literature:** vector-valued modular forms
as a free module (Marks and Mason); the Serre derivative; Feruglio, "Are neutrino masses modular forms?" (2017);
Novichkov, Penedo and Petcov, fermion mass hierarchies from residual modular symmetries near fixed points (2021);
Feruglio, Gherardi, Romanino and Titov, modular invariant dynamics and fermion mass hierarchies around τ = i (2021).

## 1. Disclosed

- **Value contact before any seal (main's, in this session).** While planning P-227 main set, from memory, the
  log-ratios of measured light-to-heavy mass ratios (about 2.9 for the charged leptons, 2.3 for the up quarks, 1.8 for
  the down quarks) beside hand estimates of this arc's exponents: first δ = ½ for the isotropy defect with a ratio
  (δ + 1)/δ = 3, then (½, 3/2) with ratio 3. Both estimates carried a slip (below); the computed exponents are (½, 1),
  ratio 2 up to the Im τ factor. No computation touched data. P-240, the comparison, will be sealed with its criterion
  stated before any data are read, and will carry this paragraph.
- **Main's slips, caught before the record.** (1) B1654's "q" in its cusp law is the nome e^{iπτ}; the first instrument
  read it as e^{2πiτ} and gave m₁/m₃ ∝ |q|^{3/2}. Caught when the constant-direction control disagreed with B1667's measured
  e^(−2.6 Im τ); confirmed in B1654's code (q = exp(−π y)). (2) The second route first dropped D's factor |R|² (a slope of
  1.2 instead of ≈ 0.95); fixed. (3) The exploration that found the census's shape was run before the instrument was
  written (`verification/before_the_instrument/`); the instrument was written after it and run as given.
- **The m₁ exponent rests on B1654's large-L formula** at L of order one (B1667: 17–25% from the exact canonical lift); the
  m₂ exponent rests on B1646's exact D3 identity alone.

## 2. Files

- `verification/qseries.py` (exact series in q^{1/8} over ℚ(i)), `verification/the_exponents.py` → `the_exponents.json`,
  `verification/the_exponents_run.txt`; `verification/before_the_instrument/` (the exploration).
- The lock: `tests/test_b1691_the_exponents_at_the_two_fixed_points.py`.

> *Addendum 2026-10-21 (S160; P-240 assessed, no data read).* **The exponents alone predict no mass, because the
> section's coefficients are free.** At weight 7/2, the lowest with a ∂²R component, a = α E₄R + β ∂²R, and the leading
> coefficients (exact: R and ∂²R on v₊ at x⁻¹ are −½ and −1/96; ∂R·∂R and ∂²R·∂²R at x² are ¼ and −5/576) give
> (m₁/m₃)/(m₂/m₃)² ∝ Im τ·|t r + r₂|³ / (|r|·|t − c₂₂/(2 d₁₁)|²) with t = α/β. Its pole (t = −5/288, where a·a's leading
> coefficient vanishes) and its zero (t = −1/48, where |a|²'s does) are distinct, so the ratio takes every positive value:
> six measured ratios against seven unknowns (|q| and one complex t per sector), and no inequality survives. A test needs
> the section fixed (P-115). **The one parameter-free covariant direction with a massive second generation** is the
> weight-3/2 section a = ∂R (the space is one-dimensional): m₁ = 0 and **m₂/m₃ = 18 |q|^½ + …** (exact leading
> coefficient; direct evaluation 18.0058, 18.00001, 18.0000000 at Im τ = 3, 5, 7). Two sectors with that Higgs would have
> equal m₂/m₃. `verification/the_coefficients_are_free.py` → `the_coefficients_are_free.json`. No comparison was made.
