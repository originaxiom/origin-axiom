# PROPOSAL — the count as an output: one derivation graph from the principle to the values

**From:** the advisor seat. **To:** cc and the owner. **Kind:** `propose:`. The owner agreed to it on 2026-11-10
(`OWNER_RULINGS_2026-11-10.md`, R5); cc confirms with the owner and may `challenge:` the design.
**Origin:** the owner's question of 2026-11-10: "0-19 is also put by hand, not through any gates nor its dynamical …
if were creating a table of interactions and mapping everything that has to come from foundational principle all the
way to the values, each node and calculation, should it automatically reflect the 0-19 claim (what if its more than
19 in our math) - and should it have some filter or scrutiny what it admits".

## 1. The finding behind the question (verified at `217e37c4f`)

| Where the figure appears | How it is produced |
|---|---|
| `README.md` state block | `scripts/views/generate.py:379` reads the sentence "Its state is **0 of 19**" from `docs/MAIN_GOAL.md` by regex. The sentence is typed by hand. |
| `docs/views/CONTEXT_RECOVERY.md` | `scripts/views/generate.py:316` writes the literal row "the Standard Model's 19 derived \| 0". |
| the `inputs-scoreboard` gate line | `scripts/checks/inputs_scoreboard.py:75` prints `"%d of 19 earned" % d["earned"]`; `earned` is a field typed into `docs/total_inputs_scoreboard.json`, and "19" is in the format string while the file's observable list has 23 rows. |

So the headline figure is typed in three places and computed in none. The scoreboard is the right seed: its joints
are typed EARNED or BORROWED and a joint counts once. What is missing is that the count follows from them.

## 2. The proposal in one sentence

**One machine-readable graph from the foundation to every number the mathematics produces; the status of a value is
computed from its ancestry; the headline is printed from the graph and typed nowhere.**

## 3. The graph

**Nodes, by kind:**

| Kind | What it is | Its own status |
|---|---|---|
| foundation | an item of `GENESIS.md` §1–§4 | POSTULATED / CHOSEN / DERIVED, as `GENESIS.md` says |
| mathematics | an arc: a theorem, an exact computation, a numerical estimate | its grade (finding M1), lock tier (L1), domain and truncations (W-a, W-b) |
| identification | "this mathematical quantity is that physical quantity" — a row of `docs/IDENTIFICATION_LEDGER.md` | EARNED / UNEARNED / REFUTED |
| output | a dimensionless number the mathematics produces, with its precision | computed (section 4) |
| target | a measured dimensionless number, with source, value, uncertainty, scale and scheme | fixed in advance (section 5) |

**Edges:** `depends_on`, as the verdict files already carry.

Most of this exists in pieces: the arcs' `depends_on`, the scoreboard's joints, the identification ledger, the kind
table, the input-completeness ledger, the forcedness census. The proposal is to make them one file that a generator
reads, not a new ledger beside them.

## 4. How a value's status is computed (the weakest link)

The status of an output is the weakest status found anywhere in its ancestry:

- **DERIVED** — every ancestor is a foundation item or a mathematics node graded theorem or exact computation, with a
  recomputing lock that has passed the mutation rule; every identification on the path is EARNED; no ancestor is
  CHOSEN or FITTED; no truncation on the path is CHOSEN; no weave-domain node rests on a thread-domain node without a
  named lifting theorem.
- **CONDITIONAL** — as above except for a listed set of POSTULATED-beyond-the-foundation, CHOSEN or UNEARNED nodes.
  The list is printed with the value. This is today's "borrowed joints", computed instead of kept by hand.
- **FITTED** — any ancestor took a continuous value from data.
- **UNVERIFIED** — any ancestor has no recomputing lock, no script in tracked files, or no declared domain.

Nobody assigns these. Changing one node's status changes every descendant's on the next generation.

## 5. Two lists, kept apart: what the theory outputs and what is measured

The owner's "what if its more than 19 in our math" is the important case. 19 is a convention of the Standard Model
(massless neutrinos, one of the 19 a dimensionful scale), not a property of this mathematics.

- **The target list** is fixed in advance from an outside source and frozen: tier 1, the Standard Model's 18
  dimensionless parameters (the 19th is the unit, which no parameter-free theory derives); tier 2, the neutrino
  sector (three masses, three angles, one to three phases); tier 3, gravity and cosmology (the scale against the
  Planck mass, the cosmological constant). Under the owner's ruling of one self-consistent outcome, a theory of
  everything owes all three tiers. **The owner's decision (2026-11-10): the headline reports tier 1, with tiers 2 and 3 beside it.**
- **The output list** is whatever the graph's output nodes are. It may be longer or shorter than the target list.

Every pair then falls in one of four cells, and the headline is the four counts:

| | a target exists | no target yet |
|---|---|---|
| **the theory outputs a DERIVED number** | compared in a sealed test: **confirmed** or **refuted** | a **prediction**, registered with its precision before any measurement is consulted |
| **the theory outputs nothing** | **not reached** | — |

So the README line becomes, for example: *derived and confirmed 0 of 18 (tier 1) · refuted 0 · predictions registered
0 · conditional readings 6, on 13 borrowed joints*. More outputs than targets is not a problem; it is where the
predictions come from. Fewer DERIVED outputs than targets means something is still free.

## 6. The filter: what the graph admits

Three gates, each mechanical.

**(a) Admitting a node.** A mathematics node enters as verified only with a script in tracked files, a recomputing
lock that has passed the mutation rule, a declared domain and a truncation list. Otherwise it enters as UNVERIFIED
and every descendant inherits that.

**(b) Admitting an output as a value.** It is dimensionless; it is one number with a stated precision (an exact
expression or a computed interval), not a menu or a range; and its node exists, with its precision, before any
comparison is run.

**(c) Admitting a match.** This is the guard against coincidence, and it matters more as the output list grows: the
more numbers the mathematics produces, the more likely one of them lands near a measured value by chance.
- **The pairing is declared first.** Which output is which target is an identification node, registered before the
  output's value is computed. An output paired to a target after its value is known is a post hoc match, not a
  derivation.
- **The scale and scheme are part of the identification.** A measured mass or coupling runs with energy; "at what
  scale and in which scheme" is either derived or it is a CHOSEN node on the path.
- **The trial count is charged.** The number of output–target pairings that could have been declared is recorded, and
  the agreement must clear the bar after that many trials.
- **One uncertainty model per target**, fixed in the target list (finding V2).

## 7. Tests for the generator (planted violations)

| # | Planted change | The computed headline must |
|---|---|---|
| DG1 | set one ancestor of a reached value to FITTED | not count that value as derived |
| DG2 | add an output with an UNEARNED identification on its path | show it as conditional, with the identification listed |
| DG3 | change the typed sentence in `docs/MAIN_GOAL.md` to "1 of 19" | have no effect; the README is printed from the graph |
| DG4 | add an output paired to a target with no prior declaration | reject the pairing |
| DG5 | mark a thread-domain arc as the sole support of a weave-domain output | show the output as UNVERIFIED |
| DG6 | remove a node's lock | turn every descendant UNVERIFIED |

## 8. What it would print today

By the record's own statuses the generator would print zero derived, zero predictions, and frame A's six mass ratios
as conditional readings — the same position as now, but as a consequence of the graph. The first value that reaches
DERIVED would change the headline without anyone editing a sentence, and no sentence could change it otherwise.
