# MEMO 189 — **THE CHECK BUILT TO CATCH RUSTED INSTRUMENTS HAS ITSELF GONE BLIND**: it sees 2 arcs out of 152 that carry exactly the structure it was written to watch

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** `certificates/instrument_coverage.py` · **Output** `outputs/instrument_coverage_out.txt`
**Gate 5** pure counting over the repository. No measured physical value.

**Already-banked check (memo 153).** Terms searched: `instrument freshness`, `results.json cache`,
`stale lock`, `coverage`, `B1054`. **The corpus already holds the arc** — `B1054` / Review 42 —
and this memo is explicitly built on it, not around it. Nothing here is claimed as new that isn't.

**Scope.** `scripts/checks/` lives on **main**. This lane does not touch main. The finding is
measured, the repair is specified exactly, and applying it is the owner's call.

---

## 1. The programme found this pattern first, and gets the credit

Memo 188 read the whole corpus and named the master pattern: *the characteristic failure is not
error, it is entropy in the programme's own instruments.* **That was not this bench's discovery.**
The programme found it, in a sharper and more specific form, at **B1054 / Review 42**, and wrote a
check for it. From `scripts/checks/instrument_freshness.py`'s own docstring:

> *"an arc's lock asserts over `frontier/BNNNN_*/results.json`; `results.json` is a CACHE, written
> once at banking time and committed; later arcs edit the files the instrument measures — that is
> what a consolidation window IS — and nothing re-runs the instrument; so the lock validates the
> cache against itself and cannot see the drift. **By construction.**"*

and Review 42's governing finding, in its own words:

> *"two locks were red at HEAD, and nobody knew."*

That is a better statement of memo 188's pattern than memo 188 made. **Memo 188 generalised a
finding the programme already owned.** Said plainly, because the reverse would be a nicer story
and would be false.

## 2. What happened next — the pattern, applied to the antibody

The check selects its subjects by looking for arcs carrying **both `verify.py` and `results.json`**.
Measured today:

```
arcs in frontier/                                  1125
arcs the check selects (verify.py + results.json)     2      0.2%
```

Because the corpus **renamed its instruments**:

```
probe.py        145        results.json         118
verdict.py       23        verification/         80
compute.py       19        per-arc *_results.json, *_out.txt
```

Widening the selector to the shapes actually in use:

```
arcs with some runnable script                      303
arcs with some committed result artefact            316
arcs with BOTH (a widened selector)                  72
arcs with a verification/ directory                  80
union                                               152
```

> **The check sees 2 of those 152. It is blind to 150 arcs that carry exactly the structure
> B1054 warned about.** It still runs. It still passes.

## 3. Why this is worse than having no check (interpretation, labelled)

**A green check with 0.2% coverage answers *"is anything stale?"* with a silence that reads as
*no*.** The failure B1054 identified was that a lock cannot see its own instrument. The failure
here is one level up: **the instrument that was built to see across locks cannot see that it has
stopped looking at anything.** Nothing red ever appears, so nothing prompts a second look.

This is the same shape as the other three instances memo 188 counted, in one day:

* `depends_on` — adopted at B800, ran at 77%, decayed to 0%;   **<- SUPERSEDED, see below**;
* `PROGRESS_LOG.md` — the log GOVERNANCE §5 requires every status change to enter, quiet since 2026-08-30;
* a minus sign that failed to survive a download, **twice** (memos 186 and 187).

**None of these is a reasoning error.** Every one is something built, used, and then not fed.

## 4. The repair, specified

Widen the selector in `scripts/checks/instrument_freshness.py` from the literal pair
`(verify.py, results.json)` to the shapes in §2. That takes it from **2 arcs to 152**.

**Two properties must survive the widening, and both are easy to lose:**

1. **It must stay non-mutating.** Running an instrument rewrites its own results; the current file
   snapshots every artefact and restores it unconditionally. Its own docstring records that the
   first version did *not*, and destroyed B946's four cached values — *"only git still had them"* —
   and that a mutating sweep inside the suite would make other locks depend on **test order**.
2. **It must stay a test, not a per-push gate.** It costs minutes at 26 instruments; at 152 it
   should be **sampled or sharded**, not run whole on every suite pass.

## 5. What is NOT claimed

**Nothing here says the 150 hidden arcs are stale.** That is the *next* measurement, and it needs
the widened selector plus the snapshot discipline above. **What is established is only that nobody
can currently see** — which is the precondition for the drift B1054 found, not the drift itself.

## 6. Named follow-up

