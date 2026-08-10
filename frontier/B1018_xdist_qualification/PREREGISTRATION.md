# B1018 PREREGISTRATION — qualifying the suite for parallel execution (sealed before the run)

**Date sealed:** 2026-08-10 · **Seat:** cc · owner-agreed ("agreed", 2026-08-10). An instrument
cell; Gate 5 untouched.

## The claim under test
The lock suite under pytest-xdist (`-n 12`, 16 cores) produces the SAME outcome inventory as the
serial run on the same tree: equal counts (passed / skipped), ZERO failures, and no test that
passed serially failing in parallel.

## The baseline
The serial certificate of `67450505`'s tree: **3898 passed / 0 failed / 35 skipped** (1:01:27,
2026-08-10). The parallel run executes on the identical tree.

## Cells
- **Q0 (done, pre-sealed):** the module-collision audit — 7 risk names found (worst: ten
  `verify.py`), fix pattern constrained to test-side `importlib` loading (banked paths never move).
- **Q1:** install pytest-xdist into the canonical pyenv env; version pinned in FINDINGS.
- **Q2:** `pytest tests/ -q -p no:randomly -n 12 --junitxml` on the same tree; run **twice**
  (schedule robustness).
- **Q3:** the diff. Aggregate counts must equal the baseline exactly and both parallel runs must
  agree per-test (junitxml). Any failure ⟹ a named parallel-unsafe lock: classify (shared-artifact
  write / module-name collision / cwd dependence / order coupling), fix in the TEST file with the
  reason written in, re-run Q2. If fixes touched files: one serial + one parallel run on the fixed
  tree, both must agree (per-test where junitxml exists on both sides).
- **Q4:** bank the config: `scripts/run_suite.sh` (parallel default, `--serial` flag) + the
  PRACTICES **arbiter rule**: *serial remains the certificate of record; any parallel-vs-serial
  disagreement is a failure and is investigated, never shipped.* Wall-clock recorded.

## Two-outcome
**QUALIFIED** (parallel default; measured speedup recorded) or **NOT-QUALIFIED** (the incompatible
locks named and priced; serial stays default). Either way the suite-growth problem (33 min at
Review 11 → 60–87 min now) gets its first measured answer. Non-weakening applies.
