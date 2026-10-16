# Prospective experiment admission with preserved historical failures

The owner approved a separate prospective gate on October 16: new
experiments require a properly sealed, source-complete design and
independent review. Historical failures remain noncompliant; the
repository must not be described as globally green. This is an
enforcement-policy implementation, not a new scientific experiment.

BANKED IDENTITY: the existing seal-provenance entry point continues to
report its complete unresolved population and fail on historical
violations. Its policy, original evidence, seal prefix and attribution
baseline are not waived. A prospective admission cannot alter that
verdict or certify earlier experiments.

PRIOR ART: personally read WORKING_RULES, GOVERNANCE, PRACTICES,
COMPUTE_THE_PROGRAM, BANKING_PROTOCOL, both existing provenance gates,
the 46-control policy test file and the earlier policy design. The
existing run_all aggregate remains the repository compliance check.
This design adds a distinct decision about one proposed experiment;
it does not reinterpret the aggregate as passing. No absence claim is
made about scientific results or other branches.

## Decision and scope

Implement a read-only command that accepts one explicit admission
manifest. Require an immutable Git commit containing its specification,
design and all declared source, input and test files, with exact current
byte agreement. The specification and design must have matching seal
rows in that commit and in the current ledger. Both literal design
fields remain required. Commands, reserved output paths, authors and
the environment descriptor must be explicit. Output paths already
present at seal or now prevent first-run admission.

A separately committed review must bind that exact sealed specification
and commit, name a non-authoring reviewer, approve execution, attest
source completeness and report no unresolved objections. A subsequent
receiver acceptance must bind the exact review commit and bytes, and
be reachable from the fetched main reference. Author-written review
labels alone are insufficient. The receiver is responsible for verifying
reviewer identity, independence and the substantive completeness of
the source/environment inventory. Git proves binding and reachability,
not personal identity, the truth of attestations, or absence of an
undisclosed earlier execution. Preserve that limitation at the point
of use. No actual review or acceptance is manufactured here.

The prospective result includes the full historical seal report and
the separate outcomes of every other existing governance gate. Any
non-historical gate failure, malformed historical policy, missing or
stale evidence, unreadable Git object or incomplete admission fails
closed. Historical problems may coexist with a prospective pass but
remain failures in the global aggregate. This is a pre-execution
admission check, not a sandbox, scientific certificate or permission
to run unspecified commands. Existing maintenance and read-only
source audits remain distinguishable from new scientific experiments.

## Controls and acceptance

Exercise the real prospective entry point on isolated Git repositories.
Recover an admissible fixture even while its historical register fails.
Reject missing or malformed manifests, duplicate keys, wrong schemas,
unsafe paths, missing or stale pins, uncommitted source, missing seals,
missing design fields, undeclared entrypoints, preexisting outputs,
self-review, absent source-completeness attestation, unresolved review
objections, mismatched specification or review, unaccepted reviews and
acceptances outside fetched main. Require another governance failure
to block admission. The ordinary global seal gate must still fail and
retain its historical evidence in the positive fixture. These are
maintenance controls, not independent review of this implementation.

Commit this design before code changes. Commit and push the implemented
checker, tests and source-pin metadata before executing them. Capture
complete outputs, exit status, elapsed time, exact source pins and
quiescent tracked-content/index states. Preserve every failed attempt.
Do not run a new scientific producer until an actual packet meets the
new requirements. Publish the mechanism and remaining independent
review duty to main; sender records remain OPEN.
