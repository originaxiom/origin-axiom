# G5 — THE LITERAL-FLAG ENUMERATION (S3a §1a follow-up; full scan, full tracing)

Cell: `reports/fresh_physics_seat_2026-09-01/internalization/G5_flag_enumeration/`.
Date: 2026-09-01. All paths repo-relative to `/home/user/origin-axiom`.

This is enumeration + tracing, not judgment of the underlying mathematics. Every flag below was
traced to its assignment line in the frontier module the test actually imports (all these tests
load the module by `importlib.util.spec_from_file_location` on an explicit `frontier/.../*.py`
path; resolution was done by parsing that pattern, and every one of the 245 flag tokens
resolved to a definition line — 0 unresolved).

## 0. The scan, stated exactly

Population: all of `tests/` (every `.py` file). An assert line is in the MAIN class when its
body (strings and comments stripped) consists solely of `<mod>.<ALL_CAPS>` attribute tokens
joined by `and`/`or`/`not` — i.e. `assert <mod>.<ALL_CAPS>` with **no comparison operator**, the
S3a §1a scan. Recorded separately, because it is the same mechanism one comparison away:
the **supplementary class** `assert <mod>.<ALL_CAPS> is True/False`.

Headline numbers:

| quantity | count |
|---|---|
| test files with main-class flag asserts | **44** |
| main-class flag **tokens** (a line `assert A and B` = 2 tokens) | **187** |
| supplementary `is True/False` tokens | **58** |
| total flag tokens traced | **245** |
| flag-assert **lines** across the 44 files | 231 (173 main + 58 supp) |
| total assert lines in those 44 files | 438 |

Per-token classification (main + supplementary, all 245):

| class | tokens | share |
|---|---|---|
| LITERAL (hand-written `True`/`False` at the definition) | **243** | 99.2% |
| — of which LITERAL-VERDICT | 57 | 23.3% |
| — of which LITERAL-RECORD | 186 | 75.9% |
| COMPUTED (assigned from a computation) | **2** | 0.8% |

The **2 computed flags** in the entire population:
- `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:74` —
  `ONLY_E6_IS_CHIRAL_CAPABLE = (chiral_capable("E6") and not chiral_capable("E7") and not chiral_capable("E8"))`
- `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:56` —
  `IMAGINARY_LADDER_FLOORS_AT_MINUS_4 = (imaginary_unimodular_discs() == [-4, -3])`

Both are first declared `= None  # set below` in the same constants block as their literal
siblings and re-assigned from a function call a few lines later — evidence the authors knew how
to wire a flag and did so for exactly two of 245.

## 1. Class definitions used (stated so the adjudicator can re-bucket)

- **LITERAL-VERDICT (LV)**: the flag asserts a first-order, computation-decidable mathematical
  proposition (a rep decomposition, a rank, a torsion statement, a p-value threshold, an
  eigenvalue list…), and the definition is a hand-written `True`/`False` with at most a comment
  citing a computation done elsewhere (Sage, SnapPy, sympy) that the lock does not run.
  **Vacuous as a lock**: flipping the cited math moves nothing; only editing the literal does.
- **LITERAL-RECORD (LR)**: the flag encodes a sealed adjudication or reading — scoping
  ("…IS_EXTERNAL", "…IS_STOP_GATE", "…IS_LEAP/HOOK"), attribution ("CHAT1_…OVERCLAIMED",
  "CHAT2_OBSTRUCTION_REFUTED"), banking/status ("STEP3_BANKED_AS_H36", "P010_UNRUN_CLAIM_IS_STALE",
  "B176_FULLY_RESOLVED"), literature citations (Mostow/Gordon–Luecke, Lisovyy–Tykhyy), and the
  firewall family (`DERIVES_SM_VALUES = False` et al.). Per the repo's own E53 row #8
  (`docs/ERROR_LEDGER.md:84`): *"An audit cell that hardcodes what it audited is a record of a
  reading, not an instrument, and must never be re-run as one."* These are records, not locks.
- **COMPUTED**: the definition's RHS is a computation in the module.
- **MIXED** (per FILE): the file contains both flag asserts and other asserts. **All 44 files are
  MIXED** — none consists solely of flag asserts; per-file vacuous fractions are in the table.

Borderline calls: the LV/LR boundary is a judgment on flag-name + comment semantics; ~10 tokens
could defensibly move across it (e.g. `YUKAWA_COUPLING_FORCED` LV↔LR, `C3_CUBICS_ARE_TOTALLY_REAL`
put in LR as a Galois-theory theorem-citation). Moving all of them changes the LV/LR split, not
the 243-literal total, which is the load-bearing number.

## 2. Reconciliation with S3a §1a's "60 files"

