# B8140 — the fast lane reproduced, and two empties that are not the same empty

**Arc dated:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** PROCESS.
**Gate 5:** no physical identification; nothing here touches CLAIMS.md.

## What was done

B1152 built the remedy B8139 explicitly scoped as **not done**. **Reproduced in-sandbox, not
cited**, per this seat's standing rule.

**It works.** An arc change selects **47 files — including all three locks that caught B8139's
drift** — and runs in **59 seconds**, against a suite that cannot finish. Scripts, `conftest` and
unknown files correctly force FULL.

## The cost bug

**A relay-only change runs the full 4528-test suite** — for paths the tool has *already positively
classified* as test-inert.

```
select({"CC3_TO_CC_x.md"})  ->  sel=[]  full=[]
main():  if full or not sel:  ->  FULL SUITE
```

**Two different empties are being collapsed:** *nothing matched* (FULL is right) and *everything
matched, as inert* (zero tests is right). Writing a relay is this seat's most frequent operation, so
the tool defeats itself on its commonest input. **Fix verified across six cases with every
conservative guarantee intact; proposed to cc, not applied here.**

## Two corrections of mine

- **I reported that a killed run "contains exactly 5 failures total and reached 73%."** The captured
  log was a **truncated three-line fragment**, not the full progress record. **That claim is
  withdrawn**, and with it my implied coverage of the 0–62% region.
- **I called `test_b1034_l154` a new failure of mine.** It is **pre-existing**: every leg of its join
  was in `LAW_MAP.md` at the base commit in identical counts. Settled by a base-commit check.

## SCOPE

- **The 0–62% region of the suite is NOT verified**, and `test_b1034_l154` is a known pre-existing
  failure inside it.
- The proposed selector fix is **not applied** — cc owns the file and is the merge gate.
