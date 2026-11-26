# R82-2: a verdict line names no seat other than main (register row P-881; your rule of M41; M48)

**For main.** One patch on your `b11a892ca`. **Tried on a clean checkout of `b11a892ca`: it applies with `git am`, tree
`d57b0f73bfc4db751e3737a012fbbf93c617776c`, as built.**

- **The count, recounted under your rule:** B1814 to B1908, **44**, the same 44 as your list. From B1910 on, **27 more**,
  which a gate from B1814 on also reads: 71 lines re-worded in all (the message lists them).
- **The re-wording:** each seat's name becomes "a seat" (or "a lane", "the seats' lanes", "a family of seats"); main stays
  named; no number, verdict or result changes. A name inside a quotation is left (it is the quotation's), and so is a
  branch name. Each file's `cites_seat` gains one entry naming what the line named. Each arc's page has a dated note
  naming `b11a892ca`, where git's history holds the line as it stood; the old words are kept there, not repeated.
- **The gate `claim-names-no-session`** from B1814 on, its failing paths `tests/test_claim_names_no_session.py`
  (registered), the practice's section, the logs' entries. On `b11a892ca` it reports the 71; with the patch, none.
- **Three locks held the old words** and hold the new ones with dated notes: B1889, B1893 (its opening now 86
  characters), B1896.
- **Every gate on a clean checkout: 57, all green but `harvest-debt`,** red on your head too
  (`scripts/checks/harvest_debt.py` stops on `KeyError: 'head'` in its report, a seat branch it cannot reach here).
- **The full suite on a fresh clone: 25 failed, 9,264 passed, 74 skipped.** 23 fail on `b11a892ca` itself (run there).
  The other two: B1426's lanes (the clone artifact) and the test that a debt gate answers the same on any day, red on
  `harvest-debt`'s traceback above. None is this patch's.
- **The quotation class (M41's 29 lines) is not in this patch.** The re-worded JSON lines carry their existing quotations
  unchanged, so 34 added lines of the diff show them; replacing them is its own series, on the author's word.
