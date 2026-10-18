# Successor infrastructure results

October 18, 2026. The runner's 20 sentinel cases passed. The focused
strict-state and base-admission fixture suite passed 51 tests in
74.68 seconds. Both first attempts exited zero; the captured outputs
and tested-source hashes are in engineering/attempt_01_runner.log and
engineering/attempt_01_strict_git.log. These are maintenance tests, not
any of the 32 mathematical controls and not prospective admission.

The runner cases retain the old refusal controls and add before/after
index checks, import failure, import and test interruption, and failure
of custody reporting without replacement of the original exception.
The real-Git cases verify unstaged, staged and cancelling index/worktree
differences. In the latter case the legacy HEAD-to-worktree diff is empty
while the strict check rejects the state. Positive synthetic admission
still preserves historical noncompliance; the wrapper cannot override
base-gate refusal or ignore state changed during that gate.

The pytest invocation was limited to the two infrastructure files with
plugin autoload, conftest and cache generation disabled. No scientific
control, retained producer or real-repository governance aggregate ran.
Temporary review/acceptance records are explicitly synthetic fixtures.

AST inspection, without import or collection, found the same 32 unique
mathematical test methods named in the runner's literal inventory. The
four additions are the two convention checks and two inherited instrument
coverage methods. Syntax/inventory agreement is not mathematical success.

These passing cases are not a security proof or a guarantee against
concurrent changes, hard process termination or storage failure. A clean,
quiescent execution checkout, separate exact-source review, main acceptance,
prospective admission and the publication checks remain required.
