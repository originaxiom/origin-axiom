# Origin Axiom: audit, retained results, and a physical next step

2026-09-05. Audited baseline **`f06d34054899e8c23672b836a7c534af77cbd35d`**.
The remote was fetched again after the full suite; main remained at this SHA.
This report distinguishes reading, reproduction of original code, independent
implementation, and physical interpretation. None is a substitute for another.

## Executive finding

The program is not merely a collection of unexplained numerical coincidences.
It has a substantial exact mathematical construction, explicit representations
and invariants, and some already-written conditional physical models. It is
also **not a verified physical theory of everything**. The principal gap is
an earned connection between those structures and physical fields, dynamics
and observables with a genuinely predictive input budget.

Both directions of skepticism were necessary in this audit:

- **Preserve positives:** the core algebra and conditional uniqueness tests
  pass; the nonabelian A2 witness passes a live exact triple/centralizer check
  after a loader repair; all five heavy reproduction batches pass, including
  carrier and Yukawa calculations. Older rank and dynamics slogans must not
  erase these assets.
- **Correct an actual instrument:** B915's purported two-loop unification
  curve does not satisfy its own two simultaneous UV equations. A comparison
  coupling leaks into its first sequential solve. A new independent solver
  fixes this; the specific historical comparison still misses its criterion.
- **Make a physical calculation:** derive beta coefficients and anomalies
  from the banked exotic multiplets, expose a full allowed-threshold condition,
  and test a common-UV-mass mechanism including radiative splitting. The result
  is a concrete mass target and a scoped mechanism constraint, not a fitted
  number relabeled as a prediction. See [PHYSICAL_MODEL.md](PHYSICAL_MODEL.md).
- **Verify the archive itself:** the clean baseline suite has five failures
  caused by missing evidence. Passing metadata tests did not guarantee that
  the evidence they described had been committed.

## 1. What the repository is for

The motivating proposal is a persistent remainder from an attempted
cancellation. Its initial mathematical realization uses two integer shears
L and R, whose first mixed product is

```text
L = [[1,1],[0,1]], R = [[1,0],[1,1]], A = LR = [[2,1],[1,1]].
det(A)=1, tr(A)=3, charpoly(A)=x²-3x+1, eigenvalues={phi²,phi^-2}.
```

The same small construction supports transfer-matrix dictionaries, a Möbius
fixed-point equation, a Lorentzian **phase-space** form, and a punctured-torus
mapping torus associated with the figure-eight complement. These relationships
are mathematical content. The phase-space signature (1,1) is not by itself
physical (3,1) spacetime.

The later program follows arithmetic fields, character varieties, trace maps,
representation categories, McKay correspondences, exceptional algebras, quantum
topological constructions, and observer/cut/closing operations. Its own P0
requires the **full relational construction**: members, fields/classes, ends,
sisters, both rows, child, cuts and axioms. Auditing only one knot invariant
would not audit that program.

The genesis is conditional on the stated axioms. A1–A6 select within their
declared construction; the remaining LR/RL convention/selection is tracked as
A7. The audit does not turn motivated assumptions into assumptions about the
actual universe that have already been experimentally established.

## 2. The journey visible in history

The clone contains 2,851 commits through the baseline. The following is a
selected dependency history, not a claim to have read every commit or arc.

| phase | achievement and change in question | source anchors |
|---|---|---|
| May: precise seed | matrices, transfer systems, topology; the conditional uniqueness theorem; early field-equation and Regge questions already exist | initial commit `517783f2`; `9d2cc5ed`, `514c046e`; B3, B6; `src/origin_axiom/` |
| June–July: relational expansion | trace/character varieties, arithmetic ends, exceptional algebra and topological/quantum dictionaries; multiple routes begin distinguishing a structure from its physical name | CLAIMS P17 onward; LAW_MAP; THE_FRAMEWORK; earlier progress-log entries |
| August: explicit algebra and physical comparisons | the E6/magic-square correspondence, 27 and cubic become executable; gauge cascades and several sealed comparisons expose specific failures | B882/B904, B884/B970; B915/B925/B926 |
| Late August: an apparent wall reopens | nonabelian holonomies evade a toral rank-preservation argument; exact landings, carrier and Yukawa tensors are constructed | `61499dfe`, `bbc2eaec`; B1098–B1102, B1148–B1150 |
| September: audit of the audit | wrong isometry tests, mislabeled curves, missing certificates, overbroad readings and dropped positive results are corrected; the retrieval system itself is repaired | `52010c9e`, `db523d5b`, `aae1a31c`, `f06d3405`; B1235–B1247 |

