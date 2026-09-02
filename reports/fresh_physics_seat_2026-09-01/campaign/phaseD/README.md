# Phase D — the certificates on the two heads Phase B never digested

Phase B's reader packets were built from four heads; `origin/codex/seat-r001` (codex's certificates r006–r034,
38 scripts) and `origin/claude/outside-bench` (cloud's `outside_bench/certificates/`, 147 scripts) were swept for
text only. Ten sweep verdicts are OPEN_LATER because the answer lives there, and the SM end of the chain (hypercharge,
Yukawa no-go, breaking chain, SUSY no-go, height-308 witness) is certified on those heads and cited on main.

- **D-1 (agents, mechanical):** 38 packets (`packets/`), one sonnet agent each, run every certificate in an isolated
  worktree of its own head (600 s cap, no edits, no commits) and report PASS / FAIL / CANNOT_RUN / TIMEOUT /
  NOT_A_CERTIFICATE with what the script certifies, its verbatim verdict lines and its external inputs
  (`workflow_phaseD_certificates.js`, run wf_c35d1039-be1).
- **D-2 (seat):** every FAIL and every PASS that main cites as load-bearing is re-read; the load-bearing ones
  (hypercharge forcing, up-Yukawa = 0, the 27-generation obstruction, breaking-chain uniqueness) get R-cells or an
  explicit "certified-on-head-X, reproduced-here / not reproducible here" line in the relay.
- **D-3:** OPEN_LATER verdicts re-adjudicated; synthesis and relay updated.
