#!/bin/sh
# Run in place, once, after the script is committed and pushed.
cd "$(dirname "$0")" && python3 -I loop_phase1_check.py > loop_phase1_out.txt 2> loop_phase1_err.txt; echo "exit $?" >> loop_phase1_err.txt
