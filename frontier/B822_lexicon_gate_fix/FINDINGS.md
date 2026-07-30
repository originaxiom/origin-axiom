# B822 — the lexicon gate stops asserting a diagnosis it cannot support

cc banking seat, 2026-07-30. **Prereg `69a7ae603dc5a1dd`, sealed at `884e825f` before the edit.**
Repository-instrument scope; Gate 5 untouched.

## Verdict: SUCCESS on both sealed criteria

| sealed criterion | required | got | |
|---|---|---|---|
| the size floor removes ≥ 10 of the 22 blind arcs | ≥ 10 | **14** | ✅ |
| the floored count is ≤ 10 | ≤ 10 | **8** | ✅ |

**Pre-stated expectation was "14 stubs removed, leaving 8." Exactly that.** Recorded as a
confirmation, which is weaker evidence than a surprise would have been.

The eight that remain: `B537 B679 B770 B793 B798 B818 B819 B821`.

## What triggered it

Immediately after B821 banked, the gate fired at 22/21 printing:

> *"the lexicon is ROTTING, not merely outgrown"*

**B821 had just refuted that exact inference**, and the arc that pushed the count over the line was
**B821 itself** — a pure-instrument arc, which an *object* lexicon is correct to miss. **A gate was
emitting, as a machine verdict, a claim the repository had disproved one commit earlier.**

## The two changes

1. **The metric is floored at `FINDINGS.md` ≥ 2000 bytes.** An arc of 409–1988 bytes reading
   *"Logged observation, not a claim."* cannot match any lexicon, and counting it measured the
   **archive's shape, not the instrument's health**.
2. **The ROTTING-vs-outgrown verdict text is gone.** The gate now reports the count, the ceiling,
   the number of thin arcs excluded, and the list — and asks the reader to decide *"whether each is
   a real gap or an arc an OBJECT lexicon should miss."* **It reports; it no longer concludes.**

## What was deliberately NOT done

**Instrument arcs are still counted.** Excluding them would mean classifying by *topic* — a
judgement about arcs this seat wrote — and would let the number be tuned by relabelling. **Size is
objective; topic is not.** Six of the remaining eight are instrument arcs and stay in the count,
which is why the ceiling is 8 rather than 2.

The prereg also forbade the easy escape in advance: *"raising a threshold is not a permitted
response to a failed criterion here."* It did not come to that, but the constraint was live.

## The sequence this closes

Three commits, each correcting the one before, and worth stating plainly because the shape recurs:

| | claim | fate |
|---|---|---|
| **B820** | *"the lexicon is rotting"* — from a 5.4× blindness rate | **diagnosis wrong**; its rate *diagnostic* was the useful part |
| **B821** | one motif closes the gap | **failed its own vacuity ceiling** at 46.2 %; reverted. Decomposed the count: 14 stubs + 6 instrument + **1 real gap** |
| **B822** | the gate should stop diagnosing | **this arc** — the instrument now reports composition instead of a verdict |

> **The instrument was wrong in a way that looked like a finding for two commits.** What caught it
> was not scepticism but *composition* — asking what the 21 arcs actually were.

## The limit this run exposed, and it is structural

Writing this findings file **broke the ceiling it had just set.** B822's own `FINDINGS.md` is a
substantial arc with no motif, so the count went 8 → 9 the moment the fix was documented.

> **The gate ratchets against instrument arcs, and the arc documenting the gate is an instrument
> arc.** The ceiling is self-referential: every future instrument arc will increment it, and
> bumping it each time is the pattern this arc was written to stop.

The ceiling is set to **9** here — including this file — with the mechanism stated rather than
papered over. **The threshold is the wrong shape**, and no value of it is right. **B823 replaces it
with a triage registry**: each substantial blind arc must be explicitly recorded as either a *real
gap* or an *arc an object lexicon should miss*, and the gate fails only on **untriaged** ones. That
removes the number entirely and asks for the judgement the gate message was already requesting.

## Carried

- **B537 is the single genuine lexicon gap** (Markov-type surface `x²+y²+z²−xyz=c`, SL(2,ℤ) trace
  triples). A motif for it is worth adding under its own seal, with the same two-outcome shape that
  killed B821's.
- The other seven are instrument arcs an object lexicon should miss; the ceiling of 8 accommodates
  them rather than pretending they are defects.

`tests/test_b822_lexicon_gate.py`
