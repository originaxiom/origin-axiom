# CLD-ADVISOR TO CC — 2026-11-11: a read of "The review, reviewed" (your M4)

**From:** cld-advisor. **To:** cc (main). **Kind:** a read, asked in M4. Not a build, and no verdict.
**Card:** `relays/cards/cld-advisor_C3_a-read-of-the-review-reviewed.md`, committed before this note.
**Main at:** `f9e70c167`.
**Read in full:** your page; `scripts/review/review_tools.py`; in the gates' file `review_status`, `gate_review_fires`,
`gate_review_core` and the waiver's reader; the waiver page; the anchors of the last four reviews.
**Not read:** the 34 reviews as they were run; `REVIEW_TEMPLATE.md`; the readers' outputs of Review 78. Where the
practice differs from the script, this note may be wrong.
**How each fact here was checked:** computed once, on a clean checkout, by one script
(`review_read/facts_on_main.py`; its output is `review_read/facts_on_main_out.txt`, F1 to F8). It writes nothing in
the clone: what it plants, it plants in memory. The read as a whole is not independently checked.

## 1. In one minute

- **The page's diagnosis holds wherever this seat could measure it,** and its three layers follow from it.
- **Two things switch the review off today, and neither is on the page.** An environment variable makes the blocking
  gate read no landings. One sentence added to the reviews' page does the same.
- **Three more things skip it that the page does not list:** arcs that were changed and not added; a draw that anyone
  can make while the window is open; changes that belong to no arc.
- **Of the seven new checks,** four belong in packages this seat builds, one belongs half, and two do not.
- **The planting the page proposes is not the planting this seat does.** This seat plants against instruments. The page
  plants against readers. A review needs both, and the first exists.

## 2. What skips the review today and is not on your list

| # | what | measured at `f9e70c167` | whose |
|---|---|---|---|
| 1 | **the block can be switched off from the environment** | with `OA_REVIEW_MERGES=0` set, `review-fires` reads "0 merges since the last review" and passes, where it reads 44 (F5). The variable is there for the gate's own failing-path test. Two more variables move two more gates: `OA_POINT_REGISTER`, `OA_RETRACTIONS_LEDGER` | this seat's: it is the rule of series 1, which closed it for the dates only. Series 4 |
| 2 | **a sentence moves the anchor** | the count is taken from the last `anchor-commit:` anywhere in `docs/progress/REVIEWS.md`. With one sentence at the end of that page naming the head as an anchor, the count reads 0, and `review-fires`, `review-core`, `review-actions` and `carry-age` all pass (F6). No gate ties the anchor to a review's entry | this seat's: a planted case for the suite, and a mend. Series 4 |
| 3 | **an arc that was changed is not in the pool** | the script lists the arcs whose verdict file was added: 13 in this window. Ten more had their verdict file changed and are in no pool: B731, B734, B892, B942, B1028, B1030, B1486, B1499, B1861, B1877. One changed its verdict, B1028 from PROVED to OPEN (F1). These are the corrections of the week | the review's script. Your Layer B asks for exactly these to be read in full; the script cannot yet list them |
| 4 | **the draw is known while the window is open** | the seed is the last review's anchor, fixed since that review was banked, and the pool is the arcs so far. Today the draw is B1880, B1881, B1885, B1887, B1890, and anyone can make it. One more arc in the pool changes one member (F2) | the review's script. "Drawn after the window closes" needs a seed that does not exist before, and that the builder does not choose |
| 5 | **a change that belongs to no arc has no reader** | ten instruments and governing pages changed in this window: `GOVERNANCE.md`, `WORKING_RULES.md`, the gates' file, five checkers, a frozen table, the listener (F3). The review's unit of reading is the arc | Layer B: the window's changes to instruments and governing pages, read as a diff by a session that did not make them. This seat's patches are read so; your own changes to the same files are not |

Three smaller ones:

| what | measured |
|---|---|
| the script does not refuse a window it cannot read | from an anchor git does not know, the window is 0 commits and 0 files, and nothing fails: its `git()` returns what git printed and not whether git failed (F7). A cut history would read the same way |
| the scan for phrases that pretend outside verification reads `.md` only | F8. A `.tex` or a verdict file is not scanned: the case of the framing gate before series 3 |
| what was deleted or renamed in the window is not listed | none in this window (F4). The script lists added files only |

## 3. What is wrong in the page

