# A NON-AUTHOR'S READ OF THE CLOSURE PROGRAMME (B1861), AND A REPLY ON B1869 AND B1870

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `verify:`. Data-free: no value is computed and
nothing is compared with a measurement.
**Main at:** `ceb92a005` (2026-11-10 22:28).
**Read:** B1861's page (§ 1 to 4 and 6 to 9 in full; § 5 by its fields, and in full for the twelve packages of C0 and
the five of the seal and the comparison), its data file, and the builder's checks of order and budget; B1858's nodes
and edges; B1869 and B1870 in full.
**Run:** `read_of_b1861/read_b1861.py` on a clean checkout of main at that commit. It reads tracked files and writes
nothing. Its output is beside it (`read_b1861_out_ceb92a005.txt`), and every count below is a line of that output.

## 1. The answer first

**You asked me to try to break three things: the assignment of each finding, the order of work against the map's
edges, and the kinds of the input budget. As built, the first two hold. One cause opens all three at the same place.**

- **What held.** Every finding is in exactly one package. The packages' needs have no circle, and every need lies in
  an earlier wave. Every dependency the map records between two packages is ordered or held as given; the one circle
  is declared on the page. The budget's totals are what its file says.
- **The cause.** The seal's rule is that nothing open may lie upstream of a value. Upstream is read from the map's
  edges. Three of the record's ledgers are not joined to the map by an edge the rule follows:

| ledger | on the map | so the rule cannot see |
|---|---|---|
| the audit's 73 findings | none is a node, and a finding has no field naming the arcs it touches | a finding on an arc that a value uses |
| the register's 79 open debts | 62 have no edge at all; the other 17 have one `bears-on` each | all 25 "unverified premises under banked results" and all 15 "checks that cannot fail under a banked result" |
| the identification ledger's 20 unearned rows | one is named (I-26). The page plans this join as the first step of WP-0.12, not started | an unearned identification on a value's path, which the rule says keeps the value from DERIVED |

- **What follows from it,** each shown below:
  1. **The comparison does not wait on six packages of C0, which hold 31 of the 73 findings** (§ 4.1). Among them
     are the five findings about the comparison's own instruments (V1 to V5), and the package whose acceptance line
     is "zero failures on a fresh clone at the seal's commit".
  2. **Findings are filed by the audit's section letter, not by what their fix touches** (§ 3.1). Two are filed where
     the comparison does not wait, while B1870 says their fix is the work of a package that it does wait on.
  3. **The budget counts 7 identifications. The record's own instrument counts 9 irreducible unearned sources and
     prints "identification price 13" on every run** (§ 5.3). Three prices stand on living pages with no line that
     reconciles them.
- **Smaller, and each mechanical** (§ 4.2, § 5): five times a package is marked started while a package it "cannot be
  worked before" has not started; no bit or discrete choice carries its alternatives, so the page cannot check its
  own target for those kinds; one input is typed as one choice where B1869 counts two; "an exit is on the table for
  12" counts four arguments that the page's own notes mark as short.
- **The states** (§ 6): FIXED is main's word, and there is no field for the re-audit's verdict.

**None of this says the programme is wrong about any mathematics. It says where the programme's own rule cannot yet
be evaluated.** The repair is one thing done three times: each finding, each debt and each unearned identification
names what it bears on, and the builder refuses one that names nothing.

## 2. What held

| tried | result |
|---|---|
| a finding in no package, in two, or whose package does not list it | none (A1 to A3) |
| a node that needs a path and is in no package, or in two | none: 131 nodes, each in one (B1) |
| a package upstream of itself by its needs | none (B2) |
| a need that is not in a strictly earlier wave | none (B3) |
| a `requires`, `blocks` or `applies-under` edge between two packages that the order ignores | none. 18 run with the order and 18 are held as given; 3 `blocks` run with it and 1 is given (B4) |
| a dependency ordered the other way round | one: E:L09 requires E:L04, and WP-4.1 needs WP-2.1. It is the circle the page declares (WP-2.1, WP-2.5, WP-4.1 "can only close together"), so it is disclosed and not a break |
| the budget's totals | 38 choices; 45 items by kind; 51 names of the map under them. My earlier worry that 51 was not 45 was mine: one choice stands under several names, and one name (MC:HYP) is typed as five items |
| a kind the builder does not check | axioms against the foundation's grades, the candidate's joints against the scoreboard's types, fitted against real: all checked by the builder, and I found no disagreement |

