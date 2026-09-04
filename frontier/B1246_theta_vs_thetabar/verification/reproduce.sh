#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 b1246_chiral_invariance.py | tail -20 | tee /dev/stderr | grep -q '^REPRODUCES$' && echo "REPRODUCES" || { echo DIFF; exit 1; }
