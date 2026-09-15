# B1360 — THE COMPANION-FREE APEX: Acharya–Witten's E₇ → E₆ unfolding cone, whose topology they left undescribed, has singular set the E₆ locus and the apex only, b₂(link) = 1, and an E₆ link that pairs non-trivially with the generator — so Witten's inflow applies to it exactly as to the twistor cone, with no A₁ companion, no cone lines and no doublet parity; three such apexes on the E₆ copy of Y₃ are the cleanest form of the design, with B1356's sum rule and charges verbatim

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (a homotopy argument whose every input is computed: the E₆ root subsystem of E₇ orthogonal to the omitted node's coweight, H₂ of the generic fibre, the centraliser of 2T in U(2), the circle's weight; the model of the link as an associated bundle glued to the central fibre is standard hyperkähler-quotient geometry, stated in §1; calibrated on AW's SU(N) cones, where the same argument returns the known answers) · **Price: unchanged** · **Numbering:** B1360 (L212, L213; the correction of record on B1355 made concrete).

## 0. Seen from above

Main's B1413 corrected B1355: Acharya–Witten's hyperkähler-quotient family does reach E₆ — their §2.3 builds, for E₆ ⊂ E₇, the cone
X = (ℍ^k///K′)/U(1)′ from Kronheimer's E₇ quiver with the U(1) of the node beyond E₆ omitted, with one chiral 27 of charge 1 by the
heterotic computation, and adds "a useful way to describe the topology of X in these examples is not clear". For the design of the
closing that topology is the whole question: does this apex carry the C-field U(1) whose inflow forces the 27 (b₂(link) ≥ 1 and
∫_U w ≠ 0 over the E₆ link), and what else passes through it? This arc answers both from the structure of the unfolding. X is the
total space of the family of Kronheimer's ALE spaces X_ζ over the omitted D-term ζ ∈ ℝ³: the fibre over 0 is ℂ²/2O, the generic
fibre is the partial resolution of the E₇ singularity in which exactly the E₆ configuration stays collapsed (the roots orthogonal to
the seventh fundamental coweight are the 72 roots of E₆ — computed), so it is smooth away from one E₆ point and retracts onto the one
surviving curve C₇ (H₂ = ℚ — computed). The link is that family over the sphere of directions, glued at infinity to the central
fibre S³/2O, and the family over the sphere is the bundle associated to the Hopf fibration by the hyperkähler circle acting on a fixed
fibre. Mayer–Vietoris gives b₂ = 1. The E₆ link U is the section through the fixed E₆ point; its pairing with the generator is the
Euler number of the normal line of C₇ at that point, twisted over the sphere by the circle — and the circle acts on the tangent cone
ℂ²/2T of the E₆ point through the centraliser of 2T in U(2), the scalars (computed), hence with non-zero weight on the normal: the
pairing is non-zero. The same argument on AW's SU(N) cones (cone over WCP³_{1,1,N,N}) returns b₂ = 1 and a circle rotating the
core P(1, N) with weight N − 1 — trivial exactly when there is no locus (N = 1) — matching the known orbifold degrees.

## 1. The cone as a family, and its link

Kronheimer: for Γ = 2O the ALE spaces are μ_K⁻¹(ζ)/K, K = ∏ U(n_i)/U(1) over the affine E₇ quiver, ζ ∈ 𝔥(E₇) ⊗ ℝ³; the fibre is
singular along the root subsystem {θ : ⟨θ, ζ⟩ = 0}. AW's unfolding keeps ζ on the line of the omitted node: with the node α₇ beyond
E₆ (Bourbaki numbering; its index in the highest root 2α₁+2α₂+3α₃+4α₄+3α₅+2α₆+α₇ is n₇ = 1 — computed, so U(n₇) = U(1)′ is the
omitted factor itself), ζ = t ω₇ and the singular subsystem is {θ : m₇(θ) = 0} = the roots of E₆ (72 of the 126; computed to
coincide with the root system of the E₆ Cartan matrix). Hence:

- X_ζ (ζ ≠ 0) is the partial resolution of ℂ²/2O with the E₆ configuration collapsed and C₇ resolved; smooth away from the E₆ point
  p, which lies on C₇ (C₇ meets C₆); it deformation-retracts onto C₇ and H₂(X_ζ; ℚ) = ℤ⁷/ℤ⁶ ⊗ ℚ = ℚ (computed).
- X = ∪_{ζ ∈ ℝ³} X_ζ; scaling x ↦ λx maps X_ζ to X_{λ²ζ}; the right quaternionic action of Sp(1) on ℍ^k commutes with K and rotates
  ζ, so X_{Rζ} = R·X_ζ isometrically and the stabiliser U(1) of a direction acts on X_ζ as the hyperkähler circle (preserving the
  complex structure I_ζ, rotating the holomorphic symplectic form with weight 1).
- The family is a submersion onto ℝ³ wherever K acts freely (the differential of a moment map is surjective where the action is
  locally free), so the singular set of X is the E₆ points of the fibres — an ℝ³ through the apex — and the apex. **No other locus,
  no codimension-six lines.**
- The link Y = {|ζ| + |x|² = 1}: the map (ζ, x) ↦ (ζ̂, x/√|ζ|) identifies Y ∖ (central fibre) with the family ∪_{ζ̂ ∈ S²} X_ζ̂ of
  unit-parameter fibres, whose ends (x → ∞) are glued to the central fibre {ζ = 0, |x| = 1} = S³/2O by (ζ̂, y) ↦ y/|y|. The family
  over S² is the associated bundle A = Sp(1) ×_{U(1)} X_t.

## 2. b₂(Y) = 1

Mayer–Vietoris for Y = A ∪ B, B a neighbourhood of the central fibre (≃ S³/2O), A ∩ B ≃ the family of ends = Sp(1) ×_{U(1)} (S³/2O × ℝ).
Over ℚ: H*(X_t) = H*(S²) (the retraction onto C₇), and the Serre spectral sequence of A → S² with fibre X_t degenerates (the only
possible differential lands in zero) so H*(A) = H*(S²) ⊗ H*(S²), b₂(A) = 2 with basis the base class b and the fibre class f;
H*(B) = H*(S³; ℚ); H*(A ∩ B) from the spectral sequence with fibre a rational S³: H²(A ∩ B) = ℚ (the base class), H¹ = 0. Then
H²(Y) = ker(H²(A) ⊕ H²(B) → H²(A ∩ B)) ⊕ coker(H¹(A) ⊕ H¹(B) → H¹(A ∩ B)) = ker(ℚ² → ℚ) ⊕ 0, and the restriction sends b to the
non-zero base class of A ∩ B, so it has rank one: **b₂(Y) = 1.** (H¹(Y) = 0 likewise.)

## 3. The E₆ link pairs non-trivially

Let U ⊂ A be the section through the E₆ point p (fixed by the circle): U = Sp(1) ×_{U(1)} {p} ≅ S², the link of the E₆ locus. Let P
= Sp(1) ×_{U(1)} C₇ ⊂ A, a closed 4-cycle (the family of surviving curves) containing U. In the rational homology manifold Y the
intersection number is U · P = ⟨e(N_{P/Y}|_U), [U]⟩, and along U the normal of P in Y is the normal line N_p of C₇ in X_t at p, twisted
over the sphere by the circle: N|_U = Sp(1) ×_{U(1)} N_p, with Euler number (Hopf number) × (weight of the circle on N_p) up to the
orbifold order at p. The circle fixes p and acts on the orbifold tangent cone ℂ²/2T through an element of U(2) commuting with 2T —
the centraliser of 2T in gl(2, ℂ) is the scalars (computed, Schur) — and rotates dz₁ ∧ dz₂ with weight 1, so it acts as the scalar
e^{iφ/2}: weight ½ on every direction, in particular on N_p. Hence U · P ≠ 0, so [U] ≠ 0 and [P] ≠ 0 in H₂(Y; ℚ), H₄(Y; ℚ); with b₂ = 1
the generator w pairs non-trivially with U: **∫_U w ≠ 0.** Witten's inflow (hep-th/0108165 §3; B1355 §3) then applies verbatim: the
apex must carry chiral E₆-charged matter with U(1) charge — AW's one 27 of charge 1.

## 4. Calibration on AW's SU(N) cones (computed)

For G = SU(N), Ĝ = SU(N+1), X is the cone over WCP³_{1,1,N,N} (AW §2.2), U(1)′ acting on (a, b, c, d) with weights (1, −1, N, −N).
The core of the generic fibre is {b = d = 0} = P(1, N), the hyperkähler circle (right multiplication) rotates it modulo U(1)′ with
relative weight N − 1 — trivial exactly for N = 1, the cone over CP³ with no locus — fixing the Z_N point p and the smooth pole p′;
the two sections give the known orbifold degrees ∫_U H = 1/N² (U = P(N, N), the SU(N) link) and ∫_V H = 1 (V = P(1, 1)), both
non-zero for N ≥ 2, and b₂ = 1. The argument of §2–§3 reproduces the structure of the known case.

## 5. What it means for the closing

The apex of the destination has two local models, and the one AW built is the cleaner: its only singular stratum through the apex is
the E₆ locus. Three such apexes on the E₆ copy of Y₃ (B1357), as a deck orbit (B1356), give three 27s charged under the apexes' own
U(1)s in the sum-zero combinations, with the charge triples and the deck action of B1356 §2 unchanged (they used only b₂(link) = 1,
∫_U w ≠ 0 and the sum rule) — and no SU(2) copy is touched, so B1358's companion pinning and the doublet parity (THE_CLOSING §6.2)
do not arise. The three faces: the unfolding is arithmetic (the node beyond E₆ in E₇'s diagram, index 1), the link's topology is
geometric (an S²-family of partial resolutions glued to S³/2O), and the pairing is quantum (the hyperkähler circle acting as a scalar
on the McKay group's tangent cone). What the design still lacks is the same as before: the compact closing, and the integral
normalisation of w that fixes the 27's charge against the Z₃ global form.

## 6. Caveats

1. The homotopy model of the link (§1) is standard for hyperkähler quotients (the family structure over the omitted D-term, the
   Sp(1) rotation, the retraction of an ALE space onto its exceptional set) and every specific input is computed; it is not a
   computation of H*(Y) from a triangulation. The intersection-theoretic step (§3) uses orbifold Poincaré duality over ℚ.
2. b₂ is rational; the integral class and the precise value of ∫_U w (hence the charge normalisation) are not computed.
3. The G₂ metric on AW's X is theirs by duality, not constructed; the E₆ locus's normal type is 2T by the root computation.
4. The compact closing with three such apexes is not constructed; the sum rule's sufficiency (extension of the apex classes) is
   not decided.

## 7. Registered

- The integral structure: H²(Y; ℤ) and ∫_U w for the generator, to pin the 27's charge against (E₆ × U(1))/Z₃.
- The same argument for the D-type and other E-type unfoldings (the D₄ → SO(8) companion of B1357's background, for instance).
- Whether the twistor cone (B1355) and the Kronheimer unfolding are the two ends of one family of G₂ cones with an E₆ line.

## Verification

`verification/companion_free_apex.py` (seconds; record `companion_free_apex_run.txt`): the E₇ root system from the Cartan matrix
(126 roots, the highest root and n₇ = 1), the 72 roots with zero α₇-coefficient equal to E₆'s, the rank of ℤ⁷/ℤ⁶, the centraliser of
2T in gl(2, ℂ) by the commutator map, and the SU(N) calibration (relative weight N − 1, orbifold degrees). Lock:
`tests/test_b1360_the_companion_free_apex.py`.

**Sources.** Acharya–Witten, hep-th/0109152 §2.2–2.3 (the unfolding, the E₆ ⊂ E₇ case, "a useful way to describe the topology … is
not clear"); Kronheimer, J. Diff. Geom. 29 (1989) (the ALE spaces as quiver quotients; singular fibres from the root hyperplanes);
Witten, hep-th/0108165 §3 (the inflow); Berglund–Brandhuber, hep-th/0205184 (SU(N) and SO(2N) unfoldings; exceptional cases not
treated). B1355 (corrected), B1356–B1359 (this branch); main's B1413.
