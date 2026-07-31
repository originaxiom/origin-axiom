# B827 — ten days of progress log went to a shadow file, and the gate for it had become unable to fail

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched. Found by the owner
asking a one-line question: *"are we always updating progresslog"*.

## The answer was no

| | |
|---|---|
| entries written to a shadow `PROGRESS_LOG.md` under `docs/` instead of the canonical `PROGRESS_LOG.md` | **37** |
| span | **B725 → B826**, 2026-07-20 → 2026-07-30 (**ten days**) |
| of those, present in the canonical log or the Q2 roll-off | **0** |
| commits this session that wrote to the shadow | 10 (vs 3 to the canonical file) |

The shadow was **created by accident** at commit `73d07f0e` (B725) and accumulated silently. It is
**not** the sanctioned roll-off — that is `docs/progress/PROGRESS_2026-Q2.md`, and none of the 37
appear there either. Its telltale: it had **no header at all**, opening mid-content on
`## B725 — THE BORN RULE`, while the canonical file opens *"Append-only, chronological… older
entries roll into `docs/progress/` by quarter."*

## Why the gate could not catch it — and this is the part worth keeping

`log-changelog-paired` compared **CHANGELOG's last-touched time against the canonical log's**:

```
if tb < ta:  fail        # ta = PROGRESS_LOG.md, tb = CHANGELOG.md
```

Once the canonical file stopped being written, **`ta` froze in the past**, so every later CHANGELOG
commit trivially satisfied `tb >= ta`.

> **A gate that watches a file nobody writes cannot detect that nobody writes it.** It did not
> merely miss this defect — it had become **incapable of failing at all**, and would have reported
> PASS forever.

This is a *fail-open by drift*: the gate was sound when written and was disarmed by a change
elsewhere, with no signal. The 2026-07-29 restart-resistance audit checked for gates that fail open
when **inputs go missing**; it did not check for gates whose input goes **stale**.

## What changed

**1. All 37 entries migrated verbatim into `PROGRESS_LOG.md`**, in original order, under a heading
that says what happened. Their dates overlap the entries above them — a consequence of recovery,
**recorded rather than smoothed over by re-sorting**, since the file is append-only.

**2. The shadow file is deleted**, and the one citation pointing at it (in the negatives-hunt
handoff) repointed — caught by `path-refs`, not by me.

**3. The gate now has two checks, both of which can fail:**

- **No shadow progress log may exist** anywhere outside the sanctioned archive. *This is the check
  that would have caught B827 on day one.* `legacy/` is excluded by name — a frozen import of the
  pre-2026-05-28 repository — so the check stays sharp everywhere else instead of being loosened
  into uselessness.
- **CHANGELOG may not run more than one commit ahead** of `PROGRESS_LOG`, encoding the standing
  *"same or next PR"* rule directly. On first run it reported **"CHANGELOG is 10 commits ahead"** —
  the exact damage, measured.

**Negative controls run:** planting a a shadow `PROGRESS_LOG.md` under `docs/` makes the gate fail and naming it;
removing it restores the pass.

## The fourth one, in two days

`REVIEWS.md`, `ROADMAP.md`, `PROGRESS_LOG.md` — three duplicated authoritative filenames found while
writing **one review** (Review 35, findings 6 and 7), plus the stale `REVIEWS.md` fork under `docs/` (deleted, B830)'s known **OI-239**.

> **Nothing in this repository prevented a second file with an authoritative name from existing**,
> and each shadow held plausible content, so opening the wrong one gave no signal. Two of the three
> were found by a *gate*; the third by the **owner asking a question**.

**R35-8 (the repo-wide sweep for duplicated authoritative filenames) is upgraded from a housekeeping
item to the highest-value open instrument task**, and the shadow-file check above is its first
enforced instance. **The sweep is not done here** — one filename is now gated; the rest are not.

## The transferable point

> **A gate proves a property held *at the moment it was written*. Nothing keeps its input the same
> file the work is going into.** Ask periodically not "does this gate pass?" but **"could it still
> fail?"** — B823 reached the same conclusion about the lexicon ceiling from the other direction.

`tests/test_b827_progresslog_recovery.py`
