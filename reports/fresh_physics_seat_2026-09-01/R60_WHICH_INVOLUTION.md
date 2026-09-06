# R60 — CORRECTION: the record's θ is the meridian-reversing involution (B347/B353), not the fiber's −I; R57 fact (3), R58 §2–§4 and R59 are retracted as statements about θ

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 69a027eb** · **Status:** seat correction, on the owner's instruction *"before you push false incompatibility, search the repo, fetch it — we already derived them."* Exact modulo two primes; script `computations/r60_which_involution.py`.

## 0. What I got wrong, and how

R57–R59 rested on one reading: THEOREM_REGISTRY's T-θTANGENT says θ *"is realized by the hyperelliptic involution (B353)"*, and I took "hyperelliptic" to mean the once-punctured-torus fiber's −I ∈ SL(2,ℤ) — the meridian-**preserving** period-2 symmetry whose fixed points are the three half-periods. **I did not open B347 to see which automorphism it used.** B347's involution is `a→a⁻¹, b→b⁻¹` on the SnapPy census presentation `⟨a,b | ab³aBA²B⟩`. Abelianising that relator: a: +1+1−1−1 = 0 and b: +3−1−1 = +1, so **b is trivial in H₁ and a generates H₁ = ℤ** (a is meridian-class, b lies in the commutator subgroup). Inverting a acts by −1 on H₁: the involution reverses the meridian class, and B347 verifies it is ℂ-linear (orientation-preserving). By §5 below that makes it a **strong inversion**. *(B347's own parenthetical calls it "the fibre-torus hyperelliptic involution"; the computation is of the strong inversion, and it is that label — not the computation — that misled me.)* The fiber's −I acts by +1 on H₁. They are different elements of the symmetry group D₄, and the record's computation (B347 numerically, B351 exactly on the algebra, B353 gauge-certified at the deformation complex) is about the strong inversion. **The record is right. My R58/R59 computed a different involution and called it θ.**

## 1. Both involutions, computed on one bench (Riley's presentation ⟨x,y | xyXYxYXyxY⟩)

| coefficient Sym^{2m} | m | record's θ = strong inversion `x→x⁻¹, y→y⁻¹` | fiber −I transported (`x→xyx⁻¹, y→xy⁻¹xyx⁻¹`) | B347 banked |
|---|---|---|---|---|
| Sym² | 1 | **+1** | +1 | + |
| Sym⁸ | 4 | **−1** | +1 | − |
| Sym¹⁰ | 5 | **+1** | +1 | + |
| Sym¹⁴ | 7 | **+1** | +1 | + |
| Sym¹⁶ | 8 | **−1** | +1 | − |
| Sym²² | 11 | **+1** | +1 | + |
| Sym⁰ | 0 | **−1** | +1 | — |
| Sym⁴ | 2 | **−1** | +1 | — |
| Sym⁶ | 3 | **+1** | +1 | — |
| Sym¹² | 6 | **−1** | +1 | — |
| Sym¹⁸ | 9 | **+1** | +1 | — |
| Sym²⁰ | 10 | **−1** | +1 | — |

- **B347's table is reproduced exactly** on a different presentation with an independent implementation (exact mod p, not mpmath): (+,−,+,+,−,+). The pattern `(−1)^{m+1}` holds at every m tested, including the non-exponents.
- The fiber's −I is **+1 on every line**. It is a symmetry of the object, but it is not θ.

## 2. The corrected physics reading

Under the record's θ, the three h¹ classes of the 27 under the principal embedding — Sym¹⁶, Sym⁸, Sym⁰ (m = 8, 4, 0) — are **all θ-odd**. So are the subregular's Sym¹², Sym⁸, Sym⁴ (m = 6, 4, 2). **R58's headline ("all three classes are θ-even") is false; the truth is the opposite sign.** In B576's dictionary (θ-odd ⇒ full-E₆ closure, chiral) the classes are on the chiral side — which is the reading the record already had, and which my R58 wrongly "refuted."

