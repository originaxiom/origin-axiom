# P-631 (2026-11-25): beyond one loop for τ, for untwisted massless six-dimensional fields on the fibre. Only a scalar cubic sunset repeats the one-loop shape: by the six-dimensional star relation it is C₁,₁,₁ = E₃ + ζ(3), reproduced here within ~1e-4. The quartic figure-eight brings new τ-dependence, E₂², outside the span of the Eisenstein series, and so, per the referee read, do the Yukawa and gauge sunsets, whose derivatives reduce them to the same E₂². The couplings that weight these terms are on no record. A principle for Im τ is sealed: a two-loop term selects Im τ only at a stationary point where it is at most a third of the one-loop term. In the model V = −αE₃ + βE₂² no such point exists: near the cusp every balance sits at |V₂/V₁| = 3/4, none of the 12 stationary points found on Im τ ∈ [1.2, 20] meets the bound, and per the referee no point of the fundamental domain does

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
- The referee read (applied here) found one physics error in the first version: it said the Yukawa and gauge sunsets
  repeat the one-loop shape. Only a dimensionless scalar cubic does. The referee's own checks, cited below as such, are
  not committed. Those checks are: the Yukawa sunset's reduction; the refined stationary points; the domain-wide bound;
  the coincident-image terms; and the extrapolation spread.
- The script's docstring states S1 for "Yukawa or gauge cubic" vertices. That is the error above, and it stays in the
  sealed text.
- The sealed principle has weaknesses the referee found (§ 0 item 6). It is reported as sealed, and a tightened
  version is offered for main to seal.

**Typing.** [E] means established on record or by a run here, or by the referee read where it says so. [J] means this
seat's judgement.

## 0. In short

1. **The one-loop term on record.**
   - [E] Every content on record has a positive total cusp coefficient (5.45 to 66.57 ζ(6)), so V₁ runs to the cusp
     (B1686, B1704).
   - [J] Schematically V₁ is a weight-3 lattice sum per area cubed, partly twisted. The record's sums carry Wilson-line
     twists and the Higgs's parity copies, and keep only the theta group: V₁ is not stationary at ω (B1686), and
     Re τ = 1/2 is not a mirror line once the copies are in (B1704).
   - This page's model takes the untwisted, SL(2, Z)-invariant part: V₁ = −α E₃, with E_s = Σ′ (y/(π|m + nτ|²))^s.
