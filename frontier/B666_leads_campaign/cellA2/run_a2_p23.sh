#!/bin/zsh
set -e
cd "$(dirname "$0")"
python3 a2_phase2.py > a2_phase2_output.txt 2>&1
echo "PHASE2 EXIT OK" >> a2_phase2_output.txt
python3 a2_phase3.py > a2_phase3_output.txt 2>&1
echo "PHASE3 EXIT OK" >> a2_phase3_output.txt
