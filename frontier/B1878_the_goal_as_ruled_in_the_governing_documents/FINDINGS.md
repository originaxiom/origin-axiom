# B1878 — The goal as the owner ruled it, carried into the governing documents; two gates

*Main, 2026-11-11 (S306p). The first landing of P-767: the first and third of the eleven rulings the owner confirmed
to main on 2026-11-10. It amends the governing document and two pages under it, and changes two gates. Nothing is
computed, and no status of the foundation changes. 0 of 19.*

## 1. The answer first

- **The governing document now states the goal as the owner ruled it:** the programme's only goal is a
  parameter-free theory of everything. The sentence it replaces is kept, with a dated note beside it.
- **The ceiling did not move.** A goal says what is sought. No page may say or imply that a value, or the Standard
  Model, has been derived. A new gate fails on such a sentence.
- **One document governs.** Three files each said that it prevails. `GOVERNANCE.md` is the governing document;
  `GENESIS.md` holds on the status of every item of the foundation, by its delegation; `CLAIMS.md` is a ledger under
  both.
- **The attribution rule is now gated as it is worded.** The gate reads every commit message since the last one that
  carried a vendor's name or a co-author trailer.
- **Not done here:** the foundation's own entries (the claim, the closed loop, the tick, the ground). They are the
  next landing, at the foundation's version 1.65.

## 2. What was amended, place by place

The advisor seat's audit named twelve places that cap the goal (its finding X1). Each keeps its original text.

| place | what it said | what the dated note says |
|---|---|---|
| `GOVERNANCE.md` § 1 | "The goal is **not** a theory of everything." | outdated; the only goal is a parameter-free theory of everything; the second sentence, on work an expert can audit, stands |
| `GOVERNANCE.md` § 2, the label | the strongest label "derives the form"; the value question "closed disjoint" | "derives" is brought down to the foundation's statuses: derives, given the premises `GENESIS.md` lists. "Closed disjoint" is a record of the routes tested, not a limit on the goal |
| `GOVERNANCE.md` § 2, the firewall | the object "never supplies" a value; prose that lets it produce one "has breached it" | prose may say that deriving the values is the goal; prose that says a value has been derived, before it passes the acceptance criteria, has breached it |
| the framing gate | banned the phrase "toward the full SM" | that phrase states an aim and leaves the list; statements of arrival are gated instead (§ 3) |
| `CLAIMS.md`, O1 to O7 | "research targets … NOT partial results" | they are what the goal consists of; their status is unchanged: open, none a partial result |
| `docs/THE_CLAIM.md` § 2, the anchor doctrine | one dimensionless frame anchor is licensed | under the goal it is a debt to be removed, not a standing licence; the unit stays; the three theorems cited there stand |

**The audit's list also names two results of the foundation, FK11 and GAP6.** They are results, and a ruling does not
amend a result. They say where a value cannot come from. The amended § 2 says so: the goal is pursued through what
the negatives leave open.

