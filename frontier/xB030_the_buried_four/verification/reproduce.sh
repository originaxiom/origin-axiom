#!/bin/sh
# xB030 -- reproduce every cell from scratch.
cd "$(dirname "$0")" && python3 buried.py && python3 u3_fix.py && python3 u2_power.py
