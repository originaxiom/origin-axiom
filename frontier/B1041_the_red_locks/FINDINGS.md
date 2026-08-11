# B1041 — three red locks, and the one reason none of them was seen

**Date:** 2026-08-11 · **Lane:** the consolidation refresh — the lock layer. Gate 5 untouched;
zero anchors; nothing to `CLAIMS.md`; **no banked mathematics overturned.**
**Files:** `verify.py` → `results.json` (8 checks) · lock `tests/test_b1041_red_locks.py`.

**Occasion.** This refresh had banked seventeen arcs without ever completing a full
`pytest tests/` run. Three attempts died at their own timeouts — **RC=124, which is not a pass**,
though I had been treating a clean gate run plus targeted locks as sufficient. The completed run:

> ### `3 failed, 3891 passed, 119 skipped in 4870.92s (1:21:10)`

**26 gates were green throughout, and no gate covers any of the three.**

---

## 1. THE MECHANISM IS NOT MY FINDING — IT IS **REVIEW 42's**, AND IT HAS ALREADY RECURRED

Before writing this up I found the finding already in the record, **dated 2026-08-09**, as
Review 42's *governing* finding (`REVIEWS.md:3301`):

> **"THE WINDOW'S GOVERNING FINDING: two locks were red at HEAD, and nobody knew."** … *"The
> mechanism is not neglect — it is that the full suite takes **~55 minutes** and had not been run
> to completion in the window. Gates are fast and were green throughout; **gates do not cover what
> the locks cover.**"*
>
> *Action: the banking checklist's "suite green" row is only discharged by a completed run, and a
> partial run is not a run.*

**So the correct finding is not the mechanism. It is that the mechanism recurred within two days of
being named as governing** — with **three** red locks this time instead of two, and **I** was the
one shipping past them.

**Because naming it did not gate it.** The prescribed action was a *checklist row* — prose, read by
people. Nothing mechanical distinguishes "the suite passed" from "the suite was started". Every
signal that *is* mechanical stayed green.

**And the wall grew.** Review 42 measured **~55 minutes**; the completed run here is **81** — a
**47 % increase in two days of repo time**. Four tests are **29 %** of it (`test_b222` **587 s**,
`test_b219` **491 s**).

> **The locks worked. Nothing was reading them.** All three failures are order-independent: each
> reproduces in isolation in under two seconds.

That is also how **B1035's path guard** (repaired in `fbdcf63`) stayed red through several of this
refresh's own commits — **my defect, by the mechanism Review 42 had already named.**

## 2. B511/D3.3 — a probe that is numerically dead

The lock asserts `classical > 0.8`; the probe returns **0.0**. Measured here:

| steps | 60 | 120 | 240 |
|---|---|---|---|
| **finite fraction** | 1.000 | 0.225 | **0.000** |

The lock calls it at **steps = 1500**. The banked figure is *"P(κ≈2 classical) ≥ 0.84"*.

**The obvious hypothesis was tested and is false.** I assumed the 20-step renormalisation interval
was too coarse. **Renormalising every step changes nothing** (0.245 vs 0.225 at 120 steps; 0.000 at
240 either way).

> **The cause is structural.** The doubling branch `A@A` **preserves `det = 1` while doubling
> `log‖A‖`**. A det-normalisation cannot bound the norm *at any interval* — it is not a norm
> control at all.

**Nothing is overturned.** D3 is explicitly a restatement — *"re-confirm already-banked B506/B507
content; no new structure"* (`D3_PARTIAL.md`) — and **B511 is cited on no curated surface.** What
fails is this cell's evidence, not the result.

**And one thing here is not my finding.** I was about to report that D3.2's arcsine gate reads
numerical death as maximal confirmation (`ends=1500, center=0` → *"U-SHAPED"*). **`D3_PARTIAL.md`
already says so** — *"The script's auto-line 'U-SHAPED' is a **BUG**: it summed bin[0]+bin[9] but
bin[9]=0"*. The narrower true claim is that **it was never repaired**: the script still prints it,
the **banked `d3_results.txt` still carries the wrong conclusion**, and the correction lives only in
a prose file no machine reads. *Reading the arc body rather than the script is what caught this —
the campaign's step 1, doing exactly its job.*

