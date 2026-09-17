#!/bin/sh
# xB018 -- reproduces every cell.  ~3 minutes.
set -e
cd "$(dirname "$0")"
python3 two_bits.py
