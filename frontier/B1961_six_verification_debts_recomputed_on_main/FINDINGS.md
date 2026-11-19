# B1961 — Six verification debts recomputed on main: the SM seat's W27, W28, W30 and W47, and main's own P-155, P-156 and P-157

**Verdict: PROVED (a verification arc).** Main, 2026-11-19. Register rows P-054, P-055, P-056, P-155, P-156, P-157.
Data-free. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /W27|W28|W30|W47|forced kernel|Dobrescu|vector-spinor|metaplectic/: 6 of 1702 arcs on main match (NEGATIVE 4, PROVED 2); 8 register rows match (DONE 3, QUEUED 5)`.
- **What the record already held:**
  - B1689 verified the SM seat's W23, W24 and W44 on main.
  - W27, W28, W30 and W47 were REGISTERED only, at harvest rows 943, 944, 946 and 1068.
  - B1634 P5 had one of the six η-character twists move χ_{3/2} to 1, at j = 4.
- **Why now:** these debts age past the register's limit on 2026-11-25.
- **The literature:**
  - the Dobrescu–Poppitz condition (B. A. Dobrescu and E. Poppitz, Phys. Rev. Lett. 87 (2001) 031801), quoted from the
    seat's relay and not re-derived here;
  - Harer and Zagier (Invent. Math. 85 (1986) 457) for χ(M₁,₂) = 1/12;
  - the binary octahedral group, the Clifford group, SL(2, 𝔽₃) and the 24 characters of Mp₂(ℤ) are standard finite-group
    facts, each computed here rather than cited.

## How it was done

- **Who computed:**
  - Seven agents of main's own family each took one claim set from its stated source: the SM seat's relay at its
    lines, or main's arcs.
  - Each wrote new code, with the claims and its expectations stated at the top before running.
  - None ran any seat's code. Each read B1620's or B1602's own functions and files only where its debt named them.
- **Main re-ran every script** from this arc's folder. Each output equals main's first re-run, and the run files
  beside the scripts are main's.
- **Main read every result behind a finding that changes the record:** W28's stabiliser, W47's index table and
  P-157's families.
- **Local paths:** two scripts carried the repository's absolute path on this machine. They now find the root from
  their own location.

## The results

### W30 (P-054), the SM seat's relay § 27 (`verification/w30.py`)

- **Q1 holds**, and it is a tautology, as the seat's rule says: the puncture's −1 has order 2, so its image has
  eigenvalues ±1, never ω.
- **Q2 holds in SU(3).**
  - The nine centre twists of the qutrit pair with commutator ω are all conjugate, with an intertwiner of dimension
    1 each.
  - In GL(3) the class is a continuous family, so "one class" needs the SU(3) qualifier.
- **The moves hold as stated.**
  - L, R and −I keep the ω class, over all 27 cases.
  - The swap P sends it to the ω̄ class; P with complex conjugation keeps it.
- **The image holds as stated.** The moves act through SL(2, 𝔽₃): with the lifts normalised to determinant 1, the
  group has order 72, which is 24 modulo scalars. On ℂ³ it splits as 2 ⊕ 1, with one invariant line.
- **One figure needs a qualifier.** With the sign −I added, the order is 216 modulo scalars and the action is
  irreducible. "216" is an order modulo scalars.
- **With W24 (B1689), P-054 is paid.**

### W27 and W28 (P-055), the relay's §§ 23 and 24 (`verification/w27.py`, `w28.py`)

- **W27's representation theory holds exactly.**
  - Three 27s of E₆ branch to the Standard Model with 18 SU(2) doublets.
  - Every cubic, mixed and gravitational anomaly sum is zero, per 27 and for three.
  - The Witten parity is even.
- **W27's Dobrescu–Poppitz clause is PARTIAL.** It is a consistency condition (a global anomaly of the six-dimensional
  theory must cancel), not a finite classification. Read as "the doublet count divisible by 6" (quoted, not
  re-derived), "iff the number of parity sectors is a multiple of three" holds when a sector counts one Standard
  Model generation (4 doublets). If a sector is a full 27 (6 doublets), the condition holds for every number of
  sectors and does not select three.
- **W27's "derived given Λ" is not checked.** It rests on Λ and F-MC's inputs, and stays the seat's.
- **W28 holds in most of its claims:**
  - the six local solutions carry 2O, of order 48;
  - they split as 2 ⊕ 4, spin ½ ⊕ spin 3/2, by characters over all 48 elements;
  - the index sets hold under each symmetry: the moves −3, −1, +1, +3; the flavour group −3, 0, +3; jointly ±3;
    locality ±3;
  - 2O is the full normaliser of Q₈, with image the 24 cube rotations (the Clifford group);
  - the moves act through PSL(2, ℤ/4) ≅ S₄;
  - SU(2)₁'s projective modular data match, and do not see the hand.
- **W28's Q₈ wording is PARTIAL.** Q₈ is the SU(2) lift of the Pauli group, which has order 16; they agree modulo
  phases. The three axes are mutually unbiased, with every overlap ½.
- **W28's flavour clause FAILS.** "The two middle conditions … break the flavour U(3) to a phase" is wrong.
  - The flavour elements that keep each middle condition span 7 dimensions, not 1. In the right basis the flavour
    algebra is 1 ⊗ M₃, and the conditions are ℂ² ⊗ (1, 1, 1) and its complement. So the unbroken group is U(1) × U(2).
  - The half "they couple the parity sectors" holds.
  - The ±3 result, which uses the whole flavour group with the moves, is unaffected.
- **W28's physics identifications are not checked:** the parities as the three global forms of su(2), and the common
  point as 't Hooft's twist-eater.
- **With W23 (B1689), P-055 is paid.** It is paid with the failure above recorded, and with the seat's readings
  kept as its own.

### W47 (P-056), the relay's § 51 (`verification/w47.py`)

- **The facts that hold:**
  - the flat line bundles are the 24 characters of Mp₂(ℤ), whose abelianisation is ℤ/24;
  - six twists keep the forced weight at 3/2;
  - every cusp exponent under every allowed twist is an odd multiple of 1/24, so the natural cusp conditions coincide.
- **The relay's index table is not reproduced.** It gives χ_{3/2} = 0 except −1 at r = 4 and r = 20.
  - With the dimension formula calibrated against known dimensions, main's run gives 0 at j = 0, 8, 12, 16 and 20,
    and +1 at j = 4 only.
  - That is B1634 P5's five zeros and one 1. The other convention (dual and conjugate) gives other values.
  - No twist reaches ±3 in either convention.
- **The headline is the seat's reading,** consistent with these facts: nothing on the surface forces one unit at
  the cusp.
- **P-056 is paid,** with the table's difference recorded.

### P-155: B1602's and B1603's forced kernel (`verification/p155.py`)

- **The record cannot identify the kernel.**
  - B1602's preregistration says the extension's sign choices "are not located in SnapPy's generators", and every
    candidate kernel was read.
  - Of 42 even-trace threads, 26 have two candidate kernels (D₄) and 16 have four (V₄).
- **The counts, restated over candidates:**
  - 17 threads carry on some kernel and 25 on none. The 17th is +LLLRLLR, whose reading B1604 withdrew.
  - On B1604's reliable kernels it is 16 of 42.
  - 12 carriers carry on every kernel, and 5 on some only.
  - Taking one kernel position alone gives 15, 12, 4 or 6 carriers.
  - ±LLR has the generation shape on every candidate.
- **P-155 is paid by its second branch:** the counts are restated as over candidate kernels, by dated notes on B1602
  and B1603. Identifying the kernel needs the seat's explicit even-trace extension.

### P-156: B1606's premises (`verification/p156.py`)

- **(i) holds on an independent construction, with a caveat.**
  - With the moves alone the group has order 48, and the invariant pieces have dimensions 0, 2, 4 and 6.
  - Adding the parity grading gives order 192, irreducible, so the index is ±3 exactly when the condition keeps the
    grading.
  - The caveat: the ±1 conditions depend on the lift's scalar on each block. In 32 of 64 sign choices the moves'
    action is irreducible, and only ±3 is left.
- **(ii) index = dim Λ₊ − 3 is not computed anywhere on main.** Only its arithmetic consistency is checked: it is
  additive over blocks and antisymmetric.
- **(iii) the M₁,₂ identification is not computed either.** What is computable holds: dim_ℂ M₁,₂ = 2, and
  χ(M₁,₂) = 1/12 by Harer–Zagier, as main's B1624 also has.
- **P-156 moves and stays open,** for (ii), (iii) and (i)'s dependence on the block scalars.

### P-157: B1620's mixed tensor assignments (`verification/p157.py`)

- **Reproduced on main**, with B1620's group and subgroup lattice imported and the mixing code written new:
  - a Dirac charged lepton with a Majorana neutrino in Sym² T gives two-parameter TM2 families;
  - TM1 appears only with a T̄ ⊗ T neutrino;
  - every non-fixed TM family has exactly two parameters.
- **B1625's same-tensor wording** ("TM1 under T̄ ⊗ T only, TM2 under T ⊗ T") omits that TM2 occurs under T̄ ⊗ T
  too.
- **P-157 is paid.** Whether any of these families reaches the PMNS data is not asked here: no data is compared.

## What it changes in the record

- Brackets on harvest rows 943, 944, 946 and 1068: verified in part on main, here.
- Dated notes on B1602 and B1603: the counts are over candidate kernels.
- A dated note on B1625: TM2 occurs under T̄ ⊗ T as well.
- The point register: P-054, P-055, P-056, P-155 and P-157 are DONE, and P-156 is moved.
- The SM seat is told of W28's flavour clause and W47's index table (M51).
- **Owed next:** the relay's lines of §§ 23, 24, 27 and 51 to be placed again in the register on this arc's ground.

## Files

`verification/w27.py`, `w28.py`, `w30.py`, `w47.py`, `p155.py`, `p156.py` and `p157.py`, each with its run file
`<name>_run.txt` (main's run from this folder). The lock is `tests/test_b1961_six_debts.py`.

0 of 19.
