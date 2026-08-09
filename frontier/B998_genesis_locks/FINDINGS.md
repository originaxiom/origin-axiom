# B998 — the axiom chain's locks do not lock it: a cited test that does not exist, and three claims unlocked

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository governance. Gate 5 untouched.
**Source:** cc3's genesis-stratum audit (B1–B100). **Verified mechanically here before acceptance.**

---

## The defect, verified

| | |
|---|---|
| forks **tested** in `tests/test_b749_genesis_forks.py` | **F4, F5, F6, F7** |
| forks **cited** beside that file in `THEOREM_LEDGER.md` | **F3, F4, F7** |
| **cited but absent** | **F3** |

`THEOREM_LEDGER.md` line 28, verbatim: *"— P019 T4 (v2, the unified form). Lock:
`tests/test_b749_genesis_forks.py` (**the F3+F7 controls**)."*

> **There is no F3 test.** The ledger names a control that does not exist.

And cc3's fuller reading, which the mechanical check corroborates: **there is no F2 test — C3's only
real price — and no F8 test — C4's entire price.**

> ### **C1, C2 and C4 are effectively UNLOCKED. C3 is locked only by a fork (F4) that prices a different axiom.**

## Why this is the day's most serious governance finding

The programme's whole claim to rigour is that **every load-bearing statement carries a lock**. These
are not ordinary statements — **C1–C4 are the axiom chain**, the steps from *minimal description* to
*the object*. They are the foundation everything else stands on, and **their locks are a citation to
a file that tests four different things.**

**It is the B982 failure class exactly** — *a citation whose target does not contain what is claimed*
— but where B982 found it in a **gate's exemption list**, this finds it **in the theorem ledger, on
the axioms**. Same shape, worse location.

**And it is invisible to every existing gate.** `chain-locks` checks that a lock **file exists**;
nothing checks that the file **tests the thing cited**. A test-file citation is exactly as weak as
B982's audit-trail citation was, and for the same reason: **nobody grepped the target.**

## Scope, stated honestly

- **The claims are not thereby false.** C1 (Morse–Hedlund) and C2 (Hurwitz/Lagrange extremality) are
  **classical theorems, cited not re-proved** — cc3 grades them PROVED and notes they *"do all the
  work"*. Their truth does not depend on our test file.
- **What is false is the ledger's assertion that they are locked here.** An unlocked classical
  theorem is fine; **an unlocked claim recorded as locked is not**, because the next reader takes the
  lock at face value.
- **The genuinely unlocked-and-not-classical items are the PRICES:** F2 (C3's) and F8 (C4's). Those
  are this programme's own computations, and they are the ones whose absence matters.

## The correction applied

1. **`THEOREM_LEDGER.md`**: the F3 citation is corrected — the file's actual coverage (F4–F7) is
   stated, and **C1/C2/C4 are marked as carrying no in-repo lock**, with the honest reason (classical
   for C1/C2; price-untested for C3's F2 and C4's F8).
2. **A gate is not added here, deliberately.** Checking that a cited test *tests the cited thing*
   requires parsing intent, not filenames. **The honest instrument is the decadal review's room
   reading** (`BANKING_PROTOCOL` Part III, room *claims*: *"is anything here … scoped wider than its
   arc proved?"*), and this arc is the first entry answering it.

---

**Verdict: the axiom chain's locks are cited, not present.** The claims stand on their classical
sources; the **record** overstated their in-repo verification, and the two prices that are genuinely
ours — **F2 and F8** — are untested. **That is the owed work, and it is now named rather than
implied.**
