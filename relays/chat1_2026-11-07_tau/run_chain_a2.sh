#!/bin/bash
# Amendment 2: runs tau_k_limit_a2.py once per member, in the order given; stdout, stderr and the exit code per member are written
# beside the script as tau_<member>_out.txt, tau_<member>_err.txt and tau_<member>_exit.txt. In stderr this folder's
# absolute path is cut to nothing, so warnings name files relative to it.
# Used as: run_chain_a2.sh k=3 k=4.
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 NUMBA_NUM_THREADS=1
for m in "$@"; do
  f="tau_${m/=/}"
  python3 -B -u tau_k_limit_a2.py "$m" 2>&1 > "${f}_out.txt" | sed "s#$PWD/##g" > "${f}_err.txt"
  echo "${PIPESTATUS[0]}" > "${f}_exit.txt"
done