S3a's list (60) and this cell's list (44) differ because S3a's grep net was wider than its own
stated scan. The 18 files on S3a's list but **not** here — `test_audit_sample, b253, b257, b258,
b262, b263, b271, b273, b275, b276, b284, b285, b351, b452, b807, b811, b822, b977` — were
re-inspected: **every ALL-CAPS assert in them carries a comparison operator** (`== <literal>`,
`is True/False` in compound form, `<`, or subscripted dicts), e.g.
`tests/test_b253_chirality_capability.py:15` (`== {...}`), `tests/test_b285_commutator_phase.py:31`
(`is False and … is True`), `tests/test_b275_witness.py:19` (`WITNESS["exp4_nonzero"]`, a dict
constant). Those are the ADJACENT class — data-pins against hand-written module constants — real,
but outside this cell's remit (S3b/E40-flavored, not the bare-flag form). Conversely
**2 files are here that S3a's list missed**: `test_b280_2T_higher_spin.py` and
`test_b283_selfgen_scoping.py` (both inside the a-l range S3a covered).

S3a's caveat (ii) — "some ALL-CAPS asserts may trace to computed module values (spot-checked 3
of 60)" — is now settled: of 245 traced, exactly 2 are computed (B315, B316 above), and the two
apparent exceptions (`b294.*`, `b295.*`, RHS `= sv.X` / `= ssb.X`) are one-hop re-exports of
hand-written literals in `frontier/B294_selection_verdict/selection_verdict.py:74-78` and
`frontier/B295_ssb_gauge_status/ssb_gauge.py:66-71`.

## 3. What genuinely computed asserts coexist (the MB12 side)

Every one of the 44 files also contains non-flag asserts (207 lines total), and in the files
spot-read these are substantially real: `test_b322…:22` runs `b322.null_test()` (2000-draw null)
and checks `p_value > 0.05`; `test_b304…:16` computes `sin2_theta_w() == F(3,8)`;
`test_b324…:17-23` runs `g_cubed_is_identity()`, `eigenvalue_magnitudes_squared() == [1,1,52]`;
`test_b307…:16-28` runs `five2_is_S3()`, `c3_samples_totally_real()`. Also, 49 of these asserts
are `assert <mod>.verdict()`, and the `verdict()` functions typically AND computed checks with
the same literals (e.g. B316's `verdict()` calls `neg7_passes_congruence()` and
`neg7_below_floor()` — so two of B316's literal flags are literal DUPLICATES of facts the same
module computes a few lines away). Caveat: a minority of "other" asserts are themselves pins
against hand-written module constants (e.g. `tests/test_b301…:14` compares to a hand-typed set),
so 207 is an upper bound on the genuinely-computed complement; no per-line audit of the 207 was
done.

## 4. THE HONEST BOTTOM LINE

- **44 banked lock files** in `tests/` assert imported ALL-CAPS module flags with no comparison
  operator; **231 of their 438 assert lines (53%) are flag asserts, and 243 of the 245 flag
  tokens (99.2%) trace to hand-written `True`/`False` literals.** As LOCKS those asserts are
  vacuous: no edit to any computation anywhere can fail them; only editing the literal itself can.
- **No file is wholly vacuous** — all 44 are MIXED, each carrying real computed asserts alongside;
  the flag layer is the vacuous fraction (per-file range: roughly a third to three-quarters of
  the file's assert lines).
- By this cell's (re-bucketable) split: **57 tokens are LITERAL-VERDICT** — computation-decidable
  math claims standing as hand-written literals; this is the E27-shaped fraction where a real
  lock was available and not wired (in at least B316 and B324 the very computation exists in the
  same module, unwired to the flag). **186 tokens are LITERAL-RECORD** — sealed
  adjudication/scoping/firewall readings for which a constant is arguably the honest
  representation, but which then, by the repo's own E53 row #8, are records and "must never be
  re-run as" locks. **2 are COMPUTED** (real locks).
- Concentration: the 2026-06 B252–B325 stratum accounts for all 44 files (B252, B279–B325 minus
  gaps). The suite's own vacuity gate (`scripts/checks/check_test_vacuity.py`, enforced at
  `scripts/gates/gates.py:515`) scans the TEST file's AST only, so all 44 pass it: the literal
  lives one import away.

## 5. Full classification table

Format per file header: flag-assert lines / total assert lines; token classes
(LV = LITERAL-VERDICT, LR = LITERAL-RECORD, C = COMPUTED); count of other (non-flag) asserts.
Evidence = the definition line in the imported frontier module (file:line) and its RHS with
comment stripped. `[is-bool form]` marks the supplementary `is True/False` asserts.

### `tests/test_b252_chirality_obstruction.py` — MIXED (flag-assert lines 2/8 of assert lines; tokens: LV=3 LR=1 C=0; other asserts: 6)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 33 | `E6_27_IS_COMPLEX` | LITERAL-VERDICT | `frontier/B252_chirality_obstruction/chirality_obstruction.py:52` | `E6_27_IS_COMPLEX = True` |
| 33 | `E6_78_IS_REAL` | LITERAL-VERDICT | `frontier/B252_chirality_obstruction/chirality_obstruction.py:53` | `E6_78_IS_REAL = True` |
| 33 | `E8_DECOMP_PAIRS_27` | LITERAL-VERDICT | `frontier/B252_chirality_obstruction/chirality_obstruction.py:54` | `E8_DECOMP_PAIRS_27 = True` |
| 34 | `STEP3_BANKED_AS_H36` | LITERAL-RECORD | `frontier/B252_chirality_obstruction/chirality_obstruction.py:55` | `STEP3_BANKED_AS_H36 = True` |

### `tests/test_b279_spin_structure_bit.py` — MIXED (flag-assert lines 2/5 of assert lines; tokens: LV=1 LR=2 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 19 | `HOMOLOGICAL_ACTION_TRIVIAL` | LITERAL-VERDICT | `frontier/B279_spin_structure_bit/spin_bit_verdict.py:11` | `HOMOLOGICAL_ACTION_TRIVIAL = True` |
| 19 | `IS_AMBIENT` | LITERAL-RECORD | `frontier/B279_spin_structure_bit/spin_bit_verdict.py:10` | `IS_AMBIENT = True` |
| 24 [is-bool form] | `PHYSICS_LINK_VERIFIED` | LITERAL-RECORD | `frontier/B279_spin_structure_bit/spin_bit_verdict.py:17` | `PHYSICS_LINK_VERIFIED = False` |

### `tests/test_b280_2T_higher_spin.py` — MIXED (flag-assert lines 1/6 of assert lines; tokens: LV=1 LR=0 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 22 | `THREE_GENERATIONS_FROM_SPIN32` | LITERAL-VERDICT | `frontier/B280_2T_higher_spin/spin_content_verdict.py:11` | `THREE_GENERATIONS_FROM_SPIN32 = False` |

### `tests/test_b281_crux_scoping.py` — MIXED (flag-assert lines 3/5 of assert lines; tokens: LV=2 LR=1 C=0; other asserts: 2)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 15 | `EVERY_TYPE_GIVES_RANK` | LITERAL-VERDICT | `frontier/B281_crux_scoping/crux_verdict.py:8` | `EVERY_TYPE_GIVES_RANK = True` |
| 16 | `EVERY_TYPE_HAS_DENSE_DIRECTIONS` | LITERAL-VERDICT | `frontier/B281_crux_scoping/crux_verdict.py:12` | `EVERY_TYPE_HAS_DENSE_DIRECTIONS = True` |
| 20 | `SETTLEABLE_IN_SANDBOX` | LITERAL-RECORD | `frontier/B281_crux_scoping/crux_verdict.py:31` | `SETTLEABLE_IN_SANDBOX = False` |

### `tests/test_b283_selfgen_scoping.py` — MIXED (flag-assert lines 2/6 of assert lines; tokens: LV=0 LR=2 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 15 | `METALLIC_IS_SPECIAL` | LITERAL-RECORD | `frontier/B283_selfgen_scoping/verdict.py:24` | `METALLIC_IS_SPECIAL = False` |
| 16 | `OBJECT_SPECIFIC_NOVEL_SIGNAL` | LITERAL-RECORD | `frontier/B283_selfgen_scoping/verdict.py:25` | `OBJECT_SPECIFIC_NOVEL_SIGNAL = False` |

### `tests/test_b286_the_seam.py` — MIXED (flag-assert lines 2/6 of assert lines; tokens: LV=0 LR=2 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT` | LITERAL-RECORD | `frontier/B286_the_seam/verdict.py:30` | `WALL_IS_AT_THE_CLOSURE_NOT_THE_OBJECT = True` |
| 24 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B286_the_seam/verdict.py:35` | `DERIVES_SM_VALUES = False` |

### `tests/test_b287_distinguished_closing.py` — MIXED (flag-assert lines 3/9 of assert lines; tokens: LV=1 LR=2 C=0; other asserts: 6)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 22 | `DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE` | LITERAL-VERDICT | `frontier/B287_distinguished_closing/verdict.py:42` | `DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE = True` |
| 35 | `SELECTIVE_FOR_OWN_STRUCTURE` | LITERAL-RECORD | `frontier/B287_distinguished_closing/verdict.py:45` | `SELECTIVE_FOR_OWN_STRUCTURE = True` |
| 36 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B287_distinguished_closing/verdict.py:46` | `DERIVES_SM_VALUES = False` |

### `tests/test_b288_arithmetic_filling_census.py` — MIXED (flag-assert lines 4/9 of assert lines; tokens: LV=1 LR=3 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 16 | `CUSPED_RESEES_SQRT_NEG3` | LITERAL-VERDICT | `frontier/B288_arithmetic_filling_census/verdict.py:21` | `CUSPED_RESEES_SQRT_NEG3 = True` |
| 31 | `E6_IS_OPEN_OBJECT_PROPERTY` | LITERAL-RECORD | `frontier/B288_arithmetic_filling_census/verdict.py:40` | `E6_IS_OPEN_OBJECT_PROPERTY = True` |
| 32 | `CRUX_LEANS_CATALOGUE` | LITERAL-RECORD | `frontier/B288_arithmetic_filling_census/verdict.py:41` | `CRUX_LEANS_CATALOGUE = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B288_arithmetic_filling_census/verdict.py:42` | `DERIVES_SM_VALUES = False` |

### `tests/test_b289_cp_sign_law.py` — MIXED (flag-assert lines 3/11 of assert lines; tokens: LV=0 LR=3 C=0; other asserts: 8)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 30 | `HANDEDNESS_IS_GALOIS_CONJUGATION` | LITERAL-RECORD | `frontier/B289_cp_sign_law/verdict.py:32` | `HANDEDNESS_IS_GALOIS_CONJUGATION = True` |
| 34 [is-bool form] | `SIGN_IS_OBJECT_DERIVABLE` | LITERAL-RECORD | `frontier/B289_cp_sign_law/verdict.py:33` | `SIGN_IS_OBJECT_DERIVABLE = False` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B289_cp_sign_law/verdict.py:34` | `DERIVES_SM_VALUES = False` |

### `tests/test_b290_core_scale_ladder.py` — MIXED (flag-assert lines 5/10 of assert lines; tokens: LV=1 LR=4 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `NZ_CUSP_SHAPE_CONTROLLED` | LITERAL-VERDICT | `frontier/B290_core_scale_ladder/verdict.py:22` | `NZ_CUSP_SHAPE_CONTROLLED = True` |
| 27 | `FILLING_N_IS_TOPOLOGICAL` | LITERAL-RECORD | `frontier/B290_core_scale_ladder/verdict.py:25` | `FILLING_N_IS_TOPOLOGICAL = True` |
| 28 | `WRT_LEVEL_K_IS_QUANTUM` | LITERAL-RECORD | `frontier/B290_core_scale_ladder/verdict.py:26` | `WRT_LEVEL_K_IS_QUANTUM = True` |
| 29 [is-bool form] | `N_EQUALS_K` | LITERAL-RECORD | `frontier/B290_core_scale_ladder/verdict.py:27` | `N_EQUALS_K = False` |
| 34 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B290_core_scale_ladder/verdict.py:31` | `DERIVES_SM_VALUES = False` |

