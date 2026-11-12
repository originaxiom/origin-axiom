# Main to the builder, 2026-11-12, second folder: two more drafts, and three corrected verdict files

*Main. The rules for building from this folder are those of the first folder's README
(`docs/handoffs/MAIN_TO_BUILDER_2026-11-12/README.md`). Everything here is main's own work; none of any other
session's code was run to make it. 0 of 19.*

## What is here

| folder | what it is | what is to be built from it |
|---|---|---|
| `wp16_all_histories_together/` | the owner's selection test of 2026-11-12 in both parts, and the law that came out of it: the sum over all histories as a product over threads, the rates at which sectors cancel, the first sector beyond the bound, the record's triplet, and what the swap does to the sectors. The page and the verdict line are in `arc_draft/`; the rule's three texts are `RULE_draft.md` | ONE arc, B1902, and the rule. **This replaces `wp16_the_selection_test/` of the first folder,** whose scripts are all here in their later form |
| `wp15_the_thread_results/` | the first step of the plan's package on the root and the thread results: the weave rows of the harvest recomputed on main's own instrument | one arc, B1903. The three rows already in the first folder's `x_c1a_on_main/` (908, 914, 917) are filed with it |
| `verdicts_corrected/` | the verdict drafts of the first folder's three mathematics arcs, with the scope's four parts as strings | they replace the first folder's three: there the scope's hypotheses were a list, which the verdict schema refuses |

## Notes for building

- **Paths.** The scripts find the repository's root as two folders above themselves, which is right where they were
  written and wrong inside an arc. Where a script imports another arc's module (`kernel_site.py` imports B1492's,
  B1493's and B1602's; several import `rates_by_sector.py` beside them), make it look upward for the folder that holds
  `frontier/`, as B1602's `forced_every.py` does.
- **What reads what.** `the_weaves_zeta.py` and `mirror_pairs_of_sectors.py` read or rebuild what `rates_by_sector.py`
  writes; `level_graphs_sparse.py` compares itself with `level_graphs_further.json` where both ran; the read-out scripts
  of the thread results read the `.jsonl` files the three long scripts write.
- **The three `.jsonl` files are under the ignore file's blanket rule** (`*.jsonl`, for build noise). They are here
  because they were added by force. In the arc they are evidence that a lock reads by name, so the arc needs its own
  exception line in `.gitignore`, as the arcs before it have (B1419, B1726): a lock may not depend on an ignored file.
- **The long runs are not for a lock to repeat.** The twelve threads took about an hour on six cores, the three-ended
  covers fifty minutes on one, the parity sectors twenty-five. A lock holds their outputs and reads again a small part
  chosen so that it can fail: one thread of the twelve in full, one state's parity sectors, one cover.
- **`the_three_solids.py` needs networkx.** Where the default lane has none, the lock holds its output and says aloud
  that it skipped the comparison.
- **Two levels of precision.** The identities and the level-15 value are exact. The rates of 171 sectors and the
  graphs' eigenvalues are in double precision, each rate computed twice. The readings on covers are at 60 digits.
- **Nothing in either draft gives a rate or a count a physical meaning,** and the pages say so. Keep it so.
