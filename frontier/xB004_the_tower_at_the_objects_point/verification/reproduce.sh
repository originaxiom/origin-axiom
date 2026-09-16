#!/usr/bin/env bash
# xB004 - B6's recipe at the object's point.  Requires sympy.  Runtime ~2 min.
set -euo pipefail
cd "$(dirname "$0")"
python3 tower_at_the_point.py
echo "REPRODUCES"
