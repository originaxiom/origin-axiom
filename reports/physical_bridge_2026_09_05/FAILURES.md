# Failures retained, not rewritten as successful runs

## Third upstream audit: NumPy dictionary keys stop JSON export

At f3696b21 the full G2/common-fixed-space calculation completes, but main
fails during json.dump: `TypeError: keys must be str, int, float, bool or
None, not int64`. The old float producer's census has NumPy integer keys.
The partial `g2_isolation_first_run.json` is retained and is NOT valid JSON.
The seven original tests give six passes and one serialization failure;
captured output is `G2_ISOLATION_FIRST_TESTS.txt`. Both source and test remain
unchanged. The separately sealed 9812f5d5 wrapper converts NumPy scalars
losslessly and writes a fresh successful `g2_isolation_rerun_1.json`. No
geometric conclusion or tolerance is changed by this export repair.

The combined quiescent run is 91 passed, 3 failed (61.66 s): this original
serialization failure plus both previously retained R7 small-step controls.
Its full captured output and gate output are in `G2_ISOLATION_CHECKS.txt`.
The three failing publication gates are attribution, test-vacuity and
seal-provenance. The last now includes the NEW UPSTREAM_3_DESIGN.md and
UPSTREAM_3_EXPORT_REPAIR.md: the literal provenance markers required by the
gate are absent/incomplete. This is a new procedural defect, not merely
old baseline debt. The original seal timing/content remain visible; neither
sealed bytes nor the gate are rewritten to manufacture compliance.

## B1098 live-test loader

The original test failed before checking the triple because the executed
certificate prefix lacked `__file__`. The failure and original source hash
are in EXTENSION_1.md. The corrected loader, with unchanged mathematical
assertions, passed in the combined run: **27 passed in 40.76 s**.

## R3 first execution: output serialization, not a model verdict

Instrument sealed at commit `c9a7ad69`; `mass_match.py` SHA-256
`f73d07ef7df14c2111283bf04d05d669351ac786750127e9597dc45b12b1c56e`.
The mathematical checks ran, but serializing a NumPy boolean failed:

```text
  File "mass_match.py", line 189, in main
    json.dump(result, handle, indent=2, allow_nan=False)
TypeError: Object of type bool is not JSON serializable
```

The original **incomplete** `mass_results_first_run.json` is retained byte for
byte. It is intentionally not valid JSON and is not a successful result.
No numerical verdict is taken from this run.

Post-hoc repair, before the rerun: convert bound results to native floats,
add a JSON round-trip regression, and serialize the entire payload before
opening the destination. The rerun uses a new output name. The pre-repair
source remains in git and both output artifacts remain on disk.

## Reporting check: source pointers missing from the law-index rows

The first post-edit focused run was **67 passed, 1 failed** in 118.58 s.
The only failure was `test_all_gates_pass`: the three new conditional-model
index rows named their report and live tests, but lacked per-row arc pointers;
the column header also did not use the index's recognized header form.

The rows now explicitly connect their representation/mass inputs to B884/B970
and the new work to B915's audit addendum, which points to R2/R3 and their
actual code. They do not attribute the new mass calculation to the old arcs.
The gate is unchanged; no numeric assertion, expected census or failure rule
was loosened. The reporting/gate checks after this documentation fix were
**13 passed, 1 warning in 79.53 s**. The 26 new gauge/mass/legacy tests also
passed separately in 2.00 s. The warning is the existing review counter.

## Staged publication check: literal upstream ref names

Once the previously untracked evidence inventory was staged, the attribution
gate reported three vendor-name tokens in its `remote_refs` field. Inspection
confirmed these are literal fetched upstream branch names, not authorship
claims. The other 29 gates passed. The earlier unstaged gate run did not reach
this new file: its green result is not a certificate for the staged tree.

The inventory and its hash are retained without rewriting the source names.
This is a **local draft**, not a publication-ready all-gates-green certificate;
no gate exception was added and nothing was pushed. A publication policy for
literal source-reference metadata is still needed.

## R4 first test run: an unevaluated zero, not a nonzero kernel residual

The sealed runner completed and wrote `vacuum_results_first_run.json`. The
separate first test run returned **7 passed, 1 failed in 13.45 s**; full output
is retained in `VACUUM_TEST_FIRST_RUN.txt`. Original test hash:
`340d031b5dc6beb8a9c394f4e405ee3b42cb8ddfcfb3286adefd34e8e442b0c0`.

The complex-VEV kernel check asked `is_zero_matrix` about unevaluated arithmetic.
Diagnostic example, obtained before editing:

```text
3 - I + (-1/5 + 7*I/5)*(1 + 2*I)
is_zero_matrix: None; simplify(...).is_zero_matrix: True
```

