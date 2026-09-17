#!/usr/bin/env bash
# B14 -- the half-step square root. Pure Python, no dependencies, under a second.
#   F = LP is an integer square root of A = LR, it is orientation-REVERSING, it is the only one up to
#   sign (proved by Cayley-Hamilton, controlled by enumeration), and L_a R_b has such a root iff a = b.
# Added 2026-09-17 (B1424): this record was banked PROVED in the repository's first week with no script
# and no lock, and it is the arithmetic under the paper's most expensive axiom.
set -euo pipefail
cd "$(dirname "$0")"
python3 square_root.py
