# P210 admission wrapper engineering design

October 24, 2026. BEFORE the new wrapper and fixture implementation.
Software infrastructure only; no scientific module may be imported,
collected or run by these fixtures.

BANKED IDENTITY: Six proposed isolated wrapper-binding and rejection controls; not a mathematical experiment, physical result or execution admission.
PRIOR ART: Existing frozen verification_v3/run_checks.py and its infrastructure controls; the P210 design at 03eba26c3 and unrun ten-method implementation at 455ff44f4. Earlier fixture results are not certification of the new wrapper binding.

The new entrypoint will read the frozen v3 runner's bytes, require its
literal SHA256 before importing it, rebind ONLY HERE, ENTRY and EXPECTED,
then delegate to its main. The frozen runner retains its own environment,
strict tracked-state, exact main-accepted prospective admission, command,
output, pre-import and final custody checks. No bypass mode or simulated
acceptance is added to the production wrapper. Failure propagates.

Six finite fixture cases are declared before implementation:

1. In an isolated synthetic directory layout, the exact permitted fixture
   source delegates once with the expected HERE, ENTRY and ten method IDs.
2. Changing that fixture source after its hash is fixed rejects before
   its module-level import marker can execute.
3. Removing its source rejects before delegation or scientific import.
4. A nonzero delegated return code is preserved.
5. A delegated exception is preserved, never converted to success.
6. AST-only inspection matches the wrapper's literal EXPECTED list to
   all ten unimported mathematical method definitions; a fake added ID
   is rejected by the fixture check.

The fixtures substitute a small stdlib-only SENTINEL for the v3 source
inside their temporary directory and substitute its hash into the copied
wrapper's single declared hash constant. The repository wrapper, frozen
runner and science sources are not edited by a test. Sentinel acceptance
is NOT real prospective admission and no fixture claims to test the
whole gate or execute P210. A marker records only synthetic import and
the binding values. Fixtures never invoke the production runner, main
gate, real acceptance records, checks.py or SymPy.

Execution scope, if performed after committing this design and software:
python3 -B with unittest only, running engineering_checks.py directly.
Use temporary directories, capture all fixture failures and process
status, and preserve the first outcome. Six methods must run with no
skips, expected failures or hidden rerun. If any fails, retain it before
a correction. A future broad test suite must not collect the scientific
module before its own admission.

This tests only the new wrapper source pin, binding, static population
and failure propagation. It does not re-certify frozen v3's runtime/gate
closure, substantively accept the science, prove global source completeness
or authorize production use. The P210 environment and full prospective
specification, independent review, main acceptance and strict execution
admission remain separate duties. Historical violations remain violations.
