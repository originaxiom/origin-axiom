# R80a — Review 80's entry and its arc B1898, one patch

The first series of main's M14, alone. The cover note is
`../ADVISOR_TO_CC_2026-11-12_R80A_REVIEW_80S_ENTRY_AND_ITS_ARC_ONE_PATCH.md`; the card is
`relays/cards/cld-advisor_C9_r80a-review-80s-entry-and-its-arc.md`.

Built on main's `10fbbc1c2`:

```
git am relays/advisor_2026-11-10_audit/r80a/0001_review_80_entered_with_its_arc_b1898.patch
```

The tree it gives is `859672ca2746`. The patch carries eight generated files, made by main's own generators on that
tree: four pages under `docs/views/`, the state block of `README.md`, `scripts/atlas/atlas_data.json`, and the page
and data of `frontier/B1883_where_we_stand/`. If main's head has moved, they are made again after the patch.

| file | what it is |
|---|---|
| `0001_review_80_entered_with_its_arc_b1898.patch` | the patch: 54 files |
| `all_53_gates_on_the_patch_out.txt` | every gate's line on the patch: 53 of 53 pass |
| `the_tests_that_read_a_changed_page_out.txt` | the 291 test files that read a page the patch changes; the summary lines at main's head and on the patch |
| `mains_checks_made_again_out.txt` | what each check main kept gave when it was made again, and where it differs |
| `the_lock_of_b1898_against_planted_changes.py`, `…_out.txt` | the arc's lock and three gates against 17 planted changes, each put back by git: 17 caught |
| `the_planted_suite_on_the_commit_read_out.txt` | the enforcement package's suite on `c40446392`: 5 of 5 controls, 24 of 37 cases read |
| `the_full_suite_on_a_fresh_clone_of_the_patch_out.txt`, `the_eight_in_fresh_clones.py` | added after sending: the full suite by the review's tool on the patch, 8 failed and 8,566 passed; the eight run alone in a fresh clone of main's head and of the patch, where the same eight fail. The cover note's § 9 |

Still to come in this folder: the full suite on a fresh clone of the patch, which was running when this was sent.
*[Added 2026-11-12: it is here, in the table's last row.]*
