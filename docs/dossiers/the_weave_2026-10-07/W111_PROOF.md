# W111 — the surface route (P-211): on a genus-g surface with one boundary, the only SL(2, ℂ) character fixed by the mapping classes is the trivial one once g ≥ 2; the odd-p Heisenberg character is fixed at every genus; the 2-group one only at g = 1 (the proof, written before its checks)

**Why.** Main's relay of 2026-10-21, CC_TO_ALL_SEATS_2026-10-21_TWO_RECORDS_CHARACTERISED_AND_THE_SURFACE_ROUTE.md (§4),
asks this seat for "a proof, with checks committed before their run, of P-211". There are two statements:
- **(a)** For g ≥ 2, is the trivial character the only SL(2, ℂ) character of F_{2g} fixed by the mapping classes of
  a genus-g surface with one boundary?
- **(b)** Is the odd-p Heisenberg character fixed at every genus, while the 2-group one is fixed only at g = 1?

On words, the count of two rests on the democratic extension of the moves (relay §168). This is the other natural
extension, on characters.

**Weave or thread.** A WEAVE result about the forms.
- It takes every move of the surface route (the mapping classes) and every character of the stated kind, with none
  hand-picked.
- Its quantity is defined by the joint action: a character fixed by every move.
- Its claim is about every genus at once.

**The order, and what was seen first.**
- This proof was worked by hand on 2026-10-21 and is committed before its checks script exists.
- **Seen first, disclosed.** To find an explicit mapping class that mixes two handles, this seat ran exploratory
  searches in scratch: products of up to three elementary Nielsen moves, and moves of a chain basis, both without a
  mixing hit; and moves changing two generators by a short word. The last found μ below.
  - μ's property is checked by hand below. The search script is committed beside this proof as
    the_surface_route_exploration.py, with its output, labelled exploratory.
  - Nothing else was computed.

## Notation

- F_{2g} is free on a₁, b₁, …, a_g, b_g. Write c_k = [a_k, b_k] = a_k b_k a_k⁻¹ b_k⁻¹ and ∂ = c₁ c₂ ⋯ c_g, the
  boundary word.
- **The moves of the surface route** are the automorphisms of F_{2g} that keep the class of ∂. By the
  Dehn–Nielsen–Baer theorem in Zieschang's form for one boundary component, they are the mapping classes of the
  genus-g surface with one boundary, up to inner automorphisms, which fix every character.
- V = H₁ mod a prime: the images ā_k, b̄_k, with the intersection form ω(ā_k, b̄_k) = 1 and the other basis pairs 0.
- **Explicit moves.** Each keeps ∂ exactly or up to conjugation; the computation is shown.
  - **The handle twists** τ_k: b_k ↦ b_k a_k and τ′_k: a_k ↦ a_k b_k. They give [a_k, b_k a_k] = c_k and
    [a_k b_k, b_k] = c_k.
  - **The adjacent handle swap** σ_k, for k < g:
    a_k ↦ c_k a_{k+1} c_k⁻¹, b_k ↦ c_k b_{k+1} c_k⁻¹, a_{k+1} ↦ a_k, b_{k+1} ↦ b_k.
    Then c_k ↦ c_k c_{k+1} c_k⁻¹ and c_{k+1} ↦ c_k, so c_k c_{k+1} is kept. Its inverse sends a_k ↦ a_{k+1} and
    b_k ↦ b_{k+1}, and a_{k+1} ↦ c′⁻¹ a_k c′ and b_{k+1} ↦ c′⁻¹ b_k c′, with c′ = c_{k+1}.
  - **The mixing move** μ on handles 1 and 2 (g ≥ 2): a₁ ↦ γ a₁, b₂ ↦ γ b₂, with γ = b₁⁻¹ a₂.
    - It is an automorphism, since γ involves neither a₁ nor b₂.
    - μ(c₁c₂) = γ a₁ b₁ a₁⁻¹ γ⁻¹ b₁⁻¹ a₂ γ b₂ a₂⁻¹ b₂⁻¹ γ⁻¹. Since γ⁻¹ b₁⁻¹ a₂ = 1, this is γ c₁ c₂ γ⁻¹.
    - So μ′ = (conjugation by γ⁻¹) ∘ μ on the free factor of handles 1 and 2, extended by the identity on the other
      handles, keeps ∂ exactly.
    - Mod 2 it acts on V as the transvection T_u, v ↦ v + ω(v, u)u, along u = b̄₁ + ā₂.

