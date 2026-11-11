#!/bin/sh
# Run in place, each script once, after it is committed and pushed.
cd "$(dirname "$0")" && python3 -I "$1.py" > "$1_out.txt" 2> "$1_err.txt"; echo "exit $?" >> "$1_err.txt"
