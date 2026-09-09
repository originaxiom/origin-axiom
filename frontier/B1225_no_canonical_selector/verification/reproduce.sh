#!/usr/bin/env bash
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
echo "B1225 is a structural argument; its inputs are banked arcs. Checking they say what is claimed:"
python3 - <<'PY'
import json, glob, sys
need = {
 "B1203": ["11720", "c-equivariance", "0 of 11720"],
 "B1191": ["GC-15"],
}
ok = True
for arc, frags in need.items():
    f = glob.glob(f"frontier/{arc}_*/arc_verdict.json")
    if not f:
        print(f"  {arc}: MISSING"); ok = False; continue
    c = " ".join(json.load(open(f[0]))["claim_one_line"].split())
    for fr in frags:
        hit = fr.lower() in c.lower()
        print(f"  {arc}: {'ok  ' if hit else 'MISS'} {fr!r}")
        ok &= hit
sys.exit(0 if ok else 1)
PY
echo
echo "REPRODUCES"
