# B1273 — THE OBJECT'S OWN THREE-FOLD CLOSING: the 3-fold cyclic branched cover of m004 is the flat Hantzsche–Wendt manifold, the object's 2T holonomy descends to it as its own flat holonomy, it carries exactly three twisted classes — one per flat direction — and the texture they force is refuted by m_t ≤ m_c + m_u

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (every structural step exact; the manifold identification classical, fingerprinted) + NEGATIVE (the tree-level texture obeys an inequality the data violate by factors 17–136) · **Price: unchanged**

## Why this arc — the step back

B1271's addendum named the object the Yukawa needs: **three cohomology classes with an H³ target**, i.e. a closing
of the object carrying three 27s that something outside E₈ tells apart; B1043 W4 named the door — *an H³-bearing
three-body assembly built from the 3-fold cyclic cover*. Stepping back: the object supplies its own closings — its
**cyclic branched covers** Y_n along the knot, indexed by n, with the deck group ℤ/n permuting n copies of the
object. B326 already counted |H₁(Y₃)| = |Δ(ω)Δ(ω²)| = 16 = |(ℤ/4)²|; B251 has Y₂ = L(5,2), the golden lens space.
**Y_n are the Fibonacci manifolds** (Helling–Kim–Mennicke: π₁(Y_n) = F(2,2n); F(2,4) = ℤ/5), and **Y₃ is the flat
Hantzsche–Wendt manifold** (the didicosm: the unique closed flat 3-manifold with holonomy ℤ₂², π₁ = F(2,6)) — the
two faces meet in the closings: the Eisenstein object's covers have golden (Fibonacci) groups. n = 3 is the
Eisenstein number; three copies of the object, permuted by ℤ/3, closed, with an H³. This arc computes what lives
on it.

## 1. Y₃ by Reidemeister–Schreier (`verification/three_fold_closing.py` (a), exact)

The kernel H of a, b ↦ 1 ∈ ℤ/3 in π₁(m004) = ⟨a, b | a w B w⁻¹⟩ is rewritten on the Schreier generators
z = a³, x_k = a^k b a^{−(k+1 mod 3)}; filling the lifted meridian z gives π₁(Y₃) = ⟨z, x₀, x₁, x₂ | R₀, R₁, R₂, z⟩.
**H₁(Y₃) = ℤ/4 ⊕ ℤ/4** (Smith form), matching B326. Fingerprint against F(2,6) = ⟨x₁…x₆ | x_i x_{i+1} = x_{i+2}⟩:
the same abelianization, **64 = 64** homomorphisms to Q₈, **16 = 16** to A₄.

## 2. The object's holonomy descends, and becomes the closing's own ((b), exact over ℚ(ω), all 48 surjections)

