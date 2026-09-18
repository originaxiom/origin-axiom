# xB026 — THE GENERATION COUNT'S INPUTS MOVE UNDER A5; THE COUNT ITSELF IS NOW SHARPLY OPEN

**Date:** 2026-09-18 · **Seat:** `xb` · **Branch:** `sep16-branch` · **Verdict: PROVED**

**PREREGISTRATION sealed `4ae71e2987b073a8…`, committed and pushed at `7d97a302` BEFORE
`verification/` existed**, with a **binding kill condition** on G2 and — written before the data —
**G5's fence on what a moved locus may not be read as.**

---

## THE RESULT

The question: **xB021/xB022 split the object's invariants into two species — which does the
generation count belong to?** B1375 finds **one net generation on every one of 80 800 backgrounds**
of the object's tower, never three. Does **A5** move it?

**DECIDED: the census's own INPUTS are not stabiliser-fixed. They move at every level.**

| n | `b++(LR)ⁿ` — the object's tower | `b+-(LR)ⁿ` — its A5 image | `H₁` differs | B1374's `N` |
|---|---|---|---|---|
| 1 | `ℤ` | `ℤ ⊕ ℤ/5` | ✔ | 12 → 60 |
| 2 | `ℤ ⊕ ℤ/5` | `ℤ ⊕ (ℤ/3)²` | ✔ | 60 → 12 |
| 3 | `ℤ ⊕ (ℤ/4)²` | `ℤ ⊕ ℤ/2 ⊕ ℤ/10` | ✔ | 12 → 60 |
| 4 | `ℤ ⊕ ℤ/3 ⊕ ℤ/15` | `ℤ ⊕ (ℤ/7)²` | ✔ | 60 → 84 |
| 5 | `ℤ ⊕ (ℤ/11)²` | `ℤ ⊕ ℤ/5 ⊕ ℤ/25` | ✔ | 132 → 300 |
| 6 | `ℤ ⊕ ℤ/8 ⊕ ℤ/40` | `ℤ ⊕ (ℤ/18)²` | ✔ | 120 → 36 |

**6 of 6. The kill condition did not fire.** `H₁` moves, the torsion exponent moves, and therefore
**B1374's own character modulus `N = lcm(12, exponent)` moves at every level** — so the loci and
character groups the census is built from are different objects on the sister's tower.

**NOT DECIDED — and the seal said so before the data.** *"One per background"* could survive on
different loci, which would make **one** the invariant and the backgrounds merely the orbit.
**This arc does not read a moved locus as a moved count.**

---

## THE CELLS

**G1 — scaffolding, by isometry signature and not by volume** (a volume coincidence is exactly how
this record's sister pair arose). `b++(LR)ⁿ` for `n = 1…5` reproduces **m004, m206, s961, t12839,
o10_150696** — **B1375's `Y₂…Y₅` and xB013's Y2, independently.** 5 of 5.

**G2 — the deciding cell.** `H₁` exact on both towers, **6 of 6 DIFFER**, 0 errors, with a positive
control (`H₁(m004) ≠ H₁(m003)`) proving the comparator can see a difference.

**G3 — the census inputs.** `N` moves at **6 of 6** levels.

**G4 — the attempt, declared in the seal as one that may not land, and it did not.** The branch's
index instrument (`main_r27_exact_lift.py`) is written for **2 generators / 1 relator over ℚ(u)**;
every cover above has a **(3, 2)** presentation. Computing the index here needs a **generalised**
instrument (arbitrary presentation, arbitrary cyclotomic field) that **this arc does not build**.
**Reported as not landing.**

**G5 — the fence, written before the data.** See above.

## G6 — BEYOND THE SEAL, LABELLED: three cross-checks, run rather than asserted

`|Tor H₁|` on `b++(LR)ⁿ`: **1, 5, 16, 45, 121, 320** · on `b+-(LR)ⁿ`: **5, 9, 20, 49, 125, 324**

1. **xB022's `+4` law EXTENDS to the tower.** Shifts `[4,4,4,4,4,4]` — constant. xB022 measured it on
   words of length ≤ 8; `(LR)⁶` has length **12**, so this extends the law rather than repeating it.
2. **The record's own Alexander-module numbers are reproduced.** `THEOREM_REGISTRY`'s
   `T-PERIOD-2-INVERTS-THE-ALEXANDER-MODULE` records `|Tors| = 5, 16, 45, 121, 320` for `n = 2…6`.
   **This arc's `b++` tower gives exactly that**, from SnapPy homology alone, with no Fox calculus.
3. **B1374's and B1375's own moduli are reproduced independently.** B1374 runs `Y₄ = t12839` at
   **`N = 60`** — computed here: **60**. B1375 re-derives `Y₅` over **ℚ(ζ₁₃₂)** — computed here:
   **`N = 132`**. Two independent confirmations of the lane's arithmetic from this branch.
4. **An observation, and explicitly not a claim.** Square `|Tor|` occurs at levels **1, 3, 5** on the
   object's tower and **2, 4, 6** on its A5 image — **they alternate**. Square torsion is necessary
   for a free orientation-reversing involution on **closed** manifolds (xB023's reading of Kawauchi
   I + III); **these covers are cusped, where xB023 MEASURED that the same predicate fails 590 of
   1260 times.** **No inference is drawn, and none may be.**

---

## WHAT THIS DOES NOT DO

It claims **no** generation count, promotes nothing to physics — **B1374/B1375 fence themselves
identically and this arc inherits the fence.** It does not re-derive the SM frame, which lives on
the lane. **It supplies no value.**

**The question is now sharp and bounded, which is the deliverable:** *run B1374's SM-frame census on
`b+-(LR)ⁿ`.* If it also gives one per background, **one** is the invariant and the count is
stabiliser-fixed — a theorem-shaped negative. If it gives something else, the count is orbit-
structured like `CS` and `H₁`, and **the family, not the object, is where to look.**

**Axes held fixed and named:** both towers to `n = 6` · `H₁` and the census inputs only, the index
**not** computed · the SM frame **not** reproduced · G6 is beyond the seal and labelled.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**
