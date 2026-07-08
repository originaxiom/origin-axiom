#!/usr/bin/env python3
"""B476 wave 2 — are the 16 locks pair-data or level-forced? Span deficits for the
off-critical pairs at their levels."""
import numpy as np, sys
np.seterr(all="ignore")

def weil(N, m):
    z = np.exp(2j*np.pi/N)
    D = np.diag([z**((j*(j-1)//2) % N) for j in range(N)])
    F = np.array([[z**((i*j) % N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    WR = (F @ D @ F.conj().T).conj().T
    return np.linalg.matrix_power(WR, m) @ np.linalg.matrix_power(D, m)

def order(M, cap=400):
    P = np.eye(len(M), dtype=complex)
    for k in range(1, cap+1):
        P = P @ M
        if np.max(np.abs(P - np.eye(len(M)))) < 1e-8: return k
    return None

def span_deficit(N, m1, m2):
    W1, W2 = weil(N, m1), weil(N, m2)
    o1, o2 = order(W1), order(W2)
    if o1 is None or o2 is None: return None
    mats = []
    P1 = np.eye(N, dtype=complex)
    for j in range(o1):
        P2 = np.eye(N, dtype=complex)
        for l in range(o2):
            mats.append((P1 @ P2).flatten())
            P2 = P2 @ W2
        P1 = P1 @ W1
    A = np.array(mats)
    s = np.linalg.svd(A, compute_uv=False)
    dim = int((s > 1e-8*s[0]).sum())
    return o1, o2, dim

for (m1, m2, N) in ((1,2,15), (1,3,27), (2,3,63)):
    r = span_deficit(N, m1, m2)
    if r is None:
        print(f"pair ({m1},{m2}) @ {N}: order cap exceeded", flush=True); continue
    o1, o2, dim = r
    print(f"pair ({m1},{m2}) @ level {N}: ord=({o1},{o2}), products={o1*o2}, span dim = {dim}", flush=True)
print("LOCKS CONTROLS DONE", flush=True)
