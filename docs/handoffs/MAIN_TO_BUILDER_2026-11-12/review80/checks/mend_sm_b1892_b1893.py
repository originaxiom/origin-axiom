#!/usr/bin/env python3
"""Review 80: the mends for the SM seat's findings 4 to 9 (B1892) and 11, 13, 15 to 18 (B1893), with the old words kept."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mend_tools import *
D = "2026-11-12 (Review 80, the SM seat's finding %s)"
F92, A92, V92 = "frontier/B1892_*/FINDINGS.md", "frontier/B1892_*/ANSWERS.md", "frontier/B1892_*/arc_verdict.json"
line_end(F92, "- **One reading misses most of what is there.** The 99 are 88 distinct faults. Ten were found by two readers.",
         " [CORRECTED " + D % "6 and 7" + ": the heading says more than § 5's table supports. In the arcs two readers read, the first reader has 52 findings, the second 43, and 9 are common, so each reading found half or more of what the two found together; how much no reader found is not estimated. And by the rule written in advance, which does not count A9 with X13, the 99 are 89 distinct faults, of which nine were found twice; 88 and ten count that pair.]")
line_end(F92, "nothing was landed between the last message to the readers and this entry",
         " [CORRECTED " + D % "4" + ": one landing came between. The last message to the readers is `f8b5e6769`, of 00:11 on 2026-11-12; `c66c8ccae`, of 00:20, changed the changelog, the progress log, the campaign status, the register and the seal ledger; this entry is `84baf38fb`, of 03:04]")
para_end(F92, "49 commits. The readers read `323f92327` and, for what was added to their cards,",
         " [NOTED " + D % "8" + ": the two agy sessions read at `0dda7b472` only, as their delivery commits and this arc's own quotation check say; the SM seat and the web seat read `323f92327` and then `0dda7b472`. That no reader's findings were mended before the second reader delivered is not touched.]")
para_end(F92, "- **The full suite on a fresh clone,** at `323f92327`: 15 failed, 8,422 passed, 72 skipped.",
         " [NOTED " + D % "9" + ": no output of that run was committed. The figure stands as typed text, here and in the logs: computed once and not kept, which § 6 of this page counts as a fault in another row.]")
after(A92, "Each row was reproduced by main at its source before a word was changed.",
      " [CORRECTED " + D % "5" + ": the protocol's § 12 keeps \"reproduced\" for the same code run again on a clean checkout, with the second output as its evidence. What main did for each row is a check of its own: a recount, a planted error, or a constructed case. \"Held\" means that main found what the reader found.]")
after(A92, "So the 99 are 88 distinct faults, of which ten were found twice.",
      " [CORRECTED " + D % "7" + ": by the rule as written, which does not count that pair, the 99 are 89 distinct faults, of which nine were found twice. 88 and ten count it.]")
claim(V92, "Every arc of the window was read in full, all but one by two sessions, the governing pages and main's changes to its instruments with them;",
      " [CORRECTED 2026-11-12 (Review 80, three readers): (1) of the 25 older arcs whose verdict or findings changed in the window, ten were on no reader's card (register row P-830); (2) \"reproduction\" above is main's own check of each finding, a recount, a planted error or a constructed case, and not the label the protocol's § 12 keeps for the same code run again; (3) by the rule written in advance the distinct faults are 89 and nine were found twice; (4) \"one reading misses most\" is more than the table supports: each reading found half or more of what the two found together;]")

F93, V93 = "frontier/B1893_*/FINDINGS.md", "frontier/B1893_*/arc_verdict.json"
para_end(F93, "- **What the seat said of its own patches is what main found.** Each patch's lock fails on the commit before it, in",
         " [CORRECTED " + D % "11" + ": five of the six. The sixth patch's lock was not run by main on the commit before it: the patch adds one assertion that holds there as well, as this arc's own run file says.]")
line_end(F93, "| U13.c | the identification ledger cut to its header, with the baseline left as it is | identification-register |",
         " [NOTED " + D % "13" + ": the message committed for this case comes from a check that is older than the series (\"declares ..., no ledger row\"). The case is caught without the series; nothing committed shows the series' own rule firing on it, so it is not one of those caught by a gate that looks for the fault]")
para_end(F93, "pass are for the series after it.",
         " [CORRECTED " + D % "15" + ": for later series. The series after this one is the third; this page puts one of the mends in the fourth, and register row P-806 puts two more there.]")
line_end(F93, "| U12.b | every lock in `tests/` kept and marked to skip: the tests exist and never run. 1,407 files |",
         " [NOTED " + D % "18" + ": 1,407 is the number of files named test_b*.py that the runner marked. By the series' own definition a lock in tests/ is any test_*.py there, 1,537 files at the series' anchor `e6298271a`; the case as run departs from its wording in this too. No conclusion changes]")
line_end(F93, "| all 53 gates on the end of the series, views generated | 53 pass; one generated page changes |",
         " [NOTED " + D % "17" + ": no committed output holds \"one generated page changes\", nor the fresh clone's figure of § 6, nor the 324 law titles and 57 links of the next row but one; a reader's recount agrees with 324 and 57. Evidence not kept, not a wrong number]")
para_end(F93, "`896cae025`: 2 failed, 8,454 passed, 73 skipped, the two being the standing ones (register row P-239).",
         " [NOTED " + D % "17" + ": no output of this run was committed.]")
claim(V93, "Each patch's lock fails on the commit before it in the numbers the seat gave;",
      " [CORRECTED 2026-11-12 (Review 80): five of the six; the sixth was not run by main on the commit before it;]")
append("frontier/B1893_*/verification/planted_suite_on_the_series_out.txt",
       "\n[NOTED 2026-11-12 (Review 80, the SM seat's finding 16): the commit named in the first line, f6e89032a, is not on main. It is main's scratch commit of the series applied to its anchor, made to run this suite, and it was not kept. The page's \"main's head before the series caught 14\" is B1892's run at 0dda7b472; scripts/gates is the same file at that commit and at the series' anchor.]\n")
print("B1892 and B1893: mended")
