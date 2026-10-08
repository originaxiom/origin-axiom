# W21 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed.
Nothing here is a result.

## Why this route

- **W20's count is not chiral** (its erratum). Group cohomology cannot tell a representation from its conjugate, so a
  chiral count needs a holomorphic quantity.
- **The weave has a complex structure of its own: the fibre's.**
  - Every point τ of the weave's moduli (every thread at once, W19) is a complex structure on the shared fibre.
  - The records' orientation fixes the half-plane: the puncture loop is [a, b], so a·b = +1 and Im τ > 0 for
    τ = ∫_b dz / ∫_a dz.
- **On a Riemann surface the chiral zero modes are holomorphic.** The kernel of the Dirac operator twisted by a bundle
  is H⁰ of that bundle times a spin structure, and its index is the degree.

## The objects, each named by principle

- **The fibre.** F₂ = ⟨a, b⟩, the once-punctured torus every thread shares, with puncture loop [a, b].
- **The common point** ρ_Q: a ↦ i, b ↦ j, [a, b] ↦ −1. It is the only point every move fixes with the puncture
  parabolic (W2, GENESIS GM4).
- **The three parities** χ_p, the non-zero classes of the records mod 2.
  - All three are taken, because the moves permute them transitively.
  - On the fibre E they are the three even spin structures, the non-trivial square roots of K_E = O. The zero parity
    is the odd one.
- **The space.** The local system 𝕎 = ⊕_p χ_p ⊗ ρ_Q, and V = H¹(F₂; 𝕎) (W10), six-dimensional.
  - Every class is interior, since ρ_Q([a, b]) = −1.
  - The moves act with the seat's lifts. Both braid-consistent choices are read.
- **The triplets** (Theorem H, W10). Under L and R, V = T ⊕ T̄, both irreducible, with T ≇ T̄.
  - T is named canonically here. It is the triplet on which Z acts as −i, where Z = S², the lift of −I, and
    S = (L R⁻¹ L)⁻¹ in braid-consistent lifts.
  - Both lift choices give the same Z.
- **The spin doublet** M = H¹(F₂; ρ_Q) (W9), the zero parity. It has two lines, μ₋ (Z = −i) and μ₊ (Z = +i).

## The theorem the route rests on (proved here; the code checks its consequences)

- **The Hodge decomposition.** For τ in the upper half-plane, V carries the Hodge decomposition of the twisted
  cohomology of E_τ ∖ {0}: V = V^(1,0)_τ ⊕ V^(0,1)_τ.
  - Each parity gives one line to each part. This is Riemann–Roch for the parabolic extension, which has degree −1
    because of the puncture's −1.
  - Equivalently, by Chevalley–Weil on the genus-3 cover w⁴ = cubic(x), whose odd holomorphic forms are dx/w³ and
    x dx/w³.
  - So dim V^(1,0) = 3.
  - V^(1,0)_τ is the kernel of the fibre's Dirac operator for the three even spin structures, with the common point as
    the gauge field. Its index is the degree: one per spin structure.
- **The weave theorem.**
  - The monodromy of V under all moves is finite: order 96 (W10).
  - So the period map τ ↦ V^(1,0)_τ descends to a finite cover of the modular curve. It is holomorphic, and bounded
    (the Hodge–Riemann form Q makes its target a bounded domain).
  - It therefore extends over the cusps, and so it is constant.
  - Hence V^(1,0) is one subspace for every τ. It is invariant under every move, so it equals T or T̄.
  - The proof uses the whole group. A single thread's group is cyclic, fixes no τ and gives no compact quotient. On a
    thread alone the holomorphic part need not be invariant.
- **What decides which.**
  - Q(u, v) = i ∫ u ∧ v̄ is the cup product taken with the invariant hermitian form. It is positive on V^(1,0) and
    negative on V^(0,1).
  - Q is topological. So the Hodge type of T is read from the sign of Q on T, without computing a period.

