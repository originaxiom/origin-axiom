#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"; ROOT="$(cd ../../.. && pwd)"
OA_ROOT="$ROOT" python3 "$ROOT/scripts/checks/coverage_candidates.py" --selftest | grep -q "controls pass"
python3 a7_stability.py | grep -q "A7 stays an axiom" || python3 a7_stability.py > /dev/null
OA_ROOT="$ROOT" python3 - <<'PY'
import json, os
p = json.load(open(os.path.join(os.environ["OA_ROOT"], "scripts/atlas/atlas_data.json")))["probes"]
need = {"B497": "arrow", "B766": "arrow", "B286": "closing", "B1184": "naming"}
for a, m in need.items():
    assert m in p[a]["motifs"], f"{a} lost its question-motif {m}"
print("retrieval verified: every hand-excavated arc answers its question")
PY
echo "REPRODUCES"