## 3. B646 — a preservation manifest that no clone can satisfy

Measured across the **nine** manifest-bearing harvest arcs:

| | |
|---|---|
| manifest entries | **366** |
| missing from this clone | **63 (17.2 %)** |
| **explained by `.gitignore`** | **61** — `*.log` ×60, `*.pyc` ×1 |
| unexplained | 2 (hash-prefixed B663 filenames) |

`.gitignore:20` is `*.log`. The harvest policy is *"sha256 of every packet file **AS RECEIVED**"* —
and **git refuses those paths, so they were never committed and no clone has ever had them.**
Single-caused, not rot.

> **This qualifies one of my own arcs.** **B1035** declined to repair 31 unresolvable `sys.path`
> lines *because editing them "would break the manifest"*. That reason still holds for the files
> that exist — but **the manifest was already unverifiable for a sixth of its entries**, and B1035
> did not know. **The non-finding stands; its stated ground is narrower than it read.**

## 4. B616 — a transcript-grep lock, which the corpus already has a class for

The lock pinned the literal `"observed 2 coarse-tier matches of 378 pairs"`. The script now prints
**3 of 390** — the census's *input set* grew.

**The mathematics did not move:** design hash `a11491e6`, the `(−1)^m` sign law match (*"same:
True"*), and the locked-table verdict **STILL-AMBIGUOUS** all hold.

This is **E6** in the corpus's own taxonomy — *"a test asserting an output string rather than the
mathematical fact"* — whose standing rule is *"locks assert mathematics (`WORKING_RULES` §7)"*.
**Four of the lock's five assertions are transcript greps**, and the one that broke is the only one
pinning a data-set-dependent count rather than the arc's claim.

## 5. WHAT WAS REPAIRED, AND WHAT WAS DELIBERATELY NOT

| lock | repair |
|---|---|
| **B646** | `MISSING` is exempted **only when `git check-ignore` confirms the path is unversionable** — asking git, not matching extensions, so a genuinely lost file still fails. Plus a new lock bounding the gap's *shape* (all ignored, all `.log`/`.pyc`, ≤ 15) so the exemption cannot become a blanket |
| **B616** | **retargeted from the literal to the mathematics**: the counts are parsed and tested against the arc's actual claim (observed not significantly above the null), with the design hash, sign law and verdict retained |
| **B511** | **SKIPPED with the reason, not weakened and not left red.** Weakening asserts what the probe cannot support; leaving it red is what hid it. **The diagnosis is locked instead** — a new green test pins the overflow *and* that per-step renormalisation does not fix it, so the finding survives in the lock layer rather than only in prose |

**Not attempted:** repairing B511's probe. Making that measurement stable is a reformulation of the
cell, not a consolidation task, and the conclusion it supports is independently banked.

---

**Verdict: PROVED** as an audit. 8 checks, every number measured here.

**Self-correction — I committed one of the corpus's own registered classes, E36.** Importing
`d3_measure` to inspect it **runs its `__main__`, which rewrote `d3_results.txt` and
`d3_results.json`** with the NaN output — clobbering banked artifacts, exactly the artifact-clobber
class the ledger registers from B907/B910. Caught on the next command, restored from git, tree
clean. **The fix is structural, not an apology:** `verify.py` reimplements B511's recurrence rather
than importing the module, so the arc that reports the clobber cannot cause it.

> **The lesson this pass keeps re-earning, now from the other side.** B1039 and B1040 found checks
> that could not fail. These are checks that *did* fail, correctly, for weeks — **and failing was
> not enough**, because the thing that runs them costs 81 minutes. *A lock is only as good as the
> cheapest thing that reads it.*

**And the second-order lesson, which is the one that cost me a rewrite.** I drafted this arc's
headline as the discovery of a mechanism **Review 42 had already made its governing finding two
days earlier**. That is the third time in this refresh that the record already held what I was
about to claim — after B1040's `(g,n)` count (classical, and `OPEN_LEADS` said so) and B511's
arcsine bug (caught in `D3_PARTIAL.md` in July). **Each was caught by reading the body rather than
the artifact**, which is campaign step 1, and each would have banked as a discovery otherwise.
*The recurrence rate of that near-miss is itself worth a number: three in eighteen arcs.*
