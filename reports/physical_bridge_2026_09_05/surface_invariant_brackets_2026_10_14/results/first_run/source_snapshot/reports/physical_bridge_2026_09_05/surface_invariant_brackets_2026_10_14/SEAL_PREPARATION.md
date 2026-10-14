# Mechanical preparation failure, before any scientific execution

The first metadata-generator launch exited1 before making INPUTS,
ARTIFACT_HASHES or appending the ledger. Ruby Pathname's overloaded
addition treated the final '/INPUTS.json' component as an absolute
replacement; the sandbox rejected that write as Operation not permitted.
The subsequent explicit stage failed for the absent INPUTS; commit
reported nothing added. No scientific producer ran, no seal was claimed,
and no outside-workspace file or Git commit was created.

The faulty expressions were root+local+'/INPUTS.json' and the analogous
ARTIFACT_HASHES expression. They are replaced with root.join(local,name).
Source hashing itself only read the enumerated relative paths.
This is a PRE-SEAL instrument-preparation correction, not a repaired
mathematical result or a post hoc prediction. No permission escalation
was used to write the incorrect target.
