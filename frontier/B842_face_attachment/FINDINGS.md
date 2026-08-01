# B842 — face attachment succeeds where the keyword classifier failed, and finds the existing attachment unreliable

cc banking seat, 2026-08-01. **Prereg `292733956195849d`, sealed before the fan-out.** Gate 5;
nothing to `CLAIMS.md`.

## The gate

| | |
|---|---|
| **Fleiss' κ** (12 raters, 16 shared arcs, **12-way** judgement) | **0.8732** |
| bootstrap 95 % CI | **[0.7388, 0.9603]** |
| sealed gate | κ ≥ 0.60 |
| **verdict** | **PASS** — CI lower bound clears it, no marginal flag |

**B806's keyword classifier scored precision 0.45 and over-predicted by 55 %. A reader panel scores
κ = 0.87 on the same task.**

> **This does not contradict B806 — it tests a different instrument.** B806's conclusion, *"face
> attachment is not mechanizable"*, **stands as written**: a mechanical matcher cannot do it. What
> is now shown is that **the task is not ill-posed** — the failure was the instrument, not the
> question. B821's lesson generalises: **a regex matches mentions; a reader can tell mentions from
> subjects.**

**My prediction was wrong, and the prereg said what that means.** I expected **κ ≈ 0.55–0.75** and
wrote: *"if κ lands above 0.80 I will have badly underestimated the panel, and that gets said
plainly."* **It landed at 0.8732. I underestimated the panel** — for the second time in two arcs,
after B841's 35 % vs 70.7 %. I also expected **`none` ≳ 25 %**; it came in at **14.5 %**, so the
eleven faces span the corpus better than I assumed too.

## The finding: the EXISTING attachment disagrees with the panel on 44 % of the calibration

**Consistency against the kill-graph's own attachment: 58.3 % per judgement, 56.2 % by panel mode
(9 of 16).** Seven disagree, several unanimously:

| arc | corpus | panel |
|---|---|---|
| **B296** | `children` | **12/12 `none`** |
| **B523** | `hearing` | **12/12 `none`** |
| **B515** | `coupled-double` | **12/12 `hearing`** |
| **B372** | `coupled-double` | **11/12 `congruence-tower`** |
| **B486** | `emittance-lengths` | **11/12 `being`** |
| B237 | `congruence-tower` | 9/12 `hearing` |
| B619 | `mtc-overlay` | split 6 `hearing` / 4 `meeting` / 2 `mtc-overlay` |

**On the two clearest cases the panel is right, and the corpus is wrong.** B296 is *"a red-team plus
prior-art audit of an already-banked arc"*; B523 *"re-examines the programme's own negative verdicts
for premature leaps"*. **Both are methodology arcs, and the corpus had attached them to object
faces.** The panel's unanimous `none` is the correct reading.

> **A panel at κ = 0.87 that agrees with the corpus only 56 % of the time is evidence about the
> CORPUS, not only about the panel.** The existing 166 attachments predate any calibration.

**Nothing existing is relabelled here.** Wave 3 established the rule: **one panel is an opinion; a
replicated one is a measurement.** B834 relabelled only after B832's finding replicated
independently. **This is one panel, so it is recorded as a flagged discrepancy and nothing more.**

## What was written

| | |
|---|---|
| attached to existing kill-graph records | **123** |
| new face-only records | **343** |
| **skipped — panel judged `none`** | **79 (14.5 %)** |
| existing attachments overwritten | **0** |
| **records carrying a face** | **166 → 673** |

**`none` was used 79 times and that is the design working.** B806's classifier failed by
over-predicting 55 %; a panel that never declined would have repeated it.

The distribution: `being` 134 · `hearing` 107 · **`none` 79** · `sln-tower` 62 · `mtc-overlay` 42 ·
`coupled-double` 30 · `children` 29 · `meeting` 28 · `congruence-tower` 23 ·
`emittance-eigenvalues` 8 · `emittance-lengths` 2 · `infinite-hecke` 1.

**The two `emittance-*` faces and `infinite-hecke` together take 11 of 545** — they are near-empty
across the corpus, which is a real observation about the taxonomy's balance.

## A tripwire that fired on its own success

`test_gaps_are_reported_not_hidden` asserted *most* arcs sit on no face, with the message *"if this
ever drops below half, the positives have been attached — update the arc."* **They have been:
383+ → 134 of 766.** Re-anchored to guard the attached state, **with a floor** so that "every arc has
a face" would now fail — because forcing an attachment is exactly the over-prediction that sank the
keyword classifier.

## Carried

- **The 166 pre-existing attachments should be re-read**, and **B296 / B523 in particular** look
  wrong. This wants a second independent panel before any relabel, per B834.
- 134 arcs remain on no face: the 79 judged `none` plus those with nothing readable.

`tests/test_b842_faces.py`
