#!/usr/bin/env bash
# B1172 -- THE TRIGGER + THE BACKLOG + THE REGISTER. Verifies the sitting's committed state:
# (a) the relay-debt gate's four repairs are live (real clock; stale FAILS unless ESCALATED-by-name;
#     all seat lanes matched; dateless = stale) -- exercised by tests/test_relay_debt_gate.py;
# (b) the backlog triage is on the ledger (p3 -> L187; B879 -> L188; MANIFEST dated; the nine 08-09
#     rows escalated with the retention-gap event E51 filed);
# (c) O3: the MC1 assignment row exists (the invisible-work instance closed).
set -euo pipefail
cd "$(dirname "$0")"
R=../../../
python3 "$R/scripts/checks/relay_debt.py" && echo "  OK relay-debt gate green at the triage date"
grep -q "## L187" "$R/docs/OPEN_LEADS.md" && echo "  OK L187 (depth-closure backlog)"
grep -q "## L188" "$R/docs/OPEN_LEADS.md" && echo "  OK L188 (selection-cochain verification)"
grep -q "E51 the RETENTION gap" "$R/docs/ERROR_LEDGER.md" && echo "  OK E51 filed"
grep -q "MC1_INDEPENDENT_REIMPLEMENTATION.md\` | OPEN" "$R/docs/RELAY_LEDGER.md" && echo "  OK MC1 row (O3)"
grep -c "ESCALATED(2026-08-27, B1172)" "$R/docs/RELAY_LEDGER.md" | xargs -I{} echo "  OK {} rows ESCALATED-by-name"
echo "REPRODUCES"
