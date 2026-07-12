#!/usr/bin/env python3
"""B534 step 0: pin the seam conventions (float).

Reproduce the banked Master Theorem fingerprint at level 15
(70 dark / 170 active on Z/20 x Z/12, magnitudes {0,1,sqrt3,sqrt5,sqrt15}),
then scan prime levels for the dark set under the same conventions.
"""
import numpy as np
from itertools import product

def weil_pair(N):
    z = np.exp(2j*np.pi/N)
    D = np.diag([z**((j*(j-1)//2) % N) for j in range(N)])
    F = np.array([[z**((i*j) % N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    WR = (F @ D @ F.conj().T).conj().T
    W1 = WR @ D
    W2 = np.linalg.matrix_power(WR, 2) @ np.linalg.matrix_power(D, 2)
    return W1, W2

def par(N):
    P = np.zeros((N, N))
    for n in range(N):
        P[n, (-n) % N] = 1
    return P

def order_of(M, cap=200):
    A = M.copy()
    for k in range(1, cap+1):
        if np.allclose(A, np.eye(len(M)), atol=1e-9):
            return k
        A = A @ M
    return None

# --- level 15 fingerprint ---
N = 15
W1, W2 = weil_pair(N)
P = par(N)
o1, o2 = order_of(W1), order_of(W2)
print(f"level 15: order(W1)={o1}, order(W2)={o2}")

dark = active = 0
mags = set()
for j, l in product(range(o1), range(o2)):
    t = np.trace(P @ np.linalg.matrix_power(W1, j) @ np.linalg.matrix_power(W2, l))
    m = abs(t)
    if m < 1e-8:
        dark += 1
    else:
        active += 1
        mags.add(round(m, 5))
print(f"level 15: dark={dark}, active={active} (banked: 70/170)")
print(f"magnitudes: {sorted(mags)}")
print(f"expected: 1, {np.sqrt(3):.5f}, {np.sqrt(5):.5f}, {np.sqrt(15):.5f}")

# --- prime levels: find the dark set ---
for p in (5, 7, 11, 13):
    W1, W2 = weil_pair(p)
    P = par(p)
    o1, o2 = order_of(W1), order_of(W2)
    darkset = []
    for j, l in product(range(o1), range(o2)):
        t = np.trace(P @ np.linalg.matrix_power(W1, j) @ np.linalg.matrix_power(W2, l))
        if abs(t) < 1e-8:
            darkset.append((j, l))
    print(f"\np={p}: orders=({o1},{o2}), #dark={len(darkset)} (claim: p-2={p-2})")
    print(f"  dark set: {darkset[:20]}")
    hyper = [(j, l) for j, l in darkset if (j*l) % p == (-4) % p]
    print(f"  on hyperbola jl=-4 mod p: {len(hyper)}/{len(darkset)}")
