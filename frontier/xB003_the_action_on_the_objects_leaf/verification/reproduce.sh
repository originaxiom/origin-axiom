#!/usr/bin/env bash
# xB003 - the monodromy action on the object's leaf.  Requires sympy.  Runtime ~30 s.
set -euo pipefail
cd "$(dirname "$0")"
python3 leaf_action.py
python3 inception_check.py
python3 founding_cluster_audit.py
echo "REPRODUCES"
