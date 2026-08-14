# B826 — B519's missing verdict was a filename gap, not a content gap

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched. Closes the item B819
registered and B818 flagged.

## What was wrong

`B519_re_mining` carried **no verdict at all**, though B525 had cracked its *"no external crossing"*
headline. B818 named it *"the arc most in need of a `RETRACTED` marker"* and B819 found it was the
**only** arc in the repository with a non-standard layout (`CAMPAIGN.md` + `VERDICT.md`, no
`FINDINGS.md`).

**On reading it, the arc turns out to be exemplary rather than deficient.** Its `VERDICT.md` already
carries the correction, prominently and in its own voice:

> *"**CRACKED by the B525 'Are You Sure' audit (necessary-not-sufficient) — this headline is
> CORRECTED below.**"*

— with the B1 row struck through (`~~REFUTED 3–0~~`) and re-marked **`LIVE (B525-reopened)`**, and
the conflation spelled out: the refutation rested on Bellissard gap-**labeling** (a *necessary*
K-theoretic constraint on *where* gaps sit) read as a *sufficient* guarantee about *which* gaps
physically **open**.

**Nothing was missing except a file called `FINDINGS.md`.**

## The actual defect: an invariant stated as a filename

Writer safety says *never write a verdict for an arc with no `FINDINGS.md`* — and it is a good rule,
which held under a live 3.0 % fault rate in wave 2 with **zero fabrications**. But the rule it was
*meant* to encode is:

> **No verdict without a substantive findings document.**

Encoded as a filename, it silently excluded the one arc that documents its own retraction best.
**A safety rule that names a file instead of a property will eventually refuse the wrong thing.**

## What changed

- **`B519` now carries `RETRACTED`**, sourced from its own correction banner and B525 — **not
  invented**. Correct under B818's rule: B519 withdraws **its own** headline.
- **The writer-safety invariant now reads `FINDINGS.md` *or* `VERDICT.md`**, in both the wave-2 lock
  and B818's self-retraction-marker check — the latter had the same narrow read, which is why B519
  looked like an untagged `RETRACTED` the moment the verdict was written.
- **The widening is guarded, and deliberately narrow.** A lock asserts `README.md` and
  `PREREGISTRATION.md` are *not* admitted: **a prereg records intent, not result, and admitting it
  would let a verdict precede the work it reports.**

## Two locks moved together, and that is the point

Writing B519's verdict immediately broke B818's marker check — because *both* checks had encoded the
same invariant as the same filename. **A single narrow read reproduced in two places looks like
corroboration until one of them is exercised.**

## Still carried

The retractions B745 and B525 trigger on **their targets** remain unrecorded: `B225` carries
`PROVED` though B745 confirmed its 2-half kill vacuous — which **may be correct for B225's surviving
content**, and needs reading rather than assuming — and `B58` is split across three directories
(`B58_phaseA`, `B58_sl4_tower_test`, `B58_stage1`), which is why wave 2 skipped it. **Not closed
here**: each needs a judgement about what still stands, and B519 was closable only because its own
document had already made that judgement.

`tests/test_b826_b519_verdict.py`