## The theorem

1. **(a) SL(2, ℂ), g ≥ 2.** If the character of ρ: F_{2g} → SL(2, ℂ) is fixed by the τ_k, the τ′_k and the σ_k, it
   is the trivial character. So the only SL(2, ℂ) character fixed by the mapping classes is the trivial one. At
   g = 1 the fixed characters are the trivial one and the quaternion point (W109 (ii)).
2. **(b) Odd p, every g.** Let H be the Heisenberg group of (ℤ/p)^{2g}, with exponent p and central z of order p.
   Let x_k, y_k be a symplectic basis, [x_k, y_k] = z, with the other pairs commuting. Let ρ_p send a_k ↦ x_k and
   b_k ↦ y_k into H's p^g-dimensional irreducible representation with z ↦ e^{2πi/p}. Then for every move φ of the
   surface route, ρ_p ∘ φ is conjugate to ρ_p. So its character is fixed at every genus.
3. **(c) p = 2.** Let E be an extraspecial group 2^{1+2g} in its 2^g-dimensional irreducible representation, and
   ρ: F_{2g} → E with ρ(a_k), ρ(b_k) anticommuting and commuting across handles. Its character is fixed by the moves
   of the surface route exactly when g = 1 and ρ(a)² = ρ(b)² = ρ(ab)² = −I. That is Q₈, the quaternion point. For
   g ≥ 2 none is fixed.

**So on the surface route the count is one handle, two records, on the rank-two side.**
- In SL(2, ℂ) a non-trivial fixed character exists only at g = 1, by (a).
- In finite targets of higher rank the odd primes keep a fixed point at every genus, by (b).
- So it is the prime, and the rank-two target that forces it to be 2, that gives two records here, not the extension
  of the moves. This is main's §3 argument, proved.

## The proof of (a)

Write A_k = ρ(a_k) and B_k = ρ(b_k). On sl(2, ℂ) take B(x, y) = −½ tr(xy), as in W109.

1. **Each handle is trivial or quaternion.**
   - τ_k and τ′_k fix the other letters. On ⟨a_k, b_k⟩ they act on (x, y, z) = (tr a_k, tr b_k, tr a_k b_k) as the
     record's L and R: (x, z, xz − y) and (z, y, yz − x).
   - So, by W109 (ii), each handle's triple is (2, 2, 2) or (0, 0, 0).
2. **A quaternion handle forces every other generator to ±I.**
   - Suppose handle k is (0, 0, 0). Then A_k² = B_k² = −I, A_k B_k = −B_k A_k, and C_k = A_k B_k is traceless with
     determinant 1. So A_k, B_k, C_k is a B-orthonormal basis of sl(2, ℂ).
   - Let Y = ρ(y) for a generator y of another handle, and Y₀ its traceless part. Then tr(XY) = tr(XY₀) for traceless
     X.
   - The test word b_k y under τ_k^{±1} gives tr(B_k A_k^{±1} Y) = tr(B_k Y). Since B_k A_k = −C_k and B_k A_k⁻¹ = C_k,
     this yields tr(C_k Y₀) = tr(B_k Y₀) = 0.
   - The test word a_k y under τ′_k^{±1} gives tr(A_k B_k^{±1} Y) = tr(A_k Y). So tr(A_k Y₀) = 0.
   - So Y₀ = 0, and Y = ±I.
   - Then every other handle's triple is (±2, ±2, ±2). By step 1 it is (2, 2, 2), so those generators are I.
