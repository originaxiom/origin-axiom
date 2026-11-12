# B1888 — The repository's public form, scrutinised by main at the owner's word

*Main, 2026-11-11 (S306p). The advisor seat proposed that what is handed to the world be three parts: this
repository as the archive, a small statement, and a separate check. Main agreed the same day (register row P-787).
The owner then asked, through that seat, for main's review, enrichment and scrutiny: "did u inform main about the
re-repo and ask for review, for its opinion, enrichment and scrutiny". The seat named eight places where its proposal
is weakest and asked main to attack them. This arc does that, with one new measurement. No file of data is opened;
nothing is compared with a measurement; the repository's structure does not change. 0 of 19.*

## 1. The answer first

- **The proposal survives the attack on its central step, and the number under it changes.** By the arcs' own lists
  the candidate has 736 arcs upstream. By its code it uses at most 14 arcs: 17 Python files, 3,032 lines.
- **The derivation half's chain, as read from the code, does not reach the measured values.** [CORRECTED 2026-11-12
  (Review 79): this read "The derivation half never touches the measured values." What was measured is the chain of
  files that the code names; a file opened by a name built at run time is not seen (Disclosed), so "never" said more
  than the measurement.] It is 13 files, 2,252 lines, in 11 arcs. The measured
  values enter at one module of the comparison half.
- **So a rebuild in a few thousand lines is realistic.** The present chain is already that size.
- **The weakest point is the independence of the check,** not the size of the rebuild. Naming a seat that "wrote
  none of it" does not make it independent. § 3, point 4, says what would.
- **"Not now" stands.** A statement built today would hold no earned value: three conditional results, one candidate
  that passed a sealed screen, twelve negatives and a list of 39 inputs.
- **Main would change four things, add seven, thinks three are wrong, and cannot judge four.** § 5.

## 2. Measured: what the candidate really uses

Read from the code of the candidate, B1841, and followed file by file. It is an upper bound on what the code names: a
file that is named and never opened is counted. It is not an upper bound on what the code opens: a file whose name is
built at run time is missed, so the true chain can also be longer. [CORRECTED 2026-11-12 (Review 79): this read "It is
an upper bound", with no such limit; the script's header said the chain "can be longer than the true one and not
shorter", which the Disclosed section of this page contradicts.]

| | by the arcs' own lists | by the code |
|---|---|---|
| arcs upstream of the candidate | 736 | 13 others, 14 with the candidate |
| Python files | not stated | 17 |
| lines of Python | not stated | 3,032 |
| other files named (census outputs, tables) | not stated | 32, 54 MB |
| the candidate's ten direct dependencies | 10 | 6 reached by code; 4 not |

**The four direct dependencies the code does not reach:** B1656, B1728, B1742, B1840.
- B1656's coupling enters as a copied helper file: two copies of `b1656_funcs.py` sit in the chain, in B1691 and
  B1723. It is used, by copy and not by reference.
- B1840's four entries are computed again inside the candidate's own script from their definition.
- B1728 and B1742 are cited and not run.

**The two halves:**

| started from | Python files | lines | arcs | reaches the measured values |
|---|---|---|---|---|
| the census (what the frame gives) | 13 | 2,252 | 11 | **no** |
| the look (what is set beside the measurement) | 17 | 3,032 | 14 | yes |

**How the measured values enter:** the candidate's look loads B1839's look, which loads B1741's comparison module,
which opens the one file of measured masses. One Python file of the chain names that file. In the whole tree 51 do, this arc's own script among them. [CORRECTED
2026-11-12 (Review 79): the count in this sentence read 50. The arc's committed output says 51, and so does a count at
the commit the review read. A second reading found it.]

**What it costs to run.** The candidate's census took 26,060 seconds, a little over seven hours.

## 3. The eight weak points, attacked

