# B1527 — PREREGISTRATION: THE CUSP DECIDES — the class index on the projective deformations of the mirror-broken word states, near their hyperbolic point (sL-10 item 8)

**Sealed before `run.py` runs.** At the seal, this arc has computed only on m004's banked Ballas axis:
- `controls.py` (C1–C6, all pass; `controls_run.txt`, `controls.json`);
- a smoke test of `run.py`'s code paths on m004: Part H's two rows at the cusp-trivial character, which B1297's T3 already decides
  (ρ_hyp is self-dual), and the scan and polish at Ballas' axis. The other rows the smoke test computed were not read. §7 lists
  what it showed.

No other word state has been touched by this arc's code.

**Source.**
- The owner (2026-10-02): *"… all oallowed not just m004, choice might be golden"*, and that nothing load-bearing is to be
  ignored. The full message is quoted in sm:B1522's PREREGISTRATION.
- sL-10 item 8 (registered in sm:B1523 §5, OPEN_LEADS), verbatim: *"On the 262 mirror-broken manifolds, near the hyperbolic point,
  no count-odd map fixes a vacuum of the projective family other than that point (Lemma T, a local statement). So B1455's
  symmetry argument cannot force the family's count to zero there. Build the family off the hyperbolic point on the first of
  them: ±LLRLRR (swaprev-only, length 6) and ±L³RLR² (chiral, length 7) … Compute main's class index (B1297, B1455) on its
  vacua ν ⊗ ρ_s. Is any of them nonzero? The control is m004's family … Seal before computing."*

## 0. Seen first, and PRIOR ART:

**The repo sweep.** `scripts/checks/prior_work.py`, 2026-10-03, after `git fetch --all`, against these heads:

| head | commit |
|---|---|
| main | `5c0951b7` |
| the audit lane | `24c039c8` |
| this branch | `48f6af3b` |
| seat/determined-hopper | `7cda35aa` |
| seat/magical-wright | `0043be2b` |
| seat/outside-bench | `13d2c5b6` |
| seat/paper-review-verification | `5d58b935` |
| seat/physics-seat-evaluation | `659487bb` |
| sep16-branch | `3205984b` |
| art/camper-van-bar | `b3745696` |

Terms: "type 1 cusp", "type-one", "type one cusp", "type 2 cusp", "generalized cusp", "unipotent direction", "Theorem 5.8",
"p-curve", "slice coordinates", "acyclic cusp", "mirror-broken", "infinite volume".
- **Absent on every head:** "type 1 cusp", "type one cusp", "type 2 cusp", "unipotent direction", "Theorem 5.8", "p-curve",
  "slice coordinates".
- **"type-one"** is only the audit lane's R44 and R48 (`CANONICAL_CUSP.md`, `CANONICAL_DUALITY.md`) and main's B1457 readers that
  row them. Read: on m004's Ballas curve (q > 0, q ≠ 1) the ends are type-one generalized cusps with one-dimensional ideal flats;
  R44 shows the end has finite volume. R44 §1 also uses the fact this arc generalises: *"On the peripheral torus Λ − I is
  invertible for q ≠ 1, also after unitary twisting and on the dual: all longitude eigenvalue moduli are q or q⁻³, never 1. The
  torus Koszul complex is acyclic."*
- **This branch's sm:B1509 T1** has the same fact for m004, for every twist: a character of H₁(m004) is trivial on the longitude,
  which bounds the fibre, so the projective four, its dual and Λ² have no boundary cohomology when q ≠ 1, and I = 0 by B1297's
  identity. Lemma C below is that argument on every word state and every representation. It is credited to sm:B1509 T1 and to
  R44.
- **"generalized cusp"**: this branch's sm:B1513, sm:B1515 and sm:B1523 preregistrations cite Ballas for m004's family or for the
  family's existence. Nobody computes a cusp type off m004.