3. **The swaps make the handles alike.** Under σ_k, handle k's triple becomes handle k + 1's, since every image in
   handle k is a conjugate of the corresponding letter of handle k + 1. So a fixed character has one triple on every
   handle. With step 2, at g ≥ 2 no handle is quaternion.
4. **All handles (2, 2, 2) is the trivial character.**
   - **The nilpotent parts.** With trace 2, (A_k − I)² = 0. So A_k = I + N_k and B_k = I + M_k with N_k, M_k
     nilpotent. These are isotropic for B.
   - **One handle at a time.** tr(A_k B_k) = 2 gives tr(N_k M_k) = 0, so N_k and M_k are orthogonal. Two orthogonal
     isotropic vectors in a non-degenerate three-dimensional quadratic space are proportional, since a totally
     isotropic subspace there has dimension at most 1. So handle k lies in a group {I + tN}.
   - **Across handles.**
     - Take a handle whose image is not trivial, with N ≠ 0 among its nilpotent parts; if every handle is trivial,
       there is nothing to prove.
     - The twist τ_k^m (or τ′_k^m) and the test word b_k y (or a_k y) give tr((I + sN)(I + X)) = 2 + s·tr(NX), for
       every s in a set ℤ + c. Here X is the nilpotent part of another generator.
     - So tr(NX) = 0, and X is proportional to N.
   - So the whole image lies in one group {I + tN}, every trace is 2, and the character is trivial. ∎

## The proof of (b)

1. **The character formula.**
   - The character of H's representation vanishes off the centre. For h not central, some k has khk⁻¹ = z^c h with
     c ≠ 0, so tr h = ζ^c tr h, where ζ = e^{2πi/p}, and tr h = 0.
   - So χ(w) = p^g ζ^{c(w)} when the class w̄ of w in V is 0 (with π(w) = z^{c(w)}), and χ(w) = 0 otherwise.
2. **The class c(w).**
   - For odd p, H is a quotient of N = F/γ₃(F)F^p, the free group of class 2 and exponent p. Its commutator subgroup
     is Λ²V, through [u, v] ↦ ū ∧ v̄.
   - The quotient map sends Λ²V to Z(H) ≅ 𝔽_p by the linear form ω̃(u ∧ v) = ω(u, v), because x_k, y_k is a
     symplectic basis.
   - For w̄ = 0, the image of w in N lies in Λ²V, and c(w) = ω̃ of it.
3. **The moves are symplectic.**
   - A move φ keeps ∂'s class. Its image in Λ²V, which is central in N, is Ω = Σ ā_k ∧ b̄_k. So Λ²φ_V(Ω) = Ω.
   - A non-degenerate bivector's stabiliser is the symplectic group of the dual form, so φ_V ∈ Sp(V, ω). Hence
     ω̃ ∘ Λ²φ_V = ω̃.
4. **So the character is fixed.**
   - (φ(w))‾ = φ_V(w̄), which is 0 exactly when w̄ = 0.
   - For such w, c(φ(w)) = ω̃(Λ²φ_V(·)) = c(w). So χ ∘ φ = χ.
   - Stone–von Neumann gives the stronger statement: φ induces an automorphism of H trivial on the centre, and the
     representation with a given central character is unique. So ρ_p ∘ φ is conjugate to ρ_p. ∎

## The proof of (c)

1. **The squares give a quadratic form.**
   - E's squares are central and depend only on the class in V. So e² = (−1)^{q(ē)}, with q a quadratic form whose
     polar form is the commutator pairing ω: q(u + v) = q(u) + q(v) + ω(u, v).
   - Then tr ρ(w²) = 2^g (−1)^{q(w̄)}. So a fixed character needs q ∘ φ_V = q for every move φ.
2. **The transvection lemma.** For the transvection T_u, q(T_u v) = q(v) + ω(v, u)(q(u) + 1). So T_u keeps q exactly
   when q(u) = 1.
