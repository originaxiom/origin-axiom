#!/usr/bin/env bash
# B1149 reproduction runner -- PROVENANCE (per the L183 reproducer-hygiene rule).
# The three certificates (trace_three.py, depth_lock.py, longitude_lock.py) and their expected
# outputs are the CLOUD SEAT's self-contained certs. Primary source: origin/outside-bench @ 1544989d
# (fetchable; NOT duplicated here -- the harvest pattern keeps cert code on its source, per B1147/B1148).
# Each cert is stdlib-only (fractions.Fraction, exact over Q and Q(q)); every claim is a preregistered
# assert, so rc=0 IS the verification (an assert firing => rc!=0 => DIFF).
# To re-run: git fetch origin claude/outside-bench && git checkout 1544989d -- \
#   outside_bench/certificates/{trace_three,depth_lock,longitude_lock}.py \
#   outside_bench/outputs/{trace_three,depth_lock,longitude_lock}_out.txt
# then run against them. reproduce.log records the run done on THIS bench (2026-08-26): 3/3 REPRODUCE,
# rc=0, byte-identical modulo timing, pyenv 3.12.1. independent_check_memo49.txt cross-verifies memo 49's
# trace-3 arithmetic with sympy (a tool distinct from the cert's own Fraction code).
set -e
CERTS="trace_three depth_lock longitude_lock"
filt() { grep -vE 'elapsed|seconds|[0-9]+\.[0-9]+ ?s$|^real|^user|^sys'; }
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "certificates/$c.py" > "our_${c}.out" 2>&1; rc=$?
  if diff <(filt < "our_${c}.out") <(filt < "outputs/${c}_out.txt") >/dev/null 2>&1; then
    echo "  rc=$rc  REPRODUCES"; else echo "  rc=$rc  DIFF"; fi
done
echo "===== DONE ====="
