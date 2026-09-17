#!/bin/sh
# xB016 -- reproduces every cell.  ~6 minutes (P3 enumerates every cover of m004
# to degree 8 and verifies the near-limit ones by isometry).
set -e
cd "$(dirname "$0")"
python3 path_a.py
