# Architecture verification: implemented, unrun, not admitted

2026-11-08. The analytical proof and design were committed and pushed
at `0437f7a84` before either new Python source was written.

## Present evidence

- `register_exact.py`: exact integer/Fraction producer, implemented.
- `test_register_architecture.py`: seven scientific control methods,
  implemented in the declared source. No extra scientific dependency
  beyond the producer and Python standard library was introduced.
- Static AST parsing, method-population count, import inventory,
  whitespace and source-hash metadata checks completed. These operations
  read source text and did not import it.
- The seven controls are **UNRUN, NOT IMPORTED, NOT COLLECTED**.
  There is no mathematical PASS/FAIL output, numerical result or claimed
  independent review. The all-word proofs remain author-unreviewed.

Different checks use graph edge chains, Schreier rewriting, tensor
coefficients, integer three-by-three matrix multiplication and permutation
composition. They share the declared underlying group/basis data; this
is not independent reconstruction of physical geometry or the complete
existing programme.

## Remaining execution duties

This is **not** a complete execution/admission seal. The declared source
inventory must be bound to the actual clean checkout, runtime and exact
gated command. Existing strict admission/custody infrastructure, its
dependency closure and environment must be pinned without weakening the
repository's rules. Scientific output locations and before/after source
custody must be declared. Then obtain independent non-authoring proof/code
review and main's separate exact execution acceptance. Earlier packages'
reviews/acceptances do not cover these new controls.

The eventual focused mathematical command would run this source's seven
unittest methods from its own directory. No such command has run. A bare
direct command is not a substitute for the required gated wrapper.

Review must check coverage against `DESIGN.md`, including what these
finite controls cannot prove: no fixed example population establishes
all-word faithfulness, all-prime separation or cofinality of the full
joint tower. Those quantifiers require the separate analytical arguments.

Any first scientific failure must be preserved before a source repair.
Repairs receive successor seals. Do not report syntactic metadata as
tests passing, a proposed witness as verified execution, or this package
as physical-input reduction. No old frozen package or canonical document
is altered by implementation.
