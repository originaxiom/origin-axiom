# B561 — the L50 CRUX computed: no Eisenstein ℤ/3 selects SU(3)² inside F₄

Seat-1's handoff assembled a chain **E₆ →[θ] F₄ →[ℤ/3?] SU(3)² →[cusp?] SM** and
asked (PRIORITY 1) whether the figure-eight's Eisenstein ℤ/3 (from its trace field
ℚ(√−3)) selects the A₂×Ã₂ = SU(3)×SU(3) maximal subalgebra of F₄. Bounded,
decidable — computed here. **Verdict: NO** — and the reason is clean and
multiply-confirmed. Firewall-clean; nothing to CLAIMS.md. Lock:
`tests/test_b561_l50_crux.py`. Memory context: the E₆→SM *dictionary* was already
verified-and-refuted once (B347, G₂⊕A₂ mislabel); only the θ = E₆→F₄ split survived.

## What is real (Step 1 — FORCED)

E₆ exponents {1,4,5,7,8,11}; the amphichiral θ-grading (−1)^{m+1} (B353, the
hyperelliptic involution) gives **θ-even = {1,5,7,11} = the F₄ exponents** (rank 4 =
SM gauge rank) and θ-odd = {4,8} (the 26). This is forced, geometric, and standard
Lie theory. The θ-even exponents are exactly the integers coprime to 6 in [1,11].

## The group-theory CONDITIONAL (true, but its premise fails)

By Borel–de Siebenthal (F₄ extended-Dynkin marks 1,2,3,4,2), F₄'s maximal-rank
subalgebras are B₄=SO(9) and C₃×A₁ (centralizers of **order-2** elements) and
**A₂×Ã₂ = SU(3)×SU(3)** (the centralizer of the **order-3** element, the mark-3
node). So **IF** a genuine order-3 automorphism of F₄ acted on the figure-eight's
character variety, its centralizer would indeed be SU(3)×SU(3). The chain hinges
entirely on that premise.

## The premise FAILS — there is no Eisenstein ℤ/3 at the figure-eight point (five checks)

1. **The F₄ sector's own symmetry is Klein-four, not ℤ/3.** The θ-even exponents
   {1,5,7,11} = (ℤ/12)*, and (ℤ/12)* ≅ ℤ/2 × ℤ/2 — every non-identity element has
   order 2. **No order-3 structure exists in the F₄ deformation grading.**
2. **The figure-eight has no order-3 symmetry.** Its isometry group is **D₄ (order
   8)** (SnapPy); by Lagrange, a group of order 8 has no order-3 element. So no
   geometric ℤ/3 acts on the character variety.
3. **The trace field's Galois group is ℤ/2, not ℤ/3.** ℚ(√−3) has Gal = ℤ/2
   (conjugation √−3 → −√−3, = complex conjugation). ω = (−1+√−3)/2 is a field
   *element*; multiplication-by-ω is **not** a character-variety automorphism. The
   handoff conflates ω∈field with a group automorphism.
4. **The order-3 Eisenstein rotation lives elsewhere.** B257: ζ₆ (ζ₆²=ω) is the
   meridian rotation at the **Euclidean transition point x=1**, where the geometry
   *collapses* and the trace field *degenerates to ℚ* — NOT the complete hyperbolic
   figure-eight (x at the geometric point, field ℚ(√−3)). The ℤ/3 is real, but at a
   different, degenerate point on the deformation curve.
5. **The trinification ℤ/3 is θ-broken.** The cyclic ℤ/3 permuting SU(3)³ in
   E₆ ⊃ SU(3)³ does not survive the fold: θ merges two of the three SU(3) factors,
   breaking the cyclic symmetry. So no residual ℤ/3 descends to the F₄ sector.

## Verdict and scope

**The E₆ → F₄ chain terminates at F₄.** The specific proposed Step-2 selector — the
Eisenstein ℤ/3 choosing SU(3)² over SO(9)/Sp(6)×SU(2) — **does not exist** at the
figure-eight's geometric point; the object's arithmetic symmetry there is **ℤ/2 ×
ℤ/2 (Klein four)**, not ℤ/3. F₄ → SU(3)² would require an order-3 selector the object
does not provide. Step 3 (cusp breaking SU(3)²→SM) is therefore moot.

This closes the *specific* L50-CRUX mechanism (Eisenstein-ℤ/3 selection); it is
consistent with B463 (principal centralizer = 0) and does not depend on the full
exceptional 3d-3d theory T[4₁;E₆] (still NEEDS-SPECIALIST, Gate B) — the algebraic
sub-question is answered without it, exactly as the handoff framed. It is **not** a
claim that "F₄→SM is impossible in general" — only that *this object's own
arithmetic does not select SU(3)²*.

## The surviving positive (worth recording)

The F₄ deformation sector carries a **ℤ/2 × ℤ/2 (Klein-four)** symmetry, matching the
figure-eight's *two* ℤ/2 gradings (θ = E₆→F₄, and the second grading of B258/B314)
and its D₄ isometry group — the object is constitutively **ℤ/2-arithmetic**, not
ℤ/3-arithmetic, at its geometric point. The Eisenstein ℤ/3 belongs to the *Euclidean*
anchor (B257), a different point of the two-/three-ended family. The honest headline
remains B353: **the E₆→F₄ θ-fold is forced; F₄ is where the gauge-structure chain
stops.**
