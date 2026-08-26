#!/usr/bin/env bash
# B1150 reproduction runner -- PROVENANCE (per the L183 reproducer-hygiene rule).
# The certs (yukawa_clock.py = memo 52; family_yukawa.py + vendored e7_ladder.py = memo 53) and their
# expected outputs are the CLOUD SEAT's self-contained certs. Primary source: origin/outside-bench @
# 1544989d (fetchable; NOT duplicated here -- the harvest pattern keeps cert code on its source, per
# B1147-B1149). Each cert is stdlib-only (fractions.Fraction, exact); every claim is a preregistered
# assert, so rc=0 IS the verification. family_yukawa.py exec()s e7_ladder.py, so keep them together.
# To re-run: git fetch origin claude/outside-bench && git checkout 1544989d -- \
#   outside_bench/certificates/{yukawa_clock,family_yukawa,e7_ladder}.py \
#   outside_bench/outputs/{yukawa_clock,family_yukawa}_out.txt
# then run against them. reproduce.log records the run on THIS bench (2026-08-26): 2/2 REPRODUCE, rc=0,
# byte-identical modulo timing, pyenv 3.12.1. independent_check_memo53.txt cross-verifies memo 53's
# FACT 7 (family factor = epsilon) via an sl3 joint-kernel computation distinct from the cert.
set -e
CERTS="yukawa_clock family_yukawa"
filt() { grep -vE 'elapsed|seconds|[0-9]+\.[0-9]+ ?s$|^real|^user|^sys'; }
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "certificates/$c.py" > "our_${c}.out" 2>&1; rc=$?
  if diff <(filt < "our_${c}.out") <(filt < "outputs/${c}_out.txt") >/dev/null 2>&1; then
    echo "  rc=$rc  REPRODUCES"; else echo "  rc=$rc  DIFF"; fi
done
echo "===== DONE ====="
