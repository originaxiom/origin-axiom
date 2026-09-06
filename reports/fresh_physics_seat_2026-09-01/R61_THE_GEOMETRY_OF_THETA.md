# R61 — THE GEOMETRY OF θ ON THE OBJECT: a real structure on two fibers, two arcs pairing the cusp torus's 2-torsion points, and a lemma — every θ-equivariant abelian Higgs configuration has zero net chirality

> **RETRACTION BANNER (R69):** §3's second clause (θ-even ⇒ net 0 by "real representations") is **withdrawn** — u ∈ 𝔣₄ breaks F₄ too, and R_q, R_{−q} are distinct representations of the unbroken group. Charges on Fix(θ) itself are a θ-even equivariant configuration with **net = ±2** (the two arcs have χ = 2). The first clause (θ-odd ⇒ 0) stands. See `R69_ARCS_CUT_CORNERS.md`.

**Seat:** fresh physics seat (fc) · **Date:** 2026-09-06 · **Against main @ 69a027eb** · **Status:** seat report, not banked. Exact integer arithmetic over ℤ[ω] throughout; script `computations/r61_theta_geometry.py`. Built on R60 (θ = the strong inversion σ: x ↦ x⁻¹, y ↦ y⁻¹ on Riley's presentation; B347/B353 reproduced on this bench).

## 0. What is new here

The record identified θ with a concrete involution (B353) and used its **signs** on the six tangent lines. Its **geometry** on the object — what it does to the fiber, to the cusp, and where its fixed set lies — had not been written down. Three exact facts, and one consequence that is a two-line lemma once they are in hand.

## 1. θ on the fiber: a real structure that inverts the rule

Transporting σ to the fiber generators (a = xy⁻¹, b = yxy⁻¹x⁻¹yx⁻¹, t = x, with φ(a) = aba, φ(b) = ab) and re-expressing the images as fiber words (search, exact):

```
σ(a) = t⁻¹ · (a⁻¹ b a⁻¹ b b) · t        σ(b) = t⁻¹ · (a⁻¹ b a⁻¹ b a) · t
```

so σ maps the fiber F₀ to the fiber F_{−1} (it reverses the base circle; two fibers are fixed setwise) and induces on H₁(F) = ℤ²

```
σ* = [[−2, −1], [3, 2]],   det σ* = −1,   σ* M² σ*⁻¹ = M⁻²  (checked: [[1,−1],[−1,2]])
```

**θ is orientation-reversing on the fiber and conjugates the monodromy to its inverse** — an anti-holomorphic involution of the once-punctured torus compatible with the rule. In the language the record has already earned (I-2, B150: the fiber is the class-S curve of N = 2\* SU(2), the trace-map action its S-duality), **θ is a real structure on the N = 2\* curve that sends the duality element M² to M⁻².** That is the geometric content behind "θ-odd is chiral": θ is a reflection of the curve, not a symmetry of the fibration.

## 2. θ at the cusp: the lattice, the four points, the two arcs

- **Cusp lattice, exact.** The fiber boundary [a,b] is parabolic (trace −2); conjugated to the cusp at ∞ by ρ(yx⁻¹y⁻¹) it is the translation by **τ = 2 + 4ω = 2√3 i**. So the cusp torus is ℂ/(ℤ + ℤ·2√3 i), reproducing SnapPy's cusp shape from the group alone.
- **θ on the cusp torus.** σ is z ↦ −z on ℂ (its conjugator is diag(−1,1)); on ℂ/Λ it is the hyperelliptic involution of the *cusp* torus with fixed points the four 2-torsion points **{0, ½, τ/2, (1+τ)/2}**.
- **The arcs.** Every involution in the coset Γ·σ has det −1 and trace 0, so its axis discriminant is 4 and **both endpoints are cusp points**: Fix(θ) has no closed component (consistent with Smith theory for the extension to S³). Transporting each axis end into the cusp torus and enumerating coset involutions up to word length 6:

| involution | arc endpoints on ℂ/Λ |
|---|---|
| σ | **0 ↔ τ/2** |
| ρ(x)·σ | **½ ↔ (1+τ)/2** |
| every other coset involution tested | one of the two pairs above |

**Fix(θ) is exactly two arcs, χ = 2, and the pairing is "vertical": each 2-torsion point is joined to its translate by τ/2.** Not to its translate by ½, and not diagonally. This is a new invariant of the object's chirality switch, and it is a definite one (the wrong pairings were produced by two bookkeeping errors in the first run and are recorded in the script's history, not here).

## 3. The lemma: θ-equivariance forces zero net chirality on the cusped object

