# THE REPOSITORY, MEASURED AND READ — and what should be handed to the world

**From:** the advisor seat. **For:** the owner, who asked. **To:** cc (main), to read at its next batch. Nothing is asked.
**Kind:** `verify:` (the measurements, §§ 2 to 4) and `propose:` (the opinion, §§ 1 and 5 to 8). Nothing on main is changed.
**Main read at:** `64bf79ebc`.

The owner's words, whole: "btw deep analyze the repo once more and conplete honest opinion on the repo structure, size,
how it reads and its purpose, and werher its final verification or public version should be the same, serve or servd
just as a historical archive of a complete new repo distilled version of our gated framework and the final
verification package which which would be handed to the world."

## 1. The opinion, in six lines

1. **The repository is a laboratory notebook.** It is written by and for the working seats. It is honest to a rare
   degree and, at its size, no person will ever read it.
2. **Its size works against the claim.** "1,095 proved" in under six months makes a physicist more wary, not less.
3. **It fails the one test a verification package must pass: the candidate cannot be checked on its own.** By the
   arcs' own lists it rests on 736 other arcs, 27 of them open and 3 retracted.
4. **So the public version should not be the same repository.** This one becomes the archive, kept whole. The world
   gets a new, small repository.
5. **The new one should be rebuilt, not copied:** derived again from the foundation and the declared inputs by a
   seat that did not write the arcs. If that cannot be done in a few thousand lines, that is the finding.
6. **Not now.** There is nothing to hand over yet: 0 of 19, and no card is sealed. Decide the shape now and build it
   when the card is sealed.

## 2. Measured

| | |
|---|---|
| tracked files | 17,124 |
| size | 766 MB of files; 792 MB of history |
| age | 173 days (first commit 2026-05-22), 4,146 commits: 24 a day |
| arcs | 1,628: 9 a day, 506 in July alone |
| text | 4.7 million lines. 7.7 million words of prose. 701,000 lines of Python in 5,715 files |
| tests | 8,403 collected, in 1,542 files |
| where the bytes are | 94% under `frontier/`. 373 MB is 28 files of census output |
| the verdicts | 1,095 PROVED, 383 NEGATIVE, 96 OPEN, 12 RETRACTED |
| who wrote the arcs, by their own field | main 435; fan-out waves 721; no author named 192 |
| arcs that are instruments, not results | 191 |
| status pages | 134 pages at the root of `docs/`; about 45 are ledgers, registers, maps or plans, among them five masterplans and three roadmaps. 282 handoffs between seats |
| the root | 25 files: eleven governing pages (79,000 words), three memos between seats, five stray result files |
| other trees | `papers/` (283 files, 33 PDFs, eight paper candidates, a note on submitting to a preprint server); `outside_bench/` (815 files, another seat's mirror); `story/`, `philosophy/`, `speculations/`, `knowledge/`, `paths/`, `legacy/`; `packaging/` (placeholders to take the project's name on package registries) |

**Reading time.** 7.7 million words is about 510 hours at 250 words a minute: thirteen working weeks to read the
prose once. The findings alone, 1.3 million words, are 89 hours.

**The prose by kind, in words:** findings 1.33 million; other pages inside arcs 2.68 million; the pages at the root of
`docs/` 1.21 million; the two logs 0.72 million; the outside bench 0.46 million; the papers 0.44 million; the
handoffs 0.13 million; the governing pages 0.08 million.

## 3. Whether the candidate can be checked alone

Read from every arc's `depends_on` in its verdict file.

| | |
|---|---|
| arcs that depend on another arc | 644 |
| arcs that another arc depends on | 863 |
| arcs that stand alone both ways | 651 |
| the candidate (B1841): direct dependencies | 10 |
| everything upstream of it | **736 arcs:** 552 PROVED, 140 NEGATIVE, 27 OPEN, 3 RETRACTED, 14 with no verdict word |
| the candidate with its upstream | 737 arcs, 7,836 files, 640 MB of the 720 MB under `frontier/` |

The list mixes what an arc uses with what it cites, which is what WP-0.12 sets out to separate. As it stands, nobody
can take the candidate out and check it. A reader who tried found the same from the code: its scripts load two
scripts of B1839 by path, an instrument of B1842 and inputs of B1753, B1713 and B1840. Through them it reaches the
measured values, one file inside B1637 that 41 scripts across the tree open. That file sits in the same tree as the
code that makes the prediction.

## 4. How it reads

**Method.** Two readers with no context, a smaller model of this seat's family, each given a clean copy of main and a
list of questions. Neither was told this seat's opinion. One read as a physicist with an hour. One read as an
engineer asked to reproduce the results. The facts below that this seat repeats, it checked.

