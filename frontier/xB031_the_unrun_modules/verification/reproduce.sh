#!/bin/sh
# xB031 -- reproduce every cell.  X2 takes ~1h, X3 ~2h.
cd "$(dirname "$0")" && python3 x1_control.py && python3 x2_complete.py && python3 x3_extend.py 4,5,6 && python3 x4_analysis.py
