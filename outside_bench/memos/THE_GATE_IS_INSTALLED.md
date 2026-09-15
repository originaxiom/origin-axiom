# Memo 217 — THE GATE IS INSTALLED: a cell's two artifacts can no longer contradict each other silently

**Authorization:** the owner, this session.
**Where:** branch `<remote>/outside-bench`, as a **proposal**. Main is not touched by this bench.
**New files:** `scripts/checks/artifact_pair_gate.py` · `tests/test_artifact_pair_gate.py`
**Output:** `outside_bench/outputs/artifact_pair_gate.txt`

---

## 0. Exhausted first — and the corpus already had the expensive half

`scripts/checks/instrument_freshness.py` **already exists** (B1054, Review 1) and attacks the
same disease from the other side: it **re-runs** every `verify.py` instrument and reports the
ones whose committed `results.json` is *"a LIE."* Its own docstring names the mechanism —
*"`results.json` is a CACHE, written once at banking time and committed … so the lock
validates the cache against itself and cannot see the drift. **By construction.**"*

**Read, not assumed:** it scans `verify.py` + `results.json` pairs, and **never reads
`output.txt`.** A different population and a different signal. The new gate is the cheap,
complementary half — a string comparison, sub-second, no re-running — and it covers the side
`instrument_freshness` cannot see: the **text**.

## 1. What the gate decides

> A pair is a **MISMATCH** when **both** artifacts carry a verdict and the text's verdict
> appears among **none** of the JSON's. A cell carrying a verdict on only one side is a
> **formatting gap**: reported, not failed.

The only judgement in the file is verdict extraction, and it is stated in the docstring:
from `output.txt`, the **last** match of `(FINAL )?VERDICT:\s*(\S+)` — cells print their
decisive verdict last, sometimes behind a log timestamp, sometimes after a `=== VERDICT ===`
banner; from `results.json`, **every string-valued `verdict` key at any depth** — some cells
nest theirs, and a deliberate second reading such as `verdict_under_universal_reading` is
**not** a `verdict` key and is ignored.

## 2. The census at HEAD

> **`artifact-pair-gate: ok` — 83 cells carry a verdict on both sides and all agree; 22
> carry one on a single side.**

**The population is larger than memo 212's 75, and that is the extractor improving, not the
corpus drifting:** memo 212's reader matched only `^VERDICT:` at the start of a line, which
misses the `[ 860.0s]   FINAL VERDICT: …` form. Stated here so the number change is not
later read as a regression.

## 3. The bite control, and the part that matters most

`--selftest` (MB12) — **PASS**: three pairs that **must fire**, five that **must stay
quiet** (agreement; nested/extra verdicts; each one-sided case), four printed-verdict shapes
the extractor must parse, and one nested-JSON case.

And the strongest check, because a gate on a clean corpus is a gate nobody watches:

> **HISTORICAL REGRESSION.** The gate was run against the three real contradictions as they
> stood **at the commit before their repair**, read directly from the git blobs:
>
> | cell | text | json | fires |
> |---|---|---|---|
> | `P2W5-L72` | `RESOLVED-A` | `['UNRESOLVED']` | **True** |
> | `W2-270` | `UNRESOLVED` | `['RESOLVED-B']` | **True** |
> | `W4-017r` | `RESOLVED-A` | `['PENDING_PART_B']` | **True** |
>
> All three fire. Those pairs are **transcribed into the lock**, so it cannot go vacuous the
> moment the corpus is clean — which is exactly when a gate stops being looked at.

`tests/test_artifact_pair_gate.py`: **5 tests, 0.38 s.**

## 4. What the gate does NOT do — the fence

- **It does not re-run anything.** A cell whose *numbers* drifted while its verdict string
  stayed put passes this gate untouched. That is `instrument_freshness`'s job, and it
  remains the stronger check.
- **It does not fix the root cause.** The two artifacts are still written by separate paths:
  `results.json` from inside `compute.py`, `output.txt` from a shell redirect. **The gate
  detects the divergence; it does not prevent it.** Prevention means writing both in one
  process exit path, in each cell's own harness — **113 cells**, and still main's call, not
  this bench's.
- **It reads verdict strings, not meaning.** Two cells agreeing on the word `RESOLVED-A`
  while disagreeing about what was resolved would pass.

## 5. Status of the corrections lane after this

| | |
|---|---|
| the twelve stale status lines | superseded in place, memo 216 |
| the three contradicting artifact pairs | regenerated from their own committed code, memo 216 |
| the census | **0 contradictions**, and now **gated** |
| the root-cause harness change | **named, not done** — main's call |
