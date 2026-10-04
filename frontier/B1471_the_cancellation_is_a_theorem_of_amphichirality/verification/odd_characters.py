#!/usr/bin/env python3
"""B1471 follow-up (post-seal, for P5): on the amphichiral members complex at odd n, find the sign character eps: pi_1 -> {+-1}
with conj R_n(t) = unit * R_n^{rho (x) eps}(t) -- the lift's Z/2.  All homs to {+-1} are enumerated from the relators."""
import sys, json, itertools, warnings; warnings.filterwarnings("ignore")
import realness as R
from mpmath import mpf, conj as cj
names = sys.argv[1:] or ["m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695"]
out = {}
for nm in names:
    pk, err = R.setup(nm); gens, rels = pk["gens"], pk["rels"]
    homs = [eps for eps in itertools.product((1, -1), repeat=len(gens))
            if all(sum((1 if ch.islower() else -1) * (0 if eps[gens.index(ch.lower())] == 1 else 1) for ch in r) % 2 == 0 for r in rels)]
    res = dict(h1=pk["h1"], phi=pk["phi"], sign_homs=len(homs), matches={})
    for n in (1, 3):
        W = R.Wada(pk, n); vals = {t: W.value(mpf(t)) for t in (mpf(2), mpf(3), mpf("0.6"))}
        for eps in homs:
            if all(e == 1 for e in eps): continue
            pk2 = dict(pk); pk2["rho"] = {g: eps[i] * pk["rho"][g] for i, g in enumerate(gens)}
            W2 = R.Wada(pk2, n)
            m = [R.unit_match(cj(vals[t]), W2.value(t), t) for t in vals]
            if all(m) and len({x[0] for x in m}) == 1:
                through_phi = all(eps[i] == (-1) ** (pk["phi"][g] % 2) for i, g in enumerate(gens))
                res["matches"].setdefault(n, []).append(dict(eps=dict(zip(gens, eps)), unit=m[0], factors_through_phi=through_phi))
    out[nm] = res; print(nm, json.dumps(res, default=str))
json.dump(out, open("odd_characters.json", "w"), indent=1, default=str)
