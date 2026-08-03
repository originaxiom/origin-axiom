# THE FIRST MEASUREMENT THEOREM
*(Solo seat, 2026-08-03. SOLO-TIER, UNBANKED; prepared to banking grade for S1
review. Every clause EXACT; per-clause method and certificate listed in §3.
Nothing herein depends on floating point. Physics reading fenced in §5.)*

## 1. Setting

𝔢₆ over ℚ in the Chevalley basis of B854 (verified there: Jacobi on 4000
triples, exponents recovered). 𝔷 := z(2T) = the object's superselection torus —
abelian by B854 (exact), toral by the fixed-point-reductivity theorem [I1].
Distinguished generators g₈, g₁₆ ∈ 𝔷 (the chirality-switch slots) and the
"switch plane" Π = span(g₈, g₁₆) ⊂ 𝔷. Write μ(ρ) =
500716339200ρ³ − 2075673600ρ² − 4769856ρ + 2197 (irreducible /ℚ; Galois S₃;
disc = 2³²·3¹⁰·5²·7³·11·13¹²; constant 13³), with three real roots ρ₁,ρ₂,ρ₃,
and x_i := g₈ + ρ_i g₁₆.

## 2. Statement

**(A) The three charges.** dim z_{𝔢₆}(x) = 12 for generic x ∈ 𝔷; = 30 for
generic x ∈ Π; and = 46 exactly when x is proportional to some x_i. The
enhancement locus in Π is precisely the three lines ℝx_i — one irreducible
S₃-Galois orbit.

**(B) Types.** z_{𝔢₆}(Π) = 𝔰𝔬(8) ⊕ 𝔲(1)² (the triality core, "core").
K_i := z_{𝔢₆}(x_i) = 𝔰𝔬(10) ⊕ 𝔲(1). K_i ∩ K_j = core for i ≠ j;
K₁ + K₂ + K₃ = 𝔢₆.

**(C) The tiling.** V_i := ad(x_j)(K_i) (any j ≠ i; the choice is immaterial)
satisfies dim V_i = 16, V_i ∩ core = 0, and
        𝔢₆ = core ⊕ V₁ ⊕ V₂ ⊕ V₃,   K_i = core ⊕ V_i.

**(D) The multiplication law.**
        [V_i, V_i] ⊆ core,      [V_i, V_j] = V_k   ({i,j,k} = {1,2,3}).

**(E) Corollary (matter = the foreign sectors).** The ad-K_i-module
𝔢₆/K_i ≅ V_j ⊕ V_k is the 16 ⊕ 16̄ of 𝔰𝔬(10) ⊕ 𝔲(1); the generation pair of
each first-breaking choice consists exactly of the two sectors not gauged.

## 3. Proof map (clause → method → certificate)

A-generic-12: exact common-kernel rank over ℚ (DomainMatrix) — B854-arc, dim 12.
A-plane-30 & B-core-type: exact nullspace of ad(g₈+g₁₆) over ℚ (dim 30) + exact
  derived rank 28 ⟹ 𝔰𝔬(8)⊕𝔲(1)² (unique rank-4 dim-28 semisimple) — levi2.py.
A-three-lines & dim 46: THE PENCIL THEOREM — det₃₆(ρ) = c·μ¹², det₁₂(ρ) = c·μ⁴,
  exact polynomial division (levi6.py); semisimplicity converts vanishing order
  to nullity; block-18 lies in core identically (its charges vanish on Π: exact
  ℚ-block structure, levi_exact/levi3). INDEPENDENT second proof of the
  per-root nullities (4 and 12): restriction-of-scalars over ℚ[ρ]/μ — the
  companion-blown matrices have exact ℚ-nullities 12 and 36 (fmt_phase2b.py).
  Genericity off the lines: μ-coprimality of the co-factors (the division is
  exact with unit quotient).
B-type-of-K_i: squeeze — derived ≥ 45 (rank_{𝔽_p} ≤ rank_ℚ at p = 40009,
  40037; levi7.py), center ≥ 1 (x_i ∈ Z(K_i)), dim = 46 exact, centralizers of
  semisimple elements are reductive [I2] ⟹ derived = 45, center = 1; D₅ is the
  unique rank-5 dim-45 semisimple algebra [I3] ⟹ 𝔰𝔬(10) ⊕ 𝔲(1). EXACT.
