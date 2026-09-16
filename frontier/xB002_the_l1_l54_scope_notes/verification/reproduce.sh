#!/usr/bin/env bash
# xB002 - re-derive the evidence under both scope notes.
#   cell 1: the shape-field family, the separator table, the cusp-trivial groups (L1)
#   cell 2: which family members can be covers of m004 (L54)
# Requires: snappy==3.3.2, sympy, mpmath.  Runtime ~3 min.
set -euo pipefail
cd "$(dirname "$0")"
python3 shape_field_family.py
python3 covers_vs_class.py
echo "REPRODUCES"
