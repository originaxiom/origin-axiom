# B1501 — THE TORUS-LINK CENSUS, run as sealed: in the four simplest G₂ cones, a singular locus that is a cone over a torus is always of A-type and the torus is always hexagonal (P1 YES, P2 YES). There are exactly two kinds: SU(n)-type loci over the diagonal torus of S³ × S³, whose isotropy is U(1), and one SU(3)-type (A₂) locus over the flag manifold's Coxeter torus, whose isotropy is ℤ₃.

**Date:** 2026-09-29 (sealed and run) · **Seat:** cc (the SM-derivation branch) · **Occasion:** B1500 made each cusp point's chirality a
local datum. The owner saw the seal and said "run it". · **Status:**
- SEALED: `PREREGISTRATION.md` was committed at d780b639, with its sha256 in SEAL_LEDGER, before any fixed set of the census was computed.
- COMPUTED: the banked identity passed (7dc86418), then the census ran as sealed: 694 classes in 847 s.
- **Verdict as sealed:** P1 YES and P2 YES. P3: torus loci on S³ × S³ and F₁,₂ only, and F₁,₂ carries one. The priors were about 90%,
  80% and 70%.

**Fence:** homogeneous nearly Kähler links; finite groups of the sealed list of automorphisms; elements of order ≤ 12. The reading for
cusps assumes a completion conformal to the cone. No physics is computed. · **Price:** unchanged, 0 of 19 · **Numbering:** B1501.

## 0. Seen from above

B1500 found that closing a cusp by a point leaves a choice at the point that only the local physics can make. In M-theory the local
physics at such a point is a G₂ cone singularity, and at a cusp point the cone's ADE locus has to be a cone over the cusp torus. This
census asked which of the simplest G₂ cones have such a locus.
- **There are exactly two kinds.**
  - **The cone over S³ × S³.** The diagonal torus U(1)³/U(1) is fixed by every left translation by a non-central element of the
    diagonal torus. Its pointwise stabiliser is the diagonal U(1) and nothing else. Every finite quotient of the cone by a cyclic group
    inside it therefore carries an A_{n−1} (SU(n)) locus that is a cone over this torus.
  - **The cone over the flag manifold F₁,₂ = SU(3)/T².** Let γ be the left translation by c₀ = diag(1, ω, ω²) composed with the right
    action of the 3-cycle, which has order 3. It fixes exactly one torus: the orbit of T² through a point where g⁻¹c₀g = P⁻¹, which
    is Kostant's principal (Coxeter) torus. The pointwise stabiliser is {1, γ, γ²} ≅ ℤ₃. It acts on the normal plane with eigenvalues
    (ω, ω²), so the locus is A₂, an SU(3) locus.
  - **Nothing else.** S⁶ and ℂP³ give points and spheres only, as the lemma proved at seal said they must. Every other class on
    S³ × S³ and F₁,₂ gives points, spheres or nothing.
- **Every torus is hexagonal:** τ = e^{2πi/3} to 10⁻¹⁵ for all 25 torus components.
- **In the frame's terms.**
  - The frame's E₆ locus cannot end on such a point unbroken. Near the point its gauge group would have to be SU(n) (S³ × S³) or
    SU(3) (F₁,₂).
  - Only hexagonal cusps match these cones, if the completion is conformal to the cone. m004's own cusp (shape 2√−3) does not.
  - Hexagonal cusps in m004's class: m003's, three of cube~3.24's four, two on each of the four unresolved B1399 members, and those
    of 14 of m004's 87 covers of degree ≤ 10.
  - B1399 found odd counts possible only at hexagonal cusps. This census finds torus-linked G₂ cone points only over hexagonal tori.
    These are two independent computations, and they point at the same cusps.

## 1. The outcome, as sealed

**The banked identity passed** before any census number was read (`verification/identity_run.txt`, commit 7dc86418):
- **The structures.** On all four links J² = −1, J is orthogonal, and J commutes with Ad(K) (so every left translation preserves J),
  all to about 10⁻¹⁵. The listed σ, σ², R_P and R_P² preserve J. S⁶'s antipodal map, ℂP³'s real structure and the transpositions
  reverse it.
