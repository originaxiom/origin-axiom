# Novelty / prior-art audit (2026-06-09, B134/V123)

A deep, adversarial literature pass (fan-out web search → fetch → 3-vote verification → cited synthesis) on whether the
project's clean recent results are genuinely new or already in the literature. **Purpose:** stop re-deriving known
mathematics; locate where the real novelty is; cite prior art. Verdict enum: **KNOWN / PARTIALLY-KNOWN / APPEARS-NOVEL
/ NEEDS-SPECIALIST**. Adversarial stance: assume known, try hard to find prior art before concluding novel.

This is a reference note (motivation/provenance), not a claim. Nothing here promotes to `../CLAIMS.md`.

---

## R1 — the chirality recursion (B128 / `../knowledge/K011`) — **PARTIALLY-KNOWN** (mechanism known; block-lift novel)

**Claim audited:** a metallic-block bundle `R^{m₁}L^{m₁}…R^{m_k}L^{m_k}` is amphichiral ⟺ the block-length sequence
`(m₁,…,m_k)` is a cyclic palindrome.

- **Prior art (the mechanism):** **Goodman–Heard–Hodgson, "Commensurators of cusped hyperbolic manifolds,"
  Experimental Math. 17(3) (2008), arXiv:0801.4815** — classify the symmetries of a once-punctured-torus bundle by its
  L/R monodromy word: **anti-palindromic** word (reverse = L↔R swap, cyclically) ⟺ orientation-**reversing** symmetry
  (amphichiral); **palindromic** word ⟺ orientation-preserving π-rotation. The figure-eight `RL` is the canonical
  anti-palindromic/amphichiral example. **This is the exact engine** behind the recursion → the *principle* is not new.
- **Neighboring prior art:** **Kauffman–Lambropoulou (math/0212011, L'Enseignement Math. 2004)** — achiral rational
  knots ⟺ even-palindromic continued fractions (called a "well-known result"); palindrome↔amphichirality is
  long-established in the 2-bridge / continued-fraction setting.
- **The novel kernel:** the lift to the **integer block-length sequence** being a cyclic palindrome is **not stated**
  in the located literature (Guéritaud–Futer math/0406242 give the LR-word formalism but no amphichirality criterion;
  Lackenby math/0112221; full-text scans show no palindrome/chirality discussion). 
- **Status (B134):** now **PROVED** as an elementary corollary of GHH 2008 (see `../frontier/B134_chirality_recursion_proved/`).
  The lift is the project's contribution; the chirality mechanism is GHH's.
- **Open / needs-specialist:** confirm GHH state the criterion as an **iff** for all these bundles; check whether
  Bowditch (arithmetic punctured-torus bundles) or Hoste–Shanahan (twist knots) state a block-sequence/continued-fraction
  palindrome criterion not surfaced here.

## R2 — the two-seed fork (B131 / `../knowledge/K014`) — **KNOWN** (with a framing qualification)

**Claim audited:** gluing two distinct once-punctured-torus bundles along cusp tori discretizes `κ` (intersection of
two distinct A-polynomial curves); same-seed glue stays a continuum.

- **Prior art (the mechanism):** **Kitano–Nozaki, "Finiteness of the image of the Reidemeister torsion of a splice,"
  Ann. Math. Blaise Pascal 27(1) (2020), arXiv:1904.02559** — finiteness via the two pieces' A-polynomial curves
  intersecting in the boundary-torus character variety; `gcd(A_{K1}(L,M), A_{K2}(M,L)) = 1` ⟹ finite (Bézout). Exactly
  the posited transverse-intersection mechanism. Corollary extends to all 2-bridge pairs.
- **Qualification (verified in B134):** Kitano–Nozaki's discreteness is driven by the meridian↔longitude-**swapping
  splice** gluing, **not** by the pieces being distinct — a same-knot splice `Σ(K,K)` is already finite; only the
  identity-glued double stays a continuum. So B131's **"heterogeneity makes the choice" is correct only for the
  identity gluing**; the general statement is *the gluing map* determines continuum-vs-discrete. (Verified: swap-glue
  fig8-to-fig8 → `P=f(f(P))`, degree 16, discrete; identity-glue same-seed → continuum.) B131 annotated accordingly.
- **Status:** the phenomenon is KNOWN; B131's math stands; its framing is qualified (gluing-map-dependent).

## R3 — the SU(2)_k field content (B132 / `../knowledge/K015`, corrected) — **KNOWN / standard**

**Claim audited:** the cyclotomic field of `ρ_k(monodromy)` eigenvalues for torus bundles is controlled by the
T-matrix root of unity (word spin-content mod 4), not chirality.

- **Prior art:** **Jeffrey, Comm. Math. Phys. 147 (1992)** — torus-bundle invariant `Z = Tr ρ(U)` is an explicit
  finite Gauss sum, cyclotomic content governed by `Tr U ∓ 2` and level `k+2`. **Dong–Lin–Ng, Algebra & Number Theory
  9(9) (2015), arXiv:1201.6644** — the modular SL(2,ℤ) representation has kernel a congruence subgroup of level
  `n=ord(T)` and is ℚ(ζₙ)-rational (resolving Coste–Gannon; corroborated by Bantay 2003, Ng–Schauenburg).
  **Lawrence–Zagier, Asian J. Math. 3 (1999)** — WRT invariants lie in ℚ(ζ) and are Galois-equivariant.
- **Status:** the general fact (cyclotomic, T-matrix-governed, chirality-irrelevant) is **firmly KNOWN/standard**. The
  specific "ℚ(i) at spin-content 2 mod 4" is a corollary-level refinement (verify directly from the T-matrix
  conformal weights `h_j = j(j+1)/(k+2)`, not a verbatim citation). This *confirms* the B133 correction: the B132
  content is standard quantum topology, not a chirality property.

---

## Net assessment

Two of the three are **known** (R2 Kitano–Nozaki; R3 standard quantum topology); one is **partially novel** with the
novel kernel now **proved** (R1, on GHH 2008). The project's recurring strength is methodological (verify-don't-trust,
firewall, first-class negatives); the genuinely-new mathematical content is narrow and best stated as: *the
block-length-sequence palindrome criterion for amphichirality of metallic-block once-punctured-torus bundles, a
corollary of Goodman–Heard–Hodgson*. The honest framing going forward: **cite GHH / Kitano–Nozaki / Jeffrey–Lawrence–
Zagier–Dong–Lin–Ng**; do not re-derive them; reserve any novelty claim for the block-lift (R1), pending a specialist
read of GHH's exact hypotheses.

**Method note (MB6, `../REPRODUCIBILITY.md`):** reproduction ≠ interpretation. **Method note (this audit):** "appears
novel" requires an adversarial prior-art search, not absence-of-memory — here it downgraded two of three.
