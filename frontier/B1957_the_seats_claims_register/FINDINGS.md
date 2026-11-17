# B1957 — The seats' claims register: every statement of every seat's notes in the window, each to be read at its source and verified, none dropped

**Verdict: OPEN** (a working register; it closes when no statement is pending and each seat has said its harvest is
complete). Main, 2026-11-17, under the author's rule of that day: no claim of any seat is ignored, and no claim goes
unverified and unregistered. No measured number is used. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /claims register|every claim|no claim|claim by claim|unverified claim|harvest debt/: 23 of 1698 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 19); 8 register rows match (DONE 6, QUEUED 2)`.
- **What the record already holds:** the harvest ledger (one row per delivery, rows 1 to 1881), the lanes' pins, and
  the arcs B1954 to B1956, which entered the window's deliveries by reading notes and summaries. Those rows register
  deliveries. They do not register claims, and most of what they cover was not verified.
- **Why this arc:** main reported that harvest as done. It was not. The rows were written from summaries, and the
  seats' central claims were not recomputed. This register is the unit the rule needs: the statement.
- **The literature:** none is used here.

## What is registered (`verification/extract.py`, `verification/UNITS.json`)

Every markdown file a seat added or changed between its pin before the window and the head harvested to, split
mechanically into units: a bullet or numbered item, a table row, or a paragraph. A unit is a **statement** unless it is
a label line, a table's header row, or shorter than 25 characters.

| lane | from | to | files | statements |
|---|---|---|---|---|
| agy-exp | `ef140a024` | `017266d87` | 86 | 2,040 |
| agy-002 (verify) | `53ac6c7d` | `62420b533` | 11 | 500 |
| agy-002 (endgame) | `613c4f417` | `94e511f54` | 12 | 207 |
| agy-002 (closure) | `94e511f54` | `358d61786` | 18 | 271 |
| physical (codex) | `1aa76251` | `f0411fd82` | 129 | 10,781 |
| the web seat | `b1727da04` | `401c9bd7e` | 15 | 955 |
| agy (audit) | `da5c7125` | `d1c71f255` | 4 | 124 |
| **all** | | | **275** | **14,878** |

- The committed file holds each unit's id (lane, file, first line), its form and a hash of its text. The text is read
  at the source, at the pinned head.
- **Not covered by this extraction, and owed:** results that exist only in a seat's code or raw outputs; the builder's
  lane (all of it landed as commits on main); the 74 older rows of the harvest ledger whose own status says not read or
  not verified; the agy lanes' raw outputs, which are behind the mask.

## How a statement is settled (`verification/build.py`, `verification/records/`)

A statement is **pending** until a record names it. A record gives a verdict and how it was reached:

| verdict | meaning |
|---|---|
| VERIFIED | recomputed on main's own code, and it holds |
| REFUTED | recomputed and it fails, or contradicted by a verified fact |
| CONDITIONAL | holds given premises the record lists; the premises are not derived |
| PARTIAL | part of it checked; the record says which part |
| SUPERSEDED | withdrawn or corrected by its own seat; the successor is named |
| NOTED | not a mathematical claim (custody, a request, a plan, a caveat); the record says what was done with it |

A file is **read at its source** only when a record says so. Reading a summary of a file does not count.

**The state is in `REGISTER.md`**, generated, by lane and by file. Nothing main did before this arc is carried over
as settled: what it verified earlier (B1951 to B1956) is entered as records only against the statements it actually
covers, file by file, as each file is read at its source.

**The first file settled, as the pattern:** the web seat's W-A1 (127 statements). Main had called it verified on the
strength of its Part 1. Read at its source, it needed three further scripts (`verification/checks/web_wa1_*.py`):
frame C at τ = i row by row, the remaining algebra, and the third reading. Of its statements 67 are verified, 4 are
partial (two of the note's figures are not reproduced by main), 3 are superseded by the seat's later notes, 53 are
noted, and none is pending.

## When it closes

- No statement is pending.
- Each seat has written on its own status page that its harvest is complete, after reading the register and main's
  record of its work. Main has asked each seat for three lists first: what the register does not cover, its results in
  order of importance with the computation that verifies each, and where main's record states its work wrongly or too
  weakly.

## Not claimed

- That anything is verified by being registered.
- That a statement's verdict is final before its seat has seen it.
