# B1123 — THE FORCEDNESS CENSUS (harvest, verified on this bench): 39 of 43 chain-links are FORCED; the stretch from the knot to the algebra is AXIOM-FREE

**Status: banked (frontier). Verdict PROVED (a map-level census, regenerated from
`docs/THEOREM_LEDGER.md` by a drift-failing checker; verified on this bench — reproduces
against current main, and FAILS on drift, non-vacuously). Harvest (cc3 branch
`audit/b775-braver-questions`, commit 27d9ceb9; owner-directed "we proved it over and over
and somehow we lost it"). Lock `tests/test_b1123_forcedness.py`. creates_law.**

## The question the owner posed

"We proved it over and over and somehow we lost it, and we present it as choices — even E₆
is presented as a choice." The forcedness was never written as ONE fact: it lived
distributed across 43 link-labels in `docs/THEOREM_LEDGER.md`, so a reader meets Part 0's
"three declared choices" and never learns how much is forced. Prose rots; a checker does
not.

## THE CENSUS (regenerated, not recalled — verified this bench)

`scripts/checks/forcedness_census.py` parses the ledger's 43 links and counts labels:

```
THEOREM 26 · IDENTITY 6 · NO-GO 5 · AXIOM 4 · COROLLARY 1 · CENSUS 1
FORCED (non-axiom): 39 of 43     axioms at: [3, 4, 5, 18]
axioms in C6..C17 (the knot -> the algebra): NONE
```

> **39 of 43 links are FORCED. Between the object and the algebra there is not one
> declared choice.** The four axioms are **C3, C4, C5** — inexhaustible description, the
> geometric carrier, orientation, **all BEFORE the knot** — and **C18**, the observer's
> closings, in the measurement layer **after the algebra is already in hand**.

## THE DOORWAY IS THREE THEOREMS, NOT A SELECTION

The hearing sits at congruence level **15**; then, by theorem only: 15 = 3·5 coprime ⟹
SL(2,ℤ/15) ≅ SL(2,3) × SL(2,5) (CRT); SL(2,3) ≅ 2T, SL(2,5) ≅ 2I; McKay: 2T → **E₆**,
2I → **E₈**. **E₆ is not chosen — it is what level 15 factors into.** (Group theory
CITED-standard: CRT, the SL(2,·) isomorphisms, McKay; orders 24/120 computed.)

## VERIFIED ON THIS BENCH (verify-don't-trust)

- The checker RUNS against current main's `docs/THEOREM_LEDGER.md` and returns
  **39 of 43, PASS** — the census is a property of the actual bank, not the branch.
- **Non-vacuous (MB12):** relabelling an in-stretch THEOREM → AXIOM trips **three**
  independent alarms (census drift · axiom-set drift · AXIOM-FREE STRETCH BROKEN) and exits
  1; an **unparseable ledger FAILS** rather than passing (empty ≠ null). The criterion can
  pass AND fail — it is a real gate.

## The honest boundary (carried)

C3/C4/C5 are real choices, upstream of the substitution. "The whole chain needs no choices"
overshoots by three; **"from the substitution to E₆ nothing is chosen" is exact** — and it
is the stretch that does the work. Reaching E₆ is separately GENERIC (~1 in 3 manifolds,
5 of 7 grammars, B993/B996), so arrival there confirms nothing: **forcedness and
discriminating power are different claims; this census makes only the first.** The doorway's
E₆-sits-inside-C6..C17 placement rests on the chain document's part ordering (flagged, not
hidden).
