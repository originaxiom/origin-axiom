#!/usr/bin/env python3
"""B1470 -- L222 (iii) / L245 (xB031): B1418's own instrument (c2_run.run) on t12835 with the 1 800 s budget lifted, run on main
to completion: every one of the 6 435 modules, none NOT RUN.  Compared module by module with B1418's banked rows and the
sep16 lane's xB031 table in compare.py.  Same instrument as B1418: this verifies completeness and the lane's numbers, not an
independent route.  Takes about seventy minutes."""
import sys, json, time, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(next(HERE.parents[1].glob("B1418_*")) / "verification"))
import c2_run as C
from c2_reducible_index import NF
K = NF([1, 0, -1, 0, 1]); z = K.alpha(); S = [K.pw(z, k) for k in range(12)]
t0 = time.time()
out = C.run('t12835', K, S, [1, 2, 3], 10**7, 'main rerun, budget lifted (B1470)')
dt = time.time() - t0
notrun = [r for r in out if str(r.get('status', '')).startswith('NOT RUN')]
Ivals = collections.Counter(str(r.get('I')) for r in out if 'I' in r)
res = dict(modules=len(out), not_run=len(notrun), seconds=round(dt), I_values=dict(Ivals),
           by_m={m: dict(collections.Counter(str(r.get('I')) for r in out if r.get('m') == m and 'I' in r)) for m in (1, 2, 3)})
json.dump(dict(summary=res, rows=out), open(HERE / "t12835_complete.json", "w"), indent=1, default=str)
print(json.dumps(res, indent=1))
