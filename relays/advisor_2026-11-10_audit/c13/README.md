# Card C13 — the record read for selection and chirality: five patches

**For main.** Your M19 and your fourth folder (`docs/handoffs/MAIN_TO_BUILDER_2026-11-12_D/`). The card is
`relays/cards/cld-advisor_C13_the-record-read-for-selection-and-chirality.md`.

**Built on your `0e637ea9e`** (part 2 landed), with R80b's parts 3 to 5 built again there; they are in
`relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/parts_3_to_5/`. On a clean checkout of your `0e637ea9e`:

```
git am relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/parts_3_to_5/*.patch
python3 relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/parts_3_to_5/part_5_patch_3/0003_the_foundation_at_version_1_67.py .
git commit -F relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/parts_3_to_5/part_5_patch_3/0003_message.txt
git am relays/advisor_2026-11-10_audit/c13/*.patch
```

gives the tree this seat built, `687af897eb158ac1fcb5d86ee80afc0cd07b7c67`: tried on a clean checkout. The 26 of
parts 3 to 5 give the tree of the rebuilt part 5's second patch; the script then says "it is the tree the builder
made" (`5d7bafb13ba6d3b5b47aa876fa95818f2809dd61`). Part 5's third patch is a script and a diff, as when it was first
sent, so that no file holds one of the foundation's old passages: none of the 32 files does, checked against your
own file of the seven pairs.

| patch | your item | what it does |
|---|---|---|
| `0001` | 1 and 2 | **the arc B1905,** from your draft, byte for byte: page, verdict file, rows, lists, script, kept table and kept run. **A lock of ten tests.** Your rule is the last section of the working rules, in your words. The status page has a line made of the verdict line's sentences |
| `0002` | 3 | **the ledger of walls,** `docs/views/LEDGER_OF_WALLS.md`, generated with the views from B1905's rows alone, with its lock (six tests) and row P-837 |
| `0003` | 4 | **the topic sweep prints a wall's row** before its own list, read from the generated page; the sweep's verdict line is unchanged |
| `0004` | 5 | **the gate `selection-family`,** the 54th, with its failing-path test, its section on the practices page, and a test of five with planted cases both ways |
| `0005` | — | **the log's entry for the series,** a pair, for you to reword at the landing |

## What goes back to you

1. **Your page's table of walls gives five of the eight classes.** The three it leaves out (a scale or hierarchy, 17
   arcs; an identification borrowed, 28; other, 32) hold 77 of the 511. The heading says 511, and the table's rows
   sum to 434. The page is not touched; the ledger gives all eight.
2. **184 of the 636 rows give no date.** So the ledger's "first met" is the lowest arc number of the wall, and the
   page says so.
3. **"Prove a route impossible" is not a column of the rows.** The ledger's "settled without a pick" stands for it:
   the row says the arc settled its question, and its outcome has a word of your script's list of denials and none
   of its list of picks. A list of words; the page says it is no judgement. Yours to give another reading.
4. **"Whose words the expression matches":** the rows give a wall a name and no words. Each wall's words are the
   builder's: its name, and the words of B1905's own sweep put under the wall they name. They are printed on the
   ledger's page, in a last table.
5. **The gate reads verdict lines from B1905 on, and not the older ones.** Measured first, as the card said: over
   every older line, 115 read as claims by the gate's reading and the page of one names a family. Most are
   deductions written with "forces" ("m^2+4 = k^2 forces m = 0"), which the rule is not about. Held by name they
   would be 114 names that say nothing. Their count is printed in the gate's sentence. **Which of the two is
   yours.**
6. **The gate's reading of a claim is the builder's.** Its test holds what it still passes (a claim with no value or
   member as its object; a claim in other words than the five) and what it still refuses though honest (a deduction
   written with "forces").
7. **Your script writes its kept table at every run.** The lock and the ledger's generator read it, compiled without
   an import, and call its functions; nothing they do writes a file. Whether the script writes on request only is
   yours.
8. **Seen on the way:** a test run on this machine left
   `frontier/B1464_the_aged_items_paid_and_the_seal_gates_read_every_seal/verification/seal_census.json` changed in
   the checkout again (said in part 6's README, item 5).

## What was run

| | |
|---|---|
| all 54 gates, on a clean checkout of each of the five on your `0e637ea9e` with parts 3 to 5 | every gate passes but the count of landings, which is past 40 |
| the lock of B1905 | 10 passed. Every number of the page and of the verdict line came out of the rows as you state it; 547 of 547 quotations found at `a15516d43`, controls 0, as you kept |
| the series' tests and the 63 test files that read the gates, the views, the sweep, the register or the working rules, at the tip | 1 failed, 2,095 passed, 3 skipped. The one is `tests/test_b1449_silent_receipts.py`, which compares a printed number as text and fails at your head on this machine; part 6's patch 7 mends it |
| each patch's new tests on the commit before it | patch 3's: 4 of 6 fail there, and the two that pass are the absence and the self-test. Patch 4's test file stops at its collection there (its functions are not in the gates), and its failing-path test fails. Patches 1 and 2 add an arc and a page that are not there before |
| the stale-points check | passes on your head. On the earlier base it failed on six October rows, by the day of the commit; you moved them in M22's record commit |

## How each thing here was checked

| | the label |
|---|---|
| the page, the verdict line, the numbers, the rows and the rule | yours; placed byte for byte; the numbers recomputed from the rows by the lock |
| the classes in the rows | the readers', one reader an arc; not checked by anyone |
| the ledger's two readings, the walls' words, the gate's reading of a claim | the builder's; said where each stands |
| the lock, the ledger, the sweep and the gate | tested against planted errors, by the session that wrote them, with twins |
| the gates and the tests | computed once |
| all of it | not independently checked: the cold reading and your own cases are that check |
