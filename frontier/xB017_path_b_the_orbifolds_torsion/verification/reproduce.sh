#!/bin/sh
# xB017 -- reproduces every cell.  ~2 minutes.
set -e
cd "$(dirname "$0")"
python3 orbifold_torsion.py