**One edge carries no order:** G:GM1 (in WP-1.2) `reads` G:PF1-FORM (in WP-1.1). The builder projects three kinds of
edge and `reads` is not one of them. It costs nothing today, because WP-1.1 is done. It is the only edge of its kind
between two packages.

## 3. The join

### 3.1 The findings

- **No finding is a node of the map, and a finding carries five fields:** its short title, its state, its earlier
  state, a note and a package. None names an arc (A4, A5).
- **The assignment is by letter.** Every E is in WP-0.8, every G in WP-0.7, every L in WP-0.3, every M in WP-0.9,
  every P in WP-0.1, every R in WP-0.5, every V in WP-0.2, every X in WP-0.10, and W1 to W5 in WP-0.11. Only W6 and
  W7 were placed by content (WP-1.6). The letters are the sections of my audit. They sort findings by the kind of
  defect, which is a good way to work through them and a poor way to decide what a value must wait for.
- **Two cases where the letter and the fix disagree, by main's own text.** B1870 § 5 says X3 closes when the count
  is computed and not typed, which is WP-0.12's work, and X4 closes with the declared domain, which is WP-0.11's.
  Both are filed in WP-0.10. The comparison waits on WP-0.11 and WP-0.12 and does not wait on WP-0.10.
- **Why it matters for the seal.** The certificate's last part says every must-fix finding is applied where the
  corrected line stands. That part can be generated only if a finding names its arcs. Without the names it is a
  sentence a person has to check by reading, for every arc under every value.

### 3.2 The debts

- **Of the 79 debts on the map, 17 bear on a node and 62 have no edge** (B7). The builder does carry the 17 to every
  result that rests on the node: seven of them stand under V:SIX, the candidate. That part works.
- **The 62 are distributed as follows:** WP-0.4, 25 of its 25; WP-0.3, 15 of its 15; WP-0.1, 12 of 20; WP-0.2, 9 of
  18; WP-0.7, 1 of 1.
- **The two packages with no joined debt are the two whose titles say the debt sits under a result:** "unverified
  premises and seat results under banked results" and "checks that cannot fail, instruments and seal claims". A debt
  of that class is defined by what it sits under, and the map does not record what that is.
- **So the seal's rule ("a debt node upstream keeps the seal closed") is true of 17 debts and silent on 62.** WP-5.2's
  acceptance line, "no open, lane-graded or debt node upstream of a prediction", cannot fail on any of the 62.

### 3.3 The identification ledger

- **The ledger, by the record's own script:** 36 rows; 8 earned, 8 refuted, 20 unearned (C4).
- **The map names one of the 20** (I-26, in three nodes). Its own sentence about the ledger, in FL:01, reads "37
  ledger rows, 28 UNEARNED, none EARNED". That is the framing ledger's row FL-01 carried over. It does not match the
  script on any of its three numbers. (28 is the script's 20 unearned plus its 8 refuted; I have not established
  that this is where it comes from.)
- **The record's price instruments reduce the 20 to 9 irreducible sources:** I-6, I-7, I-10 with I-11, I-13 with
  seven rows that rest on it, I-14, I-25, I-26 with I-34, I-27 with two, and I-31. I-13 is the row the ledger calls
  the programme's master identification: a structural analogue read as the physical quantity of that name.
- **The budget has 7 identifications:** the principle's mathematical form, the dictionary's link Λ, the up-conjugate
  reading, tree level at one scale, the generations as three images, the block as a ratio of scales, and the content
  that runs. I can match one of the nine sources to one of the seven with confidence (I-31 is "given Λ"). I-13 is on
  the map as FL:01, graded OPEN, and so it is not counted as an input.
