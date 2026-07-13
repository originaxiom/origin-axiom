# B575 / L51 — THE BRIDGE OBSTRUCTION: Q ≡ 0. The bridge is open at second order, in every direction.

**Date:** 2026-07-14. **Prereg:** PREREGISTRATION.md (run immediately on owner
directive). **Reproducer:** `l51_obstruction.py` (exact, ℚ(√−3), ~5.5 min; the
`verify` argument runs the adversarial self-checks). **Lock:**
`tests/test_b575_bridge_obstruction.py` (the full build re-runs as the lock; every
gate is an assert).

## The result

At the E₆ geometric point P = ι∘ρ, the quadratic obstruction
Q: H¹ → H², Q(u) = [u ∪ u] (cup product on the relator 2-cell with the true e₆
bracket) **vanishes identically**: all six diagonal components Q(u_m) = 0 for
m ∈ {1, 4, 5, 7, 8, 11} **and all fifteen cross-pairings B(u_a, u_b) = 0** — in
exact arithmetic, end to end.

> **The preregistered positive outcome fired in its strongest form: every
> off-factored direction — including both θ-odd directions {4, 8} — is
> unobstructed at second order. The sixth wall does not exist at this order.
> Honest rank-≥2 E₆ deformations of the geometric representation exist to
> second order in every direction: the local E₆ representation variety is not
> the SL(2)-factored curve; at quadratic order it is a smooth 6-fold through
> the principal point.**

## The build (all gates green)

e₆ constructed explicitly inside gl(27) from the minuscule weight model (27
weights; 36 edges; 10 GF(2) commuting-square constraints solved; adjacent double
squares proven absent). **G1:** [eᵢ, fⱼ] = δᵢⱼhᵢ with h-diagonals = Dynkin
labels; bracket closure dimension exactly 78. **G2:** principal sl₂ relations
exact; adjoint isotypics = (23, 17, 15, 11, 9, 3). **G3 (end-to-end):** the
figure-eight relator r = a(ba⁻¹b⁻¹a)b⁻¹(a⁻¹bab⁻¹) evaluated on
ι₂₇(ρ(a)) = exp(e_pr), ι₂₇(ρ(b)) = exp(ω·f_pr), ω = (1+√−3)/2, equals the
**exact identity** in E₆. **G4:** dim H¹(V_{2m}) = dim H²(V_{2m}) = 1 for all six
exponents (Fox calculus on the 2-generator presentation; consistent with the
banked H¹ = 6). **G5 (control):** Q(u₁) = 0 — the m = 1 direction is the existing
SL(2) character curve and must integrate; it does.

## The verification pass (the zero is real)

An identically-zero answer is what a broken cup formula would also produce, so
the zero was adversarially tested: (V1) the raw cup cocycles c(r) are **nonzero
before projection** — the classes vanish because the cocycles are genuine
coboundaries, not because the machinery produces zeros; (V2) the classes are
invariant under shifting representatives by coboundaries; (V3) the H²
functionals are nonzero; (V4) **constructive certificates:** the second-order
correction systems L·v = −c(r) were solved explicitly along both θ-odd
directions — the corrected deformations exist concretely, not just
cohomologically. **Results:** raw cocycles have 396 (u₄∪u₄), 456 (u₈∪u₈), 456
(u₄∪u₈), 219 (u₁∪u₄) nonzero entries of 729; all classes coboundary-invariant;
all six φ nonzero; the correction systems solved along u₄ (target blocks
{1, 5, 7}) and u₈ (target blocks {1, 5, 7, 11}) — **matching exactly the
Λ²-transvectant channel predictions** ([V₈,V₈] ⊆ V₂⊕V₁₀⊕V₁₄ → exponents
{1,5,7}; [V₁₆,V₁₆] adds V₂₂ → {1,5,7,11}), an independent structural
cross-check of the whole pipeline. Re-runnable via `l51_obstruction.py verify`.

## Honesty bar

- Second-order unobstructedness is not full integrability: higher (Massey)
  obstructions are not computed here. But Q ≡ 0 *identically* — not merely a
  nontrivial cone — is exactly the signature of a smooth point, and the
  Porti-style theorem (smoothness of principal-composition points of character
  varieties, proved for SL(n); the argument is expected to transfer to E₆ via
  the same boundary/duality mechanism) is the literature companion: **cited as
  expected, not assumed.** Registered as the residual caveat.
- Nothing here says the deformed representations reach a chiral selector. It
  says the fifth wall was a statement about the *point*, not the *variety*: the
  variety continues past the principal point in all six directions, and the
  reachability question is now live on the deformed locus.

## What opens (registered)

**L59 — THE REOPENED SELECTOR QUESTION:** along the θ-odd deformations
(u₄ first), what is the Zariski closure of the deformed representation, and does
the 27 become complex under it? The subalgebras of e₆ whose exponent sets
contain {1, 4} include **D₅ and A₅** — the deformed closure has somewhere
chiral to go. This is the direct successor of L51 and the σ→θ bridge's next
(and possibly last) segment: first-order motion is θ-odd (the imaginary axes of
σ, where C3's dynamics lives); if the closure lands D₅-side, the chiral 16
becomes holonomy-visible for the first time in the program's history.

Firewalled. Nothing to CLAIMS.md. The bridge opened into mathematics; whether
physics walks across it is L59's question, not tonight's claim.
