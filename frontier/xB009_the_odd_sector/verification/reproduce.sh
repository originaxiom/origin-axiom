#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 odd_sector.py
echo "REPRODUCES"
