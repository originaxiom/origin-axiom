# Phase B — the full read (owner rule 2, 2026-09-01)

Owner's words: *"its also important to read all the arcs, belts and teats [tests] maybe through
the progresslog which is also important? both the one in main and in docs"*.

Read as: every frontier arc on every remote head, every verification belt inside them, every
test file, **guided by** the progress logs (root `PROGRESS_LOG.md`, `docs/progress/PROGRESS_2026-Q2.md`,
`docs/progress/REVIEWS.md`) — the log is the project's own account of what each arc established;
the read checks the arcs against that account and the tests against the arcs.

"All" is a number, not a word. Population, computed by `phaseB/build_packets.py` from
`git ls-remote --heads origin` (owner rule 1 — sweep every head before any absence claim):

| population | count | source |
|---|---|---|
| arcs on `main` (a5138424) | 1186 | working tree `frontier/` |
| arcs only on `audit/b775-braver-questions` | 6 | read-only worktree |
| arcs only on `claude/new-session-qor5up` | 30 | read-only worktree |
| arcs only on `paper/structure-genesis-first` | 87 | read-only worktree |
| `frontier/` root files (README, REPO_STATE, EXPERT_OUTREACH, …) | 7 | pseudo-arc |
| **arc records total** | **1310** (8130 files) | 131 packets |
| arcs with a `verification/` belt directory | 85 | inside the arc packets |
| arcs without `FINDINGS.md` | 57 | listed in `phaseB/MANIFEST.json`; read whatever they have |
| test files under `tests/` | 1122 | 14 packets |
| log entries: root / Q2 / REVIEWS | 860 / 133 / 52 | 11 chunks |
| distinct arc ids mentioned in the logs | 984 | `log_index/<arc>.txt` per arc (scratch) |

The other three heads (`claude/outside-bench`, `codex/seat-r001`, this seat) add no arcs beyond main.

"Belt" in this repo's usage (THE_SPINE B930 "independent dps-80 belt", MASTERPLAN "belt639",
"belt100", "belt2: two-prime") = an independent recomputation of an arc's result, usually by a
second seat, living in the arc's `verification/` directory, a `belt_*.py`, or a sibling arc. They
are read as part of the arc packets, with the reader asked explicitly whether the belt recomputes
or merely re-reads.

## Per-file read discipline (so 35 MB effective is honest, not "skimmed")

| class | rule |
|---|---|
| `*.md`, `arc_verdict.json` | read in full (cap 120 KB, then head) |
| code `*.py *.sage *.sh` ≤ 15 KB | read in full |
| code > 15 KB | head 120 lines + `grep -n "def \|assert\|print\|==\|sympy\|mpmath\|Fraction"` |
| data `*.json *.txt *.csv …` ≤ 30 KB | read in full |
| data > 30 KB | head 40 + tail 20 + `wc -l`; grep any number the FINDINGS quotes |
| binaries (`npz pkl png`) | listed, not read; note whether a `.txt`/`.json` twin exists |

Effective read load: 34.7 MB ≈ 8.7 M tokens over 131 arc packets (median 249 KB ≈ 62 k tokens each).

## Digest schema (strict; one object per arc, written to `phaseB/digests/arcs/<batch>.json`)

```
arc, source(head), files_read[], files_sampled[], files_listed_only[]
claim_of_record        — arc_verdict.json claim_one_line / status verbatim (or "no verdict file")
log_says               — one line: what the progress log says this arc established ("not in log" allowed)
log_consistency        — CONSISTENT | DRIFT (log stronger than arc) | CONTRADICTION | NOT_IN_LOG
load_bearing[]         — {what, where(file:line), kind: COMPUTED|ASSERTED|FITTED|IMPORTED|UNCLEAR,
                          reproducible_from_committed: yes|no|unknown, why}
belt                   — NONE | RECOMPUTES (independent code/prime/seed) | RE-READS (same numbers re-printed) | UNCLEAR
absence_claims[]       — {quote, where}   ← every "no X exists / not in repo / never computed" sentence
physics_content        — OBSERVABLE (names a measurable + value) | STRUCTURAL | NO_OBSERVABLE_CONTENT
red_flags[]            — {kind, detail, where}  kinds: FITTED_VALUE, CLAIM_EXCEEDS_COMPUTATION,
                          MISSING_WITNESS, GITIGNORED_WITNESS, RETRACTION_NOT_PROPAGATED, LOG_DRIFT,
                          NO_TEST, NUMERIC_ONLY_NO_EXACT, SELF_REFERENTIAL_LOCK, IDENTIFICATION_BY_TYPE,
                          SUPERSEDED_UNMARKED, OTHER
seat_note              — ≤ 2 sentences, fresh-eyes physics judgment
```

