# R11 — can the delegated mathematical locks actually fail?

STATUS 2026-09-06: after the first reporting gates, before these controls.

BANKED IDENTITY: the domain-adapted R11 producer completed and all eight
original mathematical locks plus three adapter tests passed. The first
staged reporting gate flags the delegating test as NO-ASSERT, in addition
to the older R6 np.testing finding. Its AST checker was read completely:
it looks only for direct assertions/selected attributes inside a function,
not assertions executed through `getattr(original, name)(result)`.

PRIOR ART: R6 already preserves a separate presealed mutation-control
approach. This is a fresh application to the NEW R11 finding, not a claim
that R6's mutations validate another function. The R11 sweep/provenance
remains unchanged. Original gate output is FAMILY_ACTION_FIRST_GATES.txt.

Test the actual delegating function, not a substitute: for each of its
eight names, call it with the fresh adapted producer's result and require
success. Then deep-copy that result, change one result datum contradicted
by that lock and require AssertionError. Mutations, fixed before execution:
lattice determinant, marked-map product count, literal-action fixed
dimension, internal-action matrix entry, E6 root-cycle count, covariance
count, SU3 representative entry, and a source hash length. Do not change
source, scientific design, expected lock values, checker or gate baseline.

All eight controls must accept the genuine result and reject their
specified corruption. Failure means the classification remains unresolved
for that lock; do not weaken the mutation. Even success establishes only
that these delegated predicates can fail; it does not prove complete test
coverage or a TOE and does not turn the unchanged static gate green.

Seal this file and the new tests before execution. Preserve first outputs.
This is a verifier control, not an empirical or new physics calculation.
