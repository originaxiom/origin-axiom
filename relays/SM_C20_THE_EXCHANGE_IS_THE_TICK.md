# SM-C20 — the tick itself flips frame D1's Higgs bit: on the six Higgs modes it is an antiunitary square root of the golden act

*The SM seat, 2026-11-18. Card `relays/cards/SM_C20_is-the-exchange-the-tick.md`, sealed and pushed at 174a1ec6a before
the run. Data-free; main's B1957 instrument imported unchanged. No coupling or mass value.*


> **Corrected, 2026-11-18, after main's M41 (the physical lane's finding, computed on main).**
> - **The card's coordinate rule (line 11) is wrong.** The reflection z → z̄ with τ → −τ̄ sends ψ_k to the conjugate of
>   ψ_(−k): conjugation with the parity, not plain conjugation. Plain conjugation belongs to z → −z̄.
> - **The result survives.** T₆S₆K and P·T₆S₆K both square to U_M and agree on the ground pair, which is even under
>   P. They differ on the odd plane, so this card's two tests could not tell them apart.
> - **"One bit" and "the Higgs vacuum bit is the tick's orientation" say too much (M41).**
>   - The ground space is a plane.
>   - The tick exchanges the two eigenlines and fixes neither, and nothing computed restricts the Higgs to them.
>   - What holds: the tick acts on the ground plane as an antiunitary square root of the golden act's transport, and
>     exchanges the eigenlines.

## The answer

- **The tick σ = [[1, 1], [1, 0]] acts on frame D1's six Higgs modes as Σ = T₆S₆·K,** with K complex conjugation,
  because σ = T·S·R₀ and R₀ (τ → −τ̄) is K on these modes.
- **Σ² = U_M,** the transport along the golden act M = σ², to 2.4e-15. The phase is exactly 1, so no central factor
  appears.
- **Σ exchanges the two Higgs ground modes,** the ±π/6 pair of B1957, with overlap 1.000 both ways.
- **So frame D1's one undetermined Higgs bit is the tick's own orientation:** one bit, carried by one move of the
  genesis.
  - A history with an odd number of ticks flips it. One with an even number keeps it.
  - This ties the Higgs vacuum to the even-tick condition (the author's ruling of 2026-11-11; B1926), and to the hand's
    invariant (SM-C9, B1929).
- **Not decided here:** which sign is realised.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| C0 | the antiunitary rule, conj(T₆) = T₆⁻¹ and conj(S₆) = S₆⁻¹ (95%) | **holds:** 1.2e-16 and 9.4e-16 |
| E1 | Σ² = U_M up to a phase (75%) | **holds:** 2.4e-15, with the phase 1.000. It also equals T₆S₆T₆⁻¹S₆⁻¹ (1.5e-15), as derived |
| E2 | Σ exchanges v₊ and v₋ (90%) | **holds:** \|⟨v₋, Σv₊⟩\| = \|⟨v₊, Σv₋⟩\| = 1.000 |

E3, the factorisation σ = T·J with J = S·R₀, is the same product T₆S₆·K. The check is trivial and is reported as such
(difference 0.0).

## How the chain now reads (SM-C18 to SM-C20)

1. **SM-C18:** frame D1's triple overlap is covariant by flux-weighted conservation. With frame C's charges it is a
   section over the double cover of the point.
2. **B1957:** averaged over that cover, the Higgs selection leaves one bit, the ±π/6 transport pair.
3. **SM-C19:** that bit is exchanged only by an antiunitary built from the record's operators: the hand.
4. **SM-C20:** the antiunitary is the tick itself, an exact square root of the golden act's transport on the modes.

So the Higgs's vacuum bit in frame D1 is not a free input. It is the same bit as the tick's orientation, which the
record already carries. The choice of sign is the record's single orientation choice, not a new one.

## Not claimed

- Any coupling, mass or mixing value.
- That frame D1 is the right frame.
- Which sign is realised.

The identification holds for the six-mode Higgs sector of B1957's construction, as main built it.

## Files

`relays/sm_c20/run_c20.py`, `relays/sm_c20/c20_results.json`, `relays/sm_c20/RUN.txt`.
