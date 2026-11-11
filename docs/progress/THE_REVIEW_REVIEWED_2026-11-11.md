<!-- doc-currency: frozen -->
# The review, reviewed: what it does, what skips it, and how to raise it

*Main, 2026-11-11. A proposal, **not in force**. The owner asked to see the code, the structure and the logic of the
periodic review before it runs again, so that its job is understood, nothing skips it that should not, and it is
brought to the highest standard, in line with the way the repository is now worked: sessions with pages and cards, a
check named by its method, and a light public repository to come. The advisor seat is asked to read this as well. The
review that is due, Review 79, waits on this page.*

## 1. In one minute

- **What the review is.** Every 20 landings a check of everything landed since the last one falls due. At 40 the push
  is blocked until it is run, or the owner waives it.
- **What it does well.** It never lets an open item drop, it catches a branch nobody is watching, and it checks that
  sealed files were sealed before their results.
- **Its largest hole.** It reads in full about one arc in six of what landed. The rest is skimmed.
- **Its second hole.** Main runs it on main's own work. A builder judges its own build.
- **Its third hole.** It does not know the things made this week: the sessions' pages and cards, the labels for how a
  result was checked, the rule that the owner's messages are private.
- **The proposal.** Every arc is read by a session that did not build it. The review states its own catch rate,
  measured on faults planted for the purpose. Its trigger counts work, not commits.

## 2. Its job, in one sentence

Today no page says it in one. Proposed:

> **At a fixed interval, establish — by someone other than the builder — that everything landed since the last review
> is what the record says it is, that nothing owed was dropped, and that the instruments still catch what they are
> for; and say exactly what was not looked at.**

Four duties follow, and every step below serves one of them:

| duty | the question |
|---|---|
| truth | is each thing landed what its page says it is? |
| nothing dropped | is every open item, every seat's delivery, every promise still carried by someone? |
| the instruments work | do the gates and locks still catch what they are for? |
| honesty of scope | what did this review not look at? |

## 3. What it does today

Two halves. The first is a script; the second is main's reading.

**The mechanical half:** `scripts/review/review_tools.py`, 464 lines. Each check is a function that can fail on planted
input.

| step | what it checks | duty |
|---|---|---|
| the loop | every open item of the last review is resolved or carried, with its age in reviews | nothing dropped |
| the branch inventory | every unmerged branch is registered as a lane | nothing dropped |
| the window | which commits and which arcs the review covers | honesty of scope |
| the sample | a draw, by seed, of the arcs to be read in full: one in six, at least five | truth |
| rows added | what entered the law map and the theorem registry | truth |
| error classes | new rows of the error ledger: a new class, or an instance of a known one | the instruments |
| provenance | phrases that pretend outside verification, on lines added in the window | truth |
| terms | words the window leans on that the terminology page does not gloss | truth |
| seals | hashes unchanged, sealed before results, the seal on every mirror | the instruments |
| gate controls | every gate has a test that names it | the instruments |
| the full suite on a fresh clone | a separate step, four hours | the instruments |

**The reading half:** `docs/progress/REVIEW_TEMPLATE.md`, eight required items. Main reads the sampled arcs, says what
advanced, sweeps for promotions, and writes the action items. Since Review 74 cheaper readers have read the sample for
main; their quotes are checked by machine.

**How it is banked.** One entry in `docs/progress/REVIEWS.md`, ending in a block of action items, with the commit it
anchors on. The next review starts from that block.

**How it is enforced.** The gate `review-fires` in `scripts/gates/gates.py`: due at 20, a block at 40. The owner alone
may waive it, by a dated line in `docs/progress/REVIEW_WAIVER.md`.

## 4. What skips it today

Ordered by how much it lets through.

| # | what skips | how |
|---|---|---|
| 1 | **five arcs in six** | the sample is one in six. An arc outside the draw is not read in full by the review. Review 78's readers found ten real faults in the arcs they did read |
| 2 | **the builder's own blind spots** | main runs the review on main's work, and the judgement half is main's alone. The rule now is that no session judges what it built |
| 3 | **the suite on a fresh clone** | it is a separate step of four hours and a review can close without it. The record's package for it is not done |
| 4 | **work that is not a commit on main** | the sessions' branches enter only through harvest rows. 560 items stand registered and unread, and the review counts them but does not shrink them |
| 5 | **what was not known to it** | pages and messages to sessions; cards; whether outputs were committed before they were read; the labels for how a result was checked; quotation of the owner after 2026-11-11 |
| 6 | **corrections that did not travel** | a correction is checked where it was made. Whether the old statement still stands elsewhere is checked only where an arc's own lock sweeps for it |
| 7 | **what is behind a mask or the firewall** | readers do not open masked lanes or targets. That is right, and it means nobody on main reviews that material |
| 8 | **other repositories under the project's name** | `oa-distill` and an older one are listed as "not read" |
| 9 | **the review itself** | nothing measures how much a review catches. A reader's proposed closure held 24 times in 73 when it was checked |
| 10 | **the trigger** | it counts commits. A commit that only regenerates views, or only writes to a session's page, counts like a landing of mathematics. With messages now frequent it would fire every few hours, and be waived |

