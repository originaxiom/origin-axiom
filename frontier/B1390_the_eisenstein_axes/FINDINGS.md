# B1390 — THE EISENSTEIN AXES: in m004's commensurability class, an isometry of order 3 or 6 fixes only arcs running from cusp to cusp. So an order-3 symmetry that rotates no cusp acts freely, and sL-7's clean target (an order-3 symmetry whose fixed geodesics are all closed) does not exist in the class. Every three there is a pullback of a one, or rests on rotation residues that cancel mod 3. Order 4 fixes only closed geodesics, and every other order above 2 acts freely. The instrument that checks this on 283 arithmetic members finds the one exception in B1186's family on a non-arithmetic member. 13 of B1186's 112 are non-arithmetic, so B1186's family is not the commensurability class (a correction of record).

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** test 3 of the kill tests on the chirality mechanism.
sL-7's re-posing (7fc93d95) named the clean target, "an order-3 symmetry whose fixed geodesics are all closed", as the next computable
step toward three. Designing its search, the target was found to be excluded by arithmetic. · **Status:** PROVED (the theorem; exact)
· COMPUTED (the fixed sets on 283 arithmetic members and 13 non-arithmetic ones; exact combinatorics on SnapPy's canonical
retriangulations; arithmeticity from traces at 50 digits) · **Fence:** pure mathematics about isometries; its reading is in the seat's
frame (B1351 (ii), B1386's L4), spin-0 half · **Price:** unchanged, 0 of 19 · **Numbering:** B1390 (free on both branches; main has
B1400–B1431).

## 0. Seen from above

sL-7, re-posed after B1389, read the three as a congruence problem:
- B1371: an order-3 isometry rotates an even number of cusps.
- B1386's L4: translated and 3-cycled cusps contribute 0 mod 3.
- So N ≡ Σ_rotated χ (mod 3).

It named two structures that could give |N| = 3:
1. rotated cusps whose residues cancel mod 3;
2. the clean target: an order-3 symmetry with only closed fixed geodesics. It rotates no cusp, so its quotient is an orbifold and the
   three would not be a pullback.

**The second does not exist in m004's class, and the reason is the Eisenstein field itself:**
- **The field.** Every symmetry lies in PGL(2, ℚ(√−3)) (Skolem–Noether). An order-3 element there has t² = det, so its axis ends at
  (a − d ± t√−3)/2c: ℚ(√−3)-rational points.
- **The integrality.** With integral traces, no loxodromic element can fix such a point: its eigenvalue ratio would be a unit of
  ℤ[ω], i.e. a root of unity. So the axis is never a closed geodesic, and it runs from cusp to cusp.
- **The consequence.** An order-3 symmetry either rotates cusps or acts freely. If it acts freely, its quotient is a manifold in the
  class and every invariant class is a pullback: N = 3N(quotient).

What stays open for three, in the class:
- **The pullback three.** Three is 3 × (±1) on the free quotient, which is sL-5's level question. If it is realised, the three zero
  modes carry the three characters of the deck ℤ/3, one each (§1, (iv)).
- **The cancellation three.** Rotated cusps whose residues cancel mod 3. There N ≡ 0 (mod 3), so no symmetry forces N ≠ 0.

The computation found a correction of record. The instrument ran on all 112 of B1186's family and on B1386's 184 covers. The one
closed order-3 fixed curve it found anywhere is on o10_143602, where tr(c²) = −5/2. That trace is not an algebraic integer, so
o10_143602 is non-arithmetic. A trace sweep then found 13 such members among the 112.
- **The correction.** B1186's family (shape field ⊆ ℚ(√−3)) is not m004's commensurability class. B1385 T4 and three surfaces had
  identified the two.
- **What it changes.** One sentence in B1385, one status line of sL-1, one line of THE_VERDICT_OF_THE_OBJECT, and the class reading of
  two rows of main's B1418 (relayed).
- **What it does not change.** No verdict, because the members the verdicts rest on are arithmetic (§3).

## 1. The theorem

Let M be a cusped hyperbolic 3-manifold whose shape field (= invariant trace field kΓ, Neumann–Reid) is K = ℚ(√−3), Γ = π₁M ⊂ PSL(2, ℂ),
and R an orientation-preserving isometry of M of finite order k > 1.

