# B1011 PREREGISTRATION — the McKay⊗McKay factorization of the hearing data (chat1's derivation, exactified; sealed before compute)

**Date sealed:** 2026-08-10 · **Seat:** cc (verification) · **Source:** an incoming chat1
derivation (verify-don't-trust: framing quarantined, mathematics re-derived here in exact
arithmetic before anything banks). **Gate 5-Q.** Nothing to `CLAIMS.md`.

## The claim under test (chat1's, stated exactly)

On B593's two-sided instrument — R = T, L = S⁻¹T⁻¹S acting on SU(3)₂'s six primaries — the
generated group and its representation factorize as:

> **ρ₆ ≅ (χ ⊗ V₂(2I)) ⊕ (V₂(2T) ⊗ V₂(2I))** as a 2T×2I representation, the θ-eigenspaces being
> exactly the two summands (odd = the 2-dim, even = the 4-dim), so that **the object's hearing
> data is (E₆ McKay character) ⊗ (E₈ McKay spin) ⊕ (E₆ McKay spin) ⊗ (E₈ McKay spin)** and every
> forced coupling is a **product of a character value and a trace**. In particular **B856's
> period-5 law is DERIVED** (the tones = Re χ(A) · ½tr B on the odd side), and a **second law on
> the θ-even mirror** exists that B593's chiral observable could not see, by theorem.

## The exactification bar (chat1's own, adopted as binding)

The incoming verification is machine-precision (1.6e-14) on statements that are integer- or
exact-algebraic valued. **This cell rebuilds S and T from cyclotomic closed forms (sympy, exact
roots of unity) so that every "1.000000000000" becomes "1" — or visibly fails to.** No floating
comparison enters any verdict line.

## The cells, each two-outcome

1. **C1 — the group.** Compute ⟨R, L⟩ exactly. SEALED EXPECTATION: a finite group compatible with
   a 2T×2I product structure (order 2880 up to a stated central identification, which C1 must
   name exactly if present). FAIL = the group is not of this form; then chat1's Steps 1–4 have no
   stage and the claim dies here.
2. **C2 — the isotypic splitting.** The θ-involution's ±1 eigenspaces (dim 2 odd, dim 4 even) are
   exactly the two isotypic components of ρ₆. FAIL = any isotypic component straddles the
   eigenspaces.
3. **C3 — the four exclusion/linearity steps, exactly:** (a) χ multiplicative on all pairs
   (2T-side linearity); (b) 2T has no 4-dim irrep (character table, exact); (c) 2T does not act
   by scalars on the even space; (d) the character identity tr₆(AB) = [χ(A) + tr_{2T}(A)]·tr_{2I}(B)
   on **every** group element, exactly.
4. **C4 — the trace sets.** tr_{2T} ∈ {−2,−1,0,1,2} and tr_{2I} ∈ {−2,−φ,−1,−1/φ,0,1/φ,1,φ,2}
   **as exact algebraic numbers** (φ entering only via 2cos(π/5), 2cos(2π/5)).
5. **C5 — the derivation of B856.** The forced-coupling laws — θ-odd forced ⟺ A ∈ ker χ or
   B ∈ Z(2I), value Re χ(A)·½tr B; θ-even forced ⟺ A ∈ Z(2T) or B ∈ Z(2I), value ½tr A·½tr B —
   with counts by inclusion–exclusion matching exact enumeration (incoming: 992 and 284; the
   counts are RE-DERIVED here, not assumed). Then: **B856's banked tone set {0, 1/(2φ), 1/2,
   φ/2, 1} and h(5) = −1 recovered as special cases, exactly.**
6. **C6 — the mirror law (the genuinely new content).** State the θ-even law's value set exactly.
   Two-outcome: it is a NEW banked-law candidate (differs from the odd side's) or it collapses to
   known content; either way it is recorded with its exact values.

## Declared prior (honest)

**OUTCOME A expected** — the incoming numerics are tight (1e-14 on algebraic-valued statements)
and the structure is representation-theoretically natural. The risk concentrates in C1 (the exact
group identification, where central extensions/quotients could differ from the clean 2T×2I) and
in exactification surprises. A FAIL at any cell is reported at that cell with the discrepancy
shown; no post-hoc weakening (the non-weakening clause applies to this document).

## Scope, stated before compute

A result about **the object's hearing instrument** (B593's welded representation on SU(3)₂ modular
data) — the E₆/E₈ McKay language is about the **two ends' McKay groups** (B248/B261 context), and
**no SM quantity is involved anywhere**. If C5 lands, B856's law changes grade from observed to
derived and L150 gains a concrete closed form for the coupling side. **Nothing here is a
crossing**; if a value-facing use ever follows, it goes through `CROSSING_REQUIREMENTS.md` in
full. Relation to the u†Mu chain (B592/B593/B641/B654/B856) cited throughout; this cell exists
because B1010 restored that chain to the synthesis layer.
