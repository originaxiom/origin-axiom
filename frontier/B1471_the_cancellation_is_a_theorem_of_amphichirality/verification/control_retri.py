#!/usr/bin/env python3
"""B1471 control: presentation-independence (even n must agree up to +- t^k; at odd n the SL(2,C) lift of the new
presentation may differ by a sign character, and then R changes by more than a unit -- recorded, the lift's Z/2). For each member, retriangulate until the fundamental-group presentation differs
(different relators), then compare R_n at t = 2, 3 with the original: the ratio must be +- t^k with one integer k."""
import json, warnings; warnings.filterwarnings("ignore")
import snappy, realness as R
from mpmath import mpf, log, nstr
out = {}
for nm in ("m004", "m003", "s955", "m206", "s961", "o10_150709"):
    pk0, _ = R.setup(nm); rels0 = set(pk0["rels"])
    pk1 = None
    for k in range(1, 60):
        pk, err = R.setup(nm, randomize=k)
        if err: continue
        if set(pk["rels"]) != rels0 and len(pk["gens"]) == len(pk0["gens"]) or (set(pk["rels"]) != rels0 and k > 10):
            pk1 = pk; break
    if pk1 is None: out[nm] = "no different presentation found"; print(nm, out[nm]); continue
    row = dict(rels_original=pk0["rels"], rels_new=pk1["rels"], n={})
    for n in (1, 2, 3, 4):
        W0, W1 = R.Wada(pk0, n), R.Wada(pk1, n); ks = []
        for t in (mpf(2), mpf(3)):
            a, b = W0.value(t), W1.value(t)
            if a is None or b is None: ks.append(None); continue
            q = b / a; ks.append((float(log(abs(q)) / log(t)), complex(q / abs(q))))
        ok = all(ks) and abs(ks[0][0] - ks[1][0]) < 1e-9 and abs(ks[0][0] - round(ks[0][0])) < 1e-9 and abs(ks[0][1] - ks[1][1]) < 1e-9 and abs(abs(ks[0][1].real) - 1) < 1e-9
        ks = [(round(k, 6), (round(z.real, 6), round(z.imag, 6))) for k, z in ks]
        row["n"][n] = dict(k_sign=ks, agree=bool(ok))
    out[nm] = row; print(nm, "gens", len(pk0["gens"]), "->", len(pk1["gens"]), {n: (v["agree"], v["k_sign"][0]) for n, v in row["n"].items()})
json.dump(out, open("control_retri.json", "w"), indent=1, default=str)
