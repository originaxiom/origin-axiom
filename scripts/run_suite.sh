#!/bin/bash
# The lock suite runner (B1018). Parallel by default; serial remains the CERTIFICATE OF RECORD.
#
# THE ARBITER RULE (PRACTICES, B1018): any parallel-vs-serial disagreement is a FAILURE and is
# investigated, never shipped. When in doubt, run --serial. A bank's final pre-commit suite may
# use parallel ONLY once qualified (B1018) and unchanged in qualification-relevant ways since.
#
# Usage:  scripts/run_suite.sh [--serial] [extra pytest args...]
set -u
cd "$(dirname "$0")/.."
MODE="-n 12"
if [ "${1:-}" = "--serial" ]; then MODE=""; shift; fi
exec python3 -m pytest tests/ -q -p no:randomly $MODE "$@"
