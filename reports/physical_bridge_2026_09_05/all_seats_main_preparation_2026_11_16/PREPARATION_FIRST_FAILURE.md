# Evidence-packaging first failures

2026-11-16. Two metadata extractions stopped before writing evidence.
The first assumed that an integration call occurred only once, and the
second made the same assumption about a torsion-point loop. Both
substrings had two source occurrences. No scientific code ran.

The committed metadata collector records every matching occurrence with
its exact line and whole-blob hash. The interpretations name the
applicable lines. This repairs provenance location, without changing
scientific source, mathematical claims or any recorded run.

A later metadata manifest check initially treated a repository-relative
manifest path as manifest-directory-relative and stopped at a missing
Git path. The successor resolves the documented path against the
repository when that exact blob exists, otherwise against the manifest
directory, and records the resolved path. No scientific run was involved.
