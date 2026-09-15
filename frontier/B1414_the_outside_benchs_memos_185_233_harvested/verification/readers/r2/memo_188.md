# Reader r2 — Memo 188 (THE_VIEW_FROM_ABOVE.md)

## 1. HEADLINE
"THE VIEW FROM ABOVE, measured before interpreted": the programme's characteristic failure is
"entropy in its own instruments," not error — a census of 1125 banked arcs showing 65.2% PROVED /
26.8% NEGATIVE / 1.0% RETRACTED, a claims ledger 138 arcs stale, and a `depends_on` field that
looked decayed. Dated **2026-09-09**, with three same-day addenda that substantially revise §3 and
§5's own instance count (final state: the pattern rests on **two** instances, not four).

## 2. CLAIMS
1. Census: 1125 banked arcs, 734 PROVED (65.2%), 302 NEGATIVE (26.8%), 78 OPEN (6.9%), 11
   RETRACTED (1.0%) — **computed, stands** (memo re-ran clean on a fresh tree per Addendum 3).
2. `CLAIMS.md`'s highest reference is B1082; 138 arcs banked since; `outside_bench` appears 0
   times in `CLAIMS.md` against 192 certificates / 152 memos — **computed, stands**.
3. §3 original: `depends_on` "adopted at B800, ran at 77%, decayed to zero" — **WITHDRAWN by
   Addendum 2**: the census was run on a tree 126 commits behind `origin/main`; on `origin/main`
   the newest era (B1200–1399) shows `depends_on` at **61%** with the richest verdict records of
   any era (mean 8.8 fields). Corrected series: 3%/2%/2%/2%/77%/26%/**61%** — a dip and recovery.
4. 14% of arcs are process-named (audit/sweep/harvest/etc.); 7 of the 12 most recent — **computed,
   stands** (not revisited by any addendum).
5. §5 interpretive claim "programme's characteristic failure is entropy in its own instruments,"
   originally supported by **four** instances — **NARROWED across two addenda to two surviving
   instances**: (i) a minus sign lost twice on download (`CJTwist`, `rec.twist.knot`) — stands;
   (ii) `instrument_freshness.py` blind on 2 of 217 arcs (not 152, per Addendum 2's re-measurement
   on main — WORSE than originally reported) — stands. The `depends_on` instance is withdrawn
   (claim 3), and the "`PROGRESS_LOG.md` quiet for ten days" instance is **WITHDRAWN by Addendum 3**
   — the log had a dated section for every day 2026-08-31…2026-09-09; the "quiet" reading came from
   the same 126-behind stale tree (`fba45fc2`) as claim 3's error.
6. §6 interpretive: bottleneck is target selection, not verification, illustrated by R83 (`c_eff`
   route was never going to be evidence) — DOCUMENTARY / interpretive, not independently re-graded
   here.
7. Addendum 1 (F188-1 discharged): the promotion gate is a **"batch mechanism that works,"
   replaced by a per-item trickle** — 2026-07-03 batch adjudicated 63 candidates, +54 promoted; the
   trickle since delivered exactly **2** promotions ("Promotion logged" ×2) while arc numbering ran
   B426→B1220 (≈795 new arcs); 1 of the audit's own 7 named queued candidates has landed — verdict:
   **throughput mismatch, not obstruction, not a firewall** — computed, stands.
8. Standing rule adopted (Addendum 3): "when a diagnosis rests on several observed absences, the
   absences are not independent evidence until each has been re-read on a tree at `origin/main`" —
   a methodological rule, DOCUMENTARY.

## 3. CERTIFICATE
- `certificates/corpus_census.py` — **exists** (`outside_bench/certificates/corpus_census.py`).
- `outputs/corpus_census_out.txt` — **exists**; its final section (§5, "THE OUTSIDE BENCH's
  FOOTPRINT") reads: *"certificates : 192 / memos : 152 / occurrences of 'outside_bench' in
  CLAIMS.md : 0"* followed by *"EVERYTHING ABOVE IS A COUNT. What any of it MEANS is
  interpretation and lives in memo 188..."* — **agrees** with the memo's headline framing (counts
  vs. labelled interpretation) and with claim 2's numbers.
- Addendum 1's certificate `certificates/promotion_throughput.py` / output
  `outputs/promotion_throughput_out.txt` — **both exist**; tail reads *"the diagnosis is not
  obstruction. It is a THROUGHPUT MISMATCH..."* and *"PROGRESS_LOG.md's last dated section is
  2026-09-09 (1 day ago)... The earlier reading of this as an instance of the entropy pattern DOES
  NOT HOLD on this tree"* — **agrees** with claim 7 and pre-empts Addendum 3's own correction (the
  certificate itself, on the day-later re-run, already shows the log was current — Addendum 3
  documents that a still-earlier run had misread it).
- No seal on this memo (Gate 5 pure counting, no seal required per the bench's own convention for
  non-preregistered counting memos). No sha256 to check.

## 4. ON MAIN ALREADY?
1. **Census numbers (claim 1):** (c) NOT reproduced or cited anywhere in `docs/` or `frontier/`
   under this framing; `docs/` tracks per-arc verdicts, not a rolled-up census. No contradiction.
2. **`depends_on` recovery to 61% (claim 3, as corrected):** (c) NOT independently checked here
   against current main (`b94ed03a` was the tree Addendum 2 used; main has since advanced past it,
   e.g. to B1413+). Re-running `corpus_census.py`'s depends_on section against HEAD is exactly the
   §5 recipe below.
3. **`instrument_freshness.py` exists and is a tracked instrument** — confirmed:
   `scripts/checks/instrument_freshness.py` is present in the repo (not just `outside_bench/`).
   (a) already on main, cited by name in the memo itself as the corpus's own tool.
4. **F188-1 (batch-vs-trickle) / F188-2 (re-populate `depends_on`, standing census) / F188-3 (one
   chain not one more node):** F188-2's specific ask — "make `corpus_census.py` a standing
   instrument" — is **(c) NOT on main**: `scripts/checks/` contains `forcedness_census.py`,
   `point_census.py`, `sense_census.py`, `instrument_freshness.py`, `paper_chain_table.py`,
   `paper_provenance.py`, `retraction_sweep.py`, but **no `corpus_census.py`** — the certificate
   lives only under `outside_bench/certificates/`, never promoted into `scripts/checks/`.
5. **`CLAIMS.md` still shows 0 occurrences of `outside_bench`** (checked live on this tree,
   2026-09-16): `grep -c outside_bench CLAIMS.md` → `0`. (a) confirms claim 2 is still true on the
   current tree, i.e. the finding has NOT been overtaken by a later fix.

## 5. NEEDS COMPUTATION HERE
- **Claim 1 (census):** re-run `outside_bench/certificates/corpus_census.py` (it is a standalone,
  `__file__`-relative script) against current `origin/main` HEAD and diff the PROVED/NEGATIVE/OPEN/
  RETRACTED percentages and the `depends_on`-by-era table against the numbers quoted in the memo and
  in Addendum 2. Expected: PROVED share roughly similar (±2pp), `depends_on` for the newest era at
  or above 61% if the recovery held, higher raw arc count (>1204).
- **Claim 3/5 (the standing rule):** before trusting any future "N instances of entropy" claim from
  this lane, require it to state `git rev-parse HEAD` and `git rev-list --count HEAD..origin/main`
  the way `promotion_throughput.py` now does (Addendum 3's fix) — DOCUMENTARY (a rule, not a number),
  but checkable: run `git log -1 --format=%H` on the certificate's own tree at time of running.
- **Claim 7 (batch-vs-trickle):** count "Promotion logged" occurrences in `PROGRESS_LOG.md` since
  2026-09-09 to see whether the trickle continued or a new batch ran — `grep -c "Promotion logged"
  PROGRESS_LOG.md` restricted to sections dated after 2026-09-09.

## 6. SUPERSESSION
- §3's `depends_on` "decayed to zero" claim: **withdrawn in place by Addendum 2** (same memo).
- The "`PROGRESS_LOG.md` quiet for ten days" claim: **withdrawn in place by Addendum 3** (same
  memo) — both failures traced to the same 126-commits-stale tree `fba45fc2`.
- No later memo in `outside_bench/INDEX.md` past row 188 revisits memo 188 by number (grep of
  `memo 188` after its own row found only a *different* memo's mention of "memo 188's master
  pattern" being independently anticipated by an internal instrument, not a correction).
- Net effect: the memo's own addenda already did most of the auditing a later reader would do —
  the surviving claim is narrower than the headline as originally stated (four instances → two),
  and the memo says so loudly. Nothing outside the memo has superseded it further.

## 7. GRADE PROPOSAL
**REGISTER** (documentary, with one small REPRODUCE-AND-BANK item). The census and its
self-corrections are a governance/meta finding, not a physics result — Gate 5 declares "pure
counting... no measured physical value." The one thing worth an actual arc row is re-running
`corpus_census.py` against current HEAD (§5 above) to see whether `depends_on`'s recovery to 61%
held or is itself now stale — everything else here is already either withdrawn by the memo's own
addenda or is a process recommendation (F188-2/F188-3) that plainly has NOT been acted on (no
`corpus_census.py` under `scripts/checks/`).
