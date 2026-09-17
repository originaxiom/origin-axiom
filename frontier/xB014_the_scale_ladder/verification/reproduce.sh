#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 scale_ladder.py
echo "REPRODUCES"
