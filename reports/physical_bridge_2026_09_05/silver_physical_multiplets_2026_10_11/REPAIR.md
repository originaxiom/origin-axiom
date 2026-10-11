# Reference zero-field repair before replay

Original pre-execution seal:9e434bfaa63cff9450959d54384e1a6ad969546a.
The original native producer passed96 predicates unchanged (669.162103s).
Its output is preserved and its code, inputs and proof are not changed.
The original Fraction reference failed before any census: its optimized
sparse product skipped zero terms and left exact zero entries as Python
integers. Legacy Gaussian reconstruction requires field-valued zeros;
the arithmetic-value-only comparator did not check this API obligation.

REFERENCE_FIRST_FAILED.log and its receipt preserve the literal failure.
This is a verifier/API defect, not a negative about the construction.
The sparse product now initializes every entry in the actual input field,
retains integer-only multiplication, and rejects mixed quadratic fields.
Two distinct quadratic fields, zero-entry type preservation, nonrational
arithmetic and a wrong mixed-field control are checked BEFORE reconstruction.
No target count, boundary plane, cocycle, anomaly criterion or native
result was tuned. RESEAL_REPAIR.json and appended SEAL_LEDGER row freeze
the repaired reference before replay. All outside/full-suite/main-bank and
physical-completion duties remain. Same author, not external review.

Focused12 tests may run within the eight-packet70-test regression rather
than a redundant second invocation. The unchanged native census is live
there; no stored stdout is substituted for mathematical test assertions.
