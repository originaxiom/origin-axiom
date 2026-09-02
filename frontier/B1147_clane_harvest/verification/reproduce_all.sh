#!/usr/bin/env bash
# B1147 reproduction runner. [2026-09-02 B1240] PINNED: the certificates and expected outputs are the
# cloud seat's, vendored verbatim from origin/outside-bench @ dc937010 (the runner previously carried no SHA at all).
# [2026-09-02 B1240] THE CLOSURE IS NOW VENDORED HERE. The provenance note above described a fetch that a fresh clone
# could not perform (the run record reproduce.log is gitignored, and the certificates load sibling files the
# fetch list omitted). certificates/ and outputs/ beside this script are the full transitive closure at
# origin/outside-bench @ dc937010; see VENDORED_FROM.txt (sha256 per file). tests/test_reproduce_runners_live.py RUNS
# this script (fastest certificate by default, all under OA_SLOW=1); the runner text is no longer the lock.
cd "$(dirname "$0")/certificates"
CERTS="${CERTS:-cp1_strata cusp_beat jordan_beat a2_glue64 a5_parity_lemma b2_yukawa a4_pin c5_qp1 c1_weyl c2_habiro c2b_ohtsuki_bridge}"   # [2026-09-02 B1240] override: CERTS=<one cert> for the default test lane
for c in $CERTS; do
  echo "===== $c ====="
  python3 -u "$c.py" > "../our_${c}.out" 2>&1
  rc=$?
  if [ -f "../outputs/${c}_out.txt" ]; then
    if diff <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../our_${c}.out" | tail -30) \
            <(grep -vE '[0-9]+\.[0-9]+ ?s|elapsed|seconds' "../outputs/${c}_out.txt" | tail -30) >/dev/null 2>&1; then
      echo "  VERDICT: rc=$rc  REPRODUCES (verdict region identical)"
    else
      echo "  VERDICT: rc=$rc  DIFF"
    fi
  else
    echo "  VERDICT: rc=$rc  (no committed output)"
  fi
done
echo "===== REPRODUCE_DONE ====="
