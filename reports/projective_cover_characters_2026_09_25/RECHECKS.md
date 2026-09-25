# F17 execution, reading and custody

Entry was clean at f45e8c39 (1c402e). Active local branch remains
audit/fork-2026-09-20. No old scientific process was inherited.

## Fresh intake

The earlier fetch attempts in this continuation are retained as failed
operations: default SSH DNS failure cd7396, escalated SSH public-key
rejection 3ece28, HTTPS rewritten back to SSH d22697. None changed the
scientific tree. Public HTTPS with GIT_CONFIG_GLOBAL=/dev/null,
GIT_CONFIG_NOSYSTEM=1 and an empty per-command credential helper then
succeeded (4a85dc, exit 0). Saved Git configuration was not modified.
No keys or credential values were captured, and no branch was merged.

Read-only public ls-remote df1103 returned exactly seven advertised heads:

    audit/physical-bridge-2026-09-05 20a5c718eec9adfd2f048e37da546cc8b6064540
    claude/outside-bench 13d2c5b63ba7a3db9ea880016a43d3c688cee954
    claude/paper-review-verification-kaz3f5 cf12bd6ed25eacf5954ff69c8c4a5b4e92b495fc
    claude/physics-seat-evaluation-8dkbrl 659487bbd93c7990c4686a8b86985b6b66efedc4
    claude/standard-model-derivation-0qt6ao 235325396b2db79c78df303531af6878931b00f2
    main 987c0c8fdb07f7f79beccd6c82c1154e3e75fa47
    sep16-branch 2795e46cc992d9d4720dd5446adc3bb7ce5906a6

They match the fetched tracking refs. Historical retained refs were not
pruned or relabeled as currently advertised branches. No full fresh
body-reading claim follows from a fetch or matching head hashes.

Personal full readings: B1279 FINDINGS (176131) and producer (4b5c14),
B1274 tower producer (68316b), B1278 FINDINGS (220cb8), R44 canonical
report (176131), R46 interaction report and R47 diagnostic design
(36bf57), R47 neutral design (bcb25c). B350 and B437, including the
latter's retractions, were read through EOF in 8cf7d5 as next-step
prior art. They are not adopted as new physical claims. R47's neutral
proof was read through EOF during the read-only run in 87fc80; it is
not an independently certified input to F17. Its global hypotheses
and different base metric remain explicit.

The broad already-banked query 6573a2 returned 299 hits and 29 settled
multi-term arcs; be3e90 returned 229 and 26 for another broad query.
Those are retrieval counts, not discoveries or an absence certificate.
Failed guessed B1279 path/glob lookups and the wrong whole-picture path
in b87e78 were resolved against actual Git trees/file lists. Their
errors/empty downstream counts were NOT taken as evidence of absence.
No subagent or independent scientific reviewer participated.

## Pre-execution seal

DESIGN, PROOF, producer, tests and all three transitive repository
imports were hashed in ef727b. Explicit staging, whitespace check and
local commit **1b89cdc30e250729ccdc5fc32c9a930c1cacbae6** completed
in 864059. The tree was clean before the first scientific execution.
Python 3.12.1, SymPy 1.14.0, pytest 9.0.3 (125af3).

Commands and every raw returned chunk/session/exit are in
[EXECUTION.json](EXECUTION.json). Actual final exits, not inferred
completion from partial progress:

- New tests: session 7232, 5deeb2/f66dd6/aea3b6/06a43d;
  exit 0, **13 passed in 98.79s**.
- Exact producer: session 51076,
  fb6c18/e24d9b/e53fb1/ae96f4; exit 0. Two complete JSON lines,
  each 21,987 returned characters, retained before displaying summaries.
- Unchanged F14/F16 tests: session 23915,
  0c5bf3/9c4244/5b7405/c8dcb9/fc3103/cb489b; exit 0,
  **52 passed in 216.81s**.

Output files concatenate actual stdout with a final newline:
[new tests](TEST_OUTPUT.txt), [unchanged tests](ANTECEDENT_OUTPUT.txt),
[all exact rows](EXACT_WITNESSES.jsonl). The witness producer is the same
sealed implementation, not independent confirmation of its mathematics.
The unchanged suite is a focused regression, not a full-repository pass.

No source changes, regenerations or external scientific landings occurred
during these runs. 063ea8 confirmed the four new scientific hashes and a
clean tree while the last suite was pending; 18c57c confirmed unchanged
transitive imports and a clean tree AFTER its final exit. Only then were
outputs and reports added. No failure, correction or interrupted run
occurred in F17. Earlier cells' failures remain preserved separately.

The proof's analytic consequences are authored applications, not
verified by finite tests alone. The report does not count the same
source implementation as multiple independent confirmations.

Final report validation 1bd800 rechecked all seven sealed hashes, both
complete 64-row tables, all chain/relator/pairing flags and dual ranks,
every terminal exit, the two test summaries and local report links.
The JSONL is explicitly force-staged despite the generic ignore rule.
