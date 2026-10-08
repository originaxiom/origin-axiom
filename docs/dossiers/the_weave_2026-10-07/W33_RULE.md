# W33 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. The values below were derived by
hand before this was written and are listed as such. Nothing here is a result.

## Why this route

- **The owner, 2026-10-08:** "do it". The proposal was to test whether "three appears exactly when the odd spin
  structure is left out" holds as a law across the record's frames (the second contemplation, point 2).
- **The contemplation's reading of W32:** the weave's five cured naturally at four reads as the three parity pieces plus
  the zero parity's piece.
- **The audit lane's packets of 2026-10-08:** the record's counts are sheaf Euler characteristics. With the bounding
  spin structure, the gauge −1 channels are periodic (gapless at the complete cusp), and the gauge +1 channels are
  antiperiodic (no zero vertical modes). The record has counted the gauge +1 (character) channels two ways: 0 in W23,
  natural in W32.
- **The hand derivation already suggests the strong form fails.** This arc tests the contemplation's own claim, and a
  failure corrects it.

## Weave or thread?

- **Weave-type.** The bundles are built from the common point's blocks; every bundle L and R keep is taken; the end
  conditions are those the joint action keeps.
- **Every frame is a hypothesis** (GENESIS GAP1). Every count is conditional on it.

## The objects

- **The frames (W23's).**
  - E₆: V of rank 3, n(27) = index V.
  - SO(10): V of rank 4, n(16) = index V.
  - SU(5) (F-HE): W of rank 5, n(10) = index W, n(5̄) = index Λ²W, free of anomaly when equal.
  - E₆'s and SO(10)'s counts are free of anomaly automatically.
- **The bundles:** every sum of blocks (χ₀, χ₁, χ₂, χ₃, D = ρ_Q) of the frame's rank with trivial determinant that L
  and R keep (an invertible intertwiner for each). Computed by enumeration.
- **The index (W22, W28):** n = −r₋/2 + dim Λ₊.
- **The three conventions the record has used:**
  - **(B) W22's block rule:** Λ₊ is the whole gauge −1 eigenspace (each doublet block +1, each character block 0).
  - **(N) naturality on every channel** (W28, W32): Λ₊ kept by the lifts of L and R and by the bulk commutant.
  - **(S) the spinor rule:** naturality on the gauge −1 channels, and no gauge +1 channel in Λ₊ (the audit lane's
    antiperiodic channels).
- **The zero parity's blocks** are χ₀ and D = χ₀ ⊗ ρ_Q. Since χ_p ⊗ ρ_Q ≅ ρ_Q for every p, the doublet blocks are
  isomorphic whatever their label.

## The cells

The script is `the_odd_spin_structure_across_frames.py`, writing `.json` beside it.

- **T1, the census.** By hand: E₆: χ₀³, D ⊕ χ₀, P. SO(10): χ₀⁴, χ₀ ⊕ P, D ⊕ χ₀², D². SU(5): W32's five.
- **T2, the counts.** By hand:

  | frame | bundle | (B) | (N) | (S) |
  |---|---|---|---|---|
  | E₆ | χ₀³ | 0 | 0, 3 | 0 |
  | E₆ | D ⊕ χ₀ | 1 | −1, 0, 1, 2 | −1, 1 |
  | E₆ | P | 0 | 0, 3 | 0 |
  | SO(10) | χ₀⁴ | 0 | 0, 4 | 0 |
  | SO(10) | χ₀ ⊕ P | 0 | 0, 1, 3, 4 | 0 |
  | SO(10) | D ⊕ χ₀² | 1 | −1, 1, 3 | −1, 1 |
  | SO(10) | D² | 2 | −2, 2 | −2, 2 |

  - SU(5), the anomaly-free counts: (B) W23's set; (N) W32's table (0, 0, 1, {1, 4}, ±2); (S) 0 for χ₀⁵ and χ₀² ⊕ P,
    none for D ⊕ χ₀³ and D ⊕ P (±1 against ±3), ±2 for D² ⊕ χ₀.
- **T3, the naive law** ("a three occurs exactly for the bundles without the zero parity's blocks"). Predicted FALSE.
  - Under (N): E₆'s χ₀³, built from the zero parity alone, gives 3. SO(10)'s D ⊕ χ₀² gives 3 = 1 + 2. SO(10)'s χ₀ ⊕ P
    gives 3 with χ₀ present. Only E₆'s P fits the law.
  - Under (B) and (S) no three occurs below rank six, so the law is vacuous there.
- **T4, the spinor-rule law.** Under (S) each sector's count is ± its number of doublet blocks: the doublets form
  ρ_Q ⊗ ℂ^k whatever their labels, with commutant U(k), and naturality keeps all or none.
  - So E₆ ∈ {0, ±1}, SO(10) ∈ {0, ±1, ±2}, and SU(5)'s anomaly-free counts are 0 and ±2.
  - No three below rank six: W23's "three needs rank six", as a law.
- **T5, the doublet sectors themselves.** 𝕎 = ⊕ χ_p ⊗ ρ_Q (k = 3) and 𝕎 ⊕ D (k = 4), under (N) and (S): ±3 and ±4.
  - This is the precise form of the contemplation's point: when the zero parity's doublet shares a sector with the
    three parity doublets, the count is four, and no condition the weave keeps separates it.
- **T6, the sources of each three under (N):** which pieces Λ₊ holds. By hand:
  - E₆'s P: the three parity lines;
  - E₆'s χ₀³: three trivial lines;
  - SO(10)'s χ₀ ⊕ P: the three parity lines, χ₀ left out;
  - SO(10)'s D ⊕ χ₀²: the doublet and two trivial lines.
- **T7, the verdict (predicted).**
  - **The naive law is not a law.**
  - Under the spinor rule, three needs three doublet blocks, so rank six. Only 𝕎's sector holds them, and adding the zero
    parity's doublet makes four.
  - Under naturality, three is a rank count, available to the trivial bundle, so it is not evidence of the weave's three.
  - **The contemplation's point 2 is downgraded.** The counts do not single out the odd spin structure by its label.
    What they count is the number of doublet blocks.

## What each outcome means

- **As predicted.**
  - Point 2 is withdrawn in its strong form and kept in its precise form (T5).
  - The record's best statement for the count stays 𝕎, at rank six, with its link Λ.
  - Whether three can appear below rank six depends only on how the gauge +1 channels are counted. The audit lane's spin
    analysis favours (S), where it cannot.
- **The naive law holds.** Point 2 stands, and the odd spin structure's exclusion becomes the question.
- **(S) gives three below rank six.** Re-read the doublet structure before anything is written.
- **A different census.** Record it, and read T2 from the computed list.

## Seen before this was written

- **By hand:** every table above, from the block structure (χ_p ⊗ ρ_Q ≅ ρ_Q; Λ²(D ⊗ ℂ²) = χ₀ ⊗ ℂ³ ⊕ P; the
  commutants of sums of distinct characters).
- **The record:** W22, W23, W28 and W32; the audit lane's five packets of 2026-10-08. No cell was computed before this
  rule.
