# B1186 — the family-definition cell CLOSED: |𝓕| = 112 (not 111), the criteria are nested, and the cell's own lesson applied recursively to its own count

**Status: banked (frontier). Verdict PROVED** (census- and bound-scoped counts, with the corrective
member exactly certified). Harvests cc3's **B8152** (their branch, bfcb7a1d) under
verify-don't-trust; the verification found and fixed a **one-member undercount**.
`verification/reproduce.sh` → `REPRODUCES` (fast path: committed enumeration + exact symbolic
certification; `OA_SLOW=1` re-runs the full 212,641-manifold sweep, ~3 min). Gate 5 clean.

## What cc3 established (B8152, verified here)

Within the hour of `THE_REMAINING_MATH.md` landing, cc3 ran its cell 2 — the definitional edge
their own retraction (B8147/B1180) left open. Verified on this bench by **independent full-census
enumeration** (own code, committed here — the artifact their arc lacked):

- **The two criteria are strictly nested**: (A) *all tetrahedra regular ideal* ⊊ (B) *tetrahedron
  shape field ⊆ ℚ(√−3)*. |A| = **77** (my count = theirs), A\B = ∅.
- **Paper IV's definition is (B)** — so the 14 it enumerated were of a 100+ family; 6 of the
  original 14 are non-regular, which is what should have exposed the conflation.
- The six 2√3i cusp-shape carriers match exactly: t12840, o9_41001, o9_41009, o10_150684/85/93 —
  the cusp-shape separator stays dead (six sharers), H₁=ℤ stays dead (o10_150700).

## The correction: |B| = 112, not 111

My enumeration returned **112** members (35 non-regular, not 34). The extra member is **t06829**
(7 tetrahedra, 2 cusps, volume exactly 3×Vol(m004)) — its shapes have **denominator 98**
(e.g. Re, Im/√3 ∈ ℚ with denominators up to 98), the largest in the family; every other member's
denominators are ≤ 49. A bounded-denominator test capped at 64 misses exactly it.

**Certification is exact, not numeric**: the ℚ(√−3) candidate shapes of t06829 solve the full
rectangular **gluing-equation system symbolically** (sympy over ℚ(√3, i); every row reduces to 0
identically), with member controls certifying and the non-member control m006 correctly excluded.
The identification of candidates is from 212-bit shapes at 1e-40 agreement; the certification of
the candidates is field arithmetic, no floats.

**The recursion of the lesson**: B8152's own headline — *two criteria that agree on a sample are
nested, and a bounded test is a different claim than its criterion* — applies to B8152's own count.
"111" was the count of *criterion B at cc3's implicit denominator bound*; **112 is the count at
bound 256, with the boundary member exactly certified**. Stated scope: census members
(`snappy.OrientableCuspedCensus`, 212,641), shape-denominator bound 256 (observed max 98 — the
next-largest 49 gives comfortable margin), NOT a claim about all hyperbolic 3-manifolds.

## Consequences (each verified in the committed run)

- **Amphichirality strengthens a third time: 112/112** (14/14 → 83/83 → 111/111 → 112/112), every
  member checked by mirror isometry in the committed sweep. B1163's no-sibling-escape again more
  robust.
- **The quine (B762/B1184) survives the full family**: zero collisions — no member other than m004
  is simultaneously 1-cusped, at m004's volume, with cusp shape 2√3i. (The two 1-cusped carriers
  o9_41001/o9_41009 sit at 4× volume; t06829 at 3× volume is 2-cusped.)
- **THE ONE-WAY FAMILY TEST fires a third time** (LAW_MAP §G): enlargement 111→112 again destroyed
  an object-level-style claim (the count itself) and reinforced every family-level one
  (amphichirality, nestedness, separator failures).
- **B1180's "≥83" floor** is superseded by the definitional close: the family, per Paper IV's own
  criterion (B), is 112 at census scope.

## Routes

- Reply relay to cc3: verification + the t06829 correction + the exact certificate (theirs to
  adopt in Paper IV — count → 112 **with the bound stated**, per their own B8151 method).
- `THE_REMAINING_MATH.md` row 2 → DONE (this arc).
- The member list + sweep script are committed here (`verification/family_census.{py,json}`) —
  the dual-homed artifact B8152 lacked (their single-homed-content debt class, discharged on main).

## Fences

Counts are census- and bound-scoped, stated in-claim. The double-precision scan (tol 1e-9,
den ≤ 256) could in principle miss a member whose shapes need denominator > 256 — no such member is
suggested by the observed denominator spectrum (max 98), but the bound is part of the claim. My own
first verifier had a **double-cast precision bug** (212-bit values collapsed to double, then judged
at 1e-25 — it wrongly rejected o9_41001) — caught in-cell by chasing the disagreement with cc3's
carrier list before trusting my own tool; narrated per MB12 practice. Amphichirality checks use
SnapPy `is_isometric_to` (canonical-cell based; standard). No firewall crossing; no measured value.
