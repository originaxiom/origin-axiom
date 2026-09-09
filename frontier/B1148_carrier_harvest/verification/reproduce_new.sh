#!/usr/bin/env bash
# B1148 reproduction runner -- PROVENANCE (per the L183 reproducer-hygiene rule).
# The certificates (certificates/*.py) and their expected outputs (outputs/*_out.txt) are the
# CLOUD SEAT's self-contained certs. Primary source: origin/outside-bench @ d3c99640 (fetchable;
# NOT duplicated here -- the harvest pattern keeps cert code on its source, per B1147). To re-run:
#   git fetch origin outside-bench && git checkout d3c99640 -- <cert + output paths>
# into ./certificates and ./outputs beside this script, then execute it. reproduce.log records the
# run done on THIS bench (2026-08-26): all certs REPRODUCE byte-identical on pyenv 3.12.1.
# NOTE: memo 48 (uniqueness_chain) was reproduced separately -- see our_uniqueness_chain.out
# (self-documenting: 6615 -> 4 -> 1, survivor automatically symmetric) -- and appended to reproduce.log,
# for 8/8 total. This runner covers memos 41/43/44/45/46/47 (7 with memo 30's carrier cert).
# [2026-09-02 B1240] THE CLOSURE IS NOW VENDORED HERE. The provenance note above described a fetch that a fresh clone
# could not perform (the run record reproduce.log is gitignored, and the certificates load sibling files the
# fetch list omitted). certificates/ and outputs/ beside this script are the full transitive closure at
# origin/outside-bench @ d3c99640; see VENDORED_FROM.txt (sha256 per file). tests/test_reproduce_runners_live.py RUNS
# this script (fastest certificate by default, all under OA_SLOW=1); the runner text is no longer the lock.
cd "$(dirname "$0")/certificates"
CERTS="${CERTS:-kappa_beat fixed_twin one_bit only_spinor hitind carrier yukawa_carrier}"   # [2026-09-02 B1240] override: CERTS=<one cert> for the default test lane
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "$c.py" > "../our_${c}.out" 2>&1; rc=$?
  if [ -f "../outputs/${c}_out.txt" ]; then
    if diff <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../our_${c}.out" | tail -30) \
            <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../outputs/${c}_out.txt" | tail -30) >/dev/null 2>&1; then
      echo "  VERDICT: rc=$rc REPRODUCES"; else echo "  VERDICT: rc=$rc DIFF"; fi
  else echo "  VERDICT: rc=$rc (no committed output)"; fi
done
echo "===== DONE ====="