- **S⁶.** G₂ preserves the octonion cross product, and the coset J is x × ·. Three order-13 controls, which are not census elements,
  give two antipodal points or a great 2-sphere, as the fixed subspace says.
- **S³ × S³.** The diagonal-conjugation torus (an order-13 control) has Gram [[2/3, −1/3], [−1/3, 2/3]] in units (2π)² and is
  hexagonal. The diagonal U(1) fixes it pointwise, and H_F = U(1).

**The census** (`verification/census_run.txt`, `census.json`): 694 classes of order ≤ 12.

| link | classes | with fixed points | fixed sets | tori | centraliser types met |
|---|---|---|---|---|---|
| S⁶ | 67 (left) | 67 | 44 × two antipodal points; 23 × a great 2-sphere | 0 | T² 22, U(2) 43, SU(2)×SU(2) 1, SU(3) 1 |
| S³ × S³ | 329 (321 left, 8 twisted) | 31 | left: 23 × one torus, 298 × none; twisted: 2 × a point and a sphere, 6 × three points | 23 | T³ 189, SU(2)×T² 98, SU(2)²×U(1) 33, SU(2)³ 1; twisted U(1) 6, SU(2) 2 |
| ℂP³ | 95 (left) | 95 | 49 × four points; 22 × two points and a sphere; 24 × two spheres | 0 | T² 49, rank-2 dimension-4 (U(2) or Sp(1)×U(1)) 45, Sp(1)×Sp(1) 1 |
| F₁,₂ | 203 (111 left, 92 twisted) | 113 | left: 66 × six points, 45 × three spheres; twisted: 2 × one torus, 90 × none | 2 | T² 122, U(2) 79, SU(3) 2 |

The centraliser types are read from (dimension, rank, dimension of the derived algebra), so the names give the local type.

**The tori, all 25:**
- **S³ × S³, left translations L_(q,q,q)**: 23 classes, q ∈ {1/4, 1/6, 1/8, 1/10, 1/5, 1/12, 1/14, 1/7, 3/14, 1/16, 3/16, 1/18, 1/9, 2/9,
  1/20, 3/20, 1/22, 1/11, 3/22, 2/11, 5/22, 1/24, 5/24}, orders 2 to 12.
  - Each fixes one torus, the orbit of the maximal torus U(1)³ through its point.
  - The integral image is the whole period lattice (index 1). The Gram is [[2/3, −1/3], [−1/3, 2/3]] (2π)², so τ = e^{2πi/3}.
  - H_F = U(1) (the diagonal), with no other component: 200 of 200 seeds land in it, and no element composed with σ or σ² fixes the
    torus. So every finite subgroup of H_F is cyclic.
  - The generator acts on the normal plane with eigenvalues ±2i/√3, trace 0: SU(2)-type.
- **F₁,₂, L_{c₀} ∘ R_P and L_{c₀} ∘ R_P²** (c₀ = diag(1, ω, ω²), order 3):
  - Each fixes one torus. Its period lattice has index 3 over the integral image: the stabiliser is the centre of SU(3), so the lattice
    is the coweight lattice.
  - The Gram is [[1/3, −1/6], [−1/6, 1/3]] (2π)², so τ = e^{2πi/3}.
  - H_F is finite of order 3: the identity (left type), γ (R_P type) and γ² (R_P² type), one component each from 200 converged seeds.
    Its normal eigenvalues are (ω, ω²), with determinant 1. This is A₂.

**The predictions.**
- **P1 YES.** Every torus locus is of A-type, and every finite subgroup of every H_F is cyclic. In these models an ADE locus can end
  on a cone point along a torus only as A-type. The frame's E₆ locus cannot end on such a point unbroken.
- **P2 YES.** Every torus is hexagonal. Only hexagonal cusps have a conformal match among these cone points.
- **P3.**
  - S⁶ and ℂP³ carry no torus loci, as the lemma said.
  - S³ × S³ carries 23 classes, all over the same torus type, with continuous isotropy U(1).
  - F₁,₂ carries one torus locus per generator of the ℤ₃, the only torus in the census with a finite isotropy (ℤ₃, A₂).

