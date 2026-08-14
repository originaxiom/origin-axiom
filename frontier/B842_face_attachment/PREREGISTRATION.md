# B842 — PREREGISTRATION: face attachment by reader panel, after a keyword classifier failed

cc banking seat, 2026-08-01. **Sealed before the fan-out.** Gate 5 absolute; nothing to `CLAIMS.md`.

## Why re-attempt something measured "not mechanizable"

B806 concluded **face attachment is not mechanizable** — and its evidence was a **keyword
classifier**: precision **0.45**, recall 0.63, **exact-set match 13 %**, over-predicting by **55 %**.

**That measured a mechanical matcher, not a reader.** It is the same instrument class that failed on
the lexicon, and B821's lesson applies directly: **a regex matches *mentions*, not *subjects*.** B806
also measured that **88 % of unattached arcs name a face in their text** — so the information is
present; keyword extraction could not resolve it.

**A reader panel is a different instrument**, and this campaign has calibrated it: κ = 0.9312 /
0.9305 / 0.9300 across three verdict runs, the last two on a four-category judgement.

> **This does not contradict B806. It tests a different instrument on the same task, and B806's
> number stands as the mechanical baseline to beat.**

## The frame, measured against the repository

| | |
|---|---|
| arc ids in `frontier/` | **810** |
| carrying a face (from `kill_graph`) | **166** |
| **no face** | **644** |
| of those, **readable** (have a findings document) | **601** |
| unreadable — nothing to classify from | 43 |

## Single primary face, so the gate is well defined

Face attachment is naturally **multi-label**, and Fleiss' κ is not defined for multi-label sets.
So readers return:

- **`primary_face`** — exactly one of the **11 faces** or **`none`** → this is what κ is computed on
- **`also`** — any additional faces, recorded but **not gated**

**`none` is a first-class answer.** An arc that touches no face must be labelled so; forcing an
attachment is exactly the over-prediction (55 %) that sank the keyword classifier.

## Gates

- **Calibration block: 16 arcs that ALREADY carry a face**, drawn by committed seed `20260730`,
  judged **blind**. This gives both **Fleiss' κ** (reader-vs-reader) **and consistency against the
  existing attachment** (reader-vs-corpus) — the pair that exposed a uniformly-drifted panel in
  wave 3.
- **κ ≥ 0.60 to write.** *Lower than the verdict waves' 0.75, and stated as a deliberate choice:*
  12 categories vs 4, and the keyword baseline sits at 0.45 precision. **A bar set at 0.75 for a
  12-way judgement would be stricter than anything this repository has demonstrated.** Below 0.60,
  attachments are **held, not written**.
- **Consistency reported, not gated** — as in B832, since inventing a threshold after the fact is
  setting a bar to a number I can estimate.
- **Writer safety:** never overwrite an existing attachment; never attach for an arc with no
  findings document.

## Two-outcome

- **κ ≥ 0.60** → attachments written; the WHERE axis extends from 166 arcs toward ~750.
- **κ < 0.60** → **held**, and **B806's "not mechanizable" is upheld for reader panels too** — a
  stronger and more useful negative than the keyword result alone, because it would show the task
  is genuinely ill-posed rather than merely hard to automate.

## Pre-stated expectation

I expect **κ ≈ 0.55–0.75** — materially harder than the verdict task (12 options, and faces overlap
by construction), and I would **not** be surprised by a fail. **If κ lands above 0.80 I will have
badly underestimated the panel**, and that gets said plainly.

I expect **`none` to be common** (≳ 25 %), because 644 unattached arcs is most of the corpus and the
face taxonomy was built from the *kill graph*, not from arcs in general — **the faces may simply not
span the corpus**, which is itself a finding.
