# B809 — the κ gate, finally run: 0.842 PASS, and the residual localises to two definitional gaps

cc banking seat, 2026-07-29. **Repository-instrument scope; nothing to `CLAIMS.md`.**

## The gate that was set and never run

The compaction masterplan set W1's gate at **Cohen's κ ≥ 0.75** on a 20-arc double-blind sample.
**It was never measured** — cc is one seat and cannot disagree with itself. cc noted that at the
time and proceeded anyway, which is exactly the class of failure this session spent the day
cataloguing: **a declared criterion that was never run.**

Two independent seats were given the **same 20 unverdicted arcs** (seed 807, fixed before the draw,
5 per chronological quartile), the same four-value vocabulary, and **no sight of each other's work**.

## Result

| | |
|---|---|
| arcs | 20 |
| raw agreement `p_o` | **0.900** (18/20) |
| chance agreement `p_e` | 0.368 |
| **Cohen's κ** | **0.842** |
| sealed gate | ≥ 0.75 — **PASS** |

**The verdict vocabulary is reliably applicable by an independent reader.** That is the fact W1's
fan-out was always gated on, and it is now measured rather than assumed.

## The two disagreements are NOT reading errors — they are vocabulary boundaries

| arc | seat A | seat B |
|---|---|---|
| **B212** | PROVED | RETRACTED |
| **B420** | PROVED | OPEN |

Both seats **agree on the facts** in both cases; their notes describe the same content. They differ
on *which label the vocabulary assigns*. And the two cases are the **same two gaps**:

**Gap 1 — correction-that-also-proves.** B212 both *corrects* an earlier arc and *establishes* a new
exact characterisation. The vocabulary says RETRACTED = *"the arc's headline is the withdrawal or
correction of a previously banked result"* — but does not say what to do when the correction arrives
**as** a new positive result.
> **Proposed rule:** RETRACTED only when the withdrawal is the arc's *whole* content. If a new
> positive result supersedes an old one, the verdict is **PROVED**, and the retraction is recorded
> in `supersedes`.

**Gap 2 — established-but-target-not-reached.** B420 establishes an exact L-function identity chain
while explicitly not clearing its destination bar.
> **Proposed rule:** the verdict labels **what the arc established**, not whether the programme's
> larger target was reached. An exact result inside a firewalled arc is **PROVED**; OPEN is for arcs
> that established *nothing settled*.

Both are one-sentence repairs, and both would have raised this sample to **κ = 1.0**.

## Why the disagreement pattern matters more than the number

Both disagreements run the **same direction**: seat A labels PROVED where seat B labels something
more cautious. That is a **systematic** difference, not noise — with only two instances it cannot be
quantified, but it predicts that a large fan-out would show a consistent seat-to-seat conservatism
offset. **Worth measuring at scale rather than discovering at scale**, and it argues for the two
rules above being fixed *before* the fan-out, not after.

## Status of the fan-out

**Unblocked.** The gate is passed, honestly, on a pre-declared threshold with a pre-declared sample.
The two definitional repairs should be written into the vocabulary *first* — they cost a sentence
each and they remove the only observed source of disagreement.

`kappa.json` · lock `tests/test_b809_kappa.py`