**One governing document (the audit's finding X2).**

| file | what it said of itself | now |
|---|---|---|
| `GOVERNANCE.md` | "Every other file in this repo is subordinate to the rules here" | the one governing document: the goal and the rules |
| `GENESIS.md` | "Where any document disagrees with this file, this file holds" | holds on the status of every item of the foundation, by `GOVERNANCE.md`'s delegation. Its own line is noted at its next version |
| `CLAIMS.md` | "the living source of truth for what the project claims" | a ledger under both; last brought up to date on 2026-07-04, and it says so |

**Which file governs was main's choice.** The ruling asks for one and does not name it. `GOVERNANCE.md` calls itself
the constitution and `CLAIMS.md` already says it is governed by it, so this is the reading that changes least.

## 3. The two gates

**`arrival-phrases` (new).**
- It reads the living pages, the root pages and `docs/`, for a sentence of arrival: "the Standard Model is derived",
  "derives the Standard Model", "is a theory of everything", "all nineteen are derived", "the values are derived" and
  their kin.
- A denial, a condition or a statement of aim within the 64 characters before the phrase is not arrival. "No value of
  the Standard Model is derived" is the record's own sentence and passes.
- Three old lines are frozen, and the count may only shrink: a plan of 2026-07-24, a dated state page, and the
  owner's question of 2026-08-09, quoted.

> **NOTE 2026-11-12 (Review 79's second round; found by a reading on another family of model).** The rules of this
> section are the gates as this arc landed them. The same day, B1880 planted cases against them and four of the
> rules did not hold: a denial was taken from inside another word, an excuse was taken from another sentence, folders
> below `docs/` and `papers/` were not read, and the three frozen lines were held by count. B1880 replaced all four.
> This page did not say so, and its verdict file names no later arc. What the gates do today is B1880's page and the
> gates' own file.
>
> **CORRECTED 2026-11-12 (Review 80; found by a reading on another family of model and reproduced by main).** Five, not
> four. This section also says that the commit messages are read on the first-parent line. A commit that arrives by a
> merge is not on that line and was not read; B1880 replaced that rule as well, and the gate reads every commit
> reachable from the head. The verdict line carries a note of this from today.

| planted | result |
|---|---|
| the audit's own case: "the Standard Model is derived" added to the front page | refused |
| "The object derives the Standard Model."; "All nineteen are derived."; "Our programme is a theory of everything." | each refused |
| "The programme's only goal is a parameter-free theory of everything." | passes |
| "No value of the Standard Model is derived."; "Whether the Standard Model is derived … is the open question." | each passes |
| on main, a baseline one lower than the three frozen lines | refused |

**`attribution` (changed).**
- Before, it read tracked files and the author of the last commit. A co-author trailer or a vendor's name in a commit
  message passed. The rule is about commits.
- It now reads every commit message on the first-parent line after `da25c4f49` (2026-09-16), the most recent commit
  that carried one. 693 commits at or before it do. The 695 after it all pass, and so the practice had held for
  eight weeks before it was gated.
- It fails closed where that history is not in the clone.

| planted, each committed in a small repository | result |
|---|---|
| a co-author trailer | refused |
| a vendor's name in the message | refused |
| a commit by another author | refused |
| a first commit that is not in the clone; a history that does not descend from it | refused: cannot verify |
| no repository at all | nothing read; the gate says "skipped", as before |

**Found while writing the planted tests.** The first form of the arrival check missed a denial that opens a line: its
window did not treat a line break as a space. The test "No value of the Standard Model is derived." caught it.

## 4. What this does for the programme

- **The audit's findings X1, X2 and G9** are met as main reads their acceptance rows. The advisor seat's verdict is
  that seat's and is recorded apart when it comes.
- **The package for the goal's statement (WP-0.10)** has its first half: the goal is stated once, in one governing
  document. The other half is the foundation's entry for the claim, in the next landing.
- **Nothing here brings a value nearer.** It removes a contradiction between what the programme is doing and what
  its constitution said it was for.

## Seen first

- **The repo sweep:** the old goal sentence stood in `GOVERNANCE.md` and in four records that quote it. The phrases
  of arrival were swept over the whole tracked tree before the list was fixed: the three frozen lines are all there
  is on the living pages. The commit history was read in full: 2 965 commits on the first-parent line.
- **The literature:** none needed.

## Disclosed

- **The amendments are main's wording of the owner's ruling.** The ruling is the owner's sentence, "our only goal is
  that - full ToE", with the advisor seat's proposal for carrying it out, which the owner confirmed to main as
  written. Every amended passage can be corrected by the owner.
- **The arrival check is a list of phrases with a window.** A sentence of arrival in other words passes it. It is a
  tripwire for the plain cases, the audit's own among them, and it is not a reading of the page.
- **The three frozen lines are not adjudicated.** Two are dated pages that say "derives" of structure, which the
  amended § 2 now brings down to the foundation's statuses; they are history and are left as they were written.

## Reproduce

```
python3 scripts/gates/gates.py arrival-phrases attribution
python3 -m pytest -q tests/test_arrival_phrases.py tests/test_attribution_history.py frontier/B1878_the_goal_as_ruled_in_the_governing_documents/verification/
```
