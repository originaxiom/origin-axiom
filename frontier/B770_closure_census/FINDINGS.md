# B770 FINDINGS — THE CLOSURE CENSUS (Phase 0 of the Closure Program)

*2026-07-23. Prereg sealed 7682759b BEFORE any classification ran. Workflow
wf_4f2f28dd-762: 87 agents, 0 errors — 10 extraction agents (10/10 sources
delivered), 1 dedup-merge (groups-only contract after a first-run output-ceiling
failure; extraction results replayed from cache), 44 classify/verify agents in
batches of 8, adversarial pass on every closure verdict. cc spot-verified a
random sample (seed 770) by hand before banking.*

## Verdict

**The record's complete open surface is 352 unique items (431 raw, 10 ledgers),
now each in exactly one of the six sealed states:**

| state | n | meaning |
|---|---|---|
| LIVE | 225 | computable now — phased 1:56, 2:74, 3:50, 4:11, 5:20, unassigned:14 |
| EXTERNAL | 50 | in-sandbox exhausted; specialist register |
| CLOSED | 39 | banked two-outcome answer, verified citation, adversarially upheld |
| STALE | 27 | superseded by later banked arcs |
| CONSTITUTIVELY-OPEN | 6 | openness is itself the proven structure |
| WALLED | 5 | a no-go theorem in hand |

## The machinery's catch

The adversarial pass **refuted 16 candidate closures and reverted them to LIVE**
— each refutation names concrete unrun work (e.g. OI-046's convolution-mechanism
WHY, OI-108's B470 RF-continuations "never run anywhere in the repo"). The
no-unearned-closure invariant (prereg rules 1–3) held: every surviving
CLOSED/WALLED/STALE row carries a citation the classifier opened and verified,
then survived a refutation attempt. 71 closures were upheld.

## Integrity (locked in tests/test_b770_census.py)

1:1 items↔rows; no duplicate ids; the exact counts; the no-unearned-closure
invariant; refuted⇒LIVE; the six-state alphabet. The census self-referentially
classified its own launch row STALE (correct — it happened) and the cc3
close-out rows STALE against commit ef21c7f4 (correct).

## The courier diff

The courier's tier list entered through docs/CLOSURE_PROGRAM.md (already the
adjudicated version). No new divergence beyond the receipt's: their tier
structure survives inside the phase lists; their stale counts were already
corrected at the receipt.

## What Phase 1 inherits

The 56 phase-1 rows (the mechanical lane) — headlined by the residual quartet
(WALL-7 now 18/865; B685 3-integrality; TOMB-L310; TOMB-L34) and B500's wrap.
The 14 unassigned reverts get phases at the Phase 1 planning step. The owner
checkpoint is next: the map is the deliverable; nothing launches without the go.

Gate 5 / Gate 5-Q: structure only; no values; nothing to CLAIMS.
