#!/usr/bin/env python3
"""Two facts about a deck orbit of backgrounds, by slopes: (1) every slope of every character of a background is
constant along the orbit (no computed invariant tells the members apart); (2) whether the product of the orbit's
Higgs characters is trivial, per coupling type (a cubic, or m-fold, term joining the orbit's Higgs classes is then
allowed by the characters and is deck-invariant)."""
import sys, json, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
import orbit_tensor as ot
sc, ac, SECT = ot.sc, ot.ac, ot.SECT

def check(eps, word, k):
    r, bgs, cls = sc.slope_census(eps, word, k); N = r["N"]; phi = ac.monodromy(eps, word)
    ex = lambda w: (sum((q == 1) - (q == -1) for q in w), sum((q == 2) - (q == -2) for q in w))
    dx, dy = ex(phi[ac.X]), ex(phi[ac.Y]); tch = lambda c: ((dx[0] * c[0] + dx[1] * c[1]) % N, (dy[0] * c[0] + dy[1] * c[1]) % N)
    add = lambda x, y: ((x[0] + y[0]) % N, (x[1] + y[1]) % N); neg = lambda x: ((-x[0]) % N, (-x[1]) % N)
    seen = set(); tab = collections.Counter(); const = collections.Counter(); fixed = sum(1 for c in cls if tch(c) == c)
    for key in sorted(bgs):
        if key in seen: continue
        orb = [key]; kk = tuple(tch(c) for c in key)
        while kk != key: orb.append(kk); kk = tuple(tch(c) for c in kk)
        seen.update(orb)
        const["constant" if len({tuple(cls[c] for c in o if c != (0, 0)) for o in orb}) == 1 else "NOT constant"] += 1
        for name, (A, B) in (("up", ("Q", "uc")), ("down", ("Q", "dc")), ("neutrino", ("L", "nuc"))):
            if name == "neutrino" and bgs[key][5] != bgs[key][0]: continue
            s = (0, 0)
            for o in orb:
                al = dict(zip(SECT, o[1:])); e = add(add(al[A], al[B]), neg(o[0])); e = neg(e) if bgs[o][0] > 0 else e; s = add(s, e)
            tab["size %d, %s: product %s" % (len(orb), name, "trivial" if s == (0, 0) else "not trivial")] += 1
    return dict(state=r["state"], k=k, orbits=sum(const.values()), slopes_along_orbit=dict(const), deck_fixed_nontrivial_characters=fixed, higgs_product=dict(sorted(tab.items())))

if __name__ == "__main__":
    out = [check(1 if st[0] == "+" else -1, st[1:], k) for st, k in (("+LR", 3), ("-LLLR", 3), ("+LLR", 3), ("-LR", 3), ("+LLLR", 3), ("+LR", 4), ("+LR", 5), ("+LR", 6), ("+LR", 7))]
    for o in out: print(json.dumps(o))
    json.dump(out, open(HERE / "higgs_product.json", "w"), indent=1)
