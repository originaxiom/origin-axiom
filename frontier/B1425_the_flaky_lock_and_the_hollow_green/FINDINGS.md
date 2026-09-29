# B1425 — THE FLAKY LOCK WAS NOT FLAKY, THE STALE ROW WAS MINE, AND THE MANIFEST NAMED A COMMIT ONLY I COULD SEE

cc, 2026-09-18. Round two of an outside review. **Owner's instruction: "verify all always, don't get
gaslighted."** Every claim re-derived here before acting, including the referee's favourable ones.
**Verdict: PROVED (the audit). Three remaining defects confirmed, all fixed; one new error class minted; and the
referee's own charitable finding turns out to be wrong in our disfavour.**

## 1. "THE PACKAGE PASSES" — IT DOES NOT, AND THE FAILING LOCK WAS NEVER FLAKY (E83)
The referee's round-two correction reported the package passing end to end, 727 passed and 0 failed, and called our
changelog an undersell. Run here on our own tree: **1 failed, 728 passed.** Chased rather than shrugged at:

- The failure is `test_b1411_sm_harvest::test_b1355_geometry_is_exact`, and it is **not load and not a timeout**.
  Its script does `sp.solve(..., list(X.free_symbols))` — handing a **set** to a solver as its list of unknowns —
  then compares the answer to one written-out dictionary. Set iteration order depends on string hashing, so the
  solver normalises its answer differently from run to run.
- **Measured, pre-fix version pulled back out of git and run beside the fixed one: PASS on seeds 4 and 7 only,
  FAIL on 0, 1, 2, 3, 5, 6 — two runs in eight.** The failing set is *reproducible*, which is exactly what
  separates this class from flakiness: a flaky lock fails at random, this one fails on the same seeds every time.
- So the referee's clean run was luck, and so was this bench's earlier "passes in isolation". Worse, on 2026-09-17
  this bench *diagnosed it as a timeout under load and raised the timeout* — a wrong diagnosis that would have left
  it failing four times in five forever. That comment is corrected in place rather than deleted.
- Fixed twice over: the unknowns are sorted, **and** the assertion now tests the mathematics — substituting the
  solution back must give a multiple of the identity, whichever variable sympy solved for — rather than one spelling
  of the answer. **Verified PASS on eight consecutive seeds.**
- **Class minted as E83** and swept over all **3 872** tracked `.py` files: **34 order-sensitive sites, 30 of them
  unsorted at the point of use**, touching **five shipped locks**. All five were run together under five seeds —
  28 tests, green on every one — and they are stable because each indexes a single symbol, where order cannot bite.
  (An earlier pass of this sweep used narrower patterns and reported sixteen sites and four locks; the number here
  is the wider measurement, and it is the one the evidence file carries.)

## 2. THE STALE GENERATED ROW — CONFIRMED, AND IT WAS OUR OWN GATE'S BLIND SPOT
Exactly **1 of 57** chain-table rows disagreed with the generator that produces it: link 43 carried the Weinberg miss
as `0.9\%` where the generator emits `0.8\%`. Cause, ours: on 2026-09-17 the generator was corrected and the paper
rebuilt, but the **generated block was never re-spliced**. The gate that exists to catch exactly this read
`rows[:6] + rows[-3:]` — **9 of 57** — and the stale row sat in the 48 it never looked at. Both fixed: the block is
re-spliced (all 57 rows now match the generator verbatim, checked programmatically and in the built PDF), and the gate
reads **every** row. A drift gate that samples can only see drift at the ends.

Related and also ours: the regression test written yesterday asserted **one literal string** rather than the class, so
the third occurrence — inside the generated block — passed it green. It now asserts the figure is absent everywhere it
could be the Weinberg miss, with a bite control confirming a planted `0.9\%` is caught.

## 3. THE MANIFEST NAMED A COMMIT ONLY THIS BENCH COULD RESOLVE — CONFIRMED, AND OUR CHECK WAS CIRCULAR
`MANIFEST.json` recorded `git_head ddff9c63`. It resolves here and **nowhere else**: it is not an ancestor of HEAD and
is on no remote-tracking branch, because the manifest was built before a commit that was then amended, leaving the
recorded object dangling in this bench's store alone. **Yesterday's verification that "147/147 locks are present in
that commit" passed only because it was run against that dangling object** — a check made against something only the
author can see is not a check. `build_manifest.py` now records `git_head_published` and `git_tree_clean` beside the
hash, prints a warning when HEAD is on no remote, and a new lock asserts the recorded commit resolves, is published,
and is an ancestor of HEAD.

