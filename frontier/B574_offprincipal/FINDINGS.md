# B574 — the off-principal proposal, adjudicated: right instinct, false crux, question sharpened

**Date:** 2026-07-14. **Source:** the cross-seat "the principal point is the wrong
place to look" handoff (nilpotent-orbit escape route).
**Locks:** `tests/test_b574_offprincipal.py` (2).

## What the handoff gets right

The walls banked this week are statements about specific structures, and it is fair
to ask what they scope over. The instinct "look away from the principal point" is
the program's own open item (AP6: the non-principal lift). Credit where due: the
question "which nilpotent orbits admit which centralizers" is the right *kind* of
question.

## The crux is false — and self-contradictory

**"The minimal nilpotent of E₆ has centralizer D₅ = Spin(10)" is FALSE.** The
minimal nilpotent orbit of E₆ *is* the A₁ orbit (the highest-root sl₂) — the very
orbit the handoff's own list correctly assigns centralizer SU(6). Verified exactly
(locked): the adjoint grades under the highest-root coweight as
(1, 20, 30, 20, 1); dim z(minimal sl₂-triple) = 36 − 1 = **35 = dim A₅ = su(6)**,
not 45 = dim D₅. **No nonzero nilpotent orbit of E₆ has reductive centralizer
Spin(10).** D₅ centralizes a *semisimple* element — it is the Levi of the node-1
parabolic, which is exactly the unforced selector of clause 9 (B572), returning
through another door.

## The wall was never about the principal orbit

**At the minimal-embedding point the fifth wall applies verbatim** (locked): the 27
graded by the minimal sl₂ is **6·V₁ ⊕ 15·V₀** — six doublets and fifteen singlets,
every summand self-dual. The obstruction is not "regular nilpotent admits no
refinement"; it is: **every SL(2,ℂ) representation is self-dual.** Any composition
ι∘ρ — principal, minimal, or any of the 21 orbits' embeddings — has rank-1 Zariski
closure and is vector-like. AP4's banked statement was already
embedding-independent; changing the orbit changes nothing.

## "Nearby points with minimal meridian": impossible

Regularity is Zariski-open (the regular orbit is dense in the nilpotent cone). The
geometric point's meridian is regular (banked Jordan {3,9,11,15,17,23}), so every
point in a neighborhood has regular meridian. Minimal-meridian points exist only in
distant strata — e.g. ι_min∘ρ, which is rank-1 and killed above. The proposed
"intersection of the minimal-nilpotent locus with the non-real locus" is therefore
not the decisive computation: its candidate points are either nonexistent (near the
geometric point) or vector-like (the factored ones).

## The sharpened true question (the handoff's instinct, made precise)

The only escape from the fifth wall is a representation π₁(M₃) → E₆(ℂ) whose
Zariski closure has **rank ≥ 2** — one that does not factor through any SL(2,ℂ)
at all. The room exists: H¹ = 6 at the geometric composition, while the
SL(2)-factored locus accounts for only 1 of those directions. The five
higher-exponent directions (including the θ-odd pair {4, 8}) point off the
factored locus **to first order**. Whether they INTEGRATE to honest E₆
representations is governed by the obstruction pairing (the cup product / Goldman
bracket H¹ × H¹ → H² in adjoint coefficients):

> **THE BRIDGE QUESTION, FINAL FORM: compute the quadratic obstruction on the
> 6-dimensional H¹. If some higher-exponent direction is unobstructed, honest
> rank-≥2 E₆ deformations of the geometric representation exist, and the
> chiral-selector question reopens there. If all five are obstructed, the
> figure-eight's E₆ representations near the geometric point are exactly the
> SL(2)-factored curve — and the fifth wall becomes a sixth: chirality is
> unreachable on the entire local variety.**

Bounded, decisive, and honest — this replaces the handoff's intersection proposal.
Queued as the first post-Review-16 computation.

Firewalled. Nothing to CLAIMS.md.
