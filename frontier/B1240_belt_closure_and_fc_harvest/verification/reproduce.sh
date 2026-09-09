#!/usr/bin/env bash
# B1240 -- reproduce the harvest recomputations and the belt instrument's ratchet state.
#   fast_checks.py        R42 (own reduction vs PARI), R43, R44, B955, R50        (~20 s, snappy/mpmath/sympy)
#   r42_pari_cycles.py    R42 by the independent PARI-rho route                   (~2 s)
#   reproduce_belt.py     --selftest, then --runners/--json on THIS tree: after B1240 every runner's
#                         references are tracked (missing == 0); string locks <= 27 (the ratchet)
#   b511_d3_tracemap.py   D3.3 on the trace map at 200 bits (~6 min) -- OA_SLOW=1 only
# The repo-root copy scripts/checks/reproduce_belt.py is byte-identical to the one here (checked below).
set -e
cd "$(dirname "$0")"
ROOT="$(cd ../../.. && pwd)"
ok=1
echo "===== fast_checks ====="
python3 fast_checks.py 2>/dev/null | tail -8 | tee /dev/stderr | grep -q '^REPRODUCES$' || ok=0
echo "===== r42_pari_cycles ====="
python3 r42_pari_cycles.py 2>/dev/null | tail -2 | grep -q '^REPRODUCES$' || ok=0
echo "===== reproduce_belt ====="
cmp -s reproduce_belt.py "$ROOT/scripts/checks/reproduce_belt.py" || { echo "  repo copy of reproduce_belt.py differs"; ok=0; }
OA_ROOT="$ROOT" python3 reproduce_belt.py --selftest | grep -q '9/9 controls pass' || ok=0
OA_ROOT="$ROOT" python3 reproduce_belt.py --json /tmp/b1240_belt_$$.json >/dev/null
python3 - "/tmp/b1240_belt_$$.json" <<'PY' || ok=0
import json, sys
j = json.load(open(sys.argv[1]))
locks, missing = len(j["string_locks"]), [r["runner"] for r in j["runners"] if r["missing"]]
print(f"  string-only locks: {locks} (ratchet <= 27); runners with untracked inputs: {len(missing)} {missing}")
sys.exit(0 if locks <= 27 and not missing else 1)
PY
rm -f "/tmp/b1240_belt_$$.json"
if [ -n "$OA_SLOW" ]; then
  echo "===== b511_d3_tracemap (OA_SLOW) ====="
  python3 b511_d3_tracemap.py 2>/dev/null | tail -1 | grep -q '^REPRODUCES$' || ok=0
fi
if [ "$ok" = 1 ]; then echo "REPRODUCES"; else echo "DIFF"; exit 1; fi
