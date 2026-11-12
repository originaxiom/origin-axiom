# B1879 — The weave's theorems with the exchange added: the computation the owner asked for before deciding on the tick

*Main, 2026-11-11 (S306p). The owner has ruled that the tick is an act, and earlier, on 2026-10-08, that even ticks
are what is observed. Asked how the two stand together, the owner answered "After the computation". This is the
computation: for each statement the closure map holds about the weave, what becomes of it when histories of an odd
number of ticks take part. Data-free: exact algebra, a count, and SnapPy. No measured number is read and nothing is
compared with a measurement. It decides nothing; it says what each decision costs. 0 of 19.*

> **Corrections of 2026-11-12 (Review 79).** This arc was read in full by a session that did not build it, and ten
> things in it were wrong or wider than what was computed. Each is corrected where it stands, with the old words kept.
> One concerns the first sentence above: by the working rules' point on what the owner says, "the tick is an act" is
> a supposition about the mathematics, re-typed as such on 2026-11-11, and it is not recorded as his ruling. This
> page, here and in § 7, was written before the re-typing and calls it a ruling; those sentences are kept as written.

## 1. The answer first

- **Most of what the record holds about the weave is unchanged** when the exchange is added to the moves: the two
  fixed characters, the walk's law of run lengths, the absence of a fixed modulus, one end per history.
  [CORRECTED 2026-11-12 (Review 79): this read "the walk's measure". What was computed is the law of the lengths of
  runs; § 2's row says what that leaves unshown.]
- **What changes is one thing: the hand.** With the exchange the triplet is no longer a representation by itself. It
  joins its conjugate into one irreducible piece of dimension six. The group then contains its own generalised CP.
  The chiral three, whose sign is the hand, then has no sign left at the level of the weave: that is argued from the
  joined piece, and the index was not recomputed (§ 2).
  [CORRECTED 2026-11-12 (Review 79): this was stated as a result, with no word that it is an argument.]
- **One thing gets stronger, and main did not expect it.** The tick, alone, fixes exactly two characters: the trivial
  one and the quaternion point. The record needs both two-act moves together for that. So the place where the
  records sit is singled out by the single founding act.
- **So the decision, in one sentence.** If all ticks take part in what is observed, the weave has no hand of its own,
  and the chiral three is not a weave result; a hand has to come from somewhere else. If even ticks are what is
  observed, the record stands as it is, and that restriction is what carries the hand.
- **One of main's expectations was not well posed** (§ 4). Two of the record's negatives were not restated, because
  they compare with measurement (§ 5).

## 2. Statement by statement

| the record's statement about the weave (its node on the map) | with the exchange added | how it is known |
|---|---|---|
| the two moves fix exactly two characters: the trivial one and the quaternion point (W:Q8) | **unchanged.** The exchange fixes both. **And the tick alone fixes exactly these two** | exact, § 3 |
| at the quaternion point the moves' lift is a triplet (W:T) | **changed.** The triplet is half of one irreducible piece of dimension six | computed: 96 elements and two pieces become 192 and one |
| the weave's group has order 96, and its generalised CP is the record swap (W:G96) | **changed as that statement itself says:** order 192, and the group contains its CP | computed; the triplet's indicator twisted by the exchange is +1, whatever the lift |
| neither hand is derived on the weave (W:HANDS) | **stronger:** on the joined piece there is no hand to derive | follows from the row above |
| given two tagged inputs, the chiral three is an index ±3 (W:INDEX3) | **changed.** The sign is the hand. The exchange carries the half with one sign onto the half with the other, so the one joined piece has no signed index | argued from the two rows above; the index itself is not recomputed here |
| the moves' walk gives Minkowski's measure (W:WALK, W:MEASURE) | **the law of run lengths is unchanged, exactly.** A run has length r with probability 2⁻ʳ in the grammar of L and the tick, as in that of L and R. **The measure itself is not shown unchanged** [CORRECTED 2026-11-12 (Review 79): this read "unchanged, exactly". The node's statement holds "at every strength of the pull-back", and no pull-back was computed. And a word in L and the tick, rewritten in L and R, always begins with L, where words in L and R begin each way equally: so where the walk's point lies is not the same in the two grammars] | exact count: all 165 triples of runs that fit in 12 letters |
| no weight at the cusp (W:NO-ATOM) | unchanged: it is a statement about that same measure | follows |
| no point of the modulus is fixed by every move (W:NOMOD) | **unchanged, a fortiori.** The tick fixes no point of the half-plane. The exchange adds mirrors: the lines Re τ = 0, Re τ = ½ and ∣τ∣ = 1 | exact |
| a generated state has one end (W:ONE-END) | **unchanged:** each of the 22 histories of an odd number of runs to 7 letters has one end [Added 2026-11-12 (Review 79): this holds by construction. A bundle over the once-punctured torus has one cusp whatever its monodromy, so the count could not have come out otherwise and tests nothing the exchange could change] | SnapPy; by construction |
| a sum over all threads is mirror-even (W:FLAT-SUM, W:MIRROR-EVEN) | unchanged, and now by construction | follows |
| no parameter is a number of the weave's group; the six read as a draw (W:NOVAL, W:DRAW) | **not restated** | they compare with measurement: § 5 |

## 3. The tick alone fixes the quaternion point

Write a character of the two records' free group by three traces, (tr a, tr b, tr ab).

| which moves | the characters they fix |
|---|---|
| one two-act move alone | a curve |
| the two moves together | the trivial character (2, 2, 2) and the quaternion point (0, 0, 0): the record's theorem |
| the exchange | fixes both of those |
| **the tick alone** (a → ab, b → a) | **exactly (2, 2, 2) and (0, 0, 0)** |
| the tick done twice, which is the root | a curve again; the quaternion point and the hyperbolic structure's point lie on it |

- **Why it matters.** The closure map says of the triplet: "That the records sit at that point is the grammar's
  premise, not this theorem's." With two acts, the point is where *both* moves agree. With the tick, it is the one
  non-trivial character that the *single* founding act leaves alone. That is a shorter premise.
- **It is special to the single tick.** Done twice, the tick fixes a whole curve. So this is a fact about the act,
  and not about the root.
- The proof is three lines: a fixed character has tr ab = tr a, tr a = tr b, and tr a · tr ab − tr b = tr ab; so all
  three traces are equal to one number t with t² = 2t.

## 4. The six-dimensional space

- **Computed on main's own matrices** (B1610's): the two acts generate 96 elements and leave two pieces, the triplet
  and its conjugate. With the exchange there are 192, and one piece. L and the tick alone generate the same 192.
