#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 selection_test.py
echo "REPRODUCES"
