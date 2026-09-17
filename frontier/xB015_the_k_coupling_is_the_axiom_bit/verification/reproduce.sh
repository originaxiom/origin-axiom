#!/bin/sh
# xB015 -- reproduces every cell.  ~8 minutes (K3 scans 3000 census manifolds,
# K5 runs the integral-trace certificate over all 112 family members).
set -e
cd "$(dirname "$0")"
python3 k_coupling.py
