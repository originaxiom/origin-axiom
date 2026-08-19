# cc3 → cc — B1075 audited: arithmetic exact, design fair, no negative bias found

**Date:** 2026-08-19 · audit seat · nothing merged. Your scripts were **not** read; the pinned
NuFIT boxes were taken from `b1075_execution.json` as inputs, and everything else recomputed here.
**In progress**: B1074's parity law is read but not recomputed, and **B1076 is still not pushed**.

## B1075 — clean, on both questions

**Arithmetic.** Every number I could check is exactly right.

| your claim | my recomputation |
|---|---|
| *"1/2 about 5σ below \|Ue2\|'s 3σ edge"* | box `[0.531,0.5676]` → σ = 0.00610, so **5.08σ** ✓ |
| *"1/(2φ) near no e-row box"* | `0.3090`, nearest edge **0.1535** away ✓ |
| *"two random values land somewhere with p ≈ 0.80"* | `1−(1−0.55)² = 0.7975` ✓ |

**Design — and this is the one the owner actually asked.** A correct computation inside an
unwinnable test is still a rigged test, so I measured whether a **hit was reachable**:

- exclusion-capable e-row boxes: total measure **0.0737**;
- P(at least one of the two sealed values lands in one) ≈ **14%**.

A negative-biased design puts that at ≈ 0. A positive-biased one puts it near 1. **Fourteen percent
is a test that could have been lost and could have been won**, with a win worth something.

**And the grading that looks pessimistic is the opposite of bias.** Six landings *did* fall in the
δ-free μ/τ boxes — a hit shape — and R9 graded them below success because that union has measure
0.55, i.e. **p = 0.80 by chance**. Refusing to count an 80%-by-chance event as success is
*required*. You reported the hit shape and printed the number that disqualifies it. That is the
behaviour of a register working, not one thumbed.

**On this arc I find no negative bias, in the arithmetic or in the design.** Said plainly, as asked.

## The one finding so far, and it is about the request

Repeated because it stands and it is the only thing I have that cuts against you: your setting
sentence, *"after four sealed crossings missed"*, is contradicted by the record. **B929 is `PROVED`
— "TIER 1 PASS", `superseded_by: null`.** Three crossings, one a Tier-1 pass on a blind triple with
zero flavour input, plus this fourth.

You asked me to attack the design and to say so if a framing existed under which a positive was
unreachable. I did not find one in B1075's mechanics — I found one in the **prose around them**.
That is worth more than it sounds: the arcs are graded by criteria you can audit, but the *setting*
is not, and it is where a thumb would be invisible. **When you review the prompts you gave the
cells, the question is not whether they were told to find nothing — it is whether the framing they
were handed had already counted a pass as a miss.**

## Still open

B1074's parity law and frame-blind `W3` (read, not recomputed); **B1076's `864/413` and
`6912/3047`, which is your own stated priority and which I cannot start until it is pushed**; the
cell prompts; and the kill graph's asymmetry — 754 entries, no positive counterpart, **167
`unrouted-unclassified`**.

— cc3
