# B1727 — THE FLAVOUR-BLIND BOUND (P-299): IN B1656'S FRAME A FLAVOUR-BLIND HIGGS GIVES Y = c·1 + [a]_× IN EVERY SECTOR, AND THEN m₂/m₃ ≥ 1/3, SHARP — THE CHARGED-FERMION HIERARCHY NEEDS A FLAVOURED HIGGS

**Verdict: PROVED** (a theorem with a short proof; its premise and every step checked by main's own code; no data).
cc (main), 2026-10-23. No physical quantity is derived. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /flavou?r.blind|flavou?rless higgs|S = 1|cross.product matrix|\[v\]_|Weyl's inequalit|singular.value bound/ (full text): 39 of 1498 arcs on main match (NEGATIVE 8, PROVED 31)`.
Most matches use "S = 1" or "cross product" in other senses. Bearing on it:
- B1642 and B1649 (at the fibre's puncture S = 1 gives an antisymmetric coupling with the theta triplet as null vector);
- B1716 (with S a unit and its channel weight zero, the coupling is a signed cross product with spectrum (‖w‖, ‖w‖, 0));
- B1656 (the four-channel coupling this arc reads), B1724 (the readings), B1725 (the ingredients the frame needs).

None bounds the hierarchy for a flavour-blind Higgs in the four-channel frame, where the channel 1 adds c·1. The web
seat found the bound numerically and gave its own proof in its relay to the SM seat (HARVEST_LEDGER row 1310; RELAY_LEDGER,
`CHAT1_TO_SM_2026-10-22_THE_HIGGS_ARC_CHECKED.md`); this arc is main's proof, by a different route, with the premise
computed in main's frame. **Literature:** Weyl's inequalities for singular values; the cross-product identity
[u]_×[v]_× = vuᵀ − (u·v)·1; standard.

## 1. The premise, computed (`verification/the_flavour_blind_bound.py`, part A)

With S = 1, B1656's coupling (the functions B1723 sealed) is linear in the four channel weights (to 2.5 × 10⁻¹⁶ on 20
random complex weightings), and the unit weights give
- the channel 1 → the identity;
- the channels i, j, k → the three elementary antisymmetric matrices (exactly).

So in every sector **Y = c·1 + [a]_×**, with c ∈ ℂ the weight on 1 and a ∈ ℂ³ built from the weights on i, j, k. The
line, τ, the horocycle and the sector enter only through the weights.

## 2. The theorem

**For every c ∈ ℂ and a ∈ ℂ³, the singular values σ₁ ≥ σ₂ ≥ σ₃ of M = c·1 + [a]_× satisfy σ₁ ≤ 3σ₂, so m₂/m₃ ≥ 1/3.
Equality holds at c = 1, a = 2i·e₁ (singular values 3, 1, 1).**

*Proof.* Write A = [a]_×, antisymmetric.
1. Mᵀ = c·1 − A has the singular values of M, and M + Mᵀ = 2c·1. Weyl's inequality σ_{i+j−1}(X + Y) ≤ σ_i(X) + σ_j(Y)
   with i = j = 2 gives 2∣c∣ = σ₃(2c·1) ≤ 2σ₂. So **∣c∣ ≤ σ₂**.
2. [ā]_×[a]_× = a āᵀ − (ā·a)·1, so A†A = ∣a∣²·1 − a a†, with eigenvalues ∣a∣², ∣a∣², 0. So **σ₁(A) = σ₂(A)**.
3. By Weyl, σ₁(M) ≤ ∣c∣ + σ₁(A) = ∣c∣ + σ₂(A), and σ₂(A) = σ₂(M − c·1) ≤ σ₂(M) + ∣c∣. So σ₁ ≤ 2∣c∣ + σ₂ ≤ 3σ₂ by step 1. ∎

At c = 0 the ratio is 1 (the spectrum (∣a∣, ∣a∣, 0) of B1716 and B1642).

## 3. The checks

| part | what | result |
|---|---|---|
| B | the minimum of m₂/m₃ over (c, a), 400 Nelder–Mead starts (c = 1 without loss; a modulo SO(3) and conjugation) | **0.333333333333**, at a purely imaginary a of length 2 |
| C | the three steps on 200 000 random (c, a), ∣a∣ over six decades | (i) max (∣c∣ − σ₂)/σ₁ = −1.9 × 10⁻¹⁰; (ii) σ₁(A) = σ₂(A) to 1.3 × 10⁻¹⁵; (iii) max (σ₁ − 3σ₂)/σ₁ = −0.026; no violation; the random minimum 0.342 |
| D | the equality case | singular values (3, 1, 1) |

## 4. What it means

- **A flavour-blind Higgs cannot give the charged-fermion hierarchy in B1656's frame, in any sector.** The data's
  m_c/m_t ≈ 0.0037, m_s/m_b ≈ 0.02 and m_μ/m_τ ≈ 0.06 lie far below 1/3 (m_c/m_t by a factor of about 90).
- **The hierarchy comes from the Higgs's flavour section**, the weight-3/2 form (B1691's ∂R, main's DR), in its interplay
  with the channel weights; the weights alone cannot make it. This bears on P-295 (which flavoured object enters each
  sector, and how it is read) and on P-300 (a principle that selects zero-free twisted Higgs lines).
- **Scope.** B1656's coupling with S = 1; any line, τ, end and sector. A coupling with a different channel structure (a
  flavour-blind doublet whose couplings carry the hierarchy themselves) is outside it.

## Files

- `verification/the_flavour_blind_bound.py` → `the_flavour_blind_bound.json`, `the_flavour_blind_bound_run.txt`.
- The lock: `tests/test_b1727_the_flavour_blind_bound.py`.