## 5. The proposal: three layers and a measured catch rate

### Layer A — the mechanical layer: a function of the commit, all green or the review does not open

Everything the script does today, and seven checks it lacks:

| new check | what fails it |
|---|---|
| a card before the work | a delivery of a session whose card was committed after its outputs |
| outputs before the page that reads them | a result page committed before or with its outputs |
| a label names its evidence | a result marked "recomputed independently" with one script behind it |
| the owner is not quoted | a quotation of him in a tracked file or a commit message after 2026-11-11 |
| no session as an authority | "accepts", "approves", "rules", "verdict" with a session as subject, in a page a stranger opens |
| messages are answered | a message on a session's page older than a set age with no status file that has read it |
| the unread remainder does not grow | more registered-and-unread items than at the last review, with no card that names them |

Most of this is tooling of the kind the advisor seat builds. Its package on labels already covers the third.

### Layer B — the reading layer: every arc, by a session that did not build it

- **No sampling for what carries weight:** every arc of the window that is upstream of a claimed value, that changed a
  verdict, or that corrected an error is read in full.
- **Sampling only for the rest,** by seed, drawn after the window closes, and the review says which arcs it left.
- **The reader is not the builder.** Main's arcs are read by a verifying session; a session's deliveries are read by
  main or by another session. This is the ring that already verifies.
- **A reader returns findings with quotes,** checked by machine. A reader closes nothing.

### Layer C — the answer: main answers every finding, and says what is left

- Each finding is reproduced on main, then mended, or disputed with the computation.
- Nothing is closed on a reader's word.
- The result is one page for the owner in plain words: what was found, what was mended, what was not looked at.

### The catch rate: the review is tested against planted errors

Before the readers start, a session that is not reading plants a known number of faults in a scratch copy of the
window: a wrong number, a claim wider than its proof, a correction that did not travel, a seal broken. The readers do
not know which or how many. The review reports how many they caught.

- **A review then carries its own label:** tested against planted errors, with the count.
- **A low count is a finding about the review,** and it is fixed before the next one.
- This is what main already does to the tooling a session builds, turned on the review.

### The trigger: count work, not commits

- **Counted:** a landing that adds or changes an arc, a verdict, a gate or a governing page.
- **Not counted:** a commit that only regenerates views; a commit that only writes to a session's page.
- **Also due on content:** when ten arcs have landed, whatever the number of commits.
- The block and the owner's waiver stay as they are, and a review quotes every waiver it follows.

## 6. What stays exactly as it is

- The loop: no open item is dropped, and each carried item shows its age.
- The branch inventory.
- The seal checks.
- The rule that the review is a block and not a report.
- The rule that changes to governance are made in arcs of their own and never inside a review.

## 7. What it costs

| | today | proposed |
|---|---|---|
| arcs read in full | one in six | all that carry weight; a sample of the rest |
| who reads | main, with cheap readers | verifying sessions and cheap readers; main answers |
| main's time | most of a day | less: main answers findings and does not hunt for them |
| the sessions' time | none | one card each for a review |
| new tooling | none | seven checks and a planting script |

These are estimates. Nothing has been built to measure them.

## 8. What only the owner can settle

1. **The standard of reading.** Every arc that carries weight, as proposed; or the sample, as now.
2. **Who reads main's work.** A verifying session, as proposed; or main with readers, as now.
3. **The order.** Run Review 79 by the new rules as far as they can be followed this week, building the missing
   checks after; or build first and run later, under a longer waiver.

## 9. Asked of the advisor seat

A read of this page: what is wrong, what is missing, and which of the seven checks belong in the packages it already
builds. It builds nothing for this yet.

## Disclosed

- **Main wrote the present review's code and ran every review.** It is a party to a judgement on its own instrument.
- **The count "one in six" is the script's rule,** `max(5, len(arcs) // 6)`. Earlier reviews drew other fractions.
- **The proposal has not been tried.** The catch rate of a planted review is not known until one has been run.

## 10. Settled on 2026-11-11, and how Review 79 is run

*Added the same day. The sections above are kept as they were written.*

The owner ruled that the choices of § 8, and the question of a longer waiver, are settled by what best protects the project's integrity (register row P-805). Main settles them so:

