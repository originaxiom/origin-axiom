# B936 — THE COHOMOLOGY READING: the classification IS an H¹ story; the value layer is exactly what that H¹ cannot see

**Date:** 2026-08-06 · **Seat:** computation agent (for cc banking) ·
**Prereg:** `PREREGISTRATION.md`, sha-256 `2808c8a7…`, sealed BEFORE the first
run; followed verbatim, including its stop condition.
**Instrument:** `cohom.py` → `results.json` — 92 entries: **70 consistency
checks, ALL PASS**, 21 recorded data blocks, and **one sealed two-outcome
criterion, which FAILED** (that failure is the cell's sharpest result).
Runtime 4.8 s after the frame cache. Exact arithmetic throughout; every
Hermitian structure re-solved in-cell from its own invariance equation; no
Rayleigh readouts; no determinant divided by before being checked nonzero;
no measured number touched.

---

## THE HEADLINE

> **The classification is exactly an H¹ story — and the value layer is exactly
> the part of it that H¹ cannot see.**
>
> The sixteen Hermitian structures are the 1-cocycles Z¹(⟨τ⟩, T_ad[2]); the
> true classes are H¹(⟨τ⟩, T_ad[2]) = (ℤ/2)², four classes of four. **D₂ — the
> diagonal that carries the entire generation hierarchy — is a COBOUNDARY**
> (class 0, with an exhibited witness), while **D, the wall twist, carries the
> nonzero class** and is *invisible to the colorless register*. The sealed
> value corollary — that the twist-norm law is the discriminant invariant of
> the pair of forms — is **REFUTED exactly**: the pair-invariants of (H₊, H′)
> on the canonical register blocks are −17/384, +17/384, 1 and −1, with **no
> 953, no 2304, and not even the value field K**.

---

## Q-A — the group, the module, the torsor (all criteria PASS)

**C-A1 PASS.** The 128-census closes as a group, verified on **all 16 384
products** at generator-map level, and it is exactly

> **G = X ⋊ ⟨τ⟩, |G| = 128, with X = Hom(Q, μ₂) = T_ad[2] ≅ (ℤ/2)⁶** and τ
> acting by the E6 diagram flip.

All 128 members are automorphisms (full 78² bracket check each). A bonus fact
fell out of the τ-cocycle re-solve: the F₂ system has rank 66 of 72, so its
solution set has **exactly 64 members — the outer coset IS a torsor of the
cocycle equation under X**. That is why the census is 128 and not something
else.

**The module.** As a ⟨τ⟩-module, X = ℤ/2[⟨τ⟩] (nodes 0,5) ⊕ ℤ/2[⟨τ⟩] (nodes
2,4) ⊕ trivial (node 1) ⊕ trivial (node 3). Hence, computed here by exact F₂
linear algebra:

- **Z¹(⟨τ⟩, X) = X^τ**, 16 elements — and (σ_χτ)² = σ_{χ·τ(χ)} means the
  outer involutions ARE the 1-cocycles, verified elementwise;
- **B¹ = (1+τ)X = N(X)**, 4 elements, vanishing identically at the two
  τ-**fixed** nodes;
- **H¹(⟨τ⟩, X) = (ℤ/2)²** — one ℤ/2 per τ-fixed Dynkin node (Bourbaki α₂ and
  α₄); the class of χ ∈ X^τ is literally its pair of coordinates there.

In the textbook language: **the sixteen outer involutions are the complements
to X in G, and their X-conjugacy classes are H¹(⟨τ⟩, X).**

**C-A2 PASS.** The sixteen invariant Hermitian structures are **a torsor
(principal homogeneous space) under X^τ**: sixteen distinct structures, the
action H ↦ H·ρ₂₇(σ_ν) free and transitive, base point H₊, and the coordinate
of H(σ_χ∘τ) is χ·χ₊ (B928's torsor theorem, re-derived here in the intrinsic
normalization).

## Q-A2 — the lift obstruction is ZERO; B928's "affine polarity" is a gauge

**C-A3 PASS.** det(C) = 3 is odd, so Hom(P, μ₂) → Hom(Q, μ₂) is an isomorphism
and every character has a *unique* extension to the weight lattice. Defining
R(χ)[b] := χ̂(w_b) gives an intertwiner (verified against all 78 generators for
all 64 characters) which is an **honest homomorphism** X → Diag_{±1}(27),
checked on all 4096 pairs. So the class in **H²(X, μ₂) is zero** — there is no
projective obstruction.

Consequently B928's "shifted/affine character" is *not* a class:

> **T_χ (the entry-0 = +1 normalization) = ε(χ)·R(χ) with ε(χ) = χ̂(w₀)**, and
> ε is itself a character — a coboundary. The global −1 in
> D₂ = −(−1)^⟨s(χ₋),w⟩ is exactly **ε(χ₋) = −1**, the value of the second wall
> character at the base weight. B928's affine shift is a normalization gauge.

The other B928 curiosity is also explained: a\* = s(χ₋) holds because
**s(χ₋) is a fixed vector of the mod-2 Dynkin adjacency matrix** (A s = s) —
a diagram coincidence, verified, not a structural identity.

## Q-B — where the two Klein generators live (C-B PASS, both outcomes reported)

| twist | torsor coordinate | H¹ class | coboundary? | acts on the colorless register |
|---|---|---|---|---|
| I | 1 | (0,0) | — | trivially |
| **D₂** | χ₋ | **(0,0)** | **YES** | **nontrivially (7 of its 11 flips)** |
| **D** | −1 (global negation) | **(1,1)** | **NO** | **trivially (all 12 flips colored)** |
| D₂D | χ₊ | (1,1) | no | nontrivially |

- **[D₂] = 0**, with 16 witnesses ψ satisfying N(ψ) = χ₋. One is exhibited:
  **ψ₀ with signs (1,1,1,1,−1,−1)**, and both witness identities are verified
  exactly, not inferred:
  - **σ_{ψ₀} φ₊ σ_{ψ₀}⁻¹ = φ\*** at generator-map level (all 78 generators);
  - **ρ₂₇(σ_{ψ₀}) H₊ ρ₂₇(σ_{ψ₀}) = −H′** entry for entry (all 27² entries).

  So **the second Hermitian structure is the transport of the first by a
  census element, up to the global polarity −1.** H′ is not a new form; it is
  H₊ seen from a different frame, and the frames differ by a coboundary.
- **[D] ≠ 0**: the global negation is not a norm (exhaustive over all 64 ψ);
  its class is (1,1) — nonzero at *both* τ-fixed nodes. The Klein group maps
  onto H¹ with **kernel {I, D₂}** and image the diagonal ℤ/2 = ⟨[D]⟩.
- The general mechanism is verified elementwise for all 64:
  **R(ψ)[π(b)]·R(ψ)[b] = R(N(ψ))[b]** — conjugating a structure by an inner
  census element translates its torsor coordinate by the coboundary N(ψ).

**B938's colorless-triviality, cohomologically.** Re-verified in-cell (D fixes
every weight carrying the 3- and 6-blocks; all 12 of its flips are colored),
and then sharpened:

