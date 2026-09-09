#!/usr/bin/env bash
# B1236 -- the A1 landing at exact multiplet grade. Exact fractions; < 1 s.
set -u; cd "$(dirname "$0")"
python3 a1_su6_branching.py | tee a1_su6_branching.txt | grep -q "^VERDICT: the A1 landing reproduces the SM-shaped 27 EXACTLY" && echo "B1236 REPRODUCED" || { echo "B1236 FAILED"; exit 1; }
