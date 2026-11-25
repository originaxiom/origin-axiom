# CLAIM CARD — P-631: for untwisted massless six-dimensional fields on the fibre, only a scalar cubic sunset repeats the one-loop shape (C₁,₁,₁ = E₃ + ζ(3)); the quartic figure-eight, and per the referee the Yukawa and gauge sunsets, bring E₂², outside the span of the Eisenstein series. Under the principle sealed for Im τ (a two-loop term selects Im τ only where it is at most a third of the one-loop term), the model V = −αE₃ + βE₂² selects no Im τ: near the cusp every balance sits at |V₂/V₁| = 3/4, and none of 12 stationary points on Im τ ∈ [1.2, 20] meets the bound

- seat, branch, commit: chat1, origin/chat1/web-seat. The script is at 852afb281 and its output at 719443701; the relay
  and this card were corrected after their referee read.
- kind: negative, scoped to the untwisted massless model (V₁ ∝ E₃, V₂ ∝ E₂²)
- touches: P-631, P-373, P-629, P-380
- effect: conditions — P-373's principle for Im τ: in the untwisted massless model no stationary point of V₁ + V₂
  other than i and ω meets the sealed bound, for any β/α. Adds to P-631 the inventory (a scalar cubic sunset gives
  E₃ + ζ(3); quartic and derivative-cubic couplings give E₂²), three coupling classes absent from the record (FL-05),
  and a tightened principle for main to seal.
- imports: the six-dimensional star relation, and the identity C₁,₁,₁ = E₃ + ζ(3) (D'Hoker, Green and Vanhove, 2015;
  Zagier's direct proof, unpublished), both standard mathematics, the second reproduced numerically here.
- premises on main: B1686 and B1704 (the one-loop term and its run to the cusp), P-380 (the SM seat's census), P-629
  (stationarity at i and ω)
- decisive script: relays/chat1_2026-11-25_p631/p631_two_loop.py, SHA-256 aa5c850a33237e43; depends on only the
  standard library, numpy and mpmath, and reads no file. Run as `python3 -I p631_two_loop.py` (about 97 s). Output
  p631_two_loop_out.txt, SHA-256 0c9f970bcab17a05.
- second computation: within the script, E₂ and E₃ are computed two ways (Fourier and direct lattice sum, to 2.9e-10),
  and C₁,₁,₁ by a lattice sum against the closed form (within about 1e-4). The referee reran the script identically.
  Its own checks, not committed, are: the star relation to 1e-12; the cusp algebra; refined roots giving 3/4 to 1e-6;
  the Yukawa sunset's reduction to E₂²; and the bound failing at every point of the fundamental domain.
- already on main?: `scripts/checks/topic_sweep.py "two-loop|two loop|2-loop|modular graph|Zagier"` at 88a1e9474
  finds 11 arcs and 3 rows; none computes a two-loop vacuum term on the fibre. The nearest are P-631 itself and the
  one-loop arcs B1686 and B1704.
- what would make it fail:
  - in the model, a stationary point of V₁ + V₂ anywhere in the fundamental domain other than i and ω where
    |V₂| ≤ |V₁|/3;
  - a lattice C₁,₁,₁ that differs from E₃ + ζ(3) beyond its extrapolation spread;
  - a combination of Eisenstein series that reproduces E₂² to its evaluation precision.

## What it means

- [E] A scalar cubic sunset with three distinct images is C₁,₁,₁(τ)/(64π³A³) times the coupling and symmetry factor,
  and C₁,₁,₁ = E₃ + ζ(3).
- [E] The figure-eight is ∝ E₂², outside the span of the Eisenstein series; per the referee, the Yukawa sunset is too.
- [E] Near the cusp, V = −αE₃ + βE₂² is stationary at y* = 3αc₃/(4βc₂²), where |V₂/V₁| = 3/4 for every β/α > 0.
- [J] Within untwisted massless content no choice of couplings helps. A holder of Im τ needs non-perturbative terms,
  twisted or massive contents, or control beyond the loop expansion. The sealed principle has weaknesses (it bounds
  values, not τ-dependent parts, and exempts i and ω by an SL(2, Z) argument), and the relay offers a tightened
  version.

0 of 19.