### `tests/test_b291_scale_extremal.py` — MIXED (flag-assert lines 5/9 of assert lines; tokens: LV=4 LR=2 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 15 | `TRIANGULATION_STABLE` | LITERAL-VERDICT | `frontier/B291_scale_extremal/verdict.py:23` | `TRIANGULATION_STABLE = True` |
| 15 | `TWO_METHODS_AGREE` | LITERAL-VERDICT | `frontier/B291_scale_extremal/verdict.py:22` | `TWO_METHODS_AGREE = True` |
| 23 [is-bool form] | `SCALE_AXIS_COINCIDES_WITH_FIBER` | LITERAL-VERDICT | `frontier/B291_scale_extremal/verdict.py:28` | `SCALE_AXIS_COINCIDES_WITH_FIBER = False` |
| 24 [is-bool form] | `SCALE_AXIS_COINCIDES_WITH_ARITHMETIC` | LITERAL-VERDICT | `frontier/B291_scale_extremal/verdict.py:29` | `SCALE_AXIS_COINCIDES_WITH_ARITHMETIC = False` |
| 25 | `AXIS_STRATIFIED` | LITERAL-RECORD | `frontier/B291_scale_extremal/verdict.py:30` | `AXIS_STRATIFIED = True` |
| 30 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B291_scale_extremal/verdict.py:31` | `DERIVES_SM_VALUES = False` |

### `tests/test_b292_multiplicity_2manifold.py` — MIXED (flag-assert lines 6/11 of assert lines; tokens: LV=0 LR=7 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 16 | `FIBER_IS_THE_2MANIFOLD` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:19` | `FIBER_IS_THE_2MANIFOLD = True` |
| 23 | `FILLINGS_IS_3MFLD_SEQUENCE` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:28` | `FILLINGS_IS_3MFLD_SEQUENCE = True` |
| 23 | `TOWER_IS_3MFLD_SEQUENCE` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:25` | `TOWER_IS_3MFLD_SEQUENCE = True` |
| 27 | `MULTIPLICITY_TRIPARTITE` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:31` | `MULTIPLICITY_TRIPARTITE = True` |
| 28 [is-bool form] | `CHIRAL_DATUM_SUPPLIED` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:32` | `CHIRAL_DATUM_SUPPLIED = False` |
| 32 | `CHIRAL_4D_SM_IS_STOP_GATE` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:33` | `CHIRAL_4D_SM_IS_STOP_GATE = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B292_multiplicity_2manifold/verdict.py:34` | `DERIVES_SM_VALUES = False` |

### `tests/test_b293_peripheral_clock.py` — MIXED (flag-assert lines 6/10 of assert lines; tokens: LV=1 LR=5 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `NZ_SYMPLECTIC_OK` | LITERAL-VERDICT | `frontier/B293_peripheral_clock/verdict.py:27` | `NZ_SYMPLECTIC_OK = True` |
| 28 | `CLOCK_IS_PERIPHERAL_SYMPLECTIC` | LITERAL-RECORD | `frontier/B293_peripheral_clock/verdict.py:29` | `CLOCK_IS_PERIPHERAL_SYMPLECTIC = True` |
| 29 | `FILLING_IS_A_POLARIZATION` | LITERAL-RECORD | `frontier/B293_peripheral_clock/verdict.py:30` | `FILLING_IS_A_POLARIZATION = True` |
| 33 | `K_OF_T_TRAJECTORY_IS_STOP_GATE` | LITERAL-RECORD | `frontier/B293_peripheral_clock/verdict.py:34` | `K_OF_T_TRAJECTORY_IS_STOP_GATE = True` |
| 34 | `DYNAMICAL_GAUGE_FIXING_SHARED_B295` | LITERAL-RECORD | `frontier/B293_peripheral_clock/verdict.py:35` | `DYNAMICAL_GAUGE_FIXING_SHARED_B295 = True` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B293_peripheral_clock/verdict.py:36` | `DERIVES_SM_VALUES = False` |

### `tests/test_b294_selection_verdict.py` — MIXED (flag-assert lines 5/9 of assert lines; tokens: LV=0 LR=5 C=0; other asserts: 4)

Flags re-exported one hop: frontier/B294_selection_verdict/selection_verdict.py:74-78 (all `= True/False` literals).

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 20 | `SELECTIVE_FOR_OWN_STRUCTURE` | LITERAL-RECORD | `frontier/B294_selection_verdict/verdict.py:22` | `SELECTIVE_FOR_OWN_STRUCTURE = sv.SELECTIVE_FOR_OWN_STRUCTURE` |
| 21 | `CATALOGUE_FOR_SM_VALUES` | LITERAL-RECORD | `frontier/B294_selection_verdict/verdict.py:23` | `CATALOGUE_FOR_SM_VALUES = sv.CATALOGUE_FOR_SM_VALUES` |
| 25 | `SELECTION_IS_AXIS_STRATIFIED` | LITERAL-RECORD | `frontier/B294_selection_verdict/verdict.py:24` | `SELECTION_IS_AXIS_STRATIFIED = sv.SELECTION_IS_AXIS_STRATIFIED` |
| 30 | `STRENGTHENS_FIREWALL` | LITERAL-RECORD | `frontier/B294_selection_verdict/verdict.py:25` | `STRENGTHENS_FIREWALL = sv.STRENGTHENS_FIREWALL` |
| 31 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B294_selection_verdict/verdict.py:26` | `DERIVES_SM_VALUES = sv.DERIVES_SM_VALUES` |

### `tests/test_b295_ssb_gauge_status.py` — MIXED (flag-assert lines 6/10 of assert lines; tokens: LV=0 LR=6 C=0; other asserts: 4)

Flags re-exported one hop: frontier/B295_ssb_gauge_status/ssb_gauge.py:66-71 (all `= True/False` literals).

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 15 [is-bool form] | `CURIE_IS_A_HARD_WALL` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:27` | `CURIE_IS_A_HARD_WALL = ssb.CURIE_IS_A_HARD_WALL` |
| 25 [is-bool form] | `SSB_POTENTIAL_PRESENT` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:28` | `SSB_POTENTIAL_PRESENT = ssb.SSB_POTENTIAL_PRESENT` |
| 29 [is-bool form] | `TAU_GAUGED_IS_VERIFIED` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:29` | `TAU_GAUGED_IS_VERIFIED = ssb.TAU_GAUGED_IS_VERIFIED` |
| 34 | `SIGN_IS_EXTERNAL` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:30` | `SIGN_IS_EXTERNAL = ssb.SIGN_IS_EXTERNAL` |
| 35 [is-bool form] | `SIGN_MECHANISM_ESTABLISHED` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:31` | `SIGN_MECHANISM_ESTABLISHED = ssb.SIGN_MECHANISM_ESTABLISHED` |
| 36 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B295_ssb_gauge_status/verdict.py:32` | `DERIVES_SM_VALUES = ssb.DERIVES_SM_VALUES` |

### `tests/test_b296_seam_arc_verification.py` — MIXED (flag-assert lines 2/11 of assert lines; tokens: LV=0 LR=2 C=0; other asserts: 9)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 29 [is-bool form] | `PROGRAM_CLAIMS_MATH_AS_ORIGINAL` | LITERAL-RECORD | `frontier/B296_seam_arc_verification/verdict.py:42` | `PROGRAM_CLAIMS_MATH_AS_ORIGINAL = False` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B296_seam_arc_verification/verdict.py:44` | `DERIVES_SM_VALUES = False` |

