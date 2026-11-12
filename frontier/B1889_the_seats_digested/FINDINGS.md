# B1889 — The seats, digested: what each has sent, what became of it, and what each has shown it can do

*Main, 2026-11-11 (S306p). The owner asked for this before anything else: "did you process and harvest all branches?
should you make that priority, so you underatabd what seats you have in disposal and whats their capacity." And then:
"aftwr you process harvest verify and digest then all, we should stop and reorganize the work, so we lock the plan
together me and you". This arc is the digest, and § 7 is the proposal main brings to that lock. It is not in force.
Nothing in the mathematics is computed here; no file of data is opened; the agy lane is read only through the mask
and none of its code is run. 0 of 19.*

## 1. The answer first

> **CORRECTED 2026-11-12 (Review 79; found by a reading of this arc on another family of model, and reproduced by
> main).** The builder dropped thirteen rows of the ledger without a word. They have six cells where the others have
> eight (rows 633 to 638, the physical lane's, and 879 to 885, the web seat's), and the builder asked for eight. So
> this page counted 1,686 items of 1,699. It also did not read the cell in which main writes the register row that
> carries an item, so 18 flagged items were called uncarried that are carried. The builder is mended, the pages are
> rebuilt as of the same commit, and the numbers below are the corrected ones. What they were:
>
> | | was | is |
> |---|---|---|
> | items sent | 1,686 | 1,699 |
> | recomputed by main | 377 (349 held, 28 differed) | 382 (354 held, 28 differed) |
> | read and not recomputed | 455 | 456 |
> | not read | 55 | 61 (the six more are the physical lane's, rows 633 to 638) |
> | the web seat | 233 items, 69 recomputed (58 held) | 240 items, 74 recomputed (63 held) |
> | the physical lane | 308 items | 314 items, 6 of them not read |
> | flagged items that name a register row | 35 of 74 | 53 of 74 |
>
> Two more things were wrong. Of the 74 flagged items two are of the class "not read", where § 5 says they are all
> registered or read. And §§ 3 and 4 left out three entries that `SEATS.md` has: the physical lane's fork lane, quiet
> since 2026-10-13 with 53 items; the listening thread, ended 2026-10-06 with 2; and the weave archive, one import.
> The lock compared the builder with its own output and could not see any of this; it now counts the ledger's rows.

- **The seats have sent 1,699 items in two months. Main has recomputed 382 of them itself, 22%.** Of those,
  354 held and 28 differed. In at least three of the 28 the fault was main's (rows 86, 93, 836).
- **560 items are registered and were never fully read by main.** 239 of them are the physical lane's
  and 160 are the SM seat's. This is the largest body of work the record holds and has not used.
- **61 items are not read.** 46 are from seats that have ended, all of September. The other 15 are the physical
  lane's (6), the web seat's, the SM seat's and the advisor seat's, and are listed on the page.
- **Four seats are working today:** the web seat, the advisor seat, the agy lane and the physical lane. Three more
  worked in the past eight days: the explore seat, the SM seat and the independent audit lane.
- **No seat is to be trusted on its own word, and none is useless.** Each has a record that says what it is good for.
  § 2 gives one card for each.
- **Main is the narrow place.** For 26 of the plan's 43 packages main is the only builder named, and 4 have no owner.
  18 of the 26 packages of mathematics are not started. The seats have capacity the plan does not use.
- **The owner's question of the same afternoon,** whether a parallel seat can verify while main banks: yes. § 7 says
  which seat verifies which, and why it cannot be one seat.

The tables are on `SEATS.md`, generated from the harvest ledger as it stood at one commit.

## 2. The seats that are working, one card each

Each card says what the record shows. "Recomputed" means main ran its own code on the item.

### The web seat (chat1)

| | |
|---|---|
| sent | 240 items since 2026-09-08 |
| recomputed by main | 74: 63 held, 11 differed |
| not recomputed | 136 read, 19 registered, 5 not read |
| how main reads it | directly |
| doing now | asked for a sealed card on the lowest and simplest read-out (P-783), and for a cold read of the three-part public structure |

- **What it has shown.** Sealed, preregistered checks that use no data, whose reruns on main are identical: rows
  1344, 1354, 1364, 1472 to 1482, 1545, 1584 to 1610, 1652 to 1691. It finds real faults in main: its corrections
  were applied to B1786 (row 1428), and it found main's error in B1852 (row 1618).
- **Where it has been wrong.** Its early packages overreached: one argument was refuted and inputs were misgraded
  (rows 14, 527 to 529). Its design studies came back verified with corrections (rows 1502 to 1509). One stated error
  was six hundred times too small (row 1620).
- **What it does when it is wrong.** Several of its own hypotheses failed their sealed tests, and it reported each as
  a failure (rows 1249, 1296, 1424, 1585).
- **Its five unread items** wait under a pledge of main's own (rows 1331, 1332, 1338, 1340, 1342; P-316, P-345).

### The advisor seat (cld-advisor)

| | |
|---|---|
| sent | 46 items since 2026-11-10 |
| its audit of main | 73 findings. On main today: 40 reproduced, 19 partly fixed, 11 fixed, 3 seen by a reader only |
| how main reads it | directly |
| doing now | builds five clean-up packages. The first of four patch series for enforcement arrived today (row 1699). Its sixth re-audit arrived while this page was written, after the commit the counts are of: one of main's two mends accepted, the other accepted in part (row 1700) |

- **What it has shown.** As an auditor, findings that reproduce: every residual of its re-audits was reproduced on
  main and mended (rows 1671, 1672, 1687). Its sealed runs were re-derived on main with main's own code (rows 1638,
  1658, 1668). It reports against itself: its note on the patch series says its first build passed its own tests
  and failed four of main's.
