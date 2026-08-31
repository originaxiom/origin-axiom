#!/usr/bin/env bash
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 census_symmetry_vs_torsion.py
echo
echo "REPRODUCES"
