#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 node_z3.py
echo "REPRODUCES"
