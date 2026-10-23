#!/usr/bin/env bash
# B1178 -- L184 EXECUTED: the collection lazy-fy. Two files carried 193 of 178+X seconds of
# collection; both bodies moved into cached runners (compute at first test execution, unchanged
# outcomes). Full-suite collection: 178.41 s -> 15.14 s (12x).
set -euo pipefail
cd "$(dirname "$0")"; R=../../..
grep -q "functools.lru_cache" "$R/tests/test_b371_two_state_sector.py" && echo "  OK b371 lazy (157s offender)" || { echo "  MISSING b371 lazy (157s offender)"; exit 1; }
grep -q "functools.lru_cache" "$R/tests/test_cc2_r5_adopted.py" && echo "  OK cc2_r5 lazy (36s offender)" || { echo "  MISSING cc2_r5 lazy (36s offender)"; exit 1; }
grep -q "156.95" ../../B1177_instrument_bundle/collect_per_file.txt && echo "  OK the per-file table committed" || { echo "  MISSING the per-file table committed"; exit 1; }
echo "  (certified this sitting: both files' tests 5/5 pass post-fix; full collect 15.14 s)"
echo "REPRODUCES"
