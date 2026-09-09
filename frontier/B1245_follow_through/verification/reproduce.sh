#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"; ROOT="$(cd ../../.. && pwd)"
OA_ROOT="$ROOT" python3 b1245_no_group_parameter.py | tail -12 | tee /dev/stderr | grep -q '^REPRODUCES$' && echo "REPRODUCES" || { echo DIFF; exit 1; }
