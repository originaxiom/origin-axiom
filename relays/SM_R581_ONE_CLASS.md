# SM-R581 — one comparison class for the structural grades: the package's rate is the route's, 384 of 1199

*Page of the SM seat, 2026-11-26, for register row P-581 (main's M52, item 1). Sealed card:
`relays/cards/SM_R581_one-class-for-the-structural-grades.md`, committed with both scripts (8a6f01fd6) before any run
on the class. Data-free: census presentations and group theory only. No measured value was read or compared.*

## 1. What was run

- **Stage 1.** `relays/sm_r581/extract_presentations.py` (SHA-256 98f87a6a5684382a), in population mode. It froze
  the 1199 presentations of rule K to `relays/sm_r581/r581_presentations.json` (SHA-256 8c825d9c27295df6).
- **Stage 2, decisive.** `relays/sm_r581/run.py` (SHA-256 7307d284e7526972), run as
  `python3 -I run.py MAIN_CHECKOUT r581_presentations.json .` from relays/sm_r581/. It took 8 s.
  - Output: `relays/sm_r581/r581_run.txt` (SHA-256 0ca6caa4891c96ee) and `relays/sm_r581/r581_results.json`, which
    holds a rate for every member.
- **Rule K, as sealed.** Every orientable one-cusped hyperbolic census manifold with at most 6 ideal tetrahedra, in
  census order: N = 1199. F-MC's construction is applied to each, unchanged.
- **No post-hoc change.** Neither script was edited after sealing, and there is no posthoc file.

## 2. Results

| property | members of K | rate |
|---|---|---|
| E₆ route: π₁ ↠ 2T, at least one class | 384 | 0.3203 |
| exactly the root's count (2T classes = 2) | 304 | 0.2535 |
| ℤ₆ global form | 384 | 0.3203 |
| the hypercharge direction | 384 | 0.3203 |
| sin²θ_W = 3/8 at SU(5) | 384 | 0.3203 |
| **the package (all four)** | **384** | **0.3203** |
| E₇ label: π₁ ↠ 2O | 362 | 0.3019 |
| E₈ label: π₁ ↠ 2I | 609 | 0.5079 |
| any exceptional label | 926 | 0.7723 |
| plant: π₁ ↠ ℤ/3 | 1199 | 1.0000 |

The package's rate by number of tetrahedra:

| tetrahedra | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| members with the package | 2 of 2 | 1 of 9 | 21 of 52 | 74 of 223 | 286 of 913 |

The three steps after E₆ were computed once, and no step reads an object:
- the B862 kernel is ℤ₆;
- the traceless commutant of su(3) ⊕ su(2) in su(5) is one-dimensional, proportional to (2, 2, 2, −3, −3);
- sin²θ_W along it is 3/8.

The root, m004, has 2 classes onto 2T. It has none onto 2O and none onto 2I.

## 3. Against the sealed expectations

| | expectation | prior | outcome |
|---|---|---|---|
| E1 | E₆-route rate in [0.25, 0.45] | 80% | **holds:** 0.3203 |
| E2 | rate of exactly 2 classes in [0.22, 0.40] | 75% | **holds:** 0.2535 |
| E3 | ℤ₆, the hypercharge direction and 3/8 each at the route's rate | 98% | **holds:** 384 each |
| E4 | the package at the route's rate; no member has the route without it | 98% | **holds:** 384 = 384 |
| E5 | 2O rate below 2T rate | 60% | **holds, narrowly:** 0.3019 < 0.3203 |
| E6 | 2I rate below 2T rate | 55% | **fails:** 0.5079 > 0.3203 |
| E7 | rate at 6 tetrahedra within 0.10 of rate at ≤ 5 | 60% | **holds:** 0.3133 against 0.3427 (98 of 286) |
| E8 | some exceptional label reached by more than half of K | 45% | **holds:** 2I at 0.5079 |
| P | all plants and controls hold | 95% | **holds** (below) |

| control | must give | outcome |
|---|---|---|
| P1 | ℤ/3 rate exactly 1 | 1199 of 1199 |
| P2 | each ℤ/3 count = 3^d − 1 from H₁ mod 3 | all 1199 |
| P3 | (ℤ/2)³ rate 0 on two-generator presentations | 0 of 1041 |
| C1 | m004 has 2 classes onto 2T | 2 |
| C2 | per-object 2T class counts agree with main's B993 output | 400 of 400 |
| C3 | ℤ₆; commutant of dimension 1, ∝ (2,2,2,−3,−3); 3/8 | all three |

## 4. Reading

- **Under one rule, the structural package has one grade.** In K, ℤ₆, the hypercharge direction and sin²θ_W = 3/8
  are each reached by exactly the members that reach E₆: 384 of 1199, about one in three. Given the route, the rate
  of each is 1. FL-26's split cannot survive one class, because DERIVED against the SM and REPRODUCED against the GUT
  class read the same constant of the construction against two targets.
- **Proposal to main (a recommendation, not a finding).** GENESIS-level text should carry the package as a constant
  of F-MC's construction, reached by 32% of comparable objects (rule K). It should not grade ℤ₆, Y and 3/8
  separately. The one object-dependent fact remains π₁ ↠ 2T, as B993 said.
- **The one-in-three figure transfers to K, slightly lower.** B993's first 400 give 37.2%. K, which includes them,
  gives 32.0%. Over 6-tetrahedron manifolds alone the rate is 31.3%. The root's exact count of 2 is shared by 25.4%.
- **E6 failed, and the failure is informative.** π₁ ↠ 2I = SL(2, 5) is more common than π₁ ↠ 2T, at 51% of K. So
  E₆ is not the label most often reached. An exceptional label of some kind is reached by 77% of K.
  - **Inference, not computed:** E₇ and E₈ have no complex representations, so the cascade's chirality test cannot
    start there. If that holds, E₆ is the only label that leads to a package. That is a property of E₆, not of the
    object.
- **The root sits on the narrow side.** m004 reaches only 2T. That fits B727 (the trace field ℚ(√−3) gives only E₆),
  but it is a property of the field, which B993 and B727 show is shared beyond the root.

## 5. What is NOT checked

- **The cascade's selection itself** (B861) and its menu completeness (P5) are taken from the record. They take E₆ and
  no object, so they enter the package as a constant. A defect there would move every member at once and leave the
  rate unchanged.
- **The self-conjugacy of E₇'s and E₈'s least representations** is cited, not computed.
- **The field-level rule,** trace field ℚ(√−3) with one ramified prime, was not computed. It would give a smaller,
  stricter class.
- **Classes outside K were not computed:** multi-cusped manifolds, bounds above 6 tetrahedra, and the grammar class of
  B996.
- **No second computation by another seat exists yet.** C2 matches main's B993 code object by object on 400 members.
  That code shares the brute-force method, so it is a reproduction, not an independent check.
- **Chirality, generations, scale and values.** None of the 19 parameters is touched.
