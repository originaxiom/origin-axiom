# W100 — the rule, recorded before the code (a blind replication of B1667's end radius L at a generic τ)

The SM-derivation seat, 2026-10-16. Committed before the script that reads it exists. Nothing here is a result.

## Why this arc

- **Main's ask (S139, `CC_TO_ALL_SEATS_2026-10-16_THE_CANONICAL_CUSP.md`).** "A blind replication of L at one generic τ
  (any method) would be welcome." B1667 found that the fibre's own hyperbolic metric fixes the end radius L at order
  one, so the end supplies no hierarchy.
- **The owner's word (2026-10-16).** The owner approved this seat's recommendation to do it.
- **Also ruled by the owner the same day:** chat1's waiver of this seat's blind check of its S-shape replication is
  accepted. That check is not run.

## Weave or thread?

- **Neither: a property of the shared fibre at a supplied τ.** The punctured torus is the fibre that every thread
  carries. Its canonical cusp is a function of the modulus τ alone. The claim is about two stated values of τ and is
  checked against main's B1667. It is a replication, not a census of threads.

## The quantity (B1667's, as this seat reads its handoff)

- The fibre E_τ = ℂ/(ℤ + τℤ) with its puncture, in its complete hyperbolic metric.
- The puncture is a cusp. Its canonical horocycles are:
  - the boundary of the maximal embedded horoball;
  - the horocycle of length 2.
- Each gives a disc about the puncture in the flat coordinate of ℂ/(ℤ + τℤ). L = log(1/ε), with ε the disc's conformal
  radius, so L_max and L_2.

## The route (independent of B1667's)

B1667 works on the torus side: a Lamé-type equation and its accessory parameter, fixed by real monodromy. This seat
works on the Fuchsian side.
1. **The group.** Take Fricke traces x = tr A and y = tr B, both above 2. Then z = tr AB is a root of
   x² + y² + z² = xyz, so the commutator has trace −2.
   - The larger root covers the half of the modulus space with Re τ > 0, and the smaller root the other half. The root
     is chosen by the sign of Re τ.
   - A = diag(λ, 1/λ), and B is fixed by its trace and tr AB.
   - Both are conjugated so that the commutator fixes ∞ as w ↦ w + h.
2. **The cusp form.** The weight-two cusp form f of ⟨A, B⟩, normalised as f = Σ_{n≥1} a_n e^{2πinw/h} with a₁ = 1, is
   found by Hejhal's method:
   - sample points on a horocycle below the fundamental domain are pulled back by the group, using the words of length
     at most 5. The path is chosen in double precision and applied in mpmath;
   - the automorphy f(w) = (cw + d)⁻² f(γw) is imposed at each;
   - the system is solved by least squares.
3. **The periods.** ω_g = F(gw) − F(w), with F = Σ a_n h/(2πin) e^{2πinw/h}, evaluated at the top of g's isometric
   circle. τ_calc = ω_A/ω_B, and the lattice is ω_B(ℤ + τℤ).
4. **The target.** Newton on (x, y) makes τ_calc equal the target τ.
   - It is continued in ten steps from the hexagonal traces (3, 3), whose τ is e^{iπ/3} or e^{2πi/3} by the root, at
     N = 30.
   - It is then polished separately at N = 45 and N = 60, to 10⁻²⁴.
5. **L.** The horocycle at height Y bounds a disc of conformal radius ε = (h|a₁|/(2π|ω_B|)) e^{−2πY/h} in the flat
   coordinate. So L(Y) = 2πY/h − log(h|a₁|/(2π|ω_B|)), with:
   - Y_max = 1/min|c| over the group's elements not fixing ∞ (the maximal embedded horoball);
   - Y₂ = h/2 (the horocycle of length 2).
6. **Precision.** mpmath at 30 digits. Two truncations (N = 45 and N = 60 coefficients), each with 2N sample points.

## The targets (chosen off any round grid, before any value there was computed)

- τ₁ = 0.137 + 1.291i, in the bulk of the fundamental domain.
- τ₂ = −0.284 + 2.173i, higher toward the cusp of moduli.

## Exploration before this rule (disclosed)

The instrument was built in scratch and run at control points and at one non-target point. **No value at τ₁ or τ₂ was
computed.**
- **At ω = e^{iπ/3}** (traces 3, 3): τ_calc = e^{iπ/3}. L_max = 0.69208004049 and L_2 = 2.78647514288 equal B1667's η⁴
  closed form, which this seat had read in B1667's preregistration. This fixes the convention for L.
- **At i** (traces 2√2, 2√2): τ_calc = i, L_max = 0.688386 and L_2 = 2.719258. B1667's values at i have not been read.
- **At t = 0.31 + 1.07i** (non-target): the Newton solve converges, with L_max = 0.682265 and L_2 = 2.684577. The
  covariance machinery was developed there:
  - L(t + 1) − L(t) is about 4 × 10⁻¹¹, before the polish was added;
  - L(−1/t) − L(t) − log|t| is about 10⁻¹⁶, after the root choice was added. The first attempt, without it, failed to
    reach −1/t, which is how the half-space structure was found.
- **The smaller root at (3, 3)** gives τ = e^{2πi/3}.
- **Seen before this rule:** B1667's reported ranges over its grid (L_max 0.643–0.691, L_2 2.29–2.78 up to Im τ = 4) and
  its fall of the lift toward the cusp. Its per-point values have not been read.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **R0, the gate** | at ω, L_max and L_2 equal B1667's closed form to 10⁻⁹ (seen in exploration: a gate, not a test) | — |
| **R1, convergence** | at τ₁ and τ₂, L_max and L_2 agree between N = 45 and N = 60 to 10⁻⁹ | 90% |
| **R2, the target** | at τ₁ and τ₂, ∣τ_calc − τ∣ < 10⁻²⁰ after Newton | 95% |
| **R3, covariance** | at τ₁, each by its own Newton solve: L(τ₁ + 1) = L(τ₁), and L(−1/τ₁) = L(τ₁) + log∣τ₁∣, to 10⁻⁹, for both L_max and L_2 | 85% |
| **R4, embedding** | at τ₁ and τ₂, Y₂ = h/2 ≥ Y_max: the length-2 horocycle is embedded | 95% |
| **R5, order one** | L_max(τ₁) ∈ [0.6, 0.7] and L_2(τ₁) ∈ [2.2, 2.9]; the same at τ₂ (informed by B1667's ranges, seen) | 80% (τ₁), 75% (τ₂) |

**Main's cell, which this seat cannot score.** Main's instrument, evaluated at τ₁ and τ₂ after this seat's numbers are
posted, agrees to 10⁻⁶. That is the replication.

**The read-outs (no prior).**
- The Fricke traces (x, y, z) at each target.
- h, min∣c∣, Y_max and the first coefficients a₂, a₃.
- The Hejhal residuals.

## What the outcomes would mean

- **R0–R4 as predicted and main's cell met:** B1667's L is replicated by a second route, on the group side rather than
  the torus side. The end radius is fixed by the fibre's geometry.
- **Main's cell failing:** the two routes disagree at a generic τ. The convention (fixed at ω) or one instrument is
  wrong. That is diagnosed post hoc and labelled.
- **R3 failing:** this seat's normalisation of the flat coordinate is wrong away from ω. It is diagnosed post hoc, and
  the cell stays failed as worded.

## After the run

- Commit the output unread.
- Then record the NOTE (a section, a header bullet, a table row and a files entry), the state page, a relay section with
  the owner's two rulings, the ledger, CHANGELOG and PROGRESS_LOG, and a test.

0 of 19.
