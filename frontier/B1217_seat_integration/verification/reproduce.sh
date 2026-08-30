#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_integration.py | tee _out.txt | tail -12
grep -q VERIFIED _out.txt && echo REPRODUCES || { echo FAILED; exit 1; }
