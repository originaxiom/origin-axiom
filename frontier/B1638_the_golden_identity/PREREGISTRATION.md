# B1638 — PREREGISTRATION: THE GOLDEN IDENTITY — why the lowest coupling is golden exactly on the discriminant-5 geodesics

cc (main), 2026-10-13. **Sealed before `golden_identity.py` runs.** No data. 0 of 19.

**Why it matters.** B1636 found that the weave's lowest symmetric coupling has the masses 1 : φ⁻¹ : φ⁻² exactly where
F = Σ_p |θ_p/η|⁴ = 8. That holds at every point computed on the axis of the principle's tick, and numerically on every
geodesic of discriminant 5. It was proved only at i. A proof turns "numerical along the axis" into a theorem, and it
says why discriminant 5 (the discriminant of x² − x − 1) and no other closed geodesic.

**The mechanism, by hand.** Take a hyperbolic M = [[a, b], [c, d]].
- On its axis, the circle |τ − (a−d)/2c|² = (tr² − 4)/4c², one has τ̄ = c₀ + r²/(τ − c₀). The theta constants and η have
  real q-coefficients, so conj(g_p(τ)) = g_p(N_M τ), where g_p = (θ_p/η)² and N_M = [[d − a, −2b], [2c, d − a]]
  (determinant tr² − 4).
- So on the axis F = H_M(τ) := Σ_p g_p(τ)·g_p(N_M τ).
- If H_M is the constant 8 as a holomorphic function, F = 8 on the whole axis, and on all its SL(2, ℤ)-images, since F
  is invariant.

## Seen first

`VERDICT topic-sweep /golden identity|Weber|Schl|modular equation|degree 5|discriminant 5/: 8 of 1408 arcs on main match (NEGATIVE 2, PROVED 6)` — B1635 (the golden spectrum at i), B1636 (the axis, the controls, the discriminant-5 conjecture).
A probe before this seal evaluated H_LR at three random points off the axis and found 8 to 30 digits, with the other
matchings of p not constant (disclosed). **Literature:** Weber, *Lehrbuch der Algebra* III (1908): the functions
𝔣, 𝔣₁, 𝔣₂, with 𝔣⁸ = 𝔣₁⁸ + 𝔣₂⁸ and 𝔣𝔣₁𝔣₂ = √2, and θ₃/η = 𝔣², θ₄/η = 𝔣₁², θ₂/η = 𝔣₂². Schläfli-type modular equations
of degree 5 (Weber; Hart, Ramanujan J. 2008). A brief search found no statement of this identity.

## Disclosed

- **Not blind on I1.** The identity was seen at three points before the seal. I1 tests it at 40 points at 50 digits.
- **What this arc cannot do.** A numerical identity at many points to 50 digits is overwhelming evidence, not a proof. A
  proof needs either the q-expansions at every cusp of the identity's group (a mechanical computation), or a derivation
  from Weber's degree-5 equations. Both are named as the next step. The arc does not claim either.
- The axis-to-F step (conj(g_p(τ)) = g_p(N τ)) is elementary and is checked numerically in I5.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **I1** | H_LR(τ) = 8 at all 40 random τ, within 10⁻⁴⁰ | 95% |
| **I2** | the five other matchings of the three theta constants are not constant (spread > 10⁻³) | 90% |
| **I3** | H_M is not constant (spread > 10⁻³) for L²R, LR² (trace 4), L³R (trace 5), L²R² (trace 6) and LRLR² | 85% |
| **I4** | H_M = 8 within 10⁻⁴⁰ for the discriminant-5 controls RL, L(LR)L⁻¹ and R⁻¹(LR)R | 90% |
| **I5** | on LR's axis, conj(g_p(τ)) = g_p(N τ) and F = 8, within 10⁻⁴⁰ | 95% |

**The reading, written before the run (the cells can only lower it).**
- **If I1, I4 and I5 hold,** the golden spectrum on every discriminant-5 geodesic follows from one holomorphic identity:
  Σ_p (θ_p(τ)θ_p(Nτ)/(η(τ)η(Nτ)))² = 8, with N of determinant 5. This is a modular identity of degree 5, of Schläfli
  type.
- **If I3 holds,** the identity is special to discriminant 5. That is why the principle's own tick, and no other closed
  geodesic, carries the golden spectrum: the masses' φ and the tick's φ meet in one degree-5 relation.
- **A proof of the identity** (cusp expansions, or Weber's equations) is the next arc.

## Instruments

`verification/golden_identity.py`; hashes in `ARTIFACT_HASHES.txt`.