What θ-oddness does **not** change: net chirality `h¹(27) − h¹(27̄)` is zero. Under the principal embedding this is not even a computation: each Sym^n is self-dual, so 27̄ restricts to the same three summands and h¹(27̄) = h¹(27) = 3 termwise (E65, B1260, B1267). *(B1273 lists the SM-derivation seat's exact ℚ(ω) confirmation as harvested, **not verified on main**; I do not cite it as verified.)* A θ-odd class is a chiral *deformation direction*; it is not a nonzero *index*. R56's endpoint theorem is untouched by this correction.

## 3. What is retracted, what stands

**Retracted (as statements about θ):**
- **R57 fact (3)** — "θ fixes exactly three points per fiber." θ = the strong inversion; its fixed set is the axis meeting the knot in two points, i.e. **two arcs** from the cusp to the cusp (χ = 2), not the three half-periods.
- **R58 §2–§4** — the "all even" result, the "1 abelian + 2 chiral typing refuted" sentence, and the "opens" paragraph. The computation in R58 is a correct computation *about the period-2 involution ι*, which is not θ.
- **R59** — "the θ-twisted closing"; the twist there is by ι, not θ. As a statement about ι it stands (the sister m003 is the mapping torus of −M², and ι-fixed lines coincide); as a statement about θ it is void, since θ reverses the base and is not a mapping-torus twist at all.
- **The journey's generation note** and my last two messages to the owner where they repeat these.

**Stands:**
- **R56** in full (the endpoint theorem, the χ-accounting, the codimension gap, the two-sl₂ finding — the last now moot for chirality by §2 and by B1274's collapse of I-25 to the subregular).
- **R57 facts (1), (2), (4)**: the rule is the 3-braid σ₁σ₂⁻¹; the object is the closure of (σ₁σ₂⁻¹)² and of no 2-braid (braid index 3); M² permutes the three half-periods in a 3-cycle, so the **period-2 involution ι** has fixed set one closed geodesic meeting every fiber three times. The three half-periods are a real, listed structure of the object; they are the fixed points of ι, not of θ.
- **R58 §3 and R59 as facts about ι**: the fiber's ι-odd sector (6 in Sym⁸, 10 in Sym¹⁶) is sourced by the three half-periods (Lefschetz), and every closing by ±M² keeps one ι-even line — a correct statement about the period-2 symmetry.
- **This bench's reproduction of B347**, which is now an independent second implementation of a banked result.

## 4. The lesson, in the record's own terms

E65's rule was *"before building on a frame, ask what the frame provably cannot produce."* The rule I broke is older: **sweep before you name.** The word "hyperelliptic" in T-θTANGENT was a pointer to an arc, and I substituted my own referent for it without opening the arc. Three reports were built on the substitution. The cost is three retraction banners and one corrected journey note; the gain is a second-implementation confirmation of B347 and a clean separation of the object's two involutions, which the record had not written down side by side: **θ = the meridian-reversing strong inversion (fixed set: two arcs, χ = 2); ι = the meridian-preserving period-2 rotation (fixed set: one geodesic, three points per fiber, χ = 0).**

---

*Record sources: B347 (`e6_tangent_gradings.py:210–212, 288–294`; presentation `abbbaBAAB`), B351 (vi), B353 (A)–(C), T-θTANGENT, B576, B1272 (the exact h¹(27) = h¹(27̄) confirmation), B1274. Owner's instruction, verbatim in spirit: fetch and search before claiming an incompatibility.*

## 5. Verified, not assumed — the owner's *"don't take anything for granted"* pass

Every load-bearing statement above was re-derived on this bench after the first draft; nothing rests on a quoted arc.

| claim | how it was verified here | result |
|---|---|---|
| B351's exact 𝔢₆ and θ | ran `exact_e6.py` from main | 36 positive roots; Jacobi **0 violations / 76,076** triples; principal c = (16,22,30,42,30,16); θ automorphism, involution, fixed dim **52**, (−1)-dim **26**; θ on exponent lines **{1:+, 4:−, 5:+, 7:+, 8:−, 11:+}** |
| B347's tangent dims and signs | ran `e6_tangent_gradings.py` from main | rep residual 8e-71; dims **1,1,1,1,1,1**; amphichiral J² all +1; hyperelliptic signs **{+,−,+,+,−,+}** |
| B353's operator-level identification | ran `geometric_theta.py` from main (B351+B352+B347 machinery) | θ_chain = ⊕(−1)^{m+1}Id, residual **7.1e-102**; [θ, Ad ρ] residual 1.8e-88; per-line certificates λ = ±1 to 1e-65, residuals ≤ 1e-72 |
| my σ reproduces B347 on a different presentation and implementation | exact mod 10009 and 100003, Riley's ⟨x,y⟩ | **{+,−,+,+,−,+}** at m = 1,4,5,7,8,11; `(−1)^{m+1}` also at m = 0,2,3,6,9,10 |
| the fiber's −I is not θ | same machinery | **+1 on every line** tested (m = 0…11) |
| which symmetries are orientation-preserving | SnapPy 3.x `symmetry_group().isometries()` on m004 | 8 isometries; cusp-torus actions **+I, +I, −I, −I** (orientation-preserving: identity, ι, two strong inversions) and **diag(−1,1), diag(1,−1)** ×2 (orientation-reversing); all "extend to link" |
| σ reverses the meridian; ι preserves it | H¹(m004; ℚ) sign: σ → **−1**, ι → **+1** (n = 0 rows) | consistent with the cusp table |
| the two strong inversions have the same parities | computed σ∘ι directly | **−, +, −, −** at n = 0, 2, 8, 16 — identical to σ |
| σ's fixed component is an arc to the cusp | exact over ℚ(√−3): conjugator **G_σ = diag(−1, 1)**, i.e. z ↦ −z; axis from **0 to ∞** | both endpoints are cusp points of Γ (one cusp, class number 1) ⇒ **arc** |
| ι's fixed component is a closed geodesic | exact: G_ι = [[−1, −ω],[−1, 1]] up to scale; axis discriminant 2+2√3 i, minimal polynomial of its square root **z⁴ − 4z² + 16** (degree 4) | endpoints ∉ ℚ(ω) ⇒ **closed geodesic**; with R57's 3-cycle, one component meeting each fiber 3 times |
| θ's fixed set is exactly two arcs, χ = 2 | σ acts as −I on the cusp torus ⇒ 4 fixed points on ∂; σ extends to S³ (SnapPy); Smith theory: Fix(σ) ⊂ S³ is a circle; 4 boundary points ⇒ the circle meets the knot twice ⇒ **2 arcs**, no closed component | **χ = 2** |
| h¹(27̄) = h¹(27) under the principal embedding | Sym^n self-dual ⇒ termwise | **3 = 3**, trivially |

What remains cited rather than re-derived: that the E₆ → F₄ folding's fixed algebra has the F₄ exponents {1,5,7,11} (standard, and B351's run above exhibits it), and Smith theory for involutions of S³ (a theorem).

*Scripts: `computations/r60_which_involution.py` (mod-p parities, all three involutions), `computations/r60_exact_conjugators.py` (exact conjugators and axes).*