The program repeatedly advances by finding that a negative answered a narrower
question than a later summary implied. It also advances by withdrawing exciting
identifications when the actual maps fail. Neither pattern licenses accepting
the next positive or negative without opening its computation.

One particularly important existing result is on another fetched branch:
the physical-seat journey at `d5999b5f` already studies trinification matching.
Its Step 8 assumes D-parity and a spectrum, infers an intermediate scale from
low-energy couplings, and with its chosen upper-stage beta coefficients finds
a formal later crossing above the Planck scale. This is **prior work**, not a
new idea supplied by this audit. A subgroup name does not fix those coefficients
or thresholds. [Pinned source](https://github.com/originaxiom/origin-axiom/blob/d5999b5f2be484abcbd3a697c178b91bab18d566/reports/fresh_physics_seat_2026-09-01/THE_WHOLE_JOURNEY.md).

## 3. Assets and walls, with their scopes kept together

| area | what should be retained | what it does not yet establish |
|---|---|---|
| seed and genesis | exact trace-3/golden-spectrum algebra; conditional selection theorem; 23 focused core tests pass | the axioms' physical necessity, a measured clock or spacetime metric |
| exceptional algebra | explicit rational E6 representation machinery, 27, invariant cubic; the full heavy carrier batch reproduces | a spacetime gauge bundle, positive physical Hilbert space, or measured interaction strengths merely from the algebra's name |
| rank reduction | B1098's nonabelian A2 triple has centralizer dimension 16, checked live; the toral rank wall is not universal | A2's hypercharge histogram is not an SM product representation; B1102 locates a color-commutation obstruction |
| another landing | B1236 banks SM-shaped multiplet compatibility in the minimal-A1/SU6 stratum | its physical selection, extra-U(1) breaking, physical chirality, three generations or Lorentz spin are not earned by compatibility alone |
| Higgs/exotics | B884 and B970 contain doublets/triplets, the cubic and the S mass direction; the exotics were never simply unstudied | choosing light scalars and heavy fermions, a stable VEV and realistic mass matrices still costs dynamics/inputs |
| carrier/Yukawa | B1148's 54-dimensional pi1-module, 24/30 grading, beat covariance, cubic and selection rules reproduce | the corrected wording is semilinear, not automatically antiunitary; the internal-to-physical-spin map remains I-10/I-11 |
| family structure | B1150 gives a specific E8 possibility-space family tensor; the cubic factor is retained | E8/family multiplicity and physical statistics are not derived just by displaying three copies; no realistic flavor spectrum follows without further work |
| dynamics | B6 already supplies a **chosen-kinetic** scalar lift; B183/B187 and B496/B497/B766 contain dynamical/irreversible structures | B1157's narrow analytic-torsion assessment is not a universal proof of no dynamics; conversely a discrete map is not automatically a physical propagator |
| gravity | hyperbolic geometry, action/state-integral work, and B1242's exact principal embedding index 156 are genuine assets | E6 CS **contains** the SL2 gravitational sector; it is not identical to pure 3d gravity, and that is not yet a derivation of our 4d gravity-plus-matter theory |
| scale and CP | the dimensionless sigma anchor and the theta/theta-bar distinction are explicitly recognized in current ledgers | setting a curvature radius to one does not determine a dimensionless gravitational coupling; theta=0 alone does not fix theta-bar without the Yukawa phase |

This table contains different evidence grades. B1098 and the core tests were
run explicitly here; the heavy batches reproduce original certificates, not
independent new constructions. B1242's numerical/mathematical reproducer passed
in the baseline suite. Other rows are source-audited descriptions of the bank,
not a claim that every theorem in those arcs has been independently reproved.

B1247's recovery of B6 and the four-stratum monoid is particularly relevant
to the requested goal. Those are possible ingredients to connect to physical
observables, not missing objects to reinvent. The same latest record also
checks that both LR and RL have a stable vacuum: stability alone does not
dynamically pay A7. Neither result cancels the other.

## 4. New finding: the crossing solver was not solving the crossing

The original `frontier/B915_the_crossing/crossing.py` first solves `x1=x2`
while holding `alpha_s=0.118`, then changes alpha_s to solve `x2=x3` without
resolving the first equation. At two loops, the first equation depends on the
third coupling through the off-diagonal beta matrix. This is not an inert
initial guess: changing 0.118 to 0.09 or 0.15 changes the final curve.

R1 executed the original definitions without running their output-overwriting
top-level scan, reproduced all 16 finite archived two-loop points exactly,
and checked their final endpoints with another integration method.

| check | result |
|---|---:|
| maximum original UV equation residual | 0.02683971597 in inverse-coupling units |
| maximum endpoint change after tighter integration | 3.10e-11 |
| maximum corrected UV residual | 1.04e-10 |
| maximum independent upward/downward solver disagreement | 8.95e-12 in the two IR observables |

The corrected forward solver runs down from **one common UV coupling**, solving
only the electromagnetic normalization. An independent upward solve solves
**both** UV equations simultaneously. One-loop closed-form checks, changed
initial guesses, deliberately nonmeeting points and coupling-pole controls
make these tests able to fail. The original seals and outputs are unchanged.

The corrected 61-point grid gives a minimum historical distance about 16.485;
61- and 181-point grids with local bounded refinement agree on a lowest found
value **16.11621136**, near `MU=1.32524e13 GeV`. Thus the original `d<=3`
criterion is still not met in this recomputation. A dense grid plus local
refinement is not a certified global optimization theorem.

Important limitations:

1. The original executable restricts `sin²theta` to `[0.18,0.30]` and alpha_s
   to `[0.06,0.30]`. Only 15 of the 61 corrected comparison points satisfy
   both loops' root-box constraints. The other 46 are explicitly recorded,
   not silently converted into physics failures. The broad advertised scale
   interval was not a uniformly covered physical domain.
2. The matrix is the **gauge-only** two-loop truncation, not the full two-loop
   SM with Yukawa contributions. The latter are explicit in the primary RGE
   equations. [Bhattacherjee et al., Eq. (2.12)](https://doi.org/10.1007/JHEP05(2018)090).
3. The absolute one-/two-loop difference is an ad hoc truncation diagnostic,
   not a calibrated Gaussian error distribution. Correlations and the stored
   EM-input uncertainty are not propagated by the legacy metric. Neither
   its old 15.97 nor the corrected 16.116 is an established exclusion in sigma.
4. B1245's **group-independence under the shared embedding and desert** survives:
   no choice of simple group enters this executable calculation. Its argument
   list/string scan did not, however, certify numerical boundary residuals or
   prove there was no hidden comparison-data dependency.

The correct disposition is **instrument corrected; scoped mismatch retained;
global program kill not licensed**. R2 then changes a physical assumption—the
spectrum/thresholds—with that change declared, rather than claiming the old
model secretly succeeded.

## 5. New physical work and what it buys

`spectrum.py` derives the exact SM and exotic coefficients from representations
and statistics. `gauge_running.py` supplies checked boundary evolution and
explicit threshold events. `mass_match.py` adds exact mass-space constraints,
mass anomalous dimensions, analytic integrals and independent quadrature.

The resulting inverse condition is
`sum log(M_D/M_L)=43.4476952316`, with `MU=5.0775880e13 GeV`, for the archived
target and declared one-loop spectrum. Two and three exotic copies admit
explicit positive witnesses; one does not within the allowed mass interval.
This is **inverse matching using all three couplings**, not a prediction.

The next possible false kill was checked explicitly: a common UV mass can
split under gauge running. R3 includes that effect and bounds its entire
allowed threshold range. Its largest three-copy log-splitting bound is
6.1739004, below the required 43.4476952. Thus a common UV mass with **only
gauge mass running in this spectrum** cannot explain the witness. Additional
breaking/mixing/interactions remain live choices. This is a constraint on a
specified physical mechanism, not a claim that E6 cannot supply masses.

The executable bridge now tells a proposed mass-generating mechanism exactly
what it must calculate. The effective action and every imported assumption
are given in [PHYSICAL_MODEL.md](PHYSICAL_MODEL.md), including the physical
checks still required before calling any fitted example viable.

## 6. Verification and evidence loss

Baseline command, in a separate worktree at the pinned SHA:

```text
python3.12 -m pytest tests/ -q -p no:randomly
5 failed, 5993 passed, 60 skipped, 1 warning in 3943.22s (1:05:43)
```

The baseline worktree remained git-clean after the suite. The warning is the
review counter; the September 5 open-items document already identifies that
counter's stale-anchor issue. It is not a failed mathematical test.
[Completion output](BASELINE_TEST_OUTPUT.txt) is retained.

| failed baseline test area | what failed, as opposed to what was not checked |
|---|---|
| B1062 | a test reads five absent historical `.log` files; it never reaches their asserted contents |
| B1063 | a test reads the absent `refresh_windows.log`; the recorded window verdict is not independently recovered by that test |
| B1137 | the aggregate cannot open `real_grid.jsonl`; the null grid is also missing, so the claimed committed-grid reproduction cannot run |
| B1242 | the mathematics reproducer passes, but promised correction addenda beside B675/B715 are absent |
| B646 | eight packet logs and one cached bytecode file are missing against the as-received SHA-256 manifest |

The precise paths, expected packet hashes, fresh fetched refs, ignore rules
and reachable-history search are recorded in
[missing_evidence_inventory.json](missing_evidence_inventory.json).
The inventory's quantifier is exact paths/basenames in this fetched Git
history—not all private workspaces or original external uploads. All 19 paths
were absent from the worktree and had no exact-path history or basename hit
in the reachable object listing. Seventeen match ignore rules (`*.log`,
`*.jsonl`, or cached bytecode); the two addenda do not. The original archives
or generating workspaces may still hold the evidence: that is not checked here.
Do not manufacture historic logs from the assertions that expected to read them.

The two B1242 addenda have now been written from its already-reproduced
computation, explicitly dated as new September 5 text—not fabricated recovery
of September 3 files. The other four baseline evidence-failure areas remain
unrepaired. Their originals or a separately identified fresh reproduction are
needed; a cached-bytecode entry also needs a conscious archival policy decision.

Separate checks completed in this audit:

- core algebra/conditional uniqueness/Möbius tests: **23 passed**;
- the five complete heavy reproduction batches: **5 passed**, 306.78 s;
- the new gauge/threshold tests, mass checks, legacy-defect checks and repaired
  B1098 witness: **27 passed** before the added serialization regression;
- mass and legacy tests after that regression: **12 passed**;
- final new gauge, mass and legacy files: **26 passed**, 2.00 s;
- after correcting the new law-index source pointers, the unchanged repo gates
  with the B1242/B1245 checks: **13 passed, 1 warning**, 79.53 s.

The first post-edit wider focused run was **67 passed, 1 failed**: the failure
was that law-index provenance gate, not a numerical assertion. The corrected
checks above do not amount to a second full-suite run. A separate rerun of the
four unrepaired evidence areas was **4 failed, 11 passed, 1 skipped**.

**Staged-tree qualification:** staging the new inventory made the attribution
gate reach three literal upstream branch names containing vendor tokens.
The staged result was **29 gates passed, 1 failed**. The raw source names and
hash are preserved; the gate was not weakened. This local draft has not been
pushed and is not a publication-ready green certificate. See FAILURES.md.

The original B1098 live test skipped unless given a certificate path and then
failed with missing `__file__` when the vendored source was supplied. Its
loader now uses the committed closure and real filename; the triple relations
and dimension-16 assertion were not weakened. R3 also had a failed output
serialization, explicitly retained and repaired before a differently named
rerun. See [FAILURES.md](FAILURES.md). A successful equation test did not prevent
an output-format bug; both kinds of verification matter.

These numbers are not an assertion that 5,993 scientific interpretations were
proved. Some tests re-run calculations, others check tables, strings or file
presence; optional tests remain skipped. The census of labels likewise counts
labels, not independently established physical consequences.

## 7. Coverage and what remains to earn

The governance/grounding documents, framework and ladder, current open-items,
claim/identification/theorem ledgers, generated coverage, selected early and
latest progress entries, relevant original code and tests, and targeted history
were used. Detailed reads followed the crossing, particle content, nonabelian
landings, carrier/Yukawa, dynamics-null, recent correction and retrieval chains.
Seven unique remote branch heads were available; searches were broader than
the detailed reading. No claim is made to have read all 1,156 FINDINGS bodies
or all 13,000-plus progress-log lines, or independently checked every proof.

There is **no global absence claim** for a propagator, Ward identity, S-matrix,
physical mass law, or quantum-gravity completion. The kinetic term in B6 and
the recovered monoid already disprove a careless blanket absence of dynamics.
The extant candidate constructions must be tested against these obligations:

1. **An actual field interpretation:** connect the internal carrier and beat
   to physical spin/locality, with its assumptions exposed (I-10/I-11/I-13).
2. **A dynamical realization:** specify the action, kinetic normalization,
   vacuum and masses; derive the realized low-energy spectrum, not only its
   representation compatibility. The §5 threshold target is one immediate test.
3. **Physical gravity:** show the applicable continuum/semiclassical limit
   and its matter coupling. Preserve the 3d CS/state-integral results without
   identifying them with an already-complete 4d TOE.
4. **Predictions:** freeze the input budget and the mapping to observables,
   then test something not used to choose that mapping or fit its masses.
   Flavor, neutrino/cosmological parameters and precision constraints cannot
   be supplied by renaming structural invariants.
5. **Durable evidence:** the live result must resolve to runnable code and
   recoverable inputs on a clean clone. A string saying REPRODUCES is not that.

The actionable next step is a **specific mass/VEV/mixing mechanism feeding
the new threshold interface**, while retaining the existing dynamics and
spacetime leads. This is a research route with tests that can pass or fail.
Neither a complete TOE nor its impossibility has been established here.
