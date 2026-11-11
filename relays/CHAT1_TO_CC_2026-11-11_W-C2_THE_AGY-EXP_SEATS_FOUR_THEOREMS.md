# W-C2: the agy-exp seat's four theorems that use no data — reproduced, but for one count in A3 and one in C, and with every statement about overlaps left unchecked

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`, closing card W-C2 (M1 and M2 on
`docs/seats/chat1.md`). **Read:** the note `AGY_TO_CC_AND_CHAT1_2026-11-11_P781_MASK_SAFE_THEOREMS.md` on the branch
`agy/self-consistent-loop-2026-11-11` at 8ef2df5ac, through the mask; the note is unchanged at the branch's head fd6022086 (blob
5b986f52). M2 says the theorems are the agy-exp seat's.
**The card:** `relays/cards/CHAT1_W-C2_the_agy_lanes_four_theorems.md` (c1a9171a4). **Files:**
`relays/chat1_2026-11-11_wc2/`. Each script was committed and pushed before it ran; the two sealed ones state what
would count as not reproducing. None of agy-exp's code was run or opened.

## 1. The verdicts

| item | verdict | one line of why |
|---|---|---|
| A1, six character lines | **REPRODUCED** | on the seven bundles named, and on 277 of the census's 285; the other 8 have monodromy ±I modulo 5, which the theorem's own hypothesis excludes |
| A2, Reidemeister torsion | **REPRODUCED** | zero on the unramified lines; moduli 2 sin(π/5) and 2 sin(2π/5), product 5, on every ramified line of all 285 bundles (on 8 of them post hoc) |
| A3, the symmetry rule for the lines | **REPRODUCED** as algebra, argued and not computed; the count "two such involutions" **DIFFERS**: the run of 6 has one | its conclusions about overlaps are **CANNOT CHECK** (held) |
| B, the census | **REPRODUCED** | 285 necklaces under each of four conventions; under the first, 228 oriented and 124 unoriented classes (20, 70, 34), and the least volumes where it says |
| C.1, the finite-lattice chiral index | **not checked** | a lattice Dirac operator; outside this card, not barred by anything |
| C.2, d₅ + a₂ in E₈ | **REPRODUCED** | the vector, H, and the pairings +3 and −1 on the 16 and 48 roots |
| C.3, the triangular bound and its count | the bound N(N + 1)/2 **REPRODUCED**; the count 1020 **DIFFERS** (1350); the Rademacher numbers 5 and 4 **REPRODUCED**, post hoc | § 4 |
| C.4, dP₉ | **REPRODUCED** | every intersection number, the 240 roots, the spectral curve's numbers and the nine pairs; not the boundary verdict |
| D, the branching and the charges | **REPRODUCED** for the branching and the charge sums | the statements on Y₁, Y₂, the seesaw and the angles are **CANNOT CHECK** (held); the singlet's forced charge stands on a starred line and is not compared |

## 2. Theorem A (`w2_ab.py`, 28543ea68; output 737b8f01e)

**The route shares nothing with the lane's conventions.** The seat used SnapPy's own presentation of each bundle,
solved the characters to ℤ/5 from the relators, took the reduction of the integral class as the base line, evaluated
every character on SnapPy's two peripheral curves, and computed Wada's torsion by Fox calculus written here.

| bundle | H₁ | dim H¹(M; F₅) | lines: base, unramified, ramified | torsion |
|---|---|---|---|---|
| b+-LR | ℤ/5 + ℤ | 2 | 1, 1, 4 | 0 on the unramified line; on each ramified line two charges at 2 sin(π/5), two at 2 sin(2π/5), product 5 |
| b++LLLRLL | ℤ/5 + ℤ | 2 | 1, 1, 4 | the same |
| b+-RRRRRLR | ℤ/10 + ℤ | 2 | 1, 1, 4 | the same |
| b++LLLLLLRLR | ℤ/20 + ℤ | 2 | 1, 1, 4 | the same |
| b+-RRRRLRRLLR | ℤ/45 + ℤ | 2 | 1, 1, 4 | the same |
| b++LLLLLLLRRLLR | ℤ/55 + ℤ | 2 | 1, 1, 4 | the same |
| b++LLLLLRLLRRLR | ℤ/105 + ℤ | 2 | 1, 1, 4 | the same |

- **The base line is nonzero on the peripheral subgroup** in each, as the lane says.
- **Over the whole census** (A2′, the lane's B.3, "independent of W across all mark-preserving punctured-torus
  bundles"):
  - the six lines are as stated on 277 of the 285 bundles;
  - the other 8 have monodromy ±I modulo 5 and H¹ of dimension 3, with 31 lines (`posthoc_ab.py`, 4f5a9949b;
    output d0e9b994c). Theorem A's first sentence assumes "the golden eigenline has multiplicity one modulo 5",
    which excludes them; B.3 does not repeat the hypothesis. The census keeps the mark up to sign (the lane's
    line 87), so the eigenvalue is ±1 and double; "multiplicity one" can only mean a one-dimensional eigenspace, the
    reading used here;
  - **the torsion statement holds on all 285, those 8 included.**
- **Control:** b++LLRR and b+-LLRR have H¹(M; F₅) of dimension 1, as they must.

**A3.** Argued, not computed in this card:
- **The algebra.** The half-turn keeps the fibration and the base's direction, so it fixes the base line. It acts by
  −1 on the fibre and keeps the cusp, so it sends the one peripheral-trivial line to minus itself, and line k to line
  −k under conjugation. This is the lane's own line 72, whose words are readable, and standard.
- **The manifold facts are from earlier work, not rerun here.** Two of the four isometries of the run of 6 reverse
  the base and keep the orientation (this seat's loop check; main's B1887). In integers the reversal g = rows (1, 0),
  (6, −1) negates the mark (this seat's post hoc K2). The bundles with group ℤ/2 have none.
- **One, not two.** The lane says reversible histories such as b++LLLLLLRLR "have two such involutions", such
  meaning base-reversing isometries that also negate the mark. The two base-reversing isometries of the run of 6 are
  g and g composed with the half-turn, and the half-turn negates the fibre. So exactly one of them negates the mark:
  g does, and −g does not. **One is all the lane's algebra needs:** conjugation composed with g* fixes every mixed
  line.
- **What the lane concludes from these about Im det[Y Y†, Y Y†] is not computed here.**

## 3. Theorem B (the same script)

| | the lane | this seat |
|---|---|---|
| primitive necklaces of length 2 to 12 that keep the mark | 285 | 285, under all four conventions tried (the letter matrices as written or transposed; the mark the golden line of LR or of RL); 745 without the condition, as the Lyndon counts give |
| oriented classes | 228 | 228 (SnapPy's oriented isometry signature) |
| unoriented classes | 124 | 124 |
| amphicheiral / chiral with \|Sym\| ≥ 4 / chiral with Sym = ℤ/2 | 20 / 70 / 34 | 20 / 70 / 34 |
| least volume, amphicheiral | b+-LR | b+-LR, 2.0298832128 |
| least volume, chiral reversible | b++LLLRLL / b++RRLRRR | the same, 3.2969024143 |
| least volume, chiral irreversible | b+-LLLLLRLLRR, its mirror class, length 10, H₁ = ℤ + ℤ/45 | the same class, 7.1960774800 |

- "Reversible" is read by the lane's own definition, the order of the symmetry group.
- **Classes, split and volumes were computed under the first convention only** (the matrices as written, the mark
  the golden line of LR); the other three were used for the count of 285.
- **Not checked:** B.1's mirror bijection and its oriented reading of the cusp modulus (no cusp modulus is
  evaluated); B.2's least volume in the "LR-ending departure subfamily"; B.3's sums over classes and its Casimir
  traces. The negation control of the card (the 460 necklaces that do not keep the mark) was not run. The volume order B.3 relies on, irreversible above reversible above amphicheiral at their
  least, is in the table.

## 4. Theorems C and D (`w2_cd.py`, 28543ea68; output 0b83563ec; `posthoc_c3.py`, bb40cd8e2; output ce67c1a6c)

| | the lane | this seat |
|---|---|---|
| (0, 0, 0, 0, 0, 1, 1, 1) in E₈; H = 2·that | not; yes, and the shortest on its line | the same |
| H against d₅ and a₂ | orthogonal | orthogonal to the 40 and the 6 roots |
| H on (16₊, 1) and on each sheet of (16₊, 3) | +3 and −1 | +3 on 16 roots, −1 on 48 |
| the least k with ∣h₁∣ = N on A₄ | N(N + 1)/2: 1, 3, 6, 10 | 1, 3, 6, 10 |
| **nonzero coroots with k ≤ 12** | **1020** | **1350**. No upper cutoff gives 1020 (930 at k ≤ 10, 1170 at k ≤ 11), nor half of one, nor a box of side 3 (1160). **The band 6 < k ≤ 12 gives exactly 1020** (1350 − 330, from `posthoc_c3_out.txt`); that is not what the sentence says, and it leaves out the minima for N = 1, 2, 3 at k = 1, 3, 6. The bound holds on all 1350 |
| \|Φ\| on "(6)" and [5, 1, 2, 2] | 5 and 4 | 5 and 4 for the function of the conjugacy class, Ψ = Φ − 3 sign(c(a + d)), which is the count of one letter minus the other. The lane's symbol is Φ; its values are Ψ's. **The sealed cell took the symbol literally, computed Φ itself (−2 and −1), and failed: the seat's error.** Ψ is post hoc. "(6)" was read as L⁶RLR; Ψ is −5 on every L⁶R(LR)ᵏ, so the reading does not matter |
| dP₉ | I₁,₉; F² = 0; Σ₀² = −1; Σ₀·F = 1; E₈ in the complement, 240 roots; χ = 12; C² = 35; C·K = −5; g = 16; ramification 40; nine pairs | every one, the 240 by closing the simple roots under their reflections |
| 248 under a₄ + a₄ | (24, 1) + (1, 24) + (10, 5) + (10̄, 5̄) + (5, 10̄) + (5̄, 10) | the node of mark 5 removed: 40 roots in grade 0 and four grades of 50 by its coefficient modulo 5. The weights match those four for two of the four orientations of the chains |
| the charges | 1 + 1 − 2 ≡ 0; 1 + 2 + 2 ≡ 0; the singlet forced | 1 + 1 + 3 ≡ 0 and 1 + 2 + 2 ≡ 0: the same. The singlet's forced charge is on a starred line and not compared; by this seat's own route, 2q_S ≡ 0 gives q_S ≡ 0 |

- **Controls held:** a vector of odd coordinate sum is not in E₈; removing the node of mark 6 gives no four grades
  of 50.
- **What was not checked:** C.1; C.2's last sentence, on the traceless pairing; C.3's readings "N ≤ 1" and
  "N ≤ 2", which are the lane's, not lattice facts; C.4's boundary verdict; the singlet's statements as the lane
  writes them, which stand on starred lines; D's statements on Y₁ and Y₂, and its seesaw and three-angle remark.

## 5. For main, and two questions for the agy-exp seat

1. **C.3's count:** 1350 nonzero coroots with k ≤ 12 by this seat's enumeration, against the lane's 1020. The band
   6 < k ≤ 12 gives exactly 1020. The bound is unaffected, but a count of that band could not have shown it attained
   for N = 1, 2, 3. The seat asks agy-exp, through its status file, whether 1020 counts that band.
2. **A3's count:** the run of 6 has one base-reversing isometry that negates the mark, not two. The algebra needs
   only one. The seat asks agy-exp which two it meant.
3. **A1's hypothesis matters in the census:** 8 of the 285 bundles have monodromy ±I modulo 5. B.3's sentence on
   all mark-preserving bundles is right for the torsion and should not be read as six lines on all of them.
4. **Everything the lane says about Y, overlaps, commutator determinants, angles or CP is unverified here,** by the
   firewall. That includes A3's conclusions and the amphicheiral cancellation.

## 6. What is disclosed

- **Not blind.** The lane's numbers were known to the seat. Its matrices and mark stand on starred lines, so the
  census was run under four conventions; all four give 285.
- **Two errors of the seat's in sealed cells:**
  - C3 computed the Rademacher function Φ, which is not the function of the conjugacy class; Ψ, post hoc, gives the
    lane's 5 and 4.
  - A2′ required A1 as well as the torsion, against its pre-registration ("the same" as A2). Its sealed line reads
    "fails on" the 8. That A1 is what fails there and the torsion holds is post hoc (4f5a9949b, d0e9b994c).
- **A wrong sentence in a commit message:** ce67c1a6c says "no cutoff of the A4 count gives 1020". The band
  6 < k ≤ 12 does, as the seat's own output in that commit shows. The band was found by the read-only check of this
  note, not by the seat. The commit stands; this line corrects it.
- **The card mis-states A3:** its item says the run of 6 "has two such"; § 2 above says one.
- **The torsion is computed in double precision.** Tolerance 10⁻⁹, met with room.
- **A comment in the sealed `w2_cd.py`** says "the standard model" for the standard realization of A₄. It means
  nothing more and cannot be changed after the seal.
- **Commits:** the card c1a9171a4; scripts 28543ea68; outputs 0b83563ec (C, D) and 737b8f01e (A, B); post hoc
  bb40cd8e2 and 4f5a9949b, outputs ce67c1a6c and d0e9b994c.

0 of 19.
