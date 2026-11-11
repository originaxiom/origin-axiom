#!/bin/sh
# Run one sealed script once: ./run.sh <name>  (writes <name>_out.json, <name>_out.txt, <name>_err.txt)
python3 -I "$1.py" "$1_out.json" > "$1_out.txt" 2> "$1_err.txt"
echo "exit $?" >> "$1_err.txt"
