# The five readers of B1889

Five read-only readers on the cheaper tier, run by main on 2026-11-11. Each was given the rows of one group of seats,
cut from `docs/HARVEST_LEDGER.md` as it stood in main's working tree (rows 1 to 1698), and nothing else. Each was told
to use one tool, to open only its own files, to run no command and to write nothing.

| report | the seats whose rows it was given | rows |
|---|---|---|
| `reader_G1_sm.txt` | the SM-derivation seat | 463 |
| `reader_G2_web.txt` | the web seat | 233 |
| `reader_G3_physical.txt` | the physical lane and its fork lane; and, by a fault of main's first cut, the independent audit lane's two rows (1512, 1550) | 363 |
| `reader_G4_small_live.txt` | the advisor seat, the agy lane, the explore seat, the referee lane and three single handoffs | 90 |
| `reader_G5_retired.txt` | ten seats that have ended | 536 |

**What each was asked for:** the kinds of work, in rough shares; themes that cover all the rows, each with the rows,
what was delivered, what main did, rows where main's recomputation confirmed the seat and rows where it did not, with a
quote from the row for each; rows that were not verified and that claim something bearing on the goal; the track record;
and any limit the rows state.

**The rules each was given:** every quote copied character for character from the row it names, to be checked by
machine; nothing stated that the rows do not say; no value compared with a measurement quoted or computed; the classes
counted from the field of each row.

The reports are kept as they were received. A reader's grouping and its reasons are its own. Its quotes are checked by
`../quote_check.py`.
