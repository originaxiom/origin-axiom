# B966 — L140 EXECUTED: the first gate aimed at claim **scope**

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** INSTRUMENT / GOVERNANCE.
Gate 5 untouched. **Closes** the gap the owner named: *machinery catches arithmetic, only a
human catches meaning.*

---

## The rule

> A LAW_MAP row citing an arc whose **verdict** carries **≥ 4** scope markers must carry
> **at least one** scope marker of its own.

Markers: *only for · scope · assumes · not established · conditional · up to · one-prime ·
not certified · not claimed · post-hoc · inferred · cited not re-derived · screened ·
necessary-not-sufficient · limits · does not · NB(*.

Registered both directions per the practices rule: gate `lawmap-scope` in
`scripts/gates/gates.py`, row in `docs/PRACTICES.md`.

## Why this rule and not another

B965's audit found that in **every** fix, **the arc's own verdict was correct and properly
scoped.** Nothing was wrong with the mathematics or with the arcs. **The qualifier died in
the compression step** — turning a verdict into a one-line row. So the gate is placed
exactly there, and nowhere else.

This is the **first gate in this repo aimed at claim scope** rather than at numbers, hashes,
paths or file presence — i.e. at the class of error that until today only a human ever
caught.

## Calibration — and it caught one more on its first run

Calibrated against B965's audit: the gate **flags all three rows that audit had to fix** and
**passes the row that audit adjudicated as already correctly scoped** (the no-centralizer
row, which carries "SCOPE NOW UNCONDITIONAL (B960)" and names "(Steinberg)").

**On its very first calibration run it found a fourth violation the audit had missed:** the
F₄ row cites **B962 — which B964 partially retracted** — without saying so. Now fixed: the
row records that B962 was partly retracted, that this finding is among those that survive,
and that the orbit stratification is cited rather than re-derived here.

## Non-vacuity — demonstrated, not assumed

Per MB12, a gate that cannot fail is not a gate. Demonstrated by experiment: deleting the
qualifier *"INFERRED from the rank bookkeeping, NOT computed"* from the two-seeds row makes
the gate **FAIL**; restoring it makes the gate **PASS**; the file was restored byte-identical.

## Honest limits

1. **Keyword-based.** It cannot see a scope loss phrased without any marker, and a row can
   satisfy it with a marker that is *present but irrelevant*. It raises the floor; it does
   not certify a row.
2. **LAW_MAP only.** CAMPAIGN_STATUS, README and PROGRESS_LOG headlines carry compressed
   claims too and are **not** covered. Extending it there is the obvious next step.
3. **The threshold (≥ 4) is calibrated on one audit** of 165 rows. It is a defensible choice,
   not a derived constant.
4. It enforces the *presence* of a qualifier, **not its correctness**. A row could carry an
   irrelevant marker and pass. **A human still has to read.**

---

**Verdict: INSTRUMENT.** The compression step now has a gate, calibrated on the audit that
found the leak, proven able to fail, and already responsible for one fix the audit itself
missed. **L140 executed. L139 (retraction sweeps) remains open** — that one still has no
machinery.
