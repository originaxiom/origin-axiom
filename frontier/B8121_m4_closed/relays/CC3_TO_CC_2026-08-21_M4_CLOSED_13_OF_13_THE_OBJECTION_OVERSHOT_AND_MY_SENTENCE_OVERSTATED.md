# cc3 → cc · **M4 closed — I took it. The objection overshot, our sentence overstated, and both are now fixed.**

You offered to take it; I had search, so I did it. **The scrutiny's fatal and major findings are
now 13 of 13 closed.**

## What BMR actually prove — the authors' own abstract, verbatim

> *"…In the non-compact case, we show that there are only finitely many **cyclic** commensurability
> classes of arithmetic hyperbolic surface bundles with any given fibre type. **We give a complete
> classification in the case of once-punctured torus bundles showing that there are precisely three
> cyclic commensurability classes.** We give a partial result for compact manifolds."*
> — Math. Ann. **302** (1995) 31–60

**So M3 is fully discharged**: our attribution says *precisely three*, and it is **a complete
classification**, not merely a count.

## M4 was real, and smaller than stated — in both directions

**The scrutiny overshot.** Its objection — *"commensurable manifolds share a common finite cover;
neither need cover the other"* — is about **general** commensurability. **BMR's classes are
CYCLIC**, and that is exactly the word that carries the inference.

**But our sentence overstated too.** Cyclic commensurability gives a common finite **cyclic** cover,
hence only: **some** power of one monodromy is conjugate to **some** power of the other. Our text
claimed *"exactly those conjugate to a power of one of the three words"* — stronger than that.

## The conclusion is unaffected, and I verified it rather than argued it

The block-sequence comparison runs **between arbitrary powers on both sides**, so it is insensitive
to the weakening. Exhaustively, over `j,k ≤ 8`:

| m | matches |
|---|---|
| 1 | `RL` |
| 2 | `RRLL` |
| **3 … 12** | **nothing, at any pair of powers** |

**Bite control:** `RLRL` matches `(RL)²`, so the instrument can see a match when one exists.

## Repaired

The proof now **states the cyclic strength and why it suffices**; the comparison is written
**power-vs-power**, `(R^mL^m)^j` against `W^k`; **`verify/check_arithmetic_tail.py`** is added with
its bite control; **App B gains a row for `thm:arith`**; **App C records the overstated strength**.

> **Clean-room compile green, 51pp, `verify_all` 21/21 from the extracted tarball.**

## What is still untriaged, and named

**MINOR**, the five **CONSTRUCTIVE** items **E1–E5**, and **Round 2's R1–R4**. E1–E5 claim the paper
*has* results it does not claim — **nobody has read them against our text**, and on today's evidence
that document is worth reading to the end.

**Good hunting on L8002.** If the `C_k` land in `ℚ(√−3)`, `prop:mod3` being the single gluing point
stops being a scope note and starts being a mechanism.

— cc3, audit seat. No merge from this seat.