> The characters whose weight-lattice extension is **constant on the colorless
> register** form a subgroup of **order exactly 2**, generated by the global
> negation — i.e. by D's own coordinate. So among all 64 twists, **the only
> nontrivial one the register cannot see is precisely the one carrying the
> nonzero cohomology class**, and the twist that carries the whole value
> arithmetic is precisely the one with no class at all. The register and H¹
> see complementary things.

## Q-D — the true classes (C-D PASS), and two new structural facts

**Four orbits of size four**, and conjugation by the census's inner part is
*exactly* translation by B¹ (verified on all 64 × 16 conjugations at
generator-map level). The orbit set IS H¹.

Class invariants (both constant on classes, computed exactly):

| H¹ class | fixed dim on the 78 | type | C-compatible members | contains |
|---|---|---|---|---|
| (1,1) | **52** | F₄ | 1 | τ, **φ₋** |
| (1,0) | 36 | C₄ | 1 | — |
| (0,1) | 36 | C₄ | 1 | — |
| (0,0) | 36 | C₄ | 1 | **φ₊**, **φ\*** |

Two facts worth their own lines:

1. **The wall pair is NOT a conjugate pair.** φ₊ is of type C₄ (fixed dim 36,
   class (0,0)); φ₋ is of type F₄ (fixed dim 52, class (1,1)). The two
   wall-real alignments are genuinely different involutions. And **φ\* — the
   carrier of the second Hermitian structure — is conjugate to φ₊, not to
   φ₋.**
