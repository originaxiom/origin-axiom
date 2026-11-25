# B2004 — Listening card 19: the mechanism of the halving — the whole as the modular group ℤ₃ * ℤ₂, and the fixed points of the elements outside its commutator subgroup

Written 2026-11-25, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## Why, and what was derived by hand before this card (disclosed)

B2002 and B2003 found p_neutral(2x) = 2^d (x² − 9) x S(x). It holds exactly up the 3-tower from mod 27, where ω's exchange C
fixes three points, and nowhere else run. Main derived the following by hand before writing this card. The run checks each
step.

1. **The involution.** σ := R C⁻¹ = (x, y, z) ↦ (y, x, xy − z) is an involution. The moves are R = σC, L = σC², X = CσC, and
   their inverses. So the whole acts through the free product ℤ₃ * ℤ₂ = ⟨C⟩ * ⟨σ⟩, the modular group PSL(2, ℤ).
2. **The operator.** With P_g the permutation of g and Π_q the projector on C's sector q, W = T − D, where
   T = (1 + P_C + P_C⁻¹) P_σ (1 + P_C + P_C⁻¹) = 9 Π₀ P_σ Π₀ and D = Σₖ P_Cᵏ P_σ P_C⁻ᵏ = 3 Σ_q Π_q P_σ Π_q. Hence:
   - W|neutral = 6 Π₀ P_σ Π₀;
   - W|charged q = −3 Π_q P_σ Π_q.
3. **The twist.** Let ρ be the modular group's order-6 character, ρ(C) = ω and ρ(σ) = −1; its kernel is the commutator
   subgroup Γ′. Twisting the permutation representation by ρ moves sector q to sector q + 1 and turns P_σ into −P_σ.
   - So if Perm(orbit) ⊗ ρ ≅ Perm(orbit), the compression of P_σ to a charged sector is minus its compression to the
     neutral one, and step 2 gives the halving.
   - The two characters differ by |Fix(g)| (1 − ρ(g)), which vanishes unless an element g outside Γ′ fixes a point.
   - **The mechanism to test:** on the 3-tower, the only elements outside Γ′ that fix points are the conjugates of C^{±1}.
     Their three fixed points account for the three modes the identity leaves out.

## The checks

- **K1:** step 1 symbolically, and step 2 exactly as matrix identities on the orbit of (3,3,3) mod 27 and mod 81 and on the
  leaf mod 5.
- **K2 and K3,** the fixed-point census: for every reduced word g in C^{±1} and σ of length at most 10, the number of fixed
  points on the orbit and ρ(g). Words are classified by their cyclic reduction (a conjugate of C^{±1}, of σ, or other). Run on
  mod 27, 81, 9, 25 and 5, 7 (leaf).

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| K1 | steps 1 and 2 hold exactly, at every level run | 0.95 |
| K2 | on the 3-tower (27, 81) every word outside Γ′ with a fixed point is a conjugate of C^{±1}, with exactly three fixed points; σ fixes none | 0.5 |
| K3 | at mod 9, 25, 5 and 7, some word outside Γ′ that is not a conjugate of C^{±1} fixes a point | 0.6 |

## What it means

- **If K1 to K3 hold:** the halving is explained. The whole is the modular group, and at its prime 3, away from ω's three
  fixed points, its action cannot tell the order-6 twist from no twist. The neutral member and the charged pair are then the
  same action seen through ρ. The factor 2 is 6 : 3, the counts of the two pieces of the unfolding.
- **If K2 fails:** the mechanism is something else, and the census shows what fixes points.
- **Nothing is compared with data.**