### `tests/test_b298_generation_obstruction.py` — MIXED (flag-assert lines 3/9 of assert lines; tokens: LV=0 LR=3 C=0; other asserts: 6)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 25 [is-bool form] | `FORCES_THREE_GENERATIONS` | LITERAL-RECORD | `frontier/B298_generation_obstruction/verdict.py:27` | `FORCES_THREE_GENERATIONS = False` |
| 26 | `THREE_IS_A_VALUE_NOT_A_MULTIPLICITY` | LITERAL-RECORD | `frontier/B298_generation_obstruction/verdict.py:30` | `THREE_IS_A_VALUE_NOT_A_MULTIPLICITY = True` |
| 31 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B298_generation_obstruction/verdict.py:31` | `DERIVES_SM_VALUES = False` |

### `tests/test_b299_trinification_triality.py` — MIXED (flag-assert lines 5/10 of assert lines; tokens: LV=2 LR=3 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `IS_TRINIFICATION_TRIALITY` | LITERAL-VERDICT | `frontier/B299_trinification_triality/trinification_triality.py:99` | `IS_TRINIFICATION_TRIALITY = True` |
| 27 [is-bool form] | `H_LABEL_FROM_PHI_DERIVED` | LITERAL-VERDICT | `frontier/B299_trinification_triality/trinification_triality.py:100` | `H_LABEL_FROM_PHI_DERIVED = False` |
| 31 | `HETEROTIC_E6_IS_GENERIC` | LITERAL-RECORD | `frontier/B299_trinification_triality/trinification_triality.py:101` | `HETEROTIC_E6_IS_GENERIC = True` |
| 32 | `RIGOR_NEEDS_CLASS_S_E6` | LITERAL-RECORD | `frontier/B299_trinification_triality/trinification_triality.py:102` | `RIGOR_NEEDS_CLASS_S_E6 = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B299_trinification_triality/trinification_triality.py:103` | `DERIVES_SM_VALUES = False` |

### `tests/test_b300_cross_chat_sm_attempt.py` — MIXED (flag-assert lines 3/9 of assert lines; tokens: LV=0 LR=3 C=0; other asserts: 6)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 28 | `SEATS_CONVERGE_ON_STRUCTURAL_THEOREM` | LITERAL-RECORD | `frontier/B300_cross_chat_sm_attempt/cross_chat_sm_attempt.py:46` | `SEATS_CONVERGE_ON_STRUCTURAL_THEOREM = True` |
| 29 | `LIVE_FORCING_TRIPLE_CONVERGENT` | LITERAL-RECORD | `frontier/B300_cross_chat_sm_attempt/cross_chat_sm_attempt.py:64` | `LIVE_FORCING_TRIPLE_CONVERGENT = True` |
| 30 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B300_cross_chat_sm_attempt/cross_chat_sm_attempt.py:65` | `DERIVES_SM_VALUES = False` |

### `tests/test_b301_chirality_filter_and_convergence.py` — MIXED (flag-assert lines 6/9 of assert lines; tokens: LV=1 LR=5 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 13 | `TWENTYSEVEN_IS_COMPLEX` | LITERAL-VERDICT | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:30` | `TWENTYSEVEN_IS_COMPLEX = True` |
| 15 [is-bool form] | `STABILITY_FORCES_SO10` | LITERAL-RECORD | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:33` | `STABILITY_FORCES_SO10 = False` |
| 16 | `CHIRALITY_IS_A_PHYSICS_SELECTION_PRINCIPLE` | LITERAL-RECORD | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:34` | `CHIRALITY_IS_A_PHYSICS_SELECTION_PRINCIPLE = True` |
| 20 | `SU3CUBED_IS_THE_THETA_PHI_TRIALITY` | LITERAL-RECORD | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:37` | `SU3CUBED_IS_THE_THETA_PHI_TRIALITY = True` |
| 25 | `BOUNDARY_IS_REAL_FOUND_THREE_WAYS` | LITERAL-RECORD | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:42` | `BOUNDARY_IS_REAL_FOUND_THREE_WAYS = True` |
| 29 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B301_chirality_filter_and_convergence/chirality_filter.py:43` | `DERIVES_SM_VALUES = False` |

### `tests/test_b302_multiplicity_hidden_z3.py` — MIXED (flag-assert lines 5/10 of assert lines; tokens: LV=2 LR=3 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `KNOT_GROUP_TORSION_FREE` | LITERAL-VERDICT | `frontier/B302_multiplicity_hidden_z3/verdict.py:19` | `KNOT_GROUP_TORSION_FREE = True` |
| 23 | `COMMENSURATOR_HAS_ORDER3` | LITERAL-VERDICT | `frontier/B302_multiplicity_hidden_z3/verdict.py:23` | `COMMENSURATOR_HAS_ORDER3 = True` |
| 31 | `GENERATION_Z3_IS_HIDDEN_SYMMETRY` | LITERAL-RECORD | `frontier/B302_multiplicity_hidden_z3/verdict.py:31` | `GENERATION_Z3_IS_HIDDEN_SYMMETRY = True` |
| 32 | `EXPLAINS_B298` | LITERAL-RECORD | `frontier/B302_multiplicity_hidden_z3/verdict.py:32` | `EXPLAINS_B298 = True` |
| 33 [is-bool form] | `DERIVES_THREE_GENERATIONS` | LITERAL-RECORD | `frontier/B302_multiplicity_hidden_z3/verdict.py:33` | `DERIVES_THREE_GENERATIONS = False` |

### `tests/test_b303_clock_is_the_cp_sign.py` — MIXED (flag-assert lines 6/10 of assert lines; tokens: LV=2 LR=5 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `CP_SIGN_IS_SIGN_OF_CS` | LITERAL-RECORD | `frontier/B303_clock_is_the_cp_sign/verdict.py:21` | `CP_SIGN_IS_SIGN_OF_CS = True` |
| 18 | `AMPHICHIRAL_IS_THE_CLOCK_ORIGIN` | LITERAL-RECORD | `frontier/B303_clock_is_the_cp_sign/verdict.py:22` | `AMPHICHIRAL_IS_THE_CLOCK_ORIGIN = True` |
| 23 | `B289_FLIP` | LITERAL-VERDICT | `frontier/B303_clock_is_the_cp_sign/verdict.py:24` | `B289_FLIP = True` |
| 23 | `DEFINITE_ARROW` | LITERAL-VERDICT | `frontier/B303_clock_is_the_cp_sign/verdict.py:23` | `DEFINITE_ARROW = True` |
| 28 | `CONDITIONAL_CP_SIGN_IS_INTERNAL` | LITERAL-RECORD | `frontier/B303_clock_is_the_cp_sign/verdict.py:29` | `CONDITIONAL_CP_SIGN_IS_INTERNAL = True` |
| 32 | `BARYON_MAGNITUDE_STILL_EXTERNAL` | LITERAL-RECORD | `frontier/B303_clock_is_the_cp_sign/verdict.py:30` | `BARYON_MAGNITUDE_STILL_EXTERNAL = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B303_clock_is_the_cp_sign/verdict.py:31` | `DERIVES_SM_VALUES = False` |

### `tests/test_b304_gauge_dynamics_skeleton.py` — MIXED (flag-assert lines 4/9 of assert lines; tokens: LV=1 LR=3 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 29 | `E6_HEIGHT6_ROOTS_MUTUALLY_ORTHOGONAL` | LITERAL-VERDICT | `frontier/B304_gauge_dynamics_skeleton/gauge_dynamics_skeleton.py:68` | `E6_HEIGHT6_ROOTS_MUTUALLY_ORTHOGONAL = True` |
| 30 | `SADDLE_SU3_CLAIM_REFUTED` | LITERAL-RECORD | `frontier/B304_gauge_dynamics_skeleton/gauge_dynamics_skeleton.py:70` | `SADDLE_SU3_CLAIM_REFUTED = True` |
| 31 | `GAUGE_DYNAMICS_IS_GENERIC_GUT` | LITERAL-RECORD | `frontier/B304_gauge_dynamics_skeleton/gauge_dynamics_skeleton.py:74` | `GAUGE_DYNAMICS_IS_GENERIC_GUT = True` |
| 32 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B304_gauge_dynamics_skeleton/gauge_dynamics_skeleton.py:77` | `DERIVES_SM_VALUES = False` |

