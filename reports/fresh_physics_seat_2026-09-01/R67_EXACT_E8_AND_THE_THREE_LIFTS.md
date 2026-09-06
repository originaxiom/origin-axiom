# R67 — AN EXACT e₈ AND THE THREE LIFTS: L_g, w_{A₂}, w₃ lift to order-3 elements of E₈ in the SU(9), E₇×U(1) and E₆×SU(3) classes — R64 §4 is now computed, not assumed

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Status:** seat report, not banked. Exact integers throughout; script `computations/r67_exact_e8_lifts.py`. Closes the last caveat of R64 (the E₈ half); R66 closed the E₆ half.

## 1. The algebra

e₈ built exactly the way B351 built e₆: 240 roots by height induction from the Bourbaki Cartan matrix (chain 1-3-4-5-6-7-8, node 2 on 4), the Frenkel–Kac cocycle ε(a,b) = (−1)^{a·B·b} with B upper-triangular, brackets [e_a, e_b] = ε(a,b) e_{a+b}, [e_a, e_{−a}] = −h_a, [hᵢ, e_b] = (αᵢ, b) e_b. Controls: Jacobi on **30,000 random basis triples: 0 violations**, and on **every mixed triple (e_a, e_{−a}, e_b) with (a,b) = −1 for the first 40 positive a: 0 violations** — the triples that failed B351's first sign convention.

## 2. The lifts

Simple reflections lift as nᵢ = exp(ad eᵢ)·exp(ad e₋ᵢ)·exp(ad eᵢ), which are integer matrices (the ½(ad e)² term only reaches e_α from e_{−α}, with coefficient 1, in a simply-laced algebra); each nᵢ is checked to act on the Cartan as sᵢ. The three elements of R64 are transported from the icosian lattice to Bourbaki coordinates (simple roots by a generic functional; the Cartan matrix matched by a permutation respecting node degrees; all 240 coordinate vectors coincide with the abstract root list). Reduced words are produced by the descent algorithm (no search over W(E₈)): lengths **80** (L_g), **32** (w_{A₂}), **64** (w₃). Eigenvalue multiplicities are ranks of (ŵ − 1) and (ŵ² + ŵ + 1) modulo 10007 and 1000003, which agree.

| element | Tits lift ŵ³ | correction | order-3 lift's (fixed, ω+ω̄) | class |
|---|---|---|---|---|
| **L_g** — the founding ratio | = 1 already | none | **(80, 168)** | **SU(9)** |
| **w_{A₂}** — the family rotation | a sign character (order 6) | t_η, η = (0,1,0,0,0,0,0,0) | **(134, 114)** | **E₇ × U(1)** |
| **w₃** — the E₆ factor | a sign character (order 6) | t_η, η = (1,0,0,0,0,0,0,0) | **(86, 162)** | **E₆ × SU(3)** |

The correction is found by solving, over 𝔽₂, η + η∘w + η∘w² = δ where t_δ = ŵ³ — an 8-bit linear system; both systems were solvable, so order-3 lifts exist among sign lifts and no ω-valued torus element was needed.

## 3. What is now settled

R64 §4's table — that the founding ratio, its family factor and its E₆ factor realise the three non-central order-3 classes of E₈, one each — holds with the lifts constructed. In particular, **the founding ratio's own lift is of order 3 with no correction, and it is the SU(9)-type element**: 248 = 80 + 84 + 84̄ under its centralizer, with 84 = Λ³(9) complex, and the ω ↔ ω̄ choice is the choice of 84 versus 84̄. The element that defines the E₆ × SU(3) family structure is the E₆-internal factor w₃; the family rotation alone is the E₇ × U(1) element.

An incidental fact worth a line: the naive Tits lifts of both w_{A₂} and w₃ in E₈ have order 6, while w₃'s Tits lift built inside E₆ (R66) has order 3 — the same Weyl element lifts differently through E₆'s and E₈'s simple reflections, by a sign character. Anyone using "the lift" of a Weyl element to fix a conjugacy class must say which.

*Sweep: no exact e₈, no Tits lift in E₈, and no Kac classification of the founding ratio appear on main or the SM-derivation branch (B1275 builds E₈'s roots and an A₂ Weyl rotation but no Lie algebra and no lift).*
