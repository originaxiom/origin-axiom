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

## Addendum (probation P22, 2026-07-13): the Klein-four → SO(9) follow-up ALSO closes

Seat-1's follow-up to the L50 kill: since B561 found the F₄ sector is ℤ/2×ℤ/2 (not
ℤ/3), use the **second** ℤ/2 — γ = Gal(ℚ(√5)/ℚ), the golden conjugation (√5→−√5), a
*genuine* automorphism (the ω-error correctly fixed) — to select an order-2 subalgebra
of F₄: a (3,1) exponent split → SO(9)=B₄ → Pati-Salam → SM, vs (2,2) → Sp(6)×SU(2).
Computed (`tests/test_b561_klein_four.py`). **Verdict: TOMBSTONE — F₄ is the terminus.**

**The premise fails (a subtler cousin of the ω-error — mis-located DOMAIN, not
mis-typed element).** γ does not act on the θ-even H¹:
- The **F₄ deformation sector lives over ℚ(√−3), not ℚ(√5).** B370's depth-2 Gram data
  is **τ = −2√3·i = −2√(−3)** across all six directions (no √5); the E₆ tangent is over
  ℚ(√−3) (B347). Since γ = (√5→−√5) **fixes ℚ(√−3) pointwise**, it acts **trivially** on
  all four exponent directions — nothing to flip. By seat-1's own rubric,
  trivial-action ⇒ TOMBSTONE, F₄ terminus confirmed.
- γ's real domain is the **quantum/WRT face** (Face IV): the colored-Jones data
  J_N(4₁;ζ₅) ∈ ℚ(√5), the SU(2)₃ modular data, the Yang–Lee conjugation (B314) — the
  **E₈/golden end**, a different object from the classical E₆/√−3 deformation space.
  The Klein four is real, but its two generators act on the **two different ends**: θ
  (√−3) folds E₆→F₄; γ (√5) conjugates the quantum face. Neither is a second selector
  *within* the F₄ sector.
- **Independently, B347 already settled it:** the E₆ tangent grading is **uniform** —
  one direction per exponent, none privileged, "CP-even everywhere... does not select
  among exponents — a clean negative" (the symmetric achiral centre, K022). There is no
  (3,1)/(2,2) split to be had.
- *Secondary gap (not even needed):* the H¹ exponent directions are cohomology classes,
  not the Lie algebra f₄, so "count of γ-fixed exponents → symmetric subalgebra" is not
  an established dictionary regardless.

**So the E₆→F₄ chain terminates at F₄ under BOTH ℤ/2's and the ℤ/3** — the golden
conjugation lives on the quantum end, the Eisenstein ℤ/3 at the collapsed Euclidean
point, and the E₆-deformation grading is non-selecting. F₄ (rank 4) is where the
gauge-structure chain stops; the object stays the symmetric, achiral, value-free centre.

## Addendum (the cusp-boundary-condition reframe, examined 2026-07-13)

Seat-1's meta-point: the SM gauge group is not a symmetry-selected subalgebra but the
**holonomy centralizer at a boundary-selected point** — so ask "what is the centralizer
at the cusp-constrained point?", not "which symmetry selects a subalgebra?". The frame
is correct physics and distinct from the three kills (ℤ/3, both ℤ/2's, the grading). But
the boundary-condition computation **is already in the repo**, and it places the reframe
precisely (`tests/test_b561_klein_four.py::test_cusp_is_uniform_not_the_F4_selector`):

- **The specific mechanism ("the cusp reduces E₆→F₄ by killing the θ-odd directions") is
  REFUTED by B357.** B357 (the E₆ boundary restriction) found **rank 6/6 — no
  peripherally-invisible deformations**: all six directions restrict to nonzero boundary
  classes, each "opens the cusp" (φ_μ ≠ 0 every block). And the **universal-τ identity**:
  every exponent block sees the *same* cusp shape τ = −2√3·i = −2√(−3), "the leading
  peripheral datum does **not** split by exponent." So the cusp constraint is **uniform
  across θ-even and θ-odd** — it kills none of the six and cannot single out the θ-odd
  pair. There is no 6→4 reduction (universal-τ is a rank-1 identity that holds
  automatically, not a codim-2 cut). **The E₆→F₄ split is the amphichiral symmetry θ
  (B353), not the cusp** — the cusp is achiral and does not fold.
- **The centralizer at the cusp point was computed — B463 = 0.** B357 is explicit that
  the object is the **principal-composed geometric representation at the complete
  structure** (parabolic meridian = the cusp condition). That *is* the principal point,
  and B463 computed its centralizer = **0** (finite group centralizer, irreducible
  holonomy). So "the centralizer at the cusp-constrained point" is not un-asked — it is
  B463, and it is trivial.
- **What genuinely remains is the same SPECIALIST wall.** The one survivor: the
  centralizer at *non-principal, reducible* points that also satisfy the cusp
  A-polynomial (larger centralizer). Reaching those needs the **full E₆ A-polynomial /
  character variety** — uncomputed, the same wall as L50 (SL(2)=P23 known, SL(3)=P24
  three components, E₆ open). And nothing motivates SU(3)×SU(2)×U(1) there: a reducible
  degeneration is not the geometric structure, and no computed condition selects that
  subgroup. So the reframe is valid but its computable core is either done (B357/B463) or
  behind the E₆-A-polynomial specialist wall.

**Net (the fourth disposition):** the cusp is the object's achiral, *uniform* boundary
datum (B357); it does not select a subalgebra — it opens equally in all six directions.
The E₆→F₄ fold is the symmetry θ; F₄ is the terminus; the geometric-cusp centralizer is
0 (B463); the reducible-cusp-point question is SPECIALIST. The reframe is correctly
*placed*, not killed — but it does not open a new in-sandbox route to the SM.
