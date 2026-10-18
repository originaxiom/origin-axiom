# Verification infrastructure checks

October 18, 2026. Maintenance scope, not scientific preregistration.
Run no controls.py, checks.py, extended_checks.py, retained mathematical
producer or prospective aggregate against the real working tree.

Use CPython 3.12.1 with bytecode disabled. The checks are:

1. AST parsing and literal test-name inventory of the proposed sources,
   without import or collection. Expected mathematical method count: 32.
2. runner_policy_checks.py, which imports the standard-library runner
   and strict Git snapshot helper but substitutes only dummy admission,
   state and test-module fixtures. Expected infrastructure methods: 20.
3. pytest restricted to tests/test_strict_tracked_state.py and
   tests/test_prospective_experiment_gate.py, with --noconftest,
   PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 and -p no:cacheprovider. This excludes
   the ordinary conftest's mpmath import and plugin discovery. The gate
   tests use synthetic policy/review/acceptance records solely in their
   temporary repositories. The aggregate is limited to their fixture
   gates, not the real repository's generated views or scientific tests.

Save each attempt separately, with source hashes and exit status. A failed
test requires correction and another retained attempt, not overwriting
its record. These checks do not authorize mathematical execution or
replace independent review, main acceptance, prospective admission,
the exact-tree suite or publication requirements.