## 4. THE HOLLOW GREEN — CONFIRMED
`run_package.py` starts `all_ok = True` and `&=`-es it only against the steps that ran, so a `--seals` run printed a
bare **"Overall: PASS"** with no locks section beneath it. The verdict now names its coverage:
*"PASS (partial: only seals ran)"*, and the unqualified word is refused unless all three steps ran. The referee's
framing was generous — "you shipped a hollow green when you had a real one" — and §1 shows the real one was not there
either.

## 5. THE RETRACTIONS INDEX HAD DRIFTED, AND THE PAPER WAS QUOTING ITS OLD LENGTH (found here, not reported)
The paper tells its reader that the record's retractions index holds **twenty-seven** corrected or withdrawn
statements. The index held twenty-seven rows, so the sentence was checkable and checked out. But **neither of the
last two corrections had a row at all**: E82's arithmetic fillings (2026-09-16, the owner's catch) and E83's wrong
load diagnosis (today). `retraction-debt`, the gate built for exactly this, fires only on arcs whose own
`arc_verdict.json` says `RETRACTED` — and both corrections landed as **addenda on the arcs that erred, computation
kept**, which is the form `docs/PRACTICES.md` recommends and which never sets that verdict. **The index therefore
lags precisely for corrections done the right way.** Both rows written; the count is **29**; the paper and
`paper_provenance.py` say so; and a lock pins the paper's spelled-out number to the index's row count in both
directions, with a control confirming it goes red on disagreement.

## 6. A READER MEASURED THIS RECORD AT 101 COMMITS AND REASONED FROM IT — the history is complete, the package let them not notice (owner-raised)
An outside reader reported main as a **101-commit** repository with no shared history with an audit lane, and drew structural conclusions from it. Checked here against git:

| the claim | measured |
|---|---|
| main has 101 commits | **3 457**, identical on both mirrors, same tip, no `shallow` file, no grafts |
| the lane has 2 965 commits, a separate programme | 2 965 **total including main's shared history**; **110 unique** since the fork |
| no merge base, different roots | **same root commit**; merge base dated 2026-09-05 |

101 commits back on main reaches 2026-09-14: the reader was seeing **four days**. The cause is on their side, a depth-limited clone — but **nothing in what we ship let them notice**, and that is ours. The package named its two mirrors and gave no clone command and no statement of the history's size. Worse, two of the package's own checks, *is the recorded commit published* and *is it an ancestor of HEAD*, **answer wrongly and silently on a shallow clone** — the same failure shape as §3, where a check ran against an object only the author could see.

Repaired so a truncated clone announces itself: the manifest records `git_commits` and `git_shallow`; the runner compares the clone it is running in against that number and prints a warning **into the report as well as the terminal**; the README states the expected count, gives the clone command without `--depth`, names `git fetch --unshallow`, and says which two checks go quietly wrong. Control: a planted impossible length fires the warning and reaches `REPORT.md`; the true length is silent.

**The general rule this is the third instance of:** a check that can be satisfied by an incomplete view of the evidence is not a check. §2 sampled 9 rows of 57, §3 resolved a commit only the author had, and this one measured a history the reader did not have.

## 7. FOURTEEN ARC VERDICTS VIOLATED THE SCHEMA, AND THE LANDING RITUAL COULD NOT SEE IT
`tests/test_arc_verdict_schema.py` was failing on **fourteen** consecutive arcs, B1411 through B1425 — every arc banked since the consolidation. Two causes: **seven** (B1411–B1417, landed 2026-09-15/16) carry the verdict word `VERIFIED`, which is not in the schema's closed enum and is defined by no governance document; **seven** (B1419–B1425) omit the `creates_law` and `identifications` declarations that arcs from B1103 and B1231 must carry.

**Why it went unseen is the point.** The landing ritual runs `scripts/gates/gates.py`, which reports 33/33 in a few seconds; this test runs only in the full suite, which takes an hour and a half and had not been run to completion since the consolidation. **The gate set and the suite disagree about what is checked, and every landing this week reported the gates.** Repaired: the seven `VERIFIED` verdicts normalised to `PROVED`, each carrying a `verdict_note` that records the change and its reason rather than erasing it, since the word meant "the seat's result was re-run and held on main", which is what `PROVED` means for an audit arc here; the seven missing declarations filled, `creates_law: false` and `identifications: []`, which is what the schema documents for an arc that makes neither.