### `tests/test_b305_eisenstein_trinification_grading.py` — MIXED (flag-assert lines 7/10 of assert lines; tokens: LV=3 LR=4 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `TRINIFICATION_AT_EISENSTEIN` | LITERAL-VERDICT | `frontier/B305_eisenstein_trinification_grading/verdict.py:21` | `TRINIFICATION_AT_EISENSTEIN = True` |
| 18 | `GRADING_EIGENVALUE_IS_EISENSTEIN_OMEGA` | LITERAL-VERDICT | `frontier/B305_eisenstein_trinification_grading/verdict.py:22` | `GRADING_EIGENVALUE_IS_EISENSTEIN_OMEGA = True` |
| 22 | `THETA_PHI_IS_THE_TRINIFICATION_TRIALITY` | LITERAL-RECORD | `frontier/B305_eisenstein_trinification_grading/verdict.py:23` | `THETA_PHI_IS_THE_TRINIFICATION_TRIALITY = True` |
| 28 | `SADDLE_IS_SU2_CUBED_NOT_SU3` | LITERAL-VERDICT | `frontier/B305_eisenstein_trinification_grading/verdict.py:24` | `SADDLE_IS_SU2_CUBED_NOT_SU3 = True` |
| 32 | `WHICH_SU3_IS_COLOR_IS_EXTERNAL` | LITERAL-RECORD | `frontier/B305_eisenstein_trinification_grading/verdict.py:28` | `WHICH_SU3_IS_COLOR_IS_EXTERNAL = True` |
| 33 | `DEFORMATION_AS_RG_IS_LEAP` | LITERAL-RECORD | `frontier/B305_eisenstein_trinification_grading/verdict.py:29` | `DEFORMATION_AS_RG_IS_LEAP = True` |
| 34 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B305_eisenstein_trinification_grading/verdict.py:30` | `DERIVES_SM_VALUES = False` |

### `tests/test_b306_principal_grading_cascade.py` — MIXED (flag-assert lines 7/11 of assert lines; tokens: LV=3 LR=4 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 20 | `SM_SHAPED_POINT_IS_N5` | LITERAL-VERDICT | `frontier/B306_principal_grading_cascade/verdict.py:26` | `SM_SHAPED_POINT_IS_N5 = True` |
| 22 [is-bool form] | `SM_IS_EXACT_ENDPOINT` | LITERAL-RECORD | `frontier/B306_principal_grading_cascade/verdict.py:28` | `SM_IS_EXACT_ENDPOINT = False` |
| 26 | `CHAT1_DIM14_WINDOW_MATCHES_NO_CENTRALIZER` | LITERAL-VERDICT | `frontier/B306_principal_grading_cascade/verdict.py:29` | `CHAT1_DIM14_WINDOW_MATCHES_NO_CENTRALIZER = True` |
| 27 | `SADDLE_IS_SU2_CUBED_NOT_SU3U1_4` | LITERAL-VERDICT | `frontier/B306_principal_grading_cascade/verdict.py:30` | `SADDLE_IS_SU2_CUBED_NOT_SU3U1_4 = True` |
| 31 | `CASCADE_IS_GENERIC_E6` | LITERAL-RECORD | `frontier/B306_principal_grading_cascade/verdict.py:35` | `CASCADE_IS_GENERIC_E6 = True` |
| 32 | `N5_LEVEL_COINCIDENCE_IS_LEAP` | LITERAL-RECORD | `frontier/B306_principal_grading_cascade/verdict.py:34` | `N5_LEVEL_COINCIDENCE_IS_LEAP = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B306_principal_grading_cascade/verdict.py:36` | `DERIVES_SM_VALUES = False` |

### `tests/test_b307_totally_real_obstruction.py` — MIXED (flag-assert lines 7/12 of assert lines; tokens: LV=1 LR=6 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `FIVE2_IS_S3_SPLITS_1PLUS2` | LITERAL-VERDICT | `frontier/B307_totally_real_obstruction/verdict.py:28` | `FIVE2_IS_S3_SPLITS_1PLUS2 = True` |
| 22 | `C3_CUBICS_ARE_TOTALLY_REAL` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:21` | `C3_CUBICS_ARE_TOTALLY_REAL = True` |
| 23 | `HYPERBOLIC_TRACE_FIELD_HAS_COMPLEX_PLACE` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:22` | `HYPERBOLIC_TRACE_FIELD_HAS_COMPLEX_PLACE = True` |
| 32 | `NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:23` | `NO_HYPERBOLIC_KNOT_HAS_C3_TRACE_FIELD = True` |
| 33 | `THREE_SYMMETRIC_GENERATIONS_IMPOSSIBLE_IN_ONE_KNOT` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:24` | `THREE_SYMMETRIC_GENERATIONS_IMPOSSIBLE_IN_ONE_KNOT = True` |
| 34 | `GENERATIONS_FORCED_TO_MULTIPLICITY` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:25` | `GENERATIONS_FORCED_TO_MULTIPLICITY = True` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B307_totally_real_obstruction/verdict.py:29` | `DERIVES_SM_VALUES = False` |

### `tests/test_b308_yukawa_last_redoubt.py` — MIXED (flag-assert lines 9/12 of assert lines; tokens: LV=1 LR=8 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 18 | `YUKAWA_COUPLING_FORCED` | LITERAL-VERDICT | `frontier/B308_yukawa_last_redoubt/verdict.py:18` | `YUKAWA_COUPLING_FORCED = True` |
| 22 | `CP_PHASE_PI6_IN_STATE_NOT_COUPLING` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:20` | `CP_PHASE_PI6_IN_STATE_NOT_COUPLING = True` |
| 23 | `OMEGA_TRIALITY_IS_WITHIN_27` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:21` | `OMEGA_TRIALITY_IS_WITHIN_27 = True` |
| 24 | `MB_EQ_MTAU_FORCED_BUT_GENERIC_GUT` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:19` | `MB_EQ_MTAU_FORCED_BUT_GENERIC_GUT = True` |
| 28 [is-bool form] | `INTERGENERATION_HIERARCHY_FORCED` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:22` | `INTERGENERATION_HIERARCHY_FORCED = False` |
| 29 | `HIERARCHY_GATED_BY_GENERATION_THEOREM` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:23` | `HIERARCHY_GATED_BY_GENERATION_THEOREM = True` |
| 30 | `FIREWALL_LAST_REDOUBT_IS_FLAVOR_HIERARCHY` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:24` | `FIREWALL_LAST_REDOUBT_IS_FLAVOR_HIERARCHY = True` |
| 34 | `SCALE_IS_CLARIFIED_NOT_THE_WALL` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:25` | `SCALE_IS_CLARIFIED_NOT_THE_WALL = True` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B308_yukawa_last_redoubt/verdict.py:26` | `DERIVES_SM_VALUES = False` |

