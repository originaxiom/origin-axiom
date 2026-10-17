#!/bin/sh
# Runs every computation the note states (single-threaded BLAS).
set -e
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
for c in checks/*.py; do echo "== $c"; python3 -B "$c"; done