## 8. AN ARC SHIPPED A TRACEBACK AS ITS EVIDENCE (E83 seen from the other side)
B1411's committed receipt `main_b1355_geometry_run.txt` ends in a `Traceback` and an `AssertionError`, while the arc's claim says its locks "re-run green on main's bench". **The failure was on disk, committed, readable, for three days.** It is E83's failure published as evidence: not merely undiagnosed, but shipped. The receipt is regenerated from the fixed script and the failing one is kept here as `b1411_receipt_as_shipped.txt`, so the repair cannot erase what it repairs.

Swept: **1 458** tracked receipts, **47** carry a failure marker. Most are legitimate — this record deliberately preserves failed runs and names them (`FAILED_RUN_1.txt`). The defect is a receipt whose failure neither its filename nor its arc's text acknowledges: **15 of those are silent**, registered as **L223** with the sweep as the work list. A receipt that contradicts its arc's claim means either the claim is wrong or the receipt is stale, and from outside you cannot tell which.

Five findings in this arc now share one shape, and it is worth naming once: **§2** sampled 9 rows of 57, **§3** resolved a commit only the author had, **§5** counted an index nothing compared against, **§6** measured a history the reader did not have, and **§8** wrote a receipt nobody opened. Each is a check satisfied by an incomplete view of its own evidence.

## 9. FOUR LOCKS WERE PINNING STATES THE RECORD HAD LEGITIMATELY MOVED PAST
Running the full suite to completion a second time left five failures. One is expected (the manifest is stale until it is rebuilt after the commit). **The other four had been failing before any of this session's work, and each fails because the record improved:**

- **A lock read a branch that no longer exists.** `B1035`'s verifier hardcodes `origin/audit/b775-braver-questions`,   deleted on 2026-09-15 under the retirement rule *tag, then delete*. The bytes are in the archive tag. Fixed by   resolving the branch if present and the tag otherwise: **a retirement must not break a receipt.**
- **A lock asserted a backlog is still open.** `B1412` left 15 of 342 relays OPEN and escalated each by name; the   lock asserted they are *still* OPEN. The backlog was then paid — all 342 now read BANKED or DECLINED — so the   lock went red **for the arc having succeeded**. Rewritten to the durable facts: the 15 dated escalations are   still recorded, and no relay from that window is left open.
- **A lock asserted a corpus statistic.** `B1400`'s sweep pinned `git grep -il "L-space"` at exactly 16 files; it   is 18 today. It also pinned `-ilw` at exactly 0 — true only because every occurrence then was the *plural*, whose   trailing letter blocks the word boundary. Both replaced by the comparison the sweep was actually for: on a   hyphenated term the two flags disagree, so `-w` under-reports.
- **A lock asserted that seven ideas remain absent from the record**, and four have since entered by way of a   handoff intake and the paper's own later citations. Absence measured on a date is a finding; absence asserted   forever is a rule that the record may not grow. Rewritten so the terms still absent are still checked and the   ones that entered are **named in the test**, which records the drift instead of hiding it. Same repair for the   Jørgensen check: the finding was that two mathematicians of that name are **different people**, not that one of   them is missing, and the record now cites both.

These four join §7's fourteen: **eighteen locks were red before this session and the landing ritual could not see any of them**, because it runs the gates. The suite went 22 failures → 1 (the expected manifest), and the shape is the arc's own: a check nobody runs is a check that is not there.

## What the referee got right, verified here
The `.gitignore` fix holds and the census file is tracked; the census paragraph carries both populations with the
right conclusion; the Menal-Ferrer–Porti translation is correct at the source (`n ≥ 2 ⟺ m ≥ 1`, since the
n-dimensional irreducible is the (n−1)-st symmetric power); the figure caption, tick loop and failure-naming landed.
Their scan for locks reading untracked data agrees with ours: zero.

## Evidence
`verification/hash_seed_evidence.py` pulls the pre-fix script out of git and runs both versions under eight seeds;
`verification/order_sensitivity_sweep.py` is the corpus sweep. Both write their JSON beside them and both are read
by the lock, so the numbers in this document cannot drift from the measurement.

## Locks
`tests/test_b1425_determinism.py` (the script under several hash seeds, and the corpus sweep's shipped locks under
several more); the chain-table gate now covering all 57 rows; `tests/test_b1424_referee_defects.py` extended with the
manifest-commit assertions and the class-level percentage check.
