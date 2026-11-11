# WP-0.7, series 4 — eight patches

Patches `0001` to `0003` were built on main's `f9e70c167` and sent first. Patches `0004` to `0008` were built on main's
`323f92327`. The three series apply in order by `git am` on `323f92327`, with no conflict:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_2/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_3/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_4/000*.patch
```

Then regenerate the views (one page changes, `docs/views/THE_SPINE.md`).

Applied so, they are twenty commits, and `review-fires` counts each as a landing: 66 since the last review, past the
end of the waiver. That count is main's. Everything below that reads "on the series" was read on the same tree in
one commit on `323f92327`, where the count is 47.

The cover notes: `../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_4_ITS_FIRST_THREE_PATCHES.md` and
`../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_4_ITS_LAST_FIVE_PATCHES.md`. The card:
`relays/cards/cld-advisor_C2_wp-0-7-series-4.md`.

## The first three (sent at `03e024250`)

| file | what it is |
|---|---|
| `0001` to `0003` | the patches, one commit each |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's own tests run on the commit before it |
| `mains_own_tests_out.txt` | main's own tests of the gates at `f9e70c167`, with series 2 and 3, and with these three: the summary lines |
| `the_three_new_cases_on_mains_head_out.txt` | the suite's three new cases on `f9e70c167`: not caught, 3 of 3 |
| `planted_suite_on_the_patches_out.txt` | the whole suite on the three patches, unedited: 24 of 24 |
| `../variants_series_4_part_1.py`, `../variants_series_4_part_1_out.txt` | this seat's own eleven variants, committed before they ran, and their output, unedited |
| `../variants_series_4_part_1_first_run_out.txt` | the variants' first run: 9 of 11, two expectations failing on main's count of landings and not on the mend |

## The last five

| file | what it is |
|---|---|
| `0004` to `0008` | the patches, one commit each |
| `the_suites_new_cases_what_is_expected.md` | what was expected of the suite's eight new cases, committed before any run |
| `the_suite_on_mains_head_out.txt` | the whole suite, 32 cases, on `323f92327`, unedited: 14 of 32 caught, as expected |
| `the_suite_on_mains_new_head_out.txt` | the same on main's `0dda7b472`, unedited: 14 of 32 caught |
| `the_suite_on_the_series_out.txt` | the whole suite on the series, unedited: 32 of 32 caught, 5 of 5 controls, 6 of 6 twins pass |
| `each_of_the_five_patchs_tests_on_the_commit_before_out.txt` | each patch's own tests run on the commit before it |
| `mains_own_tests_part_2_out.txt` | main's own tests of the gates at `323f92327`, at the base of the five, and on the series: the summary lines and the names of what fails |
| `all_53_gates_on_the_series_out.txt` | every gate's line on the series |
| `how_many_lock_paths_the_gate_read.py`, `…_out.txt` | the measurement behind `0006`, on `323f92327` |
| `what_a_run_of_mains_fast_lane_rewrites_out.txt` | the tracked files that one run of main's fast lane changed, at `323f92327`: the measurement behind `0008` |
| `../variants_series_4_part_2.py`, `../variants_series_4_part_2_out.txt` | this seat's own twenty-five variants, committed before they ran, and their output, unedited |
| `../variants_series_4_part_2_first_run_out.txt` | the variants' first run: 24 of 25, one variant's plant refused by an older rule and not the one it asks about |
