"""B1538 -- Part F's planned workload, aggregate only (no candidate, character or n printed): the total planned readings, by state and
by size, from Part L's candidate list and the sealed Smith-form count.  Disclosed in B1538's FINDINGS."""
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

V = Path(__file__).resolve().parent
sys.path.insert(0, str(V))
spec = importlib.util.spec_from_file_location("b1538_run_costonly", V / "run.py")
RUN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RUN)
F = RUN.F
rows = [json.loads(x) for x in (V / "run_L.jsonl").read_text().splitlines() if x.strip()]
covers = {}
tot = Counter()
by_state = Counter()
sizes = Counter()
n = 0
for r in rows:
    if not r["read"]:
        continue
    for h in r["hits"]:
        if h["n"] < 2:
            continue
        n += 1
        cid = r["cover"]
        if cid not in covers:
            w = int(cid.rsplit(".w", 1)[1])
            covers[cid] = F.Cover(F.State(r["word"]), tuple(r["lattice"]), w)
        planned = 4 * RUN.smith_fourth_roots(covers[cid], h["zeta"], h["m"])
        tot["planned"] += planned
        by_state[r["word"]] += planned
        sizes[planned] += 1
print("candidates", n, "total planned readings", tot["planned"])
print("by state (planned readings):", dict(by_state))
print("candidates by planned size:", dict(sorted(sizes.items())))
print("at 24 readings/s, one worker: %.1f days" % (tot["planned"] / 24 / 86400))

# the scopes considered for the addendum (aggregate only)
scope = Counter()
for r in rows:
    if not r["read"]:
        continue
    for h in r["hits"]:
        if h["n"] < 2:
            continue
        planned = 4 * RUN.smith_fourth_roots(covers[r["cover"]], h["zeta"], h["m"])
        golden = r["word"] in ("+LR", "-LR")
        key = "golden" if golden else ("silver, planned 0" if planned == 0 else ("silver, planned <= 512" if planned <= 512 else "silver, planned > 512"))
        scope[key + " candidates"] += 1
        scope[key + " readings"] += planned
print(dict(scope))
