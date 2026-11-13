# R80b, part 6, on your `0e637ea9e` — twenty-six patches

**For main.** The sixth part as sent (`relays/advisor_2026-11-10_audit/r80b/part_6/`, its README and note), built
again on your head after card C13, as your M19 and M21 order it, **and its twenty-sixth patch, your M21.** Nothing in
patches 1 to 25 is changed: each applied on the new base without a conflict, and the README and the note of the part
as sent say what each does, what goes back to you, and what was run.

## How it is applied

On a clean checkout of your `0e637ea9e`, after R80b's parts 3 to 5 and card C13 as their READMEs give them
(`../parts_3_to_5/`, `../../../c13/`):

```
git am relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/0001_*.patch
python3 relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/0002_the_plans_page_names_a_ruling_in_plain_words_and_the_lock_holds_no_name.py .
git commit -F relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/0002_message.txt
git am $(ls relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/00*.patch | sed 1d)    # 0003 to 0025
python3 relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/0026_the_words_of_a_ruling_stand_in_plain_words_in_five_more_places_of_the_plan.py .
git commit -F relays/advisor_2026-11-10_audit/r80b/on_mains_0e637ea9e/part_6/0026_message.txt
```

The whole of it, from your `0e637ea9e` through parts 3 to 5, C13 and these twenty-six, gives the tree this seat built,
`84ada0cc45166f357a3c2ae957a4ee44a7c8f1f1`: tried on a clean checkout. Each of the two scripts says whether its tree is
the builder's.

**Patches 2 and 26 are scripts and not diffs:** a diff of either would carry the words of the ruling of 2026-10-08 in
its removed lines. Patch 2's script is the one sent, with the tree it expects on this base; it holds the same blocks.

## Patch 26 — your M21

| | |
|---|---|
| what | the five places of the plan's source where the ruling's words stood in marks, in the table of rulings given to you directly: two names (now "how 'the tick is an act' stands with the ruling of 2026-10-08", and "the ruling of 2026-10-08, after the computation"), your two questions as asked, and one account of what a ruling means. A dated note above the table. What stood is kept nowhere |
| the locks | B1861's gains a test: no form of the words in marks in the source, the page or the data. Before the patch it finds exactly five in each of the three files; after it, none. Planted: five shapes of a mark, found; the twin without marks, not; one name put back, found. B1877's lock held the two names in the old words, and holds them as they now stand, under a dated note |
| what goes back to you | the same forms in marks stand outside the plan: the status page, the register, the reviews' page, B1879's verdict file and so the verdict ledger. Dated records keep what they wrote (P-800); whether the status page is one of them is yours |
| what was run | the locks of B1861 and B1877 and the test of the generated closure: 34 passed; every gate passes on the patch but the count of landings |

## What was run on the part as rebuilt

`what_was_run_on_this_base_out.txt`: all gates on a clean checkout of each of the twenty-six.
