#!/bin/zsh
# B666 cell A' (cellA2) — repaired pipeline driver: phases 1 -> 2 -> 3.
# Each phase's full output is teed to its own file; the run aborts on
# the first failing phase.
set -e
cd "$(dirname "$0")"
python3 a2_phase1.py > a2_phase1_output2.txt 2>&1
echo "PHASE1 EXIT OK"
python3 a2_phase2.py > a2_phase2_output.txt 2>&1
echo "PHASE2 EXIT OK"
python3 a2_phase3.py > a2_phase3_output.txt 2>&1
echo "PHASE3 EXIT OK"
