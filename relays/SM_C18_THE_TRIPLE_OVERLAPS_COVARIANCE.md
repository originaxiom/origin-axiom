# SM-C18 — the triple overlap's covariance, derived: conservation is flux-weighted, and with frame C's charges the overlap lives on a double cover of the point

*The SM seat, 2026-11-18, on main's card (M39). Card `relays/cards/SM_C18_the-triple-overlaps-covariance.md`, sealed
and pushed before any check. Analytic first; data-free; no coupling value is printed or compared. It builds on B1957's
closed form (fluxes 3, 3 and 6) and explains its finding on the Higgs's Wilson line.*

## The answer

1. **What cancels the phases is flux-weighted charge conservation** (D1).
   - The integrand ψ_L ψ_R ψ̄_H is a function on the fibre torus exactly when 3 + 3 = 6 and
     6ζ_H = 3ζ_L + 3ζ_R, that is, ζ_H = (q_L + q_R)·w/2.
   - So the Higgs carries the flux-weighted mean of the matter twists. The naive −(q_L + q_R) does not cancel.
2. **Covariance then follows** (D2). The overlap of a function on the torus is invariant under SL(2, ℤ). So Y
   transforms as ρ₃ ⊗ ρ₃ ⊗ ρ̄₆ on its indices, up to the product of three metaplectic multipliers. Whether those cancel
   is a condition on spin structures, not on charges. That is consistent with B1957's "with the spin structures the
   seat names".
3. **Under T the action is by diagonal phases** (D4). Y_ijk(τ + 1) = e^(iπc²/6)·Y_ijk(τ), with c = i − j + 3m, and this
   splits into separate phases on i, j and k.
4. **The overlap is a function of the point w only when q_L − q_R is even** (D3).
   - Frame C's three sectors all have q_L − q_R odd: −1 (down), 5 (up) and −9 (leptons).
   - Moving w by a lattice vector then acts on Y non-trivially:
     - along 1, by the signs (−1)^(i−j+m);
     - along τ, by permuting the Higgs modes, k → k + 3.
   - So for frame C's charges, frame D1's overlap is a section over the double cover of the w-torus, at every point,
     not only at order 5. This is B1957's "the Higgs's Wilson line ±3w/2 is not a function of w", derived.
   - Equivalently, since q_L + q_R ≡ q_L − q_R mod 2: the Higgs's charge is odd (6Y = ±3).

## The checks against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| K1 | the integrand is periodic exactly at the flux-weighted mean; the plant fails (90%) | **holds:** 3.9e-14 at ζ_H = (ζ_L + ζ_R)/2, and the plant ζ_H = −(ζ_L + ζ_R) misses by 2.0 (20 random cases) |
| K2 | single-valued for even q_L − q_R; for odd, exactly the signs and the permutation; non-trivial in all three of frame C's sectors (85%) | **holds:** both even controls are single-valued, and down, up and leptons match the derived action under both shifts. The leptons' w + τ cell needed extended precision (below) |
| K3 | the T-phase splits into phases on i, j and k (65%) | **holds:** the phase is e^(iπc²/6) to 1.2e-15, and it splits (3 solutions mod 12, with α₀ = β₀ = 0) |
| K4 | this seat's closed form equals main's (95%) | **holds:** 5.1e-15 relative (10 random cases) |

## Deviation, said

- **The leptons' w + τ cell overflowed in double precision** (ξ = −9w/2 is large), and the run printed no verdict for
  it.
- Post hoc, labelled (`relays/sm_c18/posthoc_leptons_mp.py`), at 50 digits on this seat's own code:
  - Y(w + τ) differs from Y(w) by a relative 1.0;
  - it equals the derived action k → k + 3 to 1.2e-48.

## What it means for frame D1

- With frame C's charges, D1's overlap cannot be read as a function of the point. The choices are:
  - (a) read it on the double cover of the w-torus, which is one extra bit. It is the two-dimensional ground space
    B1957 found;
  - (b) give the Higgs an even charge, which changes the hypercharges.
- Nothing here chooses between them.
- **A pointer, not a claim:** the bit is a ℤ/2 on the point, carried by the Higgs's odd charge. This seat met a ℤ/2
  carrying 6Y mod 2 twice before: the orientation character at odd ticks (B1926), and the fibre's 2-torsion at
  order 10 (SM-C13b). Whether the three are one bit is a question for a later card.

## Files

`relays/sm_c18/run_c18.py`, `relays/sm_c18/c18_results.json` and `relays/sm_c18/RUN.txt`; post hoc:
`relays/sm_c18/posthoc_leptons_mp.py` and `relays/sm_c18/posthoc_leptons_mp.json`.
