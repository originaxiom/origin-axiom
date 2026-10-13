# B1638 — THE GOLDEN IDENTITY: Σ_p (θ_p(τ)θ_p(Nτ)/(η(τ)η(Nτ)))² = 8 everywhere, with N = [[−1, −2], [2, −1]] of determinant 5; on the tick's axis that is F = Σ|θ_p/η|⁴ = 8, so the weave's lowest coupling is golden on every discriminant-5 geodesic; no other closed geodesic tested has such an identity

**Verdict: PROVED** (numerically, to 49 digits; I1–I5 all hold; the proof is B1639). cc (main), 2026-10-13. Sealed
`2401dab14` before the run. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /golden identity|Weber|Schl|modular equation|degree 5|discriminant 5/: 8 of 1408 arcs on main match (NEGATIVE 2, PROVED 6)`
(word matches: Schlesinger flows, Fibonacci anyons); B1635, B1636; a probe before the seal found H = 8 at three points
(disclosed). **Literature:** Weber's functions (θ₃/η = 𝔣², θ₄/η = 𝔣₁², θ₂/η = 𝔣₂²); Schläfli-type equations of degree 5.

## 1. The mechanism

Let M = [[a, b], [c, d]] be hyperbolic. On its axis, the circle |τ − (a−d)/2c|² = (tr² − 4)/4c², the conjugate τ̄ is a
Möbius image of τ. Since θ_p and η have real q-coefficients, conj(g_p(τ)) = g_p(N_M τ), with g_p = (θ_p/η)² and
N_M = [[d − a, −2b], [2c, d − a]] (determinant tr² − 4, the discriminant). So on the axis
F = Σ|g_p|² = H_M(τ) := Σ_p g_p(τ)·g_p(N_M τ). If H_M is a constant everywhere, F is that constant on the axis.

## 2. The sealed run (`golden_identity.py`, unchanged)

| cell | prediction | prior | result |
|---|---|---|---|
| **I1** | H_LR = 8 at 40 random τ within 10⁻⁴⁰ | 95% | **HOLDS** — max \|H − 8\| = 3.0·10⁻⁴⁹ |
| **I2** | the other five matchings of p not constant | 90% | **HOLDS** — spreads 1.6, 1.7, 5.4, 10.4, 10.5 |
| **I3** | H_M not constant for L²R, LR², L³R, L²R², LRLR² | 85% | **HOLDS** — spreads 11.2, 9.4, 17.4, 5.8, 7.2 (discriminants 12, 12, 21, 32, 96) |
| **I4** | H = 8 for the discriminant-5 controls RL, L(LR)L⁻¹, R⁻¹(LR)R | 90% | **HOLDS** — within 3.2·10⁻⁴⁹ |
| **I5** | on LR's axis conj(g_p(τ)) = g_p(Nτ) and F = 8 | 95% | **HOLDS** — 1.6·10⁻⁵⁰ and 5.6·10⁻⁴⁹ |

## 3. What it says

- **The golden spectrum is one holomorphic identity of degree 5, evaluated on the axis:**
  Σ_p (θ_p(τ)θ_p(Nτ)/(η(τ)η(Nτ)))² = 8. In Weber's functions it reads
  (𝔣𝔣′)⁴ + (𝔣₁𝔣₁′)⁴ + (𝔣₂𝔣₂′)⁴ = 8, with ′ at Nτ.
- **It is special to discriminant 5.** The analogous sums for five other closed geodesics vary by 6 to 17 units. That is
  why the principle's tick (trace 3, discriminant 5, the discriminant of x² − x − 1) and no other closed geodesic tested
  carries the golden spectrum.
- B1639 derives the identity from Ramanujan's form of the degree-5 modular equation.

## 4. Disclosed

- Not blind on I1 (three points seen before the seal).
- A 49-digit agreement at many points is overwhelming numerical evidence, not by itself a proof; B1639 supplies the proof.

## 5. Files

`verification/golden_identity.py` (sealed, unchanged) with `golden_identity.json` and `golden_identity_run.txt`; the lock
`tests/test_b1638_b1639_the_golden_identity.py`.
