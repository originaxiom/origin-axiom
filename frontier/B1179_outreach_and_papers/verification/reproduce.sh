#!/usr/bin/env bash
# B1179 -- R50-7's two GO-able halves executed: the papers relay SENT (internal, cc3's assembly) and
# the specialist send-queue BUILT + PRESENTED (external sending stays owner-gated per item).
set -euo pipefail
cd "$(dirname "$0")"; R=../../..
grep -q "OWNER DECISION BOX" "$R/docs/SPECIALIST_SEND_QUEUE.md" && echo "  OK the send-queue (6 bars, decision box)" || { echo "  MISSING the send-queue (6 bars, decision box)"; exit 1; }
grep -q "STALENESS PASS (2026-08-27, B1179" "$R/frontier/EXPERT_OUTREACH.md" && echo "  OK the June brief staleness-passed" || { echo "  MISSING the June brief staleness-passed"; exit 1; }
grep -q "PAPERS_RELAY" "$R/docs/RELAY_LEDGER.md" && echo "  OK the papers relay rowed" || { echo "  MISSING the papers relay rowed"; exit 1; }
echo "REPRODUCES"
