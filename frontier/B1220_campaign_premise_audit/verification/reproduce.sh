#!/usr/bin/env bash
# B1220 -- the premise audit. Every claim is a citation into the banked record; this
# re-extracts the load-bearing lines so the audit can be checked without trusting prose.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT"
python3 - <<'PY'
import json, pathlib, re, sys
R = pathlib.Path(".")
def claim(a):
    p = next(R.glob(f"frontier/{a}_*/arc_verdict.json"))
    d = json.loads(p.read_text())
    return d["verdict"], " ".join(d["claim_one_line"].split())
checks = [
  ("B1196", "CLOSED-PERMANENT (the P3 floor)", "the P^3 floor is CLOSED-PERMANENT"),
  ("B1036", "NOT THE SYMMETRIC PAIRING",       "the double gains classes, not the pairing"),
  ("B1036", "symmetric support EMPTY",          "cell 3's question answered negative"),
]
ok = True
for arc, needle, what in checks:
    v, c = claim(arc)
    hit = needle.lower() in c.lower()
    ok &= hit and v == "PROVED"
    print(f"  {arc} {v:8s} [{'OK ' if hit else 'MISS'}] {what}")
# the contradiction inside B1196's own verdict line vs its cell record
v, c = claim("B1196")
cells = json.loads(next(R.glob("frontier/B1196_*/verification/batch5b_cells.json")).read_text())
head = cells["GC-27"]["headline"]
print(f"\n  B1196 verdict line says 'non-normalizable side' : {'non-normalizable side' in c}")
print(f"  GC-27 cell says 'opposite sides'                : {'opposite sides' in head}")
print(f"  GC-27 cell says lambda fails first hypothesis   : {'first hypothesis' in head}")
print(f"  GC-27 verdict                                    : {cells['GC-27']['verdict']}")
ok &= ("non-normalizable side" in c) and ("opposite sides" in head) and ("first hypothesis" in head)
sys.exit(0 if ok else 1)
PY
echo
echo "REPRODUCES"
