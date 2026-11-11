# WP-0.7, series 3 — six patches

Built on main's `b80c68991` with series 2 applied as sent. Apply in order, after series 2:

```
git am relays/advisor_2026-11-10_audit/wp_0_7/series_2/000*.patch
git am relays/advisor_2026-11-10_audit/wp_0_7/series_3/000*.patch
```

Then regenerate the views (one page changes, `docs/views/THE_SPINE.md`).

The cover note, with what was run, the choices made and what is not mended:
`../../ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_3_SIX_PATCHES.md`. The card: `relays/cards/cld-advisor_C1_wp-0-7-series-3.md`.

| file | what it is |
|---|---|
| `0001` to `0006` | the patches, one commit each. `0004` closes the gap main's unseen case U9.b found in series 1 |
| `each_patchs_tests_on_the_commit_before_out.txt` | each patch's own tests run on the commit before it |
| `mains_own_tests_out.txt` | main's own tests of the gates, at main's head, with series 2, and with series 3: the summary lines |
| `planted_suite_on_the_series_out.txt` | the planted suite on the end of the series, unedited |
| `../variants_series_3.py`, `../variants_series_3_out.txt` | this seat's own 22 variants, committed before they ran, and their output on the series as sent, unedited |
| `../variants_series_3_first_whole_run_out.txt` | the variants' first whole run, on the series before its last change: its last variant found one more form of main's gap U9.b, which `0004` now closes |
| `../controls_with_every_gate_unable_to_fail.py`, `controls_with_every_gate_unable_to_fail_out.txt` | a read-out for PV16, committed with its expectations before it ran: which of the 53 controls fail when every gate is made unable to fail |