## 2. Why these and no others

Each class's fixed set also follows from a short argument. `verification/post_run_checks.py` checks every one against the census (§4).
- **The equal-rank links (S⁶, ℂP³, F₁,₂), left translations.** A component of Fix(γ) is an orbit of C(γ)⁰ whose stabiliser contains a
  maximal torus of C(γ)⁰, so its Euler characteristic is positive (Hopf–Samelson). It is never a torus (the lemma, proved at seal).
  - S⁶: the fixed subspace of the torus element on ℝ⁷ gives two points or a great sphere.
  - ℂP³: the eigenlines of t on ℂ⁴ give points, or a ℂP¹ for a double eigenvalue.
  - F₁,₂: the columns of g form an eigenbasis of t, giving six points, or three spheres for a double eigenvalue.
- **S³ × S³, left L_(t₁,t₂,t₃).** gK is fixed iff g_i⁻¹t_ig_i = d for one d. So fixed points exist iff t₁, t₂, t₃ are conjugate. The set
  is then the orbit of the maximal torus, U(1)³/U(1).
  - Its metric: |X₁|² + |X₂|² + |X₃|² on X₁ + X₂ + X₃ = 0 (the normal metric). On the lattice (2πℤ)³ modulo the diagonal this is
    the Gram of the A₂ lattice.
  - An element fixing the torus pointwise is (d, d, d) with d commuting with every t, so it lies in the diagonal U(1).
- **S³ × S³, twisted L_(1,1,k) ∘ σ.** Fixing g₁ = 1 by the right Δ action gives g₃ = d, g₂ = d⁻¹ and d³ = k. That is three points for
  non-central k, and for k = ±1 a point and the 2-sphere of elements of order 3 or 6.
