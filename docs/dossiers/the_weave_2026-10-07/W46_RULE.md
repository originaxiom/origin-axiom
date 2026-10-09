# W46 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **W45 found, given Λ, that the triplet's four-dimensional index on the weave's own surface is 0.** That holds at
  the weight the geometry forces, with no zero modes at all, for the canonical conditions at both ends.
- **Two ends remain to be read in full.**
  - The puncture section: W22 and W28 give six local solutions and four conditions the moves keep, with fibre index
    −3, −1, +1 and +3.
  - The cusp: W45's post-hoc reading gives n units of end data on every component.
- **W45 took the two extreme puncture conditions only.** This arc takes all four, with the cusp's units. It so reads
  every end condition the weave keeps on its own surface.
- This is the last freedom inside the weave for GENESIS FK11's earning condition. What it leaves is GENESIS FK10's
  question at the cusp.

## Weave or thread?

The quantity is defined on the weave's own surface, by every move at once. The conditions are all the ones the moves
keep (W28); none is chosen. Weave-type.

## The object (a READING, by hand)

- **The operator.** W45's four-dimensional Dirac operator: the odd spin structure on the fibres, and weight 3/2 from
  K_Y^{1/2}.
- **The puncture condition.** 𝕎 is extended along the puncture section P by a subspace Λ₊ of the six local solutions
  L₆: exponent −½ on Λ₊ and +½ elsewhere. Λ₊ = 0 is W45's canonical condition.
- **Along P.** The quotient of the two extensions is Λ₊ ⊗ λ^{−1/2} on P ≅ M₁,₁.
  - The normal coordinate z is a section of N_P^∨ = λ. The frames are z^{∓1/2} times flat local solutions.
  - Twisted by K_Y^{1/2}|_P = λ^{3/2}, the quotient has weight 1.
  - So the index for Λ₊ is W45's plus χ₁(ρ_{Λ₊}), where ρ_{Λ₊} is the moves' action on Λ₊.
- **The local solutions' representation.**
  - W28 builds the six in the block basis. There each lift of a move acts as an unsigned permutation of the parity
    blocks times its 2O element. That is W24's blocks_action, a pushforward, so it is the monodromy directly.
  - The cohomology T is a pullback (W21's on_V), so its monodromy is the inverse.
  - Both come from the same lifts (W38's lift_choices), with σ₁ = L, σ₂ = R⁻¹, S = S̃⁻¹ and T = L, as in W45.
- **The puncture's exact sequence.** For Λ₊ = L₆:

  0 → H⁰(fibre, all allowed) ⊗ λ⁻¹ → L₆ ⊗ λ^{−1/2} → H¹(fibre, canonical) → 0.

  - So the six's exponents are the union of the two triplets' exponents.
  - The central characters fit: ρ_T(S)² = i, ρ₆(S)² = −1 and ρ̄_T(S)² = −i give the same scalar on the twisted bundles,
    at weights 3/2, 1 and ½.
  - So W45's two representations are the two extreme puncture conditions, W28's ±3, whose sign is the orientation.
    ρ_T is the canonical condition's H¹, at weight 3/2. ρ̄_T is the all-allowed condition's H⁰, at weight ½.
- **The cusp's units.** n uniform units at the cusp add n times the fibre's index, since χ_{k+12} = χ_k + d on every
  piece. Per-component units add a signed sum, so they can reach any integer, and every one of them is a choice.
- **Why everything vanishes (by hand).**
  - Every piece's exponents are at least ⅛, which is η³'s exponent.
  - Divide a zero mode by η³. The result is a holomorphic form of weight at most 0, whose multiplier has no invariant
    vector.
  - So with the canonical cusp condition every space is zero, and every χ is 0, for every puncture condition.
  - The formula agrees piece by piece: tr ρ₂(S) = tr ρ₄(S) = 0, the traces of ST are real, and the exponents are
    symmetric under λ ↦ 1 − λ.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **H1** | The structure, with the record's lifts. The braid relation holds on T and on the six. ρ₆(S)² = −I, and S̃⁴ acts on the six as I (on T, −I). V2 and V4 are invariant. tr ρ₂(S) = tr ρ₄(S) = 0; tr ρ₂(ST) = 1 and tr ρ₄(ST) = −1. Their exponents are {⅛, ⅞} and {⅛, ⅜, ⅝, ⅞}. The six's exponents are the union of ρ_T's and ρ̄_T's. The central characters fit the exact sequence at weights 3/2, 1 and ½. | 80% (70% for the union with the lifts as built) |
| **H2** | The formula: χ₁(ρ₂) = χ₁(ρ₄) = 0, and χ₁(ρ₆) = χ_{3/2}(ρ_T) + χ_{1/2}(ρ̄_T) = 0. The calibration η² at weight 1 gives 1. | 90% |
| **H3** | The other overall lift sign, which is the base direction's other square root (v_η¹²). The braid relation holds, and every χ above is 0 again, W45's included. | 85% |
| **H4** | The second route. q-expansions find M₁ and the dual S₁ zero for ρ₂ and ρ₄ under both signs, and W45's four spaces zero under the other sign. η² has dimension 1. | 85% |
| **H5** | The table. For each of the four puncture conditions, with n ∈ {−1, 0, 1} uniform cusp units, the four-dimensional index is n(\|Λ₊\| − 3). That is 0 at n = 0. At n = 1 it is −3, −1, +1 and +3, in the order Λ₊ = 0, V2, V4, L₆; at n = −1, the negatives. | 90% |

**The reading, written before the run.**
- **If H1 to H5 hold.** Given Λ, on the weave's own surface, the triplet's four-dimensional index is n times the
  fibre's index. That holds for every end condition the moves keep at the puncture and every uniform condition at the
  cusp.
- **No end condition the weave keeps gives a chiral count.** Every natural cusp condition has n = 0 (W45). So there
  is no chiral count, and no zero mode at all.
- **The record's ±3 becomes four-dimensional only with a unit at the cusp.** That ±3 comes from W22 and W28; it is a
  flat count under the natural puncture condition (ruling 3). It becomes a four-dimensional ±3 exactly when one unit
  of end data sits at the cusp.
- **So GENESIS FK11's earning condition on the weave's surface becomes GENESIS FK10's question at the cusp.**
- **If H2 or H4 fails** (a non-zero χ₁ for a middle condition), that condition carries a four-dimensional index of
  its own. The index is recorded as found, and the reading changes.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
