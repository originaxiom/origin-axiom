# Failures retained, not rewritten as successful runs

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
