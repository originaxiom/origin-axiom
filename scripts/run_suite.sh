#!/bin/bash
# The lock suite runner (B1018). Parallel by default; serial remains the CERTIFICATE OF RECORD.
#
# THE ARBITER RULE (PRACTICES, B1018): any parallel-vs-serial disagreement is a FAILURE and is
# investigated, never shipped. When in doubt, run --serial. A bank's final pre-commit suite may
# use parallel ONLY once qualified (B1018) and unchanged in qualification-relevant ways since.
#
# Modes (B1152, the cost-class remedy for cc3's B8139 — a lock never reached is a lock that
# caught nothing; the full suite's collection alone is minutes, so give the inner loop a fast lane):
#   scripts/run_suite.sh            full suite, parallel  (the pre-commit certificate)
#   scripts/run_suite.sh --serial   full suite, serial    (the certificate of record)
#   scripts/run_suite.sh --fast     full collection, skip @pytest.mark.slow tests (-m "not slow")
#   scripts/run_suite.sh --changed  ONLY the tests the working-tree diff affects (fast inner loop;
#                                   conservatively falls back to the full suite when it cannot bound
#                                   the change — never a false green). See scripts/affected_tests.py.
# --serial/--fast compose; --changed is standalone. Extra pytest args pass through.
set -u
cd "$(dirname "$0")/.."
if [ "${1:-}" = "--changed" ]; then shift; exec python3 scripts/affected_tests.py --run "$@"; fi
MODE="-n 12"; MARK=()
while :; do
  case "${1:-}" in
    --serial) MODE=""; shift;;
    --fast)   MARK=(-m "not slow"); shift;;
    *)        break;;
  esac
done
exec python3 -m pytest tests/ -q -p no:randomly $MODE ${MARK[@]+"${MARK[@]}"} "$@"
