#!/usr/bin/env bash
# B1241 -- reproduce the two fc recomputations harvested here and pin the register state this arc creates.
#   r51_all_regular_subfamily.py   fc R51 residuals on B1235's chirality_112.json: all-regular subfamily |A|=77,
#                                  34 amphichiral / 43 chiral; metallic bundles b++R^mL^m (m=1..6) all amphicheiral,
#                                  symmetry order 8, CS=0                                     (~90 s, snappy)
#   r52_anomaly_cubic.py           fc R52: the one-generation anomaly cubic on the anomaly-free plane factors as
#                                  -2 yL (2yL+3yd)(4yL-3yd)/3; three anomaly-free lines            (~1 s, sympy)
#   register pins                  I-13..I-17 present in docs/IDENTIFICATION_LEDGER.md with the statuses banked here;
#                                  the baseline's UNEARNED count equals the live count (the ratchet is by-hand raised)
set -e
cd "$(dirname "$0")"
ROOT="$(cd ../../.. && pwd)"
ok=1
echo "===== r51_all_regular_subfamily ====="
OA_ROOT="$ROOT" python3 r51_all_regular_subfamily.py 2>/dev/null | tail -3 | tee /dev/stderr | grep -q 'R51 residuals: REPRODUCE' || ok=0
echo "===== r52_anomaly_cubic ====="
python3 r52_anomaly_cubic.py 2>/dev/null | tail -1 | tee /dev/stderr | grep -q 'R52 anomaly cubic: REPRODUCES' || ok=0
echo "===== register pins ====="
python3 - "$ROOT" <<'PY' || ok=0
import json, re, sys
root = sys.argv[1]
led = open(f"{root}/docs/IDENTIFICATION_LEDGER.md", encoding="utf-8").read()
want = {"I-13": "UNEARNED", "I-14": "UNEARNED", "I-15": "UNEARNED", "I-16": "UNEARNED", "I-17": "REFUTED"}
status = {}
for m in re.finditer(r"^\|\s*(I-\d+)\s*\|(.*)$", led, re.M):
    cells = [c.strip().strip("*").strip() for c in m.group(2).split("|")]
    status[m.group(1)] = next((c for c in cells if c in ("EARNED", "REFUTED", "UNEARNED")), None)
bad = {k: status.get(k) for k, v in want.items() if status.get(k) != v}
live = sum(1 for v in status.values() if v == "UNEARNED")
base = json.load(open(f"{root}/docs/IDENTIFICATION_BASELINE.json"))
print(f"  rows I-13..I-17: {[status.get(k) for k in want]}; live UNEARNED {live}, baseline {base['unearned']}")
sys.exit(0 if not bad and live == base["unearned"] else 1)
PY
if [ "$ok" = 1 ]; then echo "REPRODUCES"; else echo "DIFF"; exit 1; fi
