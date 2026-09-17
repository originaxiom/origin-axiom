#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 scale_ladder.py
python3 extremality_recheck.py
echo "REPRODUCES"