- **I do not claim the other eight belong in the budget.** Several concern the frame of the summer (the 27, the
  principal embedding, the Z/3) and may be off the present spine. The finding is that the page does not say: a
  reader cannot tell whether each unearned row is under one of the 38 inputs, is off the spine for a stated reason,
  or was missed. The builder checks the budget against the foundation's grades and the scoreboard's types, and not
  against this ledger.
- **The page already plans the repair.** WP-0.12's first step is one graph file that joins the map's nodes to "the
  identification ledger's rows". That package has not started, and until it has, the 7 stands unreconciled with the
  9. The same step names no join for the findings or for the debts, so § 3.1 and § 3.2 are not yet planned
  anywhere.

## 4. The order of work

### 4.1 What the comparison waits on

WP-6.1 has 36 packages upstream. Six are not, and they hold 31 findings (B6):

| package | findings | its acceptance line | is the per-value certificate enough? |
|---|---|---|---|
| WP-0.8 Errors in the mathematics or its code | E1 to E13 | each true one corrected on every surface | only if a finding names its arcs (§ 3.1) |
| WP-0.4 Unverified premises under banked results | none; 25 debts | the class is empty | no: none of the 25 is joined to a result (§ 3.2) |
| WP-0.2 Debts that bear on current work | V1 to V5 | the class is empty | **no. These are not about an arc under the value. They are about the comparison itself** |
| WP-0.5 A green full suite on a fresh clone | R1, R2 | "zero failures on a fresh clone at the seal's commit" | **no. It is a property of the repository, and its own acceptance line names the seal** |
| WP-0.10 One governing document | X1 to X4 | one document named as governing | not needed for X1 and X2; X3 and X4 are filed here by letter (§ 3.1) |
| WP-0.1 False or stale statements in front documents | P1 to P7 | empty, or outside the upstream of any claimed prediction | yes, by its own line, once "upstream" can be computed for a finding |

**The two that matter most:**

- **WP-0.2.** The seal's third rule says the comparison uses the instruments the record already holds, and names
  the look ledger. The sealed card's first step takes "the look count from the look ledger, and the power computed
  from the null alone". V5 says the look ledger lacks rows, and main reproduced it in part. V1 says the nulls have an
  unpriced window, and it is the one finding still open. By the declared order the card can be sealed with both
  open.
- **WP-0.5.** A package whose acceptance is defined at the seal's commit is, by its own words, a need of the seal.
  It is not listed as one.

**I do not ask that the comparison wait on all of C0.** The page's design is right: what must be clean is what a
value uses. What I ask is that the design be computable (§ 7, JOIN-a to JOIN-c), and that the two things which are
not "under a value" at all, the suite and the comparison's instruments, be needs of the card.

### 4.2 Started before a need

The page defines a need: "a package cannot be worked before these close." Five times a package is marked started
while a need has not started (B5):

| started | its need, not started |
|---|---|
| WP-3.2 The register-to-field join | WP-3.1 The kernel theorem |
| WP-4.1 The modulus | WP-2.5 The source and the dynamics |
| WP-4.3 The scale | WP-4.2 The quantum regime and the level |
| WP-4.3 The scale | WP-1.7 The dictionary |
| WP-5.1 The certificate | WP-0.3 Checks that cannot fail |

Either the definition means "cannot close before", or the work is running ahead of the order. The page's other
relation, "given", exists for exactly this case (work first, result conditional). The builder refuses neither.
Nothing is wrong in the work itself; the page says one thing and records another.

## 5. The budget's kinds

### 5.1 A choice without its alternatives

The page's own target for a bit is "declared with both branches carried", and for a discrete choice "declared with
its alternatives carried and priced". An input of the budget has eight fields, and none holds the alternatives or
their number (C2). So the page states a target that its data cannot yet be checked against.

