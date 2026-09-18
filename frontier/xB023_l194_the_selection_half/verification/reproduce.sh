#!/bin/sh
# xB023 -- reproduce every cell from scratch.
cd "$(dirname "$0")" && python3 selection.py && python3 kawauchi_read.py \
  && python3 mo_corollary.py && python3 knot_or_not.py && python3 n3_push.py && python3 n3_covers.py