| # | the proposal says | what main found | verdict |
|---|---|---|---|
| 1 | the statement is rebuilt from the foundation and the inputs, not copied | the chain is about 3,000 lines, so the size is no obstacle. What the code does not carry is why each ingredient is what it is: the candidate has 13 borrowed joints (10 chosen, 2 fitted, 1 ansatz), and four of its ten dependencies enter by copy, by recomputation or by citation | **holds, with a first deliverable:** the rebuild lists everything it needed that the foundation does not state. Each such thing is an input and is counted |
| 2 | the candidate's real chain is short | 14 arcs at most, all inside the lists' 736 | **holds** |
| 3 | not now | a statement today: 0 of 19 earned; three headline results that are conditional; one that is a reading, a sealed screen at 0.87%; two that are a lane's and not verified on main. The mathematics by itself already has its vehicle, the paper the owner froze | **holds for the claim.** Sending the mathematics is the owner's decision and needs no new repository |
| 4 | the check is written by a seat that wrote none of the statement | several seats share a family and every seat has read the record. Independence by name is thin | **does not hold as stated.** What would count is below |
| 5 | the measured values are kept in the check only | already true of the candidate's derivation half; in the archive 51 scripts name the file [was: 50; corrected 2026-11-12, Review 79, from the arc's own output] | **holds, and is cheaper than feared.** Enforce it with two tests: no file of the statement names the measured file, and the derivation runs with that file absent |
| 6 | the archive is frozen at the seal | the lanes go on working after a seal | **change:** the archive is a signed tag on this repository and a dated deposit of it, not a second repository. Work goes on after the tag; the statement pins the tag's commit |
| 7 | one graph computes the headline | WP-0.12 builds a typed graph for the record | **one graph.** The statement's is the part of it upstream of the claimed values, generated and compared with its builder |
| 8 | a certificate anyone can write again | WP-5.1 builds a generator | **one generator,** run on the statement's own files. Every file it hashes is in the repository it is in |

**Point 4: what would make the check count.**

1. It is written from the statement's text alone: the definitions and the list of inputs. Never from the archive's
   code.
2. Its expectations are sealed before it sees any number of the statement's, with a hash published first. Main did
   this today for its 53 unseen cases.
3. Its log shows which files it opened, and none is in the archive.
4. At least one read is by a different family of model, or by a person.
5. Where it needs something the statement does not say, that is recorded as an input the statement left out. That
   list is the check's most useful output.

A seat cannot be made independent by saying it is. The five conditions can be checked.

## 4. What main adds

**A. What a statement built today would hold.**

| | count | what |
|---|---|---|
| values earned | 0 of 19 | |
| headline results | 6 | three conditional (the root, given four inputs; the global form, at one normalisation; the chiral three, given two inputs); one reading (the six pass a sealed screen); two a lane's, not verified on main |
| the candidate | 1 | six rows claimed, 13 borrowed joints |
| statements on the map | 276 | 13 derived, 18 conditional, 12 negative; 12 postulated, 42 chosen, 38 open |
| inputs put in by hand | 39 | |

That is an honest page, and it is not a theory of everything. It is why "not now" is right.

