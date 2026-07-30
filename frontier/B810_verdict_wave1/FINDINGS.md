# B810 — W1 wave 1: 290 verdicts authored, coverage 4.1 % → 43.1 %

cc banking seat, 2026-07-30. Fan-out of the W1 authoring wave, gated on B809's measured
**κ = 0.842**. Repository-instrument scope; nothing to `CLAIMS.md`.

## What ran

12 parallel readers × 25 arcs, then a 3-agent audit. **15 agents, 0 errors, 0 empty results.**
Each reader received **arc IDs only** and resolved its own paths — deliberately, because a first
attempt with hand-supplied directory names had them wrong.

| | |
|---|---|
| verdicts returned | **300** (12/12 slices, 0 duplicates) |
| written | **287** |
| skipped — no such directory | 7 |
| skipped — already authored (never overwritten) | 3 |
| **withdrawn after review** — authored from non-`FINDINGS.md` sources | **3** |
| **coverage** | **30 → 317 of 742 arcs = 4.1 % → 42.7 %** |

Distribution: **PROVED 182 · NEGATIVE 94 · OPEN 22 · RETRACTED 2**; 13 flagged `instrument`;
**28 `supersedes` links recorded** — the first edges of that kind in the corpus.

## The honesty test, supplied by cc's own error

cc hand-transcribed 300 IDs into the workflow arguments and **got nine wrong**: six identifiers with
no directory at all, three already carrying authored verdicts. That mistake accidentally produced
the test that mattered most.

**All six non-existent arcs came back `OPEN` / "directory not found", with claims stating plainly
that no content existed.** Not one reader invented an arc. The instruction to prefer *"directory not
found"* over invention was written into the prompt as a precaution and it held under a live
9-in-300 fault rate.

The three already-authored verdicts were **skipped, never overwritten** — the writer refuses to
replace an authored verdict by construction.

**A third case, and it was withdrawn rather than kept.** Three further transcribed IDs pointed at
directories that exist but hold **no `FINDINGS.md`** — `B68` (has `FINDINGS_E.md`), `B263` (a
script), `B73` (a README). The readers found the real content in those files and authored honest,
substantive verdicts from it. **That is resourceful, not fabricated** — and it is still **outside
the declared method**, which was *read `FINDINGS.md`*. The three verdicts were **deleted**, because
the wave's provenance claim ("every wave-1 verdict authored from a FINDINGS.md") has to stay true.
Keeping good work that entered through an error would have quietly falsified it.

## Two results reported with their weaknesses, not without

**1. The audit found nothing, and that is weak evidence.** 36 of 36 sampled verdicts judged
defensible, 0 disputed. Two reasons not to take that at face value:

- **The sample was not random.** The script took the *first three* of each slice — i.e. the
  lowest-numbered arcs — so it systematically sampled the earliest, most template-like arcs in every
  slice. That is a design flaw in cc's workflow script, not a property of the work.
- **An audit that disputes nothing is the vacuity pattern** this session has now flagged three
  times. 36/36 should be read as *"no defect found by a weak instrument"*, not as *"no defect"*.

**2. The predicted conservatism offset is visible but confounded.** B809 predicted a seat-to-seat
offset from n=2. Per-slice PROVED-rates:

```
0.48  0.364  0.619  0.583  0.600  0.583  0.600  0.720  0.625  0.917  0.500  0.792
                                          min 0.364   max 0.917   spread 0.553
```

A 55-point spread is large. **But the slices are chronological**, so the spread mixes two causes:
genuine differences in what each era produced, and reader-to-reader labelling bias. **This design
cannot separate them** — doing so needs overlapping slices, which wave 1 did not have.

Recorded as **unresolved**, because attributing the spread to either cause without the overlap
would be exactly the kind of unearned reading the programme bans.

## What moved in the forcing graph

| | before | after |
|---|---|---|
| arcs with no verdict | 704 | **422** |
| faces with no proved arc | 6 of 11 | **1 of 11** (`emittance-lengths`, 2 arcs) |
| chain links on unverdicted arcs | 22 | 19 |

Five of the six faces that had **no proved arc** now have one. `arcs on no face` is unchanged at 572
— as expected, since face-attachment is a separate axis and this wave authored **verdicts**, not
faces.

## Residual

- **Wave 2**: 422 arcs remain. Slices must **overlap** so the conservatism offset can be measured
  instead of confounded.
- **Re-audit wave 1 with a random sample.** The 36/36 result does not license skipping it.
- The six non-existent IDs came from cc's transcription; the pool file on disk was correct
  throughout.

`tests/test_b810_wave1.py`
