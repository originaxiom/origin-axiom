# Successor execution and review boundary

October 18, 2026. Author inventory awaiting independent acceptance.
The intended 32 mathematical controls remain unrun.

## Scientific closure

run_checks.py loads the standard library and scripts/gates/tracked_state.py
before admission. Only after the strict prospective gate and pre-import
custody checks does it import checks.py. That module imports controls.py,
extended_checks.py and SymPy. The latter two import standard-library
utilities and SymPy. controls.py loads the retained joined_background.py,
which loads cross_branch_positives.py. Both producer hashes are checked
internally as well as in the specification.

The successor copies the original control helpers unchanged. The tests
retain the old 28 methods, add the two convention controls, and add two
instrument-coverage methods. The newly called R85 fixtures and R75
algebra/root functions use the same already-pinned source closure and
no data files. Neither producer main nor R85 spectrum nor the other R75
control groups is called. Generated matrices replace no stored verdict
flag; the computations, when admitted, will construct them afresh.

External dependencies are version-pinned, not reproducible-build hashes.
The intended interpreter's metadata was confirmed as CPython 3.12.1,
SymPy 1.14.0 and mpmath 1.3.0 without scientific imports.

## Governance closure

The subprocess entrypoint is scripts/gates/prospective_strict.py. It
imports tracked_state.py and the unchanged prospective.py, which imports
gates.py and provenance_policy.py. The aggregate's existing local helpers
are check_path_references.py, check_test_vacuity.py, retraction_sweep.py,
relay_debt.py, doc_currency.py, representation_sweep.py and views/generate.py.
These source bytes remain pinned. Git and standard-library processes are
used; they are not scientific producers.

Current policy files, ledgers, Git evidence and generated views remain
the base gate's broader governance context. This context is evaluated at
the execution HEAD, not frozen forever at the scientific seal. Review
and acceptance are separately pinned later. The generated-view gate can
write tracked views; strict pre/post snapshots reject resulting changes.
Do not run that aggregate in the author's dirty worktree.

The legacy prospective.py is unchanged to preserve the original seal.
Its known index blind spot remains a historical defect. The successor
uses the strict wrapper and its own pre-import/post-run snapshots; a
bare legacy-gate pass is not sufficient for this experiment.

## Review inputs and evidence

The six original analytical notes are included unchanged as inputs.
REPAIRS explicitly corrects their register-order hypothesis and scopes
the selected-assembly wording through the owner's whole-architecture
clarification. The original design, review intake and retained AR/R85/R86
proofs preserve provenance and scopes. A rank test assuming the graph's
cohomology is not a replacement for its asphericity/peripheral-injectivity
proof. An exterior-algebra sign test is not a B1043 or E6 coupling value.

runner_policy_checks.py and the two focused gate-test files are separate
infrastructure sources, not members of the 32-test scientific suite.
Their synthetic review records exist only in temporary fixtures and
do not grant real admission. Their captured attempts and engineering
plan are evidence of machinery checks, not physics results.
