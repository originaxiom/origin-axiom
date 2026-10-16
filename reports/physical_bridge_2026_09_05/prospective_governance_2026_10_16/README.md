# Prospective experiment admission and historical noncompliance

The owner approved a separate prospective decision on October 16.
Historical failures remain noncompliant in the unchanged global gate.
A new scientific experiment needs a properly sealed specification,
complete source inventory and accepted independent review. At published
source 472be2a2a, all 88 focused maintenance tests pass: 42 prospective
controls and the unchanged 46 provenance controls. Main's independent
review remains pending. No scientific packet is admitted here.

## The two decisions

The ordinary repository check remains scripts/gates/gates.py. It reports
historical seal problems as failures, and no prospective decision turns
the repository globally green. The additional command is:

    python3 -B scripts/gates/prospective.py --admission REPOSITORY_RELATIVE_JSON

It is read-only and does not launch scientific code. Its JSON reports
prospective_admissible separately from global_compliant, retains the full
historical seal report and all gate outcomes, and exits nonzero unless
the specific admission passes. Every other governance gate must pass;
a missing or malformed historical report is not a waiver. Only the
declared commands and sources are covered, before their reserved outputs
exist. Actual execution must retain the accepted pins and usual custody.

## Evidence schema

The admission JSON has exactly schema=1, sealed_commit, specification,
review and acceptance. A pin has exactly path and sha256. Review and
acceptance references additionally carry their full commit. All file
paths are repository-relative, canonical and non-symlinked. These
references resolve actual Git objects, not merely strings in a transcript.

The specification at sealed_commit contains exactly schema=1,
experiment_id, authors, design, artifacts, commands, outputs and
environment. Its design and the specification itself require matching
seal-ledger rows at that commit and now. Design fields BANKED IDENTITY
and PRIOR ART must be literal and nonempty. Artifacts are unique pins
with role source, input or test, including at least source and test.
Environment pins a listed input describing the runtime and dependencies.
Each command gives entrypoint and argv and names a declared source;
outputs lists reserved paths absent both at seal and before admission.
Declared source, input, test and design bytes must still match exactly.

The separately committed review contains schema=1, experiment_id,
sealed_commit, specification, reviewer, nonauthoring=true,
source_complete=true, decision=APPROVE_EXECUTION, unresolved=[] and a
nonempty scope. The reviewer cannot be a declared author. The main
acceptance contains schema=1, experiment_id, sealed_commit,
specification, the exact review reference, receiver=main,
decision=ACCEPT_INDEPENDENT_REVIEW, verified_independence=true and
verified_source_completeness=true. Its separate commit must be reachable
from refs/remotes/origin/main. The same-source review can occur on
another branch without merging it; the cryptographic references bind
the sealed commit, review and acceptance without inventing execution times.

The checker cannot establish who actually authored a review, discover
every dynamic dependency or prove that nothing ran earlier off-record.
Main must verify identity, genuine non-authorship, the substantive source
and environment inventory, and the review's adequacy before acceptance.
Invented identities, self-issued acceptance or fixture records are not
independent review. Tests use synthetic repositories only and must not
be presented as real admission. Their scope excludes scientific adequacy.

## Current status and scientific next step

The implementation was designed under DESIGN.md, committed b63f03442,
before changes. Source 472be2a2a was pushed and server-confirmed before
the maintenance run. Tests pass in 70.42 seconds; the captured process
exits zero after 71.405725 seconds. The integration fixtures use two
gates in isolated synthetic repositories, not the full scientific suite.

The separate real production command executes all 30 governance gates:
29 pass and seal-provenance fails with all 643 unresolved paths retained
(562 unclassified, 76 missing-field design candidates and five explicit
historical violations). It refuses the deliberately absent admission
manifest, exit one after 39.413381 seconds. Thus the test does not issue
a real admission or describe the repository as globally compliant.

All 18,332 tracked contents, the index and nine source pins match in
complete before/after inventories. Original inventory SHA256 is
ef9c2c211996901a93597b62f1259e130a60a979de65fe715423053515be7f89.
The two identical inventories are preserved losslessly once in
results/state_before_and_after.json.gz. Complete test and production
output, four receipt presentations with original hashes, and scope
metadata are in results/VALIDATION.json. Only private absolute paths
are normalized in presentations; original captures remain in the task
workspace. The publisher verifies process exits, log sizes/hashes,
source-commit pins and the compressed inventory roundtrip. This is
selected maintenance evidence, not independent review or a full suite.

No original scientific producer, prior failed capture, attribution
budget or historical seal is amended. The later operator-custody check
is published separately and is not part of the maintenance test envelope.

The read-only critical-operator audit is recorded in
../OPERATOR_PACKET_AUDIT_2026_10_16.md. Stored-output custody is checked,
not newly reproduced; the promised rank-deficient-domain control needs
its own successor. No prior source-coverage count is incremented.
The next scientific question remains the actual induced action on its
critical coefficient quotient and the admissible end law, not selection
of a representation or domain because it yields three generations.
An actual experiment must bring its own independent review and accepted
admission; this policy implementation supplies neither.
