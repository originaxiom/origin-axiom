# P-595: the web seat's sealed exact-end look, re-run on main's tree (2026-11-04, S303)

- The rule is 5215f337a. The instrument is `relays/chat1_2026-10-28_exact_end/exact_end_look.py` at 530f964a3. Its sealed
  output is 4aa66ca45 (`exact_end_look_run.txt`).
- Main's tree is 52dc780da, main's head at the run's time. B1741's compare.py hash at that commit matches the
  instrument's assertion: 6308ed93e53ab99522cf…
- **The command:**
  - git worktree of main at 52dc780da;
  - git worktree of the web seat's branch at 4aa66ca45;
  - from the seat worktree's relay folder: `python3 -B exact_end_look.py <main worktree>`;
  - its own Pool(2), single-threaded BLAS.
- **The result:** identical to the sealed output in every row. The diff (`p595_diff_against_the_seats_output.txt`) holds
  only the runtime line and the seat file's trailing exit line.
