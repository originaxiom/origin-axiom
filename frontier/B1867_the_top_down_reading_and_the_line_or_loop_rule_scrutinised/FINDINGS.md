# B1867 — The advisor seat's top-down reading and its line-or-loop rule, scrutinised

*Main, 2026-11-10 (S306o, the refetch the owner ordered: "refetch all seats"). The advisor seat's branch moved three
times while main worked (`a13af59ae`, `73ed0fe8c`, `6ab2bbdb2`). Its three notes were read in full: the principle read top-down, the claim stated as
a closed loop, and the design of the first back-edge; with its page to all seats, "line or loop". None of its code was
run. Every fact main can test was computed with main's own code. Data-free: integers, words, and SnapPy's census of
symmetries; no measured number. 0 of 19.*

## 1. The answer first

- **The facts the three notes stand on are right.** Every one that main could test reproduces on main's own code.
- **"The record holds a line, not a loop" is true of main's own map.** None of its 286 edges is a result that
  returns to fix an input. A planted edge of that kind is seen by the same test.
- **The forcing ledger is not a derivation yet, and says so itself.** Three of its rows marked "argued forced" need a
  clause that its formal statement does not contain. Main exhibits each of the three in integers (§ 3).
- **The seat's two symmetry facts are instances of one law.** Main states the law and tests it on all 105 classes of
  words up to length 10. Half of it is on the record already (B134).
