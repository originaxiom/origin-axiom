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

---

## Stage 3 (2026-07-16): the form-adjoint realization — OBSTRUCTED (final)

The designed construction was run (`b639_stage3.py` →
`b639_stage3_output.txt`). Two results:

**Positive (the pairing exists and is exact).** The block-diagonal
SL(2)-invariant symmetric pairing B_θ on 27 = Sym¹⁶⊕Sym⁸⊕Sym⁰ (the
f-string antidiagonal recursion) satisfies ρᵀ B_θ ρ = B_θ EXACTLY for
the full holonomy — the form-adjoint contragredient
M ↦ B_θ·conj(M)·B_θ⁻¹ is the correct antilinear companion of the
weight-basis-independent contragredient. Gate: `B_theta invariance
True` at the exact field level.

**Negative (it does not glue).** The peripheral gluing gates FAIL in
all four cells: {plain, W-conjugated} × {λ⁻¹, λ⁺} — no μ-match, no
λ-match. Combined with stage 1 (the +λ intertwiner space has no
invertible element — THEOREM) and stage 2 (the naive weight-basis
transpose fails), this closes the realization question:

> **D_conjθ(M)'s 27-object admits NO representation-twisted amalgam
> realization in the tested class** (linear rep-twists through inner,
> transpose, or form-adjoint contragredients, either weld convention,
> either λ-sign). The θ-twist is irreducibly a FIBER PAIRING: the
> antilinear identification θ₂₇∘conj into the dual, glued at the torus.

**What this means for the twisted cubic (L92).** Its h¹ and any cubic
must be computed on the fiber-paired cochain complex DIRECTLY (the
pairing-glued Mayer–Vietoris, where the connecting map is antilinear on
one leg) — a new machine, not a rewiring of the amalgam-Fox pipeline.
That is a separate arc with its own prereg; L92's current cell closes
here as **resolved-negative (realization), open (dimension)**. cc2's
withdrawal of their h¹ = 3 (they assumed a λ-sign) stands; the
dimension is genuinely open.

**Insight.** The three obstructions are one fact seen three ways: θ is
SL(2)-invisible (fixes the holonomy pointwise), so every attempt to
push the twist into the REPRESENTATION collapses to the untwisted weld
(whose gluing equations then reject the extra conj) — the twist has
nowhere to live except the fiber identification itself. The object
distinguishes "how the fibers are identified" from "how the group
acts": a distinction invisible to character-variety language and
exactly the Gate-2 no-transfer class.
