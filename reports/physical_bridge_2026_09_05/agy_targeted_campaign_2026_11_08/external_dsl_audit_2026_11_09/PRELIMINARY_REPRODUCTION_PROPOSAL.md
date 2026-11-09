# Proposed bounded preliminary reproduction while AGY works

2026-11-09. PROPOSAL ONLY. No policy amendment, scientific execution,
formal acceptance or banking is inferred. Prepared in response to the
owner's question about what running the scientific code would mean.

## Exact scope

Reproduce the unchanged external source preserved at physical checkpoint
edaa4cf7cd9e1a9e082bad87ea2350a3803c32c3 and standalone external head
2f45580c4afa5985145df7520575dd9c4e51d928. CUSTODY.json pins all eleven
files and the original archive. The initial seven files are also pinned
at ad6f2f5b4f7bbdaca25bbe6dabcb1b6eb80b2f62. Do not modify scientific
source, thresholds, fixtures, expected populations or saved receipts.

This proposal concerns the external package only. It does not release
the OA gauge-response producer or any other prospective scientific packet.
It does not release new numerical searches, fitted moduli, new models,
new regression implementations or delegated agents.

## Existing review and open policy decision

REVIEW.md records the completed personal source/hand audit and its
limitations. The external package is not an accepted OA experiment.
The owner-approved GOAL_CONTRACT.md, Verification and publication, says
to obtain non-authoring review and main's acceptance before a new
scientific run, followed by prospective admission. TASKS.json retains it.

The proposed narrow amendment would allow this exact local preliminary
reproduction before those formal execution approvals. It would preserve
their unfulfilled status and require them for any formal acceptance or
banking. It would not mark past runs compliant. Without an explicit owner
decision, source/hand work continues and the following commands stay unrun.

## Environment and isolated output plan

Interpreter distribution metadata inspected without scientific imports

- /Users/dri/.pyenv/versions/3.12.1/bin/python3, CPython3.12.1
- macOS15.1, x86_64
- NumPy2.4.0, SciPy1.16.3 and mpmath1.3.0 installed distributions

Recheck those versions immediately before a permitted run. Use a fresh
directory under /private/tmp with a unique oa-preliminary-reproduction-
prefix. Reconstruct the six Python source files from the preserved bytes,
removing only their storage .txt suffix. Keep the three original JSON
receipts under expected/ and write fresh program outputs beside the
temporary source copies. Do not run inside the OA checkout or the
external author's original checkout. Preserve source SHA256 values
before and after each command and the exact selected runtime settings.
No installation, network access or original-source modification is needed.

## Proposed command order

With the declared interpreter, use the temporary source directory as
the working directory for steps1-4, and its golden_spikes_stress_test/
subdirectory for step5.

1. python3 -m unittest -v -f test_guardrail_dsl test_repo_crucial_math_with_dsl
2. python3 guardrail_dsl.py
3. python3 verify_repo_crucial_math_with_dsl.py
4. python3 golden_spikes_stress_test/verify_golden_spikes_stress_test.py
5. python3 -m unittest -v -f test_golden_spikes_stress_test

The source contains17 methods in the first suite and5 in the second.
Record the observed count rather than assigning a pass from these names.
Use a ten-minute command limit and thirty-minute total compute limit.
Preserve timeout output as an incomplete run, not a mathematical failure.
Stop the sequence at the first nonzero exit or unexpected source mutation.
Save full stdout/stderr, command, exit status and timings for every step.
No silent retries or repairs. Poll without leaving the owner without
progress communication during long computation.

## Interpretation decided before execution

Compare fresh receipts with the original saved receipts. Exact matches,
floating differences, assertion failures and unavailable dependencies get
different labels. Inspect the actual matrices/residuals and each check's
coverage. A passing test suite does not repair the known theorem-key
loophole, cached-JSON echo gap, RGE bug, missing48-scalar-state control,
conditional cohomology assumptions or wrong cusp-measure calculation.

The first output can establish reproducibility of selected finite checks
in the recorded environment. It cannot prove the continuous classification,
global operator/domain claims, SM3, nineteen measured parameters, gravity
or any foundational input reduction. Existing formal review, main
acceptance, admission and banking duties remain explicitly unfulfilled.

After the reproduction, propose a separately pinned repair/control package
for the known defects. Preserve every original and failed result alongside
the successor. Keep AGY's current hand assignment independent of this work.