B-intersections: K_i ∩ K_j = z(span(x_i,x_j)) = z(Π) = core (ρ_i ≠ ρ_j so the
  span is Π). EXACT by identity, no computation.
B-span: ≥ 78 (mod-p, levi8), ≤ 78 trivially. EXACT.
C: dim V_i = 46 − dim ker(ad x_j|K_i) = 46 − 30 = 16 (rank–nullity; ad x_j
  preserves K_i since [x_i,x_j] = 0, kills exactly K_i ∩ K_j); V_i ∩ core = 0
  and j-independence: ad x_j is semisimple and invertible on the complement
  (image = the Π-charged part of K_i, canonically). Direct sum by dimensions
  with B-span. EXACT.
D-cyclic: WEIGHT-LINE LEMMA — under Π, 𝔢₆'s nonzero-weight space has dim 48;
  the weights annihilated by x_i total 16 for each i (clause A); 16·3 = 48 ⟹
  every nonzero weight lies on one of the three annihilator lines ⟹
  [V_i,V_j] (weights = line_i + line_j sums, which avoid 0 and the other
  lines' complements) lands in V_k's weights only ⟹ ⊆ V_k A PRIORI; dim ≥ 16
  (mod-p at 40123/40493/40583, levi9/levi10) ⟹ = V_k. EXACT.
D-abelian-part: [V_i,V_i] has weights on line_i ⟹ ⊆ core ⊕ V_i a priori; the
  V_i-component vanishes ⟺ the 16-element charge multiset of V_i is sum-free
  (no a+b = c with c ≠ 0 in the multiset). Sum-freeness holds EXACTLY by the
  ONE-PRIME LEMMA [I4]: a nonzero value of a+b−c over ℚ̄ reduces to a nonzero
  value modulo any prime of good reduction; the combined (cross-block!)
  multisets are sum-free at all 3 roots of BOTH primes 40123 and 40493
  (fmt_combined.py), so no identity exists. EXACT.
E: 𝔢₆/K_i = V_j ⊕ V_k by (C); its K_i-module type 16 ⊕ 16̄ is the standard
  branching of the E₆-adjoint under D₅ ⊕ 𝔲(1) [I5], pinned to our K_i by the
  type in (B).

## 4. Imports, pinned

I1 Fixed subalgebras of finite automorphism groups of reductive Lie algebras
   are reductive (standard; used once, for torality of 𝔷).
I2 Centralizers of semisimple elements are reductive (standard).
I3 Classification table: the only semisimple Lie algebra of rank 5, dim 45 is
   D₅; of rank 4, dim 28 is D₄ (finite check against the Cartan list).
I4 One-prime lemma (elementary, proof one line): if α ∈ ℚ̄ satisfies α ≠ 0,
   then for any prime q of good reduction ᾱ ≠ 0 is possible and any single
   witness q with ᾱ ≠ 0 proves α ≠ 0; contrapositive used: absence of the
   identity at one good prime ⟹ absence over ℚ̄. (Reduction well-defined via
   the exact charpolys of the restricted operators.)
I5 E₆ ⊃ D₅ ⊕ 𝔲(1) branching: 78 = 45 + 1 + 16 + 16̄ (standard tables).

## 5. Reading (fenced) and feeds

Framework reading: symmetry breaking = superselection-charge measurement; the
first step of the world's cascade is the centralizer of any one of exactly
three conjugate distinguished charges; the unmeasured sectors become the
matter. The "3" of the triple is the "3" of triality, object-selected;
individually the three are Galois-unlabelable (no-pick, Inversion-Law-shaped).
NOT claimed: that the triple is the generation mechanism (candidate, O3 lane;
decisive test = the Descent under B861's chain). Feeds: convergence with
B861's step-1 (two independent derivations of SO(10)×U(1)); the criterion
status ladder as in JOINT_NOTE_CC §3; the held Stage-2 shot (owner-gated).

## 6. Reproducer manifest

levi_exact.py/levi3.py (ℚ-block structure) · levi2.py (core type) ·
levi6.py (pencil theorem) · levi7.py (Galois S₃ + typing primes) ·
levi9.py/levi10.py (canonical sectors, law, three-prime belt) ·
fmt_phase2b.py (restriction-of-scalars nullities + per-block spectra) ·
fmt_combined.py (combined sum-freeness, the closing certificate) ·
seal_e12.txt (the seal that killed the spurious charge rationals — §XI of the
ledger; the exact e-invariants remain queued and are NOT used anywhere above).
