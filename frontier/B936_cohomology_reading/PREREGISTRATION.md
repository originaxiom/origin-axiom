# B936 — PREREGISTRATION (sealed before the first run)

**Cell:** the cohomology reading — is the value layer an H¹ story?
**Seat:** computation agent. **Blind:** no measured number is read, cited, or
compared anywhere in this cell.

## The sealed questions

**Q-A (the classification, made precise).** Identify the group G and the module
M for which the sixteen Hermitian structures of B928 are a torsor / a set of
twisted forms, and check every cocycle condition exhaustively (the sets are
finite: 64 characters, 128 census members).

**Q-A2 (the lift obstruction).** Is the assignment χ ↦ ρ₂₇(σ_χ) — which B928
determines only up to a global sign, whence its "affine polarity" — liftable to
an honest homomorphism? Equivalently: is the associated 2-cocycle a coboundary
(class in H²(X, μ₂) trivial)?

**Q-B (locate the two Klein generators).** Compute the class of D₂ and of D
(B912's wall twist) in the H¹ of Q-A: coboundary or not? And what does B938's
"D is the identity on the colorless register" mean cohomologically?

**Q-C (the value corollary).** Is the twist-norm law (B916:
λ_τ/λ_canonical = |N_{K/ℚ}(d)|^{−1/2} = 2304/953; B928: N_{K/ℚ}(d) =
−(953/2304)²) an instance of the general twisted-form story — i.e. is it the
DISCRIMINANT (determinant) invariant of the pair of structures restricted to a
rational block?

**Q-D (the orbits).** The orbit structure of the sixteen under conjugation by
the census: how many genuine CLASSES, of what sizes?

## Two-outcome criteria (each can pass and can fail)

1. **C-A1.** The 128 census members close under composition as an exact group
   of order 128 (all products recomputed at generator-map level), isomorphic to
   X ⋊ ⟨τ⟩ with X = Hom(Q, μ₂) ≅ (ℤ/2)⁶. PASS iff every product lands in the
   census and the multiplication table matches the semidirect law exactly;
   FAIL if any product escapes or the law fails for even one pair.
2. **C-A2.** The sixteen Hermitian structures carry a FREE and TRANSITIVE
   action of X^τ (the τ-invariant characters). PASS iff free ∧ transitive on
   the nose (16 distinct structures, 16 group elements); FAIL if any two
   coincide or any structure is missed.
3. **C-A3 (Q-A2).** PASS iff an explicit sign normalization ε: X → μ₂ makes
   χ ↦ ε(χ)·T_χ a homomorphism, verified on all 64 × 64 = 4096 pairs; FAIL if
   no such ε exists (then the class in H²(X, μ₂) is nonzero and is reported).
4. **C-B.** [D₂] and [D] in H¹(⟨τ⟩, X): each is either in the image of the norm
   N = 1 + τ (⟹ coboundary, class 0) or not (⟹ nonzero class). Decided by
   exhaustive search over all 64 ψ. Both outcomes are possible and are reported
   verbatim; the coboundary case must additionally EXHIBIT ψ₀ and verify
   σ_{ψ₀} φ₊ σ_{ψ₀}^{-1} = φ\* exactly at generator-map level and
   ρ₂₇(σ_{ψ₀}) H₊ ρ₂₇(σ_{ψ₀}) = ± H(φ\*) exactly as 27×27 matrices.
5. **C-C.** det(H′|_W) / det(H₊|_W) computed exactly, in ℚ, for the three
   rational charge blocks W3 (dim 3), W6 (dim 6), W18 (dim 18), and for the
   full 27. PASS (the discriminant reading) iff the W3 ratio equals
   N_{K/ℚ}(d_S) = −(953/2304)² exactly — the banked twist norm — and FAIL
   otherwise, in which case the discriminant reading of the value law is
   REFUTED and reported as such.
6. **C-D.** The orbit count of the sixteen outer involutions under conjugation
   by the census's inner part. PASS = the orbits are exactly the cosets of
   (1+τ)X inside X^τ (verified elementwise, 64 × 16 conjugations); the orbit
   count and sizes are the reported datum either way.

## Disclosed priors (hand-derived before the run; the object may overrule)

- Q-A: G = X ⋊ ⟨τ⟩ of order 128; M = X = T_ad[2] ≅ (ℤ/2)⁶ as a ⟨τ⟩-module,
  decomposing as (two induced summands from the flipped node pairs {α₁,α₆},
  {α₃,α₅}) ⊕ (two trivial summands from the τ-fixed nodes α₂, α₄).
- The sixteen outer involutions = Z¹(⟨τ⟩, X) = X^τ, i.e. the complements to X
  in G; census conjugation = translation by B¹ = (1+τ)X; hence
  **H¹(⟨τ⟩, X) ≅ (ℤ/2)^{#τ-fixed nodes} = (ℤ/2)²** — FOUR classes of four.
- Q-A2: trivial obstruction (the μ₃-isogeny P/Q has odd order, so the 2-torsion
  lift is canonical); the "affine polarity" of B928 is ε(χ) = χ̂(w₀), a
  character, hence a coboundary — not a class.
- Q-B: **[D₂] = 0** (a coboundary; D₂'s torsor coordinate χ₋ is the norm of the
  character with sign vector (−1,1,−1,1,1,1)); **[D] ≠ 0** (its coordinate is
  the global negation, whose (α₂,α₄) components are (1,1)). So the Klein group
  maps onto H¹ with kernel {I, D₂}.
- Q-C: the law IS a discriminant statement, but the two norms are DIFFERENT
  norms — the flip-cocycle norm N = 1+τ (finite, ℤ/2) versus the generation
  field norm N_{K/ℚ} (cubic). Predicted: the W3 determinant ratio equals
  −(953/2304)², the full-27 ratio equals −1, and hence the whole prime content
  of the value layer is a SQUARE in the discriminant — invisible to the class,
  which sees only the sign.
- Q-D: four orbits of size four.

## Conventions declared

- Frame: B854 `e6_centralizer.py`, exec'd in an isolated namespace with chdir
  to scratch and `__file__` set; 72 roots, charges n ∈ {8,14,16,22}.
- The 27: B883 `rep27.json`; weights = the Cartan diagonal; the pairing
  π(b) = the index a with w_a = −flip(w_b).
- Node indexing: 0-based, matching B854's Cartan matrix (Bourbaki α_{i+1});
  the diagram flip is FLIP = {0↔5, 2↔4, 1, 3}, so the τ-FIXED nodes are
  indices 1 and 3 (Bourbaki α₂, α₄).
- Characters: χ ∈ Hom(Q, μ₂) given by its signs on the six simple roots;
  σ_χ = the inner automorphism fixing the Cartan and scaling x_r by χ(r).
- τ = the outer lift with the B907 F₂ cocycle d; the census = {σ_χ, σ_χ∘τ}.
- H₊ = the invariant pairing of φ₊ = σ_{χ₊}∘τ (B907's wall pair), re-SOLVED in
  this cell from its own invariance equation — no banked H entry is assumed;
  banked data is only ever COMPARED against.
- H′ = H(φ\*) = H₊·D₂ (B916/B928). Hermitian structures are compared up to a
  global scale; every sign is threaded explicitly and never assumed positive.
- Exact arithmetic (`fractions.Fraction`, integer linear algebra) for every
  verdict-bearing claim. No Rayleigh-quotient readouts anywhere. Numeric belts,
  if any, at dps ≥ 60 with residual certificates.
- Blind: no measured number is read or compared. Gate 5 untouched.

## Stop conditions

- Any exact check failing ⟹ the cell reports UNSTABLE at that check and stops
  (no repair-and-continue inside a sealed run).
- If C-C FAILS, the value corollary is reported REFUTED, and no unification
  statement is written.
