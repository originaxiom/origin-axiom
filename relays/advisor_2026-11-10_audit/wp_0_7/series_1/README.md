# WP-0.7, series 1 — four patches

Built on `ea41e6fc9`. Apply in order on main's head:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_1/000*.patch
```

Then regenerate the views (one page changes, `docs/views/THE_SPINE.md`, by one lock).

The cover note, with what was run and the choices made: `../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_1_FOUR_PATCHES.md`.

| file | what it is |
|---|---|
| `0001` to `0004` | the patches, one commit each |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's tests run on the commit before it: the names of those that fail |
| `mains_own_tests_base_and_series_out.txt` | main's own tests of the gates, at the base with no patch and on the series: the summary lines |
| `planted_suite_on_the_series_out.txt` | the planted suite on the end of the series, unedited: 11 of 21 |
| `../variants_series_1.py`, `../variants_series_1_out.txt` | this seat's own twelve variants, committed before they ran, and their output, unedited |
