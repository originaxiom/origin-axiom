#!/bin/sh
# xB029 -- reproduce every cell from scratch.
cd "$(dirname "$0")" && python3 g2_mssm.py && python3 g2_closed.py
