# PREREGISTRATION — CELL 10: propagation onto main, and row 5 left honest

*Outside bench, 2026-09-14. Gate 5 untouched.*

**Owner's decision, this session: addendum-only on main** — append dated addenda beside the affected
rows, **strike nothing, rewrite nothing**.

## The three corrections, each already banked in a cell of this programme

| # | file | what is wrong | banked in |
|---|---|---|---|
| 1 | `frontier/B749_genesis_forks/FINDINGS.md` | the F9 addendum states *"The price of a third record is the atom"* with **no depth qualifier**; false at depth 4 | cell 5 |
| 2 | `docs/TOE_REQUIREMENTS_LEDGER.md` §C row 2 | *"counts 2 at every fixed locus"* carries **no frame**, so its 2 and B1321's 3 read as comparable and are not | cell 3 |
| 3 | `docs/WHAT_WOULD_COUNT.md` §4A | lacks **B1116's scope caveat**, which `GRAND_COMPUTATION_LEDGER` says *"must ride with the headline"* | cell 9 |

## The instrument

**An addendum that misquotes its own certificate is worse than no addendum.** So this cell does not
produce a new result; it **verifies the propagation**:

- **S1** — the edits are **append-only**: `git diff --numstat` over the three files must show **zero
  deletions**. Strike nothing, rewrite nothing, mechanically checked.
- **S2** — every load-bearing number in an addendum must also appear in the **banked cell output that
  produced it** (`require_and_test_cell{3,5,9}_out.txt`).
- **S3** — every quotation an addendum **attributes to another file** must be present in that file
  (`ERROR_LEDGER` E2's *"reference table transcribed wrong at sealing"*).
- **S4** — the word counts asserted in the B749 addendum (332 → 10 684) are recomputed from
  Σ 6ⁿ and Σ 4ⁿ rather than copied.

## Row 5 — and this is a decision, not an omission

**Dynamics and gravity stay NOT-COMPUTABLE.** A row this bench cannot move is **reported as such, not
converted into activity.** The cell states the record's own minimal sub-question for each (§E row 1's
six declared inputs; §E row 4's I-26, *"the dimension gap not exhibited"*, carried OPEN as FRESH_EYES Q9
since 2026-09-08) and says plainly that this bench has no instrument for either.

## WHAT THIS CELL MAY NOT CONCLUDE

**Anything new.** It propagates and verifies. No verdict on main is edited, struck, or re-adjudicated.
No value.
