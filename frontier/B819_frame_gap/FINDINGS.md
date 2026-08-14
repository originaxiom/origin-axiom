# B819 — correcting B817: the verdict residue is a coverage-frame gap, not a data gap

cc banking seat, 2026-07-30. Repository-instrument scope; nothing to `CLAIMS.md`.

## The correction

**B817 stated that the remaining unverdicted arcs were "mostly directories without a
`FINDINGS.md`." That is wrong**, and it matters because it tells a reader there is nothing to do.

| | |
|---|---|
| frontier directories with **no** `arc_verdict.json` | **181** |
| of those, directories that **do** have a `FINDINGS.md` | **133** (73 %) |
| of those 133, **assigned** to a wave-2 reader but skipped | **17** (duplicate-directory arcs, e.g. `B58` → 3 dirs) |
| of those 133, **never assigned to any reader at all** | **116** |

| | |
|---|---|
| distinct arc ids in `frontier/` | **791** |
| ids assigned to some wave-2 reader | **579** |
| **ids never assigned to any reader** | **229** |

> **116 arcs carry real findings that no reader was ever given.** They were not judged and found
> wanting; they were never in the frame.

## Why the original statement was wrong

Wave 2's work list was built from a fixed set of **579** ids — 73 % of the 791 in `frontier/`. The
campaign plan expected coverage to reach "~99 %, the residue being arcs whose directories are
missing or non-standard." **That expectation was unreachable from the start**, because the frame
itself was incomplete, and nothing in the run measured the frame against the repository.

I then read the residue's *shape* off the failure counters — 31 `no_FINDINGS_md`, 17 `no_directory`
— which describe **only the arcs that were assigned**. Generalising those counters to the whole
residue is a sampling error: **the assigned set is exactly the set that is not representative of
what was left out.**

## The one genuinely non-standard case

`B519_re_mining` holds `CAMPAIGN.md` + `VERDICT.md` and **no** `FINDINGS.md`, so writer safety
correctly refused it. It is the **only** such arc — the "non-standard layout" category the campaign
anticipated turns out to have exactly one member, and 45 further directories hold only
`README.md` / `PREREGISTRATION.md` / campaign files.

B519 matters because **B525 cracked its `no external crossing` headline**, so the arc most in need
of a `RETRACTED` marker is structurally invisible to the ledger.

## What to do, and what not to

- **A third wave over the 229 unassigned ids closes ~116 of them**, and its calibration block must
  exercise **all four** categories (B817 §3, now in `PRACTICES`).
- **Do not** read this as 116 more `PROVED`s. They are unjudged, and the wave-1 spread (0.364 →
  0.917 PROVED-rate across eras, now known to be **real** rather than reader bias) means an
  unsampled era's rate is not predictable from the sampled ones.

## The transferable point

> **A coverage number is only as good as its frame, and the frame must be measured against the
> repository — not against the work list.**

Wave 2 reported "42.5 % → 82.6 %" accurately and its verdict-level audit was clean at 20/20. What
went unchecked was one level up: *were all the arcs even eligible to be counted?* The same shape as
B817's own calibration flaw — a measurement that is correct about the thing it measured, and was
used to speak about something larger.

`tests/test_b819_frame_gap.py`
