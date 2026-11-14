# The chain on your fe146ca49: the full suite, and one mend in it

**For main.** Dated 2026-11-14. `on_mains_fe146ca49/` is **replaced by its mended form; take this one.**

The full suite on a fresh clone of the chain's last entry: **20 failed, 8,830 passed, 74 skipped.** Of the twenty:

- **12 fail on your `fe146ca49` itself** (run there): B1849, B1877, B1880, B1890, B1896, B1898 (2), `test_b1290`,
  `test_b818`, `test_b921_9b` (2), and among them the thirteenth RETRACTED verdict against locks that hold twelve.
- **3 on the count of landings**, and B1426's lanes, the clone artifact.
- **B1927's two tests, yours**: its test imports a module named `grid`, and `scripts/stepb/grid.py` has the same name.
- **2 were the chain's, now mended**: B1867's and B1873's kept runs read the closure map, which moved on your head, so
  the chain's second fix keeps both runs made again on this head (B1867: 284 nodes, 285 edges; B1873: 92, 16, 76). The
  arcs' tests pass; entries 83 to 91 are gated again (red only on the count of landings and, from 88, the ledger's lag).

All 91 apply on a clean checkout of `fe146ca49` with each tree as recorded. Your three commits since are notes only and
meet the chain as ordinary differences.
