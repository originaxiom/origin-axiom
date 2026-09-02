#!/usr/bin/env bash
# B1238 -- reproduce every number this cell banks. Run from the repo root (pyenv python with snappy, cypari,
# sympy, numpy, mpmath; no Sage). The bronze step (two 1000-bit routes, LLL at 300 digits) takes ~10-15 min;
# everything else is seconds. Prints REPRODUCES when every key string matches the committed outputs.
set -u
cd "$(git rev-parse --show-toplevel)" || exit 2
V=frontier/B1238_seat_harvest_40a3_bronze_octic/verification
T=$(mktemp -d)
fail=0
run() {  # name  script  key-string...
  local name=$1 script=$2; shift 2
  python3 "$V/$script" > "$T/$name.txt" 2>/dev/null
  for k in "$@"; do
    if ! grep -qF -- "$k" "$T/$name.txt"; then echo "MISSING [$name]: $k"; fail=1; fi
  done
  echo "ran $name"
}
run r037    r037_verify.py              "Surj(pi1 m000, 2T): 48  Surj(pi1 m004, 2T): 48" "restricted image is one of m004's orbits? [False, True]"
run r037rs  r037_rs.py                  "Surj(H,2T) on my R-S presentation: 48" "codex's Tietze map sends m004's relator to 1 under all 48 2T reps of H: True"
run r038    r038_verify.py              "stabilizer in su(6)+su(2): dim 25 rank 5" "Y is supported on coords 1..5 and annihilates v: True"
run r039    r039_verify.py              "per m004 A4-map, number of its two 2T lifts that extend over m000: [1]"
run r40     r40_pisot_verify.py         "x**4 - 2*x**3 - 5*x**2 - 4*x - 1" "x**4 - 10*x**3 - 117*x**2 - 44*x - 5"
run r41     r41_trace_map_verify.py     "det_is_one(m), m=1,2,3: [True, True, True]"
run b211    b211_phi_jacobian.py        "minimal model of Jac(Phi): [0, 0, 0, -2, 1]" "equals 4*Phi: True" "is divisible by Phi (remainder 0): True" "sigma preserves Phi: True"
run z1      z1_compare.py               "rerun == main banked at levels: 22 / 22  mismatches: []"
if [ "${B1238_SKIP_BRONZE:-0}" != "1" ]; then
  run bronze bronze_invariant_trace_field.py "b++RRRLLL: invariant trace field degree 8" "x^8 + 6*x^6 - x^5 + 12*x^4 - 3*x^3 + 8*x^2 - x + 2" "routes agree (nfisisom): True" "b++RRLL: invariant trace field degree 2" "polredabs x^2 + 1"
else
  echo "bronze step SKIPPED (B1238_SKIP_BRONZE=1) -- the committed bronze_invariant_trace_field.txt is the record"
fi
if [ $fail -eq 0 ]; then echo "REPRODUCES"; else echo "DOES NOT REPRODUCE"; fi
exit $fail
