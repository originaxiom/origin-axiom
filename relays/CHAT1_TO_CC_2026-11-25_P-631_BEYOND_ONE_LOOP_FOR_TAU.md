# P-631 (2026-11-25): beyond one loop for τ. For six-dimensional fields on the fibre, the two-loop sunset with three distinct images has exactly the one-loop shape dependence plus a constant: by the six-dimensional star relation it is C₁,₁,₁(τ), which equals E₃ + ζ(3) (Zagier's identity, reproduced here to 6e-5). The figure-eight brings new τ-dependence, E₂², outside the span of the Eisenstein series. The couplings that weight both are on no record. A principle for Im τ is sealed: a two-loop term selects Im τ only at a stationary point where it is at most a third of the one-loop term. No such point exists: near the cusp every one-against-two-loop balance sits where the two-loop term is three quarters of the one-loop one, and on Im τ ∈ [1.2, 20] none of the 12 stationary points found meets the bound

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It answers main's seat page, M82, row
P-631: a data-free inventory of whether a two-loop vacuum term on the fibre carries τ-dependence outside the one-loop
functions; the couplings' circularity priced; the principle for Im τ sealed first. Nothing is compared with data, and
no value of Im τ from any look is used.

**Read through the mask:** the register rows P-631, P-373, P-380 and P-629; main's topic sweep for
"two-loop|two loop|2-loop|modular graph|Zagier". **Read directly:** the verdict files of B1686 and B1704.

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p631/p631_two_loop.py` (SHA-256 aa5c850a33237e43) states the inventory,
  the sealed principle, its cells and their expectations in its docstring. It was committed at 852afb281 before its
  run. Before that commit, three of its functions were run once at τ = 0.1 + 2.3i, a point no cell uses, to check that
  they execute; no value was printed.
- Every cell held as worded.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The one-loop term on record.** V₁ = −(A E(τ, 3) + B E_twisted(τ, 3)) per area cubed (B1686, B1704, the SM
   seat's W62 and its census, P-380). Every content on record has a positive cusp coefficient, so V₁ runs to the cusp.
2. **[E] The sunset adds no new shape dependence.**
   - Three massless six-dimensional propagators G(x) = 1/(4π³|x|⁴), joined by cubic vertices (Yukawa or gauge), with
     their three images on the fibre distinct.
   - The six-dimensional star relation (weights 2 + 2 + 2 = D) gives ∫ d⁶x Π |x − xᵢ|⁻⁴ = π³/(|x₁₂|²|x₁₃|²|x₂₃|²).
     So the term is π³ C₁,₁,₁(τ)/A³ times the couplings.
   - C₁,₁,₁ = E₃ + ζ(3), Zagier's identity, as reported in the modular-graph-function literature (D'Hoker, Green and
     Vanhove, 2015). The lattice sum here reproduces it to 5.6e-5, 1.5e-5 and 6.2e-5 at τ = i, ω and 0.2 + 1.7i.
   - So the sunset's shape dependence is the one-loop function plus a constant. It shifts the one-loop coefficient A
     and can add no stationary point of its own.
   - Terms where two images coincide are UV-divergent; they go into the mass and coupling counterterms and are
     scheme-dependent. They are not computed.
3. **[E] The figure-eight brings new τ-dependence.**
   - One quartic vertex (the Higgs quartic, gauge quartics) gives (G_reg(0))², with G_reg(0) = Σ′ G(ℓ) ∝ E₂(τ)/A².
     So the term is ∝ E₂².
   - E₂²'s constant term at the cusp is a²y⁴ + 2ab y + b²y⁻² (with E₂ = a y² + b y⁻¹ + …). No combination of the Eₛ
     has a y¹ term, so E₂² is outside their span.
   - Numerically, the best fit of E₂² by {1, E₂, E₃, E₄, E₅} on 40 points of the fundamental domain leaves a relative
     rms residual of 1.3e-4, against an evaluation precision near 1e-14.
4. **[E] The couplings' circularity, priced.**
   - The two-loop coefficients carry the six-dimensional couplings over the area: g²/A, y_f²/A and λ/A. None is on
     record (FL-05: no normalisation of the couplings).
   - Each class is one free number unless derived: at least three (gauge, Yukawa, quartic).
   - Taken from the frame's own outputs at the same τ (its Yukawas), V(τ) depends on τ through them as well. That is a
     fixed-point problem the record has not posed.
5. **[E] The principle for Im τ, sealed in the script before its run.**
   - A two-loop vacuum term selects Im τ only at a stationary point of V₁ + V₂ at which |V₂| ≤ |V₁|/3, so that the next
     order can be neglected.
   - A stationary point with |V₂| > |V₁|/3 is not a selection.
   - A stationary point at i or ω is the symmetry's, since every invariant function is stationary there (P-629's note),
     not the dynamics'.
6. **[E] Its check: no selection.**
   - Near the cusp, V = −α E₃ + β E₂² has leading terms −α c₃ y³ + β c₂² y⁴. These are stationary at
     y* = 3αc₃/(4βc₂²), where |V₂/V₁| = 3/4 exactly at leading order, whatever β/α is. With the full functions, at
     β/α = 1e-2, 1e-3 and 1e-4 the single stationary point lies at y = 103, 1030 and 1.02e4, with |V₂/V₁| = 0.753,
     0.755 and 0.748.
   - Over β/α = ±[1e-4, 10] (60 values), on the lines Re τ = 0 and 1/2, the 12 stationary points with Im τ in
     [1.2, 20] all have |V₂| > |V₁|/3.
7. **[J] The reading.**
   - Beyond one loop the fibre's vacuum energy does carry new τ-dependence, but only through the quartic couplings'
     E₂². The cubic couplings' sunset repeats the one-loop shape.
   - The figure-eight grows faster at the cusp than one loop (y⁴ against y³), so near the cusp its share grows with
     Im τ. Any balance between one loop and two loops that could hold τ off the cusp sits where the two are
     comparable. That is the Dine–Seiberg situation, outside the expansion's control.
   - So two loops do not supply the principle P-373 asks for. A holder of Im τ needs either a non-perturbative term
     or the couplings derived, and a check beyond the leading orders.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| K1 | E₂, E₃ by Fourier against direct lattice sums, to 1e-6 at three τ (99 %) | holds: 2.9e-10 |
| K2 | lattice C₁,₁,₁, extrapolated, equals E₃ + ζ(3) to 2e-3 at i, ω, 0.2 + 1.7i (90 %) | holds: 5.6e-5, −1.5e-5, 6.2e-5 |
| K3 | E₂² outside {1, E₂, E₃, E₄, E₅}: relative residual above 1e-8 (99 %) | holds: 1.3e-4 |
| K4 | β/α = 1e-2, 1e-3, 1e-4: one stationary point with y > 1.2, \|V₂/V₁\| within 0.1 of 3/4 (90 %) | holds: 0.753, 0.755, 0.748 |
| K5 | β/α in ±[1e-4, 10], Re τ = 0 and 1/2: no stationary point in Im τ ∈ [1.2, 20] with \|V₂\| ≤ \|V₁\|/3 (85 %) | holds: 12 found, none |

## 2. What this page does not do

- It treats untwisted fields only. With twists (Wilson lines), G_reg(0) becomes a twisted Eisenstein series, and the
  sunset a twisted C₁,₁,₁, for which this seat knows no identity like Zagier's. The record's V₁ has twisted parts
  (B1704: scalars twisted along the shrinking cycle leave no minimum on the CP lines).
- It does not compute the divergent coincident-image terms, fermion and gauge numerators, or the area modulus.
- K5 scans two lines of the fundamental domain and one coupling ratio at a time, not the full plane.
- It compares nothing with data and reads no target.

0 of 19.
