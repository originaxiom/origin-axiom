# B1202 — THE ALREADY-BANKED CHECK: the finished-but-forgotten class gets an instrument, not a promise

**Status: banked (frontier). Verdict PROVED** (the instrument, with two-sided controls over the four
real historical failures and two genuine blind regions). `verification/reproduce.sh` → `REPRODUCES`.
Gate 5 clean.

## Why

The owner's standing instruction is that *"we don't have X" is never terminal*. It was violated
**four times**, each time the same way: a **register** row said open and the **corpus** already held
the proof.

| the claim made | what actually existed | how long it stood |
|---|---|---|
| "QP-1 (the quine) open" | **B762** had proved it | months |
| L187: "none has been executed" | **B767** had run six of seven | ~5 weeks |
| "the F2/F8 locks are missing" | **B1003** had banked them | ~3 weeks |
| R5: "the proof is a NAMED OPEN STEP… no successor" | **B775/B778** proved it all-p | ~5 weeks |

Every one of these would have been caught by *searching the corpus instead of reading the register*.
Review 52 raised the class to a standing audit item; **an audit item is not an instrument.** This is
the instrument.

## What it is

`scripts/checks/already_banked.py` — given the terms of a claim, it scans **every**
`frontier/*/arc_verdict.json` and every nested `FINDINGS.md` (the cell-level files where B775/B778
lived, which arc-level scans miss), ranks by term coverage, and **exits non-zero if any arc in a
settled state (PROVED / NEGATIVE / RESOLVED / RESOLVED-A / THEOREM / RETRACTED) matches a real share
of the query.**

**The threshold is the design's load-bearing part.** A first version flagged any settled arc sharing
one incidental word — which would have fired on everything, and *an instrument that cries wolf gets
ignored*, which is precisely how the four misses happened in the first place. The rule is now
`matches ≥ max(2, ⌈terms/2⌉)`.

## The controls, two-sided

**Positive (must flag)** — all four real historical misses: the quine, the depth-closure
stabilizations, the genesis locks, the dark-hyperbola proof. **All four flagged**, each surfacing the
exact arc that was missed, at top rank.

**Negative (must stay silent)** — two regions the existence audit established as genuinely blind:
*inflation / reheating / e-folds* and *dark matter / relic abundance / freeze-out*. **Both clean**
(0 settled arcs above threshold), so a MISSING claim there remains admissible.

An instrument that only fired would be useless; this one discriminates.

## The rule it enforces

Added to `WORKING_RULES.md`: **no MISSING / OPEN / "never run" / "no successor" claim is admissible
until `already_banked.py` has been run on its terms, and the searched terms are stated with the
claim.** Folded into the review checklist beside VERIFY-THE-VERIFIER.

## Fences

The check is a *retrieval* aid, not an adjudicator: a flagged hit means **read that arc before
writing "missing"**, not that the claim is wrong. Term matching is lexical, so a claim phrased in
vocabulary absent from the corpus can still slip — the check reduces the class, it does not abolish
it, and the honest response to a clean result is "no settled arc matched *these terms*", which is
what the tool prints. No firewall crossing; no measured value.

## An artifact found by the controls themselves (recorded, not hidden)

Writing this arc **broke its own negative control**: the FINDINGS and verdict quote the control
phrases ("dark matter relic abundance freeze-out") verbatim, so the check began matching **its own
documentation** and reported a settled arc for a region the audit proved blind. A self-documenting
instrument pollutes its own index. Fixed with `--exclude=`, used by this arc's controls and lock;
the artifact is recorded because the same trap waits for any future instrument that names its test
cases in prose.

