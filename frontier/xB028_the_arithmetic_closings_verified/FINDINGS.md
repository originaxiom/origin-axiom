# xB028 — THE ARITHMETIC CLOSINGS, VERIFIED FROM A SECOND BENCH; B288's LOCK DIAGNOSED AND LEFT FOR ITS OWNER

**Date:** 2026-09-18 · **Seat:** `xb` · **Branch:** `sep16-branch` · **Verdict: PROVED**

**A second-bench verification, NOT a sealed prediction.** `PREREGISTRATION.md` declares in full that
the checks were run as the incoming correction was read. **No kill condition is claimed.**

---

## WHAT WAS RELAYED, AND WHAT THIS BENCH CAN CONFIRM

A seat on the paper lane reported that main's sentence — *"of the grid's 78 closed hyperbolic
fillings, zero keep `ℚ(√−3)` and zero are arithmetic"* — is **false in its second half**, that
**B718** (July) already found three arithmetic fillings by the **cocompact** criterion, and that the
correction never propagated. That seat was mid-repair (**B1376**) when it stopped.

**A1 — invariant trace fields, computed here under the xB024 height guard:**

| manifold | this bench | relayed |
|---|---|---|
| **m003(−3,1)** (Weeks) | **cubic, disc −23**, 1 real root, 1 complex place | **positive control — textbook value, PASSED** |
| **m004(6,1)** | **cubic, disc −59**, 1 real, 1 complex place | cubic, (1,1), disc −59 ✓ |
| **m004(8,1)** | **cubic, disc −31**, 1 real, 1 complex place | cubic, (1,1), disc −31 ✓ |
| m004(5,1) | **UNDETERMINED** | quartic, (2,1), disc −283 |
| m004(7,1) | **UNDETERMINED** | sextic, (2,2) |

**Two of the three claimed arithmetic fillings are confirmed with exact discriminants**, and the
**Weeks manifold reproduces its textbook `−23`** as a positive control.

**The precision ceiling is stated, not hidden.** This instrument uses SnapPy's **quad-double**
holonomy; the lane's **1000-bit polished** holonomy is not available here. The quartic and the
sextic fall outside the guard and are reported **UNDETERMINED — never guessed.**

## A2 — THE LOAD-BEARING HALF, CONFIRMED WITHOUT COMPUTING ARITHMETICITY AT ALL

Every field this arc **determined** is excluded from containing `ℚ(√−3)` **twice over**:

1. `[ℚ(√−3):ℚ] = 2`, so any field containing it has **even** degree. **A cubic cannot** — 2 ∤ 3.
2. `ℚ(√−3)` is imaginary quadratic. If `σ : K → ℝ` is a **real** embedding and `ℚ(√−3) ⊆ K`, then
   `σ(√−3)` is a real number squaring to `−3`. **Impossible.** All three determined fields have a
   real embedding.

> **The relayed conclusion — *"no closing carries the selecting field"* — is CONFIRMED where it
> could be checked, and confirmed INDEPENDENTLY OF ARITHMETICITY.** The load-bearing half of main's
> sentence survives; only its arithmeticity clause is false.

## A3 — B288's LOCK: DIAGNOSED PRECISELY, DELIBERATELY NOT REPAIRED

```python
def test_no_closed_filling_is_arithmetic():
    assert b288.N_ARITHMETIC == 0    # none imaginary-quadratic; arithmeticity lost on closing
```

**The comment contains the bug.** *"None imaginary-quadratic"* is the criterion for a **cusped**
group. A **closed** filling must be judged by the **cocompact** criterion (Maclachlan–Reid 8.3.2:
one complex place, integral traces, invariant quaternion algebra ramified at every real place).

- **The test's NAME asserts something FALSE.**
- **What it actually verifies** — no closed filling has an **imaginary-quadratic** invariant trace
  field — **is TRUE**, and is exactly the load-bearing half A2 confirms.

**A test that certifies a falsehood is worse than no test**, so this is recorded as a **live
defect**. **It is NOT repaired here.** B1376 on the paper lane is that seat's active repair, and
duplicating it would be precisely the collision this record has already been bitten by (the B1267
renumber). **Flagged, not taken.** For the same reason this arc **touches no shared ledger** —
no error class is minted, no lead registered, no lock edited.

---

## WHAT THIS ARC MAY NOT BE READ AS

It does **not** establish the three fillings arithmetic on its own authority. **Arithmeticity needs
the cocompact criterion, which this arc does NOT compute** — it verifies **trace fields**, a
necessary ingredient and not the whole criterion. The arithmeticity claim rests on **B718** and on
the lane's own re-decision, not on this bench.

**Axes held fixed and named:** five manifolds only, not the 78-slope grid · trace fields only, not
the quaternion algebra · quad-double precision, with the ceiling stated and two targets undetermined.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**
