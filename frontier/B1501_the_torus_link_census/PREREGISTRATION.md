# B1501 PREREGISTRATION — THE TORUS-LINK CENSUS: which of the simplest G₂ cone singularities have an ADE locus that is a cone over a torus, of what ADE type, and of what shape?

**Sealed 2026-09-29, before any fixed set of the census is computed. Seat: cc (the SM-derivation branch). Occasion: B1500.**
Closing a cusp by a point makes each cusp point's chirality a local datum, which only the local physics at the point can supply.
In M-theory that physics is a G₂ conical singularity (Acharya–Witten). For a cusp point, the ADE locus through it must be a cone over
the cusp torus. This census asks which such local models exist among the simplest G₂ cones. The run waits for the owner.

## The question

**The links.** The four homogeneous nearly Kähler 6-manifolds (Butruille):
- S⁶ = G₂/SU(3);
- S³ × S³ = SU(2)³/ΔSU(2);
- ℂP³ = Sp(2)/(Sp(1) × U(1));
- the flag manifold F₁,₂ = SU(3)/T².

Each is 3-symmetric, with the normal metric (Gray). The metric cone C(Y) has holonomy in G₂ (Bär).

**The quotients.** C(Y)/Γ, with Γ a finite group of automorphisms of Y's nearly Kähler structure. These are exactly the automorphisms
of the cone's G₂ structure that fix the apex.

**The loci.**
- A codimension-4 singular stratum of C(Y)/Γ is the cone over a 2-dimensional component F of the fixed set, in Y, of its isotropy
  group H_F (the pointwise stabiliser of F in Γ).
- H_F acts on F's normal space through a finite subgroup of SU(2): an element of G₂ that fixes an associative 3-plane lies in the
  SU(2) acting on its complement. McKay's correspondence gives the ADE type.

