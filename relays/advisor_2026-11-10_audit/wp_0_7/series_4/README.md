# WP-0.7, series 4 — its first three patches

Built on main's `f9e70c167` with series 2 and 3 applied as sent. Apply in order, after them:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_2/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_3/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_4/000*.patch
```

Then regenerate the views (one page changes, `docs/views/THE_SPINE.md`).

The cover note: `../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_4_ITS_FIRST_THREE_PATCHES.md`. The card:
`relays/cards/cld-advisor_C2_wp-0-7-series-4.md`. The rest of the series, the six cases the suite lists as manual, follows.

| file | what it is |
|---|---|
| `0001` to `0003` | the patches, one commit each |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's own tests run on the commit before it |
| `mains_own_tests_out.txt` | main's own tests of the gates at main's head, with series 2 and 3, and with these three: the summary lines |
| `the_three_new_cases_on_mains_head_out.txt` | the suite's three new cases on main's head: not caught, 3 of 3 |
| `planted_suite_on_the_patches_out.txt` | the whole suite on the patches, unedited: 24 of 24 |
| `../variants_series_4_part_1.py`, `../variants_series_4_part_1_out.txt` | this seat's own eleven variants, committed before they ran, and their output, unedited |
| `../variants_series_4_part_1_first_run_out.txt` | the variants' first run: 9 of 11, two expectations failing on main's count of landings and not on the mend |
