# The claim card (from 2026-11-24, at the author's word)

Every result a seat wants to bear on main's picture arrives as one claim card: a short file at
`relays/claims/CLAIM_<date>_<short_name>.md` on the seat's own branch. Everything else a seat pushes is registered by
name in bulk and is not read line by line. Main's intake script (`scripts/checks/seat_intake.py`) finds the cards,
sorts them, and flags what main already holds.

Copy the block below. Keep each field to one or two lines. A field that does not apply says "none".

```
# CLAIM CARD — <the result in one line>

- seat, branch, commit:
- kind: theorem | computation | prediction | identification | negative
- touches: <codes from docs/TOTAL_INPUTS_SCOREBOARD.md (A01 to A12, F1 to F4, S01 to S03, LAMBDA), identification rows
  (I-n), register rows (P-n), or one of the 19 parameters by name>
- effect: removes | conditions | adds | supports | refutes — <on which code>
- imports: <every structure or assumption from outside the record it rests on, each named: for example "the MSSM's
  two-loop running", "M-theory flux quantisation", "three right-handed neutrinos">
- premises on main: <arcs and register rows it uses>
- decisive script: <path>, SHA-256 <first 16 hex>, depends on <only the standard library, mpmath, sympy, numpy, scipy>,
  run as <command>, output SHA-256 <first 16 hex>
- second computation: <which seat, with code that shares nothing, its path, and whether it agrees>
- already on main?: <the topic-sweep line you ran on main, and the closest arc>
- what would make it fail: <one control that must fail if the result is wrong>
```

## How main takes a card

- **Tier A** applies when a card's effect removes, conditions or refutes a scoreboard code or one of the 19.
  - Main reproduces the decisive script in a sandbox: the author's ruling of 2026-11-24 allows a sealed,
    dependency-free script to be run there.
  - Main then re-derives the decisive step with its own code.
  - If both hold, main lands one arc and changes the scoreboard row, naming every import as a hypothesis.
  - Running the seat's script counts as reproduction, not verification. The verification is main's own computation.
- **Tier B** applies when a card supports a code.
  - It is taken on the second computation by another seat.
  - Main reproduces one decisive number in the sandbox and records the card on the register.
- **Tier C** covers process work and anything that touches no code. It is registered by name only.

A card without a second computation waits in Tier B or C until it has one. A card whose script cannot run sandboxed
(network, local paths, outside packages) is read, not run, and goes to the back of the queue.
