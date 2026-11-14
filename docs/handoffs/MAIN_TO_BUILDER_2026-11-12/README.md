# Main to the builder, 2026-11-12: main's drafts and checks, to be assembled and landed as patch series

*Main. By the owner's direction of 2026-11-12 (register row P-832) main works the frontier mathematics, and the
record-keeping is built by another session as patches, read cold by a verifying session, and landed by main after its
own check. This folder is what main hands over. Everything in it is main's own work; nothing of any other session's
code was run to make it. 0 of 19.*

## What is here

| folder | what it is | what is to be built from it |
|---|---|---|
| `review80/` | main's answers to the first 43 findings of Review 80, the state of the other 57, and every check main ran (`checks/`) | the review's arc and entry, then the mends that are not made yet (series R80) |
| `wp12/`, `wp13/`, `wp18/` | three mathematics drafts, each with its script, its kept run, its output, a page, a verdict file and a lock (the lock is named `lock_draft.py.txt` so that no collector runs it here) | three arcs, in the plan's order |
| `wp16_the_selection_test/` | the test the owner asked for on 2026-11-12, in two parts, and the texts of the rule that follows from it (`RULE_draft.md`) | one arc; the rule in the working rules, the foundation and the plan |
| `x_c1a_on_main/` | three harvest rows of the weave recomputed by main (908, 914 the group part, 917) | harvest rows re-typed; filed with the arc of the thread results when it comes |

## The rules for building from it

- **A statement of the mathematics and a number are main's.** Do not reword or change one. If a check of main's fails in
  your checkout, or a number differs, send it back with the output.
- **What main says it checked is in `review80/STATUS_OF_THE_57.md`.** Write nothing as checked by main that the table
  does not give as checked.
- **A mend keeps the old words** under a dated note. A mend of a lock comes with a planted case, in the patch's own
  test, that passes before the mend and fails after it.
- **The owner's words are quoted nowhere** (register row P-796), and no session is named as an authority.
- **Every count is recounted** from git or from the file, by a command kept in the arc.
- **Each patch passes every gate on a clean checkout,** and the full suite passes at the end of a series.

## Who reads it before main lands it

agy-002 reads each series cold, patch by patch, against the finding or the draft it answers. Main reads the difference,
runs its own unseen cases, and lands.

## Added 2026-11-13 (the building session, at main's word in M22): two files of this folder do not run in place

`review80/checks/plants_b1881_third.py` and `review80/checks/b1895_probes.py` set their root to the folder above their
own, which is not the repository's root, here or in the arc B1898: run in place, the first stops at its first search, and
so does the second. They are not changed in this folder. Each has a mended copy, differing in one marked block, beside main's file in
the arc B1898 (`verification/mended_in_r80b/`), and B1898's lock holds that each copy is main's file but for that block.
