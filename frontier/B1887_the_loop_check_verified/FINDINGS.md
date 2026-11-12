# B1887 — The web seat's check of the agy lane's loop, verified on main

*Main, 2026-11-11 (S306p). The agy lane committed a loop in four phases on a branch of its own (register row P-781).
The web seat read the first three phases through the mask and checked, with its own code, the part that is exact.
Its relay asks main to verify those cells with main's own code, or to decline with the reason. This arc verifies
them. Data-free: integers, 40-digit arithmetic for positions, SnapPy for the manifolds. Nothing of the agy lane is
read or run here, and none of the web seat's code is run. No spectrum, overlap, mixing or CP quantity is computed.
Nothing of the lane's is adopted. 0 of 19.*

## 1. The answer first

- **Every cell the web seat asked for reproduces on main's own code, by another route:** 35 checks, none failing.
  [CORRECTED 2026-11-12 (Review 79): "by another route" holds for the cells in integers, which separate code computes.
  For the cells about manifolds (the symmetry groups, amphicheirality, the Chern–Simons invariants, the isometries)
  main's numbers come from SnapPy's own routines, the library the seat's referee used: the same library run again
  by other hands, and not another route. And one of the 35, "M4 by hand", was an expression of typed integers that
  could not fail; it is computed from the matrices now.]
- **Root lattices.** Of the 95 irreducible root systems of rank 1 to 24, exactly one has an even root lattice of
  determinant 1: E₈. The lane's "one of 95" is that classical fact.
- **Metallic words.** W(m) − I has invariants (m, m). So only m = 1 gives a knot complement, which the record already
  holds (B251, B591).
- **The run of 6 under a twist.** The seat's table holds to six figures. No twisted sector has its lightest class
  at the apex of the run's own tube, for 1 to 8 golden periods.
- **The lane's summary of the run of 6 is that of one golden period.** With 2, 4, 6 or 8 golden periods both
  sectors hold a mirror pair and neither holds a single class.
- **Two words in the lane's specification are other histories** than the ones it names. Neither keeps the mark.
- **The symmetry facts hold:** the run of 6 is its own reverse and has a hand; its bundle has two isometries that
  reverse the base; the bundle of L⁵RL²R² has none.
- **What this arc does not do.** It verifies none of the lane's spectra, overlaps or counts. It says nothing about
  the lane's fourth phase.

## 2. How main's route differs from the seat's

Agreement between two runs of one method shows little. So main changed the method where it could.

| part | the seat's route | main's route |
|---|---|---|
| root lattices | Gram matrices from Dynkin diagrams | simple roots in coordinates, then inner products |
| classes of least ∣Q∣ | a box, then the box doubled | a complete enumeration within one period of the axis |
| conventions | rows, mark (1, 3) | the same, then columns, then the mirror word |
| which isometries reverse the base | the seat's referee, with SnapPy | the action on the cusp and on first homology, from the group's presentation |

**Why the enumeration is complete.** Write a vector as α e₊ + β e₋ in the history's two eigen-directions. The
history multiplies α by λ and divides β by λ, so each class has exactly one member, up to sign, with ∣β/α∣ in a
fixed window of width λ². There ∣Q∣ ≤ B bounds both α and β. The members form a bounded parallelogram, and main
walks all of it. A box can be too small. This cannot.

## 3. Root lattices

| family | ranks | determinant of the Gram matrix, shortest roots of norm 2 |
|---|---|---|
| A | 1 to 24 | n + 1 |
| B | 2 to 24 | 2ⁿ |
| C | 3 to 24 | 4 |
| D | 4 to 24 | 4 |
| E | 6, 7, 8 | 3, 2, **1** |
| F | 4 | 4 |
| G | 2 | 3 |

