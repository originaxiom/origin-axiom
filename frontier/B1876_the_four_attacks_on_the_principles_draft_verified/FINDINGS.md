# B1876 — The four remaining attacks on the principle's draft: the advisor seat's sealed run verified on main

*Main, 2026-11-11 (S306p). The advisor seat pushed the result of a sealed exercise (`459dd72fd`): four attacks on its
eight-clause draft of the founding principle, with sixteen hypotheses written and sealed before the run. The seat
asks main to re-derive what it would bank. The result, the sealed design and the seat's note were read in full. None
of the seat's code was run. Main computed every hypothesis with its own code: integers, and SnapPy for the manifolds.
Data-free: nothing is measured and nothing is compared with a measurement. 0 of 19.*

## 1. The answer first

- **All sixteen hypotheses come out on main as the seat reports them,** number for number, the Chern–Simons values
  and their signs included.
- **What they say, in four sentences.**
  1. Given two whole-number records and no subtraction, there is no choice in the acts. Everything that adds is built
     from four pieces: L, R, the tick F and its other side F′. Only the identity and the bare exchange undo
     themselves.
  2. If every history may serve as a ground, the record's rule has four root classes and is not an order. If the
     ground is the act itself, there is one: the tick, at level 5.
  3. At level 5 the tick changes nothing. The exchange is a scalar there, and every departure is allowed or not
     exactly as before.
  4. The run of 6, read alone, has a hand and a Chern–Simons invariant that is not zero. With its mirror image the
     hand cancels. A history with no hand has no such invariant at all.
- **The seat's reading of the whole is that the draft is a foundation and not a selector.** Main's own earlier
  result says the same from the other side: the selection rule picks the run of 6 only when level 5 is put in
  (B1869).
- **Two questions come out of it that the draft cannot answer.** They are the seat's questions to the owner. Main
  records them with its opinion (§ 6) and rules on neither.
- **Not verified by main:** the two readers' table of twenty-one negatives, which is judgement; and the existence of
  Pin structures, which the seat takes from theory.
- **Four additions by main** (§ 5): one count depends on whether powers are counted; one equality the seat found
  for histories with no hand holds for every history; of the seat's six "not found on the record" statements main's
  record holds part of one; and the rate at which a departure's invariants settle is identified, post hoc.

## 2. The sixteen hypotheses

| # | the seat's hypothesis, in one line | main |
|---|---|---|
| H1 | of the non-negative integer matrices of determinant ±1 with entries to 8, only 1 and P have finite order; of the rest exactly L, R, F, F′ are not a product of two others | **holds**: 174 matrices, 172 left, four atoms; every one of the 172 is a product of the four; with determinant +1 only, the atoms are L and R |
| H2 | words in L and F are all different acts, to 14 letters; words in L, R, F are not; R is not made by L and F | **holds**: 32 766 words, all different; the first coincidence is F·R = L·F; also F·F′ = L·L |
| H3 | in the grammar of L and F a history and its mirror are one cyclic word; the counts by length | **holds**: 1, 1, 2, 3, 6, 9, 18, 30, 56, 99 in all; 1, 1, 1, 2, 3, 5, 9, 16, 28, 51 with an odd number of F; to 8 letters the 32 even words are the 69 two-act histories less 5, in pairs |
| H4 | two histories of different trace never both fail to detect each other | **holds**: of 3 306 ordered pairs to trace 60, 208 go one way and none both |
| H5 | L·R is the only history alone at its trace; counted with its mirror once, the traces with one history | **holds**: 3 alone; and 3, 4, 5, 9, 21 (powers counted; see § 5) |
| H6 | the traces that are a departure of no other ground are exactly 3, 4, 5, 6 | **holds**, to trace 2 000: eight histories |
| H7 | the relation is not an order: there are chains a → b → c in which a detects c | **holds**: 209 to trace 60; the first is 3 → 7 → 11 |
| H8 | chains from the golden ground do not reach every trace | **holds**: 52 of 58; not 4, 5, 6, 9, 10, 14 |
| H9 | read by primes the relation is an order; one-prime discriminants only at traces 3 and 6 | **holds**: none further to trace 200 000; 17 minimal traces to 60 |
| H10 | L and R have a rational fixed direction, F and F′ do not, and F′ is F from the other side | **holds**: discriminants 0, 0, 5, 5; F′ = P F P |
| H11 | with the exchange the group of the acts modulo N doubles; up to scalars it does not at 5 and 13 | **holds**: 60 and 60 at level 5, 1 092 and 1 092 at 13; doubled at 3, 4, 7, 8, 9, 11 |
| H12 | at level 5 the centre is {±1, ±2}; every departure to 14 letters is allowed or not exactly as before | **holds** on all 4 096: the same matrix against the ground in both grammars; 35, 50 and 330 allowed under the three readings; the least are (6) alone, and (6) with (2,2,2) |
| H13 | the tick multiplies the mark by 3 and keeps no vector up to sign | **holds**: it keeps the four vectors of the golden line up to a scalar, and no other |
| H14 | the golden ground with 1, 2, 3 periods is its own mirror and has Chern–Simons invariant 0 | **holds** (to 10⁻¹⁰) |
| H15 | the run of 6 has a hand, its Chern–Simons invariant is not 0, and its mirror has the opposite value | **holds**: −0.07360, −0.07519, −0.07552 for 1, 2, 3 further periods |
| H16 | a history with an odd number of runs is not orientable and has no Chern–Simons invariant; a count of its fibre structures | **holds** on 16 of 16 to 6 letters; SnapPy refuses the invariant because the manifold is not oriented |

