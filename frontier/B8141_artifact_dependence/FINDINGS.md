# B8141 — the artifact class: a lock that reads a gitignored file reports on the machine

**Arc dated:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** PROCESS.
**Gate 5:** no physical identification; nothing here touches CLAIMS.md.

## The finding

**Two locks depend on six `.log` files that `.gitignore` forbids the repo from ever carrying.**

| test | gitignored artifacts it reads |
|---|---:|
| `test_b1062_bridge.py` | 5 |
| `test_b1063_refresh.py` | 1 |

`.gitignore:20` is `*.log`. So these tests **assert a property of the author's working directory**,
not of the code. On any clean checkout they **do not skip — they fail**, and two of them are failing
here right now with `FileNotFoundError`.

> **A permanently red lock trains its readers to ignore failures. That costs more than the lock was
> ever worth.**

## Third class in a series

| arc | class | shape |
|---|---|---|
| B8139 | **cost** | the lock works, but is never **reached** |
| B8140 | **two empties** | the selector proves *0 affected*, then runs everything |
| **B8141** | **artifact** | the lock **is** reached, and reports on the **machine** |

The distinction from the cost class matters: every remedy for "never reached" is useless here,
because these locks run fine — they are just answering the wrong question.

## ⚠ My instrument failed first, and reported a clean bill

**The first version of this scan matched only whole repo-relative paths written as a single string
literal.** The tests build their paths from fragments (`ROOT / "frontier" / name`), so the scan
**missed the very files that motivated it** — it printed *"0 gitignored"* while two such tests were
failing three metres away.

**Fixed** by matching basenames and indexing every file actually present. **Hardened** with a
positive control naming two independently-confirmed absent files: `scripts/checks/artifact_dependence.py`
**exits non-zero if it cannot see them**. *A scan that cannot detect a known-missing file is not
evidence of absence.*

## Deliberately not in the finding

`AUDIT_B1076_ONE_NOTATION_DEFECT.md` and `I_WAS_WRONG_THE_REAL_DEFECT.md` are absent but **not**
gitignored. This corpus keeps cross-seat relay files untracked on purpose — the ledger is the
register — and the index lock asserts those *names appear in the index text*, not that the files
exist. **Reported separately rather than folded in, because inflating a finding with legitimate
cases is how a real one stops being believed.**

## SCOPE

- **Nothing here says B1062/B1063's results are wrong.** Only that their locks cannot verify them on
  a clean checkout.
- **No remedy applied.** Commit the artifact under a non-ignored name, regenerate it in the test, or
  skip explicitly — all are judgements for the arcs' owner.
