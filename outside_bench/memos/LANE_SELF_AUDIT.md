# THE LANE SELF-AUDIT — 112 pairs re-run: ZERO failures, ONE genuine drift, and the audit's own instrument produced false positives
## (outside bench memo 140, 2026-08-29; prompted by codex finding two defects in this lane in a single pass)

**Why.** codex's audit found a reasoning gap (bench error #13) and a
reproducibility defect (six certificates on floating refs) **in one pass**.
Neither was exotic. **That is evidence this lane had not been audited by
the standard it applies to everyone else.** So: re-run every certificate
against the pinned source and diff it against its vendored output.

## THE RESULT

| | |
|---|---|
| auditable certificate/output pairs | **112** |
| **FAILURES (does not run)** | **0** |
| **STABLE (byte-identical to vendored)** | **111** |
| **GENUINE DRIFT** | **1** |

**Zero failures is the number that mattered most, and it is clean.**

## ⚠ THE AUDIT'S OWN INSTRUMENT PRODUCED FALSE POSITIVES

The first pass reported **15 drifts**. **All but one were artifacts of the
harness:** the first background launch survived when the run was
relaunched, so **two processes executed concurrently and shared the same
per-certificate temp file**, clobbering each other's captures. Every one
of the fourteen was **STABLE** on clean serial re-check
(`amphichiral_word`, `c1_weyl`, `dark_tower_counts`, `fence_independence`,
`first_beat_law`, `habiro_at_zeta`, `peripheral_identity`, `second_climb`,
`uniqueness_chain`, `yukawa_clock`).

**Recorded rather than quietly re-run.** This is the **third** time this
session an instrument of mine needed checking against itself — after the
`vol` / "in·**vol**·ves" substring match, and the keyword staleness flag
on Q2. **A detector's own output is evidence, not a result.**

## THE ONE GENUINE DRIFT — predicted before the re-check returned

`leap1_propagation.py`. **Predicted in the interim bank**, on the ground
that it sweeps this bench's own `.md` corpus, which grows with every memo
— codex's **third** charge, *"self-scan growing files"*, which I had only
checked against their first two.

**And the defect is worse than "the file grew."** The original swept the
**live worktree mid-turn**, so its output was **not a function of any
committed state**: no commit reproduces memo 131's banked "31 occurrences
across 12 documents", because that count existed only between writes
inside a single turn. **A certificate whose output no commit can
reproduce is not a certificate.**

**Fixed:** the sweep is pinned to **`38b5f578`** — the commit at which the
payment was made, which is the semantically right frame ("the propagation
as of the payment"). Verified **byte-identical across consecutive runs**
and matching the re-vendored output.

### ⚠ MEMO 131'S P1 FIGURES ARE CORRECTED
**Was:** 31 occurrences across 12 documents (unreproducible).
**Now, at the pinned commit:** **74 occurrences across 13 documents.**
**Memo 131's substance is untouched** — the P1 count was decorative
(supporting "the sweep is mechanical, not memory"); the load-bearing
content is the WAS/NOW state table and the two overstatement corrections
(T1: the CP sign is internal to the clock, not forced, adding no bit;
T2: matter-over-antimatter is doubly conditional). Neither depends on the
count.

## WHAT THIS SETTLES

**codex's audit is three for three on this lane** — floating refs, the
Cartan-vs-SU(2) reasoning gap, and self-scan growing files. I found the
third only because I took their charge seriously enough to look for it
here instead of assuming it was about main.

**And the lane is now genuinely reproducible:** every certificate runs,
111 of 112 were already byte-stable, and the twelfth is fixed at the
source. The pinned-source module (`certificates/_oa_source.py`) plus this
sweep's commit pin close the class.

**Fence.** This audit checks reproducibility, not correctness. **A
certificate can be perfectly byte-stable and still reason wrongly** —
bench error #13 was exactly that, and no re-run would ever have caught
it. That class needs a reader, which is what codex was.