### `tests/test_b309_kappa_unification.py` — MIXED (flag-assert lines 4/12 of assert lines; tokens: LV=1 LR=3 C=0; other asserts: 8)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 27 | `E6_UNIQUE_COMPLEX_AND_Z3` | LITERAL-VERDICT | `frontier/B309_kappa_unification/kappa_unification.py:65` | `E6_UNIQUE_COMPLEX_AND_Z3 = True` |
| 31 | `IS_A_CONSOLIDATION_NOT_A_DISCOVERY` | LITERAL-RECORD | `frontier/B309_kappa_unification/kappa_unification.py:68` | `IS_A_CONSOLIDATION_NOT_A_DISCOVERY = True` |
| 35 | `KAPPA_IS_THE_TOE_READING_FIREWALLED` | LITERAL-RECORD | `frontier/B309_kappa_unification/kappa_unification.py:69` | `KAPPA_IS_THE_TOE_READING_FIREWALLED = True` |
| 36 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B309_kappa_unification/kappa_unification.py:70` | `DERIVES_SM_VALUES = False` |

### `tests/test_b310_cascade_realization_exhausted.py` — MIXED (flag-assert lines 7/10 of assert lines; tokens: LV=2 LR=6 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 16 | `CASCADE_IS_GENERIC_E6` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:54` | `CASCADE_IS_GENERIC_E6 = True` |
| 22 | `EQUAL_PI3_SPACING_REFUTED` | LITERAL-VERDICT | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:55` | `EQUAL_PI3_SPACING_REFUTED = True` |
| 22 | `SPACING_EQUALS_CUSP_SHAPE_REFUTED` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:57` | `SPACING_EQUALS_CUSP_SHAPE_REFUTED = True` |
| 26 | `TRINIFICATION_EIGENVALUE_IS_OMEGA` | LITERAL-VERDICT | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:58` | `TRINIFICATION_EIGENVALUE_IS_OMEGA = True` |
| 27 [is-bool form] | `DEFORMATION_REALIZATION_VERIFIED` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:59` | `DEFORMATION_REALIZATION_VERIFIED = False` |
| 31 | `REALIZATION_IS_THE_CRUX` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:60` | `REALIZATION_IS_THE_CRUX = True` |
| 32 | `CASCADE_MATH_EXHAUSTED` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:61` | `CASCADE_MATH_EXHAUSTED = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B310_cascade_realization_exhausted/cascade_realization_exhausted.py:62` | `DERIVES_SM_VALUES = False` |

### `tests/test_b311_cascade_branch_points.py` — MIXED (flag-assert lines 7/15 of assert lines; tokens: LV=4 LR=4 C=0; other asserts: 8)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 20 | `TWO_ENDS_IN_ONE_DISCRIMINANT` | LITERAL-VERDICT | `frontier/B311_cascade_branch_points/cascade_branch_points.py:73` | `TWO_ENDS_IN_ONE_DISCRIMINANT = True` |
| 26 | `CHAT2_BRANCHPOINT_CLAIM_VERIFIED` | LITERAL-VERDICT | `frontier/B311_cascade_branch_points/cascade_branch_points.py:77` | `CHAT2_BRANCHPOINT_CLAIM_VERIFIED = True` |
| 33 | `N2_IS_BRANCH_BUT_REDUCIBLE` | LITERAL-VERDICT | `frontier/B311_cascade_branch_points/cascade_branch_points.py:74` | `N2_IS_BRANCH_BUT_REDUCIBLE = True` |
| 33 | `NGE4_NOT_BRANCH` | LITERAL-VERDICT | `frontier/B311_cascade_branch_points/cascade_branch_points.py:76` | `NGE4_NOT_BRANCH = True` |
| 37 | `OBJECT_CORE_IS_TRINIFICATION_ONLY` | LITERAL-RECORD | `frontier/B311_cascade_branch_points/cascade_branch_points.py:79` | `OBJECT_CORE_IS_TRINIFICATION_ONLY = True` |
| 38 [is-bool form] | `CASCADE_REALIZATION_CLOSED` | LITERAL-RECORD | `frontier/B311_cascade_branch_points/cascade_branch_points.py:78` | `CASCADE_REALIZATION_CLOSED = False` |
| 39 | `REALIZATION_IS_THE_CRUX` | LITERAL-RECORD | `frontier/B311_cascade_branch_points/cascade_branch_points.py:80` | `REALIZATION_IS_THE_CRUX = True` |
| 40 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B311_cascade_branch_points/cascade_branch_points.py:81` | `DERIVES_SM_VALUES = False` |

### `tests/test_b312_face_iv_houses_the_form.py` — MIXED (flag-assert lines 6/13 of assert lines; tokens: LV=1 LR=5 C=0; other asserts: 7)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 19 | `ONE_E6_THREE_ADE_HATS` | LITERAL-RECORD | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:81` | `ONE_E6_THREE_ADE_HATS = True` |
| 25 | `FACE_IV_HOUSES_BOTH_ENDS` | LITERAL-RECORD | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:82` | `FACE_IV_HOUSES_BOTH_ENDS = True` |
| 30 | `ARITHMETIC_COMPATIBLE_VIA_TRIALITY` | LITERAL-VERDICT | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:83` | `ARITHMETIC_COMPATIBLE_VIA_TRIALITY = True` |
| 34 | `LEVEL_IS_GENERIC_NOT_SELECTED` | LITERAL-RECORD | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:84` | `LEVEL_IS_GENERIC_NOT_SELECTED = True` |
| 35 | `FACE_IV_HOUSES_THE_FORM_NOT_THE_VALUES` | LITERAL-RECORD | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:85` | `FACE_IV_HOUSES_THE_FORM_NOT_THE_VALUES = True` |
| 36 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B312_face_iv_houses_the_form/face_iv_houses_the_form.py:86` | `DERIVES_SM_VALUES = False` |

### `tests/test_b313_fibonacci_bridge_and_no_forced_choice.py` — MIXED (flag-assert lines 8/12 of assert lines; tokens: LV=1 LR=8 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `MATTER_EQUALS_ANYONS_REFUTED` | LITERAL-VERDICT | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:68` | `MATTER_EQUALS_ANYONS_REFUTED = True` |
| 27 | `BRIDGE_IS_GENERIC` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:66` | `BRIDGE_IS_GENERIC = True` |
| 27 | `OBJECT_SPECIFIC_PART_IS_B261` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:67` | `OBJECT_SPECIFIC_PART_IS_B261 = True` |
| 31 | `M1_HAS_NONMETRIC_SELECTOR` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:70` | `M1_HAS_NONMETRIC_SELECTOR = True` |
| 32 | `M1_IS_MOST_SELECTED_NOT_FORCED` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:71` | `M1_IS_MOST_SELECTED_NOT_FORCED = True` |
| 33 | `SINGLE_SEED_DOES_NOT_CHOOSE` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:72` | `SINGLE_SEED_DOES_NOT_CHOOSE = True` |
| 34 | `HETEROGENEITY_MAKES_THE_FORK` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:73` | `HETEROGENEITY_MAKES_THE_FORK = True` |
| 35 | `S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:74` | `S032A_THEOREM_VERSION_IS_THE_OPEN_TARGET = True` |
| 36 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B313_fibonacci_bridge_and_no_forced_choice/fibonacci_bridge_and_no_forced_choice.py:75` | `DERIVES_SM_VALUES = False` |

### `tests/test_b314_galois_seals_face_iv.py` — MIXED (flag-assert lines 6/11 of assert lines; tokens: LV=2 LR=5 C=0; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 26 | `DISCRETE_VALUES_ARE_GALOIS_ORBIT` | LITERAL-VERDICT | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:75` | `DISCRETE_VALUES_ARE_GALOIS_ORBIT = True` |
| 26 | `FIELD_IS_GOLDEN_NOT_FULL_CYCLOTOMIC` | LITERAL-VERDICT | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:76` | `FIELD_IS_GOLDEN_NOT_FULL_CYCLOTOMIC = True` |
| 30 | `TWO_ENDS_TWO_GALOIS_GROUPS` | LITERAL-RECORD | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:77` | `TWO_ENDS_TWO_GALOIS_GROUPS = True` |
| 31 | `VALUE_FREE_MONAD_IS_A_GALOIS_THEOREM` | LITERAL-RECORD | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:78` | `VALUE_FREE_MONAD_IS_A_GALOIS_THEOREM = True` |
| 35 | `PROBLEM_A_QUANTUM_CASE_SEALED` | LITERAL-RECORD | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:79` | `PROBLEM_A_QUANTUM_CASE_SEALED = True` |
| 36 | `RESIDUAL_IS_THE_ALL_INVARIANTS_THEOREM` | LITERAL-RECORD | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:80` | `RESIDUAL_IS_THE_ALL_INVARIANTS_THEOREM = True` |
| 37 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B314_galois_seals_face_iv/galois_seals_face_iv.py:81` | `DERIVES_SM_VALUES = False` |

