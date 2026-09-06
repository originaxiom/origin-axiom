# R58 — θ-PARITY COMPUTED: the object's three h¹ classes are all θ-even, the fiber carries a θ-odd sector of 6 and 10, and the closing is what removes it

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 0ecd9557** · **Status:** seat report, not banked. Exact arithmetic modulo three primes p ≡ 1 (mod 3) (10009, 100003, 1000003), all agreeing; script `computations/r58_theta_parity.py`. Follows R56 (the endpoint theorem) and R57 (the three strands).

## 0. The question, and why it had never been asked

The record's dictionary has two rows that were never joined:

- **T-θTANGENT** (THEOREM_REGISTRY:38): the ℂ-linear θ — the E₆ → F₄ folding, the 27 ↔ 27̄ swap — *"is realized by the HYPERELLIPTIC involution (B353)."*
- **B576/B582**: θ-**odd** deformations have Zariski closure all of E₆(ℂ) and are **chiral**; θ-**even** ones stay **F₄-stable** and are **vector-like**.

The generation-count line (B632 → B1267) rests on `h¹(m004; 27_ρ) = 3` under the principal sl₂, `27 = Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰`, one class each, typed by B1253/B1256 as *"1 abelian + 2 chiral."* But "chiral" in the record's own dictionary means **θ-odd**, and θ is a concrete involution of the object. So each of the three classes has a computable parity, and nobody computed it. This report does.

## 1. The setup, verified

- **The involution.** The hyperelliptic involution of the once-punctured-torus fiber is −I ∈ SL(2,ℤ); it is central, commutes with the monodromy M², and extends fiberwise to m004 (it is in the symmetry group D₄). On π₁(m004) = ⟨a, b, t | tat⁻¹ = aba, tbt⁻¹ = ab⟩ the lift is **ι: a ↦ a⁻¹, b ↦ b⁻¹, t ↦ t·a⁻¹**; it preserves both relations (checked in the faithful Riley representation) and is an involution.
- **The conjugator.** ρ∘ι ≅ ρ: the linear system `G·ρ(ι u) = ρ(u)·G` (u = a, b, t) has a one-dimensional solution; tr G = 0, so G is the order-2 element of PSL(2,ℂ) — the π-rotation about the θ-axis geodesic of R57.
- **The action.** On cocycles, `f ↦ Sym^n(G)·(f∘ι)` preserves Z¹ and B¹; on the one-dimensional H¹ it is a scalar, and since G² is central and n is even, the scalar is ±1 with no lift ambiguity. Fox calculus on the 3-generator/2-relator presentation; the Sym^n homomorphism property is asserted before use (the B1267 bug class).

## 2. The result on the 3-manifold

| class | h¹(m004; Sym^n ρ) | θ = ι acts by |
|---|---|---|
| Sym⁰ (the "abelian" class) | 1 | **+1** |
| Sym⁸ | 1 | **+1** |
| Sym¹⁶ | 1 | **+1** |

Three primes, identical. **All three classes are θ-even.** In the record's dictionary that is: **all three are F₄-stable and vector-like.** The "2 chiral" of B1253/B1256 was a typing by summand, never a parity; the parity is even. This is R56's endpoint theorem seen from inside the record's own frame: nothing on the 3-manifold is θ-odd.

## 3. The result on the fiber — where the odd sector lives

Before closing, on the free fiber group F₂ = ⟨a, b⟩ with the same ι and G:

| n | dim H¹(F; Sym^n) | θ-even | θ-odd | tr(ι) | Lefschetz prediction |
|---|---|---|---|---|---|
| 0 | 2 | 0 | **2** | −2 | −I on H₁(F) — both odd ✔ |
| 8 | 9 | 3 | **6** | −3 | h⁰-term − 3·tr Sym⁸(G) = −3·1 ✔ |
| 16 | 17 | 7 | **10** | −3 | −3·tr Sym¹⁶(G) = −3·1 ✔ |

The trace is exactly the Lefschetz fixed-point sum over the **three half-periods** of R57 (three fixed points, index +1, tr Sym^n(G) = 1 for n ≡ 0 mod 8): the θ-odd sector on the fiber is *produced by the three fixed points*. And by the Wang sequence, `H¹(m004; V) = H¹(F; V)^{M²}` for n > 0: the one line the monodromy fixes is, in every case, inside the θ-**even** part.

> **The fiber carries chiral (θ-odd) classes — six and ten of them, sourced by the three θ-fixed points. Closing the fiber into the mapping torus keeps exactly one class per summand, and it is even. The closing removes the chiral sector.**

That is R57's sentence — *the object supplies three points and its closing erases them* — as a computed fact about cohomology rather than an Euler characteristic.

## 4. What this settles and what it opens

**Settles.** (i) The "1 abelian + 2 chiral" typing is refuted as a parity statement: 0 chiral + 3 even. (ii) I-25's stake as stated (*"the typing of h¹ depends entirely on the embedding"*) is moot for chirality: under the principal embedding all three are even, and R56 says the count is χ-type for any embedding. (iii) B1086's θ-odd *dial* (h¹ = 2 on the closed double) is a different object from the θ-parity of classes on m004; on the object itself no class is odd.

**Opens.** The θ-odd classes exist, on the fiber, and the monodromy is what kills them. So the question JOIN 1 should ask is not "what is h¹ of the 3-manifold" but **"what is the M²-action on the θ-odd sector of the fiber, and is there a *twisted* closing — the mapping torus of M² composed with θ — under which an odd class survives?"** The θ-twisted mapping torus of the fiber is the record's own object: B582's θ-odd double. On it, an invariant θ-odd class would be a chiral 27 localized at the three half-periods. That computation is the same code with one change (invariants of M²·ι instead of M²), and it is the next thing to run.

## 5. Controls

- Three primes agree on every number.
- The Lefschetz formula, computed independently from fixed points, reproduces the fiber traces (−2, −3, −3) — the fiber computation and the three-fixed-point count of R57 are the same fact.
- The n = 0 line reproduces the textbook −I on H₁(F) and the +1 on the fibration class of m004 (which comes from the H⁰ coinvariants in Wang, not from H¹(F)^{M²} = 0).
- Sym^n is asserted to be a homomorphism before use; ι is asserted to preserve both relators in the faithful representation; G is asserted to conjugate all three generator images.

---

*Record sources: T-θTANGENT (THEOREM_REGISTRY:38), B353, B576, B582, B1086, B1253, B1256, B1267 (its control table; its transpose bug is the reason for the homomorphism assertion here). Literature: Menal-Ferrer–Porti (h¹ = 1 per nontrivial odd symmetric power on the cusped manifold — reproduced); Wang sequence for mapping tori.*