2. **[E] The scalar cubic sunset repeats the one-loop shape.**
   - Three massless six-dimensional propagators G(x) = 1/(4π³|x|⁴), joined by a dimensionless scalar cubic vertex, with
     their three images on the fibre distinct.
   - The six-dimensional star relation (weights 2 + 2 + 2 = D) gives ∫ d⁶x Π |x − xᵢ|⁻⁴ = π³/(|x₁₂|²|x₁₃|²|x₂₃|²). So
     the term is C₁,₁,₁(τ)/(64π³A³) times the coupling and the symmetry factor. The referee checked the star relation
     numerically with Schwinger parameters, to 1e-12.
   - C₁,₁,₁ = E₃ + ζ(3). The identity is D'Hoker, Green and Vanhove's (2015, from the Laplace equation), with a
     direct-summation proof by Zagier (unpublished, as cited by D'Hoker and Kaidi, 2017). The lattice sum here agrees
     within its extrapolation spread, about 1e-4 (5.6e-5, −1.5e-5 and 6.2e-5 at τ = i, ω and 0.2 + 1.7i).
   - Per the referee's evaluation in dimensional regularisation, the terms with two images coinciding are finite and
     ∝ E₃, and the triple coincidence is scaleless. So for a scalar cubic the sunset only shifts α.
3. **[E] The quartic figure-eight, and (per the referee) the Yukawa and gauge sunsets, bring new τ-dependence.**
   - One quartic vertex gives (G_reg(0))², with G_reg(0) = E₂/(4πA²). So the term is ∝ E₂².
   - The power-law part of E₂²'s constant term is a²y⁴ + 2ab y + b²y⁻², with a = π²/45 and b = ζ(3)/π. No E_s with
     s ≠ 0, 1 has a y¹ term (E₀ is constant, and the Kronecker-limit Ê₁ carries −log y, which E₂² lacks). So E₂² lies
     outside the span. Non-zero modes add only O(e^(−4πy)).
   - Numerically, the best fit of E₂² by {1, E₂, E₃, E₄, E₅} on 40 points of the fundamental domain leaves a relative
     rms residual of 1.3e-4. The referee confirmed the floor: a target inside the span fits to 2.5e-15.
   - [E, the referee's check] With Yukawa vertices two lines are fermions, S = γ·∂G. Integration by parts gives
     ∫ G(∇G)² = ½ G(0)², so the Yukawa sunset is ∝ G_reg(0)² ∝ E₂². For the distinct images an identity checked by
     finite differences gives E₂² − E₄ with the same E₂² coefficient. The gauge cubic vertex reduces the same way (not
     computed).
4. **[J] The couplings' circularity, priced.**
   - The two-loop coefficients carry the six-dimensional couplings over the area: g²/A, y_f²/A, λ/A. None is on record
     (FL-05: no normalisation of the couplings). That is three coupling classes, each one free number unless derived.
   - For the τ-dependence of the untwisted model they combine into one ratio, β/α.
   - Taken from the frame's own outputs at the same τ (its Yukawas), V(τ) depends on τ through them too, a fixed-point
     problem the record has not posed.
5. **[E] The principle for Im τ, as sealed in the script before its run.**
   - A two-loop vacuum term selects Im τ only at a stationary point of V₁ + V₂ at which |V₂| ≤ |V₁|/3, so that the next
     order can be neglected.
   - A stationary point with |V₂| > |V₁|/3 is not a selection.
   - A stationary point at i or ω is the symmetry's, since every SL(2, Z)-invariant function is stationary there
     (P-629's note), not the dynamics'.
6. **The principle's weaknesses (the referee read), and a tightened version for main to seal.**
   - The record's V₁ is only theta-group invariant and is not stationary at ω, so the exemption of i and ω is an
     SL(2, Z) argument.
   - A bound on values is not invariant under τ-independent constants, such as the sunset's ζ(3) or a counterterm.
   - It would accept a one-loop stationary point slightly shifted by V₂ (contents of B1704's kind).
   - With a scalar sunset s(E₃ + ζ(3)) counted in V₂ rather than in α, |V₂/V₁| = |3/4 + s/(4α)| near the cusp. That
     meets the bound for s/α in [−13/3, −5/3], by cancellation, and only with a sunset larger than V₁.
   - Tightened, for main: state the bound on the τ-dependent parts or on their derivatives; bound each two-loop piece
     separately; require that V₁ alone not be stationary there; and name the symmetric points of the potential's own
     group.
7. **[E] The check, in the model V = −αE₃ + βE₂².**
   - Near the cusp the leading terms −α c₃ y³ + β c₂² y⁴ (c₃ = 2ζ(6)/π³, c₂ = π²/45) are stationary at
     y* = 3αc₃/(4βc₂²), where |V₂/V₁| = 3/4 at leading order, for every β/α > 0. There is none for β/α < 0.
   - With the full functions, at β/α = 1e-2, 1e-3 and 1e-4, the script's grid puts the single stationary point at
     y = 103, 1030 and 1.02e4, with |V₂/V₁| = 0.753, 0.755 and 0.748 (grid-limited, ±0.005). The referee refined the
     roots: y* = 102.31, 1023.14 and 10231.4, with |V₂/V₁| = 0.750002, 0.7500000 and 0.7500000.
   - Over β/α = ±[1e-4, 10] (60 values), on the lines Re τ = 0 and 1/2: six positive values of β/α put a stationary
     point in Im τ ∈ [1.2, 20], each on both lines (12 points, Im τ from 2.26 to 17.8). All have |V₂| > |V₁|/3.
   - [E, the referee's check] The gradients of E₂ and E₃ are never parallel inside the fundamental domain (checked to
     y = 12). So every stationary point other than i and ω lies on x = 0, x = 1/2 or the unit arc. There
     |V₂/V₁| = (∂E₃/E₃)/(2∂E₂/E₂) depends on the point alone, whatever β/α is: in [0.750, 1.47] on x = 0, in
     [0.750, 1.50] on x = 1/2, in [1.37, 1.50] on the arc, tending to 3/2 at ω. So in this model the bound fails at
     every point, for every β/α.
8. **[J] The reading.**
   - Beyond one loop, for untwisted massless content, the fibre's vacuum energy carries new τ-dependence through E₂²,
     from quartic and derivative cubic couplings alike. Only a scalar cubic repeats the one-loop shape.
   - The analogue of the Dine–Seiberg obstruction holds: a minimum from competing orders sits where the orders are
     comparable. Unlike Dine–Seiberg, the run here is toward the regime where the expansion parameter grows, roughly as
     (λ/A)·y, so the one-loop run to the cusp itself leaves control.
   - Within untwisted massless content no choice of couplings helps, since the ratio at a stationary point does not
     depend on β/α. A holder of Im τ needs non-perturbative terms, twisted or massive contents, or control beyond the
     loop expansion.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| K1 | E₂, E₃ by Fourier against direct lattice sums, to 1e-6 at three τ (99 %) | holds: 2.9e-10 |
| K2 | lattice C₁,₁,₁, extrapolated, equals E₃ + ζ(3) to 2e-3 at i, ω, 0.2 + 1.7i (90 %) | holds: 5.6e-5, −1.5e-5, 6.2e-5 (extrapolation spread about 1e-4) |
| K3 | E₂² outside {1, E₂, E₃, E₄, E₅}: relative residual above 1e-8 (99 %) | holds: 1.3e-4 |
| K4 | β/α = 1e-2, 1e-3, 1e-4: one stationary point with y > 1.2, \|V₂/V₁\| within 0.1 of 3/4 (90 %) | holds: 0.753, 0.755, 0.748 on the grid; 0.750002, 0.7500000, 0.7500000 refined (the referee) |
| K5 | β/α in ±[1e-4, 10], Re τ = 0 and 1/2: no stationary point in Im τ ∈ [1.2, 20] with \|V₂\| ≤ \|V₁\|/3 (85 %) | holds: 12 found (6 values of β/α, each on both lines), none |

- The run takes about 97 s.

## 2. What this page does not do

- It treats untwisted fields only. With twists (Wilson lines), G_reg(0) becomes a twisted Eisenstein series and the
  sunset a twisted C₁,₁,₁, for which this seat knows no identity like Zagier's. The record's V₁ has twisted parts.
- It does not compute the gauge cubic sunset, the graviton's two-loop terms or massive fields. Per the referee, the
  graviton brings weight-5 structures such as E₂E₃, whose cusp ratio would be 3/5, still above 1/3.
- It does not treat the area modulus.
- It compares nothing with data and reads no target.

0 of 19.
