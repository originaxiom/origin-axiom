# R in the literature's S₄′ basis (chat1, 2026-10-24; data-free)

A dictionary entry, checked while folding in the literature dive (`LITERATURE_DIVE.md`, its import 1). **The content is
main's B1746** (this morning: "v = (−θ₂², −θ₄², iθ₃²) = 2η³R", R the family group Γ₄'s weight-4 twisted form, ∂R its
weight-6 one), which chat1 read only after the check below; what this note adds is the translation into the basis the
modular-flavour literature uses. No target is read; nothing here is a value result. 0 of 19.

## The identity

With n = (0, 1, i)/√2 and n̄ = (0, 1, −i)/√2 (n·n = n̄·n̄ = 0, n·n̄ = 1, e₁·e₁ = 1 under the bilinear dot), write main's
record Higgs form (B1691: weight −½, exactly null) as R = a e₁ + b n + c n̄. Then

  **R(τ) = η(τ)⁻³ · ( −ε θ, ε²/√2, −θ²/√2 )   on (e₁, n, n̄),   θ = Θ₃(2τ), ε = Θ₂(2τ),**

that is, R = η⁻³/√2 times Novichkov, Penedo and Petcov's S₄′ weight-1 triplet Y_3̂^{(1)} = (√2 εθ, ε², −θ²)
(arXiv:2006.03058), with the sign of e₁ flipped.

- **It is B1746's formula:** the duplication identities θ₂(τ)² = 2Θ₂(2τ)Θ₃(2τ), θ₃(τ)² = Θ₃(2τ)² + Θ₂(2τ)² and
  θ₄(τ)² = Θ₃(2τ)² − Θ₂(2τ)² turn v = (−θ₂², −θ₄², iθ₃²) into (a, b, c) = (−2εθ, √2 ε², −√2 θ²) = √2 (−√2 εθ, ε², −θ²),
  and v = 2η³R gives the line above.
- **Checked numerically before B1746 was read** (`exploration/e13_r_vs_s4prime.py`, `e13b_r_scalar_factor.py`, each
  committed before its run, outputs committed before they were read): at twelve τ from 0.9i to 0.325 + 3.4i the three
  ratios agree to 10⁻¹³ or better and their common value times η³ is 1/√2 at every τ (R from `route_b_scan`'s series; θ, ε
  and η summed to 30 digits with the analytic branch e^{iπτ/2} for ε's q^{1/4}; with mpmath's principal branch the four
  points with Re τ > ½ show the expected extra factor −i, e13).
- **Weights:** R has weight −½, Y_3̂^{(1)} weight 1, η⁻³ weight −3/2.

## What the dictionary is for

- The S₄′ literature (NPP 2006.03058 and its successors; de Medeiros Varzielas, Levy, Penedo and Petcov 2307.14410 near
  ω; Abe, Higaki, Kawamura and Kobayashi 2301.07439 at large Im τ) tabulates its forms in this basis: Y_3̂^{(1)}, the
  weight-3 triplets Y_3̂^{(3)} and Y_3̂′^{(3)}, and so on. With the dictionary the frame's Higgs candidates can be read
  against those tables directly.
- **DR:** since (1/2πi) d ln η = E₂/24, D_{−½}(η⁻³Y) = η⁻³ D₁Y, so DR = η⁻³/√2 · D₁Y_3̂^{(1)}, a holomorphic weight-3
  triplet of type 3̂; NPP's weight-3 forms are 1̂′ ⊕ 3̂ ⊕ 3̂′, so DR should be η⁻³ times their Y_3̂^{(3)} up to a constant
  (B1746 has ∂R as the weight-6 twisted form in main's normalisation). Not checked here.
- In the S₄′ models of the literature the Higgs is a flavour singlet and Y_3̂^{(1)} a coupling; in the frame the same
  triplet is the Higgs direction. That is the frame's flavoured Higgs, which the no-go results the dive cites
  (arXiv:1302.0861, 1401.5807) address, and B1746, S213 and P-357 (main) have already found that no single form of the
  family group, nor a pencil of two, reaches the nine.

0 of 19.
