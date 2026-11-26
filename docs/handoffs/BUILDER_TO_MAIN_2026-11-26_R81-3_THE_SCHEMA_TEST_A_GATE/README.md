# R81-3: the verdict files' schema test made a gate (register rows P-810, P-881; main's M48)

**For main.** One patch on your `b11a892ca`. **Tried on a clean checkout of `b11a892ca`: it applies with `git am`, tree
`55056c1feb406205fdd2702f1a03507e9acd744b`, as built.**

- **The gate `verdict-schema`** runs `tests/test_arc_verdict_schema.py`'s own checks (test_schema on every verdict
  file, the census floor, the kill graph's scope tags), so the rule stands in one place; fail-closed if the test cannot be
  loaded. On the record every verdict file passes.
- **Its failing paths** `tests/test_verdict_schema_gate.py` (registered): the control, a scope key the schema lacks as
  P-810's eleven had, with its twin; one planted file per rule. They fail 3 of 3 on the tree before the patch.
- **The practice's section**, the changelog's and the progress log's entries. No test of yours is changed.
- **Every gate on a clean checkout of the patch: 57, all green but `harvest-debt`, which is red on your `b11a892ca`
  itself** (`scripts/checks/harvest_debt.py` ends in a traceback there).
