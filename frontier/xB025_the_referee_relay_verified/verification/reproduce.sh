#!/bin/sh
# xB025 -- reproduce the E_6 orbit computation.  The relay checks are reads of
# the SM-derivation lane at 23532539 and of B1413/B1415 on this branch.
cd "$(dirname "$0")" && python3 e6_a2_orbit.py
