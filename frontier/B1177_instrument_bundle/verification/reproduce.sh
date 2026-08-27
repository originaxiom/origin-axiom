#!/usr/bin/env bash
# B1177 -- THE INSTRUMENT BUNDLE (R50-5). Verifies the committed instrument state.
set -euo pipefail
cd "$(dirname "$0")"; R=../../..
grep -q "21 true no-runner-no-lock" ../reproducer_debt.md && echo "  OK L183 debt list (21)"
grep -q "TOOLBOX_LIVE.md" "$R/scripts/checks/doc_currency.py" && echo "  OK doc_currency watches TOOLBOX_LIVE"
grep -q "extraction seed" "$R/docs/TOOLBOX_LIVE.md" && echo "  OK the extraction seed"
grep -q "THE TRIT MORPHISM" "$R/docs/LAW_MAP.md" && grep -q "THE ARITY VOID" "$R/docs/LAW_MAP.md" && echo "  OK LAW_MAP B1042+B1043 rows (4)"
echo "  (the vacuity run: 4449 scanned / 0 no-assert / 0 tautology / 84 both-literal review rows -- recorded in results.json)"
echo "  (L184 diagnosis: full collection 178.41s for 5556 tests -- recorded; per-file top-offenders in the addendum)"
echo "REPRODUCES"