**Lemma A (the symmetries are K-rational).** After conjugation, the normaliser N(Γ) lies in PGL(2, K).
*Proof.*
- M is cusped, so the invariant quaternion algebra A₀Γ = K[Γ⁽²⁾] is M₂(K).
- An element n ∈ N(Γ) normalises Γ⁽²⁾, so conjugation by n is a K-algebra automorphism of A₀Γ ≅ M₂(K) (it fixes the centre K·I).
- By Skolem–Noether it is inner: n X n⁻¹ = h X h⁻¹ with h ∈ GL(2, K). Then h⁻¹n commutes with M₂(K), which spans M₂(ℂ), so it is
  scalar. ∎

In particular Γ ⊂ PGL(2, K), and every parabolic fixed point (cusp point) lies in P¹(K).

**Lemma B (elliptic axes).** Let g = [[a, b], [c, d]] ∈ GL(2, K) be elliptic of order k in PGL(2), with t = a + d and Δ = det g. The
eigenvalue ratio is a primitive k-th root of unity ζ, so t²/Δ = 2 + 2cos(2π/k) ∈ K ∩ ℝ = ℚ. Hence k ∈ {2, 3, 4, 6} (Niven). The fixed
points are (a − d ± √D)/2c with D = t² − 4Δ:

| k | t²/Δ | D | fixed points |
|---|---|---|---|
| 3 | 1 | −3t² = (t√−3)² | **in P¹(K)** |
| 6 | 3 | −t²/3 = (t√−3/3)² | **in P¹(K)** |
| 4 | 2 | −t² | never in P¹(K) (−1 is not a square in ℚ(√−3)) |
| 2 | 0 | −4Δ | either, depending on Δ |

(c = 0 is impossible for k = 4, since the diagonal entries would have ratio ±i ∉ K. For k = 3 and 6 with c = 0, the fixed points
are ∞ and b/(d − a), both in P¹(K).)

**Lemma C (integrality).** If every trace of Γ is an algebraic integer, no loxodromic γ ∈ Γ fixes a point of P¹(K).
*Proof.*
- If γ fixes ξ ∈ P¹(K), then γ is K-triangularisable, with eigenvalue ratio μ ∈ K.
- tr(γ²) = μ + 1/μ in the SL₂ normalisation, and it is integral, so μ is a root of x² − tr(γ²)x + 1 ∈ O_K[x]. Then μ and 1/μ are
  algebraic integers, so μ ∈ O_K* = {±1, ±ω, ±ω²} and |μ| = 1.
- So γ² is not loxodromic, and neither is γ. ∎

**Theorem (the Eisenstein axes).** Let M and R be as above.
1. If k ∉ {2, 3, 4, 6}, then R acts freely.
2. If k = 4, every fixed geodesic of R is closed and never enters a cusp.
3. If k = 3 or 6 and M is arithmetic (integral traces; equivalently, M is commensurable with m004), every fixed geodesic of R is a
   proper arc running from cusp to cusp. R rotates each cusp an arc enters: it fixes the cusp, and its linear part there has order k.

*Proof.* A fixed point of R lifts to a fixed point of an elliptic R̃ ∈ N(Γ) ⊂ PGL(2, K) of order exactly k (Lemma A). Lemma B gives
(1). Each component C of Fix(R) is a properly embedded geodesic, either closed or a line whose ends go out cusps.
- If C is closed, its lift, the axis of R̃, is the axis of a loxodromic element of Γ (the deck group of the lift of C).
- For k = 4, the axis's ends are not in P¹(K) (Lemma B), so they are not cusp points and C is closed; this gives (2).
- For k = 3 or 6, the ends are in P¹(K) (Lemma B), so C cannot be closed (Lemma C) and is a line into cusps.
- At a cusp end, R fixes the cusp and a point of its torus, and acts there by R̃'s rotation about its axis, which has order k. This gives
  (3). ∎

**Corollaries** (arithmetic M; with B1371's pairing and B1386's L4):
1. An order-3 isometry either rotates an even number ≥ 2 of cusps (B1371) or **acts freely**. None has only closed fixed
   geodesics, so **sL-7's clean target does not exist in m004's class.**
