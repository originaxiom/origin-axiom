#!/usr/bin/env bash
# B1213 -- rebuild the paper's claim base without reading the broken field.
set -euo pipefail
cd "$(dirname "$0")"
python3 claim_base.py | tee _out.txt | tail -12
python3 render_claim_base.py | head -3
grep -q "VERIFIED" _out.txt && echo REPRODUCES || { echo FAILED; exit 1; }
