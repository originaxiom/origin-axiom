# B1466 — PREREGISTRATION: THE COUNT IS THE ORDER, AND IS THE REGISTER BINARY — the two stacking orders at the counted point, their opposite counts, the cup product that decides whether both can be held at once, and the source that picks one

**Sealed before any computation on the population.** cc (main), 2026-10-03. The owner's directive of 2026-10-03
("i aprove, lets do it when right timing"): the sourced non-split configuration at a non-complete point, graded against
the bar. Lead L241 (the measurer question, refinement 2 "the count is the order", owed as a sealed arc) and GENESIS FK12
(ii) "binary or richer".

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "non-split|extension class|Ext\^1|cup product|obstruct|stacking order|the count is
  the order|both orders|source term|R76|R77"`: *VERDICT topic-sweep: 115 of 1337 arcs on main match (NEGATIVE 22, OPEN 6, PROVED 85, RETRACTED 2)*; narrowed to the
  obstruction vocabulary ("cup product|obstruct|stacking order|both orders|second-order deformation"): B270, B273, B352, B370
  — the quadratic cup-product obstruction computed at ρ_prin for the E₆ deformations, identically zero there to third order;
  the method of C3 below is theirs (the second-order term of the relator under a first-order deformation, read in H²),
  applied at the split module A ⊕ 1 instead. Read: B1453 (`join_own.py`:
  Ballas' family, μ = −1, the cocycles of the 4-dim module by linear algebra, the non-split W₁ = [[A, c], [0, 1]] with
  I(W₁) = −1 at q = 17 ± 12√2, 0 at the ±i points; h¹(A) = h¹(A*) = 1 at the four exceptional points), B1455 (L1–L3;
  the follow-up index: I(W₁) = −1, I(W₁*) = +1; ι*W₁ ≅ W₁(1/q₀), τ*W₁ ≅ W₁), B1457 (the audit lane's R41 flag balances,
  R76 — along the non-split extension scaled by t the potential is a·t² + c·t⁴ with a ≥ 0, c > 0, lowest at the split
  limit — and R77, an added source holds the counted configuration at the price of flat directions; read, not
  re-derived), B1459 (the complete points carry no reductive count), B1462 and B1465, GENESIS GAP3 ("a count needs an
  order of the pieces, an open end, and a source or a flux of the right sign") and FK12. L241's refinement 2 (exploratory,
  2026-10-02): "at one vacuum the same two pieces stacked in the two orders count −1 and +1 and side by side 0".
- **Literature.** The obstruction theory used is textbook (a first-order deformation φ ∈ Z¹(Γ; End V) extends to second
  order iff the class of φ ∪ φ in H²(Γ; End V) vanishes; for a one-relator group the presentation complex computes H²
  as V / im d¹, d¹ the Fox map of the relator). Ballas arXiv:1403.3314 for the family, as in B1455. Nothing else searched.

## 1. The objects, fixed now

Γ = ⟨m, n | mnMNmNMnmN⟩ = π₁(m004); Ballas' ρ_q at q₀ = 17 + 12√2 and q₀′ = 17 − 12√2 with the central twist μ = −1
(A = μ ⊗ ρ_q, rank 4), the two points where h¹(A) = h¹(A*) = 1 (B1453); controls at q = 2 (h¹ = 0) and at the ±i points
(B1453: the extension exists and counts 0). The fibred presentation and the class index as in `join_own.py`
(`index_num`, B1446; 60 digits; the rank gaps reported). The split module S = A ⊕ 1 (rank 5).

- **The two orders.** W = [[A, c₁], [0, 1]] with c₁ a generator of Ext¹(1, A) = H¹(A) ("1 on top of A": A the submodule,
  1 the quotient) — B1453's W₁; and W′ = [[1, c₂], [0, A]] with c₂ a generator of Ext¹(A, 1) = H¹(A*) ("A on top of 1").
- **The mixed direction.** φ = c₁ + c₂ ∈ Z¹(Γ; End S), the first-order deformation of S carrying both classes.
- **The source.** The audit lane's potential along one extension line, V(t) = a t² + c t⁴ (a ≥ 0, c > 0 as R76 states;
  read as the lane's — if its numbers are in its report they are quoted, else a, c stay symbolic), with a source
  J·t: V_J(t) = a t² + c t⁴ − J t.

## 2. The computations, fixed now

- **C1 (the count is the order).** I(W), I(W′), I(S) at q₀ and q₀′; and at the controls.
- **C2 (the orders are dual up to the inversion).** W* and ι*W′ compared by an intertwiner (`conj_to`-style null space,
  rank 5): W* ≅ ι*W′, where ι is the inversion m ↦ m⁻¹, n ↦ n⁻¹ (B1455: ρ_q* ≅ ρ_q∘ι up to q ↔ 1/q; B1453's A* and the
  twist). Then I(W′) = I(ι*W′) = I(W*) = −I(W) by L1, L2 — the theorem behind C1.