2. If R of order 3 acts freely, M → M/R is a regular 3-fold cover of a manifold in the class. Every R-invariant Higgs class is a
   pullback p*v̄ (transfer), its harmonic form is the pullback, and every cusp partition pulls back, so **N(p*v̄) = 3N(v̄)**. A three
   from such an R is three times a one: sL-5's cover-resolution question, not a derivation.
3. If R rotates cusps, then N ≡ Σ_rotated χ (mod 3) (L4). A three needs the rotated cusps' residues to cancel, and then no symmetry
   forces N ≠ 0.
4. In the free case the index splits evenly over the deck group's characters.
   - The Lefschetz number of R on the relative cohomology of (M_T, ∂⁺M_T), at an R-invariant cut, is χ(Fix R) = 0. So each character
     of ℤ/3 carries N/3.
   - At the asymptotic count, the Higgs zeros come in free orbits of three (B1388's Theorem A).
   - So a pullback three carries one zero mode per character: a ℤ/3 family charge, not three identical copies.

**The dichotomy is sharp.** Only (3) uses integral traces, and the family shows what happens without them. o10_143602 has shape field
K and two hexagonal cusps, and tr(c²) = −5/2. c² is loxodromic with eigenvalues −2 and −½ ∈ K, so its axis ends at K-rational
points. Each of its two order-3 isometries fixes a closed geodesic as well as three arcs (§2). Outside the field, the Borromean rings
(ℚ(i), where √−3 ∉ K) and s776 and s784 (ℚ(√−7)) have order-3 isometries that rotate no cusp and fix closed geodesics. That is the
orbifold structure of the clean target, but those classes have no hexagonal cusps (B1385: among arithmetic classes, hexagonal cusps
occur only for ℚ(√−3)).

## 2. Computed

`verification/eisenstein_axes.py`: three parts, each seconds to a minute. Records: `algebra_run.txt`, `family_run.txt`,
`covers_run.txt`.

**(A) The algebra, exact in ℚ(√−3)** (a small exact field class; 2 000 random elements per order, entries with denominators ≤ 3):
- Orders 3 and 6: 1 979 and 1 974 elements. The fixed points computed from the closed forms are checked to be fixed, and all are in
  P¹(K).
- Order 4: 1 989 elements. D = −t² is never a square in K (decided exactly).
- Order 2: 39 of 1 991 have K-rational fixed points and 1 952 do not.
- Also asserted: −1 is not a square in ℚ(√−3), and −3 is.

**(B) The instrument.**
- **Method.** SnapPy's canonical retriangulation is an isometry invariant, so its combinatorial automorphisms (t3mlite) are the
  isometries (|Aut| = |Isom| asserted on every manifold). For each orientation-preserving automorphism g, the fixed set is assembled
  from three kinds of piece:
  - on each tetrahedron g maps to itself, the segment joining the barycentres of the two orbits of its vertex permutation;
  - on each face class whose sides g exchanges, the segment joining the barycentres of g's orbits on the face's vertices;
  - each edge class g maps to itself with its ends kept, which is fixed pointwise.
  Every incidence at an ideal vertex is an end, i.e. a fixed point on that cusp torus.
- **Self-tests.**
  - Every interior node has degree 2, so the fixed set is a 1-manifold.
  - Every component is an arc (two ends) or a closed curve (none).
  - Per orientation-preserving element, the ends on each fixed cusp torus equal |det(A − I)| of SnapPy's cusp map, compared as
    multisets over the group. This agrees on all 112 + 184 + 3 controls.
- **Where the test has content.** A closed order-3 curve is combinatorially impossible on a retriangulation without finite vertices:
  a fixed segment runs from a fixed ideal vertex through one rotated face to the next ideal vertex. The test has content where the
  canonical cells are not tetrahedra. That is 12 of the 99 arithmetic census members (16 order-3/6 elements) and 20 of the 184
  covers.

**(B1) B1186's 112** (shape field ⊆ ℚ(√−3)). Arithmeticity comes first.
- tr(g²) was identified in ℚ(√−3) at 50 digits for every word of length ≤ 3 in the generators and their inverses (tolerance 10⁻²⁵).
- Integrality on these words gives integral traces on all of Γ (the trace ring is generated by the traces of products of at most
  three generators). With kΓ = ℚ(√−3) that is arithmeticity (Maclachlan–Reid, Thm 8.3.2).

| | count | witness of non-arithmeticity |
|---|---|---|
| arithmetic (commensurable with m004) | **99** = 77 regular + 22 non-regular | — |
| **non-arithmetic** (not commensurable with m004) | **13**, all non-regular | v2875 tr(c²), t06828 tr(a²) = 1/6 − √−3/2, t06829, t11365, o9_41000, o9_41003 tr(bc²), o9_41004, o9_41005 tr(b²) = 79/98 − (125/49)(√−3/2), o9_41006, o9_41008, o10_143600 tr(ab²), o10_143601 tr(ac²), **o10_143602 tr(c²) = −5/2** |

The fixed sets, by order (orientation-preserving elements):

| order | arithmetic 99: elements, arcs, closed curves | rotating no cusp → free | non-arithmetic 13 |
|---|---|---|---|
| 2 | 408, 648, 280 | 27 of 166 | 31, 42, 26 |
| **3** | 44, 126, **0** | **4 of 4** (s960) | **2, 6, 2 (both on o10_143602)** |
| 4 | 42, **0**, 18 | 26 of 42 | — |
| 5 | 36, 0, 0 | 36 of 36 | — |
| **6** | 46, 40, **0** | **8 of 8** | — |
| 8 | 4, 0, 0 | 4 of 4 | — |
| 10 | 32, 0, 0 | 32 of 32 | — |

Every assertion of the theorem holds on the 99:
- no closed order-3 or order-6 fixed curve;
- every order-3 or order-6 element rotating no cusp acts freely;
- order 4 fixes no arc;
- orders 5, 8 and 10 act freely.

s960, the census probe's one hexagonal translated case, is arithmetic. Its two order-3 and two order-6 elements rotate no cusp and
act freely.

**(B2) B1386's family** (ocube06_08812 and its 183 covers of degree 2 and 3, all arithmetic as covers of o10_150725, whose traces are
integral):

