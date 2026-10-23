#!/usr/bin/env bash
# B1173 -- THE DIGEST PARTIAL-CLOSE (owner-directed O4, the approved default).
set -euo pipefail
cd "$(dirname "$0")"
L=../../B1060_digest_ledger/DIGEST_LEDGER.md
grep -q "DIGEST STATUS: CLOSED-PARTIAL 2026-08-27, B1173" "$L" && echo "  OK status CLOSED-PARTIAL" || { echo "  MISSING status CLOSED-PARTIAL"; exit 1; }
[ "$(grep -c '| EMPTY |' "$L")" = "0" ] && echo "  OK zero EMPTY rows" || { echo "  MISSING zero EMPTY rows"; exit 1; }
[ "$(grep -c 'NOT-REACHED at partial-close' "$L")" = "13" ] && echo "  OK 13 NOT-REACHED (the ledger's own honesty vocabulary)" || { echo "  MISSING 13 NOT-REACHED (the ledger's own honesty vocabulary)"; exit 1; }
grep -q "L185+" "$L" && echo "  OK the stale L165+ renumber corrected to L185+" || { echo "  MISSING the stale L165+ renumber corrected to L185+"; exit 1; }
grep -q "## L185" ../../../docs/OPEN_LEADS.md && echo "  OK L185 umbrella registered" || { echo "  MISSING L185 umbrella registered"; exit 1; }
grep -q "FROZEN-RECORD-CLOSED" ../../../docs/progress/REVIEWS.md && echo "  OK qor5up released (registry entry landed; R47-3/R48-5 discharged)" || { echo "  MISSING qor5up released (registry entry landed; R47-3/R48-5 discharged)"; exit 1; }
echo "REPRODUCES"
