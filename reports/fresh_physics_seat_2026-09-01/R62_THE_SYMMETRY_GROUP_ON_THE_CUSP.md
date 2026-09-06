# R62 — THE SYMMETRY GROUP ON THE CUSP, EXACTLY: the mirror is broken by every hyperbolic filling, the strong inversion by none — so no closing in the record's family ever breaks θ

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 69a027eb** · **Status:** seat report, not banked. Exact over ℤ[ω]; script `computations/r62_cusp_actions.py`. Continues R61.

## 0. The result

The object's symmetry group D₄ acts on the cusp torus ℂ/Λ, Λ = ℤ + ℤτ, τ = 2 + 4ω = 2√3 i (R61), as follows — each line computed from the group, not read off SnapPy:

| symmetry | on ℂ (cusp at ∞) | on H₁(T²) = (meridian, longitude) | fixed points on the cusp torus |
|---|---|---|---|
| ι (period-2 rotation, the fiber's −I) | z ↦ z + τ/2 | +I | none |
| σ (strong inversion = **θ**, B347/B353) | z ↦ −z | −I | {0, ½, τ/2, (1+τ)/2} |
| σ′ = σ∘ι (the other strong inversion) | z ↦ −z − τ/2 | −I | {τ/4, 3τ/4, ½+τ/4, ½+3τ/4} — the quarter points |
| m (mirror; x ↦ x, y ↦ yxy⁻¹, conjugator z ↦ z̄ + 1 + ω) | z ↦ z̄ + (1+ω) | diag(1, −1) | — (orientation-reversing) |

Consequences for Dehn filling slopes s = p/q on this cusp:

- **σ and ι fix every slope** (−I and +I on H₁(T²)). Since −I on ∂(D²×S¹) is the restriction of (w, e^{iφ}) ↦ (w̄, e^{−iφ}), **θ extends over every Dehn filling of the object.**
- **m fixes only 1/0 and 0/1** ((p,q) ↦ (p,−q) is ±(p,q) iff pq = 0). The record already knew this in another guise — B1239 §3: *"only two invariant slopes exist"* — and the explicit slopes agree.

> **Every hyperbolic filling with an isometry group inherited from the object breaks the mirror (the CS bit) and keeps the strong inversion (the θ bit).** B432's *"31/31 fillings chiralize"* is the generic case of a theorem — for all but finitely many slopes, Isom(M(s)) is the stabiliser of s in Isom(M) (Thurston's hyperbolic Dehn surgery; cited) — and by R61's lemma the same filling can never supply a θ-breaking configuration: the closed manifold still carries σ, and any σ-equivariant abelian Higgs configuration on it has zero net chirality (which on a closed manifold R56 already forces for every configuration).

So the record's C22 — *"the closing supplies the bit"* — is exactly right for the mirror bit and exactly wrong for the fermion-chirality bit. **The two "chiral"s in the record are two different symmetries: amphichirality is broken by closing; the strong inversion is not.**

## 1. The geometric picture, consistent three ways

- ι translates the cusp torus by τ/2, and R61's two σ-arcs join **0 ↔ τ/2** and **½ ↔ ½+τ/2** — i.e. each arc joins a σ-fixed point to its ι-image. So **ι maps each σ-arc to itself, reversing it**, and its fixed geodesic crosses each σ-arc at the arc's midpoint. Likewise for σ′'s two arcs at the quarter points.
- ι is fixed-point-free on the cusp torus (a translation), fixed-point-free on the base direction, and fixes the three half-periods of each fiber (R57; a special case of **B366's puncture lemma**, which the record already has: SL(2,ℤ) fixes only the origin of the fiber's 2-torsion and cycles the other three).
- σ reverses the base and is a real structure on the two fixed fibers (R61 §1); its arcs each lie in one of those fibers? Not asserted — the arcs' fibers were not computed here.

## 2. What is new, what is the record's

| statement | status |
|---|---|
| ι = translation by τ/2 on the cusp torus; σ′'s fixed points at the quarter points | **new, computed** |
| the mirror's automorphism x ↦ x, y ↦ yxy⁻¹ and its conjugator; action diag(1,−1) | **computed** (the automorphism is surjective because the image generates a conjugate of the Galois-conjugate group, of the same covolume) |
| mirror-invariant slopes are exactly 1/0 and 0/1 | **computed**; agrees with B1239 §3 |
| σ fixes every slope and extends over every filling | **new**, elementary once σ = −I on the cusp |
| B432's 31/31 as the generic case of a theorem | the theorem is Thurston's; the reading is new; **the finitely many exceptional slopes are not examined here** |
| R57's 3-cycle on the half-periods | **the record's B366 puncture lemma** — credited |

## 3. What it means for the programme

The record has been looking for the chirality bit in the closing since B432. The closing family it uses — Dehn fillings — is invariant under the very involution that the record's own dictionary (B353, B576) identifies as the chirality switch. Nothing in that family can break θ. R61's lemma says θ-equivariant configurations carry no net count; so **the generation count cannot come from a filling, at any slope**. If it comes from anywhere in this object's world, it comes from a σ-breaking structure — a covering that does not lift σ, a boundary condition on the cusp that is not −z-symmetric, or an ambient 7-manifold in which the E₆ locus meets conical points off the σ-axis. Each of those is an input. That is H5 with the symmetry named.

---

*Computed on this bench (exact): the four cusp actions, the arc–translation consistency, the mirror automorphism and conjugator, the slope stabilisers. Cited: Thurston's Dehn surgery theorem (isometries of generic fillings), Smith theory (R61), B1239 §3, B366's puncture lemma, B432.*
