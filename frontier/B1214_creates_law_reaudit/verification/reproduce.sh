#!/usr/bin/env bash
# B1214 -- the field's state after the re-audit.
set -euo pipefail
cd "$(dirname "$0")/../../.."
python3 - << 'PY'
import json
from pathlib import Path
t=f=a=0
for p in Path("frontier").glob("*/arc_verdict.json"):
    try: v=json.loads(p.read_text(encoding="utf-8"))
    except Exception: continue
    if v.get("verdict") not in ("PROVED","NEGATIVE"): continue
    if "creates_law" not in v: a+=1
    elif v["creates_law"] is True: t+=1
    else: f+=1
print(f"settled {t+f+a} | true {t} | false {f} | absent {a} ({100*a/(t+f+a):.0f}%)")
reg = Path("docs/THEOREM_REGISTRY.md").read_text(encoding="utf-8")
laws = ["B393","B557","B727","B885","B886","B910","B918","B952","B991","B996","B997","B1070","B1073"]
missing = [x for x in laws if x not in reg]
print("the thirteen, all registered:", not missing, missing or "")
assert not missing and t >= 68
print("REPRODUCES")
PY
