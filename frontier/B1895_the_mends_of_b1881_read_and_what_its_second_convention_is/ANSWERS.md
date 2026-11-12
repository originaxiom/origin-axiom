# B1895 — main's answers to the four findings on B1881's mends

Each finding is an exact quotation, found by machine in the file it names at the commit that was read, `87bfa1f05`
(`verification/quote_check.py`). Main reproduced each at its source before changing a word. The reader's own rows are
rows 14 to 17 of its file.

| | arc | what was found | main reproduced it | what was done |
|---|---|---|---|---|
| 2A14 | B1881 | the mend of SM-11 calls the second convention the transpose of the seat's; the seat's ground is symmetric, so its transpose is itself; the convention is every word conjugated by the swap of the coordinates, on the column the mark annihilates; the docstring of the script's second function still names B1872 | yes, in full: by hand, then on all 120 matrices | corrected on the page, in the verdict line, in the script's header and docstring; the same word corrected in B1884's page and script, whose outputs are regenerated; the statement computed in this arc and held by B1881's lock |
| 2A15 | B1881 | "reproduced" for what was recomputed, in the verdict line and in § 1 of the page; the corrections of SM-11 and SM-16 had not reached the verdict line | yes for "reproduced", in both places. The name of the second convention was corrected in the verdict line by B1894 (answer 2X3), which landed after the reader had filed; that correction carried the wrong word of 2A14 | "recomputed" in both places, each keeping what it read; and in the script's header |
| 2A16 | B1881 | the script's label still says "every cyclic run sequence … (16275 sequences)", in the script, its file and its run, after the page was corrected for SM-17 | yes, in all three | the label corrected; the script computes the three counts and no longer types one; its outputs regenerated: 65 checks, none failing |
| 2A17 | B1881 | the lock holds two of the nine mends; the other seven can be undone with every test passing | yes: main took the arc as it stood at the commit read, undid the seven in five ways, and the lock passed each time (`verification/the_old_lock_with_the_mends_undone.py`) | five tests added; 18 planted reversions, all caught, with the control passing (`verification/planted_reversions.py`) |

Found by main while mending these, and not by the reader:

| | arc | what | what was done |
|---|---|---|---|
| M1 | B1881 | the check on the two conventions passed if any one of three readings agreed | it asks for the two the page states |
| M2 | B1881 | one line of the run printed a set, in an order that changed from run to run | sorted; the run is the same file at every run |
