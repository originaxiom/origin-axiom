#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 both_faces.py
python3 verify_the_pair.py
echo "REPRODUCES"
