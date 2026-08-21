# B1104 — THE 4D SUSPENSION SELECTION TEST (L177: "the dimension we lack") — PREREGISTRATION

**Sealed before computation, 2026-08-21. Owner-elected ("go to the end with L177").
The question, one line: does the object's own structure name a canonical fourth
dimension — a preferred suspension M ×_ψ S¹ over the free choice of ψ — or is the
choice a torsor one level up?**

## Ground (banked)

- The object M = m004 is itself a suspension: the punctured torus swept by the
  INFINITE-ORDER Anosov act φ = RL (the level-down genesis).
- MCG(M) ≅ Isom(M) for hyperbolic M (Mostow, CITED-grade); Isom(m004) = D₄, order 8.
- B716: a 4d filling EXISTS and is infinitely non-unique on the FILLING route; B770
  registers wall #4 (the chiral 4d lift). This cell attacks the SUSPENSION route —
  adjacent to both, colliding with neither (declared).
- B1083: the tick (det = −1), the double tick = the orientable object; Gieseking =
  one tick. The candidate 4d analog is typed there.

## Operations (MB12: non-trivial, each can genuinely not-work)

1. Enumerate all 8 isometries: orientation character on M, induced matrix on cusp
   H₁(T²) = ℤ², order, conjugacy class in D₄.
2. **The escalator-type test**: is the level-down act's TYPE (infinite-order
   monodromy) available at 4d via mapping tori of M?
3. Suspension invariants per ψ: H₁(M_ψ) = ℤ ⊕ coker(ψ★ − I on H₁(M) = ℤ);
   orientability of the total space; the cusp's flat 3-manifold type (the mapping
   torus of T² under the cusp matrix, classified by GL(2,ℤ)-conjugacy).
4. **The selection test**: apply the object's own banked filters in order — (a)
   θ-compatibility (centralizing the amphichiral structure: the center of D₄); (b)
   the tick analog (orientation-reversing involutions: the Gieseking pattern one
   level up); (c) nontriviality. Count what survives each filter and jointly.

## Sealed criteria (each can pass AND fail — vacuity-checked)

- **C1 ESCALATOR-REPEAT**: PASS iff MCG(M) contains an infinite-order element (the
  level-down act's type repeats). Non-vacuous across the family: for a NON-hyperbolic
  fiber (e.g. T³) the criterion passes; for hyperbolic M rigidity decides — the
  computation states which and the consequence either way.
- **C2 SELECTION**, three-valued, typed in advance:
  - UNIQUE-NONTRIVIAL: exactly one nontrivial conjugacy class survives all object
    filters → the object names its fourth dimension; the layer-up picture gains a
    construction.
  - ONLY-TRIVIAL: only the identity survives → the canonical suspension is M × S¹
    (no new act; the "one more layer" adds nothing the object didn't have).
  - NO-SECTION: several classes survive with nothing to split them → the choice is
    free; Class V (torsor no-sections) acquires its 4d instance; "the dimension we
    lack is the choice we are" becomes a THEOREM-SHAPED statement one level up.
- **C3 GIESEKING-ANALOG**: PASS iff an orientation-reversing INVOLUTION exists
  (non-orientable M_ψ, orientation double cover M × S¹ — the one-tick/double-tick
  pattern verbatim one level up). Can fail: D₄'s reflections could all act
  orientation-preservingly on M (the computation decides).

## Outcome grammar

Every C2 branch banks. No physics claim on any branch; the filling-route (B716) and
wall #4 (B770) stand untouched; Gate 5 untouched. `creates_law` will be declared per
whether the outcome is theorem-grade typing (expected: yes on any branch — the
finiteness statement alone is one).

## Method

SnapPy (canonical pyenv env) for the isometry group and cusp actions; exact integer
linear algebra for everything downstream; every matrix stated in the FINDINGS; an
independent re-derivation of the selection table by hand-checkable enumeration (8
elements — small enough to print in full).
