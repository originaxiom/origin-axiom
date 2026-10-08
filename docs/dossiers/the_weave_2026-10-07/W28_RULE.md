# W28 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed.
Nothing here is a result.

## Why this route

- **The owner's approval** (2026-10-08, after the two contemplation turns): verify the picture in order. Steps 1 and 2
  first (the foundation), then step 3 (the ℤ₆ twist-eater, W29).
- **Step 1 (Part I).** W24's D0 showed that the moves alone keep four end conditions at the puncture (index −3, −1, +1,
  +3), and that ±3 needs the parity grading. Part I asks what the two middle conditions are, and whether a natural
  requirement other than the grading also excludes them.
- **Step 2 (Part II).** The contemplation read the common point as the qubit: the Pauli group, with the moves as its
  Clifford group, SU(2) level 1's modular data, the three global forms of su(2), and 't Hooft's twist-eater. Part II
  checks each identification.
- **Nothing here bears on the gauge content.** That is W29.

## Weave or thread?

- **Weave.** Every cell takes all the moves (the lifts of L and R, both signs; P and −I where named) and all three
  parities, at the common point, the one point every move fixes (W2).
- **Each quantity is defined by the joint action:** the commutants of all the lifts together, the group they generate,
  and its image in SO(3).
- **Each claim is about all threads at once:** the end condition every move keeps, and the group every move's lift
  lies in.

## Part I: the end condition (the script's cells E1–E5)

- **E1, the block form.**
  - In the block basis, every lift of L and R (both signs) is Π ⊗ G: an unsigned permutation Π of the three parity
    blocks, with the same G ∈ 2O in every block.
  - Π is the move's action on the three parities mod 2, an element of SL(2, 𝔽₂) ≅ S₃.
  - Also checked: the lifts intertwine the fibre's holonomy, A 𝕎(x) A⁻¹ = 𝕎(φ(x)).
  - **Prior 99%** (blocks_action builds it so; the cell states it).
- **E2, the two middle conditions.**
  - The pieces W24 D0 found are V₂ = {(v, v, v)}, the diagonal, and V₄ = {v₁ + v₂ + v₃ = 0}. The orthogonal
    projections onto them commute with every lift and span the commutant (dimension 2).
  - Under 2O, V₂ carries the spin doublet (character tr G). V₄ carries 2O's four-dimensional irreducible, the
    restriction of spin 3/2 (character (tr G)³ − 2 tr G, and norm 1).
  - So the six local solutions are a vector-spinor: spin ½ ⊗ spin 1 = spin ½ ⊕ spin 3/2. V₂ is its γ-trace part. In
    ρ_Q ⊗ ℂ³ coordinates V₂ is {Σ_p u_p v ⊗ e_p}, the Clebsch–Gordan copy of the doublet.
  - **Prior 95%.**
- **E3, the flavor group.**
  - The flat automorphisms of 𝕎 (the commutant of 𝕎(a) and 𝕎(b) on the six) form M₃(ℂ), dimension 9. Its unitary
    part is U(3), acting on the ℂ³ of 𝕎 ≅ ρ_Q ⊗ ℂ³.
  - The lifts normalise it.
  - Its invariant subspaces are λ ⊗ ℂ³ with λ ⊂ ℂ² (the commutant of the flavor algebra is M₂). So they have
    dimension 0, 3 or 6, and index −3, 0 or +3. The index-0 conditions form a ℙ¹ (a line λ).
  - **Prior 97%.**
- **E4, the middle conditions break flavor.** The subalgebra of the flavor algebra that maps V₂ into V₂ is the scalars
  (dimension 1). The same holds for V₄. So every flavor symmetry other than a phase moves the two middle conditions.
  **Prior 95%.**
