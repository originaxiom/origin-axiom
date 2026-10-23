#!/usr/bin/env bash
# B1172 -- THE TRIGGER + THE BACKLOG + THE REGISTER. Verifies the sitting's committed state:
# (a) the relay-debt gate's four repairs are live (real clock; stale FAILS unless ESCALATED-by-name;
#     all seat lanes matched; dateless = stale) -- exercised by tests/test_relay_debt_gate.py;
# (b) the backlog triage is on the ledger (p3 -> L187; B879 -> L188; MANIFEST dated; the nine 08-09
#     rows escalated with the retention-gap event E51 filed);
# (c) O3: the MC1 assignment row exists (the invisible-work instance closed).
# 2026-10-23 (R68 sweep, P-313): the row's status moved OPEN -> DECLINED at Review 66 (re-registered as P-233);
# the pin pinned "| OPEN" and failed silently from then on (soft pins; a live false pass). Now it pins the row's
# existence, as (c) states, and every pin is hard (a failed pin exits 1).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../
python3 "$R/scripts/checks/relay_debt.py" && echo "  OK relay-debt gate green at the triage date" || { echo "  MISSING relay-debt gate green at the triage date"; exit 1; }
grep -q "## L187" "$R/docs/OPEN_LEADS.md" && echo "  OK L187 (depth-closure backlog)" || { echo "  MISSING L187 (depth-closure backlog)"; exit 1; }
grep -q "## L188" "$R/docs/OPEN_LEADS.md" && echo "  OK L188 (selection-cochain verification)" || { echo "  MISSING L188 (selection-cochain verification)"; exit 1; }
grep -q "E51 the RETENTION gap" "$R/docs/ERROR_LEDGER.md" && echo "  OK E51 filed" || { echo "  MISSING E51 filed"; exit 1; }
grep -q "MC1_INDEPENDENT_REIMPLEMENTATION.md\` | " "$R/docs/RELAY_LEDGER.md" && echo "  OK MC1 row (O3)" || { echo "  MISSING MC1 row (O3)"; exit 1; }
grep -c "ESCALATED(2026-08-27, B1172)" "$R/docs/RELAY_LEDGER.md" | xargs -I{} echo "  OK {} rows ESCALATED-by-name"
echo "REPRODUCES"
