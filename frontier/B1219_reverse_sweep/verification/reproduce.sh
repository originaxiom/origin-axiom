#!/usr/bin/env bash
# B1219 -- the reverse sweep. Planted bite controls first, then the sweep.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT"
echo "== planted bite controls (must not be able to go stale) =="
python3 scripts/checks/reverse_sweep.py --selftest
echo
echo "== the sweep =="
python3 scripts/checks/reverse_sweep.py | head -3
echo
echo "REPRODUCES"
