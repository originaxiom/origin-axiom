#!/usr/bin/env bash
# B1210 -- the paper-spine sweep: rebuild P3's claim pool from the corpus.
set -euo pipefail
cd "$(dirname "$0")"
python3 spine_sweep.py | tail -12
python3 claim_ledger.py
echo REPRODUCES
