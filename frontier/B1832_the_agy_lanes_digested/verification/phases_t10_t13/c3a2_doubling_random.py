"""agy digest, DBL on random points (two seeds; WORKING_RULES' exploratory-numerics rule): the LL pair's channel norms at
line w against each charged sector's at line 2w, main's cA.  Lines with denominators <= 12, tau in the census strip.
Data-free."""
import json, pathlib
from fractions import Fraction as F
import numpy as np
from frame_common import B, norms

OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v, flush=True)
for seed in (7301, 20261104):
    rng = np.random.default_rng(seed); worst = 0.0; worst_ll_vs_w = []; rows = []
    for _ in range(6):
        q = int(rng.integers(3, 13)); p1 = F(int(rng.integers(1, q)), q); p2 = F(int(rng.integers(0, q)), q)
        tau = complex(round(float(rng.uniform(0.0, 0.5)), 3), round(float(rng.uniform(1.6, 3.6)), 3))
        line = (float(p1), float(p2)); two = (2 * line[0], 2 * line[1])
        ll = norms(line, tau, "LL")[1]
        devs = {}
        for sec in ("up", "down", "lepton"):
            c2 = norms(two, tau, sec)[1]
            devs[sec] = max(abs(ll[k] - c2[k]) for k in ("i", "j", "k") if ll[k] is not None and c2[k] is not None)
        c1 = norms(line, tau, "down")[1]
        same_line = max(abs(ll[k] - c1[k]) for k in ("i", "j", "k") if ll[k] is not None and c1[k] is not None)
        worst = max(worst, max(devs.values()))
        rows.append({"line": (str(p1), str(p2)), "tau": str(tau), "max|LL(w) - sector(2w)| by sector": devs,
                     "LL(w) defined": "".join(k if ll[k] is not None else "-" for k in B.UNITS),
                     "max|LL(w) - down(w)| (control: same line)": same_line})
    rec("seed %d rows" % seed, rows); rec("seed %d worst |LL(w) - charged(2w)| over i,j,k" % seed, worst)
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
