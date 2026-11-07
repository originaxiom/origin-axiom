#!/bin/bash
# Runs tau_k_more.py once per member, in the order given (one at a time: k = 8's harmonic solve peaks near 4.7 GB);
# stdout, stderr and the exit code per member are written beside the script as taumore_<member>_out.txt,
# taumore_<member>_err.txt and taumore_<member>_exit.txt. In stderr this folder's absolute path is cut to nothing, so
# warnings name files relative to it. Used as: run_chain_more.sh m004 k=1 k=6 k=7 k=8 summary.
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMBA_NUM_THREADS=1
for m in "$@"; do
  f="taumore_${m/=/}"
  python3 -B -u tau_k_more.py "$m" 2>&1 > "${f}_out.txt" | sed "s#$PWD/##g" > "${f}_err.txt"
  echo "${PIPESTATUS[0]}" > "${f}_exit.txt"
done
