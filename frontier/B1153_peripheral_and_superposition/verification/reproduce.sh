#!/usr/bin/env bash
# B1153 reproduction runner -- PROVENANCE (per the L183 reproducer-hygiene rule).
# The certs (peripheral_identity.py = memo 54; c4b_superposition.py = memo 55) and their expected
# outputs are the CLOUD SEAT's self-contained certs. Primary source: origin/outside-bench @ 0c7f8b5a
# (fetchable; NOT duplicated here -- the harvest pattern keeps cert code on its source, per B1147-B1150).
#   - peripheral_identity.py: sympy, exact rational polynomial algebra (self-contained).
#   - c4b_superposition.py: numpy/scipy; reads certificates/c4data/c4_zeros_{zeta,L}.txt, which the
#     cloud VENDORED VERBATIM from main @ 522c7caa (this seat's B1151 committed scan -- the same zeros
#     live in frontier/B1151_gue_larget_superposition/verification/).
# Every claim is a preregistered assert, so rc=0 IS the verification.
# To re-run: git fetch origin claude/outside-bench && git checkout 0c7f8b5a -- \
#   outside_bench/certificates/{peripheral_identity.py,c4b_superposition.py,c4data} \
#   outside_bench/outputs/{peripheral_identity,c4b_superposition}_out.txt
# then run against them. reproduce.log records the run on THIS bench (2026-08-26): 2/2 REPRODUCE, rc=0,
# byte-identical modulo timing, pyenv 3.12.1. independent_check_memo54.txt cross-verifies memo 54's
# peripheral identity + fixed locus with sympy, a derivation distinct from the cert.
# [2026-09-02 B1240] THE CLOSURE IS NOW VENDORED HERE. The provenance note above described a fetch that a fresh clone
# could not perform (the run record reproduce.log is gitignored, and the certificates load sibling files the
# fetch list omitted). certificates/ and outputs/ beside this script are the full transitive closure at
# origin/outside-bench @ 0c7f8b5a; see VENDORED_FROM.txt (sha256 per file). tests/test_reproduce_runners_live.py RUNS
# this script (fastest certificate by default, all under OA_SLOW=1); the runner text is no longer the lock.
set -e
cd "$(dirname "$0")"   # [2026-09-02 B1240] runnable from any cwd (was: relied on cwd = this directory)
CERTS="${CERTS:-peripheral_identity c4b_superposition}"   # [2026-09-02 B1240] override: CERTS=<one cert> for the default test lane
filt() { grep -vE 'elapsed|seconds|[0-9]+\.[0-9]+ ?s$|^real|^user|^sys'; }
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "certificates/$c.py" > "our_${c}.out" 2>&1; rc=$?
  if diff <(filt < "our_${c}.out") <(filt < "outputs/${c}_out.txt") >/dev/null 2>&1; then
    echo "  rc=$rc  REPRODUCES"; else echo "  rc=$rc  DIFF"; fi
done
echo "===== DONE ====="