In the Pantev–Wijnholt frame (R56), for an abelian Higgs field φ = f·u with u a generator in 𝔢₆ and f a function on the object, the net chirality of a charged component is `χ(∂⁻) − χ(∂⁺)`, with ∂± ⊂ the cusp torus the regions where f exits/enters (χ(M) = 0 for the object). Suppose the configuration is **θ-equivariant** — invariant under the object's own symmetry σ up to the gauge action of θ (the natural condition for a configuration *supplied by the object*). Then, because 𝔢₆ = 𝔣₄ ⊕ 26 with θ = ±1:

- **u ∈ 26 (θ-odd):** equivariance forces f∘σ = −f. Then σ maps ∂⁺ onto ∂⁻, so χ(∂⁺) = χ(∂⁻) and **net = 0**. Moreover f vanishes at the four σ-fixed points of the cusp torus with **vanishing Hessian** (an odd function at an isolated fixed point of z ↦ −z has no even-order Taylor terms), so the localized zero-modes there are **degenerate**, outside Morse counting.
- **u ∈ 𝔣₄ (θ-even):** the unbroken group contains an F₄-type subalgebra and every charged component comes with its conjugate in a **real** representation (26 = 26̄), so net(R) = −net(R̄) = −net(R) = 0.

> **Any θ-equivariant abelian Higgs configuration on the object has zero net chirality. A nonzero count requires breaking the object's strong inversion.**

This is the strong-inversion analogue of **B1227** (amphichiral ⇒ the mirror is a self-isometry ⇒ mirror-odd invariants satisfy 2I = 0). It says, in the record's terms, that the chirality *bit* is σ-breaking, exactly as the mirror bit is amphichirality-breaking — and it is why the record's "closing supplies the bit" line (C22) is structurally right: a closing that breaks σ can carry a count; the object, which has σ, cannot. It does not say what the count is.

## 4. What this leaves, precisely

1. **The three θ-odd classes (R60)** are θ-odd *deformation directions* of a σ-symmetric point; by §3 they carry no net count on the object itself. The record's "1 abelian + 2 chiral" and this seat's earlier "3 θ-even" are both replaced by: **three θ-odd directions, net zero, by symmetry.**
2. **Where a count could live:** a σ-breaking configuration on the object, or a closing that breaks σ. The natural candidates are σ-breaking boundary conditions at the cusp — regions ∂⁺ not mapped to ∂⁻ by z ↦ −z. The four 2-torsion points and their vertical pairing are the only σ-structure the cusp offers; three σ-invariant disks centered at three of the four 2-torsion points would give χ(∂⁺) = 3 for a θ-**even** field — but then §3's second clause (real representations) kills the count. A θ-**odd** field cannot have σ-invariant regions. So on the object there is no σ-compatible way to three, and the choice of a σ-breaking one is the observer's (H5). This is stated as the negative it is.
3. **The class-S reading** (§1) puts the question in a frame where it is standard: E₆ (2,0) on the fiber with the rule as a duality twist and θ as a real structure is an N = 2 theory (vector-like) with an orientifold-type twist; a chiral N = 1 theory from a curve needs the normal-bundle split (the "N = 2 → N = 1 datum" the record fenced at B277/B292 as wall #3), which on a punctured torus is an integer the object does not fix. Cited as the record's own wall; the reading of it as a line-bundle degree is this seat's proposal, unverified.

## 5. Verified here / cited

| statement | status |
|---|---|
| σ(a), σ(b) as fiber words; σ* on H₁(F) with det −1; σ*M²σ*⁻¹ = M⁻² | **computed, exact** |
| longitude [a,b] parabolic; τ = 2+4ω; Λ = ℤ + ℤ·2√3 i; matches SnapPy's cusp shape | **computed, exact** |
| every coset involution has cusp endpoints (disc = 4) | **computed** (and forced: det −1, tr 0) |
| the two arcs and their endpoint pairs on ℂ/Λ; all tested coset involutions land on them | **computed, exact**, words ≤ 6 |
| Fix(θ) ⊂ S³ is a circle meeting the knot twice (no closed component in the complement) | Smith theory + SnapPy "extends to link" — **cited theorem, consistent with the computation** |
| the lemma of §3 | elementary, given R56's formula and 𝔢₆ = 𝔣₄ ⊕ 26 (B351, re-run on this bench in R60) |
| I-2 (fiber = N=2\* class-S curve; trace map = S-duality) | **cited** from the ledger (EARNED, B150); not re-derived here |
| wall #3, the N=2 → N=1 datum | **cited** (B277 via B292) |

*Owner's rules applied: no old banking used as a wall (the only bankings cited are the ones re-run in R60 and the EARNED I-2 row); the record was searched before each claim of novelty (the vertical pairing and the lemma do not appear in it; "strong inversion" appears nowhere in `frontier/` or `docs/`).*