| the choice | settled |
|---|---|
| the standard of reading | every arc of the window is read in full; nothing is sampled |
| who reads main's work | two sessions for each arc, neither of which built it; main answers every finding and closes nothing on a reader's word |
| the order | Review 79 runs now, before any more mathematics is banked |
| the waiver | not extended; main withdraws its recommendation of a longer one, which was for convenience |

**Who reads what.** The window is thirteen arcs, all main's. The rules for a reader are § 13 of `docs/seats/README.md`.

| what | first reader | second reader |
|---|---|---|
| B1878, B1880, B1883, B1886 | the web seat | agy-002 |
| B1879, B1881, B1885 | the SM seat | agy-exp |
| B1882, B1889 | the web seat | the SM seat |
| B1884, B1887 | the SM seat | agy-002 |
| B1888 | the web seat | agy-exp |
| B1890 | agy-002 | agy-exp |
| the locks on five corrections that have had one re-audit each (E3, E5, E6, E10, E13) | the SM seat, with errors it plants | — |
| the two corrections of this date (B1221's control row; the unit on three lines, B1641) | agy-002, which found them | agy-exp |

- **No session reads an arc about its own work.** The web seat reads none of the four arcs that verify its relays
  and cards; agy-exp does not read the arc on its loop.
- **The arc that ran a sealed card** (B1882) goes to the two sessions that are not read through a mask.

**What is not done in Review 79, and is said in its entry:**

- **The test against planted faults** (§ 5). Main found no way to give the readers a planted copy without putting
  false statements where a stranger could take them for the project's, and no way to stop a reader comparing the copy
  with main. In its place, what the two readers of an arc find in common gives a first estimate of what one reading
  misses. That estimate flatters the readers: a fault that is easy to find is found by both.
- **The seven new mechanical checks** (Layer A) are not built. Those that can be done by hand are done by hand, and
  the entry names which.
- **The trigger** still counts commits.

**What changes after it,** in an arc of its own and with the advisor seat's read: the template, the tools and the
trigger.

### Added the same evening: what the advisor seat's read changes

The advisor seat's read of this page came in after § 10 was written (harvest row 1712). Main has read it in full and
reproduced three of its facts. It stands as register row P-806.

**What skipped the review and was not in § 4:**

| what | how |
|---|---|
| the block can be switched off from the environment | one variable, kept for the gate's own test, makes the blocking gate read no landings. Reproduced by main |
| a sentence moves the anchor | the count is taken from the last anchor named anywhere on the reviews' page. No gate ties an anchor to a review's entry |
| an arc that was changed and not added is in no pool | eleven in this window. One changed its verdict from proved to open |
| the draw is known while the window is open | the seed is the last review's anchor |
| a change that belongs to no arc has no reader | ten instruments and governing pages in this window |

**What was wrong in this page:**

- **§ 3 counts a gate's control by its name.** A name is not a control: with every gate made unable to fail, 16 of 53
  controls still pass, by the seat's third series.
- **§ 5's Layer A is not a function of the commit alone.** Three of its seven checks read the sessions' branches. What
  can be said: a function of the commit and of the tips it names, with every age taken between two commits' dates.
- **§ 5's catch rate is half a measure.** It needs what the readers report that is not there, beside what they catch.
- **A broken seal** is an instrument's to catch, not a reader's.
- **The rule that sorts a commit as work** is itself an instrument, and is tested like one.

**What Review 79 takes from it now:**

| | how |
|---|---|
| the changed arcs are read | the eleven whose verdict file changed and the fourteen whose findings changed. Six of them were read twice already, in the re-audits and in the web seat's check of two corrections. The rest go to the web seat and agy-exp, as the window's difference |
| the changes outside any arc are read | the governing pages by the web seat and agy-002, with the two arcs that carried them (B1878, B1886); main's changes to the checkers, the gates' file and the listener by agy-002 and the SM seat |
| the environment is printed | the entry says which variables of the project were set: none |
| the instruments carry a count | tested against planted errors, n of N: the advisor seat's suite, run by main on a fresh clone at the review's head |
| false alarms are counted | for each reader, how many findings held when main reproduced them and how many did not |

**The rule for "the same finding",** written here before a second reader's file on any arc was opened: two findings are the same when they name the same arc and the same file and their quotations overlap. What two readers find in common then gives a ceiling on the rate at which one reading catches a fault, since a fault that is easy to find is found by both. The entry prints the counts, and the estimate with one added to each count where the counts are small.

**One reader changed.** The web seat left B1889, since the arc judges its work; agy-002 reads it in its place, except the part on its own family's sessions.

**What waits:** the two ways to switch the block off are closed by the seat's fourth series, which main has not yet
verified; the planted copy for readers needs a copy handed over without its history, and a second copy with nothing
planted as its control.

