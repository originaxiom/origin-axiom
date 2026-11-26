# s02_finite_orbits_C.py -- search for finite orbits over C (floating point, float64, tolerance 1e-9).
# Reasoning used (stated in report): on a fibre x = c the move L is linear in (y,z) with matrix [[0,1],[-1,c]];
# a point with finite orbit has, for each coordinate, either the other two coordinates zero ("two-zero" points),
# or that coordinate equal to 2cos(pi*r), r rational. So outside the two-zero points every coordinate of every
# orbit point is of the form 2cos(pi a/b). We enumerate triples with such coordinates (b <= B), filter, and BFS.
import numpy as np, itertools, math, sys
from collections import defaultdict
B = int(sys.argv[1]) if len(sys.argv) > 1 else 24
CAP = 6000
vals = sorted(set(round(2*math.cos(math.pi*a/b), 12) for b in range(1, B+1) for a in range(0, b+1)))
S = np.array(vals)
print("B =", B, " number of values 2cos(pi a/b), b<=B:", len(S))
Sset = S

def inS(v, tol=1e-9):
    i = np.searchsorted(Sset, v)
    i0 = np.clip(i-1, 0, len(Sset)-1); i1 = np.clip(i, 0, len(Sset)-1)
    return (np.abs(Sset[i0]-v) < tol) | (np.abs(Sset[i1]-v) < tol)

X, Y = np.meshgrid(S, S, indexing='ij'); X = X.ravel(); Y = Y.ravel()
cands = []
for zv in S:
    Z = np.full_like(X, zv)
    m = inS(X*Z - Y) & inS(Y*Z - X) & inS(X*Y - Z)
    for a, b in zip(X[m], Y[m]):
        cands.append((a, b, zv))
print("candidate triples passing the one-step filter:", len(cands))

def key(p): return tuple(int(round(c*1e8)) for c in p)
def moves(p):
    x, y, z = p
    return [(x, z, x*z-y), (z, y, y*z-x), (x, x*y-z, y), (x*y-z, y, x)]

seen = {}
orbits = []
for c in cands:
    kc = key(c)
    if kc in seen: continue
    orb = {kc: c}; stack = [c]; ok = True
    while stack and ok:
        p = stack.pop()
        for q in moves(p):
            if max(abs(t) for t in q) > 2 + 1e-7:
                # escapes [-2,2]: allowed only for two-zero points; those are not in our candidate list unless coordinate in S
                ok = False; break
            kq = key(q)
            if kq not in orb:
                orb[kq] = q; stack.append(q)
                if len(orb) > CAP: ok = False; break
    for kk in orb: seen[kk] = True
    if ok:
        pts = list(orb.values())
        kval = pts[0][0]**2 + pts[0][1]**2 + pts[0][2]**2 - pts[0][0]*pts[0][1]*pts[0][2]
        orbits.append((round(kval, 8), len(pts), pts))

byk = defaultdict(list)
for kv, n, pts in orbits: byk[kv].append((n, pts))
print("finite orbits found (coords in [-2,2], b<=%d): %d" % (B, len(orbits)))
for kv in sorted(byk):
    sizes = sorted(n for n, _ in byk[kv])
    if abs(kv-4) < 1e-6:
        print("  k=4 (Cayley leaf): %d orbits, sizes histogram:" % len(sizes), dict(sorted(((s, sizes.count(s)) for s in set(sizes)))))
    else:
        # describe each orbit by its set of absolute coordinate values
        descs = []
        for n, pts in sorted(byk[kv], key=lambda t: t[0]):
            av = sorted(set(round(abs(c), 6) for p in pts for c in p))
            twozero = all(sum(1 for c in p if abs(c) < 1e-9) >= 2 for p in pts)
            descs.append((n, av, "two-zero" if twozero else ""))
        print("  k=%.8f : %d orbits:" % (kv, len(sizes)))
        for d in descs: print("       size %d  |coords| in %s %s" % d)
