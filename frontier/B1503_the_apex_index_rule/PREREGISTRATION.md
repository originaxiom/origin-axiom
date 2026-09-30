# B1503 PREREGISTRATION — THE APEX INDEX RULE: at a G₂ cone point over a finite quotient of a nearly Kähler manifold, what do the singular loci through the point owe each other?

**Sealed 2026-09-30, before the rule is evaluated on the census. Seat: cc (the SM-derivation branch). Occasion: B1502 §5 and the
owner's go of 2026-09-29.**
B1502 found that neither half of the anomaly criterion forces chirality at the apex of B1501's two torus models. Its §5 added the cubic
half (Witten, hep-th/0108165 §3): on an SU(N) locus the normal U(1) twist L forces, at a point P of the locus, charged fields with
SU(N)³ anomaly n_P = deg(L) on the link of P. This arc asks what the link's own geometry says about those degrees, for all the loci one
symmetry fixes at once.

## The rule (proved now)

**Setting.** Y is a compact nearly Kähler 6-manifold with its SU(3)-structure (g, J, ω, Ω). γ ≠ 1 is an automorphism of finite order
of that structure. C(Y)/⟨γ⟩ is a G₂ cone point, and its singular loci are the cones over the components of Fix(γ).

**Fixed sets.** dγ commutes with J and lies in SU(3) on each tangent space it fixes. So Fix(γ) is a disjoint union of:
- isolated points p, where dγ has eigenvalues e^{iθ_j(p)} (j = 1, 2, 3) on T^{1,0}, none equal to 1, with product 1;
- closed J-holomorphic curves C, where dγ has eigenvalues (1, e^{iθ_C}, e^{−iθ_C}) on T^{1,0}.
On a curve with θ_C ∉ πℤ, the normal bundle splits into J-complex lines N₁ (eigenvalue e^{iθ_C}, 0 < θ_C < π) and N₂ (e^{−iθ_C}), of
degrees d₁ and d₂. Write Δ_C = d₁ − d₂.

**Theorem (the apex index rule).** For every such γ:

  Σ_p Π_{j=1}^{3} (1 − e^{−iθ_j(p)})^{−1} + Σ_C (i/8) cot(θ_C/2) sin^{−2}(θ_C/2) Δ_C = 0,

the second sum over the curves with θ_C ≠ π (a curve with θ_C = π contributes 0).

**Proof.**
- (1) Y is spin (the SU(3)-structure) and Einstein with positive scalar curvature, so the spin Dirac operator D has no kernel
  (Lichnerowicz). Hence its equivariant index vanishes for every lift of γ.
- (2) γ preserves the SU(3)-structure, so it lifts through SU(3) ⊂ Spin(6), and S ≅ Λ^{0,*} ⊗ K^{1/2} with K trivialised by Ω.
  D has the symbol of the Dolbeault–Dirac operator on Λ^{0,*}, with the same γ-action. The equivariant index depends only on the
  equivariant symbol class, so D's equivariant index is the holomorphic Lefschetz number of the almost complex manifold.
- (3) Atiyah–Singer (III, §4; the formula depends only on the symbol, so it holds for almost complex manifolds): that number is
  Σ_F ∫_F Td(TF) Π_θ ch_γ(λ₋₁N_θ*)⁻¹, where ch_γ(λ₋₁N_θ*) = Π_j (1 − e^{−iθ}e^{−x_j}) for
  the Chern roots x_j of the e^{iθ}-eigenbundle N_θ of the normal bundle. An isolated point gives Π_j (1 − e^{−iθ_j})⁻¹.
- (4) A curve C gives ∫_C (1 + c₁(TC)/2)(1 − e^{−iθ}e^{−x₁})⁻¹(1 − e^{iθ}e^{−x₂})⁻¹. Since c₁(Y) = 0 (Ω), x₁ + x₂ = −c₁(TC), and the
  χ(C) terms cancel. What is left is (i/2) cot(θ/2) (d₁ − d₂) / (4 sin²(θ/2)), which is independent of the genus. ∎

**Witten's inflow.** On a curve C with transverse group ℤ_N (N the order of e^{iθ_C}, N ≥ 3), the twist L of B1502 §5 has degree
n_C = (N/2) Δ_C.
- N₁ ⊗ N₂ carries the SU(2)_L part of the normal structure (the spin connection of the locus), and N₁ ⊗ N₂* carries Λ′ with weight
  2/N.
- So each curve enters the rule through its cubic inflow, with the weight (i/4N) cot(θ/2) sin^{−2}(θ/2).