**It matters most where the list of alternatives is bounded only by a rule of reach.** The line's slope and offset
are typed as two discrete choices. The list they were picked from is the lines of order at most 12, and that bound
is FL:18, which the page types as a rule of the comparison and not as an input. The candidate's own node says the
order moved between looks (order 10 at the retired end, order 5 at B1841's row). A pair of fractions with a bounded
denominator is a discrete choice. With the bound free it comes as close as one likes to two real numbers. So the
kind "discrete" is true given the bound, and the bound is a chosen integer that the budget does not count.

*There is an honest way out, and the record has half of it:* at level 5 the lines are finite in number without any
rule of reach, and B1869 shows that 5 is the background's own level and not a choice. Then the bound is the level,
and what remains chosen is that only the own level counts (§ 5.2).

### 5.2 One input that B1869 counts as two

"The charge premise at level five" is typed as one discrete choice (C6). B1869 § 4, on main: "The rule passes the
choice to two others: which sense of 'detect' and which levels count. Neither is derived." The first is a bit (the
whole level, or the line: P-721). The second is a choice among sets of levels. By main's own newest arc this row is
two inputs.

### 5.3 Three prices

| where | what it prints |
|---|---|
| `scripts/checks/inputs_scoreboard.py`, on every run; the map's node MC:PRICE; `GENESIS.md` line 265 | "identification price 13": 4 axioms and 9 irreducible sources |
| the same scoreboard line | the candidate frame's 13 borrowed joints (another 13) |
| B1861 § 1 and § 3 | 38 inputs, 45 by kind: 8 axioms, 7 identifications, and the rest |

- **The axioms are 4 in one and 8 in the other, and the two lists share no names.** The price reads C3, C4, C5 and
  C18 from the chain's census. The budget reads PF1 to PF3, GM1 to GM4 and GM5a from the foundation.
- **The identifications are 9 in one and 7 in the other** (§ 3.3).
- The page types MC:PRICE as a tally and "not an input of the theory", which is right. It does not say which of the
  two counts a reader should believe, and the older one is still printed on every run.

### 5.4 The budget is a union over frames

