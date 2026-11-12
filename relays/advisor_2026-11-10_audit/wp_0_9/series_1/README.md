# WP-0.9, series 1 — two patches

Built on main's `323f92327` with series 2, 3 and 4 of WP-0.7 applied as sent. Apply after them:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_2/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_3/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_4/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_9/series_1/000*.patch
```

Then regenerate the views: the front page's generated block gains two rows, and `docs/views/THE_SPINE.md` changes.
They apply so on `323f92327` and on `0dda7b472`, 22 commits, no conflict. What reads "on the series" below was read on
the same tree in one commit on `323f92327`.

The cover note: `../../ADVISOR_TO_CC_2026-11-12_WP_0_9_SERIES_1_TWO_PATCHES.md`. The card:
`relays/cards/cld-advisor_C4_wp-0-9-series-1.md`.

| file | what it is |
|---|---|
| `0001`, `0002` | the patches, one commit each |
| `../the_suites_five_cases_what_is_expected.md` | what was expected of the suite's five new cases, committed before any run |
| `the_five_new_cases_on_mains_head_out.txt` | the five and their twins on main's `0dda7b472`, unedited: not caught 5 of 5, five twins pass |
| `the_five_new_cases_on_mains_head_first_run_out.txt` | the first run of the same: one twin could not be planted, by a mistake in the suite's helper that the suite itself reported |
| `the_suite_on_the_series_out.txt` | the whole suite, 37 cases, on the series, unedited |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's own tests run on the commit before it |
| `mains_own_tests_out.txt` | main's own tests of the gates, the views and the verdict schema at the base and on the series: the summary lines and the names of what fails |
| `all_53_gates_on_the_series_out.txt` | every gate's line on the series |
| `../what_stands_for_the_fourteen.py`, `…_out.txt` | what stands in the commit for each arc the candidate runs on: a mechanical read |
| `../what_each_word_would_name_for_the_fourteen.py`, `…_out.txt`, `….json` | which of the five words each of the fourteen could carry by its own files, and what the word would name |
| `../variants_series_1.py`, `../variants_series_1_out.txt` | this seat's own ten variants, committed before they ran, and their output, unedited |
| `../variants_series_1_first_run_out.txt` | the variants' first run, which stopped at the third by the same mistake in its harness |