- All 95 Gram matrices are integral and even. Each determinant is the closed form above.
- G₂ and F₄ have Cartan determinant 1 and Gram determinant 3 and 4. The Cartan matrix is not the Gram matrix.
- **The domain does the selecting.** Two even lattices of determinant 1 are left out by it: E₈ + E₈, because it is
  reducible, and D₁₆⁺, because its roots generate only D₁₆. [CORRECTED 2026-11-12 (Review 79): two in rank 16. The
  domain runs to rank 24, and there the twenty-four even lattices of determinant 1 of Niemeier's classification are
  left out as well: none is the root lattice of an irreducible system. D₂₄⁺ is one of them, for the reason given for
  D₁₆⁺: the least norm in its second coset is 6. The twenty-four is the classification's count, cited and not
  recomputed. That E₈ is the only one of the 95 is not touched.] Main checked D₁₆⁺ directly: even, determinant 1, and
  every vector of its second coset has norm at least 4.

## 4. The metallic words

W(m) = LᵐRᵐ has rows (1, m), (m, m² + 1). For m = 1 to 12:

- W − I has invariants (m, m). It is invertible over the integers only at m = 1.
- W + I has invariants (1, m² + 4) for odd m and (2, (m² + 4)/2) for even m. At m = 1 that is (1, 5).

## 5. The run of 6 under the twist

**The instrument** is the record's flat-fibre bundle (B1857). A fibre mode with label κ/5 has, along the history's
axis, squared length ∣Q(κ)∣ cosh(u − u_κ) up to one constant, where Q is the history's own invariant form and u is
arclength. So a sector's lightest state sits on its classes of least ∣Q∣. The lane's finite-area spectra are not
recomputed here.

**The history** is L⁶R(LR)ᵏ: the run of 6 closed by k golden periods. Vectors are rows, the mark is (1, 3), and the
sector of charge q is the vectors congruent to ±q times the mark modulo 5.

| k | the history sends the mark to | least ∣Q∣: untwisted, mark's sector, twice the mark's | the mark's sector | the sector of twice the mark | that pair, in arclength | the run's own class is shortest out to |
|---|---|---|---|---|---|---|
| 1 | +1 | 3, 60, 35 | one class, at ½ | a pair at 0.300865 | 1.8587 | 2.0910 |
| 2 | −1 | 8, 145, 95 | a pair at 0.391512 | a pair at 0.225903 | 1.8344 | 2.0992 |
| 3 | +1 | 21, 350, 250 | one class, at ½ | a pair at 0.182225 | 1.8309 | 2.1005 |
| 4 | −1 | 55, 905, 655 | a pair at 0.420657 | a pair at 0.152882 | 1.8304 | 2.1006 |
| 5 | +1 | 144, 2340, 1715 | one class, at ½ | a pair at 0.131702 | 1.8304 | 2.1007 |
| 6 | −1 | 377, 6115, 4490 | a pair at 0.439290 | a pair at 0.115679 | 1.8304 | 2.1007 |
| 7 | +1 | 987, 15980, 11755 | one class, at ½ | a pair at 0.103133 | 1.8304 | 2.1007 |
| 8 | −1 | 2584, 41825, 30775 | a pair at 0.451091 | a pair at 0.093042 | 1.8303 | 2.1007 |

Places are in periods, measured from the apex, either side.

- **The seat's three rows, k = 1, 2, 3, hold to six figures.** Rows 4 to 8 are post hoc for the seat and for main.
- **Untwisted, the run of 6 has one class of least ∣Q∣ at every k.** The least values are every second Fibonacci
  number.
- **The seat's fifth expectation fails on two counts,** and main finds the same two. It expected a pair in the
  mark's sector and a single class in the other. At k = 1 and 3 it is the other way round. At k = 2 neither sector
  has a single class.
- **The lane's two numbers are those of k = 1:** a shift of 0.3009 in one sector and of one half in the other.
- **The pair is the same two integer vectors at every k:** (2, 1) and (8, −1), beside the apex vector (1, 0).
- **The pair lies inside the run's tube,** on its two shoulders: 1.83 to 1.86 from the apex, where the run's own
  class is the fibre's shortest out to 2.09 or 2.10.
