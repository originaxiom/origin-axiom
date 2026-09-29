# B1399 — THE RANK-TWO HIGGS: run as sealed, the escape finds nothing. On the 102 resolved members of the 109-member census no pair of cuspidal classes gives three generations (P1 NONE) or any number of generations (P2 NONE). The reason is parity: on every resolved member the count is even in every direction. The count lives only at cusps whose leading Fourier shell has three or more directions, and a shell whose vectors span a sublattice of index 2 makes a cusp's term even. The census's hexagonal cusps, the only ones that can give odd counts, sit on four members, and those four are unresolved.

**Date:** 2026-09-28 (sealed and run), banked 2026-09-29 · **Seat:** cc (the SM-derivation branch) · **Occasion:** B1398 named this
escape as the smallest change to the seat's frame. The owner saw the verdict and the seal, and asked for the run. · **Status:**
- SEALED: `PREREGISTRATION.md` was committed at b2985b42, with its sha256 in SEAL_LEDGER, before any harmonic form of the census was
  computed.
- COMPUTED: the banked identity passed (6fe28a6b), then the census ran as sealed.
- **Verdict as sealed:** P1 NONE and P2 NONE on the 102 resolved members. The 7 unresolved are listed (§4) and do not count toward NONE.
  P3 is read in §1.

**Fence:** the seat's frame with 27 matter; cuspidal Higgs classes of rank exactly two; covers of degree ≤ 3 of the 99; dimension 3
scoped to the sealed planes. · **Price:** unchanged, 0 of 19 · **Numbering:** B1399.

## 0. Seen from above

B1398 left one way to three generations inside the frame's own counting rule: 27 matter plus a Higgs field built from two independent
harmonic forms. The pattern the rule allows is g·(1, 0, −1, 0, 1, −2) on six direction classes. At g = 3 it needs the count to reach
±3 and ±6.
- **It is not there.** Of the 109 covers, 102 resolved. On 101 of them the count C is zero in every direction of every Higgs plane read.
  On one (a degree-3 cover of o10_150708) it takes the values 0 and ±2 and nothing else. No member realises any g.
