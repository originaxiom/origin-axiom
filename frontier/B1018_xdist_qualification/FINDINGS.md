# B1018 — the parallel qualification: correctness clean, one baseline-delta, a 1.42× dividend

**Date:** 2026-08-10 · **Seat:** cc · **Sealed:** `ed762886`. An instrument arc; Gate 5 untouched.

**Verdict: PROVED (QUALIFIED, under the arbiter rule; the same-tree pair certifies this very
commit — numbers in the dated addendum below).**

---

## The cells

**Q0 (pre-sealed).** The module-collision audit: **7 risk names** (worst: ten `verify.py` files);
fix pattern constrained to test-side `importlib` loading. One collision class had already bitten
serially (B943/B1012) and was fixed by rename before this arc.

**Q1.** `pytest-xdist 3.8.0` installed into the canonical pyenv env.

**Q2, run 1** (`-n 12`, 16 cores, junitxml captured): **43:16** against the serial baseline's
**61:27** — a **1.42×** dividend. **3897 passed / 1 failed / 35 skipped.**

**Q3, the one failure — classified BASELINE-DELTA, not parallel-unsafe.**
`test_b837_file_drawer::test_the_unreported_set_has_not_grown`, failing set `{B1018, B1019}` —
**reproduced serially in 0.37 s**. Cause: this arc's own seals were pushed *after* the serial
baseline, growing the unreported-prereg set; the anti-file-drawer lock did exactly its job.
**Remedy: the sealed work itself** — B1019 is banked in this same commit; this report closes the
other. **Zero parallel-unsafe locks found in run 1.**

**On the modest dividend, measured not guessed:** twelve sympy-heavy workers on eight physical
x86 cores (16 logical), all at ~87 % CPU, no memory pressure (64 GB, zero throttled pages) —
shared-cache/hyperthread-bound, plus a machine that had just run an hour of serial suite. 1.42×
is the honest number for this bench; it is still ~18 minutes back per merge.

**Q4.** `scripts/run_suite.sh` banked (parallel default, `--serial` flag) and the **ARBITER RULE**
registered in PRACTICES: *serial remains the certificate of record; any parallel-vs-serial
disagreement is a failure and is investigated, never shipped.*

## The same-tree pair (Q2 run 2 + the serial certificate) — dated addendum

*The serial run below is this commit's banking certificate; the parallel run follows on the
identical tree. Numbers appended post-run, pre-commit:*

- **serial:** **3904 passed / 0 failed / 35 skipped — 1:04:32** (junitxml captured)
- **parallel run 2:** **3904 passed / 0 failed / 35 skipped — 0:40:33** (junitxml captured)
- **per-test diff: identical test sets, ZERO outcome differences (3939 units compared).**
- **Same-tree speedup: 1.59×.** QUALIFIED — the arbiter rule stands; run 1's single failure
  remains classified BASELINE-DELTA (reproduced serially, resolved by banking the sealed work).