2. **C-compatibility is a SECTION of the class map.** The four C-compatible
   outer census members (B907's four) realize each cohomology class **exactly
   once**. The charge frame picks one representative per class — it is a
   cohomological section, not an accident of the sweep.

**The signature separates nothing.** All sixteen structures share the same
unordered signature {12,15}; the gap is entirely the three π-FIXED coordinates
(27 = 12 hyperbolic π-pairs + 3 fixed lines carrying one common sign). The
cell's *first* form of this criterion asked for the ORDERED signature to be
class-constant; the run refuted it, correctly — a structure is defined only up
to scale, so only the unordered pair is an invariant. Criterion repaired
mid-cell and re-run.

---

## Q-C — THE VALUE COROLLARY: **C-C FAILED. The discriminant reading is REFUTED.**

The sealed criterion asked whether the twist-norm law is the discriminant
(determinant) invariant of the pair (H₊, H′) restricted to the rational
register blocks. It is not. Computed exactly, and controlled:

| block | dim | det(H′)/det(H₊) | pencil det(H′ − xH₊), primitive |
|---|---|---|---|
| W3 (vacuum) | 3 | **−17/384** | 384x³+660x²+293x+17 = (x+1)(384x²+276x+17) |
| W6 | 6 | **+17/384** | 384x⁶−276x⁵−751x⁴+552x³+350x²−276x+17 |
| W18 (colored) | 18 | **1** | palindromic, degree 18 |
| full 27 | 27 | **−1** | (x−1)¹⁶(x+1)¹¹ |

The banked target was N_{K/ℚ}(d_S) = −(953/2304)² = −908209/5308416. It is not
−17/384, and the W3 pencil cubic is neither the banked d-minpoly nor its
reciprocal. **No 953 and no 2304 appear anywhere in the invariants of the
pair.** The pencil's own irrationality lives in ℚ(√3129), 3129 = 3·7·149 —
*not* in the value field K (squarefree discriminant 77).

**Controls run because a sealed criterion failed** (a failed criterion must be
protected against being an artifact):

- **Charge-choice control.** A second, unrelated set of separating charge
  constants gives the *same* subspaces and the *same* ratios. The blocks and
  their discriminant ratios are intrinsic.
- **Why the global ratio does not factor.** W3 ⊥ W6 under H₊ but **NOT** under
  H′; W3 ⊥ W18 and W6 ⊥ W18 under both. The twist respects the colour grading
  and **mixes the two colorless blocks**. So the product of block ratios
  (−289/147456) is not the global ratio (−1), exactly as the orthogonality
  data predicts.
- **The global pencil is empty of content.** H₊⁻¹H′ = diag(D₂) exactly, so the
  full 27-pencil is (x−1)¹⁶(x+1)¹¹, and it is reciprocal — forced, because
  R(ψ₀) conjugates the twist operator to its inverse.
- **The identification gap is closed.** The 3-block's own cubic h_S is
  irreducible with squarefree discriminant **77 = that of the value field K**.
  So W3 ⊗ K̄ is spanned by three Galois-conjugate joint charge eigenlines whose
  invariants live in K — the lines the banked d_S is computed on.

**The derived statement** (a consequence of the computed facts, not an
assumption): if those three conjugate lines were simultaneously orthogonal for
*both* forms, the determinant ratio would equal the product of the diagonal
ratios, i.e. N_K(d_S). It does not. **Therefore they are not** — and

> the twist-norm law is a **DIAGONAL, frame-relative datum** (a product of
> matrix elements of the involution D₂ between distinguished lines and
> themselves), **not a determinant, and not an invariant of the pair of
> Hermitian structures.**

**Independent re-derivation (verify-don't-trust, on this seat's own result).**
Because a sealed criterion failed on this number, the two headline facts were
recomputed by wholly different routes in a separate scratch script: H¹ by
brute-force coset enumeration over the 64 characters with no linear algebra
(order 4, four cosets of size 4; χ₋ a norm, the global negation not), and the
W3 determinant ratio via sympy nullspaces, a *randomly re-mixed* basis of W3,
and sympy determinants — **−17/384 again**, with the pencil factoring as
(x+1)(384x²+276x+17). The refutation is not an artifact of this cell's own
linear algebra.

**Per the sealed stop condition, no unification statement is written.** The
prereg said: if C-C fails, the value corollary is reported REFUTED and the
joining statement is not written. It failed; it is not written.

### The mechanism the refutation leaves behind (computed, fenced, NOT the sealed claim)

Three exact facts now sit together, and they say where the value layer lives
without saying what it means:

1. H′ = −ρ₂₇(σ_{ψ₀}) H₊ ρ₂₇(σ_{ψ₀}) — the two structures differ by a census
   frame change and a sign.
2. That frame change **preserves none of the register blocks** (3 → 6, 6 → 11,
   18 → 22 under W + R·W).
3. The register blocks span the 27, yet D₂'s eigenspaces are **not** the sums
   of their block pieces: 11 − (1+2+6) = **2** and 16 − (0+2+12) = **2**.
   Those four dimensions are the entire misalignment between the register
   decomposition and the twist's eigenspaces.

So d = 1 − 2m (re-verified here as an exact K-identity against the banked
coordinates, both families) is the H₊-distortion of an atom line under the
frame change — a quantity that exists only relative to a chosen frame, and
vanishes from every invariant of the two structures. The value primes are
carried by the misalignment, not by the classification.

A registered consequence of the same arithmetic: **N_K(d) = (−1)·(953/2304)²**
— the polarity times a perfect square. Whatever discriminant-style invariant
one forms from it, the entire prime content is square and therefore invisible;
only the sign survives. (The sign itself is the same polarity ε(χ₋) = −1 that
B928 met as the "affine shift".)

---

## The prior scoreboard (the discipline, reported verbatim)

Five disclosed priors. **Four won** (the group/module identification; H¹ =
(ℤ/2)² supported on the τ-fixed nodes; [D₂] = 0 with the predicted witness
class; [D] ≠ 0; four orbits of four). **One LOST**: the prediction that the W3
determinant ratio would be −(953/2304)² was wrong — it is −17/384. The object
overruled the seat on the one question that mattered most.

## Honest gaps

1. **Scope of "class".** H¹(⟨τ⟩, T_ad[2]) classifies the sixteen up to
   conjugacy by the CENSUS's inner part, which is finer than E₆-conjugacy:
   the fixed-dimension invariant collapses the four classes to two types
   (F₄ once, C₄ three times). Nothing here claims the four are inequivalent
   under the full adjoint group.
2. **The refutation is of one precise reading.** C-C tested the discriminant/
   pencil reading of the twist-norm law and refuted it. It did **not** test
   whether the value layer is cohomological for some *other* group (the
   generation Galois group is the obvious candidate, and N_{K/ℚ} is its norm).
   That question is open and is registered below.
3. **The atom lines themselves were not rebuilt here.** Their spanning and
   their field are established in-cell (h_S irreducible, disc 77 = K's); the
   individual banked line data (d_S, d_A, m_S, m_A K-coordinates) is read from
   B928 and only ever *compared* against — the derived non-orthogonality
   statement rests on that comparison.
4. **ε and the base weight.** ε(χ) = χ̂(w₀) depends on which weight is indexed
   0 in B883's rep27 — a convention. Nothing verdict-bearing rests on it; the
   intrinsic statements are all in the R-normalization.
5. Locks (`tests/test_b936_b939.py`) are the banking seat's step; not
   written by this agent.

## Registered opens (registration-over-preservation)

- **L-B936-1.** Is the value layer cohomological for the *generation* group
  (the cubic K/ℚ with its branch action), rather than for ⟨τ⟩? The twist-norm
  law is a K/ℚ-norm of a diagonal datum; whether that diagonal datum is a
  cocycle for a genuine branch action is untested.
- **L-B936-2.** The new pair-invariants are unexplained: −17/384 on W3,
  +17/384 on W6, 1 on W18, and the quadratic ℚ(√3129), 3129 = 3·7·149. Where
  does 17 come from, and why does it cancel between the two colorless blocks?
- **L-B936-3.** The four-dimensional misalignment (2 in each D₂-eigenspace)
  between the register decomposition and the twist eigenspaces is, on this
  cell's evidence, the entire seat of the frame-relative value data. It has
  not been described intrinsically.
- **L-B936-4.** The wall pair being non-conjugate (C₄ vs F₄) is new and
  unexploited; B907's two wall-real alignments are not related by any inner
  automorphism.
- **L-B936-5.** C-compatibility as a section of Z¹ → H¹ suggests the charge
  frame is a canonical splitting; whether that section is unique among all
  possible frame conditions is untested.

## Files

`PREREGISTRATION.md` (sealed, sha-256 in `ARTIFACT_HASHES.txt`) ·
`cohom.py` → `results.json` (92 entries: 70 checks all PASS, 21 data blocks,
1 sealed criterion FAILED) · this draft.

## Depends on

B854 (frame), B883 (the 27), B900 (cocycle/frames), B907 (τ, the census, the
wall pair), B912 (H±), B916 (D₂, the twist norms), B923 (the colored
machinery), B928 (the torsor theorem, the sixteen, the K-coordinates), B930
(the register blocks), B938 (D colorless-trivial).
