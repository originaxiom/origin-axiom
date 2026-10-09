# W47 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **Main named it** (relay of 2026-10-09, S104): "If you see a forcing of one unit of end data at the weave's cusp
  (FK10), that is the arc."
- **W45 and W46** found, given Λ, that the triplet's four-dimensional index on the weave's own surface is n times the
  fibre's index, where n is the cusp's units of end data. The weave's natural cusp condition gives n = 0.
- **The owner ruled the unit open** (2026-10-09): no postulate. This arc asks whether anything the surface carries
  forces it.
- **Two kinds of candidate are left:**
  - an end condition at the cusp other than the canonical one;
  - a twist of the triplet by a line bundle on the surface.
- This arc reads both, completely. What it leaves is GENESIS FK10's question, in its sharpest form.

## Weave or thread?

The quantities are defined on the weave's own surface, by every move at once. The twists are every flat line bundle the
surface admits, and the conditions are every natural one; none is chosen. Weave-type.

## The facts the arc rests on (a READING, by hand)

- **Every line bundle on the weave's open surface is flat.**
  - The surface's orbifold fundamental group is Aut⁺(F₂) on the metaplectic cover. Its inner automorphisms die in the
    abelianization: the coinvariants of H₁(F₂) under the moves are ℤ²/((L − 1)ℤ² + (R − 1)ℤ²) = 0.
  - So the characters are those of Mp₂(ℤ), whose abelianization is ℤ/24. Through B₃ → ℤ, σ ↦ 1, the element S̃⁸
    maps to 24.
  - The 24 characters are the powers ε_r = v_η^r of η's multiplier. Every non-flat twist is cusp data, the units of
    W46, since the open moduli space's Picard group is torsion.
- **Which twists are allowed.** ε_r keeps the forced weights (3/2 on T, 1 along the puncture, ½ on T̄) exactly when
  r ≡ 0 mod 4. Otherwise the twisted field has no sections and contributes nothing.
- **The exponents are never integers.**
  - The triplet's cusp exponents are odd multiples of 1/24: {3, 9, 21}/24 on T, {3, 21}/24 on V2 and {3, 9, 15, 21}/24
    on V4.
  - The reason is as follows. On T the monodromy is v_η³ times the cube's rotations (W45). The moves' c-twist
    e^{iπ(r−ℓ)/4} is that odd power of η's multiplier, and a rotation's exponents are multiples of ¼, even numerators
    over 24. On the six the monodromy is a permutation of the parities (exponents 0 or ½, even numerators) times a 2O
    element whose eigenvalues e^{±iπ/4} give odd numerators.
  - An allowed twist adds 4m/24, which is even. So no exponent is ever 0 mod 1.
  - With no integer exponent, the natural conditions at the cusp coincide: the canonical extension, the L² condition
    for the complete metric at any power of the weight, and compact support. None supplies a unit.
- **The twisted index, by the calibrated formula.**
  - At n = 0 it is 0 for every allowed twist and every puncture condition, except at r = 4 and r = 20.
  - At r = 4 it is −1 for the conditions 0 and V4.
  - At r = 20 it is −1 for V2 and L₆.
  - The sign is the record's hand convention, and the conjugate hand gives the negatives.
  - The L₆ row equals its H⁰ form, χ_{1/2}(ρ̄_T ⊗ ε_r), at every r.
- **The full index** is I(Λ₊, r, n) = n·f(Λ₊) + t(Λ₊, r), where f is the fibre index and t ∈ {0, −1} the twist's
  term. With |n| ≤ 1, |I| = 3 occurs only at a natural puncture condition, with t = 0 and n = ±1.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1** | Exact: the coinvariants of H₁(F₂) under L and R vanish; the abelianization of B₃ sends S̃⁸ to 24, so the flat line bundles are the 24 characters ε_r. ε_r keeps the forced weights exactly when r ≡ 0 mod 4. | 97% |
| **K2** | For the record's lifts and every allowed twist, every cusp exponent of T, T̄, the six, V2 and V4 is an odd multiple of 1/24. None is an integer, so the natural cusp conditions coincide. | 90% |
| **K3** | The formula's twisted index at n = 0 is 0 everywhere except: −1 at r = 4 for the conditions 0 and V4, and −1 at r = 20 for V2 and L₆. The L₆ row equals its H⁰ form at every r. No twist gives ±3. | 80% |
| **K4** | The second route (q-expansions, W45's method) gives dimension differences equal to the formula's χ for every allowed twist and piece. The individual dimensions are reported, not predicted. | 80% |
| **K5** | The full table over the four puncture conditions, the 24 characters and n ∈ {−1, 0, 1} is I = n·f + t. \|I\| = 3 occurs only at the conditions 0 or L₆, with t = 0 and n = ±1. | 85% |

**The reading, written before the run.**
- **If K1 to K5 hold, nothing on the weave's surface forces the unit.**
  - Every natural cusp condition is the canonical one, since no exponent is an integer.
  - Every flat line bundle the surface admits moves the index by at most one, never by three.
- **The only route to a chiral three on the weave's own surface is one unit of end data at the cusp.** That unit is a
  non-flat source. On the open surface it is the trivial bundle λ¹² ≅ O extended by Δ⁻¹, which vanishes nowhere on the
  open surface and has a simple pole at the cusp.
- **So GENESIS FK10 at the cusp is not answerable inside the weave.** It needs a source, as the owner's ruling keeps
  open.
- **If K3 or K5 fails** (a twist giving ±3), that twist would be the forcing main asked for, and the reading changes.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