**Consequences (proved now).**
- **(C1) A lone locus forces nothing.** If Fix(γ) is a single curve C with θ_C ≠ π, then Δ_C = 0 and n_C = 0. This holds on any nearly
  Kähler link, homogeneous or not.
- **(C2) The cusp point.** A torus-linked point is chiral through the cubic half only if the element generating the torus's transverse
  group also fixes isolated points or other curves. Those are cones through the apex: codimension-6 lines or other ADE loci. With B1502
  (the mixed half needs [F] ≠ 0 and a C-field U(1)), a cusp point can be chiral only where its locus meets another fixed locus of the
  same element at the point, or where its torus is homologically non-trivial.
- **(C3) Order two** gives no condition (cot(π/2) = 0), as SU(2) has no cubic anomaly.

## Decided at design time (from the rule and B1501's banked component list)

B1501's census (`census.json`) lists, for each class, its fixed components by type. The classes with fixed points fall into:

| link | points, spheres, tori | classes |
|---|---|---|
| S⁶ | 0, 1, 0 | 23 |
| S⁶ | 2, 0, 0 | 44 |
| S³ × S³ | 0, 0, 1 | 23 |
| S³ × S³ | 1, 1, 0 | 2 (σ, σ²) |
| S³ × S³ | 3, 0, 0 | 6 |
| ℂP³ | 0, 2, 0 | 24 |
| ℂP³ | 2, 1, 0 | 22 |
| ℂP³ | 4, 0, 0 | 49 |
| F₁,₂ | 0, 0, 1 | 2 |
| F₁,₂ | 0, 3, 0 | 45 |
| F₁,₂ | 6, 0, 0 | 66 |

So, by the rule:
- **D1.** S⁶'s 23 single-sphere classes: Δ = 0 on the sphere (C1).
- **D2.** The 25 torus classes: n = 0 (C1). This re-derives B1502 §5 by a route that does not use homogeneity.
- **D3. S³ × S³'s 3-symmetry.** Fix(σ) is the point eΔ and one sphere (banked). At eΔ, T^{1,0} is the ω-eigenspace of σ's differential,
  since J = (2σ + 1)/√3. So all three angles are 2π/3, and the point's term is (1 − ω̄)⁻³ = −i/(3√3). The sphere's normal angle is
  2π/3, since σ has order 3. So the rule forces Δ = 2 on the sphere for σ, and Δ = −2 for σ² (everything conjugates): an SU(3)
  locus with cubic inflow n = ±3, balanced by the isolated point.
  No apex in the record (swept 2026-09-29 and 2026-09-30) has a locus's forced inflow balanced by an isolated fixed point rather than
  by another locus. The census checks this one by computing Δ independently.

## The instrument (fixed now)

- **Elements.** B1501's 694 classes (order ≤ 12, the four links, the listed automorphisms).
- **Fixed components.** Recomputed by B1501's sealed routine: 400 seeds from the class's own seed, damped Newton, one component per
  C(γ)⁰-orbit at 10⁻⁶. The components must match `census.json` in number and type on every class (an identity check).
- **Angles.** At a representative of each component: dγ on T^{1,0} (J the canonical J, constant in the left-translation frame), its
  eigenvalues and eigenlines.
- **Degrees on a sphere, by isotropy weights.**
  - Z spans the stabiliser of the point in the derived algebra of 𝔠(γ), orthogonal to the part that fixes the sphere pointwise.
  - Its weights on the tangent line and on N₁, N₂ give d_j = 2 w_j / w_T.
  - d_j must be integers to 10⁻⁶, with d₁ + d₂ = −2.
- **Degrees on a sphere, by lattice (independent).**
  - The sphere is swept by the complementary su(2) from the point, on a polar grid.
  - N₁ and the tangent line are carried into the ambient space of B1501's embedding.
  - Their lattice Chern numbers (Fukui–Hatsugai–Suzuki) are computed, with the orientation fixed by deg TC = +2.
  - d₁ must equal the weights' value.
- **Degrees on a torus.** d₁ = d₂ = 0: homogeneous, and B1502 §5's lattice value.
- **The check (must pass).** For every class with fixed points, |S| < 10⁻⁸, where S is the rule's left side. If any class fails, the
  instrument or the component list is wrong: the run stops and no census reading is made.
- **Read-outs.** For each curve: N, θ, (d₁, d₂), Δ, n = (N/2)Δ. For each class: the points' sum and the curves' sum separately.

## BANKED IDENTITY:

