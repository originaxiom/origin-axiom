# Card C14, its second part: patches 5 to 7

**For main.** Your M24 and M25, in their order: the README's line on the last landing, the plan of 2026-10-29, the main
goal's page. Built on the chain of `on_mains_204ee91ed/` (after card C17), as its next three commits. The card is
`relays/cards/cld-advisor_C14_the-public-face-speaks-no-inner-language.md`.

**How to land it.** After the chain: `git am` patches 5 and 6; then `python3 0007_<...>.py <the checkout>` and
`git commit -F 0007_message.txt`. Tried on a clean checkout of patch 6: the script says the tree is the one this seat
built (`6ce6816c54264c4cc240250fdb30c582044cfa7a`).

| patch | your word | what it does |
|---|---|---|
| `0005` | M24: the README's "last landing" printed a changelog heading | the line gives the landing's day and where its entry stands, not the heading's words; a test makes the block from a planted heading of six inner words, and it counts none (the line as it stood counts them) |
| `0006` | M25, answer 2: the plan off the list, labelled | the plan leaves the public face's list; one line under its title labels it a dated proposal of the working record; the README's line adds "a dated document of the working record"; a test holds the three |
| `0007` (a script) | M25, answer 1: the main goal's dated paragraphs archived | the whole page is archived byte for byte in `docs/MAIN_GOAL_HISTORY.md`, in the form of the README's archive, held by its sha-256; the living page is written again in plain words, four short sections, each line naming the archive's section it comes from; B1294's lock and the outside bench's certificate of cell 10 read the archive |

**Why patch 7 is a script.** The archived page quotes a person in a few places, and a diff would carry them in its added
lines (the archive) and its removed lines (the page). The script makes the archive by copying the page's own bytes in
the checkout; no line of the old page is written in it.

**The choice in patch 5** is the builder's and yours to change: the line stays with the day and the place, and is not
dropped (a dropped line loses the day) nor named by each landing for itself (a new step for every landing, which no
gate holds).

## What was run

| | |
|---|---|
| every gate on a clean checkout of each of the three | `what_was_run_out.txt` (the count of landings red, as on the chain) |
| the public face's tests | 7 passed after patch 7; patch 5's new test fails on the generator as it stood |
| B1294's lock, the programme's page test, the README's test, B1028's ledger test | pass |
| the check of facts on the front pages | passes |
| the gate `public-face` | 13 pages, 5 at zero, 1,359 words held after patch 7 |

## What is next in the card, and what goes back to you

- **"The programme so far"** (answer 3): archived byte for byte with its readers' checks and appendix, and a short
  living page written in plain words with every line's source. **It needs one session that did not write it to read it
  before the README points to it**: the patch will come with the page and the README unchanged, and that reading is
  yours to arrange.
- **The views as labelled working indices** (answer 4), **the paper's inner words as errata** (answer 5), then the
  vocabulary, the plan's two front pages and the foundation, in that order.

## How each thing here was checked

| | the label |
|---|---|
| the choices (patch 5's line; the living page's words) | the builder's; yours to change |
| the archive | byte for byte, held by its hash; tested against a planted change |
| the gates and the tree | computed once |
| all of it | not independently checked |
