#!/usr/bin/env bash
# B1209 -- |a_1| = 1 at every ideal point of 4_1, from main's own A-polynomial.
set -euo pipefail
cd "$(dirname "$0")"
python3 newton_a1.py | tee newton_a1.txt | tail -1
grep -q VERIFIED newton_a1.txt && echo REPRODUCES
