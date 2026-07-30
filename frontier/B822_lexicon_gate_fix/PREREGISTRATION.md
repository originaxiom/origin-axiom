# B822 — PREREGISTRATION: the lexicon gate stops asserting a diagnosis it cannot support

cc banking seat, 2026-07-30. Sealed before the gate is edited. Repository-instrument scope.

## The trigger

Immediately after B821 banked, the gate fired at 22/21 and printed:

> *"the lexicon is ROTTING, not merely outgrown"*

**B821 had just refuted exactly that inference**, and the arc that pushed the count over was
**B821 itself** — a pure-instrument arc, which an *object* lexicon should not index. The gate is
emitting a claim its own inputs cannot support.

## What will change

1. **The metric is floored at `FINDINGS.md` ≥ 2000 bytes.** 14 of the 21 blind arcs are stubs of
   409–1988 bytes (*"Logged observation, not a claim."*) against a 4078-byte corpus median. No
   lexicon can reach them and none should try. This threshold is **objective and fixed here**.
2. **The "ROTTING vs outgrown" verdict text is REMOVED.** B821 showed count-plus-rate cannot
   distinguish lexicon decay from a shift in what the programme is doing. The gate will report the
   **numbers and the size decomposition** and leave the diagnosis to a reader.
3. The ceiling is reset to the size-floored count at this commit.

**Deliberately NOT done: hand-excluding "instrument arcs."** That classification is a judgement I
would be making about arcs I wrote, and excluding them would let me tune the number by relabelling.
Size is objective; topic is not. **The instrument arcs stay counted.**

## Two-outcome criteria, fixed before running

**SUCCESS** — both:
- the size floor removes **≥ 10** of the 22 blind arcs (i.e. thinness really is the dominant cause,
  as B821 claimed); **and**
- the floored count is **≤ 10**, small enough that a future rise means something.

**FAILURE** — either:
- the floor removes **< 10** → B821's decomposition overstated the stub effect, and the finding
  needs revisiting rather than the gate; **or**
- the floored count is **> 10** → the residue is too large to ratchet against, and the gate needs a
  different design, not a new threshold.

**On FAILURE the gate is left as it is** (with the ceiling raised by exactly the number of new arcs,
as an acknowledged debt) and the finding is recorded as unresolved. **Raising a threshold is not a
permitted response to a failed criterion here.**

## Pre-stated expectation

I expect SUCCESS: 14 stubs removed, leaving 8. Recorded so the outcome cannot be softened.