Before any census class is evaluated, the instrument must reproduce the following. If any fails, the run stops.
- **The formula's controls.** The instrument's own point and curve terms give holomorphic Lefschetz number 1, to 10⁻¹², on:
  - ℂP¹ with z ↦ λz (two points);
  - ℂP² with diag(1, 1, λ): a fixed line with normal O(1) and a fixed point.
  This is for several λ.
- **The lattice routine.** Qi–Wu–Zhang's lower band gives ±1 at |m| = 1 and 0 at |m| = 3 (B1502 §5's control).
- **The structures.** B1501's banked identity, re-run: J² = −1, J orthogonal, and the listed automorphisms preserve J.
- **S⁶'s pairs.** On each two-point class of S⁶, the two terms are opposite (the points are antipodal and J reverses between them).

## Predictions, sealed

- **P1 (ℂP³'s two-sphere classes, 24).** In every class of order ≥ 3, do the two spheres have the same normal angle and Δ = ±2 with
  opposite signs, so that the inflows n = ±N form one bifundamental-type pair? Spheres with θ = π, where Δ is not defined, are
  listed separately and do not count against P1.
  - YES: ℂP³'s cone points carry Acharya–Witten-type chirality in pairs of SU(N) loci meeting at the apex.
  - NO: list the classes and their (θ, d₁, d₂).
  - **Prior: YES, about 65%.**
- **P2 (ℂP³'s one-sphere classes, 22).** In every class, do the two isolated points' terms cancel each other, leaving Δ = 0 on the
  sphere?
  - **Prior: YES, about 75%.**
- **P3 (F₁,₂'s three-sphere classes, 45).** Is Δ = 0 on every sphere?
  - **Prior: YES, about 80%.**
- **P4 (read).**
  - The full table: per link, the classes with a curve of n ≠ 0, the values of (d₁, d₂) met, and the largest |n|.
  - Whether any class other than the σ-classes balances a curve against isolated points.

## What was seen before this seal (disclosure)

A scratch prototype, not banked and not this instrument, evaluated the rule on 32 census classes drawn at random (seed 7, 8 per
link). 19 of them have fixed points, and on those every sum vanished to 2 · 10⁻¹⁵. It saw:
- S⁶ L(0,1/11): the sphere has (d₁, d₂) = (−1, −1).
- ℂP³ L(3/20,3/20) (two spheres): (0, −2) on both, at opposite angles as labelled. With the canonical labelling that is Δ = ±2 at
  one angle.
- ℂP³ L(0,3/11) and L(0,5/12) (one sphere, two points): (−1, −1), and the points' terms cancel.
- F₁,₂ L(2/27,2/27) (three spheres): (−1, −1) on each.
- The torus classes: 0.
The priors above are set knowing these single instances. The prototype's degrees came from isotropy weights in the full derived
algebra, after one correction; its point terms used the Todd form. The lattice check did not exist then.

## Fences

- **Links and groups.** B1501's homogeneous nearly Kähler links and its cyclic classes (order ≤ 12, the listed automorphisms). For a
  larger finite Γ the rule holds element by element (the theorem). The census covers every element of order ≤ 12.
- **The reading.** Witten's n is read for A-type loci with N ≥ 3. The isolated points' terms have no established physical reading:
  their cones are codimension-6 lines, for which Acharya–Witten have "no known useful description".
- **Not covered.** The mixed half of the criterion, and torsion data.
- No physics is crossed. 0 of 19.

## PRIOR ART:

**The design-time sweep (2026-09-29, re-checked 2026-09-30).**
- **The record.**
  - This branch, main (`987c0c8f`) and the audit lane (`b72c6ae1`), fetched 2026-09-29 and again 2026-09-30 (unchanged), have no hit
    for an index or Lefschetz identity at a G₂ cone point.
  - B1355, B1356 and B1360 use Witten's *global* sum rule, ∑_α ∫_{U_α} w = 0 over the apexes of a compact closing (the mixed half), a
    different statement.
  - B1391 and B1396 use holomorphic Lefschetz on other objects.
- **The literature.**
  - Witten (hep-th/0108165): the inflow and n_α.
  - Acharya–Witten (hep-th/0109152).
  - Bilal–Metzger (hep-th/0303243): local cancellation per singularity, with n_α as Witten's, and no identity among loci.
  - Berglund–Brandhuber (hep-th/0205184): chiral matter where intersecting D6 stacks meet at a cone apex (the physical picture of P1).
  - Anguelova–Lazaroiu (hep-th/0208177).
  - Atiyah–Singer III (the Lefschetz formula); Lichnerowicz; Fukui–Hatsugai–Suzuki (the lattice Chern number).
  - The sweep found no statement of this rule. **No novelty is claimed.** The ingredients are standard.
