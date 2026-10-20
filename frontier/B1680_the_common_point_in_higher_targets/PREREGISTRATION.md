# B1680 — THE COMMON POINT IN TARGETS OF HIGHER RANK: does a non-trivial common point of the weave of n records, in U(3) or U(5) with finite irreducible image, exist only at n = 2? (PREREGISTRATION)

**Status: sealed before the run.** cc (main), 2026-10-20. POINT_REGISTER P-209 (step 2 of main's plan, at the owner's
word "start with step 1 all the way to the end"). 0 of 19.

**Why.** B1679 (the SM seat's W109, verified) settled SL(2, ℂ): a non-trivial character of F_n fixed by every move
exists only at n = 2, the quaternion point. So the rank-two target is the one input left in "two records follow from a
common point". If the same holds in targets of higher rank, then two records follow from a common point in any of
them, and the target becomes the one remaining choice.

## 0. Seen first

`VERDICT topic-sweep /common point|Heisenberg|clock and shift|Stone.von Neumann|PSL\(2, ?7\)|Klein|Delta\(54\)|higher.rank target|Sp\(2\)/: 29 of 1451 arcs on main match (NEGATIVE 4, PROVED 25)`
— chiefly B1677 and B1679. **Literature:**
- the Stone–von Neumann theorem for finite Heisenberg groups (the Weyl, or clock-and-shift, representation);
- the finite subgroups of SU(3) (Blichfeldt; Miller, Blichfeldt and Dickson 1916);
- Klein's 3-dimensional representation of PSL(2, 7);
- Dunwoody 1970 and Gilman 1977;
- the invariant theory of SL(n) on Λ²: the trivial representation occurs in Λ²(kⁿ) only for n = 2.

## 0b. Disclosed (decided or seen before the seal)

1. **The n = 2 positive controls, by argument.**
   - In U(p), p prime, the Heisenberg representation a ↦ X (shift), b ↦ Z (clock) is fixed by every move of
     determinant +1. A move sends it to an irreducible representation with the same central character, since a move
     maps the commutator [a, b] to a conjugate of itself. Stone–von Neumann then makes the two equivalent.
   - So at n = 2 common points exist in U(p) for every prime p, in SU(2) as the quaternion point.
2. **The Heisenberg family at n ≥ 3, by argument (the "SL(2) = Sp(2)" reason).**
   - A Heisenberg-type image of F_n carries an alternating commutator form on (ℤ/p)ⁿ. Every move would have to
     preserve it.
   - The transvections generate SL(n, ℤ/p), which preserves no non-zero alternating form once n ≥ 3, since Λ² contains
     the trivial representation only for n = 2. So the image is abelian, and a fixed character is then trivial.
   - **The census's Heisenberg cells at n ≥ 3 are therefore verification.**
3. **The filter.** W109's steps 1–3 hold in any rank, since they use only the trace of products: tr g_i = tr g_i g_j =
   tr g_i g_j⁻¹ = tr g_i g_j g_k = t. Fricke's identity (step 2) is specific to SL(2), so t is not restricted here.
4. **The smoke test** (`before_the_seal/smoke_orders_and_controls.py`, run). Every target has its expected order. At
   n = 2 the controls behave as predicted: Q₈ 24 of 24 generating pairs fixed, H(3) 432 of 432, H(5) 12 000 of 12 000.
   H(5) took 161 s at n = 2, so it is not run at n ≥ 3 (item 2 decides it there). **No non-control target and no
   n ≥ 3 case was run before the seal.**
5. **Dunwoody** decides every solvable target with d(G) = 2 at n ≥ 3 (A₄, S₄, Δ(54), H(3)), provided there is more than
   one class. **A₅ and PSL(2, 7) are not solvable,** and the census decides them.
6. **An observation, not a prediction.** At p = 2 the common point gives three parity lines (2² − 1). At p = 3 the
   Heisenberg common point is itself 3-dimensional. Both give three.

## 1. The instrument (`verification/the_common_point_in_higher_targets.py`, sealed)

- **A common point.** A representation ρ of F_n onto a finite irreducible G ⊂ U(m) such that ρ∘φ is equivalent to ρ
  for every move φ (R_ij and L_ij). It is tested **exactly** by solving for an intertwiner h with h ρ(φ(a_k)) =
  ρ(a_k) h for every k, and checking that h is invertible.
- **The targets.**
  - H(3) ⊂ U(3) and H(5) ⊂ U(5);
  - A₄, S₄ and A₅ ⊂ SO(3), as the adjoint images of 2T, 2O and 2I;
  - Δ(54) ⊂ SU(3);
  - Klein's PSL(2, 7) ⊂ SU(3);
  - the SU(2) controls Q₈ and 2T.
- **The range.** n = 2 and 3 for every target, n = 4 for the targets of order at most 60, H(5) at n = 2 only.
- **The search.** Every tuple that passes the filter (item 3) and generates G.

## 2. Cells (sealed)

| cell | prediction | prior |
|---|---|---|
| **C0** (n = 2, controls) | H(3), H(5) and Q₈ have a common point; the run also lists which other targets do | decided (item 1); seen (item 4) |
| **C1** (n = 3) | no target has a common point | 0.85 (Heisenberg decided by item 2; solvable by Dunwoody; A₅ and PSL(2, 7) computed) |
| **C2** (n = 4) | no target of order ≤ 60 has a common point | 0.85 |
| **bite** | if C1 or C2 fails, the run names the target and the count of fixed tuples | — |

## 3. What each outcome would mean (fixed now)

- **C1 and C2 hold.** In every target tested, a non-trivial common point exists only at two records. So "two records"
  follows from the existence of a common point in any of these targets, not only SL(2). The target becomes the one
  remaining choice, and with it the prime: p = 2 gives the quaternion point and its three parities, and p = 3 a
  3-dimensional Heisenberg point.
- **C1 or C2 fails.** A target of higher rank has a common point at more than two records. The count of two then rests
  on the rank-two target, and the target and the multiplicity it carries are named.

## 4. The run

One run of the sealed instrument, at low priority and single-threaded. Its output is committed unread, then read once.
