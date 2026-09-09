# B1351 — THE INDEX ON A THREE-MANIFOLD: the chiral count of M-theory's local model on a 3-manifold is an Euler characteristic that vanishes on every closed closing and, on the cusped object, can be non-zero only on a cusp-fixed weight with a disc-type partition — "vector-like everywhere" as a theorem in the seven-dimensional frame, with its single escape named

**Date:** 2026-09-09 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (a statement assembled from the literature's index
formula and the record's own bound, with its closed-manifold half checked character by character on the tower) · **Price:
unchanged** · main's fresh-eyes Q9 ("what does Pantev–Wijnholt state for a 3-manifold with boundary?"), answered.

## 1. The frame

M-theory on a G₂ manifold with an ADE singularity along a 3-manifold Q is, locally, 7d super-Yang–Mills on Q, twisted: a
flat connection A and an adjoint-valued 1-form Higgs field φ (Pantev–Wijnholt 2009; Braun–Cizel–Hübner–Schäfer-Nameki
2018). For a Cartan-valued φ = df, the zero modes of a sector of charge q are the Morse cohomology of q·f, and the **net**
chiral count of that sector is a relative Euler characteristic,

    N_q = χ(M, ∂⁺M; L_q) = χ(M; L_q) − χ(∂⁺M; L_q),

∂⁺M the part of the boundary on which q·f increases outward, L_q the flat line bundle of the sector (PW 3.39–3.40).

## 2. The statement

**(i) Closed Q.** χ(Q; L) = 0 for every local system on a closed odd-dimensional manifold, so N_q = 0 in every charged sector
of every abelian Higgs configuration; and every Wilson-line vacuum on the tower's closings (Y₃ … Y₂₄, B1278–B1304) is
vector-like **exactly**: h¹(Y_n; ψ) = h¹(Y_n; ψ̄) for every character ψ — Poincaré duality with h⁰ = h³ = 0 — so each weight
of the 27 is paired with its mirror weight in the 27̄. (`verification/pairs_on_the_closings.py`: every character of every
level ≤ 9, 9 321 characters, two primes, all paired.) The identification I-26 (h¹ ↔ generations) counts vector-like pairs on a
closed closing; no chiral generation can come from a Wilson line on a closed 3-manifold. This is BCHS §2.4's vanishing,
stated for the record's own objects.

**(ii) The cusped object.** χ(M; L) = 0 for the cusped manifold too, so N_q = −χ(∂⁺M; L_q). On the torus boundary, a
sector's boundary term is decided by the twisted cohomology of the torus: **if the cusp holonomy is non-trivial on the
weight, H*(T²; L_q) = 0, no boundary condition is left to choose, and N_q = 0 whatever the Morse function does.** Only a
**cusp-fixed weight** (holonomy trivial on it, one of the h⁰(∂M; V) of B1268) carries the choice, and there N_q = −χ(∂⁺_q),
which is 0 for an annular or empty or full ∂⁺ and ±1 for a disc. Hence

    −h⁰(∂M; V) ≤ N(V) ≤ h⁰(∂M; V*)      (B1268's bound, in the seven-dimensional frame),

with equality only if every fixed weight's partition is a disc of the same sign.

**(iii) What the record has computed, placed.** At the subregular point ρ₀ the 27 has three cusp-fixed weights (one per
block 13 ⊕ 9 ⊕ 5). Along every ι-odd direction the region-swap theorem (fc R71, B1281 §2D) makes each partition annular:
N = 0. Along the one ι-even direction, the V₁₀ of the 42, the generic deformed point has **no** cusp-fixed weight (B1350:
h⁰(∂M; 27) = h⁰(∂M; 27̄) = 0), so N = 0 with nothing to choose. **The single remaining escape on the object is therefore
exact:** a point on the V₁₀ direction's fixed-vector locus (μv = v, λv = v kept along the deformation), where one weight
is cusp-fixed, the field is ι-even so the region-swap theorem is silent, and the leading cusp mode of that weight cuts the
torus into discs. That locus is B1352's computation; B1268's stage (b) (the same locus along V₈) was begun and never
reached, and is completed there as the control. *(Currency 2026-09-09: B1352 done — the locus reached from every V₁₀ point is the Sp(8) family, self-dual with N = 0; exactly, the cusp-fixed vectors and self-duality are lost together at order 4 along V₁₀; the escape is void on every computed deformation.)*

## 3. What this settles

"Vector-like everywhere" is no longer an experience of computed cases. On the closings it is Poincaré duality; on the object
it is the vanishing of the torus cohomology on every weight the cusp holonomy moves. What is left for chirality on the object
is one locus, named and now being computed; what is left beyond the object is the codimension-7 enhancement point (O4,
B1353) and the non-abelian Higgs data the literature analyses only locally.

## Verification

- `verification/pairs_on_the_closings.py` (the closed-manifold half, every character of every level ≤ 9; `pairs_on_the_closings_run.txt`).
- Lock `tests/test_b1351_the_index_on_a_three_manifold.py` (fast: levels ≤ 7).
- Depends on B1268 (the bound), B1280/B1281 (the region-swap theorem), B1350 (the V₁₀ points), B1303 (the criterion);
  PW 2009 eq. 3.39–3.40 and BCHS 2018 §2.4 as cited in `docs/LITERATURE_SWEEP_2026-09-06_higgs_bundles_and_the_destination.md`.
