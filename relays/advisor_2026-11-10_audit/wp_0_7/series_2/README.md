# WP-0.7, series 2 — six patches

Built on main's `e6298271a` with series 1 applied. Apply in order, after series 1:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_1/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_2/000*.patch
```

Then regenerate the views (one page changes, `docs/views/THE_SPINE.md`).

The cover note, with what was run and the choices made: `../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_2_SIX_PATCHES.md`.

| file | what it is |
|---|---|
| `0001` to `0006` | the patches, one commit each |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's tests run on the commit before it |
| `mains_own_tests_out.txt` | main's own tests of the gates, at main's head, with series 1 and with series 2: the summary lines |
| `planted_suite_on_the_series_out.txt` | the planted suite on the end of the series, unedited: 16 of 21 |
| `../variants_series_2.py`, `../variants_series_2_out.txt` | this seat's own fourteen variants, committed before they ran, and their output, unedited |
