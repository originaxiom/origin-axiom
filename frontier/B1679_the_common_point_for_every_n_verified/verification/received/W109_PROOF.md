# W109 — B1677 for every n ≥ 3: the only character of F_n in SL(2, ℂ) fixed by every transvection is the trivial one (the proof, written before its checks)

**Why.** Main's relay of 2026-10-20, CC_TO_ALL_SEATS_2026-10-20_THE_COMMON_POINT_AND_THE_LIFTED_REGISTER.md (§2), asks
this seat for "a proof of B1677 for every n ≥ 3, or a counterexample at n ≥ 5". B1677's census stops at n = 4, because
a sub-tuple can pass its filter without generating.

**Weave or thread.** A WEAVE result about the forms (§158's level 9).
- It takes every move of the weave of n records, and every character, with none hand-picked.
- Its quantity is defined by the joint action: a character fixed by every move.
- Its claim is about all moves and all n ≥ 3 at once.

**The order.** This proof was worked by hand on 2026-10-20 and is committed before its checks script exists. Nothing
was computed for it beforehand. The commutator relations in step (iii), for the R_ij and for the L_ij, were worked by
hand on the generators.

## Notation

- F_n is free on a₁, …, a_n. For i ≠ j, R_ij is the automorphism a_i ↦ a_i a_j, and L_ij is a_i ↦ a_j a_i; the other
  letters are fixed. Automorphisms compose as maps: (φψ)(w) = φ(ψ(w)).
- For ρ: F_n → SL(2, ℂ), write g_i = ρ(a_i) and χ_ρ(w) = tr ρ(w).
- A move φ **fixes the character** when χ_{ρ∘φ} = χ_ρ, that is, tr ρ(φ(w)) = tr ρ(w) for every word w.
- The **trivial character** is χ(w) = 2 for every w.
  - A representation with that character has abelian image: every commutator has trace 2, so it is reducible, and it
    is conjugate into the unipotent upper-triangular group.
  - In SU(2), or with finite image, it is the trivial representation.

## The theorem

1. **(i) Every n ≥ 3, the character reading.** If the character of ρ: F_n → SL(2, ℂ) is fixed by every R_ij, it is the
   trivial character. The same holds with every L_ij in place of R_ij, or with one of R_ij and L_ij for each ordered
   pair (i, j).
2. **(ii) n = 2.** Write (x, y, z) = (tr a, tr b, tr ab). The characters of F₂ fixed by the record's two moves are
   exactly (2, 2, 2) and the quaternion point (0, 0, 0). The moves are R: a ↦ ab and L: b ↦ ab. Both points are fixed
   by all of Aut(F₂).
3. **(iii) Every n ≥ 3, the class reading.** Let G be a non-trivial finite subgroup of SU(2). No class of
   Epi(F_n, G)/Aut(G) is fixed by every R_ij.

**The corollary, B1677 for every n.**
- Among the characters of F_n in SL(2, ℂ), a non-trivial one fixed by every move exists only at n = 2, where it is
  the quaternion point.
- Neither SU(2) nor a finite image is assumed. At n = 2 the finite image is forced: the character (0, 0, 0) has
  tr[a, b] = x² + y² + z² − xyz − 2 = −2 ≠ 2, so it is irreducible. It is therefore Q₈'s representation, up to
  conjugacy.
- On the class reading, the same holds for every finite subgroup of SU(2), Galois twists included.

## The proof of (i), for the R_ij

Fix the character, and let i, j and k be distinct (n ≥ 3).

1. **One trace.**
   - The word a_i: R_ij(a_i) = a_i a_j, so tr(g_i g_j) = tr g_i.
   - The pair (j, i) gives tr(g_j g_i) = tr g_j. Since tr(g_i g_j) = tr(g_j g_i), every generator and every product of
     two distinct generators have one trace, t.
2. **t is 0 or 2.**
   - The word a_i a_j⁻¹: R_ij(a_i a_j⁻¹) = a_i, so tr(g_i g_j⁻¹) = tr g_i = t.
   - Fricke's identity tr(xy) + tr(xy⁻¹) = tr x · tr y then gives 2t = t², so t = 0 or t = 2.
3. **The triple products.** The word a_i a_k: R_ij(a_i a_k) = a_i a_j a_k. So tr(g_i g_j g_k) = tr(g_i g_k) = t, for
   every ordered triple of distinct indices.
4. **t = 0 is impossible.**
   - Then tr g_i = 0, so g_i² = −I by Cayley–Hamilton.
   - On the traceless matrices sl(2, ℂ), the form B(x, y) = −½ tr(xy) is symmetric and non-degenerate. B(g_i, g_i) = 1
     and B(g_i, g_j) = −½ t = 0, so g₁, g₂, g₃ are B-orthonormal, hence a basis of sl(2, ℂ).
   - Put h = g₁g₂. It is traceless (tr h = t = 0) with determinant 1, so B(h, h) = 1.
   - B(h, g₁) = −½ tr(g₁g₂g₁) = −½ tr(g₁²g₂) = ½ tr g₂ = 0, and B(h, g₂) = −½ tr(g₁g₂²) = ½ tr g₁ = 0.
   - So h lies in the B-orthogonal complement of g₁ and g₂. Since B is non-degenerate on their span, that complement is
     the line ℂg₃. With B(h, h) = 1, h = ±g₃.
   - Then tr(g₁g₂g₃) = ±tr(g₃²) = ∓2, against step 3, which gives tr(g₁g₂g₃) = t = 0.
5. **t = 2 is the trivial character.**
   - Every trace of a product of at most three distinct generators is then 2, the trivial character's value.
   - These traces determine the character. Every trace function on F_n is a polynomial in them (Horowitz 1972;
     Procesi 1976). So the character is trivial. ∎

**The left moves, and a mixed choice.**
- For L_ij the test words are a_i, a_j⁻¹a_i and a_k a_i. Step 3 then gives tr(g_k g_j g_i) = t.
- Step 4 needs one triple product, in any order. Pairwise anticommuting g₁, g₂, g₃ multiply to ±g₁g₂g₃ in every
  order, so the trace is ±2 and never 0.
- Step 5 needs both orientations of each triple. At t = 2 Fricke's triple identity,
  tr(xyz) + tr(xzy) = tr x tr(yz) + tr y tr(xz) + tr z tr(xy) − tr x tr y tr z = 4, gives the other orientation as 2.

## The proof of (ii)

- R sends (x, y, z) to (z, y, yz − x), and L sends it to (x, z, xz − y).
- R fixes the point exactly when z = x and x(y − 2) = 0. L fixes it exactly when z = y and y(x − 2) = 0.
- Together these give x = y = z with x(x − 2) = 0. So the point is (0, 0, 0) or (2, 2, 2), and by Fricke–Vogt the
  triple is the whole character.
- Aut(F₂) is generated by R, the inversion a ↦ a⁻¹, which gives (x, y, xy − z), and the swap, which gives (y, x, z).
  Each of the three fixes both points. ∎

## The proof of (iii)

1. **The automorphisms the moves induce.**
   - Let ρ ∈ Epi(F_n, G) have its class fixed by every R_ij.
   - Then each R_ij has an α_ij ∈ Aut(G) with ρ∘R_ij = α_ij∘ρ. It is unique, because ρ is onto.
   - On the stabiliser of the class, φ ↦ α_φ is a homomorphism: ρ∘φψ = α_φ∘ρ∘ψ = α_φα_ψ∘ρ.
2. **Their image in Out(G) is trivial.**
   - For distinct i, j and k, R_ij⁻¹ = R_ik⁻¹ R_kj⁻¹ R_ik R_kj in Aut(F_n). By hand, on the generators: a_i goes to
     a_i a_j⁻¹ and a_k to a_k, and every other letter is fixed.
   - So the subgroup A of Out(G) generated by the images of the R_ij is generated by commutators of its own elements,
     and A = [A, A].
   - Out(G) is solvable for every finite subgroup of SU(2) (below). So A is trivial.
3. **So the character is fixed, and (i) applies.**
   - Every α_ij is inner: conjugation by an element of G ⊂ SU(2), which keeps traces.
   - So the character of ρ is fixed by every R_ij. By (i) it is trivial; in SU(2) that makes ρ trivial and G = {1}. ∎

**Out(G) is solvable.** The finite subgroups of SU(2) are the cyclic groups, the binary dihedral groups Dic_m (m ≥ 2,
with Q₈ = Dic₂), 2T, 2O and 2I.
- **The cyclic groups.** Their automorphism groups are abelian.
- **Dic_m, m ≥ 3.**
  - Dic_m is generated by x of order 2m and y with y² = x^m and yxy⁻¹ = x⁻¹.
  - The elements outside ⟨x⟩ have order 4 < 2m, so ⟨x⟩ is characteristic.
  - Aut(Dic_m) therefore maps to Aut(ℤ/2m), which is abelian. Its kernel, the automorphisms fixing x, sends y to x^k y
    and is abelian too. So Aut(Dic_m) is metabelian.
- **Q₈, 2T and 2O.** Aut(G) has order 24, 24 and 48, so it is solvable.
- **2I.** Out(2I) has order 2 (W108: |Aut| = 120, |Inn| = 60).

## What is used, and what is new

- **Used.**
  - Fricke's identity and its triple form, Cayley–Hamilton, and the trace form on sl(2, ℂ).
  - Horowitz's and Procesi's theorem, in step 5 only.
  - One relation of Aut(F_n), and the list of finite subgroups of SU(2), in (iii) only.
  - No computation.
- **B1677's own steps.**
  - Its equal-trace filter (its preregistration, §0b item 4) is step 1.
  - Its argument at t = 0 for rank 3 ("pairwise anticommuting (i, j, ±k)") is step 4, in its SU(2) form.
- **New here.**
  - Step 2. The test word a_i a_j⁻¹, with Fricke's identity, removes every t other than 0 and 2. Those are the cases
    the census had to enumerate.
  - Step 4 made uniform in n. Only three generators are used, so n ≥ 5 needs nothing more.
  - Step 5.
  - The class reading (iii), which covers the Galois twists of 2O, 2I and Dic_m.
  - SU(2) and the finite image dropped.
- **Prior art.** The statement is elementary, and probably known. This seat has not searched the literature. Main's ask
  to the referee lane (the T-systems, and the Aut(F_n)-invariant characters) covers it.

## The checks (one script, the_record_count_for_every_n.py, committed before its one run)

The proof does not rest on them. Each check names its expected outcome and a prior.

| check | what | expected | prior |
| --- | --- | --- | --- |
| C1 | Fricke's identity, its triple form, Cayley–Hamilton at trace 0 and the polarisation xy + yx = tr(xy)·I for traceless x, y, in sympy on generic matrices | all identities exact | 99% |
| C2 | R_ij⁻¹ = R_ik⁻¹ R_kj⁻¹ R_ik R_kj on the generators of F₃ and F₄, for every ordered triple of distinct indices; the left analogue L_ij⁻¹ = L_ik⁻¹ L_kj⁻¹ L_ik L_kj | holds for every triple | 90% |
| C3 | n = 2: the solutions of the fixed equations of R and L, and their images under the inversion and the swap | exactly (0, 0, 0) and (2, 2, 2), both fixed | 99% |
| C4 | n = 3, independent of the proof's test words: a trace reducer (Fricke's identities on words), checked against random SL(2, ℂ) matrices; the action of each move on the seven coordinates and the relation of z; a Groebner basis of the fixed equations for the six R_ij, the six L_ij and all twelve | the only point on the character variety is (2, …, 2), in all three move sets | 90% |
| C5 | Aut(G), Inn(G) and the solvability of Out(G), by brute force, for Q₈, 2T, 2O, 2I and Dic_m (3 ≤ m ≤ 12) | Out(G) solvable in every case; \|Aut\| = 24, 24, 48, 120 and 2m·φ(2m); \|Inn\| = 4, 12, 24, 60 and 2m | 85% (the orders recalled, not derived) |

- **If a check fails,** it is recorded as failed. A failure of C1, C3 or C4 would be a failure of the proof, and it
  would be withdrawn as stated. A failure of C2 as written would leave (iii) to be repaired with the relation as found.
  A failure of C5's orders would leave the solvability claim to stand or fall with C5's solvability cell.

## The scope

- The target SL(2) stays priced. The rank enters through the record's reading of the two records by the commutator
  trace κ = tr[a, b], the Fricke–Vogt coordinate. Higher-rank targets are not covered here.
- Whether the principle requires a common point stays a reading, as B1677 states.

0 of 19.
