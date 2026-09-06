# R59 — THE TWISTED CLOSING IS THE SISTER, AND IT KEEPS THE SAME EVEN LINE: no orientable closing of the fiber by the rule, twisted or covered, retains a θ-odd class

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 0ecd9557** · **Status:** seat report, not banked. Exact modulo two primes p ≡ 1 (mod 3); script `computations/r59_twisted_closing.py`. Closes the door R58 §4 named.

## 0. The result

R58 found the fiber's θ-odd sector (6 classes in Sym⁸, 10 in Sym¹⁶, sourced by the three half-periods) and that the monodromy M² fixes only a θ-even line. It asked whether the **θ-twisted closing** — the mapping torus of M²∘ι — keeps an odd class. Two facts first:

- **The twisted closing is the sister.** M²∘ι acts on H₁(F) as −M² = [[−2,−1],[−1,−1]], and det(I + M²) = 5, so the bundle has H₁ = ℤ ⊕ ℤ/5: it is **m003**, the manifold B1224 places at CS = ¼ opposite m004's 0. Its fundamental group is the index-2 subgroup of the orbifold group of m004/ι on which t and ι have equal parity, so its holonomy is the geometric one, restricted from the same fiber representation.
- **Its class is the same line.** On H¹(F; Sym^n) the actions of M² and ι commute (asserted); the (−M²)-fixed subspace is one-dimensional, **θ-even, and identical to the M²-fixed line** — in Sym⁸ and Sym¹⁶, on both primes. M² has **no eigenvalue −1** on H¹(F; Sym^n), so there is no odd vector for the twist to fix.

And for cyclic covers: the invariants of (±M²)^k for k = 1…12 are one-dimensional and θ-even in every case — the same line again — as Menal-Ferrer–Porti predicts (h¹ = 1 per nontrivial odd symmetric power on any one-cusped cover).

> **Every orientable closing of the fiber by a power of the rule, twisted by θ or not, keeps exactly one class per summand, and it is the same θ-even class. The θ-odd sector of the fiber survives none of them.**

## 1. What this means

1. **The sisters are one line.** m004 (CS = 0) and m003 (CS = ¼) differ in the mirror-odd invariant the record has tracked since B1224, but their h¹ classes in the 27 coincide as subspaces of the fiber cohomology and share θ-parity. The ¼ is cusp-local (B1239); it is not a chiral matter class.
2. **The rule is what removes chirality.** On the fiber, θ-odd classes exist and are counted by the three fixed points (R58's Lefschetz identity). Applying the rule — closing along M² in any way — projects onto the M²-invariants, and those are even. This is the mechanism behind R56's zero and R57's "closing erases the endpoints", now with the operator named: **the monodromy has no invariant vector in the θ-odd sector.**
3. **Therefore the generation content of the object, if it has any, lives on the fiber F — the once-punctured torus with its three half-periods — and the rule must act on it as a symmetry, not as a compactification direction.** A frame that reads chiral matter off F (E₆ on a curve, 27s localized at the three θ-fixed points, count = a degree) is the only kind left inside this object's own data. The 3-manifold reading is closed, by computation, in every version the record or these reports have proposed.

## 2. Falsifiers and scope

- Non-orientable closings (mapping tori of ±M, the Gieseking manifold and its twin) are not tested; chirality is not defined there, and the local system needs complex conjugation (a Frobenius over 𝔽_{p²} would do it).
- Non-cyclic covers of m004 are not tested; MFP gives h¹ = (number of cusps) per odd summand, so a cover with several cusps has more classes, and their parities are a finite computation — the natural next test if anyone wants the 3-manifold frame kept alive.
- Subregular embedding (13 + 9 + 5): the same computation with Sym¹², Sym⁸, Sym⁴; not run here. R56 says the count is χ-type regardless, but the parities are cheap to add.

---

*Record sources: B1224 (m003 at ¼), B1239 (¼ cusp-local), T-θTANGENT, B576, B1086. Literature: Menal-Ferrer–Porti; Wang sequence.*
