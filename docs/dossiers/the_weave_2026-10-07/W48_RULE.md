# W48 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **W45 to W47:** given Λ, a chiral three on the weave's own surface needs one unit of end data at the cusp. Nothing in
  the weave supplies that unit (GENESIS FK10).
- **The owner chose to explore an outside source** (2026-10-09): a reading first, then a rule-first test if it holds
  up. The reading ("an outside source for the cusp's unit") is in the dossier and relay §52.
- **The reading's claims:**
  - a source of weight w turns χ_{3/2} into χ_{3/2−w};
  - three needs w = −12 with no zeros on the open surface, that is 1/Δ;
  - under the simplest dressing, the heterotic string's left-movers give one.
- **This arc computes those claims,** at all four puncture conditions, with the actual spaces counted by a second route.

## Weave or thread?

The object is the weave's own surface, read by every move at once, with every condition the moves keep. The sources
are candidates from outside the weave, chosen by a stated rule (below), none hand-picked within a family. The quantity
is weave-type. Whether any source applies is a dictionary question beyond the principle, so the arc's claim is
conditional on that dictionary.

## The rule for the candidates

- **The sources are the vacuum characters of chiral sectors with c = 24,** the value that gives one unit at the cusp,
  in two families:
  - **(L) a lattice family.** An even self-dual lattice of rank ℓ ∈ {0, 8, 16, 24} with 24 − ℓ further oscillators.
    The source is Θ_L/Δ, of weight ℓ/2 − 12 and trivial multiplier. Θ_L is 1, E₄, E₄² or E₄³ + cΔ, since M_k has
    dimension 1 for k = 4 and 8.
  - ℓ = 16 is the heterotic string's left-movers, for E₈ × E₈ and Spin(32)/ℤ₂ alike.
  - ℓ = 24 is any Niemeier or the Leech lattice. Every one gives j plus a constant, which has weight 0.
- **(O) an oscillator family.** c chiral oscillators with no lattice, 1/η^c for c ∈ {8, 12, 16, 24}. The source has
  weight −c/2 and multiplier v_η^{−c}. c = 24 is the bosonic string's light-cone left-movers.
- **The dressing.** A dressed zero mode is f = g·F with F holomorphic. A piece ρ at weight k becomes F of weight k − w
  with multiplier ρ ⊗ (g's multiplier)⁻¹, and its index is the χ of that.
- **The four-dimensional dressed index** for a puncture condition Λ₊ is
  −χ(T at 3/2) + Σ over Λ₊'s pieces of χ(piece at 1), each read in the dressed way. The L₆ row equals the dressed
  χ(T̄ at ½).

## The facts by hand (from W45's and W47's closed forms)

- **The lattice family.** tr ρ_T(ST) = 0, so χ_{3/2+4j}(ρ_T) = j and χ_{1/2+4j}(ρ̄_T) = j. On V2 and V4 the ST term
  has period 6 in the weight.
  - For w = −4j the dressed index, in the order (0, V2, V4, L₆), is:

| w | 0 | V2 | V4 | L₆ |
|---|---|---|---|---|
| +4 | +1 | 0 | 0 | −1 |
| 0 | 0 | 0 | 0 | 0 |
| −4 | −1 | 0 | 0 | +1 |
| −8 | −2 | −1 | +1 | +2 |
| −12 | −3 | −1 | +1 | +3 |
| −24 | −6 | −2 | +2 | +6 |

  - So for Θ_L/Δ at the canonical condition the count is (24 − ℓ)/8: 3, 2, 1, 0 for ℓ = 0, 8, 16, 24. That is one
    mode for every eight chiral bosons that carry no lattice.
- **The oscillator family.** The counts at the canonical condition are 1, 1, 2, 3 for c = 8, 12, 16, 24. Each is W47's
  twisted χ at r = c, carried up the weight, since F = f·η^c takes the multiplier ρ ⊗ v_η^c.
- **The analytic facts.**
  - E₄ vanishes at ω.
  - E₄² = 1 + 480q + 61920q² + …, and the two rank-16 lattices have 480 roots each.
  - 1/Δ has no zeros on the open surface, while j − 744 has one.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **S1** | The lattice family's dressed index, by the formula, is the table above at all four puncture conditions, and the L₆ row equals its H⁰ form. The canonical counts are (24 − ℓ)/8. | 90% |
| **S2** | The oscillator family's canonical counts are 1, 1, 2, 3 for c = 8, 12, 16, 24. At c = 24 the four conditions give W46's n = 1 row: −3, −1, +1, +3. | 85% |
| **S3** | The second route (q-expansions, W45's method, at the shifted weights) gives dimension differences equal to χ for every candidate and piece. At the canonical condition the dressed spaces of T have dimension 1, 2, 3 for ℓ = 16, 8, 0, with every dual cusp space zero. | 80% |
| **S4** | The analytic facts. E₄(ω) = 0 to working precision. E₄²'s q-coefficients begin 1, 480, 61920. The root counts of E₈ ⊕ E₈ and D₁₆⁺ are 480 each. | 95% |

**The reading, written before the run.**
- **If S1 to S4 hold, the source must be lattice-free.** The count of a c = 24 source is one per eight chiral bosons
  without a lattice. So three needs 24 lattice-free chiral bosons: the bosonic string's light-cone left-movers, in 26
  dimensions.
- **The heterotic string gives one.** It is the record's natural home for E₈: eight transverse bosons free, sixteen on
  the lattice.
- **No candidate natural to a four-dimensional world gives three in this dressing.** The reading's outside source does
  not hold up as the missing unit. GENESIS FK10 stays open, as the owner ruled.
- **If S1 or S3 fails,** the law is wrong and the reading is withdrawn.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
