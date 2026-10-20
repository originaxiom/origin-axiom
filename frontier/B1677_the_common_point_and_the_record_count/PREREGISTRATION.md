# B1677 — THE COMMON POINT AND THE COUNT OF RECORDS: does a weave of n records have an SU(2) common point only at n = 2? (PREREGISTRATION)

**Status: sealed before the run.** cc (main), 2026-10-20. POINT_REGISTER P-205 (first in the foundations quest) and
P-201. 0 of 19.

**Why.** The owner asked for the best parameter-free structure that could show the principle has real ground, and
whether the count of two records is forced. In rank two the triplet comes from the quaternion point, the one SU(2)
character that every move fixes. If no larger register has such a point, then two records follows from the
existence of a common point, with "SU(2) and a finite image" priced, and so does the triplet. A larger register with
its own common point would show the count is a choice. Either outcome is informative, and the second could happen.

## 0. Seen first

`VERDICT topic-sweep /common point|quaternion point|Nielsen|generating (pair|triple|tuple)|record count|substrate count|two records/: 14 of 1448 arcs on main match (NEGATIVE 1, PROVED 13)`
— expected: B1600, B1601 (the common point is the geometry mod 3), the paper's T2, B749 and B1323 (fork F9, the
substrate count), and B1672 (the four shears generate Aut⁺(F₂)). **Literature:**
- Nielsen equivalence and T-systems of finite groups (B. H. and H. Neumann 1951; Dunwoody 1970, transitivity on
  generating n-tuples of a finite solvable group for n > d(G));
- Gaschütz's lemma;
- the finite subgroups of SU(2);
- Procesi's and Fricke–Vogt's theorem that the traces of words of length at most 3 in distinct generators generate the
  coordinate ring of the SL(2) character variety of F_n.

## 0b. Disclosed (seen or decided before the seal)

1. **Design facts about SL(n, 𝔽₂)** (`before_the_seal/design_facts.py`, run). Elements acting on some line as a 3-cycle
   make up 1/3, 1/3 and 0.311 of SL(n, 2) for n = 2, 3, 4. Higher ranks add 5-, 7- and 15-cycles.
2. **Counts by hand.** Epi(F₂, Q₈) has 24 elements and Aut(Q₈) has 24, so there is one class. Epi(F₃, Q₈) has 336,
   which is 14 classes.
3. **Theory.** Every finite subgroup of SU(2) is 2-generated. For solvable G and n > d(G), the Nielsen moves act
   transitively on generating n-tuples (Dunwoody 1970), so no class can be fixed when there is more than one. **C1 and C2
   are therefore expected for every solvable G** (the binary dihedral groups, 2T, 2O) and are verification there.
   **The binary icosahedral group 2I is not solvable, and theory does not decide it.**
4. **The equal-trace filter, derived before the run.** A character fixed by a_i ↦ a_i a_j has tr a_i a_j = tr a_i, so
   every generator and every pairwise product share one trace t. **At t = 0 there is no rank-3 common point:** the
   generators are pairwise anticommuting (i, j, ±k), so a₁a₂a₃ has trace ±2, and the move a₃ ↦ a₃a₁ makes it 0.
5. **The smoke test on the rank-2 control only** (`before_the_seal/smoke_n2.py`, run). Q₈'s 24 generating pairs give one
   common character, (0, 0, 0). Among Dic₃, 2T, 2O and 2I none is common: 24 and 120 tuples pass the filter for 2T and
   2I, and none is fixed. Each group takes under a second. **No n = 3 or n = 4 case was run before the seal.**
6. **The SM seat's exploratory note** (its relay §158, read 2026-10-20 before this seal): "at rank 3 no class is kept by
   every move". Its method and scope were not read in detail.

## 1. The instrument (`verification/the_common_point.py`, sealed)

- **A common point of the weave of n records** is a character of F_n in SU(2) with finite non-abelian image, fixed by
  every move a_i ↦ a_i a_j and a_i ↦ a_j a_i (i ≠ j). These generate SAut(F_n); the left moves differ from the right
  ones by inner automorphisms, which fix characters.
- **The groups.** Dic_m (m = 2, …, 15; order 4m), 2T (24), 2O (48) and 2I (120), as unit quaternions.
- **The search.** Every n-tuple of elements of G that passes the equal-trace filter (exact, item 4 above) and generates
  G. Every generator runs over every element of the common trace, with no reduction by conjugation, which could leave G.
- **The test.** A tuple's character is the vector of the traces of every word of length 1 to 3 in increasing distinct
  generators (Procesi). It is common when every move leaves that vector unchanged.
- **The output.** Distinct common characters per (n, G), with a generating tuple and the number of tuples with that
  character, written to `the_common_point.json`.

## 2. Cells (sealed)

| cell | prediction | prior |
|---|---|---|
| **C0** (control, n = 2) | the quaternion character (0, 0, 0) is a common point, and the only one among these groups | seen (item 5) |
| **C1** (n = 3) | no common point for any G | 0.9 (solvable G decided by theory; 2I computed) |
| **C2** (n = 4) | no common point for any G | 0.9 (the same) |
| **bite** | if C1 or C2 fails, the instrument names G, the generators and the traces | — |

## 3. What each outcome would mean (fixed now)

- **C0–C2 hold.** Among the finite-image SU(2) characters of these groups, the weave has a common point only at two
  records. GM1 then follows from a weaker, stated input: the weave shares a persistent point, in SU(2), with finite
  image. The triplet follows from that point (the paper's T2). The input "SU(2), finite image" stays priced, and groups
  beyond this list (infinite images, other targets) are outside the claim.
- **C1 or C2 fails.** A larger register has its own common point: the count of two is a choice, and the multiplicity
  that point carries is named.
- **Either way.** The line's three on 𝔽₂ is rank-independent (item 1), and whether matter attaches to lines stays open.

## 4. The run

One run of the sealed instrument, at low priority and single-threaded. Its output is committed unread, then read once.
