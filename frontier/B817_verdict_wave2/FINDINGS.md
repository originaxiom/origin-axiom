# B817 — Wave 2: the reader-bias confound is resolved, and the gate that licensed it was narrower than the work it licensed

cc banking seat, 2026-07-30. 12 readers × (15 shared calibration + 47 disjoint) = **564 work
judgements + 180 calibration judgements**. Repository-instrument scope; nothing to `CLAIMS.md`.

## 1. The gate

| | |
|---|---|
| **Fleiss' κ** (12 raters, 15 shared items) | **0.9312** |
| bootstrap 95 % CI over items | **[0.7485, 1.0000]** |
| sealed gate | κ ≥ 0.75 → write; below → hold |
| **verdict** | **PASS (marginal)** — verdicts written |

**"Marginal" is applied by B815's rule, not by hindsight.** That rule — committed while this
workflow was still running and no rating had been seen — says a pass whose CI lower bound falls
below the gate is reported as marginal. Here the lower bound is **0.7485**, which sits **0.0015**
below 0.75. The point estimate clears the gate by 0.18. **The flag is pedantic and it is applied
anyway**, because a rule that is only honoured when it is comfortable is not a rule.

## 2. What wave 1 could not determine, now determined

Wave 1's per-slice PROVED-rate spanned **0.364 → 0.917**, mixing genuine era-differences with
reader-to-reader bias, and its design could not separate them. On the **identical** 15-arc block:

| reader | NEGATIVE | PROVED |
|---|---|---|
| 10 of the 12 readers | **5** | **10** |
| reader03 | 7 | 8 |
| reader07 | 6 | 9 |

> **Ten of twelve readers produced the exact same verdict mix on the same arcs.** The conservatism
> offset is essentially nil.

**Therefore wave 1's 0.364 → 0.917 spread was NOT reader bias — the eras genuinely differ.** That
is the question the whole calibration design existed to answer, and it is answered. The confound
was designed out rather than apologised for, and it resolved.

**Scoped honestly:** this establishes small reader bias *for the PROVED/NEGATIVE distinction* — see
§3, which is the reason that qualifier is not boilerplate.

Per-item, only two arcs drew any disagreement at all: **B429** (10 PROVED / 2 NEGATIVE) and
**B755** (11/1). The other thirteen were unanimous.

## 3. The flaw this run has, and it is mine

**The calibration block exercised only two of the four verdict categories.** All 12 readers used
only `PROVED` and `NEGATIVE` across the 15 shared arcs. The work blocks used four:

| | PROVED | NEGATIVE | OPEN | RETRACTED | share in categories the gate never tested |
|---|---|---|---|---|---|
| work judgements (564) | 311 | 179 | **68** | **6** | **13.1 %** |
| verdicts written (299) | 180 | 108 | **6** | **5** | **3.7 %** |

> **κ = 0.9312 certifies agreement on a two-category distinction, and it was used to license work
> on a four-category one.** It says nothing about whether readers agree on `OPEN` versus the rest —
> and `OPEN` is precisely the boundary call where wave 1's disagreements actually lived.

The calibration arcs were selected without checking that they exercised the vocabulary they were
meant to calibrate. **That is a design error in this run, caught here rather than by a later reader,
and it does not invalidate the 96 % of written verdicts in the tested categories.** The eleven
`OPEN`/`RETRACTED` writes rest on an untested part of the vocabulary and are flagged as such.

This is the same shape as the vacuity lesson already in `PRACTICES`: *check the criterion can pass
AND can fail.* Here the criterion could not even be **exercised** across the range it governed.

## 4. Writer safety — held, under a live fault rate

| outcome | count |
|---|---|
| verdicts **written** | **299** |
| already authored — **not overwritten** | 216 |
| no `FINDINGS.md` — skipped | 31 |
| **no frontier directory at all** | **17** |
| ambiguous directory (`B58` → 3 dirs) — skipped | 1 |

**All 17 readers who hit a nonexistent arc returned `OPEN` with an explicit "no frontier directory
exists" — zero fabrications.** That is the safety property that matters, tested by a real 3.0 %
fault rate rather than by assertion. `B58` maps to three directories (`B58_phaseA`,
`B58_sl4_tower_test`, `B58_stage1`); it was skipped rather than guessed.

**Coverage: 317 → 616 of 746 arcs (42.5 % → 82.6 %).**

## 5. The audit, and this time the number means something

Wave 1 audited the first three arcs of each slice and got 36/36 — uninformative, because a set
chosen after seeing the verdicts can be agreeable without anyone intending it. This audit used
**B816's committed seed (`20260730`) over the frame of what actually landed**, drawn *after* the
writes and therefore not steerable toward them.

> **20 of 20 verdicts match their arc's own `FINDINGS.md`.**

Including the cases most likely to break: **B780** is written `RETRACTED`, matching its
*"RETRACTED IN PART (B784 audit)"* header rather than its original claim; **B616** is written
`OPEN` — *"leaving the figure-eight's excess uncorroborated"* — rather than being rounded up;
and **B786**'s claim (*"the third generator is inversion ι, not reversal θ"*) stops precisely at
B786's own content instead of reaching forward into B787's later 4th-involution refinement, which
B786 itself lists only as an open possibility.

## 6. What this run does not do

- **No physics, no value, nothing to `CLAIMS.md`.** Verdicts label what an arc *established*.
- **No new lexicon.** The WHAT axis is still stale (B806).
- **No face attachment.** 573 arcs remain on no face; that is a separate axis.
- **No edges.** The forcing graph gains nodes, not edges — coverage is a precondition, not the goal.
- **130 arcs still carry no verdict**, mostly directories without a `FINDINGS.md`.

## Carried forward

1. **A calibration block that exercises all four categories** — the gap in §3. Any future wave must
   check vocabulary coverage of its calibration set *before* running, not after.
2. The 11 `OPEN`/`RETRACTED` writes sit in untested territory and should be re-read under (1).

`tests/test_b817_wave2.py`
