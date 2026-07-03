"""B388 -- the m=2 transport law: test C0-C3 per the committed prereg."""
import json, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
T15 = json.load(open(os.path.join(HERE, "..", "B384_kashaev_bridge", "t2_level15_singles.json")))["m2_ord12"]
S45 = json.load(open(os.path.join(HERE, "..", "B372_level45_sweeper", "sweep45.json")))["singles2"]

def v15(a):
    r = T15.get(str(a % 12))
    return tuple(Fr(x) for x in r) if r else (Fr(0),)*4
def v45(a):
    r = S45.get(str(a % 12))
    return tuple(Fr(x) for x in r) if r else (Fr(0),)*12

def bare(a):  return v45(a)[0:4]
def c1b(a):   return v45(a)[4:8]
def c2b(a):   return v45(a)[8:12]
def spec(a):  # zeta9 -> zeta3: c1 -> -1, c2 -> -1
    b, c1, c2 = bare(a), c1b(a), c2b(a)
    return tuple(b[i] - c1[i] - c2[i] for i in range(4))

GAL = {"id":   lambda t: t,
       "s5":   lambda t: (t[0], -t[1], t[2], -t[3]),
       "t3":   lambda t: (t[0], t[1], -t[2], -t[3]),
       "s5t3": lambda t: (t[0], -t[1], -t[2], t[3])}
RULES = [("const", lambda a: 0), ("mod2", lambda a: a % 2), ("mod3", lambda a: a % 3),
         ("mod4", lambda a: a % 4)]

def try_law(get45, name):
    # C0/C1 style: get45(a) == gamma(a) . v15(sigma(a))
    hits = []
    for u in (1, 5, 7, 11):
        for v in range(12):
            for rname, rf in RULES:
                nclasses = {rf(a) for a in range(12)}
                # assign a gamma per class, must be consistent
                import itertools
                for assign in itertools.product(GAL.keys(), repeat=len(nclasses)):
                    gm = dict(zip(sorted(nclasses), assign))
                    ok = all(get45(a) == GAL[gm[rf(a)]](v15((u*a + v) % 12)) for a in range(12))
                    if ok:
                        hits.append(dict(law=name, u=u, v=v, rule=rname, gamma=gm))
    return hits

out = {}
h0 = [h for h in try_law(bare, "C0/C1-bare") if h["u"] == 1 and h["v"] == 0 and len(set(h["gamma"].values())) == 1 and "id" in h["gamma"].values()]
print("C0 (identity, bare):", bool(h0))
h1 = try_law(bare, "C1-bare")
print(f"C1 (bare relabel+char): {len(h1)} laws"); out["C1"] = h1[:6]
h3 = try_law(spec, "C3-spec")
print(f"C3 (specialization c->-1): {len(h3)} laws")
for h in h3[:8]: print("   ", h)
out["C0"] = bool(h0); out["C3"] = h3
json.dump(out, open(os.path.join(HERE, "transport_law.json"), "w"), indent=1, default=str)
print("DONE")
