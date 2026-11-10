# RESULT — two acts or one tick: what the tick gains and what it breaks

**From:** the advisor seat. **To:** the owner and cc. **Kind:** `result:` — data-free (integers and SnapPy);
`domain: all two-act histories to 8 letters; the tick's own histories to 5 letters; levels 2, 3, 4, 5, 7, 8`.
**Sealed before the run:** `PREREGISTRATION.md` and `tick_facts.py` at commit `f57f4701f` (`ARTIFACT_HASHES.txt`).
**Outputs:** `tick_facts_out.txt` (the sealed run), `tick_facts_corrected_out.txt` (see section 5).

## 1. The answer

**Nothing in the principle forbids the tick, and nothing forces it. The computation shows the trade exactly.**

- **With two acts,** LR being its own mirror image is an unexplained special property: 11 of the 69 histories to 8
  letters have it.
- **With the tick,** it is explained: LR is the tick done twice, and a history with no hand, done twice, is its own
  mirror. The tick also turns one of the frame's chosen joints — which of two lines — into a single orbit.
- **The price:** the tick adds histories that have no hand at all; from level 3 upward the group of the moves
  doubles; over one tick the frame's line is no longer single-valued; and a single tick survives alone, which bears
  on what "not single objects alone" refers to.

Under the rulings of the day there is no "root" to pick (R15: nothing is ranked). The question is only whether "add,
and the two sides change roles" is an act. If it is allowed, then by clause 4 it happens, and both kinds of history
are in the ledger.

## 2. What was computed

**T1 — what exists.** Histories with n letters:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| two-act histories | 0 | 1 | 2 | 3 | 6 | 9 | 18 | 30 | 56 | 99 | 186 | 335 |
| added by the tick (an odd number of runs) | 1 | 1 | 1 | 2 | 3 | 5 | 9 | 16 | 28 | 51 | 93 | 170 |

The tick adds about half as many histories again. Each one checked (8 of 8, to 5 letters) is non-orientable, and its
orientation cover is the same history done twice (8 of 8): (1) covers to LR, (2) to LLRR, (3) to LLLRRR, and so on.

**T2 — handedness.** All 69 two-act histories with at most 8 letters, SnapPy against a combinatorial prediction (a
history is its own mirror exactly when its cyclic run sequence returns to itself under an odd rotation, or under a
reflection that changes the parity of positions). **The prediction agrees on 69 of 69.**

| | histories | their own mirror |
|---|---|---|
| a tick-history done twice: LR, LLRR, LLLRRR, LLLLRRRR, LLRLRRLR | 5 | 5 |
| its own mirror by a reflection: LLRLRR, LLLRLRRR, LLRLRLRR and their reverses | 6 | 6 |
| has a distinct mirror partner (29 pairs): LLR and LRR, LLLR and LRRR, … | 58 | 0 |

**T3 — the exchange at the levels.**

| level N | 2 | 3 | 4 | 5 | 7 | 8 |
|---|---|---|---|---|---|---|
| group of the two acts | 6 | 24 | 48 | 120 | 336 | 384 |
| group with the exchange | 6 | 48 | 96 | 240 | 672 | 768 |
| exchange already inside the two acts' group | yes | no | no | no | no | no |

At level 5 the tick is 3 times a unipotent matrix. It keeps the golden line and multiplies its points by 3:
(1,2) → (3,1) → (4,3) → (2,4) → (1,2). Up to sign that is (1,2) ↔ (2,4): **the tick exchanges the two lines the
record writes (1/5, 2/5) and (2/5, 4/5).** One tick fixes no non-trivial fibre character and inverts none; two ticks
invert the group of order 5.

**T4 — a single act alone.** L alone, R alone and the bare exchange alone each have a rational fixed direction: the
subtraction of the two sides ends. **The tick alone has the golden direction: it never ends.**

## 3. What it means, against what was written first

1. **At the level of parities the tick is nothing new.** Mod 2 the exchange is already made by the two acts, so the
   record's "three" (`docs/THE_WEAVE.md`, W1) does not change. From level 3 on it is a new act and the group
   doubles. Everything the record built on the two acts' group at an odd level — the level-5 representation, the
   charge and line premises — would have to be read again under the larger group. *Not computed here.*
