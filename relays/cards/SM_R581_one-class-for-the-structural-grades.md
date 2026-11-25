# SM-R581 — one comparison class for the structural grades, and the structural package's rate in it

*Card of the SM seat, 2026-11-25, for register row P-581 (main's M52, item 1: FL-26, then Q-STRUCT). Written, with
its scripts (`relays/sm_r581/extract_presentations.py`, SHA-256 98f87a6a5684382a; `relays/sm_r581/run.py`, SHA-256
7307d284e7526972), before either is run on any member
of the class. The scripts were smoke-tested only on eight census manifolds with 7 tetrahedra, outside the class, and
printed no rate. Data-free: the inputs are census presentations of fundamental groups and group theory. No measured
value is read, and none is compared.*

## 0. The question, and what the record already says

- **The row (P-581).** The structural grades use two comparison classes. ℤ₆ and the hypercharge direction are graded
  DERIVED against the SM. sin²θ_W = 3/8 is graded REPRODUCED against the GUT class. Yet every SU(5) embedding gives
  ℤ₆ (B862: "as a GROUP inside SU(5)"), and the route to E₆ is generic, about one manifold in three. The row asks for
  one rule for the class (Q2), then the package's rate among comparable objects (Q-STRUCT).
- **The package (F-MC, `GENESIS.md` § 5, v1.1).** The root's arithmetic gives π₁ → 2T. McKay gives E₆. The fused
  cascade (B861) ends at su(3) ⊕ su(2) ⊕ u(1), inside SU(5) on its last steps. The global form is
  [SU(3)×SU(2)×U(1)]/ℤ₆ (B862), and the hypercharge direction is diag(2, 2, 2, −3, −3)/6 (B862; forced by anomalies
  in B1160). sin²θ_W = 3/8 is the SU(5) normalisation of that direction.
- **What is object-specific, per the record.** B993 found that the cascade (B861, B862, B864) names no manifold. Its
  one object-dependent step is the surjection π₁ ↠ 2T, which holds for 37.2% of the first 400 one-cusped census
  manifolds; 32.8% have exactly m004's two classes. B996 found the same shape over grammars: 5 of 7 metallic words
  reach 2T. B727 found that E₆'s three faces are one ADE label, and that 4 of 13 knots, three of them non-arithmetic,
  surject onto 2T. B862's ℤ₆ is the kernel of the map into S(U(3)×U(2)) and so holds for every SU(5) embedding of the
  SM algebra.
- **Inference to be tested, stated now.** If the record is right, every property after E₆ is a constant of the
  construction, and the package's rate in any class equals the rate of its first step. The two comparison classes of
  the grades (the SM for ℤ₆ and Y, the GUT class for 3/8) are then not classes of objects. They are two targets that
  the same constant is read against.

## 1. The one rule (stated before any computation)

> **Rule K.** The comparison class of a structural grade is the set of objects of the root's kind at no greater
> complexity than a fixed bound, with the root's construction applied to each, unchanged. Here the class is every
> orientable one-cusped hyperbolic 3-manifold of the census with at most 6 ideal tetrahedra, in census order (1199
> manifolds; the root m004 has 2). The construction is F-MC's, read at the group level as B993 read it: a surjection
> π₁ ↠ 2T, then McKay, then the fused cascade with its menu and principle fixed, then the global form, the hypercharge
> direction and sin²θ_W at the SU(5) normalisation. A property's grade is its rate in K. A property whose rate is 1
> conditional on the step before it earns no grade of its own.

- **Why this rule.** "Of the root's kind" means orientable, hyperbolic and one-cusped. These are the properties the
  chain uses to reach the root; the cusp count is the root's, and B993 used it. "Same construction" forbids changing
  any step for another object. The bound of 6 tetrahedra is the smallest that contains B993's 400 manifolds; it is
  fixed now, not tuned.
- **What it rules out.** It rules out grading one property against the SM and another against the GUT class. Both are
  targets, and a rate needs a population of objects.
- **Not part of K (stated, not computed).** The field-level reading, which requires trace field ℚ(√−3) with one
  ramified prime, is stricter and would give a smaller class. B727 and B993 report that ℚ(√−3) is shared beyond
  the root (m003 has it). Multi-cusped manifolds are excluded by K. A rule that admitted them would have
  b₁ ≥ 2 and more quotients.

## 2. What is computed

- **Stage 1** (`relays/sm_r581/extract_presentations.py`, needs the census package). It freezes each member's π₁
  presentation to a JSON file. The decisive stage reads only that file and records its SHA-256.
- **Stage 2, the decisive script** (`relays/sm_r581/run.py`: standard library, numpy and sympy, plus main's B862
  module `frontier/B862_global_form/global_form.py`). For each member it counts the surjections π₁ ↠ G up to Aut(G).
  The count is exhaustive over generator images: relators are checked in G's table, and the first image is fixed to a
  class representative and weighted by the class size. G runs over 2T = SL(2, 3) (E₆), 2O (E₇) and
  2I = SL(2, 5) (E₈). The group orders and |Aut| (24/24, 48/48, 120/120) are asserted by computation.
- **The steps after E₆,** computed once and exactly, with no object as input:
  - the B862 kernel, by main's kernel_exact, which must be ℤ₆;
  - the traceless commutant of su(3) ⊕ su(2) in su(5), which must be one-dimensional and ∝ diag(2, 2, 2, −3, −3);
  - sin²θ_W = Tr T₃² / Tr Q² on the 5, along the computed direction, which must be 3/8.
- **The table.** For each property: how many members of K yield it, the rate, and the rate by tetrahedra.
- **Not computed.** The cascade's selection itself (B861) is taken from the record. It takes E₆ and no manifold, so it
  is a constant of the construction. The claim that E₇ and E₈ carry no chiral matter is not computed either: their
  least representations, the 56 (pseudoreal) and the 248 (real), are self-conjugate, so the cascade's registerability
  test cannot pass there. That is a standard fact, cited and labelled as such. The 2O and 2I rates are context and
  enter no package.

## 3. Controls and plants (each must come out as stated, or the run is void)

| | control | must give |
|---|---|---|
| P1 | plant: π₁ ↠ ℤ/3, a property every member has (H₁ ⊇ ℤ), through the same counter | rate exactly 1 |
| P2 | each member's ℤ/3 count equals 3^d − 1, d = F₃-rank of H₁ from the relator matrix (second route) | all 1199 |
| P3 | plant: π₁ ↠ (ℤ/2)³ on two-generator presentations (impossible: rank ≤ 2) | rate exactly 0 |
| C1 | the root m004: 2T classes (B266, reproduced in B993) | exactly 2 |
| C2 | per-object agreement of the 2T class count with main's B993 output (sl23_baserate.json) | 400 of 400 |
| C3 | the steps after E₆ | ℤ₆; commutant dim 1, ∝ (2,2,2,−3,−3); 3/8 |

P1 to P3 were run on the smoke inputs outside K and passed; no rate was printed.

## 4. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| E1 | the E₆ route (2T classes ≥ 1) has rate in [0.25, 0.45] over K | 80% |
| E2 | exactly the root's count (2T classes = 2) has rate in [0.22, 0.40] | 75% |
| E3 | ℤ₆, the hypercharge direction and 3/8 each have rate equal to E1's, i.e. rate 1 given the route | 98% |
| E4 | the package (all four) has rate equal to E1's; no member of K has the route without the package | 98% |
| E5 | the 2O (E₇) rate is below the 2T rate | 60% |
| E6 | the 2I (E₈) rate is below the 2T rate | 55% |
| E7 | the package rate at 6 tetrahedra differs from that at ≤ 5 by less than 0.10 | 60% |
| E8 | at least one exceptional label (2T, 2O or 2I) is reached by more than half of K | 45% |
| P | P1, P2, P3, C1, C2 and C3 all hold | 95% |

## 5. What it means

- **E1 to E4 hold.** Under one rule, ℤ₆, the hypercharge direction and sin²θ_W = 3/8 have one grade, the same as the
  package's. That grade is generic, at the rate of π₁ ↠ 2T in K. FL-26's two classes collapse into one, and the
  DERIVED/REPRODUCED split does not survive it. The proposal to main is that GENESIS-level text should carry the
  package as "a constant of the construction, reached by about r of comparable objects", where r is the measured
  rate, and should not grade its parts separately.
- **E3 or E4 fails.** Then some step after E₆ depends on the object, against B993's reading that the cascade names no
  manifold. That would be a finding about the record, reported plainly.
- **E1 is far outside its band.** The one-in-three figure does not transfer from the first 400 to K. The rate in K is
  then reported as the rate, and the figure in `GENESIS.md` is flagged.
- **Any outcome.** No outcome yields a value of any of the 19 parameters, and none bears on chirality, generations or
  scale. This is a grade of a structural statement, not a test of the SM.

## 6. Imports and files

- **Imports.** The census triangulations and the census package's presentations (stage 1 only). The cascade's menu
  completeness (P5, B861). McKay's correspondence. The self-conjugacy of the least E₇ and E₈ representations (cited).
- **Files.** relays/sm_r581/: both scripts, then r581_run.txt, r581_results.json and the frozen presentations,
  all written in phase 2. The page will be relays/SM_R581_ONE_CLASS.md, and the claim card
  relays/claims/CLAIM_2026-11-26_one-class-structural-package.md.