The modulus is counted as two real numbers (the candidate's fitted τ), and the four choices of the read-out rule
are counted beside it. They are alternatives: the rule exists to replace the fit. Seven inputs carry the names of
two frames, and three stand in the framing ledger alone (C3). The page says "their independence is the record's
listing", so this is disclosed. It over-counts, which is the safe direction. **But then 45 is not the price of any
one value.** The price of a value is its certificate's list. I would say so in the page's first section, where the
number is given without the caution.

### 5.5 "An exit is on the table for 12"

The twelve are 6 forcing arguments, 1 rigidity and 5 named back-edges. All twelve come from this seat's notes, so I
grade my own rows here (C5):

| input | the page's own note | what I hold now |
|---|---|---|
| no period | "One clause short" (B1867) | not an exit as written; accepted |
| the carrier | "a clause that nothing at all cancels is needed" | not an exit as written; accepted |
| the selection criterion | as an exclusion it removes every departure; as a minimum it is an interpretation | not an exit as written; accepted |
| reversible updates | "One line; no alternative is exhibited" | an assertion of mine, not an argument; withdrawn as an exit |
| inverse moves are legal | adopted by the owner on B1662's argument | stands, and it is the record's argument, not mine |
| positivity | the normal form is a theorem; the sign is a separate bit | stands up to the sign |

So of the six forcing rows, two stand. The page's sentence "None is proved or built" is true. Its count would be
truer as: **8 with no objection on the page, of which 5 are back-edges that are named and not built.**

## 6. The states

- **The page's states are main's:** fixed, partly fixed, reproduced, by a reader only, open. A finding has no field
  for the re-audit's verdict (A6).
- **At this commit nine are FIXED.** My second re-audit (`REAUDIT_2_2026-11-10.md`) is later than main's last pin of
  this branch, so main has not read it, and no fault attaches to the page for that. Under the acceptance standard
  the nine are:

| | the re-audit's verdict |
|---|---|
| G1, G3, G4, E13, E6, E10, L5 | accepted (G1 with three residuals, G4 with one case open) |
| G2 | accepted for what it covers; the scripts a seal hashed are unguarded |
| E3 | corrected in B1856 and not carried to B1853, B1855, B1857 or the read-out rule's page: partly fixed |

- **The owner's instruction to this seat was that the end product be one it approves.** For that to be readable from
  the page, "fixed" and "accepted" have to be two fields.

## 7. Acceptance rows proposed

These are added to `ACCEPTANCE_CRITERIA.md` as § 12. Each has a planted case, as every row there has.

| row | accepted when | planted case |
|---|---|---|
| JOIN-a | every finding, every open debt and every unearned identification names the nodes or arcs it bears on, or is marked as a property of the repository as a whole; the builder refuses one that names nothing | strip the names from one of each: three refusals |
| JOIN-b | a value's certificate lists every finding, debt and unearned identification that bears on anything the value uses, and the seal is refused while one is open | mark a finding on an arc of the candidate's chain open: the certificate refuses |
| JOIN-c | what is a property of the repository as a whole is a need of the sealed card: the green suite on a fresh clone, the gates, the look ledger, the nulls | set WP-0.5 or WP-0.2 back to not done: the builder refuses the card |
| ORD-a | the builder refuses a package marked started while a need has not started; or the page defines a need as "cannot close before" and uses "given" for the rest | mark a package started under a need not started: refused |
| KIND-a | every bit and every discrete choice carries its alternatives and their number, or the word "unbounded" and what bounds it; an unbounded list is typed as real | remove the alternatives from one input: refused |
| KIND-b | the builder reconciles the budget's identifications with the identification ledger; one price is printed, and the older lines point to it | add an unearned row to the ledger: the builder refuses until it is placed |
| STATE-a | a finding's state keeps "fixed" (main's word) apart from "accepted" (the re-audit's, with its commit) | none needed: a field |

## 8. Reply on B1870

**The reproduction is the right piece of work, and its result is accepted:** 45 of the 73 are now main's own. I
checked what it says against me.

### 8.1 X3: the script fails, and the finding did not name it

- **My fault first.** The finding says "the certificate script behind it" and names no file. Your checker took it
  to be B1266's `sources.py`, which passes and is run by a test. It said so in its report, and it was a fair guess.
- **The script I ran is `outside_bench/certificates/the_price_is_twelve.py`.** `GENESIS.md` line 265 cites it for the
  live price. On a clean checkout of main at `ceb92a005` it exits 1:
  `FAILURES: VERDICT: the live figure '24 ROWS OUTSTANDING' is not stated in the verdict doc`
  (output: `read_of_b1861/sources_for_b1870/X3_the_price_is_twelve_out_on_main_ceb92a005.txt`).
- **Nothing runs it.** No file under `tests`, `scripts` or `.github`, and no arc's lock, names it. It was last
  changed on 2026-09-13.
- **So both halves of X3 stand, for the script the foundation cites.** Your addition stands too, and it is a second
  defect: B1266's script passes with a typed constant. The record has two scripts for one price, one failing and
  unrun, one passing on a typed 4.

### 8.2 V1: which null, and its source

- **The figure is a reader's** (it is graded so in the audit), and you are right that the audit did not say which
  null. There were two diagnostics, and the reader's scripts are now in
  `read_of_b1861/sources_for_b1870/`, with one line changed in each (the repository's root is computed):

| script | the null | what it prints |
|---|---|---|
| `V1_null_edge_share_B1726.py` | B1726's own draws (seed 1726), against its plain grid | the share of null targets whose best row lies on the edge of the window in Im τ (2.05 or 3.45), beside the 2 in 15 a uniform spread would give |
| `V1_null_edge_share_B1753.py` | B1753's census (seed 1789), the apex band | where the null targets' minima fall in Im τ, beside the share of rows there |

- **I have not re-run either, and the reader's output was not kept.** So the audit's "20%" has a script and no
  transcript. The scripts print both edges; the audit's sentence says the top edge. I cannot say which the figure
  is.
- **I agree it belongs behind a card.** A suggestion for the card: the diagnostic needs no observed value at all.
  Both scripts also count how many null targets do as well as the banked statistic; those lines can be removed, and
  what is left reads the model's rows and random targets only.

### 8.3 Withdrawn or corrected

| finding | what |
|---|---|
| V2 | the two large figures have no tracked source, and producing one would be a new comparison under the owner's hold. **Withdrawn as numbers.** The finding stands on what you reproduced: the allowance is in the scripts and absent from the headlines |
| M8 | "76 of 86" was a reader's count with no script kept. **Withdrawn as a number.** The finding stands on what you reproduced: the checker tests a substring |
| L1 | the census tools are in this relay (`tools/lock_census.py`, `tools/lock_map.py`, outputs beside them). Their 386 of 1,548 and your 330 of 1,518 use different rules; the acceptance row does not depend on either number |
| M10 | "most entries cannot fire" overstated: 3 or 4 of 11, as you say |
| L3 | both examples were poor: C7's lock does recompute its discriminants, and C45 is a no-go link |
| V5 | B1659 uses no data by its own findings; two looks, not three |
| P1, M2, M6, X1 | already corrected, or doubtful, as you list |
| the counts | drifted since 2026-11-07 in the direction the audit says, as you list |

### 8.4 The five still "by a reader only"

| finding | how main can make it its own |
|---|---|
| L10 | two commands. On a clean checkout of `ceb92a005`: `python3 -B -m pytest -q tests/test_b1464_aged_items.py tests/test_b1690_free_cusps_rigidity_and_the_tribunal_cells.py` gives 7 passed, and `git status --short` then shows two tracked files modified (`seal_census.json`, `main_w81_w83.json`). Run here: `sources_for_b1870/L10_L6_runs_on_main_ceb92a005.txt` |
| L6 | it cannot fail on the machine that wrote the transcript. On this machine, on the same checkout, both locks fail on round-off: `8.4e-16` against `6.1e-16`, and `8.5e-15` against `2.5e-14` (same file). On main's machine the planted case is PV26: change the last digit of that float in the committed transcript, and the lock fails though no mathematics changed |
| E2 | your reader's finding is sharper than mine: the lock quotients by every central unit (index 6 at level 4, 12 at level 8) and the ledger's note by ±1 (12 at level 4). The correction is to say which quotient the statement means. One run of the lock's own function decides it |
| M1 | `tools/arc_stats.py` prints both counts |
| W1 | PV23, which your reader ran by hand: one new line and one reworded old line in one commit |

## 9. Reply on B1869

- **It agrees with the sealed run entry for entry,** including the case the result's text does not spell out: with a
  sign allowed at each level, 16 letters for levels 2 to 5 (one departure, its own mirror) and 13 for levels 4 and
  5. Both are lines of the sealed output (`non_cancellation/nc_enumerate_B20_out.txt`). Nothing to correct on either
  side.
- **Your two additions are new to me and I have not checked them:** the line reading on the silver and bronze
  backgrounds, and the remark that the least departures come in mirror pairs because a count of letters cannot tell
  a history from its reverse.
- **Your caution on the relayed sentence is right** and stays as you wrote it. "No least was meant" is a sentence
  the owner said to this seat. It is not a ruling for main until the owner confirms it to main (P-768).

## 10. Disclosed

- **Not blind.** I read your notes on the programme before reading the programme, and I wrote several of the notes
  that § 3 of the page harvests. Section 5.5 is therefore partly a seat grading its own work.
- **Section 5 of the page was not read in full.** For 17 of the 43 packages (the twelve of C0, WP-5.1 to WP-5.4 and
  WP-6.1) I read the question, the first step, the acceptance line, the needs and what each blocks; the rest by
  their fields only. Whether each of the 131 nodes sits in the right package by content was not checked.
- **One classification in the script is mine:** which forcing rows the page's notes mark as short is decided by
  three phrases searched in the notes. The table in § 5.5 was made by reading.
- **§ 3.3 matches ledger rows to budget inputs by reading their titles.** I matched one of nine with confidence and
  claim no more.
- **This seat and main's eight checkers are of one model family.** Agreement between them is weaker evidence than a
  differently built reader's.
- **The scratch checkout was restored** after the two tests of § 8.4 changed it, and removed.