- **This is structural, not a near miss.** The count is a sum over cusps, and each cusp's term is read from the first non-vanishing
  shell of Fourier modes there.
  - A shell with one or two directions gives a band and contributes 0 in every direction (the sealed reduction; B1370's annulus).
  - A shell whose vectors span a sublattice of index m contributes a multiple of m (§2).
  - On the resolved members, 204 of the 207 cusps lead with a one-direction shell. The other 3 lead with a three-direction shell of
    index 2, on cusps of shape √−3. So C is even everywhere on the resolved set, and 3 is odd.
- **Where odd counts could live.** A hexagonal cusp's first shell has three directions spanning the whole lattice (index 1). The census
  has 8 such cusps, two on each of four members: the four-cusped covers of o10_150704, o10_150725 and o10_150727 (two covers). These are
  exactly the four whose two seeds disagree on every rung of the ladder, so the sealed rule leaves them unresolved. Read seed by seed after
  the seal (§4), none gets past |C| = 2 or 24 breakpoints; g = 3 needs 6 and 36.
- **In the architecture's terms.** The frame's count is carried by Eisenstein cusps, and odd counts only by hexagonal ones. Small covers
  of the 99 members of m004's class have almost none. cube~3.24 has three, and its covers are outside this census by size (§5).

## 1. The outcome, as sealed

**The banked identity passed** before any census number was read (`verification/identity_run.txt`, commit 6fe28a6b):
- cube~3.24: C = +2 on v₊ and −2 on −v₊ with both seeds. The leading shells match B1387: the first hexagonal shell at cusps 0 and 3,
  one direction at cusp 1, and the √3 shell at cusp 2.
- The breakpoint machinery: 0 mismatches with the Morse count on the design-time synthetic shells.
- The linear programs: a synthetic count built to realise g = 3 was found feasible (margin 0.067), and its L re-verified. The same count
  with one required jump removed was infeasible.
- B1398's pattern, recomputed from the record's vectors: {(1, −4): 3, (1, 0): 0, (1, 1): −3, (1, 6): 0, (3, −2): 3, (3, 8): −6}.

**The census** (`verification/census.json`, one record per member; `census_run.txt`):

| | members | resolved | unresolved |
|---|---|---|---|
| cuspidal dimension 2 | 91 | 84 | 7 |
| cuspidal dimension 3 | 18 | 18 (every one on all 203 sealed planes) | 0 |
| total | 109 | **102** | **7** |

- The ladder: 88 members resolved on rung 1, 13 on rung 2 and 1 on rung 3. Every member that went past rung 1 failed its earlier rungs on
  residuals.
- **P1 (the kill test): NONE.** No resolved member realises g = 3. Prior: NONE, about 85%.
- **P2: NONE.** No resolved member realises any g ≠ 0. By oddness, L realises g exactly when −L realises −g, so g > 0 suffices. The
  pattern needs |C| = 2g on the class (3, 8), so g ≤ max |C| / 2. Prior: NONE, about 60%.
- **P3, per member** (every number in `census.json`):
  - max |C| = 0 on 101 members, with no breakpoints, on V's circle or on all 203 planes.
  - max |C| = 2 on one member, with 12 breakpoints and total variation 24 (§3).
  - achievable g: none on any member.

## 2. Why the count is even: the lattice behind the shells

**The shells.** The count at a cusp is read from its leading shell: the first set of equal-length dual-lattice vectors k whose
coefficient map on V survives the kill. In two dimensions the dual lattice is the cusp lattice turned through a right angle and
rescaled. So the shells, their numbers of directions, and the sublattices they span can all be read from SnapPy's cusp shape
(`verification/post_run_checks.py`, record `post_run_checks_run.txt`).
- All 229 cusp shapes of the 109 members lie in ℚ(√−3).
- The pipeline's leading-shell directions equal the lattice's at all 207 cusps of the resolved members. That also confirms the solve and
  SnapPy number the cusps alike.

**The parity lemma.** Let a shell's vectors span a sublattice Λ′ of index m in the dual lattice Λ*.
- Every shell function F = Σ Re(z_k e^{2πi k·x}) is invariant under translation by (Λ′)*.
- The quotient (Λ′)*/Λ has order m and acts freely on the cusp torus ℝ²/Λ.
- So {F > 0} is an m-fold cover of its image, and χ({F > 0}) is a multiple of m. ∎
- Checked directly with B1387's Morse count on 40 random shell functions for each of three shells (`post_run_checks`, item 6):
  - the √−3 cusp's third shell (index 2) gives 0 and ±2;
  - the hexagonal first shell (index 1) gives 0 and ±1;
  - the hexagonal √3 shell (index 3) gives 0 and ±3.

**The resolved set, cusp by cusp:**

| leading shell | directions | span index | cusps | contributes |
|---|---|---|---|---|
| first | 1 | — (a line) | 192 | 0 (band) |
| second | 1 | — (a line) | 12 | 0 (band) |
| third, shape √−3: {±2, ±1 ± √−3} | 3 | 2 | 3 | even |

- None of the 207 is hexagonal or square.
- The three √−3 cusps are on the covers of o10_150708, o10_150710 and o10_150718. On each, the first two shells vanish on V: their ratio
  to the largest is below 10⁻³ on both seeds. This is consistent with B1370's selection of allowed shells by a cusp's fixers, which is
  not checked here.
- **So C ∈ 2ℤ in every direction on all 102 resolved members.** That excludes g = 1 and g = 3, whose targets are odd. g = 2 needs |C| = 4,
  and the maximum is 2. The exact linear programs, run as sealed, agree: no member realises any g.

**The census's hexagonal cusps:**
- There are 8, two each on the four-cusped covers of o10_150704, o10_150725 and o10_150727 (two covers).
- Their first shell is the six units of ℤ[ω]: three directions spanning the whole lattice (index 1). These are the only first shells in
  the census that can contribute an odd term.
- All four members are unresolved (§4).

## 3. The one member with a non-zero count

The degree-3 cover of o10_150708: 30 tetrahedra, two cusps, cuspidal dimension 2. It is SnapPy's `covers()` entry 24, and entry 25 is
isometric to it.
- **The cusps.** Cusp 0 leads with a one-direction shell and contributes 0. Cusp 1 has shape √−3 and leads with its third shell (three
  directions, index 2).
- **C on V's circle.**
  - 12 breakpoints, each with jump ±2. Each is a merged pair of critical points of the angle map, as the lemma's free ℤ/2 pairs them.
  - The values run 0, 2, 0, −2 four times around the circle, with total variation 24.
- **Not realisable.**
  - The breakpoint bound allows g = 1 (24 ≥ 12).
  - The values do not: g = 1 needs ±1.
  - g = 2 needs ±4.
- **Stable.**
  - The two seeds agree within 10⁻³ at every breakpoint.
  - 720 directions away from the breakpoints each show their arc's value by a full Morse count.
  - Re-run from scratch in a fresh process, it reproduces every recorded field.

## 4. The seven unresolved members

The sealed rule: a member failing every rung is unresolved, is listed with the verdict, and does not count toward NONE. They are also
listed in `census.json` → `summary.unresolved_members`.

| parent (degree 3) | cusps | why unresolved | hexagonal cusps |
|---|---|---|---|
| o10_150704 | 4 | the seeds disagree on V on every rung (C on an arc; 20 vs 16 breakpoints; 22 vs 24) | 2 |
| o10_150725 | 4 | the seeds disagree on every rung (C on an arc; breakpoints apart > 10⁻³; 24 vs 22) | 2 |
| o10_150727 | 4 | the seeds disagree on every rung (12 vs 20 breakpoints; breakpoints apart > 10⁻³, twice) | 2 |
| o10_150727 (a second cover) | 4 | the seeds disagree on every rung (14 vs 18; 10 vs 12; C on an arc) | 2 |
| o10_150710 | 2 | the kill at cusp 1's third shell is ambiguous (ratio 0.078) | 0 |
| o10_150723 | 2 | the kill at cusp 1's first shell is ambiguous (ratio 0.041) | 0 |
| o10_150693 | 2 | B1387's walk does not terminate, on every rung and both seeds | 0 |

**A post-seal read-out.** It decides nothing and is recorded in `verification/unresolved_readout.py`, `unresolved_readout.json` and
`unresolved_readout_run.txt`.
- **Method.** Every rung is solved again with both seeds, and each seed's forms are read on their own, without the two-seed agreement.
  For an ambiguous kill, both readings are taken: the shell killed, and the shell leading. For each seed, rung and reading this gives
  max |C|, the total variation, and the g realised by the same exact linear programs.
- **The four hexagonal members.**
  - max |C| is 1 or 2 and the total variation 4 to 24, in every seed and on every rung.
  - The values include ±1, as index 1 allows.
  - No g is realised.
  - The breakpoint counts drift between seeds and rungs. On the o10_150725 cover they are 24, 24, 20, 20, 24 and 22 while the total
    variation stays at 24. So the breakpoints come in clusters too close for the solve to separate, which is the numerical risk the
    seal's fences name.
- **The ambiguous kills.** Their ratios are the same on every rung (0.041 and 0.078), so no rung could have settled them.
  - On the o10_150710 cover, the reading that kills cusp 1's third shell gives C = 0 everywhere. The reading that keeps it gives
    max |C| = 2 with total variation 24, as on o10_150708's cover.
  - On the o10_150723 cover, the reading that keeps cusp 1's first shell gives C = 0. The reading that kills it leads with the third
    shell (three directions), whose rank on the circle is itself ambiguous (ratio 0.066), so it cannot be read.
  - No g in any reading.
- **The o10_150693 cover** cannot be read: no rung produced forms.
- **So** no seed, rung or reading of the six readable members gets past |C| = 2 or 24 breakpoints, below the 6 and 36 that g = 3
  needs. This bounds what the unresolved members could hide, as numerics read without the sealed guard. It does not enter the verdict.

## 5. What is settled and what is not

**Settled on the resolved census.**
- The rank-two escape gives no generations at all, and three is excluded by parity.
- The sealed NONE branch says what comes next. The next escapes inside the E₆/E₇ frames are B1372's door-2 residual (a count rule that
  makes SL(2)_β doublets chiral) or independent walls, each with 27 matter.
