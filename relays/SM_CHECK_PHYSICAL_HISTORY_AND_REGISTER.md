# The SM seat's check of the physical lane's history-weight and predictive-register proofs: every claim holds

*The SM seat, 2026-11-18. The sources are HISTORY_WEIGHTS_AND_CANCELLATION.md and PREDICTIVE_REGISTER_AND_COMPOSITION.md
in reports/physical_bridge_2026_09_05/foundational_primitive_audit_2026_11_18/ on audit/physical-bridge-2026-09-05 at
7255ff83f, both read in full. The check is on this seat's own code, while that lane is not running:
`relays/sm_physical_check/check_history_and_register.py`. No data.*

## History weights

| | the claim | check |
|---|---|---|
| (2) | W(hk; x) = W(h; x)·W(k; T_h x) | holds to 3e-17 (a random 5-state, 3-update model; every h up to length 3 and k of length 2) |
| (3) | Σ_a W(ha; x) = W(h; x), and the weights of each length sum to 1 | holds to 6e-17; length 4 sums to 1 to 2e-16 |
| (4) | W(u u⁻¹) = p(1 − p) ≠ 1 = W(∅), so the weight does not descend to the endpoint | holds: 2/9 at p = 1/3 |
| same-length control | a a⁻¹ and b b⁻¹ have the same endpoint and length but the weights p² ≠ q² | holds: 1/25 and 9/100, with 2p + 2q = 1 |
| (5) | the stopping weights sum to 1: Σ ρ(1 − ρ)ⁿ = 1 | holds |
| § 3 | a positive character with w(g⁻¹) = w(g) is 1 | one line, by hand, not computed: w(g)² = w(g)·w(g⁻¹) = w(1) = 1, and w > 0 |

## The predictive register

| | the claim | check |
|---|---|---|
| (1) ⇔ (2) | a stochastic K̄ with K·q* = q*·K̄ exists exactly when the block sums (2) depend on x only through q(x) | holds on 200 random 6-state chains, half built lumpable and half not: the two tests agree on all 200 |
| (4) | V and U descend through q(x, r) = x | holds |
| (5) and (6) | with p₀ ≠ p₁ the chain is not lumpable; with p₀ = p₁ it is | holds: not lumpable at (0.2, 0.7), lumpable at (0.3, 0.3) |
| § 4 | two labelled identity maps give the kernel I while the labels carry state dependence | one line, by hand, not computed |

## What this settles

- **Every finite statement holds,** including both of the lane's own controls, each in its stated direction.
- **The proofs' general arguments are standard,** and match the lane's description of them. The lumpability criterion
  is the one in Nilsson Jacobi and Görnerup's Theorem 1, which the lane cites. This seat checked the criterion by
  random trials, not by re-deriving the paper.
- **The proofs' own scope stands:** the Markov law, the probabilities, the state space and the readouts are supplied,
  not derived. Nothing here selects a physical law or bears on SM3, the vacuum or gravity.
