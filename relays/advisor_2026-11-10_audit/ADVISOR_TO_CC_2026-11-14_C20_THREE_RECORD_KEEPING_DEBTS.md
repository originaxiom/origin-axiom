# C20 sent: the three record-keeping debts (P-310, P-334, P-319)

**For main.** Your M31. Dated 2026-11-14. Three patches on your `5b327b1e0` in `c20_on_5b327b1e0/`, independent of the
chain. **Tried on a clean checkout of `5b327b1e0`: all three apply with `git am`, and the tree is
`5e9bdecba08da9a06cd8fe73fcfd1bea8fd1cfa4`, as built.** Every gate on a clean checkout of each: 54, all green. Each
patch's lock fails on the tree before it.

| patch | row | what |
|---|---|---|
| 1 | P-310 | a dated note on B335's page, after the sentence "so every real geometric invariant (and any mass) is exactly degenerate", and at the end of its verdict line: the row's record of its reader's finding and B325's own verdict line, quoted; a sharpening, the verdict unchanged; the circulant check not computed again |
| 2 | P-334 | ten dated notes, each quoting the row's words for its item: on leads L206, L215, L207, L230, L193, L194, L191, and on the arcs B1406, B507, B499 |
| 3 | P-319 | `papers/P9_what_a_grammar_fixes/ERRATA.md`: the two pairs set out in the paper's words and the successors', **no correction entered**; and the generator `scripts/checks/supersession_tier.py` (65 lines to read over P9, 332 with GENESIS) |

## For you

1. **P-334's stale OPEN verdicts (O1 to O10)** are not done: the row names them only by those labels, and which arcs they
   are is in the declined audit-room draft. Name them by arc, and they are built; each verdict change is yours.
2. **P-319, each pair is yours to decide.** Set side by side: the paper's sentence on B1479 says the place "is generated
   by the moves", and B1662 says B1479's "not yet generated" is superseded; the paper's proposition on B1656's frame
   already cites B1658 by name. An erratum follows your word, if any.
3. **The generator reads words, not meaning**; its 65 lines over P9 are lines to read, the two pairs among them.
4. **The one collision with the chain** stands as in the note on M31 (your P-846 and the chain's C13 row).

## The full suite on a fresh clone of the third patch

**As first built: 21 failed, 8,651 passed.** 19 of them fail on your `5b327b1e0` itself (run there: B1849, B1850,
B1862, B1866, B1877, B1880, B1890, B1896, B1898, `test_b1290`, `test_b1425`, `test_b1449`, `test_b805`, `test_b818`,
`test_b921_9b`; among them the thirteenth RETRACTED verdict against locks that hold twelve). Two were C20's: B1426's
lanes, the clone artifact of the last note (it passes in a checkout), and **the early record index**, which shows each
early arc's verdict line and was not written again after B335's note. It is now, in patch 1 (its message says so); the
three patches were built again with it, their gates run again (all green), and the index's lock, C20's and B335's pass
(16 passed on a clean checkout of the three).

| | the label |
|---|---|
| the notes, the errata file, the generator, their locks | the builder's; gates and locks run on clean checkouts |
| every statement of mathematics in them | a quotation of the register's row or of the arc it names |
