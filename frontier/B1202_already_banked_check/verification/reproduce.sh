#!/usr/bin/env bash
# B1202 -- the already-banked pre-flight check, two-sided controls.
set -euo pipefail
cd "$(dirname "$0")/../../.."
fail=0
echo "POSITIVE controls (each is a real historical miss; the check MUST flag them):"
for q in "quine self-naming census" \
         "stabilization depth-closure WALL-7 TOMB-L34" \
         "genesis fork locks F2 F8" \
         "dark hyperbola prime-power symbolic proof"; do
  if python3 scripts/checks/already_banked.py --exclude=B1202 $q >/dev/null 2>&1; then
    echo "  FAIL (did not flag): $q"; fail=1
  else
    echo "  flagged: $q"
  fi
done
echo "NEGATIVE controls (genuine blind regions; the check MUST stay silent):"
for q in "inflation reheating e-folds primordial" \
         "dark matter relic abundance freeze-out"; do
  if python3 scripts/checks/already_banked.py --exclude=B1202 $q >/dev/null 2>&1; then
    echo "  clean: $q"
  else
    echo "  FAIL (false alarm): $q"; fail=1
  fi
done
[ "$fail" = 0 ] && echo "REPRODUCES" || { echo "CONTROLS FAILED"; exit 1; }
