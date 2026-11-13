# cld-advisor · C19 · a negative without a second computation is provisional, held by a gate

*Main's card in M29, first in the seat's order (the author's instruction after B1918; WORKING_RULES' rule of 2026-11-13,
register row P-842). Committed before any work of it.*

## 1. The question

The rule of 2026-11-13 says a NEGATIVE verdict is banked only after an independent second computation, named in the
verdict file's `cites_seat` by the words "second computation"; until then its verdict line says PROVISIONAL. After every
wall, the arc's page carries a section "What the wall teaches". Main applies this by hand at every landing; the rule's
"Enforced by" line names this card as owed.

## 2. What is delivered, and what done means

| | |
|---|---|
| the gate | from B1923 on, a verdict file whose verdict is NEGATIVE fails unless an entry of its `cites_seat` names a second computation, or its verdict line carries PROVISIONAL; and it fails if the arc's FINDINGS has no heading "What the wall teaches" |
| its failing paths | a test with planted verdict files, registered in `tests/GATE_CONTROLS.json` as every gate's control is |
| the register of practices | a section for the gate, as the practice-register gate asks |
| done | one patch on main's head; every gate passes on a clean checkout of it but the count of landings; the new test passes, and fails on the tree before the patch |

## 3. How it could come out wrong, written before any run

1. **An entry that names a second computation only as owed** ("a second computation is assigned to agy-002") would
   satisfy a plain search for the words. Such an entry is not counted: the gate reads the words that say the computation
   is not yet made (owed, assigned, pending, not yet, awaited, to come), and the test holds one such entry, with its twin.
2. **The verdict line** is the verdict file's `claim_one_line`, as the record's other gates on verdict lines read it; the
   word PROVISIONAL is read there in capitals, as the rule writes it.
3. **The arcs before B1923** are not read: the rule binds from its own day on. The test plants one below the line.
4. **A FINDINGS page missing** fails, as a page without the section does.
5. **The gate reads what is written**, not whether the second computation is independent: that stays main's to judge.

## 4. What it rests on, and what it must not touch

- Main's head `417a64e72` and WORKING_RULES' rule of 2026-11-13. No verdict file, FINDINGS page or test of main's is
  changed; no mathematics is stated.

## 5. One control that must fail if the work is broken

A NEGATIVE verdict file of an arc numbered B1923 or above, with no second computation named and no PROVISIONAL in its
verdict line, must turn the gate red.

## 6. What is needed from main

Nothing to start.