Every affected residual simplified to exactly zero; none was accepted by a
numerical tolerance. Repair: simplify the product before checking exact zero,
and add an actual non-kernel vector that must still fail. The scientific
instrument and its completed output are unchanged. The corrected test is
re-hashed and committed before its rerun.

The rerun, together with all earlier new physical-bridge tests, returned
**34 passed in 15.75 s**. No failed scientific output was overwritten.

## R4 final staged gates: two missing machine-readable headings

After adding the orientation control, all **35 new tests passed in 22.12 s**.
The staged governance run was **28 passed, 2 failed**: the already-disclosed
literal-ref-name attribution check, and `seal-provenance` on EXTENSION_2.md
and EXTENSION_2_CONTROL.md. The latter requires the exact headings
`BANKED IDENTITY:` and `PRIOR ART:`. The designs describe their inherited
identities, controls and prior work but do not use those literal headings.

The sealed originals are not rewritten after execution to simulate compliant
pre-execution wording; their hashes and commit history are preserved. This is
a genuine procedural-format defect in this local draft, not a failed invariant
or an excuse to drop the scientific result. Future designs must include both
required fields before sealing. No gate was weakened, no full-suite green or
publication readiness is claimed, and nothing has been pushed.

Final test/gate output: `VACUUM_FINAL_CHECKS.txt`. All 27 currently listed
input/design/code/output hashes matched before these reporting notes.

## R5: successful first runs; earlier governance defects remain visible

Both R5 scientific first runs succeeded: full one-loop spectrum/orientation
calculation and the independent analytic-derivative/exact-polynomial check.
The final combined physical-audit tests at 427ff18a returned **48 passed in
26.90 s**. Separate unchanged upstream tests returned **59 passed**. None of
these is the full merged repository suite.

Governance again returned **28 passed, 2 failed**, for the same original
inventory attribution and R4 seal-heading issues. R5's two designs contain
the required literal fields; the sealed R4 originals were not rewritten and
no gate was weakened. All 39 input/design/code/result hashes matched before
adding the final check transcript. Raw evidence: `QUANTUM_FINAL_CHECKS.txt`.
The raw upstream command record retains a local interpreter path: make a
labelled portable derivative before public distribution, not a silent edit
of the original result. This remains a local, unpushed research branch.

## R6 first staged gate: a new NO-ASSERT finding to verify

The first R6 staged governance run at 44a52ec4 plus the result/report changes
returned **27 passed, 3 failed**, not the previous 28/2. The additional output
was exactly:

```text
  FAIL  test-vacuity: 1 unconditionally-passing test(s): tests/test_physical_bridge_quantum_shift.py::test_vector_and_complex_Weyl_mass_derivatives
```

Source inspection shows that the checker recognizes Python assert nodes and
six pytest-style call names, but not `np.testing.assert_allclose`, which this
test uses twice. A NO-ASSERT screen is not by itself a demonstration that
the test passes unconditionally. `EXTENSION_4_CONTROL.md` seals live vector
and Weyl mutation checks before execution, plus independent full-gradient
and reduced-solve controls. The original sealed test, gate and checker are
unchanged. This failure is not silently exempted or called green; its
scientific significance depends on the bite controls. The two previous
inventory-attribution/R4-seal failures also remain.

The pre-sealed post-result controls at 2215d67b now PASS. The original
derivative test passes before perturbation; an additive corruption of the
vector orbit and, separately, of the Weyl map each trigger AssertionError.
This demonstrates a false positive in the static NO-ASSERT classification,
not an unconditionally passing mathematical test. Direct 186-component
scalar-gradient contraction and the reduced nine-mode solve also pass.
Combined regression: 59 passed in 35.56 s. Governance still reports 27/3;
no checker/test exception was introduced. Raw: `QUANTUM_SHIFT_CHECKS.txt`.

## R7 first run: numerical second-derivative control fails before physics

At a3f8f786 the first R7 runner exits 1 in the full-Hessian second finite
difference: 12/86436 elements fail atol=3e-7 at step 1e-4, maximum violation
1.84087162e-6. It never reaches classical or quantum physics results.
The zero-byte `higgs_first_run.json` is retained, as is stderr in the
explicitly portable `HIGGS_FIRST_FAILURE.txt`; the unsanitized original
transcript stays outside the repository in the local audit workspace.

`EXTENSION_5_REPAIR.md` pre-seals a polynomial-Hessian polarization control
and step sweep, with the original tolerance and all physics unchanged.
The original producer and test bytes are preserved, not overwritten. This
is not evidence of a Higgs instability. One trailing blank line in the R6
raw check transcript was also reported by diff --check at banking; its
sealed bytes are retained rather than cosmetically rewritten.

