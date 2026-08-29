#!/usr/bin/env bash
# B1210 -- the paper-spine sweep: rebuild P3's claim pool from the corpus.
set -euo pipefail
cd "$(dirname "$0")"
python3 spine_sweep.py | tee _out.txt | tail -12
python3 claim_ledger.py
grep -q "VERIFIED" _out.txt && echo REPRODUCES || { echo FAILED; exit 1; }
