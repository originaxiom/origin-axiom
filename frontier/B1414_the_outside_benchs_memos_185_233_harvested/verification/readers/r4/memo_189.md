# Reader r4 — Memo 189 (THE_ANTIBODY_RUSTED_TOO.md)

## 1. HEADLINE
"THE CHECK BUILT TO CATCH RUSTED INSTRUMENTS HAS ITSELF GONE BLIND." — the freshness check
selects arcs by the literal pair `(verify.py, results.json)`; the corpus renamed its
instruments, so the check now sees 2 arcs out of 1125 (0.2%), and 2 of the 152 arcs that
carry exactly the structure B1054/Review 42 warned about. "IT STILL RUNS AND STILL PASSES: a
green check at 0.2% coverage answers 'is anything stale?' with a silence that reads as no."
**Date 2026-09-09.**

## 2. CLAIMS
1. `instrument_freshness.py` selects 2 of 1125 frontier arcs (0.2%) by the pair
   `(verify.py, results.json)`. — MEASURED
2. Widened-selector census: `probe.py` 145, `verdict.py` 23, `compute.py` 19,
   `results.json` 118, `verification/` 80 dirs; union carrying the B1054 structure = **152**
   arcs; check sees 2 of them, blind to **150**. — MEASURED
3. Interpretation (labelled): a green check at 0.2% coverage is *worse than no check* because
   it answers "is anything stale?" with a silence that reads as no. — INTERPRETATION
4. Repair specified: widen the selector 2→152, keep it non-mutating and a test-not-gate. —
   SPECIFIED, explicitly **not applied** ("this lane does not touch main").
5. Explicitly NOT claimed: that the 150 hidden arcs *are* stale — only that nobody can
   currently see. — NEGATIVE (scope limit stated by the memo itself)
6. **ADDENDUM 1** (2026-09-09): re-measured against `origin/main` at `b94ed03a` (the body was
   126 commits behind). Check still selects **2** arcs; `verification/` dirs 80→**145**; union
   152→**217**; blind count 150→**215**. Verdict: "the finding STANDS and was UNDERSTATED." —
   MEASURED / STANDS-UNDERSTATED
7. **ADDENDUM 2** (2026-09-09): full suite on a **clean worktree** of `main` @ `b94ed03a`:
   **11 failed, 6312 passed, 68 skipped, 1h19m28s** (6391 collected). — MEASURED
8. Four of the eleven failures read files the repo deliberately does not track (`.gitignore`
   line 20 `*.log`) or a relative path: `b1062_v2_block1.log`, `refresh_windows.log`,
   `sliceC/c_beat.out`, `results/real_grid.jsonl` — "never-could-have-passed", not drift. —
   MEASURED
9. `test_no_hardcoded_paths.py::test_no_absolute_machine_paths_in_tracked_text` itself FAILS
   on the same defect class the widened sweep found (an absolute `(scratchpad)/cloud_handoff/…`
   path, R90). — MEASURED
10. Remaining 6 failures listed for completeness (manifest staleness, an email/reviewer
    placeholder, an archive/manifest mismatch, two numeric assertion misses, one held-out
    design check). — MEASURED / DOCUMENTARY
11. Self-correction: the earlier framing ("the other seat's 21 existing failures") was a
    subset run against 6391 collected; the real full-suite number is 11, and "the count was
    the wrong thing to look at." — CORRECTED
12. Two trailing blockquotes (memo 188 addenda 2 & 3, reproduced at the foot of this memo's
    file): the `depends_on` instance is **SUPERSEDED** (series `3/2/2/2/77/26/61%`, a dip and
    recovery, measured on a tree 126 commits behind main) and the `PROGRESS_LOG.md` "quiet
    since 2026-08-30" instance is **WITHDRAWN** (log has a dated section every day
    2026-08-31→2026-09-09). These are corrections to memo 188, appended here for provenance,
    not new claims of memo 189. — WITHDRAWN (both, but attributed to memo 188)

## 3. CERTIFICATE
- `outside_bench/certificates/instrument_coverage.py` — **EXISTS**.
- `outside_bench/outputs/instrument_coverage_out.txt` — **EXISTS**. Tail: *"A green check with
  0.2% coverage is worse than no check... Nothing here says the hidden arcs ARE stale...
  What is established is only that nobody can currently see."* — **agrees** with the memo's
  headline verbatim.
- No seal is named for this memo (Gate 5 pure counting; INDEX.md grades it "1B", not a sealed
  claim), so there is no sha256 to check. Addendum 2's own full-suite run is reported inline
  in the memo, not as a separate certificate/output pair, and no seal is claimed for it either.