- Outside them, the record's different-frame escape is sL-4. It is E₈, whose commutant with the Standard Model is SL₅. There, non-split
  backgrounds on the cyclic tower give an exact three as a deck orbit, and it stalls at the same cusp/end law (B1398 §3's scope note;
  B1384 S5).

**Not settled.**
- **The four hexagonal members.** They are where odd counts can occur. The instrument cannot resolve them: near-coincident breakpoints.
  An exact treatment would decide them. It would use the order-3 rotation of a hexagonal shell to place its breakpoints symmetrically
  rather than by Newton seeds.
- **Larger covers, and cube~3.24's covers.** cube~3.24 carries the count (C = ±2, B1387). Three of its four cusps are hexagonal
  (`post_run_checks`, item 5).
  - Two of them lead with their first shell.
  - Cusp 2 leads with its √3 shell. That shell's vectors span an index-3 sublattice, so by §2's lemma the cusp's term is 0 or ±3: a
    free ℤ/3 of the cusp torus. A single cusp of this kind carries a three. That is a pointer, not a result: the count's physical
    reading is unpaid (sL-8). No hexagonal cusp in this census leads with its √3 shell.
  - Its double covers (180 tetrahedra; 27 of 31 have cuspidal dimension ≥ 2) are outside by size. Covers of degree ≥ 4 of the 99 are
    outside too.
- **Rank three, t-directions and non-cuspidal Higgs classes** are outside the seal's fences.
- **The count's physical reading** still needs sL-8's completion (B1392–B1397), whatever the count.

**The architecture reading (P022).**
- This is one frame's count on one family of generated structures: the small covers of m004's class. The result says where in that
  family the count can live: at cusps whose leading shell has three or more directions, and with odd values only at hexagonal
  (Eisenstein) cusps.
