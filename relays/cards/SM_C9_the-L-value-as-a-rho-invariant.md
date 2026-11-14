# SM-C9 — is SM-C7's twisted value at s = 0 the U(1) ρ invariant of the closed torus bundle?

*Card of the SM seat, 2026-11-14, approved by main before it was written (M25). Committed and pushed, with its
expectations, before anything of it is computed. Data-free: rationals and two finite formulas. Proposed in
`relays/SM_LITERATURE_NOTE_1.md`, §§ 3 and 5.*

## 1. The question

- Atiyah (1987) showed that, for a hyperbolic M in SL(2, ℤ), the η invariant of the torus bundle T²_M equals Meyer's
  function, Hirzebruch's signature defect and the Shimizu L-value at 0. All of these are odd under orientation
  reversal.
- Bohn (arXiv:0907.3530) computed the U(1) ρ invariant of T²_M for the flat connection of every ν with
  (Id − Mᵗ)ν ∈ ℤ²: Theorem 4.4.20, and its form (4.67).
- **The question:** is SM-C7's Z(0, χ_c), on the same M and the same characters, that ρ invariant up to a stated
  normalisation?
- **Why it matters.** If it is, the record's L-value at 0 is an orientation-odd spectral invariant of the closed torus
  bundle, and so a candidate carrier for the hand (SM-C6 E2's bit c). If it is not, that reading closes.

## 2. What will be computed

- **The population.** SM-C7's 601 characters (`relays/sm_c7/population.json`), each carrying:
  - the level's monodromy M = [[a, b], [c, d]], with D = (a + d)² − 4;
  - the character (i/N, j/N);
  - SM-C7's Z(0, χ_c), as committed.
  - Nothing of SM-C7 is recomputed.
- **The flat connection.** ν = −(i/N, j/N), with Bohn's M the record's M. ρ is even in ν. That (Id − Mᵗ)ν ∈ ℤ² is
  checked on every character; a character that fails is listed and left out.
- **ρ_A(T²_M) by Bohn's (4.67):**
  - (2(a+d)/c)(P₂(ν₁) − 1/6) − 4 sgn(c)(s_ν(a, c) − s(a, c)) + sgn(c(a+d));
  - s_ν(a, c) = Σ_{k=0}^{|c|−1} P₁((k + ν₁)/c) P₁(a(k + ν₁)/c + ν₂); s(a, c) is the Dedekind sum;
  - P₁ is the sawtooth (0 on ℤ), and P₂(x) = {x}² − {x} + 1/6. Exact rationals throughout.
- **The checks of the transcription,** before any comparison:
  - T1: Theorem 4.4.20's expanded form agrees with (4.67) on every character, under one of the two readings of its
    bracket. The reading that agrees is named.
  - T2: Corollary 4.4.21, ρ ≡ 2(ν₂ m₁ − ν₁ m₂) mod ℤ, holds on every character.
  - T3: the theorem of orientation reversal, ρ(M⁻¹, ν) = −ρ(M, ν), holds on every character.
- **The comparison.** On every level: the best affine fit of ρ_A(c) against √D·Z(0, χ_c) over the level's
  characters, with its slope, its intercept and its largest residual. Across levels: whether the slope is one number.

## 3. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| T1–T3 | the transcription checks hold on every character | 90% |
| X1 | on every level with three or more distinct values of Z(0), ρ_A is an exact affine function of √D·Z(0, χ_c) (largest residual ≤ 10⁻⁹) | 50% |
| X2 | the slope is the same rational on every level | 35% |
| X3 | the intercept on each level is a function of M alone, Atiyah's untwisted η or a multiple of it | 30% |

## 4. The outcomes

- **A:** X1 and X2 hold. Up to one universal normalisation, Z(0, χ_c) is the twisted ρ invariant of the closed torus
  bundle. The record's L-value at 0 is then an orientation-odd spectral invariant, a candidate carrier for the hand.
- **B:** X1 holds and X2 does not. There is a relation level by level, with a normalisation that depends on the level;
  it is named.
- **C:** X1 fails. The reading closes. A negative is reported with its second computation (ρ by Theorem 4.4.20's
  expanded form), as main's gate asks.
- **Stop:** if T1, T2 or T3 fails, the transcription is wrong. The run says so and compares nothing.

## 5. Controls that must fail if the work is broken

- **P1 (orientation):** ρ(M⁻¹, ν) in place of ρ(M, ν), with the slope and intercept fitted on the unflipped data. The
  relation must fail wherever ρ ≠ 0. The sign must flip.
- **P2:** Z(0) permuted among a level's characters. The affine relation must fail on every level with three or more
  distinct values.

## 6. Files

relays/sm_c9/, with its script, output and run. The page is relays/SM_C9_THE_L_VALUE_AS_A_RHO_INVARIANT.md.
