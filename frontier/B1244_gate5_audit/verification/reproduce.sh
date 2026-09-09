#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"; ROOT="$(cd ../../.. && pwd)"
OA_ROOT="$ROOT" python3 b1244_checks.py | tail -18 | tee /dev/stderr | grep -q '^REPRODUCES$' && echo "REPRODUCES" || { echo DIFF; exit 1; }