- It does not speak for the architecture. It says which structures a count-based three would need: ones with enough hexagonal cusps
  whose terms add up, like cube~3.24 and its covers. And it names the joint law (sL-8, with sL-5's deck question) that any such count
  must pass before it means anything.

## 6. Implementation readings, and two faults caught before the census

The instrument (`verification/rank_two_higgs.py`) follows the seal. Where the sealed text needed a reading, the reading is stated in
the instrument's docstring and here.
- **Ambiguity before the verdict.**
  - The kill: a ratio in [10⁻³, 10⁻¹) makes the member unresolved when it occurs at a shell up to and including the leading one. Shells
    past the leading one decide nothing.
  - The rank-one test on the circle uses the same band: σ₂/σ₁ below 10⁻³ is rank one, and [10⁻³, 10⁻¹) is unresolved.
  - An incomplete Morse count, incomplete critical points at 256 seeds, a failed jump account or a failed cross-check each make the member
    unresolved.
  - A walk that does not terminate fails that rung.
- **Arcs.** C on a circle is assembled from each cusp's arcs (the union of all cusps' breakpoints, merged below 10⁻⁶).
- **The dimension-3 planes** are built from the sealed normals by a fixed completion to an orthonormal pair.
- **The linear programs.**
  - The search over assignments is depth-first with feasibility pruning, capped at 200 re-verifications per g. The cap was never
    reached. Only one member had a candidate g (g = 1, §3), and no arc there carries the value 1, so there was no assignment to try.
  - g is tried only where the total variation is at least 12g and g ≤ max |C| / 2. Both are necessary conditions proved at the seal.
- **Two faults, caught on the non-census controls before the census ran,** logged in ERROR_LEDGER. The controls were degree-3 covers
  of o10_143601 and o10_143602, which are outside the 99.
  - **SnapPy's presentation was random (an E1 instance).** Two builds of one manifold gave 17 and 16 generators and so different solved
    bases. The dimension-3 planes, drawn in that basis, would have differed between builds. The fix is `snappy.set_rand_seed(1399)`
    before every manifold is built.
  - **The seeds' agreement was coded as a final test (an E2 instance).** The seal makes agreement part of each rung's acceptance. After
    the fix a disagreement fails the rung and the ladder moves on. In this census no outcome depends on it (§1).

## 7. Verification

- **The banked identity** first (§1), inside the pipeline.
- **Per member, the sealed guards:** two seeds on every rung; jump accounting at every breakpoint; the 720-direction cross-check by
  full Morse counts; and direct re-verification of any positive. No positive occurred.
- **Reproducibility.** Five members were re-run from scratch in a fresh process: the non-zero member, two of dimension 2 with one cusp,
  one with three cusps, and one of dimension 3. All five reproduce every recorded field (status, leading shells, circles, breakpoints,
  values, g). Timings differ: the census ran four workers at once.
- **Independent of the solve.** The cusp shapes, the shells' directions and their span indices come from SnapPy's shapes and exact lattice
  arithmetic, not from the harmonic forms. They agree with the pipeline at every resolved cusp (§2).
- **The lock** is `tests/test_b1399_the_rank_two_higgs.py`, about 35 seconds. It checks:
  - the census as recorded, and parity on the resolved set;
  - the parity lemma on random shell functions, and the lattices of the non-zero member and of a hexagonal member;
  - the linear programs on the synthetic counts, and B1398's pattern;
  - that the seeded build is deterministic, and that the non-zero member and a small one re-run to their records.

## 8. Fences

- **The frame.** F27+78, or F133 with the Higgs field in the (Y, γ) plane. The 27 matter's origin is not derived. Doublets get 0 by
  Lemma A.
- **The Higgs field.** Cuspidal classes (B1395's dynamical Higgs field) of rank exactly two, stable realisations only. Dimension 3 is
  scoped to 203 planes.
- **The census.** Covers of degree 2 and 3 of the 99 arithmetic members, 109 up to isometry, of which 102 resolved. No symmetry is
  imposed.
- **The count.** It is read from numerical harmonic forms under the sealed guards. The parity statement of §2 rests on the leading
  shells, which both seeds agree on for every resolved member.
- **Physics.** None crossed. The count's physical reading needs sL-8's completion. 0 of 19.

## Files

- `PREREGISTRATION.md`: the seal (unchanged).
- `verification/census_list.py`, `census_list.json`: the census list, from design time.
- `verification/breakpoint_check.py`, `breakpoint_check_run.txt`: the design-time breakpoint check.
- `verification/rank_two_higgs.py`: the instrument.
- `verification/identity_run.txt`: the banked identity.
- `verification/census.json`, `census_run.txt`: the census. The run was resumed once after 19 members; the per-member records were
  written as each member finished.
- `verification/unresolved_readout.py`, `unresolved_readout.json`, `unresolved_readout_run.txt`: the post-seal read-out of the seven.
- `verification/post_run_checks.py`, `post_run_checks.json`, `post_run_checks_run.txt`: the cusp lattices, the parity check, the
  reproducibility re-runs.
