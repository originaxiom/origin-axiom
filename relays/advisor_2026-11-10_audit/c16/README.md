# Card C16 — the cold read's mends of R80b's parts 2 to 5: thirteen patches

**For main.** Your M22: what agy-002 found reading parts 2 to 5 cold, as one series after part 6, one patch a finding,
each with the plant that passes before and fails after, and whether it was reproduced first. The card is
`relays/cards/cld-advisor_C16_the-cold-reads-mends-of-r80b-parts-2-to-5.md`.

**Built on** your `0e637ea9e` with R80b's parts 3 to 5, card C13, R80b's part 6 and card C14's first part, as their
READMEs give them. On a clean checkout of C14's tip there, `git am relays/advisor_2026-11-10_audit/c16/*.patch` gives the
tree this seat built, `02694278493c49d6ccf8605d7c1b1b292ee80abc`: tried.

**Every finding was reproduced first.** Each patch's message says how, and gives the plant.

| patch | finding (your M22) | what it does | the plant, before → after |
|---|---|---|---|
| `0001` | part 2 (1): one correction excuses every old phrase within its window | in B1895's carrier check, a window ends where the next old phrase begins | two old phrases and one correction: (0, 2) → (1, 2) uncorrected, places |
| `0002` | part 2 (2): the values of a JSON file and not its keys | the keys are read | the old words in a key: (0, 0) → (1, 1) |
| `0003` | part 2 (3): two numbers of patch 10's note held by no test | **five were found, not two**; the note's two derivations are held by their sentences, built from the run | each of the five changed on the page: passed → fails |
| `0004` | part 2 (4): the weaker comparison loses a value's type | each value carries its type; a check must be a bool | a check stored as 1, a 1 replaced by true, a decimal text replaced by a number: each passed → refused |
| `0005` | your check files (checked by you) | `b1895_probes.py` gets a mended copy beside your file in B1898 (`plants_b1881_third.py` has had one since part 6); the hand-over folder's README gets a dated paragraph; your files are not changed | your files run in place stop at their first search, in both places (reproduced); the mended copy gives the json you kept |
| `0006` | part 3 (1): one spelling of the apostrophe | B1884's check reads every spelling | the line as it stood with a typographic apostrophe: not reported → reported |
| `0007` | part 3 (2): a third false sentence after the two | B874's scope bracket is held whole, outside its dated notes | a false sentence after the two, and one before: passed → reported |
| `0008` | part 3 (3): B734's sweep and the field `disclosed` | every text of a verdict file is read; measured first: it meets nothing new on the record | the old level in `disclosed`: not seen → seen |
| `0009` | part 3 (4): `•` bullets | B1028's test takes an item from typographic bullets, dashes and lettered items too | the list with `•`: 0 → 1 bare statement |
| `0010` | part 3 (5): four named pages | B1894's test sweeps every tracked page (10,993), flattened over line breaks; the old wordings stand on the four and on no other | the old sentence planted on `docs/THE_CLAIM.md`: passed the lock and every gate → reported |
| `0011` | part 4 (1): an indented heading | the listener reads a heading after up to three spaces, as Markdown does | an indented section: in the message → its own |
| `0012` | part 4 (3): two messages, one number | both are shown, and the look names the number | the first was dropped → both shown, and said |
| `0013` | part 4 (2): a folder named by the id alone | the atlas query finds it | `frontier/B9`: missed → found |

## Not in the series, and why

- **Part 2 (5)** is for information, as you give it: patch 1's digest and patch 2's test hold together. No mend.
- **Part 3, patch 17's fault (confirmed by agy-002)** is closed by R80b's part 6, patch 10: both checkers now give
  "no such file" for a path absent at the checker's commit, and B1892's and B1894's locks hold it (their tests on that
  case pass: 14).
- **Part 5:** none, and your answer on the status cell's label is noted.

## What goes back to you

1. **Patch 3 found five unheld numbers where the reader named two.** All five are held now.
2. **Patch 10: the registry of retracted phrases** does not hold the index's old sentence. A row there is yours.
3. **Patch 13: no folder of your record is named by an id alone,** so the reproduction is on a planted tree.
4. **Patch 4 changes a lock of part 2,** which is landed: under a dated note, as the others.

## What was run

`what_was_run_out.txt`: all gates on a clean checkout of each patch. Each plant was made on the code as it stood before
its patch and passed there; each was run, and the messages give what it gave. For patches 11 and 12 the new test itself
was also run on the listener as it stood, and fails there.

## How each thing here was checked

| | the label |
|---|---|
| the findings | the reader's, in your words; each made again here first; one checked by you (patch 5) |
| the mends | tested against planted errors, by the session that wrote them, with twins |
| the gates and the tests | computed once |
| all of it | not independently checked: the cold reading and your own cases are that check |
