# xB014 ADDENDUM 1 (2026-09-17) — Z4's KILL IS WITHDRAWN: m004 is extremal three ways, and the error was mine twice over

**Beyond the seal.** `PREREGISTRATION.md` untouched (`bc8a71ed…`). Cells `Z6`–`Z7`, written after
the owner asked four words: **"u sure about extremality"**. **He was right.**

## The two errors in Z4

**1. I tested the wrong direction.** Kojima–McShane is a **lower** bound (`log λ / vol ≥ 1/(3π)`),
so "extremal" means the **smallest** ratio — closest to the bound. **Z4 ranked for the maximum.**

**2. I mis-read my own rank.** Z4 sorted **descending** and then reported the index as a rank.
*"m004's rank: 38 of 40"* was the **descending** index. **Ascending, m004 is rank 3** — and the two
"above" it are **m206 and s961, m004's own covers**, carrying the **identical** ratio by
construction (Z3 proved the ratio is constant along the tower). So m004 was never near the bottom;
it was **at the minimum**, tied only with itself.

**And Z4 never tested the components at all** — which is where the extremality actually lives.

## What is true

| ranked ascending over 40 once-punctured-torus bundles | m004's rank |
|---|---|
| **dilatation** `log λ` | **1 of 40** |
| **volume** | **1 of 40** |
| **ratio** `log λ / vol` | **minimum**, 0 strictly below, tied only with `m206`, `s961`, `t12839` — its own tower |

**m004 is extremal three ways.** And the dilatation minimum is **forced**: trace 3 is the smallest
possible for a pseudo-Anosov in `SL(2,ℤ)`, so `λ = φ²` is the floor, not a coincidence.

> **Z4's verdict is WITHDRAWN. Path A is NOT killed by the base rate.**

## But the honest scope, which Z4 reached for the wrong reason

* **Minimal dilatation** on the once-punctured torus is a **known theorem**, and here it is forced
  by trace 3 being the minimum pseudo-Anosov trace.
* **Minimal volume** is **Cao–Meyerhoff**, already banked.
* **B207 already said it**: *"golden has the smallest regulator (log φ) → the least-hierarchical /
  extremal point."*
* The **ratio's** minimality **follows from the components'**, so it is a consequence, not an
  independent fact.

**So the extremality is real, my kill was wrong, and the extremality is also already in the record.**
Path A stands reopened but un-advanced: it still does not cross B1012's wall, which concerns a
**dimensionful** quantity, and a ladder supplies a dimensionless **index**.

## The standing lesson

This is the second time in one session that **a sort order or a rank convention produced a false
verdict** (the first was xB007's `b++`-only search, caught by a declared prior). **A kill that rests
on a ranking must state the direction and show the head of the list, not an index.** The head of
the list is in Z6 and Z7 now, where a reader can check it.

**Provenance.** `verification/extremality_recheck.py` (Z6–Z7) → `reproduce.sh`. Re-derives B207's
extremality statement, Cao–Meyerhoff, and the minimal-dilatation bound.
