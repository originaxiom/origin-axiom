# Preserved metadata-inspector error and correction

October 19, 2026. This is a metadata maintenance receipt, not a
scientific input, execution attestation or experimental review.

The first read-only metadata inspection verified specification/input
hashes but then failed on the role-policy lookup with
`key not found: "artifacts" (KeyError)`. The ad hoc inspector had assumed
the policy used the specification's `artifacts` key. The existing policy
actually uses `records`, as confirmed by reading its JSON envelope and
the unchanged provenance_policy.py source. No policy schema, scientific
source or scientific result was changed to make this inspection pass.

The corrected read-only inspector used `records` and verified all 39
artifact pins, the narrative design pin, both role-evidence pins, the
role artifact/evidence digests and absence of reserved outputs. The AST
inspection also found exactly eighteen matching test methods. These are
metadata/syntax checks, not execution of those scientific tests or the
new wrapper. The error is preserved here rather than called a clean
first attempt. No real admission manifest exists or is fabricated.
