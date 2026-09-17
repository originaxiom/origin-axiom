#!/bin/sh
# xB020 -- reproduces every cell.  ~4 minutes (H3 builds 200 orientation covers).
set -e
cd "$(dirname "$0")"
python3 conjugation.py