| | the physicist | the engineer |
|---|---|---|
| what worked | the README: 83 lines, a table of where to start, "0 of 19" stated the same everywhere he looked | the gates: 53 of 53 pass in 28.5 seconds on a clean copy, and write nothing. 8,403 tests collect with no error; a slice of 20 files passed in 35 seconds |
| what stopped him | the goal says two things in `GOVERNANCE.md` (not a theory of everything; only a theory of everything, amended a day ago). `CLAIMS.md` was last brought up to date on 2026-07-04. Two lists of inputs that differ: `docs/THE_CLAIM.md` (six axioms, one bit, five outside data) and the programme (39 choices). Six vocabularies of status. A glossary of 14,700 words | the environment is pinned in prose only; the requirement files give floors, and SnapPy is not in them. No lockfile, no container, no statement of running time. The README says the gates run on every push; the workflow is deliberately untracked, so a reader sees no public run |
| tracing one result | B997, the first positive he could find: no verification folder, no lock of its own, and the statement was later corrected by B1859. Five files and a correction | the candidate cannot be run alone (§ 3) |
| scores, 1 to 5 | purpose 3; finding what is claimed 3; checking one result 2; honesty 5; signal against noise 1 to 2 | a stranger can run the checks 3; reproducible from a clean environment 2; the verification separable from the record 2 |
| his answer | distil, and keep this as the archive | a standalone package, with the measured values kept apart from the derivation |

**What made the physicist distrust it,** in his words or close to them: a claim "line" thousands of words long;
"stated proudly" and "genuine" inside a claim document; a correction added in brackets beside the sentence it
corrects; "the owner's ruling" as an authority; verification by seats checking seats; 1,586 verdicts in six months.
This seat measured the first: the claim lines have a median of 551 characters, a tenth run past 2,674, and the
longest is 25,558.

## 5. What the repository is, and what it is good at

It does three jobs in one tree, and the first shapes it:

| the job | written for | what it needs |
|---|---|---|
| the working memory of the seats | a seat that must recover the whole context | everything, in order, never deleted |
| the evidence | whoever doubts a date, a look or a retraction | the history intact |
| the public face | a stranger | very little, said once |

**What is good, and should be kept as it is:** one arc for one question; a verdict on every arc, negatives included;
sealed comparisons with the looks counted; retractions listed; generated pages that a gate compares with their
builder; a front page that says 0 of 19 and that nothing is verified outside. Few records say so much against
themselves.

**What the size costs:**

- **The verdict word does not mean one thing.** PROVED covers a theorem, an exact computation, a numerical estimate
  and a process step. The audit's findings on labels say so, and WP-0.9 is the package for it.
- **The checks cannot keep up.** The gates check the bookkeeping, not the physics. A review reads five arcs of
  1,628 in full, and the last one found ten faults in five.
- **Nearly half the arcs came from fan-out waves.**
- **The apparatus of publication came before a result:** eight paper candidates, a submission note, placeholders
  for package names.

## 6. What should be handed to the world

**Two repositories.**

| | the archive (this one) | the package (new) |
|---|---|---|
| what it is | the notebook, whole | what a hostile referee needs for one afternoon |
| its history | untouched. Frozen by a tag when the card is sealed, and that commit deposited with an archive that dates it independently | starts at the seal |
| who reads it | nobody has to. Anybody may | everybody |
| size | as it is | under about 200 files |

**Why the archive is not pruned or rewritten.** A seal, a count of looks and a retraction mean something only if the
history under them is whole. A cleaned history would be the first thing a referee asked about.

**What the package holds:**

| | |
|---|---|
| the claim | one page: what is claimed, what is not, k of 19 |
| the inputs | every choice put in by hand, with its kind, in one list |
| the derivation | the shortest chain from the postulates to each predicted number: each step a proof or an exact computation, with its script |
| the sealed card | the predictions with their uncertainties, the hash, and the proof of its date |
| one command | a pinned environment; every number on the card computed again from the postulates, with no measured value on the disk while it runs |
| the comparison | the measured values with their source, kept apart; the one script that opens them; matches and misses |
| the looks | how many frames and variants were tried before the card, and what a random theory of the same freedom scores |
| the negatives | what was refuted, and the retractions |
| the method | who computed and who checked: the owner and assistant seats, nothing verified outside |
| the provenance | for every file and number, the commit, path and hash in the archive it answers to, and a script that checks it |
| a glossary | thirty terms |

**How it is made: rebuilt, not copied.** § 3 shows that copying drags 640 MB. A seat that did not write the arcs
derives the candidate again from `GENESIS.md` and the list of inputs alone, in the package. That is the independent
reproduction the work order already asks for (WP-5.4), and it is the strongest check the result can have. Where the
rebuild needs something the foundation does not state, that thing is an input and is counted.

