#!/usr/bin/env python3
"""THE ORBIT'S COUPLING TENSOR.

For a deck orbit B_0, ..., B_{m-1} of generation-shaped backgrounds (B1432's frame), B1438 gives the cubic couplings:
  * member i couples its sectors A, B to the spin-0 character eta_i = (alpha_A beta_B)^(-sign) of ITS OWN data, with
    strength s(l_i) - s(eta_i), the same for every member (s is deck-invariant);
  * no invariant functional joins sectors of two members (their extension characters differ), and a character eta_j
    with eta_j != eta_i admits no invariant functional on member i's sectors at all.
So the tensor of a coupling type is   Y(i, j; k) = y * [i = j] * [eta_i = eta_k]   and its whole shape is the map
i -> eta_i: how many DISTINCT Higgs characters the orbit's members couple to.

This script computes that number for every deck orbit of every level of B1439's population (slopes only), for the
up (Q.u^c), down (Q.d^c) = lepton (e^c.L) and neutrino (L.nu^c) couplings, with whether the coupling is non-zero.
"""
import sys, json, pathlib, collections, time
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1438_the_slope_law" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1439_the_census_by_slope" / "verification"))
import slope_census as sc
import census_by_slope as cb
ac = sc.ac
SECT = [s[0] for s in sc.SECT]
TYPES = {"up": ("Q", "uc"), "down": ("Q", "dc"), "lepton": ("ec", "L"), "neutrino": ("L", "nuc")}

def orbits(eps, word, k):
    r, bgs, cls = sc.slope_census(eps, word, k); N = r["N"]
    phi = ac.monodromy(eps, word)
    ex = lambda w: (sum((q == 1) - (q == -1) for q in w), sum((q == 2) - (q == -2) for q in w))
    dx, dy = ex(phi[ac.X]), ex(phi[ac.Y])
    tch = lambda c: ((dx[0] * c[0] + dx[1] * c[1]) % N, (dy[0] * c[0] + dy[1] * c[1]) % N)
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); neg = lambda x: ((-x[0]) % N, (-x[1]) % N)
    def higgs(key, cnt, A, B):
        al = dict(zip(SECT, key[1:])); e = add(add(al[A], al[B]), neg(key[0])); return neg(e) if cnt[0] > 0 else e
    seen = set(); out = []
    for key in sorted(bgs):
        if key in seen: continue
        orb = [key]; kk = tuple(tch(c) for c in key)
        while kk != key: orb.append(kk); kk = tuple(tch(c) for c in kk)
        seen.update(orb); cnt = bgs[key]; rec = dict(size=len(orb), sign=cnt[0], distinct_l=len({o[0] for o in orb}))
        for name, (A, B) in TYPES.items():
            if name == "neutrino" and cnt[5] != cnt[0]: rec[name] = None; continue
            etas = [higgs(o, bgs[o], A, B) for o in orb]
            nz = [(e == (0, 0)) or (cls[e] != cls[o[0]]) for e, o in zip(etas, orb)]
            assert len(set(nz)) == 1, "the coupling's vanishing is constant along a deck orbit"
            vals = {(cls[o[0]][0] - cls[e][0]) % r["primes"][0] if e != (0, 0) else -1 for e, o in zip(etas, orb)}
            assert len(vals) == 1, "the coupling's value is constant along a deck orbit"
            rec[name] = dict(distinct_higgs=len(set(etas)), nonzero=nz[0])
        assert rec["down"] == rec["lepton"], "down and lepton couple to the same characters"
        out.append(rec)
    return r, out

if __name__ == "__main__":
    t0 = time.time(); pop = sorted(cb.population(12, 2000), key=lambda t: (t[3], t[1], t[0], t[2])); rows = []
    for (eps, w, k, t) in pop:
        if k == 1: continue                                  # an own level has no deck
        r, orbs = orbits(eps, w, k)
        if not orbs: continue
        tab = collections.Counter()
        for o in orbs:
            tab[(o["size"], o["distinct_l"], o["up"]["distinct_higgs"], o["up"]["nonzero"], o["down"]["distinct_higgs"], o["down"]["nonzero"],
                 None if o["neutrino"] is None else o["neutrino"]["distinct_higgs"])] += 1
        rows.append(dict(state=r["state"], k=k, torsion=t, backgrounds=r["generation_backgrounds"], orbits=len(orbs),
                         table=[dict(size=a, distinct_l=b, up_distinct=c, up_nonzero=d, down_distinct=e, down_nonzero=f, neutrino_distinct=g, orbits=n)
                                for (a, b, c, d, e, f, g), n in sorted(tab.items(), key=str)]))
        print(r["state"], k, "orbits", len(orbs), {"size %d: l %d, up %d%s, down %d%s" % (a, b, c, "" if d else " (zero)", e, "" if f else " (zero)"): n for (a, b, c, d, e, f, g), n in sorted(tab.items(), key=str)}, flush=True)
    json.dump(rows, open(HERE / "orbit_tensor.json", "w"), indent=1)
    tot = collections.Counter(); full = collections.Counter()
    for r in rows:
        for x in r["table"]:
            tot[x["size"]] += x["orbits"]
            if x["up_distinct"] == x["size"] and x["down_distinct"] == x["size"]: full[x["size"]] += x["orbits"]
    print("levels with orbits:", len(rows), "; orbits by size:", dict(sorted(tot.items())), "; with one Higgs character per member (up and down):", dict(sorted(full.items())), "; seconds", round(time.time() - t0, 1))
