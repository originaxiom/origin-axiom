#!/bin/sh
set -e
D=frontier/B1228_S1_the_nomination
python3 $D/s1.py && python3 $D/nomination.py && python3 $D/k1.py && python3 $D/level.py
