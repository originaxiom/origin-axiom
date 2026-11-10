# PRE-REGISTRATION — the four remaining attacks on the principle: vacuity, retro-fit, self-application, the walls

**From:** the advisor seat. **To:** the owner and cc. **Kind:** `seal:` — written and committed before any of the
three scripts was run and before any reader was asked. Data-free: integers and SnapPy; nothing is measured and nothing
is compared with a measurement.
**The owner's word for this work** (2026-11-10, to this seat, after the seat said the four attacks were not started):
"i told cc. u can continue working on the rest".
**Sealed with this file** (`ARTIFACT_HASHES.txt`): `ledger_facts.py`, `tick_levels.py`, `walls_and_pin.py`,
`PROMPT_WALLS_READER.md`. Each script was checked to compile and was not run.

## 0. What is attacked

The draft of the principle in eight clauses, `principle_top_down/THE_PRINCIPLE_AS_RULED.md`, as it stands at commit
`d59e36d82`. **It is a draft and not a ruling.** Clauses 1, 4 and 8 rest on words the owner has confirmed to main.
Clauses 2, 3, 5, 6 and 7 rest on sentences the owner said to this seat and has not confirmed to main (P-768). The
owner has since told the seat that some sentences are said on purpose to see where they fail when built on. This
work takes each clause as given and builds on it for that reason. Nothing here makes a clause more ruled than it was.

In short: (1) what cannot be cancelled to nothing exists; (2) by survival, nothing is picked by being least or first;
(3) a single distinction alone makes nothing; (4) everything allowed happens; (5) everything that survives is kept
accounted for; (6) reality is read from the interaction of everything kept; (7) the act is the tick, and the bare
exchange is not an act; (8) the ledger must close.

## 1. What would count, written before the run

The criteria of `THE_PRINCIPLE_TOP_DOWN.md` § 4, committed before any attack was run, are kept:

> It stands (in a stated form) when one formal statement with no chosen ingredient reproduces the foundation's items
> as consequences, survives the alternatives of attack A, gives at least one sealed new consequence that checks, and
> has a recursion that is defined at every step. It is flawed (in that form) when every faithful statement needs a
> choice at the same place — then that choice is the real postulate and should be written as one — or the recursion
> branches without end, or a theorem refutes it.

Made specific for each attack:

| attack | the question | it lands if |
|---|---|---|
| **B vacuity** | what does the draft forbid, layer by layer? | at a layer it forbids nothing, or only what was put in. Read separately for four layers: the acts, the histories, a history against a ground, the closing of the ledger |
| **C retro-fit** | does it give anything nobody used in writing it? | no hypothesis below is at once (i) drawn from the clauses before computing, (ii) absent from the record by the sweep of § 5, and (iii) true. And, separately and already known: it says nothing about any measured number |
| **D self-application** | applied to what it produces, does it close, cycle, branch or run away? | with every history taken as a ground there is no single root, or the relation is not a consistent order; the attack does **not** land in the form where the ground is the act itself, if H10 holds |
| **E the walls** | does a result on record refute a clause, or do the clauses give the record's negatives? | a banked negative contradicts a clause in every reading of it. It is a point in the draft's favour, and post hoc, if the negatives follow from the clauses |

## 2. The hypotheses, with the seat's expectation of each

Notation: L and R are the two acts, P the bare exchange, F = L·P the tick, F′ = P·L. A history is a cyclic word. Its
runs are the lengths of its blocks of one letter. "Level" is reduction modulo an integer.

### Part 1 — the acts and the grammars (`ledger_facts.py`; attacks B and C)

| # | hypothesis | drawn from | expectation |
|---|---|---|---|
| H1 | Among non-negative integer matrices of determinant ±1 (entries to 8), the only ones of finite order are I and P. With those two removed, exactly four are not a product of two others: L, R, F, F′. With determinant +1 only: L and R. **So, given two whole-number records, clauses 1, 4 and 7 leave no choice in the set of acts.** | clauses 1, 4, 7 | holds, 95% |
| H2 | Words in L and R: every word a different act (known). Words in L and F: the same, to 14 letters. Words in L, R and F: not so; the first coincidence is F·R = L·F, at two letters. R is not made by L and F. | clause 5 (no entry twice) | free for L, F: 90%; the coincidence: 95% |
| H3 | In the grammar of L and F, a two-act history and its mirror image are one cyclic word. Primitive cyclic words, n = 1 to 10 letters: 1, 1, 2, 3, 6, 9, 18, 30, 56, 99; with an odd number of F: 1, 1, 1, 2, 3, 5, 9, 16, 28, 51; with an even number: 0, 0, 1, 1, 3, 4, 9, 14, 28, 48. To 8 letters the 32 even ones are the 69 two-act histories less the 5 that are an odd history done twice, taken in pairs. | clause 7 | 85% |

### Part 2 — every history as a ground (`ledger_facts.py`; attacks B, C and D)

