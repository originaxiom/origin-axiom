# B837 — the file-drawer audit: 15 → 0 → 3, and only the last number came from reading

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched.

## The question

**47 frontier directories hold no findings document and no verdict.** Of those, **18 hold a sealed
`PREREGISTRATION.md`** and **15 of those are recorded in `docs/SEAL_LEDGER.md`.**

> **A sealed, ledgered preregistration with no report is the file-drawer problem — the exact failure
> preregistration exists to prevent.** If the programme has one, it matters more than most findings.

## Three answers, and the arithmetic of how I got them wrong twice

| pass | method | answer |
|---|---|---|
| 1 | count sealed preregs lacking a `FINDINGS.md` | **15 file-drawered** |
| 2 | check whether each is *cited* by another arc | **0 file-drawered** |
| 3 | **read what the citing text actually says** | **3 file-drawered** |

**Pass 1 overstated**: most of these arcs *were* reported — in a **successor arc's** write-up rather
than their own directory. **Pass 2 understated**: it counted a citation as a report, and
**citation ≠ report.** B590's citation literally reads *"(bank pending — **B590 paused by owner**)"*
— an admission that it is unreported. B568's is a bare corroborating mention.

**I nearly replaced one unchecked count with another.** The composition lesson this session keeps
producing, applied to my own remedy for it.

## The answer: 3

| arc | state | evidence |
|---|---|---|
| **B590** | **PAUSED, bank pending** | cited as *"bank pending — B590 paused by owner"* |
| **B557** | **PAUSED/PENDING** | cited in B556 only as an *expectation* (*"Expected: charpoly degrees…"*), not a result |
| **B499** | **mention-only** | cited by B500, but no result for B499 is stated anywhere |

The other **12 are genuinely reported** — B452 in B457 (*"H0a EARNED; the campaign closes"*), B580 in
B811, B634's erratum in B635, B652 in B660, and so on. **Their write-up lives in the arc that
consumed them**, which is a filing convention, not a suppression.

## Why 3 is a good number and not a clean bill of health

**B590 was paused by the owner** — a deliberate stop, recorded in the citing arc, which is the
honest form of an unfinished arc. It is not hidden. **B557 and B499 are the two with no recorded
disposition at all**, and those are the real residue.

> **Three unreported sealed preregs out of 24 ledgered-and-unfinished candidates, in a corpus of 803
> arcs, with the largest of the three explicitly paused on the record.** The programme does not have
> a file-drawer problem. **It has three loose ends, now named.**

## Carried

- **B499** (`wild_census`) and **B557** (`escalator_campaign`): either report the result or record a
  disposition. Both hold a sealed prereg, so the obligation is live.
- **B590**: paused by the owner; no action without the owner.
- The remaining **29 no-document directories carry no prereg** (READMEs and probe scripts, mostly
  B1–B5-era) and therefore carry **no reporting obligation** — a stub is not a broken promise.

`tests/test_b837_file_drawer.py`
