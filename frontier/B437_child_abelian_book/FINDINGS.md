# B437 — C2: the child's abelian torsion book — the "golden return" [RETRACTED AS INHERITANCE, see §CORRECTION] + the Lucas-square law

**Status: banked (C2), then CORRECTED (#562). The "golden return" is NUMERATOR-FORCED, not
inheritance (trefoil control below). What survives: the Lucas-square law and the parent's
Alexander data displayed through a channel every knot shares. Firewalled.**

- **The golden return.** The child's abelian torsion (surgery formula from the parent's
  Alexander polynomial t²−3t+1 = (t−φ²)(t−φ⁻²)) traced to the real subfield:
  **Tr τ = 3 + √5/5 ∈ ℚ(√5)** — and ℚ(√5) IS the real subfield of ℚ(ζ₅), the child's abelian
  character field. The loop closes exactly: parent golden → forced slope 5 → H₁ = ℤ/5 →
  characters in ζ₅ → **the child's abelian floor speaks the parent's golden language.**
- **The Lucas-square law.** Total abelian torsion = |2−L₂ₚ| = **Lₚ²** (classical L₂ₙ = Lₙ²+2,
  odd n): child → L₅² = 121 = 11²; sibling (7) → L₇² = 841 = 29². (= |H₁| of the parent's
  p-fold cyclic branched cover.)
- **The control dichotomy (bar leg iv, exact) — corrected by B438.** What is family-generic is
  the FORMULA total abelian torsion = |Res(Φₚ, Δ_K)|; the VALUE Lₚ² = 121 is Δ_K-specific
  (trefoil → 1). It is NOT even figure-eight-unique: **5₂(5,1) also gives 121** (B438), because
  {4₁, 5₂} share the −283 trace field — a commensurability class. So the value records the
  parent's own Alexander data through a channel every knot shares, and the "special" −283 exit
  is a class property, not a fingerprint. (Original over-claim "the Lucas-square law is
  FAMILY-GENERIC" retracted: the law-as-formula is generic, its value is knot-specific but
  class-shared — see [[B438]].)
- The child's torsion prime 11 lies in the parent's Fibonacci apparition set (B423) — noted,
  not interpreted.

**Bar note:** forced ✓ (surgery formula, no choices), unsought ✓ (registered two-outcome),
exact-SM ✗ (golden/Lucas arithmetic — named mathematics), control ✓. Named positive
mathematics; no physics promotion.

**Provenance.** abelian_book.py → abelian_book.json; lock tests/test_b437_abelian_book.py.
Cross-refs: B435 (ℤ/5), B434 (slope), B423 (apparition set), B425 (Alexander machinery).

## CORRECTION (2026-07-05, Chat-2 adjudication — the trefoil control): the field-return is NUMERATOR-FORCED, not inheritance

Chat-2's catch is correct and verified here: the missing control was the SAME slope on a
DIFFERENT parent. **Trefoil(5,1): trace = 1 − √5/5 — the SAME field ℚ(√5)** (different value).
Every knot filled at slope 5 has ℤ/5 → ζ₅ → √5: the field is a theorem about the integer 5
(ℚ(√5) = ℚ(ζ₅)⁺), not the parent's memory. My slope-7 control tested slope-specificity only;
an inheritance claim needs knot-specificity too. **"The golden return" is retracted as an
inheritance claim.** What remains parent-specific in C2: the torsion VALUES carry the parent's
Alexander data (Δ₄₁ = (t−φ²)(t−φ⁻²), golden roots — the trefoil's are 6th roots of unity),
i.e. "the parent's data displayed in the numerator's forced field" — not a return.

**THE INVERSION LAW (Chat-2's articulation, now three-instance verified — banked as the
campaign's sharpest structural finding):** *every inherited-looking feature of the child is
forced-for-all-knots (ℤ/5, ζ₅/√5, the 26 abelian vacua, the Lucas-square law), and every
figure-eight-specific feature is parent-disjoint (the arithmetic quartic −283, S₄, no
quadratic subfield).* Where the child echoes the parent, it is generic; where it is special,
it is foreign. The trefoil control cannot even be posed for the geometric claims (trefoil is
not hyperbolic): the shared part is homological, the special part geometric — consistent.

**FURTHER SHARPENED BY B438 (2026-07-05 audit — the missing FOREIGN control):** C1's
arithmeticity does NOT survive as "the genuinely special, figure-eight-specific fact." The
−283 field is **shared with 5₂(5,1)** (a hyperbolic knot foreign to the parent), so it is a
**commensurability-class** property, not a figure-eight fingerprint. The Inversion Law becomes
**three tiers**: (1) numerator-forced = every knot at slope 5 (ℤ/5, √5, the 26 vacua); (2)
commensurability-shared = 4₁≈5₂ (the −283 field, the 121 value); (3) figure-eight-UNIQUE =
**none found**. The break criterion is raised accordingly: a genuine inheritance break must
distinguish 4₁ from **5₂** (its commensurability neighbor), not merely from the trefoil or a
generic knot — so C3's interior→exit control set now includes 5₂. See [[B438]].

B435 bookkeeping correction (same adjudication): 75 gcd-1 Kac solutions = order-exactly-5
classes only; full Hom(ℤ/5,E₆)/conj = **25 + 1 trivial = 26** (78 raw vectors incl. the 3
identity representatives). Locks updated.
