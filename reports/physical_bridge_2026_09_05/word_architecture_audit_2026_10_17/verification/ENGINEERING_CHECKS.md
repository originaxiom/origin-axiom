# Runner refusal checks, not mathematical results

October 18, 2026. Fourteen non-scientific infrastructure tests pass after
one test-harness correction. No mathematical control was imported,
collected or executed. No prospective experiment was admitted.

The standard-library harness runner_policy_checks.py loads only the
runner, replaces the admission subprocess and Git queries with isolated
sentinels, and uses a temporary dummy test module. These replacements
exist only in this engineering harness; the scientific entrypoint has
no bypass flag. Dummy admission messages are never actual review or
acceptance records. Temporary sentinel outputs are not science receipts.

## First attempt and correction

The first attempt stopped every case at the repository-directory check:
seven assertion failures and seven errors. The harness compared the
macOS temporary-directory alias with its resolved physical path. The
runner correctly rejected the mismatch. Resolving the harness's root
before patching it corrected the fixture; the production runner was not
weakened. The failure was replayed unchanged to preserve a full diagnostic
in engineering/attempt_01_path_alias_failure.log. Absolute repository
paths are redacted there; the raw diagnostic is retained outside Git.

The one-line harness change was:

    Path(temporary_directory) -> Path(temporary_directory).resolve()

The succeeding capture is engineering/attempt_02_policy_checks.log, with
the tested harness and runner digests. It reports fourteen tests, zero
failures/errors and exit status zero. Both outcomes remain in the record.

## What passed

- Rejected, malformed or non-positive admission cannot reach the module
  loading stage or create science outputs.
- An altered command, extra output, changed runtime or changed pinned
  file cannot reach that stage.
- An existing output is preserved, not overwritten.
- A mismatched test population halts before a test starts.
- Skipped tests and expected failures cannot produce a passing result.
- Source or tracked-state changes during a run prevent a passing result.
- A complete one-test dummy run reaches the intended recording path.

The runtime command was Python 3.12.1, bytecode disabled, on
runner_policy_checks.py. This is the author's engineering validation,
not non-authoring review, a security proof, the full repository suite,
or any of the seventeen planned mathematical tests.

## Still required

Independent review must challenge both the proofs and the runner. In
particular these sentinels do not prove the actual prospective checker's
independence checks, source inventory completeness, all filesystem-race
cases, or an adversarially modified interpreter. Those are not claimed.
The design/specification remain unsealed; genuine review and main
acceptance are absent. Mathematical execution is still prohibited until
the real prospective admission succeeds in a clean checkout.