### `tests/test_b315_e7_exclusion_vs_heterotic.py` — MIXED (flag-assert lines 9/14 of assert lines; tokens: LV=1 LR=7 C=1; other asserts: 5)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 18 | `ONLY_E6_IS_CHIRAL_CAPABLE` | COMPUTED | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:64` | `ONLY_E6_IS_CHIRAL_CAPABLE = None` |
| 27 | `HETEROTIC_SKIP_IS_NONCHIRALITY` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:65` | `HETEROTIC_SKIP_IS_NONCHIRALITY = True` |
| 28 | `OBJECT_E7_OVERDETERMINED_THREEFOLD` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:66` | `OBJECT_E7_OVERDETERMINED_THREEFOLD = True` |
| 29 | `SHARED_OBSTRUCTION_IS_NONCHIRALITY` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:67` | `SHARED_OBSTRUCTION_IS_NONCHIRALITY = True` |
| 30 [is-bool form] | `SAME_SINGLE_OBSTRUCTION` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:68` | `SAME_SINGLE_OBSTRUCTION = False` |
| 31 | `OBJECT_CONTAINS_HETEROTIC` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:69` | `OBJECT_CONTAINS_HETEROTIC = True` |
| 35 | `SHARED_ROOT_IS_PSEUDOREALITY` | LITERAL-VERDICT | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:70` | `SHARED_ROOT_IS_PSEUDOREALITY = True` |
| 36 | `TWO_ENDS_MIRROR_HETEROTIC_CHAIN_IS_HOOK` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:71` | `TWO_ENDS_MIRROR_HETEROTIC_CHAIN_IS_HOOK = True` |
| 37 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B315_e7_exclusion_vs_heterotic/e7_exclusion_vs_heterotic.py:72` | `DERIVES_SM_VALUES = False` |

### `tests/test_b316_sqrt7_chirality_field.py` — MIXED (flag-assert lines 6/10 of assert lines; tokens: LV=3 LR=3 C=1; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `IMAGINARY_LADDER_FLOORS_AT_MINUS_4` | COMPUTED | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:47` | `IMAGINARY_LADDER_FLOORS_AT_MINUS_4 = None` |
| 23 | `NEG7_PERMITTED_BY_CONGRUENCE` | LITERAL-VERDICT | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:48` | `NEG7_PERMITTED_BY_CONGRUENCE = True` |
| 23 | `NEG7_UNREACHABLE_BY_MONODROMY` | LITERAL-VERDICT | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:49` | `NEG7_UNREACHABLE_BY_MONODROMY = True` |
| 27 | `NEG7_IS_THE_CHIRALITY_FIELD` | LITERAL-RECORD | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:50` | `NEG7_IS_THE_CHIRALITY_FIELD = True` |
| 28 | `LADDER_DOES_NOT_EXTEND_TO_NEG7` | LITERAL-VERDICT | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:51` | `LADDER_DOES_NOT_EXTEND_TO_NEG7 = True` |
| 29 | `NEG7_APPEARS_PREDICTION_CONFIRMED` | LITERAL-RECORD | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:52` | `NEG7_APPEARS_PREDICTION_CONFIRMED = True` |
| 30 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B316_sqrt7_chirality_field/sqrt7_chirality_field.py:53` | `DERIVES_SM_VALUES = False` |

### `tests/test_b317_painleve_transcendental.py` — MIXED (flag-assert lines 7/11 of assert lines; tokens: LV=1 LR=6 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 23 | `METALLIC_ARE_TRANSCENDENTAL_PVI` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:53` | `METALLIC_ARE_TRANSCENDENTAL_PVI = True` |
| 24 | `DYNAMICS_IS_CHAOTIC_POSITIVE_ENTROPY` | LITERAL-VERDICT | `frontier/B317_painleve_transcendental/painleve_transcendental.py:54` | `DYNAMICS_IS_CHAOTIC_POSITIVE_ENTROPY = True` |
| 28 | `HITCHIN_LENS_ALREADY_RUN` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:51` | `HITCHIN_LENS_ALREADY_RUN = True` |
| 29 | `P010_UNRUN_CLAIM_IS_STALE` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:52` | `P010_UNRUN_CLAIM_IS_STALE = True` |
| 30 | `THIRD_LEAD_TO_REDUCE_TO_BANKED_WORK` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:56` | `THIRD_LEAD_TO_REDUCE_TO_BANKED_WORK = True` |
| 34 | `TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:55` | `TIME_IS_DIMENSIONLESS_FIREWALL_RELOCATED = True` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B317_painleve_transcendental/painleve_transcendental.py:57` | `DERIVES_SM_VALUES = False` |

### `tests/test_b318_amphichiral_mechanism.py` — MIXED (flag-assert lines 8/12 of assert lines; tokens: LV=0 LR=8 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 24 | `TAU_IS_COMPLEX_CONJUGATION` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:50` | `TAU_IS_COMPLEX_CONJUGATION = True` |
| 25 | `AMPHICHIRALITY_COVERS_EISENSTEIN` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:51` | `AMPHICHIRALITY_COVERS_EISENSTEIN = True` |
| 26 | `DEEPENS_B285_CP_SIGN_IS_GEOMETRIC` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:52` | `DEEPENS_B285_CP_SIGN_IS_GEOMETRIC = True` |
| 30 | `GOLDEN_END_IS_ARITHMETIC_ONLY` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:53` | `GOLDEN_END_IS_ARITHMETIC_ONLY = True` |
| 31 | `CHAT1_RESULT3_OVERCLAIMED_GOLDEN` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:54` | `CHAT1_RESULT3_OVERCLAIMED_GOLDEN = True` |
| 32 | `TWO_ENDS_TWO_DIFFERENT_MECHANISMS` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:55` | `TWO_ENDS_TWO_DIFFERENT_MECHANISMS = True` |
| 36 | `B311_GOLDEN_FACTOR_IS_DEFINITIONAL` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:56` | `B311_GOLDEN_FACTOR_IS_DEFINITIONAL = True` |
| 37 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B318_amphichiral_mechanism/amphichiral_mechanism.py:57` | `DERIVES_SM_VALUES = False` |

### `tests/test_b319_b176_woven_vs_single.py` — MIXED (flag-assert lines 8/10 of assert lines; tokens: LV=1 LR=7 C=0; other asserts: 2)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `SINGLE_OPERATOR_FRACTALITY_IS_MONOTONE` | LITERAL-VERDICT | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:50` | `SINGLE_OPERATOR_FRACTALITY_IS_MONOTONE = True` |
| 21 | `WOVEN_LADDER_IS_STANDALONE` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:49` | `WOVEN_LADDER_IS_STANDALONE = True` |
| 22 | `STANDALONE_IS_A_COLLECTIVE_EFFECT` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:53` | `STANDALONE_IS_A_COLLECTIVE_EFFECT = True` |
| 26 | `TWO_DIFFERENT_OBSERVABLES` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:51` | `TWO_DIFFERENT_OBSERVABLES = True` |
| 27 | `NO_CONTRADICTION` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:52` | `NO_CONTRADICTION = True` |
| 28 | `B176_FULLY_RESOLVED` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:55` | `B176_FULLY_RESOLVED = True` |
| 32 | `SINGLE_OP_MEASURE_IS_Q_SENSITIVE` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:54` | `SINGLE_OP_MEASURE_IS_Q_SENSITIVE = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B319_b176_woven_vs_single/b176_woven_vs_single.py:56` | `DERIVES_SM_VALUES = False` |

