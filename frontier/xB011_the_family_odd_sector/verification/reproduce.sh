#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 family_odd.py
echo "REPRODUCES"
