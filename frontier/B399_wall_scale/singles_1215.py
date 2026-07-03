"""B399 A1 -- m=1 singles at level 1215 (numpy F_p, 2 primes, detached)."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B391_existence_general"))
from census_big import primes_1_mod, primitive_root

N, o1 = 1215, 1620
res = {}
for p in primes_1_mod(4*N, 2, start=3*10**7):
    assert (p-1) % N == 0 and (p-1) % o1 == 0
    g = primitive_root(p)
    zN = pow(g, (p-1)//N, p)
    j = np.arange(N, dtype=np.int64)
    zrow = np.array([pow(zN, int(k), p) for k in range(N)], dtype=np.int64)
    Dd = zrow[(j*(j-1)//2) % N]
    F = np.empty((N, N), dtype=np.int64)
    for i in range(N): F[i] = zrow[(i*j) % N]
    iN = pow(N, p-2, p)
    Fi = np.empty((N, N), dtype=np.int64)
    for i in range(N): Fi[i] = zrow[(-i*j) % N] * iN % p
    Din = np.array([pow(int(x), p-2, p) for x in Dd], dtype=np.int64)
    def mm(A, B):
        C = np.zeros((A.shape[0], B.shape[1]), dtype=np.int64)
        step = max(1, (2**62) // (p*p))
        for s in range(0, A.shape[1], step):
            C = (C + A[:, s:s+step] @ B[s:s+step, :]) % p
        return C
    WR = mm(F * Din[None, :] % p, Fi)
    W1 = WR * Dd[None, :] % p
    ridx = (-j) % N
    trs = []
    P = np.eye(N, dtype=np.int64)
    for k in range(o1):
        trs.append(int(P[ridx, j].sum() % p))
        P = mm(P, W1)
        if (k+1) % 200 == 0: print(f"  p={p}: {k+1}/{o1} powers", flush=True)
    zo = pow(g, (p-1)//o1, p)
    inv = pow(o1, p-2, p)
    cells = {}
    for a in range(o1):
        t = 0
        for k in range(o1):
            t = (t + pow(zo, (-k*a) % o1, p) * trs[k]) % p
        t = t * inv % p
        if t: cells[a] = t
    res[str(p)] = cells
    print(p, "nonzero singles:", len(cells), "cells:", sorted(map(int, cells))[:14], flush=True)
json.dump(res, open(os.path.join(HERE, "singles_1215.json"), "w"), indent=1)
print("ALLDONE", flush=True)