**Post hoc at the seat, recomputed.** With 0 to 8 further periods the run of 6 has −0.065897, −0.073598, −0.075187,
−0.075521, −0.075591, −0.075606, −0.075609, −0.075609, −0.075610. Each step is about 4.8 times smaller than the one
before. (2,2,2) settles at −0.021859, and (2,1,1,1,2) with one period has −0.04324.

**Why H11 is as it is.** Up to scalars the exchange adds nothing exactly where −1 is a square modulo N. Main checked
the equivalence at the eight levels, and that −1 is a square modulo s² + 4 for every odd s to 59.

## 3. What bears on main's open points

| main's point | what is now computed on main |
|---|---|
| P-771, whether the tick is an act | H1, H2, H10 to H13. The facts are in; the ruling is the owner's |
| P-769, the tick's second debt: the record's structures at odd levels | **closed at level 5.** The exchange is a scalar there, the group up to scalars is the same 60 elements, and all 4 096 departures are allowed or not as before. At 3, 4, 7, 8, 9, 11 the group doubles and nothing is shown |
| P-769, which of the eight walls stand under the tick | computed for the first three (H14, H15, H16): they hold for the root and for a history with its mirror, and not for the run of 6 read alone. The other five are argued by the seat and not computed |
| P-769, the tick's first debt: what stands in place of a spin structure | a Pin structure, by theory. The count of H16 is verified. For the root the record holds a lane's result, registered and not re-derived on main (sm:B1382, in B1453) |
| P-769, the third debt: the weave's theorems for the larger group | not touched |

## 4. What it means for the programme

- **The selection criterion in the budget.** If the ground is the act, level 5 is named without ranking and the
  choice of a ground could leave the budget. That needs two things neither of which is in hand: the owner's word that
  the tick is an act (P-771), and a clause saying what a ground is. Nothing in the budget is changed here.
- **The candidate.** The run of 6 was shown to be least when level 5 is put in (B1855, B1869). This run adds that,
  read alone, it has a hand. The eight walls the record traces to the mirror are walls of the root and of the whole
  ledger. They are not walls of one departure. The owner's ruling confirmed to main (R10) puts the claim on all
  allowed histories together, so a reading from one departure alone is a thread's reading either way.
- **The weight.** Unchanged. The exercise found no clause that fixes how the whole is counted (B1813; P-755 as
  ruled).
- **A new number on record, with nothing claimed for it.** A departure in a long golden ground carries a definite
  Chern–Simons invariant of its own, as it carries an excess volume: −0.075610 for the run of 6. It is registered as
  a lead (P-775).

## 5. Main's additions

- **H5's list depends on counting powers.** With powers of shorter histories counted as histories, the traces with
  one history up to mirror are 3, 4, 5, 9, 21, as the seat has. Counting primitive histories only, 7 joins them: at
  trace 7 the third history is L·R done twice.
- **H16's equality is one rule for every history.** The odd quadratic form is kept by every history, so the forms a
  history keeps are as many as the fixed classes of the fibre modulo 2, and H¹ of the bundle with ℤ/2 coefficients
  has twice that. Main checked it on the 77 two-act cyclic words to 8 letters as well. So the count says nothing
  special about a history with no hand.
- **The sweep the seat asked for.** It reports six statements as not found on the record.

| the statement | on main's record? |
|---|---|
| H1 the four atoms; no choice in the acts | no. B1323 has F = L·P, F² = L·R and P L P = R |
| H2 L with F as a grammar; F·R = L·F | no |
| H3 in that grammar a history has no hand | no |
| H5 L·R is the only history alone at its trace | no; the record has no count of histories by trace |
| H6 four root classes when nothing is ranked | no; the record has the trace rule for the golden ground only |
| H10 one history made of one atom, the tick | **in part.** B1871's row T4 has it: "L, R and the bare exchange have a rational fixed direction; the tick has the golden one". That row came from this seat's own earlier sealed run. The naming of a ground "without a ranking" is not on record |

