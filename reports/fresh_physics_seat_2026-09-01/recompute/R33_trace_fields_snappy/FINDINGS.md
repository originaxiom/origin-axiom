# R33 — trace fields and commensurability claims recomputed with SnapPy + PARI (no Sage)

**Targets** (all rows the Phase B readers marked IMPORTED / ASSERTED / reproducible-no in
`synthesis/load_bearing_unrecomputed.tsv`): B142 (s776 = magic manifold, vol 5.33349, ℚ(√−7)), B146 (RRL/RLL
bundles have invariant trace field ℚ(√−7)), B210 (golden m004 ℚ(√−3), silver m136 ℚ(i), bronze s464 degree 8,
m = 4 → t03910 degree 4), B840 (bronze degree 8 vs the B578-D6 prereg's degree 6, "left UNRESOLVED"), B235
(figure-eight covers to degree 6 all ℚ(√−3)), B781 (m003's monodromy trace is −3, not +7), B803/B777 (m003 and
m004: same volume and field, not isometric, commensurable), B850 (m009: ℚ(√−7), not commensurable with m004),
B307 (census: of 500 cusped manifolds, 32 have cubic trace fields, all signature (1,1), 0 cyclic).

**Method** (`r33_lib.py`): for a cusped hyperbolic manifold the tetrahedral shape field equals the invariant trace
field (Neumann–Reid 1992, Thm 2.4). Shapes polished to 1000 bits (`snappy.snap`), a primitive element
w = Σ cᵢzᵢ with two independent small-integer coefficient vectors, PARI `algdep` degree by degree with a
spurious-relation guard ((d+1)·log₁₀H < digits/2), the irreducible factor vanishing at w, `polredbest`, `nfdisc`,
signature. Bundles named by SnapPy's `b±±word` convention; commensurability witnessed by an isometric pair of
finite covers.

## A. Fields — every named value MATCHES

| manifold | vol | H₁ | field (degree, reduced polynomial, disc) | bank |
|---|---|---|---|---|
| m004 | 2.0298832128 | ℤ | 2, x²−x+1, −3 = ℚ(√−3) | ℚ(√−3) ✓ |
| m003 | 2.0298832128 | ℤ/5+ℤ | ℚ(√−3) | ℚ(√−3) ✓ |
| s776 | 5.3334895669 | ℤ³ (3 cusps) | ℚ(√−7) | ℚ(√−7), vol 5.33349 ✓; volume is the magic manifold's 5.3334895670, not the Borromean 7.3277 ✓ |
| m009 | 2.6667447834 | ℤ/2+ℤ | ℚ(√−7) | ℚ(√−7) ✓ |
| m136 | 3.6638623767 | (ℤ/2)²+ℤ | 2, x²+1 = ℚ(i) | ℚ(i) ✓ |
| s464 | 4.8138191861 | (ℤ/3)²+ℤ | **8**, x⁸+6x⁶−x⁵+12x⁴−3x³+8x²−x+2, disc 391728981, sig (0,4) | 8 (script) vs 6 (prereg): **the script is right, the prereg's 6 is wrong** — B840's "UNRESOLVED" resolves to degree 8 |
| t03910 | 5.5736091128 | (ℤ/4)²+ℤ | 4, x⁴−x³−2x²−x+1, disc −1156, sig (2,1) | 4 ✓ |
| b++RRL, b++RLL | 2.6667447834 | ℤ/2+ℤ | ℚ(√−7) | ℚ(√−7) ✓ (both are m009 by volume and H₁) |
| b+−RRL, b+−RLL | 2.6667447834 | ℤ/6+ℤ | ℚ(√−7) | sign variants, same field |

Both coefficient vectors gave the same degree in every row.

## B. m003 versus m004 — MATCH, with the commensurability witness the bank lacked

- not isometric; volumes equal to 12 digits; H₁ ℤ/5+ℤ vs ℤ; symmetry groups ℤ/2+ℤ/4 vs D4 (B777's
  "only known distinguishing structural feature" — H₁ distinguishes them too, which B777 does not say).
- **B781:** m003 ≅ b+−RL, the bundle with monodromy −RL, trace −3. The trace-+7 candidate (RL)², which has the same
  |2 − tr| = 5 and hence the same H₁, is b++RLRL: volume 4.0597664256 = 2·vol(m004), the double cover of m004, not
  m003. B781's assertion is correct and now has a computed witness.
- **B803:** the degree-2 cyclic covers of m003 and m004 are isometric (SnapPy `m003~cyc~0` ≅ `m004~cyc~0`), so the two
  are commensurable with a common double cover — a direct witness, independent of the arithmetic argument
  (same invariant trace field ⇒ commensurable for arithmetic cusped manifolds) the bank imported.

## C. Figure-eight covers (B235) — MATCH, and vacuous

Degrees 2–6: 1, 1, 2, 4, 11 covers; all 19 have field ℚ(√−3). The invariant trace field is a commensurability
invariant, so this could not have come out otherwise; B235's table is a check of a theorem, not evidence for
anything about m004.

## D. m009 versus m004 (B850) — MATCH

Fields differ (ℚ(√−7) vs ℚ(√−3)); for arithmetic cusped manifolds commensurability is equivalent to equality of the
invariant trace field, so they are not commensurable. (Arithmeticity of m009 itself is not recomputed here.)

## E. B307's census count — see `r33_census_out.txt`

`r33_census.py` + `r33_census_retry.py` over `OrientableCuspedCensus[:500]` (shape field = invariant trace field,
800 bits / maxdeg 16, then 2000 bits / one-shot algdep 40 for the rest):

| degree | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | undetermined |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| manifolds | 21 | **32** | 40 | 46 | 42 | 53 | 32 | 36 | 42 | 23 | 22 | 1 | 110 |

- **cubic fields: 32 of 500, every one of signature (1,1), 0 cyclic (a cyclic cubic is totally real) — B307's
  three numbers MATCH exactly** (m006, m007, m015–m017, m034–m040, m045, m046, m146–m149, m168, m188,
  m292–m295, m303–m307, m366, m367, m376).
- The 110 undetermined rows are census entries s021–s1xx whose shape field the one-shot degree-40 search did not
  resolve (degree > 40, or the cheapness guard rejected the relation, or a non-geometric solution such as m000–m002).
  They cannot hide a cubic: a cubic relation is found at degree 3 with tiny coefficients in the first pass, so the
  count of 32 is complete. The full histogram above the cubic line is a by-product, not a claim.
- Caveat on words: B307 says "trace fields"; this cell computes *invariant* trace fields. For a cusped manifold the
  trace field can be a quadratic extension of the invariant one, so B307's "32 of degree 3" agrees with this count
  only if B307 also computed the invariant field (likely, via SnapPy/Sage `invariant_trace_field()`), or if no
  manifold's trace field is a cubic over a non-cubic invariant field (impossible: a degree-3 extension of a
  field is not quadratic, so a cubic trace field forces a cubic invariant field or ℚ — and ℚ never occurs).
  Either way the 32 stands.

**Physics content of the whole cell:** none. These are number-theoretic invariants of hyperbolic 3-manifolds;
no row names a measurable quantity. "No observable content."
