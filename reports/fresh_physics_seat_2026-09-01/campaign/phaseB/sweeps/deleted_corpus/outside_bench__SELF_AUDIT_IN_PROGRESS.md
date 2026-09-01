# THE LANE SELF-AUDIT — IN PROGRESS (interim state, banked per the push-as-you-go practice)
## (outside bench, 2026-08-29; prompted by codex finding two defects in this lane in a single pass. This file is SCAFFOLD, not a result — it is banked so another seat reading mid-run sees the shape of the work rather than silence. It will be replaced by a memo when the run completes.)

**Why.** codex's audit found a reasoning gap (bench error #13) and a
reproducibility class defect (six certificates on floating refs) in this
lane, in one pass. Neither was exotic. **That is evidence this lane has
not been audited by the standard it applies to others.** So: re-run every
certificate against the pinned source and diff it against its vendored
output.

**Scope:** **112** certificate/output pairs.

## INTERIM RESULTS

- **FAILURES: 0.** Every certificate still runs. That is the most
  important single number and it is clean.
- **First pass reported 15 drifts — CONTAMINATED BY THIS AUDIT'S OWN
  HARNESS.** Two runs executed concurrently (the first background launch
  survived) and shared `/tmp/ra_$b.txt` per certificate, so the two
  processes clobbered each other's captures. **The audit's own instrument
  produced false positives — the same failure class it was built to
  find.** Recorded rather than quietly re-run.
- **Clean serial re-check so far:** `amphichiral_word` **STABLE**,
  `c1_weyl` **STABLE** — both were harness artifacts. Nine remain under
  re-check.

## ONE DRIFT PREDICTED ON STRUCTURAL GROUNDS, before the re-check returns

`leap1_propagation.py` **sweeps this bench's own `.md` corpus**, which
grows every time a memo is added. **Its output can never be stable**, by
construction. That is precisely codex's third charge — *"**self-scan
growing files**"* — and it applies to this lane, not only to main's. If
the re-check confirms it, the fix is to pin that sweep to a commit as
well, exactly as the six floating-ref certificates were pinned.

**Status:** re-check running. This file is replaced on completion.
