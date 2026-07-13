# B570 Lane C, Q-A — RESULT: the trichotomy is decided. σ, θ, φ — three involutions, three levels.

**Run 2026-07-14, inline (owner directive: the crux, full commitment).**
Reproducer: `qa_trichotomy.py`. Locks: `tests/test_b570_qa_trichotomy.py`.

## The question

Is ρ̄ (the complex-conjugate holonomy) equivalent to ρ (inner — the wall), to θ∘ρ
(the fold does two jobs — the dream), or a third thing?

## The answer: the third thing — and it has three-level structure

**Level 1 — the group (E₆(ℂ)): σ and θ are independent; options (1) and (2) were
never distinct; both are FALSE.**
- The geometric character is a Galois pair: for the standard 2-bridge parabolic
  generators (relation aW = Wb, W = ba⁻¹b⁻¹a, verified exact), tr ρ(ab) =
  **(5+√−3)/2**, minimal polynomial **t² − 5t + 7, discriminant −3**. Its Galois
  conjugate (5−√−3)/2 is ρ̄'s value. Non-real ⇒ **ρ̄ ≁ ρ** (option 1 false), at
  SL(2) and — via the banked non-real adjoint trace 37437270+38799960√3·i — at E₆.
- **Option (2) was never a separate branch:** the F₄-principal nilpotent is
  REGULAR in E₆ (Jordan type on the 27: E₆-principal = (17,9,1) = F₄-principal on
  1⊕26 — exact weight-grading computation), so a principal sl₂ lies inside
  F₄ = E₆^θ and θ fixes a principal embedding ι pointwise. Hence θ∘(ι∘ρ) ~ ι∘ρ
  **always**, and "ρ̄ ≅ θ∘ρ" ⟺ "ρ̄ ≅ ρ" — killed by the same non-real trace.
- So at the group level the object carries a **Klein four ⟨θ, σ⟩**: θ = Out(E₆) =
  the fold (a symmetry of the holonomy), σ = Galois conjugation √−3 ↦ −√−3 =
  complex conjugation (NOT a symmetry — it moves the point). The chirality is σ,
  not θ. The fold does not spend it; the Galois structure of the trace field
  supplies it.

**Level 2 — the character variety: σ acts as the object's own mirror.**
By Mostow rigidity + amphichirality (4₁ ≅ its mirror; verified in-sandbox via the
symmetry group, orientation-reversing isometry exists), ρ̄ ≅ ρ∘φ where φ is the
amphichiral outer automorphism of π₁. On the geometric component: **σ(χ_ρ) =
χ_{ρ∘φ}** — the Galois twin is the same point transported by the object's own
mirror. The σ-bit (which embedding of ℚ(√−3)) = the orientation bit: free given
an orientation, exchanged by φ. **This is the B469 orientation residue again** —
the ℤ/2 the program has carried since the breath campaign is exactly the Galois
choice.

**Level 3 — the tangent (H¹): the fold is the mirror, modulo conjugation.**
*(Corrected during banking — the B570-C1 verifier caught a wording conflict in the
registry: T-θTANGENT said "the amphichiral involution IS θ", but the amphichiral
map is ANTILINEAR (B347 `_AMPHI`, conjugate=True; C1: J² = +1 on all six exponent
lines) while θ is ℂ-linear. The reconciliation, now in the registry: the
amphichiral involution acts as **conj∘θ**; the ℂ-linear θ itself is realized by
the HYPERELLIPTIC involution (B353, gauge-certified 7.1e-102).)*

With dφ = conj∘θ (antilinear) and dσ = conj:

> **d(σ∘φ⁻¹) = conj∘(conj∘θ) = θ** — the composition of the Galois conjugation
> with the object's mirror is HOLOMORPHIC and equals the fold, exactly, at the
> tangent. Its fixed directions are the θ-even (F₄) plane; the θ-odd plane is its
> (−1)-eigenspace.

So "ρ̄ = θ∘ρ" is false at the group level and **true at the tangent after
mirror-correction**: σ = φ∘(the θ-fold) infinitesimally. The antilinear real
structure conj∘θ itself has fixed form (θ-even)_ℝ ⊕ i·(θ-odd)_ℝ (exact linear
algebra, locked) — the θ-odd directions, where C3 found the living order-4
monodromy, are the imaginary axes of the object's self-mirror and the (−1)-axes
of the mirror-corrected fold.

## What this settles

- The chirality is **not dead and was never in F₄**: it is the σ-column (Galois /
  orientation / the B469 residue), independent of the θ-fold at the group level.
- The fold does two jobs only at the tangent level (dφ = θ) — it does not
  purchase a finite chirality bit, but it aligns the infinitesimal chirality
  axes with the θ-odd sector, which C3 showed is dynamically alive.
- The gap-chirality duality (B569 reframe, C2's target) gets its precise form:
  non-real traces (the compactness gap) ⟺ σ moves the point ⟺ the σ-chirality is
  nonzero. **One fact, two names — at the level of the character, exactly.**

Firewalled: no SM claim. The Klein four ⟨θ, σ⟩ + the three-level structure is
object mathematics; what couples to it is AP4/AP6's question.