| part | members | order 3: elements, arcs, closed | rotating no cusp → free (translating a cusp) | order 6: elements, arcs, closed |
|---|---|---|---|---|
| ocube06_08812 | 1 | 8, 18, 0 | 2 → 2 (2) | — |
| degree 2 | 7 | 20, 36, 0 | 14 → 14 (14) | 20, 0, 0 |
| degree 3 | 176 | 436, 270, 0 | 362 → 362 (344) | 114, 18, 0 |

The 360 order-3 elements that rotate no cusp and translate one include every candidate of the exploratory probe. Every one acts
freely, so each quotient is a manifold.

**(B3) Controls.**

| manifold | field | order-3 elements, arcs, closed curves | other |
|---|---|---|---|
| L6a4 (Borromean rings) | ℚ(i) | 8, 0, **8** (each rotates no cusp) | 2 finite vertices; order 4: 6, all free |
| s776, s784 (census ≤ 7, outside the family) | ℚ(√−7) | 4 elements, 0, **4** (none rotates a cusp) | the census's only other order-3 elements (2) rotate cusps |
| m004 | ℚ(√−3) | — | involutions: 3, arcs 4, **closed 1** (order 2 is unconstrained) |
| L5a1 (Whitehead link) | ℚ(i) | — | involutions: closed 2; order 4: 2, free |

The instrument finds closed order-3 fixed curves wherever the theorem allows them. In the arithmetic class there are none.

## 3. The correction of record: B1186's family is not m004's commensurability class

- **The identification.** B1385 T4 identified the two: "the joint region is m004's own commensurability class. That is sL-1's family,
  which the architecture enlarges from B1186's census of 112 to all covers." sL-1's status line in OPEN_LEADS repeats it, and so does
  THE_VERDICT_OF_THE_OBJECT ("The family below — the commensurability class — …").
- **Why it fails.** The invariant trace field is a commensurability invariant, which is necessary for membership. It is sufficient
  only together with integral traces, and 13 of the 112 fail integrality.
