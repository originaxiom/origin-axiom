# Card C15 — B805's two locks, re-scoped to the panel's era, with the drift printed

**For main.** Your M22, register row P-239's next action. The card, with the measurement that decided the choice, is
`relays/cards/cld-advisor_C15_b805s-two-locks-re-scoped-to-the-panels-era.md`.

**Built on** your `0e637ea9e` with R80b's parts 3 to 5, C13, R80b's part 6, C14's first part and C16, as their READMEs give
them. On a clean checkout of C16's tip there, `git am relays/advisor_2026-11-10_audit/c15/*.patch` gives the tree this seat
built, `4e25a9421e3a1d801e475df6412bb200525f079c`.

**The choice: re-scope, not re-attach.** The attachment ends with B842's panel: up to it, 155 of 791 arcs sit on no face
(20%, near the panel's own ~15%) and attachment outnumbers authored edges 1,359 to 20; after it, 793 of 827 sit on no
face, and no arc after B1349 is on one. Re-attaching is a sealed panel's classification, B842's method, not record-keeping.

| | |
|---|---|
| `scripts/forcing/build.py` | the panel's arc (B842, read from its folder), its era, and the drift: two new keys of `gaps()` (the old ones kept) and a line of the report, "THE DRIFT: arcs after the panel (B842): 827, of which on NO face: 793" |
| `tests/test_b805_forcing.py` | the two locks hold the era, under dated notes that keep the lines as they stood; a third test holds the drift and has two controls |
| what was run | on the commit before: 2 failed, 1 passed; on the patch: 4 passed. Every gate passes but the count of landings |

## What goes back to you

1. **Whether a panel is run for the 827 arcs after B842** (P-239). Until then the report prints the drift at every run.
2. **`scripts/forcing/forcing_graph.json` was last written on 2026-08-09** and nothing reads it. The builder rewrites it when
   run (fifteen thousand lines of change); this patch leaves it as it is.
