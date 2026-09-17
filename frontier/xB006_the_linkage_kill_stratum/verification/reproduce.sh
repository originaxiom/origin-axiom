#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 linkage_sweep.py
python3 adjudicate_and_retest.py
echo "REPRODUCES"
