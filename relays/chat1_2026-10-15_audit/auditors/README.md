# The auditors' scripts (2026-10-15)

These are the read-only auditors' own scripts and small outputs, filed as they wrote them so their checks can be
re-run. chat1 scanned them for side effects and did not otherwise review them.

- `A_condensate/`, `B_first_row/`, `C_scale/`, `D_selection/`: the four audits of `../AUDIT_OF_THE_NEGATIVES.md`.
- `step3a_referee/`: the referee of step 3a's scoring.
- `post_hoc_referee/`: the referee of the completions post hoc.
- `lift_review/`: LIFT's pre-seal review and chat1's own plumbing for it, with its own README.
- `lift_referee/`: the referee of LIFT's scoring (`an1.py`–`an4.py`, read-only analyses of the committed output).

Absolute sandbox paths have been replaced by `<scratch>` and `<repo>` (WORKING_RULES §11). To re-run a script, point
those placeholders at a scratch directory and a checkout of the repository.
