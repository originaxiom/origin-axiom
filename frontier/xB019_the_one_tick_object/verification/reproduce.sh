#!/bin/sh
# xB019 -- reproduces every cell.  ~2 minutes.
set -e
cd "$(dirname "$0")"
python3 one_tick.py
