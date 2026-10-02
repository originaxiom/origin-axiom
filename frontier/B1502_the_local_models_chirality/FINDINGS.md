# B1502 — THE LOCAL MODELS' CHIRALITY: B1501's two torus models force no chirality at a cusp point. Whenever a torus-linked ADE locus exists in these cones, the link has no C-field U(1) and no rational flux (b₂ = b₄ = 0), the torus is null-homologous, and the locus's normal twist over the torus is trivial (§5), so neither half of the anomaly argument has anything to act on. The S³ × S³ model's cusp point is a Dehn filling (along a shortest vector) in each of its three smooth phases. The flag-manifold model has no smooth phase at all.

**Date:** 2026-09-29 · **Seat:** cc (the SM-derivation branch) · **Occasion:** after B1501. The owner said to take the next step I
recommended: what chirality the two torus models put at a cusp point. · **Status:** PROVED, not sealed. Designing the seal, I found the
question decided at design time by standard theorems, so there was no open outcome to seal (B1396's precedent). Own-code verification:
`verification/local_models_chirality.py`, 6.1 s, all checks pass. §5 (the cubic half of the anomaly criterion) was added the same
day, after a self-caught gap (an E71 instance): `verification/cubic_inflow.py`, 18.3 s. · **Price:** unchanged, 0 of 19 · **Numbering:** B1502.

## 0. Seen from above

B1500 made each cusp point's chirality a choice that only the local physics at the point can make. B1501 found that the simplest local
models, G₂ cones over the four homogeneous nearly Kähler 6-manifolds, have torus-linked ADE loci of exactly two kinds:
- M1: SU(n) over S³ × S³'s diagonal torus;
- M2: SU(3) over the flag manifold's Coxeter torus.

This arc asks what those two models put at the point.
- **What forces chirality at a cone point.** The criterion has two halves (Witten, hep-th/0108165; Acharya–Witten, hep-th/0109152).
  - *The mixed half,* which the record already uses (B1353, B1360). Chiral fermions at a conical singularity are charged under a U(1)
    coming from the C-field on a harmonic 2-form of the link. Their mixed anomaly with the ADE group forces and detects them, through
    the pairing of the locus's link with that 2-form.
  - *The cubic half,* for SU(N) loci only (§5). The locus's normal space can be twisted by a U(1). The degree n_P of that twist on the
    link of the point forces fields with SU(N)³ anomaly n_P there.
- **Neither model has either.**
  - Any finite quotient of these cones with a torus-linked locus has b₂ = b₄ = 0 on its link. There is no C-field U(1) and no rational
    flux.
  - The torus itself is null-homologous in the link, so it would pair to zero with any such U(1) anyway.
  - The normal twist over the torus is trivial, so n_P = 0 (§5).
  - So nothing forces chirality at the point. Any chiral content there would have to be anomaly-free on its own, and the anomaly argument
    cannot see it.
- **The S³ × S³ model has three smooth phases,** the three Bryant–Salamon smoothings. The model's symmetry acts on each. In each, the
  locus becomes a solid torus: the cone over the torus is Dehn-filled along e₁, e₂ or e₃, the three shortest vectors of its lattice.
  In a smooth phase the cusp point is therefore a filling, and a filling contributes nothing (B1351; B1500's Lagrangian line is the
  slope).
- **The flag-manifold model has no smooth phase.** The 3-cycle in its symmetry permutes the three Bryant–Salamon smoothings, so none
  survives the quotient. Its apex is rigid, but it carries no inflow datum.

**What this closes.** The simplest local models do not supply the end law's chirality.

**Where the choice lives.** At a cone point the frame's SL(2)_β doublet sectors carry no choice. Under the geometric representation
their cusp local system is acyclic (the longitude acts as −(unipotent): B1368, B1372's Lemma A; checked here). The choice lives only on
the spin-0 sectors whose cusp character is trivial, which are the sectors that carry the frame's count.

**What remains:**
- a local model whose torus link is homologically non-trivial and pairs with a C-field U(1). No torus that is an orbit of a torus action
  with a fixed point can be one.
- non-abelian data on the locus near the cusp that makes the choice charge-odd (§3);
- or a charge-odd input from outside the local geometry.

## 1. The theorem

Let Y be one of the four homogeneous nearly Kähler 6-manifolds and Γ a finite group of the sealed automorphisms (B1501) such that
C(Y)/Γ has an ADE locus that is a cone over a torus F. Then:
- **(a) No C-field U(1) and no rational flux at the apex:** H²(Y/Γ; ℚ) = H⁴(Y/Γ; ℚ) = 0.
  - H^k(Y/Γ; ℚ) = H^k(Y; ℚ)^Γ, so it is enough that one element of Γ has no invariant classes.
  - For Y = S³ × S³, H² = H⁴ = 0 already.
  - For Y = F₁,₂, every torus-fixing element is L_a ∘ R_P^{±1} (B1501 §2, any order). L_a acts trivially on cohomology (SU(3) is
    connected). R_P acts on H² and on H⁴ as the Weyl group's 2-dimensional reflection representation, where a 3-cycle has trace −1 and no
    invariant vector.
  - S⁶ and ℂP³ have no torus loci (the lemma).
- **(b) The torus link is null-homologous: [F] = 0 in H₂(Y; ℚ).**
  - S³ × S³ has H₂ = 0.
  - The Coxeter torus is an orbit of the maximal torus T of SU(3), and T has fixed points on F₁,₂ (the six Weyl points). So its orbit
    map is homotopic to a constant.
- **(c) Nothing at the apex is forced.** By (a) there is no U(1) whose mixed anomaly with the ADE group could force or detect chiral
  fields at the point. By (b) the locus's link would pair to zero with one even if it existed. By (f) the cubic SU(N)³ inflow vanishes
  too. Any content at the apex is anomaly-free on its own.
- **(d) M1's phases.**
  - The three Bryant–Salamon smoothings X_k of C(S³ × S³) (the spinor bundle of S³, three ways) are SU(2)³-equivariant.
    - Model: X_k = S³ × ℍ, with (a₁, a₂, a₃) acting by (a_i q a_j⁻¹, a_k p a_j⁻¹) for (i, j, k) cyclic.
    - The principal orbit is SU(2)³/Δ = S³ × S³, and the zero section is S³.
  - The fixed set of any non-central (t, t, t) is S¹ × ℂ: q commuting with t, p in the complex line commuting with t. This is the filling
    of the cone over the diagonal torus along the circle θ_k.
    - That circle is the lattice vector e_k, of norm 2/3 (2π)², the lattice minimum.
    - The three phases fill the three shortest slopes (the A₂ roots), and σ permutes them.
  - The transverse type is constant along a connected fixed component, so it stays A_{n−1}, as on the link.
- **(e) M2's phases.**
  - The Bryant–Salamon smoothings of C(F₁,₂) are the cohomogeneity-one SU(3)-manifolds with group diagram T < U(2)_j < SU(3) (Λ²₋ℂP²,
    three ways).
  - A right action R_n extends to X_j only if n U(2)_j n⁻¹ = U(2)_j. R_P and R_P² permute the three U(2)_j and preserve none.
  - So no torus-fixing element of F₁,₂ acts on any X_j. (The excluded transposition preserves one.)
- **(f) The cubic half: n_P = 0 (§5).** A torus commuting with Γ acts transitively on F, so the locus's normal U(1) twist L is a
  homogeneous line bundle over a torus, and it is trivial.

## 2. Verification (`verification/local_models_chirality.py`, record `local_models_chirality_run.txt`)

> **Note (2026-10-02, main's S37).** On main's bench (numpy 2.4.0) the script stopped on its own assertion, reading b₃(ℂP³) = 1.
> The projection onto exact forms (line 116) used `np.linalg.pinv` at numpy's default cutoff, 10⁻¹⁵ × σ_max, and a rounding-level
> singular value (8 × 10⁻¹⁵ beside 3.46) was inverted. Here the same value is 6.8 × 10⁻¹⁶, and at degree 4 it is 1.8 × 10⁻¹⁵
> against a cutoff of 3.5 × 10⁻¹⁵, so the script passed with a margin of two. A cutoff relative to σ_max also inverts pure noise
> where the image is exactly zero (σ_max is 10⁻¹⁵ or below at one degree each of S⁶, S³ × S³ and ℂP³ here). The projection now
> uses an orthonormal basis of the exact forms cut at singular values above 10⁻⁹, the script's convention for its other ranks.
> Rerun here after the change: `local_models_chirality.json` is byte-identical, and the record differs only in its run time
> (9.5 s on a loaded bench; 6.1 s at banking). The mathematics was not in question.

- **Cohomology.** Relative Lie algebra cohomology H*(𝔤, 𝔨): K-invariant forms on 𝔪 with the Chevalley–Eilenberg differential, d² = 0
  on them to 10⁻¹⁵.
  - Betti numbers: S⁶ (1,0,0,0,0,0,1), S³ × S³ (1,0,0,2,0,0,1), ℂP³ (1,0,1,0,1,0,1), F₁,₂ (1,0,2,0,2,0,1), as expected.
  - σ and σ² on H³(S³ × S³): trace −1, no invariants, which gives L(σ) = 1 − (−1) + 1 = 3, B1501's Lefschetz number.
  - R_P and R_P² on H²(F₁,₂) and H⁴(F₁,₂): trace −1 each, no invariants.
- **The torus links.** The maximal torus fixes the six Weyl points of F₁,₂ to 10⁻¹⁶. B1501's census found the Coxeter torus to be an
  orbit of that torus.
- **M1's phases.**
  - SU(2)³ on X_k has a stabiliser of dimension 3 at a principal point (orbit S³ × S³) and 6 on the zero section (orbit S³).
  - For three non-central elements, Newton from 200 random points converged on 197 to 200 of them. Every solution has q and p diagonal
    (off-diagonal parts ≤ 10⁻³⁰), and the fixed set's tangent dimension is 3.
  - The (t, t, t) action has the same form in every X_k, so one computation serves all three phases. The phases differ in which circle
    collapses: e₁, e₂ and e₃, each of norm 2/3 (2π)², the minimum of B1501's lattice.
- **M2's phases.** R_P maps U(2)₀₁ → U(2)₁₂ → U(2)₀₂ → U(2)₀₁. R_P² maps them the other way. The transposition (12) preserves U(2)₀₁.
- **The frame's sectors on the cusp torus.** Koszul complex of ℤ² with the geometric representation's cusp holonomy: meridian
  z·[[1, 1], [0, 1]], longitude −[[1, 2√3 i], [0, 1]].
  - Spin ½: H* = (0, 0, 0) for every z sampled, including z = ±1.
  - Spin 0: (1, 2, 1) at z = 1, and (0, 0, 0) otherwise.

## 3. What it settles, and what it does not

**Settled.**
- **Neither model supplies the end law's chirality.**
  - M1 is a filling in each of its smooth phases (ε = 0 there).
  - At its singular point, and at M2's rigid apex, no C-field U(1) or rational flux exists to force or detect a chiral spectrum, and
    the normal twist is trivial (n_P = 0), so neither half of the anomaly criterion forces one.
- **The same holds for any finite quotient** of these cones that has a torus-linked locus, whatever other loci it has.

**Not settled.**
- **What M-theory actually puts at M2's rigid apex.** Anything there is anomaly-free by itself.
- **The quantum phase structure of M1's singular point.** Atiyah–Witten argue its three classical phases are smoothly connected.
- **Torsion data** (torsion in H⁴(Y/Γ; ℤ)).
- **Local models outside the census,** whose torus link would have to be homologically non-trivial.
- **Non-abelian data on the locus near a cusp point.**
  - With the frame's own cusp holonomy, the choice at a cone point sits only on spin-0 sectors with trivial cusp character (§0, §2). The
    SL(2)_β data there are charge-blind: SL(2)_β commutes with the frame's U(1)s and its representations are self-dual. So they cannot
    make the choice charge-odd.
  - A charge-odd choice would need non-abelian data charged under the frame's U(1)s. The audit lane's R35 applies to any T-brane reading
    of that: a local nilpotent Higgs field does not certify a globally non-semisimple monodromy.

## 4. Prior art and fences

- **The sweep.** This branch, main (987c0c8f) and the audit lane (aff8a569), 2026-09-29:
  - B1353 and B1360 hold the anomaly criterion used here (cited, not re-derived).
  - Main's outside_bench names the Bryant–Salamon cone over ℂP³/2T (B1355's model).
  - The audit lane's R35 holds the T-brane caution.
  - No hit computes the phases or the link cohomology of B1501's torus models.
- **Literature (standard):**
  - Bryant–Salamon (1989), the smoothings;
  - Atiyah–Witten (hep-th/0107177), the three phases;
  - Witten (hep-th/0108165) and Acharya–Witten (hep-th/0109152), chirality at conical singularities;
  - Chevalley–Eilenberg, H*(G/K) = H*(𝔤, 𝔨);
  - Borel, the Weyl group on H*(G/T);
  - Fukui–Hatsugai–Suzuki (2005), the lattice Chern number, and Qi–Wu–Zhang (2006), the control model (§5).
- **No novelty is claimed.**
- **Fences.** Only the Bryant–Salamon smoothings; rational cohomology; the anomaly criterion as Witten states it (both halves, §5). No
  physics is crossed. 0 of 19.

## 5. The cubic inflow (added the same day; an E71 instance, self-caught)

§0–§1 as first banked used one half of the anomaly criterion: the mixed U(1)·SU(N)² inflow, which needs a C-field U(1). B1355 and
B1360 used that half for E₆ loci, and for E₆ it is the whole criterion, because E₆ has no cubic anomaly. B1501's loci are A-type
(SU(n) on S³ × S³, SU(3) on F₁,₂). For SU(N), Witten has a second, independent half (hep-th/0108165 §3, (3.5)–(3.8)), and B1355 §3
had noted that for SU(N) the cubic anomaly forces by itself.
- **The mechanism.**
  - On an A_{N−1} locus the normal space ℂ²/ℤ_N can be twisted by Λ′ = U(1), the centraliser of ℤ_N in the SU(2) that contains it.
    The invariants x = a^N and y = b^N are then sections of L and L⁻¹, for a line bundle L on the locus.
  - The long-wavelength theory carries ∫_B (K/2π) ∧ ω₅(A), where K is the curvature of L. At a point P where the normal singularity is
    worse, dK = 2π n_P δ_P, and P must carry charged fields with SU(N)³ anomaly n_P.
  - n_P is the degree of L on a small surface around P in the locus. At a cusp point that surface is the torus link F.
- **Theorem (f): n_P = deg(L|_F) = 0 in both models.**
  - A torus acts transitively on F and commutes with γ. On S³ × S³ it is T³, the maximal torus of SU(2)³, with the diagonal U(1) as
    stabiliser. On F₁,₂ it is SU(3)'s maximal torus, acting on the Coxeter torus.
  - So L is a homogeneous line bundle T ×_H ℂ_χ over the torus F = T/H. Every character of a closed subgroup of a torus extends to the
    torus (Pontryagin duality), so L is trivial.
  - It stays trivial on any finite quotient whose torus link is covered by such an F, since degree multiplies under covers.
- **Checked** (`verification/cubic_inflow.py`, record `cubic_inflow_run.txt`, 18.3 s).
  - On F, the normal bundle with the complex structure in which dγ acts as the scalar ζ is E_ζ, the ζ-eigenbundle of dγ on ν ⊗ ℂ. It is
    a U(2) = (SU(2) × Λ′)/ℤ₂ bundle with det E_ζ = L^{2/N}, so deg L = (N/2) c₁(E_ζ).
  - c₁(E_ζ) is computed as a lattice Chern number (Fukui–Hatsugai–Suzuki), with E_ζ carried into the ambient space of the link's
    embedding so that the frame is global.
  - This is done for every torus class of B1501's census with transverse order N ≥ 3: 22 on S³ × S³ (N = 3 to 12) and 2 on F₁,₂ (N = 3),
    each on grids of 16 and 28. Every value is 0.
  - The acting torus commutes with γ to 10⁻¹⁵ on every class.
  - Positive control: the same routine gives the Qi–Wu–Zhang lower band's Chern numbers, ±1 at |m| = 1 and 0 at |m| = 3.
  - On S³ × S³, E_ζ is a constant subspace of the ambient space and the torus acts on it by a character, which is the theorem's mechanism
    made visible. On F₁,₂ it moves (smallest overlap between neighbouring grid points 0.89), and the lattice sum is still 0.
- **What changes.** Nothing in the verdict. The conclusion that nothing at the apex is forced now rests on both halves of the criterion.
  (c) is completed by (f), and the surfaces that said "the anomaly criterion forces nothing" now name both halves.

## Files

- `verification/local_models_chirality.py`: the checks. It writes `local_models_chirality.json` and `local_models_chirality_run.txt`.
- `verification/cubic_inflow.py`: §5's check. It writes `cubic_inflow.json` and `cubic_inflow_run.txt`.
- Lock: `tests/test_b1502_the_local_models_chirality.py`.
