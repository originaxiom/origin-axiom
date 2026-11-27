# The claim card (from 2026-11-24, at the author's word)

Every result a seat wants to bear on main's picture arrives as one claim card: a short file at
`relays/claims/CLAIM_<date>_<short_name>.md` on the seat's own branch. Everything else a seat pushes is registered by
name in bulk and is not read line by line. Main's intake script (`scripts/checks/seat_intake.py`) finds the cards,
sorts them, and flags what main already holds.

Copy the block below. Keep each field to one or two lines. A field that does not apply says "none".

```
# CLAIM CARD — <the result in one line>

- card id: new | refiles Q<nnnn>
- seat code: <the seat's neutral code, fam<n>-v<n>-<effort>-<nn>; never a name>
- seat, branch, commit: <the seat code>, <the branch>, <the full 40-hex commit>
- kind: theorem | computation | prediction | identification | negative
- touches: <codes from docs/TOTAL_INPUTS_SCOREBOARD.md (A01 to A12, F1 to F4, S01 to S03, LAMBDA), identification rows
  (I-n), register rows (P-n), or one of the 19 parameters by name>
- effect: removes | conditions | adds | supports | refutes — <on which code>; none when it touches none
- scope: frame: <the frame>; object: <the object>; reach: single | class | general; hypotheses: <each, or none>
- identifications: <each "X here is Y there" the claim makes, or the I-n rows; or none>
- definitions: <the definitions of the objects the claim uses, in words or formulas, so that it can be checked from the
  card alone; or none>
- imports: <every structure or assumption from outside the record it rests on, each named: for example "the MSSM's
  two-loop running", "M-theory flux quantisation", "three right-handed neutrinos">
- premises on main: <arcs and register rows it uses>
- decisive script: <path>, SHA-256 <first 16 hex>, depends on <only the standard library, mpmath, sympy, numpy, scipy,
  python-flint, sage, GAP>,
  run as <command>, output SHA-256 <first 16 hex>[, heavy]
- decisive lines: <n> lines marked "DECISIVE:", SHA-256 <first 16 hex of those lines, as the rerun normalises them>
- failing control: <a command, not the decisive one, that must exit with a failure if the result is wrong>
- second computation: <which seat, with code that shares nothing, its path, and whether it agrees>
- already on main?: <the topic-sweep line you ran on main, and the closest arc>
- what would make it fail: <one control that must fail if the result is wrong>
```

**The four fields added on 2026-11-26** (the framework's draft 1, § 9, agreed by the author; register row P-885; the thin
path's patch T2): the card's id, the seat's code, the decisive lines and the failing control. The intake runner checks the
form with `scripts/queue/card_form.py` before anything else. Only `imports`, `premises on main` and `second computation`
may say "none". **[CHANGED 2026-11-26 (T1b, main's M56 and M58):** `scope` and `identifications` added (door rule D1), and `definitions` (main's M60), which may say "none";
`touches` and `identifications` may say "none", and `effect` too when `touches` does; a card may declare its decisive
script heavy, which only adds work.**]** The allowed packages gain python-flint, sage and GAP (main's change of § 9; their pinned versions are
the rerun's).

## How main takes a card

**[NOTE 2026-11-26 (P-885):** this section stands until the framework's trial runs; the intake, the peer stage and the two
banking seats of the draft then take its place, and it is written again.**]**


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
