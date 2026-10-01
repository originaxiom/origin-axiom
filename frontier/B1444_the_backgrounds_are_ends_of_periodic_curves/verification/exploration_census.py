#!/usr/bin/env python3
"""The exploratory census that preceded the seal (disclosed in PREREGISTRATION section 3): eleven levels, the torsion of
every sector at the reducible end of the curve, classified against the slopes.  Not the sealed run."""
import sys, json, itertools, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import curve_engine as ce
from mpmath import nstr, mpf
jobs = [("+LR", 2, 4), ("-LR", 1, 4), ("-LR", 2, 4), ("-LLRLR", 1, 10), ("+LLR", 2, 4), ("+LR", 3, 12), ("-LLLR", 3, 4), ("+LRR", 3, 3), ("-LR", 3, 4), ("+LR", 4, 3), ("+LLRLRRLR", 1, 4)]
if len(sys.argv) > 1: jobs = [j for j in jobs if j[0] + str(j[1]) in sys.argv[1:]]
tot = collections.Counter(); out = []
for name, k, nl in jobs:
    eps = 1 if name[0] == "+" else -1; word = name[1:]
    Phi = ce.monodromy(eps, word, k); N = ce.exponent(Phi); chars = [c for c in ce.level_characters(Phi, N) if c != (0, 0)]
    cand = [c for c in chars if (2 * c[0]) % N or (2 * c[1]) % N]
    step = max(1, len(cand) // nl); ells = cand[::step][:nl]
    print("%s level %d: torsion %d exponent %d" % (name, k, len(chars) + 1, N), flush=True); tot["levels"] += 1
    for ell in ells:
        try: B, sl, rows = ce.analyse(eps, word, k, ell)
        except AssertionError as e:
            print("   l = %s: ASSERT %s" % (ell, str(e)[:100]), flush=True); tot["assert"] += 1; continue
        tot["backgrounds"] += 1; cls = collections.Counter()
        for r in rows:
            tot["sectors"] += 1; m = r["matches"]
            if r["order"] is None:
                tot["identically_zero"] += 1; tot["identically_zero_matches_%d" % m] += 1
                cls[("zero", m, None)] += 1; continue
            if r["order"] != 1 + m: tot["fail_order"] += 1; cls[("ORDER-FAIL", m, r["order"])] += 1; continue
            if m == 0:
                if abs(r["coeff"] - r["predicted"]) > mpf("1e-6") * max(1, abs(r["predicted"])): tot["fail_coeff"] += 1; cls[("COEFF-FAIL", nstr(r["coeff"].real, 8), nstr(r["predicted"], 8))] += 1
                else: tot["first_order_ok"] += 1
            else:
                d = (r["s_betainv"] - sl) if abs(r["s_alpha"] - sl) < mpf("1e-20") else (r["s_alpha"] - sl)
                cls[("matched", m, nstr(r["coeff"].real, 10), "d=" + nstr(d, 8))] += 1
        rec = dict(state=name, k=k, ell=ell, slope=nstr(sl, 12), sigma=B.sig, classes={str(a): b for a, b in sorted(cls.items(), key=str)})
        out.append(rec); print("   l = %s slope %s sigma %s  %s" % (ell, nstr(sl, 10), B.sig, rec["classes"]), flush=True)
print(json.dumps(dict(tot)))
json.dump(dict(totals=dict(tot), backgrounds=out), open(HERE / ("exploration_census%s.json" % ("" if len(sys.argv) == 1 else "_" + "_".join(sys.argv[1:]))), "w"), indent=1)
