# Phase C — recompute the load-bearing claims Phase B could not mark COMPUTED-and-reproducible

Input: `../phaseB/synthesis/load_bearing_unrecomputed.tsv` (1106 rows; indexed copy `unrecomputed_indexed.json`).

- **C-1 rerun tier (398 COMPUTED rows, 292 arcs, 59 packets in `packets/`).** Cheap agents (sonnet) rerun the committed
  script behind each claim in an isolated git worktree of the right head (main, paper/structure-genesis-first,
  claude/new-session-qor5up, audit/b775-braver-questions), 600 s per script, no edits, no commits, and report
  REPRODUCES / DIFFERS / PARTIAL / CANNOT_RUN / NOT_A_COMPUTATION with verbatim printed numbers
  (`workflow_phaseC_reruns.js`; run wf_51a83ad2-576; results land in `results/`). Agents run scripts and transcribe
  numbers; they do not judge.
- **C-2 seat judgment.** Every DIFFERS / PARTIAL is re-read and, where chain-relevant, recomputed by the seat as an
  R-cell (`../../recompute/R43+`).
- **C-3 asserted/imported tier (708 rows).** Triage view `asserted_triage_view.txt`; the tool-checkable ones (SnapPy
  census facts, PARI class numbers / units / discriminants, Lie-algebra dimensions and branchings) are verified by the
  seat; literature-only ones are listed as such.
- **C-4** synthesis §4 and the relay note updated; commit and push.

Owner policy applied: cheap agents only for mechanical reruns; verdicts are the seat's; nothing banked to main.
