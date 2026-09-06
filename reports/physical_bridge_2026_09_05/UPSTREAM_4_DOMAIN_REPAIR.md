# R11 — exact integer-domain adapter, after the first failure

STATUS 2026-09-06: before execution of this separate adapter.

BANKED IDENTITY: e066cdee seals the original design, source and eight
mathematical locks. The first producer failed before output creation;
the original test module gives eight shared-fixture errors in 4.52 s.
Both raw records are preserved in FAMILY_ACTION_FIRST_FAILURE.txt.
No action-comparison result has yet been computed.

PRIOR ART: R11's ten-head/source sweep is unchanged. Installed SymPy 1.14
`repmatrix.py:to_DM` and `domainmatrix.py:convert_to` were read. HNF
requires domain ZZ; multiplication of a QQ matrix by its denominator
retains QQ metadata even when all entries are integers. This is the
observed exception, not a conjectured physics obstruction.

Change exactly one interface: after the original integerize routine has
checked EVERY entry is integral, convert the DomainMatrix to ZZ explicitly
and convert back, verifying exact matrix equality. No integer truncation,
rounding, tolerance, root, action or scientific assertion changes.
The adapter temporarily replaces the module binding in a try/finally
context and restores it on both success and failure. No global SymPy
patching. It is for sequential runs, not shared-thread execution.

Pin the original source and test bytes; invoke all eight original
mathematical test functions against the repaired producer's fresh result
in a new parametrized test. Three additional locks check exact domain
conversion, rejection of nonintegral input, and binding restoration on an
exception. The original tests are NOT skipped, overwritten or relabelled
green; when run unadapted their fixture still raises the preserved error.

Seal this design, adapter and new tests before the rerun. Output is
family_action_rerun_1.json, opened exclusively after complete serialization.
No output overwrites. Original R11 hypotheses and physical fences all
stand; success would certify only its explicitly scoped algebraic map.