- **The quoted part of the lane's conclusion holds on this instrument:** the twisted read-out does not put the run
  of 6 at the apex of its own tube.

**The labels depend on the convention.** A row vector kept by M corresponds to the column vector J v, and
J (1, 3) = 3 (1, 3) modulo 5. So charge q by rows is charge 3q by columns, and the two sectors change places. Main
checked this by hand and by running the columns. For the mirror word the mark (3, 1) gives the same table, and the
mark (1, 2), which is twice it, gives the exchanged one. A statement about "charge 1" needs its convention beside it.

**The other declared histories,** k = 1, 2, 3:

- (2,1,2,1,2): each twisted sector has one class, at the place of the untwisted apex.
- (2,1,1,1,2), the lane's planted degenerate control: two classes untwisted, as planted, and one in each twisted
  sector.

## 6. Two declared words that are other histories

| the specification writes | its cyclic runs | keeps the mark, by rows and by columns | the word with the intended runs |
|---|---|---|---|
| (2,2,2) as L²R²L²(LR)ᵏ | 2, 2, 3, 1, then ones | no, for k = 1, 2, 3 | L²R²L²R(LR)ᵏ: runs 2, 2, 2, then ones; keeps the mark |
| (2,1⁸,2) as L²(RL)⁴RL²R(LR)ᵏ | 2, nine ones, 2, then ones | no, for k = 1, 2, 3 | L²(RL)⁴R²(LR)ᵏ: runs 2, eight ones, 2, then ones; keeps the mark |

- For k = 1 the first declared word has invariants (1, 27) and (1, 31). It keeps no line of order 5 at all.
- In the golden sea the apex of (2, 1⁸, 2) is 1.617974, which is the record's value (B1857 § 2). The declared
  string has nine ones and reads 1.618057.
- **Main cannot tell which words the lane's code runs.** It has not read the code.

## 7. The bundles

| word | its own reverse | its own mirror | symmetry group | amphicheiral | Chern–Simons, modulo ½ |
|---|---|---|---|---|---|
| the run of 6, k = 1 | yes | no | ℤ/2 + ℤ/2 | no | −0.07360 |
| the run of 6, k = 2 | yes | no | ℤ/2 + ℤ/2 | no | −0.07519 |
| the run of 6, k = 3 | yes | no | ℤ/2 + ℤ/2 | no | −0.07552 |
| L⁵RL²R² | no | no | ℤ/2 | no | −0.06655 |
| L⁵RL²R² and one golden period | no | no | ℤ/2 | no | −0.06500 |
| (2,1,2,1,2), k = 1 | yes | no | ℤ/2 + ℤ/2 | no | −0.06344 |
| (2,1,1,1,2), k = 1 | yes | no | ℤ/2 + ℤ/2 + ℤ/2 | no | −0.04324 |
| the golden ground, twice | yes | yes | order 16 | yes | 0 |

- **For each of the eight, the mirror word** has the same volume, is isometric as an unoriented manifold, and has
  the opposite Chern–Simons invariant modulo ½.
- **The three values for the run of 6 are the record's** (B1876, H15).
- **A control that can fail:** an amphicheiral bundle must have Chern–Simons invariant 0 or ¼ modulo ½. Only the
  golden ground does, and only it is amphicheiral.

**Which isometries reverse the base.**

| bundle | isometries | keep the orientation | reverse the base |
|---|---|---|---|
| the run of 6, k = 1, 2, 3 | 4 | 4 | 2, both keeping the orientation |
| L⁵RL²R² | 2 | 2 | none |
| LLRLRR and LLLRLRRR | 4 | 2 | 2, both reversing the orientation |
| the golden ground | 8 | 4 | 4, of which 2 keep the orientation |

- **In integers:** g with rows (1, 0), (6, −1) has determinant −1 and square 1, sends the mark to minus itself, and
  turns the run of 6 into its inverse, for k = 1 to 8.
