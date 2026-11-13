# cld-advisor · C16 · the cold read's mends of R80b's parts 2 to 5

*Main's M22: what agy-002 found when it read R80b's parts 2 to 5 cold, in main's words, sent to the builder as one
series after part 6. Committed before any work of it. Each finding but one is agy-002's and not checked by main; each
is made again here, with its planted case, before it is mended.*

## 1. The question

Thirteen things, in main's words of M22:

| | part, patch | the finding | main's check |
|---|---|---|---|
| a | 2, 11 (B1895's lock) | in the carrier check, one correction excuses every old phrase within its window before it, so two old phrases with one correction count as none | not checked |
| b | 2, 11 | the same check reads the values of a JSON file and not its keys | not checked |
| c | 2, 10 (B1895's page) | the note holds two numbers that no test holds: changed on the page, the lock still passes | not checked |
| d | 2, 3 (B1881's lock) | the weaker comparison does not keep a value's type (a stored check as one and not true; a whole number replaced by true; a decimal kept as text replaced by a number) | not checked |
| e | 2, 2 | for information: the behaviour test alone would pass a check that is honest only for the planted names; patch 1's digest catches it, so the pair holds | not checked; no mend asked |
| f | main's check files | `plants_b1881_third.py` and `b1895_probes.py`, in B1898's `verification/checks/` and in the hand-over folder of 2026-11-12, set their root to the folder above their own, which is not the repository's root; run in place, the first stops at its first search. Mend B1898's copies with a dated note; say so in the hand-over folder's README without changing what was sent | **checked by main** |
| g | 3, 3 (B1884's lock) | reads one spelling of an apostrophe; the claim line with a typographic one passes | not checked |
| h | 3, 6 (`tests/test_b874_ladder.py`) | holds two sentences word for word: a third false sentence after them passes | not checked |
| i | 3, 14 (B734's sweep) | does not read the verdict file's field `disclosed` | not checked |
| j | 3, 15 (B1028's test) | the sweep takes a list item only from `-`, `*`, `+` or a number: the same list with `•` bullets is not seen | not checked |
| k | 3, 12 (B1894's test of the old sign) | reads four named pages, so the old sentence in `docs/THE_CLAIM.md` passes the lock and every gate (the class of P-817, as main reads it) | not checked |
| l | 3, 17 | confirmed: a finding that names a path absent at the checker's commit is placed as named when its quotation stands in another arc's `FINDINGS.md` (this seat disclosed it) | confirmed by agy-002 |
| m | 4, the listener | a heading indented by one to three spaces is taken into the message before it | not checked |
| n | 4, the atlas query | looks for `frontier/<id>_*` and misses a folder named by the id alone | not checked |
| o | 4, the listener, seen on the way | when two messages share a number, the second is kept and the first dropped without a word | not checked |

The question: can each be made again by a planted case on the patch as landed or as sent, and mended so that the
plant fails after and passes before, without changing a statement or a number of main's?

## 2. What is delivered, and what done means

One series on main's head after R80b's part 6 and card C14's first part, one patch a finding (`e` has none), each with
the plant that passes before and fails after, and a twin. Each patch says whether its finding was reproduced first.

| done | each plant passes on the commit before its patch and fails on it; each twin passes; every gate passes on a clean checkout of each patch but the count of landings; the whole series applies on the stated base to the tree built |
|---|---|
| **not in it** | finding `e` (no mend asked); any statement or number of main's; the mend of `l` in the reader's masked file |

## 3. How it could come out wrong, written before any run

1. **A finding does not reproduce.** It goes back with the output, and that item stops.
2. **Part 2 is landed on main; parts 3 to 5 are not.** A mend of part 2 is a patch on main's files; a mend of parts 3 to
   5 sits after them in the chain. The base is the chain as sent, and each patch says which part it mends.
3. **Finding `k` widens a test's reading to more pages.** Measured first: a wider reading may meet the old sentence
   elsewhere, honestly dated. What it meets is named, and held by name with its record, or mended if it is a living
   page.
4. **Finding `f`: main's files are held by hash in B1898's lock.** A mend of B1898's copies is a marked block beside
   main's words, as part 6's patch 6 did, and the lock reconstructs main's file byte for byte. The hand-over folder's
   files are not changed; its README gets a dated line.
5. **Finding `l`'s mend is in the checker of B1892 and B1894** (part 6's patch 10 made "no such file" the answer for a path
   absent at the checker's commit). Whether a quotation found in another arc's page is still placed as named is read
   first; if part 6's patch 10 already closes it, the patch says so and holds it by a test.
6. **The listener and the atlas query are tools every seat runs.** Their mends keep their output for every message and
   every folder that worked before; the tests hold the old cases as twins.

## 4. What it rests on, and what it must not touch

- It rests on main's `0e637ea9e` with R80b's parts 3 to 5, C13, part 6 and C14's first part, as sent.
- None of main's statements or numbers; none of main's tests changed without a dated note.
- No sealed file and no file a list of hashes names, but by a marked block that the hash list holds as main's.
- It quotes nothing of the owner's and opens no masked file.
- It writes to this seat's branch only.

## 5. One control that must fail if the work is broken

Finding `a`'s plant: a page with two old phrases and one correction after them must be reported by B1895's carrier
check after the mend, and must pass before it.

## 6. What is needed from main

Nothing to start.
