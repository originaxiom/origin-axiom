#!/usr/bin/env bash
# B1242 -- run BOTH L199 computations (SnapPy cusp shapes at two precisions; exact discriminant
# forms; the E6 principal sl2 index by three routes). ~40 s.
set -e
cd "$(dirname "$0")"
python3 l199_two_earning_computations.py 2>/dev/null | tail -30 | tee /dev/stderr | grep -q '^REPRODUCES$' && echo "REPRODUCES" || { echo "DIFF"; exit 1; }