- **Main adds one fact.** LLRLRR and LLLRLRRR are not their own reverse, and their bundles still have an isometry
  that reverses the base, as the seat's referee says. That isometry reverses the orientation. So it can serve an
  argument about a scalar operator, and not one where the orientation matters.

## 8. What this means for P-781, and what is not verified

- **Verified on main, of the lane's first phase:** the root-lattice fact; the metallic invariants; and that, on the
  record's flat-fibre instrument, a twist does not put the run of 6 at the apex of its own tube.
- **To tell the lane, in main's words:** two of its declared words are other histories; its summary of the run of 6
  holds for one golden period and changes with the number; and its sector labels need the convention stated.
- **The seat's reading of the lane's two closures stands as a reading.** "One of 95" is the classical fact above
  with a domain that leaves out two lattices. "Closes m = 1 and N = 5" is on record already: m = 1 by B251 and
  B591, and the level by the rule of own lines applied to L·R, which gives the tick itself no line (B1884).
- **Not verified, by the seat or by main:** the lane's finite-area spectra, its one-loop potential and its
  chirality sector; all of the second phase's spectra; the third phase's overlaps and its gates; the fourth phase.
- **The seat's symmetry argument for the third gate is not judged here.** Main checked the manifold facts it rests
  on. Whether the lane's quantity obeys its hypotheses is not checked, and no value of it is computed.
- **Nothing is adopted.** The lane is read only through the mask, and for this arc it was not read at all.

## Seen first

Swept from main at 64bf79ebc, after the run.

- `VERDICT topic-sweep /root lattice|even unimodular|unimodular lattice|E8 lattice|E₈ lattice/ (full text): 6 of 1633 arcs on main match (NEGATIVE 3, PROVED 3); 0 register rows match (none)`
- `VERDICT topic-sweep /twisted sector|under the twist|least \|Q\||mirror pair|anti-apex/ (full text): 35 of 1633 arcs on main match (NEGATIVE 6, PROVED 29); 8 register rows match (DONE 2, QUEUED 6)`
- `VERDICT topic-sweep /amphicheiral|Chern.Simons|palindrom|reverses the base|base-reversing/ (full text): 154 of 1633 arcs on main match (NEGATIVE 36, OPEN 14, PROVED 104); 13 register rows match (DONE 5, QUEUED 8)`

On record and used: B251 and B591 (m = 1 among the metallic words); B1733 (the rule of a thread's own lines);
B1857 (the flat-fibre instrument, and the apex of (2, 1⁸, 2)); B1875 and B1876 (the run of 6 has a hand; its
Chern–Simons values); B1884 (what level a ground names).

Literature: that E₈ is the only irreducible root system with an even unimodular root lattice is classical
(Conway and Sloane, *Sphere Packings, Lattices and Groups*, ch. 4). Main computed every determinant and took none
from a table.

## Disclosed

- **Not blind.** Main read the seat's relay and its two scripts before writing its own, so it knew the seat's
  numbers. What could fail was main's code disagreeing with them. It did not.
- **Main's first run stopped at an assertion of main's own.** With the natural normalisation the vector (1, 0) sits
  exactly on the edge of the period, where a class would be counted twice or not at all. The origin of the period
  is now set off by a fixed amount, and the assertion stays.
- **One check of main's was badly made and is mended.** It asked that no twisted class lie within 0.1 of a period
  of the apex. At k = 8 the pair is 0.093 of a period away, because the period has grown. Its distance in arclength
  has not moved: 1.83. The check now uses arclength.
- **Rows 4 to 8 of the table are post hoc.** So are the pair's vectors and the tube's extent, which are the seat's
  referee's, reproduced here.
- **SnapPy's symmetry groups and isometries are floating-point computations.** The integer facts beside them are
  exact.

## Reproduce

```
python3 -B frontier/B1887_the_loop_check_verified/verification/loop_check_on_main.py
```

About ten seconds. It writes `loop_check_on_main.json` and `loop_check_on_main_run.txt` beside itself and ends with
`CHECKS: 35, FAILING: 0`.