- **F₁,₂, twisted L_t ∘ R_P.**
  - Fixed points need g⁻¹tg ∈ T P⁻¹. Every element of that coset has characteristic polynomial x³ − 1, so t must be c₀ up to the
    centre.
  - T acts transitively on T P⁻¹ by conjugation: s⁻¹(tP⁻¹)s = t·s⁻¹(P⁻¹sP)·P⁻¹, and s ↦ s⁻¹(P⁻¹sP) has finite kernel (the centre),
    so it maps T onto T. The fixed set is one T-orbit.
  - Its stabiliser is T ∩ gTg⁻¹ = g(T ∩ C(P⁻¹))g⁻¹, the elements of T commuting with the Coxeter element: the centre.
  - Ad_{g⁻¹}𝔱 = Lie C(P⁻¹) is orthogonal to 𝔱 (Kostant's principal Cartan). So the orbit's vector fields lie wholly in 𝔪, and the
    metric is the Killing metric of 𝔱 on the coweight lattice, which is hexagonal.
  - Its pointwise stabiliser: γ and γ² fix it. A left translation fixing it lies in the intersection of the T-conjugates of gTg⁻¹, a
    finite group, and the census finds only the centre there. So H_F = ⟨γ⟩.
- **Lefschetz.** χ(Fix γ) = L(γ). For left translations, which are homotopic to the identity, L = χ(Y): S⁶ 2, S³ × S³ 0, ℂP³ 4, F₁,₂ 6.
  L(σ) = 3 on S³ × S³: σ* on H³ = ℤ² is [[−1, 1], [−1, 0]], with trace −1, and σ has degree +1. L(R_P) = 0 on F₁,₂, since H*(SU(3)/T)
  is the regular representation of the Weyl group, where a 3-cycle has trace 0. Every class satisfies it (§4).

## 3. What it settles, and what it does not

**Settled.**
- **What these models allow at a cusp point.** In the simplest G₂ cones a cusp point can be the cone point of an ADE locus only for
  SU(n) (the S³ × S³ family, isotropy U(1)) or SU(3) (the flag manifold's ℤ₃). In both cases the cusp must be hexagonal, under the
  conformal reading.
- **For the frame.** The frame's E₆ locus cannot be completed at a cusp point by these models without breaking to A-type near the point.
  m004's own cusp is not hexagonal, so these models do not complete it. Its hexagonal covers (for example cube~3.24's three hexagonal
  cusps) are the candidates.
- **The one model with finite isotropy.** It is the flag manifold's A₂ locus, and there SU(3), the ℤ₃ of the 3-symmetry and the
  hexagonal lattice (A₂'s coweight lattice, the Eisenstein lattice) come together. This is a structural observation, not a derivation of
  anything in the Standard Model.

**Not settled.**
- **The chirality at such a point** (B1500's choice per charged sector). The prereg fenced it out. It would need the local C-field and
  gauge data (anomaly inflow at conical singularities, Acharya–Witten), which nothing here computes.
- **Whether the frame can break E₆ to SU(n) or SU(3) along a cusp end,** consistently with its Higgs field.
- **Other local models:**
  - non-homogeneous links (Foscolo–Haskins' cohomogeneity-one nearly Kähler structures);
  - asymptotically conical and other non-conical models;
  - automorphisms outside the sealed list, for example complex conjugation composed with a transposition on F₁,₂, if it preserves J.
- **Conformality** of a cusp's completion to the cone is an assumption (the prereg's fence), not a result.

## 4. Verification

- **The instrument's own checks.**
  - Every class with fixed points converged on all 400 seeds. Classes without fixed points never got below residual 0.49, a clear gap.
  - The dimension agreed at three points on every component, and every component is a single C(γ)⁰ orbit (internal flags: 0).
  - All 67 S⁶ classes agree with the fixed subspace.
  - The lemma held on the census's own elements.
- **`verification/post_run_checks.py`** (`post_run_checks_run.txt`):
  - (1) The fixed sets agree with the independent criteria of §2 on 694 of 694 classes.
  - (2) χ(Fix γ) = L(γ) on 694 of 694.
  - (3) Closed forms.
    - The F₁,₂ torus: Ad_{g⁻¹}𝔱 is orthogonal to 𝔱 to 3 × 10⁻¹⁶, the Gram is [[1/3, −1/6], [−1/6, 1/3]], and the census's two F₁,₂
      tori agree.
    - All 23 S³ × S³ tori have the U(1)³/U(1) Gram.
  - (4) The 25 torus classes and 12 others, re-run in a fresh process: every record agrees.
- **Two slips of mine,** both caught before any census number was read (ERROR_LEDGER, E52 instance):
  - The lattice routine used Python's `sum(vector, 0)`, which collapsed a q-vector to a scalar. The routine's own cross-check caught it
    on the order-13 control: its Newton grid disagreed with its rational enumeration.
  - The closed-form check's coweight generator was written as (1/3, 2/3). That element is diag(ω, ω², 1), which is not central. I
    caught it on re-reading, before the check ran.

## 5. Fences

- **Links:** homogeneous nearly Kähler links only.
- **Quotients:** finite groups of the sealed list of automorphisms, elements of order ≤ 12. Order ≤ 12 meets every centraliser type
  these groups have, and the census lists the types it met.
- **The cusp reading** assumes a completion conformal to the cone.
- **Physics:** the chiral content at such a point is not computed, and nothing selects the frame's choice at a cusp point (B1500). No
  physics is crossed. 0 of 19.
- **Novelty:** the census of torus-linked ADE loci in these cones is not known to this seat from the literature (the design-time sweep
  in the prereg). No novelty is claimed for the mathematics. The ingredients are standard: Gray, Butruille, Hopf–Samelson, Kostant,
  McKay.

## Files

- `PREREGISTRATION.md`: the seal, unchanged (sha256 `51b6730b…`).
- `verification/torus_link_census.py`: the instrument. `identity_run.txt` records the banked identity. `census.json` holds every class's
  record, and `census_run.txt` is the run's log.
- `verification/post_run_checks.py`: the independent criteria, Lefschetz, the closed forms and the fresh-process re-run. It writes
  `post_run_checks.json` and `post_run_checks_run.txt`.
- Lock: `tests/test_b1501_the_torus_link_census.py`.
