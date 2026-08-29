# B1207 — THE SLOW LANE'S FIRST FULL RUN, TRIAGED AND DISCHARGED (R52-4)

**Verdict**: `OPEN` (instrument arc; no mathematics) · **Banked**: 2026-08-29 · **Gate 5 clean**

## 0. What ran

The **OA_SLOW shadow suite** — fifty gated test files that no runner had ever executed — was
enumerated at B1177 and launched there. Its **first-ever complete run** finished after **4 h 45 min**:

```
9 failed, 5702 passed, 5 skipped
```

This arc triages all nine and discharges the debt. **The headline is the class, not the count**:
every one of these defects was *already committed and already invisible* — a gate that has never
been **reached** is not a gate. That is the same species as the program's finished-but-forgotten
class (B1202's instrument): not wrong work, **unreached** work.

## 1. The nine, by class

### Class A — real defects of mine, three kinds (5 of the 9)

**A1. Thirteen arc verification scripts carried absolute machine paths.** `test_no_hardcoded_paths`
is OA_SLOW-gated, so the fast lane never saw them. Root cause named honestly: these are
**agent-written scripts I copied into arc directories** during the close-loop batches (B1187–B1189)
without normalizing their paths — the script runs on the bench that wrote it and nowhere else, which
is exactly the reproducibility claim an arc's `verification/` directory is making. Fixed by deriving
the root from each file's own location; **all three touched arcs still print `REPRODUCES`**.

**A2. Ten arcs carried a verdict, results and verification — but no findings document.**
(B1176, B1177, B1178, B1179, B1181, B1182, B1183, B1194, B1195, B1196.) `test_b810_wave1` /
`test_b817_wave2` enforce writer safety; both are slow-gated. This is the **exact mirror of B1176**,
where thirteen pre-discipline arcs had FINDINGS and no verdict, and it happened on the same seat
within two days. Documents are now authored **from each arc's own banked record**, `arc_verdict.json`
primary, each stamped with that provenance — nothing supplied from memory.

**A3. Two NEGATIVE arcs were unrouted in the kill graph.** B1203 (both forcing candidates are
symmetries — a cut of exactly zero, and κ identically conserved along the climb) and B1205 (the cubic
cuts one of three dimensions). B833's lock exists precisely to stop the B801 backlog rebuilding, and
it caught the backlog rebuilding by two — **within four days of the seat that routed it**. Both now
carry `kill_form`, `fact_computed`, a hatch, and their priority.

### Class B — the locks' own bugs, two (2 of the 9)

**B1. `test_b844_review_gate` manufactured the defect it hunts.** Its ID strip was
`^R[\d-]+[^:]*:?` — greedy up to a colon — so a **colon-free** carried item had its *entire reason*
eaten by the strip and was then flagged for having no reason. Two of 127 items were colon-free; both
give perfectly good reasons. Note the irony the test's own docstring already records: an earlier form
of this same test was fixed once before for pinning a magic string instead of the invariant. Bounded
here, with the bare-ID control asserted so the lock keeps its teeth.

**B2. `test_b1034_l154`'s allowed set predated the grand-computation campaign.** The lock bars
drive-by mentions of the L154 pairing (Brown–Henneaux **and** (E₆)₁ in one file) outside registered
surfaces. Three new files trip it: **B1190 is the L154 bridge cell** — the successor entitled to
discuss the pairing exactly as B1064 is — and the two campaign docs carry its adjudicated row. Read
before admitting: each states the adjudication (*NO-EXHIBIT*, *ONE-BRIDGE-MISSING*, *the fingerprint
route is DEAD*) rather than asserting the join. Admitted **conditionally**: a new test requires each
of the three to keep that language, so the allowance cannot decay into a blanket.

### Class C — a real code bug, eight days old (1 of the 9)

**`frontier/B1113_tmeter/b1113_tmeter_verify.py` could not run at all.** `REPO_ROOT` took **two**
dirnames where the file's depth needs **three**, so the root resolved to `frontier/` itself and every
join doubled it: `frontier/frontier/B1102_.../e6_bracket_vendored.py`, `FileNotFoundError`. Banked
2026-08-21 in the breakthrough packet; **the verifier has never once executed since**, and only the
slow-gated lock exercises it. Fixed (depth 3, with the history in a comment); `test_b1113_tmeter`
now passes 4/4, including the certificate-free re-run it was written to guarantee.

### Class D — casualties of the run itself, two (2 of the 9)

`test_atlas::test_render_regenerates_the_map` and
`test_b1152_suite_cost_class::test_main_band_clean_of_the_drift_classes` **both pass in isolation**
and are not reproduced. The explanation is the run's own duration: B1203, B1205 and B1206 were
**banked while the 4 h 45 min suite was in flight**, so the atlas and the cost-class band moved
underneath the assertions that measure them.

> **THE METHOD FACT, recorded because it will recur**: *a lock run against a moving repository
> measures the motion.* The slow lane must be run **quiescent** — no banking in flight — or its
> currency-style gates report drift as defect. Two of nine findings in the first full run were this
> artifact, which is a 22 % false-positive rate bought for nothing.

### Class E — what the run DID to the repo, found by watching it (not among the nine)

The nine failures were the run's *report*. Watching the tree while it ran turned up a fourth class
the report could not contain, because these defects **succeed** silently:

**E1. The B1137 grid was appended, never truncated — so it triple-counted.** `run_pool` opened the
output with `'a'` and the arc has no resume logic, so every OA_SLOW re-run of the PSLQ probe wrote
another 216 cells into the same file. This bench's `real_grid.jsonl` held **648 rows = 3 × 216**.
The aggregator then re-derived `M_grid_cells = 432` and **halved the Šidák α off multiplicity that
was never tested** (2.37e-4 → 1.19e-4). The grid is gitignored, so nothing showed in `git status`
until the *fast* test re-aggregated it into the tracked report. Fixed at both ends: the writer
truncates, and the aggregator de-duplicates by cell identity `(name, D, H)` so a legacy contaminated
grid still aggregates correctly. **The verdict never moved** — `DISJOINT`, all-zero admissions — and
the banked `final_report.json` is now **reproduced exactly** from the restored 216-cell grid. What
was wrong was the multiplicity, and it was wrong in the *conservative* direction, which is why no
lock caught it.

**E2. The B1113 verifier wrote machine paths into a tracked file.** The banked results carried
hand-sanitized `"<repo>/…"` placeholders; the script records `CCB_PATH` raw, so the first successful
re-run (the one this arc's own fix enabled) replaced them with this bench's absolute paths. A
verifier that dirties the tree with bench detail is not reproducing its banked output. Now recorded
repo-relative, with the certificate reference elided; the re-run's only remaining differences from
the banked file are `runtime_seconds` and the cert-presence line, which are honest bench facts. The
file is also normalized to the writer's own `indent=2` so that future runs converge instead of
re-diffing.

**E3. Two more arcs rewrite tracked results with per-run timings** (B1107, B1114 — identical modulo
timestamps; reverted, not committed). Recorded as a class, not fixed here: **the slow lane cannot
currently be run without dirtying the working tree**, which is a second, independent reason it must
be run quiescent and its diff inspected rather than committed blind.

## 2. What this says about the instrument layer

Three of the five real defects were committed by the seat **that had just built or just used the
corresponding instrument** — the paths went in during the close-loop batches, the missing FINDINGS
mirror B1176's own repair two days earlier, and the unrouted negatives postdate B836's routing pass.
The lesson is not vigilance; vigilance is what failed. It is that **a gate only works where it is
reached**, so the reach itself has to be scheduled. The slow lane is now a **review-cadence item**
(quiescent run, once per review), not a thing launched and forgotten — which is precisely how it came
to sit unrun from its own creation until today.

## 3. Fences

- The ten authored documents restate their arcs' **banked verdicts**; they re-adjudicate nothing, and
  every one carries a stamp saying so. No claim's grade moved in this arc.
- Class D is diagnosed from the timing, not proved: the confirming full re-run is quiescent and its
  result is recorded in `b1207_results.json` when it lands. If either failure survives a quiescent
  run it is a real defect and returns to the queue.
- The B1113 fix restores the verifier's ability to run; it does not re-verify B1113's mathematics,
  which stands on its banked record.

## 4. The certifying record

- `verification/reproduce.sh` — re-checks all five discharged conditions from scratch (`REPRODUCES`)
- `verification/discharge.txt` — its output
- `b1207_results.json` — the triage table and the run figures
- `tests/test_b1207_slow_lane.py` — the locks