- **E5, the index sets.** For each requirement, the set of indices of the end conditions that keep it, read from the
  commutant's isotypic structure (invariant subspaces have dimensions Σ kᵢ dᵢ with 0 ≤ kᵢ ≤ mᵢ):

  | requirement | predicted index set |
  |---|---|
  | the moves (the lifts of L and R) | {−3, −1, +1, +3} |
  | the flavor group | {−3, 0, +3} |
  | the parity grading | {−3, −2, …, +3} |
  | the moves and the flavor group | {−3, +3} |
  | the moves and the parity grading | {−3, +3} |
  | locality: the commutant of the puncture's own holonomy 𝕎([a, b]) = −1 (all of M₆) | {−3, +3} |

  - Also checked: 𝕎([a, b]) = −1 on all six.
  - **Prior 97%.**
  - **The reading, if it holds:**
    - Neither the moves alone nor the flavor group alone fixes the count. Jointly they force ±3.
    - So ±3 follows from one natural requirement: the end condition breaks no symmetry of the bulk problem (the
      moves and 𝕎's flat automorphisms). Locality gives the same.
    - The middle conditions couple the three parity sectors at the puncture with Clebsch–Gordan coefficients, and
      they break flavor to a phase.

## Part II: the common point as the qubit (the script's cells I1–I5)

The Pauli matrices are X, Y, Z with Z = diag(1, −1). The rotation of a 2 × 2 unitary U is Ad(U)_{ab} = ½ tr(σ_a U σ_b U†)
in the basis (X, Y, Z).

- **I1, the Pauli group.**
  - In the record's basis, ρ(a) = iZ, ρ(b) = iY and ρ(ab) = iX. So the fibre's holonomy Q₈ is the single-qubit Pauli
    group's lift to SU(2).
  - Each parity's unit u_p (W24 D1) is one Pauli axis: (0, ½) ↦ Z, (½, 0) ↦ Y, (½, ½) ↦ X. The parity's kernel is
    the holonomies along that axis.
  - The three eigenbases are mutually unbiased: |⟨e|f⟩|² = ½ across any two.
  - **Prior 99%.**
- **I2, the Clifford group.**
  - The lifts (CP.extend), up to sign:
    - L: e^{iπZ/4}, a quarter turn about Z (the phase gate, up to a phase);
    - R: e^{−iπY/4}, a quarter turn about Y;
    - P: (iZ + iY)/√2, a half turn about (Z + Y)/√2 (a Hadamard exchanging Z and Y);
    - −I: iX.
  - The lifts of L and R generate 2O (order 48), the normaliser of Q₈ in SU(2). This is checked as: 2O normalises
    Q₈, |Aut(Q₈)| = 24, and the kernel of the conjugation map is ±1.
  - Its image in SO(3), the 24 rotations of the cube, equals the image of the standard Clifford group ⟨H, S⟩.
  - **Prior 97%.**
- **I3, SU(2) at level 1** (the semion's modular data).
  - The data: S₁ = (1/√2)[[1, 1], [1, −1]] and T₁ = e^{−2πi/24} diag(1, i) (c = 1; h = 0, ¼).
  - Checks:
    - S₁² = 1 and (S₁T₁)³ = S₁².
    - Verlinde's loops on the torus: W_A = diag(S_{½,b}/S_{0,b}) = Z, and W_B = S₁ W_A S₁⁻¹ = X. They anticommute,
      W_A W_B = −W_B W_A, which is the common point's commutator −1.
    - T₁ fixes W_A and sends W_B to a multiple of W_A W_B.
  - The projective images: ⟨Ad S₁, Ad T₁⟩ and ⟨Ad g_L, Ad g_R⟩ are both the cube's 24 rotations.
  - The weave's images satisfy the relations of the (2, 3, 4) triangle group: t = Ad g_L, s = Ad(g_L g_R⁻¹ g_L),
    with s² = (st)³ = t⁴ = 1. So the moves act on the common point through PSL(2, ℤ/4) ≅ S₄.
  - **The dictionary.** Search the cube's rotations M for M Ad(ρ(a)) M⁻¹ = Ad W_A, M Ad(ρ(b)) M⁻¹ = Ad W_B,
    M Ad(g_L) M⁻¹ = Ad T₁ and M Ad(g_R) M⁻¹ = Ad(S₁T₁⁻¹S₁⁻¹) (R = S T⁻¹ S⁻¹ in SL(2, ℤ)).
    - Predicted: exactly one, x ↦ −y, y ↦ −x, z ↦ −z.
    - With T₁ replaced by T̄₁ (the anti-semion, (E₇)₁, h = ¾): also exactly one.
    - So the projective data match both. The hand is in the phases, which the weave's lifts in SU(2) do not carry.
  - **Prior 90%.**
- **I4, the three global forms of su(2)** (Aharony–Seiberg–Tachikawa, arXiv:1305.0318).
  - The maximal isotropic subgroups of (𝔽₂², the intersection form mod 2) are exactly three, {0, v} for v ≠ 0. That
    is ℙ¹(𝔽₂).
  - Each parity's kernel on the records mod 2 is one of them: (0, ½) ↦ {0, a}, (½, 0) ↦ {0, b}, (½, ½) ↦ {0, ab}.
  - With a electric and b magnetic, these are SU(2) (the Wilson line genuine), SO(3)₊ (the 't Hooft line) and SO(3)₋
    (the dyonic line).
  - The bijection is equivariant: every move's action on the parities (u_after) equals its action on the Lagrangians
    (MAT mod 2).
    - L is the θ → θ + 2π shift: it fixes SU(2) and swaps SO(3)₊ and SO(3)₋.
    - LR⁻¹L is S-duality: it swaps SU(2) and SO(3)₊ and fixes SO(3)₋.
  - Mutual locality is the character: χ_v(x) = (−1)^{ω(v, x)}.
  - **Prior 99%.**
- **I5, 't Hooft's twist-eater.**
  - Two unit quaternions anticommute only if both are pure and orthogonal (sympy, exact). So every pair in SU(2) with
    commutator −1 is conjugate to the common point.
  - Its centraliser in SU(2) is ±1.
  - The centre symmetry (A, B) ↦ (ε_a A, ε_b B), with ε ∈ {±1}²: each of its three non-trivial elements is
    conjugation by one unit u_p (W24 D1). So the twist-eater eats the centre symmetry, and the three non-trivial
    elements are the three parities ('t Hooft's electric flux sectors, H¹(T²; ℤ₂)).
  - **Prior 99%.**

## What each outcome means

- **All as predicted.** The foundation is locked.
  - **The count.** ±3 follows from the end condition breaking no symmetry of the bulk problem (the moves and the flavor
    group), or from locality. Λ's "kept apart" is then a consequence of a natural requirement, not a separate postulate
    about sectors. The two middle conditions are the vector-spinor's spin-½ and spin-3/2 parts.
  - **The reading.** The common point is the qubit, the moves are its Clifford group, the parities are the three
    Pauli axes, the three global forms of su(2) and ℙ¹(𝔽₂), and the moves act through SU(2) level 1's projective
    modular data. The hand is invisible to all of it, which is consistent with W26.
- **E2's V₄ not spin 3/2.** The vector-spinor reading fails. The count result (E5) stands on its own.
- **E5 different.** The count's status changes. Record it, and re-read W27's T2 before anything else.
- **I3's M absent, or more than one.** The weave matches SU(2)₁ only up to an outer twist. Record which.

## Seen before this was written

- **W24's D0:** commutant 2; pieces of dimension 4 and 2, each projecting with rank 2 onto every block; conditions
  {−3, −1, +1, +3}; commutant 1 with the grading. **D1's units:** (½, 0) ↦ j, (0, ½) ↦ i, (½, ½) ↦ k.
- **By hand:**
  - the lifts are Π ⊗ G (blocks_action), so the diagonal and the sum-zero subspace are invariant;
  - std ⊗ 2_s = spin 3/2 on the classes of 2O;
  - the stabiliser computation of E4 (only scalars);
  - the lifts g_L = (1 + i)/√2, g_R = (1 − j)/√2, g_P = (i + j)/√2 and g_{−I} = k (up to sign);
  - the rotation M of I3.
- **Literature, as recalled:**
  - Aharony–Seiberg–Tachikawa (global forms);
  - 't Hooft, Nucl. Phys. B153 (1979) 141 and Commun. Math. Phys. 81 (1981) 267 (flux sectors, twist-eaters);
  - Verlinde's formula and SU(2)₁'s modular data (standard);
  - the single-qubit Clifford group (standard).
