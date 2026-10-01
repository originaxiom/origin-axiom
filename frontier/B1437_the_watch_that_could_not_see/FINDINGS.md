# B1437 — THE WATCH THAT COULD NOT SEE: the doc-currency gate was inert on ten of nineteen living documents, and the lock it cited did not exist

cc, 2026-10-01. Phase 0c and 0d of the "nothing is lost" plan (owner-approved 2026-09-18). Three defects in
`scripts/checks/doc_currency.py`, each measured before it was repaired, landed as two commits so that what the
second unmasks cannot be mistaken for a regression in the first. **Verdict: PROVED.**

## 1. A lock cited in three places and never written

The checker's comment (line 86), `docs/PRACTICES.md` and the generated verdict view all said the declared-debt set
cannot grow because `test_b984_doc_currency.py` fails if it does. No such file exists and none ever did: no file,
no deletion in history. From 2026-08-09 to 2026-10-01 nothing pinned the set.

Repaired (commit 7d494533): `tests/test_doc_currency_gate.py` is that lock. It pins the set by name, and it gives
the checker the planted controls it never had — it was the only debt-facing checker without any:

| control | what it proves |
|---|---|
| a planted document citing an arc from the middle of the corpus | a stale document is caught |
| a planted document citing the newest arc | a current one passes (the check can pass and can fail) |
| a registered document that is absent | fails |
| the frozen marker at line start, and the marker quoted in prose | only the first freezes |
| a declared debt | passes the check; the same document without the declaration fails |
| the lag of the newest, the oldest and the second-newest arc | 0, n − 1, 1 |

## 2. Two metrics for one debt

`check()` counts arcs that exist and are newer than the citation; it was repaired to that on 2026-08-13 because
reserved number ranges made numeric distance count arcs that do not exist. The debt report kept printing numeric
distance. One function, `lag_of`, now serves both, and the lock asserts the printed number is the checked number.

## 3. The mask

A document's citation was the largest `B<number>` in its text. Another seat's arc numbers, in the range B81xx,
are cited bare on main and are larger than every arc here. Measured before the repair:

| document | tolerance | read as | newest arc of this repository cited | true lag |
|---|---|---|---|---|
| docs/COMPUTE_THE_PROGRAM.md | 25 | lag 0 | B1153 | **202** |
| docs/THE_FRAMEWORK.md | 10 | lag 0 | B1235 | **120** |
| WORKING_RULES.md | 40 | lag 0 | B1307 | **66** |
| docs/THE_LADDER.md | 10 | lag 0 | B1322 | **63** |
| docs/THE_SM_VERDICT.md | 15 | lag 0 | B1322 | **63** |
| docs/PRACTICES.md | 40 | lag 0 | B1410 | 25 |
| docs/ERROR_LEDGER.md | 40 | lag 0 | B1425 | 10 |
| docs/LAW_MAP.md | 10 | lag 0 | B1433 | 2 |
| docs/CAMPAIGN_STATUS.md | 5 | lag 0 | B1434 | 1 |
| docs/OPEN_LEADS.md | 10 | lag 0 | B1434 | 1 |

Ten of nineteen watched documents could not go stale. Five were past tolerance, three of them the documents a
reader forms the picture of the programme from.

Repaired (commit 27453ee5): a number is a citation only if an arc with that number exists under `frontier/`. With
the four debts of 2026-08-09 and the mask off, the checker reports exactly the five above and no others. They are
declared as debts dated 2026-10-01, with the lag measured that day, and the reads are registered as lead L232. The
lock plants a foreign number and asserts it does not count, and asserts that no living document's citation is a
number without an arc.

## What this corrects in the record

The plan of 2026-09-18 said that registering a lead resets the leads file's clock. It does not. The file's clock
was not being reset; it could not run. The effect described was real and the cause given was wrong.

## Not done here

- The five reads (L232). Declaring a debt records that a read is owed; it is not the read.
- `docs/THEOREM_LEDGER.md` now cites B1433 and measures as current. One corrected clause does not make a ledger
  current, and its debt of 2026-08-09 stays declared. The measure is crude in both directions.
- The measure itself: the newest arc cited says when a document was last touched, not whether it is right.

## Verification

`tests/test_doc_currency_gate.py` (11 tests, about two seconds). `python3 scripts/checks/doc_currency.py` prints the
nine debts with one metric.