## 4. ON MAIN ALREADY?
1. B1054 / Review 42 / `instrument_freshness.py`'s docstring — **(a) already on main**,
   `scripts/checks/instrument_freshness.py` (docstring lines 1–26 quote exactly the passage
   the memo cites).
2. The narrow selector — **still true on current main**: `grep -n "verify.py\|results.json"
   scripts/checks/instrument_freshness.py` shows the pair-selector unchanged (line 55:
   `v, r = os.path.join(d, "verify.py"), os.path.join(d, "results.json")`) and a grep for
   `probe.py|verdict.py|compute.py|verification/` inside that file returns **nothing** — the
   widened selector from F189-1 is **(c) NOT on main**. The owner-register (line ~1884-1885)
   still lists "widen `instrument_freshness.py`'s selector, 2 → 152 arcs" as an open,
   unblocked action ("nothing. Your call").
3. The four "never-could-have-passed" artefacts — **(b) partially applied via the merge**:
   `git ls-files` confirms `frontier/B1062_bridge_cell/b1062_v2_block1.log`,
   `frontier/B1063_refresh_verdict/refresh_windows.log`, and
   `frontier/B1306_the_older_debt/verification/sliceC/c_beat.out` are now **tracked** on main
   (the `.gitignore` gained a `!frontier/*/verification/*.out` exception, commit `cd582111`,
   for exactly the P3-manifest reason the memo's own repair section names). `results/
   real_grid.jsonl` remains **untracked / absent** — that one instance of claim 8 is **(c)
   NOT on main**, i.e. still open.
4. `test_no_hardcoded_paths.py` on main still contains
   `test_no_absolute_machine_paths_in_tracked_text` (R28-9) — the check the memo says failed
   is present; whether it currently passes was not re-run here (would require running pytest,
   out of scope for a bounded reader) — **(a) present on main**, pass/fail state not
   re-verified.
5. Claims 6/12 (the withdrawals of the `depends_on` and `PROGRESS_LOG.md` instances) are
   themselves memo-188 corrections reproduced verbatim; they are dated 2026-09-09 and are
   part of the merged outside-bench history — **(a) already on main** as historical memo text
   (`outside_bench/memos/THE_ANTIBODY_RUSTED_TOO.md` itself, post-merge).

## 5. NEEDS COMPUTATION HERE
- Claim 1/2 (selector coverage 2/1125, union 152/217): re-run
  `python3 outside_bench/certificates/instrument_coverage.py` (or an equivalent glob count
  over `frontier/*/{verify.py,results.json,probe.py,verdict.py,compute.py,verification/}`) on
  current `HEAD`; expected: the narrow selector still returns 2 (confirmed unchanged in §4.2),
  the union count should be re-measured since the corpus has grown further since `b94ed03a`.
- Claim 7 (11 failed / 6312 passed / 68 skipped): re-run `python3 -m pytest -q` on a **fresh
  worktree** of current `main` (not this reader's working tree). Expected outcome if F189-1's
  repair is only partially applied: 3 of the original 4 file-not-found failures should now be
  gone (files are tracked), `real_grid.jsonl` should still fail, and the `test_no_hardcoded_
  paths` failure's current status is unknown and is the single most decision-relevant number
  to recompute.
- Claim 9 (absolute-path leak): `git grep -n "(scratchpad)/cloud_handoff"` or the guard's own
  `_FORBIDDEN` fragments over tracked text, to see if R90's leak was cleaned up since.

## 6. SUPERSESSION
- The memo's own headline (the 2/152 blindness) is **not** superseded by any later INDEX row
  found; ADDENDUM 1 *strengthens* it (2/217) rather than retracting it.
- Two sub-claims *attributed to memo 188* and reproduced at the foot of this file (the
  `depends_on` and `PROGRESS_LOG.md` instances) are explicitly **WITHDRAWN by memo 188's own
  addenda 2 and 3** (same date), leaving memo 188's pattern resting on two instances (a minus
  sign twice) rather than four. This is internal-memo supersession, not a later memo
  superseding 189.
- No later memo in `INDEX.md` (190+) or the owner register was found revisiting or retracting
  memo 189's coverage numbers or repair spec.

## 7. GRADE PROPOSAL
**REPRODUCE-AND-BANK** — this is a live, cheap, well-specified computation (F189-1: widen the
selector, run non-mutating, report how many of the (now likely >152, since main has grown
past `b94ed03a`) committed results no longer reproduce) that sits entirely on main, is
unblocked ("nothing. Your call" — owner register), and the interim state (3 of 4 log/out files
now tracked, `real_grid.jsonl` still not) shows the repair is mid-flight and worth finishing
and re-measuring rather than merely registering.
