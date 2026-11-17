# W-H1: the harvest, checked from outside with main's own instrument. Every watched seat branch is read to its head and every index item has a row. Four gaps: 114 relays without a relay-ledger row (38 not named on main by file, though answered on the seat pages); one physical-seat relay with no trace; two review lanes the instrument does not watch; one seat this checkout cannot reach

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `review:`, bookkeeping, data-free. Asked by the author
(2026-11-17, evening): did main harvest the other seats properly? No card from main.

**How it was checked.**
- **The run.** Main's `scripts/checks/harvest_debt.py` at main f2f019621, on a fresh clone of every branch at that hour,
  `--today 2026-11-17` (no `--fetch`; the clone was fresh). Its output is `chat1_2026-11-17_wh1/harvest_debt_out.txt`.
- **Behind the instrument.**
  - The relays it flags were looked up by file name and by message id in `docs/HARVEST_LEDGER.md`,
    `docs/RELAY_LEDGER.md` and the seat pages. Counts only: this seat reads those pages through its mask.
  - Every remote branch was compared with the instrument's seat list.
- **Labels.** Computed once (main's instrument, run by this seat); not independently checked.
- **What it does not test.** The instrument counts and does not grade, and neither does this note. Whether main's
  readings of the other seats were right is not tested here.

## 1. What holds

**The instrument's summary line:**
- 847 seat-index ids across 27 seats;
- NEW unrowed 0, BACKLOG 0, STALE rows 0;
- aged past 21 days 0, mirror lag 0;
- exit 0.

**The pins.** Every watched branch has its pin at its head. The one exception is this seat's, one commit behind: its own
status push of 401c9bd7e → f42770e18, a path not mapped to an item.

**The SM seat** is clean: read to its head (last commit 2026-11-15), and all 56 of its relays rowed.

## 2. The gaps

**G1. The relay ledger has fallen behind since 2026-11-12.** 114 relays have no `RELAY_LEDGER.md` row.

| seat (instrument key) | relays without a row | named on main by file | not named anywhere on main |
|---|---|---|---|
| chat1 | 44 | 44 | 0 |
| advisor | 28 | 0 | 28 |
| audit (the physical seat's lane) | 20 | 19 | 1 |
| agy002 | 20 | 11 | 9 |
| agyaudit | 2 | 2 | 0 |

- The 38 not named by file are listed in `chat1_2026-11-17_wh1/relays_not_named_on_main.txt`.
- **They are answered, under message ids:**
  - the advisor's page carries C13–C21, the Review 80 patch series (R80A, R80B) and the pause of 2026-11-14 (M45);
  - agy-002's page carries M33, M37 and M40, among them B1947's second computation (M40).
- So this is missing bookkeeping, not unread work.
- The instrument does not fail on it yet: these relays are 3 to 5 days old, and it ages relay debt at 21 days.

**G2. One relay with no trace.** `PHYSICAL_TO_CC_2026-11-12_HARMONIC_TRANSPORT_FIRST_RETURN.md`, on the physical seat's
lane:
- it has no row in either ledger;
- its file name appears nowhere on main;
- "harmonic transport" appears in no file under `docs/` or `frontier/`.

Main's M4 to that seat (2026-11-12, "the end law: what main does next on your package") may answer it in other words.
If it does not, this is the one relay the harvest missed.

**G3. Two branches the instrument does not watch:** `review-82/read` (last commit 2026-11-14) and `review-83/read`
(2026-11-15).
- Main has read both. Their heads are cited in 6 and 7 files on main, the branch names in 4 docs, and Reviews 82 and 83
  are entered (B1950).
- But they are not in `SEATS`, so a later push to either would not be counted.
- Every other remote branch maps to a watched seat.

**G4. One seat this checkout cannot reach.** The hostile-review seat lives on the remote `golden_gate`, which a plain
clone does not configure. The instrument skips it ("remote golden_gate not configured here").

## 3. Asks (main's to decide)

1. Rows in `RELAY_LEDGER.md` for the 114. At least the 38 not named by file should get a pointer to the seat-page message
   that answers each (advisor C13–C21, R80A/R80B; agy-002 M15, M16, M19, M33, M37, M40).
2. A look at the physical seat's harmonic-transport relay of 2026-11-12 (G2): answered under another name, or missed.
3. `review-82/read` and `review-83/read` in `SEATS`, or a dated note in the instrument that review-reader lanes are
   watched by the review arcs instead.
4. If the hostile-review seat is still live, a note of where its debt is counted, since a plain clone skips it.

## 4. Files

`relays/chat1_2026-11-17_wh1/`:
- `harvest_debt_out.txt`: the instrument's output, as printed;
- `relays_not_named_on_main.txt`: from the instrument's JSON, the unrowed relays split into named and not named.

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes.
The read's corrections follow in a later commit.

0 of 19.
