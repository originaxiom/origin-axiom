# xB010 — PREREGISTRATION (sealed BEFORE the rule and its instrument are built)

**Seat `xb`, `sep16-branch`, 2026-09-17. Sealed, hashed and pushed before any code exists.**

## P0

Repository governance. No mathematics of the object, no value, no physics reading. Gate 5 absolute.

## The owner's instruction, 2026-09-17, verbatim in substance

> *"make rule to always sweep the repo to see if what you plan to do doesn't already exist. if it
> does, redo it anyway, because if it's negative it might be misinformed, bugged or wrongly done —
> verify verify."*

## Why the existing rule is not this rule

**B1202** already requires `scripts/checks/already_banked.py` before any MISSING/OPEN claim, and
the absence-sweep rule requires a complete sweep before an absence is even a finding. **Both govern
ABSENCE.** Neither says what to do when the sweep **finds** something — and in practice a hit is
read as *"already settled, move on"*. `already_banked.py`'s own output says **"read it BEFORE
writing MISSING/OPEN"**: read, not re-derive.

> **A banked result is currently treated as an ANSWER. The owner's instruction is that it is a
> HYPOTHESIS.**

The asymmetry that makes this urgent: **a wrong POSITIVE gets re-tested downstream because people
build on it; a wrong NEGATIVE is never re-tested, because it stopped everyone.** A bad kill is
silent and permanent. This session alone: **B742 revived 2 of 33** re-adjudicated kills; this seat's
own **xB005 Q3 was a wrong kill** caught only because the owner said *reverify*; **B146's
justification was wrong** though its kill survived; and this seat's one unverified acceptance
(*"the verification package FAILS"*) **was itself wrong** — its own missing dependencies.

## The rule to be written

**THE RE-DERIVATION RULE.** Sweep first. When the sweep finds something the planned work touches or
leans on, **re-derive it independently before accepting it** — own code where feasible, the
discriminating fact computed in-sandbox (extending **E4**, "compute the discriminating fact", and
**E3**, the stale-checkout false negative). **Priority: banked NEGATIVES that would stop the work.**
Then **declare** what was re-derived and what came back.

**CITE ≠ RE-DERIVE.** Reading an arc's conclusion and using it is citing. Re-deriving is computing
the discriminating fact again and comparing.

## Cells and two-outcome criteria — declared before writing any code

| cell | criterion | PASS | FAIL |
|---|---|---|---|
| **R1** | the rule is written where the standing rules live (`WORKING_RULES.md`) **and** registered in `docs/PRACTICES.md`, since this repo's own lesson is that *a self-declaration a gate reads beats a standing rule nobody reads* (B1226/B1231) | both present | either missing |
| **R2** | a **`rederived`** declaration in `arc_verdict.json`, and a gate that reads it. It must bind **NEW** arcs including this seat's own — a numeric cutoff cannot, because the seat prefix makes `xB009 → 9` | a frozen roster of existing arcs; any arc **not** in it must declare | it does not bind this seat's own next arc |
| **R3** | the present tree stays green | 34/34 → 35/35, 0 FAIL | it reds retroactively: the roster is wrong |
| **R4** | two-way selftest | an arc declaring nothing is caught; an arc with an honest declaration passes; **`NOT_RERUN` with a stated reason passes** — the rule must permit an honest refusal, or it will be satisfied by lying | either direction fails |
| **R5** | **this seat eats it first**: xB010 itself declares what it re-derived, and this arc re-derives at least one banked result it leans on | declared and re-derived | not — the rule ships unapplied by its author |

## Declared prior

All five PASS. **R4 is the one that could go wrong by design**: a rule that forbids saying *"I did
not re-run this"* does not produce re-derivation, it produces **false declarations** — the B1222
shape turned on ourselves, and the exact reason `identification-register` is a ratchet. The
declaration must make an honest **NOT_RERUN** cheap and a silent omission impossible.

## Scope and honest limit, stated before building

**"Redo everything" cannot mean all 1248 arcs.** The executable form of the owner's instruction is:
**redo everything the planned work touches or leans on, and declare anything you did not redo and
why.** That is faithful to the intent — nothing load-bearing is accepted unverified — and it is
affordable. The narrowing is stated here, in the seal, rather than made silently.

The gate enforces **completeness, never judgment**: it cannot tell whether a re-derivation was
real, only that the question was answered where a reader can find it. `creates_law` false.
