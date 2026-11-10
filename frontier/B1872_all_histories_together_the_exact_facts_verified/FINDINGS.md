# B1872 — "All allowed histories together": the web seat's definition read, and its exact facts verified on main

*Main, 2026-11-10 (S306o). The owner's confirmed ruling puts the claim on all allowed histories together. Main's
opinion on it was that it closes nothing until "together" and its read-out are defined. The owner chose, with the web
seat, to have it defined. The seat's relay does so (`relays/CHAT1_TO_CC_2026-11-10_A_ALL_IN_WEAVE_FORM.md` @
`a711bd189`), with eleven exact facts at level 5. Main read the relay in full, ran none of its code, and recomputed
the facts with its own: seven in B1868, the other four here. Data-free: integers only. 0 of 19.*

## 1. The answer first

- **"Together" has a definition the record already holds.** It is the weave's own sentence applied to the allowed
  set: the joint action of the allowed histories on the shared records — the group they generate — and what that
  action forces. The seat calls the result an allowed subweave.
- **It has two requirements.** The allowed set must be closed under composition, and its data must sit on the shared
  records and not on each history separately.
- **At level 5 the allowed subweave is the stabiliser of one marked line, up to sign.** The two readings of the
  level-5 premise allow different words and generate that same group.
- **Read through what it fixes, it selects nothing.** It keeps both twin lines, never one. It fixes no value of the
  modulus. The loop closes trivially at every level.
- **So the definition is done and the read-out is not.** A back-edge needs a quantity taken on the subweave as a
  whole that its fixed data do not determine. Nothing on record supplies one.
- **The facts hold.** All eleven reproduce on main.

## 2. The four further facts, on main

| | the fact | the seat | main |
|---|---|---|---|
| F8 | four histories that the charge reading allows — L⁶R(LR)^k and LR⁶(LR)^k, k = 1, 2 — generate, in the modular group up to sign, a subgroup of index | 12, the whole stabiliser of the line | **12**, by another instrument (coset enumeration on the presentation with one generator of order 2 and one of order 3); the same instrument gives 1 for the whole group and 3 for a subgroup of known index |
| F9 | positive words of 1 to 12 letters that keep the line; of those, a word that is ±1 at level 5 followed by golden periods | 694; 204 | the same; and every one of the 694 keeps the twin line too |
| F10 | cyclic words of 2 to 12 letters with trace ±2 at level 5; with no rotation that keeps the marked line | 330; 23, the first LLLRLRRR | the same |
| F11 | the group generated at level 5 by LR and RL | all 120 elements | the same |

What they show, in the relay's words and main's check:

- **The two readings allow different words and generate one group** (F8, F9). Their difference is in which words are
  counted, not in what they jointly do.
- **A line belongs on the shared records** (F10, F11). A thread's own line moves with its base point: one thread read
  from its two base points already keeps no line jointly.
- **The twins come together** (F9). No history that keeps a line keeps it without its twin.

## 3. What it means for the programme

- **The weight's package has a sharper statement.** The missing object is a function on the allowed subweave's
  quotient — the modulus together with the marked line — that the joint action itself defines and that singles out a
  point or an orbit. The weave's text allows one form of it, the minima of the joint action's own functional, and
  holds none. The other meanings of "together" need a counting rule or an action, or read one history.
- **"One departure" and "least" are not part of what is allowed.** Neither is closed under composition. They are
  selections made afterwards, and the owner's ruling already places "least" on a thread.
- **"A single state",** the first back-edge's condition, is part of what is allowed only if it is shown closed under
  composition. Nobody has shown it. Otherwise that back-edge has to be restated as a read-out on the subweave.
- **Which level counts is still a choice** (P-721), and the record's own rule for ladders takes every finite level at
  once.

**A link to B1871, main's.** At level 5 the tick multiplies the points of the golden line by 3, so it exchanges a
line with its twin. If the tick is an act, the mark cannot be one twin: it is both. The seat's third fork ("one twin
or both as the mark") is then answered by the grammar. With both twins as one datum, the only points with a
non-trivial stabiliser lie over the symmetric point, where the record warns that a fixed point "is not a world".

## 4. The seat's asks

1. **Recorded** against the closed-loop claim (P-761), the carrying-out of the rulings (P-767) and the weight's
   package.
2. **Verified,** as above.
3. **A dated note is on B1856:** at level 5 the line reading and the charge reading allow different words and
   generate the same group up to sign.
4. **Passed to the advisor seat** in main's reply: under the joint action its second condition is part of what is
   allowed only if it is closed under composition, and its "frame's line" must be a mark on the shared records.

## 5. The seat's three forks, with main's opinion

| | the fork | main's opinion |
|---|---|---|
| 1 | is "together" the joint action? | Yes. It is the weave's own sentence, which the owner fixed on 2026-10-07; applying it to the allowed set needs no new rule. |
| 2 | where does "a single state" belong? | Outside what is allowed, until it is shown closed under composition; as a read-out on the subweave it is a candidate, not yet defined. |
| 3 | one twin or both as the mark? | With two acts it is a convention the joint action does not read. If the tick is an act it is both (§ 3). |

None of the three is ruled.

## Seen first

- **The repo sweep:** the seat's seven sweeps were read with its relay. The record holds the lines of order 5 thread
  by thread (B1733, B1845, B1853, B1856), the weave's own sentence and its clause on minima (THE_WEAVE), and the
  orbit-to-point gap (B990; B1867 § 4). It does not hold the allowed histories as a group, whether a condition is
  closed under composition, or a definition of the joint read-out.
- **The literature:** the congruence subgroups of level 5 and their indices are classical; the index is computed
  here, not cited.

## Disclosed

- **Main read the seat's numbers before computing.** The index is computed by another instrument; the counts are
  enumerations and leave no room for a second answer.
- **This arc verifies facts and records a definition.** It derives nothing and selects nothing.
- **The link to the tick in § 3 depends on a question the owner has not ruled** (whether the tick is an act).

## Reproduce

```
python3 -B frontier/B1872_all_histories_together_the_exact_facts_verified/verification/together_facts.py
python3 -m pytest -q frontier/B1872_all_histories_together_the_exact_facts_verified/verification/
```