### `tests/test_b320_chat1_three_points.py` — MIXED (flag-assert lines 4/11 of assert lines; tokens: LV=1 LR=4 C=0; other asserts: 7)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 18 | `DEMOCRATIC_RANK1_NEEDS_S3_NOT_Z3` | LITERAL-VERDICT | `frontier/B320_chat1_three_points/chat1_three_points.py:83` | `DEMOCRATIC_RANK1_NEEDS_S3_NOT_Z3 = True` |
| 18 | `FUSION_REFUTED` | LITERAL-RECORD | `frontier/B320_chat1_three_points/chat1_three_points.py:82` | `FUSION_REFUTED = True` |
| 29 | `OBSERVER_SEAM_IS_FIREWALLED_HOOK` | LITERAL-RECORD | `frontier/B320_chat1_three_points/chat1_three_points.py:86` | `OBSERVER_SEAM_IS_FIREWALLED_HOOK = True` |
| 33 | `EXHAUSTION_STANDS` | LITERAL-RECORD | `frontier/B320_chat1_three_points/chat1_three_points.py:87` | `EXHAUSTION_STANDS = True` |
| 34 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B320_chat1_three_points/chat1_three_points.py:88` | `DERIVES_SM_VALUES = False` |

### `tests/test_b321_seam_geometry_adjudication.py` — MIXED (flag-assert lines 7/11 of assert lines; tokens: LV=2 LR=6 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 18 | `CUSP_NORM_IS_BASIS_DEPENDENT` | LITERAL-VERDICT | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:66` | `CUSP_NORM_IS_BASIS_DEPENDENT = True` |
| 18 | `CUSP_NORM_IS_HE6` | LITERAL-VERDICT | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:65` | `CUSP_NORM_IS_HE6 = True` |
| 24 | `CP_PHASE_EQ_CORE_LENGTH_IS_SPLICE` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:67` | `CP_PHASE_EQ_CORE_LENGTH_IS_SPLICE = True` |
| 28 | `DEMOCRATIC_RANK1_FROM_Z3_CONTRADICTS_B320` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:68` | `DEMOCRATIC_RANK1_FROM_Z3_CONTRADICTS_B320 = True` |
| 32 | `SELF_REALIZABILITY_IS_REFRAME_OF_BANKED` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:69` | `SELF_REALIZABILITY_IS_REFRAME_OF_BANKED = True` |
| 33 | `FLOW_SELECTION_SPLICE_CORRECTLY_KILLED` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:70` | `FLOW_SELECTION_SPLICE_CORRECTLY_KILLED = True` |
| 34 | `SHARPENED_MULTIPLICITY_GATE_IS_THE_RESIDUE` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:71` | `SHARPENED_MULTIPLICITY_GATE_IS_THE_RESIDUE = True` |
| 35 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B321_seam_geometry_adjudication/seam_geometry_adjudication.py:72` | `DERIVES_SM_VALUES = False` |

### `tests/test_b322_value_hunt_filling_invariants.py` — MIXED (flag-assert lines 5/9 of assert lines; tokens: LV=1 LR=4 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 27 | `SM_MATCHED_AT_CHANCE` | LITERAL-VERDICT | `frontier/B322_value_hunt_filling_invariants/value_hunt_filling_invariants.py:74` | `SM_MATCHED_AT_CHANCE = True` |
| 28 | `OBJECT_DOES_NOT_ENCODE_SM_VALUES` | LITERAL-RECORD | `frontier/B322_value_hunt_filling_invariants/value_hunt_filling_invariants.py:75` | `OBJECT_DOES_NOT_ENCODE_SM_VALUES = True` |
| 29 | `FIREWALL_HOLDS_BY_COMPUTATION` | LITERAL-RECORD | `frontier/B322_value_hunt_filling_invariants/value_hunt_filling_invariants.py:76` | `FIREWALL_HOLDS_BY_COMPUTATION = True` |
| 30 | `VALUES_LIVE_AT_THE_GATES_NOT_THE_OBJECT` | LITERAL-RECORD | `frontier/B322_value_hunt_filling_invariants/value_hunt_filling_invariants.py:77` | `VALUES_LIVE_AT_THE_GATES_NOT_THE_OBJECT = True` |
| 31 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B322_value_hunt_filling_invariants/value_hunt_filling_invariants.py:78` | `DERIVES_SM_VALUES = False` |

### `tests/test_b323_four_levels_adjudication.py` — MIXED (flag-assert lines 6/10 of assert lines; tokens: LV=1 LR=6 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 18 | `FOUR_LEVELS_FRAMING_VERIFIED` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:62` | `FOUR_LEVELS_FRAMING_VERIFIED = True` |
| 18 | `TWO_Z3_ARE_DISTINCT` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:63` | `TWO_Z3_ARE_DISTINCT = True` |
| 22 | `FRAMING_IS_A_HELPFUL_CONSOLIDATION` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:64` | `FRAMING_IS_A_HELPFUL_CONSOLIDATION = True` |
| 26 | `OMEGA_PERTURBATION_IS_TAUTOLOGICAL` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:65` | `OMEGA_PERTURBATION_IS_TAUTOLOGICAL = True` |
| 28 | `YUKAWA_RATIO_DOES_NOT_MATCH_SM` | LITERAL-VERDICT | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:66` | `YUKAWA_RATIO_DOES_NOT_MATCH_SM = True` |
| 29 | `PART3_IS_NOT_A_CROSSING` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:67` | `PART3_IS_NOT_A_CROSSING = True` |
| 33 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B323_four_levels_adjudication/four_levels_adjudication.py:68` | `DERIVES_SM_VALUES = False` |

### `tests/test_b324_omega_circulant_verified.py` — MIXED (flag-assert lines 7/11 of assert lines; tokens: LV=2 LR=5 C=0; other asserts: 4)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 19 | `EXACT_STRUCTURAL_FACT_VERIFIED` | LITERAL-VERDICT | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:75` | `EXACT_STRUCTURAL_FACT_VERIFIED = True` |
| 24 | `MAGNITUDES_DEGENERATE_NO_HIERARCHY` | LITERAL-VERDICT | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:77` | `MAGNITUDES_DEGENERATE_NO_HIERARCHY = True` |
| 28 | `IS_STRUCTURE_NOT_VALUES` | LITERAL-RECORD | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:76` | `IS_STRUCTURE_NOT_VALUES = True` |
| 29 | `OMEGA_IS_THE_UBIQUITOUS_EISENSTEIN` | LITERAL-RECORD | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:78` | `OMEGA_IS_THE_UBIQUITOUS_EISENSTEIN = True` |
| 30 | `CIRCULANT_IS_TAUTOLOGICAL` | LITERAL-RECORD | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:79` | `CIRCULANT_IS_TAUTOLOGICAL = True` |
| 31 | `GENERATIONS_ARE_CONJUGATES_SAME_CHARACTER` | LITERAL-RECORD | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:80` | `GENERATIONS_ARE_CONJUGATES_SAME_CHARACTER = True` |
| 32 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B324_omega_circulant_verified/omega_circulant_verified.py:81` | `DERIVES_SM_VALUES = False` |

### `tests/test_b325_z3_protection_refuted.py` — MIXED (flag-assert lines 7/10 of assert lines; tokens: LV=2 LR=5 C=0; other asserts: 3)

| test line | flag | class | definition (evidence) | RHS |
|---|---|---|---|---|
| 17 | `LIGHT_MODES_ARE_DIFFERENT_IRREPS` | LITERAL-VERDICT | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:53` | `LIGHT_MODES_ARE_DIFFERENT_IRREPS = True` |
| 22 | `Z3_INVARIANT_CAN_SPLIT_LIGHT` | LITERAL-VERDICT | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:54` | `Z3_INVARIANT_CAN_SPLIT_LIGHT = True` |
| 27 | `OVERLAP_DEGENERACY_IS_ACCIDENTAL` | LITERAL-RECORD | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:55` | `OVERLAP_DEGENERACY_IS_ACCIDENTAL = True` |
| 28 | `OVERLAP_NOT_THE_PHYSICAL_MASS` | LITERAL-RECORD | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:56` | `OVERLAP_NOT_THE_PHYSICAL_MASS = True` |
| 32 | `CHAT2_OBSTRUCTION_REFUTED` | LITERAL-RECORD | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:57` | `CHAT2_OBSTRUCTION_REFUTED = True` |
| 33 | `CRUX_STAYS_LEVEL3_NOT_RELOCATED` | LITERAL-RECORD | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:58` | `CRUX_STAYS_LEVEL3_NOT_RELOCATED = True` |
| 34 [is-bool form] | `DERIVES_SM_VALUES` | LITERAL-RECORD | `frontier/B325_z3_protection_refuted/z3_protection_refuted.py:59` | `DERIVES_SM_VALUES = False` |
