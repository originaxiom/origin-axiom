# B1274 — THE SECOND COLLAPSE: I-25's multiplicity 4 falls to a point, and both collapses run through the object's own 2T

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact; four MB12 controls) · **Second dent in the H5 pattern**

## Why this arc

**B1273's addendum** collapsed **I-6's binary** by two concordant selectors — the owner's **arithmetic**
one (holonomy mod (1−ω)) and codex's **topological** one (extension over m000). That was the **first**
of the H5 census's **eight measured multiplicities** to become a **point** rather than a count.
**Was it a one-off?** No.

## I-25 already had two selectors, and nobody had checked they agree

| | selector | from |
|---|---|---|
| **1** | the **unique** E₆ nilpotent orbit whose Slodowy slice meets the nilpotent cone in a **SURFACE** — which Brieskorn–Slodowy identifies as **ℂ²/2T**, the very group that **built E₆** by McKay | B1257 (geometric) |
| **2** | of the **four** labellings typing h¹ = 3 as three chiral, the only one with **no even-dimensional summand** — i.e. the only one admissible for the object's **canonical PSL(2,ℂ)** holonomy, since even-dimensional (Sym^odd) reps are not PSL(2,ℂ) reps at all | B1256 addendum (representation-theoretic) |

**Computed here: both return (2,2,2,0,2,2) — the SUBREGULAR, 27 = 13 + 9 + 5.**

> **I-25's multiplicity 4 collapses to a point.**

## The shape is the same as I-6's — and the common factor is 2T

| row | selector A | selector B |
|---|---|---|
| **I-6** | *geometric*: the holonomy reduced mod (1−ω) lands in a specific 2T quotient | *topological*: that quotient is the one **extending over m000** |
| **I-25** | *geometric*: the slice that **returns ℂ²/2T** | *representation-theoretic*: the embedding the **PSL(2,ℂ)** holonomy admits |

**In both, one selector is "the structure that returns the object's own 2T" and the other is a
compatibility condition. The object's 2T is doing the selecting.**

## What this does to H5 — and what it does not

**OPEN_ITEMS H5** says the object supplies every **space** and never a **point**. **Two** of the
census's eight measured multiplicities are now **points**, each pinned by **two independent concordant
criteria**. That is genuine counter-pressure on the pattern.

**But it is NOT a falsification, and this arc does not claim one.** H5's falsifier asks for an
**other-referential** point. *"Which 2T quotient"* and *"which sl₂ embedding"* are both facts about how
the object sits inside structures **the object itself generated** (E₆ came from its own 2T by McKay) —
so they are **self-referential**, which H5 explicitly permits.

**What has changed is the pattern's reach, not its truth:** the object is **far more decisive about
itself** than the census suggested, and **the remaining multiplicities should each be attacked for a
selector rather than counted.**

## Controls (MB12, both directions)

- Each selector is **recomputed here from its own definition**, not read from the parent arcs.
- **Selector 2's discriminating power is exhibited:** it starts from **four** candidates and cuts to
  one — so agreement is **not vacuous**.
- Selector 1's uniqueness is checked against **all 30** integral labellings.
- The two are compared **as sets**, so a mismatch would be reported rather than assumed away.

## Verification

`verification/second_collapse.py` — standalone; imports both parent verifications directly.

- **Feeds on:** B1257, B1256 (+ addendum), B1264 (the census), B1272/B1273 (the first collapse).
- **Registers:** **I-25**'s multiplicity objection **paid**; the row stays **UNEARNED** (deriving
  *which* sl₂ the object supplies is still not the same as *exhibiting* the object supplying it).
