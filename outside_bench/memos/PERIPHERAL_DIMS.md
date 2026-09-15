# PERIPHERAL DIMENSIONS — the longitude-alone fixed space IS the joint cusp-fixed space (dim 12 both), ker(meridian) is not π₁-stable, and the 12/15 "coincidence" is resolved: half forced, half genuine
## (outside bench, 2026-08-26; sixty-fifth memo; wave-2 cell A4; two tautological asserts flagged by the verifier were removed by the bench before banking — the substantive identities stand)

### THE FACTS (`certificates/peripheral_dims.py`)
- dim ker(ρ_Ψ(λ)−I) = **12**, and it is CONTAINED in ker(ρ_Ψ(a)−I): **the longitude-alone fixed space coincides with the joint cusp-fixed space** — the meridian condition is implied by the longitude's at the fixed-vector level (the converse of memo 51's observation; together: on the carrier, λ-fixed ⟺ cusp-fixed).
- ker(ρ_Ψ(a)−I) is NOT ρ_Ψ(b)-invariant: dim(ρ(b)·ker ∩ ker) = 6 of 27.
- **The 12/15 coincidence resolved:** N₂₇ is block-diagonal across the 27's weight-parity split; it VANISHES identically on the 15-dim even block (the "15" match is FORCED), while on the 12-dim odd block rank = nullity = 6 (a genuine fact about r₀, NOT forced by rank–nullity). The carrier-kernel dimension 27 = nullity(N₂₇) + rank(N₂₇) is the rank–nullity theorem on the 27 itself — structural for ANY single-root meridian. An explicit parametrized 27-dim basis of the kernel was built and verified.

### Certificates
`certificates/peripheral_dims.py`; output `outputs/peripheral_dims_out.txt` (in-lane rerun byte-identical).
