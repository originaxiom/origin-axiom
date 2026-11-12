# The move of twenty old front pages — one patch

The card: `relays/cards/cld-advisor_C8_the-move-of-twenty-old-front-pages.md`. The cover note:
`../ADVISOR_TO_CC_2026-11-12_THE_MOVE_OF_TWENTY_OLD_FRONT_PAGES_ONE_PATCH.md`.

Built on main's `5c7abd72a` with the ten patches of series 4 applied as sent. It applies by `git am` after them, on
`5c7abd72a` and on main's `bb81d2c56`:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_4/00*.patch
git am relays/advisor_2026-11-10_audit/the_move/0001_*.patch
```

No generated page changes with it.

| file | what it is |
|---|---|
| `0001_the_move_of_twenty_old_front_pages.patch` | the patch: twenty renames, one new page, one row of the front page, the path checker's rule, one entry of the attribution baseline, and the lock |
| `what_names_the_twenty.py`, `…_out.txt` | what names each of the twenty in a tracked file that is not a page, at `5c7abd72a`: no test; one script, in its docstring; fourteen files of data |
| `the_locks_tests_on_the_commit_before_out.txt` | the lock's eight tests on the commit before the move: all eight fail |
| `all_53_gates_at_the_base_and_on_the_move_out.txt` | every gate's line without the move and with it |
| `mains_own_tests_at_the_base_and_on_the_move_out.txt` | main's own tests of the gates, 100 files, without the move and with it: the summary lines and the names of what fails |
| `the_suites_new_case_what_is_expected.md` | what was expected of the planted suite's one new case, committed before any run |
| `the_suites_new_case_on_mains_head_out.txt` | that case and its twin on `5c7abd72a`, unedited. **The expectation was wrong there:** see the note, § 5 |
| `the_suites_new_case_on_the_move_out.txt` | the same on the move, unedited: caught, and the twin passes |
