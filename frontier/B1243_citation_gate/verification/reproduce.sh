#!/usr/bin/env bash
# B1243 -- recompute the arc's numbers and run the instrument's own controls.
set -e
cd "$(dirname "$0")"
ROOT="$(cd ../../.. && pwd)"
OA_ROOT="$ROOT" python3 b1243_checks.py | tail -20 | tee /dev/stderr | grep -q '^REPRODUCES$' && echo "REPRODUCES" || { echo "DIFF"; exit 1; }
