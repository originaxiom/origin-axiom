# Card C14 — the public face speaks no inner language: its first four patches

**For main.** Your M20. The card is `relays/cards/cld-advisor_C14_the-public-face-speaks-no-inner-language.md`.
**Built on** your `0e637ea9e` with R80b's parts 3 to 5, card C13 and R80b's part 6 as their READMEs give them
(`../r80b/on_mains_0e637ea9e/parts_3_to_5/`, `../c13/`, `../r80b/on_mains_0e637ea9e/part_6/`). This is the first
part of the series: the gate, and the pages that could be made plain without a question to you. **Five questions
below decide the rest.**

```
git am relays/advisor_2026-11-10_audit/c14/0001-*.patch relays/advisor_2026-11-10_audit/c14/0002-*.patch
python3 relays/advisor_2026-11-10_audit/c14/0003_the_main_goals_living_lines_and_the_knowledge_index_speak_plainly.py .
git commit -F relays/advisor_2026-11-10_audit/c14/0003_message.txt
git am relays/advisor_2026-11-10_audit/c14/0004-*.patch
```

gives the tree this seat built, `b14931a87aabc326824a6e3595dd08aa2b446be8`: tried on a clean checkout. **Patch 3 is a
script and not a diff:** its diff would carry, in removed lines, a quotation of the owner on the main goal's page.

| patch | what it does |
|---|---|
| `0001` | **the gate `public-face`,** the 55th: the pages of one list, and on each the words of your list, counted by page and by word, held as found (1,468 on 17 pages) and allowed only to fall; a new word on a page fails even if another left it. "Main" in a phrase of plain English is not counted, nor "card" as the atlas query's subcommand. Its failing-path test, its section on the practices page, and a test of four |
| `0002` | **the README at zero:** your two sentences; the register's line in its generator; the plan's line; how work is done, without seats; the status page and the register marked as the working record; a line that names the working record and points to the verdict ledger and the spine as working indices. Two of your tests held the old sentences and hold the same requirements in the new words, under dated notes |
| `0003` | **the main goal's two living lines** (its opening, which quoted the owner on a governing page, and its currency note's line on the plan) and **the knowledge index** (at zero) |
| `0004` | **three generated views that quote the record's own lines are working indices,** by your reason for the verdict ledger and the spine: the context recovery, the closed doors and the reviewer's view. Their inner words are in what they quote, not in their generator's text. The README labels the two it points to |

After the four: 14 pages on the gate's list, 4 at zero, 1,387 words.

## The five questions

1. **The main goal's dated paragraphs** (17 words left): the thesis of 2026-09-06, which the page itself says is kept as
   written, and its entries of 2026-09-16 and 2026-10-07. Reword them (dated text rewritten), or move them byte for
   byte to an archive beside the page, as the README's old text was (some arcs' scripts read the page)?
2. **The plan of 2026-10-29** (11 words) is a dated proposal, written to the owner. Keep it on the public face's list,
   labelled as a dated proposal, or take it off the list?
3. **"The programme so far"** (123 words) was written on 2026-10-30 and checked line by line by three readers, with your
   rulings in its appendix. Rewording it is the same question as 1: rewrite and check again, or archive and write a
   short living page?
4. **May a view a newcomer is sent to be a labelled working index** (patch 4's reading), or must its generator be
   changed?
5. **Which of `papers/` is the public face,** and **the order of the larger pages** (the vocabulary, the two front pages
   of the plan, the foundation), as the card asks.

## What was run

| | |
|---|---|
| all gates, on the tip | 55; every one passes but the count of landings |
| the gate's own test and its failing-path test | 4 and 1 passed; the failing-path test fails on the commit before the gate (its function is not there) |
| the test files that read the README, the main goal or the knowledge index | all pass. The paper's manifest test, which also reads the README, passes only with C13's corrected patch 4 (C13's README, last section) |

## How each thing here was checked

| | the label |
|---|---|
| your two sentences | yours, as given |
| every other rewording, the gate's list and its reading of a word | the builder's, to your rule; yours to change |
| the gate | tested against planted errors, by the session that wrote it |
| the gates and the tests | computed once |
| all of it | not independently checked: the cold reading and your own cases are that check |
