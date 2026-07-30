# B825 — the Markov-cubic motif SUCCEEDS; the last known lexicon gap closes

cc banking seat, 2026-07-30. **Prereg `2812a0c550ae2b92`, sealed at `60a705e1` before the edit.
Attempt 2 of a declared maximum of 2.** Repository-instrument scope; Gate 5 untouched.

## Verdict: SUCCESS on all three sealed criteria

| sealed criterion | required | got | |
|---|---|---|---|
| 1 — hits `B537` | yes | **yes** | ✅ |
| 2 — matches ≤ 15 % of corpus | ≤ 15 % | **8.3 %** (62/750) | ✅ |
| 3 — not ≥ 90 % inside any single existing motif | < 90 % | **75.8 %** (in `trace_map`) | ✅ |

**The criteria were identical to B824's, not relaxed.** Only the patterns changed, and the change
applied B824's own measurement rather than searching for a passing configuration: the single
ambient term `character variety` (13.8 % of the corpus alone) was dropped, and every remaining
pattern had measured ≤ 4.1 % individually.

**Pre-stated expectation: SUCCESS, landing near 6–9 %. It landed at 8.3 %.** Recording the predicted
*range* rather than the direction is what makes that a real check — a pass at 14.5 % would have
cleared the ceiling while telling me the patterns overlap far more than I thought.

## The attempt cap did its job by existing

The seal fixed **two attempts, declared before attempt 2 ran**, because "iterate the patterns until
the share clears the ceiling" has no natural stopping rule and would eventually yield a passing
motif **by search rather than by insight**. The cap was not reached — but it is what makes the
success interpretable, since two attempts with the exposure stated is a very different claim from
an unbounded search that happened to stop here.

## What closed, and what emphatically did not

`docs/atlas/BLIND_ARCS.md` now shows **0 open `GAP` rows**.

> **That means "no known uncovered object topic among substantial blind arcs." It does NOT mean the
> lexicon is complete.** The motifs remain grounded in K001–K022 and unrevisited since 2026-07-01;
> **B806's call for a full re-grounding is untouched by this arc**, and the registry says so in
> place so a later reader cannot mistake an empty `GAP` column for a finished instrument.

## A known false-positive mode, recorded rather than filtered

B821, B822 and B823 dropped off the blind registry — **not because they are about the Markov cubic,
but because they *quote* it while discussing the gap.** A regex motif matches **mentions, not
subjects.**

This is left in place deliberately. Filtering it would mean classifying by topic, which is exactly
what B822 refused on the grounds that it lets the number be tuned by relabelling. **The honest move
is to write the limitation where a reader meets it**, which is the registry.

## The six-arc sequence this ends

| | | |
|---|---|---|
| **B820** | *"the lexicon is rotting"* | diagnosis **wrong**; its rate diagnostic was the useful part |
| **B821** | a meta-layer motif closes the gap | **failed** its vacuity ceiling (46.2 %); decomposed the count into 14 stubs + 6 instrument + **1 real gap** |
| **B822** | the gate should stop diagnosing | **succeeded**, then broke its own ceiling by being written |
| **B823** | the gate should stop counting | triage registry; **no threshold** |
| **B824** | a character-variety motif closes `B537` | **failed** at 18.4 %; isolated `character variety` as ambient at 13.8 % |
| **B825** | the **Markov cubic** closes `B537` | **this arc** — 8.3 %, all three criteria |

> **Two vacuity ceilings fired and killed two motifs before one passed.** The instrument that ends
> this sequence is not the motif — it is the ceiling that refused the first two.

`tests/test_b825_markov_motif.py`
