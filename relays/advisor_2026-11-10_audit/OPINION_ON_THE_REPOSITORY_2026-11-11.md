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

## 10. The seat's vision of the end product, given before the owner shares his

He asked three things: what the end product looks like after (if) the values are got, in structure and detail; how
it is connected to this repository; and what each is for in five to ten years. This is the seat's own view. It is a
design, not a measurement, and nothing in it is built.

### 10.1 What the end product is

Not a repository first. **A claim, with the proof that the test of it was fair.** Four objects carry it:

| object | what it is | who reads it |
|---|---|---|
| the paper | the claim and its derivation, in the form physics reads | physicists |
| the package | the light public repository: everything needed to check the paper in an afternoon | anyone who doubts it |
| the card | the predictions, sealed and dated by someone outside before any measured value was opened | everyone, first |
| the archive | this repository: how it was found, with every error | almost nobody; whoever asks whether the test was fair |

### 10.2 The package

```
README            one page: the claim in five sentences; k of n; check it in ten minutes; what would refute it
CLAIM             what is claimed and what is not; the postulates; every choice put in by hand, counted
statement/        the derivation, postulates to values: a chapter for each step, the mathematics beside its script
  values/         one page for each value: where it comes from, and the number with a proved error bound
card/             the sealed predictions: numbers, uncertainties, the hash, the outside date; later cards after it
compare/          the measured values with their sources, and the ONE script that opens them; matches and misses
check/            the recomputation written by others from the text alone: a short form and a full one; who ran it
looks/            what was tried before the card, how many times, and what a random theory of the same freedom scores
negatives/        what was refuted on the way, and the retractions
falsifiers        the measurements that could still refute it, each with the experiment and the year expected
provenance/       generated: the archive's pinned commit; the map from each claim to its arcs; hashes; the matching run
method            how the work was done and by whom; what nobody outside has yet verified
```

Under about two hundred files. A few thousand lines of code. Thirty to sixty pages of prose.

### 10.3 The details that decide whether it can be doubted

| detail | why |
|---|---|
| every number is an interval with a proved bound, never a printed float | two of main's own locks fail on this seat's machine today because a float prints differently |
| no measured value is on the disk while the derivation runs | a prediction that can see its target is not one |
| "k of n" is computed from each value's ancestry and typed nowhere | the audit's first lesson |
| the front page is the map: postulates to values, each node coloured by what it rests on | the scoreboard built for the owner becomes the public face, drawn from the same graph |
| releases are numbered; a changed derivation is a new release with a new card | nobody can say the claim moved |
| an open list of errata and of failed checks, each answered in public | the archive's honesty, kept up after the seal |
| reproductions by outsiders are listed with their own code | no arrangement of this project's seats is independent |
| later: the mathematical core in a proof assistant | tests show the code does what it did; a checked proof shows the mathematics follows |

### 10.4 How it is tied to this repository

| tie | what it is |
|---|---|
| the pin | each release names one signed tag of the archive and its outside deposit |
| the map | every step of the statement names the arcs where it was first found, with their dates and the errors on the way |
| the matching run | the clean statement gives the same numbers as the chain it replaces |
| the looks and the seals | extracted from the archive by a script; their worth is the whole history under them |
| the direction | the package cites the archive; the archive never depends on the package |
| the two front doors | the archive's first line sends a checker to the package; the package's last line sends a historian to the archive |

Work goes on in the archive after the seal. A later release pins a later tag.

### 10.5 In five to ten years

| if | the package | the archive |
|---|---|---|
| the values hold and outsiders reproduce them | the reference: what a paper cites for a number, and the bench others build on. Its card becomes a running record, sealed predictions against each new measurement | a primary source: the proof of priority, and a complete record of one person directing assistants to a result, which nobody else has. Frozen at its tags; cited for how, not for what |
| some hold and some do not | an honest scorecard, k of n, with the falsifiers deciding the rest | still the place of work |
| a sealed prediction fails | the record of a clean refutation: a parameter-free proposal that named its own test and met it. That outcome has to be as plain on the front page as success would be; it is what makes success believable | the account of it |

**In every case the package is the claim under test, and the archive is the evidence that the test was fair.**

### 10.6 A third thing

The machinery (seals, gates, the count of looks, planted violations, one channel to the owner) is the most reusable
thing here, whatever becomes of the physics. In ten years it may be the part most used by others. It is not ready to
be shown: it catches 11 of this seat's 21 planted cases with the first series applied, and that series is not landed.

### 10.7 Where this seat is unsure

- **Where the principle sits.** The seat would put the numbers and the card first, and the principle as the first
  postulate in its exact form, with the intuition in an essay the claim never depends on. The owner may want the
  vision first. Both can exist; they should not be mixed.
- **Who keeps the package in ten years.** One person and assistants can build it. A reference needs a keeper that
  outlasts both.
- **How much of the mathematics can be machine-checked.** The finite computations, yes. The analytic parts, this seat
  cannot judge.

## 11. The website, as the owner asked for it

