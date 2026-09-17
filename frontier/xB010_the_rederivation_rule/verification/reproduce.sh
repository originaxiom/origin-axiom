#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 ../../../scripts/checks/rederivation.py --selftest
python3 rule_cells.py
echo "REPRODUCES"