For every surjection ρ: π₁(m004) ↠ 2T (B1263's 48, meridian order 3 or 6), the real 3 of 2T — the adjoint of the
2 × 2 model — satisfies 3_ρ(a³) = 1, so **3_ρ descends to Y₃**. On Y₃ its image is the **Klein four-group V₄**
(order 4, exponent 2) = ker(A₄ → ℤ/3): **the holonomy group of the flat manifold**. By Fox calculus on the
branched-cover presentation:

| coefficients on Y₃ | h⁰ | h¹ |
|---|---|---|
| trivial | 1 | **0** (b₁ = 0) |
| each of the three non-trivial sign characters χ₁, χ₂, χ₃ of H₁ = ℤ₄² | 0 | **1** |
| the descended **3_ρ** | 0 | **3** — and each χ_i occurs in 3_ρ with multiplicity **1** |
| the descended spin lift 2_ρ (meridian order 3) | 0 | 0 |

So **3_ρ|_{Y₃} = χ₁ ⊕ χ₂ ⊕ χ₃**, the three characters with h¹ = 1 — which are the three holonomy characters of
the flat manifold (H¹(Y₃; χ_i) is the χ_i-line of H¹(T³) = ℂ dx_i under the torus cover): **the object's family
SU(3) holonomy, descended to the object's own closing, is the closing's tangent bundle, and the three classes are
its three flat directions x, y, z — permuted by the deck ℤ/3.** Same for all 48 surjections.

## 3. The E₈ transport on Y₃ ((c), by characters)

With the golden E₈ along Y₃ and the descended V₄ ⊂ SU(3) as holonomy: gauge algebra = the centralizer of V₄ in
E₈ through E₆ × SU(3) = **e₆ ⊕ u(1)²** (the family SU(3)'s torus; no invariants in (27,3), (27̄,3̄), and 2 in
(1,8)); matter = (27,3) ⊗ H¹(3_ρ) = **three 27s with family charges e₁, e₂, e₃**, the mirror (27̄,3̄) ⊗ H¹(3̄) =
**three 27̄s**, (1,8) ⊗ H¹(8_ρ) = 2·0 + 2·3 = **six singlets** with charges ±(e_i − e_j), and **no E₆-adjoint
chiral** (b₁ = 0). Vector-like (B1260 (1)); the chirality bit is the orientation of Y₃ = the sign of the triple
product; the six singlets are the flavons whose VEVs would pair 27_j with 27̄_i — values the object does not
supply (H5).

## 4. The texture, and its refutation ((d))

The characters allow exactly one cubic among the three 27s, χ₁χ₂χ₃ = 1: **W = λ d_abc 27^a_1 27^b_2 27^c_3**, with
λ ∝ ∫_{Y₃} dx₁ ∧ dx₂ ∧ dx₃ ≠ 0 — the first non-vanishing three-generation Yukawa in the programme, on a closing
the object supplies. Every tree-level charged-fermion mass matrix is then complex symmetric with **zero diagonal**
(the Higgs doublets sit in the 10 ⊂ 27_i, M_jk = λ |ε_ijk| ⟨H_i⟩).

**Theorem.** A complex symmetric 3 × 3 matrix with zero diagonal has singular values σ₁ ≤ σ₂ + σ₃. (Takagi:
M = U Σ Uᵀ, so 0 = M_ii = Σ_k σ_k U_ik²; hence σ₁|U_i1|² ≤ Σ_{k≥2} σ_k |U_ik|², and summing over i with unit
columns gives σ₁ ≤ σ₂ + σ₃.) Checked on 20 000 random matrices (max ratio 1.000000).

| sector | m_heaviest / (m_second + m_lightest) | bound |
|---|---|---|
| up (t; c, u) | **135.8** | ≤ 1 |
| down (b; s, d) | **42.8** | ≤ 1 |
| charged leptons (τ; μ, e) | **16.7** | ≤ 1 |

**The closing's three generations have a Yukawa, and its tree-level texture is refuted in every charged sector.**
The negative is general for the route: any three generations carried by three *distinct characters* couple only
through the product-trivial triple, so the class-basis mass matrix is zero-diagonal and the bound applies. Lifting
it needs a diagonal source — a non-tree-level term (an instanton, a loop) or generations that are not
character-distinguished — none of which the object supplies here.

## 5. Ledger

- **The named door of B1043 W4 and the named object of B1271 are the same object, and it is the object's own
  3-fold branched cover** — computed, flat, with exactly three classes.
- **Three generations = the three flat directions of the object's closing**, permuted by its ℤ/3; the family
  SU(3) holonomy is the closing's tangent bundle. Structure; no identification with a physical index (E63).
- **The first non-zero three-generation Yukawa** in the programme, and the sharpest value negative: an
  *inequality* the data violate by up to two orders of magnitude.
- Chirality: N = 0 (closed); values: 0 of 19; price unchanged.

## Controls (MB12)

- The presentation is derived (Reidemeister–Schreier), not imported; H₁ is computed and matches B326; the
  F(2,6) fingerprint uses two independent target groups.
- All 48 surjections are run, both meridian-order classes; the multiplicities of *all four* sign characters in
  3_ρ are computed (three 1s and a 0), so "3_ρ = χ₁ ⊕ χ₂ ⊕ χ₃" is not read off but measured; h¹(trivial) = 0 and
  h¹(2_ρ) = 0 are the controls that a wrong presentation would break.
- The texture bound is proved and numerically saturated (ratio → 1.000000), so the refutation is not a numerical
  artefact.

## Verification

`verification/three_fold_closing.py` (exact; ~1 min; `SELFTEST: PASS`), run record
`verification/three_fold_closing_run.txt`. Lock: `tests/test_b1273_the_three_fold_closing.py`.
Feeds on: B1263/B1270 (the 48 surjections, the 2T model), B326 (the torsion), B251 (Y₂ = L(5,2)), B1043 (the
door), B1271 (the named object), B1260 (N = 0 on closed manifolds), B1268 (the bound). Literature: Helling–Kim–
Mennicke, *A geometric study of Fibonacci groups* (the Fibonacci manifolds as cyclic branched covers of 4₁);
Hantzsche–Wendt (the flat manifold). Registers no identification change.