R7 repaired scientific run succeeds at f5c40f4f in 20.33 s. The independent
polynomial polarization agrees to 1.07e-14; the step sweep verifies roundoff
amplification as the original failure's cause. The focused suite including
the unchanged original tests returns 2 failed, 8 passed in 21.48 s: exactly
the two calls to the old small-step control fail. The replacement controls
and all other tests pass. Full output: `HIGGS_FIRST_TESTS.txt`; no skip or
xfail was introduced. Negative Higgs loop curvatures and large singlet
shifts are separately reported as physical-model results, not test defects.

## R8: successful first execution; previous test and governance debt preserved

The pre-sealed R8 first scientific execution succeeds in 60.23 s; all eight
new tests pass in 57.33 s. The combined quiescent regression returns 99
passed and three failed in 96.30 s. The failures are exactly the original
G2 NumPy-key exporter test and both original R7 small-step controls. The
separately sealed G2 export and R7 polynomial/larger-step controls pass.
No original failure was hidden, no old source altered and no tolerance
relaxed. Raw successful output and complete failed-test traces are in
BROKEN_VACUUM_CHECKS.txt; the first scientific JSON is complete and valid.

The staged reporting gates return 27 pass, 3 fail: inventory attribution,
the R6 static NO-ASSERT classification already mutation-checked above,
and seal-provenance. The latter still names EXTENSION_2.md,
EXTENSION_2_CONTROL.md, UPSTREAM_3_DESIGN.md and
UPSTREAM_3_EXPORT_REPAIR.md. The two G2 omissions were new errors in that
earlier audit, not retroactively excused as preexisting. R8's design contains
both required literal fields and does not add a provenance failure. All
86 then-listed latest-path hashes match; generated views are already current.
Captured gates: BROKEN_VACUUM_GATES.txt. The transcript/reporting hashes are
added afterward, with a fresh final hash check before the local commit.
This remains a local research checkpoint, not publication/full-suite green.

## R9: successful first execution; no new test or governance failure

The pre-sealed R9 first scientific execution succeeds in 4.87 s. All eight
new tests pass in 5.89 s; the combined quiescent regression returns 107
passed and three failed in 94.59 s. The failures remain the original G2
NumPy-key exporter and both original R7 small-step controls, with separately
sealed repairs passing. No original source, test or tolerance was changed;
no skip or xfail was added. Complete first output and failed-test traces:
INFRARED_ALIGNMENT_CHECKS.txt.

The staged reporting gates return 27 pass, 3 fail: the existing inventory
attribution finding, R6 static-vacuity classification and four earlier
seal-marker omissions listed above. R9 adds no provenance failure. The
review-due warning also remains visible; this is not a decadal review.
All 93 then-listed latest-path hashes match and generated views are already
current. Captured gates: INFRARED_ALIGNMENT_GATES.txt. These final notes and
the gate transcript/hash are added afterward and are not covered by that
earlier staged gate run. A final artifact-hash check follows before the
local commit. No full-suite green, publication readiness or push is claimed.

Final latest-path artifact check: 94 hashes, zero mismatches. The staged
diff whitespace check flags only pytest's verbatim trailing spaces in
INFRARED_ALIGNMENT_CHECKS.txt; these raw evidence bytes are deliberately
retained, not silently reformatted. The sealed R9 design, source and tests
have no diff from dac87d46.

## R10: successful finite computation, unchanged earlier failure debt

Source/design/eight tests sealed at 8cbd10ed before first execution.
Scientific run succeeds in 9.47 s; new tests 8 passed in 10.29 s. Combined
quiescent regression: 115 passed, 3 failed in 111.84 s, exactly the
original G2 NumPy-key exporter and both original R7 small-step controls;
separate sealed repairs pass. No skip, xfail, tolerance relaxation or old
source rewrite. Raw successful output and full failure traces are in
FINITE_ALIGNMENT_CHECKS.txt. Their original local interpreter paths and
pytest trailing whitespace are retained as raw local evidence, not a
privacy-scrubbed public derivative.

Staged reporting gates: 27 pass, 3 fail, the same inventory attribution,
R6 static-vacuity classification and four earlier seal-marker omissions.
R10 adds no provenance defect. The review-due warning remains; this is
not a decadal review. All 101 then-listed latest-path artifact hashes
match and generated views are already current. Captured gates:
FINITE_ALIGNMENT_GATES.txt. These final notes and that transcript/hash
postdate the staged gate run. Final hashes are checked again before the
local reporting commit. No full-suite green or publication claim; no push.

Final artifact check: 102 latest-path hashes, zero mismatches. R10's
design/source/tests have no diff from 8cbd10ed. The staged whitespace check
passes excluding the verbatim test transcript; its pytest-generated
trailing spaces remain part of the preserved raw evidence.
