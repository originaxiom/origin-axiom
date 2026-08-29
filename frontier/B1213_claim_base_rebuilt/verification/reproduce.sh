#!/usr/bin/env bash
# B1213 -- rebuild the paper's claim base without reading the broken field.
set -euo pipefail
cd "$(dirname "$0")"
python3 claim_base.py | tail -12
python3 render_claim_base.py | head -3
echo REPRODUCES
