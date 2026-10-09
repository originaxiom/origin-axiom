# W45 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-09. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **GENESIS FK11's earning condition** (main, B1604): an even-dimensional object the weave forces, carrying a non-flat
  bundle whose index is the count.
- **W19 named the object:** the weave's own surface M₁,₂, the universal punctured fibre over the moduli M₁,₁ of the
  shared fibre.
- **W20 read it in the 27** and found three, but not chiral. Its erratum named the next step, "not a result": a
  holomorphic index of the complex triplet T on the weave's orbifold, which can tell T from T̄.
- **Main's map** (2026-10-08) lists "the gauge count's chirality from end data or dimension ≥ 4".
- This arc takes that step for T, given Λ (the owner's ruling 2: the left-handed states are the fibre's holomorphic
  zero modes).

## Weave or thread?

The quantity is defined on the weave's own surface, by the joint action of every move: all of the modular group
through T's representation. No thread is chosen. Weave-type.

## The object, and why the weight is forced (a READING, by hand)

- **The operator:** the four-dimensional Dirac operator on Y = M₁,₂, twisted by 𝕎, with the fibre's odd spin
  structure. That is the only spin structure every move preserves; the moves permute the three even ones.
- **The weight.** Kodaira's formula gives K_Y = π*λ³ up to the cusp, with λ the records' Hodge line, so the spinors
  carry π*λ^{3/2}.
- **Leray.** The fibre's H⁰ vanishes, and R¹π_* of 𝕎 is the bundle of the conjugates of the fibre's zero modes. 𝕎's
  monodromy is finite, so its period map is constant, and the zero modes form a flat bundle 𝒯 with monodromy ρ_T.
- **So the index is a Riemann–Roch number** of vector-valued modular forms:
  - χ_k(ρ) = dim M_k(ρ) − dim S_{2−k}(ρ^∨), taken at weight 3/2;
  - for one hand ρ = ρ_T, for the other ρ = ρ̄_T.

  The sign is the hand, a convention (GENESIS v1.31). The magnitude is not.
- **The weight is forced, not chosen (cell E1).**
  - In Aut⁺(F₂), the element S̃⁴ = (L R⁻¹ L)⁴ is an inner automorphism. On T its lift acts as −I, for every choice of
    lift signs.
  - Every inner automorphism acts on T by a parity sign, of determinant +1.
  - So T is not a local system on M₁,₂ itself. It is one on the metaplectic double cover (S̃⁸ acts as 1), where only
    half-integral weights carry it.

## The formula, and how its signs are fixed

- χ_k(ρ) = d(k − 1)/12 + ¼ Re[e^{iπk/2} tr ρ(S)] + (2/(3√3)) Re[e^{iπ(2k+1)/6} tr ρ(ST)] + d/2 − Σ_j λ_j.
  - The source is Borcherds (2000, §7) and Skoruppa.
  - ρ(T) has eigenvalues e^{2πiλ_j}, with 0 ≤ λ_j < 1.
  - The convention is f(γτ) = (cτ + d)^k ρ(γ) f(τ), with the principal √τ.
- **The two phase signs were fixed by hand on known cases** while this rule was written. Cell E2 recomputes them:
  - the trivial representation at weights 0, 2 and 12 (χ = 1, 0, 2);
  - η at weight ½ (χ = 1);
  - W41's Weil representation of (θ₃, θ₂)(· | 2τ), with W(T) = diag(1, i), at weight ½ (χ = 1).
- **ρ_T's data** come from W38's normal form, through the braid generators σ₁ = L and σ₂ = R⁻¹, with S̃ = σ₁σ₂σ₁ and U
  = ST.
  - Both identifications S ↔ S̃^{±1} and T ↔ L^{±1} are taken, for ρ_T and for ρ̄_T.
  - A convention is kept only if χ_k is an integer at every weight up to 15/2 that its central character allows,
    ρ(S)² = e^{−iπk}.

## The second route

- The dimensions dim M_k and dim S_k are found numerically, with the convention E3 keeps.
  - The q-expansions are taken to order N, with each component carrying its exponent λ_j.
  - f(−1/τ) = τ^k ρ(S) f(τ) is imposed at points of the unit arc between ω and ω + 1, where |q| ≤ e^{−π√3}.
  - The dimension is the number of singular values below a gap, which is reported.
- It is calibrated first on η and on the Weil representation (dimension 1 each at weight ½).
- It is then run:
  - for ρ_T: M_{3/2}, M_{7/2}, and S_{1/2} of ρ_T^∨;
  - for ρ̄_T: M_{1/2}, M_{5/2}, and the matching cusp spaces.
- So χ is checked against actual dimensions.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **E1** | (L R⁻¹ L)⁴ is an inner automorphism of F₂; its lift acts on T as −I for every lift sign, while every inner automorphism acts by a parity sign of determinant 1; S̃⁸ acts as 1. So T is a genuine representation of the metaplectic group, not a local system on M₁,₂. | 95% |
| **E2** | The formula with the stated signs gives 1, 0, 2 (trivial), 1 (η) and 1 (Weil). | 95% (by hand) |
| **E3** | Integrality across the allowed weights keeps exactly one of the four identifications for each hand: for ρ_T the pair (S ↔ S̃, T ↔ L⁻¹), which is the left action the record's right action gives, and for ρ̄_T its conjugate. Under it: χ_{3/2}(ρ_T) = 0 and χ_{7/2}(ρ_T) = 1; χ_{1/2}(ρ̄_T) = χ_{5/2}(ρ̄_T) = 0 and χ_{9/2}(ρ̄_T) = 1. By hand, tr ρ_T(ST) = 0, and the S-term and the cusp exponents cancel at the lowest weights. | 80% |
| **E4** | The numerical dimensions agree with χ at every weight computed. Whether the individual spaces at the lowest weights are zero is not predicted. | 75% |

**The reading, written before the run.**
- If E1 to E4 hold, then on the weave's own surface, read by the four-dimensional Dirac operator with the only spin
  structure the moves keep, the triplet's index is zero for both hands. The weave's even-dimensional object gives no
  chiral three. Any zero modes it has come in vector-like pairs.
- Three needs weight 15/2 or more in this table, and nothing in the geometry supplies that weight.
- With T-NO-INDEX-IN-THREE (B1604, on threads) and W20 (an Euler characteristic, not chiral), this closes the weave's
  own route to GENESIS FK11's index in its canonical reading. The chiral three needs end data (GENESIS FK10) or a frame
  beyond the weave's surface.
- If E3 fails (an index of ±3 at the geometric weight), the earning condition would be met in this form, given Λ.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.
