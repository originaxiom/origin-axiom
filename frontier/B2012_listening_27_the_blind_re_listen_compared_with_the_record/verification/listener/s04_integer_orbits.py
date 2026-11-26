# s04_integer_orbits.py -- orbits of <L,R> on integer points of the leaf k, computed inside a box |coords|<=H.
# Union-find over moves that stay inside the box. An orbit is counted if it has a point with max|coord| <= H0.
# Stability of the count from H to 2H is checked (reported as 'stable').
import numpy as np, sys
from collections import defaultdict

def points(k, H):
    r = np.arange(-H, H+1, dtype=np.int64)
    X, Y = np.meshgrid(r, r, indexing='ij'); X = X.ravel(); Y = Y.ravel()
    D = X*X*Y*Y - 4*(X*X + Y*Y - k)
    m = D >= 0
    X, Y, D = X[m], Y[m], D[m]
    s = np.floor(np.sqrt(D.astype(np.float64))).astype(np.int64)
    for _ in range(2):
        s = np.where(s*s > D, s-1, s); s = np.where((s+1)*(s+1) <= D, s+1, s)
    m = s*s == D
    X, Y, s = X[m], Y[m], s[m]
    out = set()
    for sg in (1, -1):
        num = X*Y + sg*s
        mm = (num % 2 == 0)
        Z = num[mm]//2
        mm2 = np.abs(Z) <= H
        for a, b, c in zip(X[mm][mm2], Y[mm][mm2], Z[mm2]):
            out.add((int(a), int(b), int(c)))
    return out

def components(k, H):
    pts = points(k, H)
    parent = {p: p for p in pts}
    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]; p = parent[p]
        return p
    closed = {p: True for p in pts}
    for p in pts:
        x, y, z = p
        for q in ((x, z, x*z-y), (z, y, y*z-x)):
            if q in parent:
                a, b = find(p), find(q)
                if a != b: parent[a] = b
            else:
                closed[p] = False
        for q in ((x, x*y-z, y), (x*y-z, y, x)):
            if q not in parent: closed[p] = False
    comps = defaultdict(list)
    for p in pts: comps[find(p)].append(p)
    return list(comps.values()), closed

def summarize(k, H, H0):
    comps, closed = components(k, H)
    core = [c for c in comps if min(max(abs(t) for t in p) for p in c) <= H0]
    fin = [c for c in core if all(closed[p] for p in c)]
    return core, fin

if __name__ == "__main__":
    kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
    H0 = int(sys.argv[3]) if len(sys.argv) > 3 else 40
    for k in range(kmin, kmax+1):
        c1, f1 = summarize(k, 4*H0, H0)
        c2, f2 = summarize(k, 8*H0, H0)
        stable = (len(c1) == len(c2))
        c = c2
        # mirror tau(x,y,z)=(y,x,z) and sign changes: which orbits do they fix?
        idx = {}
        for i, comp in enumerate(c):
            for p in comp: idx[p] = i
        def img(f):
            res = []
            for comp in c:
                p = min(comp, key=lambda q: max(map(abs, q)))
                res.append(idx.get(f(p), None))
            return res
        tau = img(lambda p: (p[1], p[0], p[2]))
        s12 = img(lambda p: (-p[0], -p[1], p[2]))
        ntau_fixed = sum(1 for i, j in enumerate(tau) if i == j)
        sizes_fin = sorted(len(cc) for cc in c if all(q in idx for q in cc) and len(cc) < 50)
        print("k=%4d  orbits(with a point of height<=%d)=%3d  stable(H=%d vs %d)=%s  finite-looking=%s  tau-fixed orbits=%d"
              % (k, H0, len(c), 4*H0, 8*H0, stable, sorted(len(f) for f in f2), ntau_fixed))
        sys.stdout.flush()