- **C3 (binary or richer: the cup product).** H²(Γ; End S) by the presentation complex (one relator): the Fox map
  d¹: C¹ = End(S)² → C² = End(S), H² = End(S)/im d¹. The second-order obstruction of φ = c₁ + c₂: with
  ρ_ε(g) = ρ(g)(1 + ε φ_g), the ε²-coefficient of ρ_ε(R) is a 2-cochain; its class ob(φ) ∈ H². Also ob(c₁) and ob(c₂)
  alone (both must vanish: W and W′ exist). The cross term ob(c₁ + c₂) − ob(c₁) − ob(c₂) = [c₁ ∪ c₂ + c₂ ∪ c₁] projected
  to the diagonal blocks — read in the Hom(1,1) = ℂ block (H²(Γ; ℂ) = ℂ for one cusp) and the End(A) block. **Decides:
  if the class is non-zero, no flat module carries both orders to second order near S — the register at this point is
  binary; if zero, a mixed flat deformation may exist** (and the arc then follows it to the module and computes its
  index, as a follow-up C3b, not sealed in detail: Newton from the second-order solution).
- **C4 (the source).** For V_J(t) = a t² + c t⁴ − J t: the stationary points for J ≠ 0 (one real root, sign(t*) = sign(J),
  since dV/dt is monotone when a ≥ 0, c > 0), and the observation that t ↦ −t is an isomorphism of the module (the
  class c₁ ↦ −c₁ is the same extension), so **a source along one line does not choose between the orders; only a source
  with a component on each line does** — and then C3 says whether the two components can both be carried. Graded
  against THE_BAR: the card is written here. Population: the two orders at the point. Rule fixed before computing: the
  order with the component of J. Base rate: 1/2 under the census's own law. p = 1/2; grade **UNJUDGED-as-selection**
  — a source is an input (THE_BAR §grades; GENESIS GAP3). The grade is predicted; the arc states it as computed.
- **C5 (the internal source, posed, not computed).** Whether any object-defined quantity odd under the exchange of the
  two orders exists (a candidate list, each with its trap named — e.g. the sign of the Chern–Simons invariant on a
  chiral state, which is B347's numerology unless a coupling is derived). No claim is made; the list is the output.

## 3. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | I(W) = −1, I(W′) = +1, I(S) = 0 at q₀ and at q₀′; at the ±i points both orders count 0; at q = 2 h¹ = 0 and no order exists | 90% |
| P2 | W* ≅ ι*W′ (an invertible intertwiner, gap reported) | 85% |
| P3 | ob(c₁) = ob(c₂) = 0 in H² (the two orders exist, as computed in C1) | 97% |
| **P4** | **the cross term [c₁ ∪ c₂ + c₂ ∪ c₁] is non-zero in H²(Γ; ℂ): the register at the counted point is binary — no flat module near S carries both orders** | 60% |
| P5 | with a source on one extension line only, the stationary module is isomorphic for J and −J; a source must have a component on each line to choose, and C3 says whether it can | 90% |
| P6 | the bar grades the source's selection UNJUDGED/FITTED: a supplied input, not a derivation | 95% |

**What a failure would mean.** P4 false (cross term zero): a mixed module may exist; the arc follows it (C3b) and its
index becomes the question — "both at once" would then be a live possibility at this point, and the register richer
than a bit. P2 false: the two orders are not related by the symmetry and C1's opposite signs would need another
explanation. P1 false: L241's refinement 2 was wrong and B1453's count is not an order.

## 4. Disclosed

Known before the seal: I(W₁) = −1 (B1453, B1455, computed), I(W₁*) = +1 (B1455), ι*W₁ ≅ W₁(1/q₀) and τ*W₁ ≅ W₁ (B1455);
the exploratory "+1 for the other order" of L241's refinement 2 was computed once, unsealed, on 2026-10-02 by this seat,
by stacking in the other order at one q — it is the reason P1 is at 90% and not 60%. Not computed before the seal: W′ at
q₀′, any intertwiner for C2, any H² or cup product, any sourced stationary point. R76's a and c are not on main; if the
audit lane's report gives numbers they are quoted as read.

## 5. Scope

Frame F-HE for the vacuum language, F-CI for the index; object m004's Ballas family at its counted points, level one;
reach *single* (one object, two points) for C1–C4, with C2's theorem general to any point where the two Ext groups are
one-dimensional and A* ≅ ι*A. Nothing here is a count on a vacuum: W and W′ are not harmonic (B1455), and the source is
an input by construction. **The question the arc answers is whether the register at the counted point is a bit.**