- **What the programme gains.** Each of its 38 inputs now carries the route these notes name for it, if they name
  one. An exit is on the table for 12 of the 38. None of the 12 is proved or built. [Corrected 2026-11-10 (B1873, the advisor seat's read): 8, not 12 — three of the forcing arguments are one clause short by B1867's own finding and one was withdrawn by its author; of the 8, five are back-edges that are named and not built.]
- **The owner confirmed the first eleven relayed rulings to main while this arc was being written** ("yes, but i
  also wanr your opinion on all"; P-758). The seat relayed two more after main had asked; those two are asked. This
  arc acts on none of the thirteen. Carrying out the eleven is registered (P-767), and the page the seat asks main to
  write waits on the thirteenth (P-765).

## 2. The symmetries of a bundle, read off its word

A history is a cyclic word in L and R. Three operations act on cyclic words: start elsewhere (rotation), read
backwards (reversal), exchange the two letters (the swap). The stabiliser of a word is the set of combinations of the
three that leave it unchanged.

| | the law | tested |
|---|---|---|
| 1 | the bundle's isometries number twice the stabiliser (the factor two is the fibre's central involution) | 105 of 105 classes |
| 2 | an isometry reverses orientation exactly when its element contains the swap; so the bundle is its own mirror image exactly when the stabiliser contains a swap | 105 of 105 |
| 3 | the bundle of the swapped word is the mirror image of the bundle of the word; the bundle of the reversed word is the same bundle with the same orientation | 28 words that are not their own mirror image: every isometry found has the sign the law gives |
| 4 | an isometry reverses the direction of the base exactly when its element contains the reversal | 105 of 105, by the action on the fibre's boundary |

The control that can fail: with the swap left out of the stabiliser, the count is wrong on 22 words, and they are
exactly the 22 that are their own mirror image.

**The seat's ten rows are instances.** Main's numbers equal the seat's in all ten.

| history | stabiliser | isometries | what is kept |
|---|---|---|---|
| the golden ground with k periods (k = 1, 2, 3, 4) | 4k | 8k | all three: k rotations, k rotations with the swap, 2k reversals with or without it |
| the run of 6 (L⁶RLR), and with two golden periods | 2 | 4 | one reversal; no rotation, no swap |
| (2,2,2) and (2,1,2,1,2) | 2 | 4 | one reversal |
| (2,3) | 1 | 2 | nothing |
| the row the seat calls (2,1,1,1,2) | 4 | 8 | it is the word LLRLR written twice: one rotation and two reversals |

**What follows.**

- **The run of 6 has a hand and a place and no arrow.** It keeps no swap, so it differs from its mirror image. It
  keeps no rotation. It keeps one reversal, an isometry that turns the base around. The seat reads this from its
  rows; the law gives it for every word. The record holds the same reversal as B1852's σ, and "the arrow absent" in
  B1750.
- **The seat's row (2,1,1,1,2) is not one departure.** Closed by one golden period the word is LLRLR twice over. Its
  eight isometries come from that repetition.
- **The mirror is the swap, for every word.** A rule that treats the two letters alike therefore selects a word and
  its mirror together. This is why the seat finds that "handedness arrives in pairs", and it is not special to the
  first departure. A net hand needs a rule that tells the letters apart: the order bit, which the grammar leaves open
  (GM5c).

**Grade.** Tested, not proved on main. A proof or a verified citation is owed before anything rests on it (P-766).
The statement is about every word: weave.

## 3. The forcing ledger: its facts hold, and three rows are one clause short

The ledger asks of each foundation item whether the principle forces it. Its own label: "Every row is an argument to
be proved or refuted. None is a result." Main checked the facts the arguments cite.

| row | the fact cited | main's check |
|---|---|---|
| positivity | every hyperbolic class is plus or minus a positive word | all 168 hyperbolic matrices with entries from −5 to 5: a positive word with both letters is found, with the conjugating matrix, for every one. 84 of them are minus a positive word |
| positivity | L⁵R⁻¹ has trace −3 and is the class of −LR | exact; the conjugating matrix is exhibited |
| the selection criterion | the torsion's order is the number of fibre characters the act leaves fixed | exact on 777 words: that number is the trace less two. SnapPy's homology has that torsion on 135 of 135 words |
| the selection criterion | — | LR is the only word with one fixed character. With the other sign the number is the trace plus two, never one: the same count decides the sign that positivity leaves open |
| no period | the trefoil's act has trace 1 and order 6 | exact. It also fixes one character only, so the selection criterion alone admits it and "no period" removes it |
| the orientation | the golden ground is its own mirror image | law 2: its stabiliser contains swaps |

So the selection criterion carries the whole choice of the object. Given positivity, "one fixed character" is
"trace 3", and that is LR. Whether the principle forces that criterion is the question that matters most in the
ledger.

**Three rows need a clause that the formal statement does not contain.** The formal statement reads: what exists
relative to a ground is an act the ground reads as nothing and which is not nothing; an act is cancelled when it is
the identity or becomes it when repeated.

1. **No period.** The statement removes acts of finite order. It does not remove a fixed direction. A single shear L
   never becomes the identity, and at every level N its N-th power is read as nothing and is not nothing. It meets
   the statement's own form of existing. The row's sentence "a fixed direction is a side that never changes" is an
   added clause.
2. **The carrier.** The row argues that if the difference between "a then b" and "b then a" is not cancelled, the
   group is free. Not commuting does not give free: in the integer Heisenberg group two generators do not commute and
   their commutator commutes with both. The row needs "nothing at all is cancelled", which is a stronger clause. The
   step from a free group to the puncture is the SM seat's B1380, not verified on main.
3. **The selection criterion.** The row excludes an act that fixes a character, because "a fixed character is a place
   where nothing happened". At the selection layer the same relation is what makes a departure exist: the run of 6
   equals the golden word at level 5, the level cannot tell them apart, and that is why it is selected. The run of 6
   itself fixes 20 characters, and every word other than LR fixes at least 2. As an exclusion the row removes every
   departure. As a minimum, "the least remainder", it is the reading `GENESIS.md` § 4 already holds and grades an
   interpretation.

The third is the place where the seat itself expects the principle to be short: "who the ground is and at which
level it looks". Main's check shows the shortage is already inside the ledger: one relation is read with opposite
verdicts at two layers.

**What main did not do.** Main proved and refuted no row. No grade in `GENESIS.md` changes on an argument. The
seat's ambiguity attack is pre-registered and had not run at the revision read. Main has read the formal statement,
so main cannot serve as one of that attack's blind readers.

## 4. Line or loop

**The statement tested on main's map.** The closure map (B1858) has 268 nodes and 286 edges of 11 kinds. The
programme's budget names 51 of the nodes as inputs. Sixty-one edges end on an input: 39 "requires", 13
"applies-under", 4 "bears-on", 2 "reads", 2 "same-as", 1 "answers". Each says something depends on the input. Eight
edges on the whole map are of a kind that says the source settles the target. None goes from a result back to an
input. The one that ends on an input joins one choice to itself under two names. **Back-edges: none.** With one
planted, the count is one.

**What the map cannot show** is a relation the record holds in prose only. The seat names one: "the departure fixes
the frame's line", banked as a premise. Main checked what stands behind it, in integers:

- LR − 1 has determinant of absolute value 1: the golden ground fixes no non-trivial character of the fibre.
- LR + 1 has determinant of absolute value 5: exactly four points of order 5 are sent to their inverse, ±(1,2) and
  ±(2,4).
- On that line the sign alternates with the number of golden periods that close a history. For the run of 6 it is
  +, −, + at one, two and three periods. The seat's table for four histories reproduces, including the one entry
  where the history is −1 on all of level 5.
- A flat line on the fibre extends over a history exactly when the history fixes its character. So "the departure
  fixes the line" is the condition that the line extends. It is a consistency condition between a history and a
  line, as the seat says. It cuts the lines to those the history fixes. It does not by itself pick one.

**Main's one qualification, which the seat reached too.** The seat's page first said only a loop can fix its own
beginning. Its addition at `6ab2bbdb2` says that this is an argument and not a theorem, and that a forward
characterisation can also single out one object. Main agrees and names the routes. An input can leave in three ways,
and the loop is the third:

1. a theorem that kills its alternatives, for a choice from a list;
2. rigidity, for a continuous number: once the history is fixed its metric is unique, so every number read from the
   metric is fixed with it (the seat's own note says so of the first link);
3. a condition computed downstream that the choice must satisfy, for what neither of the first two removes.

After the second, what stays free on a history's chain is discrete: which history, and which read-out. That is where
a theorem or a back-edge has to act.

**A loop fixes an orbit, not a point.** The seat's addition says so, and law 3 of § 2 is the first case: the swapped
word is the mirror image for every word, so no rule that respects the swap can prefer one of a mirror pair. This is
the record's B990 in the loop's terms.

## 5. What changes on main

- **The programme (B1861).** Its budget has a new table: for each of the 38 inputs, the route the three notes name.
  The builder refuses an input without a line (a fifteenth rule, with planted controls).

  | route | inputs |
  |---|---|
  | kept: the principle itself | 3 |
  | a forcing argument is written, not proved | 6 |
  | admitted, no route | 2 |
  | pressed: the notes argue against it standing as it is | 4 |
  | rigid once the history is fixed | 1 |
  | a back-edge is named, none built | 5 |
  | the dictionary: not paid by the loop | 6 |
  | untouched by the three notes | 11 |

  The table is a harvest of three notes, with main's checks beside it. It is not a sweep of the record: "untouched"
  says only that these notes name no route.
- **The register.** P-764 (the forcing ledger: prove or strike each row), P-765 (line or loop: the owner's
  confirmation and the three asks of main), P-766 (the symmetry law: proof owed). P-755 records the owner's
  agreement to rule on the law's reading after the computation registered for it. P-758 now counts thirteen relayed
  rulings: eleven confirmed by the owner to main, with main's opinion on each, and two asked. P-767 registers the
  carrying-out of the eleven. P-761 records that the closed-loop note and the design were read in full and checked.
- **No governing document changes.** `GENESIS.md`, `TERMINOLOGY.md` and the verdict fields are as they were.
- **The seat's first re-audit** (`REAUDIT_1_2026-11-10.md` @ `6ab2bbdb2`) ran its planted violations on main at
  `034b6438d`: 6 of 21 caught, the same fifteen left that main lists. It confirms main's count in B1865, including
  that the seventh reported catch was an artefact of the seat's own test. It accepts no row in full yet: that needs
  each mechanism read. The fifteen are the programme's enforcement package, as before.

## Seen first

- **The repo sweep:** topic sweeps for symmetry groups and amphichirality (247 arcs match the wide expression; the
  nearest are B134, B613, B848, B1852, B1750) and for palindromes (9 arcs; P-740). On the record: the amphichirality
  criterion for metallic blocks (B134, from Goodman, Heard and Hodgson); the reversal σ of the run of 6 (B1852);
  "the arrow absent" (B1750); the uniqueness of LR by trace 3 and torsion-free homology (B197, B781). A sweep for the
  count of isometries found nothing: 7 arcs match the expression and none states it.
- **The literature:** that the isometries of a hyperbolic once-punctured torus bundle preserve its fibration is
  standard (the canonical triangulation of these bundles); it is context here, not evidence, and is not verified on
  main. That every automorphism of the free group on two letters comes from the punctured torus is Nielsen's theorem,
  likewise cited as context.

## Disclosed

- **The table of routes is main's reading of three notes.** Its kinds are main's words. A row marked "forcing
  argued" or "back-edge named" is not a result.
- **SnapPy is the judge of laws 1 to 4.** It reports the full symmetry group for all 105 classes. Its computation
  is combinatorial on a triangulation it finds numerically.
- **The seat's symmetry script was not run.** Its ten rows were compared with main's after main's run.
- **The seat's sealed run on the principle as a selection rule is still not verified on main** (P-762). § 3's third
  point uses only the congruence at level 5, which is exact.
- **Eleven of the thirteen relayed rulings were confirmed by the owner to main while this arc was being written; two
  are asked.** Nothing in this arc acts on any of them. The census of § 4 and the table of routes are checks and a
  harvest; neither is a rule.

## Reproduce

```
python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/word_symmetries.py 10
python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/ledger_facts.py
python3 -B frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/line_or_loop.py
python3 -m pytest -q frontier/B1867_the_top_down_reading_and_the_line_or_loop_rule_scrutinised/verification/
```