- **The error class.** This is E4 (necessary read as sufficient); E71's criterion names the integrality half. B1186 defined the
  family by the shape field (Paper IV's definition) and never claimed it was the class. The identification came later.

**What changes.**
- **The class's census part is 99, not 112.** The 13 non-arithmetic members share the field but no finite cover with m004. They lie
  outside the region the covering relation reaches (B1385 T4 stands as stated for the class).
- **B1369's census rows** (the free-cusp theorem on all 112; the parity sweep) are true of the family as computed. Its title's "a
  member of the figure-eight's commensurability class" is correct for the theorem, which uses no arithmeticity. One member B1369
  names is non-arithmetic: t06828, one of the six one-cusped members with b₁ = 2, and one of the eight whose free classes do not span
  H₁.
- **Main's B1418** (relayed, not edited):
  - Cell 1 treats the 112 as "the class". t11365 (Q1.1's list) and o10_143602 (Q1.2's list of three-attainers) are non-arithmetic, so
    those rows are rows of the family, not of the class.
  - B1418's headline members s958, v2873, t12833, t12835 and o10_150701 are all arithmetic, so its "members of the figure-eight's own
    commensurability class" stands.

**What does not change.**
- B1385's pilot and B1386's search ran on o10_150704, o10_150725 and o10_150729 and their covers, all arithmetic.
- B1386's T1 (cube~3.24 is in the class) stands.
- B1387–B1389 are unaffected.
- No verdict changes.

## 4. What this settles for the three, and what it does not

- **Settled (sL-7).** The clean target does not exist in m004's commensurability class. Test 3's search for it is decided by the
  theorem before it is run, so no sealed test is spent on it.
- **Refined.** A three in the class comes in one of two forms:
  - a pullback, 3 × (±1) through a free order-3 symmetry. Here the level (sL-5) must decide between the cover and the quotient; if it
    is realised, the three zero modes are one per character of the deck ℤ/3;
  - a cancellation, with rotated cusps' residues summing to 0 mod 3. Here N ≡ 0 is allowed, so no symmetry forces the three.
- **Nowhere in the class does an order-3 symmetry force |N| = 3.** A three is ≡ 0 (mod 3), and a mod-3 congruence can protect only
  non-zero residues.
- **Not settled.** Whether any member realises either form. Whether the pullback's quotient or its cover is the physical level
  (sL-5). Which count is physical (sL-8). And the spin-½ half. 0 of 19.
- **Outside the class.** The clean structure exists over ℚ(i) and ℚ(√−7), which lack hexagonal cusps. Among non-arithmetic
  manifolds with shape field ℚ(√−3) it has not been found: the census's only non-arithmetic order-3 elements, on o10_143602, also
  rotate cusps. Such a member would share no cover with m004.

## 5. Fences

- **The theorem** is exact. It uses the arithmetic of ℚ(√−3) and standard facts: Skolem–Noether, Niven, Maclachlan–Reid 8.3.2, and the
  trace-ring lemma. Its statement is likely classical in the Bianchi-group literature (the singular locus of H³/PSL(2, O₃) has its
  order-3 edges running between cusps). What is new here is its use for sL-7 and the record's correction.
- **The computation.**
  - The fixed sets are exact combinatorics on SnapPy's canonical retriangulations, whose correctness rests on SnapPy's canonisation
    in double precision (as in B1369–B1386).
  - The traces are identified at 50 digits.
  - The arithmeticity test is complete on words of length ≤ 3, which suffices by the trace-ring lemma for arithmetic, and a single
    non-integral trace is a certificate for non-arithmetic.
- **No physics is crossed.** The reading in §4 is in the seat's frame, spin-0 half, and waits on sL-8 for which count is physical.

## 6. Prior art (swept before banking)

Both branches were swept: this one at 7fc93d95 and origin/main at 987c0c8f. The sweep used git grep for "order-3 elliptic", "closed
fixed geodesic", "fixed geodesics are all closed", "P¹(K)" and "acts freely", plus `scripts/checks/already_banked.py` on "order-3
elliptic closed geodesic fixed" and "acts freely order-3 rotates no cusp".
- No arc states the field constraint on elliptic axes, or that the clean target is impossible.
- **The nearest banked facts:**
  - B1371 §2 (fixed ends pair; the parity);
  - B1386's L4 (the fixed-point congruence);
  - B1385's L2 (a rotation's invariant classes are H¹ of its quotient orbifold);
  - B1356 (a Euclidean closing's deck fixes one closed geodesic, a different setting).
- **On the family/class identification:**
  - B1186 defines the family by the shape field;
  - B1385 T4 and main's B1418 read it as the class;
  - B1371 item 3 checks membership by the shape field. Its six named members (m004, m003, m202, s959, v3551, s596) are all among the
    99 arithmetic ones.
