# modn.py -- orbits of <L,R> on (Z/n)^3, leaf by leaf (exact integer arithmetic, numpy int64)
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from collections import Counter

def maps(n):
    N = n**3
    i = np.arange(N, dtype=np.int64)
    x, y, z = i // (n*n), (i // n) % n, i % n
    Li = (x*n + z)*n + (x*z - y) % n
    Ri = (z*n + y)*n + (y*z - x) % n
    k = (x*x + y*y + z*z - x*y*z) % n
    return x, y, z, Li, Ri, k

def orbits(n):
    x, y, z, Li, Ri, k = maps(n)
    N = n**3
    rows = np.concatenate([np.arange(N), np.arange(N)]); cols = np.concatenate([Li, Ri])
    G = coo_matrix((np.ones(2*N, dtype=np.int8), (rows, cols)), shape=(N, N))
    nc, lab = connected_components(G, directed=True, connection='weak')
    return x, y, z, Li, Ri, k, nc, lab

def leaf_summary(n):
    x, y, z, Li, Ri, k, nc, lab = orbits(n)
    sizes = np.bincount(lab)
    out = {}
    for kv in range(n):
        labs = np.unique(lab[k == kv])
        out[kv] = sorted((int(sizes[l]) for l in labs), reverse=True)
    return out, (x, y, z, Li, Ri, k, lab, sizes)

def fmt(sz):
    c = Counter(sz)
    return " ".join(("%d" % s) if m == 1 else ("%dx%d" % (s, m)) for s, m in sorted(c.items(), reverse=True))
