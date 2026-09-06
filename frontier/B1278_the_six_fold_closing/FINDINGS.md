# B1278 — THE TOWER'S WILSON LINES, THE THREE FACES AT ONCE: on Y₃ and Y₆ the Standard-Model group and three generations still exclude each other (by theorem and by exhaustive enumeration), but on Y₉ — the object's own 9-fold closing, hyperbolic, with the prime 19 in its torsion — Wilson lines valued in the closing's own order-19 and order-38 characters break SU(5) to exactly the Standard Model with three complete generations of the 27: the first vacuum of the programme with the SM gauge group and three generations, vector-like

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (H₁ by Smith form with Fox's product as check; every character's h¹ by a 40-digit sweep with every non-zero confirmed exactly over the cyclotomic field; the Wilson-line enumerations complete — exhaustive on Y₃ and Y₆, complete through the three-generation alphabet on Y₉) + POSITIVE (the SM group with three generations exists on Y₉) + the standing NEGATIVE (the count is vector-like, B1260) · **Price: unchanged**

## Why this arc — the owner's reminder, taken literally

*"We're not dealing with an object alone, but three faces of it."* The corpus's own statement of the three faces is
B258's table — **geometry, arithmetic, quantum**, each resolving into the object's **two ends**: the hyperbolic /
E₆ / ℚ(√−3) end and the spherical / E₈ / ℚ(√5) end, with the Euclidean point between them (B248, B257: cone angle
α = 2π/3, the order-3 meridian ω, Vol = CS = 0, the branch point of the character variety). The closings
B1273–B1277 computed on are **the manifold covers of that transition**: Y₂ = L(5,2) covers the spherical end's
ℤ/2 orbifold (|H₁| = 5 = det, the golden determinant), **Y₃ — the flat Hantzsche–Wendt manifold — covers the
Euclidean point** (|H₁| = 16 = |Δ(ω)|², the golden polynomial Δ = t² − 3t + 1 at the Eisenstein root), and Y_n for
n ≥ 4 cover the hyperbolic cone manifolds. So B1277's theorem was proved at the Euclidean middle, where the
quantum face is empty (Vol = 0: no exponential sector — the same fact as the closing's tree-level-only Yukawa).
The destination ledger's D3 needs Vol ≠ 0, the hyperbolic branch; the three generations need the descent 3 | n
(B1274). **The first closing with both is Y₆**, whose torsion by Fox's product is 5 · 16 · 4 = 320 — the golden
end's 5 and the Eisenstein end's 16 in one group. **The next is Y₉**, where the golden polynomial at the primitive
ninth roots of unity has norm 19² and H₁ = (ℤ/76)². This arc asks B1277's question on both.

## 1. The closings' torsion and characters ((a), exact)

| closing | geometry | π₁ (Reidemeister–Schreier, B1274) | H₁ (Smith form) | Fox's ∏\|Δ(ζ)\| | exponent m |
|---|---|---|---|---|---|
| Y₃ | flat (the Euclidean point's cover) | 4 generators, 4 relators | ℤ/4 ⊕ ℤ/4 | 16 ✓ | 4 |
| Y₆ | hyperbolic | 7 generators, 7 relators | **ℤ/8 ⊕ ℤ/40** | 320 = 5·16·4 ✓ | 40 |
| Y₉ | hyperbolic | 10 generators, 10 relators | **ℤ/76 ⊕ ℤ/76** | 5776 = 16·19² ✓ | 76 |

The characters of H₁ are enumerated exactly from the Smith transforms (a = V·c with D·c ≡ 0 mod m); every relator
is checked killed.

## 2. Every character's h¹ ((b), the sweep and its exact confirmation)

Fox calculus on the presentation, h¹(ψ) = (#generators − rank d₁) − rank d₀, the ranks by singular values at 40
digits (the smallest accepted and the largest rejected singular value are printed: 0.66 vs 10⁻⁴¹ on Y₃, 0.11 vs
10⁻⁴¹ on Y₆, 3.6·10⁻³ vs 10⁻⁴⁰ on Y₉), then **every character with h¹ > 0 recomputed exactly** by Gaussian
elimination over ℚ(ζ_m) (polynomials modulo Φ_m), plus zero controls.

| closing | characters | with h¹ = 1 | the three family characters | the rest | closed under the family characters? |
|---|---|---|---|---|---|
| Y₃ | 16 | 3 | 3 (order 2) | none | — |
| Y₆ | 320 | **27** | 3 | **24 of order 8** | no (24 of 72 products) |
| Y₉ | 5776 | **147** | 3 | **36 of order 19, 108 of order 38** | **yes (432 of 432)** |

No character has h¹ ≥ 2 on any of the three. On Y₉ the h¹ = 1 set has a structure: 36 = 2 × 18 characters of
order 19 are the non-trivial elements of **two cyclic subgroups C₁, C₂ of order 19** in the 19-part (ℤ/19)² of the
character group, and the 108 of order 38 are their products with the three family characters — the set is
(C₁ ∪ C₂) × V₄ minus the identity, where V₄ is the group of the family characters.

## 3. The family characters ((c), all 48 surjections)

The descended 3_ρ (B1273/B1274; Klein image) splits into three sign characters χ₁, χ₂, χ₃ of H₁(Y_n), the same
triple for all 48 surjections π₁(m004) ↠ 2T, with χ₁χ₂χ₃ = 1 and h¹(χ_i) = 1 on Y₃, Y₆ and Y₉. The three 27s of
the E₈ theory on each closing are carried by them (B1273 §3), so the multiplicity of the component c of the 27
under a flat E₆ connection W acting on it by the character ψ_c is **m(c) = Σ_i h¹(χ_i ψ_c)**.

## 4. The three-generation alphabet ((d)) — trivial on Y₃ and Y₆, 145 elements on Y₉

K3 = {ψ : Σ_i h¹(χ_iψ) ≥ 3}. On **Y₃ and Y₆ it is the trivial character alone** (on Y₆ the distribution of
Σ_i h¹(χ_iψ) is 268 : 24 : 27 : 1 for the values 0, 1, 2, 3), so B1277 (d) applies verbatim: three generations
of Q, u^c, e^c force ψ = 1 on the 10 of SU(5), W commutes with SU(5), **no SM vacuum with three generations on Y₃
or Y₆, with or without Wilson lines, abelian or not.** On **Y₉, K3 has 145 elements**: the identity and the 144
characters (c, s), c ∈ (C₁ ∪ C₂) ∖ {1}, s ∈ V₄ — exactly the characters whose three family twists all carry a
class. The alphabet the theorem said a closing would need exists on the object's own 9-fold closing.

## 5. The Wilson lines ((e) exhaustive on Y₃, Y₆; (e′) complete on Y₉)

An SM-commuting flat E₆ connection is a homomorphism P/Q_SM → Ĥ₁ (the weight lattice modulo the SM-root lattice
into the character group); the SM-root lattice is primitive of rank 3 in P (invariant factors 1, 1, 1), so W ↔
three free characters. The characters of Q, u^c and L determine W (their coefficient matrix on P/Q_SM has
determinant 1), and every other component's character follows.

| closing | SM-commuting W | breaking SU(5) with 3 generations of Q, u^c, d^c, L, e^c | best SU(5)-breaking: min generations |
|---|---|---|---|
| Y₃ | 4 096 (all) | **0** | 2 (48 lines) |
| Y₆ | 32 768 000 (all) | **0** | 2 (4 464 lines) |
| Y₉ | 145³ = 3 048 625 candidates with three generations of Q, u^c, L (complete: every other line fails on Q, u^c or L) | **737 568** | 3 |

On Y₃ and Y₆ the two-generation spectra come in several patterns — three generations of the doublets Q, L with
two of u^c, d^c, e^c; or three of Q, d^c with two of u^c, L, e^c; and others: **which two labels drop is the
line's choice, that some label drops is the theorem.**

**On Y₉:** of the 737 568 SU(5)-breaking three-generation lines, **706 464 are SM vacua** — ⟨N⟩ and ⟨ν^c⟩ available
(B1277's rank-reducing pair), H_u and H_d present — and at the ⟨N⟩, ⟨ν^c⟩ point **every one of them keeps exactly
the 8 roots of the Standard Model** (colour A₂ and weak A₁; the 12 X-type roots of SU(5) are broken by the line).
**568 656 of them keep all 81 states of the three 27s**: the spectrum {Q 18, u^c 9, d^c 9, L 6, e^c 3, ν^c 3, H_u 6,
H_d 6, D 9, D̄ 9, S 3} — three complete 27s, nothing projected — while SU(5) is broken. This is possible because the
line's image lies in one C_a × V₄ (order dividing 76, exponent 38) and the homomorphism P → ℤ/19 it induces
vanishes on the SM roots and on no SM multiplet of the 27: every component's character has a non-trivial 19-part, every family twist of it carries a
class. The lines' images in the character group are ℤ/19 (12 996 lines), ℤ/19 × ℤ/2 (205 308) or ℤ/19 × V₄ (350 352). Beside the 27s: the six flavons (unchanged), and
**64 E₆-adjoint chirals** from the 64 broken roots (each ψ_α ≠ 1 carries one class; ±α pair up: 32 vector-like
pairs in the E₆/SM coset), or fewer on the lines that project part of the 27.

**The 4d spectrum at such a point:** gauge su(3) ⊕ su(2) ⊕ u(1)_Y ⊕ u(1)² (the family torus mixed with the E₆
Cartan, as in B1277), matter 3 × (27 ⊕ 27̄) with the one-coupling superpotential of B1276, six flavons, 32 vector-
like pairs of coset states. **It is the Standard-Model gauge group with three complete generations, on a closing
the object supplies, broken to it by the closing's own characters.** It is vector-like: the 27̄s mirror the 27s
(B1260 — a closed 3-manifold), so no chirality; the line is one of 706 464 (a discrete choice; the orbits under the deck
ℤ/9 and the closing's automorphisms are registered, L206).

## 6. Ledger

- **The three faces, placed.** The tower of closings is the geometric transition's tower of covers; B1277 sat at
  the Euclidean middle (quantum face empty), B1278 at the first two hyperbolic closings with the three
  characters. The answer changes with the closing: the theorem's exclusion holds on Y₃ and Y₆ and **fails on Y₉**,
  where the arithmetic face brings the prime 19 (the norm of the golden polynomial at the ninth roots) and with it
  the alphabet the theorem said was needed.
- **The first SM-group, three-generation vacuum of the programme**: on Y₉, by Wilson lines in the closing's own
  order-19/38 characters composed with the SM's commutant torus, plus B1277's ⟨N⟩, ⟨ν^c⟩. Vector-like.
- **What stands:** chirality (N = 0 on every closed closing, B1260); the values (0 of 19); the doublet–triplet and
  one-coupling relations of B1276 now hold on a spectrum that is the SM's.
- **What is new for the destination:** D2's space and D3's exponential sector are now posed on a closing whose
  spectrum is the SM's (Y₉: Vol ≠ 0); the chiral closing named in the ledger no longer needs to supply the group
  or the count — only the chirality bit.

## Controls (MB12)

- H₁'s order is checked against Fox's product on every closing (16, 320, 5776); the Y₃ row reproduces B1277 exactly.
- The numeric ranks have gaps of ≥ 37 orders of magnitude; every non-zero h¹ (3, 27, 147) is recomputed exactly
  over ℚ(ζ_m), with zero controls.
- The family characters are computed from all 48 surjections and found to be the same triple on every closing.
- On Y₃ and Y₆ the enumeration is exhaustive over Hom(P/Q_SM, Ĥ₁) and finds W = 1 as the unique SU(5)-preserving
  three-generation line — the theorem's statement reached independently by counting. On Y₉ the search is
  complete: a line with three generations of Q, u^c, L has its three characters in K3 (a necessary condition), and
  every such triple is scanned; the coefficient matrix's determinant 1 is asserted, and the characters recomputed
  from the solved line are asserted equal to the triple.
- The kept-root count is asserted to be 8 on every SM vacuum; the SM vacua are counted after requiring the fields
  the vacuum needs (N, ν^c, H_u, H_d).
- The theorem's proof (Y₃, Y₆) does not use the enumeration; the enumeration does not use the theorem.

## Verification

`verification/six_fold_closing.py` (Y₃, Y₆ with the exhaustive enumeration: `SELFTEST: PASS`, run record
`verification/six_fold_closing_run.txt`; Y₉: `python3 six_fold_closing.py 9`, `SELFTEST: PASS`, run record
`verification/six_fold_closing_run_9.txt`, ~25 min, the exact cyclotomic confirmations dominating). Lock:
`tests/test_b1278_the_six_fold_closing.py` (Y₃ fast; Y₆ and Y₉ slow-marked).
Feeds on: B1277 (the theorem's mechanism, the SM's commutant, the descent data, the ⟨N⟩, ⟨ν^c⟩ point), B1274 (the
tower's presentations and the descent), B1273 (the family characters), B1248/B257/B258 (the transition, its three
anchors, the three faces), B326/B251 (|H₁(Y₃)|, Y₂ = L(5,2)), B1260 (vector-like on closed manifolds), B1276 (the
superpotential the spectrum carries). Literature: Fox, *Free differential calculus III* (|H₁| of cyclic branched
covers as ∏|Δ(ζ)|); Helling–Kim–Mennicke (Y_n as the Fibonacci manifolds); Wilson-line breaking of SU(5) with
discrete torsion (Witten 1985; Candelas–Horowitz–Strominger–Witten).
Registers no identification change.