- **Where it has been wrong.** Nine details of its audit were corrected (row 1629). A script it named fails on main
  (row 1665). The form it gave its first back-edge closes nothing (row 1670). Its claim that a check is independent
  because another seat wrote it does not hold (row 1697). Sentences it relayed as the owner's rulings were not
  rulings for main (rows 1648, 1656).
- **A limit it states itself.** Its readers are instances of one family of model (row 1655).
- **Its leading words understate it.** Most of its rows begin READ and go on to say what main reproduced, so the
  share recomputed on `SEATS.md` is a floor for this seat.

### The agy lane

| | |
|---|---|
| sent | 32 items since 2026-10-27, on four branches |
| recomputed by main | parts of ten rows, on the mathematics that uses no value [CORRECTED 2026-11-12 (Review 79's second round): no file of this arc lists the ten. The number was main's count on reading the lane's 32 rows. By leading words the generated table gives the lane 4 rows that open with a recomputation] |
| how main reads it | through the mask only. Its code is never run by main |
| doing now | a loop in four phases on its fourth branch; four theorems that use no data, stated for main to check (row 1696; P-781) |

- **What it has shown.** Speed and width, on another family of model than main's. Where its mathematics uses no
  value and main checked it, a good part held and was banked with credit: rows 1558, 1563, 1581, 1582, 1604, 1621,
  and row 1643, where ten of its claims were verified and none found wrong.
- **Where it has been wrong.** Fourteen of its rows carry a refutation, a decline or a correction by main. [CORRECTED 2026-11-12 (Review 79's second round): no file of this arc lists the fourteen either. A search of the 32 dispositions for such words finds thirteen rows, some of which name the failure of something else; so neither number can be held to a file, and main gives none.] Early
  fits made after the fact were presented as selections (rows 1406, 1511). Later theorems were not proofs (rows
  1539, 1571), contradicted the record (row 1604), or were refuted (rows 1560, 1562, 1568).
- **The firewall.** It looked at held-out targets twice (rows 1539, 1547) and ran one unsealed evaluation, which it
  removed when told (row 1608). This is why main reads it through a mask.
- **What it adds that no other seat does.** Instruments. Two of the six guardrails of its prototype are worth
  testing as gates: no proof by a typed flag or zero, which is the fault main mended in B1028 this same day, and a
  referee that cannot import what it referees. The advisor seat planted ten cheats on that prototype and six were
  caught (row 1695).

### The physical lane (the audit seat)

| | |
|---|---|
| sent | 314 items since 2026-09-08, and 53 more on its fork lane |
| recomputed by main | 31, and all 31 held |
| not recomputed | 87 read, 187 registered, 6 not read; on the fork lane 52 of 53 registered |
| how main reads it | its purely mathematical files, through the second mask |
| doing now | its work order of 2026-11-10 for closing the record before calibration, which main took into its plan (P-748) |

- **What it has shown.** Nothing of its that main recomputed has differed. It found a defect in main's B915 (row
  55). Its audit of B1642's raw tensor was credited where three routes agreed (row 1111). It grades its own work
  with care: "unreviewed" and "unrun" are its own labels (rows 1522, 1628).
- **The size of what is unchecked.** Two thirds of what it sent is registered and was never fully read by main. Most
  of it is hand derivations: thresholds, kernels, index counts, controls written and not run.
- **Where its labels were too strong.** Six of its early rows were regraded from verified to reproduced (rows 56 to
  62). One review it called independent was by its own sub-agent (row 1533).

## 3. The seats that are quiet

| seat | last sent | what the record shows |
|---|---|---|
| the SM seat | 2026-11-06 | 463 items. Main recomputed 124: 119 held, 5 differed, and two of the 5 were corrections of main (rows 86, 836). Main once called a sentence of its refuted and withdrew that (rows 1091, 1151). Its recurring fault, in main's own notes: a headline wider than its proof (rows 649, 664, 667, 672, 678, 690). 160 items registered and 166 read without recomputation |
| the explore seat | 2026-11-07 | 5 items, all 5 verified on main's own code. Every run was preregistered; a crashed attempt was kept; a missed sweep was disclosed (rows 1612 to 1617) |
| the independent audit lane | 2026-11-04 | 2 items: its audit of the agy lane, verified in part, and its 22 outputs reproduced (rows 1512, 1550) |
| the referee lane | 2026-10-20 | 4 items from an outside referee's reports |
| the physical lane's fork lane | 2026-10-13 | 53 items, 52 of them registered and none recomputed (added 2026-11-12, Review 79: this row was left out) |

The owner's word of 2026-11-05 on the SM seat and the web seat stands until he changes it: they are asked "only when
their expertise is required".

## 4. The seats that have ended

Ten seats of August to October: the cloud seat, cc3 and its second branch, the physics seat, the codex seat, the
sep16 seat, the consolidation seat, the hostile-review seat, and two single handoffs. Their counts are on `SEATS.md`.
[Added 2026-11-12 (Review 79): two more entries of `SEATS.md` were left out here, the listening thread, ended 2026-10-06
with 2 items, and the weave archive, which is one import and not a seat.]
They will not work again. What matters is what of theirs was never read.

- **46 of their items are not read.** They are what is left of the September backlog after Review 76 closed the
  rest at a pointer.
- **Two of the 46 sit under open leads,** checked by main at the rows: the codex seat's R013 (row 214), on which
  P-613 rests, and the physics seat's R55 (row 187), the dictionary P-615 is about.
- **Four more carry a dated note that names a claim nobody verified** (rows 171, 374, 414, 448).
- **218 of their items were closed by triage.** The weakest ground used is that no later arc names the item. That
  is a test of citation and not of content.

## 5. What the record holds and has not used

- **560 registered items** and **456 read ones** were not recomputed.
- **The five readers flagged 74 of them** as possibly bearing on the goal: a choice removed, a route killed,
  an error in main's work, or an instrument. The list is the last table of `SEATS.md`.
- **53 of the 74 name a register row,** so they are carried. **21 name none.** Two of the 74 are items main has not
  read at all (rows 1331 and 1698), and not registered or read ones.
- **Main has not judged the 74.** A flag is a reader's pointer. Sorting them is register row P-791: each one is
  taken into the card of the package it bears on, or closed with its reason.

## 6. How this was made, and what it is not

| step | what was done |
|---|---|
| the counts | read by `build_seats.py` from the harvest ledger at one commit. Every row falls to exactly one seat |
| the classes | the leading words of each row's disposition. A row that begins READ may go on to name a recomputation |
| the themes | five readers on the cheaper tier, read-only, each given one group of seats' rows as main wrote them. Their reports are kept as received |
| the quotes | every quote a reader gave was checked by `quote_check.py` against the row it names: 430 of 436 are in that row word for word. The other 6 are generic phrases or a paraphrase and are not used |
| main's own reading | the 28 rows that differed; the 55 not read; every row named in § 2 to § 4; the advisor seat's relay and plan page; the agy lane's two notes, through the mask |

- **It is a digest of main's ledger, not of the seats' branches.** A reader saw what main wrote about an item, not
  the item.
- **It verifies nothing.** No registered item was recomputed for this arc.
- **A reader's theme is a reading.** Only its quotes are checked.
- **The agy lane's seven reports are not read.**

## 7. The proposal main brings to the lock

**Not in force.** The owner said "we lock the plan together me and you". This is main's draft for that.

### 7.1 The goal, in one line

Every parameter of the Standard Model derived from the one object with nothing put in by hand, or counted as an
input; every step computed, checked by a second route and reproducible by a stranger; and all of that before any
value is set beside a measurement.

### 7.2 The plan: the programme as it stands, in three stages

| stage | packages | it is done when | today |
|---|---|---|---|
| 1. a record that can be trusted | 12 | every planted violation is caught; every finding of the audit is fixed and re-audited; the full suite is green on a fresh clone; the count of inputs is computed from the graph and typed nowhere | 0 done, 10 started |
| 2. the mathematics complete | 26 | every statement on the map has a grade and a path; each of the 39 inputs is derived and leaves the count, or is declared and stays in it | 1 done, 7 started |
| 3. the reading | 5 | the certificate is generated; the upstream audit is done; the card is sealed; a seat that built none of it has challenged it. Then the comparison, which is the owner's | 1 started |

**One change in how.** Stages 1 and 2 run side by side, because different seats do them. The sealed card still
waits on every package of stage 1.

### 7.3 Who does what

| seat | role in the plan | why, by its record |
|---|---|---|
| main | orchestrates; recomputes what decides, and lands; keeps the map, the programme, the register and the foundation; mends the errors in the mathematics; builds only where no seat can | the owner's rule: main is the final verifier |
| the advisor seat | builds the record's tooling, five packages of stage 1; re-audits every package main closes | § 2 |
| the web seat | builds the packages of pure mathematics in stage 2; verifies the SM seat's results and the agy lane's theorems; reads every headline result cold | § 2 |
| the SM seat | verifies the physical lane's results; builds the parameter inventory, the framing of the tests, anomalies and unwanted sectors; supplies the null for every look | § 3 |
| the physical lane | builds the packages on the action and the dynamics that it already holds, each delivered with a computation that is committed | § 2 |
| the agy lane | second derivations of results that use no data, from the statement alone; instruments; routes. It never certifies | § 2 |
| the explore seat | short tests that use no data, on call; a second checker | § 3 |
| one new seat, of another family of model | the independent challenge at the end, and the few headline results | a seat of the builders' family shares their blind spots (B1888 § 3) |

**Verification in parallel, as the owner asked.** No seat verifies its own work, so it is a ring and not one seat:

| whose results | verified by | size |
|---|---|---|
| the physical lane's | the SM seat | 187 items registered, and 52 on the fork lane |
| the SM seat's | the web seat | 160 items registered, and the 21 arcs on main whose verdict files say they rest on the SM seat |
| the agy lane's four theorems | the web seat | one relay (row 1696) |
| the web seat's | the SM seat or the explore seat | 19 items registered |

**Amended on 2026-11-11 by three things the owner said to main after this page was landed** (register rows P-792, P-794). The two tables above are kept as they were written.

- **The advisor seat builds and is not asked to verify.** Its re-audit of main's corrections ends with its sixth, which it had already sent.
- **Four seats verify:** the SM seat, the web seat, agy-exp and a second seat of the agy family, agy-002. The agy lane itself goes on with frontier work, which is verified later (P-798).
- **No new seat is needed** for the final challenge. The two agy seats are of another family of model than the builders.

Main's proposal for who checks whom with those four, put to him and not yet answered:

| whose work | checked by |
|---|---|
| the physical lane's | the SM seat |
| the SM seat's | the web seat where it touches data; agy-exp where it is pure mathematics |
| the web seat's | the SM seat; agy-exp where it is pure mathematics |
| the agy lane's theorems | the web seat |
| main's own corrections and new arcs | the web seat; agy-002 derives the headline results again from their statements |
| what the advisor seat builds | main, with its unseen cases |

Two guardrails for the two agy seats: only work that uses no measured data, and main recomputes the deciding number before it banks.

**Corrected the same evening.** The two agy seats have said who they are: agy-002 is the session of the branch stage4-sync-2026-11-11, and agy-exp that of the branch self-consistent-loop-2026-11-11. Neither is the seat this page's § 3 calls the explore seat; main had supposed that agy-exp was.

**First what the plan rests on, not everything:** the 26 debts of the package "unverified premises and seat results
under banked results", and those 21 arcs. The rest is verified when a card needs it.

### 7.4 The rule: one card for each piece of work

**Before it starts, the seat commits one page:**

1. the package and the question, in a sentence;
2. what it will deliver, and what done means;
3. how it could come out wrong, written before any run;
4. what it rests on, and what it must not touch;
5. one control that must fail if the work is broken;
6. what it needs from main or from the owner.

**Main answers once:** approved, or amended with the reason. After that the seat works its own way. No step is
checked.

**On delivery:**

- outputs are committed before the page that reads them;
- where the result bears a headline, a second seat checks it by its own route;
- main recomputes what decides, and lands it or sends it back with the reason;
- the grade it enters at says how far it was checked.

**What stays fixed, for every seat:**

- the firewall: no held-out target is touched and nothing is compared with data outside a sealed card;
- no seat gives a verdict on its own build;
- nothing changes on main before main has recomputed it;
- the owner is asked no question of fact;
- what was not done is said.

**What a seat is free to do:** propose a card for anything, in the plan or not; decline one; run several; choose its
method. Its name stands on the result in the record.

The advisor seat already works this way, and its plan page is the model: its status first, its goal, its rules,
what it has open, and how main supervises it.

### 7.5 How the lock becomes work

1. The owner changes this or accepts it.
2. Main sends each seat one note: the plan, what the record says it is good for, the rule. Each answers with the
   cards it can stand behind.
3. Main approves the cards. The programme's page shows every card and its state.
4. Main reports at each landing, as now.

### 7.6 What only the owner can settle

1. **The standard.** Verify what the plan rests on first and the rest as cards need it, as § 7.3 has it; or
   everything before anything else.
2. **The team.** Whether the SM seat and the physical lane are brought in for the work named; and whether a new seat
   of another family is opened for the final challenge.
3. **The order.** Side by side from now; or the clean-up first.

## Seen first

Swept from main at 338b14fe3.

- `VERDICT topic-sweep /seat digest|seats digested|what each seat|capacity of the seats|roster|work card|preregistration by a seat|lane survey|unwatched seat/ (full text): 4 of 1635 arcs on main match (OPEN 1, PROVED 2, no verdict file 1); 7 register rows match (DONE 2, QUEUED 5)`

The arc with no verdict file is this one, then unfinished. On record and used: B1208 (the first cross-seat harvest), B1426 (the unwatched seat's
survey), B1832 (the agy lanes digested), B1850 (Review 76's check of the backlog's closures, whose
quote checker this arc's follows), B1861 (the programme), B1870 (the multi-agent run of 2026-11-10, whose pattern for
readers this arc keeps), B1883 (the status page), B1888 (the five conditions for a check that counts), and the
harvest ledger itself.

Literature: none. This is a measurement of the record and a proposal for how to work.

## Disclosed

- **Main's first cut put two rows under the wrong seat.** The independent audit lane's two rows (1512, 1550) were
  filed with the physical lane's, and that reader saw them as the lane's. The generator sorts them rightly; the
  reader's report is kept as received and its two rows are not used for the physical lane.
- **Main had told the owner "about 46 unread".** The count is 61 not read and 560 never fully read [55 as this page first
  counted it]. It
  was corrected to him the same hour.
- **The readers are of one family of model, and of main's.** Their quotes are checked; their grouping is not.
- **The classes are main's typing.** A disposition that begins with a word outside them is counted as "other" and
  listed: 6 rows.
- **The states of the seats are as fetched on 2026-11-11.** Which seats the owner still runs is his to say.
- **The proposal is main's.** Main is a party: it proposes that it keep the verifying and the landing.

## Reproduce

```
python3 -B frontier/B1889_the_seats_digested/verification/build_seats.py
python3 -B frontier/B1889_the_seats_digested/verification/quote_check.py
```

A few seconds each. The first recomputes both generated files from the commit they name and compares.
