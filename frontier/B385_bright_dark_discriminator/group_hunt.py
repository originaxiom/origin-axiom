"""B385 T1 -- the group-invariant hunt over the 12 banked pairs (exact, mod 15)."""
import json, os
from itertools import product

BRIGHT = [(1,2),(2,3),(2,4),(3,4),(1,7),(3,7),(2,7)]
DARK   = [(1,3),(1,4),(3,5),(1,5),(4,5)]

def A(m, n): return ((1+m*m) % n, m % n, m % n, 1 % n)
def mul(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n, (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n, (a[2]*b[1]+a[3]*b[3]) % n)
def gen_group(gens, n):
    I = (1 % n, 0, 0, 1 % n)
    G = {I}
    frontier = [I]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                x = mul(g, h, n)
                if x not in G:
                    G.add(x); nxt.append(x)
        frontier = nxt
    return G

from math import gcd
def invariants(m1, m2):
    out = {}
    for n, tag in ((15, "15"), (3, "3"), (5, "5")):
        G = gen_group([A(m1, n), A(m2, n)], n)
        negI = ((n-1) % n, 0, 0, (n-1) % n)
        # det(-g - I) class multiset
        classes = {}
        for g in G:
            d = ((-g[0]-1)*(-g[3]-1) - g[1]*g[2]) % n
            c = gcd(d, n)
            classes[c] = classes.get(c, 0) + 1
        out[tag] = dict(order=len(G), has_negI=negI in G,
                        det_classes={str(k): v for k, v in sorted(classes.items())})
        # QR data mod 5: the set of traces, and whether all traces are QRs+{0,..}
        if n == 5:
            trs = sorted({(g[0]+g[3]) % 5 for g in G})
            out[tag]["traces"] = trs
    return out

table = {}
for (m1, m2) in BRIGHT + DARK:
    table[f"{m1},{m2}"] = dict(status=("bright" if (m1,m2) in BRIGHT else "dark"),
                               **invariants(m1, m2))

# print compact comparison
print(f"{'pair':7s} {'stat':7s} {'|G15|':6s} {'|G3|':5s} {'|G5|':5s} {'-I@3':5s} {'-I@5':5s} {'tr@5'}")
for k, v in table.items():
    print(f"{k:7s} {v['status']:7s} {v['15']['order']:<6d} {v['3']['order']:<5d} {v['5']['order']:<5d} "
          f"{str(v['3']['has_negI']):5s} {str(v['5']['has_negI']):5s} {v['5']['traces']}")

# automated separator scan over scalar invariants
def scan():
    feats = {}
    for k, v in table.items():
        feats[k] = dict(o15=v['15']['order'], o3=v['3']['order'], o5=v['5']['order'],
                        n3=v['3']['has_negI'], n5=v['5']['has_negI'],
                        n15=v['15']['has_negI'],
                        tr5=tuple(v['5']['traces']),
                        dc15=tuple(sorted(v['15']['det_classes'].items())),
                        dc5=tuple(sorted(v['5']['det_classes'].items())),
                        dc3=tuple(sorted(v['3']['det_classes'].items())))
    hits = []
    names = list(next(iter(feats.values())))
    for f in names:
        bvals = {str(feats[f"{a},{b}"][f]) for a, b in BRIGHT}
        dvals = {str(feats[f"{a},{b}"][f]) for a, b in DARK}
        if not (bvals & dvals):
            hits.append((f, sorted(bvals), sorted(dvals)))
    return hits

hits = scan()
print("\nSEPARATING invariants (bright-values vs dark-values disjoint):")
for f, bv, dv in hits: print(f"  {f}: bright={bv}  dark={dv}")
if not hits: print("  NONE — the registered kill fires")
json.dump(dict(table=table, separators=[h[0] for h in hits]),
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "group_hunt.json"), "w"),
          indent=1)
print("DONE")