## The read-out (one run)

- **Q on V,** from the cup product on the relative class of the punctured torus:
  Q(u, v) = i [H(u(a), ρ(a) v(b)) − H(u(aba⁻¹), ρ(aba⁻¹) v(a))].
  Here u is normalized by a coboundary so that u([a, b]) = 0.
- **The controls.** Each must hold before the read-out is accepted.
  - On trivial coefficients Q is the Riemann bilinear form: Q(dz, dz) = 2 Im τ for (∫_a dz, ∫_b dz) = (1, τ).
  - Q is hermitian, and it does not depend on the cocycle chosen in each class.
  - Q is invariant under L and R with every lift.
  - The swap P reverses its sign, because P reverses the orientation.
  - Q is nondegenerate, with signature (3, 3) on V and (1, 1) on M.
  - T and T̄ are Q-orthogonal.
- **The read-outs.**
  1. The signs of Q on T and on T̄: which triplet is holomorphic. Each must be definite, and the two signs opposite.
  2. The same on M's two lines: which line is holomorphic. Then its character μ on L and on S, written as a power of
     η's character (j mod 24).
  3. Z on the holomorphic triplet.
  4. Whether T_hol = μ_hol ⊗ P, with P factoring through PSL(2, ℤ/4) ≅ S₄. This reads again W10's "S₄'s triplet
     times a character of ℤ/8".

## Seen before this was written

- **The structural check.**
  - With the lifts (0, 1) and (1, 0) the braid relation holds.
  - S² = −i on T (as named here) and +i on T̄; (ST)³ = S²; S⁸ = 1.
  - The eigenvalues of L, S and SL on T.
- **W9 and W10.**
  - W9: L and R act on M by rotations through 45° and 135°, with W9's lifts; the group is cyclic of order 8.
  - W10: the group on V is A₄ ⋊ ℤ/8, and T is S₄'s triplet times a faithful character of ℤ/8.
- **The count and the cover.**
  - The Riemann–Roch count above.
  - The genus-3 cover: on w⁴ = cubic, the automorphism J: w ↦ iw is a lift of −I and acts on both odd holomorphic
    forms by +i.
  - Whether the braid lift Z equals J or −J was not settled. So this does not decide the read-out.
- **A route set aside.** The Riemann–Roch index of vector-valued modular forms for T at its allowed weight 1/2. By
  hand on the seen eigenvalues it gives −1. The principle fixes no weight, so it is not used.
- **Nothing about the sign of Q.**

## What each outcome means

- **Q definite and opposite on T and T̄** (the theorem's prediction).
  - The holomorphic zero modes on the weave's fibre are one chiral triplet: three states, one per parity, all of one
    chirality.
  - The triplet is irreducible under the weave's group and not equivalent to its conjugate. Its index is three.
  - That is a chiral three, on the weave, and it is the same three as the parities.
  - Which triplet it is names the hand relative to the records' orientation. The swap reverses the orientation and
    exchanges the triplets, so the absolute hand is that orientation. In physics the name of a hand is a convention;
    that a hand exists is not.
- **Q not definite on T or T̄, or T and T̄ not orthogonal:** the theorem or the code is wrong. Stop, and find the error
  before any reading.
- **The links that stay readings,** with their status:
  - the dictionary: holomorphic zero modes on the internal fibre are the left-handed matter. This is the standard
    compactification reading (GENESIS FK11, I-26).
  - the gauge content of each generation: one 27 of E₆, by F-MC and the dictionary;
  - the zero parity: the odd spin structure adds one more holomorphic zero mode. It is a singlet of the weave's group,
    not a fourth member of the triplet, and its role is not read here;
  - the orientation of the records.
- **The weave's rule.**
  - Every thread is in the group.
  - The quantity, the invariant holomorphic subspace, is defined by the joint action.
  - The claim is about every thread and every point of the weave's moduli at once.
