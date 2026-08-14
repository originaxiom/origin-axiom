# B832 — wave 3: κ held on four categories, my prediction failed, and the panel disagrees with the corpus in one direction

cc banking seat, 2026-07-30. **Prereg `ddb2ff0b25c2d777`, sealed before the fan-out.** Repository-
instrument scope; Gate 5 untouched.

## 1. The gate — and my pre-stated expectation was WRONG

| | |
|---|---|
| **Fleiss' κ** (12 raters, **16 shared arcs, all four categories**) | **0.9305** |
| bootstrap 95 % CI over items | **[0.8286, 1.0000]** |
| sealed gate | κ ≥ 0.75 → write |
| verdict | **PASS** — CI lower bound clears the gate, so no marginal flag |

**I predicted κ ≈ 0.75–0.90, *lower* than wave 2's 0.9312, on the reasoning that a four-category
judgement is strictly harder.** The prereg fixed the consequence in advance: *"if κ comes out ≥ 0.93
I will have been wrong about why wave 2 scored so well, and that must be reported rather than
smoothed."*

> **κ = 0.9305 against wave 2's 0.9312 — indistinguishable. I was wrong.** Wave 2's high agreement
> was **not** an artifact of its accidentally two-category block. The panel agrees at ≈ 0.93
> whether the vocabulary has two live categories or four.

That does **not** retire B817's caveat — a two-category block still *licensed* four-category work
without testing it, and B818 found 2 real errors in that residue. **The scope objection was valid;
my prediction of its numerical consequence was not.** Those are different things and only the
second was wrong.

## 2. The measure wave 2 could not compute, and it found something

**Consistency against the corpus: 79.7 %** per judgement (153/192), **81.2 %** by panel mode (13/16).

Three items disagree — and **every one is unanimous or near-unanimous, and every one moves toward
`PROVED`:**

| arc | corpus | panel | |
|---|---|---|---|
| **B61** | `OPEN` | **12/12 `PROVED`** | unanimous |
| **B556** | `OPEN` | **11/12 `PROVED`** | near-unanimous |
| **B746** | `NEGATIVE` | **12/12 `PROVED`** | unanimous |

> **This is exactly the failure mode the measure was sealed to catch: a panel can be perfectly
> self-consistent and uniformly drifted from the corpus, and κ is blind to it.** κ = 0.9305 while
> 3 of 16 items are read systematically differently.

## 3. What the three disagreements actually are — not drift, a VOCABULARY GAP

Reading them, all three are **the same kind of arc: a verified core plus an unsettled extension.**
B556 says so in its own header — *"the computational core is VERIFIED EXACTLY; the
tower-as-physics-ladder reading is banked as a labeled HYPOTHESIS."* B61: *"Numerical,
high-precision… **Not a symbolic proof**"*, resolving 22 of 24. B746 tested "golden all the way up",
found it **gapped**, and in doing so established a two-column structure.

**The four-category vocabulary forces one label onto arcs that genuinely carry both.** The corpus
resolved them toward *what remains unsettled*; the panel resolved them toward *what was established*
— and **the panel is applying the stated rule more faithfully**, since `PRACTICES` says the verdict
labels **what the arc established, not whether the programme's target was reached**.

**No verdict is relabelled here.** Three one-off edits would treat a vocabulary gap as three
mistakes. **The fix is a rule for mixed arcs, and it is registered rather than improvised** at the
end of a long run.

## 4. A serious execution error of mine, and its exact cost

**I hand-typed the reader work-lists instead of using the computed file.** The script had written
the correct 183 ids to `/tmp/wave3_args.json`; I sent a plausible-looking sequence instead.

| | |
|---|---|
| arcs sent | 183 |
| **actually in the frame** | **57** |
| already judged — sent in error | **126** |
| **frame arcs never sent to any reader** | **126** |

**Writer safety absorbed all of it**: 119 already-authored verdicts were **not overwritten**, 7 had
no directory, 6 no findings document, 1 ambiguous. **50 verdicts written, all valid.** Nothing was
corrupted; the cost is wasted reader effort and a wave that covered a third of its frame.

**This is the same error class as the earlier 300-id transcription (9 wrong) — but at 69 %.** The
correct list existed in a file and I retyped it. **Wave 3b has been relaunched on the recomputed
135-arc frame, copied verbatim.**

**κ is unaffected** — the calibration block was passed correctly and is the only input to the gate.

## 5. State

**Coverage 617 → 667 of 758 arcs (88.0 %).** Written mix: 27 `PROVED`, 23 `NEGATIVE`.

## Carried

1. **A vocabulary rule for MIXED arcs** — a verified core with an unsettled extension. The three
   calibration disagreements are all this shape, and it is the largest remaining source of
   reader-vs-corpus divergence.
2. Wave 3b's 135 arcs, in flight.
3. **Never retype a computed list.** The file existed both times.

`tests/test_b832_wave3.py`
