# B1448 — THE REVIEW'S INSTRUMENTS: the mechanical half of the decadal review as tested tools, after a review run by hand found its own process to be the defect

cc, 2026-10-02. **Owner-directed:** *"is decadal run properly developed and sophisticated as a process and bugfree?
is it time to advance it?"* and then *"finish the queue first … then we fix decadal and run it."* The review had sat
at three times its period (61 merges against 20; a window of 472 commits). Run by hand, half of it turned out to be
scripts written on the spot. **Verdict: PROVED (an instrument: the tools exist and each check fails on planted input).**

## What was wrong with the process (each seen, not supposed)

1. **It does not fire.** `review-due` reports and nothing follows. Leads, relays and seat items fail a push when
   they age; the review does not, and it aged to 61.
2. **Its instruments are improvised at every review.** The branch inventory, the seal check, the provenance sweep
   and the glossary check were each written from nothing this time, and the first versions were wrong in three
   ways: a third remote (a different repository) was read as this one's, making every seal "not on every remote"
   and seven unmerged refs "unregistered"; a rewritten row of the error ledger was counted as a new class; and a
   shell quoting slip reported four mirror pushes as done when three had failed. Review 57 withdrew three findings
   the same day for the same reason.
3. **Carried items do not age.** Eleven action items of Review 55 had been "carried unchanged" through two
   reviews, and one item since Review 50 under four keys. Restating an item satisfies the loop.
4. **It cannot see a gate that cannot fail.** R55-16 has said so for three reviews (20 of 31 gates with no test);
   on 2026-10-02, 15 of 34 gates are still named by no test, and twelve of those have no test of their checker
   either. The inert currency watch, the lock cited in three places that never existed, and the hash-order class
   were all found outside a review.
5. **Its sample is the reviewer's choice.** "Which arcs were read in full" is declared and not drawn.

## What is built (`scripts/review/review_tools.py`, lock `tests/test_review_tools.py`)

Every check is a pure function that fails on planted input; thin wrappers gather its input from git and the tree.
`python3 scripts/review/review_tools.py` prints the draft of a review's mechanical sections.

| template section | function | planted control |
|---|---|---|
| 1 the loop | `action_loop` — open items of the last block, and for each carried item **how many reviews it has aged** | an open item left in a superseded block is found; a twice-carried item counts two |
| 1b branch inventory | `branch_inventory` — every unmerged ref on the two mirrors, matched on its **leaf**; other remotes named and not read | the R57-1 regression: a registered leaf under a path prefix is not reported |
| 2 modulus | `sample_draw` — the arcs to be read in full, **seeded by the anchor** | same seed, same draw; another seed, another draw |
| 3 advancement | `table_rows_added` on the law map and the theorem registry | — |
| 4 error recurrence | `error_rows` — a class is new only if its id heads no row at the anchor | a rewritten row counts as a recurrence |
| 5 provenance | `provenance_hits` on the lines **added** in the window; `term_candidates` — the window's new vocabulary against the glossary | a pretense phrase is hit, "internally verified" is not |
| 7 protocol integrity | `seal_check` — hashes against the files, sealed strictly before results, seal on every mirror | each of six defects, including a hash file no parser reads |
| + | `gate_controls` — gates no test names; `relay_split` — the open relays by direction (R55-3) | a gate nobody tests is listed |

The live wrapper is exercised by the lock on this repository.

## What it does not do

The judgement half: what the window means, what is promoted, whether a carried item should be declined. And it does
not make the review fire or make carried items age — those change governance and are put to the owner as a
proposal in Review 58, not switched on.
