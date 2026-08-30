#!/usr/bin/env bash
# B1208 -- the five-memo harvest, re-verified from MAIN's own data (no seat branch needed).
set -euo pipefail
cd "$(dirname "$0")"
ok=1
for s in independent_lambda_check census_legs verify_s5 verify_dm_census verify_b8154 verify_kappa_irremovable verify_r021; do
  printf "%-28s " "$s"
  if out=$(python3 "$s.py" 2>&1); then
    echo "$out" | grep -qE "VERIFIED|CENSUS ALONE|CONFIRMED" && echo "OK" || { echo "NO MARKER"; ok=0; }
  else
    echo "FAILED"; ok=0
  fi
done
[ "$ok" = 1 ] && echo "REPRODUCES" || { echo "FAILED"; exit 1; }