**The question.** For which (Y, H_F, F) is F a torus? What is the ADE type, and what is F's shape τ in Y's metric (reduced to
SL(2, ℤ)'s fundamental domain)?

## The reduction (proved now)

**(i) Fixed components are points or surfaces.** An element of G₂ fixes a subspace of dimension 1, 3 or 7 of each tangent space of the
cone. So in Y a non-trivial automorphism's fixed components have dimension 0 or 2.

**(ii) Single elements suffice.** Let F be a torus component of Fix(H). For every non-trivial h ∈ H, F lies in a 2-dimensional
component of Fix(h), which by (i) is F itself. So the census of single elements finds every F. H_F is then computed as F's full
pointwise stabiliser.

**(iii) The equal-rank lemma.** Let Y = G/K with rank K = rank G, and let γ act by left translation by an element of G.
- A component of Fix(γ) is an orbit of C_G(γ)⁰ whose stabiliser contains a maximal torus of C_G(γ)⁰. Proof: if g⁻¹γg ∈ K, a maximal
  torus S of K containing it is maximal in G, and gSg⁻¹ ⊂ C_G(γ).
- By Hopf–Samelson the orbit has positive Euler characteristic. So it is never a torus.
- S⁶, ℂP³ and F₁,₂ have equal rank (2 = 2). S³ × S³ does not (3 against 1).

**(iv) Where tori can come from.** Tori can come only from:
- S³ × S³;
- automorphisms that are not left translations. These are right actions by N_G(K)/K and outer automorphisms of G preserving K, and they
  count only if they preserve the nearly Kähler J. An anti-holomorphic map does not preserve the G₂ structure.

**The automorphisms used.** Every candidate outer element is checked in code, before use, to preserve J and ω, or to reverse J.
- **S⁶:** G₂. The right action of N(SU(3))/SU(3) = ℤ₂ is the antipodal map, which reverses J.
- **ℂP³:** Sp(2). The right ℤ₂ of the normaliser is the twistor real structure, which reverses the nearly Kähler J.
- **S³ × S³:** SU(2)³ and the cyclic permutations of the factors, a ℤ₃ (the 3-symmetry). The transpositions reverse J.
- **F₁,₂:** SU(3) on the left and, on the right, the order-3 Weyl elements (the 3-symmetry), a ℤ₃. The transpositions reverse J.

## Design-time reasoning, recorded as the basis of the priors (no fixed set was computed)

**S³ × S³.**
- An element (a₁, a₂, a₃) of the torus U(1)³ has fixed points only if its three factors are conjugate. Its fixed set is then the torus
  U(1)³/U(1).
- B1500 §5 found that torus hexagonal in the normal metric. Its pointwise stabiliser contains the diagonal U(1), so every finite H_F
  would be cyclic.
- A cyclic permutation σ·(a₁, a₂, a₃) reduces to k³ = a₃a₂a₁ modulo the diagonal. That gives points, or spheres when a₃a₂a₁ is
  central.

**F₁,₂.**
- A twisted element (h on the left, the Coxeter element n of the Weyl group on the right) has fixed points exactly when g⁻¹hg lies in
  the coset T²n⁻¹. Kostant: those elements are regular.
- Its centraliser is a maximal torus T′ whose Lie algebra lies in the root spaces, orthogonal to 𝔱. So the orbit through a fixed point
  is 2-dimensional (T′ ∩ T² is finite) and carries the Killing metric of a Cartan subalgebra: a hexagonal torus, with a ℤ₃ isotropy.

This reasoning is not a computation of the census. The census computes the fixed sets, the tori, their exact lattices and the full
isotropy groups independently, and checks every step above.

## The census (fixed now)

- **Elements.** For each Y, every conjugacy class of automorphisms γ of order at most 12 that is:
  - a left translation by an element of a maximal torus of G, up to the Weyl group, the centre and the outer part; or
  - such a translation composed with one of the outer elements listed above.
  Order at most 12 realises every centraliser type of these groups. The census lists the types it meets.
- **The fixed set of each γ.** The coset equation g⁻¹γg ∈ K is solved (twisted where needed) by damped Newton from 400 random seeds on
  G. Two solutions belong to one component when the identity component of C(γ) carries one to the other; this is decided by minimising
  their distance over C(γ)⁰, with a threshold of 10⁻⁶.
- **The dimension of each component** is the dimension of the kernel of dγ − 1 on its tangent space, computed at three points of the
  component. The three must agree.
- **Topology.** A 2-dimensional component is the orbit of C(γ)⁰ through one of its points.
  - Torus: C(γ)⁰ acts through a 2-torus with finite stabiliser.
  - Sphere: through SU(2) or SO(3) with a U(1) stabiliser.
  - Anything else is reported as found.
- **Shape of a torus.**
  - The period lattice is {X ∈ Lie(T) : exp X ∈ the point's stabiliser}.
  - The metric is Y's normal metric on the orbit's tangent vectors, the same at every point, since T acts by isometries.
  - τ is reduced to the fundamental domain. Hexagonal means |τ − e^{iπ/3}| < 10⁻⁹, up to reflection.
- **H_F for a torus.** The group of automorphisms fixing three generic points of F, which then fix F pointwise; checked on 20 points.
  Report whether it is finite or continuous, its order or type, and whether every finite subgroup is cyclic.
- **The normal type.** H_F's action on F's normal space, in Y's J: SU(2)-type means eigenvalues (e^{iφ}, e^{−iφ}) with the tangent line
  of F fixed.

## BANKED IDENTITY:

Before any census number is read, the instrument must reproduce the following. If any fails, the run stops.
- **S³ × S³, B1500 §5.** The diagonal-conjugation torus is hexagonal, with Gram [[2/3, −1/3], [−1/3, 2/3]] in units (2π)², and its
  pointwise stabiliser contains the diagonal U(1).
- **S⁶.** For an element of G₂'s maximal torus the fixed set on S⁶ is a pair of antipodal points (all three eigenvalue pairs on ℂ³
  non-trivial) or a great 2-sphere (one trivial), never a torus. Checked against the octonion cross product, with J_x(v) = x × v.
- **The structures.**
  - The normal metric and the canonical J of each 3-symmetric space: J² = −1, and J is orthogonal.
  - Every left translation preserves J.
  - Each listed outer element preserves J and ω.
  - Each excluded one (S⁶'s antipodal map, ℂP³'s real structure, the transpositions) reverses J.
- **The lemma, on the census's own elements.** Left translations on S⁶, ℂP³ and F₁,₂ give no torus component. This is a check that
  must pass, not an outcome.

## Predictions, sealed

- **P1 (the type).** Is every torus component's isotropy of A-type, with all finite subgroups of H_F cyclic?
  - YES: in these models an ADE locus can end on a cone point along a torus only as A-type. The frame's E₆ locus cannot end on such a
    point unbroken: near the point it must break to A-type.
  - NO: the first local models in which a D- or E-type locus is coned over a torus, listed by (Y, H_F, F).
  - **Prior: YES, about 90%.**
- **P2 (the shape).** Is every torus component hexagonal?
  - YES: only hexagonal cusps have a conformal match among these cone points. Among the members checked so far, hexagonal cusps occur
    on m003 (B1222), cube~3.24 (three), the four unresolved members of B1399's census (two each) and 14 of m004's 87 covers to degree
    ten (main's census), and on none of B1399's 102 resolved members. m004's own cusp (shape 2√−3) is not hexagonal.
  - NO: the other shapes found, and which cusps of the class have them.
  - **Prior: YES, about 80%.**
- **P3 (read).**
  - Which links carry torus loci at all. By (iii), S⁶ and ℂP³ carry none.
  - For each torus: the element class, the ADE type, the order of H_F or its continuous part, and the lattice.
  - Whether F₁,₂ carries any. Prior: yes, about 70% (the design-time reasoning above).

## Fences

- **Links.** Homogeneous nearly Kähler links only. Foscolo–Haskins' cohomogeneity-one nearly Kähler structures on S⁶ and S³ × S³, and
  every non-conical or asymptotically conical local model, are outside.
- **Quotients.** Finite groups of automorphisms only, drawn from the automorphisms listed above. If a link has further automorphisms,
  they are outside.
- **The reading.** The reading of P2 for cusps assumes the completion is conformal to the cone, so that the cusp torus's shape must match
  the link's. That is an assumption, not part of the census.
- **Physics.** The chiral content at such a point is not computed here. Nothing selects the frame's choice at a cusp point (B1500).
  No physics is crossed. 0 of 19.

## PRIOR ART:

**The design-time sweep.** On this branch, main (`987c0c8f`) and the audit lane (`aff8a569`), fetched 2026-09-29, there are no hits for
nearly Kähler, Harvey–Lawson, special Lagrangian, J-holomorphic, perversity, intersection homology, non-Witt, or Cheeger's ideal
boundary conditions.
- The record's G₂ local models (B1084's flat cone; B1353–B1360's E₇ apexes) have smooth loci through the apex, with sphere links.
- B1500 §5 checked the S³ × S³ torus and Harvey–Lawson's cone.

**The literature.**
- Butruille (the classification of homogeneous nearly Kähler 6-manifolds, 2005);
- Gray (3-symmetric spaces, 1972);
- Bär (cones over nearly Kähler manifolds, 1993);
- Hopf–Samelson (Euler characteristics of homogeneous spaces of maximal rank);
- Kostant (the Coxeter element and its principal torus);
- Acharya–Witten (hep-th/0109152) and Atiyah–Witten (hep-th/0107177), for the physics of G₂ cones;
- Foscolo–Haskins (Ann. of Math. 2017), the fence.

The census of torus-linked ADE loci in these cones is not known to this seat from the literature. The sweep found nothing in the
record.