Tests digest (`phaseB/digests/tests/<batch>.json`, one object per file): `file, target_arcs[],
what_it_locks, lock_type: RECOMPUTES | COMPARES_TO_STORED | TAUTOLOGICAL | SMOKE | SKIPPED_OR_XFAIL,
hardcoded_constants[] {value, provenance_stated: yes|no}, red_flags[]`.

Log digest (`phaseB/digests/log/<chunk>.json`, one object per entry): `date, title, arcs[],
established (1 line), status_words[], retractions[], owner_elections_verbatim[], red_flags[]`.

## Workflow shape (owner opted in to multi-agent orchestration; 4-CPU box ⇒ 2 concurrent agents per workflow)

- **W-A / W-B**: arc packets 0–65 and 66–130, `pipeline` over packets → sonnet reader (effort medium)
  writes the digest file, returns a summary (schema-enforced). Two workflows so four readers run at once.
- **W-C**: 11 log chunks + 14 test packets, same pattern (sonnet; tests at effort low — mechanical).
- **W-D (synthesis, after all three)**: higher-tier agents over the digests: (1) red-flag rollup ranked by
  load; (2) absence-claims → `sweeps/absence_claims_phaseB.tsv` for `sweep_batch.sh`; (3) log-vs-arc
  discrepancy table; (4) load-bearing computations not yet recomputed by this seat → next recompute ring;
  (5) completeness critic ("which packet returned thin, which arc has no digest").
- **W-E**: run the sweep executor on (2); verdicts written by the seat (never delegated).

Guideline note: the default medium workflow size (<15 agents) is exceeded deliberately — the owner's
mandate is the whole population, and the readers are the cheap tier. No expensive agent reads; the
expensive tier only synthesizes.

Nothing in Phase B banks anything: digests live under this seat's `reports/` tree; findings go to cc
by relay under integrate-don't-merge.

## Progress

- 2026-09-01: packets built (`phaseB/MANIFEST.json`); W-A, W-B, W-C launched.
- 2026-09-01 (evening): all three reader workflows died on the session limit (reset 22:50 UTC) with 39 arc
  packets, 11/11 log chunks and 2 test packets landed; resumed from cache at 22:58 UTC (script copied to
  `phaseB/workflow_phaseB_readers.js`, same run ids). `rollup.py` extended with the test lock-type column.
- W-E executor written (`phaseB/sweeps/sweep_batch.py`): every absence claim the readers extracted is swept over
  all 7 remote heads and the ever-deleted-file corpus (15 materialised files). First full pass (425 claims): 341
  LEAD / 15 GENERIC / 50 NO_HIT / 19 UNSWEEPABLE — the LEAD rate was an artefact of `CHANGELOG.md` and the
  progress logs echoing every claim (239 of 341 leads had CHANGELOG.md in their top paths). Second pass
  separates those catch-all files into a DOC_ECHO status and stores the full substantive hit list
  (`absence_sweep_paths.json`); verdicts are written by the seat on the substantive LEADs only.
- Reader flags turned into recompute cells the same evening: R31 (B208, MATCH), R32 (B213, MATCH with four
  corrections and one provenance finding), R33 (eight trace-field/commensurability rows, all MATCH; bronze
  degree 8 resolves B840; m003/m004 common double cover), R34 (B252 E6 27/78, MATCH). See
  `recompute/R3_REPORT.md` dated closures.