He has the domain `originaxiom.org`. He asked how the seat would structure a public website whose content comes
from the public repository and is updated through it; what function it should have; whether it should be a
laboratory with personal accounts or read-only; and whether it should hold an interactive visualisation of the whole
of existence. It is to serve scientists and professionals, lay readers, and curious children. This is the seat's own
view: a design, and nothing of it is built.

### 11.1 Its function

**The reading room and the instrument panel of the claim.** It explains, it shows where the claim stands today, and it
lets a visitor test a step. **It is never a source.** Every sentence, number and mark on it is built from a file of
the public repository at a named release, and says which.

| it is for | it is not for |
|---|---|
| explaining the claim at four depths | stating anything the repository does not |
| showing the live state: k of n, each value against its measurement | holding anybody's personal data |
| letting a visitor run a step and see the number come out | running long computations for visitors |
| the public lists: what would refute it, errata, reproductions | discussion; that stays where the code is hosted |

### 11.2 One truth at four depths, not four sites

Every node of the map (a postulate, a step, a value) carries four texts, kept beside it in the repository:

| depth | for | what it is |
|---|---|---|
| 1 | a curious child | one sentence and a picture |
| 2 | a lay reader | a paragraph, no symbols |
| 3 | a scientist | the mathematics |
| 4 | a checker | the script, the data, the hash, "run it" |

A visitor turns a dial; the page stays the same page. People do not sort themselves into audiences, and one reader
moves between depths. **A gate holds the simple texts to the node's grade:** a sentence for a child may not say
"proved" where the node is conditional. That is WP-0.9's rule, carried to the public prose.

### 11.3 Its parts

| part | what it holds |
|---|---|
| the front page | the claim in one sentence; k of n, live; the map, small; three doors: understand it, explore it, check it |
| the idea | the story in about ten screens, at depths 1 and 2; what is claimed and what is not |
| the map | the interactive derivation, from the first postulate to each value (§ 11.5) |
| the numbers | the card: each value, predicted and measured, the date it was sealed; kept up as measurements arrive |
| check it | the ten-minute check; steps that run in the browser; the full check; who has reproduced it; how to report a failure |
| what would refute it | the measurements that could, with the experiment and the year |
| how it was made | the method, the count of looks, the retractions, the timeline; the door to the archive |
| for teachers and children | guided paths through the map, a glossary of thirty terms, pages to print |
| what changed | releases and errata, generated |

### 11.4 Laboratory or read-only: neither end

**Read-only content, with real instruments that run on the visitor's own machine, and no personal accounts.**

| | |
|---|---|
| independent exploration | yes. The map; switching a choice off and watching which values lose their footing; steps that run in the browser from the repository's own scripts; notes and bookmarks kept in the visitor's browser |
| personal accounts | no, at the start. Accounts are personal data, and with children among the visitors that is a legal duty of its own; they need security, moderation and a keeper; and a site with members reads as a product before the claim is verified |
| heavy computation | not on the site. The laboratory is the public repository: anybody clones it, or opens it in a hosted notebook under their own account elsewhere |
| contributions | where the code is hosted: a failed check is an issue, a reproduction is a change to the list of reproductions |
| later | if the values hold and there is a keeper, a hosted laboratory can be added. It is the one part that needs an organisation behind it |

### 11.5 The visualisation: yes, as the centre, and as a map of the derivation

**A map of what follows from what, and how sure each step is. Not a picture of existence.**

| rule | why |
|---|---|
| every mark is a node or an edge of the repository's graph | then it cannot say more than the claim does, and it cannot drift |
| colour is the grade: earned, conditional, chosen by hand, open, refuted | the reader sees the state, including what is missing |
| one map, zoomed: the first postulate at the centre, the values at the rim | intuitive, and the same object for a child and a physicist |
| a guided path for children: one route from the first distinction to one number | a story told on the true map |
| known physics shown for context is marked as measured, apart from what is derived | accuracy |
| nothing is drawn that no node backs: no cosmic animation | that would claim what is not earned |
| every chart has a table behind it | so that it can be read without seeing it |

It shows exactly as much of existence as the claim has earned the right to draw. If the count reaches n of n, the
map is the picture he asks for, and it got there by being true at every step before.

The owner's intuition of the principle belongs in the site as an essay, marked as the idea behind the work. The
claim does not depend on it, and the two are not mixed.

### 11.6 How it is fed

- **Built, not edited.** A script in the public repository builds the whole site from the repository's files at each
  release. No content system, no database, no server-side code.
- **Every page names the release it was built from** and links to the file it shows.
- **The same commit gives the same site,** and a gate checks that. The site is one more generated view.
- **No trackers and no cookies.** There are children among the visitors, and nothing needs them.
- **Translations are files in the repository,** keyed by node, under the same gate.

### 11.7 When, and where the seat is unsure

Design it with the package, because it is drawn from the same graph as the scoreboard and WP-0.12. Launch it with the
seal. Until then the scoreboard is its private preview.

- **Whether to open it before any value is earned.** An honest page reading 0 of 19 is true and is not yet a reason
  to visit.
- **How much runs in a browser.** The finite steps do. The seven-hour census does not, and the site should say so.
- **Who answers the public.** Errata and failed checks need a person, on a clock.