3. **What the moves force.**
   - τ_k acts on V as T_{ā_k} and τ′_k as T_{b̄_k}. So a fixed character has q(ā_k) = q(b̄_k) = 1.
   - **For g ≥ 2,** μ′ acts as T_u with u = b̄₁ + ā₂. But q(u) = 1 + 1 + ω(b̄₁, ā₂) = 0, so μ′ moves q. Hence no
     2-group character is fixed.
   - **For g = 1,** the twists force q(ā) = q(b̄) = 1. Then q(ā + b̄) = 1 + 1 + 1 = 1, and q is 1 on every non-zero
     vector. This is the form of Arf invariant 1: ρ(a), ρ(b) and ρ(ab) all square to −I, which is Q₈, the quaternion
     point.
   - Conversely, that point is fixed by every move at g = 1 (W109 (ii)). ∎

## What is used, and what is new

- **Used.**
  - Fricke's identities and W109's step (ii), for (a).
  - The free class-2 exponent-p group, the character of H, and Stone–von Neumann, for (b).
  - The squaring form of an extraspecial 2-group, for (c).
  - Zieschang's form of Dehn–Nielsen–Baer, only to call the moves mapping classes.
  - The explicit moves: their properties are computed above, and checked below.
- **New here.**
  - (a), with its handle-by-handle proof. The web seat's exploratory search at g = 2 is consistent with it.
  - (b) and (c) with explicit moves: main's §3 argument, proved.
  - The transvection lemma replaces the orbit count of the Arf forms.
  - The statements are elementary, and probably known in some form. This seat has not searched the literature.
    Main's prior-art ask to the referee lane covers them.

## The checks (one script, the_surface_route.py, committed before its one run)

The proof does not rest on them.

| check | what | expected | prior |
| --- | --- | --- | --- |
| C1 | the explicit moves on words, for g = 2, 3: τ_k, τ′_k, σ_k keep ∂ exactly; σ_k composed with its stated inverse is the identity; μ′ keeps ∂ exactly; μ′ mod 2 is T_u | all hold | 95% |
| C2 | step 2 of (a), exact: with A = diag(i, −i) and B = [[0, 1], [−1, 0]] and Y generic in SL(2, ℂ), the four test-word equations | Y = ±I only | 97% |
| C3 | step 4 of (a), exact: N = [[0, 1], [0, 0]] and X nilpotent with tr(NX) = 0 | X ∝ N | 99% |
| C4 | (a) by numerical search at g = 2, every zero of the move-defect from 120 random starts in SL(2, ℂ)⁴, the moves τ_k^{±1}, τ′_k^{±1}, σ₁^{±1}, μ′^{±1}, on the traces of every word of length ≤ 3 in distinct letters | every zero found trivial; at g = 1 the zeros are the trivial and the quaternion points | 85% |
| C5 | (b): H(3) at g = 1, 2 and H(5) at g = 1. For each explicit move, an invertible intertwiner between ρ_p and ρ_p ∘ φ (the linear system solved numerically, its singular values reported); and the character formula on random words | an intertwiner for every move; the formula holds | 95% |
| C6 | (c) at g = 2: the sixteen forms q with polar ω, each realised as a 2^{1+4} representation by Pauli matrices. Which forms the τ's, σ and μ′ keep, by the character on every word of length ≤ 4. The transvection lemma, exhaustively at g = 1, 2, 3. No form is 1 on V∖0 at g = 2, 3; exactly one at g = 1 | as stated | 95% |

- **If a check fails,** it is recorded as failed. A failure of C1, C2, C3 or C6 would put the proof in question, and
  the statement would be withdrawn as written. A failure of C4 would show a fixed character the proof missed. A
  failure of C5 would put (b) in question.

## The scope

- The surface route is one extension of the moves; the democratic one is W109 and W110.
- The target SL(2, ℂ) is the record's rank-two price. The finite targets in (b) and (c) are the Heisenberg family
  only.

0 of 19.
