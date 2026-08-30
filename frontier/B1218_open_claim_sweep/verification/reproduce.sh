#!/usr/bin/env bash
# B1218 -- the open-claim sweep. Bite control both directions, then the sweep itself.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT"
echo "== bite control (MB12: must find the five, must be silent on nonsense) =="
python3 scripts/checks/open_claim_sweep.py --selftest
echo
echo "== the sweep =="
python3 scripts/checks/open_claim_sweep.py | head -5
echo
echo "REPRODUCES"
