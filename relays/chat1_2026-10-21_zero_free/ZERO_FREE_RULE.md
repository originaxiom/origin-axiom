# The zero-free layer: the strong angle's census read as "where a quark is massless" (the rule, committed before the code)

chat1, 2026-10-21. Committed and pushed before the script that reads it exists. Nothing here is a result. 0 of 19.

## Why

- **W113 and W114** (the SM seat, c9f001d9d) sort every quark sector of the record's frame by whether θ̄ is constant
  over the weave:
  - automatic, at w = 0;
  - tuned, at w = 12n, costing n real conditions;
  - impossible, at every other w.
  Here det Y = η^a·g, with g a level-one form of weight w = 3k − a/2. W113's lemma says why: a level-one form is
  zero-free on H only if it is cΔ^n.
- **W114** found θ̄ = 0 at every τ compatible with the quarks only where the model carries as many numbers as the
  data. It read the tunings as bought: "the Standard Model's own count with θ̄ tuned to zero".
- **The reading this rule prepares** (chat1; to be written after the run, not assumed by any cell):
  - A zero of g in H is a state τ₀ where a quark is massless.
  - So "θ̄ constant over the weave" is the same as "no state inside the weave has a massless quark".
  - If PF1 is read on the weave ("cancelling to nothing completes only at the end"), the tuned layer is forced, not
    bought.
  - Feruglio, Marrone, Strumia and Titov (arXiv:2505.20395, 2025) assume exactly that ("quark masses never vanish
    except in the de-compactification limit τ = i∞"), with no reason given.
- **What this rule tests** is the physical reading of the census on the seat's own code, the claims the reading needs
  that are not already on record. It also tests the same condition on the record's other modular object, the cusp's
  dressing (W48).

## The instrument (the script, written after this rule)

- **The SM seat's code, unchanged.** It imports `the_strong_angle.py` (sha256 a9c4b15b…028622) and `the_tuned_fit.py`
  (sha256 21f979be…49c713b). Both are read from `docs/dossiers/the_weave_2026-10-07/` at c9f001d9d into a temporary
  directory, and their hashes are checked before import.
- **Precision.** mpmath at 50 digits for every cell value, set after import. Seed 20261021.
- **Definitions.**
  - r(τ) = σ_min(Y(τ))/σ_max(Y(τ)), the massless measure. r = 0 is a massless quark.
  - G(τ) = det Y(τ)/η(τ)^{6k}, of weight 0. At w = 12 it should be αj + β.
  - Members are real combinations of the seat's real basis, with coefficients drawn standard normal.
  - "Generic τ" means the seat's GENERIC5[0:3].

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| Z0 | the control: the seat's spaces give W113's recorded dimensions for all 16 (type, k); `classify` returns the recorded class; w = 3k − a/2 lies in 6ℤ for all 16 | 98% |
| Z1 | impossible means a massless quark at τ = i, for every coupling: in each of the seven impossible sectors with w > 0 (T⊗T at k = 3 and 7, T̄⊗T̄ at 5, mixed at 2 and 6 in both orders), for 10 random real members, r(i) < 10⁻²⁵, while r > 10⁻¹² at ω and at the three generic τ | 88% |
| Z2 | a generic tuned member has a massless point, on a CP locus: in each of the four w = 12 sectors (T⊗T at 5, T̄⊗T̄ at 7, mixed at 4 in both orders), for 10 random real members, (a) G = αj + β to 10⁻²⁵ (fitted at two τ, checked at four more); (b) α and β real to 10⁻²⁵; (c) the point τ₀ of F̄ with j(τ₀) = −β/α, found by bisection on the CP locus where j takes that real value, has r(τ₀) < 10⁻²⁰ | 85% |
| Z3 | tuned members are zero-free: in the same four sectors, for 10 random lines through the seat's tuned-variety parametrisation (W114's `SectorParam`, root refined at 50 digits), every root with G ≢ 0 has G constant to 10⁻²⁰ across six τ (the three generic τ, i + 0.01i, ω + 0.01i, and 2.5i), and r > 10⁻¹⁵ at τ = i and τ = ω and at those six τ. Roots with G ≡ 0 (rank-two members, as in W113 T1) are counted, at most two in the forty | 85% |
| Z4 | the end's dressing (W48's candidates with trivial multiplier): (a) \|E₄(ω)\| < 10⁻⁴⁰, so E₄/Δ and E₄²/Δ vanish at ω; (b) the Niemeier dressings Θ_L/Δ = j − 720 + N vanish inside F̄ for N = 0 (Leech) and N = 1104 (D₂₄⁺), at the τ₀ found by bisection, to 10⁻³⁰; (c) η^c(τ + 1)/η^c(τ) = e^{2πic/24}, trivial only for c = 24 among 8, 12, 16, 24. So 1/Δ is the only candidate zero-free on H with trivial multiplier | 98% |
| R1 | read-out: ψ(τ) = (Im τ)^{1/2}\|η(τ)\|² on a grid of F̄ (with the Kähler factor (2 Im τ)^{k/2} per entry, a zero-free sector's \|det\| is \|c\|·2^{3k/2}·ψ^{3k}); the maximum's location and value, and ψ at i and at ω. The prediction for the record is that the maximum is at ω | 90% |
| R2 | read-out (feasibility, no data, no fit): the leptons under the reading at a fixed τ. The symmetric parts' dimensions of T⊗T at k = 1, 5 and T̄⊗T̄ at k = 3, 7, taking a Weinberg coupling in the symmetric part of the (s_L, s_L) space, chat1's assumption; whether the w = 12 cubic restricted to the symmetric part has non-degenerate real roots; and the table of admissible (charged-lepton, Weinberg) pairs with free real numbers at fixed τ against the seven measured lepton observables | — |

## What the outcomes mean (fixed now)

- **Z1 to Z3 hold.**
  - The seat's census, read physically, is this. An impossible sector has a massless quark at τ = i for every
    coupling. A tuned sector's generic member has a massless point on a CP locus, and the one real condition removes
    it. A zero-free member has no massless point anywhere inside H.
  - So "θ̄ constant over the weave" (W113's lemma) is the same as "no state inside the weave has a massless quark".
  - The reading is then a candidate source of the tuned layer: forced if PF1 is read on the weave. That is a reading,
    not a cell, and nothing here adopts it.
- **Z1 fails.** The impossible class is not "massless at i" as worded, and the reading's account of it fails.
- **Z2 fails.** The tuning is not the removal of one massless point as worded. The reading's identification of
  "tuned" with "no interior massless state" has to be restated.
- **Z3 fails.** This would contradict W113 T1 and W114 U1. It is read as an instrument error until found.
- **Z4.** The facts are textbook, so a failure is read as a coding error. If it holds, the reading applied to the
  cusp's dressing keeps only 1/Δ among W48's candidates. With W48's S1, the dressed counts then come in 3ℤ, and three
  is the least non-zero.
- **In every case nothing here lowers the count.** 0 of 19.

## Seen before the rule (disclosed)

- **Read in full:**
  - W113 and W114: the rules, the NOTE sections, the code and W114's run output, including the sixteen χ²_min and the
    best τ;
  - W45 to W48's NOTE sections, including W48's S1 to S4 (|E₄(ω)| = 1.5 × 10⁻¹⁵ is on record there);
  - the abstracts and excerpts of arXiv:2305.08908 (FST 2023), 2406.01689 (FPST 2024) and 2505.20395 (FMST 2025).
- **Estimated by hand while writing this rule** (no code): ψ(i) ≈ 0.590, ψ(ω) ≈ 0.596 and ψ(1.5i) ≈ 0.558.
- **No code has been run** on any space, member, root or dressing.

## Discipline

- This rule is committed and pushed before the script exists.
- The script is committed before its one run, and its output is committed before it is read.
- A failed launch is disclosed, with its log kept. A failed cell is recorded as failed. Any later check is labelled
  post hoc.

chat1, 2026-10-21. 0 of 19.