- **"acyclic cusp"**: item 8's own text and its copies on the seat lanes.
- **"mirror-broken"**: this branch only (sm:B1523 and its surfaces).
- **"infinite volume"**: unrelated (the audit lane's product normal line; a Corlette citation note).
- **So no head computes the cusp type of any projective deformation off m004, or the class index on one.**

**The literature.** Each read on 2026-10-03 at the place cited (texts in the seat's scratchpad, extracted from the arXiv PDFs).
- **S. Ballas**, *Constructing convex projective 3-manifolds with generalized cusps*, arXiv:1805.09274v3:
  - (3.1): the slice S, ρ_s(γ_i) = exp(m^i_s), m = x(E12 + aE22 + E24) + y(E13 + bE33 + E34); ϖ(M) = |det M|^(−1/4) M (p. 15).
  - Thm 3.2: points of S are holonomies of generalized cusps of type 0, 1 or 2 (b = 0, a ≠ 0: type 1; both non-zero: type 2).
  - Prop. 3.6 and Cor. 3.7: at a type-0 point the only redundancy of S up to conjugacy is the cusp shape's (a rotation).
  - §4, the strategy paragraph: *"S has dimension 5 and hence codimension 13 in Hom(Z², G). Thus the intersection of S and the
    image of res is a 2-dimensional submanifold. However, by Proposition 3.6, only 1 of these dimensions is accounted for by
    conjugacy"*. Thms 4.1 and 4.2 (codimension 3).
  - Thm 5.1 and Remark 5.2: slice coordinates; both non-zero gives type 2; one zero gives type 1 or 2 (first order only).
  - Lemma 5.3, Thm 5.8, Cor. 5.9, Lemmas 5.10–5.11: an orientation-reversing symmetry acting as the identity on H¹(Γ; v) gives
    type-1 structures; in (5.6)–(5.7) the p-curve γ₊ has the simple eigenvalue e^{3t} and γ₋ stays unipotent to first order.
  - Introduction (pp. 2–3): *"a 'generic' deformation constructed by Theorem 0.2 will have only type 2 cusps"*, and type 1 is
    obtained there only through symmetry.
- **S. Ballas, D. Cooper, A. Leitner**, *Generalized cusps in real projective manifolds: classification*, arXiv:1710.03132:
  - the unipotent rank u(ψ) = max(n − t − 1, 0) (p. 1);
  - Thm 0.6: a generalized cusp has finite volume iff u(ψ) > 0 iff G(ψ) contains a parabolic. For n = 3: types 0 and 1 have
    finite volume, types 2 and 3 do not;
  - Thm 0.5: the underlying Euclidean structure.
- **S. Ballas, J. Danciger, G.-S. Lee**, arXiv:1508.04794, Thm 3.2: rigid rel ∂M makes ρ_hyp a smooth point.
- **M. Heusener, J. Porti**, arXiv:0908.2863, Def. 7.1 (a rigid slope), Lemma 5.5 and Remark 5.6 (π/3), as read for sm:B1523.
- **M. D. Bobb**, *Convex projective manifolds with a cusp of any non-diagonalizable type*, arXiv:1808.02779 (intro, Thm 8.2):
  every non-diagonalizable type is realised, by bending arithmetic manifolds along totally geodesic hypersurfaces. Nothing on
  type 1 near ρ_hyp without symmetry.
- **C. Daly**, arXiv:2411.04431 and 2408.08405: rigidity certificates; no cusp types.
- **A web search** (2026-10-03: generalized cusps type 1 without symmetry; type 1 once-punctured torus bundles) found these and
  nothing that computes cusp types on punctured-torus bundles or states the dimension of the generalized-cusp locus near ρ_hyp.

## 1. The question

On a mirror-broken word state, near its hyperbolic point, is the class index of any vacuum ν ⊗ ρ_s of a projective deformation
non-zero? Asked for the projective four ν ⊗ ρ_s and for ν ⊗ Λ²ρ_s, every character ν of Γ.

What changed since the item was registered: the deformations near ρ_hyp are not one family. Ballas' count (§0) leaves a
two-dimensional set S ∩ I, of which conjugacy accounts for one dimension only at the hyperbolic point itself. Proposition Π (§3)
draws the consequence: the generalized-cusp locus near ρ_hyp is two-dimensional, with three type-one curves through ρ_hyp and
type two elsewhere. So item 8 is answered here on the whole locus near ρ_hyp, not on one curve:
- on the type-one curves (finite volume, BCL Thm 0.6), by Part A;
- on the type-two points, by Lemma C, except on the curves where ρ(ℓ) acquires the eigenvalue 1. Those are left as the next
  question (§9).

## 2. Definitions and conventions

- **The word state** (sign, word): Γ = ⟨a, b, t ∣ t x t⁻¹ = φ(x)⟩, φ = ι^[−] ∘ φ_{w₁} ∘ … ∘ φ_{wₙ}, φ_L: a ↦ ab, φ_R: b ↦ ba,
  ι: a ↦ a⁻¹, b ↦ b⁻¹ (sm:B1523's route F; `family_lib.word_group`).
- **The cusp** Δ = ⟨ℓ, t′⟩: the fibre boundary ℓ = abAB (sm:B1523's μ) and the section t′ = t (sign +) or abt (sign −)
  (sm:B1523's λ up to a multiple of ℓ).
- **Characters.** ν(a), ν(b) torsion with ν ∘ φ = ν on F (there are D = ∣det(M − 1)∣ of them, M the homology matrix), and
  ν(t) = λ ∈ ℂ*. Always ν(ℓ) = 1, since ℓ is a commutator. **λ_c** is the twist making ν trivial on t′: λ_c = 1 for +, and
  (ν(a)ν(b))⁻¹ for −. It is unitary.
- **The index** (main's B1297): n(V) = dim ker(H¹(Γ; V) → H¹(Δ; V)), I(V) = n(V) − n(V*). Its identities: B1297's
  I = (a0 − b0) + s0 − r1, and r1 + q1 = h¹(Δ; V) = t0 + s0. Here a0 = h⁰(Γ; V), b0 = h⁰(Γ; V*), t0 = h⁰(Δ; V),
  s0 = h⁰(Δ; V*).
- **The slice** (Ballas (3.1), SL-normalised): ρ(γ) = |det|^(−1/4) exp(X_γ N_a + Y_γ N_b), with N_a = E12 + aE22 + E24 and
  N_b = E13 + bE33 + E34, for γ ∈ Δ. The SL eigenvalues of ρ(γ) are e^{−(ψa+ψb)/4} (twice), e^{(3ψa−ψb)/4} and e^{(3ψb−ψa)/4},
  where ψa = aX_γ and ψb = bY_γ. Type one: exactly one of a, b is zero. Type two: both non-zero.
- **The frame.** α is the angle of ℓ's translation in the slice's (X, Y) plane. β is the angle of the unipotent line (X = 0,
  when b = 0) measured from ℓ mod 180°, in the orientation that puts t′ at an angle in (0°, 180°).
- **The scale.** Fixing a fixes the slice's scaling, (a, b, X, Y) ~ (a/s, b/s, sX, sY), which is a conjugation. So a fixed a is
  a chart, not a radius. The distance from ρ_hyp is set by ψ = aX, about a × (the translations of ρ_hyp).

## 3. The theorems (proved at design time)

**Lemma C (the cusp decides).** Let ρ: Γ → GL(n, ℂ) be any representation of a word state with ρ(ℓ) having no eigenvalue 1, and ν
any character. Then H*(Δ; ν ⊗ ρ) = 0 = H*(Δ; (ν ⊗ ρ)*), and I(ν ⊗ ρ) = a0 − b0.
- *Proof.* ν(ℓ) = 1, so (ν ⊗ ρ)(ℓ) = ρ(ℓ) has no fixed vector, and neither has its inverse transpose. So h⁰(Δ) = 0 for V and V*.
  On T², h² = h⁰ of the dual (Poincaré duality) and χ(T²) = 0, so h¹(Δ) = 0 too. B1297's T5 (an acyclic cusp gives
  I = a0 − b0) finishes.
- On m004's Ballas family this is sm:B1509 T1 and the audit lane's R44 §1. Here it holds on every word state and every
  representation.

**Lemma E (the index through h¹).** For V flat on a word state (χ(M) = 0, one torus cusp):
I(V) = h¹(Γ; V*) − h¹(Γ; V) + 2(a0 − b0) + s0 − t0.
- *Proof.* From the pair's sequence, n(V) = h¹(M, ∂M; V) − (t0 − a0). Poincaré–Lefschetz duality gives
  h¹(M, ∂M; V) = h²(M; V*), and χ = 0 with h³ = 0 gives h²(V*) = h¹(V*) − b0. So n(V) = h¹(V*) − b0 − t0 + a0. Swapping V and
  V* and subtracting gives the formula.
- It makes a second route (W) possible: h¹ through the fibration, with no restriction map (§4).

**Part H (the hyperbolic point).** On every word state, for every character ν and the hyperbolic holonomy ρ_hyp in SO(3,1):
I(ν ⊗ ρ_hyp) = 0 and I(ν ⊗ Λ²ρ_hyp) = 0.
- *Proof.* ρ_hyp(Δ) is unipotent: the Hermitian map g ↦ (H ↦ gHg*) kills the sign of a ±parabolic.
  - If ν(t′) ≠ 1, every element of ν ⊗ ρ_hyp(t′) has the single eigenvalue ν(t′) ≠ 1. So the cusp is acyclic for V and V*.
    ρ_hyp is irreducible (Borel density), so a0 = b0 = 0, and Λ²ρ_hyp ⊗ ℂ = Ad h ⊕ Ad h̄ has no invariant line. T5 gives I = 0.
  - If ν(t′) = 1, then λ = λ_c and ν is unitary. ρ_hyp and Λ²ρ_hyp are real and self-dual (the form, the Killing form). So
    V* ≅ ν̄ ⊗ ρ = conj(V). Complex conjugation is a semilinear isomorphism of the restriction sequences, so n(V*) = n(V) and
    I = 0.
  - Predicted data: at λ_c, t0 = s0 = 1 for the four (the fixed null vector) and 2 for Λ² (the translations); elsewhere
    t0 = s0 = 0.

**Part A (type one near ρ_hyp).** Let ρ_s (s near 0) be a smooth path with ρ_0 = ρ_hyp, non-zero tangent, and ρ_s|Δ conjugate,
smoothly in s, into Ballas' slice with b ≡ 0. On a word state that is rigid rel cusp with ℓ a rigid slope (all 536 by sm:B1523,
P2 and P6), ρ_s(ℓ) has no eigenvalue 1 for every small s ≠ 0. So by Lemma C, I(ν ⊗ ρ_s) = I(ν ⊗ Λ²ρ_s) = 0 for every ν.
- *Proof.* Write the slice path s ↦ (a(s), 0, X(s), Y(s)), with limit frame s₀ ∈ C. Its tangent is w = ȧD_a + (so(3,1)-valued
  cocycles from the translations). So the v-part of the family's class restricted to the cusp is c = ȧ[π_v D_a].
- A non-zero tangent with c = 0 would have a pure so(3,1) tangent. That makes the cusp loxodromic at first order, outside S. So
  ȧ ≠ 0.
- D_a(ℓ) = ∂_a ϖ(exp(X_ℓ N_a + Y_ℓ N_b)) vanishes when X_ℓ(s₀) = 0, since a enters only through aX. Then c∣ℓ = 0, which
  contradicts ℓ being a rigid slope. So X_ℓ(s₀) ≠ 0.
- Hence ψ(ℓ) = a(s)X_ℓ(s) = ȧ X_ℓ(s₀) s + O(s²) ≠ 0 for small s ≠ 0. The SL eigenvalues e^{−ψ/4} and e^{3ψ/4} are not 1. The
  same holds for Λ², with eigenvalues e^{±ψ/2}.
- a0 = b0 = 0 near ρ_hyp: ρ_s is irreducible (an open condition), and ν ⊗ Λ²ρ_s has no invariant line. Such a line would be a
  common eigenvector of Λ²ρ_s(F) with a torsion character, F being Zariski dense in PSL(2, ℂ) at s = 0 (a non-elementary
  normal subgroup). The condition is closed in s, so it fails near 0 uniformly in ν.

**Proposition Π (the polar locus).** On every one-cusped hyperbolic M rigid rel cusp (every word state, by sm:B1523), the
representations near ρ_hyp whose cusp is a generalized cusp form a two-dimensional set L, the image of the annulus S ∩ I. In it:
- the type-one points form three smooth curves through ρ_hyp, six branches from ρ_hyp;
- their limiting axes are 60° apart, and their unipotent lines tend to the three zero lines of the family's cusp class (sm:B1523's
  Lemma S);
- every other point of L \ {ρ_hyp} is type two.

*Proof, with the cited steps marked.*
1. (Ballas §4, cited) S ⋔ I at ρ_hyp∣Δ, and S ∩ I is a two-dimensional submanifold.
2. Transversality holds at every point of the rotation circle C_z (all conjugate to ρ_hyp∣Δ). The circle lies in S ∩ I, so near it
   S ∩ I is an annulus (θ, t), θ the frame and t transverse with (ȧ, ḃ) ≠ 0. (C ∩ I is the circle, by Mostow and rigidity rel
   ∂M.)
3. Off C, S is a slice: its normaliser equals the centraliser of the slice group, dimension 3 (computed, `controls.py` C6; at C
   the normaliser has dimension 5, rotation and scaling). The eigenvalue forms ψa = aX and ψb = bY pin the frame. So points
   (θ, t) with t ≠ 0 are pairwise non-conjugate, and L is two-dimensional.
4. In the frame θ the slice coordinates of the fixed class c are (ȧ, ḃ)(θ) ∝ (cos, −sin)(3θ − φ₀). The frame rotation acts on
   H¹(Δ; v) ≅ ℂ with weight 3 (sm:B1523's Lemma S: the classes c_a vanish on slope t iff Re(a t³) = 0).
5. b(θ, t) = t·β(θ, t) with β(θ, 0) = ḃ(θ), which has simple zeros at six frames (three axes). The implicit function theorem gives
   the curves θ = θ_k(t), on which b = 0 and a = ȧ(θ_k)t + O(t²) ≠ 0: type one. Elsewhere a ≠ 0 ≠ b: type two.
6. Each type-one curve's unipotent line is ⊥ its axis. By step 4 at the axes, that is a zero line of c.

**Corollary (finite volume carries no reductive count near ρ_hyp).** On every word state, every finite-volume convex projective
structure near the hyperbolic one with generalized cusps (types 0 and 1, BCL Thm 0.6; by Π these are ρ_hyp and the three
type-one curves) has I(ν ⊗ ρ) = I(ν ⊗ Λ²ρ) = 0 for every ν. Part H covers ρ_hyp, Part A the curves.

**What Π changes in the record.** sm:B1523's "one-parameter projective family at the hyperbolic point" is one curve of L (Ballas'
Thm 0.2 builds one per frame). Ballas' symmetric type-one family (Thm 5.8) is the case where a symmetry pins one of the three
curves to a straight line, making the inverted slope γ₋ exactly unipotent (Lemma 5.11). Π says the other two curves, and all
three on a state with no symmetry, exist anyway. The literature read (§0) does not state this. It is claimed only as far as the
sweep, and only if P2–P5 confirm it.

## 4. The instruments

- **Route Fox** (`cusp_lib.py`): B1297's index by Fox calculus on Γ's presentation at 60 digits. Every reading checks three
  identities (B1297's; r1 + q1 = t0 + s0; Lemma E) and keeps the smallest-kept and largest-dropped singular values.
- **Route W** (`wang_lib.py`): h¹ through the fibration (Lyndon–Hochschild–Serre: H¹(Z; V^F) and the t-fixed part of
  H¹(F; V) = V²/δV), then the index by Lemma E. It has its own Fox routine on F, its own ranks, and no restriction map.
- **The scans** (`scan_lib.py`, float64, Levenberg–Marquardt with complex-step Jacobians):
  - the type-one system: 66 residuals, 52 unknowns; b = 0 and a fixed;
  - the b-free system: 53 unknowns.
  - Seeds: the hyperbolic point (sm:B1523's route F holonomy, `family_lib.hyperbolic_sl2`) in the cusp frame rotated by
    0°, 5°, …, 355°.
  - Converged: ∣F∣ < max(10⁻¹¹, 100 × the seed's own residual at a = 0). The float64 floor grows with word length: 10⁻¹⁴ on
    +LR, 10⁻⁸ on −LLLLRLRRRLRR.
- **The polish** (`family_lib.solve_type_one`, 60 digits): to ∣F∣ < 10⁻⁴⁸.
- **The Jacobian nullity**: read at the largest ratio among the eight smallest singular values.
- **`run.py`** (sealed with this file) runs H, S1, S2 and P per manifold. **`read_out.py`** (sealed) reads P1–P8.

## 5. The manifolds

| manifold | class (sm:B1523) | D (torsion characters) | why |
|---|---|---|---|
| +LR = m004, −LR | reflective (rev, swap, swaprev) | 1, 5 | the control; Ballas' family on +LR |
| +LLRLRR, −LLRLRR | swaprev-only, mirror-broken | 13, 17 | item 8's first; Ballas Cor. 5.9 applies |
| +LLLRLRR, −LLLRLRR (±L³RLR²) | chiral, mirror-broken | 18, 22 | item 8's first chiral |
| +LLLLRLLLRR, −LLLLRLLLRR (±L⁴RL³R²) | chiral, golden (trace 47) | 45, 49 | the owner's "golden" |
| +LLLLRLRRRLRR, −LLLLRLRRRLRR (±L⁴RLR³LR²) | chiral, golden (trace 123) | 121, 125 | the other golden pair |

## 6. Predictions (sealed; `read_out.py` reads them)

| # | prediction | reason | prior |
|---|---|---|---|
| P1 | Part H: I = 0 on every row (all D characters × {λ_c, 1, 1.7, e^{0.9i}, −1} × both modules); t0 = s0 = 1 or 2 at λ_c, 0 elsewhere; a0 = 0; route W agrees on every row it reads; every identity and margin holds | theorem; the risk is a bug | 97% |
| P2 | on every manifold the type-one scan finds exactly six frames (α-clusters) and three unipotent lines (β, mod 180°), pairwise 60° ± 1° apart | Π (step 4's weight 3, Ballas' two-dimensional S ∩ I) | 80% |
| P3 | on the four reflective manifolds the lines extrapolated to a = 0 lie at 30°, 90°, 150° ± 0.3° from ℓ (sm:B1523's coset), and the 90° family has a lattice slope exactly unipotent (∣X∣ < 10⁻²⁵ after polish: m004's section; −LR's (1, 2); ±LLRLRR's γ₋) | Π with Ballas' Lemma 5.11 | 85% given P2 |
| P4 | Part A at every polished type-one point: ρ(ℓ) has no eigenvalue within 10⁻⁶ of 1; for every tested (ν, λ, module) the cusp is acyclic (t0 = s0 = h¹(Δ) = 0), a0 = b0 = 0, I = 0; route W agrees; identities and margins hold | theorem (Part A, Lemma C) | 97% |
| P5 | the b-free scan: at least half the seeds converge, at least 90% of those within 5° of their seed's frame, and b changes sign across every type-one frame (the nearest converged points within 15° on either side have opposite b) | Π: L is two-dimensional, b vanishes exactly on the type-one curves | 70% |
| P6 | on every manifold some converged type-two point pair (within 15°, ∣b∣ < 50a) brackets a sign change of ψa + ψb, 3ψa − ψb or 3ψb − ψa at ℓ: the eigenvalue-one curves exist on the type-two part of L | first order: these are trigonometric polynomials in θ with real zeros | 75% |
| P7 | at every polished type-one point the Jacobian nullity is 4 for the type-one system and 5 for the b-free one (gauge 3, plus the curve and the surface), each with a gap ratio > 10⁶ | Π; at m004's axis it is already so (C6, disclosed) | 85% |
| P8 | the four golden manifolds behave as the two chiral ones: P2 and P4 hold on all six | the field does not enter Π or Part A | 90% |

**Outcomes.**
- **A:** P1, P2 and P4 hold. Item 8 is answered NEGATIVE on every computed state: every finite-volume projective deformation near
  the hyperbolic point carries no reductive count, mirror-broken or not. The mirror-broken states have finite-volume type-one
  deformations as the symmetric ones do. Routed to the kill graph with its scope (near ρ_hyp; reductive modules ν ⊗ ρ and
  ν ⊗ Λ²ρ; types 0 and 1).
- **B:** P1 and P4 hold, but P2 fails on a chiral or golden state (no type-one frame found). Then near ρ_hyp those states have no
  finite-volume deformation with generalized cusps found by this scan, and Π fails there. A step of Π's proof is wrong and is
  logged.
- **C:** P1 or P4 fails. A non-zero index at the hyperbolic point or on a type-one curve contradicts Lemma C, Part H or Part A.
  Bug until shown otherwise: both routes, the identities and the margins are re-examined before anything is claimed.

Expected count: 0.97 + 0.80 + 0.68 + 0.97 + 0.70 + 0.75 + 0.85 + 0.72 ≈ 6.4 of 8.

## 7. Controls and disclosures (before the seal, m004 only)

`controls.py`, all pass (`controls_run.txt`):
- **C1** the slice in closed form against mpmath's expm: 3.3 × 10⁻¹⁵.
- **C2** route Fox reproduces sm:B1509's exact extension indices on Ballas' presentation:
  - at q = 17 ± 12√2 with μ = −1: I(W₁) = −1, I(W₂) = +1, and W₁'s data (0, 1, 1, 1);
  - at q = 7 + 4√3 with μ = i: 0.
  This is the positive control: the instrument detects non-zero indices.
- **C3** the isomorphism of Ballas' presentation onto +LR (a = nm⁻¹, b = mn⁻¹mnm⁻², t = m): relators to 3 × 10⁻⁵⁸. abAB has the
  power sums of (q, q, q, q⁻³) to 9 × 10⁻⁵⁸, so it is the knot longitude.
  - Disclosed: C3's first form compared eigenvalues at 10⁻⁴⁰. A Jordan block limits those to about 10⁻³⁰ at 60 digits, so it
    failed on its own design. It was replaced by power sums before any other state was touched.
- **C4** W₁ and W₂ transported to +LR: routes Fox and W agree, I = −1 and +1, every identity (Lemma E included) holds.
- **C5** the type-one solver at Ballas' axis reproduces Ballas' family:
  - eleven traces agree with ρ_q transported to 3 × 10⁻³¹ (40-digit polish), with q = 0.99324 read off ℓ;
  - the section is unipotent (X_t ≈ 10⁻³⁰).
- **C6 (disclosed; it bears on Π)** at that point (a = 0.01):
  - the type-one system's nullity is 4 and the b-free system's is 5. The gauge is 3: the slice group's centraliser, for type one
    and type two alike.
  - So the type-one set is a curve and the generalized-cusp set a surface, at that point.
  - The b-free solver, started there, landed on a nearby type-two point with b/(a × frame offset) = −3.0000003: the weight 3 of
    Π's step 4.
  - This is local evidence for Π on m004. P2–P7's global tests (the three frames, the coset, the sign pattern) were not run.

The smoke test of `run.py` on m004:
- Part H's λ_c rows: I = 0 and t0 = 1 and 2, which B1297's T3 decides (ρ_hyp self-dual).
- Ballas' axis: β = 90° to 4 × 10⁻⁹ degrees; the polish reached 7 × 10⁻⁵¹ in 10 iterations; the section is unipotent to
  2 × 10⁻⁴⁸; nullities 4 and 5.
- After the smoke test, two robustness edits were made to `run.py` before the seal, both prompted by scale (the hyperbolic
  holonomy's words have entries up to 7 × 10³ on −LLLLRLRRRLRR):
  - the convergence threshold made relative to the seed's own float64 floor;
  - the nullity read at the largest singular-value gap rather than a fixed relative threshold.

## 8. BANKED IDENTITY: checked before reading

`controls.py` is re-run first and must match `controls.json`. Every reading must carry its identities (B1297's, the
annihilator, Lemma E) and its margins. A row failing an identity is a bug, not a result.

## 9. What this arc does not decide (the next questions)

- **The eigenvalue-one curves of the type-two part of L** (P6 tests only that they exist). There ρ(ℓ) has eigenvalue 1, the cusp
  is not acyclic for one twist λ, and by Lemma E the index is h¹(V*) − h¹(V) + s0 − t0, which can jump at isolated points. These
  points have infinite volume (BCL Thm 0.6). Registered as the next arc, sealed separately.
- **Non-split extensions** (sm:B1509's W₁, W₂, where the index is ∓1) on the type-one curves of the mirror-broken states.
- **Far from ρ_hyp** (Part A is local), and representations outside Ballas' slice (types 3 and loxodromic cusps).
- **0 of 19 stays 0.** A NEGATIVE here closes one place a count could live: the reductive vacua of finite-volume projective
  deformations near the hyperbolic point. It does not close the others above.
