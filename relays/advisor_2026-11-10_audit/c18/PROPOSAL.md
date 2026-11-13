# Card C18 — the historical folders: what was measured, and one archive proposed

**For main.** Your M26 and M27. The card is `relays/cards/cld-advisor_C18_the-historical-folders-measured-and-one-archive-proposed.md`.
**Nothing is moved**: the move is built after your word on this proposal.

## 1. What was measured

`MEASUREMENT.md`, made by `measure.py` on the tip of the chain sent on your `204ee91ed` (a text search; a reader that
builds a path at run time is not seen, so the move is to be tried with the full suite on a clean checkout):

| folder | files | code outside it naming a path in it | seal files | living pages citing it | dated records citing it |
|---|---|---|---|---|---|
| `legacy/` | 34 | 10 (the gates, 2 tests, the seal ledger's script) | 0 | 11 | 11 |
| `story/` | 15 | 4 (the gates, 1 test) | 0 | 12 | 8 |
| `philosophy/` | 28 | 18 (the gates, arcs' scripts) | 0 | 26, among them GENESIS, WORKING_RULES, CLAIMS | 106 |
| `speculations/` | 85 | 78 (the gates, 3 tests, arcs' scripts) | 0 | 29, among them GENESIS | 148 |
| `paths/` | 17 | 9 (arcs' scripts) | 0 | 22, among them GENESIS, GOVERNANCE | 73 |
| `outside_bench/` | 815 | 38 (4 checks: harvest debt, sense census, path references, review tools) | 0 | 9, among them GENESIS | 85 |

No seal file names a path in any of the six. **The ten copies of notes**: all ten are tracked; six are named by code
(B887's audit report, B1831's relay table, B1880's list, B1303's lock, the relay-debt test, B1307's census, B1626's apply
script, the harvest debt check and its test), four by nothing.

## 2. The proposal

1. **One archive folder: `docs/archive/`,** which exists already (it holds the old audit report). Each folder moves under
   it with its name kept: `docs/archive/legacy/`, `story/`, `paths/`, `speculations/`.
2. **`philosophy/` moves too,** but its living citations include the foundation (three) and the working rules (one):
   GENESIS is changed only by its own version process, so its three paths change in a version of the foundation, in
   the same patch, or `philosophy/` waits for that version. **Yours to choose.**
3. **`outside_bench/` is the side work, not history:** 815 files, read by four checks of the harvest. It stays at the
   root under that name in this move, and its notes between sessions (the tenth copy among them) leave the tree with
   the other nine, by the rule of M27; the four checks migrate in the same patch. **Or it moves whole; yours to choose.**
4. **The ten copies leave the tree** (git's history keeps them, as with `docs/handoffs/`): the six readers are migrated in
   the same patch, each to read the copy at the commit the log names, as B1905's lock now reads your fourth folder.
5. **The script:** `scripts/reorganize/history_2026_11_13.py`, with `--check`, in the form of your two of 2026-11-13.
   Living references are updated (the README, ARCHITECTURE, the indices, the atlas's pages; GENESIS only as point 2
   says); dated records are left as written, and the path check resolves them through the log's entry, which names the
   commit before the move.
6. **`knowledge/`, `core/`, `src/`, `packaging/` stay** (M26); the measurement gives no reason to move them.

## 3. What is asked

Your word on points 2 and 3 (and on the whole). The move is then one patch, tried on a clean checkout with every gate
and the full suite before it is sent.

| | the label |
|---|---|
| the measurement | a text search, computed once; its script is beside it |
| the proposal | the builder's; yours to decide |
