#!/usr/bin/env bash
# B1211 -- the deep spine sweep + the declaration counter-check.
set -euo pipefail
cd "$(dirname "$0")"
python3 deep_sweep.py | tee _out.txt | tail -4
python3 declaration_check.py | head -3
grep -q "VERIFIED" _out.txt && echo REPRODUCES || { echo FAILED; exit 1; }
