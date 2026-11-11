#!/bin/sh
# Run in place, once, after the seal is pushed.
cd "$(dirname "$0")" && python3 -I golden_state_peak.py > golden_state_out.txt 2> golden_state_err.txt; echo "exit $?" >> golden_state_err.txt
