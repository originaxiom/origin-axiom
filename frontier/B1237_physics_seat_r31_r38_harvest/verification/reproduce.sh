#!/usr/bin/env bash
# B1237 -- every correction in this cell recomputed here (SnapPy + PARI via snappy.pari + mpmath; no Sage).
# Run from the repo root:  bash frontier/B1237_physics_seat_r31_r38_harvest/verification/reproduce.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 traces_from_b1236.py ../../B1236_a1_landing_exact/verification/a1_su6_branching.py | tee traces_from_b1236.txt
python3 silver_arithmetic.py            | tee silver_arithmetic.txt
python3 b850_multiplicities.py          | tee b850_multiplicities.txt
python3 b333_fundamental_discriminants.py | tee b333_fundamental_discriminants.txt
python3 b213_40a1.py                    | tee b213_40a1.txt
python3 b213_isogeny_class.py           | tee b213_isogeny_class.txt
