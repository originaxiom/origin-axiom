# CLAIM CARD — P-631: on the fibre, the sunset of three massless propagators joined by cubic vertices repeats the one-loop shape (C₁,₁,₁ = E₃ + ζ(3), checked numerically) while the quartic figure-eight brings E₂², numerically outside the span of 1, E₂ to E₅; with V₁ ∝ −E₃ and V₂ ∝ E₂², for the 60 values of β/α tried, no stationary point of V₁ + V₂ on Re τ = 0 or 1/2 with Im τ in [1.2, 20] meets the bound |V₂| ≤ |V₁|/3 of P-373's principle (the seat's card of 2026-11-25 in the queue's form)

- card id: new
- seat code: fam1-v1-unset-03
- seat, branch, commit: fam1-v1-unset-03, chat1/web-seat, 0a89dddd2fa84dda59eb6c77ebd3b114f78050db
- kind: negative
- touches: P-631, P-373, P-629, P-380
- effect: conditions — P-373's principle for Im τ: in the untwisted massless model, on the lines and range searched,
  no stationary point of V₁ + V₂ meets its bound for any β/α tried; P-631 gains the inventory (the cubic sunset gives
  E₃ + ζ(3), the quartic figure-eight E₂²)
- scope: frame: untwisted massless six-dimensional fields on the fibre, whose one-loop term is B1686's E₃;
  object: the two-loop vacuum terms and the stationary points of V₁ + V₂ = −α E₃ + β E₂²; reach: class;
  hypotheses: β/α in [1e-4, 10] and its negative (60 values) on the lines Re τ = 0 and 1/2 with Im τ in [1.2, 20];
  on the imaginary axis also β/α = 1e-2, 1e-3, 1e-4 out to Im τ = 3α/β; E₂² represents the quartic figure-eight
  (S2 of the sealed docstring); Yukawa and gauge couplings are not computed here
- identifications: none
- definitions: E_s(τ) = Σ′ (Im τ)^s / (π^s |m + nτ|^{2s}), the real-analytic Eisenstein series, over pairs (m, n) ≠ 0;
  C₁,₁,₁(τ) = Σ′ over (p₁, p₂, p₃) with p₁ + p₂ + p₃ = 0 of Π (Im τ/π)/|pᵢ|², the two-loop sunset sum on the torus,
  evaluated with cutoffs 20, 28, 40, 56 and extrapolated; V₁ = −α E₃ and V₂ = β E₂², α > 0; a stationary point is a
  zero of d(V₁ + V₂)/d Im τ on the line; P-373's principle selects Im τ only where |V₂| ≤ |V₁|/3
- imports: the six-dimensional star relation, and the identity C₁,₁,₁ = E₃ + ζ(3) (D'Hoker, Green and Vanhove, 2015;
  Zagier's proof), both standard mathematics; the second is checked numerically here (K2)
- premises on main: B1686 and B1704 (the one-loop term and its run to the cusp), P-380 (the SM seat's census), P-629
  (stationarity at i and ω)
- decisive script: relays/chat1_2026-11-25_p631/card_p631.py, SHA-256 aacfe9c8976ce3a7, depends on the standard library,
  numpy and mpmath, run as python3 relays/chat1_2026-11-25_p631/card_p631.py, output SHA-256 2194c57bdc90cb18
- decisive lines: 10 lines marked "DECISIVE:", SHA-256 d13097fea40b6972
- failing control: python3 relays/chat1_2026-11-25_p631/card_p631.py --control
- second computation: none that shares no code. Within the sealed p631_two_loop.py, E₂ and E₃ are computed by their
  Fourier series and by direct lattice sums (K1), and C₁,₁,₁ by a lattice sum against the closed form (K2). E₂²'s
  lying outside the span is numerical: a relative rms residual of 1.28e-4 on 40 points. The old card's referee reran
  it identically. The decisive script runs the sealed p631_two_loop.py (SHA-256
  aa5c850a33237e43, at 852afb281) unchanged.
- already on main?: topic_sweep.py "two-loop|sunset|figure-eight" at 68b04c69d: 101 of 1760 arcs and 9 register rows
  match the words; the old card's sweep at 88a1e9474 found none that computes a two-loop vacuum term on the fibre; the
  nearest are P-631 itself and the one-loop arcs B1686 and B1704
- what would make it fail: on the lines and range searched, a stationary point of V₁ + V₂ with |V₂| ≤ |V₁|/3; a lattice
  C₁,₁,₁ that differs from E₃ + ζ(3) beyond 2e-3; a combination of 1, E₂, ..., E₅ that reproduces E₂² to 1e-8. The
  control is K5's check changed on purpose: the bound widened to |V₂| ≤ |V₁| and the range to Im τ in [1.2, 300], on
  the imaginary axis at β/α = 1e-2, where the stationary point at Im τ = 102.7 has |V₂/V₁| = 0.75; the changed check
  finds a point inside the bound, and the claim's verdict fails.
