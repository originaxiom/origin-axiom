# B1505 — THE ORBIFOLD LINKS: in the known G₂ cones whose links are orbifolds but not global quotients, no ADE locus is a cone over a torus of constant type, so none can model a cusp point. The twistor family's loci are spheres, and quotienting by isometries adds no torus of constant type: a toric self-dual Einstein orbifold's only torus-shaped fixed sets cross its orbifold locus. A torus locus in that family could only arrive as one of two oppositely chiral sections.

**Date:** 2026-09-30 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's approval of B1505, the census of G₂ cones
whose links are orbifolds but not global quotients. B1503's rule covers only finite quotients of smooth links, and B1504 showed the
architecture itself supplies no chiral end, so a chiral cusp point would need such a model. · **Status:**
- PROVED: T1–T5 (§2), decided at design time.
- COMPUTED: the census of toric data, the curvature identity on explicit metrics, the pairing, Hitchin's family and AW's §2 family
  (§3–§5), own code.
- Not sealed. The question closed at design time as a theorem, so there was no open outcome to seal. This follows the record's rule
  for such arcs (B1396, B1500, B1502, B1504).

**Fence:** the known class (§1); "a cusp point's model" means an ADE locus coned over a closed torus of constant transverse type
(B1501's standard); the G₂ metrics of AW's §2 family are argued by duality, not constructed. · **Price:** unchanged, 0 of 19 ·
**Numbering:** B1505.

## 0. Seen from above

B1503 proved that on finite quotients of smooth nearly Kähler links a lone locus forces nothing. Outside that class a lone locus can
be chiral: Witten's cone over WCP³_{N,N,1,1} (B1503 C4). A cusp point needs an ADE locus coned over a torus. So the question was:
does any known G₂ cone over an orbifold link that is not a global quotient have a torus locus, and could it be chiral on its own?

The known class has three parts:
- **(A)** Acharya–Witten §2: cones over WCP³_{n,n,m,m}/ℤ_r. The G₂ metrics are argued by heterotic duality, not constructed.
- **(B)** Acharya–Witten §3: cones over the twistor space Z(M) of a compact self-dual Einstein 4-orbifold M of positive scalar
  curvature. The metrics are explicit. The known M are every toric one (up to orbifold covering a quaternion-Kähler torus quotient,
  by Calderbank–Singer's Theorem A) and Hitchin's SO(3)-invariant family.
- **(C)** Quotients of (B) by finite groups of orientation-preserving isometries of M.

The answers:
- **The twistor family's loci are spheres or sections over fixed surfaces (T1).** A locus through the apex is a cone over a twistor
  fibre (a sphere) or over one of the two sections above a surface that an isometry or a local group of M fixes. For toric M this is
  Anguelova–Lazaroiu's list: horizontal spheres over the polygon's edges, vertical spheres over its vertices.
- **A curvature identity (T2).** A totally geodesic surface F in a self-dual Einstein orbifold has
  e_orb(N_F) = χ_orb(F) − s·area_orb(F)/24π. So a totally geodesic torus in positive curvature has a twisted normal bundle, e < 0.
- **No toric orbifold has a fixed torus of constant type (T3).** An isometry of a compact positive toric self-dual Einstein orbifold
  fixes pointwise only spheres, or a "real locus" (the isometry covers the identity of the orbit polygon and acts on the torus by −1).
  - A real locus has χ = 4 − k, where k is the number of edges.
  - At k = 4 it has χ = 0, but it passes through every torus-fixed point and every exceptional surface.
  - For k ≥ 4 the orbifold is not smooth (Hitchin), so the real locus always meets the orbifold locus, where the isotropy jumps.
- **A torus section is never alone (T4).** The two sections over a fixed surface F carry opposite cubic inflows ±(N/2)(2e − χ). For a
  torus that is ±N·e(N_F), nonzero by T2 and opposite in sign: two partners, not a lone locus.
- **AW's §2 family has only spheres (T5).** Its strata are the two coordinate lines and points. Hitchin's family fixes only 2-spheres
  and carries an RP² stratum.

The answer to the approved question: none of the known orbifold links can model a cusp point. With B1501–B1503 for the global
quotients, no known G₂ cone supplies a chiral cusp point. A positive would need a positive self-dual Einstein 4-orbifold (non-toric,
by T3) with a torus fixed by an isometry away from its orbifold locus. There T2 and T4 would make the torus's two sections oppositely
chiral. Or it would need a nearly Kähler orbifold outside the twistor and AW families.

## 1. The class, and what it rests on

- **Acharya–Witten, hep-th/0109152.**
  - §2: X = X̂/U(1)′, with X̂ a hyperkähler quotient cone and U(1)′ preserving its hyperkähler structure. The cone over WCP³_{n,n,m,m}
    (divided by ℤ_r when gcd(p, q) = r > 1) carries SU(p) × SU(q) with chiral bifundamentals at the apex. The G₂ metric is "argued"
    by duality ("we do not know how to actually construct a G₂ metric on X̂/U(1)").
  - §3: U(1) inside the SU(2) that rotates the complex structures. The quotient is the cone over the twistor space Y of a self-dual
    Einstein orbifold M, and its G₂ metric is explicit ((3.1); Bryant–Salamon, Gibbons–Page–Pope). M = WCP²_{q₁,q₂,q₃} is the
    Galicki–Lawson family. The loci are spheres: two sections over each orbifold CP¹ of M, and twistor fibres over its vertices.
- **Anguelova–Lazaroiu, hep-th/0204249.** The toric case in full. Every locus of Y is a horizontal sphere Y_e (the lift of the sphere
  over an edge e of the polygon) or a vertical sphere Y_j (a fibre over a vertex).
- **Calderbank–Singer, math/0405020.**
  - Theorem A: every compact self-dual Einstein 4-orbifold of positive scalar curvature with a 2-torus of isometries is, up to an
    orbifold covering, a quaternion-Kähler quotient of ℍP^{k−1} by a (k−2)-torus.
  - Theorem B: its exceptional surfaces are totally geodesic, with [S̄_j]² = Δ_{j−1,j+1}/(Δ_{j−1,j}Δ_{j,j+1}) and
    χ_orb(S̄_j) = (Δ_{j−1,j} + Δ_{j,j+1})/(Δ_{j−1,j}Δ_{j,j+1}).
  - Any compact totally geodesic 2-suborbifold Σ of such an orbifold has Σ·Σ < χ_orb(Σ).
  - The metric is unique up to homothety for given isotropy data, so every combinatorial symmetry of the data is realized by an
    isometry.
- **Calderbank–Pedersen, math/0105263, (1.1).** The explicit metric from a hyperbolic eigenfunction F; here F is the positive
  multipole Σᵢ √(aᵢ²ρ² + (aᵢη − bᵢ)²)/√ρ.
- **Hitchin.** S⁴ and CP² are the only smooth positive self-dual Einstein 4-manifolds, and he gives an SO(3)-invariant orbifold family
  on S⁴ with an RP² stratum.

## 2. The statements

**T1 (where the loci are).** Let Γ be a finite group of orientation-preserving isometries of M. It acts on Y = Z(M) preserving the
nearly Kähler structure, hence on the G₂ cone.
- Let y lie on a 2-dimensional stratum of Y/Γ, and let g be an element of its isotropy. g fixes x = π(y), and Fix_M(g) is 0- or
  2-dimensional near x.
  - If it is a surface F, g rotates N_F by θ ≠ 0. On the twistor fibre over each point of F it acts as a rotation fixing exactly the
    two poles. The locus is one of the two sections Σ± over F: the points ±β with β = e₁∧e₂ − e₃∧e₄ the anti-self-dual form of TF.
  - If x is isolated, g acts on the fibre through its Λ⁻ part: trivially (the whole fibre, a sphere) or with two fixed points (not
    2-dimensional).
- So every locus is a cone over a sphere or over a section Σ± ≅ F. A torus locus exists iff some isometry or local group of M fixes a
  torus.

**T2 (the curvature identity).** Let F be a compact totally geodesic surface in a self-dual Einstein 4-orbifold (W⁻ = 0), with
orthonormal frame e₁, e₂ tangent and e₃, e₄ normal. Write e₁∧e₂ = α + β with α ∈ Λ⁺, β ∈ Λ⁻ and |α|² = |β|² = ½.
- The Gauss equation gives K_F = W⁺(α, α) + s/12. The Ricci equation gives the normal curvature κ_N = W⁺(α, α).
- Gauss–Bonnet and Chern–Weil then give **e_orb(N_F) = χ_orb(F) − s·area_orb(F)/24π**. (area_orb counts F with weight 1/|Γ_F|, Γ_F
  the generic local group along F.)
- Calderbank–Singer's inequality e < χ_orb for s > 0 is its consequence.
- For a torus: e = −s·area/24π < 0. A totally geodesic torus in a positive self-dual Einstein orbifold has a twisted normal bundle, so
  it is never a principal orbit and never a surface whose normal bundle has a nowhere-zero section.

**T3 (fixed surfaces in the toric case).** Let M be compact, positive, toric self-dual Einstein, with k edges carrying isotropy
vectors v_j. By CS the lines [v_j] ∈ RP¹ are distinct and in cyclic order. Let σ be an orientation-preserving isometry of finite order.
It normalizes a 2-torus acting with this orbit structure (Isom₀ is that torus, or a larger compact group, and a finite-order
automorphism preserves a maximal torus). So σ acts on the orbit polygon W by an isometry σ̄ and on the torus by A ∈ GL(2, ℤ). A
2-dimensional component of Fix(σ) is then one of:
- **σ̄ = id, A = I.** σ lies in the torus, and its fixed surfaces are exceptional surfaces, which are spheres.
- **σ̄ = id, A = −I.** A real locus: four copies of W glued along the edges, χ = 4 − k. It passes through every torus-fixed point and
  meets every exceptional surface in a circle. (The involution (φ, ψ) ↦ (−φ, −ψ) is an isometry of every Calderbank–Pedersen metric.)
- **σ̄ a reflection** (A a reflection, det A = −1). The fixed set lies over the reflection's line L, as circles in the direction u of
  A's +1 eigenvector.
  - At an end of L on an edge whose collapsing direction is u, the circles cap. At an end on an edge whose collapsing direction is
    A's −1 eigenvector, the two families glue. A vertex caps.
  - A torus would need both ends to glue, so both edges' vectors would lie on the same line [v] ∈ RP¹, which CS's cyclic order
    forbids. So these fixed sets are one or two spheres.
- **σ̄ a rotation.** It fixes a surface only if it fixes a principal orbit, which needs A = I. A principal orbit has trivial normal
  bundle, which T2 forbids (and the distinct lines forbid A = I combinatorially). With A ≠ I the fixed points are isolated.

**Consequence.** No 2-dimensional stratum of constant isotropy in M/Γ is a closed torus.
- The only χ = 0 fixed surfaces are real loci with k = 4.
- For k ≥ 4, M is not smooth (Hitchin, via Theorem B's data). The real locus crosses every exceptional surface and every vertex, so it
  meets the orbifold locus, where the local group grows (ℤ_g on an edge of label g, dihedral once divided by σ).
- Its constant-type part is a torus minus circles or points, never a closed torus.

**T4 (the pairing).** Let F be fixed by an isometry rotating N_F with order N. Compute each section's normal degrees with its own
complex orientation (J_NK horizontal = the tautological structure, vertical reversed; c₁ = 0):
- Σ₊: TΣ has degree χ; H(N) has degree −e, where the generator acts by e^{−iθ}; V has degree e − χ, where it acts by e^{+iθ}.
- Σ₋: the same degrees, with the eigenvalues exchanged.
- With B1503's inflow n = (N/2)(d₁ − d₂): **n± = ±(N/2)(2e − χ)**, opposite.
- For a great sphere in S⁴ this is B1503's banked ℂP³ pair (d₁, d₂) = (−2, 0), (0, −2), n = ∓N.
- For a torus: n± = ±N·e = ∓N·s·area/24π. That is nonzero, but the section's partner carries the opposite sign.
- A section-type locus is never alone. (Fibre-type loci can be: AW's single A_{q−1} sphere in the (p, p, q) model carries chiral
  matter. But fibres are spheres.)

**T5 (AW's §2 family).** A point of WCP³_{n,n,m,m}/ℤ_r has isotropy fixed by its support. The singular strata are the two coordinate
lines {w₃ = w₄ = 0} and {w₁ = w₂ = 0}, which are 2-spheres, and points. **Hitchin's family:** SO(3) on S⁴ ⊂ Sym²₀ℝ³ fixes a 2-sphere
(order 2) or two points (order ≥ 3), and the orbifold stratum is the RP² orbit SO(3)/O(2).

## 3. The census, computed

`verification/orbifold_links.py census`; recorded in `orbifold_links.json` and `orbifold_links_run.txt`.
- **The data.** Calderbank–Singer's (aᵢ, bᵢ) with 2aᵢ ∈ {1, 2}, 2bᵢ ∈ [−6, 6], bᵢ/aᵢ increasing and the v_j integral (deduplicated by
  v), for k = 3, 4, 5, 6: 606, 3 295, 13 009 and 40 078 data.
- **The checks on every datum.**
  - Consecutive vectors are in cyclic order (Δ_{j−1,j} > 0).
  - Every exceptional surface satisfies CS's inequality e < χ_orb: 320 511 surfaces in all.
  - Smooth data occur only at k = 3: 6 data, all ℂP². There are none at k ≥ 4 (Hitchin).
- **The symmetries.** Every combinatorial automorphism: B ∈ GL(2, ℤ) on the characters with a dihedral permutation of the edges,
  realized by an isometry by CS's uniqueness. For each orientation-preserving one, its fixed surfaces by T3's case analysis:
  - rotations: 48, 10 and 20 at k = 3, 4 and 6. None fixes a principal orbit.
  - reflections: never a torus. At k = 3 they give 114 spheres and 114 pairs of spheres; at k = 4, 536 and 44; at k = 5, 261 and 261;
    at k = 6, 1 112 and 20.
  - real loci: χ = 4 − k on every datum. Every one meets the orbifold locus, except on the 6 smooth ℂP² data, where it is RP².

## 4. The curvature identity, computed

`verification/orbifold_links.py identity`. On four data sets: ℂP², k = 3 with labels (1, 1, 3), a symmetric k = 4 with labels
(2, 8, 2, 4), and k = 5.
- **Self-dual Einstein, from the full curvature tensor.** At three points each (mpmath, 30 digits), the scalar curvature is 12, the
  Einstein residual is at most 10⁻²⁴, and the Λ⁻ block of the curvature operator equals (s/12)·I to 10⁻²⁴. W⁺ is non-zero and
  sectional curvatures can be negative (k = 4, 5), so positivity alone does not rule out tori.
- **Closed forms.** D = F² − 4ρ²|∇F|² = 4ρ Σ_{i<j} c_ij²/(r_i r_j), with c_ij = det((aᵢ, bᵢ), (a_j, b_j)), wᵢ = aᵢη − bᵢ and
  rᵢ = √(aᵢ²ρ² + wᵢ²). The torus block is (u₁u₁ᵀ + u₂u₂ᵀ)/(F²D) with u₁ = −2 Σ (wᵢ/rᵢ)(bᵢ, aᵢ) and u₂ = 2ρ Σ (aᵢ/rᵢ)(bᵢ, aᵢ). They agree
  with the symbolic build to 5·10⁻¹⁶. At ρ → 0 they give each exceptional surface's area as an explicit integral over its edge.
- **T2 on all 15 exceptional surfaces.** area_orb/2π = χ_orb − e (s = 12) to 10⁻¹⁶: 1, 1, 1 on ℂP²; 2/15, 4/15, 2/9;
  1/48, 1/32, 1/48, 1/24; 1/35, 1/20, 1/16, 1/16, 5/56.
- **ℂP²'s real locus (RP²: χ = 1, e = −1).** area/4π = 1.0000000004.
- **The orbifold form was found by computation, not assumed.** My first form weighted χ_orb and e by the edge's label; the areas came
  out exactly one label smaller. The identity holds with area_orb, as stated in T2 and as S⁴/ℤ_g's great sphere confirms by hand.

## 5. The pairing, Hitchin's family and AW's §2, computed

- **The pairing** (`pairing`). The degree bookkeeping of T4 reproduces B1503's banked ℂP³ pair, (−2, 0) and (0, −2). For a torus with
  e = −1, −2, −3 the inflows are ±N·e.
- **Hitchin's family** (`hitchin`). Rotations of order 2 fix a 3-dimensional subspace of ℝ⁵, so a 2-sphere; orders 3 to 12 fix a line,
  so two points. diag(1, 1, −2) has stabilizer O(2), so its orbit is RP².
- **AW's §2** (`aw2`). 140 cones (gcd(n, m) = 1, n, m ≤ 7, r ≤ 4). The 2-dimensional strata are only the lines (0, 1) and (2, 3)
  (127 and 133 occurrences); the rest are points.

## 6. What it means

**Q: does any known G₂ cone over an orbifold link that is not a global quotient model a cusp point?** No.
- AW's §2 family has sphere loci only.
- The twistor family's loci are spheres or sections over fixed surfaces of M (T1).
- On the toric orbifolds, which are all the positive toric self-dual Einstein ones, no fixed surface is a torus of constant type (T3).
  Hitchin's family fixes only spheres.

**Q: could such a model be chiral on its own, as Witten's lone locus is?**
- A torus locus in the twistor family would be a section, and sections come in pairs with opposite inflows (T4).
- Witten's lone chiral locus is a sphere, in the family whose metric is not constructed.

**For the chain (sL-8).** With B1501–B1503 for the global quotients, no known local model supplies a chiral cusp point. The
positive's shape is now explicit:
- a positive self-dual Einstein 4-orbifold, necessarily non-toric, with a torus that an isometry fixes away from the orbifold locus;
- there T2 makes the normal bundle twisted, e = −s·area/24π, and T4 makes the two sections oppositely chiral, n = ±N·s·area/24π;
- or a nearly Kähler orbifold outside the twistor and AW families.
None is known.

## 7. Prior art and fences

- **Harvested by citation:** AW (the class, the §3 loci, the (p, p, q) model); AL (the toric twistor loci, spheres only);
  CS (Theorem A; Theorem B's formulas, the inequality, uniqueness); CP (the metric); Hitchin; Galicki–Lawson; Boyer–Galicki–Mann.
  B1355 and B1356 used AW's twistor family for 2T points, and B1356 already noted that the rest lies in "Galicki–Lawson quotients
  and their kin". B1503 C4 named Witten's lone locus.
- **T2** is a short computation (Gauss, Ricci, Gauss–Bonnet), and CS's inequality is its consequence. No novelty is claimed for it.
- **The sweep.** This branch, main (`987c0c8f`) and the audit lane (`e94abeb1`) were searched for twistor spaces, self-dual Einstein
  and quaternion-Kähler orbifolds, Galicki–Lawson, Calderbank, weighted projective planes, totally geodesic tori, normal Euler
  numbers and torus loci. The literature was checked through AW, AL (three papers), CS and CP. The audit lane's "fixed torus" hits
  are points of a cusp torus fixed by an order-3 map (unrelated).
  - No prior statement was found of T3 (fixed surfaces of isometries of toric self-dual Einstein orbifolds: no torus of constant
    type), of T4 (the opposite inflows of the two sections), or of their consequence for cusp points.
- **Fences.**
  - The class is the known one. Non-toric positive self-dual Einstein orbifolds beyond Hitchin's family are not classified, and the
    hatch is exactly there.
  - AW's §2 metrics are not constructed.
  - A cusp model needs a closed torus of constant transverse type. The k = 4 real loci are tori or Klein bottles cut by circles or
    points of larger isotropy; physically, a torus locus meeting other loci along lines.
  - T3 uses an invariant maximal torus for isometries of finite order.
  - Order-2 loci (SU(2)) carry no cubic inflow (B1503 C3).
  - The inflow bookkeeping of T4 is checked against B1503's banked pair, not derived independently of B1503's formula.
  - No physics crossed. 0 of 19.

## 8. Files

- `verification/orbifold_links.py`: parts A–E (the census, the identity, the pairing, Hitchin's family, AW's §2).
- `verification/orbifold_links.json`, `verification/orbifold_links_run.txt`: the recorded run.
- `tests/test_b1505_the_orbifold_links.py`: the lock.