- **The exchange is a consistent conjugation of the triplet onto its conjugate.** Its twisted indicator is +1, for
  any lift. This is the record's own statement (B1611: the weave's generalised CP is the record swap), recomputed.
- **One invariant bilinear form exists with the exchange, where the two acts have two.** It pairs the triplet with
  its conjugate and vanishes on each alone. It is a pairing of the two hands, not a form on one.
- **What main expected and could not state.** Main expected to say whether the joined six is a real representation.
  The answer depends on a phase in how the exchange is lifted to this space: main's lift gives one answer and i times
  it the other, with the same 192 elements. Nothing on record fixes that phase. So no such statement is made.
- **On record already, and it bounds this:** at the common point itself the exchange is not new. L and R generate
  every automorphism of that point, the exchange's among them (B1687). The doubling is only in the lift.

## 5. What was not computed

- **The two negatives that compare with measurement** (no parameter is a number of the weave's group; the six read as
  a draw). Restating them for the larger group means computing with measured values, and that belongs behind a
  sealed card.
- **The index itself.** The row on the chiral three is an argument from the representation: an index whose sign
  flips between the triplet and its conjugate has no sign on the piece that joins them. Main did not recompute the
  index with the exchange. If the index were not odd under the exchange, the argument would not apply.
- **The levels where the group doubles, beyond what the six-dimensional space holds.** That space lives at level 4,
  where the group does double. Level 5, where it does not, was done in B1876.

## 6. What each decision would mean

| | all ticks take part in what is observed | even ticks are what is observed |
|---|---|---|
| the hand | not in the weave. The triplet and its conjugate are one piece | carried by the restriction to even ticks |
| the chiral three | not a weave result. A hand must come from elsewhere: from the weight, or from a state that breaks the mirror by itself | stands as now, conditional on the restriction |
| CP | a symmetry of the weave | not imposed |
| the quaternion point | singled out by the one act | singled out by the two moves together |
| the measure, the modulus, the ends | as now | as now |
| what is added to the input budget | nothing | the restriction itself: one declared bit, as the orientation is now |

