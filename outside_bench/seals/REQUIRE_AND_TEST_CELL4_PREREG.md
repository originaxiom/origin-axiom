# PREREGISTRATION — CELL 4: the remaining §A rows, and whether the walls are about the OBJECT

*Outside bench, 2026-09-14. Sealed before the certificate runs. Gate 5 untouched.*

## What this cell is

Cells 1–3 measured base rates for §A rows 1 and 2. This cell completes the table: rows **3, 4, 5, 6, 7,
8**. Most are **assembly**, not sweeps — so the certificate's job is not to compute a rate but to
**verify that every quoted line is present verbatim in the file it is attributed to**, and to answer one
computable question about row 3.

**Why verification-of-citation is the right instrument here.** `docs/ERROR_LEDGER.md`'s E2 names *"a
reference table transcribed wrong at sealing"* as a defect class. An assembly cell is exactly where that
defect lives. Every quotation this cell uses is asserted against its source file; a single missing
string fails the cell.

## THE COMPUTABLE QUESTION — row 3, and it decides how R144 should be read

`docs/WHAT_WOULD_COUNT.md` §4A re-scoped the value tier. Its argument is **not** disappointment: it is
that the tier is **E2/MB12-vacuous** because every licensed route is closed, three of them by theorem —

1. **B666 cell S**, the scale-torsor no-go (`docs/LAW_MAP.md`);
2. **B936**, the value-invisibility theorem (`frontier/B936_cohomology_reading`);
3. **B1096**, the anomaly layer identically zero (`frontier/B1096_anomaly_layer`).

E2's own wording for this defect class is *"a sealed gate that **cannot pass for any genuine object**"*.

> **THE QUESTION: do those three theorems mention the object at all?**

**The test, fixed now:** for each theorem, take its own statement as the record carries it (the
`arc_verdict.json` claim line, or the `LAW_MAP.md` paragraph for B666) and search it for any object
token — `m004`, `figure-eight`, `figure eight`, `4_1`, `4₁`. **Nothing else is consulted**; the question
is what the theorem's own statement says, not what its arc directory contains.

- **OUTCOME I — OBJECT-FREE:** no theorem's statement names the object. Then §4A's re-scope is
  **correct and provable**: the value criterion cannot pass for *any* object through these routes, so
  it carries no information about which object was chosen. Row 3's base rate is **0 for every object**,
  and that is a fact about the **requirement**, not about m004.
- **OUTCOME II — OBJECT-BOUND:** at least one statement names the object. Then the wall is at least
  partly m004's, and re-scoping the criterion absorbed evidence that should have been read as being
  about the object.

**This cell will say which, and it corrects this bench if the answer is I.** R144-4 wrote that when
falsifier 2 fired the programme took reading (a) *values are the wrong criterion* and never (b) *the
object is the wrong object*. **If OUTCOME I holds, then for row 3 reading (a) is not a re-framing but a
theorem, and R144's sentence is too strong for this row specifically.** That correction is
preregistered here so it cannot be presented afterwards as if it had been the plan.

## THE ROWS, and the verdict each may carry

| §A row | the verdict this cell may return |
|---|---|
| 3 values | P writable; T = LACKS (V-3); **B settled by the question above** |
| 4 dynamics | **NOT-COMPUTABLE** — no derived action on main; §E row 1 lists six declared inputs |
| 5 gravity | **NOT-COMPUTABLE** — *"containment, not a theory"*: a spin-2 slot, no propagator, no coupling |
| 6 quantum consistency | **DOWNSTREAM** — anomaly-freedom is a property of a *closing*, not of the object, so it cannot discriminate objects until a closing is derived rather than chosen |
| 7 predictions | P writable; T = P9 is a **regime**, conditional and sealed |
| 8 say which endpoint | **NOT A CELL** — the only §A row whose status column is the ledger itself; a discipline rule on claims |

A row whose honest verdict is NOT-COMPUTABLE is **reported as NOT-COMPUTABLE with what would make it
computable**, never quietly upgraded.

## CONTROLS

| # | control | catches |
|---|---|---|
| M1 | every quoted string asserted present in its named file; count printed | E2's "transcribed wrong at sealing" |
| M2 | the object-token search is shown to WORK — run it on a statement that *does* name the object (B1321's claim line) and it must find one | a search that finds nothing because it is broken (#164) |
| M3 | the number of quotations checked is printed and asserted > 0 | the B1197 vacuity trap |

## WHAT THIS CELL MAY NOT CONCLUDE

That row 3's walls are the only walls, or that no route to values exists — §4A's own fence says the
coupling-channel leg is *"empirical exhaustion, not theorem"*, and that distinction is kept. No value.
Nothing about rows 4–6 beyond NOT-COMPUTABLE/DOWNSTREAM.

---

# ADDENDUM 1 (2026-09-14) — CONTROL M2's PROBE WAS MIS-CHOSEN

**M2 as sealed said:** *"run it on a statement that does name the object (B1321's claim line) and it
must find one."* **B1321's claim line does not name the object** — B1321 is about the **sibling**
(m202, s959), so its claim line names m202 and never m004. The first run returned `tokens found: []`
and **M2 correctly FAILED.** The search was not broken; the probe was.

**This is the second mis-specified control in this programme** (Cell 3's L1 was the first). Both were
assumptions this bench made about what the record says, and both were caught by the control rather
than by re-reading. Recorded as such.

**CORRECTED M2 — three probes, chosen to exercise the token list, not one:**

| probe | the spelling it carries |
|---|---|
| `frontier/B803_commensurability_audit` claim line | `m004` |
| `frontier/B282_e6_is_arithmetic_not_geometric` claim line | **`4₁`** — the digit-subscript spelling |
| `frontier/B1163_w0_attempt` claim line | `m004` **and** `4_1` |

**All three must find at least one token, and between them they must exercise at least three distinct
spellings.** This is not decoration: `ERROR_LEDGER` **E54** records a search of this exact kind that
missed its target *"because the search lacked the DIGIT spelling"*. A single-probe control would not
have tested that.

**Not changed:** the question, the three theorems, the two outcomes, the quotation list, or the row
table. Only the control's probe — and only because the seal named one that could not pass.
