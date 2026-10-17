#!/bin/zsh
# Re-executes six of the ninety sealed configurations with the unmodified instrument (two processes, three each).
cd "$(dirname "$0")"
run() { for i in "$@"; do nice -n 10 python3 -B repro_driver.py instrument/forms.pkl $i >> repro_run_$1.txt 2>&1; done; }
run 35 3 56 &
run 23 84 15 &
wait
