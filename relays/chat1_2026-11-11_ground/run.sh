#!/bin/sh
# Run in place, once, after the seal is pushed.
cd "$(dirname "$0")" && python3 -I ground_names_a_level.py > ground_out.txt 2> ground_err.txt; echo "exit $?" >> ground_err.txt
