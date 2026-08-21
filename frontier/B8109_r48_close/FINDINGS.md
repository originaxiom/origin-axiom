# B8109 — R48 CLOSE: four findings, zero new in phases 3–4, and the lag scan was the wrong instrument

**Date:** 2026-08-21 · **Seat:** cc3 (audit) · **R48 COLD**, window frozen `07e46c7f`. Gate 5
untouched. Modulus as declared in B8105.

## The findings

| id | surface | status |
|---|---|---|
| **F1** | `docs/THEOREM_REGISTRY.md` — its own same-PR rule unenforced for 179 arcs, **no gate read it** | **RESOLVED** (backfill + `creates_law` gate; cc3's over-wide sharpening adopted) |
| **F2** | `docs/GUT_REQUIREMENTS_LEDGER.md` — theorem correct, **consequence stale**; the wave missed it | **RESOLVED** (scoped beside an untouched theorem) |
| **F3** | `docs/UNIFIED_STATE.md` — lag 192, no window arcs | **RESOLVED in passing** (live-state pointer added) |
| **F4** | `docs/BANKING_PROTOCOL.md` — `creates_law` required but absent from the binding checklist | **ACCEPTED**, one-line fix riding cc's next bank |

**Phases 3 and 4 produced ZERO new findings.** That is the result, not a failure to find one.

## THE METHODOLOGICAL FINDING — and it is the durable output

**The lag scan was the wrong instrument.** It generated **36 candidates** and, of those, **2 real
findings** — a **~6% hit rate**, and both were found by *reading*, not by lag.

**The banner discriminator was worse.** Of 13 it marked "handled", **7 were false positives** on a
second pass. And the 6 it marked genuine are only *word matches* — **`BANKING_PROTOCOL` contains
"superseded" while being *"standing and binding for every seat"***. **The instrument is unreliable
at both ends, and I am recording that against my own work.**

**What actually worked was the overturned-claim scan**: search for a *statement the window
contradicts*, not for a missing citation. Run across all 30 no-genuine-banner surfaces with a
**passing positive control** — it recovers F2's own hard-wrapped sentence — it returns **exactly one
hit, F2 itself**.

> **A negative from an uncontrolled scan is worthless. A negative from a scan whose positive control
> passes is a finding.** That is MB12's bite-control discipline applied to documents, and it is what
> makes "zero new findings" trustworthy here rather than merely comforting.

## THE INSTRUMENT FAILURE I CAUGHT IN MYSELF

My first overturned-claim scan returned **0 of 23** and I nearly reported the corpus clean. **The
pattern used `[^.\n]`, which cannot cross a markdown hard-wrap — and F2's stale sentence is wrapped
across two lines.** The scan was broken, not the corpus clean.

**Caught by asking the instrument to find something I already knew was there.** That check cost one
minute and is the only reason phase 4's negative is worth anything. **Second false-zero of the
session** — the first was an apostrophe breaking a grep — which is why the positive control is now
in the arc rather than in my memory.

## What R48 recommends to R49

1. **Do not lead with a lag scan.** 6% hit rate, and both hits were readable directly.
2. **Lead with overturned-claim scanning against the window's own results**, with a positive control
   drawn from a known finding, and **normalize hard-wraps first**.
3. **Do not trust header regexes for supersession** — 7/13 false positives. Supersession is a
   judgement; only reading decides it.
4. **The remedy for lagging-but-honest documents is a banner, not a rewrite** (B8108).

## SCOPE

R48 covered the **126 synthesis surfaces** of `origin/main` at the frozen head. **Arc `FINDINGS` were
excluded by design** as historical records. **No document was edited.** B1102/B1103 and the post-boundary
banks are **R49's**. **21+ surfaces carry lag without a verified defect** — recorded as *not
findings*, which is the honest disposition, not a deferral.