The record's rule for the golden ground: its level is 5 = trace + 2, and another history is not detected when its
trace is ±2 modulo 5 (B1733, P-312). The draft's clause 2 forbids picking a ground by rank. So the rule is applied
here with **every** history as a ground, each at its own level, trace + 2.

| # | hypothesis | drawn from | expectation |
|---|---|---|---|
| H4 | Two histories of different trace never fail to detect each other. Each fails to detect the other exactly when the traces are equal. | algebra | 97% (a short proof) |
| H5 | **Exactly one two-act history is alone at its trace: L·R.** (For trace t ≥ 4 the words L^(t−2)R and LR^(t−2) differ.) Counting a history and its mirror once, the traces with one history include 3, 4, 5 and 9; the seat does not know whether the list is finite and expects between 5 and 12 of them up to 60. | clause 2 with the record's rule | first part 97%; the list: 60% |
| H6 | The traces that are a departure of no other ground are exactly 3, 4, 5 and 6: eight histories in four classes. **So with nothing ranked the rule has no single root.** | clause 2 with the record's rule | 90% |
| H7 | The relation is not a consistent order: there are chains a → b → c in which a detects c. One such is 3 → 7 → 16. | algebra | 90% |
| H8 | Chains from the golden ground do not reach every trace; 9 is not reached. | algebra | 85%; the example 80% |
| H9 | Read by primes instead (a history is not detected when its discriminant has every prime of the ground's): the relation is then a consistent order. The only traces whose discriminant has one prime are 3 (the prime 5) and 6 (the prime 2). Among traces to 60 more than six are minimal. | algebra | single-prime: 95%; more than six: 75% |
| H10 | **Of the four atoms, two (L, R) have a rational fixed direction and two (F, F′) do not, and F′ is F seen from the other side. So exactly one history is made of one atom: the tick.** Its discriminant is 5. Under clause 7 the ground and its level are then named without any ranking. | clauses 3, 7 | 100% as algebra; whether the owner accepts "the ground is the act" is not the seat's to say |

### Part 3 — the tick at the levels (`tick_levels.py`; the tick's second debt; attack B)

| # | hypothesis | expectation |
|---|---|---|
| H11 | With the exchange, the group of the acts modulo N has twice the order for N ≥ 3 (known). **Up to scalars it does not double at N = 5 or 13, and does at 3, 4, 7, 8, 9, 11**: where −1 is a square, the exchange is a scalar times something already there. | primes: 90%; N = 4, 8, 9: 75% |
| H12 | At level 5 the centre of the larger group is {±1, ±2}, and F is 3 times a unipotent. **Every departure to 14 letters is allowed or not exactly as before:** its matrix against the ground is the same whether written with two acts or with the tick; the line reading against F is the line reading against L·R; no departure is a scalar 2 or 3. So the record's level-5 premises are unchanged by the tick, and the least departures are still (6) alone under the charge reading and (6) with (2,2,2) under the line reading. | 90% |
| H13 | F multiplies the mark (1,2) by 3. It keeps no vector up to sign and keeps the four non-zero vectors of the golden line up to a scalar. So under the tick the mark is the line and not one twin (main's remark in B1872, here as a count). | 100% as algebra |

**A wrong expectation, recorded:** before working it through the seat expected the tick to allow departures shorter
than six letters. Its own algebra then showed E is unchanged (H12). The earlier expectation is recorded because it
was held.

### Part 4 — the hand, and a history with no hand (`walls_and_pin.py`; attack E; the tick's first debt)

| # | hypothesis | expectation |
|---|---|---|
| H14 | The golden ground with 1, 2 and 3 periods is its own mirror image and its Chern–Simons invariant is 0 modulo 1/2 (known for one period). | 95% |
| H15 | **The run of 6 has a hand, and its Chern–Simons invariant is not 0** (for 1, 2 and 3 further periods); its mirror has the opposite value. So the eight walls that the record traces to the mirror (B1234) do not hold for that history taken alone, and hold again for the pair. | chiral: known; not zero: 80%; opposite: 95% |
| H16 | For every history with an odd number of runs to 6 letters: it is not orientable; the Chern–Simons invariant is not defined; and twice the number of fibre structures it keeps (of the four quadratic forms) equals the number of elements of H¹(bundle; ℤ/2), which is the number of Pin structures of either kind. The tick alone keeps one form, the odd one. | 90% |

### Part 5 — the walls, by reading (attack E)

Twenty-one negatives of the record: the twelve nodes graded NEGATIVE on main's closure map at `d91e91469`, the eight
walls of B1234, and B990. Each is set against the eight clauses as FOLLOWS, INDEPENDENT or OPPOSES.

- **Two readers** are given `PROMPT_WALLS_READER.md` and nothing else, on two different models of one family. They
  do not see the seat's table.
- **The seat's own table is sealed here:**

| # | the negative | the seat's label |
|---|---|---|
| 1 | W:DRAW | INDEPENDENT |
| 2 | W:HANDS | FOLLOWS (7; 2, 4) |
| 3 | W:NO-ATOM | FOLLOWS (2, 4) |
| 4 | W:NOMOD | FOLLOWS (2, 4); OPPOSES 8 if 8 means one point |
| 5 | W:NOVAL | FOLLOWS (2, 4); OPPOSES 8 if 8 means one point |
| 6 | W:ONE-END | INDEPENDENT |
| 7 | V:WALL | FOLLOWS (6, 2) |
| 8 | T:NO-PLACE | FOLLOWS (2, 4); OPPOSES 8 if 8 means one point |
| 9 | SC:CARD | INDEPENDENT |
| 10 | SC:UNIT | INDEPENDENT |
| 11 | GR:VECTORLIKE | FOLLOWS (7), low confidence |
| 12 | CO:S3 | INDEPENDENT |
| 13–16, 18–20 | seven of B1234's eight | FOLLOWS (7) |
| 17 | B1234's naming wall | FOLLOWS (7) for "mirror-even"; INDEPENDENT for "dimensionless" |
| 21 | B990 | FOLLOWS (2, 5); OPPOSES 8 if 8 means one point |

- **Expectations:** the seat's count is 16 FOLLOWS and 5 INDEPENDENT. It expects each reader to give FOLLOWS to at
  least 12 of the 21, to agree with the seat's FOLLOWS-or-not on at least 14, to find none that opposes clause 1,
  and to find at least 3 that oppose clause 8 read as a single point. 65% for all four together.
- **What the table cannot show:** the clauses were written after every one of these negatives. Agreement is post hoc
  and is not evidence for the draft. It can only show whether the draft and the record's negatives say the same
  thing.

## 3. What the seat expects overall, written before the run

- **B.** The draft forbids a definite thing at the first layer (two acts, I and P, and every act that subtracts),
  nothing among histories beyond the one-letter words, nothing overall at the relative layer once every history may
  be a ground, and nothing at the closing as the record now defines it. **Not vacuous as a foundation; vacuous as a
  selector.**
- **C.** Some hypotheses drawn from the clauses will hold and be new to the record (H1, H2, H5, H6, H10 are the
  candidates). None touches a measured number.
- **D.** With every history as a ground: four root classes, not one, and no consistent order under the record's rule.
  With the act as the ground: one ground and one level. The draft does not say which is meant.
- **E.** The clauses give most of the record's negatives, and clause 8 is the one place where the draft and the
  negatives pull apart.
- **The seat's guess at the whole:** the draft stands as a generator of the ledger and forbids the selections that
  the record's value frame makes. 70%.

## 4. Controls built into the scripts

Each script asserts facts known before the run and stops if one fails: F·F = L·R, P·P = I, the run-sequence form of a
two-act word; the library's names for m004 and m000 and the orientation cover; and, in `tick_levels.py`, the least
departures to 14 letters, which the sealed run `non_cancellation/` already gives ((6) alone under the charge reading
with the next at 11 or 10; (6) and (2,2,2) under the line reading with the next at 7).

## 5. Seen first: the sweep of the record (a read-only search by one reader, before this file was written)

| | on the record | not found on the record |
|---|---|---|
| the trace rule | for the golden ground: B1733 ("N ∣ t − 2 or N ∣ t + 2"), P-312, B1868, B1872; the level as det(A + I) = tr A + 2 = 5 (the scale card's design) | the rule for a general ground; the discriminant as a level; "ramified" |
| equal trace | — | that two histories fail to detect each other exactly at equal trace; any count of histories by trace |
| the atoms | B1323: the non-negative matrices of GL(2, ℤ) are those of L, R, P; B1454: every hyperbolic matrix in a box is ± a positive word | that the monoid of L and R is free; the four atoms; a grammar of L and F; the relation F·R = L·F |
| the tick | B14, B469, B1607, B1323, B1871 (the tick as the rule; the bare exchange done twice is the identity) | that this makes the bare exchange "not an act"; the root named without a ranking |
| the group with the exchange | its orders at levels 2 to 8 (B1871, from this seat's run) | its centre; whether it doubles up to scalars |
| the hand of a departure | B1867: "the run of 6 has a hand and a place and no arrow" | a Chern–Simons invariant of any departure |
| Pin structures | B1175 and B1141 (m000 has two Pin⁻ structures; one of m004's two spin structures does not extend); sm:B1382 as harvested in B1453 (m004's two spin structures are the pullbacks of m000's Pin⁺ and Pin⁻ structures) | a count for other histories with no hand |

Under the record's rule a statement in the right-hand column is "not found on the record", not "new".

## 6. Disclosed before the run

- **The seat designed the hypotheses knowing the record's results and its own earlier runs.** H4, H5's first part,
  H9's first part, H10, H12 and H13 were worked by hand first; for those the run is a check of the algebra, and the
  probabilities say so.
- **Parts 2 and 3 use the record's level construction** (cancelling relative to a ground, at the ground's level). No
  reader of the owner's words reached that construction in attack A. It is the record's and the seat's.
- **The walls table is judgement.** Two readers of one model family and the seat are not independent witnesses.
- **Nothing here is, or needs, a look at data.**
