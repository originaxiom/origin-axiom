#!/usr/bin/env bash
# xB001 - the session's own computations: the congruence level, and the two killed/banked cells.
set -euo pipefail
cd "$(dirname "$0")"
python3 congruence_level.py
python3 amphichiral_palindrome.py
echo "REPRODUCES"
