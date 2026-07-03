# B382 (D3(b)) — leg 1 BANKED: the phase-ratio law verified on its exact classical domain

**Status: leg 1 banked (frontier); legs 2–3 (the (γ−I)⁻¹ matching with the ordering correction,
then the slot-constant closed form) pending. Pre-registration: PREREGISTRATION.md (PR #477,
first). Firewalled.**

## The intertwining (exact)

`D·X·D⁻¹ = X·Z` and `D·Z·D⁻¹ = Z` — phase-free, the clean shear on the Heisenberg frame.
The WR-side conjugation carries phases (handled empirically per word by the γ-extraction).

## The phase-ratio law (the formula's core; verified on all 225 shifts per word)

For a word U with group element γ (extracted empirically from the Heisenberg conjugation):

    tr(U · XᵃZᵇ) = tr(U) · ζ₁₅^{Q(a,b)},   Q quadratic,

verified EXACTLY (every shift, exact field division) on all sampled words with `det(γ−I)`
invertible mod 15 — words (1,0), (0,1), (1,1), (2,1), (2,3). The two sampled words where the
ratio is NOT a pure phase — (1,3) and (3,1) — have `det(γ−I) ≡ 5 (mod 15)` exactly: **the
failures are the classical domain boundary of the trace formula, confirmed by the data.**

## The universal linear part

Across every passing word the linear part of Q is the SAME: `+7a + 8b (mod 15)` — the shift
operator's own fingerprint, independent of γ; only the quadratic coefficients carry the word.
(Q-tables banked in `trace_formula.json`.)

## Next legs (named)

Leg 2: derive the X^aZ^b ↔ Weyl-ordering correction and match the empirical Q's quadratic part
to the classical `½·v·(γ−I)⁻¹·v` form — pinning every convention. Leg 3: assemble the slot
constant `Π_H tr(Par·H₁H₂)` from the closed form and identify the origin of the 1/12 among the
three registered readings. KILLS unchanged from the pre-registration.

**Provenance.** PREREGISTRATION.md; P56/P57/P60/P62 (the machinery). Reproducer:
`trace_formula.py` (~3 min); locks: `tests/test_b382_trace_formula.py`.
