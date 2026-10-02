#!/usr/bin/env python3
"""The population run: complete_points on B1445's sixteen frame levels.  usage: population.py <first> <last>"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import complete_points as cp
import mass_term as mt
out = HERE / "run"; out.mkdir(exist_ok=True)
for i in range(int(sys.argv[1]), min(int(sys.argv[2]), len(mt.FRAME))):
    name, k = mt.FRAME[i]
    try: rec = cp.run(name, k, 8, 12)
    except (AssertionError, ZeroDivisionError) as ex: rec = dict(state=name, k=k, exponent=0, backgrounds=0, points={}, sectors=[], couplings=[], failed=str(ex)[:200])
    json.dump(rec, open(out / ("complete_%02d_%s_%d.json" % (i, name, k)), "w"), indent=1)
