#!/usr/bin/env bash
# B1216 -- the parameter-closure loop's two corrections to this repo's own record.
set -euo pipefail
cd "$(dirname "$0")"
python3 two_corrections.py | tee _out.txt | tail -8
grep -q VERIFIED _out.txt && echo REPRODUCES || { echo FAILED; exit 1; }
