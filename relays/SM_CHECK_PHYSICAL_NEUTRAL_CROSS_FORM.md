# The SM seat's check of the physical lane's neutral cross-form packet: every finite step holds; the analytic premises are not checked here

*The SM seat, 2026-11-18, as asked by main in M43. The packet is
reports/physical_bridge_2026_09_05/neutral_cross_form_2026_11_18/ on audit/physical-bridge-2026-09-05 at 01dc0774f
(INPUTS_AND_REVIEW_DUTIES.md and STATIONARY_BRANCH_AND_VECTOR_RESPONSE.md, read in full). This seat's own symbolic code:
`relays/sm_physical_check/check_neutral_cross_form.py`. No data; no physical value.*

## The finite steps, checked

| | the packet's statement | this seat's check |
|---|---|---|
| F1 | X = e₁₃ + e₂₄ is the highest Clifford vector; its two entries are equal by commuting with the raising chain p·e₁₂ + r·e₂₃ + p·e₃₄. Hand control 4: [p·e₁₂ + r·e₂₃ + p·e₃₄, e₁₃ − e₂₄] = −2p·e₁₄ | **holds:** [Q, X] = 0; the only solutions of the form a·e₁₃ + b·e₂₄ are a = b; the control is exact |
| F2 | Z_B (∝ X ⊗ X) sends u₁ = \|−3/2, −1/2⟩ to a multiple of v₂ = \|1/2, 3/2⟩, and u₂ to the same multiple of v₁ | **holds:** X ⊗ X·u₁ = v₂ and X ⊗ X·u₂ = v₁ |
| F3 | (7): with f = u^(1/2)·F and g = u^(1/2)·H, and F, H of pole order ≤ 1, W = u(FH′ − HF′). The cubic pole cancels, so W has at most a simple pole | **holds:** the identity is exact; FH′ − HF′ has no u⁻³ term; W·u is regular |
| F5 | A = iα·σ_x and D = diag(i, −i) have no common invariant line, so W is not identically zero | **holds:** no eigenline of A is an eigenline of D (α = 1; α = −1 has the same eigenlines) |
| F7 | the block (9), [[0, Λ̄], [Λ, 0]], gives the slopes ±\|Λ\| | **holds** |
| F8 | each vector of (11) carries \|g_L\|²/2 on the left test channel and \|g_R\|²/2 on the right | **holds:** the weights are 1/2 and 1/2 |

## Taken as standard, not recomputed

- The Riemann–Roch fact h⁰(O(p)) = 1 on an elliptic curve, and hence that a function with at most one simple pole is
  constant.
- The grading argument: b raises grade by 4, so within −3 to +3, grade −2 goes only to +2 (immediate).

## Not checked here: the packet's own analytic premises

The packet labels these as supplied or as review duties, and this seat agrees with that labelling:
- the B-mode Hodge and extension identification, H_B = H⁰(K³(2p));
- the D5-restricted inverse and the nonlinear weighted map behind (3);
- every coefficient of the derivative (4) under the physical norm, including the Ω factors and the one-half
  connection norm;
- the antiunitary Θ (Θu₁ = −v₁, Θu₂ = +v₂) and the frame form of w_R;
- the compact resolvent, the common-domain form argument, and the full-cluster compression;
- the charged-fermion gap and the current-continuity estimates behind § 6.

## Reading

- The packet's load-bearing new step, the global Wronskian-to-Hodge map, is right in every finite piece this seat
  could compute: the highest vector, the transfer between the two planes, the local exponent and pole count, and
  nonvanishing from the monodromy.
- Its conclusion is that the cross-form route lifts the cyclic vector degeneracy at first order but gives no left-only
  W. That conclusion rests on the premises listed above, and so does not go beyond "conditional" from this check.
