# R63 — TWO sl₂'s, ONE HOLONOMY: after B1274 the record holds the principal (I-19 EARNED, the B347–B353 θ-grading) and the subregular (B1257/B1274) as *the* embedding of the object's SL(2), and they cannot both be it

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 69a027eb** · **Status:** seat report, not banked; a flag for cc. Exact; script `computations/r63_sl2_adjoint.py`. Swept before writing: B1256, B1257, B1274 and the I-19 ledger row contain no mention of θ, F₄, B353, or the index-156 containment in connection with the subregular.

## 1. The two decompositions, from the root system

| | principal (2,2,2,2,2,2) | subregular (2,2,2,0,2,2) |
|---|---|---|
| 78 = | 23 + 17 + 15 + 11 + 9 + 3 | 17 + 15 + 11 + 11 + 9 + 7 + 5 + 3 |
| spin-2 summands (V₂) | **1** | **1** |
| trivial summands | 0 | 0 (distinguished) |
| 27 = | 17 + 9 + 1 | 13 + 9 + 5 |
| Dynkin index (adjoint route = 27 route) | **156** | **84** |
| dim H¹(m004; 𝔢₆∘φ) = number of nontrivial odd summands (MFP; each h¹ = 1 computed on this bench, R60) | **6** = rank E₆ (B347) | **8** |
| sl₂ ⊂ some F₄? (⇔ the 27 has a trivial summand) | **yes** (27 ⊃ 1; B351: θ commutes with it) | **no** (13+9+5 has no trivial summand) |

## 2. What follows

- **I-19 does not discriminate.** "E₆(ℂ) Chern–Simons contains 3d gravity as the spin-2 sector" holds at both points — there is exactly one V₂ in each — with coefficient 156 or 84. B1242 computed 156 *for the principal*; if the object's SL(2) sits subregularly, I-19's coefficient is 84 and its EARNED row needs its number changed.
- **The θ-grading is principal-only.** B351(vi) (θ commutes with the principal sl₂) and B353 (σ induces θ on the tangent space) both use that the principal sl₂ lies in the θ-fixed F₄. The subregular sl₂ lies in **no** F₄, so θ does not commute with it, and the six-line grading (−1)^{m+1} — the record's chirality dictionary at the tangent level — **has no counterpart at the subregular point without a new identification.** The manifold's involution σ still acts there (by conjugation with φ_sub(G), an inner element), and its signs on the eight SL(2)-lines are computable ((−1)^{m+1}: three odd, five even), but calling them θ-parities would be the same substitution I made in R58, one level up.
- **The tangent dimension differs.** Six at the principal point, eight at the subregular point. The E₆ character variety of m004 is not smooth of one dimension along "the object's" point unless one point is chosen.

> **B1274's collapse of I-25 to the subregular and the record's I-19/B347–B353 principal-based structure are in conflict. The object's holonomy embeds one way. Either (a) I-25 = principal, in which case B1257/B1274's 2T-selector picks a mathematical structure of E₆ that the object's holonomy does not realise — and the "three chiral summands" typing goes back to 1 + 2; or (b) I-25 = subregular, in which case I-19 is re-derived at 84, the θ-grading of B347–B353 is a statement about a *different* point of the character variety than the object's, and the record's tangent-level chirality dictionary must be rebuilt at the subregular point (8 lines, no F₄ split).**

## 3. Is there an object-intrinsic discriminator?

Not one I could find. Both embeddings are projective in B1112's sense; both give three θ-odd (σ-odd) classes in the 27 (R60); both contain one spin-2 sector; the Chern–Simons invariants are proportional (156 : 84 = 13 : 7). The two selectors in the record select by different criteria — Brieskorn's slice geometry (returns 2T) versus the 3d-gravity containment (assumes principal) — and both are identifications, not derivations from the holonomy. **The choice is therefore a row in the ledger, not a computation**, and until it is made the record carries two incompatible EARNED/PROVED items. That is the flag.

## 4. Verified / cited

| statement | status |
|---|---|
| both adjoint and 27 decompositions; V₂ and trivial counts; both indices by two routes | **computed, exact** (root system built here; agrees with B1256/B1242 where they overlap) |
| h¹(Sym^{2m}) = 1 for m = 1…8 on m004 | **computed** (R60, three primes) |
| 27 = 26 + 1 under F₄ ⊂ E₆; F₄ = 𝔢₆^θ | standard; B351's run on this bench (R60) exhibits 𝔣₄ = fixed algebra of θ, dim 52 |
| the subregular orbit is θ-stable (unique of dimension 70) | B1256's uniqueness over 30 labellings, cited; θ preserves orbit dimension |
| absence of the conflict in B1256/B1257/B1274 and the I-19 row | **swept** on main @ 69a027eb |