**F189-1.** Apply the widened selector (owner's call, on main), then run it non-mutating over the
152 and report how many committed results no longer reproduce. That is the number Review 42 would
have wanted and nobody has.

---

## ADDENDUM 1 (2026-09-09) — **re-measured on `main`: the finding stands and was UNDERSTATED**

The body was measured on `claude/outside-bench`, **126 commits behind `origin/main`** (the
staleness that forced memo 188 addendum 2's withdrawal). Re-run against `origin/main` at
`b94ed03a`:

| | this branch (stale) | `origin/main` |
|---|---|---|
| arcs the check selects | 2 | **2** |
| arcs with a `verification/` directory | 80 | **145** |
| union carrying the structure B1054 warned about | 152 | **217** |
| **blind to** | 150 | **215** |

> **The check still sees exactly two arcs. The corpus grew; its coverage did not.** 2 of 217.

**Unlike memo 188 §3, nothing here is withdrawn — the number moved the wrong way for the
programme and the right way for the finding.** The repair specified in §4 is unchanged and its
value is now larger.

**And the staleness lesson applies here too, in the other direction:** a stale tree can understate
a finding as easily as it can manufacture one. **The rule adopted in memo 188 addendum 2 — state
the tree, and how far it is from `main`** — is why this was caught within the hour.

---

## ADDENDUM 2 (2026-09-09) — **the full suite run on a clean `main`: 11 failures, and four of them are tests that read files the repo deliberately does not track**

**Method.** `origin/main` at `b94ed03a` checked out into a **fresh worktree**, `python3 -m pytest -q`,
run to completion: **11 failed, 6312 passed, 68 skipped, 1 h 19 m 28 s.**

*(Note on scope: the other seat's audit reported "309 passed; the same 21 existing failures/errors
remain." That is a subset run. The full suite collects **6391**. The two numbers are not
comparable and neither should be quoted as the other.)*

### The four that matter — and they are not drift, they are *never-could-have-passed*

```
test_b1062_bridge.py::test_block_logs_pin_the_numbers
    FileNotFoundError: frontier/B1062_bridge_cell/b1062_v2_block1.log
test_b1063_refresh.py::test_window_log_pins_the_misses
    FileNotFoundError: frontier/B1063_refresh_verdict/refresh_windows.log
test_b1306_the_older_debt.py::test_slice_c_own_rederivations_are_pinned
    FileNotFoundError: frontier/B1306_the_older_debt/verification/sliceC/c_beat.out
test_b1137_regulator_probe.py::test_aggregate_re_derives_from_pinned_grids
    FileNotFoundError: results/real_grid.jsonl        (a RELATIVE path — cwd-dependent)
```

**`.gitignore` line 20 is `*.log`.** The first two read `.log` files that the repository is
configured never to track. The third reads a `.out` file that is not in the tree. The fourth
reads a relative path.

> **These four tests pass only on a machine where someone previously generated those files. On a
> clean clone of `main` they cannot pass, and never could.**

This is Review 42's *"two locks were red at HEAD, and nobody knew"* in a **worse** form. Review 42
found drift — instruments whose committed cache had gone stale. **These never had a cache to go
stale.** They are green on a developer's machine and red on a fresh checkout, permanently, and
the difference is invisible to anyone who does not check out clean.

### And one of the failures is the repo's own check for the defect this bench found

```
test_no_hardcoded_paths.py::test_no_absolute_machine_paths_in_tracked_text
    AssertionError: absolute paths in tracked text
```

**The repository already has a check for absolute machine paths in tracked files, and it is
failing.** That is the same defect class the widened freshness sweep found inside the arc
instruments — two of them carrying a literal `(scratchpad)/cloud_handoff/…` path (R90). The
programme built the antibody, and it is red.

### The remaining six, for completeness

| test | reason |
|---|---|
| `test_p3_verification_package.py::test_manifest_is_current` | *"MANIFEST.json is stale: run build_manifest.py"* — **the reviewer-facing verification package added in `main`'s own HEAD commit** |
| `test_public_surface_scan.py::test_no_email_addresses_or_reviewer_placeholders` | a placeholder left in `CHANGELOG.md` |
| `test_b646_wave2.py::test_archive_matches_manifest_except_disclosed` | files listed in a manifest that are `MISSING` from the archive |
| `test_b565_realform.py::test_snappy_gate` | numerical: `assert 4.0 < 1e-09` — a trace that should match and is off by exactly 4 |
| `test_b511_d5.py::test_d3_wild_dynamically_suppressed` | numerical: `assert 0.0 > 0.8` |
| `test_b616_heldout.py::test_b616_heldout` | a held-out design check: *"observed 2 coarse-tier matches of 378 pairs"* not found in the expected string |

### What this changes about memo 188's pattern

Memo 188 addendum 2 **withdrew** the `depends_on` instance. This addendum **adds two stronger
ones**, both measured rather than inferred:

* four tests that are structurally unable to pass from the repository alone;
* the programme's own hardcoded-path check, red.

**And it corrects the framing this bench used one turn earlier.** I flagged the other seat's "21
existing failures" as a candidate instance of instrument decay. On the full suite the number is
**11**, and the interesting thing is not the count — it is that **four of them never ran from a
clean tree.** The count was the wrong thing to look at.

### The repair, specified (not applied — this lane does not touch `main`)

Either commit the four artefacts (with a `.gitignore` exception, as the repo already does for
`legacy/` text), or make the tests **generate** what they read, or mark them as requiring a
prior generation step. **Whichever is chosen, a test that reads an untracked file should say so
when the file is missing rather than raising `FileNotFoundError`.**


> **SUPERSEDED on its final term (memo 188 addendum 2, 2026-09-09).** The census that produced the `0%` ran on a tree **126 commits behind main** and read its zeros as decay. On main the newest era declares `depends_on` at **61%** with the richest verdict records of any era (mean 8.8). The honest series is `3% / 2% / 2% / 2% / 77% / 26% / 61%` — **a dip and a recovery, not a decay** — so the pattern below stands on three instances, not four. Left in place rather than rewritten, per the addendum-only rule.
