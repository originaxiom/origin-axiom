# SM-C18 — the triple overlap's covariance, derived: where charge conservation cancels the phases, and where it cannot

*Card of the SM seat, 2026-11-18, set by main in M39. Committed and pushed before any check is run. Analytic first;
data-free; **no coupling value** is printed or compared. Read before this card: B1947, B1946, B1953, and B1957's closed
form of the closed-fibre triple overlap (`checks/cim_closed.py`, fluxes 3, 3, 6), with its finding that the Higgs's
Wilson line ±3w/2 is not a function of the point w.*

## 0. What is new here

- B1957 has the closed form and checks its covariance numerically.
- This card derives *why* it is covariant, and states the exact condition under which the overlap is a function of
  the point w. It then checks each derived statement on this seat's own code.

## 1. The derivation, written before any check

**D1. The conservation that cancels the phases is flux-weighted.**
- A zero mode of flux N with Wilson line ζ is a section ψ(z + ζ) of the degree-N line bundle on the fibre torus.
- The product ψ_L ψ_R ψ̄_H is a function on the torus (a section of the trivial bundle) exactly when the degrees add
  (3 + 3 = 6) and N_H ζ_H = N_L ζ_L + N_R ζ_R. With charges on the line, ζ = q·w, this gives
  ζ_H = (q_L + q_R)·w/2.
- So the Higgs's twist is the flux-weighted mean of the matter twists, (q_L + q_R)/2 in units of w. It is not
  −(q_L + q_R), as a naive "q_H = −(q_L + q_R)" would suggest. The sign is the conjugate in ψ̄_H, and the 1/2 is the
  flux ratio.

**D2. Covariance follows from D1, up to three multipliers.**
- Under γ ∈ SL(2, ℤ) the torus, its measure and a function on it are carried along, so the overlap integral is
  invariant.
- Each family of zero modes of flux N transforms by the Weil representation ρ_N of ℤ/N, times a metaplectic
  multiplier and a shift of characteristic (the spin structure). Hence

  Y_ijk(γτ, γw) = μ(γ) Σ ρ₃(γ)_ii′ ρ₃(γ)_jj′ conj(ρ₆(γ))_kk′ Y_i′j′k′(τ, w),

  with μ the product of the three multipliers.
- **Charge conservation (D1) cancels the phases that depend on the point w; it does not cancel μ.** μ is trivial only
  for the spin structures that make the multipliers of the two flux-3 families match that of the flux-6 family. That
  is a condition on characteristics, not on charges.

**D3. The condition for the overlap to be a function of w: q_L − q_R even.**
- The closed form depends on the lines only through ξ = (ζ_L − ζ_R)/2 = (q_L − q_R)·w/2.
- Moving w by a lattice vector moves ξ by (q_L − q_R)/2 lattice vectors.
  - If q_L − q_R is even, Y returns to itself, up to the standard factor of a section.
  - If it is odd, ξ moves by half a lattice vector:
    - along 1, θ[c/6](6ξ + 3, 6τ) = e^(iπc)·θ[c/6](6ξ, 6τ), with c = i − j + 3m, so the entries change by the signs
      (−1)^(i−j+m);
    - along τ, the characteristic moves by 1/2, which is m → m + 1, so the Higgs modes are permuted, k → k + 3.
- Frame C's charges give q_L − q_R = −1 (down), 5 (up) and −9 (leptons). **All three are odd.** So in every sector
  the overlap is a section over the double cover of the w-torus, not a function of w. This is B1957's finding,
  derived, and it holds for every point, not only at order 5.
- Since q_L + q_R ≡ q_L − q_R mod 2, the same condition reads: the Higgs's charge q_L + q_R is even. Frame C's Higgs
  has 6Y = ±3, which is odd.

**D4. Under T alone,** θ[a](z, 6τ + 6) = e^(6πia²)·θ[a](z, 6τ), so Y_ijk(τ + 1) = e^(iπc²/6)·Y_ijk(τ). Whether this phase
splits into separate phases for i, j and k (a covariance by diagonal phases alone) is decided by solving
c²/12 ≡ α_i + β_j + γ_k mod 1, with k = i + j + 1 + 3m.

## 2. What is checked (this seat's own code)

- **K1 (D1):** at random τ and w, the integrand ψ_L ψ_R ψ̄_H is periodic on the fibre lattice exactly when
  ζ_H = (ζ_L + ζ_R)/2. Plant: ζ_H = −(ζ_L + ζ_R) must fail.
- **K2 (D3):**
  - with q_L − q_R even, Y(w + 1) and Y(w + τ) equal Y(w) up to the section factor;
  - with it odd, they differ by exactly the signs (−1)^(i−j+m) and the permutation k → k + 3;
  - for frame C's three sectors, the difference is non-trivial.
- **K3 (D4):** whether the T-phase splits into phases on i, j and k, solved exactly mod 12.
- **K4 (D2):** this seat's closed form against main's (`cim_closed.py`), to 1e-10. This is an implementation check
  only; neither form is a coupling value used anywhere.

## 3. Expectations, written before any check

| | expectation | prior |
|---|---|---|
| K1 | periodic exactly at the flux-weighted mean; the plant fails | 90% |
| K2 | single-valued for even q_L − q_R; for odd, exactly the signs and the permutation; non-trivial in all three of frame C's sectors | 85% |
| K3 | the T-phase splits into phases on i, j and k (the metaplectic part is diagonal) | 65% |
| K4 | the two closed forms agree | 95% |

## 4. What it means

- **If K2 holds:** frame D1 cannot be a function of the point for frame C's charges. Either the Higgs's charge is
  doubled, so that it is even, or the read-out lives on the double cover of the w-torus. That cover is one bit, and it
  is the same bit B1957 found as the two-dimensional ground space.
- Whether that bit is the record's parity again (B1926, SM-C13b) is a question for after, not a claim here.

## 5. Files

relays/sm_c18/, with its script, output and run. The page will be relays/SM_C18_THE_TRIPLE_OVERLAPS_COVARIANCE.md.