2. **The gain at level 5 is one chosen joint.** B1845 says the frame's line is "the hand plus one binary choice", and
   the scoreboard carries the line's offset as CHOSEN (A03). Under the tick the two lines are one orbit, so there is
   nothing to choose.
3. **The cost at level 5 is that the line is not single-valued over one tick.** Over two ticks it extends as a pair
   (this relay's `back_edge_A/`, §2.3). Over one tick the four characters go round in a cycle, so only all four
   together extend.
4. **The root's mirror symmetry becomes a consequence.** B1234 found that eight banked walls pass through
   amphichirality and that an orientation double cover has it by construction (40 of 40). T2 shows the same inside
   the grammar: every history that is a tick-history done twice is its own mirror (5 of 5), and LR is the first.
5. **A hand still arrives only in pairs.** 58 of the 69 two-act histories have a distinct mirror partner, and the
   tick adds histories with no hand at all. Neither grammar supplies one hand.
6. **A single tick survives alone (T4).** Under the two acts no single act survives, and only their meeting does,
   which fits "not single objects alone" read of acts. Under the tick that sentence has to be read of the two sides:
   they meet inside one tick — one takes from the other, and they change roles. So the question "two acts or one
   tick" is also the question **what the two distinctions are: the two acts, or the two sides.**
7. **The ledger's first line does not see the exchange.** Swapping a and b sends the commutator to its inverse, and
   the trace of an inverse is the same trace. κ is kept under either ruling.

## 4. For the ruling

| | Two acts only | The tick is an act |
|---|---|---|
| what the two distinctions are | the two acts | the two sides |
| the owner's "a, ab, ba" rule | two steps of it | the rule itself (B1607) |
| histories with no hand | none | about half as many again as the rest |
| LR its own mirror | a special property | a consequence |
| the two level-5 lines | a choice | one orbit |
| the group at odd levels | as the record has it | doubled; to be read again |
| spin structures on every history | yes | not on the added ones; what replaces them is not computed |
| on record | SE2 CHOSEN, "the most fragile link" | GM5c OPEN; FK2's second option, "carrying both m004 and m000 as states" |

**The seat's advice, now that it is computed:** admit the tick as an act and keep both kinds of history in the
ledger. Three reasons: it is the owner's own founding rule; nothing in the principle forbids it, and clause 4 says
what is allowed happens; and it explains the root's mirror symmetry instead of assuming it. **Two debts come with
it and should be named in the ruling:** what replaces a spin structure on a history with no hand, and the record's
odd-level structures read again under the doubled group. It does not supply a hand.

## 5. Disclosures

- **The sealed script had a counting error, found on reading its output.** It tested primitivity on the run sequence
  where it belongs on the word, so it dropped every history that is a tick-history done twice — LR among them — and
  counted histories up to the mirror. Its class "double of an odd sequence" came out empty, which is how it was
  seen. `tick_facts_corrected.py` was hashed and run after; both outputs are kept. T3 and T4 are unaffected. The
  sealed run's T2 agreement (64 of 64) stands for the 64 it did check; the corrected run checks all 69.
- **One sealed expectation was wrong:** the seat expected the tick to add "roughly as many histories again". It adds
  about half as many.
- **The others held:** the prediction agrees with SnapPy on every history; every double is its own mirror; the first
  history with a mirror partner has 3 letters; no added history is orientable; the exchange is inside the two acts'
  group only at level 2; the tick exchanges the two lines; the tick alone never ends.
- **In passing:** two readers of attack A called LLRLRR and LLRRLR a chiral pair. They are one manifold (a word and
  its reverse), and it is its own mirror.

## 6. Not computed, and owed before anything is built on the tick

- B1234's eight walls, one by one, with the tick's histories in the ledger.
- Pin structures on the non-orientable histories, in place of the spin structures of B1477–B1481.
- The level-5 representation and the charge and line premises under the doubled group.
- What the record's structural chain needs of orientability. (`GENESIS.md` notes one thing that does not: π₁(m000)
  has the same 48 surjections onto 2T.)
