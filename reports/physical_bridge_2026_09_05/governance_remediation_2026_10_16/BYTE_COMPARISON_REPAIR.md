# Identical bytes were falsely labelled as changed

The retained HISTORICAL_DESIGN_AUDIT.json reports five of six R40 files
unchanged. Its own hash fields already contradict the remaining false
label: COEFFICIENT_PARENT_PRIOR.md has the same SHA256 in both columns.
A direct Git comparison with the sealed source is also empty.

The new metadata helper compared UTF-8 text returned by Git with binary
file data. On this Ruby version, identical non-ASCII bytes with those
different encoding tags compare unequal. The original helper and its
faulty result are retained; this is not evidence of a changed R40 file.
The repaired comparison uses binary strings on both sides and rejects
a deliberately changed byte. No scientific producer, old seal, expected
physics or numerical tolerance changes.

The interrupted helper's process handle and private temporary capture
directory are no longer available in this environment. Its generated
JSON remains in the worktree, but a raw success receipt is not invented.
Earlier path-normalized captures and their hashes are already committed;
this does not assert that their old private temporary originals remain
accessible now. New captures use a workspace directory outside the Git
checkout, and durable evidence is published before relying on its survival.

This is a post-reading metadata repair, not a retrospective scientific
preregistration or historical execution-time certificate. The actual
attribution and provenance rule questions remain open with main.
