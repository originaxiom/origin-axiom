# The planted suite's new case for the move: what is expected, written before any run

One case is added to `tools/planted_violations.py`, with its twin. Committed before the suite was run on either.

| the case | what is planted | on main's `5c7abd72a` | on the move |
|---|---|---|---|
| PV38 | a row in the page of moved pages whose page is not where the row says | **not caught.** No gate reads such a table, and on main's head the page is not there until the plant makes it | **caught** by `path-refs` |
| its twin | the same row, with the page where the row says | passes | passes |

The five controls must be caught on both. The other 37 cases are not run again for the move: it changes one gate,
the one that reads path citations, and the cases of that gate are PV38 and the control of main's own test.