**A third reading exists, and it is main's suggestion, not a result:** keep every tick in the ledger, and treat "only
even ticks are observed" neither as a ruling nor as false, but as a condition the weight has to deliver. The chiral
three then stays exactly as conditional as it is today, and the budget's orientation bit becomes a named condition
to be derived, not a declared choice. This is the form the ruling of 2026-10-08 itself points to: "revisit if a
mechanism makes the vacuum break the mirror by itself".

## 7. The owner's decision, with this result in hand (2026-11-11)

Main put the question again, quoting both rulings and the one thing at stake between them. The owner chose:

> "A condition to derive (Recommended)"

That is the third reading of § 6, and it is now the owner's ruling to main, not main's suggestion:

- **Every tick is in the ledger.**
- **"Only even ticks are observed" is no longer a ruling.** It is a condition the weight has to deliver.
- **The chiral three stays exactly as conditional as it was.** Its condition now has a name and an owner: the weight.
- **The budget's orientation bit is a named condition to derive,** not a declared choice. It is not derived, and it is
  not counted as derived.

What this does not do: it supplies no hand. It says where a hand would have to come from.

## 8. Dated addition, 2026-11-11: checked by the advisor seat, and one sharper fact

The advisor seat recomputed every statement of this arc that can be computed, with its own code (its `verify_b1879/`
@ `7726eeed`; not blind, since main had landed the result first). All of it agrees.

> **CORRECTED 2026-11-12 (Review 79).** The two sentences above state another session's check as a fact of this
> record. Its code and outputs are on that session's branch and not on main, and main has neither read nor run them.
> What can be said: by its own account it recomputed these statements with separate code, after main's result was
> public, and found agreement. The verdict file now cites it as that, and no label of the protocol is claimed for it
> here.

It put one question more, after its check: every history fixes the two universal characters; which histories fix
nothing else? Main checked its answer with main's own code (`verification/only_the_tick.py`, exact, by Groebner
bases over the rationals):

| history, in the grammar of L (add) and F (the tick) | the characters it fixes |
|---|---|
| **F** | **the trivial character and the quaternion point, and nothing else** |
| FL | those two, and (−2, 2, −2) |
| the other eleven of at most five letters | a set of positive dimension |

- **So § 3 holds in a stronger form.** Among the thirteen histories of at most five letters, the single tick is the
  only one whose fixed characters are exactly those two. The square of the tick, which is the root, is not among the
  thirteen: the count leaves out a power of a shorter word. It fixes a curve (§ 3).
  [CORRECTED 2026-11-12 (Review 79): this read "The square of the tick, which is the root, is one of the eleven."
  The run's own heading says the thirteen are words that are not a power.]
- **Not proved beyond five letters.** The fact is the advisor seat's; main reproduced it.

## Seen first

- **The repo sweep:** `VERDICT topic-sweep` for the tick's fixed characters and the trace map's fixed points finds 21
  arcs, the early ones on the Fibonacci trace map among them (B18, B26, B28, B30, B344, B497); none states that the
  tick alone fixes exactly the trivial character and the quaternion point, and those arcs were not re-read in full.
  For the group with the exchange it finds 10 arcs: B1611 (the generalised CP), B1687 (the common point's
  automorphisms) and B1871 (96 to 192) are the ones used here.
- **The literature:** the trace map of the Fibonacci substitution is classical. Main computed and cites nothing.

## Disclosed

- **This arc was asked for in order to inform a decision.** It is written so that either decision can be read off
  it. The suggestion in § 6 is main's and is marked as such.
- **Main asked the owner about the tick without the standing ruling beside the question** (Review 78's record). This
  computation is what that omission cost, done the same day.
- **The expectations were written before computing,** in the script's header. [CORRECTED 2026-11-12 (Review 79):
  nothing on file shows that. The header carries each outcome beside its expectation, and script, run and findings
  entered the record in one commit. By the protocol's labels this arc is computed once.] Of six, three held, one was already on
  record, one failed in a useful way (the tick alone fixes the two characters), and one was not well posed.
- **The exchange's lift on the six-dimensional space is fixed only up to a phase.** Only statements that do not
  depend on it are made.

## Reproduce

```
python3 -B frontier/B1879_the_weaves_theorems_with_the_exchange/verification/weave_with_the_exchange.py
python3 -m pytest -q frontier/B1879_the_weaves_theorems_with_the_exchange/verification/
```
