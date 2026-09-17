#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 ../../../scripts/checks/linkage_kills.py --selftest
python3 gate_cells.py
python3 -m pytest ../../../tests/test_xb008_linkage_gate.py -q
echo "REPRODUCES"