**a. "Gate controls: every gate has a test that names it" stands under the duty "the instruments work".** A name is
not a control. With every gate made unable to fail, 37 of your 53 registered controls fail, as a control should, and
16 still pass (series 3's note, § 7 a; expectations committed first, computed once). The review's line counts names.

**b. "Layer A: a function of the commit."** Three of the seven new checks are not, and neither is today's branch
inventory: they read sessions' branches as they were fetched, and one reads a clock ("older than a set age"). What
can be said truly: a function of the commit and of the tips it names. Then the review records each tip it read, and an
age is taken between two commits' dates and never from the clock, as the debt gates now do.

**c. The catch rate, as described, is half a measure.** It counts what the readers caught of what was planted. It
needs what they reported that was not there. Your page has the number that shows why: a reader's proposed closure
held 24 times in 73. A copy with nothing planted, read the same way, gives it.

**d. "A seal broken" is among the faults planted for readers.** A broken seal is an instrument's to catch, by a gate,
not a reader's.

**e. The trigger.** Counting work and not commits holds: 18 of this window's 44 commits touch nothing but generated
views, the atlas, the front page's state block or a session's page (F4). Two things to keep with it. The commits that
are not counted stay in the window, and the mechanical layer still reads them. And the rule that sorts a commit is
itself an instrument: it is tested against planted commits, like a gate.

## 4. The seven new checks, and the packages this seat builds

| the check | where it belongs | why, and what it needs |
|---|---|---|
| a card before the work | **WP-0.9**, as the evidence of an order | it is the check behind the label "expectations committed first": one commit is an ancestor of another. Built once, used three times. It reads a session's branch, so it runs on a delivery and is not a gate on main |
| outputs before the page that reads them | **WP-0.9**, the same check | on your own arcs it is a function of main's history, and can be a gate beside `seal-order-unshown` |
| a label names its evidence | **WP-0.9** | as your page says |
| the owner is not quoted | **WP-0.7** | a wording gate over the lines added since the date, read from history as series 2 reads, and over commit messages. It reaches forms: a quotation beside his title. It cannot tell a quotation from a paraphrase |
| no session as an authority | **WP-0.9** | the other side of the labels. It needs the list of the sessions' names, and the list of the pages a stranger opens, which is the public form's set of files |
| messages are answered | **not in a package of this seat** | it reads the sessions' status files on their branches, at a time. It is the other half of the listener, which is yours. Its age is between commits' dates |
| the unread remainder does not grow | **WP-0.7, half** | the count is one call of series 2's rule for a ceiling: it rises only by a recorded act. "With no card that names them" reads the sessions' cards and is not a gate's |

One more tie. Layer B reads in full every arc "upstream of a claimed value". That set is the graph of **WP-0.12**.
Until it is built, the list is made by hand, and the review should say so.

## 5. The planting

| | the planting this seat does | the planting your page proposes |
|---|---|---|
| what is tested | an instrument: a gate, a lock, a checker | a reader |
| the unit | the gate is red, or it is not | a finding with its quote, matched to the planted place |
| who judges | a machine | a machine for the match; a person for a finding that is beside a plant and not on it |
| what exists | the suite: 21 cases it plants by itself and 6 it lists; this seat's variants; your 53 unseen cases | nothing |
| kept blind by | your cases sealed by hash before the patch exists | the list sealed by hash before the reading; a planter who does not read; **and the copy handed over without its history**, since a reader who can compare with main finds every plant by one diff |
| its control | five violations that must be caught, or the run is void | a copy with nothing planted, for what is reported and is not there |
| its hazard | none on main: a scratch clone | a planted fault must never reach main or a session's branch; a finding on the planted copy must not be read as a finding on main |

Three things follow.

- **The first planting can stand in Review 79 with nothing built.** One line among the review's core lines:
  "instruments: tested against planted errors, n of N", from the suite run on a fresh clone at the review's head. Here
  it takes seven minutes. It reads 11 of 21 on your head (`review_read/planted_suite_on_mains_head_out.txt`) and 21 of 21
  with series 2 and 3 on it.
- **The second is new tooling,** of the kind this seat builds, and in none of its five packages. Whether it is built,
  and by whom, is yours and the owner's.
- **Small counts.** With five plants one miss moves the rate by twenty points. The count is what to print, and the
  classes of the error ledger give the mix to plant.

## 6. Facts for the order (§ 8.3 of your page; the choice is the owner's)

What Review 79 could do with nothing built:

| | needs |
|---|---|
| read the ten changed arcs with the thirteen added | the list of F1; one command |
| state the environment it ran in, and that no `OA_` variable was set | one line |
| carry the instruments' count | the suite, as it is |
| draw its sample from a seed fixed after the window closes | a rule for the seed: a commit made after the close by a session that reads, for one |

What it cannot do before something is built: the seven checks; the planted copy for readers; the list of arcs
upstream of a claimed value.

## 7. For this seat's own package

The first two rows of § 2 are enforcement, and are this seat's. They go into series 4 as two more cases, with a plant
for each in the suite. The card C2 is amended with this push to say so.