**The package is generated where it can be,** with a gate that compares it with its builder, so that it cannot
drift from the archive. The audit's lesson is that a typed number drifts.

**On "our gated framework".** If it means the theory as it stands after the gates, that is what the package holds
and nothing else. If it means the machinery (the gates, the seals, the count of looks), it is the most reusable
thing here and may deserve a small repository of its own later. It is not ready to be shown as a method: it catches
8 of this seat's 21 planted violations.

## 7. When, and what is cheap now

**Not now.** Building the public shell before there is a result would be work that finishes nothing, which is what
this seat said of main's last eighteen hours. Two things do follow now:

- **The shape changes the order of work a little.** The certificate (WP-5.1), the typed graph (WP-0.12) and the
  independent challenge (WP-5.4) all feed the package. If the package is the aim, each is built so that it can be
  lifted out.
- **The archive is already public** (no licence, no stars, no forks). Three things cost little:

| | |
|---|---|
| a licence | there is none, so nobody may reuse or redistribute anything in it |
| the front door | the goal's two sentences, `CLAIMS.md` dated July, the two lists of inputs, "the gates run on every push". All are in WP-0.1 already |
| the history | 2,285 commit messages name an AI vendor or model, or carry a co-author line; 15 commits are authored under a vendor's name; 38 tracked files name one; three author addresses are not no-reply addresses. None of this can be removed without rewriting the history, which § 6 advises against. The owner should know it is there |

## 8. Disclosed

- **The full suite was not run,** by this seat or by either reader. Nor was any script of the candidate.
- **The two readers are of this seat's family,** and each made about fifteen tool calls. Their scores are two
  readings, not a survey.
- **The physics was not judged here.** Whether any of the mathematics is new, and whether the papers' claims hold,
  is outside what this seat measured.
- **The upstream count is only as good as `depends_on`,** which mixes uses and cites. The true chain is shorter.
  How much shorter is what a rebuild would show.
- **The search for credentials used four patterns** and found nothing. That is not a clearance.
- **This seat is a party.** It is a natural candidate to do the rebuild, and it is the seat that audits main.

## 9. Later the same day: "whats the best way to do it"

The owner asked this seat for its honest opinion on the best way to do it: how the light public repository is tied
to this one. Main had by then attacked §§ 6 and 7 at his word (B1888). This section is the seat's answer to him. It
keeps §§ 6 and 7 where main left them standing, takes main's changes, and adds two things.

**The rule that carries the rest: there are never two places of work.** This repository is the only place anything
is written. The public one is a release built from it and is not edited by hand. Then there is no second history to
reconcile, and nothing in the public one can drift.

| part of the public repository | how it is made |
|---|---|
| the statement | the short chain written again, clean. Main measured it at 14 arcs and about 3,000 lines. It lives in a folder of THIS repository, under the same gates and this seat's audit, and is exported from a tagged commit |
| the provenance | generated, not written: the tagged commit and its deposit; the map from each claim to the arcs behind it (the part of WP-0.12's graph upstream of the claimed values); the hash of every file (WP-5.1's certificate); and a run that shows the clean chain gives the same numbers as the chain it replaces |
| the check | the one part written outside: from the statement's text alone, its expectations sealed first, by main's five conditions (B1888 § 3). Under a permissive licence, so that nobody is blocked from running it |

**Three ties, each of which a stranger can check:** the pinned commit; the map; the matching numbers.

**What changes from § 6.** The archive is a signed tag and a dated deposit of this repository, not a second
repository (main's change, taken). The clean statement is kept here and exported, so the public repository is never
worked in (new). The check counts by main's five conditions and not by who wrote it (main's change, taken).

**What to do now, and nothing else for the public face:**

1. **Have someone else date the history.** A commit's date is typed by whoever makes the commit; this seat met that
   the same day, building the gate that takes its day from the commit (`wp_0_7/series_1/`, the fourth patch). So a
   sceptic can say the record was rewritten last week, and today the only outside witness is the host. A snapshot
   taken and dated by an outside archive, now and at each seal, makes the history the fact the owner wants it to be.
   It matters most for a sealed prediction: that it was sealed before the reading has to be someone else's record.
2. **The licence.** Main's answer to him fits his aim, and this seat adds nothing to it but the same limit: a licence
   covers the text and the code, not the theory.

**Two things said plainly.** A public page built today would read 0 of 19; building the shell now finishes nothing,
and the clean-up is what decides the date. And no arrangement of this project's own seats makes the check
independent: before any claim it needs one reader from outside, a person or another family of model.

**Not done by this seat:** no outside archive was contacted and no snapshot was requested. That sends the project's
name outside, and it is the owner's to do or to order.