Also not on record: a Chern–Simons invariant of any departure.

- **What the "4.79" is (post hoc, labelled).** The seat reports that the steps shrink by about 4.79 and claims nothing
  for the number. Main asked what it is.
  - *Exact.* The root's monodromy acts on the characters of the fibre's group. At the point that carries the
    hyperbolic structure, the derivative of that action has characteristic polynomial (t − 1)(t² − 5t + 1). Its
    larger root is (5 + √21)/2 = 4.791288.
    The polynomial t² − 5t + 1 is already on record as the adjoint torsion at the geometric representation (B98).
    Main recomputed it here from the action on characters.
  - *Seen.* For three departures, (6), (2,2,2) and (3,4,3), the steps of the excess volume and of the Chern–Simons
    invariant both shrink by a ratio that tends to 4.791.
  - *So,* each added golden period brings a departure's own invariants closer to their limit by that factor. A
    departure is a local object in a long ground, and this is how fast the rest of the ground stops mattering.
  - That the ratio of settling is that eigenvalue is observed to four digits on three departures and is not proved
    here. It is the content of the lead P-775.

## 6. The seat's two questions, and main's opinion

Both are put to the owner by the seat. Neither is ruled, and main does not rule.

**What is a ground: anything that exists, or the act itself?**
- *The facts.* With every history as a ground there are four root classes and no order (H4 to H8). With the act as
  the ground there is one, and its level is 5 (H10).
- *Main's opinion.* The second is the cleaner reading, and it is a new clause. If it is adopted it should be written
  as a postulate with its own number, not counted as derived. It also rests on the tick being an act, which main has
  asked the owner once (P-771).

**Does "the ledger must close" mean the whole agrees with itself, or that one value comes out?**
- *The facts.* The seat's two readers both say the second reading contradicts the clauses that forbid picking. That
  is two readers of one model family, and judgement.
- *Main's opinion.* The owner's rulings as confirmed to main already fit the first reading. The claim is "one
  self-consistent outcome", self-consistent "means the closed loop", and the weight "stays open as the object of the
  closed loop". Main recorded with its confirmation that "one outcome" must mean one orbit of the whole, not one
  history picked. On that reading the closing selects nothing by itself, and a value can only be read from the whole,
  which needs the weight. So no further ruling is needed for main's next step; the wording goes into the foundation
  under P-767.

## 7. What main did not verify

- **The walls table** (twenty-one negatives against eight clauses; the seat and two readers). It is judgement, by
  three instances of one model family, and every negative was known when the clauses were written. The seat says all
  of this itself, and withdraws four of its own labels.
- **Existence of Pin structures,** and the pullbacks to the root's manifold.
- **The seat's row "walls 4 to 8"** in its table of § 6.4, which it marks as argued and not computed.
- **The eight clauses themselves.** Five rest on sentences the owner has not confirmed to main (P-768). The exercise
  builds on them to see where they fail. Main banks the sixteen computed facts and no clause.

## Seen first

- **The repo sweep:** seven sweeps, in § 5's table and its last line. Their verdict lines are in the run's own
  record of this session; the arcs they found are B1323, B1083, B1341 and B1871 for the tick, and none for the
  others.
- **For the settling rate:** the record holds the polynomial t² − 5t + 1 (B98 and the arcs that build on it; 25
  arcs match the sweep). It holds nothing on how a departure's volume or Chern–Simons invariant settles as periods of
  the ground are added (0 arcs).
- **The literature:** that words in L and R are all different acts is classical. That the monoid of non-negative
  unimodular matrices is generated by L, R and P is standard and is on record (B1323). Main computed and cites
  nothing.

## Disclosed

- **Main read the seat's numbers before computing.** The method is independent; the reading was not blind.
- **One of main's assertions was wrong before it was right.** It expected the golden ground to fail to detect 23
  traces besides its own; the seat's 23 includes its own. The seat's number stands.
- **H12 uses main's own enumeration of departures from B1869,** imported, not re-written.
- **The sign of a Chern–Simons invariant depends on an orientation convention.** Main used the same bundle names as
  the seat and gets the same signs. Only the relative sign of a history and its mirror is free of the convention.
- **SnapPy gives the invariant modulo ½.**

## Reproduce

```
python3 -B frontier/B1876_the_four_attacks_on_the_principles_draft_verified/verification/attacks_on_main.py
python3 -B frontier/B1876_the_four_attacks_on_the_principles_draft_verified/verification/settling_rate.py
python3 -m pytest -q frontier/B1876_the_four_attacks_on_the_principles_draft_verified/verification/
```