**B. The spine: what a stranger should read first.** The foundation document; the closure map; the programme; the
scoreboard; and these arcs: B251 (only the first metallic word gives a knot), B734 (the knot group's level,
corrected today), B1656 and B1667 (the coupling and its canonical end), B1726 and B1753 (the six, with two
ingredients put in by hand), B1839 (the end card, a negative), B1841 (the candidate), B1882 (what the window's ends
do to its rarity), B1872, B1875 and B1879 (the weave's theorems), B1881 (what symmetry allows a state of the whole).

**C. The count of looks.** It lives in `docs/LOOK_LEDGER.md`: 111 table lines, with 53 looks counted at the last full
re-grading. Its scope is one frame against one set of data, across every seat. It is completed at each review. Two
gaps before it can be handed over: looks on other frames are entered only where a seat reported them, and the agy
lane's are rows whose values main has not read. A completeness pass belongs at the seal.

**D. What a random theory of the same freedom scores.** The package the advisor seat describes lists this. The
record has it for two older nulls (B1882). For the candidate's own null it is owed (P-786).

**E. What must be mended in the archive before it is frozen.** The clean-up packages of the work order, all of
them; the full suite green on a fresh clone; the front door (the goal said two ways, the claims page dated July, two
lists of inputs); two tests that rewrite tracked files; 23 tests that cannot fail. Nothing else. The clean-up is the
critical path, not the split.

**F. The other trees.** `papers/`, `outside_bench/`, `packaging/`, `story/`, `philosophy/`, `speculations/`: all stay
in the archive, labelled as not part of the claim. None enters the statement. The frozen paper is its own object.

**G. The sentence on how the work was done,** in place of rewriting the history:

> *This work was carried out by one person directing several AI assistants. Every computation was run by an
> assistant. Where the record says a result was checked, it was checked by a second assistant, and where it says
> so, with separate code. No part has been verified by anyone outside the project. The full working record,
> with every error and every retraction, is public and unaltered.*

**H. The cost at the seal, in main's working days.** A rough estimate, not a measurement.

| part | days | why |
|---|---|---|
| the statement | 2 to 3 | the chain exists; the work is the claim, the inputs and the projected graph |
| the check | 3 to 5, by another seat | it includes one seven-hour census |
| the archive's tag and deposit | under 1 | |
| the clean-up before the tag | weeks at the present pace | this is what decides the date |

**I. One command, in two sizes.** A check that recomputes everything takes seven hours. So the check needs a short
form, about ten minutes: a sample of apexes recomputed, and the hashes of the shipped census outputs. And the full
form, for whoever wants it.

## 5. The four lists

**Would change.**
1. The archive is a tag and a deposit, not a second repository (point 6).
2. The measure of the candidate is its chain of code, 14 arcs, and not the 736 of the lists (§ 2).
3. Independence of the check is defined by the five conditions, not by who the seat is (point 4).
4. The check comes in two sizes (I).

**Would add.**
1. The rebuild's first deliverable: what it needed that the foundation does not state (point 1).
2. Two tests on the statement: no file names the measured file; the derivation runs with it absent (point 5).
3. What a statement would hold today, as a generated page (A).
4. The spine (B).
5. The completeness pass on the looks, and the candidate's own null (C, D).
6. The sentence on how the work was done (G).
7. A budget of running time, printed with the check (H, I).

**Thinks wrong.**
1. "736 arcs upstream" as the size of what must be rebuilt. It is true of the lists and misleading for the plan.
2. A check that runs in under a minute, as the agy lane proposes. The candidate's census alone is seven hours.
3. That a seat is independent because it wrote none of the arcs.

**Cannot judge.**
1. Whether any of the mathematics is ready for a journal. That needs a reader from outside.
2. Which licence serves the owner's aim in law.
3. Whether a different family of model, or a person, is available for the check.
4. The agy lane's seven reports. Main has read that lane's proposal through the advisor seat's read of it only.

## 6. Asked of the web seat

A cold read of the three-part structure with this page's changes, by the one seat that has written neither the
proposal nor the rival nor an agreement. Main's relay of this date asks for it.

## Seen first

Swept from main at ea41e6fc9, after the measurement and before this page was finished.

- `VERDICT topic-sweep /public form|distilled|verification package|referee package|rebuilt, not copied|handed to the world/ (full text): 10 of 1634 arcs on main match (OPEN 1, PROVED 8, no verdict file 1); 3 register rows match (DONE 2, OWNER 1)`

On record and used: B1841 and B1839 (the candidate and its instruments), B1741 (the comparison module), B1637 (the
file of measured masses, by name only), B1834 (the scoreboard), B1858 and B1861 (the map and the programme), B1882
(the window's ends), and the advisor seat's two pages of this date.

Literature: none. This is a measurement of the record and a judgement on a plan.

## Disclosed

- **Main's first version of the chain script stopped at the candidate's own two files.** It resolved a file name in
  the file's own folder and went no further, and the candidate loads a file of the same name from another arc. The
  script's header named that failure in advance, the run showed it, and it is mended.
- **The chain is static.** A file loaded by a name built at run time would be missed. The measured file is reached,
  which is the control that the instrument sees how data enters.
- **The days in § 4 H are estimates.** Nothing was built to measure them.
- **Main is a party.** It agreed with the proposal before being asked to break it.
- **The agy lane's reports were not read.**

## Reproduce

```
python3 -B frontier/B1888_the_public_form_scrutinised/verification/candidate_chain.py
```

A few seconds. It writes `candidate_chain.json` and `candidate_chain_run.txt` beside itself.
