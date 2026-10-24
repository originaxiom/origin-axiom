# R is the S₄′ weight-1 triplet (chat1, 2026-10-24; data-free)

A numerical identity found while folding in the literature dive (`LITERATURE_DIVE.md`, its import 1). No target is read;
nothing here is a value result. 0 of 19.

## The identity

With n = (0, 1, i)/√2 and n̄ = (0, 1, −i)/√2 (so n·n = n̄·n̄ = 0, n·n̄ = 1, e₁·e₁ = 1 under the bilinear dot), write main's
record Higgs form (B1691: weight −½, exactly null) as R = a e₁ + b n + c n̄. Then

  **R(τ) = η(τ)⁻³ · ( −ε θ, ε²/√2, −θ²/√2 )   on (e₁, n, n̄),   θ = Θ₃(2τ), ε = Θ₂(2τ),**

that is, R = η⁻³/√2 times Novichkov, Penedo and Petcov's S₄′ weight-1 triplet Y_3̂^{(1)} = (√2 εθ, ε², −θ²)
(arXiv:2006.03058), with the sign of e₁ flipped.

- **Checked** at twelve τ from 0.9i to 0.325 + 3.4i, Re τ from 0 to 0.9 (`exploration/e13_r_vs_s4prime.py` and
  `e13b_r_scalar_factor.py`, each committed before its run, outputs committed before they were read): the three ratios
  a/Y₁′, b/Y₂′, c/Y₃′ agree to 10⁻¹³ or better and their common value times η³ is 1/√2 at every τ. (R from `route_b_scan`'s
  series, θ, ε and η summed to 30 digits with the analytic branch e^{iπτ/2} for ε's q^{1/4}; with mpmath's principal
  branch the four points with Re τ > ½ show the expected extra factor −i, e13.)
- **Weights agree:** R has weight −½, Y_3̂^{(1)} weight 1, η⁻³ weight −3/2.
- **What it is not:** a proof. Both sides are vector-valued modular forms of the same weight and multiplier, so a proof
  would match q-expansions up to a Sturm-type bound; twelve points at 10⁻¹³ make an accident implausible.

## What follows (not computed unless said)

- The frame's Higgs form is an object of level-4 modular flavour symmetry (Γ′₄ ≅ S₄′), the group the literature dive
  identifies as the family group's level; its cusp structure (δ = 2√2 r^½, ε = 4r) is that triplet's Z₄^T counting.
- **DR**, B1700's h₁ (the Serre derivative): since (1/2πi) d ln η = E₂/24, D_{−½}(η⁻³Y) = η⁻³ D₁Y, so DR = η⁻³/√2 ·
  D₁Y_3̂^{(1)}, a holomorphic weight-3 triplet of the same type. In NPP's tables the weight-3 forms are 1̂′ ⊕ 3̂ ⊕ 3̂′, one
  triplet of type 3̂, so DR should be η⁻³ times Y_3̂^{(3)} up to a constant — **to be checked** (data-free, minutes).
- For the plan's B-2 and C-1: a "rule for h" can be stated in NPP's ring of S₄′ forms (Y_3̂^{(1)} = R, Y_3̂^{(3)},
  Y_3̂′^{(3)}, and their products with E₄, E₆), so a candidate rule names a multiplet rather than a direction.
- In the S₄′ models of the literature the Higgs is a flavour singlet and Y_3̂^{(1)} is a coupling; in the frame the same
  triplet is the Higgs direction. That difference is the frame's flavoured Higgs, which the no-go results the dive cites
  (arXiv:1302.0861, 1401.5807) address.

0 of 19.
