# B639 — C2 honest partial: the twisted double's 27-realization is NOT SL(2)-visible

**Date: 2026-07-16. Prereg 7075dd63… (sealed first); the G1-adjudication
branch taken as provided. Mathematics only.**

## The three probe results (exact, banked)

1. **The λ↦+λ conjugate gluing is INCOMPATIBLE:** the intertwiner space
   is 1-dimensional with NO invertible element — the weld's λ-inversion
   is rigid (`b639_output.txt`).
2. The SL(2)-level "contragredient" probes are equivalent to plain-conj
   statements: for SL(2) the contragredient is INNER ((gᵀ)⁻¹ = wgw⁻¹),
   so no SL(2)-level solve can see θ (`b639_repair.py`).
3. The naive 27-level contragredient lift FAILS both peripheral gates
   (`b639_stage2_output.txt`) — confirming (2) at the module level.

## The structural insight these force

**θ (the E₆ diagram involution) FIXES the holonomy pointwise** — the
principal nilpotents e_pr = Σeᵢ, f_pr = Σfᵢ are θ-invariant (the
diagram symmetry permutes the simple roots; the sums are symmetric), so
θ∘ρ = ρ for the whole geometric image. Hence conj∘θ∘ρ = conj∘ρ: **the
twisted double's REPRESENTATION is the same as the weld's; the θ-twist
lives entirely in the FIBER IDENTIFICATION** — the gluing of the
27-fibers across the torus by the antilinear pairing θ₂₇∘conj
(θ₂₇: 27 → 27̄ the diagram-involution intertwiner). D_conjθ(M)'s
27-object is a local system glued through a PAIRING, not a
representation twist — exactly the Gate-2 class of subtlety (no
invariant transfer without the explicit map). cc2's per-block
computation saw this structure correctly through the self-dual adjoint
blocks; the 27 needs θ₂₇ built explicitly.

## The designed next construction (registered; not run)

Build θ₂₇ exactly from B575's data (the invariant pairing
27 ⊗ 27̄ → ℂ composed with the weight-negation/longest-element map);
realize the twisted local system as the θ₂₇∘conj-glued module; rerun
the pipeline (h¹ = 3 check vs cc2; the C/C*-glued cubic; the one
number). Registered as the C2-completion cell in OPEN_LEADS.
