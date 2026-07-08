#!/usr/bin/env python3
"""B476 wave 2b — decompose the control spans: CRT factorization at 63, parity
sectors at 27/63; count the locks per pair. Baseline (1,2)@15: 49 vs CRT 5*13=65,
16 locks."""
import numpy as np
np.seterr(all="ignore")

def weil(N, m):
    z = np.exp(2j*np.pi/N)
    D = np.diag([z**((j*(j-1)//2) % N) for j in range(N)])
    F = np.array([[z**((i*j) % N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    WR = (F @ D @ F.conj().T).conj().T
    return np.linalg.matrix_power(WR, m) @ np.linalg.matrix_power(D, m)

def order(M, cap=600):
    P = np.eye(len(M), dtype=complex)
    for k in range(1, cap+1):
        P = P @ M
        if np.max(np.abs(P - np.eye(len(M)))) < 1e-8: return k
    return None

def products(N, m1, m2):
    W1, W2 = weil(N, m1), weil(N, m2)
    o1, o2 = order(W1), order(W2)
    mats = []
    P1 = np.eye(N, dtype=complex)
    for j in range(o1):
        P2 = np.eye(N, dtype=complex)
        for l in range(o2):
            mats.append(P1 @ P2)
            P2 = P2 @ W2
        P1 = P1 @ W1
    return mats, o1, o2

def spandim(mats):
    A = np.array([M.flatten() for M in mats])
    s = np.linalg.svd(A, compute_uv=False)
    return int((s > 1e-8*s[0]).sum())

def parity(N):
    P = np.zeros((N,N))
    for j in range(N): P[(-j)%N, j] = 1
    return P

def sector_spans(N, m1, m2):
    mats, o1, o2 = products(N, m1, m2)
    total = spandim(mats)
    P = parity(N)
    evals, evecs = np.linalg.eigh(P)
    Pp = evecs[:, evals > 0]; Pm = evecs[:, evals < 0]
    out = {}
    for (nm, B) in (("even", Pp), ("odd", Pm)):
        proj = [B.conj().T @ M @ B for M in mats]
        out[nm] = (B.shape[1], spandim(proj))
    return total, o1, o2, out

for (m1, m2, N) in ((1,2,15),(1,3,27),(2,3,63),(2,3,9),(2,3,7),(1,3,3)):
    total, o1, o2, sec = sector_spans(N, m1, m2)
    blocks = sum(d*d for d,_ in sec.values())
    secstr = ", ".join(f"{nm}:{s}/{d*d}(dim {d})" for nm,(d,s) in sec.items())
    print(f"({m1},{m2})@{N}: span={total}, ord=({o1},{o2}); sectors {secstr}; parity-block bound {blocks}; deficit vs sectors = {sum(s for _,(d,s) in [(k,v) for k,v in sec.items()]) - total}", flush=True)
print("CRT test @63: factorizes iff span63 == span9 * span7", flush=True)
print("LOCKS CONTROLS 2 DONE", flush=True)
