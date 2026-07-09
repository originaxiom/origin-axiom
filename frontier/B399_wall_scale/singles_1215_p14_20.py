"""Phase 1a (cont.) -- primes 11-20 for the 1215 triple e3 reconstruction.
e1=0, e2=-1/48 exact from 10 primes; e3 (the product) has large height (leave-one-out
unstable at 10 primes) -> extend the CRT modulus. Same census as p7_10.py, TARGETS=prs[13:20]."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B391_existence_general"))
from census_big import primes_1_mod, primitive_root

N, o1 = 1215, 1620
prs = primes_1_mod(4*N, 20, start=3*10**7)
TARGETS = prs[13:20]
RES = {}
for p in TARGETS:
    print("prime:", p, flush=True)
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
        if (k+1) % 300 == 0: print(f"  {k+1}/{o1}", flush=True)
    zo = pow(g, (p-1)//o1, p)
    inv = pow(o1, p-2, p)
    cells = {}
    for a in range(o1):
        t = 0
        for k in range(o1):
            t = (t + pow(zo, (-k*a) % o1, p) * trs[k]) % p
        t = t * inv % p
        if t: cells[a] = t
    RES[str(p)] = cells
    print("nonzero:", len(cells), flush=True)
    json.dump(RES, open(os.path.join(HERE, "singles_1215_p14_20.json"), "w"), indent=1)  # incremental
print("ALLDONE", flush=True)
